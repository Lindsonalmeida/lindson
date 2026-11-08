// Curso de Processo Legislativo · "Hemiciclo Premium" (conta Leandro, 08/11/2026). Agente: designer-grafico (branch principal, conta Zuleide).
// Pedido do Lindson: "baseado nas novas informações do repositório e novos agentes, recrie a identidade visual dele para algo super premium".
// Base (privado, dados/agencia/referencias/): social-media-advocacia (2.987 artes Behance), pinterest-advocacia (2.062 pins),
// identidades-visuais-advocacia (top 10) e amaral-velasco. Evolui a Hemiciclo aprovada em 08/11 (mantém o § no hemiciclo e o verde).
// O que muda para "premium", tirado das pesquisas:
//  · o advogado é o protagonista (50–70% da arte), recortado, luz quente de contorno, cor de cinema e grão (Pinterest §1 e §5; Behance §1);
//  · paleta curta: verde-escuro + creme + acento metálico só em detalhe (Pinterest §2: "vinho ou verde-escuro + creme"; Behance: acento metálico);
//  · 1 palavra em itálico serifado no título (Behance §1; Pinterest §3), título em sans bold;
//  · palavra gigante atrás das pessoas, cortada pela borda (estilo E "Black & Gold Autoridade" e Pinterest §3);
//  · assinatura gráfica que atravessa o carrossel: o arco do plenário (estilo F); rodapé fixo com logo, nomes, OAB e nº do slide.
// Uso: SOCIOS=<privado>/dados/clientes-arquivos/curso/socios SAIDA=<pasta> node gerar.js  (peças com rosto ficam fora do Git)
const { chromium } = require('playwright'), path = require('path'), fs = require('fs');
const SOC = process.env.SOCIOS || '/home/user/centrallindsonalmeida/dados/clientes-arquivos/curso/socios', OUT = process.env.SAIDA || __dirname;
const img = f => { const p = path.join(SOC, f); return fs.existsSync(p) ? 'data:image/png;base64,' + fs.readFileSync(p).toString('base64') : ''; };
const T = img('cut-tiago-azevedo/recorte-limpo.png'), R = img('cut-rafael-araujo-veras/recorte-limpo.png');
const C = { v: '#0A1F17', v2: '#123528', cr: '#EFE6D4', la: '#C8A96B', la2: '#E6CF9C', mu: '#8FA79A' };
const css = `*{box-sizing:border-box;margin:0;padding:0}html,body{background:#000}
.a{position:relative;overflow:hidden;background:${C.v};color:${C.cr};font-family:'Inter Tight',sans-serif}
.abs{position:absolute}.t{font-weight:800;letter-spacing:-.035em;line-height:.98}
.it{font-family:'Instrument Serif',serif;font-style:italic;font-weight:400;letter-spacing:-.01em;color:${C.la2}}
.r{font:600 20px 'Inter Tight';letter-spacing:.24em;text-transform:uppercase}
.luz{background:radial-gradient(ellipse at 50% 30%,rgba(200,169,107,.28),transparent 60%)}
.grao{position:absolute;inset:0;pointer-events:none;opacity:.10;mix-blend-mode:overlay;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='220' height='220'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='3'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E")}
.vin{position:absolute;inset:0;pointer-events:none;background:radial-gradient(ellipse at 50% 45%,transparent 55%,rgba(0,0,0,.55) 100%)}
.pes{filter:drop-shadow(0 30px 40px rgba(0,0,0,.55)) drop-shadow(-6px -4px 0 rgba(200,169,107,.0)) saturate(.92) contrast(1.06) sepia(.12)}
.fio{position:absolute;height:1px;background:linear-gradient(90deg,transparent,${C.la},transparent)}`;
const arcos = (cx, cy, r0, n, gap, op) => { let s = ''; for (let i = 0; i < n; i++) { const r = r0 + i * gap;
  s += `<path d="M ${cx - r} ${cy} A ${r} ${r} 0 0 1 ${cx + r} ${cy}" fill="none" stroke="${C.la}" stroke-opacity="${op * (1 - i / (n + 2))}" stroke-width="1.6"/>`;
  const k = 9 + i * 3; for (let j = 1; j < k; j++) { const a = Math.PI - Math.PI * j / k; s += `<circle cx="${cx + r * Math.cos(a)}" cy="${cy - r * Math.sin(a)}" r="2.6" fill="${C.la}" fill-opacity="${op * .9 * (1 - i / (n + 2))}"/>`; } } return s; };
const simb = (t, bg, fg) => `<svg width="${t}" height="${t}" viewBox="0 0 200 200"><rect width="200" height="200" rx="100" fill="${bg}"/><circle cx="100" cy="100" r="92" fill="none" stroke="${fg}" stroke-opacity=".5" stroke-width="2"/>
  <path d="M 36 146 A 64 64 0 0 1 164 146" fill="none" stroke="${fg}" stroke-width="7" stroke-linecap="round"/><path d="M 62 146 A 38 38 0 0 1 138 146" fill="none" stroke="${fg}" stroke-opacity=".45" stroke-width="5" stroke-linecap="round"/>
  <text x="100" y="134" text-anchor="middle" font-family="Instrument Serif" font-style="italic" font-size="96" fill="${fg}">§</text></svg>`;
const logo = (s = 1, cor = C.cr, it = C.la2) => `<div style="display:flex;align-items:center;gap:${16 * s}px">${simb(70 * s, C.v2, C.la)}<div style="line-height:1"><div style="font:800 ${32 * s}px 'Inter Tight';letter-spacing:-.03em;color:${cor}">Processo <span class="it" style="font-size:${36 * s}px;color:${it}">Legislativo</span></div><div style="font:600 ${11 * s}px 'Inter Tight';letter-spacing:.3em;text-transform:uppercase;color:${C.mu};margin-top:${8 * s}px">Curso · Câmara municipal</div></div></div>`;
const rodape = (n, tot, w) => `<div class="fio" style="left:72px;right:72px;bottom:118px"></div><div class="abs" style="left:72px;right:72px;bottom:62px;display:flex;justify-content:space-between;align-items:center;font:600 20px 'Inter Tight';color:${C.mu}">
  <span>Tiago Azevedo · Rafael Araújo Veras · <b style="color:${C.cr}">OAB/MA</b></span><span style="font-family:'Instrument Serif';font-style:italic;font-size:26px;color:${C.la2}">${n}<span style="opacity:.6">/${tot}</span></span></div>`;
const P = {
 'prancha.png': [1920, 1080, `<div class="a" style="width:1920px;height:1080px"><div class="abs luz" style="inset:0"></div>
   <svg class="abs" style="left:0;top:0" width="1920" height="1080">${arcos(1420, 1180, 240, 9, 64, .55)}</svg>
   <div class="abs t" style="left:930px;top:140px;font-size:300px;color:${C.v2};letter-spacing:-.05em;white-space:nowrap">PLENÁRIO</div>
   <img class="abs pes" src="${R}" style="left:1430px;bottom:-40px;height:860px"><img class="abs pes" src="${T}" style="left:1010px;bottom:-60px;height:900px">
   <div class="abs" style="left:0;right:0;bottom:0;height:240px;background:linear-gradient(180deg,transparent,${C.v})"></div>
   <div class="abs" style="left:96px;top:90px">${logo(1.25)}</div>
   <div class="abs r" style="left:96px;top:300px;color:${C.la}">Identidade · Hemiciclo Premium</div>
   <div class="abs t" style="left:96px;top:345px;font-size:86px;width:860px">Saia do improviso.<br>Atue com <span class="it" style="font-size:100px">segurança.</span></div>
   <div class="abs" style="left:96px;top:690px;display:flex;gap:18px">${[[C.v, 'Verde plenário', '60%', 1], [C.v2, 'Musgo', '25%', 1], [C.cr, 'Creme', '10%'], [C.la, 'Latão · só detalhe', '5%']].map(([c, n, p, b]) => `<div style="width:190px"><div style="height:120px;border-radius:18px;background:${c};${b ? 'border:1px solid rgba(239,230,212,.25)' : ''}"></div><div style="font:700 19px 'Inter Tight';margin-top:12px">${n}</div><div style="font:500 16px 'Inter Tight';color:${C.mu}">${c.toUpperCase()} · ${p}</div></div>`).join('')}</div>
   <div class="abs" style="left:96px;top:955px;font:500 19px/1.5 'Inter Tight';color:${C.mu};width:820px">Inter Tight 800 no título, <span class="it" style="font-size:24px">Instrument Serif itálica</span> em 1 palavra de destaque. O professor é o protagonista. O arco atravessa o carrossel. Rodapé fixo: nomes, OAB e nº do slide.</div>
   <div class="grao"></div><div class="vin"></div></div>`],
 'carrossel-01.png': [1080, 1350, `<div class="a" style="width:1080px;height:1350px"><div class="abs luz" style="inset:0"></div>
   <svg class="abs" style="left:0;top:0" width="1080" height="1350">${arcos(1080, 980, 200, 8, 70, .6)}</svg>
   <div class="abs t" style="left:-30px;top:250px;font-size:250px;color:${C.v2};letter-spacing:-.05em;white-space:nowrap">LEGISLATIVO</div>
   <img class="abs pes" src="${R}" style="left:520px;top:300px;height:820px"><img class="abs pes" src="${T}" style="left:110px;top:290px;height:850px">
   <div class="abs" style="left:0;right:0;top:820px;height:530px;background:linear-gradient(180deg,transparent,${C.v} 42%)"></div>
   <div class="abs" style="left:72px;top:72px">${logo(.95)}</div>
   <div class="abs r" style="left:72px;top:960px;color:${C.la}">Turma básica</div>
   <div class="abs t" style="left:72px;right:72px;top:1000px;font-size:82px">Chega de improviso na <span class="it" style="font-size:96px">câmara.</span></div>
   ${rodape(1, 3)}<div class="grao"></div><div class="vin"></div></div>`],
 'carrossel-02.png': [1080, 1350, `<div class="a" style="width:1080px;height:1350px">
   <svg class="abs" style="left:0;top:0" width="1080" height="1350">${arcos(0, 980, 200, 8, 70, .6)}</svg>
   <div class="abs" style="left:72px;top:72px">${logo(.95)}</div>
   <div class="abs r" style="left:72px;top:270px;color:${C.la}">O que você vai dominar</div>
   <div class="abs t" style="left:72px;right:72px;top:320px;font-size:76px">O rito, do protocolo à <span class="it" style="font-size:90px">votação.</span></div>
   <div class="abs" style="left:72px;right:72px;top:600px">${['Quem pode propor cada projeto', 'Quando vale o regime de urgência', 'Quórum e o que anula uma votação', 'Sessão, pauta e prazos'].map((x, i) => `<div style="display:flex;align-items:baseline;gap:30px;padding:26px 0;border-top:1px solid rgba(200,169,107,.28)"><span class="it" style="font-size:58px;min-width:70px">0${i + 1}</span><span style="font:600 40px 'Inter Tight';letter-spacing:-.01em">${x}</span></div>`).join('')}</div>
   ${rodape(2, 3)}<div class="grao"></div><div class="vin"></div></div>`],
 'carrossel-03.png': [1080, 1350, `<div class="a" style="width:1080px;height:1350px;background:${C.cr};color:${C.v}">
   <svg class="abs" style="left:0;top:0" width="1080" height="1350">${arcos(540, 1350, 260, 8, 66, .7)}</svg>
   <div class="abs" style="left:72px;top:72px">${logo(.95, C.v, '#8A6A2E')}</div>
   <div class="abs" style="left:300px;top:330px;width:480px;height:480px;border-radius:50%;overflow:hidden;background:${C.v}">
     <img src="${T}" style="position:absolute;left:30px;top:40px;height:520px"></div>
   <div class="abs" style="left:300px;top:330px;width:480px;height:480px;border-radius:50%;border:2px solid ${C.la}"></div>
   <div class="abs t" style="left:72px;right:72px;top:880px;font-size:78px;text-align:center">Vagas por <span class="it" style="font-size:92px;color:#9A7B3F">turma.</span></div>
   <div class="abs" style="left:240px;right:240px;top:1040px;text-align:center;padding:26px 0;border-radius:99px;background:${C.v};color:${C.cr};font:700 30px 'Inter Tight'">Responda CURSO no direct</div>
   <div class="fio" style="left:72px;right:72px;bottom:118px;background:linear-gradient(90deg,transparent,#9A7B3F,transparent)"></div>
   <div class="abs" style="left:72px;right:72px;bottom:62px;display:flex;justify-content:space-between;font:600 20px 'Inter Tight';color:#5E6F66"><span>Tiago Azevedo · Rafael Araújo Veras · <b style="color:${C.v}">OAB/MA</b></span><span style="font-family:'Instrument Serif';font-style:italic;font-size:26px;color:#9A7B3F">3<span style="opacity:.6">/3</span></span></div>
   <div class="grao"></div></div>`],
 'avatar.png': [1080, 1080, `<div class="a" style="width:1080px;height:1080px;display:flex;align-items:center;justify-content:center"><div class="abs luz" style="inset:0"></div>${simb(820, C.v2, C.la)}<div class="grao"></div></div>`],
};
(async () => {
  const b = await chromium.launch(); const p = await b.newPage();
  for (const [arq, [w, h, html]] of Object.entries(P)) {
    await p.setViewportSize({ width: w, height: h });
    await p.setContent(`<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@400;500;600;700;800&family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet"><style>${css}</style></head><body>${html}</body></html>`, { waitUntil: 'networkidle' });
    await p.waitForTimeout(600); await p.screenshot({ path: path.join(OUT, arq) }); console.log('ok', arq);
  }
  await b.close();
})();
