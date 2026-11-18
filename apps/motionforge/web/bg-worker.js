// Remoção de fundo dentro do navegador (Web Worker), com Transformers.js + ONNX Runtime Web.
// Modelos testados em 18/11/2026: onnx-community/BiRefNet_lite-ONNX (MIT) e Xenova/modnet (Apache-2.0, pessoas).
// Usa a placa de vídeo (WebGPU) quando o navegador tem; senão, o processador (WASM).
import { pipeline, RawImage, env } from "https://cdn.jsdelivr.net/npm/@huggingface/transformers@4.3.2/+esm";

env.allowLocalModels = false;
let seg = null, current = "";

async function load(model) {
  if (seg && current === model) return;
  const gpu = !!(self.navigator && navigator.gpu && (await navigator.gpu.requestAdapter().catch(() => null)));
  const device = gpu ? "webgpu" : "wasm";
  const dtype = model.includes("modnet") ? (gpu ? "fp16" : "q8") : (gpu ? "fp16" : "fp32");
  const files = {};
  seg = await pipeline("background-removal", model, {
    device, dtype,
    progress_callback: (p) => {
      if (p.status === "progress" && p.total) {
        files[p.file] = [p.loaded, p.total];
        const tot = Object.values(files).reduce((a, [l, t]) => [a[0] + l, a[1] + t], [0, 0]);
        postMessage({ type: "progress", loaded: tot[0], total: tot[1] });
      }
    },
  });
  current = model;
  postMessage({ type: "ready", device });
}

self.onmessage = async (ev) => {
  const m = ev.data;
  try {
    if (m.type === "load") { await load(m.model); return; }
    if (m.type === "run") {
      await load(m.model);
      const img = await RawImage.fromBlob(m.blob);
      const out = await seg(img);
      const blob = await out.toBlob("image/png");
      postMessage({ type: "done", id: m.id, blob, width: out.width, height: out.height });
    }
  } catch (e) {
    postMessage({ type: "error", id: m.id, message: String((e && e.message) || e) });
  }
};
