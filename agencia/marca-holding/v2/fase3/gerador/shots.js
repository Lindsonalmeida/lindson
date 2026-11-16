const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
(async () => { const b = await chromium.launch(); const S = path.resolve(__dirname, '../site'), B = path.resolve(__dirname, '../bio'), O = path.resolve(__dirname, '../previas');
 const pags = ['index', 'labs', 'barzakh', 'media', 'ventures', 'cases', 'sobre', 'contato'].map(f => [f, S + '/' + f + '.html']).concat([['bio', B + '/index.html']]);
 for (const [w, h, sf, tag] of [[1440, 900, 1, 'pc'], [390, 844, 2, 'cel']]) {
  const p = await b.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: sf }); const erros = [];
  p.on('pageerror', e => erros.push(e.message)); p.on('requestfailed', r => erros.push('falhou ' + r.url().slice(0, 90)));
  for (const [f, u] of pags) {
   await p.goto('file://' + u); await p.evaluate(() => document.querySelectorAll('img').forEach(i => i.loading = 'eager')); await p.waitForTimeout(1400);
   await p.evaluate(async () => { for (let y = 0; y < document.body.scrollHeight; y += 400) { scrollTo(0, y); await new Promise(r => setTimeout(r, 40)); } scrollTo(0, 0); });
   await p.evaluate(() => document.querySelectorAll('.rv').forEach(e => e.classList.add('in'))); await p.waitForTimeout(1200);
   const sw = await p.evaluate(() => document.documentElement.scrollWidth - innerWidth); if (sw > 0) erros.push(f + ' rolagem horizontal ' + sw);
   const quebrados = await p.evaluate(() => [...document.querySelectorAll('a[href]')].map(a => a.getAttribute('href')).filter(h => !/^(https?:|#|mailto)/.test(h)));
   for (const h of quebrados) { const alvo = path.resolve(path.dirname(u), h.split('#')[0]); if (!fs.existsSync(alvo)) erros.push(f + ' link quebrado ' + h); }
   await p.screenshot({ path: `${O}/${f}-${tag}.jpg`, type: 'jpeg', quality: 72, fullPage: true });
   if (tag == 'pc' && f == 'index') await p.screenshot({ path: S + '/i/og.jpg', type: 'jpeg', quality: 82, clip: { x: 0, y: 0, width: 1200, height: 630 } });
  }
  console.log(tag, erros.length ? [...new Set(erros)] : 'sem erros'); await p.close(); }
 const p = await b.newPage({ viewport: { width: 1200, height: 630 } }); await p.setContent(`<body style="margin:0;background:#0B0C0E;display:flex;align-items:center;gap:60px;padding:0 90px;height:630px;font-family:serif;color:#EFEAE1">
 <img src="file://${S}/i/simbolo-latao.svg" style="width:300px"><div><p style="font:600 16px sans-serif;letter-spacing:.25em;color:#8E8A82">AL KÁNTARA GROUP · LINKS</p><h1 style="font:400 84px/1 Georgia,serif;margin:0">Estrutura para<br><i style="color:#B8955A">o que vem.</i></h1>
 <p style="font:500 22px sans-serif;color:#8E8A82;margin-top:26px">Labs · <span style="color:#C9A35A">Barzakh</span> · Media · Ventures</p></div></body>`); await p.waitForTimeout(500);
 await p.screenshot({ path: B + '/og.jpg', type: 'jpeg', quality: 85 });
 await b.close(); })();
