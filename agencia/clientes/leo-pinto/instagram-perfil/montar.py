# Foto de perfil do Instagram · Vereador Leo Pinto (identidade v3 / feed v12). Conta Lindson, 02/11/2026.
import sys, math, numpy as np
from PIL import Image, ImageDraw, ImageFilter
D = sys.argv[1]; S = 1080
ROY, MAR, SOL, LAR, DEEP = (35,80,245), (5,49,110), (255,194,14), (255,122,26), (10,31,122)
p = Image.open(f'{D}/leo-23-original.png').convert('RGBA')
# posição do rosto no recorte (medida pela máscara: cabeça de x 413 a 899, topo do cabelo em y 30, queixo perto de 600)
fx, fy, fw, fh = 440, 170, 430, 430
def radial(c0, c1, c2, cx=.5, cy=.42):
    y, x = np.mgrid[0:S, 0:S]; r = np.hypot(x/S-cx, y/S-cy)/.75
    a = np.clip(r, 0, 1)[..., None]
    out = np.where(a < .45, np.array(c0)*(1-a/.45) + np.array(c1)*(a/.45), np.array(c1)*(1-(a-.45)/.55) + np.array(c2)*((a-.45)/.55))
    return Image.fromarray(out.astype('uint8')).convert('RGBA')
def raios(cx, cy, cor, op, n=24):
    L = Image.new('RGBA', (S, S)); d = ImageDraw.Draw(L)
    for i in range(n):
        a0 = 2*math.pi*i/n; a1 = a0 + math.pi/n*.55; R = S*1.2
        d.polygon([(cx, cy), (cx+R*math.cos(a0), cy+R*math.sin(a0)), (cx+R*math.cos(a1), cy+R*math.sin(a1))], fill=cor+(int(255*op),))
    m = Image.new('L', (S, S), 0); md = ImageDraw.Draw(m)
    for k in range(40): rr = S*.75*(1-k/40); md.ellipse([cx-rr, cy-rr, cx+rr, cy+rr], fill=int(255*k/40))
    L.putalpha(Image.fromarray(np.minimum(np.array(L.getchannel('A')), np.array(m))))
    return L
def montar(nome, fundo, raio_cor, raio_op, disco=None, anel=SOL):
    im = fundo.copy()
    hx, hy = S*.5, S*.36
    im.alpha_composite(raios(int(hx), int(hy), raio_cor, raio_op))
    if disco:
        d = Image.new('RGBA', (S, S)); dd = ImageDraw.Draw(d); r = S*.27
        for k in range(60):
            t = k/60; c = tuple(int(disco[0][i]*(1-t)+disco[1][i]*t) for i in range(3)); rr = r*(1-t*.98)
            dd.ellipse([hx-rr, hy-rr+20, hx+rr, hy+rr+20], fill=c+(255,))
        im.alpha_composite(d)
    if anel:  # anel fino na cor de destaque, atrás do corpo, dentro da área do círculo do Instagram
        a = Image.new('RGBA', (S, S)); ImageDraw.Draw(a).ellipse([22, 22, S-22, S-22], outline=anel+(255,), width=16); im.alpha_composite(a)
    esc = (S*.25)/fw  # rosto = 25% da largura: lê bem no círculo pequeno
    pp = p.resize((int(p.width*esc), int(p.height*esc)), Image.LANCZOS)
    ox, oy = int(hx-(fx+fw/2)*esc), int(hy-(fy+fh*.45)*esc)
    sombra = Image.new('RGBA', (S, S)); sh = Image.new('RGBA', pp.size, (2,20,64,150)); sh.putalpha(pp.getchannel('A').point(lambda a: a*.55))
    sombra.paste(sh, (ox+10, oy+14), sh); im.alpha_composite(sombra.filter(ImageFilter.GaussianBlur(18)))
    im.alpha_composite(pp, (max(ox,0), oy) if ox >= 0 else (0, oy), (0 if ox >= 0 else -ox, 0))
    im.convert('RGB').save(f'{D}/{nome}.jpg', quality=95)
    return im
A = montar('perfil-A-azul', radial((70,110,255), ROY, DEEP), (255,255,255), .16)
B = montar('perfil-B-marinho', radial((29,79,184), MAR, (2,20,64), cy=.3), SOL, .12, disco=((255,247,218), LAR))
C = montar('perfil-C-sol', radial((255,241,176), (255,210,58), LAR, cy=.36), (255,255,255), .30, anel=ROY)
# prévia: como aparece no Instagram (círculo grande, médio e pequeno)
pv = Image.new('RGB', (1500, 560), (250,250,250)); d = ImageDraw.Draw(pv)
for j, (im, rot) in enumerate([(A,'A · azul'), (B,'B · marinho com sol'), (C,'C · amarelo')]):
    x = 40 + j*490
    for sz, yy, dx in [(300, 60, 0), (110, 390, 40), (56, 418, 190)]:
        t = im.convert('RGB').resize((sz, sz), Image.LANCZOS); m = Image.new('L', (sz, sz), 0); ImageDraw.Draw(m).ellipse([0, 0, sz-1, sz-1], fill=255)
        pv.paste(t, (x+dx+(0 if sz == 300 else 0), yy), m)
    d.text((x+40, 20), rot, fill=(20,20,20))
pv.save(f'{D}/previa-perfil.jpg', quality=90)
print('ok', fx, fy, fw, fh)
