// Cliente mínimo do fal.ai via HTTP (sem SDK), para rodar no Node do CEP.
// Refs:
//  Queue API:   https://docs.fal.ai/model-endpoints/queue
//  Upload/CDN:  https://docs.fal.ai/model-endpoints/server-side#file-uploads
//  Modelos:     https://fal.ai/models  (confira IDs e parâmetros atuais de cada modelo)
const fs = require("fs");
const path = require("path");

const QUEUE = "https://queue.fal.run";
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

function headers(key, extra) {
  return Object.assign({ Authorization: "Key " + key }, extra || {});
}

// Envia o arquivo inline como data URI (simples e aceito pelos endpoints do fal).
// Para arquivos grandes, prefira o upload para o storage do fal (ver ref acima).
function toDataUri(file) {
  const ext = path.extname(file).slice(1).toLowerCase();
  const mime = ext === "jpg" || ext === "jpeg" ? "image/jpeg" : "image/png";
  return "data:" + mime + ";base64," + fs.readFileSync(file).toString("base64");
}

async function run(key, modelId, input, onStatus) {
  const sub = await fetch(`${QUEUE}/${modelId}`, {
    method: "POST",
    headers: headers(key, { "Content-Type": "application/json" }),
    body: JSON.stringify(input),
  });
  if (!sub.ok) throw new Error(`fal ${sub.status}: ${await sub.text()}`);
  const { status_url, response_url } = await sub.json();

  const t0 = Date.now();
  while (true) {
    if (Date.now() - t0 > 10 * 60 * 1000) throw new Error("Timeout (10 min)");
    await sleep(3000);
    const st = await (await fetch(status_url, { headers: headers(key) })).json();
    onStatus && onStatus(st.status + (st.queue_position != null ? ` (fila ${st.queue_position})` : ""));
    if (st.status === "COMPLETED") break;
    if (st.status === "FAILED" || st.error) throw new Error("Falhou: " + JSON.stringify(st));
  }
  const res = await fetch(response_url, { headers: headers(key) });
  if (!res.ok) throw new Error(`fal ${res.status}: ${await res.text()}`);
  return res.json();
}

async function download(url, outFile) {
  const r = await fetch(url);
  if (!r.ok) throw new Error("Download " + r.status);
  fs.writeFileSync(outFile, Buffer.from(await r.arrayBuffer()));
  return outFile;
}

module.exports = { run, download, toDataUri };
