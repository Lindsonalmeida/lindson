#!/bin/bash
# Renderiza um vídeo por vez (máquina frágil): espera ffmpeg de outro agente terminar
cd "$(dirname "$0")"; for n in "$@"; do while pgrep -x ffmpeg >/dev/null; do sleep 10; done
NODE_PATH=$(npm root -g) node render.js $n && SSL_CERT_FILE=/root/.ccr/ca-bundle.crt python3 montar.py $n && rm -rf tmp/v$n; done; echo FIM
