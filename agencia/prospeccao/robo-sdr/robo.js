// Robô SDR (conta Leandro, 11/11/2026): pega 20 contatos da aba SDR da Central e manda a mensagem de cada um pelo WhatsApp Web, sozinho.
// Roda no computador do Lindson (fica aberto enquanto envia). Usa a rota /api/sdr com o token AUTOMACAO_TOKEN.
// ATENÇÃO: automação no WhatsApp Web vai contra as regras do WhatsApp. Use um chip separado (decisão do Lindson, 11/11/2026).
import pkg from 'whatsapp-web.js';
import qrcode from 'qrcode-terminal';
import { readFileSync, writeFileSync, existsSync } from 'fs';
const { Client, LocalAuth } = pkg;
const CENTRAL = 'https://lindsonalmeida.pages.dev/api/sdr';
const TOKEN = process.env.SDR_TOKEN || (existsSync('token.txt') ? readFileSync('token.txt', 'utf8').trim() : '');  // token.txt fica só no PC
const LOTE = Math.min(+process.env.LOTE || 20, 20);
// Limites seguros (pedido do Lindson, 11/11/2026: "limite de acordo com as políticas de envio da Meta"), número principal:
const MIN = 4, MAX = 9;             // minutos entre envios (aleatório)
const POR_DIA = 20;                 // no máximo 20 contatos novos por dia
const HORA_INI = 9, HORA_FIM = 18;  // só em horário comercial, segunda a sexta
const MAX_SEM_WA = 3;               // 3 números sem WhatsApp seguidos = para (lista ruim derruba a reputação)
const hoje = () => new Date().toLocaleDateString('sv-SE');
const CONTA = 'enviados-hoje.json';
const lerConta = () => { try { const j = JSON.parse(readFileSync(CONTA, 'utf8')); return j.dia === hoje() ? j.n : 0; } catch (e) { return 0; } };
const somaConta = () => writeFileSync(CONTA, JSON.stringify({ dia: hoje(), n: lerConta() + 1 }));
const podeAgora = () => { const d = new Date(), h = d.getHours(), w = d.getDay(); return w >= 1 && w <= 5 && h >= HORA_INI && h < HORA_FIM; };
if (!TOKEN) { console.log('Falta o arquivo token.txt nesta pasta (veja o README).'); process.exit(1); }
const api = (corpo) => fetch(CENTRAL + (corpo ? '' : '?lote=' + LOTE), {
  method: corpo ? 'POST' : 'GET',
  headers: { Authorization: 'Bearer ' + TOKEN, 'Content-Type': 'application/json' },
  body: corpo ? JSON.stringify(corpo) : undefined,
}).then(async r => { const j = await r.json(); if (!r.ok) throw new Error(j.erro || r.status); return j; });
const espera = ms => new Promise(r => setTimeout(r, ms));
const hora = () => new Date().toLocaleTimeString('pt-BR');

// usa o Chrome já instalado no PC (o navegador interno do puppeteer nem sempre baixa)
const CHROME = [process.env.CHROME, 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe', 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe',
  (process.env.LOCALAPPDATA || '') + '\\Google\\Chrome\\Application\\chrome.exe', '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'].find(c => c && existsSync(c));
const wa = new Client({ authStrategy: new LocalAuth({ clientId: 'sdr' }), 
  puppeteer: { headless: false, executablePath: CHROME, args: ['--no-sandbox', '--disable-gpu'] } });
wa.on('qr', qr => { console.log('Escaneie o QR na janela do Chrome que abriu (WhatsApp do chip → Aparelhos conectados → Conectar).'); });
wa.on('loading_screen', (p, m) => console.log(hora(), `Carregando WhatsApp ${p}%`));
wa.on('authenticated', () => console.log(hora(), 'Login feito. Esperando o WhatsApp abrir as conversas…'));
wa.on('disconnected', r => { console.log(hora(), 'WhatsApp desconectou:', r); process.exit(1); });
wa.on('auth_failure', m => { console.log('Falha no login do WhatsApp:', m); process.exit(1); });
// Modo contínuo (Lindson, 11/11/2026: "não quero fazer nada manual"): fica ligado; todo dia útil, no horário seguro,
// pega os próximos leads da aba SDR e envia até o limite do dia. Lista vazia = espera leads novos e confere de novo a cada hora.
const MINUTO = 60e3;
async function umEnvio() {
  if (!podeAgora()) return 'fora';
  if (POR_DIA - lerConta() <= 0) return 'limite';
  let lote; try { ({ lote } = await api()); } catch (e) { console.log(hora(), 'Central fora do ar:', e.message); return 'erro'; }
  const c = lote[0]; if (!c) return 'vazio';
  etapa = 'conferir o número ' + c.wa; const id = await wa.getNumberId(c.wa);
  if (!id) { semWa++; await api({ id: c.id, acao: 'etapa', etapa: 'perdido' }); console.log(hora(), `${c.nome}: sem WhatsApp → Perdido`); return semWa >= MAX_SEM_WA ? 'semwa' : 'pulou'; }
  semWa = 0;
  try { const chat = await wa.getChatById(id._serialized); await chat.sendStateTyping(); } catch (e) {}  // conversa nova pode não ter "digitando"
  await espera(Math.min(c.msg.length * 60, 12000) + Math.random() * 3000);
  etapa = 'enviar mensagem'; await wa.sendMessage(id._serialized, c.msg); somaConta();
  etapa = 'avisar a Central';
  await api({ id: c.id, acao: 'enviado', canal: 'whatsapp' });
  console.log(hora(), `${c.nome}: enviado ✓ (${lerConta()}/${POR_DIA} hoje)`);
  return 'ok';
}
let semWa = 0, etapa = '', erros = 0;
wa.on('ready', async () => {
  await espera(15000);  // deixa o WhatsApp Web terminar de carregar (99%) antes do 1º envio
  console.log(hora(), 'WhatsApp conectado. Robô ligado: envia sozinho de seg a sex, das ' + HORA_INI + 'h às ' + HORA_FIM + 'h, até ' + POR_DIA + ' por dia.');
  let aviso = '';
  for (;;) {
    // sinal de vida para a Central (aba SDR mostra ligado/desligado) e botão Pausar/Ligar de lá
    let pausado = false; try { pausado = !!(await api({ acao: 'robo', estado: aviso || 'Trabalhando', enviados: lerConta() })).pausado; } catch (e) {}
    if (pausado) { if (aviso !== 'Pausado pela Central.') { aviso = 'Pausado pela Central.'; console.log(hora(), aviso); } await espera(2 * MINUTO); continue; }
    let r; try { etapa = ''; r = await umEnvio(); erros = 0; } catch (e) {
      const msg = String((e && (e.message || e)) || e);
      if (/detached Frame|Execution context was destroyed|Target closed|Session closed|Protocol error/i.test(msg)) {
        console.log(hora(), 'A página do WhatsApp recarregou. Reiniciando o robô sozinho (volta em 1 min)...');
        try { await wa.destroy(); } catch (x) {} process.exit(2); }
      erros++; console.log(hora(), `Erro ao ${etapa || 'buscar a lista'}: ${(e && (e.message || e)) || e}`, erros >= 3 ? '→ pausa de 1 hora.' : '→ tento de novo em 3 min.'); r = 'erro'; }
    const msg = { fora: 'Fora do horário. Aguardando…', limite: 'Limite do dia atingido. Volto amanhã às ' + HORA_INI + 'h.', vazio: 'Lista do SDR vazia. Confiro de novo a cada hora.', semwa: '3 números sem WhatsApp seguidos. Pausa de 1 dia (confira a lista).' }[r];
    if (msg && msg !== aviso) { console.log(hora(), msg); aviso = msg; } else if (!msg) aviso = '';
    if (r === 'semwa') { semWa = 0; await espera(24 * 60 * MINUTO); continue; }
    if (r === 'ok' || r === 'pulou') { await espera((MIN + Math.random() * (MAX - MIN)) * MINUTO); continue; }
    await espera((r === 'erro' ? (erros >= 3 ? 60 : 3) : 10) * MINUTO);
  }
});
// quem responder vai sozinho para "Respondeu" na esteira
wa.on('message', async m => {
  try { const n = m.from.replace(/@.*/, ''); const { contatos } = await (await fetch(CENTRAL, { headers: { Authorization: 'Bearer ' + TOKEN } })).json();
    const c = (contatos || []).find(x => x.wa === n && x.etapa === 'enviado'); if (c) { await api({ id: c.id, acao: 'etapa', etapa: 'respondeu' }); console.log(hora(), `${c.nome} RESPONDEU → esteira`); } } catch (e) {}
});
console.log(hora(), 'Iniciando o robô…');
wa.initialize();
