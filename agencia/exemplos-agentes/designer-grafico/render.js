// Uso: python3 gerar.py && node render.js  -> prancha.png e aplicacoes.png (1440 de largura). Designer gráfico, conta Zuleide, 08/11/2026.
const { chromium } = require('playwright'); const path = require('path');
(async () => {
  const b = await chromium.launch();
  for (const n of ['prancha', 'aplicacoes']) {
    const p = await b.newPage({ viewport: { width: 1440, height: 1000 }, deviceScaleFactor: 1 });
    await p.goto('file://' + path.join(__dirname, n + '.html'), { waitUntil: 'networkidle' });
    await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(700);
    await p.screenshot({ path: path.join(__dirname, n + '.png'), fullPage: true });
  }
  await b.close();
})();
