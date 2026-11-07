// Capas v4: visual de impacto na paleta do cartaz (verde-garrafa, dourado, branco). Sem fotos: o espaço da pessoa fica para depois.
const { chromium } = require('playwright');
const path = require('path');
const CSS = `
*{box-sizing:border-box;margin:0;padding:0}
.c{width:1080px;height:1920px;position:relative;overflow:hidden;font-family:'Inter Display',Inter,sans-serif;color:#FCFCFC;background:#00241C}
.glow{position:absolute;inset:0;background:radial-gradient(900px 900px at 50% 28%, rgba(200,176,120,.35), transparent 60%),radial-gradient(700px 700px at 10% 100%, rgba(0,120,90,.45), transparent 60%)}
.grid{position:absolute;inset:0;background-image:linear-gradient(rgba(200,176,120,.10) 1px,transparent 1px),linear-gradient(90deg,rgba(200,176,120,.10) 1px,transparent 1px);background-size:90px 90px;-webkit-mask-image:radial-gradient(ellipse at 50% 35%,#000 20%,transparent 75%)}
.ring{position:absolute;border-radius:50%;border:2px solid rgba(200,176,120,.55)}
.gold{background:linear-gradient(120deg,#F3E2B0 0%,#C8B078 45%,#8E7440 100%);-webkit-background-clip:text;background-clip:text;color:transparent}
.h{position:absolute;left:80px;right:80px;font-weight:900;text-transform:uppercase;letter-spacing:-.05em;line-height:.84}
.top{position:absolute;left:80px;right:80px;top:80px;display:flex;justify-content:space-between;align-items:center;font-family:'JetBrains Mono',monospace;font-size:24px;letter-spacing:.12em;text-transform:uppercase;color:#C8B078}
.logo{font-weight:900;font-size:38px;letter-spacing:-.02em;color:#FCFCFC;text-transform:uppercase}
.glass{position:absolute;left:80px;right:80px;bottom:100px;padding:44px 48px;border-radius:36px;background:rgba(252,252,252,.06);border:1.5px solid rgba(200,176,120,.45);backdrop-filter:blur(12px);box-shadow:0 30px 80px rgba(0,0,0,.35) inset,0 0 60px rgba(200,176,120,.15)}
.chip{display:inline-block;margin:0 10px 12px 0;padding:14px 22px;border-radius:999px;border:1.5px solid rgba(200,176,120,.7);font-family:'JetBrains Mono',monospace;font-size:24px;letter-spacing:.06em;text-transform:uppercase;color:#F3E2B0}
.mono{font-family:'JetBrains Mono',monospace;text-transform:uppercase;letter-spacing:.12em;font-size:24px;color:#C8B078}
.foot{position:absolute;left:80px;right:80px;bottom:44px;display:flex;justify-content:space-between;font-family:'JetBrains Mono',monospace;font-size:22px;letter-spacing:.1em;color:rgba(252,252,252,.6);text-transform:uppercase}
`;
const top = (n) => `<div class="top"><span class="logo">Processo Legislativo</span><span>Nº ${n}/03</span></div>`;
const foot = `<div class="foot"><span>@curso_processo_legislativo_</span><span>Curso básico</span></div>`;
const C = [
 ['capa-v4-01-plenario', `<section class="c"><div class="glow"></div><div class="grid"></div>
   <div class="ring" style="width:1000px;height:1000px;left:40px;top:-60px"></div>
   <div class="ring" style="width:720px;height:720px;left:180px;top:80px;border-color:rgba(200,176,120,.35)"></div>
   ${top('01')}
   <div class="mono" style="position:absolute;left:80px;top:720px">Votação · regra da sessão</div>
   <div class="h gold" style="top:760px;font-size:200px">Pode</div>
   <div class="h gold" style="top:930px;font-size:200px">votar</div>
   <div class="h" style="top:1100px;font-size:200px">sem</div>
   <div class="h" style="top:1270px;font-size:200px">quórum?</div>
   <div class="glass"><span class="chip">Quórum</span><span class="chip">Sessão</span><span class="chip">Regimento</span><p style="font-size:38px;line-height:1.35;color:rgba(252,252,252,.9)">Entenda a regra antes de votar, com clareza e sem jargão.</p></div>
   ${foot}</section>`],
 ['capa-v4-02-ordem', `<section class="c" style="background:linear-gradient(160deg,#F3E2B0 0%,#C8B078 55%,#A38A52 100%);color:#00241C">
   <div class="grid" style="background-image:linear-gradient(rgba(0,36,28,.10) 1px,transparent 1px),linear-gradient(90deg,rgba(0,36,28,.10) 1px,transparent 1px)"></div>
   <div class="ring" style="width:1200px;height:1200px;left:-60px;top:500px;border-color:rgba(0,36,28,.25)"></div>
   <div class="ring" style="width:800px;height:800px;left:140px;top:700px;border-color:rgba(0,36,28,.35)"></div>
   <div class="top" style="color:#00241C"><span class="logo" style="color:#00241C">Processo Legislativo</span><span>Nº 02/03</span></div>
   <div class="h" style="top:380px;font-size:300px;color:#00241C">Devido</div>
   <div class="h" style="top:640px;font-size:220px;color:#00241C">processo</div>
   <div class="h" style="top:900px;font-size:120px;color:#00241C;text-transform:none;font-weight:700;letter-spacing:-.03em;line-height:1.05">O que é o devido processo legislativo?</div>
   <div class="glass" style="background:rgba(0,36,28,.9);border-color:rgba(0,36,28,.9)"><span class="chip" style="color:#F3E2B0;border-color:#C8B078">Regra da casa</span><p style="font-size:38px;line-height:1.35;color:#FCFCFC">Cada etapa do processo tem uma ordem. Aprenda qual é.</p></div>
   <div class="foot" style="color:rgba(0,36,28,.7)"><span>@curso_processo_legislativo_</span><span>Curso básico</span></div></section>`],
 ['capa-v4-03-sessao', `<section class="c"><div class="glow" style="background:radial-gradient(1000px 1000px at 50% 45%, rgba(200,176,120,.28), transparent 62%)"></div>
   <div style="position:absolute;left:50%;top:-200px;width:1400px;height:2600px;margin-left:-700px;background:conic-gradient(from 200deg at 50% 0%, transparent 0deg, rgba(200,176,120,.18) 20deg, transparent 40deg, transparent 320deg, rgba(200,176,120,.18) 340deg, transparent 360deg);filter:blur(4px)"></div>
   <div class="grid"></div>
   ${top('03')}
   <div class="h gold" style="top:380px;left:0;right:0;text-align:center;font-size:760px;line-height:.8">?</div>
   <div class="h" style="top:1200px;left:80px;right:80px;text-align:center;font-size:190px;letter-spacing:-.05em">Sessão</div>
   <div class="h" style="top:1390px;left:80px;right:80px;text-align:center;font-size:190px;letter-spacing:-.05em">secreta</div>
   <div class="mono" style="position:absolute;left:0;right:0;top:1640px;text-align:center;font-size:30px">Pode acontecer? · veja a regra do regimento</div>
   ${foot}</section>`],
];
(async () => {
  const b = await chromium.launch({ args: ['--no-sandbox'] });
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
  for (const [name, html] of C) {
    await p.setContent(`<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>${CSS}</style></head><body style="margin:0">${html}</body></html>`, { waitUntil: 'load' });
    await p.evaluate(() => document.fonts.ready);
    await (await p.$('section')).screenshot({ path: path.join(__dirname, 'capas-v4', name + '.png') });
  }
  await b.close(); console.log('ok', C.length);
})().catch(e => { console.error(e.message); process.exit(1); });
