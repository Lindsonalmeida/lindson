// Robô SDR (conta Leandro, 11/11/2026): pega 20 contatos da aba SDR da Central e manda a mensagem de cada um pelo WhatsApp Web, sozinho.
// Roda no computador do Lindson (fica aberto enquanto envia). Usa a rota /api/sdr com o token AUTOMACAO_TOKEN.
// ATENÇÃO: automação no WhatsApp Web vai contra as regras do WhatsApp. Use um chip separado (decisão do Lindson, 11/11/2026).
import pkg from 'whatsapp-web.js';
import qrcode from 'qrcode-terminal';
import { readFileSync, existsSync } from 'fs';
const { Client, LocalAuth } = pkg;
const CENTRAL = 'https://lindsonalmeida.pages.dev/api/sdr';
const TOKEN = process.env.SDR_TOKEN || (existsSync('token.txt') ? readFileSync('token.txt', 'utf8').trim() : '');  // token.txt fica só no PC
const LOTE = Math.min(+process.env.LOTE || 20, 20);
const MIN = 2, MAX = 5; // minutos entre envios
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
const wa = new Client({ authStrategy: new LocalAuth({ clientId: 'sdr' }), webVersionCache: { type: 'none' },
  puppeteer: { headless: false, executablePath: CHROME, args: ['--no-sandbox', '--disable-gpu'] } });
wa.on('qr', qr => { console.log('Escaneie o QR na janela do Chrome que abriu (WhatsApp do chip → Aparelhos conectados → Conectar).'); });
wa.on('auth_failure', m => { console.log('Falha no login do WhatsApp:', m); process.exit(1); });
wa.on('ready', async () => {
  console.log(hora(), 'WhatsApp conectado. Buscando o lote…');
  let lote; try { ({ lote } = await api()); } catch (e) { console.log('Não consegui ler a Central:', e.message); process.exit(1); }
  if (!lote.length) { console.log('Lista do SDR vazia.'); process.exit(0); }
  let ok = 0, pulados = 0;
  for (const [i, c] of lote.entries()) {
    try {
      const id = await wa.getNumberId(c.wa);
      if (!id) { await api({ id: c.id, acao: 'etapa', etapa: 'perdido' }); pulados++; console.log(hora(), `${i + 1}/${lote.length} ${c.nome}: número sem WhatsApp → Perdido`); continue; }
      await wa.sendMessage(id._serialized, c.msg);
      await api({ id: c.id, acao: 'enviado', canal: 'whatsapp' }); ok++;
      console.log(hora(), `${i + 1}/${lote.length} ${c.nome}: enviado ✓`);
    } catch (e) {
      console.log(hora(), `${c.nome}: erro (${e.message}). Parando por segurança.`); break;
    }
    if (i < lote.length - 1) { const m = MIN + Math.random() * (MAX - MIN); console.log(`   próximo em ${m.toFixed(1)} min`); await espera(m * 60e3); }
  }
  console.log(hora(), `Fim do lote: ${ok} enviados, ${pulados} pulados. Rode de novo para o próximo lote.`);
  await espera(5000); await wa.destroy(); process.exit(0);
});
// quem responder vai sozinho para "Respondeu" na esteira
wa.on('message', async m => {
  try { const n = m.from.replace(/@.*/, ''); const { contatos } = await (await fetch(CENTRAL, { headers: { Authorization: 'Bearer ' + TOKEN } })).json();
    const c = (contatos || []).find(x => x.wa === n && x.etapa === 'enviado'); if (c) { await api({ id: c.id, acao: 'etapa', etapa: 'respondeu' }); console.log(hora(), `${c.nome} RESPONDEU → esteira`); } } catch (e) {}
});
wa.initialize();
