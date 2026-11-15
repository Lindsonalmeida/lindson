# Capas 9:16 dos Reels da WF no painel (motion-02 x5 + vídeo do processo), área segura 4:5 (y 285–1635) · conta Pedro · 15/11/2026
import os, subprocess
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
D = os.path.dirname(os.path.abspath(__file__)); W = os.path.join(D, '..'); F = '/usr/share/fonts/opentype/inter/'
fb = lambda s: ImageFont.truetype(F+'InterDisplay-Black.otf', s); fm = lambda s: ImageFont.truetype(F+'Inter-SemiBold.otf', s)
AZ, SI, CA, PR = (199,201,204), (199,201,204), (0,0,0), (142,138,132)
LUZ = (47,107,255)  # azul só como luz (identidade aprovada B: preto, grafite, titânio, prata, branco)
LOGO = Image.open(os.path.join(W, 'identidade/logo-b/wf-logo-b-branca.png')).convert('RGBA')
C = [('motion-02/wf-motion2-01-13-pro-max.mp4', 6.0, 'Oferta', ['iPhone 13', 'Pro Max'], 'por R$ 2.699'),
     ('motion-02/wf-motion2-02-15-pro-max.mp4', 6.0, 'POV', ['Entrei na WF', 'com R$ 3.950'], 'e saí com um 15 Pro Max'),
     ('motion-02/wf-motion2-03-12-pro-max.mp4', 6.0, 'Pare de rolar', ['12 Pro Max', 'R$ 2.299'], 'com laudo e garantia'),
     ('motion-02/wf-motion2-04-14-pro-max.mp4', 6.0, 'Seminovo', ['Medo de', 'seminovo?'], 'veja o Laudo WF'),
     ('motion-02/wf-motion2-05-17-pro-max-silver.mp4', 6.0, 'Baixou', ['17 Pro Max', 'Silver'], 'era R$ 6.499, agora R$ 6.399'),
     ('video-processo/wf-processo-60s.mp4', 20.0, 'Bastidores', ['A nova WF', 'em 1 minuto'], 'do perfil antigo à marca nova')]
out = []
FOTO = {1:'motion-01/img/13-graphite.png',2:'motion-01/img/15-hero.jpg',3:'motion-01/img/12-blue.jpg',4:'motion-01/img/14-black.png',5:'motion-01/img/17-silver.jpg'}
for i, (v, ss, tag, tit, sub) in enumerate(C, 1):
    fr = os.path.join(D, f'_f{i}.jpg'); subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', str(ss), '-i', os.path.join(W, v), '-frames:v', '1', '-q:v', '2', fr], check=True)
    im = Image.open(fr).convert('RGB').resize((1080, 1920)); os.remove(fr)
    ph = FOTO.get(i)
    if ph:
        p0 = Image.open(os.path.join(W, ph)).convert('RGB'); r = max(1080/p0.width, 1920/p0.height); p0 = p0.resize((int(p0.width*r)+1, int(p0.height*r)+1)); x = (p0.width-1080)//2; im = p0.crop((x, 0, x+1080, 1920))
        im = ImageEnhance.Brightness(im).enhance(.7)
    else: im = ImageEnhance.Brightness(im.filter(ImageFilter.GaussianBlur(14))).enhance(.45)
    g = Image.new('L', (1, 1920)); [g.putpixel((0, y), int(240*max(0, (y-650)/1270)**0.9)) for y in range(1920)]
    im = Image.composite(Image.new('RGB', im.size, (0,0,0)), im, g.resize(im.size))
    d = ImageDraw.Draw(im, 'RGBA')
    d.ellipse((620, 360, 1260, 1000), outline=LUZ+(150,), width=6)  # círculo da marca (memória do cliente)
    lg = LOGO.copy(); lg.thumbnail((220, 130)); im.paste(lg, (90, 340), lg)
    f = fm(40); tw = d.textlength(tag.upper(), font=f); d.rounded_rectangle((90, 980, 90+tw+52, 1050), 35, fill=SI); d.text((116, 992), tag.upper(), font=f, fill=CA)
    y = 1080
    for k, l in enumerate(tit):
        s = 150; ft = fb(s)
        while d.textlength(l, font=ft) > 900: s -= 6; ft = fb(s)
        d.text((86, y), l, font=ft, fill=(255,255,255) if k == 0 else AZ); y += int(s*1.02)
    d.text((90, y+20), sub, font=fm(46), fill=PR)
    d.rectangle((90, 1590, 330, 1598), fill=LUZ)
    p = os.path.join(D, f'capa-reel-{i:02d}.jpg'); im.save(p, quality=90); out.append(p)
# prancha: 6 capas + guia 4:5
pr = Image.new('RGB', (6*360+70, 700), CA); dd = ImageDraw.Draw(pr)
for i, p in enumerate(out):
    t = Image.open(p).resize((360, 640)); x = 10+i*370; pr.paste(t, (x, 50))
    dd.rectangle((x, 50+95, x+360, 50+545), outline=SI, width=2)
dd.text((10, 12), 'WF · capas dos Reels (linha clara = recorte 4:5 do grid)', font=fm(26), fill=PR)
pr.save(os.path.join(D, 'prancha.png')); print('ok')
