# Corta a arte-mestra (3104 px) nos 3 posts 1080×1350 e monta as prévias: grade do perfil (3:4) e feed.
import sys; from PIL import Image, ImageDraw
d = sys.argv[1]; P = Image.open(f'{d}/out/painel.png').convert('RGB'); B = 34
nomes = ['1-esquerda', '2-meio', '3-direita']; posts = []
for i, n in enumerate(nomes):
    c = P.crop((i*1012, 0, i*1012 + 1080, 1350)); c.save(f'{d}/out/leo-v13-{n}.jpg', quality=95); posts.append(c)
# grade: miniatura 3:4 central de cada post (1012×1350), vão de 3 px — 2 linhas: as 3 artes em cima, perfil abaixo vazio
tw = 400; th = int(tw*1350/1012); g = 4; G = Image.new('RGB', (3*tw + 2*g, th), (255, 255, 255))
for i, c in enumerate(posts): G.paste(c.crop((B, 0, B + 1012, 1350)).resize((tw, th), Image.LANCZOS), (i*(tw + g), 0))
G.save(f'{d}/out/previa-grade.jpg', quality=90)
