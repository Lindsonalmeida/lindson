// MotionForge · ExtendScript do After Effects (ES3: sem let/const, sem JSON nativo).
// Refs: https://ae-scripting.docsforadobe.dev/
//  CompItem.saveFrameToPng · ImportOptions (sequence, forceAlphabetical) · AVLayer.replaceSource
//  Layer.duplicate · FootageSource.conformFrameRate · app.beginUndoGroup
// Toda alteração fica num grupo de desfazer "MotionForge" (Ctrl+Z desfaz de uma vez).

// ---------- JSON mínimo (o ExtendScript do AE não tem JSON nativo) ----------
function _q(s) {
  s = String(s);
  var out = '"', i, c, code;
  for (i = 0; i < s.length; i++) {
    c = s.charAt(i); code = s.charCodeAt(i);
    if (c === '"' || c === "\\") out += "\\" + c;
    else if (c === "\n") out += "\\n";
    else if (c === "\r") out += "\\r";
    else if (c === "\t") out += "\\t";
    else if (code < 32) out += "\\u" + ("000" + code.toString(16)).slice(-4);
    else out += c;
  }
  return out + '"';
}
function _json(v) {
  var t = typeof v, parts = [], k, i;
  if (v === null || v === undefined) return "null";
  if (t === "number") return isFinite(v) ? String(v) : "null";
  if (t === "boolean") return v ? "true" : "false";
  if (t === "string") return _q(v);
  if (v instanceof Array) { for (i = 0; i < v.length; i++) parts.push(_json(v[i])); return "[" + parts.join(",") + "]"; }
  for (k in v) { if (v.hasOwnProperty(k) && typeof v[k] !== "function") parts.push(_q(k) + ":" + _json(v[k])); }
  return "{" + parts.join(",") + "}";
}
function _err(msg) { return _json({ error: String(msg) }); }

// ---------- utilidades ----------
function _comp() {
  var c = app.project ? app.project.activeItem : null;
  return (c && c instanceof CompItem) ? c : null;
}
function _compById(id) {
  if (!id) return _comp();
  var i, it;
  for (i = 1; i <= app.project.numItems; i++) { it = app.project.item(i); if (it.id === id && it instanceof CompItem) return it; }
  return null;
}
function _folder() {
  var i, it;
  for (i = 1; i <= app.project.numItems; i++) { it = app.project.item(i); if (it instanceof FolderItem && it.name === "MotionForge") return it; }
  return app.project.items.addFolder("MotionForge");
}
var IMG_RE = /\.(png|jpe?g|webp|bmp|tiff?)$/i;

function mf_ping() { return _json({ ok: true, version: app.version, lang: app.isoLanguage }); }

function mf_getCompSettings() {
  var c = _comp();
  if (!c) return _err("Abra uma composição.");
  return _json({ id: c.id, name: c.name, width: c.width, height: c.height, fps: c.frameRate, duration: c.duration, time: c.time, pixelAspect: c.pixelAspect });
}

function mf_getSelectedLayerInfo() {
  var c = _comp();
  if (!c) return _err("Abra uma composição e selecione uma camada.");
  var comp = { id: c.id, name: c.name, width: c.width, height: c.height, fps: c.frameRate, duration: c.duration, time: c.time };
  if (c.selectedLayers.length === 0) return _json({ error: "Selecione uma camada na composição.", comp: comp, noLayer: true });
  var l = c.selectedLayers[0];
  var r = { name: l.name, index: l.index, comp: comp, kind: "outra", file: null, isStill: false, isVideo: false,
    inPoint: l.inPoint, outPoint: l.outPoint, startTime: l.startTime, stretch: 100, timeRemap: false, srcWidth: 0, srcHeight: 0, srcFps: 0, srcDuration: 0, enabled: l.enabled };
  try {
    r.stretch = l.stretch;
    r.timeRemap = !!l.timeRemapEnabled;
    if (l.source) {
      r.srcWidth = l.source.width; r.srcHeight = l.source.height;
      if (l.source instanceof CompItem) r.kind = "precomp";
      else if (l.source.mainSource) {
        var ms = l.source.mainSource;
        if (ms instanceof SolidSource) r.kind = "sólido";
        else if (ms.file) {
          r.isStill = ms.isStill;
          r.kind = ms.isStill ? "imagem" : "vídeo";
          r.isVideo = !ms.isStill && l.source.hasVideo;
          r.file = ms.file.fsName;
          r.srcFps = l.source.frameRate; r.srcDuration = l.source.duration;
          if (ms.isStill && !IMG_RE.test(r.file)) { r.fileUnsupported = true; }
        }
      }
    } else if (l instanceof TextLayer) r.kind = "texto";
    else if (l instanceof ShapeLayer) r.kind = "forma";
  } catch (e) { r.warn = e.toString(); }
  return _json(r);
}

// Deixa só a camada visível para exportar o frame. Devolve o estado anterior para restaurar.
function mf_isolate(compId, index) {
  var c = _compById(compId);
  if (!c) return _err("Composição não encontrada.");
  var off = [], i, l, self = c.layer(index), wasOn = self.enabled;
  for (i = 1; i <= c.numLayers; i++) {
    l = c.layer(i);
    if (i !== index && l.enabled && l.hasVideo && !l.adjustmentLayer) { try { l.enabled = false; off.push(i); } catch (e) {} }
  }
  if (!wasOn) self.enabled = true;
  return _json({ off: off, selfWasOn: wasOn });
}
function mf_restore(compId, index, offCsv, selfWasOn) {
  var c = _compById(compId);
  if (!c) return "ok";
  var parts = String(offCsv || "").split(","), i;
  for (i = 0; i < parts.length; i++) { if (parts[i]) { try { c.layer(parseInt(parts[i], 10)).enabled = true; } catch (e) {} } }
  if (!selfWasOn) { try { c.layer(index).enabled = false; } catch (e) {} }
  return "ok";
}

// saveFrameToPng grava o arquivo de forma assíncrona: o painel espera o arquivo aparecer.
function mf_exportFrame(outPath, compId, time) {
  var c = _compById(compId);
  if (!c) return _err("Composição não encontrada.");
  try { c.saveFrameToPng(time === undefined || time === null ? c.time : time, new File(outPath)); }
  catch (e) { return _err(e.toString()); }
  return _json({ ok: true });
}

// Importa e posiciona. mode:
//  "dup"     duplica a camada (mantém transformações, keyframes e efeitos) e troca a fonte
//  "replace" troca a fonte da própria camada
//  "comp"    nova camada do tamanho da comp, acima da selecionada, mesmo in/out
//  "fit"     nova camada no tempo atual, ajustada para caber na comp (resultados de IA)
//  "project" só importa no painel Projeto
function mf_place(filePath, mode, compId, layerIndex, isSeq, fps, offset, hideOriginal, label) {
  var f = new File(filePath);
  if (!f.exists) return _err("Arquivo não encontrado: " + filePath);
  app.beginUndoGroup("MotionForge");
  try {
    var io = new ImportOptions(f);
    if (isSeq) { io.sequence = true; io.forceAlphabetical = true; }
    var item = app.project.importFile(io);
    try { item.parentFolder = _folder(); } catch (e0) {}
    if (label) { try { item.name = label; } catch (e1) {} }
    if (isSeq && fps > 0) { try { item.mainSource.conformFrameRate = fps; } catch (e2) {} }
    if (/\.png$/i.test(filePath)) { try { item.mainSource.alphaMode = AlphaMode.STRAIGHT; } catch (e3) {} }

    var c = _compById(compId);
    if (!c || mode === "project") return _json({ ok: true, item: item.name, layer: null });
    var sel = null;
    if (layerIndex > 0 && layerIndex <= c.numLayers) sel = c.layer(layerIndex);
    var layer;

    if ((mode === "dup" || mode === "replace") && sel && sel.source) {
      layer = mode === "dup" ? sel.duplicate() : sel;
      layer.replaceSource(item, false);
      if (offset) layer.startTime = sel.startTime + offset;
      if (mode === "dup") {
        layer.name = sel.name + " · sem fundo";
        try { layer.inPoint = sel.inPoint; layer.outPoint = sel.outPoint; } catch (e4) {}
        if (hideOriginal) sel.enabled = false;
      }
    } else {
      layer = c.layers.add(item);
      if (sel) layer.moveBefore(sel);
      if (mode === "comp") {
        if (sel) { layer.startTime = sel.inPoint; try { layer.outPoint = sel.outPoint; } catch (e5) {} }
        else layer.startTime = c.time;
        if (hideOriginal && sel) sel.enabled = false;
      } else {
        layer.startTime = c.time;
        var s = Math.min(c.width / item.width, c.height / item.height) * 100;
        if (Math.abs(s - 100) > 0.01) layer.property("ADBE Transform Group").property("ADBE Scale").setValue([s, s]);
      }
      layer.property("ADBE Transform Group").property("ADBE Position").setValue([c.width / 2, c.height / 2]);
    }
    try { var k; for (k = 1; k <= c.numLayers; k++) c.layer(k).selected = false; layer.selected = true; } catch (e6) {}
    return _json({ ok: true, item: item.name, layer: layer.name, index: layer.index });
  } catch (e) {
    return _err(e.toString());
  } finally {
    app.endUndoGroup();
  }
}

// Compatibilidade com o MVP.
function mf_importToComp(path) { var c = _comp(); var sel = c && c.selectedLayers.length ? c.selectedLayers[0].index : 0; return mf_place(path, "fit", c ? c.id : 0, sel, false, 0, 0, false, ""); }
function mf_exportFrameLegacy(outPath) { return mf_exportFrame(outPath, 0); }
