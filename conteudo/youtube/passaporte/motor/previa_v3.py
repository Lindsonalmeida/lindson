"""Prévia das capas v3 (longos 10-12): as 3 novas, as 3 referências copiadas e a simulação da busca do YouTube
a 320 px (computador/tablet) e a 160 px (lista do celular). python3 previa_v3.py -> ../capas-longos-10-12/previa-v2.jpg"""
import os
from PIL import Image, ImageDraw, ImageFont
P = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'capas-longos-10-12')
F = '/usr/share/fonts/opentype/inter/Inter-'
def f(w, s): return ImageFont.truetype(F + w + '.otf', s)
NOVAS = [('capa-10.jpg', 'Os milagres de Jesus que ninguém te explicou'), ('capa-11.jpg', 'Êxodo explicado: por que Israel quis voltar?'),
         ('capa-12.jpg', 'Apóstolo Paulo: o perseguidor que mudou tudo')]
REFS = [('referencias/02-epic-history-mutiny-UK.jpg', '1 · Epic History (Reino Unido) → capa 10: palavra gigante no alto, figura na frente'),
        ('referencias/01-ciencia-todo-dia-flow-BR.jpg', '2 · Ciência Todo Dia (Brasil) → capa 11: close, palavra gigante de lado a lado'),
        ('referencias/03-johnny-harris-close-US.jpg', '3 · Johnny Harris (EUA) → capa 12: personagem de um lado, texto do outro')]
OUTRAS = ['referencias/07-historia-meia-hora-BR.jpg', 'referencias/09-fall-of-civilizations-UK.jpg', 'referencias/06-terra-x-zu-reich-DE.jpg']
W = 1920; BG = (15, 15, 15); TX = (241, 241, 241); CINZA = (170, 170, 170)
im = Image.new('RGB', (W, 2150), BG); d = ImageDraw.Draw(im)
def th(p, w): return Image.open(os.path.join(P, p)).convert('RGB').resize((w, w * 9 // 16), Image.LANCZOS)
d.text((40, 30), 'PASSAPORTE DA BÍBLIA · capas v3 dos longos 10, 11 e 12', font=f('Bold', 40), fill=TX)
x = 40
for a, t in NOVAS:
    im.paste(th(a, 600), (x, 100)); d.text((x, 450), t, font=f('SemiBold', 24), fill=TX); x += 620
d.text((40, 510), 'As 3 referências copiadas (capturas em referencias/)', font=f('Bold', 30), fill=TX)
x = 40
for a, t in REFS:
    im.paste(th(a, 600), (x, 560)); n, r = t.split(' → ')
    d.text((x, 902), n, font=f('SemiBold', 20), fill=TX); d.text((x, 930), r, font=f('Regular', 17), fill=CINZA); x += 620
# simulação da busca do YouTube, miniatura a 320 px de largura
y0 = 980; d.text((40, y0), 'Busca do YouTube · miniatura a 320 px', font=f('Bold', 30), fill=TX)
mix = [NOVAS[0][0], OUTRAS[0], NOVAS[1][0], OUTRAS[1], NOVAS[2][0], OUTRAS[2]]
nomes = [NOVAS[0][1], 'concorrente', NOVAS[1][1], 'concorrente', NOVAS[2][1], 'concorrente']
for i, (a, n) in enumerate(zip(mix, nomes)):
    x = 40 + (i % 3) * 620; y = y0 + 60 + (i // 3) * 210
    im.paste(th(a, 320), (x, y)); tt = n if n != 'concorrente' else 'Vídeo de outro canal'
    import textwrap; d.multiline_text((x + 336, y + 4), '\n'.join(textwrap.wrap(tt, 22)[:3]), font=f('SemiBold', 20), fill=TX, spacing=6)
    d.text((x + 336, y + 100), 'Passaporte da Bíblia' if n != 'concorrente' else 'canal de história', font=f('Regular', 17), fill=CINZA)
# lista do celular, miniatura a 160 px
y0 = 1500; d.text((40, y0), 'Lista do celular · miniatura a 160 px', font=f('Bold', 30), fill=TX)
for i, (a, n) in enumerate(zip(mix, nomes)):
    x = 40 + (i % 3) * 620; y = y0 + 60 + (i // 3) * 110
    im.paste(th(a, 160), (x, y)); d.text((x + 172, y + 4), (n if n != 'concorrente' else 'Vídeo de outro canal')[:30] + ('…' if len(n) > 30 and n != 'concorrente' else ''), font=f('SemiBold', 17), fill=TX)
    d.text((x + 172, y + 30), 'Passaporte da Bíblia' if n != 'concorrente' else 'canal de história', font=f('Regular', 15), fill=CINZA)
im = im.crop((0, 0, W, 1800)); im.save(os.path.join(P, 'previa-v2.jpg'), quality=88); print('ok')
