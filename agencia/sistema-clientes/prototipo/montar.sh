#!/bin/bash
# Monta a tela de login com a foto recortada (sem fundo) embutida. A foto fica fora do Git: ../fotos/recorte-68.webp
# (recorte feito com rembg, modelo u2net_human_seg, a partir de ../fotos/68.jpg)
cd "$(dirname "$0")"; python3 -c "
import base64
s=open('login.html').read();b=base64.b64encode(open('../fotos/recorte-68.webp','rb').read()).decode()
open('central-lindson.html','w').write(s.replace('__FOTO__','data:image/webp;base64,'+b));print('ok central-lindson.html')"
