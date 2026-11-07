// Capas v11 (Reels 1080x1920): composição do template de advocacia recebido pelo Lindson.
// Cores medidas no template: preto #080808, degradê marrom-escuro no canto, dourado fosco #A89048
// (luz #C8A860, sombra #6E5A2A), branco #F8F8F8. Títulos em Inter peso 800-900.
// Não usa foto, logo, nome nem texto de terceiros. Espaço do instrutor tracejado, aguardando a foto.
const { chromium } = require('playwright');
const path = require('path');

const BASE_CSS = `*{box-sizing:border-box;margin:0;padding:0}
html,body{background:#080808}
.c{width:1080px;height:1920px;position:relative;overflow:hidden;background:#080808;color:#F8F8F8;font-family:Inter,"Inter Display",Arial,sans-serif;-webkit-font-smoothing:antialiased}
.corner{position:absolute;inset:0;background:radial-gradient(circle at 0% 0%,rgba(110,90,42,.30) 0%,rgba(110,90,42,.10) 35%,rgba(8,8,8,0) 62%)}
.blob{position:absolute;background:linear-gradient(155deg,#C8A860 0%,#A89048 52%,#6E5A2A 100%)}
.frame{position:absolute;border:3px dashed #F8F8F8;background:rgba(8,8,8,.35);display:flex;align-items:center;justify-content:center}
.legend{background:#080808;color:#C8A860;font-weight:700;font-size:26px;letter-spacing:.08em;text-transform:uppercase;text-align:center;line-height:1.5;padding:18px 24px}
.logo{position:absolute;font-weight:900;font-size:28px;letter-spacing:.08em;color:#F8F8F8}
.logo b{color:#A89048;font-weight:900}
.t{position:absolute;font-weight:900;letter-spacing:-.04em;line-height:1.0;color:#F8F8F8}
.g{color:#A89048}
.body{position:absolute;font-weight:500;color:#F8F8F8}
.pill{position:absolute;height:100px;padding:0 52px;border-radius:999px;background:#A89048;color:#080808;font-weight:800;font-size:32px;letter-spacing:.01em;display:flex;align-items:center;white-space:nowrap}
.handle{position:absolute;font-weight:700;font-size:30px;color:#F8F8F8;letter-spacing:.01em}`;

const frame = (style) => `<div class="frame" style="${style}"><div class="legend">Espaço do instrutor<br>(aguardando a foto)</div></div>`;

// A: título grande à esquerda, mancha dourada à direita, espaço do instrutor tracejado
const A = `
<div class="corner"></div>
<div class="logo" style="left:90px;top:90px">PROCESSO <b>LEGISLATIVO</b></div>
<h1 class="t" style="left:90px;top:250px;font-size:132px">Pode votar<br><span class="g">sem quórum?</span></h1>
<p class="body" style="left:90px;top:640px;width:430px;font-size:40px;line-height:1.35">Entenda a regra da sessão antes de votar, com clareza.</p>
<div class="blob" style="right:-200px;top:800px;width:760px;height:880px;border-radius:46% 54% 38% 62% / 44% 40% 60% 56%"></div>
${frame('right:90px;top:760px;width:420px;height:980px')}
<div class="pill" style="left:90px;top:1420px">Assista ao curso básico</div>
<div class="handle" style="left:90px;bottom:90px">@curso_processo_legislativo_</div>`;

// B: título centralizado no topo, mancha dourada ocupando a base, pílula no meio
const B = `
<div class="corner"></div>
<div class="logo" style="left:0;right:0;top:90px;text-align:center">PROCESSO <b>LEGISLATIVO</b></div>
<h1 class="t" style="left:0;right:0;top:220px;text-align:center;font-size:124px">Pode votar<br><span class="g">sem quórum?</span></h1>
<p class="body" style="left:150px;right:150px;top:560px;text-align:center;font-size:40px;line-height:1.35">Entenda a regra da sessão antes de votar, com clareza.</p>
<div class="pill" style="left:50%;transform:translateX(-50%);top:730px">Assista ao curso básico</div>
<div class="blob" style="left:-140px;top:960px;width:1360px;height:760px;border-radius:50% 50% 46% 54% / 60% 58% 42% 40%"></div>
${frame('left:300px;top:1020px;width:480px;height:660px')}
<div class="handle" style="left:0;right:0;top:1800px;text-align:center">@curso_processo_legislativo_</div>`;

// C: caixa alta fragmentada em 3 linhas, mancha dourada diagonal, handle e logo em texto no topo
const C = `
<div class="corner"></div>
<div class="handle" style="left:90px;top:90px">@curso_processo_legislativo_</div>
<div class="logo" style="right:90px;top:90px;text-align:right">PROCESSO <b>LEGISLATIVO</b></div>
<h1 class="t" style="left:90px;top:230px;font-size:124px;text-transform:uppercase">Pode votar</h1>
<h1 class="t g" style="left:330px;top:400px;font-size:124px;text-transform:uppercase">Sem</h1>
<h1 class="t g" style="left:90px;top:570px;font-size:124px;text-transform:uppercase">Quórum?</h1>
<div class="blob" style="left:250px;top:880px;width:1000px;height:560px;transform:rotate(-26deg);border-radius:50% 50% 46% 54% / 60% 40% 60% 40%"></div>
${frame('right:90px;top:960px;width:400px;height:640px')}
<p class="body" style="left:90px;top:800px;width:470px;font-size:40px;line-height:1.35">Entenda a regra da sessão antes de votar, com clareza.</p>
<div class="pill" style="left:90px;top:1600px">Assista ao curso básico</div>`;

const pages = [
  { name: 'capa-v11-A.png', body: A },
  { name: 'capa-v11-B.png', body: B },
  { name: 'capa-v11-C.png', body: C },
];

(async () => {
  const b = await chromium.launch({ args: ['--no-sandbox'] });
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
  for (const pg of pages) {
    const html = `<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>${BASE_CSS}</style></head><body><section class="c">${pg.body}</section></body></html>`;
    await p.setContent(html, { waitUntil: 'load' });
    await p.evaluate(() => document.fonts.ready);
    await (await p.$('section')).screenshot({ path: path.join(__dirname, 'capas-v11', pg.name) });
    console.log('ok', pg.name);
  }
  await b.close();
})().catch(e => { console.error(e.message); process.exit(1); });
