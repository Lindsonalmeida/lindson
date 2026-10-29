#!/bin/bash
# Raposa e Leão — renderiza o lote com a voz humanizada e a conversa com o ouvinte.
# Uso: motor/lote.sh shorts [NN ...]   |   motor/lote.sh longos [NN ...]
# Sem números, faz todos. Os quadros temporários são apagados depois de cada vídeo.
cd "$(dirname "$0")"; S=/tmp/claude-0/-home-user/5acf6937-9ac6-56e0-bc29-78bef210dc8b/scratchpad
tipo=$1; shift
if [ "$tipo" = shorts ]; then
  for n in ${@:-$(ls ../shorts | grep -E '^[0-9]{2}$')}; do
    echo "== short $n $(date +%T)"; python3 short2.py $n 2>&1 | tail -1; rm -rf $S/rl_work_$n/fr
  done
else
  python3 conversa_longos.py "$@"
  for n in ${@:-01 02 03 04 05 06 07 08 09 10 11}; do
    echo "== longo $n $(date +%T)"; python3 longo2.py ../longos/$n 2>&1 | tail -1; rm -rf $S/lg_$n/fr
  done
fi
echo FIM
