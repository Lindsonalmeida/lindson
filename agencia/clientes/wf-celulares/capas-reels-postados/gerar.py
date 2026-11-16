# WF · capas 9:16 dos 5 Reels já postados (41–45) · feed xadrez escuro/claro · conta Pedro · 16/11/2026
# Composição copiada: apple.com/iphone-17-pro (produto em palco, título gigante, preço embaixo) +
# Back Market (preço em bloco) + Swappie (fundo claro de vitrine). Texto e aparelho na área 4:5 (y 285–1635).
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance, ImageChops
D = os.path.dirname(os.path.abspath(__file__)); W = os.path.join(D, '..'); F = '/usr/share/fonts/opentype/inter/'
IMG = '/tmp/claude-0/-home-user/71909cf5-3742-5a17-8357-bcbb30dd10b8/images/'
fb = lambda s: ImageFont.truetype(F+'InterDisplay-Black.otf', s); fm = lambda s: ImageFont.truetype(F+'Inter-SemiBold.otf', s)
LUZ = (47, 107, 255)
ESC = dict(bg=(0, 0, 0), t1=(255, 255, 255), t2=(199, 201, 204), mu=(142, 138, 132), chip=(199, 201, 204), chipt=(0, 0, 0), logo='wf-logo-b-branca.png')
CLA = dict(bg=(236, 236, 238), t1=(0, 0, 0), t2=(58, 58, 60), mu=(110, 108, 104), chip=(0, 0, 0), chipt=(255, 255, 255), logo='wf-logo-b-preta.png')
C = [('41', '41.png', (27, 165, 467, 560), ESC, 'Lançamento · Azul', ['17 Pro Max', 'Azul 256GB'], 'R$ 6.700', 'garantia Apple até abril/2027'),
     ('42', '42.webp', (44, 170, 524, 670), CLA, 'Telão + bateria', ['iPhone', '14 Plus'], 'R$ 2.499', '128GB · procedência e garantia'),
     ('43', '43.webp', (33, 215, 513, 745), ESC, 'Pro Max por pouco', ['iPhone', '12 Pro Max'], 'R$ 2.199', 'tela gigante, câmera Pro'),
     ('44', '44.webp', (45, 115, 525, 630), CLA, 'Seminovo · Laranja', ['17 Pro Max', '256GB'], 'R$ 5.850', 'garantia da loja de 6 meses'),
     ('45', '45.png', (51, 135, 491, 570), ESC, 'Titânio · 48MP', ['15 Pro Max', '256GB'], 'R$ 3.900', 'garantia da loja de 6 meses')]
def mask_fade(w, h, top, bot, side):
    m = Image.new('L', (w, h), 255); d = ImageDraw.Draw(m)
    for y in range(h):
        v = min(1, y/top if top else 1, (h-1-y)/bot if bot else 1)
        d.line((0, y, w, y), fill=int(255*max(0, v)**1.4))
    s = Image.new('L', (w, h), 255); ds = ImageDraw.Draw(s)
    for x in range(w):
        v = min(1, x/side, (w-1-x)/side); ds.line((x, 0, x, h), fill=int(255*max(0, v)**1.4))
    return ImageChops.multiply(m, s)
out = []
for k, f, box, T, tag, tit, preco, sub in C:
    im = Image.new('RGB', (1080, 1920), T['bg'])
    fr = Image.open(IMG+f).convert('RGB').crop(box)
    r = 1180/fr.width; fr = fr.resize((1180, int(fr.height*r)), Image.LANCZOS)
    fr = ImageEnhance.Sharpness(fr.filter(ImageFilter.UnsharpMask(3, 120, 2))).enhance(1.2)
    if T is ESC: fr = ImageEnhance.Brightness(fr).enhance(.82)
    # fundo: o mesmo quadro bem desfocado e quase transparente, para a cor não ficar "dura"
    amb = fr.resize((1080, 1920)).filter(ImageFilter.GaussianBlur(60)); im = Image.blend(im, amb, .22 if T is ESC else .18)
    fh = min(fr.height, 1060); fr = fr.crop((0, 0, 1180, fh))
    im.paste(fr, (-50, 120), mask_fade(1180, fh, 300, 380, 110))
    d = ImageDraw.Draw(im, 'RGBA')
    # topo: logo com faixa suave
    sc = Image.new('L', (1, 560)); [sc.putpixel((0, y), int(230*min(1,(560-y)/330))) for y in range(560)]
    im.paste(Image.new('RGB', (1080, 560), T['bg']), (0, 0), sc.resize((1080, 560)))
    lg = Image.open(os.path.join(W, 'identidade/logo-b', T['logo'])).convert('RGBA'); lg.thumbnail((200, 120)); im.paste(lg, (80, 310), lg)
    d = ImageDraw.Draw(im, 'RGBA')
    f = fm(36); tw = d.textlength(tag.upper(), font=f); x2 = 1000; d.rounded_rectangle((x2-tw-50, 322, x2, 386), 32, fill=T['chip']); d.text((x2-tw-25, 333), tag.upper(), font=f, fill=T['chipt'])
    y = 1040
    for i, l in enumerate(tit):
        s = 180; ft = fb(s)
        while d.textlength(l, font=ft) > 920: s -= 4; ft = fb(s)
        d.text((76, y), l, font=ft, fill=T['t1'] if i == 0 else T['t2']); y += int(s*1.0)
    y += 22
    fp = fb(96); pw = d.textlength(preco, font=fp)
    d.rounded_rectangle((80, y, 80+pw+64, y+128), 22, fill=LUZ); d.text((112, y+8), preco, font=fp, fill=(255, 255, 255))
    d.text((82, y+145), sub, font=fm(40), fill=T['mu'])
    if d.textlength(sub, font=fm(34)) > 1000-(80+pw+96): pass
    p = os.path.join(D, f'capa-reel-{k}.jpg'); im.save(p, quality=92); out.append(p)
# prévia do feed 3 colunas (recorte 4:5 = y 285–1635), mais novo primeiro: 41..45 + capas anteriores
ant = [os.path.join(W, f'capas-reels/capa-reel-{i:02d}.jpg') for i in range(1, 7)]
lista = out + [a for a in ant if os.path.exists(a)]
cw, ch, g = 360, 450, 6; rows = (len(lista)+2)//3
pv = Image.new('RGB', (3*cw+4*g, rows*ch+(rows+1)*g+70), (255, 255, 255)); dp = ImageDraw.Draw(pv)
dp.text((g+4, 20), 'WF · prévia do feed (mais novo primeiro) · 5 novas + 6 capas anteriores', font=fm(24), fill=(0, 0, 0))
for i, p in enumerate(lista):
    t = Image.open(p).crop((0, 285, 1080, 1635)).resize((cw, ch), Image.LANCZOS)
    pv.paste(t, (g+(i % 3)*(cw+g), 70+g+(i//3)*(ch+g)))
pv.save(os.path.join(D, 'previa-feed.jpg'), quality=90); print('ok')
