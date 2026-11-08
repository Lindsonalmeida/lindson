// Gera painel.png (1440 de largura) e previa-feed.jpg a partir do gerador.html
// Uso: node render.js   (dentro desta pasta)
const fs = require('fs'), path = require('path');
const { chromium } = require('playwright');
(async () => {
  const dir = __dirname;
  const md = fs.readFileSync(path.join(dir, 'LEGENDAS.md'), 'utf8');
  const leg = md.split('<!-- LEGENDA -->')[1].split('<!-- /LEGENDA -->')[0].trim();
  const html = fs.readFileSync(path.join(dir, 'gerador.html'), 'utf8')
    .replace('__LEGENDA__', leg.replace(/\\/g, '\\\\').replace(/`/g, '\\`').replace(/\$\{/g, '\\${'));
  const tmp = path.join(dir, '_render.html');
  fs.writeFileSync(tmp, html);
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1 });
  await p.goto('file://' + tmp);
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(800);
  await p.screenshot({ path: path.join(dir, 'painel.png'), fullPage: true });
  const f = await b.newPage({ viewport: { width: 1080, height: 900 }, deviceScaleFactor: 1 });
  await f.goto('file://' + tmp + '#feed');
  await f.evaluate(() => document.fonts.ready);
  await f.waitForTimeout(800);
  await f.screenshot({ path: path.join(dir, 'previa-feed.jpg'), fullPage: true, type: 'jpeg', quality: 90 });
  console.log('caracteres da legenda:', leg.length);
  await b.close();
  fs.unlinkSync(tmp);
})();
