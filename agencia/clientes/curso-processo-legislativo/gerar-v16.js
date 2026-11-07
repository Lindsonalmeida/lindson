// Capas v16 (1080x1920) do curso de processo legislativo, e prancha sistema-elementos.png.
// Padrões aplicados (ver identidade/ENGENHARIA-REVERSA-V16.md):
//   capa 1 = arcos dourados + selo com asterisco + destaque em caixa dourada + chips com ícone + barra inferior com pílula + tarja vertical + degradê de leitura + rótulo de série.
//   capa 2 = feixe de luz diagonal + selo circular com texto + lista em cartão com marcador triangular + barra inferior + rótulo de série.
//   capa 3 = feixe vertical de luz + cartão de dados no canto + destaque em caixa dourada + barra inferior + tarja vertical + rótulo de série.
// Marca (identidade/BRANDBOOK-V10.md): preto #080808, dourado fosco #A89048, highlight #C8A860, branco #F8F8F8, Inter Display 800.
// Espaço do instrutor: recorte tracejado dourado, rotulado "Espaço do instrutor (aguardando a foto)".
// Fotos: só de fotos-banco/ (ver FOTOS-USADAS.md, seção v16). Imagens embutidas como data URI.
// Uso: node gerar-v16.js   (Node + Playwright, com --no-sandbox). Saída em capas-v16/.
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const ROOT = __dirname;
const OUT = path.join(ROOT, 'capas-v16');
const foto = (f) =>
  'data:image/jpeg;base64,' + fs.readFileSync(path.join(ROOT, 'fotos-banco', f)).toString('base64');

// Peças de SVG reutilizáveis
const CHECK = `<svg width="26" height="26" viewBox="0 0 24 24"><path d="M5 12.5l4.5 4.5L19 7.5" fill="none" stroke="#A89048" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>`;
const TRI = `<svg width="22" height="22" viewBox="0 0 22 22"><path d="M5 3l13 8-13 8z" fill="#A89048"/></svg>`;
const ASTERISCO = (cor, sw = 5) => `<g stroke="${cor}" stroke-width="${sw}" stroke-linecap="round">
  <line x1="50" y1="22" x2="50" y2="78"/>
  <line x1="50" y1="22" x2="50" y2="78" transform="rotate(60 50 50)"/>
  <line x1="50" y1="22" x2="50" y2="78" transform="rotate(120 50 50)"/></g>`;
const SELO_ASTERISCO = `<svg class="abs" width="150" height="150" viewBox="0 0 100 100">
  <circle cx="50" cy="50" r="48" fill="rgba(8,8,8,.7)" stroke="#A89048" stroke-width="2"/>
  <circle cx="50" cy="50" r="41" fill="none" stroke="#6E5A2A" stroke-width="1"/>
  ${ASTERISCO('#C8A860', 5)}</svg>`;
const SELO_CIRCULAR = `<svg class="abs" width="250" height="250" viewBox="0 0 240 240">
  <defs><path id="anel" d="M120,120 m-92,0 a92,92 0 1,1 184,0 a92,92 0 1,1 -184,0"/></defs>
  <circle cx="120" cy="120" r="118" fill="rgba(8,8,8,.75)" stroke="#A89048" stroke-width="2"/>
  <text font-family="Inter" font-weight="700" font-size="19" fill="#C8A860" letter-spacing="2"><textPath href="#anel" textLength="570" lengthAdjust="spacing">PROCESSO LEGISLATIVO · CURSO BÁSICO · PROCESSO LEGISLATIVO ·</textPath></text>
  <circle cx="120" cy="120" r="56" fill="none" stroke="#6E5A2A" stroke-width="1.5"/>
  <g transform="translate(90 90) scale(0.6)">${ASTERISCO('#C8A860', 6)}</g></svg>`;
// Asterisco centrado no selo: centro (50,50) da peça 100 vai para (120,120) do selo 240 (translate 120-50*0.6 = 90)
const SELO_CIRCULAR_FIX = SELO_CIRCULAR;

const ARCOS = (cx, cy, cor = '#C8A860') => `<svg class="abs" style="left:${cx}px;top:${cy}px" width="980" height="980" viewBox="0 0 980 980">
  <g fill="none" stroke="${cor}" stroke-width="2" opacity=".55">
    <circle cx="490" cy="490" r="300" stroke-dasharray="620 1200" transform="rotate(200 490 490)"/>
    <circle cx="490" cy="490" r="380" stroke-dasharray="760 1500" transform="rotate(190 490 490)"/>
    <circle cx="490" cy="490" r="460" stroke-dasharray="880 1800" transform="rotate(205 490 490)" opacity=".35"/>
  </g></svg>`;

const CSS = `
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1920px;background:#080808;overflow:hidden}
.c{position:relative;width:1080px;height:1920px;overflow:hidden;background:#080808;color:#F8F8F8;font-family:Inter,Arial,sans-serif;-webkit-font-smoothing:antialiased}
.abs{position:absolute}
.full{position:absolute;inset:0}
.logo{position:absolute;left:86px;top:134px;font-family:'Inter Display',Inter,sans-serif;font-weight:800;letter-spacing:.035em;text-transform:uppercase;white-space:nowrap;line-height:1;font-size:46px;color:#F8F8F8}
.logo b{color:#A89048;font-weight:800}
.serie{position:absolute;top:140px;font-weight:700;font-size:26px;letter-spacing:.14em;text-transform:uppercase;color:#A89048;white-space:nowrap;line-height:1}
.fit{position:absolute;white-space:nowrap;font-family:'Inter Display',Inter,sans-serif;font-weight:800;line-height:1;letter-spacing:-.025em;color:#F8F8F8}
.g{color:#A89048}
.box{display:inline-block;background:#A89048;color:#080808;padding:0 .14em .16em;line-height:1.02}
.chip{position:absolute;display:inline-flex;align-items:center;gap:14px;height:76px;padding:0 30px;border:2px solid #A89048;border-radius:999px;background:rgba(8,8,8,.7);font-weight:700;font-size:26px;letter-spacing:.12em;text-transform:uppercase;color:#F8F8F8;white-space:nowrap}
.apoio{position:absolute;font-size:40px;line-height:1.35;color:#F8F8F8;font-weight:400}
.pill{display:inline-flex;align-items:center;height:84px;padding:0 34px;border:3px solid #A89048;border-radius:999px;color:#F8F8F8;font-family:'Inter Display',Inter,sans-serif;font-weight:800;font-size:26px;white-space:nowrap;background:rgba(8,8,8,.6)}
.barra{position:absolute;left:86px;right:86px;bottom:134px;display:flex;align-items:center;justify-content:space-between}
.handle{font-weight:700;font-size:20px;letter-spacing:.08em;text-transform:uppercase;color:#F8F8F8;white-space:nowrap;line-height:1}
.regra{position:absolute;left:86px;right:86px;bottom:226px;height:2px;background:linear-gradient(90deg,#A89048 0%,rgba(168,144,72,.25) 100%)}
.tarja-d{position:absolute;right:0;top:0;width:18px;height:620px;background:#A89048}
.tarja-e{position:absolute;left:0;width:14px;background:#A89048}
.leitura{position:absolute;inset:0;background:linear-gradient(180deg,rgba(8,8,8,.92) 0%,rgba(8,8,8,.35) 30%,rgba(8,8,8,.25) 55%,rgba(8,8,8,.9) 80%,#080808 100%)}
.feixe{position:absolute;background:linear-gradient(115deg,rgba(200,168,96,0) 40%,rgba(200,168,96,.2) 50%,rgba(200,168,96,0) 60%)}
.slot{position:absolute;display:flex;align-items:center;justify-content:center;text-align:center;border:3px dashed #A89048;background:rgba(8,8,8,.88);color:#C8A860;font-family:Inter,Arial,sans-serif;font-weight:700;font-size:26px;letter-spacing:.06em;line-height:1.35;padding:30px}
.cartao{position:absolute;right:86px;top:250px;width:330px;padding:28px 30px;background:rgba(8,8,8,.78);border:2px solid #6E5A2A;border-radius:18px}
.cartao .k{font-weight:700;font-size:22px;letter-spacing:.14em;text-transform:uppercase;color:#A89048}
.cartao .t{font-family:'Inter Display',Inter,sans-serif;font-weight:800;font-size:44px;line-height:1.05;margin-top:10px;color:#F8F8F8}
.cartao .s{font-size:24px;line-height:1.35;color:#C8C6C0;margin-top:12px}
.lista{position:absolute;left:86px;width:520px;padding:26px 36px;background:rgba(8,8,8,.72);border:1px solid #6E5A2A;border-radius:18px}
.lista div{display:flex;align-items:center;gap:18px;font-weight:700;font-size:32px;letter-spacing:.02em;color:#F8F8F8;line-height:1}
.lista div+div{margin-top:26px}
`;

// Ajusta tamanhos: data-w = largura alvo em px (escala a fonte); data-cap = teto; data-center = centraliza na peça.
const FIT_JS = `
function fitAll(){
  document.querySelectorAll('[data-w]').forEach(function(el){
    var target = +el.dataset.w;
    el.style.fontSize = '100px';
    var w = el.getBoundingClientRect().width;
    var size = 100 * target / w;
    if (el.dataset.cap) size = Math.min(size, +el.dataset.cap);
    el.style.fontSize = size + 'px';
    if (el.dataset.center) {
      var w2 = el.getBoundingClientRect().width;
      el.style.left = ((1080 - w2) / 2) + 'px';
    }
  });
}
document.fonts.ready.then(async function(){
  fitAll();
  if (window.__task) await window.__task();
  window.__ready = true;
});
`;

const doc = (body, script = '') =>
  `<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<meta name="viewport" content="width=1080">
<style>${CSS}</style></head>
<body>${body}<script>${FIT_JS}${script}</script></body></html>`;

const HANDLE = '@curso_processo_legislativo_';
const BARRA = (pill = 'Assista ao curso básico') => `
  <div class="regra"></div>
  <div class="barra"><div class="handle">${HANDLE}</div><div class="pill">${pill}</div></div>`;
const SLOT = (l, t, w, h) => `<div class="slot" style="left:${l}px;top:${t}px;width:${w}px;height:${h}px">Espaço do instrutor<br>(aguardando a foto)</div>`;

// ---------- Capa 1: "Pode votar / sem quórum?" ----------
const FOTO1 = foto('diversas/perguntas-podio.jpg'); // Pakutaso, pódio com perguntas (licença comercial livre). Reutilizada, ver FOTOS-USADAS.md
const capa1 = doc(
  `
<div class="c">
  <div class="full" style="background:url(${FOTO1}) 50% 50%/cover no-repeat;filter:saturate(.55) brightness(.62) contrast(1.06)"></div>
  <div class="leitura"></div>
  <div class="feixe" style="left:-200px;top:-100px;width:1000px;height:1200px;transform:rotate(12deg)"></div>
  ${ARCOS(300, -150)}
  <div class="tarja-d"></div>
  <div class="logo">PROCESSO <b>LEGISLATIVO</b></div>
  <div class="serie" style="left:86px;top:226px">Curso básico · Aula 01 / 03</div>
  <div class="fit" data-w="700" data-cap="150" style="left:86px;top:360px">
    <div>Pode votar</div>
    <div>sem <span class="box">quórum?</span></div>
  </div>
  ${SELO_ASTERISCO.replace('class="abs"', 'class="abs" style="left:800px;top:330px"')}
  <div class="apoio" style="left:86px;top:735px;width:700px">Entenda a regra antes de votar.</div>
  <div class="chip" style="left:86px;top:830px">${CHECK}Regimento</div>
  <div class="chip" style="left:86px;top:926px">${CHECK}Presença</div>
  ${SLOT(600, 980, 394, 640)}
  ${BARRA()}
</div>`
);

// ---------- Capa 2: "Quórum é o mínimo / para a votação valer." ----------
const FOTO2 = foto('pakutaso-v16/pakutaso-politico-maos-9243.jpg'); // Pakutaso (licença comercial sem atribuição), recorte sem o rosto
const capa2 = doc(
  `
<div class="c">
  <canvas id="foto2" class="full" style="width:1080px;height:1920px"></canvas>
  <div class="abs" style="left:0;top:960px;width:1080px;height:260px;background:linear-gradient(180deg,#080808 0%,rgba(8,8,8,0) 100%)"></div>
  <div class="leitura"></div>
  <div class="feixe" style="left:380px;top:-200px;width:900px;height:1300px;transform:rotate(-18deg)"></div>
  <div class="tarja-e" style="top:420px;height:600px"></div>
  <div class="logo">PROCESSO <b>LEGISLATIVO</b></div>
  <div class="serie" style="left:86px;top:226px">Curso básico · Aula 02 / 03</div>
  ${SELO_CIRCULAR_FIX.replace('<svg class="abs" width="250" height="250"', '<svg class="abs" style="left:770px;top:150px" width="250" height="250"')}
  <div class="fit" data-w="860" data-cap="118" style="left:86px;top:520px">
    <div>Quórum é o</div>
    <div class="g">mínimo</div>
    <div>para a votação</div>
    <div>valer.</div>
  </div>
  <div class="abs" style="left:86px;top:1010px;width:140px;height:3px;background:#C8A860"></div>
  <div class="apoio" style="left:86px;top:1040px;width:800px">Antes de contar votos, confira o número mínimo de presentes.</div>
  <div class="lista" style="top:1190px">
    <div>${TRI}Regimento interno</div>
    <div>${TRI}Presença</div>
    <div>${TRI}Votação</div>
  </div>
  ${SLOT(640, 1170, 354, 480)}
  ${BARRA()}
</div>`,
  `
window.__task = async function(){
  const img = new Image(); img.src = ${JSON.stringify(FOTO2)}; await img.decode();
  const c = document.getElementById('foto2'); c.width = 1080; c.height = 1920;
  const x = c.getContext('2d');
  x.fillStyle = '#080808'; x.fillRect(0, 0, 1080, 1920);
  // recorte da faixa inferior: x 560..1560, y 200..1045 (sem o rosto, cortado no alto da foto original)
  const sx = 560, sy = 200, sw = 1000, sh = img.height - 200;
  const dh = Math.round(1080 * sh / sw);
  x.filter = 'saturate(.5) brightness(.7) contrast(1.05)';
  x.drawImage(img, sx, sy, sw, sh, 0, 1920 - dh, 1080, dh);
  x.filter = 'none';
};`
);

// ---------- Capa 3: "Quem pode propor?" ----------
// Capa 3 sem foto de banco: o pódio de 1600 px é igual à perguntas-podio (capa 1), e as demais candidatas tinham 800 px.
const capa3 = doc(
  `
<div class="c">
  <div class="deg"></div>
  <div class="leitura"></div>
  <div class="feixe" style="left:300px;top:-300px;width:560px;height:2400px;background:linear-gradient(90deg,rgba(200,168,96,0) 0%,rgba(200,168,96,.2) 50%,rgba(200,168,96,0) 100%)"></div>
  ${ARCOS(90, 300)}
  <div class="tarja-e" style="top:0;height:300px"></div>
  <div class="logo">PROCESSO <b>LEGISLATIVO</b></div>
  <div class="cartao">
    <div class="k">Aula 03 / 03</div>
    <div class="t">Iniciativa</div>
    <div class="s">Quem apresenta a proposta na casa.</div>
  </div>
  ${SLOT(470, 500, 470, 690)}
  <div class="fit" data-w="860" data-cap="150" style="left:86px;top:1230px">
    <div>Quem pode</div>
    <div><span class="box">propor?</span></div>
  </div>
  <div class="apoio" style="left:86px;top:1580px;width:900px">Quem tem legitimidade para iniciar a proposta.</div>
  ${BARRA()}
</div>`
);

// ---------- Prancha: elementos isolados (sistema-elementos.png, 1600x1100) ----------
const ELEMENTOS = `
<div class="c" style="width:1600px;height:1180px;padding:60px;background:#080808">
  <div class="logo" style="position:absolute;left:60px;top:44px;font-size:34px">PROCESSO <b>LEGISLATIVO</b></div>
  <div class="serie" style="position:absolute;right:60px;top:52px;font-size:20px">Sistema de elementos · v16</div>
  <div style="position:absolute;left:60px;top:120px;width:1480px;height:920px;display:grid;grid-template-columns:repeat(4,1fr);grid-auto-rows:270px;gap:24px">
    <div class="tile"><div class="tt">1 · Arcos de luz</div><svg width="100%" height="190" viewBox="0 0 320 190" preserveAspectRatio="xMidYMid slice"><g fill="none" stroke="#C8A860" stroke-width="2" opacity=".6"><circle cx="150" cy="260" r="120" stroke-dasharray="330 800" transform="rotate(200 150 260)"/><circle cx="150" cy="260" r="165" stroke-dasharray="420 1100" transform="rotate(190 150 260)"/><circle cx="150" cy="260" r="210" stroke-dasharray="500 1400" transform="rotate(205 150 260)" opacity=".4"/></g></svg></div>
    <div class="tile"><div class="tt">2 · Selo com asterisco</div><div style="position:relative;height:190px"><svg width="170" height="170" viewBox="0 0 100 100" style="position:absolute;left:50%;top:10px;transform:translateX(-50%)"><circle cx="50" cy="50" r="48" fill="rgba(8,8,8,.7)" stroke="#A89048" stroke-width="2"/><circle cx="50" cy="50" r="41" fill="none" stroke="#6E5A2A" stroke-width="1"/>${ASTERISCO('#C8A860', 5)}</svg></div></div>
    <div class="tile"><div class="tt">3 · Selo circular com texto</div><div style="position:relative;height:190px"><div style="position:absolute;left:50%;top:0;transform:translateX(-50%);width:180px;height:180px">${SELO_CIRCULAR_FIX.replace('<svg class="abs" width="250" height="250"', '<svg width="180" height="180"')}</div></div></div>
    <div class="tile"><div class="tt">4 · Destaque em caixa dourada</div><div style="font-family:'Inter Display';font-weight:800;font-size:64px;line-height:1.2;padding-top:40px">sem <span class="box">quórum?</span></div></div>
    <div class="tile"><div class="tt">5 · Chips com ícone</div><div style="position:relative;height:190px"><div class="chip" style="position:absolute;left:0;top:30px">${CHECK}Regimento</div><div class="chip" style="position:absolute;left:0;top:120px">${CHECK}Presença</div></div></div>
    <div class="tile"><div class="tt">6 · Lista em cartão com marcador</div><div style="position:relative;height:190px"><div class="lista" style="position:absolute;left:0;top:10px;width:300px;padding:18px 22px">
      <div style="font-size:19px;white-space:nowrap">${TRI}Regimento interno</div><div style="font-size:19px;margin-top:16px">${TRI}Presença</div></div></div></div>
    <div class="tile"><div class="tt">7 · Barra inferior com pílula</div><div style="position:relative;height:190px"><div style="position:absolute;left:0;right:0;top:30px;display:flex;flex-direction:column;gap:18px;align-items:flex-start"><div class="handle" style="font-size:14px">${HANDLE}</div><div class="pill" style="height:60px;font-size:18px;padding:0 24px">Assista ao curso básico</div></div></div></div>
    <div class="tile"><div class="tt">8 · Tarja vertical e feixe de luz</div><div style="position:relative;height:190px;background:linear-gradient(115deg,#111 0%,#1a160c 100%);overflow:hidden"><div style="position:absolute;right:0;top:0;width:12px;height:190px;background:#A89048"></div><div class="feixe" style="left:-40px;top:-60px;width:280px;height:300px"></div></div></div>
    <div class="tile"><div class="tt">9 · Espaço do instrutor</div><div style="position:relative;height:190px"><div class="slot" style="position:absolute;left:50%;top:14px;transform:translateX(-50%);width:200px;height:160px;font-size:16px;padding:14px">Espaço do instrutor<br>(aguardando a foto)</div></div></div>
    <div class="tile"><div class="tt">10 · Cartão de dados</div><div style="position:relative;height:190px"><div class="cartao" style="position:absolute;right:auto;left:0;top:10px;width:300px;padding:18px 22px"><div class="k" style="font-size:18px">Aula 03 / 03</div><div class="t" style="font-size:34px">Iniciativa</div><div class="s" style="font-size:19px">Quem apresenta a proposta.</div></div></div></div>
    <div class="tile"><div class="tt">11 · Rótulo de série e filete</div><div style="position:relative;height:190px"><div class="serie" style="position:absolute;left:0;top:60px;font-size:15px;letter-spacing:.1em">Curso básico · Aula 01 / 03</div><div style="position:absolute;left:0;top:120px;width:140px;height:3px;background:#C8A860"></div></div></div>
    <div class="tile"><div class="tt">12 · Degradê de leitura</div><div style="position:relative;height:190px;background:linear-gradient(180deg,rgba(8,8,8,.92) 0%,rgba(8,8,8,.35) 30%,rgba(8,8,8,.25) 55%,rgba(8,8,8,.9) 80%,#080808 100%),#777671"></div></div>
  </div>
  <div style="position:absolute;left:60px;right:60px;bottom:36px;display:flex;gap:12px">
    <div class="sw" style="background:#080808;color:#F8F8F8">#080808 preto</div>
    <div class="sw" style="background:#A89048;color:#080808">#A89048 dourado fosco</div>
    <div class="sw" style="background:#C8A860;color:#080808">#C8A860 highlight</div>
    <div class="sw" style="background:#F8F8F8;color:#080808">#F8F8F8 branco</div>
    <div class="sw" style="background:#6E5A2A;color:#F8F8F8">#6E5A2A sombra do dourado</div>
    <div class="sw" style="background:#777671;color:#080808">#777671 cinza-quente (derivado)</div>
  </div>
</div>`;
const ELEM_CSS = `
.tile{position:relative;background:#111;border:1px solid #2a2a2a;border-radius:14px;padding:18px 20px;overflow:hidden}
.tt{font-weight:700;font-size:16px;letter-spacing:.1em;text-transform:uppercase;color:#A89048;margin-bottom:8px}
.sw{flex:1;padding:14px 14px;font-weight:700;font-size:16px;border-radius:12px;border:1px solid #2a2a2a}
`;
const elementosHtml = `<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>${CSS}${ELEM_CSS}html,body{width:1600px;height:1180px}</style></head><body>${ELEMENTOS}</body></html>`;

const CAPAS = [
  { file: 'capa-v16-1.png', html: capa1, w: 1080, h: 1920 },
  { file: 'capa-v16-2.png', html: capa2, w: 1080, h: 1920 },
  { file: 'capa-v16-3.png', html: capa3, w: 1080, h: 1920 },
  { file: 'sistema-elementos.png', html: elementosHtml, w: 1600, h: 1180 },
];

(async () => {
  fs.mkdirSync(OUT, { recursive: true });
  const browser = await chromium.launch({ args: ['--no-sandbox'] });
  for (const capa of CAPAS) {
    const page = await browser.newPage({ viewport: { width: capa.w, height: capa.h }, deviceScaleFactor: 1 });
    await page.setContent(capa.html, { waitUntil: 'load' });
    await page.evaluate(() => document.fonts.ready);
    await page.waitForFunction('window.__ready === true', null, { timeout: 60000 }).catch(() => {});
    await page.screenshot({ path: path.join(OUT, capa.file), clip: { x: 0, y: 0, width: capa.w, height: capa.h } });
    console.log('ok', path.join(OUT, capa.file));
    await page.close();
  }
  await browser.close();
})().catch((e) => { console.error(e); process.exit(1); });
