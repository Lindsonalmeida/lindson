// Renderiza cada section.f de pecas.html em ../pecas/<id>.jpg (conta Zuleide 18/11/2026)
const { chromium } = require('playwright'); const path = require('path');
(async () => { const d = __dirname; const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 2600, height: 1500 } });
  await p.goto('file://' + path.join(d, 'pecas.html'), { waitUntil: 'networkidle' }); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(800);
  for (const el of await p.$$('section.f')) { const id = await el.getAttribute('id');
    await el.screenshot({ type: 'jpeg', quality: 92, path: path.join(d, '..', 'pecas', id + '.jpg') }); }
  await b.close(); })();
