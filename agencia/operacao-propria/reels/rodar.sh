#!/bin/bash
# Renderiza a semana 1, um Reels por vez, com retomada (pula o que já tem mp4). Uso: setsid nohup bash rodar.sh > rodar.log 2>&1 &
cd "$(dirname "$0")/motor"; export REEL_LEVA=.. REEL_FOTOS=../fotos SSL_CERT_FILE=/root/.ccr/ca-bundle.crt
for i in $(seq ${ATE_INI:-1} ${ATE:-21}); do n=$(printf %02d $i)
  out=../semana-1/$n; [ -s $out/OT-$n.mp4 ] && continue
  echo "== OT-$n $(date +%T)"; python3 reel.py OT-$n --saida $out --work /tmp/reel-ot || echo "FALHOU OT-$n"
done; echo FIM
