// ExtendScript do After Effects.
// Refs: https://ae-scripting.docsforadobe.dev/
//  CompItem.saveFrameToPng: https://ae-scripting.docsforadobe.dev/item/compitem/
//  ImportOptions:           https://ae-scripting.docsforadobe.dev/other/importoptions/
//  LayerCollection.add:     https://ae-scripting.docsforadobe.dev/layer/layercollection/

function _comp() {
  var c = app.project.activeItem;
  return (c && c instanceof CompItem) ? c : null;
}

function mf_getSelectedLayerInfo() {
  var c = _comp();
  if (!c) return JSON.stringify({ error: "Abra uma composição." });
  if (c.selectedLayers.length === 0) return JSON.stringify({ error: "Selecione uma camada." });
  var l = c.selectedLayers[0], file = null;
  try {
    if (l.source && l.source.mainSource && l.source.mainSource.file && l.source.mainSource.isStill)
      file = l.source.mainSource.file.fsName;
  } catch (e) {}
  return JSON.stringify({ name: l.name, index: l.index, file: file,
    width: c.width, height: c.height, fps: c.frameRate, time: c.time });
}

function mf_exportFrame(outPath) {
  var c = _comp();
  if (!c) return "error: sem comp";
  var f = new File(outPath);
  c.saveFrameToPng(c.time, f);   // assíncrono no AE: o painel espera o arquivo aparecer
  return "ok";
}

function mf_importToComp(path) {
  var c = _comp();
  if (!c) return "error: sem comp";
  app.beginUndoGroup("MotionForge import");
  try {
    var item = app.project.importFile(new ImportOptions(new File(path)));
    var layer = c.layers.add(item);
    var sel = c.selectedLayers.length ? c.selectedLayers[0] : null;
    if (sel && sel !== layer) layer.moveBefore(sel);
    layer.startTime = c.time;
    // Ajusta à comp
    var s = Math.min(c.width / item.width, c.height / item.height) * 100;
    layer.property("Scale").setValue([s, s]);
    return layer.name;
  } catch (e) {
    return "error: " + e.toString();
  } finally {
    app.endUndoGroup();
  }
}
