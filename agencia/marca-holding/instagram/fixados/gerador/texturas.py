# Fixados Barzakh (conta Leandro, 21/11/2026): texturas oficiais para o render 3D (trilho A).
# Logo = PNG ouro oficial, sem redesenho; vira "hot stamping" (mapa de metal) dentro do render.
import os
from PIL import Image, ImageDraw, ImageFilter, ImageChops
H = os.path.dirname(os.path.abspath(__file__)); O = os.path.join(H, 'tex')
L = os.path.join(H, '../../../../marca-lindson/projeto-designer/v3/marca/logos/png/ouro')
def logo(n, w):
    im = Image.open(f'{L}/barzakh-{n}-ouro.png').convert('RGBA'); bb = im.getbbox(); im = im.crop(bb)
    return im.resize((w, int(im.height * w / im.width)), Image.LANCZOS)
def face(name, size, base, lg, w, cy, glow=None):
    W, Hh = size; im = Image.new('RGB', size, base)
    if glow:
        g = Image.new('L', size, 0); r = int(W * .32)
        ImageDraw.Draw(g).ellipse([W//2-r, int(Hh*cy)-r, W//2+r, int(Hh*cy)+r], fill=150)
        g = g.filter(ImageFilter.GaussianBlur(r * .45)); im = Image.composite(Image.new('RGB', size, glow), im, g)
    l = logo(lg, w); x, y = (W - l.width)//2, int(Hh*cy) - l.height//2
    im.paste(l, (x, y), l)
    n = Image.effect_noise(size, 30).convert('L'); im = Image.blend(im, Image.merge('RGB', [ImageChops.add(c, n, 1, -128) for c in im.split()]), .25)
    mr = Image.new('RGB', size, (0, 215, 0)); a = l.split()[3]
    mr.paste(Image.new('RGB', l.size, (0, 55, 255)), (x, y), a)
    im.save(f'{O}/{name}.png'); mr.save(f'{O}/{name}_mr.png')
os.makedirs(O, exist_ok=True)
face('placa', (1600, 1920), (40, 40, 43), 'vertical', 900, .47, glow=(43, 58, 143))
face('cartao', (1100, 640), (15, 15, 16), 'simbolo', 300, .5)
face('caderno', (1000, 1400), (14, 14, 15), 'vertical', 520, .5)
face('timbrado', (1240, 1754), (236, 231, 221), 'horizontal', 380, .1)
face('envelope', (1600, 800), (17, 17, 18), 'horizontal', 520, .55)
face('caixa', (1200, 1200), (13, 13, 14), 'simbolo', 520, .5)
face('ecobag', (1000, 1150), (15, 15, 16), 'vertical', 520, .52)
print('ok')
