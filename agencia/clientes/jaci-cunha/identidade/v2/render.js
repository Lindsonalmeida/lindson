// Gera o PDF do manual: node render.js [pasta-de-previas]
const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch({ executablePath: process.env.CHROME || '/opt/pw-browsers/chromium' });
  const p = await b.newPage({ viewport: { width: 1080, height: 1350 } });
  await p.goto('file://' + path.join(__dirname, 'manual.html'), { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(1200);
  await p.pdf({ path: path.join(__dirname, 'jaci-cunha-manual-de-identidade.pdf'), width: '1080px', height: '1350px', printBackground: true });
  const out = process.argv[2];
  if (out) { const els = await p.$$('.p'); for (let i = 0; i < els.length; i++) await els[i].screenshot({ path: `${out}/q${String(i + 1).padStart(2, '0')}.png` }); }
  await b.close();
})();
