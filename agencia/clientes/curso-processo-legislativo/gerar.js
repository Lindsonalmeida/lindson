// Gera as 9 capas de Reels (1080x1920), a prancha das duas direções e o avatar provisório.
// Uso: cd agencia/clientes/curso-processo-legislativo && node gerar.js
// Direção aprovada para as capas: A "Ata" (ver identidade/DIRECOES.md). Dependência: Playwright (Chromium).
const { chromium } = require('playwright');
const path = require('path');

const FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,600;1,400;1,600&family=Inter:wght@400;600;800&display=swap" rel="stylesheet">';

const BASE_CSS = `
:root{--bg:#F1EBDD;--ink:#1D1B17;--red:#A4402A;--mute:#6B645A;--paper:#FBF8F1}
*{box-sizing:border-box;margin:0;padding:0}
body{background:#777}
.capa{width:1080px;height:1920px;position:relative;overflow:hidden;background:var(--bg);color:var(--ink);font-family:'Inter','Liberation Sans',Arial,sans-serif}
.inv{background:var(--ink);color:var(--bg)}
.inv .red{color:#E9876E}
.inv .foot{color:#CDC4B2}
.logo{position:absolute;top:96px;left:96px;right:96px;display:flex;align-items:baseline;gap:18px;font-family:'Fraunces','Liberation Serif',Georgia,serif;font-size:60px;font-weight:600;letter-spacing:-.01em}
.logo i{font-weight:400}
.tag{font-family:'Inter',Arial,sans-serif;font-size:22px;font-weight:800;letter-spacing:.28em;text-transform:uppercase;border:2px solid currentColor;padding:8px 14px;align-self:center}
.foot{position:absolute;bottom:96px;left:96px;right:96px;display:flex;justify-content:space-between;white-space:nowrap;font-family:'Inter',Arial,sans-serif;font-size:21px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:var(--mute)}
.rule{position:absolute;left:96px;right:96px;height:3px;background:currentColor}
.t{position:absolute;left:96px;right:96px;font-family:'Fraunces','Liberation Serif',Georgia,serif;font-weight:600;letter-spacing:-.02em;line-height:.98}
.red{color:var(--red)}
.k{position:absolute;left:96px;font-family:'Inter',Arial,sans-serif;font-size:26px;font-weight:800;letter-spacing:.24em;text-transform:uppercase;color:var(--mute)}
.inv .k{color:#CDC4B2}
`;

const LOGO = '<div class="logo"><span>Processo</span><i>Legislativo</i><span class="tag">Curso</span></div>';
const FOOT = '<div class="foot"><span>Curso de processo legislativo</span><span>@curso_processo_legislativo_</span></div>';
const wrap = (cls, inner) => `<section class="capa ${cls}">${inner}</section>`;

const CAPAS = [
  // 01 cor invertida: título em carvão, palavra vermelha
  ['capa-01-urgencia', wrap('inv', LOGO +
    '<div class="rule" style="top:330px"></div>' +
    '<div class="k" style="top:380px">Regime de urgência</div>' +
    '<div class="t" style="top:460px;font-size:150px">O que muda no <span class="red">regime de urgência</span>?</div>' + FOOT)],
  // 02 número de fundo: "?" gigante ao fundo
  ['capa-02-pode-votar', wrap('', LOGO +
    '<div class="t" style="top:300px;font-size:1400px;opacity:.07;left:0;right:0;text-align:center;line-height:1">?</div>' +
    '<div class="k" style="top:560px">Votação</div>' +
    '<div class="t" style="top:620px;font-size:132px">Pode votar sem <span class="red">quórum</span>?</div>' + FOOT)],
  // 03 problema × solução: metade clara e metade carvão
  ['capa-03-projeto-tramitar', wrap('', LOGO +
    '<div class="k" style="top:400px">Problema</div>' +
    '<div class="t" style="top:470px;font-size:124px">Um projeto pode tramitar <span class="red">sem parecer</span>?</div>' +
    '<div style="position:absolute;left:0;right:0;top:1000px;bottom:0;background:var(--ink);color:var(--bg)"></div>' +
    '<div class="k" style="top:1090px;color:#CDC4B2">Solução</div>' +
    '<div class="t" style="top:1160px;font-size:112px;color:var(--bg)">Veja a regra que vale na <span style="color:#E9876E">sua casa</span>.</div>' + FOOT)],
  // 04 palavra gigante: "DEVIDO" enche a largura
  ['capa-04-devido-processo', wrap('', LOGO +
    '<div class="k" style="top:360px">O que é</div>' +
    '<div class="t red" style="top:420px;font-size:230px;letter-spacing:-.04em">DEVIDO</div>' +
    '<div class="t" style="top:680px;font-size:168px;letter-spacing:-.04em">PROCESSO</div>' +
    '<div class="t" style="top:900px;font-size:150px;font-style:italic;font-weight:400">legislativo?</div>' + FOOT)],
  // 05 cartão: bloco claro com borda sobre o fundo
  ['capa-05-sessao-secreta', wrap('', LOGO +
    '<div style="position:absolute;left:96px;right:96px;top:460px;height:920px;background:var(--paper);border:3px solid var(--ink);box-shadow:16px 16px 0 var(--ink)"></div>' +
    '<div class="k" style="top:560px;left:150px">Caso prático</div>' +
    '<div class="t" style="top:630px;left:150px;right:150px;font-size:118px">Sessão secreta pode <span class="red">acontecer</span>?</div>' + FOOT)],
  // 06 faixas: três bandas horizontais
  ['capa-06-principio', wrap('', LOGO +
    '<div style="position:absolute;left:0;right:0;top:420px;height:360px;background:var(--red)"></div>' +
    '<div class="k" style="top:470px;color:#F6E6DD">Princípio</div>' +
    '<div style="position:absolute;left:0;right:0;top:780px;height:560px;background:var(--ink)"></div>' +
    '<div class="t" style="top:860px;font-size:124px;color:var(--bg)">O que é o princípio da <span style="color:#E9876E">publicidade</span>?</div>' +
    '<div style="position:absolute;left:0;right:0;top:1340px;height:120px;border-top:3px solid var(--ink);border-bottom:3px solid var(--ink)"></div>' + FOOT)],
  // 07 anel com monograma
  ['capa-07-medida-provisoria', wrap('', LOGO +
    '<div style="position:absolute;left:190px;top:460px;width:700px;height:700px;border-radius:50%;border:44px solid var(--red);display:flex;align-items:center;justify-content:center;font-family:Fraunces,\'Liberation Serif\',serif;font-weight:600;font-size:260px;color:var(--red)">MP</div>' +
    '<div class="t" style="top:1260px;font-size:124px">O que é <span class="red">medida provisória</span>?</div>' + FOOT)],
  // 08 frase de impacto
  ['capa-08-quorum', wrap('', LOGO +
    '<div class="k" style="top:360px">Quórum</div>' +
    '<div class="t red" style="top:470px;font-size:360px;line-height:.7">“</div>' +
    '<div class="t" style="top:700px;font-size:138px;font-style:italic;font-weight:400">Quórum é o número mínimo para a votação valer.</div>' +
    '<div class="t" style="top:1330px;font-size:70px;font-weight:600">O que é quórum de votação?</div>' + FOOT)],
  // 09 número grande
  ['capa-09-quem-propoe', wrap('', LOGO +
    '<div class="t red" style="top:330px;font-size:760px;left:0;right:0;text-align:center;letter-spacing:-.04em;line-height:1">PL</div>' +
    '<div class="t" style="top:1200px;font-size:124px">Quem pode <span class="red">propor</span> um projeto de lei?</div>' + FOOT)],
];

const BOARD = `
<section style="width:1600px;height:900px;display:flex;font-family:'Inter',Arial,sans-serif">
  <div style="width:800px;height:900px;background:#F1EBDD;color:#1D1B17;padding:70px;position:relative">
    <div style="font-size:24px;font-weight:800;letter-spacing:.24em;color:#6B645A">DIREÇÃO A · ATA · usada nas capas</div>
    <div style="font-family:'Fraunces','Liberation Serif',serif;font-size:96px;font-weight:600;margin-top:40px;line-height:1">Processo <i style="font-weight:400">Legislativo</i></div>
    <div style="font-family:'Fraunces','Liberation Serif',serif;font-size:72px;font-weight:600;margin-top:40px;line-height:1.02">O que é <span style="color:#A4402A">medida provisória</span>?</div>
    <div style="display:flex;gap:18px;margin-top:70px">
      <div style="width:150px;height:150px;background:#F1EBDD;border:2px solid #1D1B17"></div>
      <div style="width:150px;height:150px;background:#1D1B17"></div>
      <div style="width:150px;height:150px;background:#A4402A"></div>
      <div style="width:150px;height:150px;background:#6B645A"></div>
    </div>
    <div style="font-size:24px;line-height:1.5;margin-top:40px;color:#1D1B17">Papel marfim #F1EBDD · carvão #1D1B17 · vermelho-tijolo #A4402A · cinza #6B645A<br>Títulos: Fraunces (serifa, peso 600) · Textos e rótulos: Inter<br>Regra: vermelho só numa palavra por peça; carvão nas peças invertidas.</div>
  </div>
  <div style="width:800px;height:900px;background:#10291F;color:#ECE6D6;padding:70px;position:relative">
    <div style="font-size:24px;font-weight:800;letter-spacing:.24em;color:#D8A24A">DIREÇÃO B · REGIMENTO · alternativa</div>
    <div style="font-family:'Inter',Arial,sans-serif;font-size:92px;font-weight:800;margin-top:40px;line-height:.95;letter-spacing:-.02em">PROCESSO<br><span style="color:#D8A24A">LEGISLATIVO</span></div>
    <div style="font-family:'JetBrains Mono',monospace;font-size:44px;margin-top:60px;color:#D8A24A">ART. 01 — REGRA DA SESSÃO</div>
    <div style="display:flex;gap:18px;margin-top:70px">
      <div style="width:150px;height:150px;background:#10291F;border:2px solid #ECE6D6"></div>
      <div style="width:150px;height:150px;background:#ECE6D6"></div>
      <div style="width:150px;height:150px;background:#D8A24A"></div>
      <div style="width:150px;height:150px;background:#3E5A4D"></div>
    </div>
    <div style="font-size:24px;line-height:1.5;margin-top:40px">Verde-floresta #10291F · creme #ECE6D6 · âmbar #D8A24A · musgo #3E5A4D<br>Títulos: Inter peso 800 · Numeração de artigo: JetBrains Mono<br>Regra: todo post numera a regra (ART. 01, 02…) e usa a palavra-chave em âmbar.</div>
  </div>
</section>`;

(async () => {
  const dir = __dirname;
  const browser = await chromium.launch({ args: ['--no-sandbox'] });
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
  const html = `<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">${FONTS}<style>${BASE_CSS}</style></head><body>${CAPAS.map(c => c[1]).join('')}</body></html>`;
  await page.setContent(html, { waitUntil: 'load' });
  await page.evaluate(() => document.fonts.ready);
  const sections = await page.$$('section.capa');
  for (let i = 0; i < sections.length; i++) {
    await sections[i].screenshot({ path: path.join(dir, 'capas', CAPAS[i][0] + '.png') });
  }
  // prancha das duas direções
  const board = await browser.newPage({ viewport: { width: 1600, height: 900 }, deviceScaleFactor: 1 });
  await board.setContent(`<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">${FONTS}</head><body style="margin:0">${BOARD}</body></html>`, { waitUntil: 'load' });
  await board.evaluate(() => document.fonts.ready);
  await (await board.$('section')).screenshot({ path: path.join(dir, 'identidade', 'direcoes.png') });
  // avatar provisório de marca (sem pessoas)
  const av = await browser.newPage({ viewport: { width: 1080, height: 1080 }, deviceScaleFactor: 1 });
  await av.setContent(`<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">${FONTS}<style>${BASE_CSS}</style></head><body style="margin:0"><section style="width:1080px;height:1080px;background:#1D1B17;color:#F1EBDD;position:relative;font-family:'Fraunces','Liberation Serif',serif;display:flex;flex-direction:column;align-items:center;justify-content:center"><div style="font-size:150px;font-weight:600;line-height:1">Processo</div><div style="font-size:150px;font-style:italic;line-height:1.1">Legislativo</div><div style="font-family:Inter,Arial,sans-serif;font-size:30px;font-weight:800;letter-spacing:.3em;margin-top:40px;border:2px solid #F1EBDD;padding:12px 20px">CURSO</div></section></body></html>`, { waitUntil: 'load' });
  await av.evaluate(() => document.fonts.ready);
  await (await av.$('section')).screenshot({ path: path.join(dir, 'avatar', 'avatar-marca-provisoria.png') });
  await browser.close();
  console.log('ok:', sections.length, 'capas + direcoes.png + avatar');
})().catch(e => { console.error('FALHOU:', e.message); process.exit(1); });
