S=/tmp/claude-0/-home-user/5acf6937-9ac6-56e0-bc29-78bef210dc8b/scratchpad
cd /home/user/lindson/conteudo/youtube/passaporte/motor
for v in longo-09 longo-05 longo-06 longo-07 longo-08; do
  [ -s ../videos/$v-app.mp4 ] && continue
  until [ -s ../roteiros/$v.json ]; do sleep 30; done
  python3 lote3.py >/dev/null
  echo "== $v $(date +%T)"
  RETOMAR=1 python3 pintura.py ../pintura.json $v 2>&1 | grep -v '^$' | tail -2
  [ -s ../videos/$v.mp4 ] || { echo "FALHOU $v"; continue; }
  d=$(ffprobe -v error -show_entries format=duration -of csv=p=0 ../videos/$v.mp4); br=$(python3 -c "print(int(19*8*1024/$d-90))")
  ffmpeg -y -loglevel error -i ../videos/$v.mp4 -vf scale=1280:720 -c:v libx264 -b:v ${br}k -pass 1 -passlogfile $S/pl$v -an -f null /dev/null && \
  ffmpeg -y -loglevel error -i ../videos/$v.mp4 -vf scale=1280:720 -c:v libx264 -b:v ${br}k -pass 2 -passlogfile $S/pl$v -c:a aac -b:a 80k -movflags +faststart ../videos/$v-app.mp4 && ls -la ../videos/$v-app.mp4 && rm -rf $S/pv/$v/fr $S/pl$v*
done
echo FIM7
