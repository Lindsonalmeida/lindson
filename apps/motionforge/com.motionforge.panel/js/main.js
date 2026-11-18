// Lógica do painel. Ref CSInterface: https://github.com/Adobe-CEP/CEP-Resources/tree/master/CEP_11.x
const cs = new CSInterface();
const fs = require("fs");
const os = require("os");
const path = require("path");
const { execFile } = require("child_process");
const extDir = cs.getSystemPath(SystemPath.EXTENSION);
const fal = require(path.join(extDir, "js/providers/fal.js"));

const BASE = path.join(os.homedir(), "MotionForge");
const OUT = path.join(BASE, "outputs");
const TMP = path.join(BASE, "tmp");
const CFG = path.join(BASE, "config.json");
[BASE, OUT, TMP].forEach((d) => fs.mkdirSync(d, { recursive: true }));

const $ = (id) => document.getElementById(id);
const status = (m) => ($("status").textContent = m);
const busy = (b) => ($("prog").hidden = !b);
const stamp = () => new Date().toISOString().replace(/[:.]/g, "-");

// ---- Config ----
function loadCfg() { try { return JSON.parse(fs.readFileSync(CFG, "utf8")); } catch { return {}; } }
let cfg = loadCfg();
$("cfgKey").value = cfg.falKey || "";
$("cfgPy").value = cfg.python || "";
$("cfgRembg").value = cfg.rembg || "";
$("btnSave").onclick = () => {
  cfg = { falKey: $("cfgKey").value.trim(), python: $("cfgPy").value.trim(), rembg: $("cfgRembg").value.trim() };
  fs.writeFileSync(CFG, JSON.stringify(cfg, null, 2));
  status("Configuração salva.");
};

// ---- Abas ----
document.querySelectorAll("nav button").forEach((b) => (b.onclick = () => {
  document.querySelectorAll("nav button, .tab").forEach((e) => e.classList.remove("active"));
  b.classList.add("active"); $(b.dataset.tab).classList.add("active");
}));
document.querySelectorAll(".presets button").forEach((b) => (b.onclick = () => ($("animPrompt").value = b.dataset.p)));

// ---- Ponte com o ExtendScript ----
const jsx = (code) => new Promise((r) => cs.evalScript(code, r));
const q = (s) => JSON.stringify(s.replace(/\\/g, "/"));

async function waitFile(p, ms = 15000) {
  const t = Date.now();
  while (Date.now() - t < ms) {
    if (fs.existsSync(p) && fs.statSync(p).size > 0) { await new Promise((r) => setTimeout(r, 300)); return; }
    await new Promise((r) => setTimeout(r, 200));
  }
  throw new Error("Frame não exportado a tempo.");
}

async function getSourceImage() {
  const info = JSON.parse(await jsx("mf_getSelectedLayerInfo()"));
  if (info.error) throw new Error(info.error);
  if (info.file) return { file: info.file, info };
  const out = path.join(TMP, `frame_${stamp()}.png`);
  await jsx(`mf_exportFrame(${q(out)})`);
  await waitFile(out);
  return { file: out, info };
}

async function importFile(p) {
  const r = await jsx(`mf_importToComp(${q(p)})`);
  if (String(r).startsWith("error")) throw new Error(r);
  return r;
}

async function guard(fn) {
  busy(true);
  try { await fn(); } catch (e) { status("Erro: " + e.message); }
  finally { busy(false); }
}

// ---- Remover fundo (local) ----
$("btnBg").onclick = () => guard(async () => {
  status("Exportando imagem...");
  const { file } = await getSourceImage();
  const out = path.join(OUT, `nobg_${stamp()}.png`);
  status("Removendo fundo (primeira vez baixa o modelo)...");
  await new Promise((res, rej) => execFile(
    cfg.python || "python3",
    [path.join(extDir, "python/remove_bg.py"), file, out, cfg.rembg || "birefnet-general"],
    { timeout: 5 * 60 * 1000 },
    (err, so, se) => (err ? rej(new Error(se || err.message)) : res())
  ));
  status("Importado: " + (await importFile(out)));
});

// ---- Animar (imagem -> vídeo) ----
$("btnAnim").onclick = () => guard(async () => {
  if (!cfg.falKey) throw new Error("Configure a chave do fal.ai.");
  const prompt = $("animPrompt").value.trim();
  if (!prompt) throw new Error("Escreva o prompt de movimento.");
  status("Preparando imagem...");
  const { file } = await getSourceImage();
  // Parâmetros variam por modelo: confira a aba "API" da página do modelo em fal.ai/models
  const res = await fal.run(cfg.falKey, $("animModel").value.trim(), {
    prompt, image_url: fal.toDataUri(file), duration: $("animDur").value,
  }, (s) => status("Gerando vídeo: " + s));
  const url = res.video && res.video.url;
  if (!url) throw new Error("Resposta sem vídeo: " + JSON.stringify(res).slice(0, 300));
  const out = await fal.download(url, path.join(OUT, `anim_${stamp()}.mp4`));
  status("Importado: " + (await importFile(out)));
});

// ---- Gerar imagem ----
$("btnGen").onclick = () => guard(async () => {
  if (!cfg.falKey) throw new Error("Configure a chave do fal.ai.");
  const info = JSON.parse(await jsx("mf_getSelectedLayerInfo()"));
  const size = info.width ? { width: info.width, height: info.height } : "landscape_16_9";
  const res = await fal.run(cfg.falKey, $("genModel").value.trim(),
    { prompt: $("genPrompt").value, image_size: size }, (s) => status("Gerando: " + s));
  const url = res.images && res.images[0] && res.images[0].url;
  if (!url) throw new Error("Resposta sem imagem.");
  const out = await fal.download(url, path.join(OUT, `gen_${stamp()}.png`));
  status("Importado: " + (await importFile(out)));
});

status("Pronto.");
