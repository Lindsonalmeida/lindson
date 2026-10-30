#!/bin/bash
# Monta a tela de login (login.html) com as fotos recortadas e as imagens dos clientes embutidas.
# As fotos ficam fora do Git em ../fotos (rec-68..72.webp, recortadas com rembg u2net_human_seg) e ../fotos/casos (prints).
cd "$(dirname "$0")"; python3 - <<'PY'
import base64, os
d = lambda p, t='webp': f'data:image/{t};base64,' + base64.b64encode(open(p, 'rb').read()).decode()
s = open('login.html').read()
for n in ['68', '69', '70', '71', '72']: s = s.replace(f'__F{n}__', d(f'../fotos/rec-{n}.webp'))
for k in ['rafael', 'sf', 'passaporte', 'raposa']: s = s.replace(f'__{k.upper()}__', d(f'../fotos/casos/{k}.webp'))
open('central-lindson.html', 'w').write(s); print('ok central-lindson.html', os.path.getsize('central-lindson.html') // 1024, 'KB')
PY
