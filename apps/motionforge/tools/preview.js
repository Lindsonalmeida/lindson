// Pré-visualização da UI fora do AE (Playwright): node tools/preview.js <pasta-saida>
// Usa um núcleo simulado só para desenhar as telas.
const { chromium } = require("playwright");
const path = require("path");
const out = process.argv[2] || ".";
const panel = path.join(__dirname, "..", "com.motionforge.panel", "index.html");
const thumb = path.join(__dirname, "..", "com.motionforge.panel", "icons", "icon-dark@2x.png");
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 360, height: 640 }, deviceScaleFactor: Number(process.env.DSF || 2) });
  await p.addInitScript(({ thumb }) => {
    const models = {
      i2v: [{ id: "fal-ai/kling-video/v3/standard/image-to-video", label: "Kling 3.0 Standard", durations: [5, 10, 15], input: { start_image_url: "{{image}}", prompt: "{{prompt}}", negative_prompt: "{{negative}}", duration: "{{duration:str}}", generate_audio: "{{audio}}" } }],
      t2i: [{ id: "fal-ai/flux/schnell", label: "FLUX.1 schnell (rápido)", input: { prompt: "{{prompt}}", seed: "{{seed}}" } }],
      bg: [{ id: "fal-ai/birefnet/v2", label: "BiRefNet v2 (Heavy)", input: { image_url: "{{image}}" } }],
    };
    let cfg = { provider: "fal", falKey: "x", bgEngine: "local", bgInsert: "dup", hideOriginal: true, isolateLayer: true, rembgModel: "birefnet-general", outDir: "C:/Users/Lindson/MotionForge/outputs", selected: {}, customModels: [], comfyWorkflows: {}, comfyUrl: "http://127.0.0.1:8188", lastTab: "bg" };
    const hist = [1, 2, 3, 4, 5].map((i) => ({ id: "h" + i, type: ["bg", "anim", "gen"][i % 3], file: thumb, thumb, exists: true, createdAt: new Date().toISOString(), prompt: "zoom lento" }));
    window.MF_PREVIEW_CORE = {
      getCfg: () => cfg, setCfg: (p) => (cfg = Object.assign({}, cfg, p)), models: (pv, k) => models[k] || [],
      layerInfo: async () => ({ name: "Produto_Frasco_Hero.png", index: 2, kind: "imagem", srcWidth: 2400, srcHeight: 3000, file: thumb, isStill: true, comp: { id: 1, name: "Comp 1", fps: 30, width: 1920, height: 1080 } }),
      exportFrame: async () => thumb, estimate: async (k) => (k === "bg-local" ? { text: "Grátis · roda no seu computador" } : { text: "≈ US$ 0,42 · US$ 0,084/second", usd: 0.42 }),
      historyList: async () => hist, paths: { config: "C:\\Users\\Lindson\\MotionForge\\config.json", logs: "" }, friendly: (e) => e.message, openPath() {}, cancel() {}, isRunning: () => false,
      removeBg: () => new Promise(() => {}), animate: () => new Promise(() => {}), generate: () => new Promise(() => {}),
    };
  }, { thumb });
  await p.goto("file://" + panel);
  await p.waitForTimeout(700);
  for (const t of ["bg", "anim", "gen", "hist", "cfg"]) {
    await p.evaluate((t) => window.MF_UI.setTab(t), t);
    if (t === "anim") await p.click("#animPresets button:nth-child(1)");
    await p.waitForTimeout(450);
    await p.screenshot({ path: path.join(out, `ui-${t}.png`) });
  }
  await p.evaluate(() => window.MF_UI.setTab("anim"));
  await p.click("#cta");
  await p.evaluate(() => { document.getElementById("jobText").textContent = "Na fila (posição 2)…"; });
  await p.waitForTimeout(500);
  await p.screenshot({ path: path.join(out, "ui-job.png") });
  const errs = [];
  p.on("pageerror", (e) => errs.push(e.message));
  await b.close();
  if (errs.length) { console.error(errs); process.exit(1); }
  console.log("ok");
})();
