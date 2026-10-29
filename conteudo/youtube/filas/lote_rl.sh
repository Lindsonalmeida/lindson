# Raposa e Leão: renderiza os longos 12-16 depois que a fila do Passaporte (lote7) terminar
S=/tmp/claude-0/-home-user/5acf6937-9ac6-56e0-bc29-78bef210dc8b/scratchpad
R=/home/user/lindson/conteudo/youtube/raposa-e-leao
cd /home/user/lindson/conteudo/youtube/passaporte/motor
while pgrep -f lote7.sh >/dev/null; do sleep 60; done
for v in longo-12 longo-13 longo-14 longo-15 longo-16; do
  [ -s $R/videos/$v-app.mp4 ] && continue
  until [ -s $R/roteiros/$v.json ]; do sleep 60; done
  python3 $R/motor/lote_rl.py >/dev/null
  echo "== $v $(date +%T)"
  RETOMAR=1 python3 pintura.py $R/pintura.json $v 2>&1 | grep -v '^$' | tail -2
  [ -s $R/videos/$v.mp4 ] || { echo "FALHOU $v"; continue; }
  d=$(ffprobe -v error -show_entries format=duration -of csv=p=0 $R/videos/$v.mp4); br=$(python3 -c "print(int(19*8*1024/$d-90))")
  ffmpeg -y -loglevel error -i $R/videos/$v.mp4 -vf scale=1280:720 -c:v libx264 -b:v ${br}k -pass 1 -passlogfile $S/pl$v -an -f null /dev/null && \
  ffmpeg -y -loglevel error -i $R/videos/$v.mp4 -vf scale=1280:720 -c:v libx264 -b:v ${br}k -pass 2 -passlogfile $S/pl$v -c:a aac -b:a 80k -movflags +faststart $R/videos/$v-app.mp4 && ls -la $R/videos/$v-app.mp4 && rm -rf $S/pv/$v/fr $S/pl$v*
done
echo FIM_RL
