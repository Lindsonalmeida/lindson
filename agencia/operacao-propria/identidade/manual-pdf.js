const { chromium } = require('playwright'); const path = require('path');
(async () => { const b = await chromium.launch(); const p = await b.newPage();
  await p.goto('file://' + path.join(__dirname, 'manual.html'), { waitUntil: 'networkidle' }); await p.evaluate(() => document.fonts.ready);
  await p.pdf({ path: path.join(__dirname, 'oregano-turbo-manual-de-marca.pdf'), width: '1080px', height: '1350px', printBackground: true }); await b.close(); })();
