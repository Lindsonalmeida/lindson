const { chromium } = require('playwright'); const path = require('path');
(async () => { const d = process.argv[2]; const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1100, height: 1400 } });
 await p.goto('file://' + path.join(d, 'artes.html'), { waitUntil: 'networkidle' }); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(500);
 for (const el of await p.$$('section.f')) await el.screenshot({ path: path.join(d, 'out', (await el.getAttribute('id')) + '.jpg'), type: 'jpeg', quality: 93 });
 await b.close(); })();
