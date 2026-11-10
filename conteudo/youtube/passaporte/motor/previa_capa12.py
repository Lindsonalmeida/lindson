"""Prévia das 3 opções da capa 12 ao lado das capas 10 e 11 aprovadas, com o teste a 160 px.
python3 previa_capa12.py -> ../capas-longos-10-12/previa-capa12-opcoes.jpg"""
import os
from PIL import Image, ImageDraw, ImageFont
P = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'capas-longos-10-12')
F = '/usr/share/fonts/opentype/inter/Inter-'
def f(w, s): return ImageFont.truetype(F + w + '.otf', s)
def th(p, w): return Image.open(os.path.join(P, p)).convert('RGB').resize((w, w * 9 // 16), Image.LANCZOS)
W = 1920; TX = (241, 241, 241); CZ = (170, 170, 170)
im = Image.new('RGB', (W, 1500), (15, 15, 15)); d = ImageDraw.Draw(im)
d.text((40, 26), 'PASSAPORTE DA BÍBLIA · capa 12 (Paulo): 3 opções', font=f('Bold', 38), fill=TX)
d.text((40, 74), 'em cima as aprovadas 10 e 11; embaixo as 3 opções da 12 (Caravaggio, "Conversão de São Paulo", domínio público)', font=f('Regular', 22), fill=CZ)
for i, (a, t) in enumerate([('capa-10.jpg', 'APROVADA · 10 · MILAGRE?'), ('capa-11.jpg', 'APROVADA · 11 · VOLTAR?')]):
    im.paste(th(a, 900), (40 + i * 940, 120)); d.text((40 + i * 940, 632), t, font=f('Bold', 22), fill=(120, 230, 140))
OP = [('capa-12a.jpg', 'Opção A · CEGO? · copia Epic History "MUTINY"'), ('capa-12b.jpg', 'Opção B · ELE CAIU · copia Ciência Todo Dia "FLOW"'),
      ('capa-12c.jpg', 'Opção C · MUDOU · copia Johnny Harris')]
for i, (a, t) in enumerate(OP):
    im.paste(th(a, 600), (40 + i * 620, 690)); d.text((40 + i * 620, 1035), t, font=f('SemiBold', 20), fill=TX)
y = 1100; d.text((40, y), 'Teste a 160 px (lista do celular)', font=f('Bold', 28), fill=TX); y += 54
for i, (a, t) in enumerate([('capa-10.jpg', 'Os milagres de Jesus que ninguém…'), ('capa-11.jpg', 'Êxodo explicado: por que Israel…')] + [(o[0], 'Apóstolo Paulo: o perseguidor… (' + o[1][6] + ')') for o in OP]):
    x = 40 + (i % 3) * 620; yy = y + (i // 3) * 110
    im.paste(th(a, 160), (x, yy)); d.text((x + 172, yy + 4), t, font=f('SemiBold', 17), fill=TX); d.text((x + 172, yy + 30), 'Passaporte da Bíblia', font=f('Regular', 15), fill=CZ)
im.crop((0, 0, W, y + 230)).save(os.path.join(P, 'previa-capa12-opcoes.jpg'), quality=88); print('ok')
