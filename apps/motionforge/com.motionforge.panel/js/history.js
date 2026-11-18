// Histórico de tudo o que o painel gerou (~/MotionForge/history.json).
"use strict";
const fs = require("fs");
const path = require("path");
const S = require("./settings");

const MAX = 500;

function list() {
  let arr = [];
  try { arr = JSON.parse(fs.readFileSync(S.paths.history, "utf8")); } catch (e) { arr = []; }
  return (Array.isArray(arr) ? arr : []).filter((h) => h && h.file);
}

function write(arr) {
  const tmp = S.paths.history + ".tmp";
  fs.writeFileSync(tmp, JSON.stringify(arr.slice(0, MAX), null, 1));
  fs.renameSync(tmp, S.paths.history);
}

function add(entry) {
  const e = Object.assign({ id: Date.now().toString(36) + Math.random().toString(36).slice(2, 6), createdAt: new Date().toISOString() }, entry);
  const arr = list();
  arr.unshift(e);
  write(arr);
  return e;
}

function update(id, patch) {
  const arr = list();
  const i = arr.findIndex((h) => h.id === id);
  if (i >= 0) { arr[i] = Object.assign({}, arr[i], patch); write(arr); return arr[i]; }
  return null;
}

function remove(id) { write(list().filter((h) => h.id !== id)); }

function exists(h) { try { return fs.existsSync(h.file); } catch (e) { return false; } }

function thumbPath(h) { return path.join(S.paths.thumbs, h.id + ".jpg"); }

module.exports = { list, add, update, remove, exists, thumbPath };
