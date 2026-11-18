// Teste do MotionForge Web no Chromium (Playwright): node tools/web-teste.js <pasta-montada> <saida>
// 1) remove o fundo de verdade no navegador (MODNet) 2) gerar e animar com o fal.ai simulado (page.route).
const { chromium } = require("playwright");
const http = require("http"), fs = require("fs"), path = require("path");
const root = process.argv[2], out = process.argv[3] || ".";
const IMG = process.argv[4];
const MIME = { ".html": "text/html", ".js": "text/javascript", ".css": "text/css", ".woff2": "font/woff2", ".png": "image/png" };
const srv = http.createServer((q, r) => {
  let p = decodeURIComponent(q.url.split("?")[0]);
  if (p === "/painel/motionforge") p += ".html";
  const f = path.join(root, p);
  if (!fs.existsSync(f) || fs.statSync(f).isDirectory()) { r.writeHead(404); return r.end(); }
  r.writeHead(200, { "Content-Type": MIME[path.extname(f)] || "application/octet-stream" }); fs.createReadStream(f).pipe(r);
}).listen(0);
(async () => {
  const port = srv.address().port;
  const px = process.env.HTTPS_PROXY || process.env.https_proxy;
  const b = await chromium.launch({ proxy: px ? { server: px, bypass: "127.0.0.1,localhost" } : undefined });
  const ctx = await b.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, ignoreHTTPSErrors: true });
  const p = await ctx.newPage();
  const errs = [];
  p.on("pageerror", (e) => errs.push(e.message));
  p.on("console", (m) => { if (m.type() === "error") errs.push("console: " + m.text()); });
  // fal.ai simulado
  const png = fs.readFileSync(IMG);
  let polls = 0;
  await p.route("https://queue.fal.run/**", (r) => {
    const u = r.request().url();
    if (r.request().method() === "POST") return r.fulfill({ json: { request_id: "x", status_url: "https://queue.fal.run/m/requests/x/status", response_url: "https://queue.fal.run/m/requests/x", cancel_url: "https://queue.fal.run/m/requests/x/cancel" } });
    if (u.endsWith("/status")) return r.fulfill({ json: { status: ++polls % 2 ? "IN_PROGRESS" : "COMPLETED" } });
    return r.fulfill({ json: u.includes("x") && polls < 4 ? { images: [{ url: "https://v3.fal.media/gen.png" }], seed: 1 } : { video: { url: "https://v3.fal.media/v.mp4" } } });
  });
  await p.route("https://v3.fal.media/**", (r) => r.request().url().endsWith(".png") ? r.fulfill({ body: png, contentType: "image/png" }) : r.fulfill({ body: fs.readFileSync(process.argv[5]), contentType: "video/mp4" }));
  await p.route("https://api.fal.ai/**", (r) => r.fulfill({ json: { prices: [{ endpoint_id: "x", unit_price: 0.003, unit: "megapixels", currency: "USD" }] } }));

  await p.goto(`http://127.0.0.1:${port}/painel/motionforge`);
  await p.waitForTimeout(800);
  await p.screenshot({ path: path.join(out, "web-1-vazio.png") });
  await p.setInputFiles("#fileIn", IMG);
  await p.selectOption("#bgLocalModel", "Xenova/modnet");
  await p.click("#cta");
  await p.waitForFunction(() => !window.MF.state.busy && window.MF.state.items[0] && (window.MF.state.items[0].out || document.querySelector(".toast.err")), null, { timeout: 300000 });
  const t1 = await p.evaluate(() => window.MF.state.items[0].out ? "ok, resultado " + window.MF.state.items[0].out.blob.size + " bytes" : document.querySelector(".toast.err").textContent);
  await p.waitForTimeout(500);
  await p.screenshot({ path: path.join(out, "web-2-fundo.png") });
  console.log("fundo:", t1);
  // gerar (simulado)
  await p.evaluate(() => { localStorage.setItem("mf.falKey", "k-teste"); });
  await p.evaluate(() => { const i = document.getElementById("falKey"); i.value = "k-teste"; i.dispatchEvent(new Event("change")); });
  await p.click('#nav button[data-tab="gen"]');
  await p.fill("#genPrompt", "pizza artesanal");
  await p.waitForTimeout(600);
  await p.click("#cta");
  await p.waitForFunction(() => window.MF.state.items.length === 2 && !window.MF.state.busy, null, { timeout: 60000 });
  console.log("gerar: itens na mesa =", await p.evaluate(() => window.MF.state.items.length), "| custo:", await p.textContent("#cost"));
  await p.screenshot({ path: path.join(out, "web-3-gerar.png") });
  // animar (simulado)
  await p.click('#nav button[data-tab="anim"]');
  await p.click("#animPresets button");
  await p.click("#cta");
  await p.waitForFunction(() => window.MF.state.items.length === 3 && !window.MF.state.busy, null, { timeout: 60000 });
  console.log("animar: último item =", await p.evaluate(() => window.MF.state.items[2].kind));
  await p.screenshot({ path: path.join(out, "web-4-animar.png") });
  await p.click('#nav button[data-tab="hist"]');
  await p.waitForTimeout(700);
  console.log("histórico:", await p.evaluate(() => document.querySelectorAll(".hcard").length), "itens");
  await p.screenshot({ path: path.join(out, "web-5-hist.png") });
  await p.setViewportSize({ width: 390, height: 844 });
  await p.click('#nav button[data-tab="bg"]');
  await p.waitForTimeout(400);
  await p.screenshot({ path: path.join(out, "web-6-celular.png"), fullPage: false });
  console.log("erros:", errs.length ? errs : "nenhum");
  await b.close(); srv.close();
})().catch((e) => { console.error("FALHOU", e.message); process.exit(1); });
