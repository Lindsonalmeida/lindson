// MotionForge Web · lógica do estúdio (navegador). Sem servidor próprio:
// remover fundo roda no navegador (bg-worker.js) e animar/gerar chamam o fal.ai direto (fal-web.js).
import { createFal, friendly } from "/painel/motionforge/fal-web.js";

const M = window.MFModels;
const fal = createFal();
const $ = (id) => document.getElementById(id);
const $$ = (s, r) => Array.from((r || document).querySelectorAll(s));
const ls = {
  get(k, d) { try { const v = localStorage.getItem("mf." + k); return v == null ? d : v; } catch (e) { return d; } },
  set(k, v) { try { localStorage.setItem("mf." + k, v); } catch (e) { /* ignora */ } },
};
const state = { tab: ls.get("tab", "bg"), items: [], sel: -1, busy: false, abort: null };
let uid = 0;

// ---------- avisos ----------
function toast(msg, kind, ms) {
  const el = document.createElement("div");
  el.className = "toast " + (kind || "info");
  el.innerHTML = `<svg><use href="#${kind === "ok" ? "i-check" : kind === "err" ? "i-alert" : "i-gen"}"/></svg><span></span>`;
  el.querySelector("span").textContent = msg;
  $("toasts").appendChild(el);
  const kill = () => { el.classList.add("out"); setTimeout(() => el.remove(), 260); };
  el.onclick = kill;
  setTimeout(kill, ms || (kind === "err" ? 8000 : 3500));
}

// ---------- utilidades ----------
const key = () => ls.get("falKey", "");
function custom() { try { return JSON.parse(ls.get("customModels", "[]")) || []; } catch (e) { return []; } }
const models = (kind) => M.byKind("fal", kind, custom());
const baseName = (n) => String(n || "arquivo").replace(/\.[^.]+$/, "");
const stamp = () => new Date().toISOString().slice(0, 19).replace(/[-:T]/g, "");
function download(blob, name) {
  const a = document.createElement("a");
  a.href = URL.createObjectURL(blob); a.download = name; document.body.appendChild(a); a.click();
  setTimeout(() => { URL.revokeObjectURL(a.href); a.remove(); }, 4000);
}
async function fetchBlob(url, signal) {
  const r = await fetch(url, { signal });
  if (!r.ok) throw new Error("Não consegui baixar o resultado (" + r.status + ").");
  return r.blob();
}
function canvasBlob(c, type, q) { return new Promise((res) => c.toBlob(res, type, q)); }
async function toJpegDataUrl(blob, max = 2048) {
  const bmp = await createImageBitmap(blob);
  const s = Math.min(1, max / Math.max(bmp.width, bmp.height));
  const c = document.createElement("canvas");
  c.width = Math.round(bmp.width * s); c.height = Math.round(bmp.height * s);
  const g = c.getContext("2d"); g.fillStyle = "#000"; g.fillRect(0, 0, c.width, c.height); g.drawImage(bmp, 0, 0, c.width, c.height);
  return { url: c.toDataURL("image/jpeg", 0.92), w: bmp.width, h: bmp.height };
}
async function fillColor(png, color) {
  const bmp = await createImageBitmap(png);
  const c = document.createElement("canvas"); c.width = bmp.width; c.height = bmp.height;
  const g = c.getContext("2d"); g.fillStyle = color; g.fillRect(0, 0, c.width, c.height); g.drawImage(bmp, 0, 0);
  return canvasBlob(c, "image/png");
}
const fmtUsd = (v) => "US$ " + (v < 0.1 ? v.toFixed(3) : v.toFixed(2)).replace(".", ",");
const fmtTime = (s) => `${Math.floor(s / 60)}:${String(Math.floor(s % 60)).padStart(2, "0")}`;

// ---------- histórico (IndexedDB, só neste navegador) ----------
const DB = new Promise((res, rej) => {
  const r = indexedDB.open("motionforge", 1);
  r.onupgradeneeded = () => r.result.createObjectStore("items", { keyPath: "id" });
  r.onsuccess = () => res(r.result); r.onerror = () => rej(r.error);
});
async function dbDo(mode, fn) {
  const db = await DB;
  return new Promise((res, rej) => { const tx = db.transaction("items", mode); const st = tx.objectStore("items"); const out = fn(st); tx.oncomplete = () => res(out && out.result !== undefined ? out.result : out); tx.onerror = () => rej(tx.error); });
}
const histAdd = (e) => dbDo("readwrite", (st) => st.put(Object.assign({ id: Date.now().toString(36) + Math.random().toString(36).slice(2, 6), at: Date.now() }, e))).catch(() => {});
const histAll = () => dbDo("readonly", (st) => st.getAll()).then((a) => (a || []).sort((x, y) => y.at - x.at)).catch(() => []);
const histDel = (id) => dbDo("readwrite", (st) => st.delete(id));
const histClear = () => dbDo("readwrite", (st) => st.clear());

// ---------- remoção de fundo no navegador (worker) ----------
let worker = null, wseq = 0;
const wwait = new Map();
let wprog = null;
function getWorker() {
  if (worker) return worker;
  worker = new Worker("/painel/motionforge/bg-worker.js", { type: "module" });
  worker.onmessage = (ev) => {
    const m = ev.data;
    if (m.type === "progress" && wprog) wprog(m.loaded / m.total);
    if (m.type === "ready") { $("gpuStat").textContent = m.device === "webgpu" ? "Placa de vídeo (WebGPU) ativa" : "Processador (sem WebGPU)"; }
    if ((m.type === "done" || m.type === "error") && wwait.has(m.id)) {
      const p = wwait.get(m.id); wwait.delete(m.id);
      m.type === "done" ? p.res(m.blob) : p.rej(new Error("Remoção de fundo: " + m.message));
    }
  };
  worker.onerror = (e) => { wwait.forEach((p) => p.rej(new Error("O navegador não conseguiu carregar o modelo: " + (e.message || "erro")))); wwait.clear(); worker = null; };
  return worker;
}
function cutLocal(blob, model, signal) {
  const id = ++wseq;
  return new Promise((res, rej) => {
    wwait.set(id, { res, rej });
    if (signal) signal.addEventListener("abort", () => { if (wwait.has(id)) { wwait.delete(id); rej(Object.assign(new Error("Cancelado."), { name: "Cancelled" })); } }, { once: true });
    getWorker().postMessage({ type: "run", id, blob, model });
  });
}

// ---------- mesa ----------
function addItem(blob, name, extra) {
  const kind = /^video\//.test(blob.type) || /\.(mp4|mov|webm|m4v)$/i.test(name) ? "video" : "image";
  const it = Object.assign({ id: ++uid, name, kind, src: blob, srcUrl: URL.createObjectURL(blob), out: null }, extra || {});
  state.items.push(it);
  return it;
}
function addFiles(list) {
  const files = Array.from(list || []).filter((f) => /^(image|video)\//.test(f.type) || /\.(png|jpe?g|webp|mp4|mov|webm)$/i.test(f.name));
  if (!files.length) { toast("Formato não suportado. Use PNG, JPG, WebP, MP4, MOV ou WebM.", "err"); return; }
  files.forEach((f) => addItem(f, f.name));
  select(state.items.length - files.length);
}
const cur = () => state.items[state.sel] || null;
function select(i) { state.sel = i; render(); }
function setOut(it, out) { if (it.out && it.out.url) URL.revokeObjectURL(it.out.url); it.out = out; if (out && out.blob && !out.url) out.url = URL.createObjectURL(out.blob); }

function render() {
  const it = cur();
  $("drop").hidden = !!it;
  $("viewImg").hidden = !it || (it.kind !== "image" && !(it.out && it.out.preview));
  $("viewVideo").hidden = true;
  if (it) {
    const outVideo = it.out && it.out.kind === "video";
    if (it.kind === "video" && !it.out) { showVideo(it.srcUrl); }
    else if (outVideo) { showVideo(it.out.url); }
    else {
      const after = it.out ? (it.out.preview || it.out.url) : it.srcUrl;
      $("imgAfter").src = after;
      $("imgBefore").src = it.kind === "image" ? it.srcUrl : (it.out && it.out.before) || it.srcUrl;
      $("cmp").classList.toggle("has", !!it.out);
      $("viewImg").hidden = false;
    }
    const tag = it.out ? (it.out.kind === "zip" ? ` · ${it.out.frames} frames sem fundo` : " · sem fundo") : "";
    $("stageName").innerHTML = "";
    $("stageName").append(document.createTextNode(it.name), Object.assign(document.createElement("small"), { textContent: (it.kind === "video" ? "vídeo" : "imagem") + tag }));
  } else $("stageName").textContent = "Mesa de trabalho";
  $("btnDownload").hidden = !it;
  $("dlLabel").textContent = it && it.out ? (it.out.kind === "zip" ? "Baixar frames (.zip)" : "Baixar resultado") : "Baixar";
  $("btnZip").hidden = state.items.filter((x) => x.out && x.out.kind !== "zip").length < 2;
  // faixa
  const strip = $("strip");
  strip.innerHTML = "";
  state.items.forEach((x, i) => {
    const t = document.createElement("div");
    t.className = "thumb checker" + (i === state.sel ? " on" : "");
    const media = x.kind === "video" && !(x.out && x.out.preview) ? Object.assign(document.createElement("video"), { src: (x.out && x.out.kind === "video" ? x.out.url : x.srcUrl) + "#t=0.3", muted: true }) : Object.assign(document.createElement("img"), { src: x.out ? (x.out.preview || x.out.url) : x.srcUrl });
    t.appendChild(media);
    const b = document.createElement("span"); b.className = "b" + (x.out ? " ok" : ""); b.textContent = x.out ? "pronto" : x.kind === "video" ? "vídeo" : "foto"; t.appendChild(b);
    const del = document.createElement("button"); del.className = "x"; del.title = "Tirar da mesa"; del.innerHTML = '<svg><use href="#i-x"/></svg>';
    del.onclick = (e) => { e.stopPropagation(); state.items.splice(i, 1); if (state.sel >= state.items.length) state.sel = state.items.length - 1; render(); };
    t.appendChild(del);
    t.onclick = () => select(i);
    strip.appendChild(t);
  });
  if (state.items.length) { const a = document.createElement("div"); a.className = "thumb add"; a.title = "Adicionar"; a.innerHTML = '<svg><use href="#i-plus"/></svg>'; a.onclick = () => $("fileIn").click(); strip.appendChild(a); }
  updateTabUI();
}
function showVideo(url) { const v = $("viewVideo"); if (v.src !== url) v.src = url; v.hidden = false; $("viewImg").hidden = true; }

// comparação antes/depois
(function () {
  let drag = false;
  const set = (x) => { const r = $("cmp").getBoundingClientRect(); const p = Math.max(0, Math.min(1, (x - r.left) / r.width)); $("cmpBefore").style.clipPath = `inset(0 ${100 - p * 100}% 0 0)`; $("cmpHandle").style.left = p * 100 + "%"; };
  $("cmp").addEventListener("pointerdown", (e) => { if (!$("cmp").classList.contains("has")) return; drag = true; $("cmp").setPointerCapture(e.pointerId); set(e.clientX); });
  $("cmp").addEventListener("pointermove", (e) => drag && set(e.clientX));
  $("cmp").addEventListener("pointerup", () => (drag = false));
})();

// entrada de arquivos
$("drop").onclick = () => $("fileIn").click();
$("btnAdd").onclick = () => $("fileIn").click();
$("fileIn").onchange = (e) => { addFiles(e.target.files); e.target.value = ""; };
let dragN = 0;
window.addEventListener("dragenter", (e) => { if (e.dataTransfer && Array.from(e.dataTransfer.types).includes("Files")) { dragN++; $("dragover").classList.add("on"); } });
window.addEventListener("dragleave", () => { dragN = Math.max(0, dragN - 1); if (!dragN) $("dragover").classList.remove("on"); });
window.addEventListener("dragover", (e) => e.preventDefault());
window.addEventListener("drop", (e) => { e.preventDefault(); dragN = 0; $("dragover").classList.remove("on"); if (e.dataTransfer.files.length) addFiles(e.dataTransfer.files); });
window.addEventListener("paste", (e) => { const f = Array.from(e.clipboardData.files || []); if (f.length) addFiles(f); });
$("btnDownload").onclick = () => {
  const it = cur(); if (!it) return;
  if (!it.out) return download(it.src, it.name);
  const ext = it.out.kind === "zip" ? "zip" : it.out.ext || "png";
  download(it.out.blob, `${baseName(it.name)}-${it.out.suffix || "sem-fundo"}.${ext}`);
};
$("btnZip").onclick = async () => {
  const zip = new window.JSZip();
  state.items.filter((x) => x.out && x.out.kind !== "zip").forEach((x, i) => zip.file(`${String(i + 1).padStart(2, "0")}-${baseName(x.name)}-${x.out.suffix || "sem-fundo"}.${x.out.ext || "png"}`, x.out.blob));
  download(await zip.generateAsync({ type: "blob" }), `motionforge-${stamp()}.zip`);
};

// ---------- abas e controles ----------
const CTA = { bg: "Remover fundo", anim: "Animar imagem", gen: "Gerar imagem" };
function segSet(el, v) { $$("button", el).forEach((b) => b.classList.toggle("on", b.dataset.v === String(v))); }
const segVal = (el) => { const b = $$("button.on", el)[0]; return b ? b.dataset.v : null; };
$$(".seg").forEach((el) => el.addEventListener("click", (e) => {
  const b = e.target.closest("button"); if (!b) return;
  segSet(el, b.dataset.v); ls.set(el.id, b.dataset.v); updateTabUI(); refreshCost();
}));
["bgEngine", "bgFill", "genAspect", "animDur"].forEach((id) => { const v = ls.get(id, null); if (v) segSet($(id), v); });

function setTab(t) {
  state.tab = t; ls.set("tab", t);
  $$("#nav button").forEach((b) => b.classList.toggle("on", b.dataset.tab === t));
  $$(".view").forEach((v) => v.classList.toggle("on", v.id === "view-" + t));
  $("cta").hidden = !CTA[t]; $("cost").hidden = !CTA[t];
  $("ctaLabel").textContent = CTA[t] || "";
  if (t === "hist") renderHist();
  updateTabUI(); refreshCost();
}
$$("#nav button").forEach((b) => (b.onclick = () => setTab(b.dataset.tab)));
$("provPill").onclick = () => setTab("cfg");

function fill(sel, list, saved) {
  sel.innerHTML = "";
  list.forEach((m) => { const o = document.createElement("option"); o.value = m.id; o.textContent = m.label + (m.custom ? " ★" : ""); o.title = m.id; sel.appendChild(o); });
  if (saved && list.some((m) => m.id === saved)) sel.value = saved;
}
function fillModels() {
  fill($("animModel"), models("i2v"), ls.get("animModel"));
  fill($("genModel"), models("t2i"), ls.get("genModel"));
  fill($("bgCloudModel"), models("bg"), ls.get("bgCloudModel"));
  $("bgLocalModel").value = ls.get("bgLocalModel", "onnx-community/BiRefNet_lite-ONNX");
  fillDur(); applyUses();
}
const curModel = (kind) => models(kind).find((m) => m.id === $(kind === "i2v" ? "animModel" : kind === "t2i" ? "genModel" : "bgCloudModel").value);
function fillDur() {
  const ds = (curModel("i2v") || {}).durations || [5, 10];
  const want = Number(ls.get("animDur", "5"));
  $("animDur").innerHTML = ds.map((d) => `<button data-v="${d}">${d} s</button>`).join("");
  segSet($("animDur"), ds.reduce((a, b) => (Math.abs(b - want) < Math.abs(a - want) ? b : a), ds[0]));
}
function applyUses() {
  const uses = (m, f) => !!m && JSON.stringify(m.input || {}).includes("{{" + f);
  $$("#view-anim [data-uses]").forEach((el) => (el.hidden = !uses(curModel("i2v"), el.dataset.uses)));
  $$("#view-gen [data-uses]").forEach((el) => (el.hidden = !uses(curModel("t2i"), el.dataset.uses)));
}
["animModel", "genModel", "bgCloudModel", "bgLocalModel"].forEach((id) => ($(id).onchange = () => { ls.set(id, $(id).value); if (id === "animModel") { fillDur(); applyUses(); } if (id === "genModel") applyUses(); refreshCost(); }));

function updateTabUI() {
  const it = cur();
  const cloud = segVal($("bgEngine")) === "cloud";
  $("bgLocalBox").hidden = cloud; $("bgCloudBox").hidden = !cloud;
  $("bgColor").hidden = segVal($("bgFill")) !== "color";
  const isVid = it && it.kind === "video";
  $("bgVideoBox").hidden = !isVid;
  $("bgVideoLocalOpts").hidden = cloud; $("bgVideoCloudOpts").hidden = !cloud;
  $("bgVideoTxt").textContent = cloud
    ? "O vídeo vai para o fal.ai (BiRefNet vídeo) e volta com transparência, pronto para editar."
    : "Cada quadro é recortado aqui no navegador e você baixa uma sequência PNG com transparência (.zip). Para vídeos longos, use a Nuvem.";
  const imgs = state.items.filter((x) => x.kind === "image").length;
  $("bgAllBox").hidden = !(it && it.kind === "image" && imgs > 1);
  $("bgAllN").textContent = imgs;
  $("animUseCutBox").hidden = !(it && it.kind === "image" && it.out && it.out.kind === "image");
  const ok = !!key();
  $("provPill").querySelector(".dot").className = "dot " + (ok ? "ok" : "warn");
  $("provTxt").textContent = ok ? "fal.ai conectado" : "Falta a chave";
  if (state.tab === "anim") $("ctaLabel").textContent = it && it.kind === "video" ? "Animar o quadro atual" : "Animar imagem";
}

// ---------- custo ----------
let costT = null, costSeq = 0;
function refreshCost() { clearTimeout(costT); costT = setTimeout(doCost, 250); }
async function price(id) {
  const c = JSON.parse(ls.get("price:" + id, "null") || "null");
  if (c && Date.now() - c.t < 12 * 3600e3) return c.v;
  const all = await fal.pricing(key(), [id]);
  if (all[id]) ls.set("price:" + id, JSON.stringify({ t: Date.now(), v: all[id] }));
  return all[id];
}
const UNIT = { second: "segundo", seconds: "segundo", image: "imagem", images: "imagem", video: "vídeo", videos: "vídeo", megapixel: "megapixel", megapixels: "megapixel", request: "uso", requests: "uso" };
async function estimate(id, vars) {
  const p = await price(id);
  if (!p) return { text: "Preço indisponível para este modelo" };
  const u = String(p.unit || "").toLowerCase();
  const n = /second/.test(u) ? Number(vars.duration) || 5 : /megapixel/.test(u) && vars.size ? (vars.size.width * vars.size.height) / 1e6 : 1;
  return { usd: p.price * n, text: `≈ ${fmtUsd(p.price * n)} · ${fmtUsd(p.price)}/${UNIT[u] || p.unit || "uso"}` };
}
async function doCost() {
  const my = ++costSeq, el = $("cost");
  let r = null;
  try {
    if (state.tab === "bg" && segVal($("bgEngine")) === "local") r = { text: "Grátis · roda no seu navegador" };
    else if (!CTA[state.tab]) r = null;
    else if (!key()) r = { text: "Cole a chave do fal.ai em Config para ver o custo" };
    else if (state.tab === "bg") { const it = cur(); r = it && it.kind === "video" ? await estimate("fal-ai/birefnet/v2/video", { duration: 5 }) : await estimate($("bgCloudModel").value, {}); }
    else if (state.tab === "anim") r = await estimate($("animModel").value, { duration: Number(segVal($("animDur"))) || 5 });
    else if (state.tab === "gen") r = await estimate($("genModel").value, { size: genSize() });
  } catch (e) { r = { text: "Custo: " + friendly(e) }; }
  if (my !== costSeq) return;
  el.innerHTML = "";
  if (r && r.text) { const [a, ...b] = r.text.split(" · "); const s = document.createElement("b"); s.textContent = a; el.append(s); if (b.length) el.append(" · " + b.join(" · ")); }
}

// ---------- trabalhos ----------
let tick = null;
function jobStart(t) {
  state.busy = true; state.abort = new AbortController();
  $("job").hidden = false; $("cta").disabled = true; $("jobText").textContent = t || "Preparando…";
  const t0 = Date.now(); $("jobTime").textContent = "0:00";
  tick = setInterval(() => ($("jobTime").textContent = fmtTime((Date.now() - t0) / 1000)), 500);
  prog(-1);
  return state.abort.signal;
}
function prog(p) { const b = $("bar"); if (p == null || p < 0) b.classList.add("indet"); else { b.classList.remove("indet"); $("barFill").style.width = Math.round(Math.min(1, p) * 100) + "%"; } }
const status = (t, p) => { $("jobText").textContent = t; if (p !== undefined) prog(p); };
function jobEnd() { state.busy = false; clearInterval(tick); $("job").hidden = true; $("cta").disabled = false; $("barFill").style.width = "0"; wprog = null; }
$("btnCancel").onclick = () => { if (state.abort) state.abort.abort(); $("jobText").textContent = "Cancelando…"; };
async function runJob(fn) {
  if (state.busy) return;
  const signal = jobStart();
  try { const msg = await fn(signal); if (msg) toast(msg, "ok"); }
  catch (e) { if (e.name === "Cancelled" || e.name === "AbortError") toast("Cancelado.", "info", 2000); else { console.error(e); toast(friendly(e), "err"); } }
  finally { jobEnd(); render(); }
}
function needKey() { if (!key()) { setTab("cfg"); $("falKey").focus(); throw new Error("Cole a chave do fal.ai para usar a nuvem (fal.ai/dashboard/keys)."); } }
function needItem() { const it = cur(); if (!it) throw new Error("Adicione uma foto ou vídeo na mesa primeiro."); return it; }

// ===== remover fundo =====
async function doBg(signal) {
  const it = needItem();
  const cloud = segVal($("bgEngine")) === "cloud";
  const color = segVal($("bgFill")) === "color" ? $("bgColor").value : null;
  if (it.kind === "video") return cloud ? bgVideoCloud(it, signal) : bgVideoLocal(it, signal);
  if (cloud) needKey();
  const list = $("bgAll").checked && !$("bgAllBox").hidden ? state.items.filter((x) => x.kind === "image") : [it];
  const model = $("bgLocalModel").value;
  if (!cloud) wprog = (p) => status(`Baixando o modelo (só na primeira vez)… ${Math.round(p * 100)}%`, p);
  for (let i = 0; i < list.length; i++) {
    const x = list[i];
    const pre = list.length > 1 ? `${i + 1}/${list.length} · ` : "";
    status(pre + (cloud ? "Enviando…" : "Recortando…"), list.length > 1 ? i / list.length : -1);
    let png;
    if (cloud) {
      const m = curModel("bg");
      const img = await toJpegDataUrl(x.src);
      const res = await fal.run(key(), m.id, M.render(m.input, { image: img.url }), { signal, onStatus: (t) => status(pre + t) });
      png = await fetchBlob(M.extractUrls(res)[0], signal);
    } else {
      png = await cutLocal(x.src, model, signal);
      wprog = null;
    }
    if (color) png = await fillColor(png, color);
    setOut(x, { kind: "image", blob: png, ext: "png", suffix: "sem-fundo" });
    histAdd({ type: "bg", name: `${baseName(x.name)}-sem-fundo.png`, blob: png, model: cloud ? curModel("bg").id : model });
    if (x === cur()) render();
  }
  return list.length > 1 ? `${list.length} imagens sem fundo. Use "Baixar tudo".` : "Fundo removido.";
}

async function bgVideoLocal(it, signal) {
  const fps = Number($("bgFps").value), max = Number($("bgMax").value);
  const model = $("bgLocalModel").value;
  const v = document.createElement("video");
  v.muted = true; v.preload = "auto"; v.src = it.srcUrl;
  await new Promise((res, rej) => { v.onloadedmetadata = res; v.onerror = () => rej(new Error("O navegador não conseguiu abrir este vídeo. Tente MP4 (H.264) ou use a Nuvem.")); });
  const dur = Math.min(v.duration || 0, max);
  const n = Math.max(1, Math.floor(dur * fps));
  const c = document.createElement("canvas"); c.width = v.videoWidth; c.height = v.videoHeight;
  const g = c.getContext("2d");
  const zip = new window.JSZip();
  const color = segVal($("bgFill")) === "color" ? $("bgColor").value : null;
  wprog = (p) => status(`Baixando o modelo (só na primeira vez)… ${Math.round(p * 100)}%`, p);
  let last = null, first = null;
  const t0 = Date.now();
  for (let i = 0; i < n; i++) {
    if (signal.aborted) throw Object.assign(new Error("Cancelado."), { name: "Cancelled" });
    await new Promise((res) => { v.onseeked = res; v.currentTime = Math.min(i / fps, v.duration - 0.001); });
    g.drawImage(v, 0, 0);
    const frame = await canvasBlob(c, "image/jpeg", 0.95);
    let png = await cutLocal(frame, model, signal);
    wprog = null;
    if (color) png = await fillColor(png, color);
    zip.file(`quadro_${String(i + 1).padStart(5, "0")}.png`, png);
    last = png; if (!first) first = frame;
    const left = ((Date.now() - t0) / (i + 1)) * (n - i - 1) / 1000;
    status(`Recortando quadro ${i + 1}/${n} · falta ~${fmtTime(left)}`, (i + 1) / n);
  }
  status("Montando o .zip…", -1);
  const blob = await zip.generateAsync({ type: "blob" });
  setOut(it, { kind: "zip", blob, frames: n, ext: "zip", suffix: `sem-fundo-${fps}fps`, preview: URL.createObjectURL(last), before: URL.createObjectURL(first) });
  histAdd({ type: "bg", name: `${baseName(it.name)}-sem-fundo-${fps}fps.zip`, blob, preview: last, model });
  return `${n} quadros sem fundo. Clique em "Baixar frames (.zip)".`;
}

async function bgVideoCloud(it, signal) {
  needKey();
  const m = models("bgv")[0];
  status("Enviando o vídeo…", -1);
  const url = await fal.upload(key(), it.src, it.name, signal);
  const outType = $("bgVideoOut").value;
  const input = Object.assign(M.render(m.input, { video: url }), { video_output_type: outType });
  const res = await fal.run(key(), m.id, input, { signal, onStatus: (t) => status(t) });
  status("Baixando o resultado…", -1);
  const blob = await fetchBlob(M.extractUrls(res)[0], signal);
  const ext = /webm/i.test(outType) ? "webm" : "mov";
  setOut(it, { kind: "video", blob, ext, suffix: "sem-fundo" });
  histAdd({ type: "bg", name: `${baseName(it.name)}-sem-fundo.${ext}`, blob, model: m.id });
  return ext === "mov" ? "Pronto. O MOV ProRes pode não tocar no navegador, mas abre no Premiere/After/DaVinci." : "Vídeo sem fundo pronto.";
}

// ===== animar =====
async function currentFrame(it) {
  const v = $("viewVideo");
  const c = document.createElement("canvas"); c.width = v.videoWidth; c.height = v.videoHeight;
  c.getContext("2d").drawImage(v, 0, 0);
  return canvasBlob(c, "image/jpeg", 0.95);
}
async function doAnim(signal) {
  needKey();
  const it = needItem();
  const m = curModel("i2v");
  const prompt = $("animPrompt").value.trim();
  if (!prompt) throw new Error("Escreva o movimento que você quer.");
  let blob = it.src;
  if (it.kind === "video") blob = await currentFrame(it);
  else if ($("animUseCut").checked && it.out && it.out.kind === "image") blob = it.out.blob;
  status("Preparando a imagem…");
  const img = await toJpegDataUrl(blob);
  const vars = {
    image: img.url, prompt, negative: $("animNeg").value.trim(), seed: $("animSeed").value.trim() === "" ? "" : Number($("animSeed").value),
    audio: $("animAudio").checked, duration: M.nearestDuration(m, Number(segVal($("animDur"))) || 5),
    aspect: m.aspects ? M.nearestAspect(m.aspects, img.w, img.h) : "",
  };
  const res = await fal.run(key(), m.id, M.render(m.input, vars), { signal, onStatus: (t) => status(t) });
  status("Baixando o vídeo…");
  const vb = await fetchBlob(M.extractUrls(res)[0], signal);
  const name = `${baseName(it.name)}-animado.mp4`;
  const est = await estimate(m.id, vars).catch(() => null);
  histAdd({ type: "anim", name, blob: vb, prompt, model: m.id, cost: est && est.usd });
  addItem(vb, name, { origin: "anim" });
  state.sel = state.items.length - 1;
  return "Vídeo pronto. Use \"Baixar\" para salvar.";
}

// ===== gerar =====
function genSize() {
  const [a, b] = (segVal($("genAspect")) || "1:1").split(":").map(Number);
  const s = 1440 / Math.max(a, b);
  const r16 = (v) => Math.max(256, Math.round((v * s) / 16) * 16);
  return { width: r16(a), height: r16(b) };
}
async function doGen(signal) {
  needKey();
  const m = curModel("t2i");
  const prompt = $("genPrompt").value.trim();
  if (!prompt) throw new Error("Descreva a imagem que você quer.");
  const size = genSize();
  const vars = { prompt, negative: $("genNeg").value.trim(), seed: $("genSeed").value.trim() === "" ? "" : Number($("genSeed").value), size, aspect: segVal($("genAspect")) };
  const res = await fal.run(key(), m.id, M.render(m.input, vars), { signal, onStatus: (t) => status(t) });
  const urls = M.extractUrls(res);
  status("Baixando…");
  const est = await estimate(m.id, vars).catch(() => null);
  for (let i = 0; i < urls.length; i++) {
    const b = await fetchBlob(urls[i], signal);
    const ext = /png/.test(b.type) ? "png" : "jpg";
    const name = `gerada-${stamp()}${urls.length > 1 ? "-" + (i + 1) : ""}.${ext}`;
    histAdd({ type: "gen", name, blob: b, prompt, model: m.id, seed: res.seed, cost: est && est.usd });
    addItem(new File([b], name, { type: b.type }), name, { origin: "gen" });
  }
  state.sel = state.items.length - 1;
  return "Imagem na mesa. Dá para animar ou remover o fundo dela agora.";
}

function doCta() {
  if (state.tab === "bg") runJob(doBg);
  else if (state.tab === "anim") runJob(doAnim);
  else if (state.tab === "gen") runJob(doGen);
}
$("cta").onclick = doCta;
document.addEventListener("keydown", (e) => {
  if ((e.ctrlKey || e.metaKey) && e.key === "Enter" && CTA[state.tab] && !state.busy) { e.preventDefault(); doCta(); }
  if (e.key === "Escape" && state.busy && state.abort) state.abort.abort();
});

// ---------- prompts salvos ----------
[["animPrompt", "animCount"], ["genPrompt", "genCount"]].forEach(([t, c]) => {
  const el = $(t); el.value = ls.get(t, "");
  const up = () => { $(c).textContent = el.value.length; ls.set(t, el.value); };
  el.addEventListener("input", up); up();
});
["animNeg", "animSeed", "genNeg", "genSeed"].forEach((k) => { $(k).value = ls.get(k, ""); $(k).addEventListener("input", () => ls.set(k, $(k).value)); });
$$("#animPresets button").forEach((b) => (b.onclick = () => { $$("#animPresets button").forEach((x) => x.classList.toggle("on", x === b)); $("animPrompt").value = b.dataset.p; $("animPrompt").dispatchEvent(new Event("input")); }));

// ---------- histórico ----------
let histFilter = "all", histUrls = [];
$$("#histFilter button").forEach((b) => (b.onclick = () => { $$("#histFilter button").forEach((x) => x.classList.toggle("on", x === b)); histFilter = b.dataset.f; renderHist(); }));
async function renderHist() {
  histUrls.forEach((u) => URL.revokeObjectURL(u)); histUrls = [];
  let items = await histAll();
  if (histFilter !== "all") items = items.filter((h) => h.type === histFilter);
  const g = $("histGrid"); g.innerHTML = "";
  $("histEmpty").hidden = items.length > 0;
  const TYPE = { bg: "Sem fundo", anim: "Vídeo", gen: "Imagem" };
  items.slice(0, 200).forEach((h, n) => {
    const c = document.createElement("div");
    c.className = "hcard" + (h.type === "bg" ? " checker" : "");
    c.style.animationDelay = Math.min(n, 14) * 22 + "ms";
    const isVid = /^video\//.test(h.blob.type);
    const src = URL.createObjectURL(h.preview || h.blob); histUrls.push(src);
    const media = isVid && !h.preview ? Object.assign(document.createElement("video"), { src: src + "#t=0.3", muted: true }) : Object.assign(document.createElement("img"), { src });
    c.appendChild(media);
    c.insertAdjacentHTML("beforeend", `<span class="b">${TYPE[h.type] || h.type}</span><button class="x" title="Apagar"><svg><use href="#i-trash"/></svg></button>`);
    c.title = `${h.name}\n${h.model || ""}${h.cost != null ? " · ≈ " + fmtUsd(h.cost) : ""}${h.prompt ? "\n" + h.prompt : ""}\nClique para levar à mesa`;
    c.onclick = async (e) => {
      if (e.target.closest(".x")) { await histDel(h.id); renderHist(); return; }
      if (/zip/.test(h.blob.type) || /\.zip$/.test(h.name)) { download(h.blob, h.name); return; }
      addItem(new File([h.blob], h.name, { type: h.blob.type }), h.name); state.sel = state.items.length - 1; render();
      toast("Levado para a mesa.", "ok", 1600);
    };
    g.appendChild(c);
  });
  try { const est = await navigator.storage.estimate(); $("histUse").textContent = `Usando ${(est.usage / 1048576).toFixed(0)} MB neste navegador`; } catch (e) { /* ignora */ }
}
$("histClear").onclick = async () => { if (confirm("Apagar todo o histórico deste navegador?")) { await histClear(); renderHist(); } };

// ---------- config ----------
$("falKey").value = key();
$("falKey").addEventListener("change", () => { ls.set("falKey", $("falKey").value.trim()); updateTabUI(); refreshCost(); toast("Chave salva neste navegador.", "ok", 1500); });
$("revealKey").onclick = () => { const i = $("falKey"); i.type = i.type === "password" ? "text" : "password"; };
$("testKey").onclick = async () => {
  ls.set("falKey", $("falKey").value.trim());
  const s = $("keyStat"); s.className = "stat"; s.textContent = "Testando…";
  try { await fal.pricing(key(), ["fal-ai/flux/schnell"]); s.className = "stat ok"; s.innerHTML = '<svg><use href="#i-check"/></svg>Chave válida'; }
  catch (e) { s.className = "stat err"; s.textContent = friendly(e); }
  updateTabUI(); refreshCost();
};
$("customModels").value = ls.get("customModels", "") === "[]" ? "" : ls.get("customModels", "");
$("customModels").addEventListener("change", () => {
  const s = $("cmStat"), t = $("customModels").value.trim() || "[]";
  try { const j = JSON.parse(t); if (!Array.isArray(j)) throw new Error("precisa ser uma lista [ … ]"); ls.set("customModels", JSON.stringify(j)); s.className = "stat ok"; s.textContent = `${j.length} modelo(s) extra(s) ativos`; fillModels(); }
  catch (e) { s.className = "stat err"; s.textContent = "JSON inválido: " + e.message; }
});
$("gpuStat").textContent = navigator.gpu ? "WebGPU disponível" : "Sem WebGPU (usa o processador)";

// ---------- início ----------
fillModels();
setTab(state.tab);
render();
if (!key()) setTimeout(() => toast("Remover fundo já funciona grátis. Para animar e gerar, cole a chave do fal.ai em Config.", "info", 7000), 700);
window.MF = { state, addItem, render, setTab };
