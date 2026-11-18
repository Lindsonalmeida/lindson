// Cliente ComfyUI local (padrão http://127.0.0.1:8188).
// Ref: https://github.com/comfyanonymous/ComfyUI (script_examples/websockets_api_example.py e server.py)
//  POST /upload/image (multipart: image, overwrite) -> {name, subfolder, type}
//  POST /prompt {prompt: <workflow formato API>, client_id} -> {prompt_id, node_errors}
//  WS   /ws?clientId=<id>  mensagens progress {value,max} e executing {node:null} = terminou
//  GET  /history/<prompt_id> -> outputs[node].images|gifs|videos [{filename, subfolder, type}]
//  GET  /view?filename=&subfolder=&type= · POST /interrupt · POST /queue {delete:[id]}
// Workflows ficam em /comfy (formato API: no ComfyUI, "Exportar (API)"). Marcadores aceitos:
//  {{image}} {{prompt}} {{negative}} {{seed}} {{width}} {{height}} {{frames}} {{fps}}
"use strict";
const fs = require("fs");
const path = require("path");
const crypto = require("crypto");
const H = require("../lib/http");
const M = require("../models");

function create(opts = {}) {
  const POLL = opts.pollMs || 1500;
  const TIMEOUT = opts.timeoutMs || 60 * 60 * 1000; // local pode demorar
  const WS = opts.WebSocket !== undefined ? opts.WebSocket : (typeof WebSocket !== "undefined" ? WebSocket : null);

  const base = (job) => String(job.url || "http://127.0.0.1:8188").replace(/\/+$/, "");

  function loadWorkflow(model, job) {
    const custom = job.workflowPath;
    const file = custom && fs.existsSync(custom) ? custom : path.join(job.workflowDir || path.join(__dirname, "..", "..", "comfy"), model.workflow);
    let wf;
    try { wf = JSON.parse(fs.readFileSync(file, "utf8")); } catch (e) { throw new Error("Workflow do ComfyUI ilegível: " + file); }
    if (wf.nodes && wf.links) throw new Error("Este workflow está no formato da interface. No ComfyUI use \"Exportar (API)\" e aponte para esse arquivo.");
    delete wf._motionforge;
    return wf;
  }

  async function uploadImage(b, file, token) {
    const mp = H.multipart([
      { name: "image", filename: "mf_" + Date.now() + path.extname(file), contentType: "image/png", data: fs.readFileSync(file) },
      { name: "overwrite", value: "true" },
    ]);
    const r = await H.json(`${b}/upload/image`, { method: "POST", headers: { "Content-Type": mp.contentType }, body: mp.body, token });
    return r.subfolder ? `${r.subfolder}/${r.name}` : r.name;
  }

  async function run(job) {
    const { model, vars, token, onStatus = () => {} } = job;
    const b = base(job);
    const v = Object.assign({ negative: "blurry, low quality, distorted", seed: Math.floor(Math.random() * 2 ** 31) }, vars);
    if (v.seed === "" || v.seed == null) v.seed = Math.floor(Math.random() * 2 ** 31);
    v.seed = Number(v.seed);
    if (!v.negative) v.negative = "blurry, low quality, distorted";
    const fps = model.fps || 16;
    v.fps = fps;
    v.frames = Math.round((Number(v.duration) || 5) * fps) + 1;
    if (job.files && job.files.image) { onStatus("Enviando imagem ao ComfyUI…", -1); v.image = await uploadImage(b, job.files.image, token); }
    const wf = M.render(loadWorkflow(model, job), v);

    const clientId = crypto.randomBytes(8).toString("hex");
    let promptId = null;
    let ws = null, wsDone = false, wsErr = null;
    if (WS) {
      try {
        ws = new WS(b.replace(/^http/, "ws") + "/ws?clientId=" + clientId);
        ws.onmessage = (ev) => {
          let msg; try { msg = JSON.parse(typeof ev.data === "string" ? ev.data : ""); } catch (e) { return; }
          const d = msg.data || {};
          if (msg.type === "progress") onStatus(`Gerando… passo ${d.value}/${d.max}`, d.max ? d.value / d.max : -1, { phase: "run" });
          if (msg.type === "executing" && d.node === null && d.prompt_id === promptId) wsDone = true;
          if (msg.type === "execution_error" && d.prompt_id === promptId) wsErr = d.exception_message || "erro na execução";
        };
        ws.onerror = () => {};
      } catch (e) { ws = null; }
    }

    let res;
    try {
      res = await H.json(`${b}/prompt`, { method: "POST", body: { prompt: wf, client_id: clientId }, token, retries: 1 });
    } catch (e) {
      if (ws) try { ws.close(); } catch (x) { /* ignora */ }
      if (e.status === 400) throw new Error("O ComfyUI recusou o workflow: " + nodeErrors(e.body));
      throw e;
    }
    promptId = res.prompt_id;
    if (res.node_errors && Object.keys(res.node_errors).length) throw new Error("O ComfyUI recusou o workflow: " + nodeErrors(JSON.stringify(res)));

    const off = token ? token.onCancel(() => {
      H.raw(`${b}/queue`, { method: "POST", body: { delete: [promptId] }, headers: { "Content-Type": "application/json" }, timeout: 5000 }).catch(() => {});
      H.raw(`${b}/interrupt`, { method: "POST", body: { prompt_id: promptId }, headers: { "Content-Type": "application/json" }, timeout: 5000 }).catch(() => {});
    }) : () => {};

    try {
      onStatus("Na fila do ComfyUI…", -1, { phase: "queue" });
      const t0 = Date.now();
      for (;;) {
        if (Date.now() - t0 > TIMEOUT) throw new Error("O ComfyUI passou de 60 min sem terminar.");
        if (wsErr) throw new Error("ComfyUI: " + wsErr);
        await H.sleep(wsDone ? 50 : POLL, token);
        const hist = await H.json(`${b}/history/${promptId}`, { token, retries: 2 });
        const h = hist[promptId];
        if (!h) continue;
        const st = h.status || {};
        if (st.status_str === "error") {
          const m = (st.messages || []).find((x) => x[0] === "execution_error");
          throw new Error("ComfyUI: " + ((m && m[1] && m[1].exception_message) || "erro na execução"));
        }
        if (st.completed === false) continue;
        const files = [];
        Object.keys(h.outputs || {}).forEach((node) => {
          const o = h.outputs[node];
          ["videos", "gifs", "images"].forEach((k) => (o[k] || []).forEach((f) => { if (f.type !== "temp") files.push(Object.assign({ kind: k }, f)); }));
        });
        if (!files.length) throw new Error("O workflow terminou sem salvar arquivo (falta um nó Save Image/Save Video).");
        const vids = files.filter((f) => f.kind !== "images" || /\.(mp4|mov|webm)$/i.test(f.filename));
        const pick = vids.length ? [vids[0]] : files.filter((f) => /\.(png|jpe?g|webp|exr|tiff?)$/i.test(f.filename));
        const urls = pick.map((f) => `${b}/view?` + new URLSearchParams({ filename: f.filename, subfolder: f.subfolder || "", type: f.type || "output" }).toString());
        return { urls, requestId: promptId, sequence: !vids.length && urls.length > 1, fps, raw: h };
      }
    } finally {
      off();
      if (ws) try { ws.close(); } catch (x) { /* ignora */ }
    }
  }

  function nodeErrors(body) {
    try {
      const j = JSON.parse(body);
      const parts = [];
      if (j.error && j.error.message) parts.push(j.error.message + (j.error.details ? ": " + j.error.details : ""));
      Object.keys(j.node_errors || {}).forEach((n) => {
        const ne = j.node_errors[n];
        (ne.errors || []).forEach((er) => parts.push(`${ne.class_type || "nó " + n}: ${er.message}${er.details ? " (" + er.details + ")" : ""}`));
      });
      return parts.join(" · ").slice(0, 400) || "sem detalhe";
    } catch (e) { return String(body).slice(0, 300); }
  }

  async function check(url) {
    const r = await H.json(String(url).replace(/\/+$/, "") + "/system_stats", { retries: 1, timeout: 5000 });
    const dev = (r.devices || [])[0];
    return dev ? `${dev.name} · ${Math.round((dev.vram_total || 0) / 1073741824)} GB VRAM` : "conectado";
  }

  return { name: "ComfyUI", run, check, nodeErrors };
}

module.exports = Object.assign(create(), { create });
