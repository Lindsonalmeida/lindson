// node --test tests/   (Node 18+)
"use strict";
const test = require("node:test");
const assert = require("node:assert");
const fs = require("fs");
const os = require("os");
const path = require("path");

process.env.MOTIONFORGE_HOME = fs.mkdtempSync(path.join(os.tmpdir(), "mf-test-"));
const { start, PNG } = require("./mock-server");
const H = require("../js/lib/http");
const M = require("../js/models");
const E = require("../js/lib/errors");
const log = require("../js/lib/logger");

const tmpImg = path.join(process.env.MOTIONFORGE_HOME, "in.png");
fs.writeFileSync(tmpImg, PNG);

// ---------- modelos ----------
test("render: tipos, sufixos e campos vazios", () => {
  const out = M.render({ a: "{{duration}}", b: "{{duration:str}}", c: "{{duration}}s", d: "{{seed}}", e: "{{audio}}", f: { g: "{{prompt}}" }, h: 1, i: "x {{negative}}" },
    { duration: 5, seed: "", audio: false, prompt: "oi", negative: "" });
  assert.deepStrictEqual(out, { a: 5, b: "5", c: "5s", e: false, f: { g: "oi" }, h: 1 });
});

test("catálogo: todo modelo de nuvem tem id, tipo e template com a imagem/prompt", () => {
  for (const m of M.BUILTIN) {
    assert.ok(m.id && m.provider && m.kind, JSON.stringify(m));
    if (m.provider === "comfy") { assert.ok(fs.existsSync(path.join(__dirname, "..", "comfy", m.workflow))); continue; }
    const s = JSON.stringify(m.input);
    if (m.kind === "i2v") assert.ok(s.includes("{{image}}") && s.includes("{{prompt}}"), m.id);
    if (m.kind === "t2i") assert.ok(s.includes("{{prompt}}"), m.id);
    if (m.kind === "bg") assert.ok(s.includes("{{image}}"), m.id);
  }
  assert.strictEqual(M.nearestDuration({ durations: [6, 10] }, 5), 6);
  assert.strictEqual(M.nearestAspect(["16:9", "9:16", "1:1"], 1080, 1920), "9:16");
  assert.deepStrictEqual(M.imageSize(3840, 2160), { width: 1536, height: 864 });
  const custom = M.all([{ provider: "fal", kind: "i2v", id: "x/y", label: "Y", input: { image_url: "{{image}}", prompt: "{{prompt}}" } }]);
  assert.ok(custom.find((m) => m.id === "x/y" && m.custom));
});

test("extractUrls cobre fal, Replicate e listas", () => {
  assert.deepStrictEqual(M.extractUrls({ video: { url: "https://a/v.mp4" } }), ["https://a/v.mp4"]);
  assert.deepStrictEqual(M.extractUrls({ images: [{ url: "https://a/i.png" }] }), ["https://a/i.png"]);
  assert.deepStrictEqual(M.extractUrls(["https://a/1.png", "https://a/2.png"]), ["https://a/1.png", "https://a/2.png"]);
  assert.deepStrictEqual(M.extractUrls("https://a/o.mp4"), ["https://a/o.mp4"]);
});

// ---------- http ----------
test("http: retry com backoff em 503 e sucesso na 3ª tentativa", async () => {
  let n = 0;
  const srv = await start({ "GET /x": () => (++n < 3 ? { status: 503, json: { detail: "ocupado" } } : { ok: 1 }) });
  const r = await H.json(srv.base + "/x", { backoffMs: 10 });
  assert.deepStrictEqual(r, { ok: 1 });
  assert.strictEqual(n, 3);
  srv.close();
});

test("http: 401 não repete e vira mensagem clara", async () => {
  let n = 0;
  const srv = await start({ "GET /x": () => { n++; return { status: 401, json: { detail: "Invalid key" } }; } });
  await assert.rejects(H.json(srv.base + "/x", { backoffMs: 10 }), (e) => e.status === 401 && /Chave de API inválida/.test(E.friendly(e, "fal.ai")));
  assert.strictEqual(n, 1);
  assert.match(E.friendly(new H.HttpError(402, '{"detail":"User is locked. Reason: Exhausted balance"}')), /Sem saldo/);
  assert.match(E.friendly(new H.HttpError(422, '{"detail":[{"loc":["body","duration"],"msg":"must be 5 or 10"}]}')), /duration: must be 5 or 10/);
  srv.close();
});

test("http: download com redirecionamento e progresso", async () => {
  const srv = await start({ "GET /r": () => ({ status: 302, headers: { Location: "/f.png" }, raw: "" }), "GET /f.png": () => ({ raw: PNG, type: "image/png" }) });
  const dest = path.join(process.env.MOTIONFORGE_HOME, "dl.png");
  let last = 0;
  await H.download(srv.base + "/r", dest, { onProgress: (p) => (last = p) });
  assert.ok(fs.readFileSync(dest).equals(PNG));
  assert.strictEqual(last, 1);
  srv.close();
});

test("logger não grava chaves", () => {
  assert.strictEqual(log.scrub('Authorization: Key abcd1234:efgh5678 "falKey": "segredo123"'), 'Authorization: Key *** "falKey": "***"');
});

// ---------- fal.ai ----------
function falRoutes(state) {
  return {
    "POST /storage/upload/initiate": (c) => { state.init = c; return { upload_url: state.base + "/put/abc", file_url: "https://v3.fal.media/files/abc.png" }; },
    "PUT /put/abc": (c) => { state.put = c; return { status: 200, json: {} }; },
    "POST /fal-ai/kling-video/v3/standard/image-to-video": (c) => {
      state.submit = c;
      return { request_id: "r1", status_url: state.base + "/fal-ai/kling-video/requests/r1/status", response_url: state.base + "/fal-ai/kling-video/requests/r1", cancel_url: state.base + "/fal-ai/kling-video/requests/r1/cancel" };
    },
    "GET /fal-ai/kling-video/requests/r1/status": () => { state.polls = (state.polls || 0) + 1; return state.polls < 2 ? { status: "IN_QUEUE", queue_position: 0 } : state.polls < 3 ? { status: "IN_PROGRESS" } : { status: "COMPLETED" }; },
    "GET /fal-ai/kling-video/requests/r1": () => ({ video: { url: state.base + "/out.mp4" } }),
    "PUT /fal-ai/kling-video/requests/r1/cancel": () => { state.cancelled = true; return { status: 202, json: { status: "CANCELLATION_REQUESTED" } }; },
    "GET /models/pricing": (c) => ({ prices: [{ endpoint_id: decodeURIComponent(c.url.split("endpoint_id=")[1]), unit_price: 0.084, unit: "seconds", currency: "USD" }] }),
  };
}

test("fal: upload + fila + status + resultado, com a chave no cabeçalho", async () => {
  const st = {};
  const srv = await start(falRoutes(st)); st.base = srv.base;
  const fal = require("../js/providers/fal").create({ queue: srv.base, rest: srv.base, api: srv.base, pollMs: 5 });
  const model = M.find("fal", "fal-ai/kling-video/v3/standard/image-to-video");
  const seen = [];
  const r = await fal.run({ key: "k-teste", model, vars: { prompt: "zoom", duration: 5, audio: false, negative: "" }, files: { image: tmpImg }, onStatus: (t) => seen.push(t) });
  assert.deepStrictEqual(r.urls, [srv.base + "/out.mp4"]);
  assert.strictEqual(st.init.headers.authorization, "Key k-teste");
  assert.strictEqual(st.init.json.content_type, "image/png");
  assert.ok(st.put.body.equals(PNG));
  assert.deepStrictEqual(st.submit.json, { start_image_url: "https://v3.fal.media/files/abc.png", prompt: "zoom", duration: "5", generate_audio: false });
  assert.ok(seen.some((s) => /fila/.test(s)) && seen.some((s) => /Gerando/.test(s)));
  const price = await fal.pricing("k-teste", [model.id]);
  assert.strictEqual(price[model.id].price, 0.084);
  assert.strictEqual(fal.units("seconds", model, { duration: 10 }), 10);
  srv.close();
});

test("fal: cancelar chama cancel_url e encerra com CancelledError", async () => {
  const st = {};
  const routes = falRoutes(st);
  routes["GET /fal-ai/kling-video/requests/r1/status"] = () => ({ status: "IN_PROGRESS" });
  const srv = await start(routes); st.base = srv.base;
  const fal = require("../js/providers/fal").create({ queue: srv.base, rest: srv.base, api: srv.base, pollMs: 20 });
  const token = new H.CancelToken();
  setTimeout(() => token.cancel(), 80);
  await assert.rejects(fal.run({ key: "k", model: M.find("fal", "fal-ai/kling-video/v3/standard/image-to-video"), vars: { prompt: "p", duration: 5 }, files: { image: tmpImg }, token }), (e) => e instanceof H.CancelledError);
  await H.sleep(60);
  assert.ok(st.cancelled);
  srv.close();
});

test("fal: COMPLETED com erro vira mensagem", async () => {
  const st = {};
  const routes = falRoutes(st);
  routes["GET /fal-ai/kling-video/requests/r1/status"] = () => ({ status: "COMPLETED", error: "NSFW detectado" });
  const srv = await start(routes); st.base = srv.base;
  const fal = require("../js/providers/fal").create({ queue: srv.base, rest: srv.base, api: srv.base, pollMs: 5 });
  await assert.rejects(fal.run({ key: "k", model: M.find("fal", "fal-ai/kling-video/v3/standard/image-to-video"), vars: { prompt: "p", duration: 5 }, files: { image: tmpImg } }), /NSFW/);
  srv.close();
});

// ---------- Replicate ----------
test("replicate: modelo oficial, polling, progresso pelos logs e cancelamento", async () => {
  const st = { n: 0 };
  const srv = await start({
    "POST /models/black-forest-labs/flux-schnell/predictions": (c) => { st.create = c; return { status: 201, json: { id: "p1", status: "starting", urls: { get: srv.base + "/predictions/p1", cancel: srv.base + "/predictions/p1/cancel" } } }; },
    "GET /predictions/p1": () => (++st.n < 2 ? { id: "p1", status: "processing", logs: "50%|#####     | 2/4" } : { id: "p1", status: "succeeded", output: [srv.base + "/o.png"] }),
  });
  const rep = require("../js/providers/replicate").create({ api: srv.base, pollMs: 5 });
  const prog = [];
  const r = await rep.run({ key: "r8_x", model: M.find("replicate", "black-forest-labs/flux-schnell"), vars: { prompt: "gato", aspect: "16:9", seed: "" }, onStatus: (t, p) => prog.push(p) });
  assert.deepStrictEqual(r.urls, [srv.base + "/o.png"]);
  assert.strictEqual(st.create.headers.authorization, "Bearer r8_x");
  assert.deepStrictEqual(st.create.json.input, { prompt: "gato", aspect_ratio: "16:9", output_format: "png", num_outputs: 1 });
  assert.ok(prog.includes(0.5));
  srv.close();
});

// ---------- ComfyUI ----------
test("comfy: upload, prompt com marcadores, histórico e /view", async () => {
  const st = { polls: 0 };
  const srv = await start({
    "POST /upload/image": (c) => { st.upload = c; return { name: "mf_1.png", subfolder: "", type: "input" }; },
    "POST /prompt": (c) => { st.prompt = c.json; return { prompt_id: "abc", number: 1, node_errors: {} }; },
    "GET /history/abc": () => (++st.polls < 2 ? {} : { abc: { status: { status_str: "success", completed: true }, outputs: { 60: { images: [{ filename: "wan_00001_.png", subfolder: "MotionForge", type: "output" }, { filename: "wan_00002_.png", subfolder: "MotionForge", type: "output" }] } } } }),
  });
  const comfy = require("../js/providers/comfy").create({ pollMs: 5, WebSocket: null });
  const model = M.find("comfy", "comfy/wan21-i2v");
  const r = await comfy.run({ url: srv.base, model, vars: { prompt: "acena", duration: 5, width: 832, height: 480, seed: 7 }, files: { image: tmpImg } });
  const wf = st.prompt.prompt;
  assert.strictEqual(wf["52"].inputs.image, "mf_1.png");
  assert.strictEqual(wf["6"].inputs.text, "acena");
  assert.strictEqual(wf["50"].inputs.length, 81);
  assert.strictEqual(wf["50"].inputs.width, 832);
  assert.strictEqual(wf["3"].inputs.seed, 7);
  assert.ok(!wf._motionforge);
  assert.strictEqual(r.sequence, true);
  assert.strictEqual(r.urls.length, 2);
  assert.match(r.urls[0], /\/view\?filename=wan_00001_.png&subfolder=MotionForge&type=output/);
  srv.close();
});

test("comfy: erro de nó vira mensagem legível", async () => {
  const srv = await start({ "POST /prompt": () => ({ status: 400, json: { error: { message: "Prompt outputs failed validation" }, node_errors: { 37: { class_type: "UNETLoader", errors: [{ message: "Value not in list", details: "unet_name: 'x.safetensors' not in []" }] } } } }) });
  const comfy = require("../js/providers/comfy").create({ pollMs: 5, WebSocket: null });
  await assert.rejects(comfy.run({ url: srv.base, model: M.find("comfy", "comfy/sdxl-t2i"), vars: { prompt: "p", width: 1024, height: 1024 } }), /UNETLoader: Value not in list/);
  srv.close();
});
