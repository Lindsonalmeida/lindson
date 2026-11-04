# Motion v1 do Leo · recorte de uma foto do álbum (conta Pedro, 04/11/2026). Padrão de agencia/marca-lindson/ferramentas/recorte.py.
# Uso (1 foto por processo): python recortar.py <album>/f07.jpg <assets>/recortes/f07.png
# recorte BiRefNet portrait (padrão recorte.py) com a foto reduzida para 2600 px no lado maior
import sys, numpy as np
from PIL import Image, ImageEnhance
from rembg import remove, new_session
src, dst = sys.argv[1], sys.argv[2]
im = Image.open(src).convert('RGB'); im.thumbnail((2600, 2600), Image.LANCZOS)
ses = new_session('birefnet-portrait')
m = remove(im, session=ses, only_mask=True)
a = np.asarray(m).astype(float) / 255; a = np.clip((a - .35) / .4, 0, 1); a = a * a * (3 - 2 * a)
im = ImageEnhance.Color(im).enhance(1.12); im = ImageEnhance.Contrast(im).enhance(1.04)
rgba = im.copy(); rgba.putalpha(Image.fromarray((a * 255).astype('uint8')))
bb = rgba.getbbox(); print(src, im.size, 'bbox', bb)
rgba.save(dst)
