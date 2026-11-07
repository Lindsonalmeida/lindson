// Capas v13 (1080x1920) do curso de processo legislativo.
// Modulam as referências escolhidas em TEMPLATE-V12.md:
//   capa 1 = Strava (Hello Monday): título centrado em duas linhas, foto P&B com meio-tom, etiqueta inclinada;
//            acabamento Norton: marca gigante no topo, rótulo pequeno espaçado.
//   capa 2 = Norton (Koto): marca gigante no topo, foto escurecida em tela cheia, rótulo pequeno.
//   capa 3 = Scout Motors (Locomotive): título grande no terço inferior à esquerda, foto em caixa com margem, metadados nos cantos.
// Marca: BRANDBOOK-V10.md (preto #080808, dourado fosco #A89048, branco #F8F8F8, Inter Display 800).
// Fotos: só de fotos-banco/ (ver FOTOS-USADAS.md). Imagens embutidas como data URI.
// Uso: node gerar-v13.js   (Node + Playwright, com --no-sandbox). Saída em capas-v13/.
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const ROOT = __dirname;
const OUT = path.join(ROOT, 'capas-v13');
const foto = (f) =>
  'data:image/jpeg;base64,' + fs.readFileSync(path.join(ROOT, 'fotos-banco', f)).toString('base64');

const CSS = `
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1920px;background:#080808;overflow:hidden}
.c{position:relative;width:1080px;height:1920px;overflow:hidden;background:#080808;color:#F8F8F8;font-family:Inter,Arial,sans-serif;-webkit-font-smoothing:antialiased}
.abs{position:absolute}
.full{position:absolute;inset:0}
.deg{position:absolute;inset:0;background:radial-gradient(ellipse 1000px 760px at 0% 0%,#2A1E0F 0%,rgba(42,30,15,.55) 45%,rgba(8,8,8,0) 62%)}
.logo{position:absolute;font-family:'Inter Display',Inter,sans-serif;font-weight:800;letter-spacing:.035em;text-transform:uppercase;white-space:nowrap;line-height:1;color:#F8F8F8}
.logo b{color:#A89048;font-weight:800}
.fit{position:absolute;white-space:nowrap;font-family:'Inter Display',Inter,sans-serif;font-weight:800;line-height:.98;letter-spacing:-.025em;color:#F8F8F8}
.g{color:#A89048}
.rot{position:absolute;font-weight:700;font-size:28px;letter-spacing:.14em;text-transform:uppercase;color:#777671;white-space:nowrap;line-height:1}
.ap{position:absolute;font-size:40px;line-height:1.4;color:#F8F8F8;white-space:nowrap}
.pill{position:absolute;height:96px;padding:0 48px;border:3px solid #A89048;border-radius:999px;color:#F8F8F8;font-weight:800;font-size:32px;display:flex;align-items:center;white-space:nowrap;background:transparent}
.handle{position:absolute;left:86px;bottom:134px;font-weight:700;font-size:28px;letter-spacing:.14em;text-transform:uppercase;color:#F8F8F8;white-space:nowrap;line-height:1}
.tag{position:absolute;left:50%;transform:translateX(-50%) rotate(-6deg);background:#A89048;color:#080808;font-weight:800;font-size:34px;letter-spacing:.12em;text-transform:uppercase;padding:20px 40px;white-space:nowrap;line-height:1}
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

// ---------- Capa 1: Strava (título centrado, P&B com meio-tom) + acabamento Norton ----------
const FOTO1 = foto('diversas/perguntas-podio.jpg'); // foto ainda não usada no curso
const capa1 = doc(
  `
<div class="c">
  <canvas id="ht" class="full" style="width:1080px;height:1920px"></canvas>
  <div class="full" style="background:linear-gradient(180deg,rgba(8,8,8,.9) 0%,rgba(8,8,8,.35) 26%,rgba(8,8,8,.3) 52%,rgba(8,8,8,.55) 70%,rgba(8,8,8,.94) 100%)"></div>
  <div class="logo" data-w="908" style="left:86px;top:134px">PROCESSO <b>LEGISLATIVO</b></div>
  <div class="rot" style="left:86px;top:250px;color:#F8F8F8;opacity:.85">Regra da sessão, explicada com calma</div>
  <div class="fit" data-w="860" data-cap="168" data-center="1" style="top:700px">
    <div>Pode votar</div>
    <div>sem <span class="g">quórum?</span></div>
  </div>
  <div class="abs" style="left:470px;top:1040px;width:140px;height:3px;background:#C8A860"></div>
  <div class="tag" style="top:1120px">Curso básico · 2026</div>
  <div class="pill" style="left:50%;transform:translateX(-50%);top:1440px;white-space:nowrap">Assista ao curso básico</div>
  <div class="handle">@curso_processo_legislativo_</div>
</div>`,
  `
window.__task = async function(){
  const img = new Image(); img.src = ${JSON.stringify(FOTO1)}; await img.decode();
  const W = 1080, H = 1920;
  const off = document.createElement('canvas'); off.width = W; off.height = H;
  const o = off.getContext('2d');
  const scale = H / img.height;
  const sw = W / scale;               // largura de origem que cabe em 1080x1920
  const sx = (img.width - sw) * 0.62; // enquadra o pódio
  o.filter = 'grayscale(1) contrast(1.4) brightness(1.1)';
  o.drawImage(img, sx, 0, sw, img.height, 0, 0, W, H);
  o.filter = 'none';
  const d = o.getImageData(0, 0, W, H).data;
  const c = document.getElementById('ht'); c.width = W; c.height = H;
  const x = c.getContext('2d');
  x.fillStyle = '#080808'; x.fillRect(0, 0, W, H);
  x.fillStyle = '#F8F8F8';
  // Trama de meio-tom: pontos em grade girada 45 graus; raio proporcional à luz da foto.
  const S = 13, cx = W / 2, cy = H / 2, R = Math.hypot(W, H) / 2, k = Math.SQRT1_2;
  for (let u = -R; u <= R; u += S) {
    for (let v = -R; v <= R; v += S) {
      const px = cx + (u * k - v * k), py = cy + (u * k + v * k);
      if (px < 0 || py < 0 || px >= W || py >= H) continue;
      const L = d[(Math.floor(py) * W + Math.floor(px)) * 4] / 255;
      const r = S * 0.52 * Math.sqrt(L);
      if (r < 0.6) continue;
      x.beginPath(); x.arc(px, py, r, 0, Math.PI * 2); x.fill();
    }
  }
};`
);

// ---------- Capa 2: Norton (marca gigante no topo, foto escurecida, rótulo pequeno) ----------
const FOTO2 = foto('camara-plenario-pakutaso.jpg');
const capa2 = doc(
  `
<div class="c">
  <div class="full" style="background:url(${FOTO2}) 50% 50%/cover no-repeat;filter:saturate(.45) brightness(.5) contrast(1.08)"></div>
  <div class="full" style="background:linear-gradient(180deg,rgba(8,8,8,.9) 0%,rgba(8,8,8,.25) 30%,rgba(8,8,8,.3) 50%,rgba(8,8,8,.9) 74%,rgba(8,8,8,.98) 100%)"></div>
  <div class="deg"></div>
  <div class="logo" data-w="908" style="left:86px;top:134px">PROCESSO <b>LEGISLATIVO</b></div>
  <div class="rot" style="left:86px;top:250px;color:#F8F8F8;opacity:.85">Curso básico · 2026</div>
  <div class="fit" data-w="908" data-cap="128" style="left:86px;top:1000px">
    <div>Quórum é o</div>
    <div class="g">mínimo</div>
    <div>para a votação</div>
    <div>valer.</div>
  </div>
  <div class="pill" style="left:86px;top:1560px">Assista ao curso básico</div>
  <div class="handle">@curso_processo_legislativo_</div>
</div>`
);

// ---------- Capa 3: Scout Motors (título no terço inferior, foto em caixa, metadados nos cantos) ----------
const FOTO3 = foto('diversas/microfones.jpg');
const capa3 = doc(
  `
<div class="c">
  <div class="deg"></div>
  <div class="logo" data-w="380" style="left:86px;top:134px">PROCESSO <b>LEGISLATIVO</b></div>
  <div class="rot" style="right:86px;top:140px;text-align:right">Curso básico · 2026</div>
  <div class="abs" style="left:300px;top:250px;width:694px;height:800px;border:2px solid #A89048;padding:22px;background:#080808">
    <div style="width:100%;height:100%;background:url(${FOTO3}) 50% 50%/cover no-repeat"></div>
  </div>
  <div class="fit" data-w="908" data-cap="150" style="left:86px;top:1130px">
    <div>Quem pode</div>
    <div class="g">propor?</div>
  </div>
  <div class="ap" style="left:86px;top:1488px">Quem tem legitimidade para iniciar a proposta.</div>
  <div class="pill" style="left:86px;top:1600px">Assista ao curso básico</div>
  <div class="handle">@curso_processo_legislativo_</div>
</div>`
);

const CAPAS = [
  { file: 'capa-v13-1.png', html: capa1 },
  { file: 'capa-v13-2.png', html: capa2 },
  { file: 'capa-v13-3.png', html: capa3 },
];

(async () => {
  fs.mkdirSync(OUT, { recursive: true });
  const browser = await chromium.launch({ args: ['--no-sandbox'] });
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
  for (const capa of CAPAS) {
    await page.setContent(capa.html, { waitUntil: 'load' });
    await page.waitForFunction('window.__ready === true', null, { timeout: 60000 });
    await page.screenshot({ path: path.join(OUT, capa.file), clip: { x: 0, y: 0, width: 1080, height: 1920 } });
    console.log('ok', path.join(OUT, capa.file));
  }
  await browser.close();
})().catch((e) => { console.error(e); process.exit(1); });
