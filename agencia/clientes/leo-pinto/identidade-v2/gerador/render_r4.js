// renderiza redes4.html -> entregas/redes-v4/<id>.jpg (conta Pedro, 18/11/2026)
const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 3000, height: 2000 } });
  await p.goto('file://' + path.resolve(__dirname, 'redes4.html')); await p.waitForTimeout(1500);
  const out = path.resolve(__dirname, '../entregas/redes-v4'); fs.mkdirSync(out, { recursive: true });
  for (const e of await p.$$('.t')) {
    const id = await e.getAttribute('id');
    if (id === 'camiseta') await e.screenshot({ path: out + '/' + id + '.png', omitBackground: true });
    else await e.screenshot({ path: out + '/' + id + '.jpg', type: 'jpeg', quality: 88 });
  }
  await b.close();
})();
