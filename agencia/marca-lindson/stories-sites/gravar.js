// Grava os sites no ar quadro a quadro (rolagem suave e exata, sem tremida), na duração que a narração pedir. Conta Pedro, 05/11/2026.
// Uso: node gravar.js <pasta-quadros> <nome> <quadros>     ex.: node gravar.js /tmp/q rafael-m 360
// Celular: 360×779 em 2x (720×1558). Computador: 800×450 em 2x (1600×900). Os quadros saem em <pasta>/<nome>/001.jpg …
const { chromium } = require('playwright'), path = require('path'), fs = require('fs');
const SITES = {
  'rafael-m': ['https://rafaelimports.pages.dev/', 1], 'sf-d': ['https://desentupidorasf.pages.dev/', 0], 'sf-m': ['https://desentupidorasf.pages.dev/', 1],
  'tribuna-m': ['https://tribuna98.pages.dev/', 1], 'realtimebio-m': ['https://realtimeslz.pages.dev/bio/', 1], 'jacibio-m': ['https://drajacicunha.pages.dev/bio/', 1],
};
const ease = x => x < .5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2;
(async () => {
  const [dir, nome, nq] = [process.argv[2], process.argv[3], +process.argv[4]], [url, cel] = SITES[nome];
  const out = path.join(dir, nome); fs.rmSync(out, { recursive: true, force: true }); fs.mkdirSync(out, { recursive: true });
  const b = await chromium.launch();
  const p = await b.newPage(cel ? { viewport: { width: 360, height: 779 }, deviceScaleFactor: 2, isMobile: true, hasTouch: true } : { viewport: { width: 800, height: 450 }, deviceScaleFactor: 2 });
  await p.goto(url, { waitUntil: 'networkidle', timeout: 60000 }); await p.waitForTimeout(2500);
  // passa a página inteira uma vez para carregar imagens preguiçosas e animações de entrada, depois volta ao topo
  const alto = await p.evaluate(() => document.documentElement.scrollHeight - innerHeight);
  for (let y = 0; y < alto; y += 300) { await p.evaluate(y => scrollTo(0, y), y); await p.waitForTimeout(120); }
  await p.evaluate(() => scrollTo(0, 0)); await p.waitForTimeout(1500);
  const max = Math.min(alto, cel ? 2600 : 1500), parado = Math.round(nq * .1);   // 10% parado no topo, depois desce suave
  for (let f = 0; f < nq; f++) {
    const t = Math.max(0, (f - parado) / (nq - 1 - parado));
    await p.evaluate(y => scrollTo(0, y), Math.round(ease(t) * max)); await p.waitForTimeout(25);
    await p.screenshot({ path: path.join(out, String(f + 1).padStart(3, '0') + '.jpg'), type: 'jpeg', quality: 92 });
  }
  await b.close(); console.log(nome, nq, 'quadros');
})();
