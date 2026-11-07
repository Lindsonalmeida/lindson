// Modelo v3 (com espaço para a foto do instrutor). Uma capa de exemplo na paleta do cartaz.
// Não tem foto real: o retângulo é um espaço reservado, até as fotos chegarem (uma por mensagem).
const { chromium } = require('playwright');
const path = require('path');
const html = `<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>
*{box-sizing:border-box;margin:0;padding:0}
.c{width:1080px;height:1920px;position:relative;overflow:hidden;background:#00241C;color:#FCFCFC;font-family:'Inter Display',Inter,sans-serif}
.band{position:absolute;left:0;right:0;top:1040px;height:430px;background:#C8B078}
.slot{position:absolute;left:150px;top:300px;width:780px;height:880px;border:4px dashed #C8B078;color:#C8B078;font-family:'JetBrains Mono',monospace;display:flex;align-items:center;justify-content:center;text-align:center;font-size:30px;letter-spacing:.06em;text-transform:uppercase;padding:40px}
.h{position:absolute;left:72px;right:72px;font-weight:900;text-transform:uppercase;letter-spacing:-.045em;line-height:.86}
.pill{position:absolute;left:72px;top:1560px;background:#FCFCFC;color:#00241C;font-family:'JetBrains Mono',monospace;font-size:30px;font-weight:700;padding:18px 28px;letter-spacing:.04em;text-transform:uppercase}
.bar{position:absolute;left:72px;right:72px;top:72px;display:flex;justify-content:space-between;font-family:'JetBrains Mono',monospace;font-size:24px;border-bottom:3px solid #FCFCFC;padding-bottom:22px}
</style></head><body>
<section class="c">
  <div class="bar"><span style="font-weight:900;font-family:'Inter Display',Inter;font-size:40px">PROCESSO LEGISLATIVO</span><span>Curso · 01</span></div>
  <div class="slot">Espaço da foto do instrutor<br>(recorte, rosto na parte superior)<br><br>aguardando a foto</div>
  <div class="band"></div>
  <div class="h" style="top:1080px;font-size:140px;color:#00241C">Pode votar<br>sem quórum?</div>
  <div class="pill">Curso básico · Câmara municipal</div>
</section></body></html>`;
(async () => {
  const b = await chromium.launch({ args: ['--no-sandbox'] });
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
  await p.setContent(html, { waitUntil: 'load' });
  await p.evaluate(() => document.fonts.ready);
  await (await p.$('section')).screenshot({ path: path.join(__dirname, 'capas-v2', 'modelo-v3-com-foto.png') });
  await b.close();
  console.log('ok');
})().catch(e => { console.error(e.message); process.exit(1); });
