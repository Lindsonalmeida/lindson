# Saídas finais do perfil: avatar 1080 e 320 (PNG), prova de leitura a 40 px, e a prévia do perfil no celular. Paollo, 06/11/2026.
import os, glob
from PIL import Image, ImageDraw, ImageFont
D = os.path.dirname(os.path.abspath(__file__))
av = Image.open(os.path.join(D, 'avatar-1080.jpg')).convert('RGB')
av.save(os.path.join(D, 'avatar-1080.png')); av.resize((320, 320), Image.LANCZOS).save(os.path.join(D, 'avatar-320.png'))
# prova a 40 px: avatar e destaques cortados em círculo, no tamanho real do celular, em fundo branco e preto
def circ(im, t):
    im = im.resize((t, t), Image.LANCZOS); m = Image.new('L', (t * 4, t * 4), 0); ImageDraw.Draw(m).ellipse((0, 0, t * 4 - 1, t * 4 - 1), fill=255)
    out = Image.new('RGBA', (t, t)); out.paste(im, (0, 0), m.resize((t, t), Image.LANCZOS)); return out
dest = sorted(glob.glob(os.path.join(D, 'destaque-*.jpg')))
prova = Image.new('RGB', (760, 220), '#FFFFFF'); ImageDraw.Draw(prova).rectangle((0, 110, 760, 220), fill='#000000')
for row, y in enumerate((35, 145)):
    prova.paste(circ(av, 40), (20, y), circ(av, 40)); prova.paste(circ(av, 64), (80, y - 12), circ(av, 64))
    for i, f in enumerate(dest):
        im = Image.open(f).convert('RGB'); im = im.crop((0, 420, 1080, 1500))
        c = circ(im, 56); prova.paste(c, (170 + i * 95, y - 8), c)
prova.save(os.path.join(D, 'prova-40px.png'))
# prévia no celular
tela = Image.open(os.path.join(D, 'tela-perfil.jpg')).convert('RGB')
W, H = tela.size; b = 34; R = 120
fr = Image.new('RGB', (W + 2 * b + 220, H + 2 * b + 220), '#1E5B3B')
dr = ImageDraw.Draw(fr)
for x in range(0, fr.width, 60):
    for y in range(0, fr.height, 60):
        if (x // 60 + y // 60) % 2 == 0: dr.rectangle((x, y, x + 59, y + 59), fill='#1A5034')
ox, oy = 110, 110
dr.rounded_rectangle((ox + 18, oy + 22, ox + W + 2 * b + 18, oy + H + 2 * b + 22), R + b, fill='#0E2A1B')
dr.rounded_rectangle((ox, oy, ox + W + 2 * b, oy + H + 2 * b), R + b, fill='#141311')
m = Image.new('L', (W, H), 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, W - 1, H - 1), R, fill=255)
fr.paste(tela, (ox + b, oy + b), m)
dr.rounded_rectangle((ox + b + W // 2 - 110, oy + b + 18, ox + b + W // 2 + 110, oy + b + 62), 22, fill='#141311')
fr = fr.resize((fr.width * 2 // 3, fr.height * 2 // 3), Image.LANCZOS)
fr.save(os.path.join(D, 'previa-perfil.jpg'), quality=90)
print(fr.size)
