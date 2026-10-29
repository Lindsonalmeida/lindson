# refaz todo o Passaporte antigo com a voz humanizada, conversa e cortes (marca .v2 quando pronto)
S=/tmp/claude-0/-home-user/5acf6937-9ac6-56e0-bc29-78bef210dc8b/scratchpad
cd /home/user/lindson/conteudo/youtube/passaporte/motor
while pgrep -f lote7.sh >/dev/null; do sleep 60; done
for v in pv-01 short-01 short-02 short-03 short-04 short-05 short-06 short-07 short-08 short-09 short-10 short-11 short-12 short-13 short-14 short-15 short-16 short-17 short-18 short-19 short-20 longo-01 longo-02 longo-03 longo-04; do
  [ -f ../videos/$v.v2 ] && continue
  echo "== $v $(date +%T)"
  [ -f $S/pv/$v/.v2ini ] || { rm -rf $S/pv/$v/fr; mkdir -p $S/pv/$v; touch $S/pv/$v/.v2ini; }
  RETOMAR=1 python3 pintura.py ../pintura.json $v 2>&1 | grep -v '^$' | tail -1
  [ -s ../videos/$v.mp4 ] || { echo "FALHOU $v"; continue; }
  d=$(ffprobe -v error -show_entries format=duration -of csv=p=0 ../videos/$v.mp4)
  case $v in longo-*) br=$(python3 -c "print(int(19*8*1024/$d-90))"); sc="-vf scale=1280:720"; ab=80k;; *) br=$(python3 -c "print(min(2600,int(19*8*1024/$d-170)))"); sc=""; ab=160k;; esac
  ffmpeg -y -loglevel error -i ../videos/$v.mp4 $sc -c:v libx264 -b:v ${br}k -pass 1 -passlogfile $S/pl$v -an -f null /dev/null && \
  ffmpeg -y -loglevel error -i ../videos/$v.mp4 $sc -c:v libx264 -b:v ${br}k -pass 2 -passlogfile $S/pl$v -c:a aac -b:a $ab -movflags +faststart ../videos/$v-app.mp4 && touch ../videos/$v.v2 && ls -la ../videos/$v-app.mp4 && rm -rf $S/pv/$v/fr $S/pl$v*
done
echo FIM8
