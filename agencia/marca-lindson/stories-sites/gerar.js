// Gera a sequência "Stories · Vender sites" (conta Pedro, 05/11/2026): PNG das telas paradas, MP4 das telas com site rolando,
// guia com as figurinhas e a prévia (todas lado a lado).
// Uso: node gerar.js [n ...]          (sem número = as 10 telas)
//   SAIDA=pasta    onde salvar (padrão: privado CentralLindsonALmeida/painel/admin-rede/stories-sites, porque 2 telas têm o rosto dele)
//   QUADROS=pasta  quadros dos vídeos dos sites (padrão: /tmp/stories-sites-quadros; são extraídos sozinhos das gravações do site)
// Precisa: playwright (chromium), ffmpeg, as fotos-variação em ../artes-v1/fotos/ (fora do Git, ver README) e o privado clonado ao lado.
const { chromium } = require('playwright'), path = require('path'), fs = require('fs'), { execFileSync } = require('child_process');
const D = __dirname, PRIV = process.env.PRIV || '/home/user/centrallindsonalmeida';   // clone do privado CentralLindsonALmeida
const SAIDA = process.env.SAIDA || path.join(PRIV, 'painel/admin-rede/stories-sites');
const QUADROS = process.env.QUADROS || '/tmp/stories-sites-quadros';
const MEDIA = path.join(PRIV, 'site/media');   // gravações em 2x dos sites no ar (site-*.mp4, 30 fps, 9 s)
const VIDEOS = { 4: ['rafael-m'], 5: ['sf-d', 'sf-m'], 6: ['tribuna-m'], 7: ['realtimebio-m', 'jacibio-m'] }, N = 210; // 7 s a 30 fps
(async () => {
  const ids = process.argv.slice(2).length ? process.argv.slice(2).map(Number) : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
  fs.mkdirSync(path.join(SAIDA, 'guia'), { recursive: true });
  for (const v of new Set(ids.flatMap(i => VIDEOS[i] || []))) {   // quadros: pula o 1º segundo (página parada) e pega 7 s
    const p = path.join(QUADROS, v); if (fs.existsSync(path.join(p, '210.jpg'))) continue; fs.mkdirSync(p, { recursive: true });
    execFileSync('ffmpeg', ['-v', 'error', '-y', '-ss', '1', '-i', path.join(MEDIA, `site-${v}.mp4`), '-frames:v', String(N), '-q:v', '2', path.join(p, '%03d.jpg')]);
  }
  const b = await chromium.launch();
  for (const s of ids) {
    const nn = String(s).padStart(2, '0'), url = q => 'file://' + path.join(D, 'stories.html') + `?s=${s}&q=${encodeURIComponent(QUADROS)}` + q;
    const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
    await p.goto(url(VIDEOS[s] ? '&f=45' : '')); await p.waitForFunction(() => window.pronto, null, { timeout: 60000 });
    await p.screenshot({ path: path.join(SAIDA, `s${nn}.png`) });          // tela parada (nas de vídeo: o quadro 45, serve de capa)
    if (VIDEOS[s]) {
      const tmp = fs.mkdtempSync('/tmp/st-' + nn + '-');
      for (let f = 0; f < N; f++) { await p.evaluate(f => window.setF(f), f); await p.screenshot({ path: path.join(tmp, String(f).padStart(3, '0') + '.jpg'), type: 'jpeg', quality: 95 }); }
      execFileSync('ffmpeg', ['-v', 'error', '-y', '-framerate', '30', '-i', path.join(tmp, '%03d.jpg'), '-c:v', 'libx264', '-profile:v', 'high', '-pix_fmt', 'yuv420p', '-crf', '17', '-preset', 'slow', '-movflags', '+faststart', '-an', path.join(SAIDA, `s${nn}.mp4`)]);
      fs.rmSync(tmp, { recursive: true });
    }
    await p.goto(url((VIDEOS[s] ? '&f=45' : '') + '&guia=1')); await p.waitForFunction(() => window.pronto, null, { timeout: 60000 });
    await p.screenshot({ path: path.join(SAIDA, 'guia', `s${nn}.png`) });
    await p.close(); console.log('tela', nn, VIDEOS[s] ? '(png + mp4)' : '(png)');
  }
  await b.close();
})();
