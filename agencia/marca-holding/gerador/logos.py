# Al Kántara Group · logos em SVG com texto convertido em curvas (conta Leandro, 16/11/2026)
# Símbolo: três arcos concêntricos da ponte de Alcántara (Trajano, 106 d.C.) redesenhados em geometria pura + tabuleiro.
import os, sys
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
FD = sys.argv[1] if len(sys.argv) > 1 else 'fonts'
OUT = '/home/user/lindson/agencia/marca-holding/elementos/logos/svg'
os.makedirs(OUT, exist_ok=True)

def text_path(fontfile, s, size, x0, y0, track=0):
    f = TTFont(fontfile); gs = f.getGlyphSet(); cmap = f.getBestCmap(); upm = f['head'].unitsPerEm
    sc = size/upm; pen = SVGPathPen(gs); x = 0
    for ch in s:
        g = cmap.get(ord(ch))
        if g is None: x += 0.3*upm; continue
        tp = TransformPen(pen, (sc, 0, 0, -sc, x0 + x*sc, y0))
        gs[g].draw(tp); x += gs[g].width + track/sc
    return pen.getCommands(), (x*sc - track)

def simbolo(cx, base, R, cor, acento):
    # arcos semicirculares (anéis) com espessura proporcional; vão interno = luz
    w = R*0.13; out = []
    for i, r in enumerate([R, R*0.66]):
        ro, ri = r, r - w
        out.append(f'<path fill="{cor}" d="M{cx-ro},{base} A{ro},{ro} 0 0 1 {cx+ro},{base} L{cx+ri},{base} A{ri},{ri} 0 0 0 {cx-ri},{base} Z"/>')
    rk = R*0.32
    out.append(f'<path fill="{acento}" d="M{cx-rk},{base} A{rk},{rk} 0 0 1 {cx+rk},{base} Z"/>')
    out.append(f'<rect fill="{cor}" x="{cx-R*1.18}" y="{base+R*0.1}" width="{R*2.36}" height="{w*0.55}"/>')
    return ''.join(out)

SER = FD + '/InstrumentSerif-Regular.ttf'; SANS = FD + '/InterTight'
CORES = {'positivo': ('#0A0C10', '#B4935A', None), 'negativo': ('#EEEAE2', '#B4935A', None),
         'mono-preto': ('#0A0C10', '#0A0C10', None), 'mono-branco': ('#FFFFFF', '#FFFFFF', None),
         'bronze': ('#B4935A', '#B4935A', None)}

def svg(w, h, body): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">{body}</svg>'

def build(nome, cor, ac):
    files = {}
    files['simbolo'] = svg(240, 200, simbolo(120, 150, 100, cor, ac))
    # horizontal
    p1, w1 = text_path(SER, 'AL KÁNTARA', 92, 0, 0, track=6)
    p2, w2 = text_path(SANS, 'G R O U P', 22, 0, 0, track=4)
    W = 230 + w1 + 20
    body = simbolo(95, 132, 80, cor, ac)
    body += f'<g transform="translate(230,118)"><path fill="{cor}" d="{text_path(SER,"AL KÁNTARA",92,0,0,6)[0]}"/></g>'
    body += f'<g transform="translate(234,160)"><path fill="{cor}" d="{text_path(SANS,"G R O U P",22,0,0,4)[0]}"/></g>'
    body += f'<rect fill="{ac}" x="{234+w2+18}" y="150" width="{w1-w2-22}" height="1.6"/>'
    files['horizontal'] = svg(int(W), 200, body)
    # vertical
    Wv = max(w1, 400) + 80; cx = Wv/2
    body = simbolo(cx, 200, 110, cor, ac)
    body += f'<g transform="translate({cx-w1/2},330)"><path fill="{cor}" d="{text_path(SER,"AL KÁNTARA",92,0,0,6)[0]}"/></g>'
    body += f'<g transform="translate({cx-w2/2},380)"><path fill="{cor}" d="{text_path(SANS,"G R O U P",22,0,0,4)[0]}"/></g>'
    files['vertical'] = svg(int(Wv), 420, body)
    # logotipo só
    files['logotipo'] = svg(int(w1+40), 130, f'<g transform="translate(20,100)"><path fill="{cor}" d="{p1}"/></g>')
    for k, v in files.items():
        open(f'{OUT}/alkantara-{k}-{nome}.svg', 'w').write(v)

for n, (c, a, _) in CORES.items(): build(n, c, a)
# endosso: "uma empresa Al Kántara Group"
p, w = text_path(SANS, 'UMA EMPRESA', 16, 0, 0, 3); p2, w2 = text_path(SER, 'AL KÁNTARA GROUP', 30, 0, 0, 2)
for n, c in [('positivo', '#0A0C10'), ('negativo', '#EEEAE2')]:
    open(f'{OUT}/alkantara-endosso-{n}.svg', 'w').write(svg(int(70+max(w, w2)+10), 70,
        simbolo(28, 52, 24, c, '#B4935A') + f'<g transform="translate(66,24)"><path fill="{c}" opacity=".7" d="{p}"/></g><g transform="translate(66,56)"><path fill="{c}" d="{p2}"/></g>'))
print(sorted(os.listdir(OUT)))
