// Renderiza o panorama 3240x1350 e corta em 01/02/03.jpg + previa-grid.jpg (conta Zuleide, 10/11/2026)
const { chromium } = require('playwright'); const path = require('path');
(async () => { const d = __dirname; const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 3240, height: 1350 } });
  await p.goto('file://' + path.join(d, 'pecas.html'), { waitUntil: 'networkidle' }); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(800);
  await (await p.$('#pano')).screenshot({ path: path.join(d, 'panorama.png') }); await b.close(); })();
