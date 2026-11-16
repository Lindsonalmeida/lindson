// v2.1 (conta Leandro): fotografa elementos de um HTML com fundo transparente → PNG
const { chromium } = require('playwright'); const path = require('path');
(async () => {
  const [html, outdir, ...ids] = process.argv.slice(2);
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 2000, height: 1400 }, deviceScaleFactor: 2 });
  await p.goto('file://' + path.resolve(html)); await p.waitForTimeout(1200);
  for (const id of ids) { const e = await p.$('#' + id); await e.screenshot({ path: path.join(outdir, id + '.png'), omitBackground: true }); console.log(id); }
  await b.close();
})();
