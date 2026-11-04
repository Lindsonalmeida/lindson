// Gera as capas da área de membros (membros.html) em artes/membros/. Conta Pedro, 04/11/2026.
const { chromium } = require('playwright'), path = require('path'), fs = require('fs');
const P = ['kit-mes-pronto', 'kit-whatsapp-que-fecha', 'kit-prospeccao', 'raio-x-do-perfil', 'bio-que-vende'];
const T = { hero: [1920, 760] }; P.forEach(k => { T['v-' + k] = [600, 1000]; T['h-' + k] = [830, 440]; });
(async () => {
  const out = path.join(__dirname, 'artes', 'membros'); fs.mkdirSync(out, { recursive: true });
  const b = await chromium.launch();
  for (const [id, [w, h]] of Object.entries(T)) {
    const p = await b.newPage({ viewport: { width: w, height: h } });
    await p.goto('file://' + path.join(__dirname, 'membros.html') + '?a=' + id); await p.waitForFunction(() => window.pronto, null, { timeout: 30000 });
    await p.screenshot({ path: path.join(out, id + '.jpg'), type: 'jpeg', quality: 92 }); await p.close();
  }
  await b.close(); console.log('pronto', Object.keys(T).length);
})();
