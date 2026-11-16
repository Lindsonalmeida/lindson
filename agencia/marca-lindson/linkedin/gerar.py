# LinkedIn do Lindson Almeida Studio: banner, foto e carrossel PDF (conta Zuleide, 16/11/2026)
# Uso: python3 gerar.py  (so PIL, sem ffmpeg)
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
B = os.path.dirname(os.path.abspath(__file__))
PINS = os.path.join(B, '../projeto-designer/pinterest/v2/pins')
OUT = os.path.join(B, 'artes'); os.makedirs(OUT, exist_ok=True)
FOTO = os.environ.get('FOTO', '/tmp/reel2-work/L30-05/c10-rec2.png')  # recorte c10 (mesmo avatar do mini site/Instagram)
PRETO, AMA, BR, CIN = (10, 10, 10), (245, 197, 24), (255, 255, 255), (150, 150, 150)
ANTON = os.path.join(B, '../projeto-designer/pinterest/Anton-Regular.ttf')
INTER = '/usr/share/fonts/opentype/inter/Inter-%s.otf'
def F(n, s): return ImageFont.truetype(ANTON if n == 'A' else INTER % n, s)
def pin(n): return Image.open(os.path.join(PINS, n)).convert('RGB')
def cover(im, w, h):
    r = max(w / im.width, h / im.height); im = im.resize((int(im.width * r) + 1, int(im.height * r) + 1))
    x, y = (im.width - w) // 2, (im.height - h) // 2; return im.crop((x, y, x + w, y + h))
def sombra(base, box, r=18):
    s = Image.new('RGBA', base.size, (0, 0, 0, 0)); ImageDraw.Draw(s).rectangle(box, fill=(0, 0, 0, 170))
    base.alpha_composite(s.filter(ImageFilter.GaussianBlur(r)))

# 1) Banner 1584x396: texto no centro (a foto de perfil cobre o canto inferior esquerdo), mosaico de cases a direita
bn = Image.new('RGBA', (1584, 396), PRETO + (255,)); d = ImageDraw.Draw(bn)
xs = [1080, 1250, 1420]
for i, n in enumerate(['01-oregano-fachada.jpg', '09-jaci-retrato.jpg', '13-wf-fachada.jpg']):
    x = xs[i]; y = 30 if i % 2 == 0 else -40
    t = cover(pin(n), 160, 400); sombra(bn, (x + 8, y + 14, x + 168, y + 414)); bn.paste(t, (x, y))
g = Image.new('RGBA', (300, 396)); gd = ImageDraw.Draw(g)
for k in range(300): gd.line([(k, 0), (k, 396)], fill=PRETO + (int(255 * (1 - k / 300)),))
bn.alpha_composite(g, (1040, 0)); d = ImageDraw.Draw(bn)
d.text((380, 70), 'LINDSON ALMEIDA STUDIO', font=F('Bold', 22), fill=AMA)
d.text((380, 104), 'MARCAS QUE PARECEM', font=F('A', 70), fill=BR)
d.text((380, 184), 'DO TAMANHO QUE SÃO.', font=F('A', 70), fill=AMA)
d.text((380, 284), 'Identidade visual · Brand book · Site  |  São Luís (MA) para o Brasil', font=F('Medium', 22), fill=CIN)
bn.convert('RGB').save(os.path.join(OUT, 'banner-1584x396.jpg'), quality=92)

# 2) Foto de perfil 800x800: busto recortado sobre amarelo, luz suave
pf = Image.new('RGBA', (800, 800), AMA + (255,)); gl = Image.new('RGBA', (800, 800), (0, 0, 0, 0))
ImageDraw.Draw(gl).ellipse((120, 60, 680, 620), fill=(255, 225, 110, 160)); pf.alpha_composite(gl.filter(ImageFilter.GaussianBlur(60)))
if os.path.exists(FOTO):
    f = Image.open(FOTO).convert('RGBA'); bb = f.getbbox(); f = f.crop(bb)
    w = 760; f = f.resize((w, int(f.height * w / f.width)))
    pf.alpha_composite(f.crop((0, 0, w, min(f.height, 740))), (20, 800 - min(f.height, 740)))
pf.convert('RGB').save(os.path.join(OUT, 'foto-perfil-800.jpg'), quality=92)

# 3) Carrossel PDF 1080x1350 (8 telas, cada uma com composicao diferente)
W, H = 1080, 1350
def tela(): im = Image.new('RGBA', (W, H), PRETO + (255,)); return im, ImageDraw.Draw(im)
def rod(d, n, cor=CIN):
    d.text((70, H - 80), 'LINDSON ALMEIDA STUDIO', font=F('Bold', 22), fill=cor); d.text((W - 140, H - 80), f'{n}/8', font=F('Bold', 22), fill=cor)
def txt(d, x, y, linhas, f, cor, esp=1.1):
    for l in linhas: d.text((x, y), l, font=f, fill=cor); y += int(f.size * esp)
    return y
S = []
im, d = tela(); im.paste(cover(pin('04-oregano-avental.jpg'), W, 760), (0, 0))
txt(d, 70, 810, ['SUA MARCA PARECE', 'MENOR DO QUE', 'SEU NEGÓCIO?'], F('A', 110), BR); d.rectangle((70, 1200, 380, 1208), fill=AMA); rod(d, 1); S.append(im)
im, d = tela(); txt(d, 70, 200, ['O CLIENTE', 'JULGA ANTES', 'DE PROVAR.'], F('A', 140), AMA)
txt(d, 70, 760, ['Antes de pedir, ligar ou entrar, ele olha o', 'Instagram, a fachada, o cartão. Se a marca', 'parece improvisada, o preço parece caro.'], F('Medium', 38), BR, 1.4)
d.text((70, 120), 'A VERDADE', font=F('Bold', 28), fill=AMA); rod(d, 2); S.append(im)
im, d = tela(); im.paste(cover(pin('07-oregano-grid.jpg'), W, H), (0, 0)); ov = Image.new('RGBA', (W, 520), PRETO + (235,)); im.alpha_composite(ov, (0, H - 520)); d = ImageDraw.Draw(im)
d.text((70, H - 480), 'ERRO 1', font=F('Bold', 28), fill=AMA); txt(d, 70, H - 430, ['CADA POST NUMA', 'COR DIFERENTE.'], F('A', 96), BR); rod(d, 3); S.append(im)
im = Image.new('RGBA', (W, H), AMA + (255,)); d = ImageDraw.Draw(im); d.text((70, 120), 'ERRO 2', font=F('Bold', 28), fill=PRETO)
txt(d, 70, 180, ['LOGO QUE', 'SÓ FUNCIONA', 'GRANDE.'], F('A', 140), PRETO)
c = cover(pin('15-oregano-logo.jpg'), 600, 600); sombra(im, (250, 680, 850, 1280)); im.paste(c, (240, 660)); d = ImageDraw.Draw(im); rod(d, 4, PRETO); S.append(im)
im, d = tela(); a, b = cover(pin('19-wf-cartao.jpg'), 500, 800), cover(pin('11-oregano-cartao.jpg'), 500, 800)
im.paste(a, (30, 300)); im.paste(b, (550, 300)); d.text((70, 120), 'ERRO 3', font=F('Bold', 28), fill=AMA)
d.text((70, 170), 'NENHUMA REGRA ESCRITA.', font=F('A', 80), fill=BR); d.text((70, 1130), 'Sem manual, cada fornecedor inventa uma marca nova.', font=F('Medium', 32), fill=BR); rod(d, 5); S.append(im)
im, d = tela(); d.text((70, 120), 'O QUE MUDA COM UM SISTEMA', font=F('Bold', 30), fill=AMA); y = 220
for n, t in [('01', 'Logo, versões e área de proteção'), ('02', 'Paleta com proporção de uso'), ('03', '2 fontes, sempre as mesmas'), ('04', 'Aplicações: fachada, farda, post'), ('05', 'Manual que qualquer um segue')]:
    d.text((70, y), n, font=F('A', 110), fill=AMA); d.text((260, y + 40), t, font=F('SemiBold', 44), fill=BR); y += 170
rod(d, 6); S.append(im)
im, d = tela(); im.paste(cover(pin('18-oregano-sacola.jpg'), W, H), (0, 0)); ov = Image.new('RGBA', (W, 380), PRETO + (220,)); im.alpha_composite(ov, (0, 0)); d = ImageDraw.Draw(im)
d.text((70, 90), 'CASE · ORÉGANO TURBO', font=F('Bold', 28), fill=AMA); txt(d, 70, 140, ['A MESMA MARCA', 'DA FACHADA À SACOLA.'], F('A', 90), BR); rod(d, 7, BR); S.append(im)
im = Image.new('RGBA', (W, H), AMA + (255,)); d = ImageDraw.Draw(im)
txt(d, 70, 260, ['SUA MARCA', 'ESTÁ NO', 'TAMANHO', 'CERTO?'], F('A', 170), PRETO)
d.text((70, 1020), 'Comente "MARCA" ou chame no WhatsApp.', font=F('SemiBold', 40), fill=PRETO); d.text((70, 1080), 'Mostro o que eu mudaria na sua, sem compromisso.', font=F('Medium', 32), fill=PRETO); rod(d, 8, PRETO); S.append(im)
S = [s.convert('RGB') for s in S]
S[0].save(os.path.join(OUT, 'carrossel-marca-menor.pdf'), save_all=True, append_images=S[1:], resolution=150)
for i, s in enumerate(S): s.resize((360, 450)).save(os.path.join(OUT, f'_c{i+1}.jpg'), quality=80)
# Previa: perfil montado (banner + foto) + telas do carrossel
pv = Image.new('RGB', (1584, 396 + 260 + 470), (243, 242, 238)); pv.paste(Image.open(os.path.join(OUT, 'banner-1584x396.jpg')), (0, 0))
m = Image.new('L', (300, 300), 0); ImageDraw.Draw(m).ellipse((0, 0, 299, 299), fill=255)
ImageDraw.Draw(pv).ellipse((50, 236, 362, 548), fill=BR); pv.paste(Image.open(os.path.join(OUT, 'foto-perfil-800.jpg')).resize((300, 300)), (56, 242), m)
dv = ImageDraw.Draw(pv); dv.text((400, 420), 'Lindson Almeida', font=F('Bold', 40), fill=(20, 20, 20))
dv.text((400, 474), 'Designer de marcas | Identidade visual, brand book e site para negócios locais | Lindson Almeida Studio', font=F('Medium', 22), fill=(60, 60, 60))
for i in range(8): pv.paste(Image.open(os.path.join(OUT, f'_c{i+1}.jpg')).resize((188, 235)), (12 + i * 196, 640))
pv.save(os.path.join(OUT, 'previa.jpg'), quality=88)
for i in range(8): os.remove(os.path.join(OUT, f'_c{i+1}.jpg'))
print('ok')
