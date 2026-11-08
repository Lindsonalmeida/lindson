# Prévias do kit v5 (conta Zuleide, 08/11/2026): feed 3×4 na ordem de grid.txt (o Reels entra pelo recorte central 4:5),
# carrossel em tira (c1–c7) e stories lado a lado.
import os
from PIL import Image
D = os.path.dirname(os.path.abspath(__file__)); J = lambda n: os.path.join(D, 'pecas', n + '.jpg')
def abre(n):
    im = Image.open(J(n))
    return im.crop((0, 285, 1080, 1635)) if im.height == 1920 else im
ids = open(os.path.join(D, 'grid.txt')).read().split()
W, H, G = 360, 450, 6
s = Image.new('RGB', (W * 3 + G * 2, H * 4 + G * 3), '#fff')
for i, n in enumerate(ids):
    s.paste(abre(n).resize((W, H), Image.LANCZOS), ((i % 3) * (W + G), (i // 3) * (H + G)))
s.save(os.path.join(D, 'previa-feed.jpg'), quality=90)
c = [f'c{k}' for k in range(1, 8)]
cs = sorted(f[:-4] for f in os.listdir(os.path.join(D, 'pecas')) if f[:3] in [x + '-' for x in c])
t = Image.new('RGB', (len(cs) * (W + G) - G, H), '#fff')
for i, n in enumerate(cs): t.paste(Image.open(J(n)).resize((W, H), Image.LANCZOS), (i * (W + G), 0))
t.save(os.path.join(D, 'previa-carrossel.jpg'), quality=90)
st = ['p03-reels-pizza-no-ar'] + sorted(f[:-4] for f in os.listdir(os.path.join(D, 'pecas')) if f.startswith('s'))
u = Image.new('RGB', (len(st) * (W + G) - G, 640), '#fff')
for i, n in enumerate(st): u.paste(Image.open(J(n)).resize((W, 640), Image.LANCZOS), (i * (W + G), 0))
u.save(os.path.join(D, 'previa-stories.jpg'), quality=90)
print(len(ids), len(cs), len(st))
