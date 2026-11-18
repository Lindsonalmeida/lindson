// Cliente fal.ai via HTTP (sem SDK), para o Node do CEP.
// Refs (conferidas em 18/11/2026):
//  Fila:    https://fal.ai/docs/documentation/model-apis/inference/queue.md
//           submit POST https://queue.fal.run/<modelo> -> {request_id, status_url, response_url, cancel_url}
//           status IN_QUEUE | IN_PROGRESS | COMPLETED (com "error" se falhou) · cancelar: PUT cancel_url
//           Use SEMPRE as URLs devolvidas no submit (elas usam só dono/app, não o caminho inteiro).
//  Upload:  POST https://rest.fal.ai/storage/upload/initiate?storage_type=fal-cdn-v3 {content_type, file_name}
//           -> {upload_url, file_url}; depois PUT do arquivo em upload_url (mesmo fluxo do @fal-ai/client 1.11)
//  Preço:   GET https://api.fal.ai/v1/models/pricing?endpoint_id=<id> -> {prices:[{unit_price, unit, currency}]}
"use strict";
const fs = require("fs");
const path = require("path");
const H = require("../lib/http");
const M = require("../models");

const MIME = { png: "image/png", jpg: "image/jpeg", jpeg: "image/jpeg", webp: "image/webp", mp4: "video/mp4", mov: "video/quicktime", webm: "video/webm" };
const mimeOf = (f) => MIME[path.extname(f).slice(1).toLowerCase()] || "application/octet-stream";

function create(opts = {}) {
  const QUEUE = opts.queue || "https://queue.fal.run";
  const REST = opts.rest || "https://rest.fal.ai";
  const API = opts.api || "https://api.fal.ai/v1";
  const POLL = opts.pollMs || 2500;
  const TIMEOUT = opts.timeoutMs || 15 * 60 * 1000;
  const auth = (key) => ({ Authorization: "Key " + key });

  async function upload(key, file, token, onProgress) {
    const init = await H.json(`${REST}/storage/upload/initiate?storage_type=fal-cdn-v3`, {
      method: "POST", headers: auth(key), token,
      body: { content_type: mimeOf(file), file_name: path.basename(file) },
    });
    if (!init.upload_url || !init.file_url) throw new Error("fal: upload não iniciado.");
    await H.request(init.upload_url, { method: "PUT", headers: { "Content-Type": mimeOf(file) }, body: fs.readFileSync(file), token, timeout: 300000 });
    if (onProgress) onProgress(1);
    return init.file_url;
  }

  async function run(job) {
    const { key, model, vars, token, onStatus = () => {} } = job;
    if (!key) throw new Error("Cole a chave do fal.ai na aba Config.");
    const v = Object.assign({}, vars);
    if (job.files && job.files.image) { onStatus("Enviando imagem…", -1); v.image = await upload(key, job.files.image, token); }
    if (job.files && job.files.video) { onStatus("Enviando vídeo…", -1); v.video = await upload(key, job.files.video, token); }
    const input = M.render(model.input, v);

    onStatus("Na fila…", -1);
    const sub = await H.json(`${QUEUE}/${model.id}`, { method: "POST", headers: auth(key), body: input, token });
    if (!sub.status_url || !sub.response_url) throw new Error("fal: resposta de envio inesperada.");
    const cancelUrl = sub.cancel_url || sub.status_url.replace(/\/status$/, "/cancel");
    const offCancel = token ? token.onCancel(() => { H.raw(cancelUrl, { method: "PUT", headers: auth(key), timeout: 10000 }).catch(() => {}); }) : () => {};

    try {
      const t0 = Date.now();
      let lastStatus = "";
      for (;;) {
        if (Date.now() - t0 > TIMEOUT) {
          H.raw(cancelUrl, { method: "PUT", headers: auth(key), timeout: 10000 }).catch(() => {});
          throw new Error(`O provedor passou de ${Math.round(TIMEOUT / 60000)} min sem terminar. O pedido foi cancelado; tente um modelo mais rápido.`);
        }
        await H.sleep(POLL, token);
        const st = await H.json(sub.status_url, { headers: auth(key), token });
        if (st.status === "IN_QUEUE") onStatus(st.queue_position != null ? `Na fila (posição ${st.queue_position + 1})…` : "Na fila…", -1, { phase: "queue" });
        else if (st.status === "IN_PROGRESS") onStatus("Gerando…", -1, { phase: "run" });
        if (st.status === "COMPLETED") {
          if (st.error) throw Object.assign(new Error("O modelo falhou: " + st.error), { provider: "fal.ai" });
          break;
        }
        if (st.status && st.status !== lastStatus) lastStatus = st.status;
      }
      onStatus("Buscando resultado…", -1);
      const res = await H.json(sub.response_url, { headers: auth(key), token });
      const urls = M.extractUrls(res);
      if (!urls.length) throw new Error("O modelo respondeu sem arquivo: " + JSON.stringify(res).slice(0, 240));
      return { urls, requestId: sub.request_id, raw: res, seed: res.seed };
    } finally { offCancel(); }
  }

  async function pricing(key, ids) {
    if (!key || !ids.length) return {};
    const q = ids.map((i) => "endpoint_id=" + encodeURIComponent(i)).join("&");
    const r = await H.json(`${API}/models/pricing?${q}`, { headers: auth(key), retries: 1, timeout: 15000 });
    const out = {};
    (r.prices || []).forEach((p) => { out[p.endpoint_id] = { unit: p.unit, price: p.unit_price, currency: p.currency || "USD" }; });
    return out;
  }

  // Quantas unidades o trabalho deve cobrar, a partir da unidade informada pelo fal.
  function units(unit, model, vars) {
    const u = String(unit || "").toLowerCase();
    if (/second|segundo/.test(u)) return Number(vars.duration) || 5;
    if (/megapixel/.test(u)) { const s = vars.size; return s && s.width ? (s.width * s.height) / 1e6 : 1; }
    return 1; // por imagem / por vídeo / por requisição
  }

  async function checkKey(key) {
    // Chamada barata e autenticada: preço de um modelo.
    await H.json(`${API}/models/pricing?endpoint_id=fal-ai/flux/schnell`, { headers: auth(key), retries: 1, timeout: 15000 });
    return true;
  }

  return { name: "fal.ai", upload, run, pricing, units, checkKey };
}

module.exports = Object.assign(create(), { create });
