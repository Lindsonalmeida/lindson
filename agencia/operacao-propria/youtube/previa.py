# Prévia única do kit do YouTube (Paollo, conta Zuleide, 15/11/2026)
import os
from PIL import Image, ImageDraw
D = os.path.dirname(os.path.abspath(__file__)); P = lambda n: os.path.join(D, 'pecas', n)
W = Image.new('RGB', (2000, 2140), '#141311')
def put(n, box, xy, circ=False):
    im = Image.open(P(n)).convert('RGBA'); im.thumbnail(box, Image.LANCZOS)
    if circ:
        m = Image.new('L', im.size, 0); ImageDraw.Draw(m).ellipse((0, 0, *im.size), fill=255); im.putalpha(m)
    W.paste(im, xy, im)
put('banner-2560x1440.jpg', (1960, 1103), (20, 20))
put('perfil-800.jpg', (360, 360), (20, 1150), True)
put('marca-dagua-150.png', (150, 150), (125, 1560))
put('thumb-longo-1-dia-fraco.jpg', (760, 428), (420, 1150))
put('thumb-longo-2-taxa-do-app.jpg', (760, 428), (420, 1600))
put('capa-short-1080x1920.jpg', (520, 925), (1220, 1150))
W.save(os.path.join(D, 'previa.jpg'), quality=88)
