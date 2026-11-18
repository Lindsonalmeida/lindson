// book3.html -> entregas/leo-pinto-identidade-v3-redes.pdf + páginas JPG (conferência de texto fora da página) · conta Pedro, 18/11/2026
const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1920, height: 1080 } });
  await p.goto('file://' + path.resolve(__dirname, 'book3.html')); await p.waitForTimeout(2000);
  const prob = await p.evaluate(() => { const out = []; document.querySelectorAll('.pg').forEach((pg, i) => { const R = pg.getBoundingClientRect();
    pg.querySelectorAll('*').forEach(e => { const t = [...e.childNodes].filter(n => n.nodeType === 3 && n.textContent.trim()).map(n => n.textContent.trim()).join(' '); if (!t) return;
      const r = e.getBoundingClientRect(); if (r.width === 0) return;
      if (r.left < R.left - 1 || r.right > R.right + 1 || r.top < R.top - 1 || r.bottom > R.bottom + 1) out.push(`p${i + 1} FORA: ${t.slice(0, 50)}`); }); }); return out; });
  prob.forEach(x => console.log('  !', x));
  const E = path.resolve(__dirname, '../entregas'); fs.mkdirSync(E + '/paginas-v3', { recursive: true });
  await p.pdf({ path: E + '/leo-pinto-identidade-v3-redes.pdf', width: '1920px', height: '1080px', printBackground: true });
  const els = await p.$$('.pg');
  for (let i = 0; i < els.length; i++) await els[i].screenshot({ path: E + '/paginas-v3/' + String(i + 1).padStart(2, '0') + '.jpg', type: 'jpeg', quality: 78 });
  console.log('paginas', els.length); await b.close();
})();
