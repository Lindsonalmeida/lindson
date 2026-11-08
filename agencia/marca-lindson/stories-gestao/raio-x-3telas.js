// 3 telas de story · Gestão de redes + 5 Raio-X grátis · identidade preto e amarelo (v2).
// Composições copiadas dos modelos aprovados em agencia/marca-lindson/stories-sites/TEMPLATE.md:
// tela 1 = INFLURY (palavra gigante atrás do recorte), tela 2 = Man UpRight (número gigante + degradê), tela 3 = Jonatas Torres + Z1 (foto com luz âmbar + passos em cartões).
const { chromium } = require('playwright'), path = require('path'), fs = require('fs');
const D = __dirname;
const png = f => 'data:image/png;base64,' + fs.readFileSync(path.join(D, f)).toString('base64');
const jpg = f => 'data:image/jpeg;base64,' + fs.readFileSync(path.join(D, f)).toString('base64');
const css = `*{box-sizing:border-box;margin:0;padding:0}html,body{background:#000}
.a{position:relative;width:1080px;height:1920px;overflow:hidden;background:#0A0A0A;color:#F5F3EE;font-family:Manrope,sans-serif}
.a.am{background:#F5C518;color:#0A0A0A}
.abs{position:absolute}
.ant{font-family:Anton;text-transform:uppercase;line-height:.84;letter-spacing:-.005em}
.ouro{background:linear-gradient(180deg,#FFE27A 0%,#F5C518 45%,#D99A06 100%);-webkit-background-clip:text;background-clip:text;color:transparent;filter:drop-shadow(0 14px 40px rgba(245,197,24,.28))}
.breu{background:linear-gradient(180deg,#2A2A2A 0%,#0A0A0A 60%,#000 100%);-webkit-background-clip:text;background-clip:text;color:transparent}
.h{font:800 84px/1.02 Manrope;letter-spacing:-.045em}
.cx{background:#F5C518;color:#0A0A0A;padding:0 .14em;margin:0 -.04em;display:inline-block;line-height:1.04;box-shadow:0 12px 30px rgba(245,197,24,.28)}
.cxp{background:#0A0A0A;color:#F5C518;padding:0 .14em;margin:0 -.04em;display:inline-block;line-height:1.04}
.marca{font:800 30px Manrope;letter-spacing:-.02em}.marca i{display:inline-block;width:12px;height:12px;border-radius:50%;background:#F5C518;margin-left:4px}.am .marca i{background:#0A0A0A}
.mono{font-family:'JetBrains Mono';font-weight:500;letter-spacing:.1em;text-transform:uppercase}
.vidro{display:inline-flex;align-items:center;gap:12px;padding:12px 22px;border-radius:99px;background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.22);backdrop-filter:blur(14px);font:500 24px 'JetBrains Mono';letter-spacing:.08em;text-transform:uppercase}
.am .vidro{background:rgba(10,10,10,.07);border-color:rgba(10,10,10,.28)}
.vidro b{width:12px;height:12px;border-radius:50%;background:#FF3B30;box-shadow:0 0 12px #FF3B30}
.canto{position:absolute;width:46px;height:46px;border-color:rgba(245,243,238,.55);border-style:solid}
.am .canto{border-color:rgba(10,10,10,.5)}
.vinheta{position:absolute;inset:0;pointer-events:none;background:radial-gradient(ellipse at 50% 45%,transparent 55%,rgba(0,0,0,.55) 100%)}
.am .vinheta{background:radial-gradient(ellipse at 50% 45%,transparent 60%,rgba(120,80,0,.25) 100%)}
.grao{position:absolute;inset:0;pointer-events:none;opacity:.13;mix-blend-mode:overlay;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='220' height='220'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='3'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E")}
.card{background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.16);backdrop-filter:blur(16px);border-radius:28px;padding:34px 40px;display:flex;align-items:center;gap:30px;font:700 44px/1.15 Manrope}
.card .n{font:400 92px/1 Anton;color:#F5C518;min-width:110px}`;
const cantos = (n) => `<div class="canto" style="left:56px;top:96px;border-width:3px 0 0 3px"></div><div class="canto" style="right:56px;top:96px;border-width:3px 3px 0 0"></div>
  <div class="canto" style="left:56px;bottom:96px;border-width:0 0 3px 3px"></div><div class="canto" style="right:56px;bottom:96px;border-width:0 3px 3px 0"></div>
  <div class="abs mono" style="right:80px;top:150px;font-size:24px;opacity:.75">[0${n}/03]</div>`;
const T = [
 // 1 · INFLURY: "REDES" gigante ouro atrás do recorte, luz âmbar, degradê preto com a manchete
 { cls: '', html: `
   <div class="abs" style="left:-200px;top:200px;width:1100px;height:1100px;border-radius:50%;background:radial-gradient(circle,rgba(232,163,23,.45),transparent 65%)"></div>
   <div class="abs ant ouro" style="left:0;right:0;top:380px;text-align:center;font-size:400px">REDES</div>
   <img class="abs" src="${png('cut-c07/recorte.png')}" style="left:50%;transform:translateX(-50%);bottom:520px;height:1100px;filter:drop-shadow(0 40px 50px rgba(0,0,0,.6)) saturate(1.05)">
   <div class="abs" style="left:0;right:0;bottom:0;height:900px;background:linear-gradient(180deg,transparent,#0A0A0A 52%)"></div>
   <div class="abs marca" style="left:80px;top:150px">Lindson Almeida<i></i></div>
   <div class="abs" style="left:80px;top:250px"><span class="vidro"><b></b>Gestão de redes</span></div>
   <div class="abs h" style="left:80px;right:80px;top:1330px">Seu Instagram vende <span class="cx">ou só ocupa espaço?</span></div>
   <div class="abs" style="left:80px;right:80px;top:1610px;font:600 38px/1.3 Manrope;color:#A7A39A">Toque para ver o que eu faço →</div>` },
 // 2 · MAN UPRIGHT: fundo amarelo, "5" gigante em breu, recorte à direita, manchete com caixa preta
 { cls: 'am', html: `
   <div class="abs ant breu" style="left:50px;top:270px;font-size:860px;line-height:1.02;padding-bottom:40px">5</div>
   <img class="abs" src="${png('cut-c08/recorte.png')}" style="right:-190px;bottom:0;height:1180px;z-index:2;filter:drop-shadow(-20px 30px 40px rgba(80,50,0,.35))">
   <div class="abs marca" style="left:80px;top:150px">Lindson Almeida<i></i></div>
   <div class="abs" style="left:80px;top:250px;z-index:5"><span class="vidro">Raio-X do perfil</span></div>
   <div class="abs ant" style="left:80px;top:1170px;font-size:140px;line-height:1.02;color:#0A0A0A;z-index:5">RAIO-X<br><span class="cxp" style="padding:0 .1em">GRÁTIS</span></div>
   <div class="abs" style="left:80px;width:390px;top:1480px;font:800 40px/1.25 Manrope;z-index:5">Só 5 vagas.<br><span style="font-weight:600">Eu analiso o seu perfil e te mostro o que ajustar.</span></div>` },
 // 3 · JONATAS TORRES + Z1: foto com luz âmbar no topo, passos em cartões de vidro, chamada em caixa amarela
 { cls: '', html: `
   <img class="abs" src="${jpg('c09.jpg')}" style="left:0;top:0;width:1080px;height:1150px;object-fit:cover;object-position:50% 18%;filter:saturate(1.08) contrast(1.05)">
   <div class="abs" style="left:0;right:0;top:0;height:1150px;background:linear-gradient(180deg,rgba(10,10,10,.65) 0%,rgba(10,10,10,0) 30%,rgba(10,10,10,0) 60%,#0A0A0A 100%)"></div>
   <div class="abs" style="right:-260px;top:300px;width:900px;height:900px;border-radius:50%;background:radial-gradient(circle,rgba(232,163,23,.35),transparent 65%)"></div>
   <div class="abs marca" style="left:80px;top:150px">Lindson Almeida<i></i></div>
   <div class="abs" style="left:80px;top:250px"><span class="vidro">Como funciona</span></div>
   <div class="abs h" style="left:80px;right:80px;top:930px;font-size:78px">Responde <span class="cx">RAIO-X</span> no direct.</div>
   <div class="abs" style="left:80px;right:80px;top:1140px;display:flex;flex-direction:column;gap:22px">
     <div class="card"><span class="n">01</span>Você me manda o seu @</div>
     <div class="card" style="margin-left:40px"><span class="n">02</span>Eu analiso o perfil todo</div>
     <div class="card"><span class="n">03</span>Te mostro o que ajustar</div>
   </div>` },
];
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
  for (let i = 0; i < T.length; i++) {
    const t = T[i];
    const html = `<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Anton&family=Manrope:wght@500;600;700;800&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet"><style>${css}</style></head><body><div class="a ${t.cls}">${t.html}${cantos(i + 1)}<div class="vinheta"></div><div class="grao"></div></div></body></html>`;
    await p.setContent(html, { waitUntil: 'networkidle' }); await p.waitForTimeout(600);
    await p.locator('.a').screenshot({ path: path.join(D, `tela-0${i + 1}.png`) }); console.log('ok', i + 1);
  }
  await b.close();
})();
