// Sequência de 5 stories "Gestão de redes sociais completa" (conta Leandro, 08/11/2026).
// Identidade do Lindson v2 (preto e amarelo #F5C518, Anton + Manrope), composições copiadas da sequência "Vender sites" (conta Pedro, 05/11).
// Sem foto de pessoa, sem preço, sem promessa de resultado. Uso: node stories.js
const { chromium } = require('playwright'), fs = require('fs'), path = require('path');
const D = __dirname;
const base = `*{box-sizing:border-box;margin:0;padding:0}html,body{background:#000}
.a{position:relative;width:1080px;height:1920px;overflow:hidden;background:#0A0A0A;color:#F5F3EE;font-family:Manrope,sans-serif}
.a.am{background:#F5C518;color:#0A0A0A}
.marca{position:absolute;left:80px;top:150px;font:800 30px Manrope}.marca i{display:inline-block;width:12px;height:12px;border-radius:50%;background:#F5C518;margin-left:4px}.am .marca i{background:#0A0A0A}
.rot{position:absolute;left:80px;top:230px;font:500 26px 'JetBrains Mono';letter-spacing:.08em;text-transform:uppercase;opacity:.8}
.ant{font-family:Anton;text-transform:uppercase;line-height:.86;letter-spacing:-.005em}
.cx{background:#F5C518;color:#0A0A0A;padding:0 .14em;display:inline-block;line-height:1.04}
.am .cx{background:#0A0A0A;color:#F5C518}
.txt{font:700 58px/1.18 Manrope;letter-spacing:-.02em}
.btn{position:absolute;left:80px;right:80px;bottom:300px;text-align:center;padding:34px 0;border-radius:99px;background:#F5C518;color:#0A0A0A;font:800 44px Manrope}
.am .btn{background:#0A0A0A;color:#F5C518}
.card{position:absolute;left:80px;right:80px;padding:44px 48px;border-radius:30px;background:#141414;border:2px solid #2a2a2a;font:700 46px/1.25 Manrope}
.am .card{background:#0A0A0A;color:#F5F3EE;border-color:#0A0A0A}
.num{font:400 120px Anton;color:#F5C518;margin-right:26px;line-height:1}
.am .num{color:#F5C518}`;
const S = [
 { n: '01', bg: '', html: `<div class="rot">Gestão de redes</div>
   <div class="ant" style="position:absolute;left:60px;right:60px;top:560px;font-size:250px;color:#F5C518">PARADO?</div>
   <div class="txt" style="position:absolute;left:80px;right:80px;top:1040px">Seu cliente procura o seu negócio, vê o perfil <span class="cx">sem post há semanas</span> e chama o concorrente.</div>
   <div class="txt" style="position:absolute;left:80px;right:80px;top:1400px;font-size:44px;opacity:.85">Toque para ver como eu cuido disso →</div>` },
 { n: '02', bg: 'am', html: `<div class="rot">Por que acontece</div>
   <div class="ant" style="position:absolute;left:80px;right:80px;top:420px;font-size:200px">POSTA<br>QUANDO<br>DÁ?</div>
   <div class="card" style="top:1000px">Sem calendário, o post sai quando sobra tempo.</div>
   <div class="card" style="top:1210px">Sem roteiro, cada arte sai de um jeito.</div>
   <div class="card" style="top:1420px">Sem resposta, o direct esfria e o cliente some.</div>` },
 { n: '03', bg: '', html: `<div class="rot">O que eu faço</div>
   <div class="ant" style="position:absolute;left:80px;right:80px;top:420px;font-size:170px">GESTÃO<br>COMPLETA</div>
   <div style="position:absolute;left:80px;right:80px;top:1000px;font:800 52px/1.2 Manrope">
     <div style="margin-bottom:56px"><span class="num">01</span>Calendário e roteiro</div>
     <div style="margin-bottom:56px"><span class="num">02</span>Artes, vídeos e legendas</div>
     <div><span class="num">03</span>Postagem e respostas</div></div>` },
 { n: '04', bg: 'am', html: `<div class="rot">Como começa</div>
   <div class="ant" style="position:absolute;left:80px;right:80px;top:420px;font-size:200px">3<br>PASSOS.</div>
   <div class="card" style="top:1000px"><span class="num">01</span>Você responde GESTÃO aqui.</div>
   <div class="card" style="top:1210px"><span class="num">02</span>Eu monto o plano do seu negócio.</div>
   <div class="card" style="top:1420px"><span class="num">03</span>A gente combina o início. Sem contrato sem conversa.</div>` },
 { n: '05', bg: '', html: `<div class="rot">Fale comigo</div>
   <div class="ant" style="position:absolute;left:80px;right:80px;top:500px;font-size:190px">RESPONDE<br><span style="color:#F5C518">GESTÃO</span><br>AQUI.</div>
   <div class="txt" style="position:absolute;left:80px;right:80px;top:1080px;font-size:50px">Responde aqui e eu te explico o plano. O valor a gente conversa no WhatsApp.</div>
` },
];
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
  for (const s of S) {
    const html = `<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Anton&family=Manrope:wght@500;700;800&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet"><style>${base}</style></head><body><div class="a ${s.bg}"><div class="marca">Lindson Almeida<i></i></div>${s.html}</div></body></html>`;
    await p.setContent(html, { waitUntil: 'networkidle' }); await p.waitForTimeout(400);
    await p.locator('.a').screenshot({ path: path.join(D, `s${s.n}.png`) });
    console.log('ok', s.n);
  }
  await b.close();
})();
