// Renderiza os carrosséis de novembro em 2x (2160x2700) para o painel (conta Leandro, 04/11/2026)
const { chromium } = require('playwright'); const path = require('path');
(async () => { const d = process.argv[2]; const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1100, height: 1400 }, deviceScaleFactor: 2 });
 await p.goto('file://' + path.join(d, 'artes.html'), { waitUntil: 'networkidle' }); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(600);
 for (const el of await p.$$('section.f')) await el.screenshot({ path: path.join(d, 'out', (await el.getAttribute('id')) + '.jpg'), type: 'jpeg', quality: 92 });
 await b.close(); })();
