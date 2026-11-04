// Motion v1 do Leo Pinto · motor de animação determinístico (conta Pedro, 04/11/2026).
// Tudo sai de render(t): nenhum CSS transition, timer ou requestAnimationFrame. O render.js chama render(t) quadro a quadro.
// Um vídeo = VIDEO {id, shots:[...]} definido em vN.js. Cada shot tem t0/t1 (segundos absolutos), pre/post (sobreposição
// para transição), cam (trilhas do quadro inteiro: whip pan, zoom) e layers (camadas com trilhas de keyframes).
'use strict';
const W = 1080, H = 1920, FPS = 30;
const C = { roy: '#2350F5', mar: '#082063', nav: '#05316E', sol: '#FFC20E', lar: '#FF7A1A', bra: '#FFFFFF', cla: '#8CC0FF' };
const A = new URLSearchParams(location.search).get('a') || '../assets';   // pasta de assets (fora do Git)

// ---------- easing ----------
const c1 = 1.70158, c3 = c1 + 1;
const EASE = {
  lin: t => t,
  inQ: t => t * t, outQ: t => 1 - (1 - t) * (1 - t), ioQ: t => t < .5 ? 2 * t * t : 1 - (-2 * t + 2) ** 2 / 2,
  inC: t => t ** 3, outC: t => 1 - (1 - t) ** 3, ioC: t => t < .5 ? 4 * t ** 3 : 1 - (-2 * t + 2) ** 3 / 2,
  inE: t => t <= 0 ? 0 : 2 ** (10 * t - 10), outE: t => t >= 1 ? 1 : 1 - 2 ** (-10 * t),
  ioE: t => t <= 0 ? 0 : t >= 1 ? 1 : t < .5 ? 2 ** (20 * t - 10) / 2 : (2 - 2 ** (-20 * t + 10)) / 2,
  outB: t => 1 + c3 * (t - 1) ** 3 + c1 * (t - 1) ** 2, inB: t => c3 * t ** 3 - c1 * t * t,
  hold: t => t >= 1 ? 1 : 0,
  outBo: t => { const n = 7.5625, d = 2.75; if (t < 1 / d) return n * t * t; if (t < 2 / d) return n * (t -= 1.5 / d) * t + .75; if (t < 2.5 / d) return n * (t -= 2.25 / d) * t + .9375; return n * (t -= 2.625 / d) * t + .984375; },
};
const clamp = (v, a = 0, b = 1) => Math.max(a, Math.min(b, v));
const hex = s => [1, 3, 5].map(i => parseInt(s.slice(i, i + 2), 16));
function mix(a, b, k) {
  if (typeof a === 'number') return a + (b - a) * k;
  if (typeof a === 'string') { const x = hex(a), y = hex(b); return 'rgb(' + x.map((v, i) => Math.round(v + (y[i] - v) * k)).join(',') + ')'; }
  return a.map((v, i) => v + (b[i] - v) * k);
}
// trilha = [[t, valor, easing-do-trecho-que-chega], ...]
function val(tr, t) {
  if (!tr || !tr.length) return undefined;
  if (t <= tr[0][0]) return tr[0][1];
  for (let i = 1; i < tr.length; i++) {
    const [ta, va] = tr[i - 1], [tb, vb, e] = tr[i];
    if (t < tb) { const k = (EASE[e || 'ioC'])((t - ta) / (tb - ta)); return mix(va, vb, k); }
  }
  return tr[tr.length - 1][1];
}

// ---------- ajudantes de trilha (usados nos arquivos vN.js) ----------
const H_ = {
  pop: (t, d = .34, o = 1.1) => ({ s: [[t, 0], [t + d * .62, o, 'outC'], [t + d, 1, 'ioQ']], o: [[t, 0], [t + .05, 1, 'lin']] }),
  fade: (a, b, d = .3) => ({ o: [[a, 0], [a + d, 1, 'outQ'], [b - d, 1], [b, 0, 'inQ']] }),
  inOut: (a, b, d = .3) => [[a, 0], [a + d, 1, 'outQ'], [b - d, 1], [b, 0, 'inQ']],
  // wipe com clip-path inset [cima, direita, baixo, esquerda] em %
  wipe: (dir, t, d = .5, e = 'ioE') => {
    const from = { l: [0, 100, 0, 0], r: [0, 0, 0, 100], u: [0, 0, 100, 0], d: [100, 0, 0, 0] }[dir];
    return [[t, from], [t + d, [-12, -2, -12, -2], e]];   // fim levemente negativo: acentos (Ã, Ê) não são cortados
  },
  wipeOut: (dir, t, d = .45, e = 'ioE') => {
    const to = { l: [0, 100, 0, 0], r: [0, 0, 0, 100], u: [0, 0, 100, 0], d: [100, 0, 0, 0] }[dir];
    return [[t, [0, 0, 0, 0]], [t + d, to, e]];
  },
  merge: (...xs) => Object.assign({}, ...xs),
  // n palavras saltando (0 → 110 → 100%) uma depois da outra
  words: (lines, t0, step = .14, d = .34) => lines.join(' ').split(' ').map((w, i) => H_.pop(t0 + i * step, d)),
  nWords: lines => lines.join(' ').split(' ').length,
  // área segura (texto entre y 250 e 1600) com filhos empilhados e centralizados na vertical
  area: (kids, o = {}) => Object.assign({ css: Object.assign({ left: '90px', top: (o.y0 ?? 250) + 'px', width: '900px', height: ((o.y1 ?? 1600) - (o.y0 ?? 250)) + 'px', display: 'flex', flexDirection: 'column', justifyContent: o.justify || 'center', alignItems: o.align || 'center' }, o.css || {}), kids }, o.tr ? { tr: o.tr } : {}),
  // bloco de linhas empilhadas, cada linha ajustada à largura w (teto max), no fluxo da área
  blk: (lines, o = {}) => Object.assign({ lines, fit: { w: o.w || 900, max: o.max || 170 }, cls: o.cls || 'B', css: Object.assign({ position: 'relative', width: (o.w || 900) + 'px' }, o.css || {}) }, o.extra || {}),
};
const BG = 'radial-gradient(1500px 1300px at 560px 760px,#4A78FF 0,#2E5BFA 24%,#2350F5 42%,#1539BE 66%,#0B2A8A 86%,#082063 100%)';

// ---------- montagem do DOM ----------
let STAGE, SVGDEFS, LAYERS = [], SHOTS = [], GRAIN, LIGHT, mbN = 0, META = window.META || {};
function el(tag, cls, css, html) { const e = document.createElement(tag); if (cls) e.className = cls; if (css) Object.assign(e.style, css); if (html != null) e.innerHTML = html; return e; }
function mbFilter() {
  const id = 'mb' + (mbN++);
  const f = document.createElementNS('http://www.w3.org/2000/svg', 'filter');
  f.setAttribute('id', id); f.setAttribute('x', '-50%'); f.setAttribute('y', '-50%'); f.setAttribute('width', '200%'); f.setAttribute('height', '200%');
  f.setAttribute('color-interpolation-filters', 'sRGB');
  const g = document.createElementNS('http://www.w3.org/2000/svg', 'feGaussianBlur'); g.setAttribute('stdDeviation', '0 0'); f.appendChild(g); SVGDEFS.appendChild(f);
  return { id, g };
}
// texto com marcação: *amarelo*  ^degradê amarelo→laranja^  _laranja_  ~branco~  [royal]  §marinho§  {O} = letra do zoom-through
function mark(s) {
  return s.replace(/\*([^*]+)\*/g, '<span class="y">$1</span>').replace(/\^([^^]+)\^/g, '<span class="g">$1</span>')
    .replace(/_([^_]+)_/g, '<span class="o">$1</span>').replace(/~([^~]+)~/g, '<span class="w">$1</span>').replace(/\[([^\]]+)\]/g, '<span class="r">$1</span>').replace(/\{O\}/g, '<span class="zo">O</span>').replace(/§([^§]+)§/g, '<span class="m">$1</span>');
}
function mapSVG(o) {
  const M = window.MAPA; const w = o.w || 900, k = w / M.w, h = M.h * k;
  const sw = (o.sw || 6) / k;
  let s = `<svg width="${w}" height="${h}" viewBox="-20 -20 ${M.w + 40} ${M.h + 40}" style="overflow:visible;display:block">
  <defs><linearGradient id="mg${o.id}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#8CC0FF" stop-opacity=".55"/><stop offset="1" stop-color="#5A86FF" stop-opacity=".22"/></linearGradient></defs>`;
  if (o.echo) s += `<polygon class="echo" points="${M.pts}" transform="translate(26,22)" fill="none" stroke="${o.echoColor || '#9CC4FF'}" stroke-opacity=".38" stroke-width="${sw * .7}" stroke-linejoin="round"/>`;
  s += `<polygon class="fill" points="${M.pts}" fill="url(#mg${o.id})" stroke="none"/>`;
  s += `<polygon class="line" points="${M.pts}" fill="none" stroke="${o.stroke || C.sol}" stroke-width="${sw}" stroke-linejoin="round" stroke-linecap="round"/>`;
  return s + '</svg>';
}
function photoBox(L) {
  // posiciona o recorte pelo rosto: face = {cx, cy, w} em px do palco (centro do rosto e largura do rosto)
  const m = META[L.src]; if (!m) throw new Error('sem META para ' + L.src);
  const k = L.face.w / m.fw, w = m.W * k, h = m.H * k;
  const left = L.face.cx - (m.fx + m.fw / 2) * k, top = L.face.cy - (m.fy + m.fh / 2) * k;
  return { left, top, w, h, k, m };
}
function build(V) {
  STAGE = document.getElementById('stage');
  SVGDEFS = document.querySelector('#defs defs');
  LIGHT = document.getElementById('light'); GRAIN = document.getElementById('grain');
  for (const sh of V.shots) {
    const root = el('div', 'S'); if (sh.bg) root.style.background = sh.bg;
    STAGE.insertBefore(root, GRAIN.previousElementSibling ? GRAIN : GRAIN);
    const S = { def: sh, root, layers: [], mb: null }; SHOTS.push(S);
    for (const L of sh.layers) S.layers.push(makeLayer(L, root));
  }
}
function makeLayer(L, parent) {
  const d = el('div', 'L ' + (L.cls || ''), L.css || {});
  if (L.k === 'photo') {
    const b = photoBox(L);
    Object.assign(d.style, { left: b.left + 'px', top: b.top + 'px', width: b.w + 'px', height: b.h + 'px', transformOrigin: `${L.face.cx - b.left}px ${L.face.cy - b.top}px` });
    const fadeB = L.fade == null ? 7 : L.fade;
    const im = el('img', '', { width: '100%', height: '100%', display: 'block' }); im.src = `${A}/recortes/${L.src}.png`;
    // a borda inferior da foto nunca aparece: degradê para transparente nos últimos %
    // e se o recorte toca a lateral da foto original (ombro cortado), essa lateral também some num degradê
    const mks = [`linear-gradient(180deg,#000 ${100 - fadeB}%,transparent 100%)`];
    if (b.m.edge.r) mks.push(`linear-gradient(90deg,#000 ${100 - (L.fadeR || 9)}%,transparent 100%)`);
    if (b.m.edge.l) mks.push(`linear-gradient(270deg,#000 ${100 - (L.fadeL || 9)}%,transparent 100%)`);
    im.style.webkitMaskImage = mks.join(','); im.style.maskImage = mks.join(',');
    if (mks.length > 1) { im.style.webkitMaskComposite = 'source-in'; im.style.maskComposite = 'intersect'; }
    if (L.shadow !== false) d.style.filter = 'drop-shadow(0 30px 40px rgba(2,12,50,.45))';
    d.appendChild(im); L._box = b;
  } else if (L.k === 'img') {
    const im = el('img', '', Object.assign({ display: 'block', width: '100%' }, L.imgCss || {})); im.src = L.src.startsWith('@') ? `${A}/${L.src.slice(1)}` : L.src; d.appendChild(im);
  } else if (L.k === 'map') {
    d.innerHTML = mapSVG(L); L._line = d.querySelector('.line'); L._fill = d.querySelector('.fill'); L._echo = d.querySelector('.echo');
  } else if (L.lines) {
    // linhas empilhadas; cada palavra vira uma "parte" com trilhas próprias
    d.classList.add('stack');
    L._parts = [];
    L.lines.forEach((ln, li) => {
      const row = el('div', 'row', Object.assign({}, (L.rowCss && L.rowCss[li]) || {}));
      const words = (L.words === false) ? [ln] : ln.split(' ');
      words.forEach((w, wi) => {
        const sp = el('span', 'p', {}, mark(w)); row.appendChild(sp);
        if (wi < words.length - 1) row.appendChild(document.createTextNode(' '));
        L._parts.push(sp);
      });
      d.appendChild(row);
    });
  } else if (L.html != null) d.innerHTML = mark(L.html);
  parent.appendChild(d);
  const o = { L, d, base: d.style.filter || '', mb: null, kids: [], last: {} };
  if (L.kids) for (const K of L.kids) o.kids.push(makeLayer(K, d));
  return o;
}
// ajusta cada linha de um bloco empilhado para a mesma largura (frase empilhada), com teto de tamanho
function fitAll() {
  for (const S of SHOTS) for (const o of S.layers) fitLayer(o);
}
function fitLayer(o) {
  const L = o.L;
  if (L.fit && L.lines) {
    const rows = o.d.querySelectorAll(':scope > .row');
    rows.forEach((r, i) => {
      const max = Array.isArray(L.fit.max) ? L.fit.max[i] : L.fit.max;
      r.style.fontSize = '100px'; r.style.display = 'inline-block'; r.style.whiteSpace = 'nowrap';
      const w = r.scrollWidth; let fs = 100 * L.fit.w / w; if (max) fs = Math.min(fs, max);
      r.style.fontSize = fs.toFixed(1) + 'px'; r.style.display = 'block';
    });
  }
  if (L.zo) {   // origem do zoom-through no centro da letra marcada {O}
    const z = o.d.querySelector('.zo'), a = o.d.getBoundingClientRect(), b = z.getBoundingClientRect();
    const ox = b.left + b.width / 2 - a.left, oy = b.top + b.height * (L.zoY || .5) - a.top;
    o.d.style.transformOrigin = `${ox.toFixed(1)}px ${oy.toFixed(1)}px`;
    o.zoD = [W / 2 - (a.left + ox), H / 2 - (a.top + oy)];   // quanto falta para a letra chegar ao centro da tela (trilha zc 0→1)
  }
  for (const k of o.kids) fitLayer(k);
}

// ---------- aplicar estado ----------
function apply(o, t) {
  const L = o.L, tr = L.tr || {}, d = o.d;
  let vis = true; if (L.on) vis = t >= L.on[0] && t < L.on[1];
  const op = tr.o ? val(tr.o, t) : 1;
  if (!vis || op <= 0.001) { if (o.last.v !== 0) { d.style.visibility = 'hidden'; o.last.v = 0; } return; }
  if (o.last.v !== 1) { d.style.visibility = 'visible'; o.last.v = 1; }
  d.style.opacity = op;
  let x = val(tr.x, t) || 0, y = val(tr.y, t) || 0; const s = val(tr.s, t), sx = val(tr.sx, t), sy = val(tr.sy, t), r = val(tr.r, t) || 0, sk = val(tr.sk, t) || 0;
  if (o.zoD && tr.zc) { const k = val(tr.zc, t); x += o.zoD[0] * k; y += o.zoD[1] * k; }
  let T = `translate3d(${x.toFixed(2)}px,${y.toFixed(2)}px,0)`;
  if (r) T += ` rotate(${r}deg)`; if (sk) T += ` skewX(${sk}deg)`;
  const S1 = s == null ? 1 : s; T += ` scale(${(S1 * (sx == null ? 1 : sx)).toFixed(4)},${(S1 * (sy == null ? 1 : sy)).toFixed(4)})`;
  d.style.transform = T;
  if (tr.w) d.style.width = val(tr.w, t) + 'px';
  if (tr.h) d.style.height = val(tr.h, t) + 'px';
  if (tr.l) d.style.left = val(tr.l, t) + 'px';
  if (tr.tp) d.style.top = val(tr.tp, t) + 'px';
  if (tr.rad) d.style.borderRadius = val(tr.rad, t) + 'px';
  if (tr.bg) d.style.background = val(tr.bg, t);
  if (tr.col) d.style.color = val(tr.col, t);
  if (tr.ls) d.style.letterSpacing = val(tr.ls, t) + 'em';
  if (tr.clip) { const c = val(tr.clip, t); d.style.clipPath = `inset(${c.map(v => v.toFixed(2) + '%').join(' ')})`; }
  if (tr.poly) { const p = val(tr.poly, t); let q = []; for (let i = 0; i < p.length; i += 2) q.push(`${p[i].toFixed(2)}% ${p[i + 1].toFixed(2)}%`); d.style.clipPath = `polygon(${q.join(',')})`; }
  // filtros: desfoque direcional (whip pan) + desfoque comum + filtro base (sombra)
  let F = '';
  const mbx = val(tr.mbx, t) || 0, mby = val(tr.mby, t) || 0;
  if (mbx > .3 || mby > .3) { if (!o.mb) o.mb = mbFilter(); o.mb.g.setAttribute('stdDeviation', `${mbx.toFixed(1)} ${mby.toFixed(1)}`); F += `url(#${o.mb.id}) `; }
  const bl = val(tr.blur, t) || 0; if (bl > .2) F += `blur(${bl.toFixed(1)}px) `;
  F += o.base; d.style.filter = F.trim() || 'none';
  // conteúdo dinâmico
  if (L.k === 'map') {
    const dr = clamp(val(tr.dash, t) ?? 1);
    if (o.len == null) { o.len = L._line.getTotalLength(); L._line.style.strokeDasharray = o.len; if (L._echo) L._echo.style.strokeDasharray = o.len; }
    L._line.style.strokeDashoffset = o.len * (1 - dr);
    const ed = clamp(val(tr.echoDash, t) ?? dr); if (L._echo) L._echo.style.strokeDashoffset = o.len * (1 - ed);
    L._fill.style.opacity = clamp(val(tr.fill, t) ?? 1);
    L._line.style.opacity = dr <= .002 ? 0 : clamp(val(tr.lineO, t) ?? 1);   // sem ponto solto antes do traço começar
    if (L._echo) L._echo.style.opacity = ed <= .002 ? 0 : 1;
  }
  if (L.count) {           // contador: {tr:[[t,v,e]], pad} dígitos em caixas de largura fixa
    const v = Math.round(val(L.count, t)); if (o.last.c !== v) { o.last.c = v; d.innerHTML = String(v).split('').map(c => `<span class="dg">${c}</span>`).join(''); }
  }
  if (L.type) {            // máquina de escrever: {text, t0, t1, cursor}
    const tx = L.type.text, n = Math.round(clamp((t - L.type.t0) / (L.type.t1 - L.type.t0)) * tx.length);
    const blinkOn = (t < L.type.t1 + .05) || (Math.floor((t - L.type.t1) / .45) % 2 === 0);
    const cur = (L.type.cursor !== false && t < (L.type.hide ?? 99)) ? `<span class="cur" style="opacity:${blinkOn ? 1 : 0}"></span>` : '';
    const key = n + '|' + cur; if (o.last.ty !== key) { o.last.ty = key; d.innerHTML = tx.slice(0, n).replace(/\n/g, '<br>') + cur + `<span style="visibility:hidden">${tx.slice(n).replace(/\n/g, '<br>')}</span>`; }
  }
  if (L.parts && L._parts) L.parts.forEach((ptr, i) => { const sp = L._parts[i]; if (!sp || !ptr) return; applyPart(sp, ptr, t); });
  for (const k of o.kids) apply(k, t);
}
function applyPart(sp, tr, t) {
  const op = tr.o ? val(tr.o, t) : 1; sp.style.opacity = op;
  let x = val(tr.x, t) || 0, y = val(tr.y, t) || 0; const s = val(tr.s, t) ?? 1, r = val(tr.r, t) || 0;
  sp.style.transform = `translate(${x.toFixed(2)}px,${y.toFixed(2)}px) rotate(${r}deg) scale(${s.toFixed(4)})`;
  if (tr.bg) sp.style.background = val(tr.bg, t);
  if (tr.col) sp.style.color = val(tr.col, t);
  if (tr.clip) { const c = val(tr.clip, t); sp.style.clipPath = `inset(${c.map(v => v.toFixed(2) + '%').join(' ')})`; }
  const bl = val(tr.blur, t) || 0; sp.style.filter = bl > .2 ? `blur(${bl.toFixed(1)}px)` : 'none';
}

function render(t) {
  const V = window.VIDEO;
  // fundo: luz diagonal suave que respira devagar; granulação de 10% que muda a cada 2 quadros
  const f = Math.round(t * FPS);
  LIGHT.style.transform = `translate(${(Math.sin(t * .35) * 60).toFixed(1)}px,${(Math.cos(t * .27) * 80).toFixed(1)}px)`;
  const g = Math.floor(f / 2); GRAIN.style.backgroundPosition = `${(g * 73) % 300}px ${(g * 151) % 300}px`;
  for (const S of SHOTS) {
    const sh = S.def, lt = t - sh.t0, pre = sh.pre || 0, post = sh.post || 0;
    const on = t >= sh.t0 - pre && t < sh.t1 + post && !(t >= 40 && sh.t1 < 40);
    if (!on) { if (S.vis !== 0) { S.root.style.display = 'none'; S.vis = 0; } continue; }
    if (S.vis !== 1) { S.root.style.display = 'block'; S.vis = 1; }
    const cam = sh.cam || {};
    const x = val(cam.x, lt) || 0, y = val(cam.y, lt) || 0, s = val(cam.s, lt) ?? 1, r = val(cam.r, lt) || 0;
    S.root.style.transform = `translate3d(${x.toFixed(2)}px,${y.toFixed(2)}px,0) rotate(${r}deg) scale(${s.toFixed(4)})`;
    S.root.style.opacity = cam.o ? val(cam.o, lt) : 1;
    if (cam.clip) { const c = val(cam.clip, lt); S.root.style.clipPath = `inset(${c.map(v => v.toFixed(2) + '%').join(' ')})`; }
    if (cam.poly) { const p = val(cam.poly, lt); let q = []; for (let i = 0; i < p.length; i += 2) q.push(`${p[i]}% ${p[i + 1]}%`); S.root.style.clipPath = `polygon(${q.join(',')})`; }
    const mbx = val(cam.mbx, lt) || 0, mby = val(cam.mby, lt) || 0, bl = val(cam.blur, lt) || 0;
    let F = '';
    if (mbx > .3 || mby > .3) { if (!S.mb) S.mb = mbFilter(); S.mb.g.setAttribute('stdDeviation', `${mbx.toFixed(1)} ${mby.toFixed(1)}`); F += `url(#${S.mb.id}) `; }
    if (bl > .2) F += `blur(${bl.toFixed(1)}px)`;
    S.root.style.filter = F.trim() || 'none';
    for (const o of S.layers) apply(o, lt);
  }
}
window.render = render;

// ---------- carregamento ----------
function loadScript(src) { return new Promise((ok, err) => { const s = document.createElement('script'); s.src = src; s.onload = ok; s.onerror = () => err(new Error('falhou ' + src)); document.head.appendChild(s); }); }
window.READY = (async () => {
  const q = new URLSearchParams(location.search), v = q.get('v') || 'v1';
  await loadScript(`${A}/meta.js`); META = window.META;
  await loadScript('mapa.js');
  await loadScript(`${v}.js`);
  build(window.VIDEO);
  await document.fonts.ready;
  await Promise.all([...document.images].map(i => i.decode().catch(e => { throw new Error('imagem ' + i.src); })));
  fitAll();
  render(+(q.get('t') || 0));
  return { shots: window.VIDEO.shots.map(s => [s.t0, s.t1, s.n]) };
})();
