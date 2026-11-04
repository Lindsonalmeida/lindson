// Gera a foto de perfil (pf) e as capas de destaques (h1..h6) de perfil.html em artes/. Conta Pedro, 04/11/2026.
const { chromium } = require('playwright'), path = require('path');
(async () => {
  const b = await chromium.launch();
  for (const id of ['pf', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']) {
    const p = await b.newPage({ viewport: { width: 1080, height: id === 'pf' ? 1080 : 1920 } });
    await p.goto('file://' + path.join(__dirname, 'perfil.html') + '?a=' + id); await p.waitForFunction(() => window.pronto, null, { timeout: 30000 });
    await p.screenshot({ path: path.join(__dirname, 'artes', 'perfil-' + id + '.png') }); await p.close(); console.log(id);
  }
  await b.close();
})();
