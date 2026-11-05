// Renderiza cada <section class="f"> de pecas.html em pecas/<id>.png. Conta Leandro, 05/11/2026.
const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
(async () => { const d = __dirname; fs.mkdirSync(path.join(d, 'pecas'), { recursive: true });
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1200, height: 2000 }, deviceScaleFactor: 1 });
  await p.goto('file://' + path.join(d, 'pecas.html'), { waitUntil: 'networkidle' }); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(500);
  for (const el of await p.$$('section.f')) await el.screenshot({ path: path.join(d, 'pecas', (await el.getAttribute('id')) + '.png') });
  await b.close(); })();
