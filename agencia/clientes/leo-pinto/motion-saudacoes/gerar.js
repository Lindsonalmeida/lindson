// Leo Pinto · 10 saudações animadas para Stories (motion design, 1080x1920, 30 fps, 8 s) · conta Leandro, 14/11/2026.
// Pedido do Lindson: "crie 10 artes animadas para storys, grafic motion, designer motion, não vídeo, pro Leo Pinto. Saudações para postar
// uma por dia. Todas com foto dele do busto pra cima, em alto nível, upscale, premium."
// Identidade: padrão aprovado v13 v3 (só fontes, logo e cores; mapa oficial de SJB; sem raios, faixas, ícones, fumaça ou sol).
// Regra de situação: só saudação, fé, família, trabalho e "conte sempre comigo" (../instagram-v15-saudacoes/TEXTOS.md).
// node gerar.js <assets> <saida> [id]   assets = pasta com hd/<foto>.png, logo.png, logo-marinho.png, avatar.jpg
// Tudo determinístico: as animações são CSS pausadas e o quadro N é "currentTime = N/30". Sem timers.
const { chromium } = require('playwright'), path = require('path'), fs = require('fs'), { spawn } = require('child_process');
const [A, OUT, SO] = process.argv.slice(2), D = __dirname, FPS = 30, DUR = 8;
const b64 = (f, t) => `data:image/${t};base64,` + fs.readFileSync(f).toString('base64');
const MAPA = JSON.parse(fs.readFileSync(path.join(D, '..', 'motion-v1', 'mapa.js'), 'utf8').split('window.MAPA=')[1].replace(/;\s*$/, ''));

const TEMA = {
  royal:   { bg: 'radial-gradient(1300px 1300px at 70% 34%,#3F6DFF 0,#2350F5 34%,#1337B5 64%,#082063 100%)', tx: '#fff', ac: '#FFC20E', ac2: '#FF7A1A', cx: ['#FFC20E', '#082063', '#fff', '#2350F5'], base: '8,32,99', mapa: 'rgba(160,190,255,.20)', claro: 0 },
  sol:     { bg: 'radial-gradient(1300px 1300px at 30% 30%,#FFE98F 0,#FFCB2B 36%,#FFC20E 62%,#EFA300 100%)', tx: '#082063', ac: '#2350F5', ac2: '#FF7A1A', cx: ['#082063', '#FFC20E', '#fff', '#2350F5'], base: '214,138,0', mapa: 'rgba(8,32,99,.13)', claro: 1 },
  laranja: { bg: 'radial-gradient(1300px 1300px at 68% 30%,#FFA552 0,#FF7A1A 38%,#EE5F08 66%,#B94300 100%)', tx: '#fff', ac: '#FFE27A', ac2: '#082063', cx: ['#fff', '#FF7A1A', '#082063', '#FFC20E'], base: '150,52,0', mapa: 'rgba(255,255,255,.20)', claro: 0 },
  noite:   { bg: 'radial-gradient(1200px 1200px at 50% 38%,#1C3FA8 0,#0E2A7A 36%,#082063 62%,#030B2A 100%)', tx: '#fff', ac: '#FFC20E', ac2: '#8FB0FF', cx: ['#FFC20E', '#082063', '#fff', '#082063'], base: '3,11,42', mapa: 'rgba(143,176,255,.18)', claro: 0 },
  claro:   { bg: 'radial-gradient(1300px 1300px at 62% 32%,#FFFFFF 0,#FFF7E8 40%,#F8E7CB 70%,#EBD3A8 100%)', tx: '#082063', ac: '#2350F5', ac2: '#FF7A1A', cx: ['#2350F5', '#fff', '#FF7A1A', '#fff'], base: '226,196,150', mapa: 'rgba(35,80,245,.13)', claro: 1 },
};
// foto: w = largura em px no palco, x = esquerda; a base da foto sai pela base da arte e as laterais cortadas ficam fora do palco.
const S = [
  { id: '01-boa-semana',   tema: 'royal',   tipo: 'pilha', rot: 'SEGUNDA-FEIRA', l1: 'BOA', l2: 'SEMANA', frase: 'Que a semana comece com *fé e trabalho.*', foto: 'd-bracos-cruzados-branca', top: 880, w: 1240, x: -80, entra: 'sobe', mapa: [430, 250, 760, 6] },
  { id: '02-bom-dia',      tema: 'sol',     tipo: 'cruza', rot: 'BOM DIA, SÃO JOÃO BATISTA', l1: 'BOM', l2: 'DIA', frase: 'Que o seu dia *renda* e seja *leve.*', foto: 'i-maos-abertas-branca', top: 950, w: 1200, x: -60, entra: 'zoom', mapa: [-140, 640, 720, -8] },
  { id: '03-boa-tarde',    tema: 'laranja', tipo: 'caixas', rot: 'PASSANDO PRA DESEJAR', l1: 'BOA', l2: 'TARDE', frase: 'Segue firme: *o dia ainda rende.*', foto: 'f-punhos', top: 960, w: 760, x: 160, entra: 'sobe', mapa: [520, 900, 640, 10] },
  { id: '04-boa-noite',    tema: 'noite',   tipo: 'letra', rot: 'SÃO JOÃO BATISTA', l1: 'Boa noite', l2: 'BOM DESCANSO', frase: 'Descansa. *Amanhã a gente continua.*', foto: 'c-maos-juntas-laranja', top: 950, w: 1200, x: -60, entra: 'sobe', mapa: [180, 300, 720, 0] },
  { id: '05-sextou',       tema: 'royal',   tipo: 'eco', rot: 'SEXTA-FEIRA', l1: 'SEXTOU', l2: '', frase: 'Semana vencida. *Obrigado por cada dia.*', foto: 'b-punho', top: 900, w: 1260, x: -90, entra: 'esq', mapa: [560, 1060, 560, -6] },
  { id: '06-bom-sabado',   tema: 'claro',   tipo: 'pilha', rot: 'SÁBADO', l1: 'BOM', l2: 'SÁBADO', frase: 'Dia de *feira, família* e descanso.', foto: 'e-celular', top: 960, w: 860, x: 150, entra: 'dir', mapa: [-120, 300, 700, 12] },
  { id: '07-bom-domingo',  tema: 'sol',     tipo: 'letra', rot: 'DOMINGO', l1: 'Abençoado', l2: 'DOMINGO', frase: 'Um domingo de *paz* na sua casa.', foto: 'd-bracos-cruzados-branca', flip: 1, top: 960, w: 860, x: 110, entra: 'sobe', mapa: [470, 640, 700, 8] },
  { id: '08-fe-no-dia',    tema: 'claro',   tipo: 'cruza', rot: 'BOM DIA', l1: 'FÉ', l2: 'NO DIA', frase: 'Com fé, *todo dia começa bem.*', foto: 'c-maos-juntas-laranja', flip: 1, top: 950, w: 1200, x: -60, entra: 'esq', mapa: [420, 300, 700, -10] },
  { id: '09-boa-noite-paz', tema: 'noite',  tipo: 'eco', rot: 'BOA NOITE, SÃO JOÃO BATISTA', l1: 'BOA NOITE', l2: '', frase: 'Que a noite traga *paz pra sua família.*', foto: 'i-maos-abertas-branca', flip: 1, top: 960, w: 820, x: 130, entra: 'zoom', mapa: [-160, 980, 640, 6] },
  { id: '10-deus-abencoe', tema: 'laranja', tipo: 'caixas', rot: 'UMA PALAVRA PRA HOJE', l1: 'DEUS', l2: 'ABENÇOE', frase: 'Você, a sua família e *a nossa cidade.*', foto: 'f-punhos', flip: 1, top: 960, w: 760, x: 160, entra: 'zoom', mapa: [-160, 300, 680, -6] },
];

const css = `*{box-sizing:border-box;margin:0;padding:0}html,body{background:#000}
.a{position:relative;width:1080px;height:1920px;overflow:hidden;font-family:Montserrat,sans-serif}
.abs{position:absolute}.mk{overflow:hidden;position:absolute}
.ant{font-family:Anton;text-transform:uppercase;line-height:1.08;padding-top:.06em;white-space:nowrap}
.kau{font-family:'Kaushan Script';white-space:nowrap;line-height:1.1}
.rot{font:700 24px Montserrat;letter-spacing:.38em;text-transform:uppercase;white-space:nowrap}
.frase{font:700 42px/1.28 Montserrat;letter-spacing:-.01em}.frase span{display:inline-block;white-space:pre}
.pill{display:flex;align-items:center;gap:14px;font:700 26px Montserrat;padding:7px 26px 7px 7px;border-radius:99px;white-space:nowrap}
.pill img{width:54px;height:54px;border-radius:50%;object-fit:cover}
.grao{position:absolute;inset:0;pointer-events:none;opacity:.10;mix-blend-mode:overlay;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='300'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E")}
.luz{position:absolute;top:-20%;height:140%;width:520px;left:0;pointer-events:none;mix-blend-mode:soft-light;background:linear-gradient(100deg,transparent 0,rgba(255,236,170,.75) 50%,transparent 100%);filter:blur(30px)}
.cxa{display:inline-block;font:900 100px/1 Montserrat;padding:.12em .2em .1em;white-space:nowrap;letter-spacing:-.03em;box-shadow:0 26px 60px rgba(0,0,0,.28)}
@keyframes sobe{from{transform:translateY(112%)}to{transform:none}}
@keyframes desce{from{transform:translateY(-112%)}to{transform:none}}
@keyframes deEsq{from{transform:translateX(-118%)}to{transform:none}}
@keyframes deDir{from{transform:translateX(118%)}to{transform:none}}
@keyframes surge{from{opacity:0;transform:translateY(34px)}to{opacity:1;transform:none}}
@keyframes some0{from{opacity:0}to{opacity:1}}
@keyframes pop{0%{transform:scale(0) rotate(var(--r0,0deg))}62%{transform:scale(1.12) rotate(var(--r,0deg))}100%{transform:scale(1) rotate(var(--r,0deg))}}
@keyframes abre{from{clip-path:inset(0 100% 0 0)}to{clip-path:inset(0 -6% 0 0)}}
@keyframes larga{from{letter-spacing:1.4em;opacity:0}to{letter-spacing:.38em;opacity:1}}
@keyframes fSobe{from{transform:translateY(16%);opacity:0}to{transform:none;opacity:1}}
@keyframes fEsq{from{transform:translateX(-46%);opacity:0}to{transform:none;opacity:1}}
@keyframes fDir{from{transform:translateX(46%);opacity:0}to{transform:none;opacity:1}}
@keyframes fZoom{from{transform:scale(1.22);opacity:0;filter:blur(18px)}to{transform:none;opacity:1;filter:blur(0)}}
@keyframes flutua{from{transform:scale(1)}to{transform:scale(1.045)}}
@keyframes deriva{from{transform:translate(0,0) rotate(var(--mr,0deg))}to{transform:translate(var(--dx,26px),-30px) rotate(var(--mr,0deg))}}
@keyframes traca{from{stroke-dashoffset:1}to{stroke-dashoffset:0}}
@keyframes enche{from{fill-opacity:0}to{fill-opacity:1}}
@keyframes varre{from{transform:translateX(-700px) skewX(-12deg)}to{transform:translateX(1500px) skewX(-12deg)}}
@keyframes eco{from{opacity:0;transform:translateY(-70%)}to{opacity:var(--o,1);transform:none}}
@keyframes pulsa{0%,100%{transform:scale(1)}50%{transform:scale(1.035)}}
@keyframes respira{0%,100%{transform:translateY(0)}50%{transform:translateY(-7px)}}`;
const EXPO = 'cubic-bezier(.16,1,.3,1)', BACK = 'cubic-bezier(.34,1.56,.64,1)';
const an = (n, d, dl, e = EXPO) => `animation:${n} ${d}s ${e} ${dl}s both`;
const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;');
// frase palavra por palavra; *trecho* = cor de destaque
function frase(txt, t, t0, extra = '') {
  let dest = false, i = 0, h = '';
  for (const parte of txt.split(/(\*)/)) {
    if (parte === '*') { dest = !dest; continue; }
    for (const w of parte.split(/(\s+)/)) { if (!w) continue;
      if (/^\s+$/.test(w)) { h += ' '; continue; }
      h += `<span style="${dest ? `color:${t.ac};` : ''}${an('surge', .5, t0 + i++ * .075)}">${esc(w)}</span>`; }
  }
  return { html: `<div class="frase" style="color:${t.tx};${extra}">${h}</div>`, n: i };
}
const TIPO = {
  // pilha: linha 1 menor + linha 2 gigante na largura toda, subindo de dentro da máscara (kinetic type)
  pilha: (s, t, c) => { c.push([.25, 'whoosh'], [.55, 'boom'], [1.5, 'pop']);
    const f = frase(s.frase, t, 1.45, 'left:64px;right:64px;top:770px;position:absolute');
    return `<div class="mk" style="left:64px;top:290px;height:200px;width:952px"><div class="ant" style="font-size:160px;color:${t.ac};${an('sobe', .7, .25)}">${esc(s.l1)}</div></div>
     <div class="mk" style="left:64px;top:462px;width:952px;height:330px"><div class="ant" data-fit="952" data-max="330" style="color:${t.tx};${an('sobe', .8, .5)}">${esc(s.l2)}</div></div>${f.html}`; },
  // cruza: linha 1 entra da esquerda, linha 2 da direita, alinhadas em lados opostos; frase em linhas grifadas
  cruza: (s, t, c) => { c.push([.2, 'whoosh'], [.5, 'whoosh'], [.95, 'boom'], [1.6, 'pop']);
    const f = frase(s.frase, t, 1.55, 'left:64px;right:64px;top:800px;position:absolute;text-align:right');
    return `<div class="mk" style="left:0;top:290px;width:1080px;height:270px"><div class="ant abs" data-fit="${s.l1.length < 3 ? 330 : 560}" data-max="270" style="left:64px;color:${t.tx};${an('deEsq', .75, .2)}">${esc(s.l1)}</div></div>
     <div class="mk" style="left:0;top:540px;width:1080px;height:270px"><div class="ant abs" data-fit="${s.l2.length < 4 ? 520 : 760}" data-max="270" style="right:64px;color:${t.ac2};${an('deDir', .75, .45)}">${esc(s.l2)}</div></div>${f.html}`; },
  // caixas: cada palavra numa caixa de cor (como LEO | PINTO), estourando com leve giro
  caixas: (s, t, c) => { c.push([.3, 'pop'], [.6, 'pop'], [.62, 'boom'], [1.6, 'pop']);
    const f = frase(s.frase, t, 1.5, 'left:64px;right:64px;top:790px;position:absolute');
    return `<div class="abs" style="left:64px;top:310px;transform-origin:0 100%"><span class="cxa" data-fit="${Math.min(560, 150 * s.l1.length + 80)}" data-max="230" style="--r0:-14deg;--r:-3deg;background:${t.cx[0]};color:${t.cx[1]};${an('pop', .6, .3, BACK)}">${esc(s.l1)}</span></div>
     <div class="abs" style="left:64px;top:520px"><span class="cxa" data-fit="${Math.min(940, 150 * s.l2.length + 80)}" data-max="230" style="--r0:10deg;--r:2deg;background:${t.cx[2]};color:${t.cx[3]};${an('pop', .6, .58, BACK)}">${esc(s.l2)}</span></div>${f.html}`; },
  // letra: saudação manuscrita que se escreve (máscara da esquerda para a direita) + linha em caixa alta que fecha o espaçamento
  letra: (s, t, c) => { c.push([.3, 'whoosh'], [1.2, 'chime'], [1.9, 'pop']);
    const f = frase(s.frase, t, 1.9, 'left:64px;right:64px;top:800px;position:absolute;text-align:center');
    return `<div class="abs kau" data-fit="900" data-max="250" data-centro="1" style="left:64px;top:320px;color:${t.ac};transform:rotate(-5deg);transform-origin:50% 60%"><span style="display:inline-block;padding:0 .12em .1em 0;${an('abre', 1.1, .3, 'cubic-bezier(.65,0,.35,1)')}">${esc(s.l1)}</span></div>
     <div class="abs ant" style="left:0;right:0;top:610px;text-align:center;font-size:150px;color:${t.tx};${an('surge', .7, 1.0)}">${esc(s.l2)}</div>${f.html}`; },
  // eco: palavra gigante cheia + 3 ecos em contorno que descem por trás do Leo
  eco: (s, t, c) => { c.push([.25, 'boom'], [.55, 'whoosh'], [.75, 'whoosh'], [.95, 'whoosh'], [1.7, 'pop']);
    const f = frase(s.frase, t, 1.6, 'left:64px;right:64px;top:300px;position:absolute');
    const linha = (i) => `<div class="mk" style="left:0;top:${440 + i * 235}px;width:1080px;height:250px;z-index:1"><div class="ant abs" data-fit="952" data-max="250" style="left:64px;${i ? `color:transparent;-webkit-text-stroke:3px ${t.ac};--o:${[1, .7, .42, .22][i]};${an('eco', .7, .4 + i * .2)}` : `color:${t.ac};${an('sobe', .7, .25)}`}">${esc(s.l1)}</div></div>`;
    return f.html + [0, 1, 2, 3].map(linha).join(''); },
};
function pagina(s) {
  { const png = fs.readFileSync(path.join(A, 'hd', s.foto + '.png')), pw = png.readUInt32BE(16), ph = png.readUInt32BE(20), top = s.top ?? 960;
    const w0 = s.w; if (s.sangra) s.w = Math.max(s.w, Math.ceil((1950 - top) * pw / ph)); s.x = Math.round(s.x - (s.w - w0) / 2); }
  const t = TEMA[s.tema], cues = [], corpo = TIPO[s.tipo](s, t, cues), [mx, my, mw, mr] = s.mapa;
  const ent = { sobe: 'fSobe', esq: 'fEsq', dir: 'fDir', zoom: 'fZoom' }[s.entra]; cues.push([.05, 'whooshL'], [2.6, 'chime']);
  const logo = b64(path.join(A, t.claro ? 'logo-marinho.png' : 'logo.png'), 'png');
  const html = `<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Anton&family=Kaushan+Script&family=Montserrat:wght@600;700;800;900&display=swap" rel="stylesheet"><style>${css}</style></head><body>
  <div class="a" style="background:${t.bg}">
   <svg class="abs" viewBox="0 0 ${MAPA.w} ${MAPA.h}" style="left:${mx}px;top:${my}px;width:${mw}px;--mr:${mr}deg;--dx:${mx < 300 ? 28 : -28}px;overflow:visible;animation:deriva 8s linear 0s both">
     <polygon points="${MAPA.pts}" pathLength="1" fill="${t.mapa}" stroke="${t.mapa.replace(/[\d.]+\)$/, '.55)')}" stroke-width="3" stroke-dasharray="1" style="animation:traca 2.2s cubic-bezier(.65,0,.35,1) .1s both,enche 1.2s ease 1.6s both"/></svg>
   <div class="luz" style="animation:varre 3.4s cubic-bezier(.45,0,.55,1) .1s both"></div>
   ${corpo}
   <div class="abs" style="left:${s.x}px;top:${s.top ?? 960}px;width:${s.w}px;z-index:2;animation:${ent} 1.1s ${EXPO} 0s both"><div style="transform-origin:50% 100%;animation:flutua 8s linear 0s both">
     <img src="${b64(path.join(A, 'hd', s.foto + '.png'), 'png')}" style="display:block;width:100%;${s.flip ? 'transform:scaleX(-1);' : ''}${s.solto ? '-webkit-mask-image:linear-gradient(180deg,#000 62%,transparent 96%);mask-image:linear-gradient(180deg,#000 62%,transparent 96%);' : ''}filter:drop-shadow(0 30px 60px rgba(${t.base},.55)) saturate(1.06) contrast(1.03)"></div></div>
   <div class="abs" style="left:0;right:0;bottom:0;height:520px;z-index:3;background:linear-gradient(180deg,rgba(${t.base},0) 0,rgba(${t.base},.82) 58%,rgba(${t.base},.96) 100%)"></div>
   <div class="abs" style="left:64px;top:150px;z-index:5;${an('desce', .6, .15)}"><div class="pill" style="background:${t.claro ? 'rgba(8,32,99,.08)' : 'rgba(255,255,255,.14)'};border:1.5px solid ${t.claro ? 'rgba(8,32,99,.22)' : 'rgba(255,255,255,.3)'};color:${t.tx}"><img src="${b64(path.join(A, 'avatar.jpg'), 'jpeg')}">@_leonardopinto</div></div>
   <div class="abs rot" style="left:64px;top:246px;z-index:5;color:${t.tx};opacity:.9;font-size:${s.rot.length > 22 ? 20 : 24}px;animation:larga .9s ${EXPO} .35s both">${esc(s.rot)}</div>
   <div class="abs" style="left:64px;bottom:170px;z-index:6;width:190px;${an('surge', .7, 2.5)}"><img src="${logo}" style="width:100%;display:block;filter:drop-shadow(0 10px 22px rgba(0,0,0,.3));animation:pulsa 2.4s ease-in-out 3.4s infinite"></div>
   <div class="abs" style="right:64px;bottom:184px;z-index:6;text-align:right;${an('surge', .7, 2.8)}"><div class="kau" style="font-size:46px;color:${t.claro ? '#082063' : '#FFC20E'};animation:respira 3s ease-in-out 3.6s infinite">Conte sempre comigo.</div>
     <div style="font:700 18px Montserrat;letter-spacing:.2em;color:${t.claro ? '#082063' : '#fff'};opacity:.85;margin-top:4px">VEREADOR · SÃO JOÃO BATISTA</div></div>
   <div class="grao"></div>
  </div></body></html>`;
  return { html, cues };
}
(async () => {
  fs.mkdirSync(OUT, { recursive: true });
  const b = await chromium.launch(), pg = await b.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
  for (const s of S) {
    if (SO && !s.id.startsWith(SO)) continue;
    const { html, cues } = pagina(s);
    await pg.setContent(html, { waitUntil: 'networkidle' });
    await pg.evaluate(async () => { await document.fonts.ready;
      for (const f of ['400 100px Anton', '400 100px "Kaushan Script"', '900 100px Montserrat', '700 40px Montserrat']) await document.fonts.load(f);
      // ajusta cada linha à largura pedida (data-fit), com teto de altura (data-max)
      for (const e of document.querySelectorAll('[data-fit]')) { const W = +e.dataset.fit, M = +e.dataset.max;
        if (getComputedStyle(e).display === 'block') e.style.display = 'inline-block';
        e.style.fontSize = '100px'; const w = e.offsetWidth, h = e.offsetHeight;
        e.style.fontSize = Math.min(100 * W / w, 100 * M / h) + 'px';
        if (e.dataset.centro) { e.style.left = '0'; e.style.right = '0'; e.style.textAlign = 'center'; e.style.display = 'block'; } }
      document.getAnimations().forEach(a => a.pause()); });
    fs.writeFileSync(path.join(OUT, s.id + '.cues.json'), JSON.stringify({ tema: s.tema, cues: cues.sort((x, y) => x[0] - y[0]) }));
    const mudo = path.join(OUT, s.id + '.mudo.mp4');
    const ff = spawn('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(FPS), '-c:v', 'mjpeg', '-i', '-', '-c:v', 'libx264', '-preset', 'slow', '-crf', '15', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', mudo], { stdio: ['pipe', 'inherit', 'inherit'] });
    for (let f = 0; f < FPS * DUR; f++) {
      await pg.evaluate(ms => { document.getAnimations().forEach(a => { a.currentTime = ms; }); }, f * 1000 / FPS);
      const buf = await pg.locator('.a').screenshot({ type: 'jpeg', quality: 95 });
      if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
      if (f === 200) fs.writeFileSync(path.join(OUT, s.id + '.jpg'), buf);  // quadro final para a folha de contato e a capa
    }
    ff.stdin.end(); await new Promise(r => ff.on('close', r)); console.log(mudo);
  }
  await b.close();
})();
