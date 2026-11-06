# Monta a prévia em grade (carrossel + post + stories): python3 previa.py <pasta privada>  -> <pasta>/previa.jpg (conta Leandro, 06/11/2026)
import sys
from PIL import Image, ImageDraw
D = sys.argv[1]
fe = [f'carrossel-{i}' for i in range(1, 8)] + ['post-perfil']
st = ['story-1', 'story-2']
w, h = 432, 540; hs = 768; g = 16
W = 4 * w + 5 * g + 2 * (h * 1080 // 1920 * 0 + 432) + 2 * g
sh = Image.new('RGB', (4 * (w + g) + g + 2 * (432 + g), 2 * (h + g) + g + 40), '#EFE7DC')
for k, n in enumerate(fe):
    sh.paste(Image.open(f'{D}/out/{n}.jpg').convert('RGB').resize((w, h)), (g + (k % 4) * (w + g), g + (k // 4) * (h + g)))
for k, n in enumerate(st):
    im = Image.open(f'{D}/out/{n}.jpg').convert('RGB').resize((432, hs))
    sh.paste(im, (g + 4 * (w + g) + k * (432 + g), g))
ImageDraw.Draw(sh).text((g, sh.height - 30), 'Dra. Jaci Cunha · Prova social Contorno facial masculino · carrossel 7 telas + post + 2 stories · 06/11/2026', fill='#5A4033')
sh.save(f'{D}/previa.jpg', quality=88)
print(sh.size)
