// Gera os PNGs das artes (artes.html?a=<id>) em artes/ e a prévia do perfil (grid 3 colunas). Conta Pedro, 03/11/2026.
// Uso: node gerar.js [id ...]   (sem id = todas). Fotos em fotos/ (fora do Git).
const { chromium } = require('playwright'), path = require('path'), fs = require('fs');
const D = __dirname, IDS = ['a1', 'c1', 'r1', 'p1'];
(async () => {
  const b = await chromium.launch(), ids = process.argv.slice(2).length ? process.argv.slice(2) : IDS;
  fs.mkdirSync(path.join(D, 'artes'), { recursive: true });
  for (const id of ids) {
    const h = id.startsWith('r') ? 1920 : 1350, p = await b.newPage({ viewport: { width: 1080, height: h } });
    await p.goto('file://' + path.join(D, 'artes.html') + '?a=' + id); await p.waitForFunction(() => window.pronto, null, { timeout: 30000 });
    await p.screenshot({ path: path.join(D, 'artes', id + '.png') }); await p.close(); console.log(id);
  }
  await b.close();
})();
