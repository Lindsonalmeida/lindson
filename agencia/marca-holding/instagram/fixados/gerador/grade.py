# Simulação do perfil @barzakhstudio: avatar e destaques do kit + 3 fixados no topo da grade 3:4.
import os
from PIL import Image, ImageDraw, ImageFont
H = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.dirname(H); K = os.path.join(H, '../../../kit-contas/01-instagram')
FS = os.path.join(H, '../../../v2/fase3/site/f/fraunces-sb.ttf'); SANS = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'; SB = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
W = 1080; G = 3; cw = (W - 2 * G) // 3; ch = int(cw * 4 / 3)
Hh = 760 + ch + 40; im = Image.new('RGB', (W, Hh), (12, 12, 13)); d = ImageDraw.Draw(im)
f = lambda p, s: ImageFont.truetype(p, s)
d.text((40, 40), 'barzakhstudio', font=f(SB, 40), fill=(240, 240, 240))
av = Image.open(f'{K}/foto-de-perfil.png').convert('RGBA').resize((190, 190)); m = Image.new('L', (190, 190), 0); ImageDraw.Draw(m).ellipse([0, 0, 189, 189], fill=255)
im.paste(av, (40, 120), m)
for i, (n, l) in enumerate([('3', 'posts'), ('—', 'seguidores'), ('—', 'seguindo')]):
    x = 330 + i * 250; d.text((x, 160), n, font=f(SB, 38), fill=(240, 240, 240)); d.text((x, 212), l, font=f(SANS, 26), fill=(200, 200, 200))
y = 340
for s, fo, c in [('Barzakh · um estúdio Al Kántara', SB, (240, 240, 240)), ('A passagem da sua marca.', SANS, (225, 225, 225)),
                 ('Identidade visual, embalagem e site', SANS, (225, 225, 225)), ('São Luís · atende todo o Brasil', SANS, (225, 225, 225)), ('↓ Fale com o estúdio', SANS, (150, 170, 230))]:
    d.text((40, y), s, font=f(fo, 27), fill=c); y += 38
dest = sorted(x for x in os.listdir(f'{K}/destaques') if 'circulo' in x); nomes = ['Cases', 'Processo', 'Pacotes', 'Bastidor', 'Dúvidas', 'Contato']
for i, x in enumerate(dest[:6]):
    c = Image.open(f'{K}/destaques/{x}').convert('RGBA').resize((130, 130)); mm = Image.new('L', (130, 130), 0); ImageDraw.Draw(mm).ellipse([0, 0, 129, 129], fill=255)
    cx = 40 + i * 172; d.ellipse([cx - 6, 554, cx + 136, 696], outline=(90, 90, 95), width=3); im.paste(c, (cx, 560), mm)
    t = nomes[i]; d.text((cx + 65 - d.textlength(t, font=f(SANS, 22)) / 2, 706), t, font=f(SANS, 22), fill=(220, 220, 220))
for i in range(3):
    p = Image.open(os.path.join(OUT, f'0{i + 1}.jpg')).resize((cw, ch), Image.LANCZOS); x = i * (cw + G); im.paste(p, (x, 760))
    d.polygon([(x + cw - 40, 778), (x + cw - 22, 778), (x + cw - 26, 800), (x + cw - 36, 800)], fill=(255, 255, 255))  # alfinete de fixado
    d.line([(x + cw - 31, 800), (x + cw - 31, 812)], fill=(255, 255, 255), width=3)
im.save(os.path.join(OUT, 'grade.jpg'), quality=92); print('ok')
