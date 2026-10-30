#!/bin/bash
# Monta a tela de login (login.html) com as imagens embutidas. Imagens fora do Git em ../fotos:
#   heroi-70.webp (foto recortada, peito para cima), parede/tNN.webp (portfólio real), casos/*.webp (prints dos clientes e projetos)
cd "$(dirname "$0")"; python3 - <<'PY'
import base64, os
d = lambda p: 'data:image/webp;base64,' + base64.b64encode(open(p, 'rb').read()).decode()
s = open('login.html').read().replace('__HEROI__', d('../fotos/heroi-70.webp'))
for n in ['68', '69', '70', '71', '72']: s = s.replace(f'__D{n}__', d(f'../fotos/d-{n}.webp'))
for k in range(20): s = s.replace(f'__T{k:02d}__', d(f'../fotos/parede/t{k:02d}.webp'))
s = s.replace('__F68__', d('../fotos/rec-68.webp')).replace('__CINE__', d('../fotos/principal-cine.webp')).replace('__PROF__', d('../fotos/principal-prof.webp'))
for k in ['rafael', 'sf', 'passaporte', 'raposa']:
    s = s.replace(f'__{k.upper()}__', d(f'../fotos/casos/{k}.webp'))
    for i in range(1, 5):
        if os.path.exists(f'../fotos/casos/{k}-{i}.webp'): s = s.replace(f'__{k.upper()}{i}__', d(f'../fotos/casos/{k}-{i}.webp'))
open('central-lindson.html', 'w').write(s); print('ok', os.path.getsize('central-lindson.html') // 1024, 'KB')
PY
