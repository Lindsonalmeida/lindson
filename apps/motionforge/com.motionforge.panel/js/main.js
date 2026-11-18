// MotionForge · UI do painel (DOM). A lógica fica em core.js (Node).
// Ref CSInterface: https://github.com/Adobe-CEP/CEP-Resources/tree/master/CEP_11.x
/* global CSInterface, SystemPath */
"use strict";
(function () {
  const VERSION = "1.0.0";
  const $ = (id) => document.getElementById(id);
  const $$ = (sel, root) => Array.from((root || document).querySelectorAll(sel));

  // ---------- backend ----------
  let cs = null, core, nodePath = null;
  if (typeof window.__adobe_cep__ !== "undefined" && typeof CSInterface !== "undefined") {
    cs = new CSInterface();
    nodePath = require("path");
    const ext = cs.getSystemPath(SystemPath.EXTENSION);
    core = require(nodePath.join(ext, "js", "core.js")).createCore({
      evalScript: (code) => new Promise((r) => cs.evalScript(code, r)),
      comfyDir: nodePath.join(ext, "comfy"),
    });
  } else if (window.MF_PREVIEW_CORE) {
    core = window.MF_PREVIEW_CORE; // pré-visualização no navegador (tests/preview)
  } else {
    document.body.innerHTML = "<p style='padding:20px;color:#aaa'>Abra este painel dentro do After Effects (Janela › Extensões › MotionForge).</p>";
    return;
  }

  let cfg = core.getCfg();
  const state = { tab: cfg.lastTab || "bg", info: null, infoKey: "", animSource: null, lastGen: null, histFilter: "all", busy: false };
  const ls = { get(k, d) { try { const v = localStorage.getItem("mf." + k); return v == null ? d : v; } catch (e) { return d; } }, set(k, v) { try { localStorage.setItem("mf." + k, v); } catch (e) { /* ignora */ } } };
  const fileUrl = (p) => p ? "file:///" + encodeURI(String(p).replace(/\\/g, "/").replace(/^\/+/, "")).replace(/#/g, "%23") : "";

  // ---------- tema do AE ----------
  function hex(c) { return "#" + [c.red, c.green, c.blue].map((v) => Math.round(v).toString(16).padStart(2, "0")).join(""); }
  function shade(c, d) { return hex({ red: Math.min(255, c.red + d), green: Math.min(255, c.green + d), blue: Math.min(255, c.blue + d) }); }
  function applyTheme() {
    if (!cs) return;
    try {
      const skin = cs.getHostEnvironment().appSkinInfo;
      const c = skin.panelBackgroundColor.color;
      const lum = (0.2126 * c.red + 0.7152 * c.green + 0.0722 * c.blue) / 255;
      const light = lum > 0.5;
      const r = document.documentElement.style;
      r.setProperty("--bg", hex(c));
      r.setProperty("--s1", shade(c, light ? -10 : 7));
      r.setProperty("--s2", shade(c, light ? -18 : 14));
      r.setProperty("--s3", shade(c, light ? -28 : 23));
      document.body.classList.toggle("light", light);
    } catch (e) { /* mantém o padrão */ }
  }
  applyTheme();
  if (cs) cs.addEventListener("com.adobe.csxs.events.ThemeColorChanged", applyTheme);

  // ---------- avisos ----------
  function toast(msg, kind, ms) {
    const el = document.createElement("div");
    el.className = "toast " + (kind || "info");
    el.innerHTML = `<svg><use href="#${kind === "ok" ? "i-check" : kind === "err" ? "i-alert" : "i-gen"}"/></svg><span></span>`;
    el.querySelector("span").textContent = msg;
    $("toasts").appendChild(el);
    const kill = () => { el.classList.add("out"); setTimeout(() => el.remove(), 260); };
    el.onclick = kill;
    setTimeout(kill, ms || (kind === "err" ? 7000 : 3200));
  }

  // ---------- abas ----------
  const CTA = { bg: "Remover fundo", anim: "Animar camada", gen: "Gerar imagem", hist: "", cfg: "" };
  function moveInd() {
    const b = $$(".tabs button").find((x) => x.dataset.tab === state.tab);
    if (!b) return;
    const ind = $("tabInd");
    ind.style.width = b.offsetWidth + "px";
    ind.style.transform = `translateX(${b.offsetLeft - 3}px)`;
  }
  function setTab(t) {
    state.tab = t;
    $$(".tabs button").forEach((b) => b.classList.toggle("on", b.dataset.tab === t));
    $$(".view").forEach((v) => v.classList.toggle("on", v.id === "view-" + t));
    moveInd();
    $("cta").hidden = !CTA[t];
    if (t === "anim") $("ctaLabel").textContent = state.animSource ? "Animar imagem" : "Animar camada";
    else $("ctaLabel").textContent = CTA[t];
    if (t === "hist") renderHistory();
    refreshCost();
    save({ lastTab: t }, true);
  }
  $$(".tabs button").forEach((b) => (b.onclick = () => setTab(b.dataset.tab)));
  window.addEventListener("resize", moveInd);

  // ---------- segmentados ----------
  function segSet(el, v) { $$("button", el).forEach((b) => b.classList.toggle("on", b.dataset.v === String(v))); }
  function segVal(el) { const b = $$("button", el).find((x) => x.classList.contains("on")); return b ? b.dataset.v : null; }
  $$(".seg").forEach((el) => {
    el.addEventListener("click", (ev) => {
      const b = ev.target.closest("button"); if (!b || !el.contains(b)) return;
      segSet(el, b.dataset.v);
      if (el.dataset.key) { save({ [el.dataset.key]: b.dataset.v }); onCfgChanged(el.dataset.key); }
      if (el.id === "animDur") ls.set("animDur", b.dataset.v);
      if (el.id === "genAspect") ls.set("genAspect", b.dataset.v);
      refreshCost();
    });
  });

  // ---------- config ----------
  let saveTimer = null;
  function save(patch, silent) {
    try { cfg = core.setCfg(patch); } catch (e) { toast("Não salvou: " + e.message, "err"); return false; }
    if (!silent) { clearTimeout(saveTimer); saveTimer = setTimeout(() => toast("Configuração salva", "ok", 1400), 450); }
    return true;
  }

  function fillSelect(sel, list, current) {
    sel.innerHTML = "";
    list.forEach((m) => { const o = document.createElement("option"); o.value = m.id; o.textContent = m.label + (m.custom ? " ★" : ""); o.title = m.id; sel.appendChild(o); });
    if (current && list.some((m) => m.id === current)) sel.value = current;
  }
  function selModel(kind) { return ((cfg.selected || {})[kind] || {})[cfg.provider]; }
  function setSelModel(kind, id) { const s = JSON.parse(JSON.stringify(cfg.selected || {})); s[kind] = s[kind] || {}; s[kind][cfg.provider] = id; save({ selected: s }, true); }

  function fillModels() {
    fillSelect($("animModel"), core.models(cfg.provider, "i2v"), selModel("i2v"));
    fillSelect($("genModel"), core.models(cfg.provider, "t2i"), selModel("t2i"));
    fillSelect($("bgCloudModel"), core.models(cfg.provider === "comfy" ? "fal" : cfg.provider, "bg"), selModel("bg"));
    $("bgLocalModel").value = cfg.rembgModel || "birefnet-general";
    fillDurations();
    applyUses();
  }

  function currentModel(kind) {
    const id = kind === "i2v" ? $("animModel").value : kind === "t2i" ? $("genModel").value : $("bgCloudModel").value;
    return core.models(kind === "bg" && cfg.provider === "comfy" ? "fal" : cfg.provider, kind).find((m) => m.id === id);
  }

  function fillDurations() {
    const m = currentModel("i2v");
    const ds = (m && m.durations) || [5, 10];
    const el = $("animDur");
    const want = Number(ls.get("animDur", "5"));
    el.innerHTML = ds.map((d) => `<button data-v="${d}">${d} s</button>`).join("");
    const pick = ds.reduce((a, b) => (Math.abs(b - want) < Math.abs(a - want) ? b : a), ds[0]);
    segSet(el, pick);
  }

  // Mostra só os campos que o modelo usa (negativo, seed, áudio).
  function applyUses() {
    const m = currentModel("i2v"), g = currentModel("t2i");
    const uses = (mm, f) => !!mm && (mm.workflow ? ["prompt", "negative", "seed", "image", "duration"].includes(f) : JSON.stringify(mm.input || {}).includes("{{" + f));
    $$("#view-anim [data-uses]").forEach((el) => (el.hidden = !uses(m, el.dataset.uses)));
    $$("#view-gen [data-uses]").forEach((el) => (el.hidden = !uses(g, el.dataset.uses)));
  }

  function provStatus() {
    const p = cfg.provider;
    $("provName").textContent = { fal: "fal.ai", replicate: "Replicate", comfy: "ComfyUI" }[p];
    const ok = p === "fal" ? !!cfg.falKey : p === "replicate" ? !!cfg.replicateKey : !!cfg.comfyUrl;
    $("provPill").querySelector(".dot").className = "dot " + (ok ? "ok" : "warn");
    $("provPill").title = ok ? "Provedor ativo" : "Falta configurar a chave em Config";
    $$("[data-prov]").forEach((el) => (el.hidden = el.dataset.prov !== p));
  }

  function onCfgChanged(key) {
    if (key === "provider") { fillModels(); provStatus(); }
    if (key === "bgEngine") { $("bgLocalBox").hidden = cfg.bgEngine !== "local"; $("bgCloudBox").hidden = cfg.bgEngine === "local"; updateLayerUI(); }
    if (key === "bgInsert") $("bgInsertHint").textContent = cfg.bgInsert === "dup" ? "Duplica a camada com as mesmas animações e efeitos, já sem fundo." : "Troca a imagem da própria camada (Ctrl+Z volta).";
  }

  function loadCfgUI() {
    segSet(document.querySelector("[data-key=provider]"), cfg.provider);
    segSet(document.querySelector("[data-key=bgEngine]"), cfg.bgEngine);
    segSet(document.querySelector("[data-key=bgInsert]"), cfg.bgInsert);
    ["falKey", "replicateKey", "comfyUrl", "python", "ffmpeg", "outDir"].forEach((k) => ($(k).value = cfg[k] || ""));
    $("wfI2v").value = (cfg.comfyWorkflows || {}).i2v || "";
    $("wfT2i").value = (cfg.comfyWorkflows || {}).t2i || "";
    $("customModels").value = (cfg.customModels || []).length ? JSON.stringify(cfg.customModels, null, 1) : "";
    $("hideOriginal").checked = !!cfg.hideOriginal;
    $("isolateLayer").checked = !!cfg.isolateLayer;
    $("generateAudio").checked = !!cfg.generateAudio;
    $("cfgPath").textContent = core.paths.config;
    $("ver").textContent = VERSION;
    ["provider", "bgEngine", "bgInsert"].forEach(onCfgChanged);
    provStatus();
  }

  ["falKey", "replicateKey", "comfyUrl", "python", "ffmpeg", "outDir"].forEach((k) => {
    $(k).addEventListener("change", () => { save({ [k]: $(k).value.trim() }); provStatus(); refreshCost(); });
  });
  $("wfI2v").addEventListener("change", () => save({ comfyWorkflows: { i2v: $("wfI2v").value.trim(), t2i: $("wfT2i").value.trim() } }));
  $("wfT2i").addEventListener("change", () => save({ comfyWorkflows: { i2v: $("wfI2v").value.trim(), t2i: $("wfT2i").value.trim() } }));
  $("customModels").addEventListener("change", () => {
    const st = $("cmStat");
    try { cfg = core.setCfg({ customModels: $("customModels").value }); st.className = "stat ok"; st.textContent = `${(cfg.customModels || []).length} modelo(s) extra(s) ativos`; fillModels(); }
    catch (e) { st.className = "stat err"; st.textContent = "JSON inválido: " + e.message; }
  });
  ["hideOriginal", "isolateLayer", "generateAudio"].forEach((k) => $(k).addEventListener("change", () => save({ [k]: $(k).checked }, true)));
  $("bgLocalModel").onchange = () => save({ rembgModel: $("bgLocalModel").value }, true);
  $("bgCloudModel").onchange = () => { setSelModel("bg", $("bgCloudModel").value); refreshCost(); };
  $("animModel").onchange = () => { setSelModel("i2v", $("animModel").value); fillDurations(); applyUses(); refreshCost(); };
  $("genModel").onchange = () => { setSelModel("t2i", $("genModel").value); applyUses(); refreshCost(); };
  $$("[data-reveal]").forEach((b) => (b.onclick = () => { const i = $(b.dataset.reveal); i.type = i.type === "password" ? "text" : "password"; }));
  $("provPill").onclick = () => setTab("cfg");
  $("openOut").onclick = () => core.openPath(cfg.outDir);
  $("histFolder").onclick = () => core.openPath(cfg.outDir);
  $("openLogs").onclick = () => core.openPath(core.paths.logs);

  async function test(btn, stat, fn) {
    const s = $(stat), b = $(btn);
    b.disabled = true; s.className = "stat"; s.textContent = "Testando…";
    try {
      const r = await fn();
      const ok = typeof r === "object" ? r.ok : true;
      s.className = "stat " + (ok ? "ok" : "warn");
      s.innerHTML = `<svg><use href="#${ok ? "i-check" : "i-alert"}"/></svg>`;
      s.appendChild(document.createTextNode(typeof r === "object" ? r.text : r));
      if (r && r.cmd && !cfg.python) { /* detectado automaticamente */ }
    } catch (e) {
      s.className = "stat err"; s.innerHTML = '<svg><use href="#i-alert"/></svg>';
      s.appendChild(document.createTextNode(core.friendly(e)));
    } finally { b.disabled = false; }
  }
  $("testFal").onclick = () => { save({ falKey: $("falKey").value.trim() }, true); test("testFal", "falStat", core.testFal); };
  $("testRep").onclick = () => { save({ replicateKey: $("replicateKey").value.trim() }, true); test("testRep", "repStat", core.testReplicate); };
  $("testComfy").onclick = () => { save({ comfyUrl: $("comfyUrl").value.trim() }, true); test("testComfy", "comfyStat", core.testComfy); };
  $("testPy").onclick = () => test("testPy", "pyStat", core.testPython);
  $("testFf").onclick = () => test("testFf", "ffStat", core.testFfmpeg);

  // ---------- camada selecionada ----------
  function fmtTime(s) { s = Math.max(0, s || 0); const m = Math.floor(s / 60); return `${m}:${String(Math.floor(s % 60)).padStart(2, "0")}`; }
  function updateLayerUI() {
    const i = state.info, card = $("layerCard");
    card.classList.remove("warn");
    if (!i || i.error) {
      $("layerName").textContent = i && i.comp ? i.comp.name : "Nenhuma camada";
      $("layerSub").textContent = (i && i.error) || "Abra uma composição";
      card.classList.toggle("warn", !!(i && i.error && !i.noLayer));
      $("thumb").classList.remove("has");
      $("bgVideoNote").hidden = true;
      return;
    }
    $("layerName").textContent = i.name;
    const parts = [i.kind];
    if (i.srcWidth) parts.push(`${i.srcWidth}×${i.srcHeight}`);
    if (i.isVideo) parts.push(fmtTime(i.outPoint - i.inPoint));
    parts.push(`${Math.round(i.comp.fps * 100) / 100} fps`);
    $("layerSub").textContent = parts.join(" · ");
    $("bgVideoNote").hidden = !i.isVideo;
    if (i.isVideo) $("bgVideoText").textContent = cfg.bgEngine === "cloud"
      ? "O trecho usado na comp vai para o fal.ai (BiRefNet vídeo) e volta como ProRes 4444 com alpha, alinhado à camada."
      : "O recorte é feito frame a frame (ffmpeg + rembg) e volta como sequência PNG com alpha, alinhada à camada.";
  }

  async function pollLayer(force) {
    if (state.busy && !force) return;
    let info;
    try { info = await core.layerInfo(); } catch (e) { info = { error: core.friendly(e) }; }
    const key = info && !info.error ? `${info.comp.id}:${info.index}:${info.name}:${info.file || ""}` : "x:" + (info && info.error);
    state.info = info;
    if (key !== state.infoKey || force) { state.infoKey = key; updateLayerUI(); refreshThumb(force); refreshCost(); }
  }

  let thumbSeq = 0;
  async function refreshThumb(force) {
    const i = state.info, img = $("thumbImg"), box = $("thumb");
    const my = ++thumbSeq;
    if (!i || i.error) { box.classList.remove("has"); return; }
    let src = null;
    if (i.file && i.isStill && !i.fileUnsupported) src = i.file;
    else if (force || !i.file || i.isVideo) {
      try { src = await core.exportFrame(i, false); } catch (e) { src = null; }
    }
    if (my !== thumbSeq) return;
    if (!src) { box.classList.remove("has"); return; }
    img.onload = () => box.classList.add("has");
    img.onerror = () => box.classList.remove("has");
    img.src = fileUrl(src) + "?t=" + Date.now();
  }
  $("btnRefresh").onclick = async () => { const b = $("btnRefresh"); b.classList.add("spinning"); await pollLayer(true); setTimeout(() => b.classList.remove("spinning"), 400); };
  setInterval(() => { if (!document.hidden) pollLayer(false); }, 1500);
  window.addEventListener("focus", () => pollLayer(false));

  // ---------- custo ----------
  let costSeq = 0, costTimer = null;
  function refreshCost() { clearTimeout(costTimer); costTimer = setTimeout(doCost, 250); }
  async function doCost() {
    const el = $("cost"), my = ++costSeq;
    let r = null;
    try {
      if (state.tab === "bg") {
        r = cfg.bgEngine === "local" ? await core.estimate("bg-local") : await core.estimate("bg", cfg.provider === "comfy" ? "fal" : cfg.provider, (state.info && state.info.isVideo ? "fal-ai/birefnet/v2/video" : $("bgCloudModel").value), { duration: state.info && state.info.isVideo ? state.info.outPoint - state.info.inPoint : 0 });
      } else if (state.tab === "anim") {
        const m = currentModel("i2v"); if (m) r = await core.estimate("i2v", cfg.provider, m.id, { duration: Number(segVal($("animDur"))) || 5 });
      } else if (state.tab === "gen") {
        const m = currentModel("t2i"); if (m) r = await core.estimate("t2i", cfg.provider, m.id, { size: { width: 1440, height: 810 } });
      }
    } catch (e) { r = { text: "Custo: " + core.friendly(e, "fal.ai") }; }
    if (my !== costSeq) return;
    el.innerHTML = "";
    if (r && r.text) {
      const t = r.text.split(" · ");
      const b = document.createElement("b"); b.textContent = t[0]; el.appendChild(b);
      if (t[1]) el.appendChild(document.createTextNode(" · " + t.slice(1).join(" · ")));
      el.title = r.usd != null ? "Estimativa com o preço atual da sua conta no provedor. O valor final é o que o provedor cobrar." : "";
    }
  }

  // ---------- contadores e prompts salvos ----------
  [["animPrompt", "animCount"], ["genPrompt", "genCount"]].forEach(([t, c]) => {
    const el = $(t);
    el.value = ls.get(t, "");
    const upd = () => { $(c).textContent = el.value.length; ls.set(t, el.value); };
    el.addEventListener("input", upd); upd();
  });
  ["animNeg", "animSeed", "genNeg", "genSeed"].forEach((k) => { $(k).value = ls.get(k, ""); $(k).addEventListener("input", () => ls.set(k, $(k).value)); });
  $$("#animPresets button").forEach((b) => (b.onclick = () => {
    $$("#animPresets button").forEach((x) => x.classList.remove("on"));
    b.classList.add("on");
    $("animPrompt").value = b.dataset.p; $("animPrompt").dispatchEvent(new Event("input"));
  }));
  segSet($("genAspect"), ls.get("genAspect", "comp"));

  function setAnimSource(file) {
    state.animSource = file;
    const box = $("animSource");
    box.classList.toggle("custom", !!file);
    $("animSourceName").textContent = file ? file.split(/[\\/]/).pop() : "camada selecionada";
    $("animSourceClear").hidden = !file;
    if (state.tab === "anim") $("ctaLabel").textContent = file ? "Animar imagem" : "Animar camada";
  }
  $("animSourceClear").onclick = () => setAnimSource(null);

  // ---------- trabalhos ----------
  let tick = null;
  function jobStart(text) {
    state.busy = true;
    $("job").hidden = false; $("cta").disabled = true;
    $("jobText").textContent = text || "Preparando…";
    const t0 = Date.now();
    $("jobTime").textContent = "0:00";
    tick = setInterval(() => ($("jobTime").textContent = fmtTime((Date.now() - t0) / 1000)), 500);
    setProgress(-1);
  }
  function setProgress(p) {
    const bar = $("bar");
    if (p == null || p < 0) { bar.classList.add("indet"); }
    else { bar.classList.remove("indet"); $("barFill").style.width = Math.round(Math.min(1, p) * 100) + "%"; }
  }
  function jobEnd() {
    state.busy = false;
    clearInterval(tick);
    $("job").hidden = true; $("cta").disabled = false;
    $("barFill").style.width = "0";
  }
  const onStatus = (t, p) => { $("jobText").textContent = t; setProgress(p); };
  $("btnCancel").onclick = () => { core.cancel(); $("jobText").textContent = "Cancelando…"; };

  async function runJob(fn, okMsg) {
    if (state.busy) return;
    jobStart();
    try {
      const r = await fn();
      toast(okMsg(r), "ok");
      return r;
    } catch (e) {
      if (e.cancelled) toast("Cancelado.", "info", 2000); else toast(e.message, "err");
      return null;
    } finally { jobEnd(); pollLayer(true); }
  }

  async function doCta() {
    if (state.tab === "bg") {
      await runJob(() => core.removeBg({ cloudModel: $("bgCloudModel").value, localModel: $("bgLocalModel").value }, onStatus),
        (r) => r.frames ? `${r.frames} frames sem fundo importados` : "Fundo removido · camada importada");
    } else if (state.tab === "anim") {
      await runJob(() => core.animate({
        modelId: $("animModel").value, prompt: $("animPrompt").value, duration: segVal($("animDur")),
        negative: $("animNeg").value.trim(), seed: $("animSeed").value.trim(), audio: $("generateAudio").checked, sourceFile: state.animSource,
      }, onStatus), () => "Vídeo importado no tempo atual");
    } else if (state.tab === "gen") {
      const r = await runJob(() => core.generate({
        modelId: $("genModel").value, prompt: $("genPrompt").value, negative: $("genNeg").value.trim(), seed: $("genSeed").value.trim(), aspect: segVal($("genAspect")),
      }, onStatus), () => "Imagem gerada e importada");
      if (r) { state.lastGen = r; $("genResult").hidden = false; $("genResultImg").src = fileUrl(r.file) + "?t=" + Date.now(); }
    }
  }
  $("cta").onclick = doCta;
  document.addEventListener("keydown", (e) => {
    if ((e.ctrlKey || e.metaKey) && e.key === "Enter" && !$("cta").hidden && !state.busy) { e.preventDefault(); doCta(); }
    if (e.key === "Escape" && state.busy) core.cancel();
  });
  $("genAnimate").onclick = () => { if (state.lastGen) { setAnimSource(state.lastGen.file); setTab("anim"); $("animPrompt").focus(); } };
  $("genReimport").onclick = async () => { if (state.lastGen) { try { await core.reimport(state.lastGen.history.id); toast("Importado", "ok"); } catch (e) { toast(e.message, "err"); } } };

  // ---------- histórico ----------
  const TYPE = { bg: "Fundo", anim: "Vídeo", gen: "Imagem" };
  $$("#histFilter button").forEach((b) => (b.onclick = () => {
    $$("#histFilter button").forEach((x) => x.classList.toggle("on", x === b));
    state.histFilter = b.dataset.f; renderHistory();
  }));
  async function renderHistory() {
    const grid = $("histGrid");
    let items = [];
    try { items = await core.historyList(); } catch (e) { items = []; }
    if (state.histFilter !== "all") items = items.filter((h) => h.type === state.histFilter);
    grid.innerHTML = "";
    $("histEmpty").hidden = items.length > 0;
    items.slice(0, 120).forEach((h, n) => {
      const c = document.createElement("div");
      c.className = "card" + (h.type === "bg" ? " checker" : "") + (h.exists ? "" : " missing");
      c.style.animationDelay = Math.min(n, 12) * 25 + "ms";
      c.innerHTML = (h.thumb ? `<img loading="lazy" alt="">` : `<div class="ph-video"><svg><use href="#i-anim"/></svg></div>`) +
        `<span class="badge">${TYPE[h.type] || h.type}${h.seq ? " · seq" : ""}</span>` +
        `<div class="acts">${h.type === "gen" ? '<button data-a="anim" title="Animar esta"><svg><use href="#i-anim"/></svg></button>' : ""}<button data-a="del" title="Tirar do histórico"><svg><use href="#i-trash"/></svg></button></div>` +
        `<div class="meta"></div>`;
      if (h.thumb) c.querySelector("img").src = fileUrl(h.thumb);
      const when = new Date(h.createdAt);
      c.querySelector(".meta").textContent = (h.prompt ? h.prompt.slice(0, 60) + " · " : "") + when.toLocaleDateString("pt-BR") + " " + when.toLocaleTimeString("pt-BR", { hour: "2-digit", minute: "2-digit" });
      c.title = `${h.model || ""}${h.cost != null ? " · ≈ US$ " + Number(h.cost).toFixed(2) : ""}\nClique para importar na comp`;
      c.onclick = async (ev) => {
        const a = ev.target.closest("button");
        if (a && a.dataset.a === "del") { core.historyRemove(h.id); renderHistory(); return; }
        if (a && a.dataset.a === "anim") { setAnimSource(h.file); setTab("anim"); return; }
        if (!h.exists) { toast("O arquivo foi apagado ou movido.", "err"); return; }
        try { await core.reimport(h.id); toast("Importado na comp", "ok"); } catch (e) { toast(e.message, "err"); }
      };
      grid.appendChild(c);
    });
  }

  // ---------- início ----------
  loadCfgUI();
  fillModels();
  setTab(state.tab);
  requestAnimationFrame(moveInd);
  setTimeout(moveInd, 300);
  pollLayer(true);
  if (!cfg.falKey && cfg.provider === "fal") setTimeout(() => toast("Bem-vindo! Para animar e gerar, cole a chave do fal.ai em Config. Remover fundo local já funciona.", "info", 6500), 600);
  window.MF_UI = { setTab, toast, state };
})();
