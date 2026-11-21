# Compõe o painel 3240x1440 (render 3D + grão + frase contínua + assinatura plana) e corta os 3 posts.
# Modelo copiado: abertura Mova Street v5 (19/11, "ótimo"): frase na base dos 3, mesmo tamanho e altura,
# centralizada em cada post, letra clara peso 600 com sombra suave, assinatura pequena no alto do post 3.
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops
H = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.dirname(H)
F = os.path.join(H, '../../../v2/fase3/site/f/fraunces-sb.ttf')
LOGO = os.path.join(H, '../../../../marca-lindson/projeto-designer/v3/marca/logos/png/ouro/barzakh-horizontal-ouro.png')
FRASE = ['A PASSAGEM', 'DA SUA', 'MARCA.']
W, Hh = 3240, 1440
im = Image.open(os.path.join(H, 'cru.png')).convert('RGB').resize((W, Hh), Image.LANCZOS)
# profundidade de campo leve: desfoca o topo da parede e a frente do banco (gradiente)
bl = im.filter(ImageFilter.GaussianBlur(3.2)); dm = Image.new('L', (W, Hh), 0); dd = ImageDraw.Draw(dm)
for y in range(Hh):
    t = max(0, (260 - y) / 260) if y < 260 else max(0, (y - 1180) / 260)
    dd.line([(0, y), (W, y)], fill=int(255 * min(1, t)))
im = Image.composite(bl, im, dm)
v = Image.new('L', (W, Hh), 0); ImageDraw.Draw(v).ellipse([-W * .15, -Hh * .5, W * 1.15, Hh * 1.4], fill=255)
v = v.filter(ImageFilter.GaussianBlur(260)); im = Image.composite(im, ImageChops.multiply(im, Image.new('RGB', (W, Hh), (150, 150, 155))), v)
n = Image.effect_noise((W, Hh), 22).convert('RGB'); im = Image.blend(im, ImageChops.overlay(im, n), .12)
font = ImageFont.truetype(F, 66); TR = 14; Y = 1268
txt = Image.new('RGBA', (W, Hh), (0, 0, 0, 0)); d = ImageDraw.Draw(txt)
def largura(s): return sum(d.textlength(c, font=font) for c in s) + TR * (len(s) - 1)
for i, s in enumerate(FRASE):
    x = i * 1080 + (1080 - largura(s)) / 2
    for c in s: d.text((x, Y), c, font=font, fill=(240, 233, 220, 255)); x += d.textlength(c, font=font) + TR
sh = txt.split()[3].filter(ImageFilter.GaussianBlur(10)).point(lambda a: a * .7)
im.paste(Image.new('RGB', (W, Hh), (0, 0, 0)), (0, 6), sh); im.paste(txt, (0, 0), txt)
lg = Image.open(LOGO).convert('RGBA'); lg = lg.crop(lg.getbbox()); lw = 250; lg = lg.resize((lw, int(lg.height * lw / lg.width)), Image.LANCZOS)
im.paste(lg, (2160 + (1080 - lw) // 2, 120), lg)
im.save(os.path.join(OUT, 'painel.jpg'), quality=94)
for i in range(3): im.crop((i * 1080, 0, (i + 1) * 1080, Hh)).save(os.path.join(OUT, f'0{i + 1}.jpg'), quality=94)
print('ok')
