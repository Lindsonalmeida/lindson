// Servidor HTTP local que imita fal.ai, Replicate e ComfyUI para os testes.
"use strict";
const http = require("http");

function start(routes) {
  const calls = [];
  const srv = http.createServer((req, res) => {
    const chunks = [];
    req.on("data", (c) => chunks.push(c));
    req.on("end", () => {
      const body = Buffer.concat(chunks);
      const call = { method: req.method, url: req.url, headers: req.headers, body, json: null };
      try { call.json = JSON.parse(body.toString("utf8")); } catch (e) { /* não JSON */ }
      calls.push(call);
      const path = req.url.split("?")[0];
      const key = Object.keys(routes).find((k) => {
        const [m, p] = k.split(" ");
        return m === req.method && (p === path || (p.endsWith("*") && path.startsWith(p.slice(0, -1))));
      });
      if (!key) { res.writeHead(404, { "Content-Type": "application/json" }); return res.end('{"detail":"rota não simulada: ' + req.method + " " + path + '"}'); }
      const out = routes[key](call, srv);
      const wrapped = out && (out.json !== undefined || out.raw !== undefined);
      const status = wrapped && out.status ? out.status : 200;
      const headers = Object.assign({ "Content-Type": wrapped && out.raw !== undefined ? (out.type || "application/octet-stream") : "application/json" }, (wrapped && out.headers) || {});
      res.writeHead(status, headers);
      if (wrapped && out.raw !== undefined) res.end(out.raw);
      else res.end(JSON.stringify(wrapped ? out.json : out));
    });
  });
  return new Promise((r) => srv.listen(0, "127.0.0.1", () => {
    srv.base = `http://127.0.0.1:${srv.address().port}`;
    srv.calls = calls;
    r(srv);
  }));
}

// PNG 1x1 válido
const PNG = Buffer.from("89504e470d0a1a0a0000000d4948445200000001000000010806000000" + "1f15c4890000000d49444154789c6360f8cfc0f01f0005000201" + "e221bc330000000049454e44ae426082", "hex");

module.exports = { start, PNG };
