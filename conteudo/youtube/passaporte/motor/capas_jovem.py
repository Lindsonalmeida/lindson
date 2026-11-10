"""Capas v3 "jovens" dos longos 10 a 12 (conta Zuleide, 10/11/2026). Pedido do Lindson: "gosto desse estilo (as 3 referências),
copie para fazer as nossas assim, mais jovens". Cor viva, contraste alto, 1 palavra gigante, cara de YouTube 2025.
Gravuras de Doré recortadas (BiRefNet portrait, depois de ampliar 2x com Real-ESRGAN) e colorizadas com cor de cinema.
Recortes prontos em ../capas-longos-10-12/fontes/. Pesquisa e referências: ../capas-longos-10-12/TEMPLATE.md.
- capa-10 copia EPIC HISTORY "MUTINY" (UK): céu azul vivo, palavra branca gigante no alto de ponta a ponta,
  personagem recortado e colorido NA FRENTE da palavra, selo do canal no canto.
- capa-11 copia CIÊNCIA TODO DIA "FLOW" (Brasil): close extremo num rosto, cor quente saturada, palavra gigante
  atravessando a imagem com brilho e contraste máximo.
- capa-12 copia JOHNNY HARRIS (EUA): foto de cinema no fim de tarde, céu aberto, personagem em meio corpo de um lado,
  horizonte limpo do outro.
python3 capas_jovem.py -> ../capas-longos-10-12/capa-10.jpg, capa-11.jpg, capa-12.jpg"""
import base64, io, json, os, subprocess, sys
import numpy as np, cv2
from PIL import Image, ImageFilter
D = os.path.dirname(os.path.abspath(__file__)); P = os.path.join(D, '..', 'capas-longos-10-12'); FT = P + '/fontes/'
TMP = os.environ.get('TMPDIR_CAPAS', '/tmp/capas_jovem'); os.makedirs(TMP, exist_ok=True)
W, H = 1280, 720

def rampa(L, pts):
    out = np.zeros(L.shape + (3,), np.float32)
    for (a, ca), (b, cb) in zip(pts, pts[1:]):
        m = (L >= a) & (L <= b); t = ((L - a) / (b - a))[m][:, None]
        out[m] = np.array(ca) * (1 - t) + np.array(cb) * t
    return out

# cor de cinema saturada: sombra azul-petróleo, meio-tom pele/âmbar, luz creme quente
CINEMA = [(0, (14, 22, 40)), (.25, (52, 52, 74)), (.5, (176, 100, 62)), (.75, (240, 170, 110)), (1, (255, 242, 222))]
ROUPA = [(0, (34, 10, 28)), (.3, (120, 36, 38)), (.55, (220, 120, 76)), (.8, (252, 210, 160)), (1, (255, 250, 238))]
QUENTE = [(0, (30, 6, 4)), (.25, (110, 28, 12)), (.5, (214, 92, 34)), (.75, (255, 170, 80)), (1, (255, 246, 214))]

def colorir(rgb, pts, clahe=2.0, suave=7):
    g = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
    g = cv2.bilateralFilter(g, suave, 50, 7)   # tira a hachura miúda da gravura
    g = cv2.createCLAHE(clipLimit=clahe, tileGridSize=(6, 6)).apply(g).astype(np.float32) / 255
    g = np.clip((g - .05) / .9, 0, 1)
    return np.clip(rampa(g, pts), 0, 255).astype(np.uint8)

def uri(im, fmt='PNG'):
    b = io.BytesIO(); im.save(b, fmt, **({'quality': 93} if fmt == 'JPEG' else {}))
    return f'data:image/{fmt.lower()};base64,' + base64.b64encode(b.getvalue()).decode()

def recorte(arq, pts, borda=(120, 220, 255)):
    """Recorte colorizado + luz de contorno (rim light) do lado do céu."""
    im = Image.open(arq).convert('RGBA'); a = np.array(im)[..., 3].astype(np.float32) / 255
    rgb = colorir(np.array(im)[..., :3], pts).astype(np.float32)
    er = cv2.erode((a > .5).astype(np.uint8), np.ones((9, 9), np.uint8))
    rim = np.clip(cv2.GaussianBlur(a - er, (0, 0), 3) * 1.6, 0, 1)[..., None]
    rgb = rgb * (1 - rim * .55) + np.array(borda) * rim * .55
    return Image.fromarray(np.dstack([np.clip(rgb, 0, 255).astype(np.uint8), (a * 255).astype(np.uint8)]), 'RGBA')

def nuvens(seed, w=W, h=H):
    rng = np.random.default_rng(seed); n = np.zeros((h, w), np.float32)
    for s, amp in [(4, 1), (8, .5), (16, .25), (32, .12)]:
        z = rng.random((h // (w // s) + 2, s + 1)).astype(np.float32)
        n += cv2.resize(z, (w, h), interpolation=cv2.INTER_CUBIC) * amp
    return (n - n.min()) / (n.max() - n.min())

def ceu_azul():
    yy = np.linspace(0, 1, H)[:, None, None]
    c = np.array([28, 104, 214]) * (1 - yy) + np.array([120, 190, 245]) * yy
    c = np.repeat(c, W, 1).astype(np.float32)
    n = np.clip((nuvens(3) - .45) / .4, 0, 1)[..., None] ** 1.4
    c = c * (1 - n * .8) + np.array([250, 252, 255]) * n * .8
    return Image.fromarray(np.clip(c, 0, 255).astype(np.uint8))

def fim_de_tarde():
    """Céu aberto de fim de tarde e chão de deserto, horizonte limpo em y=470."""
    hz = 470; yy = np.arange(H)[:, None].astype(np.float32); xx = np.arange(W)[None, :].astype(np.float32)
    t = np.clip(yy / hz, 0, 1)[..., None]
    ceu = np.array([30, 60, 120]) * (1 - t) ** 1.6 + np.array([255, 150, 70]) * (1 - (1 - t) ** 1.6)
    ceu = np.broadcast_to(ceu, (H, W, 3)).copy()
    sol = np.exp(-(((xx - 860) / 260) ** 2 + ((yy - hz + 20) / 120) ** 2))[..., None]
    ceu += sol * np.array([255, 200, 120]) * .9
    chao_t = np.clip((yy - hz) / (H - hz), 0, 1)[..., None]
    chao = np.array([150, 82, 40]) * (1 - chao_t) + np.array([40, 22, 16]) * chao_t
    rng = np.random.default_rng(5); gr = cv2.GaussianBlur(rng.random((H, W)).astype(np.float32), (0, 0), 1.2)[..., None]
    chao = chao * (.9 + gr * .2)
    out = np.where(yy[..., None] < hz, ceu, chao)
    return Image.fromarray(np.clip(out, 0, 255).astype(np.uint8))

CSS = '''<link href="https://fonts.googleapis.com/css2?family=Anton&family=Special+Elite&display=swap" rel="stylesheet"><style>
*{margin:0;box-sizing:border-box}body{width:1280px;height:720px;overflow:hidden;background:#000;position:relative;font-family:Anton}
.l{position:absolute}.sh{position:absolute;inset:0}
.t{position:absolute;color:#fff;text-transform:uppercase;line-height:.86;white-space:nowrap}
.t b{color:#FFD23F;font-weight:400}
.selo{position:absolute;left:0;bottom:0;background:#1F2544;padding:14px 22px 12px 26px;clip-path:polygon(0 0,92% 0,100% 100%,0 100%)}
.selo div{font:400 34px/0.95 Anton;color:#fff;letter-spacing:.02em}.selo span{display:block;font:400 19px Anton;color:#5EE6EB;letter-spacing:.18em}
.tag{position:absolute;padding:8px 18px;background:#5EE6EB;color:#0B1C22;font:400 30px Anton;letter-spacing:.04em;transform:rotate(-3deg);box-shadow:0 8px 22px rgba(0,0,0,.45)}
.mk{position:absolute;font:400 20px 'Special Elite';letter-spacing:.3em;color:#fff;text-shadow:0 2px 10px rgba(0,0,0,.9)}
</style>'''
def pagina(c): return '<!doctype html><html><head><meta charset="utf-8">' + CSS + '</head><body>' + c + '</body></html>'
SELO = '<div class="selo"><div>PASSAPORTE</div><span>DA BÍBLIA</span></div>'

def capa10():
    # Ref. EPIC HISTORY "MUTINY": céu azul vivo, palavra branca gigante de ponta a ponta no alto,
    # Jesus (Doré 080, ressurreição de Lázaro) recortado e colorido passando na frente da palavra; selo no canto.
    fig = recorte(FT + 'recorte-jesus-080.png', ROUPA, borda=(255, 236, 200))
    fig = fig.resize((int(fig.width * 1.62), int(fig.height * 1.62)), Image.LANCZOS)
    som = Image.new('RGBA', fig.size, (8, 20, 50, 0)); som.putalpha(fig.getchannel('A').filter(ImageFilter.GaussianBlur(18)).point(lambda v: v * .55))
    return pagina(f'''<img class="l" style="inset:0" src="{uri(ceu_azul(), 'JPEG')}">
<div class="t" style="left:0;right:0;top:18px;text-align:center;font-size:262px;letter-spacing:.015em;text-shadow:0 10px 0 rgba(10,30,70,.35)">MILAGRE?</div>
<img class="l" style="left:{600 - fig.width // 2 + 40}px;top:56px" src="{uri(som)}">
<img class="l" style="left:{600 - fig.width // 2}px;top:30px" src="{uri(fig)}">
<div class="sh" style="background:linear-gradient(0deg,rgba(10,25,60,.55),rgba(0,0,0,0) 30%)"></div>
{SELO}<div class="tag" style="right:36px;bottom:34px">OS MILAGRES DE JESUS</div>''')

def capa11():
    # Ref. CIÊNCIA TODO DIA "FLOW": close extremo no rosto de Moisés (Doré, Sinai, 1920 px), cor quente saturada,
    # palavra gigante branca atravessando a imagem com brilho; o rosto fica livre acima da palavra.
    im = Image.open(FT + 'dore-moises-desce-do-sinai-commons-1920.jpg').convert('RGB')
    c = im.crop((664, 500, 1384, 905)).resize((W, H), Image.LANCZOS)
    rgb = colorir(np.array(cv2.GaussianBlur(np.array(c), (0, 0), 1.6)), QUENTE, clahe=2.2, suave=11).astype(np.float32)
    yy, xx = np.mgrid[0:H, 0:W]; r = np.sqrt(((xx / W - .5) * 1.3) ** 2 + (yy / H - .4) ** 2)
    rgb *= np.clip(1.25 - r ** 2 * 2.2, .25, 1)[..., None]
    bg = Image.fromarray(np.clip(rgb, 0, 255).astype(np.uint8)).filter(ImageFilter.UnsharpMask(2, 70, 2))
    return pagina(f'''<img class="l" style="inset:0" src="{uri(bg, 'JPEG')}">
<div class="t" style="left:0;right:0;top:400px;text-align:center;font-size:300px;letter-spacing:.02em;
 background:linear-gradient(180deg,#fff 55%,#d9f6ff);-webkit-background-clip:text;color:transparent;
 filter:drop-shadow(0 0 3px #FFD23F) drop-shadow(0 12px 18px rgba(0,0,0,.75)) drop-shadow(0 0 40px rgba(255,170,60,.6))">VOLTAR?</div>
<div class="mk" style="left:40px;top:34px">PASSAPORTE DA BÍBLIA</div><div class="tag" style="left:42px;top:76px">ÊXODO</div>''')

def capa12():
    # Ref. JOHNNY HARRIS: foto de cinema no fim de tarde, céu aberto e horizonte limpo à esquerda,
    # Saulo (Doré 095, a caminho de Damasco) em meio corpo à direita, contra o sol.
    fig = recorte(FT + 'recorte-saulo-095.png', CINEMA, borda=(255, 210, 140))
    fig = fig.resize((int(fig.width * 1.4), int(fig.height * 1.4)), Image.LANCZOS)
    return pagina(f'''<img class="l" style="inset:0" src="{uri(fim_de_tarde(), 'JPEG')}">
<div class="sh" style="background:radial-gradient(circle at 70% 18%,rgba(255,240,200,.55),rgba(255,240,200,0) 30%)"></div>
<div class="sh" style="mix-blend-mode:screen;background:linear-gradient(112deg,rgba(0,0,0,0) 52%,rgba(255,236,190,.45) 60%,rgba(255,236,190,0) 72%);filter:blur(10px)"></div>
<img class="l" style="right:-90px;bottom:-60px" src="{uri(fig)}">
<div class="sh" style="background:linear-gradient(0deg,rgba(20,10,8,.45),rgba(0,0,0,0) 25%)"></div>
<div class="t" style="left:44px;top:96px;font-size:150px;text-shadow:0 8px 0 rgba(0,0,0,.55),0 0 40px rgba(0,0,0,.5)"><b>PERSEGUIDOR</b></div>
<div class="mk" style="left:46px;top:40px">PASSAPORTE DA BÍBLIA</div><div class="tag" style="left:48px;top:262px">APÓSTOLO PAULO</div>''')

CAPAS = {'capa-10': capa10, 'capa-11': capa11, 'capa-12': capa12}
if __name__ == '__main__':
    pages = []
    for k in sys.argv[1:] or list(CAPAS):
        f = f'{TMP}/{k}.html'; open(f, 'w').write(CAPAS[k]()); pages.append((f, f'{P}/{k}.jpg'))
    js = "const {chromium}=require('/opt/node-tools/node_modules/playwright');(async()=>{const b=await chromium.launch();for(const [f,o] of " + json.dumps(pages) + "){const p=await b.newPage({viewport:{width:1280,height:720}});await p.goto('file://'+f,{waitUntil:'networkidle'});await p.evaluate(()=>document.fonts.ready);await p.screenshot({path:o,type:'jpeg',quality:92});await p.close()}await b.close()})()"
    subprocess.run(['nice', 'node', '-e', js], check=True); print(len(pages), 'capas')
