// Catálogo de modelos (configurável). IDs e parâmetros conferidos em 18/11/2026:
//  - fal.ai: catálogo https://api.fal.ai/v1/models e schema de cada endpoint
//            (https://fal.ai/api/openapi/queue/openapi.json?endpoint_id=<id>)
//  - Replicate: aba API de cada modelo (https://replicate.com/<dono>/<modelo>/api/schema)
// Modelos mudam rápido: para trocar ou acrescentar, use Config > Modelos (JSON), sem mexer no código.
//
// Template de entrada: strings "{{campo}}" viram o valor do trabalho.
//   {{prompt}} {{negative}} {{image}} {{video}} {{seed}} {{aspect}} {{size}} {{audio}}
//   {{duration}} (número) · {{duration:str}} (texto) · "{{duration}}s" (texto com sufixo)
// Campo que fica vazio (ex.: seed não informada) é removido do envio.
"use strict";

const ASPECTS_LUMA = ["16:9", "9:16", "1:1", "4:3", "3:4", "21:9"];

const BUILTIN = [
  // ---------- fal.ai · imagem -> vídeo ----------
  { provider: "fal", kind: "i2v", id: "fal-ai/kling-video/v3/standard/image-to-video", label: "Kling 3.0 Standard", durations: [5, 10, 15],
    input: { start_image_url: "{{image}}", prompt: "{{prompt}}", negative_prompt: "{{negative}}", duration: "{{duration:str}}", generate_audio: "{{audio}}" } },
  { provider: "fal", kind: "i2v", id: "fal-ai/kling-video/v2.5-turbo/pro/image-to-video", label: "Kling 2.5 Turbo Pro", durations: [5, 10],
    input: { image_url: "{{image}}", prompt: "{{prompt}}", negative_prompt: "{{negative}}", duration: "{{duration:str}}" } },
  { provider: "fal", kind: "i2v", id: "kling/v4/image-to-video", label: "Kling 4.0", durations: [5, 10],
    input: { start_image_url: "{{image}}", prompt: "{{prompt}}", duration: "{{duration}}", resolution: "1080p" } },
  { provider: "fal", kind: "i2v", id: "wan/v2.6/image-to-video/flash", label: "Wan 2.6 Flash", durations: [5, 10, 15],
    input: { image_url: "{{image}}", prompt: "{{prompt}}", negative_prompt: "{{negative}}", duration: "{{duration:str}}", resolution: "1080p", generate_audio: "{{audio}}", seed: "{{seed}}" } },
  { provider: "fal", kind: "i2v", id: "fal-ai/minimax/hailuo-2.3-fast/standard/image-to-video", label: "Hailuo 2.3 Fast", durations: [6, 10],
    input: { image_url: "{{image}}", prompt: "{{prompt}}", duration: "{{duration:str}}" } },
  { provider: "fal", kind: "i2v", id: "luma/agent/ray/v3.2/image-to-video", label: "Luma Ray 3.2", durations: [5, 10], aspects: ASPECTS_LUMA,
    input: { image_url: "{{image}}", prompt: "{{prompt}}", duration: "{{duration}}s", aspect_ratio: "{{aspect}}", resolution: "720p" } },
  { provider: "fal", kind: "i2v", id: "fal-ai/ltx-2.3/image-to-video/fast", label: "LTX 2.3 Fast", durations: [6, 8, 10],
    input: { image_url: "{{image}}", prompt: "{{prompt}}", duration: "{{duration}}", generate_audio: "{{audio}}" } },
  { provider: "fal", kind: "i2v", id: "bytedance/seedance-2.0/fast/image-to-video", label: "Seedance 2.0 Fast", durations: [5, 10],
    input: { image_url: "{{image}}", prompt: "{{prompt}}", duration: "{{duration:str}}", resolution: "720p", generate_audio: "{{audio}}" } },

  // ---------- fal.ai · texto -> imagem ----------
  { provider: "fal", kind: "t2i", id: "fal-ai/flux/schnell", label: "FLUX.1 schnell (rápido)",
    input: { prompt: "{{prompt}}", image_size: "{{size}}", seed: "{{seed}}", num_images: 1, output_format: "png" } },
  { provider: "fal", kind: "t2i", id: "fal-ai/flux/dev", label: "FLUX.1 dev",
    input: { prompt: "{{prompt}}", image_size: "{{size}}", seed: "{{seed}}", num_images: 1, output_format: "png" } },
  { provider: "fal", kind: "t2i", id: "fal-ai/flux-pro/v1.1", label: "FLUX 1.1 pro",
    input: { prompt: "{{prompt}}", image_size: "{{size}}", seed: "{{seed}}", output_format: "png" } },
  { provider: "fal", kind: "t2i", id: "fal-ai/flux-2-pro", label: "FLUX 2 pro",
    input: { prompt: "{{prompt}}", image_size: "{{size}}", seed: "{{seed}}", output_format: "png" } },
  { provider: "fal", kind: "t2i", id: "fal-ai/fast-sdxl", label: "SDXL",
    input: { prompt: "{{prompt}}", negative_prompt: "{{negative}}", image_size: "{{size}}", seed: "{{seed}}", format: "png" } },

  // ---------- fal.ai · remover fundo (nuvem) ----------
  { provider: "fal", kind: "bg", id: "fal-ai/birefnet/v2", label: "BiRefNet v2 (Heavy)",
    input: { image_url: "{{image}}", model: "General Use (Heavy)", operating_resolution: "2048x2048", output_format: "png", refine_foreground: true } },
  { provider: "fal", kind: "bg", id: "fal-ai/bria/background/remove", label: "Bria RMBG 2.0",
    input: { image_url: "{{image}}" } },
  { provider: "fal", kind: "bgv", id: "fal-ai/birefnet/v2/video", label: "BiRefNet v2 vídeo (ProRes 4444 com alpha)",
    input: { video_url: "{{video}}", model: "General Use (Heavy)", video_output_type: "PRORES4444 (.mov)", video_quality: "high", refine_foreground: true } },

  // ---------- Replicate ----------
  { provider: "replicate", kind: "i2v", id: "kwaivgi/kling-v2.5-turbo-pro", label: "Kling 2.5 Turbo Pro", durations: [5, 10],
    input: { start_image: "{{image}}", prompt: "{{prompt}}", negative_prompt: "{{negative}}", duration: "{{duration}}" } },
  { provider: "replicate", kind: "i2v", id: "minimax/hailuo-02", label: "Hailuo 02", durations: [6, 10],
    input: { first_frame_image: "{{image}}", prompt: "{{prompt}}", duration: "{{duration}}" } },
  { provider: "replicate", kind: "i2v", id: "wan-video/wan-2.2-i2v-fast", label: "Wan 2.2 I2V Fast (≈5 s)", durations: [5],
    input: { image: "{{image}}", prompt: "{{prompt}}", seed: "{{seed}}", resolution: "720p" } },
  { provider: "replicate", kind: "t2i", id: "black-forest-labs/flux-schnell", label: "FLUX.1 schnell",
    input: { prompt: "{{prompt}}", aspect_ratio: "{{aspect}}", seed: "{{seed}}", output_format: "png", num_outputs: 1 }, aspects: ["1:1", "16:9", "21:9", "3:2", "2:3", "4:5", "5:4", "3:4", "4:3", "9:16", "9:21"] },
  { provider: "replicate", kind: "t2i", id: "black-forest-labs/flux-dev", label: "FLUX.1 dev",
    input: { prompt: "{{prompt}}", aspect_ratio: "{{aspect}}", seed: "{{seed}}", output_format: "png", num_outputs: 1 }, aspects: ["1:1", "16:9", "21:9", "3:2", "2:3", "4:5", "5:4", "3:4", "4:3", "9:16", "9:21"] },
  { provider: "replicate", kind: "bg", id: "bria/remove-background", label: "Bria Remove Background",
    input: { image: "{{image}}" } },

  // ---------- ComfyUI local (workflows em /comfy, formato API) ----------
  { provider: "comfy", kind: "i2v", id: "comfy/wan21-i2v", label: "Wan 2.1 I2V 480p (local)", durations: [3, 5], workflow: "wan21-i2v-api.json", fps: 16 },
  { provider: "comfy", kind: "t2i", id: "comfy/sdxl-t2i", label: "SDXL (local)", workflow: "sdxl-t2i-api.json" },
];

function all(custom) {
  const list = BUILTIN.slice();
  (custom || []).forEach((m) => {
    if (!m || !m.id || !m.provider || !m.kind) return;
    const i = list.findIndex((x) => x.provider === m.provider && x.id === m.id);
    const entry = Object.assign({ custom: true }, m);
    if (i >= 0) list[i] = Object.assign({}, list[i], entry); else list.push(entry);
  });
  return list;
}

function byKind(provider, kind, custom) { return all(custom).filter((m) => m.provider === provider && m.kind === kind); }
function find(provider, id, custom) { return all(custom).find((m) => m.provider === provider && m.id === id); }

function usesField(model, field) {
  if (model.workflow) return field === "prompt" || field === "negative" || field === "seed" || field === "image" || field === "duration";
  return JSON.stringify(model.input || {}).indexOf("{{" + field) >= 0;
}

// Substitui os marcadores. Strings iguais a "{{x}}" recebem o valor tipado.
function render(tpl, vars) {
  const DROP = {};
  function val(name) {
    const [k, mod] = name.split(":");
    let v = vars[k];
    if (v === undefined || v === null || v === "") return DROP;
    if (mod === "str") v = String(v);
    if (mod === "int") v = parseInt(v, 10);
    return v;
  }
  function walk(x) {
    if (typeof x === "string") {
      const whole = x.match(/^\{\{([a-z_:]+)\}\}$/i);
      if (whole) return val(whole[1]);
      let dropped = false;
      const s = x.replace(/\{\{([a-z_:]+)\}\}/gi, (m, n) => { const v = val(n); if (v === DROP) { dropped = true; return ""; } return String(v); });
      return dropped ? DROP : s;
    }
    if (Array.isArray(x)) return x.map(walk).filter((v) => v !== DROP);
    if (x && typeof x === "object") {
      const o = {};
      Object.keys(x).forEach((k) => { const v = walk(x[k]); if (v !== DROP) o[k] = v; });
      return o;
    }
    return x;
  }
  return walk(tpl);
}

function nearestDuration(model, want) {
  const ds = model.durations;
  if (!ds || !ds.length) return want;
  return ds.reduce((a, b) => (Math.abs(b - want) < Math.abs(a - want) ? b : a), ds[0]);
}

// Proporção mais próxima da comp dentro da lista do modelo.
function nearestAspect(list, w, h) {
  const r = w / h;
  let best = list[0], bd = Infinity;
  list.forEach((a) => { const [x, y] = a.split(":").map(Number); const d = Math.abs(Math.log((x / y) / r)); if (d < bd) { bd = d; best = a; } });
  return best;
}

// Tamanho de imagem para fal (múltiplo de 16, lado maior até 2048, mantendo a proporção da comp).
function imageSize(w, h, maxSide) {
  if (!w || !h) return "landscape_16_9";
  const m = maxSide || 1536;
  const s = Math.min(1, m / Math.max(w, h));
  const r16 = (v) => Math.max(256, Math.round((v * s) / 16) * 16);
  return { width: r16(w), height: r16(h) };
}

// Procura a(s) URL(s) do resultado em qualquer formato comum de resposta.
function extractUrls(res) {
  const urls = [];
  const push = (u) => { if (typeof u === "string" && /^(https?:|data:)/.test(u)) urls.push(u); };
  if (!res) return urls;
  if (typeof res === "string") { push(res); return urls; }
  if (Array.isArray(res)) { res.forEach((r) => urls.push(...extractUrls(r))); return urls; }
  if (res.video && res.video.url) push(res.video.url);
  if (res.images) res.images.forEach((i) => push(i && i.url));
  if (res.image && res.image.url) push(res.image.url);
  if (res.output !== undefined) urls.push(...extractUrls(res.output));
  if (!urls.length && res.url) push(res.url);
  return urls;
}

module.exports = { BUILTIN, all, byKind, find, render, usesField, nearestDuration, nearestAspect, imageSize, extractUrls };
