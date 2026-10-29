#!/bin/bash
# Monta a tela de login com a foto embutida (a foto fica fora do Git, em ../fotos/68.jpg)
cd "$(dirname "$0")"; python3 - <<'PY'
from PIL import Image, ImageEnhance; import base64, io
im = Image.open('../fotos/68.jpg').convert('RGB'); im = im.crop((0, 0, im.width, int(im.height * .80))); im.thumbnail((720, 1100))
b = io.BytesIO(); ImageEnhance.Contrast(im).enhance(1.08).save(b, 'JPEG', quality=80)
open('central-lindson.html', 'w').write(open('login.html').read().replace('__FOTO__', 'data:image/jpeg;base64,' + base64.b64encode(b.getvalue()).decode()))
print('ok central-lindson.html')
PY
