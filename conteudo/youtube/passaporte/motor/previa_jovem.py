"""Prévia das capas v3 "jovens": cada capa ao lado da referência copiada e o teste a 160 px (lista do celular).
python3 previa_jovem.py -> ../capas-longos-10-12/previa-v3.jpg"""
import os
from PIL import Image, ImageDraw, ImageFont
P = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'capas-longos-10-12')
F = '/usr/share/fonts/opentype/inter/Inter-'
def f(w, s): return ImageFont.truetype(F + w + '.otf', s)
PARES = [('capa-10.jpg', 'referencias/02-epic-history-mutiny-UK.jpg', 'Capa 10 · Milagres', 'copia Epic History "MUTINY" (Reino Unido)', 'Os milagres de Jesus que ninguém te explicou'),
         ('capa-11.jpg', 'referencias/01-ciencia-todo-dia-flow-BR.jpg', 'Capa 11 · Êxodo', 'copia Ciência Todo Dia "FLOW" (Brasil)', 'Êxodo explicado: por que Israel quis voltar?'),
         ('capa-12.jpg', 'referencias/03-johnny-harris-close-US.jpg', 'Capa 12 · Paulo', 'copia Johnny Harris (EUA)', 'Apóstolo Paulo: o perseguidor que mudou tudo')]
OUTRAS = ['referencias/07-historia-meia-hora-BR.jpg', 'referencias/05-epic-history-waterloo-UK.jpg', 'referencias/06-terra-x-zu-reich-DE.jpg']
W = 1920; BG = (15, 15, 15); TX = (241, 241, 241); CZ = (170, 170, 170)
im = Image.new('RGB', (W, 2300), BG); d = ImageDraw.Draw(im)
def th(p, w): return Image.open(os.path.join(P, p)).convert('RGB').resize((w, w * 9 // 16), Image.LANCZOS)
d.text((40, 28), 'PASSAPORTE DA BÍBLIA · capas v3 (estilo das referências, mais jovem)', font=f('Bold', 38), fill=TX)
d.text((40, 76), 'à esquerda a nossa capa, à direita a referência copiada', font=f('Regular', 22), fill=CZ)
y = 120
for a, r, t, c, _ in PARES:
    im.paste(th(a, 880), (40, y)); im.paste(th(r, 880), (1000, y))
    d.text((40, y + 500), t, font=f('Bold', 24), fill=TX); d.text((1000, y + 500), c, font=f('Regular', 22), fill=CZ); y += 560
d.text((40, y + 10), 'Teste a 160 px (lista do celular)', font=f('Bold', 30), fill=TX)
y += 70
for i, ((a, _, _, _, tt), o) in enumerate(zip(PARES, OUTRAS)):
    x = 40 + i * 620
    im.paste(th(a, 160), (x, y)); d.text((x + 172, y + 4), tt[:30] + '…', font=f('SemiBold', 17), fill=TX); d.text((x + 172, y + 30), 'Passaporte da Bíblia', font=f('Regular', 15), fill=CZ)
    im.paste(th(o, 160), (x, y + 110)); d.text((x + 172, y + 114), 'Vídeo de outro canal', font=f('SemiBold', 17), fill=TX); d.text((x + 172, y + 140), 'canal de história', font=f('Regular', 15), fill=CZ)
im.crop((0, 0, W, y + 220)).save(os.path.join(P, 'previa-v3.jpg'), quality=88); print('ok')
