// Gera a sequência "Stories · Vender sites" (conta Pedro, 05/11/2026): PNG das telas paradas, MP4 das telas com site rolando,
// guia com as figurinhas e a prévia (todas lado a lado).
// Uso: node gerar.js [n ...]          (sem número = as 10 telas)
//   SAIDA=pasta    onde salvar (padrão: privado CentralLindsonALmeida/painel/admin-rede/stories-sites, porque 2 telas têm o rosto dele)
//   QUADROS=pasta  quadros dos sites gravados no ar (padrão: /tmp/stories-sites-quadros; gravar.js grava sozinho na duração certa)
// Depois dos vídeos: python3 audio.py (voz, SFX e trilha). Ordem completa no README.
// Precisa: playwright (chromium), ffmpeg, as fotos-variação em ../artes-v1/fotos/ (fora do Git, ver README) e o privado clonado ao lado.
const { chromium } = require('playwright'), path = require('path'), fs = require('fs'), { execFileSync } = require('child_process');
const D = __dirname, PRIV = process.env.PRIV || '/home/user/centrallindsonalmeida';   // clone do privado CentralLindsonALmeida
const SAIDA = process.env.SAIDA || path.join(PRIV, 'painel/admin-rede/stories-sites');
const QUADROS = process.env.QUADROS || '/tmp/stories-sites-quadros';
const VIDEOS = { 4: ['rafael-m'], 5: ['sf-d', 'sf-m'], 6: ['tribuna-m'], 7: ['realtimebio-m', 'jacibio-m'] };
// duração de cada vídeo em quadros (30 fps): segue a narração (narra.py grava duracoes.json); sem narração, 7 s
const DUR = fs.existsSync(path.join(D, 'duracoes.json')) ? JSON.parse(fs.readFileSync(path.join(D, 'duracoes.json'))) : {};
const nq = s => DUR[s] || 210;
(async () => {
  const ids = process.argv.slice(2).length ? process.argv.slice(2).map(Number) : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
  fs.mkdirSync(path.join(SAIDA, 'guia'), { recursive: true });
  for (const s of ids) for (const v of VIDEOS[s] || []) {   // grava o site no ar quadro a quadro, na duração do vídeo (gravar.js)
    const pasta = path.join(QUADROS, 's0' + s); if (fs.existsSync(path.join(pasta, v, String(nq(s)).padStart(3, '0') + '.jpg'))) continue;
    execFileSync('node', [path.join(D, 'gravar.js'), pasta, v, String(nq(s))], { stdio: 'inherit' });
  }
  const b = await chromium.launch();
  for (const s of ids) {
    const nn = String(s).padStart(2, '0'), N = nq(s), url = q => 'file://' + path.join(D, 'stories.html') + `?s=${s}&n=${N}&q=${encodeURIComponent(path.join(QUADROS, 's0' + s))}` + q;
    const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
    await p.goto(url(VIDEOS[s] ? '&f=45' : '')); await p.waitForFunction(() => window.pronto, null, { timeout: 60000 });
    await p.screenshot({ path: path.join(SAIDA, `s${nn}.png`) });          // tela parada (nas de vídeo: o quadro 45, serve de capa)
    if (VIDEOS[s]) {
      const tmp = fs.mkdtempSync('/tmp/st-' + nn + '-');
      for (let f = 0; f < N; f++) { await p.evaluate(f => window.setF(f), f); await p.screenshot({ path: path.join(tmp, String(f).padStart(3, '0') + '.jpg'), type: 'jpeg', quality: 95 }); }
      fs.writeFileSync(path.join(QUADROS, 's0' + s, 'cues.json'), JSON.stringify(await p.evaluate(() => window.cues)));
      execFileSync('ffmpeg', ['-v', 'error', '-y', '-framerate', '30', '-i', path.join(tmp, '%03d.jpg'), '-c:v', 'libx264', '-profile:v', 'high', '-pix_fmt', 'yuv420p', '-crf', '17', '-preset', 'slow', '-movflags', '+faststart', '-an', path.join(SAIDA, `s${nn}.mp4`)]);
      fs.rmSync(tmp, { recursive: true });
    }
    await p.goto(url((VIDEOS[s] ? '&f=45' : '') + '&guia=1')); await p.waitForFunction(() => window.pronto, null, { timeout: 60000 });
    await p.screenshot({ path: path.join(SAIDA, 'guia', `s${nn}.png`) });
    await p.close(); console.log('tela', nn, VIDEOS[s] ? '(png + mp4)' : '(png)');
  }
  await b.close();
})();
