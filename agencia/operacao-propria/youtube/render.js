// Renderiza cada <section class="f"> de pecas.html em pecas/<id>.(jpg|png). Paollo, conta Zuleide, 15/11/2026.
// Uso: NODE_PATH=$(npm root -g) node render.js
const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
(async () => { const d = __dirname; fs.mkdirSync(path.join(d, 'pecas'), { recursive: true });
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 2600, height: 2000 } });
  await p.goto('file://' + path.join(d, 'pecas.html'), { waitUntil: 'networkidle' }); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(800);
  for (const el of await p.$$('section.f')) { const id = await el.getAttribute('id'); const png = id.startsWith('marca');
    await el.screenshot(png ? { type: 'png', omitBackground: true, path: path.join(d, 'pecas', id + '.png') } : { type: 'jpeg', quality: 92, path: path.join(d, 'pecas', id + '.jpg') }); }
  await b.close(); })();
