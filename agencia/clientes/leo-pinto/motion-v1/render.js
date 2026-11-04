// Renderizador do Motion v1 do Leo (conta Pedro, 04/11/2026).
// Abre engine.html no Chromium (Playwright), chama render(t) para cada um dos 1200 quadros (30 fps × 40 s),
// tira o print do palco 1080×1920 e manda os quadros JPEG para o ffmpeg (H.264 + faixa AAC muda).
// Uso:
//   FFMPEG=/caminho/ffmpeg node render.js v1 [v2 v3 v4] --a <assets> --out <saida>
//   node render.js v1 --a <assets> --out <saida> --previa 1.2,5,9.5     (só quadros soltos, para conferir)
const { chromium } = require('playwright');
const { spawn, execFileSync } = require('child_process');
const path = require('path'), fs = require('fs');
const args = process.argv.slice(2);
const opt = (k, d) => { const i = args.indexOf(k); return i >= 0 ? args[i + 1] : d; };
const vids = args.filter((a, i) => /^v\d$/.test(a) && !['--a', '--out', '--previa'].includes(args[i - 1]));
const ASSETS = path.resolve(opt('--a', path.join(__dirname, '../assets')));
const OUT = path.resolve(opt('--out', path.join(__dirname, 'saida')));
const PREV = opt('--previa', null);
const FFMPEG = process.env.FFMPEG || 'ffmpeg';
const FPS = 30, DUR = 40, N = FPS * DUR;
// aplica o estado do tempo t e espera 2 quadros do navegador (garante que o print não pega o quadro anterior)
const SET = t => new Promise(r => { window.render(t); requestAnimationFrame(() => requestAnimationFrame(r)); });
fs.mkdirSync(OUT, { recursive: true });

async function one(browser, v) {
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
  page.on('console', m => console.log(`[${v}] ${m.text()}`));
  page.on('pageerror', e => console.log(`[${v}] ERRO ${e.message}`));
  await page.goto('file://' + path.join(__dirname, 'engine.html') + `?v=${v}&a=${encodeURIComponent(ASSETS)}`);
  const info = await page.evaluate(() => window.READY);
  const stage = await page.$('#stage');
  const shot = async (t, file) => { await page.evaluate(SET, t); return stage.screenshot({ type: 'jpeg', quality: 93, path: file }); };
  if (PREV) {
    for (const t of PREV.split(',').map(Number)) await shot(t, path.join(OUT, `${v}-t${t.toFixed(2)}.jpg`));
    await page.close(); return;
  }
  // folha de contato: 1 quadro por cena, depois que o texto já entrou (≈ 72% da cena)
  const sheetT = info.shots.map(([a, b]) => a + (b - a) * .72);
  const sheetF = new Set(sheetT.map(t => Math.round(t * FPS)));
  const tmp = path.join(OUT, `.${v}-folha`); fs.mkdirSync(tmp, { recursive: true });
  const mp4 = path.join(OUT, `leo-motion-${v}.mp4`);
  const ff = spawn(FFMPEG, ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(FPS), '-c:v', 'mjpeg', '-i', '-',
    '-f', 'lavfi', '-i', 'anullsrc=r=48000:cl=stereo',
    '-map', '0:v', '-map', '1:a', '-c:v', 'libx264', '-preset', 'slow', '-crf', '17', '-pix_fmt', 'yuv420p', '-profile:v', 'high',
    '-r', String(FPS), '-frames:v', String(N), '-c:a', 'aac', '-b:a', '96k', '-t', String(DUR), '-movflags', '+faststart', mp4], { stdio: ['pipe', 'inherit', 'inherit'] });
  const t0 = Date.now(); let k = 0;
  for (let f = 0; f < N; f++) {
    await page.evaluate(SET, f / FPS);
    const buf = await stage.screenshot({ type: 'jpeg', quality: 94 });
    if (sheetF.has(f)) fs.writeFileSync(path.join(tmp, `${String(++k).padStart(2, '0')}.jpg`), buf);
    if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
    if (f % 150 === 0) console.log(`[${v}] quadro ${f}/${N} · ${((Date.now() - t0) / 1000).toFixed(0)} s`);
  }
  ff.stdin.end(); await new Promise(r => ff.on('close', r));
  execFileSync(FFMPEG, ['-y', '-loglevel', 'error', '-framerate', '1', '-i', path.join(tmp, '%02d.jpg'), '-vf', 'scale=432:768,tile=5x2:padding=8:color=white', '-frames:v', '1', '-q:v', '3', path.join(OUT, `leo-motion-${v}-folha.jpg`)]);
  fs.rmSync(tmp, { recursive: true });
  console.log(`[${v}] pronto: ${mp4}`);
  await page.close();
}
(async () => {
  const b = await chromium.launch({ args: ['--disable-gpu-vsync', '--force-color-profile=srgb'] });
  await Promise.all(vids.map(v => one(b, v)));
  await b.close();
})();
