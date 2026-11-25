// Robô SDR do WhatsApp, time de 3 números (conta Leandro 11/11/2026; time de SDR: conta Pedro 22/11/2026).
// Uso: node robo.js --numero sdr1|sdr2|sdr3   (cada número = sessão própria do WhatsApp, LocalAuth clientId "sdr-<n>")
// A Central (/api/sdr) entrega só leads deste número, já reservados (dois números nunca pegam o mesmo lead).
// ATENÇÃO: automação no WhatsApp Web vai contra as regras do WhatsApp. Use chips separados (decisão do Lindson, 11/11/2026).
import pkg from 'whatsapp-web.js';
import qrcode from 'qrcode-terminal';
import { readFileSync, writeFileSync, existsSync, renameSync } from 'fs';
import { dirname, join } from 'path';
import { fileURLToPath } from 'url';
const { Client, LocalAuth } = pkg;
const PASTA = dirname(fileURLToPath(import.meta.url));          // sempre a pasta do robô, de onde quer que seja aberto
process.chdir(PASTA);
const arg = process.argv.indexOf('--numero'), NUMERO = (arg > 0 ? process.argv[arg + 1] : process.env.SDR_NUMERO) || 'sdr1';
if (!/^sdr[1-9]$/.test(NUMERO)) { console.log('Use --numero sdr1 a sdr9.'); process.exit(1); }
const CENTRAL = process.env.SDR_CENTRAL || 'https://lindsonalmeida.pages.dev/api/sdr';
const TOKEN = process.env.SDR_TOKEN || (existsSync(join(PASTA, 'token.txt')) ? readFileSync(join(PASTA, 'token.txt'), 'utf8').trim() : '');
if (!TOKEN) { console.log('Falta o arquivo token.txt nesta pasta (veja o README).'); process.exit(1); }

// ---- config do número (config.json) ----
const PADRAO = { nome: NUMERO.toUpperCase(), inicio: '', teto: 40, inicial: 20, aumento: 10, hora_ini: '09:00', hora_fim: '18:00', intervalo_min: 4, intervalo_max: 9, digitando: true, fim_de_semana: false };
let CFG_TODO = {}; try { CFG_TODO = JSON.parse(readFileSync(join(PASTA, 'config.json'), 'utf8')); } catch (e) {}
const CFG = { ...PADRAO, ...(CFG_TODO[NUMERO] || {}) };
const hoje = () => new Date().toLocaleDateString('sv-SE');
if (!/^\d{4}-\d{2}-\d{2}$/.test(CFG.inicio)) {                 // 1º dia do número: começa o aquecimento hoje
  CFG.inicio = hoje(); CFG_TODO[NUMERO] = { ...(CFG_TODO[NUMERO] || {}), inicio: CFG.inicio };
  try { writeFileSync(join(PASTA, 'config.json.tmp'), JSON.stringify(CFG_TODO, null, 2)); renameSync(join(PASTA, 'config.json.tmp'), join(PASTA, 'config.json')); } catch (e) {}
}
// aquecimento: 20/dia na 1ª semana, +10 por semana, até o teto
// "inicio" vazio (config de 30/dia, 22/11/2026) dava NaN: o limite ia nulo e a Central mostrava /20. Agora sem início = sem aquecimento.
export const limiteDoDia = (cfg, dia = hoje()) => { const t = Date.parse(cfg.inicio || ''); const sem = isNaN(t) ? 0 : Math.max(0, Math.floor((Date.parse(dia) - t) / (7 * 864e5))); return Math.min(cfg.teto, cfg.inicial + (cfg.aumento || 0) * sem) || cfg.teto || 30; };
const minutos = s => { const [h, m] = String(s).split(':').map(Number); return h * 60 + (m || 0); };
const podeAgora = () => { const d = new Date(), w = d.getDay(), m = d.getHours() * 60 + d.getMinutes(); return (CFG.fim_de_semana || (w >= 1 && w <= 5)) && m >= minutos(CFG.hora_ini) && m < minutos(CFG.hora_fim); };
const MAX_SEM_WA = 3;               // 3 números sem WhatsApp seguidos = pausa (lista ruim derruba a reputação)
const CONTA = join(PASTA, `enviados-${NUMERO}.json`);
const lerConta = () => { try { const j = JSON.parse(readFileSync(CONTA, 'utf8')); return j.dia === hoje() ? j.n : 0; } catch (e) { return 0; } };
const somaConta = () => writeFileSync(CONTA, JSON.stringify({ dia: hoje(), n: lerConta() + 1 }));
// Follow-ups contam à parte (Lindson, 25/11/2026: "30 mensagens novas, mais o follow up"). Teto de segurança próprio.
const CONTA_FU = join(PASTA, `followups-${NUMERO}.json`), TETO_FU = 40;
const lerFU = () => { try { const j = JSON.parse(readFileSync(CONTA_FU, 'utf8')); return j.dia === hoje() ? j.n : 0; } catch (e) { return 0; } };
const somaFU = () => writeFileSync(CONTA_FU, JSON.stringify({ dia: hoje(), n: lerFU() + 1 }));

// chamadas à Central, uma de cada vez (o laço de envio e o aviso de resposta não gravam juntos)
let fila = Promise.resolve();
const chama = (q, corpo) => fetch(CENTRAL + q, { method: corpo ? 'POST' : 'GET', headers: { Authorization: 'Bearer ' + TOKEN, 'Content-Type': 'application/json' },
  body: corpo ? JSON.stringify({ numero: NUMERO, ...corpo }) : undefined, signal: AbortSignal.timeout(30e3) })
  .then(async r => { const j = await r.json(); if (!r.ok) throw new Error(j.erro || r.status); return j; });
const api = (q, corpo) => (fila = fila.catch(() => {}).then(() => chama(q, corpo)));
const espera = ms => new Promise(r => setTimeout(r, ms));
const hora = () => new Date().toLocaleTimeString('pt-BR');
const diz = (...t) => console.log(hora(), `[${CFG.nome}]`, ...t);

const CHROME = [process.env.CHROME, 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe', 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe',
  (process.env.LOCALAPPDATA || '') + '\\Google\\Chrome\\Application\\chrome.exe', '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'].find(c => c && existsSync(c));
// sessão própria por número; o sdr1 reaproveita a sessão antiga ("sdr") para não pedir QR de novo
const clientId = NUMERO === 'sdr1' && existsSync(join(PASTA, '.wwebjs_auth', 'session-sdr')) ? 'sdr' : 'sdr-' + NUMERO;
const wa = new Client({ authStrategy: new LocalAuth({ clientId, dataPath: join(PASTA, '.wwebjs_auth') }),
  puppeteer: { headless: false, executablePath: CHROME, args: ['--no-sandbox', '--disable-gpu'] } });
process.title = 'Robo ' + CFG.nome;
wa.on('qr', qr => { console.log(`\n=== ${CFG.nome}: escaneie este QR com o WhatsApp DESTE chip (Aparelhos conectados → Conectar) ===`); qrcode.generate(qr, { small: true }); });
wa.on('loading_screen', p => diz(`Carregando WhatsApp ${p}%`));
wa.on('authenticated', () => diz('Login feito. Esperando o WhatsApp abrir as conversas…'));
wa.on('disconnected', r => { diz('WhatsApp desconectou:', r); process.exit(1); });
wa.on('auth_failure', m => { diz('Falha no login do WhatsApp:', m); process.exit(1); });

const MINUTO = 60e3;
let semWa = 0, etapa = '', erros = 0;
async function umEnvio() {
  if (!podeAgora()) return 'fora';
  if (limiteDoDia(CFG) - lerConta() <= 0) return 'limite';
  let r; try { r = await api('?lote=1&numero=' + NUMERO); } catch (e) { diz('Central fora do ar:', e.message); return 'erro'; }
  if (r.pausado) return 'pausado';
  const c = r.lote && r.lote[0]; if (!c) return 'vazio';
  etapa = 'conferir o número ' + c.wa; const id = await wa.getNumberId(c.wa);
  if (!id) { semWa++; await api('', { id: c.id, acao: 'etapa', etapa: 'perdido' }); diz(`${c.nome}: sem WhatsApp → Perdido`); return semWa >= MAX_SEM_WA ? 'semwa' : 'pulou'; }
  semWa = 0;
  if (CFG.digitando) { try { const chat = await wa.getChatById(id._serialized); await chat.sendStateTyping(); } catch (e) {} }
  await espera(Math.min(c.msg.length * 60, 12000) + Math.random() * 3000);
  etapa = 'enviar mensagem'; meus.add(c.msg.trim()); await wa.sendMessage(id._serialized, c.msg); ultimoEnvio[id._serialized] = Date.now(); somaConta();
  etapa = 'avisar a Central'; await api('', { id: c.id, acao: 'enviado', canal: 'whatsapp' });
  diz(`${c.nome}: enviado ✓ (${lerConta()}/${limiteDoDia(CFG)} hoje)`);
  return 'ok';
}
// DDD do próprio chip: 11 = capta no Brasil inteiro; os outros só no Maranhão (Lindson, 22/11/2026)
const meuDDD = () => { const u = String((wa.info && wa.info.wid && wa.info.wid.user) || ''); const ddd = u.startsWith('55') ? u.slice(2, 4) : ''; return { ddd, regiao: CFG.regiao || (ddd === '11' ? 'BR' : 'MA') }; };
wa.on('ready', async () => {
  await espera(15000);
  diz(`WhatsApp conectado. Envia de seg a sex, das ${CFG.hora_ini} às ${CFG.hora_fim}, até ${limiteDoDia(CFG)} por dia (aquecimento desde ${CFG.inicio}, teto ${CFG.teto}).`);
  let aviso = '', ultFU = 0;
  for (;;) {
    let pausado = false;
    try { pausado = !!(await api('', { acao: 'robo', estado: aviso || 'Trabalhando', enviados: lerConta(), limite: limiteDoDia(CFG), nome: CFG.nome, ...meuDDD() })).pausado; } catch (e) {}
    if (pausado) { if (aviso !== 'Pausado pela Central.') { aviso = 'Pausado pela Central.'; diz(aviso); } await espera(2 * MINUTO); continue; }
    if (Date.now() - ultFU > 60 * MINUTO) { ultFU = Date.now(); try { await followUps(); } catch (e) {} }
    let r; try { etapa = ''; r = await umEnvio(); erros = 0; } catch (e) {
      const msg = String((e && (e.message || e)) || e);
      if (/detached Frame|Execution context was destroyed|Target closed|Session closed|Protocol error/i.test(msg)) {
        diz('A página do WhatsApp recarregou. Reiniciando o robô sozinho (volta em 1 min)...');
        try { await wa.destroy(); } catch (x) {} process.exit(2); }
      erros++; diz(`Erro ao ${etapa || 'buscar a lista'}: ${msg}`, erros >= 3 ? '→ pausa de 1 hora.' : '→ tento de novo em 3 min.'); r = 'erro'; }
    const msg = { fora: 'Fora do horário. Aguardando…', limite: 'Limite do dia atingido. Volto amanhã às ' + CFG.hora_ini + '.', vazio: 'Sem leads livres para este número. Confiro de novo a cada hora.', pausado: 'Pausado pela Central.', semwa: '3 números sem WhatsApp seguidos. Pausa de 1 dia (confira a lista).' }[r];
    if (msg && msg !== aviso) { diz(msg); aviso = msg; } else if (!msg) aviso = '';
    if (r === 'semwa') { semWa = 0; await espera(24 * 60 * MINUTO); continue; }
    if (r === 'ok' || r === 'pulou') { await espera((CFG.intervalo_min + Math.random() * (CFG.intervalo_max - CFG.intervalo_min)) * MINUTO); continue; }
    await espera((r === 'erro' ? (erros >= 3 ? 60 : 3) : r === 'vazio' ? 60 : 10) * MINUTO);
  }
});
// ---- CONVERSA (22/11/2026): o robô conversa com quem responde, no fluxo da Central (/api/sdr-conversa) ----
// Respostas automáticas do lead (bot/IA dele) são ignoradas; se o Lindson escrever pelo celular, o robô sai daquela conversa.
const CONVERSA = CENTRAL.replace(/\/api\/sdr$/, '/api/sdr-conversa');
const conv = (q, corpo) => (fila = fila.catch(() => {}).then(() => fetch(CONVERSA + q, { method: corpo ? 'POST' : 'GET',
  headers: { Authorization: 'Bearer ' + TOKEN, 'Content-Type': 'application/json' }, body: corpo ? JSON.stringify({ numero: NUMERO, ...corpo }) : undefined,
  signal: AbortSignal.timeout(30e3) }).then(async r => { const j = await r.json(); if (!r.ok) throw new Error(j.erro || r.status); return j; })));
const meus = new Set();                 // textos que o próprio robô mandou (para separar do Lindson digitando no celular)
const ultimoEnvio = {};                 // wa → hora do último envio do robô (resposta em < 8 s = automática)
const ocupado = new Set();              // um lead por vez (mensagens em sequência viram uma só)
const pendente = {};
async function digitaEEnvia(chatId, texto) {
  try { const chat = await wa.getChatById(chatId); await chat.sendSeen(); await espera(2000 + Math.random() * 3000); await chat.sendStateTyping(); } catch (e) {}
  await espera(Math.min(texto.length * 55, 11000) + Math.random() * 2500);
  meus.add(texto.trim()); await wa.sendMessage(chatId, texto); ultimoEnvio[chatId] = Date.now();
}
async function acharLead(n) {
  const { contatos } = await api('');
  return (contatos || []).find(x => x.wa === n && (x.sdr || 'sdr1') === NUMERO && x.etapa !== 'novo');
}
wa.on('message', async m => {
  try {
    if (m.from.endsWith('@g.us') || m.from === 'status@broadcast' || m.isStatus) return;
    const n = m.from.replace(/@.*/, '');
    const texto = m.hasMedia && !m.body ? (m.type === 'ptt' || m.type === 'audio' ? '[áudio]' : '[arquivo]') : (m.body || '');
    (pendente[m.from] = pendente[m.from] || []).push(texto);
    if (ocupado.has(m.from)) return; ocupado.add(m.from);
    await espera(20000);                // espera a pessoa terminar de escrever (junta mensagens seguidas)
    const tudo = pendente[m.from].join('\n'); delete pendente[m.from];
    const c = await acharLead(n); if (!c) { ocupado.delete(m.from); return; }
    const seg = ultimoEnvio[m.from] ? (Date.now() - ultimoEnvio[m.from] - 20000) / 1000 : 999;
    const entrada = /^\[(áudio|arquivo)\]$/.test(tudo.trim()) ? tudo + ' (o robô não ouve áudio)' : tudo;
    const r = await conv('', { acao: 'msg', id: c.id, texto: entrada, segundos: seg, nicho: c.nicho || '' });
    if (r.auto) { diz(`${c.nome}: resposta automática do lead (ignorada, espero uma pessoa)`); ocupado.delete(m.from); return; }
    if (r.etapa && r.etapa !== c.etapa) await api('', { id: c.id, acao: 'etapa', etapa: r.etapa });
    if (r.responder && r.responder.length) {
      await espera(Math.max(0, (r.atraso || 40) - 20) * 1000);
      for (const t of r.responder) await digitaEEnvia(m.from, t);
    }
    diz(`${c.nome} respondeu → ${r.motivo}${r.humano ? ' · PASSOU PARA O LINDSON' : ''}`);
  } catch (e) { diz('Erro na conversa:', String(e && e.message || e)); }
  ocupado.delete(m.from);
});
// o Lindson digitou no celular, num chat de lead: o robô para de responder esse lead
wa.on('message_create', async m => {
  try { if (!m.fromMe || meus.has((m.body || '').trim()) || m.to.endsWith('@g.us')) return;
    const c = await acharLead(m.to.replace(/@.*/, '')); if (!c) return;
    await conv('', { acao: 'lindson', id: c.id, texto: m.body || '' }); diz(`${c.nome}: o Lindson assumiu a conversa pelo celular.`);
  } catch (e) {}
});
// follow-ups (D+3, D+6 e D+9 para quem não respondeu; o D+9 oferece o Instagram organizado grátis; "depois" volta em 3 dias), no horário e dentro do limite do dia
async function followUps() {
  if (!podeAgora()) return;
  let r; try { r = await conv('?followup=1&numero=' + NUMERO); } catch (e) { return; }
  for (const f of (r.lista || [])) {
    if (lerFU() >= TETO_FU) return;
    try { const id = await wa.getNumberId(f.wa); if (!id) continue;
      await digitaEEnvia(id._serialized, f.msg); somaFU();
      const x = await conv('', { acao: 'fu', id: f.id, texto: f.msg, tipo: f.tipo });
      if (x.etapa) await api('', { id: f.id, acao: 'etapa', etapa: x.etapa });
      diz(`Follow-up (${f.tipo}) enviado (${lerFU()} follow-ups hoje, fora das ${limiteDoDia(CFG)} novas).`);
      await espera((CFG.intervalo_min + Math.random() * (CFG.intervalo_max - CFG.intervalo_min)) * MINUTO);
    } catch (e) { diz('Erro no follow-up:', String(e && e.message || e)); }
  }
}
diz('Iniciando o robô…');
wa.initialize();
