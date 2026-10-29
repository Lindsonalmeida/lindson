"""Capas v2 (estilo dos vídeos que viralizam): close dramático no personagem, contraste alto, cores de cinema
(sombras azul-petróleo, luz laranja), brilho atrás da figura e 1 a 3 palavras gigantes. Também "duelo"
(duas gravuras lado a lado com VS) e "símbolo".
python3 capas2.py [id ...] -> ../capas/v2/<id>-A.jpg, -B.jpg, -C.jpg (1280x720)"""
import base64, io, json, os, subprocess, sys
import numpy as np, cv2
from PIL import Image, ImageFilter
D = os.path.dirname(os.path.abspath(__file__)); RAIZ = os.path.join(D, '..'); OUT = RAIZ + '/capas/v2'; os.makedirs(OUT, exist_ok=True)
TMP = '/tmp/claude-0/-home-user/5acf6937-9ac6-56e0-bc29-78bef210dc8b/scratchpad/th2'; os.makedirs(TMP, exist_ok=True)
sys.path.insert(0, D)

def foco(g):
    """Centro do primeiro plano (pelo mapa de profundidade): onde está a figura principal."""
    d = cv2.imread(f'{RAIZ}/dore/prof/{g}.png', 0).astype(np.float32) / 255
    m = d > np.quantile(d, .88); ys, xs = np.nonzero(m)
    return xs.mean() / d.shape[1], ys.mean() / d.shape[0]

def grade(im, glow=(0.5, 0.45)):
    """Mapa de cor de cinema a partir da gravura P&B: sombra petróleo, meio âmbar, luz creme; contraste local."""
    g = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2GRAY)
    g = cv2.bilateralFilter(g, 9, 40, 7)   # suaviza a hachura da gravura para não virar ruído
    g = cv2.createCLAHE(clipLimit=2.6, tileGridSize=(8, 8)).apply(g).astype(np.float32) / 255
    g = np.clip((g - .08) / .84, 0, 1) ** 1.15
    pts = [(0, (8, 20, 28)), (.28, (18, 58, 72)), (.55, (196, 110, 40)), (.8, (246, 184, 92)), (1, (255, 240, 205))]
    out = np.zeros(g.shape + (3,), np.float32)
    for (a, ca), (b, cb) in zip(pts, pts[1:]):
        m = (g >= a) & (g <= b); t = ((g - a) / (b - a))[m][:, None]
        out[m] = np.array(ca) * (1 - t) + np.array(cb) * t
    h, w = g.shape; yy, xx = np.mgrid[0:h, 0:w]
    r = np.sqrt(((xx / w - glow[0]) * 1.6) ** 2 + (yy / h - glow[1]) ** 2)
    out += (np.clip(1 - r / .55, 0, 1) ** 2)[..., None] * np.array([90, 50, 10])   # brilho quente atrás da figura
    vig = np.clip(1.25 - (((xx / w - glow[0]) * 1.3) ** 2 + (yy / h - glow[1]) ** 2) * 2.6, .22, 1)[..., None]   # escurece longe da figura
    return Image.fromarray(np.clip(out * vig, 0, 255).astype(np.uint8))

def recorte(g, zoom, f=None, ar=16 / 9, W=1280, H=720):
    im = Image.open(f'{RAIZ}/dore/{g}.jpg').convert('RGB'); fx, fy = f or foco(g)
    cw = im.width * zoom; ch = cw / ar
    if ch > im.height: ch = im.height; cw = ch * ar
    x0 = min(max(fx * im.width - cw / 2, 0), im.width - cw); y0 = min(max(fy * im.height - ch * .45, 0), im.height - ch)
    c = im.crop((int(x0), int(y0), int(x0 + cw), int(y0 + ch))).resize((W, H), Image.LANCZOS).filter(ImageFilter.UnsharpMask(2, 90, 2))
    return grade(c, ((fx * im.width - x0) / cw, (fy * im.height - y0) / ch))

def uri(im):
    b = io.BytesIO(); im.save(b, 'JPEG', quality=92); return 'data:image/jpeg;base64,' + base64.b64encode(b.getvalue()).decode()

CSS = '''<link href="https://fonts.googleapis.com/css2?family=Anton&family=Special+Elite&display=swap" rel="stylesheet"><style>
*{margin:0;box-sizing:border-box}body{width:1280px;height:720px;overflow:hidden;background:#000;position:relative;font-family:Anton}
.bg{position:absolute;inset:0;background-size:cover;background-position:center}
.t{position:absolute;color:#fff;text-transform:uppercase;line-height:.92;letter-spacing:.01em;
 -webkit-text-stroke:6px #000;paint-order:stroke fill;text-shadow:0 10px 0 #000,0 0 50px rgba(0,0,0,.95)}
.t b{color:#FFD23F;font-weight:400}.t i{font-style:normal;color:#5EE6EB}
.mk{position:absolute;font:400 20px 'Special Elite';letter-spacing:.28em;color:rgba(255,240,205,.85);text-shadow:0 2px 8px #000}
.vs{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%) rotate(-6deg);width:150px;height:150px;border-radius:50%;background:#FFD23F;
 color:#111;font:400 74px/150px Anton;text-align:center;box-shadow:0 0 0 8px #111,0 14px 40px rgba(0,0,0,.7)}
.div{position:absolute;left:50%;top:-20px;bottom:-20px;width:14px;background:#111;transform:rotate(6deg)}
.tag{position:absolute;padding:10px 22px;background:#5EE6EB;color:#0B1C22;font:400 34px Anton;letter-spacing:.04em;transform:rotate(-3deg);box-shadow:0 8px 24px rgba(0,0,0,.6)}
</style>'''

def pagina(corpo): return '<!doctype html><html><head><meta charset="utf-8">' + CSS + '</head><body>' + corpo + '</body></html>'

def close(c):
    im = recorte(c['grav'], c.get('zoom', .55), c.get('foco'))
    lado = c.get('lado', 'esq'); pos = 'left:56px' if lado == 'esq' else 'right:56px;text-align:right'
    return pagina(f'''<div class="bg" style="background-image:url({uri(im)})"></div>
<div style="position:absolute;inset:0;background:linear-gradient({'90deg' if lado == 'esq' else '270deg'},rgba(0,0,0,.55),rgba(0,0,0,0) 55%)"></div>
<div class="t" style="{pos};bottom:{'44px' if lado == 'esq' else '96px'};font-size:{c.get('fs', 182)}px;max-width:900px;line-height:.86">{c['txt']}</div>
<div class="mk" style="{pos};top:40px">PASSAPORTE DA BÍBLIA</div>{f'<div class="tag" style="{pos};top:90px">{c["tag"]}</div>' if c.get('tag') else ''}''')

def duelo(c):
    a = recorte(c['grav'], c.get('zoom', .6), c.get('foco'), ar=(640 / 720), W=680, H=720)
    b = recorte(c['grav2'], c.get('zoom2', .6), c.get('foco2'), ar=(640 / 720), W=680, H=720)
    return pagina(f'''<div class="bg" style="right:50%;background-image:url({uri(a)})"></div><div class="bg" style="left:50%;background-image:url({uri(b)})"></div>
<div class="div"></div><div class="vs">VS</div>
<div class="t" style="left:40px;bottom:40px;font-size:{c.get('fs', 128)}px;width:600px">{c['txt']}</div>
<div class="t" style="right:40px;bottom:92px;font-size:{c.get('fs', 128)}px;width:600px;text-align:right">{c['txt2']}</div>
<div class="mk" style="left:40px;top:36px">PASSAPORTE DA BÍBLIA</div>''')

def vclose(c):
    im = recorte(c['grav'], c.get('zoom', .8), c.get('foco'), ar=9 / 16, W=1080, H=1920)
    return pagina(f'''<style>body{{width:1080px;height:1920px}}</style><div class="bg" style="background-image:url({uri(im)});filter:brightness(1.35) contrast(1.12) saturate(1.15)"></div>
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,0) 45%,rgba(0,0,0,.7) 85%)"></div>
<div class="mk" style="left:0;right:0;text-align:center;top:90px;font-size:26px">PASSAPORTE DA BÍBLIA</div>
<div class="t" style="left:60px;right:60px;text-align:center;bottom:330px;font-size:{c.get('fs', 190)}px;line-height:.9">{c['txt']}</div>
{f'<div class="tag" style="left:50%;transform:translateX(-50%) rotate(-3deg);top:150px;font-size:44px">{c["tag"]}</div>' if c.get('tag') else ''}''')

ESTILOS = dict(close=close, duelo=duelo, vclose=vclose)
CAPAS = json.load(open(RAIZ + '/capas_v2.json'))
ids = sys.argv[1:] or list(CAPAS)
pages = []
for k in ids:
    for var, c in CAPAS[k].items():
        f = f'{TMP}/{k}-{var}.html'; open(f, 'w').write(ESTILOS[c['estilo']](c)); v = c['estilo'] == 'vclose'; pages.append((f, f'{OUT}/{k}' + ('' if v else f'-{var}') + '.jpg', 1080 if v else 1280, 1920 if v else 720))
js = "const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();for(const [f,o,w,h] of " + json.dumps(pages) + "){const p=await b.newPage({viewport:{width:w,height:h}});await p.goto('file://'+f,{waitUntil:'networkidle'});await p.evaluate(()=>document.fonts.ready);await p.screenshot({path:o,type:'jpeg',quality:92});await p.close()}await b.close()})()"
subprocess.run(['node', '-e', js], check=True); print(len(pages), 'capas em', OUT)
