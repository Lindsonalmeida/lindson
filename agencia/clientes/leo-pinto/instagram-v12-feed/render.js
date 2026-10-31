// Renderiza cada <section class="f"> de artes.html em out/<id>.png
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const only = process.argv.slice(2);
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1200, height: 2000 } });
  await p.goto('file://' + path.join(__dirname, 'artes.html'));
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(800);
  for (const el of await p.$$('section.f')) {
    const id = await el.getAttribute('id');
    if (only.length && !only.some(o => id.startsWith(o))) continue;
    await el.screenshot({ path: path.join(__dirname, 'out', id + '.png') });
  }
  await b.close();
})();
