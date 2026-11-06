// Renderiza cada <section class="f"> de pecas4.html em pecas-v4/<id>.png. Paollo · conta Leandro, 06/11/2026.
// Uso: python3 gerar4.py && node render4.js   (SO=v4-08 python3 gerar4.py gera só uma prancha)
const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
(async () => { const d = __dirname; fs.mkdirSync(path.join(d, 'pecas-v4'), { recursive: true });
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1200, height: 2000 }, deviceScaleFactor: 1 });
  await p.goto('file://' + path.join(d, 'pecas4.html'), { waitUntil: 'networkidle' }); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(800);
  for (const el of await p.$$('section.f')) await el.screenshot({ path: path.join(d, 'pecas-v4', (await el.getAttribute('id')) + '.png') });
  await b.close(); })();
