// node pdf.js <html> <pdf> <w> <h> [prefixo_jpg]  (Al Kántara fase 2)
const { chromium } = require('playwright'); const path = require('path');
(async () => { const [h, o, w, ht, pre] = process.argv.slice(2); const b = await chromium.launch();
 const p = await b.newPage({ viewport: { width: +w, height: +ht } }); await p.goto('file://' + path.resolve(h)); await p.waitForTimeout(1200);
 if (o !== '-') await p.pdf({ path: o, width: w + 'px', height: ht + 'px', printBackground: true });
 if (pre) { const els = await p.$$('.pg'); for (let i = 0; i < els.length; i++) await els[i].screenshot({ path: pre + '-' + String(i + 1).padStart(2, '0') + '.jpg', type: 'jpeg', quality: 86 }); }
 await b.close(); })();
