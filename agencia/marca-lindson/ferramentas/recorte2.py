# Recorte v2 do Lindson para o site: BiRefNet portrait em resolução cheia + filtro guiado + descontaminação de cor (pymatting)
# Uso: python recorte2.py foto.jpg saida.webp [corte_baixo 0-1]
import sys, numpy as np, cv2
from PIL import Image
from rembg import remove, new_session
from pymatting import estimate_foreground_ml

src, out = sys.argv[1], sys.argv[2]
corte = float(sys.argv[3]) if len(sys.argv) > 3 else 1.0
im = Image.open(src).convert('RGB')
ses = new_session('birefnet-portrait')
m = np.asarray(remove(im, session=ses, only_mask=True)).astype(np.float32) / 255
I = np.asarray(im).astype(np.float32) / 255
# filtro guiado: a borda da máscara segue as bordas reais da foto (cabelo, ombro)
g = cv2.ximgproc.guidedFilter(guide=(I * 255).astype(np.uint8), src=(m * 255).astype(np.uint8), radius=3, eps=60).astype(np.float32) / 255
a = np.clip((g - 0.12) / 0.76, 0, 1)
a = a * a * (3 - 2 * a)
# tira 1 px da borda (sem franja) mantendo o cabelo macio
nucleo = cv2.erode((a > 0.98).astype(np.uint8), np.ones((3, 3), np.uint8))
a = np.where(nucleo > 0, 1.0, a)
a = cv2.GaussianBlur(a, (0, 0), 0.6)
a[a < 0.03] = 0
# descontaminação: cor da frente estimada sem o fundo bege/cinza
F = estimate_foreground_ml(I.astype(np.float64), a.astype(np.float64))
F = np.clip(F, 0, 1)
rgba = np.dstack([F, a])
rgba = (rgba * 255 + 0.5).astype(np.uint8)
res = Image.fromarray(rgba, 'RGBA')
if corte >= 0:
    bb = res.getbbox(); res = res.crop(bb)
if 0 <= corte < 1: res = res.crop((0, 0, res.width, int(res.height * corte)))
res.save(out, 'WEBP', quality=90, method=6)
res.save(out.replace('.webp', '.png'))
print(out, res.size)
