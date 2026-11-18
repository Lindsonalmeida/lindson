// Cliente Replicate via HTTP.
// Ref: https://replicate.com/docs/reference/http (conferida em 18/11/2026)
//  POST /v1/models/{dono}/{modelo}/predictions {input}   (modelos oficiais, sem "version")
//  POST /v1/predictions {version, input}                 (modelo com versão fixa: id "dono/modelo:versao")
//  GET  /v1/predictions/{id} · POST /v1/predictions/{id}/cancel
//  status: starting | processing | succeeded | failed | canceled
//  Arquivos de entrada: data URL (a doc recomenda URL HTTP acima de 256 KB; o painel reduz a imagem antes).
"use strict";
const fs = require("fs");
const path = require("path");
const H = require("../lib/http");
const M = require("../models");

function create(opts = {}) {
  const API = opts.api || "https://api.replicate.com/v1";
  const POLL = opts.pollMs || 2500;
  const TIMEOUT = opts.timeoutMs || 15 * 60 * 1000;
  const auth = (key) => ({ Authorization: "Bearer " + key });

  function dataUrl(file) {
    const ext = path.extname(file).slice(1).toLowerCase();
    const mime = { jpg: "image/jpeg", jpeg: "image/jpeg", png: "image/png", webp: "image/webp", mp4: "video/mp4", mov: "video/quicktime" }[ext] || "application/octet-stream";
    return `data:${mime};base64,` + fs.readFileSync(file).toString("base64");
  }

  async function run(job) {
    const { key, model, vars, token, onStatus = () => {} } = job;
    if (!key) throw new Error("Cole o token do Replicate na aba Config.");
    const v = Object.assign({}, vars);
    if (job.files && job.files.image) v.image = dataUrl(job.files.image);
    if (job.files && job.files.video) v.video = dataUrl(job.files.video);
    const input = M.render(model.input, v);

    onStatus("Enviando…", -1);
    const [ref, version] = model.id.split(":");
    const url = version ? `${API}/predictions` : `${API}/models/${ref}/predictions`;
    const body = version ? { version, input } : { input };
    let p = await H.json(url, { method: "POST", headers: auth(key), body, token, timeout: 120000 });
    const getUrl = (p.urls && p.urls.get) || `${API}/predictions/${p.id}`;
    const cancelUrl = (p.urls && p.urls.cancel) || `${API}/predictions/${p.id}/cancel`;
    const off = token ? token.onCancel(() => { H.raw(cancelUrl, { method: "POST", headers: auth(key), timeout: 10000 }).catch(() => {}); }) : () => {};
    try {
      const t0 = Date.now();
      while (!["succeeded", "failed", "canceled"].includes(p.status)) {
        if (Date.now() - t0 > TIMEOUT) {
          H.raw(cancelUrl, { method: "POST", headers: auth(key), timeout: 10000 }).catch(() => {});
          throw new Error(`O provedor passou de ${Math.round(TIMEOUT / 60000)} min sem terminar. O pedido foi cancelado.`);
        }
        await H.sleep(POLL, token);
        p = await H.json(getUrl, { headers: auth(key), token });
        const pct = progressFromLogs(p.logs);
        onStatus(p.status === "starting" ? "Iniciando a máquina…" : "Gerando…", pct, { phase: p.status === "starting" ? "queue" : "run" });
      }
      if (p.status === "failed") throw new Error("O modelo falhou: " + (p.error || "sem detalhe"));
      if (p.status === "canceled") throw new H.CancelledError();
      const urls = M.extractUrls(p.output);
      if (!urls.length) throw new Error("O modelo respondeu sem arquivo.");
      return { urls, requestId: p.id, raw: p, authHeaders: auth(key) };
    } finally { off(); }
  }

  // Muitos modelos escrevem barras do tqdm nos logs ("45%|####"). Usa o último percentual.
  function progressFromLogs(logs) {
    if (!logs) return -1;
    const m = String(logs).match(/(\d{1,3})%\|[^\n]*$/);
    return m ? Math.min(1, Number(m[1]) / 100) : -1;
  }

  async function checkKey(key) {
    await H.json(`${API}/account`, { headers: auth(key), retries: 1, timeout: 15000 });
    return true;
  }

  return { name: "Replicate", run, checkKey, progressFromLogs };
}

module.exports = Object.assign(create(), { create });
