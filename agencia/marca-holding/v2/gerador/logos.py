# Al Kántara Group v2 · logos em curvas (conta Pedro, 16/11/2026)
import os, json
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from simbolo import pecas, path
B = os.path.dirname(os.path.abspath(__file__)) + '/..'
FS = B + '/fontes/InterTight-SemiBold.ttf'; FM = B + '/fontes/InterTight-Medium.ttf'
# kerning óptico ajustado à mão (unidades de em/1000), aplicado sobre o tracking
KERN = {('A','L'): -10, ('L',' '): -40, (' ','K'): -10, ('K','Á'): -38, ('Á','N'): 4, ('N','T'): -6, ('T','A'): -62, ('A','R'): -12, ('R','A'): -30, ('G','R'):0, ('O','U'):6}
def texto(ff, s, size, x0, y0, track):
    f = TTFont(ff); gs = f.getGlyphSet(); cm = f.getBestCmap(); upm = f['head'].unitsPerEm; sc = size/upm
    pen = SVGPathPen(gs); x = 0
    for i, ch in enumerate(s):
        g = cm[ord(ch)]
        gs[g].draw(TransformPen(pen, (sc,0,0,-sc,x0+x*sc,y0)))
        x += gs[g].width + track*upm/1000
        if i+1 < len(s): x += KERN.get((ch, s[i+1]), 0)*upm/1000
    return pen.getCommands(), x*sc - track*size/1000
CORES = {'positivo': ('#0B0C0E', None), 'negativo': ('#EFEAE1', None), 'mono-preto': ('#000000', None), 'mono-branco': ('#FFFFFF', None), 'latao': ('#B8955A', None)}
DIV = [('labs','#2E4BFF'),('studio','#E8461E'),('media','#F0A202'),('ventures','#0E8C66')]
def simb(s, ox, oy, cor, destaque=None, idx=None):
    out = ''
    for i, p in enumerate(pecas()):
        c = destaque if (idx is not None and i == idx) else cor
        out += f'<path fill="{c}" d="{path(p, s, ox, oy)}"/>'
    return out
def svg(w, h, body): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.0f} {h:.0f}" width="{w:.0f}" height="{h:.0f}">{body}</svg>'
def wordmark(cor, x, y, cap, sub='GROUP'):
    d, w = texto(FS, 'AL KÁNTARA', cap/0.727, x, y, 40)
    d2, w2 = texto(FM, sub, cap*0.36/0.727, x + w - 0, y + cap*0.66, 420) if sub else ('', 0)
    # GROUP alinhado à direita da wordmark
    if sub:
        d2, w2 = texto(FM, sub, cap*0.36/0.727, x + w - w2, y + cap*0.66, 420)
    return f'<path fill="{cor}" d="{d}"/><path fill="{cor}" d="{d2}"/>', w
def gerar():
    out = {}
    for nome, (cor, _) in CORES.items():
        S = 20  # módulo
        out[f'simbolo-{nome}'] = svg(24*S, 24*S, simb(S, 0, 0, cor))
        wm, w = wordmark(cor, 0, 128, 100)
        out[f'wordmark-{nome}'] = svg(w+4, 212, wm)
        # horizontal: símbolo altura = 1,9 x altura de caixa alta; espaço = 1 pedra (8 mód)
        s = 190/24; wm, w = wordmark(cor, 24*s + 8*s*0.9, 116, 100)
        out[f'horizontal-{nome}'] = svg(24*s + 8*s*0.9 + w + 4, 190, simb(s, 0, 0, cor))
        out[f'horizontal-{nome}'] = svg(24*s + 8*s*0.9 + w + 4, 192, simb(s,0,0,cor) + wm)
        s = 12; wm, w = wordmark(cor, 0, 0, 70)
        sw = 24*s; tot = max(sw, w)
        wm, w = wordmark(cor, (tot-w)/2, sw + 150, 70)
        out[f'vertical-{nome}'] = svg(tot, sw + 220, simb(s, (tot-sw)/2, 0, cor) + wm)
    for i, (d, c) in enumerate(DIV):
        for nome, cor in [('positivo','#0B0C0E'), ('negativo','#EFEAE1')]:
            S = 20
            out[f'div-{d}-simbolo-{nome}'] = svg(480, 480, simb(S,0,0,cor,c,i))
            s = 190/24; wm, w = wordmark(cor, 24*s+7*s, 116, 100, d.upper())
            out[f'div-{d}-horizontal-{nome}'] = svg(24*s+7*s+w+4, 192, simb(s,0,0,cor,c,i)+wm)
    for k, v in out.items(): open(f'{B}/logos/svg/alkantara-{k}.svg','w').write(v)
    return out
if __name__ == '__main__':
    print(len(gerar()))
