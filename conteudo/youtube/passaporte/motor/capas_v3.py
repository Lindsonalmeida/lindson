"""Capas v3 dos longos 10 a 12 (conta Zuleide, 09/11/2026): close dramático em Doré, um só foco, luz de cinema.
Pesquisa e referências em ../capas-longos-10-12/TEMPLATE.md (capturas em referencias/).
- capa-10: copia a composição de EPIC HISTORY "MUTINY" (UK): palavra gigante no alto, figura na frente cobrindo a palavra.
- capa-11: copia JOHNNY HARRIS (EUA): rosto em close de um lado, olhar forte, luz quente, texto no espaço livre do outro lado.
- capa-12: copia CIÊNCIA TODO DIA "FLOW" (Brasil): close extremo, um ponto de luz, palavra gigante cruzando a imagem.
Mantém a identidade do canal: cor de cinema do capas2 (sombra petróleo, luz âmbar), "PASSAPORTE DA BÍBLIA",
etiqueta ciano da série e a palavra-chave em amarelo.
python3 capas_v3.py -> ../capas-longos-10-12/capa-10.jpg, capa-11.jpg, capa-12.jpg"""
import base64, io, json, os, subprocess
import numpy as np, cv2
from PIL import Image, ImageFilter
D = os.path.dirname(os.path.abspath(__file__)); RAIZ = os.path.join(D, '..'); OUT = RAIZ + '/capas-longos-10-12'
TMP = os.environ.get('TMPDIR_CAPAS', '/tmp/capas_v3'); os.makedirs(TMP, exist_ok=True)

def grade(g, glow, forca=1.0, c_gama=1.0, vmin=.16):
    """Cor de cinema do capas2.py (mesma rampa), com mais contraste e luz concentrada num ponto só."""
    g = cv2.bilateralFilter(g, 9, 45, 7)
    g = cv2.createCLAHE(clipLimit=2.4, tileGridSize=(6, 6)).apply(g).astype(np.float32) / 255
    g = np.clip((g - .06) / .80, 0, 1) ** c_gama
    pts = [(0, (6, 16, 22)), (.28, (16, 52, 66)), (.55, (196, 110, 40)), (.8, (248, 188, 96)), (1, (255, 242, 210))]
    out = np.zeros(g.shape + (3,), np.float32)
    for (a, ca), (b, cb) in zip(pts, pts[1:]):
        m = (g >= a) & (g <= b); t = ((g - a) / (b - a))[m][:, None]
        out[m] = np.array(ca) * (1 - t) + np.array(cb) * t
    h, w = g.shape; yy, xx = np.mgrid[0:h, 0:w]
    r = np.sqrt(((xx / w - glow[0]) * 1.5) ** 2 + (yy / h - glow[1]) ** 2)
    out += (np.clip(1 - r / .5, 0, 1) ** 2)[..., None] * np.array([110, 60, 12]) * forca   # brilho quente atrás do foco
    vig = np.clip(1.25 - r ** 2 * 2.6, vmin, 1)[..., None]   # fundo afunda no escuro: um só ponto de foco
    return np.clip(out * vig, 0, 255).astype(np.uint8)

def corte(arq, cx, cy, cw, W=1280, H=720):
    """Recorte 16:9 em fração da gravura (centro cx, cy; largura cw) ampliado para W x H."""
    im = Image.open(arq).convert('L'); iw, ih = im.size
    w = cw * iw; h = w * H / W
    x0 = min(max(cx * iw - w / 2, 0), iw - w); y0 = min(max(cy * ih - h / 2, 0), ih - h)
    box = (int(x0), int(y0), int(x0 + w), int(y0 + h))
    return im.crop(box).resize((W, H), Image.LANCZOS), box

def capa(c):
    g, box = corte(c['arq'], *c['crop'])
    g = g.filter(ImageFilter.UnsharpMask(2, 80, 2))
    rgb = grade(np.array(g), c['glow'], c.get('forca', 1), c.get('gama', 1.0), c.get('vmin', .16))
    fg = ''
    if c.get('prof'):   # figura da frente recortada pelo mapa de profundidade (a palavra passa por trás dela)
        p = Image.open(c['prof']).convert('L').resize(Image.open(c['arq']).size).crop(box).resize((1280, 720), Image.LANCZOS)
        p = np.array(p).astype(np.float32) / 255
        a = np.clip((p - c['corte_prof']) / c.get('rampa', .03), 0, 1)
        if c.get('so_acima'): a[int(720 * c['so_acima']):] = 0
        a = cv2.GaussianBlur(a, (0, 0), 1.6)
        rgba = np.dstack([rgb, (a * 255).astype(np.uint8)])
        fg = f'<img class="fg" src="{uri(Image.fromarray(rgba, "RGBA"), "PNG")}">'
    # fundo levemente desfocado longe do foco (profundidade de campo)
    h, w = 720, 1280; yy, xx = np.mgrid[0:h, 0:w]
    r = np.clip(np.sqrt(((xx / w - c['glow'][0]) * 1.4) ** 2 + (yy / h - c['glow'][1]) ** 2) / .6, 0, 1)[..., None]
    bl = cv2.GaussianBlur(rgb, (0, 0), c.get('desfoque', 6))
    bg = (rgb * (1 - r) + bl * r).astype(np.uint8)
    return pagina(f'<img class="bg" src="{uri(Image.fromarray(bg))}">' + c['antes'] + fg + c['depois'])

def uri(im, fmt='JPEG'):
    b = io.BytesIO(); im.save(b, fmt, **({'quality': 93} if fmt == 'JPEG' else {})); return f'data:image/{fmt.lower()};base64,' + base64.b64encode(b.getvalue()).decode()

CSS = '''<link href="https://fonts.googleapis.com/css2?family=Anton&family=Special+Elite&display=swap" rel="stylesheet"><style>
*{margin:0;box-sizing:border-box}body{width:1280px;height:720px;overflow:hidden;background:#000;position:relative;font-family:Anton}
.bg,.fg{position:absolute;inset:0;width:1280px;height:720px}
.t{position:absolute;color:#fff;text-transform:uppercase;line-height:.84;letter-spacing:.005em;
 -webkit-text-stroke:7px #000;paint-order:stroke fill;text-shadow:0 12px 0 #000,0 0 60px rgba(0,0,0,.9)}
.t b{color:#FFD23F;font-weight:400}
.mk{position:absolute;font:400 22px 'Special Elite';letter-spacing:.3em;color:rgba(255,240,205,.92);text-shadow:0 2px 10px #000}
.tag{position:absolute;padding:9px 20px;background:#5EE6EB;color:#0B1C22;font:400 32px Anton;letter-spacing:.04em;transform:rotate(-3deg);box-shadow:0 8px 24px rgba(0,0,0,.6)}
.sh{position:absolute;inset:0;pointer-events:none}
</style>'''
def pagina(corpo): return '<!doctype html><html><head><meta charset="utf-8">' + CSS + '</head><body>' + corpo + '</body></html>'

DORE = RAIZ + '/dore/'
CAPAS = {
 # Ref. EPIC HISTORY "MUTINY": palavra gigante no alto, a figura (Jesus, braço erguido diante do túmulo de Lázaro) passa na frente dela.
 'capa-10': dict(arq=DORE + '080.jpg', prof=DORE + 'prof/080.png', corte_prof=.095, rampa=.012, crop=(.60, .245, .66), glow=(.50, .48), forca=.7,
   antes='<div class="sh" style="background:linear-gradient(180deg,rgba(0,0,0,.55),rgba(0,0,0,0) 45%)"></div>'
         '<div class="t" style="left:0;right:0;top:14px;text-align:center;font-size:290px;letter-spacing:.03em"><b>SHOW?</b></div>',
   depois='<div class="sh" style="background:linear-gradient(0deg,rgba(0,0,0,.75),rgba(0,0,0,0) 34%)"></div>'
          '<div class="t" style="left:48px;bottom:34px;font-size:128px">NÃO ERA</div>'
          '<div class="mk" style="right:44px;bottom:44px">PASSAPORTE DA BÍBLIA</div>'
          '<div class="tag" style="right:46px;bottom:86px">OS MILAGRES DE JESUS</div>'),
 # Ref. JOHNNY HARRIS (EUA): o personagem em close de um lado, luz quente nele, fundo afundado no escuro,
 # texto empilhado no espaço livre do outro lado. Saulo cobrindo o rosto diante da luz (Atos 9).
 'capa-12': dict(arq=DORE + '095.jpg', crop=(.52, .53, .70), glow=(.72, .50), forca=.5, gama=1.2, vmin=.10, desfoque=10,
   antes='<div class="sh" style="background:linear-gradient(90deg,rgba(0,0,0,.85),rgba(0,0,0,.45) 42%,rgba(0,0,0,0) 62%)"></div>'
         # o feixe de luz do céu (o da gravura, reforçado) caindo do alto sobre o rosto de Saulo
         '<div class="sh" style="mix-blend-mode:screen;background:linear-gradient(118deg,rgba(0,0,0,0) 38%,rgba(255,226,160,.0) 44%,rgba(255,226,160,.55) 52%,rgba(255,240,205,.75) 56%,rgba(255,226,160,.45) 61%,rgba(0,0,0,0) 70%);filter:blur(14px)"></div>',
   depois='<div class="mk" style="left:52px;top:44px">PASSAPORTE DA BÍBLIA</div>'
          '<div class="tag" style="left:54px;top:92px">APÓSTOLO PAULO</div>'
          '<div class="t" style="left:48px;top:236px;font-size:150px">ELE<br><b style="font-size:182px">PERSEGUIA</b></div>'),
 # Ref. CIÊNCIA TODO DIA "FLOW" (Brasil): close num só personagem, luz num ponto, palavra gigante cruzando a imagem de lado a lado.
 # Moisés desce do Sinai com as tábuas (Doré, Bíblia inglesa 1866, placa 039, domínio público, Wikimedia Commons, 1920 px):
 # é a cena em que ele encontra o povo que quis voltar ao Egito (o bezerro de ouro).
 'capa-11': dict(arq=RAIZ + '/capas-longos-10-12/fontes/dore-moises-desce-do-sinai-commons-1920.jpg', crop=(.52, .305, .74), glow=(.52, .36), forca=.75, gama=1.1, vmin=.12,
   antes='',
   depois='<div class="sh" style="background:linear-gradient(0deg,rgba(0,0,0,.8),rgba(0,0,0,0) 42%)"></div>'
          '<div class="mk" style="left:44px;top:40px">PASSAPORTE DA BÍBLIA</div>'
          '<div class="tag" style="left:46px;top:86px">ÊXODO</div>'
          '<div class="t" style="left:0;right:0;text-align:center;bottom:26px;font-size:232px;letter-spacing:.01em">QUIS <b>VOLTAR?</b></div>'),
}

def render(nomes):
    pages = []
    for k in nomes:
        f = f'{TMP}/{k}.html'; open(f, 'w').write(capa(CAPAS[k])); pages.append((f, f'{OUT}/{k}.jpg'))
    js = "const {chromium}=require('/opt/node-tools/node_modules/playwright');(async()=>{const b=await chromium.launch();for(const [f,o] of " + json.dumps(pages) + "){const p=await b.newPage({viewport:{width:1280,height:720}});await p.goto('file://'+f,{waitUntil:'networkidle'});await p.evaluate(()=>document.fonts.ready);await p.screenshot({path:o,type:'jpeg',quality:92});await p.close()}await b.close()})()"
    subprocess.run(['nice', 'node', '-e', js], check=True)

if __name__ == '__main__':
    import sys
    render(sys.argv[1:] or list(CAPAS))
