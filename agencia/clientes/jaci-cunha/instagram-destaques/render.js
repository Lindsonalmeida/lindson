// node render.js -> out/<destaque>-<n>.jpg (2160x3840, alta qualidade). Conta Leandro, 03/11/2026.
const { chromium } = require('playwright');
(async () => { const b = await chromium.launch({ args: ['--allow-file-access-from-files'] }); const p = await b.newPage({ viewport: { width: 1100, height: 1960 }, deviceScaleFactor: 2 });
 await p.goto('file://' + __dirname + '/artes.html', { waitUntil: 'networkidle' }); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(800);
 for (const el of await p.$$('section.f')) await el.screenshot({ path: __dirname + '/out/' + (await el.getAttribute('id')) + '.jpg', type: 'jpeg', quality: 93 });
 await b.close(); })();
