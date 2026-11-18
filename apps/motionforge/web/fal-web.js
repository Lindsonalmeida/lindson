// Cliente fal.ai para o navegador (fetch). Mesmo fluxo de js/providers/fal.js do plugin.
// CORS conferido em 18/11/2026: queue.fal.run (POST/GET/PUT), rest.fal.ai, api.fal.ai e *.fal.media aceitam o navegador.
// Refs: https://fal.ai/docs/documentation/model-apis/inference/queue.md
export class Cancelled extends Error { constructor() { super("Cancelado."); this.name = "Cancelled"; } }
export class FalError extends Error { constructor(status, body) { super("fal " + status); this.status = status; this.body = body; } }

export function createFal(opts = {}) {
  const QUEUE = opts.queue || "https://queue.fal.run";
  const REST = opts.rest || "https://rest.fal.ai";
  const API = opts.api || "https://api.fal.ai/v1";
  const POLL = opts.pollMs || 2500;
  const TIMEOUT = opts.timeoutMs || 15 * 60 * 1000;
  const f = opts.fetch || ((...a) => fetch(...a));
  const sleep = (ms, signal) => new Promise((res, rej) => {
    const t = setTimeout(res, ms);
    if (signal) signal.addEventListener("abort", () => { clearTimeout(t); rej(new Cancelled()); }, { once: true });
  });

  async function req(url, { key, method = "GET", body, headers = {}, signal, retries = 3 } = {}) {
    let last;
    for (let i = 0; i < retries; i++) {
      if (signal && signal.aborted) throw new Cancelled();
      try {
        const h = Object.assign({}, headers);
        if (key) h.Authorization = "Key " + key;
        let b = body;
        if (b && !(b instanceof Blob) && typeof b !== "string") { b = JSON.stringify(b); h["Content-Type"] = "application/json"; }
        const r = await f(url, { method, headers: h, body: b, signal });
        const txt = await r.text();
        if (!r.ok) {
          const e = new FalError(r.status, txt);
          if ((r.status === 429 || r.status >= 500) && i < retries - 1) { last = e; await sleep(1000 * 2 ** i, signal); continue; }
          throw e;
        }
        try { return txt ? JSON.parse(txt) : {}; } catch (e) { return { raw: txt }; }
      } catch (e) {
        if (e.name === "AbortError" || e instanceof Cancelled) throw new Cancelled();
        if (e instanceof FalError) throw e;
        last = e;
        if (i === retries - 1) throw e;
        await sleep(1000 * 2 ** i, signal);
      }
    }
    throw last;
  }

  async function upload(key, blob, name, signal) {
    const type = blob.type || "application/octet-stream";
    const init = await req(`${REST}/storage/upload/initiate?storage_type=fal-cdn-v3`, { key, method: "POST", body: { content_type: type, file_name: name || "arquivo" }, signal });
    const r = await f(init.upload_url, { method: "PUT", headers: { "Content-Type": type }, body: blob, signal });
    if (!r.ok) throw new FalError(r.status, await r.text());
    return init.file_url;
  }

  async function run(key, modelId, input, { signal, onStatus = () => {} } = {}) {
    if (!key) throw new Error("Cole a chave do fal.ai em Config.");
    onStatus("Na fila…");
    const sub = await req(`${QUEUE}/${modelId}`, { key, method: "POST", body: input, signal });
    const cancelUrl = sub.cancel_url || String(sub.status_url).replace(/\/status$/, "/cancel");
    const cancel = () => f(cancelUrl, { method: "PUT", headers: { Authorization: "Key " + key } }).catch(() => {});
    if (signal) signal.addEventListener("abort", cancel, { once: true });
    const t0 = Date.now();
    for (;;) {
      if (Date.now() - t0 > TIMEOUT) { cancel(); throw new Error(`Passou de ${Math.round(TIMEOUT / 60000)} min sem terminar; o pedido foi cancelado. Tente um modelo mais rápido.`); }
      await sleep(POLL, signal);
      const st = await req(sub.status_url, { key, signal });
      if (st.status === "IN_QUEUE") onStatus(st.queue_position != null ? `Na fila (posição ${st.queue_position + 1})…` : "Na fila…");
      else if (st.status === "IN_PROGRESS") onStatus("Gerando…");
      if (st.status === "COMPLETED") {
        if (st.error) throw new Error("O modelo falhou: " + st.error);
        break;
      }
    }
    onStatus("Buscando resultado…");
    return req(sub.response_url, { key, signal });
  }

  async function pricing(key, ids) {
    const q = ids.map((i) => "endpoint_id=" + encodeURIComponent(i)).join("&");
    const r = await req(`${API}/models/pricing?${q}`, { key, retries: 1 });
    const out = {};
    (r.prices || []).forEach((p) => { out[p.endpoint_id] = { unit: p.unit, price: p.unit_price, currency: p.currency || "USD" }; });
    return out;
  }

  return { upload, run, pricing, req };
}

export function friendly(e) {
  if (!e) return "Erro desconhecido.";
  if (e instanceof Cancelled || e.name === "Cancelled") return "Cancelado.";
  if (e instanceof FalError) {
    let d = "";
    try { const j = JSON.parse(e.body); d = j.detail || j.error || j.message || ""; if (Array.isArray(d)) d = d.map((x) => (x.loc ? x.loc.slice(-1)[0] + ": " : "") + x.msg).join("; "); if (typeof d === "object") d = d.message || JSON.stringify(d); } catch (x) { d = String(e.body || "").slice(0, 200); }
    const low = String(d).toLowerCase();
    if (e.status === 401) return "Chave do fal.ai inválida. Confira em Config.";
    if (e.status === 402 || /balance|credit|exhausted|insufficient|billing/.test(low)) return "Sem saldo no fal.ai. Recarregue em fal.ai/dashboard/billing.";
    if (e.status === 403) return "Acesso negado pelo fal.ai: " + (d || "a chave não pode usar este modelo") + ".";
    if (e.status === 404) return "Modelo não encontrado no fal.ai. Escolha outro.";
    if (e.status === 422 || e.status === 400) return "O modelo recusou os parâmetros: " + (d || "confira prompt, duração e imagem") + ".";
    if (e.status === 429) return "Muitas requisições. Espere um pouco e tente de novo.";
    if (e.status >= 500) return `O fal.ai está instável (${e.status}). Tente de novo.`;
    return `Erro ${e.status}: ${d}`;
  }
  if (e.name === "TypeError" && /fetch/i.test(e.message)) return "Sem conexão com a internet (ou bloqueio de rede).";
  return e.message || String(e);
}
