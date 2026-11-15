#!/bin/bash
# Semana 2 (OT-22..30), um por vez, espera ffmpeg livre (máquina compartilhada). Uso: setsid nohup bash rodar2.sh > rodar2.log 2>&1 &
cd "$(dirname "$0")/motor"; export REEL_LEVA=.. REEL_FOTOS=../fotos SSL_CERT_FILE=/root/.ccr/ca-bundle.crt
for i in $(seq ${ATE_INI:-22} ${ATE:-30}); do n=$(printf %02d $i)
  out=../semana-2/$n; [ -s $out/OT-$n.mp4 ] && continue
  while pgrep -x ffmpeg >/dev/null; do sleep 20; done
  echo "== OT-$n $(date +%T)"; python3 reel.py OT-$n --saida $out --work /tmp/reel-ot2 || echo "FALHOU OT-$n"
done; echo FIM
