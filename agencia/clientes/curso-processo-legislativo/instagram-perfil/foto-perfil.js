// Foto de perfil v2 do curso (conta Leandro, 08/11/2026). Lindson: "a foto do perfil não ficou legal, quero a foto dele e o nome ou logo".
// Duas opções, as duas com os professores + marca, pensadas para o círculo pequeno do Instagram (tudo dentro do círculo inscrito).
const { chromium } = require('playwright'), path = require('path'), fs = require('fs');
const SOC = process.env.SOCIOS || '/home/user/centrallindsonalmeida/dados/clientes-arquivos/curso/socios';
const OUT = process.env.SAIDA_PRIVADA || '/home/user/centrallindsonalmeida/dados/clientes-arquivos/curso/instagram-perfil';
const img = f => 'data:image/png;base64,' + fs.readFileSync(path.join(SOC, f)).toString('base64');
const T = img('cut-tiago-azevedo/recorte-limpo.png'), R = img('cut-rafael-araujo-veras/recorte-limpo.png');
const C = { v: '#0A1F17', v2: '#123528', cr: '#EFE6D4', la: '#C8A96B', la2: '#E6CF9C' };
const simb = (t) => `<svg width="${t}" height="${t}" viewBox="0 0 200 200"><path d="M 36 146 A 64 64 0 0 1 164 146" fill="none" stroke="${C.la}" stroke-width="8" stroke-linecap="round"/><path d="M 62 146 A 38 38 0 0 1 138 146" fill="none" stroke="${C.la}" stroke-opacity=".45" stroke-width="6" stroke-linecap="round"/><text x="100" y="134" text-anchor="middle" font-family="Instrument Serif" font-style="italic" font-size="100" fill="${C.la2}">§</text></svg>`;
const base = `*{margin:0;padding:0;box-sizing:border-box}html,body{background:#000}.a{position:relative;width:1080px;height:1080px;overflow:hidden;background:radial-gradient(ellipse at 50% 30%,#1B4434,${C.v} 72%)}.abs{position:absolute}
.pes{filter:drop-shadow(0 24px 30px rgba(0,0,0,.55)) saturate(.92) contrast(1.06) sepia(.1)}.it{font-family:'Instrument Serif';font-style:italic;color:${C.la2}}`;
const pessoas = (top, h) => `<img class="abs pes" src="${R}" style="left:540px;top:${top + 20}px;height:${h * .95}px"><img class="abs pes" src="${T}" style="left:150px;top:${top}px;height:${h}px">
  <div class="abs" style="left:0;right:0;bottom:0;height:150px;background:linear-gradient(180deg,transparent,${C.v})"></div>`;
const OP = {
  'foto-perfil-a-nome.png': `<div class="a">${pessoas(400, 760)}
    <div class="abs" style="left:0;right:0;top:150px;text-align:center;line-height:.95">
      <div style="font:800 112px 'Inter Tight';letter-spacing:-.04em;color:${C.cr}">Processo</div>
      <div class="it" style="font-size:132px;letter-spacing:-.01em">Legislativo</div></div></div>`,
  'foto-perfil-b-logo.png': `<div class="a">${pessoas(430, 730)}
    <div class="abs" style="left:0;right:0;top:120px;display:flex;justify-content:center">${simb(330)}</div></div>`,
};
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1080 } });
  for (const [arq, html] of Object.entries(OP)) {
    await p.setContent(`<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@800&family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet"><style>${base}</style></head><body>${html}</body></html>`, { waitUntil: 'networkidle' });
    await p.waitForTimeout(500); await p.screenshot({ path: path.join(OUT, arq) }); console.log('ok', arq);
  }
  // prévia no círculo, tamanho grande e pequeno (como aparece no feed)
  const u = f => 'data:image/png;base64,' + fs.readFileSync(path.join(OUT, f)).toString('base64');
  await p.setViewportSize({ width: 900, height: 480 });
  await p.setContent(`<body style="margin:0;background:#000;display:flex;gap:60px;padding:40px;align-items:center">${Object.keys(OP).map(f => `<div style="display:flex;gap:30px;align-items:center"><div style="width:300px;height:300px;border-radius:50%;background:url(${u(f)}) center/cover"></div><div style="width:64px;height:64px;border-radius:50%;background:url(${u(f)}) center/cover"></div></div>`).join('')}</body>`);
  await p.screenshot({ path: path.join(OUT, 'previa-foto-perfil-v2.png') }); console.log('ok previa'); await b.close();
})();
