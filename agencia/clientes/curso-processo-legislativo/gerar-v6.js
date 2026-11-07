// Capa v6: martelo real (Pexels 5668473) com duotone verde e título dourado.
const { chromium } = require('playwright');
const path = require('path');
const dir = __dirname;
const html = `<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>
*{box-sizing:border-box;margin:0;padding:0}
.c{width:1080px;height:1920px;position:relative;overflow:hidden;background:#00241C;color:#FCFCFC;font-family:'Inter Display',Inter,sans-serif}
.ph{position:absolute;inset:0;background-color:#00241C;background-image:url('file://${path.join(dir,'fotos-banco','martelo-pexels-5668473.jpg')}');background-repeat:no-repeat;background-size:cover;background-position:62% center}
.duo{position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,36,28,.55) 0%,rgba(0,36,28,.2) 35%,rgba(0,36,28,.85) 70%,rgba(0,36,28,.98) 100%)}
.h{position:absolute;left:80px;right:80px;font-weight:900;text-transform:uppercase;letter-spacing:-.05em;line-height:.84}
.gold{color:#C8B078}
.top{position:absolute;left:80px;right:80px;top:80px;display:flex;justify-content:space-between;font-family:'JetBrains Mono',monospace;font-size:24px;letter-spacing:.12em;text-transform:uppercase;color:#C8B078}
.logo{font-weight:900;font-size:38px;letter-spacing:-.02em;color:#FCFCFC;text-transform:uppercase}
.sub{position:absolute;left:80px;right:80px;font-size:40px;line-height:1.35;color:rgba(252,252,252,.92)}
.foot{position:absolute;left:80px;right:80px;bottom:60px;display:flex;justify-content:space-between;font-family:'JetBrains Mono',monospace;font-size:22px;letter-spacing:.1em;color:rgba(252,252,252,.7);text-transform:uppercase}
</style></head><body style="margin:0"><section class="c">
<div class="ph"></div><div class="duo"></div>
<div class="top"><span class="logo">Processo Legislativo</span><span>Nº 01/01</span></div>
<div class="h" style="top:1000px;font-size:200px">Quórum</div>
<div class="h gold" style="top:1190px;font-size:150px;letter-spacing:-.04em">é o mínimo</div>
<div class="sub" style="top:1420px">para a votação valer. Entenda a regra antes de votar.</div>
<div class="foot"><span>@curso_processo_legislativo_</span><span>Curso básico</span></div>
</section></body></html>`;
(async () => {
  const b = await chromium.launch({ args: ['--no-sandbox'] });
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
  await p.setContent(html, { waitUntil: 'load' });
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(400);
  await (await p.$('section')).screenshot({ path: path.join(dir, 'capas-v5', 'capa-v6-martelo-quorum.png') });
  await b.close(); console.log('ok');
})().catch(e => { console.error(e.message); process.exit(1); });
