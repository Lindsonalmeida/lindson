// After Effects de mentira para rodar jsx/host.jsx em Node (vm) e testar o fluxo inteiro.
"use strict";
const fs = require("fs");
const path = require("path");
const vm = require("vm");

function createAE(opts = {}) {
  const log = { undoOpen: 0, undoGroups: 0, imports: [], frames: [] };
  let nextId = 100;

  class File {
    constructor(p) { this.fsName = String(p).replace(/\//g, path.sep); }
    get exists() { return fs.existsSync(this.fsName); }
  }
  class FolderItem { constructor(name) { this.name = name; this.id = nextId++; } }
  class SolidSource {}
  class FileSource { constructor(file, isStill) { this.file = file; this.isStill = isStill; this.conformFrameRate = 0; this.alphaMode = null; } }
  class FootageItem {
    constructor(file, o = {}) {
      this.id = nextId++; this.name = path.basename(file.fsName);
      this.mainSource = new FileSource(file, o.isStill !== false);
      this.width = o.width || 320; this.height = o.height || 240; this.frameRate = o.fps || 0; this.duration = o.duration || 0; this.hasVideo = true;
      this.parentFolder = null; this.sequence = !!o.sequence;
    }
  }
  class Property { constructor(v) { this.value = v; } setValue(v) { this.value = v; } }
  class AVLayer {
    constructor(comp, source, name) {
      this.comp = comp; this.source = source; this.name = name || (source ? source.name : "camada");
      this.enabled = true; this.hasVideo = true; this.adjustmentLayer = false; this.selected = false;
      this.inPoint = 0; this.outPoint = comp.duration; this.startTime = 0; this.stretch = 100; this.timeRemapEnabled = false;
      this._tr = { "ADBE Scale": new Property([100, 100]), "ADBE Position": new Property([0, 0]) };
    }
    get index() { return this.comp._layers.indexOf(this) + 1; }
    property(n) { if (n === "ADBE Transform Group") return { property: (k) => this._tr[k] }; return this._tr[n]; }
    duplicate() { const d = Object.assign(Object.create(Object.getPrototypeOf(this)), this); d._tr = JSON.parse(JSON.stringify(this._tr)); Object.keys(d._tr).forEach((k) => { d._tr[k] = new Property(this._tr[k].value); }); this.comp._layers.splice(this.index - 1, 0, d); return d; }
    replaceSource(item) { this.source = item; }
    moveBefore(other) { const L = this.comp._layers; L.splice(L.indexOf(this), 1); L.splice(L.indexOf(other), 0, this); }
  }
  class TextLayer extends AVLayer { constructor(comp, name) { super(comp, null, name); } }
  class ShapeLayer extends AVLayer {}
  class CompItem {
    constructor(o) {
      Object.assign(this, { id: nextId++, name: "Comp 1", width: 1920, height: 1080, frameRate: 30, duration: 10, time: 1 }, o);
      this._layers = [];
      const self = this;
      this.layers = { add(item) { const l = new AVLayer(self, item); self._layers.unshift(l); return l; } };
    }
    get numLayers() { return this._layers.length; }
    layer(i) { return this._layers[i - 1]; }
    get selectedLayers() { return this._layers.filter((l) => l.selected); }
    saveFrameToPng(t, file) {
      const visible = this._layers.filter((l) => l.enabled).map((l) => l.name);
      log.frames.push({ t, visible });
      // grava de forma "assíncrona", como o AE
      setTimeout(() => fs.copyFileSync(opts.framePng, file.fsName), 30);
    }
  }
  class ImportOptions { constructor(f) { this.file = f; this.sequence = false; this.forceAlphabetical = false; } }

  const items = [];
  const project = {
    activeItem: null,
    get numItems() { return items.length; },
    item(i) { return items[i - 1]; },
    items: { addFolder(n) { const f = new FolderItem(n); items.push(f); return f; } },
    importFile(io) {
      if (!io.file.exists) throw new Error("arquivo não existe");
      const ext = path.extname(io.file.fsName).toLowerCase();
      const isStill = /\.(png|jpe?g|webp)$/.test(ext) && !io.sequence;
      const it = new FootageItem(io.file, { isStill, sequence: io.sequence, width: 640, height: 360 });
      log.imports.push({ file: io.file.fsName, sequence: io.sequence });
      items.push(it); return it;
    },
  };
  const app = {
    project, version: "24.0.0", isoLanguage: "pt_BR",
    beginUndoGroup() { log.undoOpen++; log.undoGroups++; },
    endUndoGroup() { log.undoOpen--; },
  };

  const ctx = { app, File, CompItem, FolderItem, SolidSource, TextLayer, ShapeLayer, ImportOptions, AlphaMode: { STRAIGHT: 1 } };
  vm.createContext(ctx);
  vm.runInContext(fs.readFileSync(path.join(__dirname, "..", "jsx", "host.jsx"), "utf8"), ctx, { filename: "host.jsx" });

  function evalScript(code) {
    return new Promise((resolve) => setImmediate(() => {
      try { const r = vm.runInContext(code, ctx); resolve(r === undefined ? "undefined" : String(r)); } catch (e) { resolve("EvalScript error."); }
    }));
  }

  // monta cenas
  function newComp(o) { const c = new CompItem(o); items.push(c); project.activeItem = c; return c; }
  function addFootage(comp, file, o = {}) {
    const it = new FootageItem(new File(file), o); items.push(it);
    const l = new AVLayer(comp, it); comp._layers.unshift(l);
    Object.assign(l, o.layer || {});
    return l;
  }
  function addText(comp, name) { const l = new TextLayer(comp, name); comp._layers.unshift(l); return l; }
  function select(comp, layer) { comp._layers.forEach((l) => (l.selected = l === layer)); }

  return { evalScript, ctx, log, project, newComp, addFootage, addText, select, File };
}

module.exports = { createAE };
