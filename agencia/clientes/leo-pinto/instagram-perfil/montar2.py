# Foto de perfil v2 do Instagram · Vereador Leo Pinto: foto leo-14 (busto), fundo laranja com degradê amarelo (sol), sem raios.
# Uso: python3 montar2.py <pasta com leo-14-original.png>. Conta Lindson, 02/11/2026.
import sys, numpy as np
from PIL import Image, ImageFilter
D = sys.argv[1]; S = 1080
p = Image.open(f'{D}/leo-14-original.png').convert('RGBA')
HX = 850  # centro da cabeça no recorte (medido pela máscara)
def fundo(cy, raio):
    y, x = np.mgrid[0:S, 0:S]; r = np.clip(np.hypot(x-S/2, y-cy)/(S*raio), 0, 1)
    pts = [(0, (255,214,60)), (.28, (255,180,20)), (.55, (255,122,26)), (.8, (240,96,16)), (1, (214,72,10))]  # luz → amarelo → laranja
    out = np.zeros((S, S, 3))
    for (a0, c0), (a1, c1) in zip(pts, pts[1:]):
        m = (r >= a0) & (r <= a1); t = ((r-a0)/(a1-a0))[m][:, None]
        out[m] = np.array(c0)*(1-t) + np.array(c1)*t
    return Image.fromarray(out.astype('uint8')).convert('RGBA')
def montar(nome, esc, cy, raio):
    im = fundo(cy, raio)
    pp = p.resize((int(p.width*esc), int(p.height*esc)), Image.LANCZOS)
    ox, oy = int(S/2 - HX*esc), S - pp.height
    sh = Image.new('RGBA', (S, S)); sombra = Image.new('RGBA', pp.size, (120,40,0,0)); sombra.putalpha(pp.getchannel('A').point(lambda a: int(a*.35)))
    sh.paste(sombra, (ox+8, oy+12), sombra); im.alpha_composite(sh.filter(ImageFilter.GaussianBlur(22)))
    lay = Image.new('RGBA', (S, S)); lay.paste(pp, (ox, oy), pp); im.alpha_composite(lay)
    im.convert('RGB').save(f'{D}/{nome}.jpg', quality=95); return im
A = montar('perfil-v2-sol', .62, 360, .9)
B = montar('perfil-v2-sol-aberto', .56, 380, .95)
from PIL import ImageDraw
pv = Image.new('RGB', (1000, 520), (250,250,250))
for j, im in enumerate([A, B]):
    x = 40 + j*490
    for sz, xx, yy in [(320, x, 30), (110, x+30, 380), (56, x+190, 408)]:
        t = im.convert('RGB').resize((sz, sz), Image.LANCZOS); m = Image.new('L', (sz, sz), 0); ImageDraw.Draw(m).ellipse([0, 0, sz-1, sz-1], fill=255); pv.paste(t, (xx, yy), m)
pv.save(f'{D}/previa-perfil-v2.jpg', quality=90); print('ok')
