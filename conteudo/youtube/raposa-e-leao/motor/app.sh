#!/bin/bash
# Versão para baixar pelo app: mesmo vídeo em 1080p, 2 passes, cabe em 19 MB. Uso: app.sh <NN> <saida>
V=$(dirname "$0")/../longos/$1/video.mp4; O=$2/$1.mp4; L=$2/log$1
D=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$V")
BR=$(python3 -c "print(int((18.5e6*8/$D-80000)/1000))")
ffmpeg -loglevel error -y -i "$V" -c:v libx264 -b:v ${BR}k -pass 1 -passlogfile $L -preset slow -tune animation -an -f mp4 /dev/null
ffmpeg -loglevel error -y -i "$V" -c:v libx264 -b:v ${BR}k -pass 2 -passlogfile $L -preset slow -tune animation -c:a aac -b:a 80k -movflags +faststart "$O"
rm -f $L*; ls -la "$O"
