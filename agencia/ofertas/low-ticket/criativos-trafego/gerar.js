// 30 criativos de tráfego (6 produtos da Hubla x 5) no estilo infoprodutor do Behance, na marca preto e amarelo do Lindson (conta Leandro, 09/11/2026).
// Base de CSS: os stories aprovados (agencia/marca-lindson/stories-gestao/raio-x-3telas.js). Referências e descartes em TEMPLATE.md.
// node gerar.js <pasta-recortes fNN.png> <pasta-saida> [slug]  → <saida>/<slug>/<slug>-0N.jpg (1080x1350, 4:5, feed e Reels/Stories com margem segura)
const { chromium } = require('playwright'), path = require('path'), fs = require('fs');
const [REC, OUT, SO] = process.argv.slice(2), C = '/home/user/centrallindsonalmeida/';
const D = JSON.parse(fs.readFileSync(path.join(__dirname, 'criativos.json'), 'utf8'));
const b64 = (f, t) => `data:image/${t};base64,` + fs.readFileSync(f).toString('base64');
const foto = n => b64(path.join(REC, `f${String(n).padStart(2, '0')}.png`), 'png');
const capa = p => b64(C + p.capa, 'jpeg');
const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;');
// |palavra| = destaque: caixa amarela no escuro, caixa preta no amarelo
const hl = (s, am) => esc(s).replace(/\|([^|]+)\|/g, `<span class="${am ? 'cxp' : 'cx'}">$1</span>`);
const css = `*{box-sizing:border-box;margin:0;padding:0}html,body{background:#000}
.a{position:relative;width:1080px;height:1350px;overflow:hidden;background:#0A0A0A;color:#F5F3EE;font-family:Manrope,sans-serif}
.a.am{background:#F5C518;color:#0A0A0A}
.abs{position:absolute}
.ant{font-family:Anton;text-transform:uppercase;line-height:.86;letter-spacing:-.005em}
.ouro{background:linear-gradient(180deg,#FFE27A 0%,#F5C518 45%,#D99A06 100%);-webkit-background-clip:text;background-clip:text;color:transparent}
.breu{background:linear-gradient(180deg,#2A2A2A 0%,#0A0A0A 60%,#000 100%);-webkit-background-clip:text;background-clip:text;color:transparent}
.vaz{color:transparent;-webkit-text-stroke:2px rgba(245,197,24,.45)}.am .vaz{-webkit-text-stroke:2px rgba(10,10,10,.28)}
.h{font:800 68px/1.04 Manrope;letter-spacing:-.045em}
.cx{background:#F5C518;color:#0A0A0A;padding:0 .14em;margin:0 -.03em;display:inline;line-height:1.16;box-decoration-break:clone;-webkit-box-decoration-break:clone;box-shadow:0 10px 28px rgba(245,197,24,.25)}
.cxp{background:#0A0A0A;color:#F5C518;padding:0 .14em;margin:0 -.03em;display:inline;line-height:1.16;box-decoration-break:clone;-webkit-box-decoration-break:clone}
.marca{font:800 28px Manrope;letter-spacing:-.02em}.marca i{display:inline-block;width:11px;height:11px;border-radius:50%;background:#F5C518;margin-left:4px}.am .marca i{background:#0A0A0A}
.mono{font-family:'JetBrains Mono';font-weight:500;letter-spacing:.12em;text-transform:uppercase}
.vidro{display:inline-flex;align-items:center;gap:12px;padding:11px 20px;border-radius:99px;background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.22);backdrop-filter:blur(14px);font:500 21px 'JetBrains Mono';letter-spacing:.1em;text-transform:uppercase}
.am .vidro{background:rgba(10,10,10,.07);border-color:rgba(10,10,10,.3)}
.vidro b{width:11px;height:11px;border-radius:50%;background:#F5C518;box-shadow:0 0 12px #F5C518}.am .vidro b{background:#0A0A0A;box-shadow:none}
.btn{display:inline-flex;align-items:center;gap:16px;padding:24px 38px;border-radius:99px;background:#F5C518;color:#0A0A0A;font:800 32px Manrope;letter-spacing:-.02em;box-shadow:0 18px 50px rgba(245,197,24,.35),inset 0 -4px 0 rgba(0,0,0,.15)}
.am .btn{background:#0A0A0A;color:#F5C518;box-shadow:0 18px 40px rgba(0,0,0,.25)}
.btn s{text-decoration:none;display:inline-grid;place-items:center;width:44px;height:44px;border-radius:50%;background:#0A0A0A;color:#F5C518;font-size:26px}.am .btn s{background:#F5C518;color:#0A0A0A}
.sub{font:600 30px/1.32 Manrope;color:#B9B4AA}.am .sub{color:#3A3426}
.vinheta{position:absolute;inset:0;pointer-events:none;background:radial-gradient(ellipse at 50% 45%,transparent 55%,rgba(0,0,0,.55) 100%)}
.am .vinheta{background:radial-gradient(ellipse at 50% 45%,transparent 60%,rgba(120,80,0,.22) 100%)}
.grao{position:absolute;inset:0;pointer-events:none;opacity:.12;mix-blend-mode:overlay;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='220' height='220'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='3'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E")}
.card{background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.15);backdrop-filter:blur(16px);border-radius:24px;padding:22px 28px;display:flex;align-items:center;gap:20px;font:700 29px/1.2 Manrope}
.am .card{background:rgba(10,10,10,.92);color:#F5F3EE;border-color:transparent}
.card .n{font:400 46px/1 Anton;color:#F5C518;min-width:58px}
.raio{position:absolute;pointer-events:none;mix-blend-mode:screen;background:linear-gradient(100deg,transparent 40%,rgba(255,214,90,.22) 50%,transparent 60%)}
.mock{position:absolute;border-radius:14px;box-shadow:0 50px 90px rgba(0,0,0,.6),0 0 0 1px rgba(255,255,255,.12);transform:perspective(1600px) rotateY(-16deg) rotateX(4deg) rotateZ(-3deg)}`;
// pessoa: sai pela base da arte (o corte de baixo nunca aparece) com contorno de luz âmbar
const pessoa = (n, s) => `<img class="abs" src="${foto(n)}" style="${s};filter:drop-shadow(0 0 2px rgba(255,214,120,.55)) drop-shadow(0 0 28px rgba(245,197,24,.28)) drop-shadow(0 40px 50px rgba(0,0,0,.55)) saturate(1.05) contrast(1.04)">`;
const topo = (p, c) => `<div class="abs marca" style="left:64px;top:60px">Lindson Almeida<i></i></div><div class="abs mono" style="right:64px;top:66px;font-size:20px;opacity:.7">${esc(p.nome)}</div>
 <div class="abs" style="left:64px;top:120px;z-index:6"><span class="vidro"><b></b>${esc(c.tag)}</span></div>`;
const botao = c => `<span class="btn">${esc(c.cta)}<s>→</s></span>`;
const L = {
 // L1 · especialista: palavra gigante em ouro atrás, recorte grande à direita, capa do produto em 3D à esquerda, manchete no rodapé
 L1: (p, c, am) => `
  <div class="abs" style="right:-260px;top:120px;width:1100px;height:1100px;border-radius:50%;background:radial-gradient(circle,${am ? 'rgba(255,255,255,.55)' : 'rgba(232,163,23,.42)'},transparent 64%)"></div>
  <div class="abs ant ${am ? 'breu' : 'ouro'}" style="left:-10px;right:-10px;top:150px;text-align:center;font-size:${p.palavra.length > 4 ? 330 : 420}px;opacity:.95">${esc(p.palavra)}</div>
  ${pessoa(c.foto, 'right:-60px;bottom:-40px;height:1020px;z-index:2')}
  <img class="mock" src="${capa(p)}" style="left:64px;top:420px;width:250px;z-index:3">
  <div class="abs" style="left:0;right:0;bottom:0;height:640px;z-index:3;background:linear-gradient(180deg,transparent,${am ? '#F5C518' : '#0A0A0A'} 55%)"></div>
  <div class="abs h" style="left:64px;right:64px;top:820px;z-index:5">${hl(c.titulo, am)}</div>
  <div class="abs sub" style="left:64px;right:300px;top:1080px;z-index:5;font-size:27px">${esc(c.sub)}</div>
  <div class="abs" style="left:64px;bottom:60px;z-index:5">${botao(c)}</div>`,
 // L2 · dor: "?" gigante vazado, recorte à esquerda olhando a pergunta, manchete grande à direita
 L2: (p, c, am) => `
  <div class="abs ant vaz" style="right:-40px;top:60px;font-size:1250px;line-height:1">?</div>
  <div class="abs" style="left:-300px;bottom:-200px;width:1000px;height:1000px;border-radius:50%;background:radial-gradient(circle,${am ? 'rgba(255,255,255,.5)' : 'rgba(232,163,23,.38)'},transparent 64%)"></div>
  ${pessoa(c.foto, 'left:-150px;bottom:-30px;height:900px;z-index:2')}
  <div class="abs" style="left:480px;right:64px;top:250px;z-index:5"><div class="h" style="font-size:64px">${hl(c.titulo, am)}</div><div class="sub" style="margin-top:28px;font-size:28px">${esc(c.sub)}</div></div>
  <div class="abs" style="left:0;right:0;bottom:0;height:260px;z-index:3;background:linear-gradient(180deg,transparent,${am ? '#F5C518' : '#0A0A0A'} 70%)"></div>
  <div class="abs" style="right:64px;bottom:60px;z-index:5">${botao(c)}</div>`,
 // L3 · o que vem dentro: capa em 3D com brilho e raios, entregáveis em cartões numerados (sem foto nova)
 L3: (p, c, am) => `
  <div class="abs" style="left:-200px;top:260px;width:1000px;height:1000px;border-radius:50%;background:radial-gradient(circle,${am ? 'rgba(255,255,255,.6)' : 'rgba(232,163,23,.45)'},transparent 62%)"></div>
  <div class="raio" style="left:-200px;top:200px;width:1100px;height:900px"></div>
  <div class="abs h" style="left:64px;right:64px;top:210px;font-size:64px;z-index:5">${hl(c.titulo, am)}</div>
  <img class="mock" src="${capa(p)}" style="left:70px;top:470px;width:400px;z-index:3">
  <div class="abs" style="left:540px;right:64px;top:470px;display:flex;flex-direction:column;gap:14px;z-index:4">${p.itens.slice(0, 5).map((t, i) => `<div class="card"><span class="n">0${i + 1}</span>${esc(t)}</div>`).join('')}</div>
  <div class="abs" style="left:64px;bottom:60px;z-index:5">${botao(c)}</div>
  <div class="abs mono" style="right:64px;bottom:80px;font-size:19px;opacity:.7">Acesso na hora · área de membros</div>`,
 // L4 · número gigante vazado em ouro, recorte à direita cruzando o número, legenda com caixa
 L4: (p, c, am) => `
  <div class="abs" style="right:-200px;top:200px;width:1000px;height:1000px;border-radius:50%;background:radial-gradient(circle,${am ? 'rgba(255,255,255,.55)' : 'rgba(232,163,23,.4)'},transparent 62%)"></div>
  <div class="abs ant ${am ? 'breu' : 'ouro'}" style="left:40px;top:190px;font-size:700px;line-height:1;z-index:1">${esc(c.num)}</div>
  ${pessoa(c.foto, 'right:-90px;bottom:-30px;height:900px;z-index:2')}
  <div class="abs ant" style="left:64px;top:890px;font-size:110px;z-index:5;color:${am ? '#0A0A0A' : '#F5F3EE'}">${esc(c.unid)}</div>
  <div class="abs" style="left:0;right:0;bottom:0;height:420px;z-index:3;background:linear-gradient(180deg,transparent,${am ? '#F5C518' : '#0A0A0A'} 50%)"></div>
  <div class="abs h" style="left:64px;right:330px;top:1010px;z-index:5;font-size:44px">${hl(c.titulo, am)}</div>
  <div class="abs" style="left:64px;bottom:60px;z-index:5">${botao(c)}</div>`,
 // L5 · virada: cartão ANTES apagado x cartão DEPOIS em destaque, recorte no centro-baixo
 L5: (p, c, am) => `
  <div class="abs" style="left:140px;top:420px;width:900px;height:900px;border-radius:50%;background:radial-gradient(circle,${am ? 'rgba(255,255,255,.55)' : 'rgba(232,163,23,.38)'},transparent 62%)"></div>
  <div class="abs h" style="left:64px;right:64px;top:200px;font-size:72px;z-index:5">${hl(c.titulo, am)}</div>
  <div class="abs" style="left:64px;width:440px;top:400px;z-index:5;padding:28px;border-radius:24px;border:2px dashed ${am ? 'rgba(10,10,10,.35)' : 'rgba(255,255,255,.25)'};background:${am ? 'rgba(255,255,255,.25)' : 'rgba(255,255,255,.04)'}">
    <div class="mono" style="font-size:20px;opacity:.65;margin-bottom:14px">✕ Antes</div><div style="font:600 30px/1.3 Manrope;opacity:.7;text-decoration:line-through;text-decoration-thickness:2px">${esc(c.antes)}</div></div>
  <div class="abs" style="right:64px;width:460px;top:470px;z-index:5;padding:28px;border-radius:24px;background:${am ? '#0A0A0A' : '#F5C518'};color:${am ? '#F5F3EE' : '#0A0A0A'};box-shadow:0 30px 70px rgba(0,0,0,.35);transform:rotate(2deg)">
    <div class="mono" style="font-size:20px;margin-bottom:14px;color:${am ? '#F5C518' : '#0A0A0A'}">✓ Depois</div><div style="font:800 32px/1.25 Manrope">${esc(c.depois)}</div></div>
  ${c.foto ? pessoa(c.foto, 'left:50%;transform:translateX(-50%);bottom:-40px;height:780px;z-index:2')
    : `<img class="mock" src="${capa(p)}" style="left:50%;margin-left:-180px;top:790px;width:360px;z-index:2">`}
  <div class="abs" style="left:0;right:0;bottom:0;height:300px;z-index:3;background:linear-gradient(180deg,transparent,${am ? '#F5C518' : '#0A0A0A'} 65%)"></div>
  <div class="abs" style="left:50%;transform:translateX(-50%);bottom:60px;z-index:5;white-space:nowrap">${botao(c)}</div>`,
};
(async () => {
  const b = await chromium.launch(), pg = await b.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 1 });
  for (const p of D.produtos) {
    if (SO && p.slug !== SO) continue;
    fs.mkdirSync(path.join(OUT, p.slug), { recursive: true });
    for (const [i, c] of p.criativos.entries()) {
      // cor alterna dentro do produto: nunca dois seguidos iguais (regra dos posts estáticos)
      const am = (p.fundo === 'amarelo') !== (i % 2 === 1);
      const html = `<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Anton&family=Manrope:wght@500;600;700;800&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet"><style>${css}</style></head>
       <body><div class="a ${am ? 'am' : ''}">${L[c.l](p, c, am)}${topo(p, c)}<div class="vinheta"></div><div class="grao"></div></div></body></html>`;
      await pg.setContent(html, { waitUntil: 'networkidle' }); await pg.evaluate(() => document.fonts.ready);
      const f = path.join(OUT, p.slug, `${p.slug}-0${i + 1}.jpg`);
      await pg.locator('.a').screenshot({ path: f, type: 'jpeg', quality: 92 }); console.log(f);
    }
  }
  await b.close();
})();
