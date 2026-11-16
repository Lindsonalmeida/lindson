// renderiza paginas/<doc>.html em PDF e JPGs (conta Pedro, 16/11/2026)
const { chromium } = require('playwright'); const path = require('path');
(async () => {
  const b = await chromium.launch();
  for (const d of process.argv.slice(2)) {
    const p = await b.newPage({ viewport: { width: 1920, height: 1080 } });
    await p.goto('file://' + path.resolve(__dirname, '../paginas/' + d + '.html')); await p.waitForTimeout(1500);
    await p.pdf({ path: path.resolve(__dirname, '../entregas/alkantara-' + d + '.pdf'), width: '1920px', height: '1080px', printBackground: true });
    const els = await p.$$('.pg');
    for (let i = 0; i < els.length; i++) {
      await els[i].screenshot({ path: path.resolve(__dirname, '../paginas/' + d + '-' + String(i + 1).padStart(2, '0') + '.jpg'), type: 'jpeg', quality: 82 });
    }
    console.log(d, els.length);
  }
  await b.close();
})();
