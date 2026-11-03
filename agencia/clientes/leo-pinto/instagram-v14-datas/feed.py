# Prévia do feed do perfil em ordem de postagem (mais novo no topo à esquerda), miniaturas 3:4 como o Instagram mostra,
# com a tag da linha editorial e a data abaixo de cada post (só na prévia; a tag não vai na arte publicada).
import sys, json; from PIL import Image, ImageDraw, ImageFont
d, v13 = sys.argv[1], sys.argv[2]; T = json.load(open(f'{d}/textos.json'))
F = lambda s, b=True: ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans' + ('-Bold' if b else '') + '.ttf', s)
COR = {'Leo na rua': (255,122,26), 'Mandato que entrega': (35,80,245), 'Voz do povo': (37,180,110), 'Nossa Baixada': (8,150,200),
       'Leo de perto': (230,60,120), 'A cidade que eu sonho': (140,90,230), 'Apresentação': (5,49,110)}
posts = [(f'{v13}/leo-v13-1-esquerda.jpg', 'Apresentação', 'apresentação 3/3'), (f'{v13}/leo-v13-2-meio.jpg', 'Apresentação', 'apresentação 2/3'), (f'{v13}/leo-v13-3-direita.jpg', 'Apresentação', 'apresentação 1/3')]
novos = [(f'{d}/out/{k}.jpg', T[p]['linha'], T[p]['data']) for p, k in [('p1','p1-15-11'),('p2','p2-20-11'),('p3','p3-11-12'),('p4','p4-25-12'),('p5','p5-31-12'),('p6','p6-01-01')]]
grade = list(reversed(novos)) + posts  # mais novo primeiro
tw, th, g, lab = 330, 440, 4, 64
G = Image.new('RGB', (3*tw + 2*g, (len(grade)//3)*(th + lab)), (255,255,255)); dr = ImageDraw.Draw(G)
for i, (f, linha, data) in enumerate(grade):
    im = Image.open(f).convert('RGB'); cw = int(1350*3/4); im = im.crop(((1080-cw)//2, 0, (1080-cw)//2 + cw, 1350)).resize((tw, th), Image.LANCZOS)
    x, y = (i % 3)*(tw + g), (i // 3)*(th + lab); G.paste(im, (x, y))
    c = COR.get(linha, (90,90,90)); dr.rounded_rectangle((x+8, y+th+10, x+8+dr.textlength(linha, F(17))+20, y+th+38), 8, fill=c)
    dr.text((x+18, y+th+13), linha, font=F(17), fill='white'); dr.text((x+10, y+th+42), data, font=F(15, False), fill=(80,80,80))
G.save(f'{d}/out/previa-feed.jpg', quality=90)
