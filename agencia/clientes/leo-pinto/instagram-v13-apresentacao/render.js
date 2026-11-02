const { chromium } = require('playwright'); const path = require('path');
(async () => { const d = process.argv[2]; const b = await chromium.launch();
 const p = await b.newPage({ viewport: { width: 3104, height: 1350 } });
 await p.goto('file://' + path.join(d, 'artes.html'), { waitUntil: 'networkidle' }); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(500);
 await (await p.$('#p')).screenshot({ path: path.join(d, 'out', 'painel.png') }); await b.close(); })();
