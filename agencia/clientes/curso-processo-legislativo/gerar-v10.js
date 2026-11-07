// Capa v10: composição do template de advocacia de referência, com as cores medidas no template.
// Fundo #080808 com degradê marrom-escuro no canto superior esquerdo; dourado fosco #A89048 (luz #C8A860, sombra #6E5A2A); branco #F8F8F8.
// Não usa foto, logo, nome ou texto do anúncio de referência. Espaço do instrutor reservado (recorte tracejado dourado).
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

const CSS = `
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1920px;background:#080808}
.c{width:1080px;height:1920px;position:relative;overflow:hidden;color:#F8F8F8;
   font-family:Inter,sans-serif;
   background:radial-gradient(ellipse 900px 760px at 0% 0%,rgba(110,90,42,.30) 0%,rgba(110,90,42,0) 70%),#080808}
.logo{position:absolute;left:90px;top:96px;font-size:30px;font-weight:800;letter-spacing:.2em;color:#F8F8F8;white-space:nowrap}
.logo i{display:inline-block;width:14px;height:14px;background:#A89048;margin-right:18px;vertical-align:2px}
.h{position:absolute;left:90px;top:330px;font-weight:900;letter-spacing:-.035em;line-height:1.0;white-space:nowrap}
.h .gold{color:#A89048}
.body{position:absolute;left:90px;top:700px;width:760px;font-size:40px;line-height:1.42;font-weight:500;color:rgba(248,248,248,.88)}
.blob{position:absolute;left:420px;top:870px;width:600px;height:700px;
   background:linear-gradient(162deg,#C8A860 0%,#A89048 52%,#6E5A2A 100%);
   border-radius:46% 54% 42% 58% / 38% 46% 54% 62%}
.slot{position:absolute;left:540px;top:930px;width:400px;height:540px;border:4px dashed #C8A860;
   background:rgba(8,8,8,.42);display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;
   color:#C8A860;padding:40px}
.slot b{display:block;font-size:34px;font-weight:800;letter-spacing:.02em;line-height:1.25}
.slot span{display:block;margin-top:14px;font-size:26px;font-weight:500;letter-spacing:.02em;line-height:1.3}
.pill{position:absolute;left:90px;top:1600px;height:104px;padding:0 56px;border-radius:999px;background:#A89048;color:#080808;
   display:flex;align-items:center;font-size:36px;font-weight:800;letter-spacing:.01em;white-space:nowrap}
.foot{position:absolute;left:90px;bottom:96px;right:90px}
.foot .handle{font-size:32px;font-weight:800;color:#F8F8F8;letter-spacing:.01em}
.foot .sub{margin-top:14px;font-size:26px;font-weight:500;color:rgba(248,248,248,.78);letter-spacing:.01em}
`;

const HTML = `<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>${CSS}</style></head>
<body><section class="c">
  <div class="logo"><i></i>PROCESSO LEGISLATIVO</div>
  <h1 class="h" id="t"><span>Pode votar</span><br><span class="gold">sem quórum?</span></h1>
  <p class="body">Entenda a regra da sessão antes de votar, com clareza.</p>
  <div class="blob"></div>
  <div class="slot"><div><b>Espaço do instrutor</b><span>(aguardando a foto)</span></div></div>
  <div class="pill">Assista ao curso básico</div>
  <div class="foot"><div class="handle">@curso_processo_legislativo_</div><div class="sub">Curso básico para vereadores, assessores e servidores</div></div>
</section></body></html>`;

(async () => {
  const outDir = path.join(__dirname, 'capas-v10');
  fs.mkdirSync(outDir, { recursive: true });
  const b = await chromium.launch({ args: ['--no-sandbox'] });
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
  await p.setContent(HTML, { waitUntil: 'load' });
  await p.evaluate(() => document.fonts.ready);
  // Ajuste do título: o maior tamanho que cabe em 900px (margem de 90px de cada lado).
  const info = await p.evaluate(() => {
    const h = document.getElementById('t');
    let size = 190;
    h.style.fontSize = size + 'px';
    while (h.scrollWidth > 900 && size > 60) { size -= 1; h.style.fontSize = size + 'px'; }
    const r = h.getBoundingClientRect();
    return { size, width: Math.round(r.width), height: Math.round(r.height), bottom: Math.round(r.bottom) };
  });
  console.log(JSON.stringify(info));
  const pill = await p.evaluate(() => { const r = document.querySelector('.pill').getBoundingClientRect(); return { x: r.x, w: r.width, r: r.right }; });
  console.log(JSON.stringify(pill));
  await (await p.$('section')).screenshot({ path: path.join(outDir, 'capa-v10-template-cores.png') });
  await b.close();
  console.log('ok');
})().catch(e => { console.error(e.message); process.exit(1); });
