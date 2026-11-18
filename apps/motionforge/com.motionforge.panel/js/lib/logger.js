// Log diário em ~/MotionForge/logs/AAAA-MM-DD.log (nunca grava chaves).
"use strict";
const fs = require("fs");
const path = require("path");

let dir = null;
function init(logDir) { dir = logDir; try { fs.mkdirSync(dir, { recursive: true }); } catch (e) { /* ignora */ } }

function scrub(s) {
  return String(s)
    .replace(/(Key|Bearer|Token)\s+[A-Za-z0-9:_\-.]{8,}/g, "$1 ***")
    .replace(/("?(?:falKey|replicateKey|api[_-]?key|token)"?\s*[:=]\s*")[^"]+/gi, "$1***");
}

function pad(n) { return String(n).padStart(2, "0"); }

function write(level, msg, extra) {
  if (!dir) return;
  const d = new Date();
  const file = path.join(dir, `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())}.log`);
  let line = `${pad(d.getHours())}:${pad(d.getMinutes())}:${pad(d.getSeconds())} [${level}] ${msg}`;
  if (extra) line += " " + (extra instanceof Error ? (extra.stack || extra.message) + (extra.body ? " body=" + String(extra.body).slice(0, 500) : "") : JSON.stringify(extra));
  try { fs.appendFileSync(file, scrub(line) + "\n"); } catch (e) { /* ignora */ }
}

module.exports = {
  init,
  scrub,
  info: (m, x) => write("INFO", m, x),
  warn: (m, x) => write("WARN", m, x),
  error: (m, x) => write("ERRO", m, x),
  dir: () => dir,
};
