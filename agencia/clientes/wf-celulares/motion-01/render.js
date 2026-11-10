// Captura os quadros de v<N>.html (30 fps, 14 s) em tmp/v<N>/ · conta Leandro, 10/11/2026
const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
(async () => { const n = process.argv[2], dur = 14, fps = 30, d = __dirname, out = path.join(d, 'tmp', 'v' + n); fs.mkdirSync(out, { recursive: true });
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  await p.goto('file://' + path.join(d, 'v' + n + '.html'), { waitUntil: 'networkidle' }); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(500);
  for (let i = 0; i < dur * fps; i++) { await p.evaluate(t => render(t), i / fps); await p.screenshot({ path: path.join(out, String(i).padStart(4, '0') + '.jpg'), type: 'jpeg', quality: 88 }); }
  await b.close(); })();
