// Perfil do @curso_processo_legislativo_ na identidade Hemiciclo Premium (conta Leandro, 08/11/2026): foto de perfil com os dois professores e capas dos destaques.
// Foto de perfil tem rosto: sai em SAIDA_PRIVADA (fora do Git). Capas sem rosto: aqui.
const { chromium } = require('playwright'), path = require('path'), fs = require('fs');
const SOC = process.env.SOCIOS || '/home/user/centrallindsonalmeida/dados/clientes-arquivos/curso/socios';
const PRIV = process.env.SAIDA_PRIVADA || '/home/user/centrallindsonalmeida/dados/clientes-arquivos/curso/instagram-perfil';
fs.mkdirSync(PRIV, { recursive: true });
const img = f => 'data:image/png;base64,' + fs.readFileSync(path.join(SOC, f)).toString('base64');
const C = { v: '#0A1F17', v2: '#123528', cr: '#EFE6D4', la: '#C8A96B', la2: '#E6CF9C' };
const arcos = (cx, cy, r0, n, gap, op, w = 1.6, pr = 2.6) => { let s = ''; for (let i = 0; i < n; i++) { const r = r0 + i * gap;
  s += `<path d="M ${cx - r} ${cy} A ${r} ${r} 0 0 1 ${cx + r} ${cy}" fill="none" stroke="${C.la}" stroke-opacity="${op * (1 - i / (n + 2))}" stroke-width="${w}"/>`;
  const k = 9 + i * 3; for (let j = 1; j < k; j++) { const a = Math.PI - Math.PI * j / k; s += `<circle cx="${cx + r * Math.cos(a)}" cy="${cy - r * Math.sin(a)}" r="${pr}" fill="${C.la}" fill-opacity="${op * .9 * (1 - i / (n + 2))}"/>`; } } return s; };
const css = `*{margin:0;padding:0;box-sizing:border-box}html,body{background:#000}.a{position:relative;overflow:hidden;background:radial-gradient(ellipse at 50% 35%,${C.v2},${C.v} 70%)}.abs{position:absolute}
.grao{position:absolute;inset:0;opacity:.10;mix-blend-mode:overlay;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='220' height='220'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='3'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E")}
.pes{filter:drop-shadow(0 24px 30px rgba(0,0,0,.55)) saturate(.92) contrast(1.06) sepia(.12)}`;
// ícones de traço fino em latão (sem balança nem martelo)
const IC = {
  curso: '<path d="M30 70 A40 40 0 0 1 110 70" /><path d="M48 70 A22 22 0 0 1 92 70"/><text x="70" y="64" text-anchor="middle" font-family="Instrument Serif" font-style="italic" font-size="44" fill="#C8A96B" stroke="none">§</text><path d="M20 88h100"/>',
  grade: '<rect x="28" y="22" width="84" height="96" rx="8"/><path d="M44 46h52M44 64h52M44 82h52M44 100h30"/>',
  professores: '<circle cx="50" cy="48" r="16"/><circle cx="92" cy="52" r="13"/><path d="M22 112c4-22 18-34 28-34s24 12 28 34M74 112c3-16 11-26 18-26s16 10 20 26"/>',
  turmas: '<rect x="22" y="30" width="96" height="84" rx="10"/><path d="M22 54h96M48 20v20M92 20v20"/><circle cx="52" cy="80" r="5" fill="#C8A96B"/><circle cx="72" cy="80" r="5" fill="#C8A96B"/><circle cx="92" cy="80" r="5" fill="#C8A96B" fill-opacity=".4"/>',
  duvidas: '<path d="M30 30h80a10 10 0 0 1 10 10v44a10 10 0 0 1-10 10H62l-22 18v-18H30a10 10 0 0 1-10-10V40a10 10 0 0 1 10-10z"/><text x="70" y="78" text-anchor="middle" font-family="Instrument Serif" font-style="italic" font-size="46" fill="#C8A96B" stroke="none">?</text>',
  contato: '<path d="M26 40h88v60H26z"/><path d="M26 40l44 34 44-34"/>',
};
const CAPAS = [['01-curso', 'curso', 'Curso'], ['02-grade', 'grade', 'Grade'], ['03-professores', 'professores', 'Professores'], ['04-turmas', 'turmas', 'Turmas'], ['05-duvidas', 'duvidas', 'Dúvidas'], ['06-contato', 'contato', 'Contato']];
const P = {};
P[path.join(PRIV, 'foto-perfil.png')] = [1080, 1080, `<div class="a" style="width:1080px;height:1080px">
  <svg class="abs" style="left:0;top:0" width="1080" height="1080">${arcos(540, 1080, 260, 7, 62, .55, 2.2, 3.6)}</svg>
  <img class="abs pes" src="${img('cut-rafael-araujo-veras/recorte-limpo.png')}" style="left:520px;top:205px;height:900px">
  <img class="abs pes" src="${img('cut-tiago-azevedo/recorte-limpo.png')}" style="left:95px;top:190px;height:930px">
  <div class="abs" style="left:0;right:0;bottom:0;height:160px;background:linear-gradient(180deg,transparent,${C.v})"></div><div class="grao"></div></div>`];
for (const [arq, ic, nome] of CAPAS) P[path.join(__dirname, `destaque-${arq}.png`)] = [1080, 1920, `<div class="a" style="width:1080px;height:1920px">
  <svg class="abs" style="left:0;top:0" width="1080" height="1920">${arcos(540, 1300, 300, 6, 60, .35)}</svg>
  <div class="abs" style="left:290px;top:710px;width:500px;height:500px;border-radius:50%;border:2px solid rgba(200,169,107,.55);display:flex;align-items:center;justify-content:center">
    <svg width="300" height="300" viewBox="0 0 140 140" fill="none" stroke="${C.la}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round">${IC[ic]}</svg></div>
  <div class="grao"></div></div>`];
(async () => {
  const b = await chromium.launch(); const p = await b.newPage();
  for (const [out, [w, h, html]] of Object.entries(P)) {
    await p.setViewportSize({ width: w, height: h });
    await p.setContent(`<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@600;700;800&family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet"><style>${css}</style></head><body>${html}</body></html>`, { waitUntil: 'networkidle' });
    await p.waitForTimeout(500); await p.screenshot({ path: out }); console.log('ok', path.basename(out));
  }
  // prévia: perfil no círculo + destaques
  await p.setViewportSize({ width: 1080, height: 700 });
  const u = f => 'data:image/png;base64,' + fs.readFileSync(f).toString('base64');
  const caps = CAPAS.map(([a, , n]) => `<div style="text-align:center;width:150px"><div style="width:130px;height:130px;border-radius:50%;margin:0 auto;padding:4px;border:2px solid #444"><div style="width:100%;height:100%;border-radius:50%;background:url(${u(path.join(__dirname, 'destaque-' + a + '.png'))}) center 52%/150% auto"></div></div><div style="font:500 22px system-ui;color:#eee;margin-top:10px">${n}</div></div>`).join('');
  await p.setContent(`<body style="margin:0;background:#000;font-family:system-ui;color:#eee;padding:50px"><div style="display:flex;gap:40px;align-items:center"><div style="width:220px;height:220px;border-radius:50%;background:url(${u(path.join(PRIV, 'foto-perfil.png'))}) center/cover;border:3px solid #333"></div><div><div style="font:700 34px system-ui">curso_processo_legislativo_</div><div style="font:500 24px system-ui;margin-top:12px;line-height:1.4;white-space:pre-line;color:#ccc">${fs.readFileSync(path.join(__dirname, 'BIO.txt'), 'utf8')}</div></div></div><div style="display:flex;gap:18px;margin-top:50px">${caps}</div></body>`, { waitUntil: 'networkidle' });
  await p.screenshot({ path: path.join(PRIV, 'previa-perfil.png') }); console.log('ok previa');
  await b.close();
})();
