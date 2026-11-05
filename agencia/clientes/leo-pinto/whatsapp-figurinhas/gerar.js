// Figurinhas de WhatsApp do Leo Pinto (conta Leandro, 05/11/2026). Uso: node gerar.js <pasta privada com recortes/> → <pasta>/brutas/NN.png (1024x1024, fundo transparente)
// Depois: python3 acabamento.py <pasta> → contorno branco, sombra, 512x512 em .webp (< 100 KB) e .png, e o ícone do pacote (96x96).
// Composição copiada de (TEMPLATE.md):
//  1. Figurinhas do Álvaro Uribe (Colômbia): o rosto real recortado, uma expressão por figurinha, nada em volta.
//  2. Figurinhas de campanha no GIPHY (EUA): contorno branco grosso de "adesivo recortado" e texto curto e pesado.
//  3. Pacotes oficiais do WhatsApp com os ídolos do Egito e do Al Ahly: cada figurinha é uma reação do dia a dia e o pacote
//     inteiro segue um padrão só.
// Regras do Leo: só fontes, cores e foto (nada de raio, faixa, ícone, sol); situação; nada de pedir voto ou número.
const { chromium } = require('playwright'); const fs = require('fs'), path = require('path');
const MAR = '#05316E', ROY = '#2350F5', SOL = '#FFC20E', LAR = '#FF7A1A';
const caixa = { sol: [SOL, MAR], lar: [LAR, '#fff'], roy: [ROY, '#fff'], mar: [MAR, '#fff'] };
// [arquivo do recorte, linhas da caixa, cor, frase manuscrita (acima da caixa; abaixo quando a linha termina em vírgula), altura da foto, deslocamento x, base da foto]
const F = [
  ['a-close-laranja', ['BOM DIA,'], 'sol', 'meu povo!', 700, 0],
  ['b-punho', ['TAMO', 'JUNTO!'], 'lar', '', 720, 20],
  ['c-maos-juntas-laranja', ['OBRIGADO!'], 'roy', '', 800, 0],
  ['d-bracos-cruzados-branca', ['TÁ FEITO!'], 'sol', 'Pediu?', 760, 0],
  ['e-celular', ['ME CHAMA NO ZAP!'], 'lar', '', 720, 0, 250],
  ['f-punhos', ['BORA', 'TRABALHAR!'], 'roy', '', 820, 0],
  ['g-maos-juntas-amarela', ['KKKKKK'], 'sol', '', 760, 0],
  ['h-close-amarela', ['BOA NOITE!'], 'mar', '', 700, 0],
  ['i-maos-abertas-branca', ['CONTE', 'COMIGO!'], 'lar', '', 820, 0],
  ['j-close-sorrindo', ['PARABÉNS!'], 'roy', 'Felicidades!', 760, 0],
];
(async () => {
  const pasta = path.resolve(process.argv[2]); fs.mkdirSync(path.join(pasta, 'brutas'), { recursive: true });
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1024, height: 1024 } });
  for (const [i, [arq, linhas, cor, script, alt, dx, base = 72]] of F.entries()) {
    const foto = 'data:image/png;base64,' + fs.readFileSync(path.join(pasta, 'recortes', arq + '.png')).toString('base64');
    const [bg, fg] = caixa[cor]; const mx = Math.max(...linhas.map(l => l.length)); const tam = mx > 12 ? 84 : mx > 8 ? 104 : 128; const depois = linhas[linhas.length - 1].endsWith(',');
    const html = `<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@1,900&family=Kaushan+Script&display=swap" rel="stylesheet">
<style>html,body{margin:0;background:transparent}#c{position:relative;width:1024px;height:1024px;overflow:hidden}
#foto{position:absolute;left:50%;bottom:${base}px;height:${alt}px;max-width:900px;object-fit:contain;transform:translateX(calc(-50% + ${dx}px))}
#txt{position:absolute;left:0;right:0;bottom:${depois ? 20 : 70}px;display:flex;flex-direction:column;align-items:center;transform:rotate(-5deg)}
.cx{background:${bg};color:${fg};font:italic 900 ${tam}px/0.95 Montserrat;letter-spacing:-.02em;padding:14px 34px 18px;margin-top:-6px;box-shadow:0 12px 0 ${cor === 'mar' ? ROY : MAR}}
.sc{font:${script.length > 8 ? 84 : 96}px 'Kaushan Script';color:${cor === 'sol' || cor === 'mar' ? '#fff' : SOL};margin-bottom:-14px;
 -webkit-text-stroke:14px ${MAR};paint-order:stroke fill;transform:rotate(-3deg)}</style></head>
<body><div id="c"><img id="foto" src="${foto}">
<div id="txt">${script && !depois ? `<div class="sc">${script}</div>` : ''}${linhas.map(l => `<div class="cx">${l}</div>`).join('')}${script && depois ? `<div class="sc" style="margin:-4px 0 0 260px">${script}</div>` : ''}</div></div></body></html>`;
    await p.setContent(html, { waitUntil: 'networkidle' }); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(200);
    const n = String(i + 1).padStart(2, '0');
    await (await p.$('#c')).screenshot({ path: path.join(pasta, 'brutas', `${n}-${arq}.png`), omitBackground: true }); console.log(n, arq);
  }
  await b.close();
})();
