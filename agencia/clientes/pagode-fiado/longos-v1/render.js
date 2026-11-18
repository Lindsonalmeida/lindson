// Renderiza paginas.json em PNG transparente 1920x1080. Uso: node render.js <pasta>
const { chromium } = require('playwright'); const fs = require('fs');
(async () => {
  const dir = process.argv[2]; const pags = JSON.parse(fs.readFileSync(dir + '/paginas.json'));
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1920, height: 1080 } });
  for (const g of pags) {
    await p.setContent(g.html, { waitUntil: 'networkidle' }); await p.evaluate(() => document.fonts.ready);
    await p.screenshot({ path: `${dir}/${g.nome}.png`, omitBackground: true });
  }
  await b.close(); console.log('ok', pags.length);
})();
