// frames da vinheta (30 fps, 6 s) -> /tmp frames; bio.html -> bio-celular.jpg (conta Pedro, 18/11/2026)
const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
const FR = process.argv[2];
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  await p.goto('file://' + path.resolve(__dirname, 'vinheta.html')); await p.waitForTimeout(800);
  fs.mkdirSync(FR, { recursive: true });
  for (let i = 0; i < 180; i++) { await p.evaluate(t => frame(t), i / 30); await p.screenshot({ path: FR + '/f' + String(i).padStart(3, '0') + '.jpg', type: 'jpeg', quality: 90 }); }
  const m = path.resolve(__dirname, '../entregas/motion'); fs.mkdirSync(m, { recursive: true });
  for (const [k, t] of [[0, .5], [1, 1.5], [2, 3], [3, 5]]) { await p.evaluate(t => frame(t), t); await p.screenshot({ path: m + '/q' + k + '.jpg', type: 'jpeg', quality: 80, clip: { x: 0, y: 420, width: 1080, height: 1080 } }); }
  const q = await b.newPage({ viewport: { width: 390, height: 800 }, deviceScaleFactor: 2 });
  await q.goto('file://' + path.resolve(__dirname, '../entregas/bio.html')); await q.waitForTimeout(1200);
  await q.screenshot({ path: path.resolve(__dirname, '../entregas/bio-celular.jpg'), type: 'jpeg', quality: 85, fullPage: true });
  await b.close();
})();
