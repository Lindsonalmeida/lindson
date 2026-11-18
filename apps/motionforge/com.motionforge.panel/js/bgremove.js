// Remoção de fundo local: rembg (Python) para imagem e, com ffmpeg, para vídeo
// (extrai frames -> rembg em lote -> sequência PNG com alpha que o AE importa).
"use strict";
const fs = require("fs");
const path = require("path");
const { spawn } = require("child_process");
const S = require("./settings");
const { CancelledError } = require("./lib/http");

const SCRIPT = path.join(__dirname, "..", "python", "remove_bg.py");
let pyCache = null;

// Executa um programa; devolve {code, out, err}. Cancela matando o processo.
function exec(cmd, args, opts = {}) {
  return new Promise((resolve, reject) => {
    let p;
    try { p = spawn(cmd, args, { windowsHide: true, cwd: opts.cwd, env: Object.assign({}, process.env, { PYTHONIOENCODING: "utf-8", PYTHONUTF8: "1" }) }); } catch (e) { return reject(e); }
    let out = "", err = "", buf = "";
    const off = opts.token ? opts.token.onCancel(() => { try { p.kill(); } catch (e) { /* ignora */ } }) : () => {};
    p.stdout.on("data", (d) => {
      const s = d.toString("utf8"); out += s;
      if (opts.onLine) { buf += s; let i; while ((i = buf.indexOf("\n")) >= 0) { const line = buf.slice(0, i).trim(); buf = buf.slice(i + 1); if (line) opts.onLine(line); } }
    });
    p.stderr.on("data", (d) => { const s = d.toString("utf8"); err += s; if (err.length > 20000) err = err.slice(-20000); if (opts.onErr) opts.onErr(s); });
    p.on("error", (e) => { off(); reject(e); });
    p.on("close", (code) => {
      off();
      if (opts.token && opts.token.cancelled) return reject(new CancelledError());
      resolve({ code, out, err });
    });
    if (opts.timeout) setTimeout(() => { try { p.kill(); } catch (e) { /* ignora */ } }, opts.timeout);
  });
}

async function findPython(cfg) {
  const cands = S.pythonCandidates(cfg);
  if (pyCache && cands.includes(pyCache)) return pyCache;
  for (const c of cands) {
    try {
      const r = await exec(c, ["--version"], { timeout: 15000 });
      if (r.code === 0 && /Python 3/.test(r.out + r.err)) { pyCache = c; return c; }
    } catch (e) { /* tenta o próximo */ }
  }
  throw new Error("Python 3 não encontrado. Instale o Python (marque \"Add to PATH\") ou informe o caminho em Config.");
}

function lastError(r) {
  const lines = (r.out || "").trim().split("\n").reverse();
  for (const l of lines) { try { const j = JSON.parse(l); if (j.event === "error") return j.msg; } catch (e) { /* ignora */ } }
  const err = (r.err || "").trim();
  if (/No module named ['"]?rembg/.test(err)) return "O rembg não está instalado neste Python. Rode: pip install \"rembg[cpu]\" pillow";
  if (/No module named ['"]?onnxruntime/.test(err)) return "Falta o onnxruntime. Rode: pip install \"rembg[cpu]\"";
  return err.split("\n").slice(-3).join(" ").slice(0, 400) || `processo terminou com código ${r.code}`;
}

async function runPy(cfg, args, opts = {}) {
  const py = await findPython(cfg);
  const r = await exec(py, [SCRIPT].concat(args), {
    token: opts.token,
    onLine: (line) => { if (!opts.onEvent) return; try { opts.onEvent(JSON.parse(line)); } catch (e) { /* linha não JSON */ } },
  });
  if (r.code !== 0) throw new Error("Remoção de fundo: " + lastError(r));
  return r;
}

async function image(cfg, src, dst, opts = {}) {
  await runPy(cfg, [src, dst, opts.model || cfg.rembgModel || "birefnet-general"], {
    token: opts.token,
    onEvent: (e) => { if (e.event === "status" && opts.onStatus) opts.onStatus(/carregando/.test(e.msg) ? "Carregando o modelo (a 1ª vez baixa ~1 GB)…" : "Recortando…"); },
  });
  if (!fs.existsSync(dst)) throw new Error("O rembg não gerou o arquivo de saída.");
  return dst;
}

async function prep(cfg, src, dst, maxSide) {
  await runPy(cfg, ["--prep", src, dst, "--max", String(maxSide || 2048)]);
  return dst;
}

async function check(cfg) {
  const py = await findPython(cfg);
  const r = await exec(py, [SCRIPT, "--check"], { timeout: 60000 });
  const line = (r.out || "").trim().split("\n").pop();
  const j = JSON.parse(line || "{}");
  j.cmd = py;
  return j;
}

// ---------- ffmpeg ----------
async function ffmpegOk(cfg) {
  try { const r = await exec(S.ffmpegPath(cfg), ["-version"], { timeout: 15000 }); return r.code === 0 ? (r.out.split("\n")[0] || "ffmpeg") : null; } catch (e) { return null; }
}

async function probe(cfg, file) {
  const r = await exec(S.ffprobePath(cfg), ["-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height,r_frame_rate,nb_frames:format=duration", "-of", "json", file], { timeout: 30000 });
  if (r.code !== 0) throw new Error("ffprobe não conseguiu ler o vídeo: " + r.err.slice(0, 200));
  const j = JSON.parse(r.out);
  const s = (j.streams || [])[0] || {};
  const [a, b] = String(s.r_frame_rate || "30/1").split("/").map(Number);
  return { width: s.width, height: s.height, fps: b ? a / b : a, duration: Number((j.format || {}).duration) || 0 };
}

// Extrai frames [start, start+dur) para dir/f_00001.png.
async function extractFrames(cfg, src, dir, range, opts = {}) {
  fs.mkdirSync(dir, { recursive: true });
  const args = ["-hide_banner", "-y"];
  if (range && range.start > 0) args.push("-ss", range.start.toFixed(4));
  args.push("-i", src);
  if (range && range.duration > 0) args.push("-t", range.duration.toFixed(4));
  args.push("-vsync", "0", "-pix_fmt", "rgba", "-progress", "pipe:1", "-nostats", path.join(dir, "f_%05d.png"));
  const total = opts.expectFrames || 0;
  const r = await exec(S.ffmpegPath(cfg), args, {
    token: opts.token,
    onLine: (l) => { const m = l.match(/^frame=(\d+)/); if (m && opts.onProgress) opts.onProgress(total ? Math.min(1, Number(m[1]) / total) : -1, Number(m[1])); },
  });
  if (r.code !== 0) throw new Error("ffmpeg falhou ao extrair os frames: " + r.err.split("\n").slice(-3).join(" ").slice(0, 300));
  const n = fs.readdirSync(dir).filter((f) => /^f_\d+\.png$/.test(f)).length;
  if (!n) throw new Error("ffmpeg não extraiu nenhum frame.");
  return n;
}

// Vídeo inteiro: frames -> rembg em lote -> pasta com sequência PNG (alpha).
async function video(cfg, src, range, outDir, opts = {}) {
  const work = path.join(S.paths.tmp, "frames_" + path.basename(outDir));
  const info = await probe(cfg, src);
  const expect = Math.max(1, Math.round((range && range.duration > 0 ? range.duration : info.duration) * info.fps));
  opts.onStatus && opts.onStatus("Extraindo frames…", 0);
  const n = await extractFrames(cfg, src, work, range, { token: opts.token, expectFrames: expect, onProgress: (p) => opts.onStatus && opts.onStatus("Extraindo frames…", p * 0.1) });
  opts.onStatus && opts.onStatus(`Recortando ${n} frames…`, 0.1);
  await runPy(cfg, ["--batch", work, outDir, "--model", opts.model || cfg.rembgModel || "birefnet-general"], {
    token: opts.token,
    onEvent: (e) => {
      if (!opts.onStatus) return;
      if (e.event === "progress") opts.onStatus(`Recortando frame ${e.done}/${e.total}…`, 0.1 + 0.9 * (e.done / e.total));
      if (e.event === "status") opts.onStatus("Carregando o modelo…", 0.1);
    },
  });
  try { fs.rmSync(work, { recursive: true, force: true }); } catch (e) { /* ignora */ }
  const frames = fs.readdirSync(outDir).filter((f) => /\.png$/i.test(f)).sort();
  return { first: path.join(outDir, frames[0]), frames: frames.length, fps: info.fps };
}

// Corta um trecho do vídeo (para mandar só o necessário à nuvem).
async function trim(cfg, src, dst, range, token) {
  const args = ["-hide_banner", "-y"];
  if (range.start > 0) args.push("-ss", range.start.toFixed(4));
  args.push("-i", src);
  if (range.duration > 0) args.push("-t", range.duration.toFixed(4));
  args.push("-an", "-c:v", "libx264", "-crf", "14", "-preset", "fast", "-pix_fmt", "yuv420p", dst);
  const r = await exec(S.ffmpegPath(cfg), args, { token });
  if (r.code !== 0) throw new Error("ffmpeg falhou ao cortar o vídeo: " + r.err.split("\n").slice(-2).join(" ").slice(0, 300));
  return dst;
}

async function thumb(cfg, file, out) {
  const r = await exec(S.ffmpegPath(cfg), ["-hide_banner", "-y", "-ss", "0.3", "-i", file, "-frames:v", "1", "-vf", "scale=320:-2", out], { timeout: 30000 });
  return r.code === 0 && fs.existsSync(out) ? out : null;
}

module.exports = { exec, findPython, runPy, image, prep, check, ffmpegOk, probe, extractFrames, video, trim, thumb, SCRIPT };
