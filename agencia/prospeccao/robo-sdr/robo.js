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
if (!/^sdr[1-3]$/.test(NUMERO)) { console.log('Use --numero sdr1, sdr2 ou sdr3.'); process.exit(1); }
const CENTRAL = process.env.SDR_CENTRAL || 'https://lindsonalmeida.pages.dev/api/sdr';
const TOKEN = process.env.SDR_TOKEN || (existsSync(join(PASTA, 'token.txt')) ? readFileSync(join(PASTA, 'token.txt'), 'utf8').trim() : '');
if (!TOKEN) { console.log('Falta o arquivo token.txt nesta pasta (veja o README).'); process.exit(1); }

// ---- config do número (config.json) ----
const PADRAO = { nome: NUMERO.toUpperCase(), inicio: '', teto: 40, inicial: 20, aumento: 10, hora_ini: '09:00', hora_fim: '18:00', intervalo_min: 4, intervalo_max: 9, digitando: true };
let CFG_TODO = {}; try { CFG_TODO = JSON.parse(readFileSync(join(PASTA, 'config.json'), 'utf8')); } catch (e) {}
const CFG = { ...PADRAO, ...(CFG_TODO[NUMERO] || {}) };
const hoje = () => new Date().toLocaleDateString('sv-SE');
if (!/^\d{4}-\d{2}-\d{2}$/.test(CFG.inicio)) {                 // 1º dia do número: começa o aquecimento hoje
  CFG.inicio = hoje(); CFG_TODO[NUMERO] = { ...(CFG_TODO[NUMERO] || {}), inicio: CFG.inicio };
  try { writeFileSync(join(PASTA, 'config.json.tmp'), JSON.stringify(CFG_TODO, null, 2)); renameSync(join(PASTA, 'config.json.tmp'), join(PASTA, 'config.json')); } catch (e) {}
}
// aquecimento: 20/dia na 1ª semana, +10 por semana, até o teto
export const limiteDoDia = (cfg, dia = hoje()) => { const sem = Math.max(0, Math.floor((Date.parse(dia) - Date.parse(cfg.inicio)) / (7 * 864e5))); return Math.min(cfg.teto, cfg.inicial + cfg.aumento * sem); };
const minutos = s => { const [h, m] = String(s).split(':').map(Number); return h * 60 + (m || 0); };
const podeAgora = () => { const d = new Date(), w = d.getDay(), m = d.getHours() * 60 + d.getMinutes(); return w >= 1 && w <= 5 && m >= minutos(CFG.hora_ini) && m < minutos(CFG.hora_fim); };
const MAX_SEM_WA = 3;               // 3 números sem WhatsApp seguidos = pausa (lista ruim derruba a reputação)
const CONTA = join(PASTA, `enviados-${NUMERO}.json`);
const lerConta = () => { try { const j = JSON.parse(readFileSync(CONTA, 'utf8')); return j.dia === hoje() ? j.n : 0; } catch (e) { return 0; } };
const somaConta = () => writeFileSync(CONTA, JSON.stringify({ dia: hoje(), n: lerConta() + 1 }));

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
  etapa = 'enviar mensagem'; await wa.sendMessage(id._serialized, c.msg); somaConta();
  etapa = 'avisar a Central'; await api('', { id: c.id, acao: 'enviado', canal: 'whatsapp' });
  diz(`${c.nome}: enviado ✓ (${lerConta()}/${limiteDoDia(CFG)} hoje)`);
  return 'ok';
}
wa.on('ready', async () => {
  await espera(15000);
  diz(`WhatsApp conectado. Envia de seg a sex, das ${CFG.hora_ini} às ${CFG.hora_fim}, até ${limiteDoDia(CFG)} por dia (aquecimento desde ${CFG.inicio}, teto ${CFG.teto}).`);
  let aviso = '';
  for (;;) {
    let pausado = false;
    try { pausado = !!(await api('', { acao: 'robo', estado: aviso || 'Trabalhando', enviados: lerConta(), limite: limiteDoDia(CFG), nome: CFG.nome })).pausado; } catch (e) {}
    if (pausado) { if (aviso !== 'Pausado pela Central.') { aviso = 'Pausado pela Central.'; diz(aviso); } await espera(2 * MINUTO); continue; }
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
// quem responder vai sozinho para "Respondeu" na esteira (só leads que ESTE número enviou)
wa.on('message', async m => {
  try { const n = m.from.replace(/@.*/, ''); const { contatos } = await api('');
    const c = (contatos || []).find(x => x.wa === n && x.etapa === 'enviado' && (x.sdr || 'sdr1') === NUMERO);
    if (c) { await api('', { id: c.id, acao: 'etapa', etapa: 'respondeu' }); diz(`${c.nome} RESPONDEU → esteira`); } } catch (e) {}
});
diz('Iniciando o robô…');
wa.initialize();
