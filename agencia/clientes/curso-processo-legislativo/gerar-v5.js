// Capas v5: fotos reais de banco (Pakutaso, uso comercial livre segundo o site) com duotone verde e título dourado.
const { chromium } = require('playwright');
const path = require('path');
const dir = __dirname;
const img = (f) => 'file://' + path.join(dir, 'fotos-banco', f);
const CSS = `*{box-sizing:border-box;margin:0;padding:0}
.c{width:1080px;height:1920px;position:relative;overflow:hidden;background:#00241C;color:#FCFCFC;font-family:'Inter Display',Inter,sans-serif}
.ph{position:absolute;inset:0;background-size:cover;background-position:center}
.duo{position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,36,28,.25) 0%,rgba(0,36,28,.75) 55%,rgba(0,36,28,.97) 100%)}
.h{position:absolute;left:80px;right:80px;font-weight:900;text-transform:uppercase;letter-spacing:-.05em;line-height:.84}
.gold{color:#C8B078}
.top{position:absolute;left:80px;right:80px;top:80px;display:flex;justify-content:space-between;font-family:'JetBrains Mono',monospace;font-size:24px;letter-spacing:.12em;text-transform:uppercase;color:#C8B078}
.logo{font-weight:900;font-size:38px;letter-spacing:-.02em;color:#FCFCFC;text-transform:uppercase}
.foot{position:absolute;left:80px;right:80px;bottom:60px;display:flex;justify-content:space-between;font-family:'JetBrains Mono',monospace;font-size:22px;letter-spacing:.1em;color:rgba(252,252,252,.7);text-transform:uppercase}
.sub{position:absolute;left:80px;right:80px;font-size:40px;line-height:1.35;color:rgba(252,252,252,.92)}`;
const C = [
 ['capa-v5-01-plenario', `<div class="ph" style="background-image:url('${img('camara-plenario-pakutaso.jpg')}');background-position:40% center"></div><div class="duo"></div>
   <div class="top"><span class="logo">Processo Legislativo</span><span>Nº 01/02</span></div>
   <div class="h" style="top:980px;font-size:200px">Pode votar</div>
   <div class="h gold" style="top:1150px;font-size:200px">sem quórum?</div>
   <div class="sub" style="top:1380px">Entenda a regra antes de votar, com clareza e sem jargão.</div>
   <div class="foot"><span>@curso_processo_legislativo_</span><span>Curso básico</span></div>`],
 ['capa-v5-02-proposta', `<div class="ph" style="background-image:url('${img('discurso-pakutaso.jpg')}');background-position:60% center"></div><div class="duo"></div>
   <div class="top"><span class="logo">Processo Legislativo</span><span>Nº 02/02</span></div>
   <div class="h" style="top:1000px;font-size:190px">Quem pode</div>
   <div class="h gold" style="top:1165px;font-size:190px">propor?</div>
   <div class="sub" style="top:1380px">Veja quem tem a iniciativa de um projeto de lei, e como ele começa.</div>
   <div class="foot"><span>@curso_processo_legislativo_</span><span>Curso básico</span></div>`],
];
(async () => {
  const b = await chromium.launch({ args: ['--no-sandbox'] });
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
  for (const [name, html] of C) {
    await p.setContent(`<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>${CSS}</style></head><body style="margin:0"><section class="c">${html}</section></body></html>`, { waitUntil: 'load' });
    await p.evaluate(() => document.fonts.ready);
    await p.waitForTimeout(300);
    await (await p.$('section')).screenshot({ path: path.join(dir, 'capas-v5', name + '.png') });
  }
  await b.close(); console.log('ok');
})().catch(e => { console.error(e.message); process.exit(1); });
