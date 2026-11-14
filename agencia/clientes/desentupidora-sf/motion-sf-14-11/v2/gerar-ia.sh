#!/bin/bash
# 3 filas em paralelo no Stable Horde (processamento remoto, não pesa na máquina)
cd "$(dirname "$0")"; fila(){ awk -v k=$1 'NR%3==k' lista.tsv | while IFS=$'\t' read -r n p; do [ -f ia/$n.webp ] && continue; timeout 1200 python3 horde.py ia/$n.webp "$p" || echo "ERRO $n"; done; }
fila 0 & fila 1 & fila 2 & wait; echo FIM
