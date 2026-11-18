#!/bin/bash
# Versão do painel (720p, até ~19 MB, dois passos) de cada longo v2. Uso: painel.sh <pasta_trabalho> <faixa> <destino>
W=$1; k=$2; DST=$3; v=$W/pagode-fiado-$k-v2.mp4
d=$(ffprobe -v error -show_entries format=duration -of csv=p=0 $v)
br=$(python3 -c "print(int(18.6*8*1024/$d-160))")
nice -n 10 ffmpeg -y -v error -i $v -vf scale=1280:720:flags=lanczos -c:v libx264 -preset slow -b:v ${br}k -pass 1 -passlogfile $W/pl$k -an -f null /dev/null && \
nice -n 10 ffmpeg -y -v error -i $v -vf scale=1280:720:flags=lanczos -c:v libx264 -preset slow -b:v ${br}k -pass 2 -passlogfile $W/pl$k -c:a aac -b:a 160k -movflags +faststart $DST/pagode-fiado-$k-v2.mp4 && rm -f $W/pl$k* && ls -la $DST/pagode-fiado-$k-v2.mp4
