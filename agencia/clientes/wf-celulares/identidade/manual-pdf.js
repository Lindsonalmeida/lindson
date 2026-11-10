// manual.html -> PDF 16:9 + miniaturas das páginas (conta Leandro, 10/11/2026; base manual-pdf.js da Orégano)
const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
(async () => { const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1920, height: 1080 } });
  await p.goto('file://' + path.join(__dirname, 'manual.html'), { waitUntil: 'networkidle' }); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(800);
  const out = process.argv[2] || path.join(__dirname, 'manual-wf-celulares.pdf');
  await p.pdf({ path: out, width: '1920px', height: '1080px', printBackground: true });
  fs.mkdirSync(path.join(__dirname, 'manual-pags'), { recursive: true }); let i = 1;
  for (const el of await p.$$('section.p')) await el.screenshot({ path: path.join(__dirname, 'manual-pags', String(i++).padStart(2, '0') + '.jpg'), type: 'jpeg', quality: 60 });
  await b.close(); })();
