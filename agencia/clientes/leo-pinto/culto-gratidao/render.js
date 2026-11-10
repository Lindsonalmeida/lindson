const { chromium } = require('playwright'); const path = require('path');
(async () => { const d = process.argv[2]; const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
 await p.goto('file://' + path.join(d, 'pecas.html'), { waitUntil: 'networkidle' }); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(600);
 for (const id of ['c1','c2','c3','c4','s1','s2','s3']) await (await p.$('#'+id)).screenshot({ path: path.join(d, 'out', id + '.png') }); await b.close(); })();
