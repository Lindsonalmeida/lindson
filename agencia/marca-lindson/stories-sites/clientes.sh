#!/bin/bash
# Um vídeo por cliente (conta Pedro, 10/11/2026): gera, põe voz/SFX/trilha e dá o nome final. Uso: bash clientes.sh <id> [id ...]
#   11 rafael · 12 sf · 13 tribuna · 14 realtime · 15 jaci      Precisa: VOZ (pasta com sNN.wav do narra.py), MUSICAS, QUADROS
set -e
D=$(cd "$(dirname "$0")" && pwd); PRIV=${PRIV:-/home/user/centrallindsonalmeida}; OUT=$PRIV/painel/admin-rede/stories-sites/clientes
declare -A NOME=([11]=rafael [12]=sf [13]=tribuna [14]=realtime [15]=jaci)
mkdir -p "$OUT/guia"
for s in "$@"; do
  SAIDA=$OUT node "$D/gerar.js" "$s"
  python3 "$D/audio.py" "$OUT" "$VOZ" "$MUSICAS" "$QUADROS" "$s"
  n=${NOME[$s]}
  mv -f "$OUT/s$s.mp4" "$OUT/cliente-$n.mp4"; mv -f "$OUT/s$s.png" "$OUT/cliente-$n.png"; mv -f "$OUT/guia/s$s.png" "$OUT/guia/cliente-$n.png"
  rm -rf "$QUADROS/s$s"
  echo "pronto: cliente-$n"
done
