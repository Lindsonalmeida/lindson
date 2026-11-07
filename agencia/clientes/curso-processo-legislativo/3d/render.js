const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch({ args: ['--no-sandbox','--use-gl=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist'] });
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
  p.on('console', m => { if (m.type()==='error') console.log('console:', m.text().slice(0,120)); });
  await p.goto('file://' + path.join(__dirname, 'cena.html'), { waitUntil: 'load', timeout: 60000 });
  await p.waitForFunction(() => window.__done === true, null, { timeout: 60000 }).catch(e => console.log('timeout', e.message.slice(0,80)));
  await p.locator('canvas').screenshot({ path: path.join(__dirname, 'cena-camara-3d.png') });
  await b.close(); console.log('ok');
})().catch(e => { console.error('FALHOU', e.message.slice(0,200)); process.exit(1); });
