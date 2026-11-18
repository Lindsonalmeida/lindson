// Renderiza camadas HTML em PNG transparente. Uso: node render.js <pasta> (lê <pasta>/paginas.json)
// Cada página: {nome, html, sel?} -> <nome>.png (recorte do elemento sel, ou a tela 1920x1080) e caixas das palavras .w em <pasta>/caixas.json
const { chromium } = require('playwright'); const fs = require('fs');
(async () => {
  const dir = process.argv[2]; const pags = JSON.parse(fs.readFileSync(dir + '/paginas.json'));
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1920, height: 1080 } });
  const caixas = {};
  for (const g of pags) {
    await p.setContent(g.html, { waitUntil: 'networkidle' }); await p.evaluate(() => document.fonts.ready);
    if (g.sel) {
      const el = await p.$(g.sel); const bb = await el.boundingBox();
      const ws = await p.$$eval('.w', (xs) => xs.map((x) => { const r = x.getBoundingClientRect(); return [r.left, r.right]; }));
      caixas[g.nome] = { x: bb.x, y: bb.y, w: bb.width, h: bb.height, pal: ws.map(([a, z]) => [a - bb.x, z - bb.x]) };
      await el.screenshot({ path: `${dir}/${g.nome}.png`, omitBackground: true });
    } else {
      await p.screenshot({ path: `${dir}/${g.nome}.png`, omitBackground: true });
    }
  }
  fs.writeFileSync(dir + '/caixas.json', JSON.stringify(caixas));
  await b.close(); console.log('ok', pags.length);
})();
