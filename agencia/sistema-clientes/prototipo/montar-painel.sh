#!/bin/bash
# Monta o painel com as imagens do bloco de promoção (foto do Lindson fora do Git em ../fotos; portfólio em ../fotos/casos)
cd "$(dirname "$0")"; python3 - <<'PY'
import base64
d = lambda p: 'data:image/webp;base64,' + base64.b64encode(open(p, 'rb').read()).decode()
s = open('painel.html').read().replace('__CINE__', d('../fotos/principal-cine.webp'))
for k in ['rafael', 'sf', 'passaporte', 'raposa']: s = s.replace(f'__{k.upper()}1__', d(f'../fotos/casos/{k}-1.webp' if k in ('passaporte','raposa') else f'../fotos/casos/{k}.webp'))
open('painel-montado.html', 'w').write(s); print('ok painel-montado.html')
PY
