// Prancha da marca v10 do curso de processo legislativo (1600x900).
// Cores e tipografia conforme BRANDBOOK-V10.md. Não cria capas.
// Uso: node gerar-marca-v10.js   (Node + Playwright, com --no-sandbox)
const { chromium } = require('playwright');
const path = require('path');

const CSS = `*{box-sizing:border-box;margin:0;padding:0}
:root{--preto:#080808;--dourado:#A89048;--highlight:#C8A860;--sombra:#6E5A2A;--branco:#F8F8F8;--cinza:#777671;--marrom:#2A1E0F}
html,body{width:1600px;height:900px;background:var(--preto)}
.board{position:relative;width:1600px;height:900px;overflow:hidden;color:var(--branco);
  font-family:Inter,Arial,sans-serif;
  background:radial-gradient(1100px 760px at 0% 0%, var(--marrom) 0%, var(--preto) 60%), var(--preto);
  padding:52px 72px;overflow:hidden}
.top{display:flex;justify-content:space-between;align-items:center;height:40px}
.rot{font-weight:700;font-size:22px;letter-spacing:.14em;text-transform:uppercase;color:var(--cinza)}
.rule{height:2px;background:var(--dourado);margin:18px 0 26px;width:100%;opacity:.9}
.grid{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.1fr);gap:56px;height:610px}
.col-h{display:flex;flex-direction:column;gap:14px;min-width:0}
.box{position:relative;display:flex;align-items:center;justify-content:center;border-radius:6px}
.logo{font-family:'Inter Display',Inter,Arial,sans-serif;font-weight:800;text-transform:uppercase;letter-spacing:.035em;white-space:nowrap;line-height:1}
.logo .p{color:var(--branco)} .logo .l{color:var(--dourado)}
.logo.inv{color:var(--preto)}
.head{font-family:'Inter Display',Inter,Arial,sans-serif;font-weight:800;font-size:64px;line-height:1.02;letter-spacing:-.025em;margin-top:8px}
.gold{color:var(--dourado)}
.bullets{display:flex;flex-direction:column;gap:8px;font-size:22px;line-height:1.3;color:rgba(248,248,248,.9)}
.bullets b{color:var(--dourado);font-weight:700}
.sw{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
.card{display:flex;flex-direction:column;gap:6px;min-width:0}
.chip{height:104px;border-radius:6px}
.hex{font-size:22px;font-weight:700;letter-spacing:.02em}
.desc{font-size:18px;line-height:1.25;color:var(--cinza)}
.scale{margin-top:22px;display:flex;flex-direction:column;gap:12px;border-top:1px solid rgba(248,248,248,.12);padding-top:18px}
.srow{display:flex;align-items:baseline;justify-content:space-between;gap:24px}
.srow .lab{font-size:18px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--cinza);width:150px;flex:none}
.srow .s1{font-family:'Inter Display',Inter,sans-serif;font-weight:800;font-size:72px;line-height:1;letter-spacing:-.025em;white-space:nowrap}
.srow .s2{font-family:'Inter Display',Inter,sans-serif;font-weight:800;font-size:44px;line-height:1;letter-spacing:-.02em;white-space:nowrap}
.srow .s3{font-size:36px;line-height:1;white-space:nowrap}
.srow .s4{font-size:28px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;white-space:nowrap}
.foot{position:absolute;left:72px;right:72px;bottom:36px;display:flex;justify-content:space-between;gap:24px}
.foot span{font-size:20px;color:var(--cinza)}
.foot .h{color:var(--branco);font-weight:700}
`;

const swatches = [
  { hex: '#080808', name: 'Preto · fundo', bg: '#080808', border: true, d: 'Fundo e texto invertido' },
  { hex: '#A89048', name: 'Dourado fosco · destaque', bg: '#A89048', d: 'Até 2 palavras por peça' },
  { hex: '#C8A860', name: 'Highlight · brilho', bg: '#C8A860', d: 'Só filete e reflexo, nunca texto' },
  { hex: '#6E5A2A', name: 'Sombra · dourado', bg: '#6E5A2A', d: 'Bordas e faixas sobre o dourado' },
  { hex: '#F8F8F8', name: 'Branco · texto', bg: '#F8F8F8', d: 'Texto principal' },
  { hex: '#777671', name: 'Cinza-quente · DERIVADO', bg: '#777671', d: 'Rótulos e legendas (ver brandbook)' },
];

const cardsHtml = swatches.map(s => `
  <div class="card">
    <div class="chip" style="background:${s.bg};${s.border ? 'box-shadow:inset 0 0 0 2px #2b2b2b' : ''}"></div>
    <div class="hex">${s.hex}</div>
    <div class="desc" style="color:#F8F8F8">${s.name}</div>
    <div class="desc">${s.d}</div>
  </div>`).join('');

const HTML = `<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>${CSS}</style></head><body>
<section class="board">
  <div class="top">
    <div class="rot">Marca · Curso de processo legislativo · v10</div>
    <div class="rot">@curso_processo_legislativo_</div>
  </div>
  <div class="rule"></div>

  <div class="grid">
    <div class="col-h">
      <div class="rot">Logo em texto · positiva</div>
      <div class="box" style="height:130px;background:#080808;box-shadow:inset 0 0 0 2px #1d1d1d">
        <div class="logo" style="font-size:38px"><span class="p">Processo</span> <span class="l">Legislativo</span></div>
      </div>
      <div class="rot">Logo em texto · invertida</div>
      <div class="box" style="height:110px;background:#A89048">
        <div class="logo inv" style="font-size:38px">Processo Legislativo</div>
      </div>
      <div class="head">Entenda <span class="gold">antes</span> de votar.</div>
      <div class="bullets">
        <div><b>Dourado:</b> até 2 palavras por peça, sempre no título.</div>
        <div><b>Margens:</b> 8% das laterais e 7% de cima e de baixo.</div>
        <div><b>Pessoa</b> à direita, rosto no terço superior, foto real.</div>
        <div><b>Handle</b> no rodapé, à esquerda, em todas as peças.</div>
      </div>
    </div>

    <div class="col-h">
      <div class="rot">Paleta · hexadecimais</div>
      <div class="sw">${cardsHtml}</div>
      <div class="scale">
        <div class="rot" style="margin-bottom:4px">Tipografia · Inter Display 800 (título) · Inter (texto e rótulo)</div>
        <div class="srow"><div class="lab">Título</div><div class="s1">Pode votar?</div></div>
        <div class="srow"><div class="lab">Subtítulo</div><div class="s2">Quórum e votação</div></div>
        <div class="srow"><div class="lab">Texto</div><div class="s3">Texto corrido, peso 400, com entrelinha de 1,4.</div></div>
        <div class="srow"><div class="lab">Rótulo</div><div class="s4">Caixa alta · tracking 0,14</div></div>
      </div>
    </div>
  </div>

  <div class="foot">
    <span class="h">Brandbook v10 · pendente de aprovação do Lindson</span>
    <span>Fundo: degradê marrom-escuro #2A1E0F no canto superior esquerdo, até #080808</span>
  </div>
</section></body></html>`;

(async () => {
  const b = await chromium.launch({ args: ['--no-sandbox'] });
  const p = await b.newPage({ viewport: { width: 1600, height: 900 }, deviceScaleFactor: 1 });
  await p.setContent(HTML, { waitUntil: 'load' });
  await p.evaluate(() => document.fonts.ready);
  await (await p.$('section')).screenshot({ path: path.join(__dirname, 'marca-v10.png') });
  await b.close();
  console.log('ok');
})().catch(e => { console.error(e.message); process.exit(1); });
