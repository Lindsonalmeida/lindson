// Capas v12 (1080x1920) com a marca aprovada: BRANDBOOK-V10.md.
// Preto #080808, degradê marrom #2A1E0F no canto, dourado fosco #A89048, branco #F8F8F8.
// Títulos em Inter Display 800, texto em Inter. Sem foto, logo ou texto de terceiros.
// Espaço do instrutor: recorte tracejado dourado, aguardando a foto.
// Uso: node gerar-v12.js   (Node + Playwright, com --no-sandbox). Saída em capas-v12/.
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

const BASE_CSS = `*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1920px;background:#080808;overflow:hidden}
.c{position:relative;width:1080px;height:1920px;overflow:hidden;background:#080808;color:#F8F8F8;font-family:Inter,Arial,sans-serif;-webkit-font-smoothing:antialiased}
.deg{position:absolute;inset:0;background:radial-gradient(ellipse 1000px 760px at 0% 0%,#2A1E0F 0%,rgba(42,30,15,.55) 45%,rgba(8,8,8,0) 62%)}
.logo{position:absolute;top:134px;font-family:'Inter Display',Inter,sans-serif;font-weight:800;font-size:40px;letter-spacing:.035em;text-transform:uppercase;white-space:nowrap;line-height:1;color:#F8F8F8}
.logo b{color:#A89048;font-weight:800}
.t{position:absolute;font-family:'Inter Display',Inter,sans-serif;font-weight:800;letter-spacing:-.03em;line-height:.98;white-space:nowrap;color:#F8F8F8}
.g{color:#A89048}
.ap{position:absolute;font-weight:400;font-size:40px;line-height:1.4;color:#F8F8F8;white-space:nowrap}
.pill{position:absolute;height:100px;padding:0 50px;border-radius:999px;background:#A89048;color:#080808;font-weight:800;font-size:32px;display:flex;align-items:center;white-space:nowrap}
.handle{position:absolute;left:86px;bottom:134px;font-weight:700;font-size:28px;letter-spacing:.14em;text-transform:uppercase;color:#F8F8F8;white-space:nowrap;line-height:1}
.blob{position:absolute;background:#A89048}
.frame{position:absolute;background:#080808;outline:3px dashed #A89048;outline-offset:-22px;display:flex;align-items:center;justify-content:center}
.legend{width:78%;text-align:center;color:#C8A860;font-weight:700;font-size:30px;line-height:1.4}
.card{position:absolute;background:#080808;border:3px solid #A89048;border-radius:6px}
.rot{position:absolute;font-weight:700;font-size:28px;letter-spacing:.14em;text-transform:uppercase;color:#777671;white-space:nowrap;line-height:1}
`;

const frame = (style) =>
  `<div class="frame" style="${style}"><div class="legend">Espaço do instrutor (aguardando a foto)</div></div>`;

const logo = (style) =>
  `<div class="logo" style="${style}">PROCESSO <b>LEGISLATIVO</b></div>`;

const handle = `<div class="handle">@curso_processo_legislativo_</div>`;

// 1. Título à esquerda; forma dourada grande cortando a borda direita.
const V1 = `
<div class="deg"></div>
${logo('left:86px')}
<h1 class="t" style="left:86px;top:500px;font-size:124px">Pode votar<br><span class="g">sem quórum?</span></h1>
<p class="ap" style="left:86px;top:840px">A regra da sessão, explicada com calma.</p>
<div class="pill" style="left:86px;top:1010px">Assista ao curso básico</div>
<div class="blob" style="left:660px;top:930px;width:620px;height:820px;border-radius:58% 42% 38% 62% / 46% 54% 46% 54%"></div>
${frame('left:700px;top:1110px;width:300px;height:520px')}
${handle}`;

// 2. Título centralizado no topo; forma elíptica ocupando a base; pílula no meio.
const V2 = `
<div class="deg"></div>
${logo('left:86px')}
<h1 class="t" style="left:0;width:1080px;text-align:center;top:300px;font-size:132px">Quem pode<br><span class="g">propor?</span></h1>
<p class="ap" style="left:0;width:1080px;text-align:center;top:600px">Quem tem legitimidade para iniciar a proposta.</p>
<div class="pill" style="left:50%;transform:translateX(-50%);top:880px">Assista ao curso básico</div>
<div class="blob" style="left:40px;top:1160px;width:1000px;height:560px;border-radius:50%"></div>
${frame('left:370px;top:1240px;width:340px;height:400px')}
${handle}`;

// 3. Título escalonado em 3 linhas; forma diagonal; logo no topo à direita.
const V3 = `
<div class="deg"></div>
${logo('right:86px;text-align:right')}
<h1 class="t" style="left:86px;top:400px;font-size:128px">O que é</h1>
<h1 class="t" style="left:300px;top:540px;font-size:128px">medida</h1>
<h1 class="t" style="left:86px;top:680px;font-size:128px"><span class="g">provisória?</span></h1>
<p class="ap" style="left:86px;top:880px">O instrumento, o prazo e quem decide.</p>
<div class="pill" style="left:86px;top:1040px">Assista ao curso básico</div>
<div class="blob" style="left:-200px;top:1200px;width:1500px;height:330px;transform:rotate(-20deg);border-radius:165px"></div>
${frame('left:640px;top:1100px;width:300px;height:360px')}
${handle}`;

// 4. Faixa dourada horizontal dividindo a peça; título acima, espaço do instrutor abaixo.
const V4 = `
<div class="deg"></div>
${logo('left:86px')}
<h1 class="t" style="left:86px;top:330px;font-size:124px">Devido<br><span class="g">processo<br>legislativo</span></h1>
<p class="ap" style="left:86px;top:740px">A ordem dos atos, do começo ao fim.</p>
<div class="blob" style="left:0;top:860px;width:1080px;height:96px"></div>
<div class="rot" style="left:86px;top:893px;color:#080808;font-size:30px;font-weight:700">Curso básico · processo legislativo</div>
${frame('left:86px;top:1000px;width:908px;height:520px;background:#141414')}
<div class="pill" style="left:86px;top:1600px">Assista ao curso básico</div>
${handle}`;

// 5. Cartão escuro com borda dourada sobreposto a um degradê; título dentro; forma dourada atrás.
const V5 = `
<div class="deg"></div>
<div class="blob" style="left:470px;top:1000px;width:760px;height:800px;border-radius:46% 54% 40% 60% / 50% 40% 60% 50%"></div>
${logo('left:86px')}
<div class="card" style="left:86px;top:300px;width:908px;height:820px"></div>
<div class="rot" style="left:150px;top:360px">Curso básico</div>
<h1 class="t" style="left:150px;top:430px;font-size:96px">Sessão secreta<br><span class="g">pode acontecer?</span></h1>
<p class="ap" style="left:150px;top:680px">O que a regra diz, e o que ela não diz.</p>
<div class="pill" style="left:150px;top:920px">Assista ao curso básico</div>
${frame('left:600px;top:1180px;width:300px;height:500px')}
${handle}`;

const pages = [
  { name: 'capa-v12-1.png', body: V1 },
  { name: 'capa-v12-2.png', body: V2 },
  { name: 'capa-v12-3.png', body: V3 },
  { name: 'capa-v12-4.png', body: V4 },
  { name: 'capa-v12-5.png', body: V5 },
];

(async () => {
  const outDir = path.join(__dirname, 'capas-v12');
  fs.mkdirSync(outDir, { recursive: true });
  const b = await chromium.launch({ args: ['--no-sandbox'] });
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
  for (const pg of pages) {
    const html = `<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>${BASE_CSS}</style></head><body><section class="c">${pg.body}</section></body></html>`;
    await p.setContent(html, { waitUntil: 'load' });
    await p.evaluate(() => document.fonts.ready);
    // Verificação: textos dentro das margens (86 px laterais, 134 px verticais) e sem estouro horizontal.
    const report = await p.evaluate(() => {
      const sec = document.querySelector('section').getBoundingClientRect();
      const out = [];
      document.querySelectorAll('.t, .ap, .logo, .pill, .handle, .legend, .rot').forEach((el) => {
        const r = el.getBoundingClientRect();
        const txt = (el.textContent || '').trim().slice(0, 30);
        const L = r.left - sec.left, R = r.right - sec.left, T = r.top - sec.top, B = r.bottom - sec.top;
        const bad = L < 86 - 1 || R > 994 + 1 || T < 134 - 1 || B > 1786 + 1 || el.scrollWidth > el.clientWidth + 1;
        out.push({ txt, L: Math.round(L), R: Math.round(R), T: Math.round(T), B: Math.round(B), bad });
      });
      return out;
    });
    report.filter((r) => r.bad).forEach((r) => console.log('  AVISO margem:', pg.name, JSON.stringify(r)));
    await (await p.$('section')).screenshot({ path: path.join(outDir, pg.name) });
    console.log('ok', pg.name);
  }
  await b.close();
})().catch((e) => { console.error(e.message); process.exit(1); });
