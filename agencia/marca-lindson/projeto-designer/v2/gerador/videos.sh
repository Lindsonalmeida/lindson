#!/bin/bash
# Projeto Designer v2 (conta Leandro, 16/11/2026): 3 pins de vídeo 1080x1920, 12,6 s, zoom lento e fusão.
# Trilha Mixkit #623 e whoosh Mixkit #1489 (licença Mixkit, sem crédito obrigatório), de agencia/clientes/wf-celulares/video-processo/som/.
# Uso: bash videos.sh <mockups> <saida> <pasta_som>
MK=$1; OUT=$2; S=$3; mkdir -p $OUT
for k in realtime oregano curso; do
  in=""; f=""; i=0
  for c in cartoes papelaria embalagem; do
    in="$in -loop 1 -t 4.6 -i $MK/$k-$c-r.jpg"
    f="$f[$i:v]scale=1280:1920,crop=1080:1920,zoompan=z='1+0.0008*on':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=138:s=1080x1920:fps=30,setsar=1[v$i];"; i=$((i+1))
  done
  ffmpeg -y -loglevel error $in -i $S/trilha.mp3 -i $S/whoosh.mp3 -filter_complex "$f[v0][v1]xfade=transition=fade:duration=0.6:offset=4[x1];[x1][v2]xfade=transition=fade:duration=0.6:offset=8,format=yuv420p[v];[3:a]atrim=0:12.6,afade=t=in:d=0.5,afade=t=out:st=11.4:d=1.2,volume=0.7[m];[4:a]adelay=3800|3800,volume=0.5[w1];[4:a]adelay=7800|7800,volume=0.5[w2];[m][w1][w2]amix=inputs=3:normalize=0[a]" \
    -map "[v]" -map "[a]" -t 12.6 -c:v libx264 -crf 22 -preset medium -c:a aac -b:a 128k -movflags +faststart $OUT/video-$k.mp4 && echo "$k ok"
done
