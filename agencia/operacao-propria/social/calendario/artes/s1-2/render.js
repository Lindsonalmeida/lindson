// Renderiza cada <section class="f"> de pecas.html em <id>.jpg (qualidade 92). Paollo, conta Leandro, 06/11/2026.
// Uso: node render.js [trecho-do-id]
const { chromium } = require('playwright'); const path = require('path');
(async () => { const d = __dirname;
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1200, height: 2100 }, deviceScaleFactor: 1 });
  await p.goto('file://' + path.join(d, 'pecas.html'), { waitUntil: 'networkidle' }); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(800);
  const only = process.argv[2];
  for (const el of await p.$$('section.f')) { const id = await el.getAttribute('id'); if (only && !id.includes(only)) continue;
    await el.screenshot({ type: 'jpeg', quality: 92, path: path.join(d, id + '.jpg') }); }
  await b.close(); })();
