// Identidade "Hemiciclo" do Curso de Processo Legislativo (conta Leandro, 08/11/2026).
// Pedido do Lindson: "recrie a identidade visual do curso baseada nas novas informações do Behance" (Amaral & Velasco, Gabriel Gaos;
// análise na Central: dados/agencia/referencias/amaral-velasco/README.md). Copiamos os PRINCÍPIOS, não o símbolo, o nome nem as cores:
// uma cor em dois tons + neutro, uma família tipográfica só, o símbolo vira grafismo e moldura, série de stories com progresso, nome + OAB em destaque.
// Evitado: serifa antiga e papel bege (identidade "Ata" reprovada em 07/11), balança, martelo e colunas.
// Uso: node gerar.js  → prancha.png (1920x1080), story-01..03.png (1080x1920), post-01.png (1080x1350)
const { chromium } = require('playwright'), path = require('path');
const D = __dirname;
const C = { esc: '#08231A', esc2: '#0E3324', viv: '#35D48A', neu: '#F2F2EE', cinza: '#9DB3A8' };
const base = `*{box-sizing:border-box;margin:0;padding:0}html,body{background:#000}
body{font-family:'Inter Tight',sans-serif}
.esc{background:${C.esc};color:${C.neu}}.viv{color:${C.viv}}.neu{background:${C.neu};color:${C.esc}}
.t{font-weight:800;letter-spacing:-.035em;line-height:.98}
.r{font:600 22px 'Inter Tight';letter-spacing:.16em;text-transform:uppercase}
.abs{position:absolute}`;
// hemiciclo: arcos concêntricos de "bancadas", com pontos (cadeiras); base do grafismo, da moldura e do selo
const arcos = (cx, cy, r0, n, gap, cor, op, pontos) => {
  let s = '';
  for (let i = 0; i < n; i++) { const r = r0 + i * gap;
    s += `<path d="M ${cx - r} ${cy} A ${r} ${r} 0 0 1 ${cx + r} ${cy}" fill="none" stroke="${cor}" stroke-opacity="${op}" stroke-width="${Math.max(2, gap * .18)}"/>`;
    if (pontos) { const k = 7 + i * 3; for (let j = 0; j <= k; j++) { const a = Math.PI - (Math.PI * j / k); s += `<circle cx="${cx + r * Math.cos(a)}" cy="${cy - r * Math.sin(a)}" r="${gap * .14}" fill="${cor}" fill-opacity="${op}"/>`; } } }
  return s;
};
// símbolo: § dentro do hemiciclo (o parágrafo da lei sentado no plenário)
const simbolo = (tam, corA, corB) => `<svg width="${tam}" height="${tam}" viewBox="0 0 200 200"><rect width="200" height="200" rx="46" fill="${corA}"/>
  <path d="M 30 150 A 70 70 0 0 1 170 150" fill="none" stroke="${corB}" stroke-width="14" stroke-linecap="round"/>
  <path d="M 58 150 A 42 42 0 0 1 142 150" fill="none" stroke="${corB}" stroke-opacity=".45" stroke-width="10" stroke-linecap="round"/>
  <text x="100" y="138" text-anchor="middle" font-family="Inter Tight" font-weight="800" font-size="92" fill="${corB}">§</text></svg>`;
const logo = (cor, viv, tam = 1, sA, sB) => `<div style="display:flex;align-items:center;gap:${18 * tam}px">${simbolo(78 * tam, sA || viv, sB || C.esc)}
  <div style="line-height:1"><div style="font:800 ${38 * tam}px 'Inter Tight';letter-spacing:-.03em;color:${cor}">Processo</div><div style="font:800 ${38 * tam}px 'Inter Tight';letter-spacing:-.03em;color:${viv}">Legislativo</div>
  <div style="font:600 ${13 * tam}px 'Inter Tight';letter-spacing:.22em;text-transform:uppercase;color:${cor};opacity:.7;margin-top:${8 * tam}px">Curso · Câmara municipal</div></div></div>`;
const progresso = (n, tot) => `<div class="abs" style="left:80px;right:80px;top:96px;display:flex;gap:10px">${Array.from({ length: tot }, (_, i) => `<div style="flex:1;height:6px;border-radius:9px;background:${i < n ? C.viv : 'rgba(242,242,238,.22)'}"></div>`).join('')}</div>`;
const P = {
 prancha: { w: 1920, h: 1080, html: `<div class="esc" style="position:relative;width:1920px;height:1080px;overflow:hidden">
   <svg class="abs" style="left:0;top:0" width="1920" height="1080">${arcos(1500, 1080, 180, 9, 70, C.viv, .14, true)}</svg>
   <div class="abs" style="left:90px;top:80px">${logo(C.neu, C.viv, 1.5)}</div>
   <div class="abs r" style="left:90px;top:300px;color:${C.cinza}">Identidade · Hemiciclo</div>
   <div class="abs t" style="left:90px;top:350px;font-size:84px;width:900px">Saia do improviso.<br><span class="viv">Atue com segurança.</span></div>
   <div class="abs" style="left:90px;top:620px;display:flex;gap:22px">
     ${[[C.esc, 'Verde plenário', C.esc, '60%', true], [C.viv, 'Verde voto', C.viv, '25%'], [C.neu, 'Papel', C.neu, '15%']].map(([c, n, h, p, b]) => `<div style="width:230px"><div style="height:150px;border-radius:22px;background:${c};${b ? 'border:2px solid rgba(242,242,238,.25)' : ''}"></div><div style="font:700 22px 'Inter Tight';margin-top:14px">${n}</div><div style="font:500 18px 'Inter Tight';opacity:.7">${h} · ${p}</div></div>`).join('')}</div>
   <div class="abs" style="left:90px;top:900px;font:500 20px 'Inter Tight';opacity:.8;width:780px">Uma família só: <b>Inter Tight</b> 400 a 800. Título curto, segunda linha em verde voto. Nome do professor sempre com a OAB.</div>
   <div class="abs" style="left:1120px;top:120px;width:640px;height:780px;border-radius:320px 320px 28px 28px;overflow:hidden;background:linear-gradient(160deg,${C.esc2},#061a13)">
     <svg class="abs" style="left:0;top:0" width="640" height="780">${arcos(320, 780, 90, 8, 62, C.viv, .22, true)}</svg>
     <div class="abs" style="left:40px;right:40px;bottom:60px"><div class="r" style="color:${C.viv}">Moldura de foto</div><div style="font:800 46px 'Inter Tight';letter-spacing:-.03em;margin-top:10px">O arco do plenário<br>emoldura o professor.</div></div></div>
 </div>` },
 s1: { w: 1080, h: 1920, html: `<div class="esc" style="position:relative;width:1080px;height:1920px;overflow:hidden">
   ${progresso(1, 3)}
   <svg class="abs" style="left:0;top:0" width="1080" height="1920">${arcos(540, 1920, 200, 10, 78, C.viv, .13, true)}</svg>
   <div class="abs" style="left:80px;top:170px">${logo(C.neu, C.viv, .9)}</div>
   <div class="abs r" style="left:80px;top:560px;color:${C.viv}">Episódio 01 · Regime de urgência</div>
   <div class="abs t" style="left:80px;right:80px;top:620px;font-size:118px">O que muda quando o projeto vira <span class="viv">urgente?</span></div>
   <div class="abs" style="left:80px;right:120px;top:1130px;font:500 44px/1.35 'Inter Tight';opacity:.9">Prazo, pauta e quem decide. Em 1 minuto, sem juridiquês.</div>
   <div class="abs" style="left:80px;bottom:330px;font:700 34px 'Inter Tight';color:${C.viv}">Toque para continuar →</div></div>` },
 s2: { w: 1080, h: 1920, html: `<div class="neu" style="position:relative;width:1080px;height:1920px;overflow:hidden">
   <div class="abs" style="left:80px;right:80px;top:96px;display:flex;gap:10px">${[1, 1, 0].map(f => `<div style="flex:1;height:6px;border-radius:9px;background:${f ? C.esc : 'rgba(8,35,26,.18)'}"></div>`).join('')}</div>
   <div class="abs" style="left:80px;top:170px">${logo(C.esc, '#1E9E62', .9)}</div>
   <div class="abs" style="left:150px;right:150px;top:470px;height:900px;border-radius:390px 390px 30px 30px;overflow:hidden;background:${C.esc}">
     <svg class="abs" style="left:0;top:0" width="780" height="900">${arcos(390, 900, 110, 8, 70, C.viv, .25, true)}</svg>
     <div class="abs" style="left:0;right:0;top:300px;text-align:center">${simbolo(220, C.viv, C.esc)}</div>
     <div class="abs r" style="left:0;right:0;bottom:50px;text-align:center;color:${C.viv}">Foto do professor aqui</div></div>
   <div class="abs t" style="left:80px;right:80px;top:1420px;font-size:76px;color:${C.esc}">Tiago Azevedo</div>
   <div class="abs" style="left:80px;right:80px;top:1510px;font:600 34px/1.3 'Inter Tight';color:${C.esc};opacity:.8">Vice-presidente da Comissão de Direito Parlamentar e Processo Legislativo · <b>OAB/MA</b></div></div>` },
 s3: { w: 1080, h: 1920, html: `<div class="esc" style="position:relative;width:1080px;height:1920px;overflow:hidden">
   ${progresso(3, 3)}
   <div class="abs" style="left:80px;top:170px">${logo(C.neu, C.viv, .9)}</div>
   <div class="abs" style="left:80px;right:80px;top:520px;border-radius:36px;background:${C.esc2};padding:60px 56px;border:2px solid rgba(53,212,138,.25)">
     <div class="r" style="color:${C.viv}">Na prática</div>
     <div class="t" style="font-size:84px;margin-top:22px">3 regras que todo vereador precisa <span class="viv">saber.</span></div>
     ${['Quem pode propor cada tipo de projeto', 'Quando o regime de urgência vale', 'O que anula uma votação'].map((x, i) => `<div style="display:flex;gap:26px;align-items:center;margin-top:${i ? 26 : 50}px;font:600 40px 'Inter Tight'"><span style="flex:none;width:76px;height:76px;border-radius:50%;background:${C.viv};color:${C.esc};font:800 36px 'Inter Tight';display:flex;align-items:center;justify-content:center">${i + 1}</span>${x}</div>`).join('')}</div>
   <div class="abs" style="left:80px;right:80px;bottom:330px;text-align:center;padding:34px 0;border-radius:99px;background:${C.viv};color:${C.esc};font:800 42px 'Inter Tight'">Responda CURSO no direct</div></div>` },
 post: { w: 1080, h: 1350, html: `<div class="esc" style="position:relative;width:1080px;height:1350px;overflow:hidden">
   <div class="abs" style="left:0;top:0;width:1080px;height:640px;background:${C.viv};clip-path:polygon(0 0,100% 0,100% 72%,0 100%)"></div>
   <svg class="abs" style="left:0;top:0;clip-path:polygon(0 0,100% 0,100% 72%,0 100%)" width="1080" height="640">${arcos(540, 640, 120, 7, 64, C.esc, .18, true)}</svg>
   <div class="abs" style="left:84px;top:84px">${logo(C.esc, C.esc, .8, C.esc, C.viv)}</div>
   <div class="abs r" style="left:84px;top:700px;color:${C.viv}">Turma básica</div>
   <div class="abs t" style="left:84px;right:84px;top:750px;font-size:96px">Saia do improviso na <span class="viv">câmara municipal.</span></div>
   <div class="abs" style="left:84px;right:84px;bottom:90px;display:flex;justify-content:space-between;align-items:end;font:600 28px 'Inter Tight'"><span>Tiago Azevedo · Rafael Araújo Veras<br><span style="opacity:.7">OAB/MA</span></span><span class="viv">@curso_processo_legislativo_</span></div></div>` },
};
(async () => {
  const b = await chromium.launch(); const p = await b.newPage();
  for (const [nome, x] of Object.entries(P)) {
    await p.setViewportSize({ width: x.w, height: x.h });
    await p.setContent(`<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@400;500;600;700;800&display=swap" rel="stylesheet"><style>${base}</style></head><body>${x.html}</body></html>`, { waitUntil: 'networkidle' });
    await p.waitForTimeout(500);
    const arq = { prancha: 'prancha.png', s1: 'story-01.png', s2: 'story-02.png', s3: 'story-03.png', post: 'post-01.png' }[nome];
    await p.screenshot({ path: path.join(D, arq) }); console.log('ok', arq);
  }
  await b.close();
})();
