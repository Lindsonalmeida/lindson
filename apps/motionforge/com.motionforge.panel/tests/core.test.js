// Fluxo completo: núcleo + host.jsx num AE simulado + rembg real + fal.ai simulado.
"use strict";
const test = require("node:test");
const assert = require("node:assert");
const fs = require("fs");
const os = require("os");
const path = require("path");
const { execFileSync } = require("child_process");

process.env.MOTIONFORGE_HOME = fs.mkdtempSync(path.join(os.tmpdir(), "mf-core-"));
const { start, PNG } = require("./mock-server");
const { createAE } = require("./fake-ae");
const { createCore } = require("../js/core");
const S = require("../js/settings");
const H = require("../js/lib/http");

const HOME = process.env.MOTIONFORGE_HOME;
const img = path.join(HOME, "foto.png");
execFileSync("python3", ["-c", `
from PIL import Image, ImageDraw
im=Image.new('RGB',(320,240),(30,120,220)); d=ImageDraw.Draw(im); d.ellipse([100,50,220,190],fill=(240,200,40)); im.save(r'${img}')`]);

let hasRembg = true;
try { execFileSync("python3", ["-c", "import rembg"], { stdio: "ignore" }); } catch (e) { hasRembg = false; }
let hasFfmpeg = true;
try { execFileSync("ffmpeg", ["-version"], { stdio: "ignore" }); } catch (e) { hasFfmpeg = false; }

S.save(Object.assign(S.load(), { python: "python3", rembgModel: "u2netp", falKey: "k-teste", provider: "fal" }));

async function falMock() {
  const st = { submits: [] };
  const srv = await start({
    "POST /storage/upload/initiate": () => ({ upload_url: srv.base + "/put", file_url: "https://cdn/x.png" }),
    "PUT /put": () => ({ json: {} }),
    "POST /fal-ai/*": (c) => { st.submits.push(c); return { request_id: "r", status_url: srv.base + "/q/r/status", response_url: srv.base + "/q/r", cancel_url: srv.base + "/q/r/cancel" }; },
    "GET /q/r/status": () => (st.hang ? { status: "IN_PROGRESS" } : { status: "COMPLETED" }),
    "GET /q/r": () => (st.submits[st.submits.length - 1].url.includes("flux") ? { images: [{ url: srv.base + "/img.png" }], seed: 42 } : { video: { url: srv.base + "/v.mp4" } }),
    "PUT /q/r/cancel": () => { st.cancelled = true; return { status: 202, json: {} }; },
    "GET /img.png": () => ({ raw: PNG, type: "image/png" }),
    "GET /v.mp4": () => ({ raw: Buffer.from("fake mp4 bytes"), type: "video/mp4" }),
    "GET /models/pricing": () => ({ prices: [{ endpoint_id: "fal-ai/kling-video/v3/standard/image-to-video", unit_price: 0.084, unit: "seconds", currency: "USD" }] }),
  });
  srv.st = st;
  return srv;
}

function mkCore(ae, srv) {
  const fal = require("../js/providers/fal").create({ queue: srv ? srv.base : undefined, rest: srv ? srv.base : undefined, api: srv ? srv.base : undefined, pollMs: 5 });
  return createCore({ evalScript: ae.evalScript, providers: { fal }, makeThumbs: false });
}

test("sem comp: mensagem clara, sem travar", async () => {
  const ae = createAE({ framePng: img });
  const core = mkCore(ae);
  const info = await core.layerInfo();
  assert.match(info.error, /Abra uma composição/);
  await assert.rejects(core.removeBg({}), /Abra uma composição/);
});

test("remover fundo (rembg real) numa camada de imagem: duplica, troca a fonte, oculta a original", { skip: !hasRembg }, async () => {
  const ae = createAE({ framePng: img });
  const comp = ae.newComp();
  const l = ae.addFootage(comp, img, { isStill: true, layer: { name: "Foto", inPoint: 1, outPoint: 4 } });
  ae.select(comp, l);
  const core = mkCore(ae);
  const seen = [];
  const r = await core.removeBg({ engine: "local" }, (t) => seen.push(t));
  assert.ok(fs.existsSync(r.file));
  assert.strictEqual(comp.numLayers, 2);
  const dup = comp.layer(1);
  assert.strictEqual(dup.name, "Foto · sem fundo");
  assert.strictEqual(path.basename(dup.source.mainSource.file.fsName), path.basename(r.file));
  assert.strictEqual(dup.inPoint, 1);
  assert.strictEqual(comp.layer(2).enabled, false, "original oculta");
  assert.strictEqual(ae.log.undoOpen, 0);
  assert.strictEqual(ae.log.undoGroups, 1, "um grupo de desfazer");
  const out = execFileSync("python3", ["-c", `from PIL import Image; im=Image.open(r'${r.file}'); print(im.mode, im.getpixel((5,5))[3], im.getpixel((160,120))[3])`]).toString().trim();
  assert.match(out, /^RGBA 0 2\d\d$/);
  assert.ok(core.historyList && (await core.historyList()).some((h) => h.type === "bg" && h.file === r.file));
});

test("camada de texto: exporta o frame só dela (isolada) e restaura as outras", { skip: !hasRembg }, async () => {
  const ae = createAE({ framePng: img });
  const comp = ae.newComp();
  ae.addFootage(comp, img, { layer: { name: "Fundo" } });
  const t = ae.addText(comp, "Título");
  ae.select(comp, t);
  const core = mkCore(ae);
  await core.removeBg({ engine: "local", isolate: true });
  assert.deepStrictEqual(ae.log.frames[0].visible, ["Título"]);
  assert.ok(comp._layers.find((x) => x.name === "Fundo").enabled, "Fundo voltou a ficar visível");
  assert.strictEqual(comp.layer(1).source.mainSource.isStill, true);
  assert.strictEqual(comp.layer(2).enabled, false);
});

test("vídeo: ffmpeg extrai o trecho usado, rembg em lote e importa sequência com offset", { skip: !hasRembg || !hasFfmpeg }, async () => {
  const ae = createAE({ framePng: img });
  const comp = ae.newComp({ frameRate: 10 });
  const vid = path.join(HOME, "clip.mp4");
  execFileSync("ffmpeg", ["-hide_banner", "-loglevel", "error", "-y", "-f", "lavfi", "-i", "testsrc=size=160x120:rate=10:duration=1", "-pix_fmt", "yuv420p", vid]);
  const l = ae.addFootage(comp, vid, { isStill: false, fps: 10, duration: 1, layer: { name: "Clip", startTime: 2, inPoint: 2.3, outPoint: 2.8 } });
  ae.select(comp, l);
  const core = mkCore(ae);
  const prog = [];
  const r = await core.removeBg({ engine: "local" }, (t, p) => prog.push(p));
  assert.ok(r.frames >= 4 && r.frames <= 6, "frames do trecho: " + r.frames);
  const imp = ae.log.imports[ae.log.imports.length - 1];
  assert.strictEqual(imp.sequence, true);
  const dup = comp.layer(1);
  assert.ok(Math.abs(dup.startTime - 2.3) < 1e-6, "alinhado ao trecho: " + dup.startTime);
  assert.strictEqual(dup.source.mainSource.conformFrameRate, 10);
  assert.ok(prog.some((p) => p > 0.5 && p <= 1));
});

test("animar com fal.ai (simulado): envia a imagem, baixa o MP4 e importa no tempo atual", async () => {
  const srv = await falMock();
  const ae = createAE({ framePng: img });
  const comp = ae.newComp({ time: 3.5 });
  const l = ae.addFootage(comp, img, { layer: { name: "Produto" } });
  ae.select(comp, l);
  const core = mkCore(ae, srv);
  const r = await core.animate({ modelId: "fal-ai/kling-video/v3/standard/image-to-video", prompt: "giro 360", duration: 10, audio: false });
  assert.match(r.file, /anim_.*\.mp4$/);
  assert.strictEqual(fs.readFileSync(r.file, "utf8"), "fake mp4 bytes");
  const sub = srv.st.submits[0];
  assert.strictEqual(sub.headers.authorization, "Key k-teste");
  assert.deepStrictEqual(sub.json, { start_image_url: "https://cdn/x.png", prompt: "giro 360", duration: "10", generate_audio: false });
  assert.strictEqual(comp.layer(1).startTime, 3.5);
  const h = (await core.historyList()).find((x) => x.type === "anim");
  assert.ok(Math.abs(h.cost - 0.84) < 1e-9, "custo estimado = 10 s × 0,084");
  const est = await core.estimate("i2v", "fal", "fal-ai/kling-video/v3/standard/image-to-video", { duration: 5 });
  assert.strictEqual(est.text, "≈ US$ 0,42 · US$ 0,084/segundo");
  srv.close();
});

test("gerar imagem (simulado) no tamanho da comp e importar", async () => {
  const srv = await falMock();
  const ae = createAE({ framePng: img });
  ae.newComp({ width: 1080, height: 1920 });
  const core = mkCore(ae, srv);
  const r = await core.generate({ modelId: "fal-ai/flux/schnell", prompt: "pizza", aspect: "comp", seed: "" });
  assert.ok(fs.readFileSync(r.file).equals(PNG));
  assert.deepStrictEqual(srv.st.submits[0].json, { prompt: "pizza", image_size: { width: 816, height: 1440 }, num_images: 1, output_format: "png" });
  srv.close();
});

test("cancelar um trabalho em andamento", async () => {
  const srv = await falMock();
  srv.st.hang = true;
  const ae = createAE({ framePng: img });
  const comp = ae.newComp();
  ae.select(comp, ae.addFootage(comp, img));
  const core = mkCore(ae, srv);
  const p = core.animate({ modelId: "fal-ai/kling-video/v3/standard/image-to-video", prompt: "x", duration: 5 });
  await H.sleep(120);
  assert.ok(core.isRunning());
  core.cancel();
  await assert.rejects(p, (e) => e.cancelled === true);
  await H.sleep(50);
  assert.ok(srv.st.cancelled);
  assert.ok(!core.isRunning());
  srv.close();
});

test("chave do fal.ai ausente: pede para colar em Config", async () => {
  const ae = createAE({ framePng: img });
  const comp = ae.newComp();
  ae.select(comp, ae.addFootage(comp, img));
  const core = mkCore(ae);
  core.setCfg({ falKey: "" });
  await assert.rejects(core.animate({ prompt: "x" }), /chave do fal\.ai em Config/);
  core.setCfg({ falKey: "k-teste" });
  // e a chave fica fora do repositório, só no config do usuário
  assert.ok(S.paths.config.startsWith(HOME));
});
