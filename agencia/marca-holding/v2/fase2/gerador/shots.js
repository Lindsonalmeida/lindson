const { chromium } = require('playwright'); const path = require('path');
(async () => { const b = await chromium.launch(); const S = path.resolve(__dirname, '../site'), O = path.resolve(__dirname, '../previas');
 for (const [w, h, sf, tag] of [[1440, 900, 1, 'pc'], [390, 844, 2, 'cel']]) {
  const p = await b.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: sf }); const erros = [];
  p.on('pageerror', e => erros.push(e.message));
  for (const f of ['index', 'labs', 'studio', 'media', 'ventures', 'cases', 'sobre', 'contato']) {
   await p.goto('file://' + S + '/' + f + '.html'); await p.waitForTimeout(1600);
   await p.evaluate(async () => { for (let y = 0; y < document.body.scrollHeight; y += 400) { scrollTo(0, y); await new Promise(r => setTimeout(r, 40)); } scrollTo(0, 0); });
   await p.evaluate(()=>document.querySelectorAll('.rv').forEach(e=>e.classList.add('in'))); await p.waitForTimeout(1200);
   const sw = await p.evaluate(() => document.documentElement.scrollWidth - innerWidth); if (sw > 0) erros.push(f + ' rolagem horizontal ' + sw);
   await p.screenshot({ path: `${O}/site-${f}-${tag}.jpg`, type: 'jpeg', quality: 80, fullPage: tag == 'pc' || f == 'index' });
   if (f == 'index' && tag == 'pc') await p.screenshot({ path: S + '/i/og.jpg', type: 'jpeg', quality: 82, clip: { x: 0, y: 0, width: 1200, height: 630 } });
  }
  console.log(tag, erros.length ? erros : 'sem erros'); }
 await b.close(); })();
