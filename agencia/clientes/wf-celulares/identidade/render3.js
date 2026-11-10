// Renderiza cada <section class="f"> de pecas.html em pecas/<id>.jpg. WF Celulares, conta Leandro, 10/11/2026 (copiado do kit v4).
// Uso: node render.js [trecho-do-id]
const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
(async () => { const d = __dirname; fs.mkdirSync(path.join(d, 'pecas-final'), { recursive: true });
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 2000, height: 1400 }, deviceScaleFactor: 1 });
  await p.goto('file://' + path.join(d, 'pecas3.html'), { waitUntil: 'networkidle' }); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(800);
  const only = process.argv[2];
  for (const el of await p.$$('section.f')) { const id = await el.getAttribute('id'); if (only && !id.includes(only)) continue;
    await el.screenshot({ type: 'jpeg', quality: 92, path: path.join(d, 'pecas-final', id + '.jpg') }); }
  await b.close(); })();
