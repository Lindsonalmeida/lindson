// Renderiza cada <section class="f"> de pecas.html em artes/<id>.jpg (2x, JPG q92) e monta previa-feed.jpg.
// Paollo · sessão paralela da conta Leandro, 06/11/2026. Uso: python3 gerar.py && node render.js [parte-do-id]
const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
(async () => { const d = __dirname; const out = path.join(d, 'artes'); fs.mkdirSync(out, { recursive: true });
  const so = process.argv[2];
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1200, height: 2100 }, deviceScaleFactor: 2 });
  await p.goto('file://' + path.join(d, 'pecas.html'), { waitUntil: 'networkidle' }); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(800);
  for (const el of await p.$$('section.f')) { const id = await el.getAttribute('id'); if (so && !id.includes(so)) continue;
    await el.screenshot({ path: path.join(out, id + '.jpg'), type: 'jpeg', quality: 92 }); console.log(id); }
  // Prévia do feed como no Instagram: o post mais novo (12) no canto de cima à esquerda.
  const posts = fs.readdirSync(out).filter(f => f.startsWith('post-')).sort().reverse();
  const cel = posts.map(f => `<div style="aspect-ratio:4/5;background:url('file://${path.join(out, f)}') center/cover"></div>`).join('');
  const g = await b.newPage({ viewport: { width: 1080, height: 1440 }, deviceScaleFactor: 1 });
  const gp = path.join(d, '.previa.html'); fs.writeFileSync(gp, `<body style="margin:0;background:#fff"><div style="display:grid;grid-template-columns:repeat(3,1fr);gap:4px;width:1080px">${cel}</div></body>`); await g.goto('file://' + gp);
  await g.waitForTimeout(1000); await g.screenshot({ path: path.join(d, 'previa-feed.jpg'), type: 'jpeg', quality: 85, fullPage: true }); fs.unlinkSync(gp);
  await b.close(); })();
