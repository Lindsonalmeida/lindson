#!/usr/bin/env bash
# Monta o MotionForge Web dentro do clone da Central (CentralLindsonALmeida), em /painel/motionforge (só admin).
# Uso: web/montar.sh [/caminho/para/centrallindsonalmeida]   (padrão: ../../../../centrallindsonalmeida)
set -euo pipefail
AQUI="$(cd "$(dirname "$0")" && pwd)"
PANEL="$AQUI/../com.motionforge.panel"
CENTRAL="${1:-$AQUI/../../../../centrallindsonalmeida}"
[[ -d "$CENTRAL/painel" ]] || { echo "Central não encontrada em $CENTRAL"; exit 1; }
OUT="$CENTRAL/painel/motionforge"
mkdir -p "$OUT"
cp "$AQUI/index.html" "$CENTRAL/painel/motionforge.html"
cp "$AQUI/app.js" "$AQUI/fal-web.js" "$AQUI/bg-worker.js" "$AQUI/style.css" "$OUT/"
cp "$PANEL/js/models.js" "$OUT/models.js"
cp "$PANEL/css/fonts/Inter.woff2" "$OUT/Inter.woff2"
cp "$PANEL/icons/icon-dark@2x.png" "$OUT/icon.png"
echo "Montado em $CENTRAL/painel/motionforge.html + $OUT/"
