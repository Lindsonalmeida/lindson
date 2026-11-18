// HTTP com o Node do CEP (sem fetch do navegador: evita CORS e funciona igual nos testes).
// - retry com backoff (3 tentativas) em erro de rede, 429 e 5xx
// - cancelamento por CancelToken
// - download em disco com progresso e redirecionamento
"use strict";
const http = require("http");
const https = require("https");
const fs = require("fs");
const { URL } = require("url");

class HttpError extends Error {
  constructor(status, body, url) {
    super(`HTTP ${status}`);
    this.name = "HttpError";
    this.status = status;
    this.body = body;
    this.url = url;
  }
}

class CancelledError extends Error {
  constructor() { super("Cancelado pelo usuário."); this.name = "CancelledError"; }
}

class CancelToken {
  constructor() { this.cancelled = false; this._fns = []; }
  cancel() {
    if (this.cancelled) return;
    this.cancelled = true;
    this._fns.splice(0).forEach((f) => { try { f(); } catch (e) { /* ignora */ } });
  }
  onCancel(fn) {
    if (this.cancelled) { fn(); return () => {}; }
    this._fns.push(fn);
    return () => { this._fns = this._fns.filter((x) => x !== fn); };
  }
  throwIfCancelled() { if (this.cancelled) throw new CancelledError(); }
}

const sleep = (ms, token) => new Promise((res, rej) => {
  const t = setTimeout(() => { off(); res(); }, ms);
  const off = token ? token.onCancel(() => { clearTimeout(t); rej(new CancelledError()); }) : () => {};
});

// Requisição crua. Resolve com { status, headers, body: Buffer } (sem lançar por status).
function raw(url, opts = {}) {
  const { method = "GET", headers = {}, body, token, timeout = 60000, redirects = 5, onData } = opts;
  return new Promise((resolve, reject) => {
    if (token && token.cancelled) return reject(new CancelledError());
    const u = new URL(url);
    const lib = u.protocol === "http:" ? http : https;
    const h = Object.assign({ "User-Agent": "MotionForge/1.0" }, headers);
    let payload = body;
    if (payload != null && !Buffer.isBuffer(payload) && typeof payload !== "string") payload = JSON.stringify(payload);
    if (payload != null) h["Content-Length"] = Buffer.byteLength(payload);
    const req = lib.request(u, { method, headers: h }, (res) => {
      const loc = res.headers.location;
      if (loc && res.statusCode >= 300 && res.statusCode < 400 && redirects > 0) {
        res.resume();
        const next = new URL(loc, u).toString();
        // Redirecionamento para outro host (CDN) não leva a chave.
        const nh = Object.assign({}, headers);
        if (new URL(next).host !== u.host) delete nh.Authorization;
        return resolve(raw(next, Object.assign({}, opts, { headers: nh, redirects: redirects - 1, method: res.statusCode === 303 ? "GET" : method, body: res.statusCode === 303 ? undefined : body })));
      }
      const chunks = [];
      res.on("data", (c) => { if (onData) onData(c, res); else chunks.push(c); });
      res.on("end", () => resolve({ status: res.statusCode, headers: res.headers, body: Buffer.concat(chunks) }));
      res.on("error", reject);
    });
    const off = token ? token.onCancel(() => { req.destroy(new CancelledError()); }) : () => {};
    req.setTimeout(timeout, () => req.destroy(Object.assign(new Error("Tempo de conexão esgotado"), { code: "ETIMEDOUT" })));
    req.on("error", (e) => { off(); reject(token && token.cancelled ? new CancelledError() : e); });
    req.on("close", off);
    if (payload != null) req.write(payload);
    req.end();
  });
}

const RETRY_NET = new Set(["ECONNRESET", "ETIMEDOUT", "ECONNREFUSED", "EAI_AGAIN", "ENOTFOUND", "EPIPE", "ENETUNREACH", "ECONNABORTED"]);

// Requisição com retry. Lança HttpError se status >= 400.
async function request(url, opts = {}) {
  const tries = opts.retries == null ? 3 : opts.retries;
  const base = opts.backoffMs == null ? 1000 : opts.backoffMs;
  let lastErr;
  for (let i = 0; i < tries; i++) {
    try {
      const r = await raw(url, opts);
      if (r.status >= 400) {
        const err = new HttpError(r.status, r.body.toString("utf8"), url);
        if ((r.status === 429 || r.status >= 500) && i < tries - 1) { lastErr = err; await sleep(base * Math.pow(2, i), opts.token); continue; }
        throw err;
      }
      return r;
    } catch (e) {
      if (e instanceof HttpError || e instanceof CancelledError) throw e;
      lastErr = e;
      if (!RETRY_NET.has(e.code) || i === tries - 1) throw e;
      if (opts.onRetry) opts.onRetry(i + 1, e);
      await sleep(base * Math.pow(2, i), opts.token);
    }
  }
  throw lastErr;
}

async function json(url, opts = {}) {
  const headers = Object.assign({ Accept: "application/json" }, opts.headers || {});
  if (opts.body != null && !Buffer.isBuffer(opts.body) && typeof opts.body !== "string") headers["Content-Type"] = "application/json";
  const r = await request(url, Object.assign({}, opts, { headers }));
  const txt = r.body.toString("utf8");
  if (!txt) return {};
  try { return JSON.parse(txt); } catch (e) { throw new Error("Resposta inválida do servidor: " + txt.slice(0, 200)); }
}

// Baixa url -> arquivo, com progresso (0..1 quando o tamanho é conhecido).
async function download(url, dest, opts = {}) {
  const tmp = dest + ".part";
  let attempt = 0;
  for (;;) {
    let out;
    try {
      out = fs.createWriteStream(tmp);
      let got = 0, total = 0, status = 0;
      const r = await raw(url, Object.assign({}, opts, {
        timeout: opts.timeout || 120000,
        onData: (c, res) => {
          status = res.statusCode;
          if (status >= 400) return;
          total = Number(res.headers["content-length"]) || 0;
          got += c.length; out.write(c);
          if (opts.onProgress) opts.onProgress(total ? got / total : -1, got, total);
        },
      }));
      await new Promise((res) => out.end(res));
      if ((r.status || status) >= 400) throw new HttpError(r.status, "", url);
      if (got === 0) throw new Error("Download vazio");
      fs.renameSync(tmp, dest);
      if (opts.onProgress) opts.onProgress(1, got, total || got);
      return dest;
    } catch (e) {
      if (out) { try { out.destroy(); } catch (x) { /* ignora */ } }
      try { fs.unlinkSync(tmp); } catch (x) { /* ignora */ }
      attempt++;
      const retriable = RETRY_NET.has(e.code) || (e instanceof HttpError && (e.status === 429 || e.status >= 500));
      if (e instanceof CancelledError || !retriable || attempt >= 3) throw e;
      await sleep(1000 * Math.pow(2, attempt - 1), opts.token);
    }
  }
}

// multipart/form-data simples: fields = [{name, value} | {name, filename, contentType, data:Buffer}]
function multipart(fields) {
  const boundary = "----MotionForge" + Math.random().toString(16).slice(2);
  const parts = [];
  for (const f of fields) {
    let head = `--${boundary}\r\nContent-Disposition: form-data; name="${f.name}"`;
    if (f.filename) head += `; filename="${f.filename}"\r\nContent-Type: ${f.contentType || "application/octet-stream"}`;
    head += "\r\n\r\n";
    parts.push(Buffer.from(head), Buffer.isBuffer(f.data) ? f.data : Buffer.from(String(f.value != null ? f.value : f.data)), Buffer.from("\r\n"));
  }
  parts.push(Buffer.from(`--${boundary}--\r\n`));
  return { body: Buffer.concat(parts), contentType: "multipart/form-data; boundary=" + boundary };
}

module.exports = { raw, request, json, download, multipart, sleep, HttpError, CancelledError, CancelToken };
