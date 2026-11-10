# Recorte de foto de produto com fundo branco liso: alfa por inundação a partir das bordas (conta Leandro, 10/11/2026)
import sys
from PIL import Image, ImageDraw, ImageFilter
im = Image.open(sys.argv[1]).convert('RGB'); w, h = im.size
m = im.convert('L').point(lambda v: 255 if v > 238 else 0)  # quase branco
seed = m.copy()
for p in [(0, 0), (w-1, 0), (0, h-1), (w-1, h-1)]: ImageDraw.floodfill(seed, p, 128)
a = seed.point(lambda v: 0 if v == 128 else 255).filter(ImageFilter.GaussianBlur(1.2))
out = im.convert('RGBA'); out.putalpha(a); out.save(sys.argv[2])
