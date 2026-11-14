// Captura os quadros de v<N>.html (30 fps) em tmp/v<N>/ · base wf-celulares/motion-01 (conta Leandro) · conta Zuleide 14/11/2026
// Uso: node render.js N [só_estes_segundos,separados,por,vírgula]
const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
(async () => { const n = process.argv[2], d = __dirname, dur = JSON.parse(fs.readFileSync(path.join(d, 'v' + n + '.json'))).dur, fps = 30;
  const out = path.join(d, 'tmp', 'v' + n); fs.mkdirSync(out, { recursive: true });
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  await p.goto('file://' + path.join(d, 'v' + n + '.html'), { waitUntil: 'networkidle' }); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(600);
  await p.evaluate(() => fit());
  if (process.argv[3]) { for (const s of process.argv[3].split(',')) { await p.evaluate(t => render(t), +s); await p.screenshot({ path: path.join(out, 'q' + s + '.jpg'), type: 'jpeg', quality: 80 }); } }
  else for (let i = 0; i < Math.round(dur * fps); i++) { await p.evaluate(t => render(t), i / fps); await p.screenshot({ path: path.join(out, String(i).padStart(4, '0') + '.jpg'), type: 'jpeg', quality: 88 }); }
  await b.close(); })();
