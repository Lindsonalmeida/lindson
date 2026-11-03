# Prévia do feed da Desentupidora SF na ordem de postagem (mais novo no topo à esquerda), miniaturas 3:4 como o Instagram
# mostra, com a tag da linha editorial e a data embaixo de cada post (só na prévia; a tag não vai na arte publicada).
# Cópia adaptada do feed.py do Leo (instagram-v14-datas). Uso: python3 feed.py .
import sys, json
from PIL import Image, ImageDraw, ImageFont
d = sys.argv[1] if len(sys.argv) > 1 else '.'
T = json.load(open(f'{d}/textos.json'))
F = lambda s, b=True: ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans' + ('-Bold' if b else '') + '.ttf', s)
COR = {'Socorro rápido': (255, 106, 0), 'Evite o prejuízo': (200, 40, 40), 'Bastidores do serviço': (10, 42, 110), 'Fala com a gente': (29, 95, 208)}
posts = [(f'{d}/{T[k]["arquivo"]}', T[k]['linha'], T[k]['data']) for k in ('p1', 'p2', 'p3', 'p4')]
grade = list(reversed(posts))  # mais novo primeiro
tw, th, g, lab = 330, 440, 4, 64
linhas = (len(grade) + 2) // 3
G = Image.new('RGB', (3*tw + 2*g, linhas*(th + lab)), (255, 255, 255)); dr = ImageDraw.Draw(G)
for i in range(linhas*3):
    x, y = (i % 3)*(tw + g), (i // 3)*(th + lab)
    if i >= len(grade):  # espaço do que já está no perfil
        dr.rectangle((x, y, x+tw, y+th), fill=(236, 240, 247)); dr.text((x+92, y+th//2-10), 'posts atuais', font=F(18, False), fill=(140, 150, 170)); continue
    f, linha, data = grade[i]
    im = Image.open(f).convert('RGB'); cw = int(1350*3/4); im = im.crop(((1080-cw)//2, 0, (1080-cw)//2 + cw, 1350)).resize((tw, th), Image.LANCZOS)
    G.paste(im, (x, y)); c = COR.get(linha, (90, 90, 90))
    dr.rounded_rectangle((x+8, y+th+10, x+8+dr.textlength(linha, F(17))+20, y+th+38), 8, fill=c)
    dr.text((x+18, y+th+13), linha, font=F(17), fill='white'); dr.text((x+10, y+th+42), data, font=F(15, False), fill=(80, 80, 80))
G.save(f'{d}/previa-feed.jpg', quality=90)
print('previa-feed.jpg ok')
