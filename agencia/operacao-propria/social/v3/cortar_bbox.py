# Gera versões recortadas no contorno (bbox) dos recortes em quadro cheio, para posicionar livre. (Paollo, 06/11/2026)
import os, glob
from PIL import Image
D = os.path.dirname(os.path.abspath(__file__))
for f in glob.glob(os.path.join(D, 'recortes', '*.webp')):
    if f.endswith('-bb.webp'): continue
    im = Image.open(f); bb = im.getbbox(); c = im.crop(bb)
    c.save(f[:-5] + '-bb.webp', quality=92, method=6)
    print(os.path.basename(f), im.size, bb, c.size)
