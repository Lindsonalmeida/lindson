// Capas v15 (1080x1920) do curso de processo legislativo + prancha dos elementos do sistema.
// Sistema de elementos repetido nas três peças: grade dourada a 12%, margens de 86 px, rótulo de série no topo,
// selo (circular ou retangular) com seta, chips numerados, cantoneira, tarja, moldura de foto, bloco de citação
// e barra de metadados no rodapé (handle à esquerda, CURSO · 2026 à direita, separados por filete).
// Marca: BRANDBOOK-V10.md (preto #080808, dourado fosco #A89048, branco #F8F8F8, Inter Display 800).
// Fotos: só de fotos-banco/ (ver FOTOS-USADAS.md, seção v15). Imagens embutidas como data URI.
// Uso: node gerar-v15.js   (Node + Playwright, com --no-sandbox). Saída em capas-v15/.
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const ROOT = __dirname;
const OUT = path.join(ROOT, 'capas-v15');
const foto = (f) =>
  'data:image/jpeg;base64,' + fs.readFileSync(path.join(ROOT, 'fotos-banco', f)).toString('base64');

const CSS = `
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1920px;background:#080808;overflow:hidden}
.c{position:relative;width:1080px;height:1920px;overflow:hidden;background:#080808;color:#F8F8F8;font-family:Inter,Arial,sans-serif;-webkit-font-smoothing:antialiased}
.abs{position:absolute}
.full{position:absolute;inset:0}
.g{color:#A89048}
.grid{position:absolute;inset:0;pointer-events:none}
.grid i{position:absolute;top:0;bottom:0;width:1px;background:rgba(168,144,72,.12)}
.head{position:absolute;left:86px;right:86px;top:134px;display:flex;justify-content:space-between;align-items:center}
.logo{font-family:'Inter Display',Inter,sans-serif;font-weight:800;letter-spacing:.035em;text-transform:uppercase;white-space:nowrap;line-height:1;color:#F8F8F8}
.logo b{color:#A89048;font-weight:800}
.rot{font-weight:700;font-size:28px;letter-spacing:.14em;text-transform:uppercase;color:#777671;white-space:nowrap;line-height:1}
.fit{position:absolute;white-space:nowrap;font-family:'Inter Display',Inter,sans-serif;font-weight:800;line-height:.98;letter-spacing:-.025em;color:#F8F8F8}
.rule{position:absolute;left:86px;right:86px;top:1730px;height:2px;background:#A89048;opacity:.8}
.handle,.meta{position:absolute;top:1758px;font-weight:700;font-size:28px;letter-spacing:.14em;text-transform:uppercase;color:#F8F8F8;white-space:nowrap;line-height:1}
.handle{left:86px}
.meta{right:86px}
.chips{position:absolute;left:86px;display:flex;gap:16px}
.chip{height:84px;padding:0 26px;border:2px solid #A89048;display:flex;align-items:center;gap:14px;font-weight:700;font-size:30px;color:#F8F8F8;white-space:nowrap;line-height:1}
.chip b{font-family:'Inter Display',Inter,sans-serif;font-weight:800;color:#A89048;font-size:30px}
.cit{position:absolute;left:86px;width:908px;display:flex;gap:26px;align-items:flex-start}
.qm{font-family:'Inter Display',Inter,sans-serif;font-weight:800;font-size:150px;line-height:.6;color:#A89048;flex:none;height:90px}
.cit p{font-size:42px;line-height:1.35;color:#F8F8F8;font-weight:500}
.ap{position:absolute;left:86px;width:908px;font-size:40px;line-height:1.4;color:#F8F8F8}
.tarja{position:absolute;left:0;right:0;height:84px;background:#A89048;color:#080808;font-family:'Inter Display',Inter,sans-serif;font-weight:800;font-size:30px;letter-spacing:.12em;text-transform:uppercase;padding-left:86px;line-height:84px;white-space:nowrap}
.cant{position:absolute;width:56px;height:56px;border:0 solid #A89048}
.cant.tl{left:0;top:0;border-top-width:3px;border-left-width:3px}
.cant.tr{right:0;top:0;border-top-width:3px;border-right-width:3px}
.cant.bl{left:0;bottom:0;border-bottom-width:3px;border-left-width:3px}
.cant.br{right:0;bottom:0;border-bottom-width:3px;border-right-width:3px}
.filete{position:absolute;height:3px;background:#C8A860}
.selo-r{position:absolute;display:inline-flex;align-items:center;gap:18px;border:2px solid #A89048;padding:20px 28px;font-family:'Inter Display',Inter,sans-serif;font-weight:800;font-size:28px;letter-spacing:.14em;text-transform:uppercase;color:#F8F8F8;white-space:nowrap;line-height:1;background:rgba(8,8,8,.72)}
.selo-r span{color:#A89048;font-size:34px;letter-spacing:0}
.bignum{position:absolute;font-family:'Inter Display',Inter,sans-serif;font-weight:800;font-size:520px;line-height:1;letter-spacing:-.04em;color:transparent;-webkit-text-stroke:2px rgba(168,144,72,.5);white-space:nowrap}
`;

// Ajusta tamanhos: data-w = largura alvo em px (escala a fonte); data-cap = teto; data-center = centraliza.
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

const doc = (body, script = '', extraCss = '') =>
  `<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<meta name="viewport" content="width=1080">
<style>${CSS}${extraCss}</style></head>
<body>${body}<script>${FIT_JS}${script}</script></body></html>`;

// ---------- Elementos do sistema (mesmo HTML nas três capas e na prancha) ----------
const grid = () =>
  `<div class="grid">${[0, 1, 2, 3, 4, 5, 6].map((i) => `<i style="left:${86 + (i * 908) / 6}px"></i>`).join('')}</div>`;

const footer = () =>
  `<div class="rule"></div><div class="handle">@curso_processo_legislativo_</div><div class="meta">CURSO · 2026</div>`;

const chips = (items, top) =>
  `<div class="chips" style="top:${top}px">${items
    .map((t, i) => `<span class="chip"><b>${String(i + 1).padStart(2, '0')}</b>${t}</span>`)
    .join('')}</div>`;

const cit = (texto, top) =>
  `<div class="cit" style="top:${top}px"><div class="qm">“</div><p>${texto}</p></div>`;

let SEAL_N = 0;
// Selo circular: anel dourado, texto em volta, seta de direção (para baixo quando down = true).
const seloCirc = (size = 220, down = false) => {
  const id = 'sp' + ++SEAL_N;
  const rot = down ? ' transform="rotate(90 110 110)"' : '';
  return `<svg width="${size}" height="${size}" viewBox="0 0 220 220" style="display:block;overflow:visible">
<defs><path id="${id}" d="M110,110 m-86,0 a86,86 0 1,1 172,0 a86,86 0 1,1 -172,0"/></defs>
<circle cx="110" cy="110" r="108" fill="rgba(8,8,8,.72)" stroke="#A89048" stroke-width="2"/>
<circle cx="110" cy="110" r="64" fill="none" stroke="#A89048" stroke-width="1"/>
<text fill="#A89048" font-family="Inter, Arial, sans-serif" font-weight="800" font-size="19" letter-spacing="2"><textPath href="#${id}" textLength="536" lengthAdjust="spacing">REGRA DA SESSÃO · REGRA DA SESSÃO · </textPath></text>
<g${rot}><path d="M88,110 L128,110" stroke="#F8F8F8" stroke-width="3" fill="none"/><path d="M118,100 L130,110 L118,120" stroke="#F8F8F8" stroke-width="3" fill="none"/></g>
</svg>`;
};

const seloRet = (style) => `<div class="selo-r" style="${style}">REGRA DA SESSÃO <span>→</span></div>`;

const cantos = (size = 56) =>
  ['tl', 'tr', 'bl', 'br'].map((k) => `<i class="cant ${k}" style="width:${size}px;height:${size}px"></i>`).join('');

const head = (serie) =>
  `<div class="head"><div class="logo" data-w="440">PROCESSO <b>LEGISLATIVO</b></div><div class="rot">${serie}</div></div>`;

// Duotone dourado: sombras em preto, meios-tons em dourado fosco, luz alta clareando até branco suave.
const DUOTONE_JS = `
window.__duotone = function(canvas, img, W, H, mode){
  var off = document.createElement('canvas'); off.width = W; off.height = H;
  var o = off.getContext('2d');
  var s = Math.max(W / img.width, H / img.height);
  var dw = img.width * s, dh = img.height * s;
  o.drawImage(img, (W - dw) / 2, (H - dh) / 2, dw, dh);
  var d = o.getImageData(0, 0, W, H), p = d.data;
  var K = [8, 8, 8], G = [168, 144, 72], Wt = [248, 248, 248];
  function mix(a, b, t){ return [a[0]+(b[0]-a[0])*t, a[1]+(b[1]-a[1])*t, a[2]+(b[2]-a[2])*t]; }
  var c = canvas.getContext('2d'); canvas.width = W; canvas.height = H;
  var out = c.createImageData(W, H), q = out.data;
  for (var i = 0; i < p.length; i += 4) {
    var L = (0.3 * p[i] + 0.59 * p[i+1] + 0.11 * p[i+2]) / 255;
    L = Math.min(1, Math.max(0, (L - 0.5) * 1.25 + 0.5));
    var col = L < 0.8 ? mix(K, G, L / 0.8) : mix(G, Wt, ((L - 0.8) / 0.2) * 0.6);
    q[i] = col[0]; q[i+1] = col[1]; q[i+2] = col[2]; q[i+3] = 255;
  }
  c.putImageData(out, 0, 0);
};`;

// ---------- Capa 1 (01/05): "Pode votar sem quórum?" · moldura de foto com duotone dourado e cantoneiras ----------
const FOTO1 = foto('diversas/perguntas-podio.jpg'); // Pakutaso, pódio com cadeiras vazias (licença livre, uso comercial)
const capa1 = doc(
  `
<div class="c">
  ${grid()}
  ${head('Curso básico · 01/05')}
  <div class="fit" data-w="908" data-cap="190" style="left:86px;top:300px">
    <div>Pode votar</div>
    <div>sem <span class="g">quórum?</span></div>
  </div>
  <div class="abs" style="left:86px;top:712px;width:908px;height:620px">
    <canvas id="ht" style="position:absolute;inset:0;width:908px;height:620px"></canvas>
    ${cantos()}
    <div style="position:absolute;right:30px;bottom:30px">${seloCirc(200)}</div>
  </div>
  ${cit('Sem o quórum exigido pelo regimento, a votação não acontece.', 1372)}
  ${chips(['Presença', 'Maioria', 'Regimento'], 1540)}
  ${footer()}
</div>`,
  `
${DUOTONE_JS}
window.__task = async function(){
  const img = new Image(); img.src = ${JSON.stringify(FOTO1)}; await img.decode();
  window.__duotone(document.getElementById('ht'), img, 908, 620, 'gold');
};`
);

// ---------- Capa 2 (02/05): "Quórum é o mínimo para a votação valer." · foto em faixa, tarja e número de fundo ----------
const FOTO2 = foto('pakutaso-v15/pakutaso-speech-documents-58277.jpg'); // Pakutaso 58277 (vereador falando com documentos)
const capa2 = doc(
  `
<div class="c">
  <div class="full" style="height:740px;bottom:auto;background:url(${FOTO2}) 50% 38%/cover no-repeat;filter:saturate(.25) contrast(1.12) brightness(.72)"></div>
  <div class="full" style="height:740px;bottom:auto;background:linear-gradient(180deg,rgba(8,8,8,.94) 0%,rgba(8,8,8,.82) 16%,rgba(8,8,8,.12) 36%,rgba(8,8,8,.1) 50%,rgba(8,8,8,.6) 80%,#080808 100%)"></div>
  ${grid()}
  <div class="bignum" style="right:34px;top:150px">02</div>
  ${head('Curso básico · 02/05')}
  ${seloRet('left:86px;top:330px')}
  <div class="fit" data-w="908" data-cap="124" style="left:86px;top:780px">
    <div>Quórum é o</div>
    <div class="g">mínimo</div>
    <div>para a votação</div>
    <div><span class="g">valer.</span></div>
  </div>
  ${chips(['Instalação', 'Deliberação', 'Votação'], 1300)}
  <div class="tarja" style="top:1420px">Antes da votação, o quórum</div>
  <div class="ap" style="top:1540px">O número mínimo de presentes é definido pelo regimento interno de cada câmara.</div>
  ${footer()}
</div>`
);

// ---------- Capa 3 (03/05): "Quem pode propor?" · foto em tela cheia, selo circular com seta e cantoneira ----------
const FOTO3 = foto('pakutaso-v15/pakutaso-diet-road-4769.jpg'); // Pakutaso 4769 (entrada do prédio do parlamento nacional, sem pessoas)
const capa3 = doc(
  `
<div class="c">
  <div class="full" style="background:url(${FOTO3}) 50% 40%/cover no-repeat;filter:grayscale(.85) contrast(1.15) brightness(.78)"></div>
  <div class="full" style="background:linear-gradient(180deg,rgba(8,8,8,.92) 0%,rgba(8,8,8,.25) 22%,rgba(8,8,8,.2) 40%,rgba(8,8,8,.78) 62%,#080808 80%)"></div>
  ${grid()}
  ${head('Curso básico · 03/05')}
  <div class="abs" style="right:86px;top:250px">${seloCirc(220, true)}</div>
  <i class="cant tl" style="left:86px;top:1038px;width:64px;height:64px"></i>
  <div class="fit" data-w="908" data-cap="170" style="left:86px;top:1080px">
    <div>Quem pode</div>
    <div class="g">propor?</div>
  </div>
  ${chips(['Vereadores', 'Prefeito', 'Cidadãos'], 1470)}
  ${cit('Depende do tipo de proposta e da lei orgânica do município.', 1590)}
  ${footer()}
</div>`
);

// ---------- Prancha: os doze elementos isolados, com legenda ----------
const BOARD_CSS = `
html,body{width:1600px;height:auto;overflow:visible;background:#0b0b0b}
.board{position:relative;width:1600px;padding:70px 60px 60px;background:#0b0b0b;color:#F8F8F8;font-family:Inter,Arial,sans-serif}
.board h1{font-family:'Inter Display',Inter,sans-serif;font-weight:800;font-size:46px;letter-spacing:-.01em}
.board .sub{font-size:22px;color:#777671;margin-top:12px;line-height:1.4;max-width:1200px}
.grid-b{display:grid;grid-template-columns:repeat(4,340px);gap:44px 40px;margin-top:50px}
.card{width:340px}
.tile{position:relative;width:340px;height:230px;background:#080808;border:1px solid rgba(168,144,72,.3);overflow:hidden}
.tile .grid i{width:1px}
.cap{margin-top:14px}
.cap b{display:block;font-size:20px;font-weight:700;color:#F8F8F8}
.cap span{display:block;font-size:17px;color:#777671;margin-top:6px;line-height:1.35}
.num{position:absolute;left:0;top:0;font-size:6px}
`;

const tile = (inner, nome, desc) =>
  `<div class="card"><div class="tile">${inner}</div><div class="cap"><b>${nome}</b><span>${desc}</span></div></div>`;

const FOTO_BOARD = FOTO1;
const board = doc(
  `
<div class="board">
  <h1>Sistema de elementos · capas v15</h1>
  <div class="sub">Doze elementos usados nas três capas. Cada capa combina alguns; o sistema é o mesmo. Marca: preto #080808, dourado fosco #A89048, branco #F8F8F8, Inter Display 800.</div>
  <div class="grid-b">
    ${tile(
      `<div class="grid" style="position:absolute;inset:0">${[0, 1, 2, 3, 4, 5, 6].map((i) => `<i style="left:${20 + (i * 300) / 6}px"></i>`).join('')}</div>
       <div style="position:absolute;left:20px;right:20px;top:20px;bottom:20px;border:1px dashed rgba(168,144,72,.35)"></div>`,
      'Grade e margens',
      'Linhas finas em dourado a 12%. Margem de 86 px nas capas de 1080.'
    )}
    ${tile(
      `<div class="rot" style="position:absolute;left:20px;top:24px;font-size:20px">Curso básico · 01/05</div>
       <div style="position:absolute;left:20px;top:64px;width:120px;height:2px;background:#A89048"></div>`,
      'Rótulo de série',
      'No topo, em caixa alta. Mostra a aula: 01/05, 02/05...'
    )}
    ${tile(
      `<div class="bignum" style="left:14px;top:-30px;font-size:230px;-webkit-text-stroke:1.5px rgba(168,144,72,.6)">03</div>`,
      'Número de fundo',
      'Número grande em contorno, atrás do título. Discreto.'
    )}
    ${tile(
      `<div style="position:absolute;left:85px;top:30px">${seloCirc(170)}</div>`,
      'Selo circular',
      'Texto em círculo, anel dourado fino e seta de direção.'
    )}
    ${tile(
      `<div style="position:absolute;left:20px;top:40px">${seloRet('position:static;font-size:18px')}</div>
       <div style="position:absolute;left:20px;top:150px;font-family:'Inter Display',Inter,sans-serif;font-weight:800;font-size:20px;color:#F8F8F8">Pode ir sobre a foto.</div>`,
      'Selo retangular',
      'Texto curto com seta. Fica dentro da moldura ou da foto.'
    )}
    ${tile(
      `<div style="position:absolute;left:0;right:0;top:150px;height:2px;background:#A89048;opacity:.8"></div>
       <div style="position:absolute;left:20px;top:168px;font-weight:700;font-size:12px;letter-spacing:.06em;color:#F8F8F8;white-space:nowrap">@CURSO_PROCESSO_LEGISLATIVO_</div>
       <div style="position:absolute;left:20px;top:192px;font-weight:700;font-size:12px;letter-spacing:.06em;color:#A89048;white-space:nowrap">CURSO · 2026</div>`,
      'Barra de metadados',
      'Filete acima. Handle à esquerda, CURSO · 2026 à direita.'
    )}
    ${tile(
      `<div style="position:absolute;left:20px;top:60px;display:flex;gap:10px">${['Presença', 'Maioria', 'Votação']
        .map(
          (t, i) =>
            `<span style="height:44px;padding:0 9px;border:2px solid #A89048;display:flex;align-items:center;gap:6px;font-weight:700;font-size:12px;color:#F8F8F8;white-space:nowrap"><b style="font-family:'Inter Display',Inter,sans-serif;font-weight:800;color:#A89048;font-size:12px">0${i + 1}</b>${t}</span>`
        )
        .join('')}</div>`,
      'Chips numerados',
      'Dois ou três, em linha, com borda dourada e número.'
    )}
    ${tile(
      `<div style="position:absolute;left:20px;top:20px;width:300px;height:190px;border:1px solid rgba(168,144,72,.25)">${cantos(36)}</div>`,
      'Cantoneira',
      'Marca de canto dourada, nos cantos de uma moldura ou de um bloco.'
    )}
    ${tile(
      `<div class="tarja" style="top:70px;height:56px;line-height:56px;font-size:16px;padding-left:20px">Antes da votação, o quórum</div>`,
      'Tarja',
      'Faixa dourada de largura total com texto preto. Uma por capa, no máximo.'
    )}
    ${tile(
      `<div style="position:absolute;left:20px;top:20px;width:300px;height:190px;background:url(${FOTO_BOARD}) 30% 60%/cover no-repeat;filter:grayscale(.2) brightness(.8)"></div>
       <div style="position:absolute;left:20px;top:20px;width:300px;height:190px">${cantos(36)}</div>`,
      'Moldura de foto',
      'Foto com tratamento (duotone dourado, P&B ou escurecida). Uma vez só.'
    )}
    ${tile(
      `<div class="cit" style="left:20px;top:40px;width:300px;gap:12px"><div class="qm" style="font-size:90px;height:50px">“</div><p style="font-size:20px;line-height:1.35">Sem o quórum exigido, a votação não acontece.</p></div>`,
      'Bloco de citação',
      'Aspas grandes em dourado e frase curta, sem promessa.'
    )}
    ${tile(
      `<div class="logo" style="position:absolute;left:20px;top:44px;font-size:19px">PROCESSO <b>LEGISLATIVO</b></div>
       <div class="filete" style="left:20px;top:100px;width:120px"></div>`,
      'Logo e filete',
      'Logo em texto no topo, à esquerda. Filete claro para destaque.'
    )}
  </div>
</div>`,
  '',
  BOARD_CSS
);

const CAPAS = [
  { file: 'capa-v15-1.png', html: capa1 },
  { file: 'capa-v15-2.png', html: capa2 },
  { file: 'capa-v15-3.png', html: capa3 },
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
  const pb = await browser.newPage({ viewport: { width: 1600, height: 1400 }, deviceScaleFactor: 1 });
  await pb.setContent(board, { waitUntil: 'load' });
  await pb.waitForFunction('window.__ready === true', null, { timeout: 60000 });
  const h = await pb.evaluate(() => document.querySelector('.board').getBoundingClientRect().height);
  await pb.setViewportSize({ width: 1600, height: Math.ceil(h) });
  await pb.screenshot({ path: path.join(OUT, 'sistema-elementos.png'), clip: { x: 0, y: 0, width: 1600, height: Math.ceil(h) } });
  console.log('ok', path.join(OUT, 'sistema-elementos.png'));
  await browser.close();
})().catch((e) => { console.error(e); process.exit(1); });
