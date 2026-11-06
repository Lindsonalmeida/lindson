// Renderiza kit-mockup/pecas.html em PNGs transparentes (um por peça). Conta Leandro, 06/11/2026.
const { chromium } = require('playwright'); const path = require('path');
(async () => { const d = path.join(__dirname, 'kit-mockup') + '/'; const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 2000, height: 1200 } });
  await p.goto('file://' + d + 'pecas.html', { waitUntil: 'networkidle' }); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(600);
  for (const el of await p.$$('.p')) { const id = await el.getAttribute('id'); await el.screenshot({ path: d + id + '.png', omitBackground: true }); console.log(id); }
  await b.close(); })();
