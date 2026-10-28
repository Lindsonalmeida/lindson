// Grava o mini site como se fosse a gravação de tela de um iPhone: node gravar.js <roteiro.json> <pasta-saida>
// O roteiro tem a URL e a lista de ações (esperar, rolar, tocar). Saída: quadros JPEG + tempos.json + eventos.json
const {chromium, devices} = require('playwright'); const fs = require('fs');
const R = JSON.parse(fs.readFileSync(process.argv[2])); const OUT = process.argv[3];
const W = 393, H = 578, DPR = 1080 / 393;
(async () => {
  fs.rmSync(OUT, {recursive: true, force: true}); fs.mkdirSync(OUT + '/q', {recursive: true});
  const b = await chromium.launch();
  const c = await b.newContext({...devices['iPhone 13'], viewport: {width: W, height: H}, deviceScaleFactor: DPR});
  await c.route(/wa\.me|api\.whatsapp|instagram\.com|linkedin\.com|threads\.net/, r => r.abort());
  const p = await c.newPage(); const cdp = await c.newCDPSession(p);
  const tempos = []; const eventos = []; let t0 = null, n = 0;
  cdp.on('Page.screencastFrame', async f => {
    const t = f.metadata.timestamp; if (t0 === null) t0 = t;
    fs.writeFileSync(`${OUT}/q/${String(n).padStart(5, '0')}.jpg`, Buffer.from(f.data, 'base64')); tempos.push(t - t0); n++;
    await cdp.send('Page.screencastFrameAck', {sessionId: f.sessionId}).catch(() => {});
  });
  const agora = () => Date.now() / 1000; let inicio;
  // dedo: bolinha que aparece no toque e acompanha a rolagem
  const DEDO = `(()=>{if(window.__dedo)return;const d=document.createElement('div');d.id='__dedo';d.style.cssText='position:fixed;z-index:2147483647;width:46px;height:46px;margin:-23px 0 0 -23px;border-radius:50%;background:rgba(255,255,255,.38);border:2px solid rgba(255,255,255,.85);box-shadow:0 0 0 1px rgba(0,0,0,.25),0 4px 14px rgba(0,0,0,.35);pointer-events:none;opacity:0;transition:opacity .15s,transform .15s;left:0;top:0';document.documentElement.appendChild(d);window.__dedo=d})()`;
  await p.addInitScript(DEDO);
  const dedo = (x, y, vis, esc = 1) => p.evaluate(([x, y, v, e]) => { const d = document.getElementById('__dedo'); if (!d) return; d.style.left = x + 'px'; d.style.top = y + 'px'; d.style.opacity = v ? 1 : 0; d.style.transform = `scale(${e})`; }, [x, y, vis, esc]);
  const rolar = (alvo, dur) => p.evaluate(([alvo, dur]) => new Promise(res => {
    const y0 = scrollY, dy = alvo - y0, ini = performance.now(), d = document.getElementById('__dedo'), x = innerWidth * .62, yb = innerHeight * .78;
    document.documentElement.style.scrollBehavior = 'auto';
    if (d) { d.style.transition = 'opacity .15s'; d.style.left = x + 'px'; d.style.top = yb + 'px'; d.style.opacity = 1 }
    const pas = k => { const u = Math.min(1, (k - ini) / (dur * 1000)), e = u < .5 ? 2 * u * u : 1 - Math.pow(-2 * u + 2, 2) / 2; scrollTo(0, y0 + dy * e);
      if (d) d.style.top = (yb - Math.sign(dy) * Math.min(innerHeight * .5, Math.abs(dy)) * Math.min(1, u * 1.6)) + 'px';
      if (u < 1) requestAnimationFrame(pas); else { if (d) d.style.opacity = 0; setTimeout(res, 120) } };
    requestAnimationFrame(pas) }), [alvo, dur]);
  await cdp.send('Page.startScreencast', {format: 'jpeg', quality: 90, maxWidth: 1080, maxHeight: 1700, everyNthFrame: 1});
  inicio = Date.now() / 1000;
  await p.goto(R.url, {waitUntil: 'domcontentloaded'}); await p.evaluate(DEDO);
  for (const a of R.acoes) {
    if (a.esperar) await p.waitForTimeout(a.esperar * 1000);
    if (a.rolar !== undefined) {
      let y = a.rolar; if (typeof y === 'string') y = await p.evaluate(s => { const e = document.querySelector(s); return e ? e.getBoundingClientRect().top + scrollY - 70 : 0 }, y);
      if (a.mais) y += a.mais; await rolar(y, a.dur || 1.5);
    }
    if (a.tocar) {
      const loc = a.exato ? p.getByText(a.tocar, {exact: true}).nth(a.n || 0) : p.getByText(a.tocar).nth(a.n || 0);
      await loc.scrollIntoViewIfNeeded().catch(() => {}); const bx = await loc.boundingBox();
      if (!bx) { console.log('não achei', a.tocar); continue }
      const x = bx.x + bx.width * (a.fx || .5), y = bx.y + bx.height / 2;
      await dedo(x, y, true, 1.15); await p.waitForTimeout(160); await dedo(x, y, true, .85); eventos.push({t: agora(), tipo: 'toque'});
      if (a.som) eventos.push({t: agora(), tipo: 'musica', arq: a.som});
      if (!a.so_mostrar) await loc.click({timeout: 3000}).catch(e => console.log('clique', e.message.slice(0, 60)));
      await p.waitForTimeout(180); await dedo(x, y, false, 1);
    }
  }
  const fim = agora() - t0; await cdp.send('Page.stopScreencast'); await p.waitForTimeout(300); await b.close();
  fs.writeFileSync(OUT + '/tempos.json', JSON.stringify({tempos, fim})); fs.writeFileSync(OUT + '/eventos.json', JSON.stringify(eventos.map(e => ({...e, t: e.t - t0}))));
  console.log('quadros', n, 'duração', fim.toFixed(1));
})();
