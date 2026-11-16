# Barzakh · um estúdio Al Kántara · logos em SVG com texto em curvas (conta Leandro, 16/11/2026)
# Símbolo "Dois mares": o arco da holding (régua de logos.py da holding) espelhado abaixo da linha,
# o reflexo em contorno, e o disco de luz partido na linha (Bronze em cima, Lápis embaixo).
# Uso: python3 logos.py <pasta_fontes> <saida>   (InstrumentSerif-Regular.ttf, InterTight-Medium.ttf)
import os, sys, subprocess
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
FD = sys.argv[1]; OUT = sys.argv[2]
os.makedirs(OUT + '/svg', exist_ok=True); os.makedirs(OUT + '/png', exist_ok=True)
OBS, MAR, GRA, PED, BRO, LAP = '#0A0C10', '#EEEAE2', '#22262E', '#8A8F98', '#B4935A', '#2B3A8F'
SER = FD + '/InstrumentSerif-Regular.ttf'; SANS = FD + '/InterTight-Medium.ttf'

def text_path(fontfile, s, size, track=0):
    f = TTFont(fontfile); gs = f.getGlyphSet(); cmap = f.getBestCmap(); upm = f['head'].unitsPerEm
    sc = size / upm; pen = SVGPathPen(gs); x = 0
    for ch in s:
        g = cmap.get(ord(ch))
        if g is None: x += 0.3 * upm; continue
        gs[g].draw(TransformPen(pen, (sc, 0, 0, -sc, x * sc, 0))); x += gs[g].width + track / sc
    return pen.getCommands(), x * sc - track

def anel(cx, base, ro, ri, sentido):
    # sentido 1 = arco para cima; -1 = espelhado para baixo
    s = 1 if sentido > 0 else 0; s2 = 0 if sentido > 0 else 1
    return f'M{cx-ro},{base} A{ro},{ro} 0 0 {s} {cx+ro},{base} L{cx+ri},{base} A{ri},{ri} 0 0 {s2} {cx-ri},{base} Z'

def simbolo(cx, base, R, cor, reflexo, luz, mar):
    w = R * 0.13; g = w * 0.55; o = []
    for r in (R, R * 0.66):  # mundo de cima: anéis cheios (régua da holding)
        o.append(f'<path fill="{cor}" d="{anel(cx, base - g, r, r - w, 1)}"/>')
    sw = w * 0.35
    for r in (R, R * 0.66):  # mundo de baixo: o reflexo em contorno fino
        rm = r - w / 2
        o.append(f'<path fill="none" stroke="{reflexo}" stroke-width="{sw}" d="M{cx-rm},{base+g} A{rm},{rm} 0 0 0 {cx+rm},{base+g}"/>')
    rk = R * 0.32
    o.append(f'<path fill="{luz}" d="M{cx-rk},{base-g} A{rk},{rk} 0 0 1 {cx+rk},{base-g} Z"/>')
    o.append(f'<path fill="{mar}" d="M{cx-rk},{base+g} A{rk},{rk} 0 0 0 {cx+rk},{base+g} Z"/>')
    o.append(f'<rect fill="{cor}" x="{cx-R*1.18}" y="{base-g*0.42}" width="{R*2.36}" height="{g*0.84}"/>')
    return ''.join(o)

def svg(w, h, body, bg=None):
    b = f'<rect width="{w}" height="{h}" fill="{bg}"/>' if bg else ''
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.0f} {h:.0f}" width="{w:.0f}" height="{h:.0f}">{b}{body}</svg>'

# variações: nome -> (cor do traço, reflexo, luz, mar, fundo da prévia)
VAR = {'positivo': (OBS, OBS, BRO, LAP, MAR), 'negativo': (MAR, MAR, BRO, LAP, OBS),
       'lapis': (MAR, MAR, BRO, OBS, LAP), 'mono-preto': (OBS, OBS, OBS, OBS, MAR),
       'mono-branco': (MAR, MAR, MAR, MAR, OBS), 'bronze': (BRO, BRO, BRO, BRO, OBS)}
P1, W1 = text_path(SER, 'BARZAKH', 100, 14)
P2, W2 = text_path(SANS, 'DESIGN · BRANDING', 19, 6)
P3, W3 = text_path(SANS, 'UM ESTÚDIO AL KÁNTARA', 15, 4.5)
PT, WT = text_path(SER, 'A passagem da sua marca.', 40, 0)
files = []
for n, (c, rf, l, m, bg) in VAR.items():
    sub = PED if n in ('positivo', 'negativo', 'lapis') else c
    sub = MAR if n == 'lapis' else sub
    out = {}
    out['simbolo'] = (240, 240, simbolo(120, 120, 92, c, rf, l, m))
    # horizontal: símbolo + BARZAKH + DESIGN · BRANDING
    Wh = 262 + W1 + 34
    b = simbolo(118, 108, 82, c, rf, l, m)
    b += f'<g transform="translate(252,112)"><path fill="{c}" d="{P1}"/></g>'
    b += f'<g transform="translate(256,152)"><path fill="{sub}" d="{P2}"/></g>'
    b += f'<rect fill="{l}" x="{256+W2+18}" y="144.5" width="{max(W1-W2-26, 20):.1f}" height="1.6"/>'
    out['horizontal'] = (Wh, 216, b)
    # vertical: símbolo, nome, endosso
    Wv = max(W1, 420) + 120; cx = Wv / 2
    b = simbolo(cx, 170, 112, c, rf, l, m)
    b += f'<g transform="translate({cx-W1/2:.1f},392)"><path fill="{c}" d="{P1}"/></g>'
    b += f'<g transform="translate({cx-W3/2:.1f},436)"><path fill="{sub}" d="{P3}"/></g>'
    out['vertical'] = (Wv, 470, b)
    out['logotipo'] = (W1 + 40, 130, f'<g transform="translate(20,102)"><path fill="{c}" d="{P1}"/></g>')
    # assinatura com tagline
    Wa = max(W1, WT) + 80
    b = f'<g transform="translate(40,110)"><path fill="{c}" d="{P1}"/></g><rect fill="{l}" x="40" y="138" width="56" height="2"/><g transform="translate(40,196)"><path fill="{sub}" d="{PT}"/></g>'
    out['assinatura'] = (Wa, 230, b)
    for k, (w, h, body) in out.items():
        fn = f'barzakh-{k}-{n}'
        open(f'{OUT}/svg/{fn}.svg', 'w').write(svg(w, h, body))
        open(f'/tmp/{fn}.svg', 'w').write(svg(w, h, body, bg))  # prévia com fundo
        files.append(fn)
# avatar: só o disco partido na linha
for n, bg, l, m, c in [('obsidiana', OBS, BRO, LAP, MAR), ('lapis', LAP, BRO, OBS, MAR), ('marfim', MAR, BRO, LAP, OBS)]:
    b = f'<rect width="400" height="400" fill="{bg}"/><path fill="{l}" d="M110,196 A90,90 0 0 1 290,196 Z"/><path fill="{m}" d="M110,204 A90,90 0 0 0 290,204 Z"/><rect fill="{c}" x="70" y="198" width="260" height="4"/>'
    if m == bg: b = b.replace(f'<path fill="{m}" d="M110,204', f'<path fill="none" stroke="{c}" stroke-width="3" d="M111.5,204')
    open(f'{OUT}/svg/barzakh-avatar-{n}.svg', 'w').write(svg(400, 400, b)); files.append(f'barzakh-avatar-{n}')
# endosso holding: "Barzakh · um estúdio Al Kántara"
print(len(files), 'svgs')
