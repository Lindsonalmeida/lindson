// Capa v9: composição do template de advocacia recebido (fundo escuro, mancha dourada atrás da pessoa, título em duas cores, pílula de ação).
// Não usa a foto, a marca ou o texto do anúncio original. Espaço do instrutor reservado.
const { chromium } = require('playwright');
const path = require('path');
const CSS = `*{box-sizing:border-box;margin:0;padding:0}
.c{width:1080px;height:1920px;position:relative;overflow:hidden;background:#0B0B0B;color:#F4F1EA;font-family:Inter,Arial,sans-serif}
.blob{position:absolute;right:-120px;top:520px;width:860px;height:1000px;background:linear-gradient(160deg,#E2C98A 0%,#B8954F 60%,#7A5F2B 100%);border-radius:48% 52% 40% 60% / 40% 50% 50% 60%}
.slot{position:absolute;right:90px;top:430px;width:560px;height:1040px;border:3px dashed rgba(226,201,138,.8);display:flex;align-items:center;justify-content:center;text-align:center;font-size:26px;letter-spacing:.1em;text-transform:uppercase;color:#E2C98A;background:rgba(0,0,0,.25)}
.grid{position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.04) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.04) 1px,transparent 1px);background-size:120px 120px}
.h{position:absolute;left:90px;font-weight:800;font-size:132px;line-height:1.02;letter-spacing:-.03em}
.gold{color:#E2C98A}
.body{position:absolute;left:90px;width:520px;font-size:38px;line-height:1.4;color:rgba(244,241,234,.9)}
.pill{position:absolute;left:90px;height:92px;padding:0 48px;border:2px solid #E2C98A;border-radius:999px;display:flex;align-items:center;font-size:30px;font-weight:700;letter-spacing:.04em;color:#E2C98A;background:rgba(0,0,0,.4)}
.brand{position:absolute;left:90px;bottom:90px;font-size:30px;font-weight:800;letter-spacing:.02em}
.foot{position:absolute;right:90px;bottom:100px;font-size:26px;color:rgba(244,241,234,.8);text-align:right;line-height:1.5}`;
const HTML = `<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>${CSS}</style></head><body style="margin:0"><section class="c">
<div class="grid"></div><div class="blob"></div>
<div class="slot">Espaço do instrutor<br><br>(recorte, aguardando a foto)</div>
<div class="h" style="top:300px;width:800px">Pode votar<br><span class="gold">sem quórum?</span></div>
<div class="body" style="top:720px">Entenda a regra da sessão antes de votar, com clareza e sem jargão.</div>
<div class="pill" style="top:960px">Assista ao curso básico</div>
<div class="brand">Processo Legislativo</div>
<div class="foot">@curso_processo_legislativo_<br>Para vereadores, assessores e servidores</div>
</section></body></html>`;
(async () => {
  const b = await chromium.launch({ args: ['--no-sandbox'] });
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
  await p.setContent(HTML, { waitUntil: 'load' });
  await p.evaluate(() => document.fonts.ready);
  await (await p.$('section')).screenshot({ path: path.join(__dirname, 'capas-v9', 'capa-v9-composicao-template.png') });
  await b.close(); console.log('ok');
})().catch(e => { console.error(e.message); process.exit(1); });
