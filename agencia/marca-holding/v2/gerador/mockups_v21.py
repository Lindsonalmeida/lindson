# Al Kántara v2.1 · mockups fotorrealistas (conta Leandro, 16/11/2026)
# Fotos reais livres (créditos em fotos-v2.1/CREDITOS.md) + arte renderizada em HTML e aplicada em perspectiva.
# Copia a composição de Pentagram/Mastercard (marca aplicada em foto real de lugar, não render chapado).
import os, sys, subprocess, numpy as np
from PIL import Image, ImageFilter, ImageDraw, ImageChops, ImageEnhance
G = os.path.dirname(os.path.abspath(__file__)); B = os.path.abspath(G + '/..'); F = B + '/fotos-v2.1'; T = F + '/_arte'
os.makedirs(T, exist_ok=True)
sys.path.insert(0, G)
from simbolo import pecas, path
INK, LIME, BRASS, GRAPH = '#0B0C0E', '#EFEAE1', '#B8955A', '#1A1C20'
def K(s, cor):
    return f'<svg viewBox="0 0 {24*s} {24*s}" width="{24*s}" height="{24*s}">' + ''.join(f'<path fill="{cor}" d="{path(p, s)}"/>' for p in pecas()) + '</svg>'
OURO = 'linear-gradient(135deg,#8a6a35 0%,#e9d09a 28%,#b8955a 46%,#f3dfb0 62%,#8f6d38 100%)'
def Kouro(s, id_):
    return (f'<svg viewBox="0 0 {24*s} {24*s}" width="{24*s}" height="{24*s}"><defs><linearGradient id="{id_}" x1="0" y1="0" x2="1" y2="1">'
            '<stop offset="0" stop-color="#8a6a35"/><stop offset=".3" stop-color="#ecd49e"/><stop offset=".5" stop-color="#b8955a"/><stop offset=".68" stop-color="#f3dfb0"/><stop offset="1" stop-color="#8f6d38"/></linearGradient></defs>'
            + ''.join(f'<path fill="url(#{id_})" d="{path(p, s)}"/>' for p in pecas()) + '</svg>')
DIVS = [('Labs', '#2E4BFF'), ('Barzakh', '#E8461E'), ('Media', '#F0A202'), ('Ventures', '#0E8C66')]
html = f'''<!doctype html><meta charset=utf-8><style>
@font-face{{font-family:F;src:url(../fontes/Fraunces-Regular.ttf)}}@font-face{{font-family:I;src:url(../fontes/InterTight-Medium.ttf);font-weight:500}}
@font-face{{font-family:I;src:url(../fontes/InterTight-SemiBold.ttf);font-weight:600}}@font-face{{font-family:M;src:url(../fontes/JetBrainsMono-Medium.ttf)}}
body{{margin:0;background:transparent}} *{{box-sizing:border-box}}</style>
<div id="site" style="width:1440px;height:900px;background:{INK};position:relative;overflow:hidden;font-family:I;color:{LIME}">
 <div style="position:absolute;right:-160px;top:40px;opacity:1">{K(30,'#15171a')}</div>
 <div style="position:absolute;left:70px;top:40px"><img src="../logos/svg/alkantara-horizontal-negativo.svg" style="height:34px"></div>
 <div style="position:absolute;right:70px;top:48px;display:flex;gap:40px;font:500 17px I;opacity:.85"><span>Labs</span><span>Barzakh</span><span>Media</span><span>Ventures</span><span style="color:{BRASS}">Contato →</span></div>
 <div style="position:absolute;left:70px;top:230px"><div style="font:500 15px M;letter-spacing:.18em;color:{BRASS}">GRUPO DE TECNOLOGIA · SÃO LUÍS</div>
 <div style="font:400 140px/.95 F;letter-spacing:-.015em;margin-top:24px">Estrutura<br>para o que <i style="color:{BRASS}">vem.</i></div>
 <div style="margin-top:34px;display:inline-block;background:{LIME};color:{INK};font:600 19px I;padding:18px 30px">Conheça as divisões</div></div>
 <div style="position:absolute;left:0;right:0;bottom:0;display:grid;grid-template-columns:repeat(4,1fr)">''' + ''.join(f'<div style="border-top:5px solid {c};padding:24px 34px;background:#121316"><div style="font:400 36px F">{n}</div></div>' for n, c in DIVS) + f'''</div></div>
<div id="placa" style="width:300px;height:940px;padding:0;background:linear-gradient(180deg,#26282d,#141518);position:relative;border-radius:3px;box-shadow:inset 0 1px 0 rgba(255,255,255,.12),inset 0 -2px 0 rgba(0,0,0,.6)">
 <div style="position:absolute;left:62px;top:80px">{Kouro(7.33,'g1')}</div>
 <div style="position:absolute;left:0;right:0;top:330px;text-align:center;font:600 46px/1.15 I;letter-spacing:.06em;background:{OURO};-webkit-background-clip:text;color:transparent">AL<br>KÁN<br>TARA</div>
 <div style="position:absolute;left:0;right:0;top:560px;text-align:center;font:500 17px M;letter-spacing:.42em;color:#c7a66c">GROUP</div>
 <div style="position:absolute;left:60px;right:60px;top:640px;height:1px;background:#8a6a35"></div>
 <div style="position:absolute;left:0;right:0;top:672px;text-align:center;font:500 14px/2 M;letter-spacing:.2em;color:#a98a55">LABS<br>BARZAKH<br>MEDIA<br>VENTURES</div>
 <div style="position:absolute;left:0;right:0;bottom:44px;text-align:center;font:500 13px M;letter-spacing:.2em;color:#7d6844">Nº 199</div>
 <div style="position:absolute;inset:0;background:linear-gradient(115deg,rgba(255,255,255,.10),transparent 40%,rgba(0,0,0,.2));border-radius:3px"></div></div>
<div id="grav" style="width:700px;height:1500px;position:relative">
 <div style="position:absolute;left:210px;top:330px">{K(11.67,'#b89458')}</div>
 <div style="position:absolute;left:0;right:0;top:1150px;text-align:center;font:600 54px I;letter-spacing:.08em;color:#b89458">AL KÁNTARA</div>
 <div style="position:absolute;left:0;right:0;top:1225px;text-align:center;font:500 20px M;letter-spacing:.42em;color:#a9895a">GROUP</div></div>
'''
open(B + '/paginas/_mock-v2.1.html', 'w').write(html)
subprocess.run(['node', G + '/shots_v21.js', B + '/paginas/_mock-v2.1.html', T, 'site', 'placa', 'grav'], check=True, env={**os.environ, 'NODE_PATH': '/opt/node-tools/node_modules'})

def coeffs(dst, src):
    # PIL PERSPECTIVE: mapeia ponto de saída (dst) → entrada (src)
    A = []; b = []
    for (x, y), (u, v) in zip(dst, src):
        A += [[x, y, 1, 0, 0, 0, -u*x, -u*y], [0, 0, 0, x, y, 1, -v*x, -v*y]]; b += [u, v]
    return np.linalg.solve(np.array(A, float), np.array(b, float)).tolist()
def warp(art, size, quad):
    w, h = art.size
    return art.transform(size, Image.PERSPECTIVE, coeffs(quad, [(0, 0), (w, 0), (w, h), (0, h)]), Image.BICUBIC)
def quadmask(size, quad, blur=1.2):
    m = Image.new('L', size, 0); ImageDraw.Draw(m).polygon(quad, fill=255); return m.filter(ImageFilter.GaussianBlur(blur))
def crop169(im, cy=None):
    W, H = im.size; h = int(W * 9 / 16); cy = H // 2 if cy is None else cy; y0 = max(0, min(H - h, cy - h // 2))
    return im.crop((0, y0, W, y0 + h)).resize((1920, 1080), Image.LANCZOS)
def grao(im, a=6):
    n = np.random.default_rng(3).normal(0, a, (im.height, im.width, 1)); return Image.fromarray(np.clip(np.asarray(im, float) + n, 0, 255).astype('uint8'))

# 1) notebook: site na tela da foto real (home-office.jpg, CC0)
im = Image.open(F + '/home-office.jpg').convert('RGB')
q = [(2000, 155), (3157, 485), (2730, 1355), (1605, 882)]
site = Image.open(T + '/site.png').convert('RGB')
scr = warp(site, im.size, q); scr = ImageEnhance.Brightness(scr).enhance(.92)
glare = Image.new('RGB', im.size, (255, 255, 255)); gm = Image.new('L', im.size, 0); ImageDraw.Draw(gm).polygon([(2000, 155), (2650, 345), (1900, 1050), (1605, 882)], fill=16)
im.paste(scr, (0, 0), quadmask(im.size, q)); im.paste(glare, (0, 0), ImageChops.multiply(gm, quadmask(im.size, q)))
crop169(grao(im, 4), 1150).save(F + '/mock-notebook.jpg', quality=90)

# 2) fachada: placa vertical em latão na parede de azulejo, Centro Histórico de São Luís (CC BY 4.0)
im = Image.open(F + '/slz-portugal.jpg').convert('RGB')
pl = Image.open(T + '/placa.png').convert('RGBA'); pl = pl.resize((int(pl.width * 900 / pl.height * 0.5), 450), Image.LANCZOS) if False else pl
ph = 700; pl = pl.resize((int(pl.width * ph / pl.height), ph), Image.LANCZOS)
x0, y0 = 2656 - pl.width // 2, 1060
sh = Image.new('L', im.size, 0); a = pl.getchannel('A'); sh.paste(a, (x0 + 22, y0 + 30)); sh = sh.filter(ImageFilter.GaussianBlur(18)).point(lambda v: int(v * .62))
im.paste(Image.new('RGB', im.size, (10, 12, 14)), (0, 0), sh)
im.paste(pl, (x0, y0), pl)
# parafusos de afastamento
d = ImageDraw.Draw(im)
for (px, py) in [(x0 + 22, y0 + 22), (x0 + pl.width - 22, y0 + 22), (x0 + 22, y0 + ph - 22), (x0 + pl.width - 22, y0 + ph - 22)]:
    d.ellipse((px - 7, py - 7, px + 7, py + 7), fill=(150, 120, 70)); d.ellipse((px - 3, py - 4, px + 2, py), fill=(235, 210, 160))
crop169(grao(im, 3), 1300).save(F + '/mock-fachada.jpg', quality=90)
# recorte vertical para close
im.crop((2656 - 700, 760, 2656 + 700, 2340)).resize((1080, 1219), Image.LANCZOS).save(F + '/mock-fachada-close.jpg', quality=90)

# 3) gravação em uma cor: capa preta fosca do celular com gravação a laser em latão (foto CC0)
im = Image.open(F + '/celular-mao.jpg').convert('RGB'); A = np.asarray(im, float)
q = [(1516, 435), (2202, 435), (2533, 1938), (1793, 2100)]
R, Gc, Bc = A[..., 0], A[..., 1], A[..., 2]
pele = ((R - Bc) > 22) & (R > 80)
qm = np.asarray(quadmask(im.size, q, 0), float) / 255
# apaga a maçã e os textos: pinta com a cor média local do aparelho (borrão grande)
reg = [(1880, 700, 2060, 900), (1990, 1550, 2300, 1750)]
lim = im.copy(); blur = im.filter(ImageFilter.GaussianBlur(60))
for r in reg:
    mk = Image.new('L', im.size, 0); ImageDraw.Draw(mk).rectangle(r, fill=255); mk = mk.filter(ImageFilter.GaussianBlur(25)); lim.paste(blur, (0, 0), mk)
lim = Image.fromarray(np.where(pele[..., None], A, np.asarray(lim, float)).astype('uint8'))
art = Image.open(T + '/grav.png').convert('RGBA'); wa = warp(art, im.size, q)
al = np.asarray(wa.getchannel('A'), float) / 255 * qm * (~pele)
L = np.asarray(lim, float); lum = (L.mean(axis=2, keepdims=True) / 95).clip(.5, 1.0)
C = np.asarray(wa.convert('RGB'), float) * lum
out = L * (1 - al[..., None] * .85) + C * al[..., None] * .85
# leve relevo: sombra 1 px
crop169(grao(Image.fromarray(out.clip(0, 255).astype('uint8')), 3), 1250).save(F + '/mock-gravacao.jpg', quality=90)
print('ok')
