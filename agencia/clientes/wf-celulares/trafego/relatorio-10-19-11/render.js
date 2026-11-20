// relatorio.html e cliente.html -> PDF 16:9 + páginas JPG (conta Pedro, 20/11/2026)
const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
(async () => { const b = await chromium.launch();
  for (const [html, pdf, pasta] of [['relatorio.html', 'wf-relatorio-meta-ads-10-19-11.pdf', 'pags'], ['cliente.html', 'wf-resumo-cliente-10-19-11.pdf', 'pags-cliente']]) {
    const p = await b.newPage({ viewport: { width: 1920, height: 1080 } });
    await p.goto('file://' + path.join(__dirname, html), { waitUntil: 'networkidle' }); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(500);
    await p.pdf({ path: path.join(__dirname, pdf), width: '1920px', height: '1080px', printBackground: true });
    fs.mkdirSync(path.join(__dirname, pasta), { recursive: true }); let i = 1;
    for (const el of await p.$$('section.p')) await el.screenshot({ path: path.join(__dirname, pasta, String(i++).padStart(2, '0') + '.jpg'), type: 'jpeg', quality: 70 });
    await p.close(); }
  await b.close(); })();
