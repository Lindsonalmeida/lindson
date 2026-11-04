// Gera os pôsteres (p-) e miniaturas (t-) de keyart.html em artes/membros/. Conta Pedro, 04/11/2026.
const { chromium } = require('playwright'), path = require('path');
const P = ['kit-mes-pronto', 'kit-whatsapp-que-fecha', 'kit-prospeccao', 'raio-x-do-perfil', 'bio-que-vende'];
(async () => { const b = await chromium.launch();
  for (const k of P) for (const [t, w, h] of [['p', 1000, 1500], ['t', 1280, 720]]) {
    const p = await b.newPage({ viewport: { width: w, height: h } });
    await p.goto('file://' + path.join(__dirname, 'keyart.html') + '?a=' + t + '-' + k); await p.waitForFunction(() => window.pronto, null, { timeout: 30000 });
    await p.screenshot({ path: path.join(__dirname, 'artes', 'membros', t + '-' + k + '.jpg'), type: 'jpeg', quality: 90 }); await p.close(); }
  await b.close(); console.log('pronto'); })();
