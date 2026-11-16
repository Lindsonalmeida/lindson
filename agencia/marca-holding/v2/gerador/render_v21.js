// v2.1 (conta Leandro): saída em entregas/v2.1/ · renderiza paginas/<doc>.html em PDF e JPGs (conta Pedro, 16/11/2026)
const { chromium } = require('playwright'); const path = require('path');
(async () => {
  const b = await chromium.launch();
  for (const d of process.argv.slice(2)) {
    const p = await b.newPage({ viewport: { width: 1920, height: 1080 } });
    await p.goto('file://' + path.resolve(__dirname, '../paginas/' + d + '-v2.1.html')); await p.waitForTimeout(1500);
    // conferência v2.1: texto cortado pela borda da página ou estourando a caixa
    const prob = await p.evaluate(() => { const out = []; document.querySelectorAll('.pg').forEach((pg, i) => { const R = pg.getBoundingClientRect();
      pg.querySelectorAll('*').forEach(e => { const t = [...e.childNodes].filter(n => n.nodeType === 3 && n.textContent.trim()).map(n => n.textContent.trim()).join(' '); if (!t) return;
        const r = e.getBoundingClientRect(); if (r.width === 0) return;
        if (r.left < R.left - 1 || r.right > R.right + 1 || r.top < R.top - 1 || r.bottom > R.bottom + 1) out.push(`p${i + 1} FORA: ${t.slice(0, 50)}`);
        if (e.scrollWidth > e.clientWidth + 2 && getComputedStyle(e).overflow === 'hidden') out.push(`p${i + 1} ESTOURA: ${t.slice(0, 50)}`); }); }); return out; });
    prob.forEach(x => console.log('  !', x));
    await p.pdf({ path: path.resolve(__dirname, '../entregas/v2.1/alkantara-' + d + '-v2.1.pdf'), width: '1920px', height: '1080px', printBackground: true });
    const els = await p.$$('.pg');
    for (let i = 0; i < els.length; i++) {
      await els[i].screenshot({ path: path.resolve(__dirname, '../entregas/v2.1/paginas/' + d + '-' + String(i + 1).padStart(2, '0') + '.jpg'), type: 'jpeg', quality: 82 });
    }
    console.log(d, els.length);
  }
  await b.close();
})();
