// Núcleo do MotionForge (Node). Não toca no DOM: a UI (main.js) só chama estas funções.
// Recebe evalScript (ponte com o ExtendScript) para poder ser testado em Node com um AE simulado.
"use strict";
const fs = require("fs");
const path = require("path");
const S = require("./settings");
const M = require("./models");
const H = require("./lib/http");
const E = require("./lib/errors");
const log = require("./lib/logger");
const bg = require("./bgremove");
const hist = require("./history");
const providers = { fal: require("./providers/fal"), replicate: require("./providers/replicate"), comfy: require("./providers/comfy") };

const PROV_NAME = { fal: "fal.ai", replicate: "Replicate", comfy: "ComfyUI" };
const stamp = () => new Date().toISOString().replace(/[-:]/g, "").replace(/\..+/, "").replace("T", "_");

function createCore(opts) {
  const evalScript = opts.evalScript;
  const prov = Object.assign({}, providers, opts.providers || {});
  let cfg = S.load();
  log.init(S.paths.logs);
  let running = null; // { token, kind }

  // ---------- ponte com o AE ----------
  async function jsx(code) {
    const r = await evalScript(code);
    if (r === "EvalScript error." || r === undefined) throw new Error("O After Effects não respondeu ao script (" + code.split("(")[0] + ").");
    return r;
  }
  async function jsxJson(code) {
    const r = await jsx(code);
    try { return JSON.parse(r); } catch (e) { throw new Error("Resposta inesperada do AE: " + String(r).slice(0, 200)); }
  }
  const q = (s) => JSON.stringify(String(s).replace(/\\/g, "/"));

  async function layerInfo() { return jsxJson("mf_getSelectedLayerInfo()"); }

  async function waitFile(p, ms = 30000, token) {
    const t = Date.now();
    let last = -1;
    while (Date.now() - t < ms) {
      if (token) token.throwIfCancelled();
      if (fs.existsSync(p)) {
        const s = fs.statSync(p).size;
        if (s > 0 && s === last) return p;
        last = s;
      }
      await H.sleep(150);
    }
    throw new Error("O AE não exportou o frame a tempo. Tente de novo (a comp está com render muito pesado?).");
  }

  async function exportFrame(info, isolate, token) {
    const out = path.join(S.paths.tmp, `frame_${stamp()}_${Math.random().toString(36).slice(2, 6)}.png`);
    let st = null;
    if (isolate && info.index) st = await jsxJson(`mf_isolate(${info.comp.id}, ${info.index})`);
    try {
      const r = await jsxJson(`mf_exportFrame(${q(out)}, ${info.comp.id}, ${Number(info.comp.time) || 0})`);
      if (r.error) throw new Error("AE: " + r.error);
      await waitFile(out, 30000, token);
    } finally {
      if (st && !st.error) await jsx(`mf_restore(${info.comp.id}, ${info.index}, ${q((st.off || []).join(","))}, ${st.selfWasOn ? "true" : "false"})`).catch(() => {});
    }
    return out;
  }

  async function sourceImage(info, isolate, token) {
    if (info.file && info.isStill && !info.fileUnsupported && fs.existsSync(info.file)) return { file: info.file, fromFile: true };
    return { file: await exportFrame(info, isolate, token), fromFile: false };
  }

  async function place(file, mode, ctx, extra = {}) {
    const r = await jsxJson(`mf_place(${q(file)}, ${q(mode)}, ${(ctx && ctx.compId) || 0}, ${(ctx && ctx.index) || 0}, ${extra.seq ? "true" : "false"}, ${Number(extra.fps) || 0}, ${Number(extra.offset) || 0}, ${extra.hide ? "true" : "false"}, ${q(extra.label || "")})`);
    if (r.error) throw new Error("AE: " + r.error);
    return r;
  }

  // ---------- trabalhos ----------
  async function job(kind, onStatus, fn) {
    if (running) throw new Error("Já existe um trabalho em andamento.");
    const token = new H.CancelToken();
    running = { token, kind };
    const t0 = Date.now();
    log.info(`início ${kind}`);
    try {
      const r = await fn(token, (text, p) => onStatus && onStatus(text, p == null ? -1 : p));
      log.info(`fim ${kind} em ${Math.round((Date.now() - t0) / 1000)}s`, r && { file: r.file });
      return r;
    } catch (e) {
      log.error(`falha ${kind}`, e);
      const err = new Error(E.friendly(e, e.provider || (running && running.provName)));
      err.cancelled = e instanceof H.CancelledError || e.name === "CancelledError";
      throw err;
    } finally { running = null; }
  }
  function cancel() { if (running) running.token.cancel(); }
  const isRunning = () => !!running;

  function keyFor(p) { return p === "fal" ? cfg.falKey : p === "replicate" ? cfg.replicateKey : ""; }

  function extOf(url, fallback) {
    const m = String(url).split("?")[0].match(/\.([a-z0-9]{2,4})$/i);
    if (m && /^(png|jpe?g|webp|mp4|mov|webm|gif)$/i.test(m[1])) return m[1].toLowerCase();
    const f = String(url).match(/filename=[^&]*\.([a-z0-9]{2,4})(?:&|$)/i);
    return f ? f[1].toLowerCase() : fallback;
  }

  async function fetchTo(url, dest, token, headers, onP) {
    if (/^data:/.test(url)) { fs.writeFileSync(dest, Buffer.from(url.split(",")[1], "base64")); return dest; }
    return H.download(url, dest, { token, headers, onProgress: onP });
  }

  function runProvider(p, model, vars, files, token, status, extra) {
    if (running) running.provName = PROV_NAME[p];
    return prov[p].run(Object.assign({ key: keyFor(p), model, vars, files, token, onStatus: (t, pr) => status(t, pr), url: cfg.comfyUrl, workflowDir: opts.comfyDir }, extra || {}));
  }

  function needKey(p) {
    if (p === "fal" && !cfg.falKey) throw new Error("Cole a chave do fal.ai em Config (fal.ai/dashboard/keys).");
    if (p === "replicate" && !cfg.replicateKey) throw new Error("Cole o token do Replicate em Config.");
  }

  // Reduz a imagem antes de mandar à nuvem (rápido e dentro dos limites). Sem Python, manda a original.
  async function cloudImage(file, p) {
    const size = fs.statSync(file).size;
    if (p === "comfy" || (p === "fal" && size < 6e6)) return file;
    try { return await bg.prep(cfg, file, path.join(S.paths.tmp, `up_${stamp()}.jpg`), p === "replicate" ? 1280 : 2048); } catch (e) { return file; }
  }

  // ===== 1. Remover fundo =====
  async function removeBg(o, onStatus) {
    return job("fundo", onStatus, async (token, status) => {
      status("Lendo a camada…");
      const info = await layerInfo();
      if (info.error) throw new Error(info.error);
      const ctx = { compId: info.comp.id, index: info.index };
      const engine = o.engine || cfg.bgEngine;
      const insert = o.insert || cfg.bgInsert;
      const hide = o.hideOriginal != null ? o.hideOriginal : cfg.hideOriginal;
      const tag = stamp();

      // ---- vídeo ----
      if (info.isVideo && info.file) {
        let range = { start: 0, duration: info.srcDuration || 0 }, offset = 0;
        if (Math.abs((info.stretch || 100) - 100) < 0.01 && !info.timeRemap) {
          range = { start: Math.max(0, info.inPoint - info.startTime), duration: Math.max(0.04, info.outPoint - info.inPoint) };
          offset = range.start;
        }
        if (!(await bg.ffmpegOk(cfg))) throw new Error("Para vídeo é preciso o ffmpeg. Instale (winget install Gyan.FFmpeg) ou informe o caminho em Config.");
        if (engine === "cloud") {
          const p = cfg.provider;
          if (p !== "fal") throw new Error("Na nuvem, o recorte de vídeo é só pelo fal.ai. Use o motor Local ou troque o provedor.");
          needKey(p);
          const model = M.find("fal", o.cloudModelVideo || "fal-ai/birefnet/v2/video", cfg.customModels) || M.byKind("fal", "bgv", cfg.customModels)[0];
          status("Cortando o trecho do vídeo…");
          const clip = await bg.trim(cfg, info.file, path.join(S.paths.tmp, `clip_${tag}.mp4`), range, token);
          const r = await runProvider("fal", model, {}, { video: clip }, token, status);
          const out = path.join(cfg.outDir, `nobg_${tag}.${extOf(r.urls[0], "mov")}`);
          status("Baixando o vídeo recortado…");
          await fetchTo(r.urls[0], out, token, null, (pp) => status("Baixando…", pp));
          status("Importando no AE…");
          const pl = await place(out, insert, ctx, { offset, hide, label: path.basename(out) });
          const h = hist.add({ type: "bg", file: out, video: true, provider: "fal", model: model.id, layer: info.name });
          return { file: out, layer: pl.layer, history: h };
        }
        const dir = path.join(cfg.outDir, `nobg_${tag}`);
        const v = await bg.video(cfg, info.file, range, dir, { token, model: o.localModel || cfg.rembgModel, onStatus: status });
        status("Importando a sequência no AE…");
        const pl = await place(v.first, insert, ctx, { seq: true, fps: v.fps, offset, hide, label: `${info.name} · sem fundo` });
        const h = hist.add({ type: "bg", file: v.first, seq: true, fps: v.fps, frames: v.frames, provider: "local", model: o.localModel || cfg.rembgModel, layer: info.name });
        return { file: v.first, layer: pl.layer, frames: v.frames, history: h };
      }

      // ---- imagem / frame ----
      status("Preparando a imagem…");
      const isolate = o.isolate != null ? o.isolate : cfg.isolateLayer;
      const src = await sourceImage(info, isolate, token);
      const out = path.join(cfg.outDir, `nobg_${tag}.png`);
      let model = o.localModel || cfg.rembgModel, provider = "local";
      if (engine === "cloud") {
        provider = cfg.provider;
        if (provider === "comfy") throw new Error("Remoção na nuvem não está disponível no ComfyUI. Use o motor Local (grátis).");
        needKey(provider);
        const m = M.find(provider, o.cloudModel, cfg.customModels) || M.byKind(provider, "bg", cfg.customModels)[0];
        model = m.id;
        const r = await runProvider(provider, m, {}, { image: await cloudImage(src.file, provider) }, token, status);
        status("Baixando…");
        await fetchTo(r.urls[0], out, token, r.authHeaders);
      } else {
        await bg.image(cfg, src.file, out, { token, model, onStatus: status });
      }
      status("Importando no AE…");
      const mode = src.fromFile ? insert : "comp";
      const pl = await place(out, mode, ctx, { hide, label: path.basename(out) });
      const h = hist.add({ type: "bg", file: out, provider, model, layer: info.name });
      return { file: out, layer: pl.layer, history: h };
    });
  }

  function compDims(info) { return info && info.comp ? { w: info.comp.width, h: info.comp.height } : null; }

  function wanDims(w, h) {
    const r = w / h;
    if (r > 1.2) return { width: 832, height: 480 };
    if (r < 0.83) return { width: 480, height: 832 };
    return { width: 624, height: 624 };
  }

  // ===== 2. Animar imagem =====
  async function animate(o, onStatus) {
    return job("animar", onStatus, async (token, status) => {
      const p = o.provider || cfg.provider;
      needKey(p);
      const model = M.find(p, o.modelId, cfg.customModels) || M.byKind(p, "i2v", cfg.customModels)[0];
      if (!model) throw new Error("Nenhum modelo de vídeo para este provedor.");
      const prompt = String(o.prompt || "").trim();
      if (!prompt) throw new Error("Escreva o movimento que você quer.");
      let info = null;
      try { info = await layerInfo(); } catch (e) { info = null; }
      let file = o.sourceFile;
      if (!file) {
        if (!info || info.error) throw new Error((info && info.error) || "Selecione uma camada.");
        status("Preparando a imagem…");
        file = (await sourceImage(info, o.isolate != null ? o.isolate : cfg.isolateLayer, token)).file;
      }
      const ctx = info && !info.error ? { compId: info.comp.id, index: info.index } : (info && info.comp ? { compId: info.comp.id, index: 0 } : null);
      const dims = compDims(info) || { w: 1920, h: 1080 };
      const vars = {
        prompt, negative: o.negative || "", seed: o.seed === "" || o.seed == null ? "" : Number(o.seed),
        audio: !!(o.audio != null ? o.audio : cfg.generateAudio), duration: M.nearestDuration(model, Number(o.duration) || 5),
        aspect: model.aspects ? M.nearestAspect(model.aspects, dims.w, dims.h) : "",
      };
      Object.assign(vars, wanDims(dims.w, dims.h));
      const r = await runProvider(p, model, vars, { image: await cloudImage(file, p) }, token, status, { workflowPath: cfg.comfyWorkflows && cfg.comfyWorkflows.i2v });
      const tag = stamp();
      let out, seq = false, fps = 0;
      if (r.sequence) {
        const dir = path.join(cfg.outDir, `anim_${tag}`);
        fs.mkdirSync(dir, { recursive: true });
        for (let i = 0; i < r.urls.length; i++) {
          status(`Baixando frames ${i + 1}/${r.urls.length}…`, i / r.urls.length);
          await fetchTo(r.urls[i], path.join(dir, `f_${String(i + 1).padStart(5, "0")}.png`), token);
        }
        out = path.join(dir, "f_00001.png"); seq = true; fps = r.fps || model.fps || 16;
      } else {
        out = path.join(cfg.outDir, `anim_${tag}.${extOf(r.urls[0], "mp4")}`);
        status("Baixando o vídeo…", 0);
        await fetchTo(r.urls[0], out, token, r.authHeaders, (pp) => status("Baixando o vídeo…", pp));
      }
      status("Importando no AE…");
      const pl = await place(out, "fit", ctx, { seq, fps, label: path.basename(seq ? path.dirname(out) : out) });
      const cost = await estimate("i2v", p, model.id, vars).catch(() => null);
      const h = hist.add({ type: "anim", file: out, seq, fps, provider: p, model: model.id, prompt, duration: vars.duration, cost: cost && cost.usd, source: file });
      return { file: out, layer: pl.layer, history: h };
    });
  }

  function aspectDims(aspect, info, long) {
    const L = long || 1440;
    let w, h;
    if (aspect === "comp" || !aspect) { const d = compDims(info); if (d) { w = d.w; h = d.h; } else { w = 16; h = 9; } }
    else { const [a, b] = aspect.split(":").map(Number); w = a; h = b; }
    const s = L / Math.max(w, h);
    const r16 = (v) => Math.max(256, Math.round((v * s) / 16) * 16);
    return { width: r16(w), height: r16(h), ratio: w / h };
  }

  // ===== 3. Gerar imagem =====
  async function generate(o, onStatus) {
    return job("gerar", onStatus, async (token, status) => {
      const p = o.provider || cfg.provider;
      needKey(p);
      const model = M.find(p, o.modelId, cfg.customModels) || M.byKind(p, "t2i", cfg.customModels)[0];
      const prompt = String(o.prompt || "").trim();
      if (!prompt) throw new Error("Descreva a imagem que você quer.");
      let info = null;
      try { info = await layerInfo(); } catch (e) { info = null; }
      const d = aspectDims(o.aspect, info);
      const vars = { prompt, negative: o.negative || "", seed: o.seed === "" || o.seed == null ? "" : Number(o.seed), size: { width: d.width, height: d.height } };
      if (model.aspects) { const [a, b] = [d.width, d.height]; vars.aspect = M.nearestAspect(model.aspects, a, b); }
      if (p === "comfy") { const c = aspectDims(o.aspect, info, 1216); vars.width = Math.round(c.width / 64) * 64; vars.height = Math.round(c.height / 64) * 64; }
      const r = await runProvider(p, model, vars, null, token, status, { workflowPath: cfg.comfyWorkflows && cfg.comfyWorkflows.t2i });
      const out = path.join(cfg.outDir, `gen_${stamp()}.${extOf(r.urls[0], "png")}`);
      status("Baixando a imagem…");
      await fetchTo(r.urls[0], out, token, r.authHeaders);
      status("Importando no AE…");
      const ctx = info && info.comp ? { compId: info.comp.id, index: info.index || 0 } : null;
      const pl = await place(out, ctx ? "fit" : "project", ctx, { label: path.basename(out) });
      const cost = await estimate("t2i", p, model.id, vars).catch(() => null);
      const h = hist.add({ type: "gen", file: out, provider: p, model: model.id, prompt, seed: r.seed, cost: cost && cost.usd });
      return { file: out, layer: pl.layer, history: h };
    });
  }

  // ===== custo estimado =====
  const fmtUsd = (v) => "US$ " + (v < 0.1 ? v.toFixed(3) : v.toFixed(2)).replace(".", ",");
  async function estimate(kind, p, modelId, vars) {
    if (kind === "bg-local") return { text: "Grátis · roda no seu computador" };
    if (p === "comfy") return { text: "Grátis · roda na sua GPU (ComfyUI)" };
    if (p === "replicate") return { text: `Preço por uso: replicate.com/${String(modelId).split(":")[0]}`, link: `https://replicate.com/${String(modelId).split(":")[0]}` };
    if (p === "fal") {
      if (!cfg.falKey) return { text: "Cole a chave do fal.ai para ver o custo" };
      const ck = "fal-price:" + modelId;
      let pr = S.cacheGet(ck, 12 * 3600 * 1000);
      if (!pr) {
        const all = await prov.fal.pricing(cfg.falKey, [modelId]);
        pr = all[modelId];
        if (pr) S.cacheSet(ck, pr);
      }
      if (!pr) return { text: "Preço indisponível para este modelo" };
      const model = M.find("fal", modelId, cfg.customModels) || {};
      const u = prov.fal.units(pr.unit, model, vars || {});
      const usd = pr.price * u;
      const UNIT = { second: "segundo", seconds: "segundo", image: "imagem", images: "imagem", video: "vídeo", videos: "vídeo", megapixel: "megapixel", megapixels: "megapixel", request: "uso", requests: "uso" };
      const unitTxt = UNIT[String(pr.unit || "").toLowerCase()] || String(pr.unit || "uso");
      return { usd, text: `≈ ${fmtUsd(usd)} · ${fmtUsd(pr.price)}/${unitTxt}`, unit: pr.unit, price: pr.price };
    }
    return { text: "" };
  }

  // ===== histórico =====
  async function historyList() {
    const items = hist.list();
    for (const h of items) {
      h.exists = hist.exists(h);
      if (/\.(png|jpe?g|webp)$/i.test(h.file)) h.thumb = h.file;
      else if (h.exists) {
        const t = hist.thumbPath(h);
        if (fs.existsSync(t)) h.thumb = t;
        else if (opts.makeThumbs !== false) h.thumb = await bg.thumb(cfg, h.file, t).catch(() => null);
      }
    }
    return items;
  }
  async function reimport(id) {
    const h = hist.list().find((x) => x.id === id);
    if (!h) throw new Error("Item não encontrado.");
    if (!hist.exists(h)) throw new Error("O arquivo não existe mais: " + h.file);
    let info = null;
    try { info = await layerInfo(); } catch (e) { info = null; }
    const ctx = info && info.comp ? { compId: info.comp.id, index: info.index || 0 } : null;
    return place(h.file, ctx ? "fit" : "project", ctx, { seq: h.seq, fps: h.fps, label: path.basename(h.seq ? path.dirname(h.file) : h.file) });
  }

  // ===== config e testes =====
  function getCfg() { return cfg; }
  function setCfg(patch) {
    if (patch.customModels !== undefined && typeof patch.customModels === "string") {
      const t = patch.customModels.trim();
      patch.customModels = t ? JSON.parse(t) : [];
      if (!Array.isArray(patch.customModels)) throw new Error("A lista de modelos precisa ser um array JSON [ … ].");
    }
    cfg = S.save(S.merge(cfg, patch));
    return cfg;
  }
  function models(p, kind) { return M.byKind(p || cfg.provider, kind, cfg.customModels); }

  async function testFal() { await prov.fal.checkKey(cfg.falKey); return "Chave válida"; }
  async function testReplicate() { await prov.replicate.checkKey(cfg.replicateKey); return "Token válido"; }
  async function testComfy() { return prov.comfy.check(cfg.comfyUrl); }
  async function testPython() {
    const r = await bg.check(cfg);
    if (!r.rembg) return { ok: false, text: `Python ${r.python} ok, mas falta o rembg: pip install "rembg[cpu]" pillow` };
    return { ok: true, text: `Python ${r.python} · rembg ${r.rembg} · ${r.gpu ? "GPU ativa" : "CPU"}`, cmd: r.cmd };
  }
  async function testFfmpeg() { const v = await bg.ffmpegOk(cfg); if (!v) throw new Error("ffmpeg não encontrado"); return v.replace(/ Copyright.*/, ""); }

  function openPath(p) {
    const { spawn } = require("child_process");
    const cmd = process.platform === "win32" ? "explorer" : process.platform === "darwin" ? "open" : "xdg-open";
    try { spawn(cmd, [p], { detached: true, stdio: "ignore" }).unref(); } catch (e) { /* ignora */ }
  }

  return {
    openPath, layerInfo, exportFrame, sourceImage, place, removeBg, animate, generate, estimate, cancel, isRunning,
    historyList, reimport, historyRemove: hist.remove, getCfg, setCfg, models,
    testFal, testReplicate, testComfy, testPython, testFfmpeg, paths: S.paths, friendly: E.friendly,
  };
}

module.exports = { createCore };
