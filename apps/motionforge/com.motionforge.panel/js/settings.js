// Preferências e chaves do usuário: JSON fora do plugin, na pasta do usuário.
// Windows: C:\Users\<voce>\MotionForge\config.json · macOS: ~/MotionForge/config.json
// As chaves NUNCA ficam no código nem no repositório.
"use strict";
const fs = require("fs");
const os = require("os");
const path = require("path");

const BASE = process.env.MOTIONFORGE_HOME || path.join(os.homedir(), "MotionForge");
const isWin = process.platform === "win32";

const DEFAULTS = {
  version: 1,
  provider: "fal",                 // fal | replicate | comfy
  falKey: "",
  replicateKey: "",
  comfyUrl: "http://127.0.0.1:8188",
  python: "",                      // vazio = detectar (py / python / python3)
  ffmpeg: "",                      // vazio = "ffmpeg" no PATH
  outDir: path.join(BASE, "outputs"),
  rembgModel: "birefnet-general",
  bgEngine: "local",               // local (rembg) | cloud (provedor ativo)
  bgInsert: "dup",                 // dup = nova camada acima com as mesmas animações | replace = troca a fonte
  hideOriginal: true,
  isolateLayer: true,              // exporta só a camada selecionada (sem as outras)
  generateAudio: false,
  selected: { i2v: {}, t2i: {}, bg: {} }, // modelo escolhido por provedor
  customModels: [],                // modelos extras (ver models.js)
  comfyWorkflows: { i2v: "", t2i: "" }, // caminhos de workflows próprios (formato API)
  lastTab: "bg",
};

const paths = {
  base: BASE,
  config: path.join(BASE, "config.json"),
  history: path.join(BASE, "history.json"),
  tmp: path.join(BASE, "tmp"),
  logs: path.join(BASE, "logs"),
  thumbs: path.join(BASE, "thumbs"),
  cache: path.join(BASE, "cache.json"),
};

function ensureDirs(cfg) {
  [paths.base, paths.tmp, paths.logs, paths.thumbs, (cfg && cfg.outDir) || DEFAULTS.outDir].forEach((d) => {
    try { fs.mkdirSync(d, { recursive: true }); } catch (e) { /* ignora */ }
  });
}

function merge(a, b) {
  const out = Array.isArray(a) ? a.slice() : Object.assign({}, a);
  Object.keys(b || {}).forEach((k) => {
    const v = b[k];
    if (v && typeof v === "object" && !Array.isArray(v) && a && typeof a[k] === "object" && !Array.isArray(a[k])) out[k] = merge(a[k], v);
    else if (v !== undefined) out[k] = v;
  });
  return out;
}

function load() {
  let saved = {};
  try { saved = JSON.parse(fs.readFileSync(paths.config, "utf8")); } catch (e) { saved = {}; }
  const cfg = merge(DEFAULTS, saved);
  ensureDirs(cfg);
  return cfg;
}

function save(cfg) {
  ensureDirs(cfg);
  const clean = merge(DEFAULTS, cfg);
  const tmp = paths.config + ".tmp";
  fs.writeFileSync(tmp, JSON.stringify(clean, null, 2), { mode: 0o600 });
  fs.renameSync(tmp, paths.config);
  return clean;
}

// Cache simples (preços etc.) com validade.
function cacheGet(key, maxAgeMs) {
  try {
    const c = JSON.parse(fs.readFileSync(paths.cache, "utf8"));
    const e = c[key];
    if (e && Date.now() - e.t < maxAgeMs) return e.v;
  } catch (e) { /* sem cache */ }
  return undefined;
}
function cacheSet(key, v) {
  let c = {};
  try { c = JSON.parse(fs.readFileSync(paths.cache, "utf8")); } catch (e) { c = {}; }
  c[key] = { t: Date.now(), v };
  try { fs.writeFileSync(paths.cache, JSON.stringify(c)); } catch (e) { /* ignora */ }
}

function pythonCandidates(cfg) {
  if (cfg.python) return [cfg.python];
  return isWin ? ["py", "python", "python3"] : ["python3", "python"];
}
function ffmpegPath(cfg) { return cfg.ffmpeg || "ffmpeg"; }
function ffprobePath(cfg) {
  const f = ffmpegPath(cfg);
  if (f === "ffmpeg") return "ffprobe";
  return f.replace(/ffmpeg(\.exe)?$/i, (m, ext) => "ffprobe" + (ext || ""));
}

module.exports = { DEFAULTS, paths, load, save, merge, ensureDirs, cacheGet, cacheSet, pythonCandidates, ffmpegPath, ffprobePath, isWin };
