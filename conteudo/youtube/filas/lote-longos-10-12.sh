#!/bin/bash
# Fila dos longos 10, 11 e 12 do Passaporte (conta Zuleide, Peter, 09/11/2026).
# Um longo por vez, desacoplado, com prioridade baixa (nice) para não atrapalhar outros trabalhos da CPU.
# Disparar:   setsid nohup bash conteudo/youtube/filas/lote-longos-10-12.sh > <scratchpad>/lote-10-12.log 2>&1 < /dev/null &
# Acompanhar: tail -f <scratchpad>/lote-10-12.log <scratchpad>/render-longo-1*.log   (uma linha 'bloco k' a cada 1.800 quadros = 1 min de vídeo)
# Retomar:    rodar de novo o mesmo comando (RETOMAR=1 + BLOCO: continua do último bloco pronto; vídeo pronto tem o marcador videos/<id>.v2).
S=${S:-/tmp/claude-0/-home-user/90050ae9-6cfe-5d35-9728-99eedbe6040e/scratchpad}
VELHO=/tmp/claude-0/-home-user/5acf6937-9ac6-56e0-bc29-78bef210dc8b
mkdir -p $S/old-scratch/modelos $VELHO; [ -e $VELHO/scratchpad ] || ln -sfn $S/old-scratch $VELHO/scratchpad
# o edge-tts usa o certifi: nesta nuvem ele precisa do certificado do proxy
mkdir -p $S/sc; [ -f $S/sc/sitecustomize.py ] || printf "import certifi\ncertifi.where = lambda: '/root/.ccr/ca-bundle.crt'\n" > $S/sc/sitecustomize.py
export PYTHONPATH=$S/sc${PYTHONPATH:+:$PYTHONPATH}
cd /home/user/lindson/conteudo/youtube/passaporte/motor
while pgrep -f "^python3 pintura.py" >/dev/null; do sleep 60; done   # nunca dois renders juntos       
for v in ${IDS:-longo-10 longo-11 longo-12}; do
  [ -f ../videos/$v.v2 ] && { echo "== $v já pronto"; continue; }
  echo "== $v $(date +%T)"
  for t in 1 2 3; do
    RETOMAR=1 BLOCO=1800 CRF=${CRF:-22} nice -n 10 python3 pintura.py ../pintura.json $v >> $S/render-$v.log 2>&1; tail -2 $S/render-$v.log
    [ -s ../videos/$v.mp4 ] && break
    echo "tentativa $t falhou, repetindo em 60 s"; sleep 60
  done
  [ -s ../videos/$v.mp4 ] || { echo "FALHOU $v"; continue; }
  d=$(ffprobe -v error -show_entries format=duration -of csv=p=0 ../videos/$v.mp4)
  br=$(python3 -c "print(int(19*8*1024/$d-90))")
  nice -n 10 ffmpeg -y -loglevel error -i ../videos/$v.mp4 -vf scale=1280:720 -c:v libx264 -b:v ${br}k -pass 1 -passlogfile $S/pl$v -an -f null /dev/null && \
  nice -n 10 ffmpeg -y -loglevel error -i ../videos/$v.mp4 -vf scale=1280:720 -c:v libx264 -b:v ${br}k -pass 2 -passlogfile $S/pl$v -c:a aac -b:a 80k -movflags +faststart ../videos/$v-app.mp4 && \
  touch ../videos/$v.v2 && ls -la ../videos/$v.mp4 ../videos/$v-app.mp4 && echo "duração $d s" && rm -rf $S/old-scratch/pv/$v/fr $S/old-scratch/pv/$v/blk $S/pl$v*
done
echo FIM-10-12
