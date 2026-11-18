"""Carrosséis do Instagram do Passaporte da Bíblia (conta Zuleide, 18/11/2026).
Capa = visual aprovado do canal (gravura de Doré com a cor de cinema do capas2.py: sombra petróleo, luz âmbar,
"PASSAPORTE DA BÍBLIA" no topo, etiqueta ciano, Anton branco com 1 palavra amarela).
Telas de dentro = identidade do produto (azul-noite, creme, dourado, cor da região; Baloo 2, Nunito, Special Elite),
alternando com telas de gravura em tela cheia. Nenhuma tela repete o layout da anterior (o script confere).
python3 carrosseis.py [id ...] -> ../instagram/carrosseis/<id>/NN.jpg (1080x1350) + previa.jpg
Dados: ../instagram/carrosseis.json. Gravuras: ../dore/NNN.jpg (Gutenberg 8710, domínio público)."""
import base64, io, json, os, subprocess, sys
import numpy as np, cv2
from PIL import Image, ImageFilter
D = os.path.dirname(os.path.abspath(__file__)); RAIZ = os.path.join(D, '..')
OUT = RAIZ + '/instagram/carrosseis'; TMP = os.environ.get('TMPDIR', '/tmp') + '/carrosseis'; os.makedirs(TMP, exist_ok=True)
W, H = 1080, 1350
REG = {'lei': '#D9573B', 'hist': '#E9A23B', 'poe': '#E2668E', 'pma': '#3F9A55', 'pme': '#9CC152', 'ev': '#3B8EDB', 'cartas': '#8466C4', 'ap': '#8E2C48',
       'noite': '#1F2544', 'ouro': '#C9A227', 'carimbo': '#D7263D'}

def grade(im, glow=(0.5, 0.45)):
    """Mesmo mapa de cor do capas2.py (sombra petróleo, meio âmbar, luz creme)."""
    g = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2GRAY)
    g = cv2.bilateralFilter(g, 9, 40, 7)
    g = cv2.createCLAHE(clipLimit=2.6, tileGridSize=(8, 8)).apply(g).astype(np.float32) / 255
    g = np.clip((g - .08) / .84, 0, 1) ** 1.15
    pts = [(0, (8, 20, 28)), (.28, (18, 58, 72)), (.55, (196, 110, 40)), (.8, (246, 184, 92)), (1, (255, 240, 205))]
    out = np.zeros(g.shape + (3,), np.float32)
    for (a, ca), (b, cb) in zip(pts, pts[1:]):
        m = (g >= a) & (g <= b); t = ((g - a) / (b - a))[m][:, None]
        out[m] = np.array(ca) * (1 - t) + np.array(cb) * t
    h, w = g.shape; yy, xx = np.mgrid[0:h, 0:w]
    r = np.sqrt(((xx / w - glow[0]) * 1.6) ** 2 + (yy / h - glow[1]) ** 2)
    out += (np.clip(1 - r / .55, 0, 1) ** 2)[..., None] * np.array([90, 50, 10])
    vig = np.clip(1.25 - (((xx / w - glow[0]) * 1.3) ** 2 + (yy / h - glow[1]) ** 2) * 2.6, .22, 1)[..., None]
    return Image.fromarray(np.clip(out * vig, 0, 255).astype(np.uint8))

def recorte(g, zoom=1, f=(.5, .5), ar=W / H, w=W, h=H):
    im = Image.open(f'{RAIZ}/instagram/carrosseis/ia/{g}' if '.' in g else f'{RAIZ}/dore/{g}.jpg').convert('RGB'); fx, fy = f   # "img": arquivo do Gemini em instagram/carrosseis/ia/
    cw = im.width * zoom; ch = cw / ar
    if ch > im.height: ch = im.height; cw = ch * ar
    x0 = min(max(fx * im.width - cw / 2, 0), im.width - cw); y0 = min(max(fy * im.height - ch / 2, 0), im.height - ch)
    c = im.crop((int(x0), int(y0), int(x0 + cw), int(y0 + ch))).resize((w, h), Image.LANCZOS).filter(ImageFilter.UnsharpMask(2, 90, 2))
    return grade(c, ((fx * im.width - x0) / cw, (fy * im.height - y0) / ch))

def uri(im):
    b = io.BytesIO(); im.save(b, 'JPEG', quality=90); return 'data:image/jpeg;base64,' + base64.b64encode(b.getvalue()).decode()

def bg(t):
    return f'<div class="bg" style="background-image:url({uri(recorte(t.get("img") or t["grav"], t.get("zoom", 1), tuple(t.get("foco", (.5, .5)))))})"></div>'

CSS = '''<link href="https://fonts.googleapis.com/css2?family=Anton&family=Baloo+2:wght@600;800&family=Nunito:wght@600;800;900&family=Special+Elite&display=swap" rel="stylesheet"><style>
*{margin:0;padding:0;box-sizing:border-box}body{width:1080px;height:1350px;overflow:hidden;position:relative;font-family:Nunito;background:#1F2544;color:#FFF7E8}
.bg{position:absolute;inset:0;background-size:cover;background-position:center}
.sh{position:absolute;inset:0}
.A{font-family:Anton;text-transform:uppercase;line-height:.9;color:#fff;-webkit-text-stroke:5px #000;paint-order:stroke fill;text-shadow:0 8px 0 #000,0 0 50px rgba(0,0,0,.9)}
.A b{color:#FFD23F;font-weight:400}
.B{font-family:'Baloo 2';font-weight:800;line-height:1}
.S{font-family:'Special Elite'}
.mk{position:absolute;left:0;right:0;top:56px;text-align:center;font:400 26px 'Special Elite';letter-spacing:.3em;color:rgba(255,240,205,.92);text-shadow:0 2px 10px #000}
.tag{position:absolute;padding:12px 26px;background:#5EE6EB;color:#0B1C22;font:400 40px Anton;letter-spacing:.05em;transform:rotate(-3deg);box-shadow:0 8px 24px rgba(0,0,0,.6)}
.pe{position:absolute;left:64px;right:64px;bottom:44px;display:flex;justify-content:space-between;font:400 24px 'Special Elite';letter-spacing:.12em;opacity:.8}
.rot{display:inline-block;font:400 28px 'Special Elite';letter-spacing:.18em;padding:8px 18px;border:2px solid currentColor;border-radius:6px}
.creme{background:#FFF7E8;color:#1F2544}
.ref{font:400 30px 'Special Elite';letter-spacing:.06em}
.stamp{position:absolute;border:16px double #D7263D;box-shadow:inset 0 0 0 10px transparent,inset 0 0 0 14px #D7263D;color:#D7263D;border-radius:50%;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;font-family:'Special Elite';transform:rotate(-12deg);opacity:.92}
</style>'''

def pe(t, i, n, claro=False):
    return f'<div class="pe" style="color:{"#1F2544" if claro else "#FFF7E8"}"><span>@passaportedabiblia</span><span>{i}/{n}</span></div>'

# ---------------- layouts ----------------
def capa(t, i, n):
    return bg(t) + f'''<div class="sh" style="background:linear-gradient(180deg,rgba(0,0,0,.55) 0,rgba(0,0,0,0) 22%,rgba(0,0,0,0) 45%,rgba(0,0,0,.82) 100%)"></div>
<div class="mk">PASSAPORTE DA BÍBLIA</div><div class="tag" style="left:64px;top:120px">{t["tag"]}</div>
<div class="A" style="position:absolute;left:60px;right:60px;bottom:{170 if t.get("sub") else 120}px;font-size:{t.get("fs", 190)}px">{t["txt"]}</div>
{f'<div class="B" style="position:absolute;left:64px;right:64px;bottom:86px;font-size:44px;color:#FFF7E8;text-shadow:0 3px 14px #000">{t["sub"]}</div>' if t.get("sub") else ""}
<div class="S" style="position:absolute;right:64px;top:132px;font-size:28px;color:#FFF7E8;text-shadow:0 2px 8px #000">arraste ✈</div>'''

def numero(t, i, n):
    c = REG.get(t.get('cor', 'ouro'), t.get('cor'))
    return f'''<div class="sh" style="background:radial-gradient(circle at 50% 38%,#2c3563,#1F2544 60%,#121633)"></div>
<div style="position:absolute;left:64px;top:90px"><span class="rot" style="color:{c}">{t.get("rot", "")}</span></div>
<div class="A" style="position:absolute;left:0;right:0;top:200px;text-align:center;font-size:{t.get("fs", 460)}px;color:{c};-webkit-text-stroke:0;text-shadow:0 18px 0 rgba(0,0,0,.35)">{t["n"]}</div>
<div class="B" style="position:absolute;left:80px;right:80px;top:{t.get("y", 760)}px;text-align:center;font-size:76px;color:#FFF7E8">{t["txt"]}</div>
<div style="position:absolute;left:110px;right:110px;top:{t.get("y", 760) + 230}px;text-align:center;font-size:38px;font-weight:600;color:#cfd3ea">{t.get("sub", "")}</div>''' + pe(t, i, n)

def grade8(t, i, n):
    rs = [('lei', 'Lei', 'Gênesis a Deuteronômio', 5), ('hist', 'Históricos', 'Josué a Ester', 12), ('poe', 'Poéticos', 'Jó a Cânticos', 5), ('pma', 'Profetas Maiores', 'Isaías a Daniel', 5),
          ('pme', 'Profetas Menores', 'Oseias a Malaquias', 12), ('ev', 'Evangelhos e Atos', 'Mateus a Atos', 5), ('cartas', 'Cartas', 'Romanos a Judas', 21), ('ap', 'Apocalipse', 'o último livro', 1)]
    cards = ''.join(f'''<div style="background:{REG[k]};border-radius:26px;padding:30px 30px;color:#fff;position:relative;box-shadow:0 10px 0 rgba(31,37,68,.18);display:flex;flex-direction:column;justify-content:flex-end">
<div class="B" style="font-size:48px">{nome}</div><div style="font-size:29px;font-weight:800;opacity:.92">{sub}</div>
<div class="A" style="position:absolute;right:26px;top:18px;font-size:110px;color:rgba(255,255,255,.95);-webkit-text-stroke:0;text-shadow:none">{q}</div></div>''' for k, nome, sub, q in rs)
    return f'''<div class="sh creme"></div><div style="position:absolute;left:64px;right:64px;top:80px">
<div class="B" style="font-size:70px;color:#1F2544">{t["titulo"]}</div><div style="font-size:32px;font-weight:700;color:#1F2544;opacity:.75;margin:6px 0 30px">{t.get("sub", "")}</div>
<div style="display:grid;grid-template-columns:1fr 1fr;grid-auto-rows:225px;gap:22px">{cards}</div></div>''' + pe(t, i, n, True)

def cena(t, i, n):
    topo = t.get('pos') == 'topo'
    g = 'rgba(0,0,0,.85) 0,rgba(0,0,0,0) 55%' if topo else 'rgba(0,0,0,0) 35%,rgba(0,0,0,.88) 100%'
    return bg(t) + f'''<div class="sh" style="background:linear-gradient(180deg,{g})"></div>
<div style="position:absolute;left:70px;right:70px;{"top:110px" if topo else "bottom:130px"}">
{f'<div class="rot" style="color:#5EE6EB;margin-bottom:24px">{t["rot"]}</div>' if t.get("rot") else ""}
<div class="A" style="font-size:{t.get("fs", 110)}px">{t["txt"]}</div>
{f'<div class="ref" style="margin-top:22px;color:#FFE7B0;text-shadow:0 2px 10px #000">{t["ref"]}</div>' if t.get("ref") else ""}</div>''' + pe(t, i, n)

def bilhete(t, i, n):
    c = REG[t['cor']]
    lin = ''.join(f'<div><div class="S" style="font-size:22px;letter-spacing:.2em;opacity:.65">{k}</div><div class="B" style="font-size:46px">{v}</div></div>' for k, v in t['linhas'])
    return f'''<div class="sh" style="background:{c}"></div>
<div style="position:absolute;left:64px;right:64px;top:150px;bottom:150px;background:#FFF7E8;border-radius:34px;color:#1F2544;overflow:hidden;box-shadow:0 30px 60px rgba(0,0,0,.3)">
<div style="background:#1F2544;color:#FFF7E8;padding:34px 46px;display:flex;justify-content:space-between;align-items:center">
<span class="S" style="font-size:28px;letter-spacing:.25em">BILHETE DE EMBARQUE</span><span class="S" style="font-size:28px;color:#C9A227">DESTINO {t["n"]}</span></div>
<div style="padding:40px 46px 0"><div class="S" style="font-size:26px;letter-spacing:.25em;color:{c}">DESTINO</div>
<div class="A" style="font-size:190px;color:#1F2544;-webkit-text-stroke:0;text-shadow:none;line-height:1">{t["livro"]}</div></div>
<div style="margin:26px 46px;border-top:4px dashed #1F254455"></div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:34px 30px;padding:0 46px">{lin}</div>
<div class="stamp" style="right:56px;bottom:46px;width:230px;height:230px;font-size:30px">EMBARQUE<br>LIBERADO</div></div>''' + pe(t, i, n)

def frase(t, i, n):
    c = REG.get(t.get('cor', 'noite'), t.get('cor'))
    return f'''<div class="sh" style="background:{c}"></div>
<div style="position:absolute;left:64px;top:110px"><span class="rot" style="color:#FFF7E8">{t["rot"]}</span></div>
<div style="position:absolute;left:64px;right:64px;top:290px;background:#FFF7E8;color:#1F2544;border-radius:46px;padding:64px 60px;box-shadow:0 26px 0 rgba(0,0,0,.18)">
<div class="B" style="font-size:{t.get("fs", 84)}px">{t["txt"]}</div>
<div style="position:absolute;left:90px;bottom:-56px;width:0;height:0;border-left:30px solid transparent;border-right:50px solid transparent;border-top:60px solid #FFF7E8"></div></div>
{f'<div style="position:absolute;left:70px;right:70px;bottom:150px;font-size:40px;font-weight:700;color:#FFF7E8">{t["sub"]}</div>' if t.get("sub") else ""}''' + pe(t, i, n)

def lista(t, i, n):
    c = REG.get(t.get('cor', 'ouro'), t.get('cor'))
    it = ''.join(f'''<div style="display:flex;gap:30px;align-items:flex-start;position:relative;padding-bottom:{t.get("gap", 50)}px">
<div class="A" style="flex:0 0 96px;height:96px;border-radius:50%;background:{c};color:#1F2544;-webkit-text-stroke:0;text-shadow:none;font-size:50px;display:flex;align-items:center;justify-content:center;z-index:1">{k + 1}</div>
<div><div class="B" style="font-size:{t.get("fs", 58)}px;color:#FFF7E8">{a}</div><div class="ref" style="color:{c};font-size:32px;margin-top:4px">{b}</div></div></div>''' for k, (a, b) in enumerate(t['itens']))
    return f'''<div class="sh" style="background:#1F2544"></div>
<div style="position:absolute;left:109px;top:330px;bottom:170px;border-left:6px dotted {c}66"></div>
<div style="position:absolute;left:64px;right:64px;top:90px"><span class="rot" style="color:{c}">{t["rot"]}</span>
<div class="B" style="font-size:72px;margin:24px 0 46px">{t["titulo"]}</div>{it}</div>''' + pe(t, i, n)

def cartoes(t, i, n):
    c = REG.get(t.get('cor', 'noite'), t.get('cor'))
    it = ''.join(f'''<div style="flex:1;background:#fff;border-radius:28px;padding:30px 40px;border-left:18px solid {c};box-shadow:0 10px 0 rgba(31,37,68,.12);display:flex;flex-direction:column;justify-content:center">
<div class="B" style="font-size:60px;color:#1F2544">{a}</div><div style="font-size:36px;font-weight:700;color:#3a4066;margin-top:8px">{b}</div></div>''' for a, b in t['itens'])
    return f'''<div class="sh creme"></div><div style="position:absolute;left:64px;right:64px;top:90px;bottom:120px;display:flex;flex-direction:column">
<div><span class="rot" style="color:{c}">{t["rot"]}</span></div><div class="B" style="font-size:76px;color:#1F2544;margin:22px 0 36px">{t["titulo"]}</div>
<div style="flex:1;display:flex;flex-direction:column;gap:26px">{it}</div></div>''' + pe(t, i, n, True)

def divide(t, i, n):
    return f'''<div class="sh" style="bottom:50%;background:#121633"></div><div class="sh creme" style="top:50%"></div>
<div style="position:absolute;left:70px;right:70px;top:110px"><div class="rot" style="color:#D7263D">{t["a_rot"]}</div>
<div class="B" style="font-size:66px;margin-top:28px;color:#FFF7E8">{t["a"]}</div></div>
<div class="A" style="position:absolute;left:50%;top:50%;transform:translate(-50%,-50%) rotate(-6deg);background:#FFD23F;color:#1F2544;-webkit-text-stroke:0;text-shadow:none;font-size:64px;padding:14px 34px;border-radius:14px;box-shadow:0 0 0 8px #1F2544">{t.get("x", "NA VERDADE")}</div>
<div style="position:absolute;left:70px;right:70px;top:760px"><div class="rot" style="color:#3F9A55">{t["b_rot"]}</div>
<div class="B" style="font-size:66px;margin-top:28px;color:#1F2544">{t["b"]}</div></div>''' + pe(t, i, n, True)

def versiculo(t, i, n):
    return f'''<div class="sh" style="background:#C9A227"></div><div class="sh" style="background:radial-gradient(circle at 70% 20%,rgba(255,255,255,.35),transparent 55%)"></div>
<div style="position:absolute;left:70px;right:70px;top:110px"><span class="rot" style="color:#1F2544">{t.get("rot", "VERSÍCULO DE BOLSO")}</span></div>
<div class="B" style="position:absolute;left:70px;top:190px;font-size:300px;color:#1F2544;opacity:.25">“</div>
<div style="position:absolute;left:70px;right:70px;top:400px"><div class="B" style="font-size:{t.get("fs", 76)}px;color:#1F2544">{t["txt"]}</div>
<div class="ref" style="margin-top:40px;color:#1F2544;font-size:38px">{t["ref"]}</div>
{"" if t.get("sem_salva") else '<div style="margin-top:50px;font-size:32px;font-weight:800;color:#1F2544;opacity:.75">Salva e põe de papel de parede.</div>'}</div>''' + pe(t, i, n, True)

def dica(t, i, n):
    return bg(t) + f'''<div class="sh" style="background:rgba(10,18,26,.62);backdrop-filter:blur(3px)"></div>
<div style="position:absolute;left:0;right:0;top:120px;text-align:center"><span class="rot" style="color:#5EE6EB">QUEM SOU EU?</span></div>
<div class="A" style="position:absolute;left:0;right:0;top:230px;text-align:center;font-size:250px;color:#FFD23F">DICA {t["n"]}</div>
<div class="B" style="position:absolute;left:90px;right:90px;top:620px;text-align:center;font-size:76px;color:#FFF7E8;text-shadow:0 4px 20px #000">{t["txt"]}</div>
<div class="ref" style="position:absolute;left:0;right:0;bottom:130px;text-align:center;color:#FFE7B0">{t.get("ref", "")}</div>''' + pe(t, i, n)

def revela(t, i, n):
    im = recorte(t['grav'], t.get('zoom', .7), tuple(t.get('foco', (.5, .5))), ar=1080 / 640, w=1080, h=640)
    lin = ''.join(f'<div style="display:flex;gap:18px;font-size:33px;font-weight:700;margin-top:16px"><span style="color:#D7263D">✦</span><span>{x}</span></div>' for x in t['linhas'])
    return f'''<div class="sh creme"></div><div class="bg" style="bottom:auto;height:640px;background-image:url({uri(im)})"></div>
<div class="S" style="position:absolute;left:64px;top:60px;font-size:26px;letter-spacing:.3em;color:#FFF7E8;text-shadow:0 2px 8px #000">PASSAPORTE DO PERSONAGEM</div>
<div style="position:absolute;left:64px;right:64px;top:560px;background:#FFF7E8;border-radius:28px;padding:36px 44px;color:#1F2544;box-shadow:0 -10px 40px rgba(0,0,0,.3)">
<div class="S" style="font-size:24px;letter-spacing:.25em;opacity:.6">NOME</div><div class="A" style="font-size:120px;color:#1F2544;-webkit-text-stroke:0;text-shadow:none">{t["nome"]}</div>{lin}</div>
<div class="stamp" style="right:70px;top:470px;width:210px;height:210px;font-size:30px;background:rgba(255,247,232,.9)">{t.get("selo", "REVELADO")}</div>''' + pe(t, i, n, True)

def rotas(t, i, n):
    linhas = ''
    for k, (nome, cor, paradas, nota) in enumerate(t['rotas']):
        y = 330 + k * 300
        est = ''.join(f'<div style="text-align:center;width:180px"><div style="width:44px;height:44px;border-radius:50%;background:#FFF7E8;border:10px solid {cor};margin:0 auto"></div><div style="font-size:26px;font-weight:800;margin-top:10px">{p}</div></div>' for p in paradas)
        linhas += f'''<div style="position:absolute;left:64px;right:64px;top:{y}px"><div class="B" style="font-size:46px;color:{cor}">{nome}</div>
<div style="position:relative;margin-top:16px"><div style="position:absolute;left:60px;right:60px;top:17px;height:12px;background:{cor};border-radius:6px"></div>
<div style="position:relative;display:flex;justify-content:space-between">{est}</div></div><div style="font-size:26px;opacity:.75;margin-top:6px">{nota}</div></div>'''
    return f'''<div class="sh" style="background:#1F2544"></div><div style="position:absolute;left:64px;right:64px;top:90px">
<span class="rot" style="color:#C9A227">{t["rot"]}</span><div class="B" style="font-size:70px;margin-top:22px">{t["titulo"]}</div></div>{linhas}''' + pe(t, i, n)

def carimbo(t, i, n):
    return f'''<div class="sh creme"></div><div class="sh" style="background:repeating-linear-gradient(0deg,transparent 0 58px,rgba(31,37,68,.06) 58px 60px)"></div>
<div class="S" style="position:absolute;left:64px;top:80px;font-size:26px;letter-spacing:.3em;color:#1F2544">PASSAPORTE DA BÍBLIA · PÁGINA DE SELOS</div>
<div class="stamp" style="left:50%;top:330px;margin-left:-270px;width:540px;height:540px;font-size:74px;font-weight:700;line-height:1.05">{t["carimbo"]}</div>
<div class="B" style="position:absolute;left:70px;right:70px;top:940px;text-align:center;font-size:66px;color:#1F2544">{t["txt"]}</div>
<div style="position:absolute;left:50%;transform:translateX(-50%);top:1130px;background:#1F2544;color:#FFF7E8;border-radius:60px;padding:24px 50px;font:800 40px Nunito;white-space:nowrap">{t["cta"]}</div>''' + pe(t, i, n, True)

LAY = dict(capa=capa, numero=numero, grade8=grade8, cena=cena, bilhete=bilhete, frase=frase, lista=lista, cartoes=cartoes, divide=divide,
           versiculo=versiculo, dica=dica, revela=revela, rotas=rotas, carimbo=carimbo)

def pagina(corpo): return '<!doctype html><html><head><meta charset="utf-8">' + CSS + '</head><body>' + corpo + '</body></html>'

DADOS = json.load(open(RAIZ + '/instagram/carrosseis.json'))
ids = sys.argv[1:] or list(DADOS)
jobs = []
for cid in ids:
    telas = DADOS[cid]['telas']; os.makedirs(f'{OUT}/{cid}', exist_ok=True)
    for a, b in zip(telas, telas[1:]):
        assert a['l'] != b['l'] or a['l'] == 'dica', f'{cid}: duas telas seguidas no layout {a["l"]}'
    for k, t in enumerate(telas, 1):
        f = f'{TMP}/{cid}-{k:02d}.html'; open(f, 'w').write(pagina(LAY[t['l']](t, k, len(telas))))
        jobs.append((f, f'{OUT}/{cid}/{k:02d}.jpg'))
js = "const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1350}});for(const [f,o] of " + json.dumps(jobs) + "){await p.goto('file://'+f,{waitUntil:'networkidle'});await p.evaluate(()=>document.fonts.ready);await p.screenshot({path:o,type:'jpeg',quality:90})}await b.close()})()"
subprocess.run(['node', '-e', js], check=True)
for cid in ids:   # prévia: todas as telas lado a lado
    fs = sorted(x for x in os.listdir(f'{OUT}/{cid}') if x[:2].isdigit()); tw = 270; th = 338
    pv = Image.new('RGB', (tw * len(fs) + 10 * (len(fs) + 1), th + 20), '#111')
    for k, x in enumerate(fs): pv.paste(Image.open(f'{OUT}/{cid}/{x}').resize((tw, th)), (10 + k * (tw + 10), 10))
    pv.save(f'{OUT}/{cid}/previa.jpg', quality=85)
print(len(jobs), 'telas em', OUT)
