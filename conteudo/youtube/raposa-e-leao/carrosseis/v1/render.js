// Renderiza cada <section class="f"> de pecas.html em cNN/cNN-XX.jpg (2160x2700, deviceScaleFactor 2). Conta Zuleide, 18/11/2026.
// Uso: node render.js [trecho-do-id]   ex.: node render.js c03-01 (só a capa do c03, depois de pôr fundos/c03-capa.jpg)
const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
(async () => { const d = __dirname;
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1400 }, deviceScaleFactor: 2 });
  await p.goto('file://' + path.join(d, 'pecas.html'), { waitUntil: 'networkidle' }); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(800);
  const only = process.argv[2];
  for (const el of await p.$$('section.f')) { const id = await el.getAttribute('id'); if (only && !id.includes(only)) continue;
    const dir = path.join(d, id.split('-')[0]); fs.mkdirSync(dir, { recursive: true });
    await el.screenshot({ type: 'jpeg', quality: 86, path: path.join(dir, id + '.jpg') }); }
  await b.close(); })();
