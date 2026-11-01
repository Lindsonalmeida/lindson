// Gera o PDF do manual: node render.js [pasta-de-previas]
const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch({ executablePath: process.env.CHROME || '/opt/pw-browsers/chromium' });
  const p = await b.newPage({ viewport: { width: 1080, height: 1350 } });
  await p.goto('file://' + path.join(__dirname, 'manual.html'));
  await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(1500);
  await p.pdf({ path: path.join(__dirname, 'jaci-cunha-manual-identidade-v1.pdf'), width: '1080px', height: '1350px', printBackground: true, margin: { top: 0, right: 0, bottom: 0, left: 0 } });
  const out = process.argv[2];
  if (out) { const n = await p.$$eval('.p', x => x.length); for (let i = 0; i < n; i++) { const e = (await p.$$('.p'))[i]; await e.screenshot({ path: `${out}/p${String(i + 1).padStart(2, '0')}.png` }); } }
  await b.close();
})();
