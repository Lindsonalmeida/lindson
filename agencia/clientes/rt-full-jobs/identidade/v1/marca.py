"""Marca Real Time v1 (conta Pedro, 03/11/2026). Gera os SVGs da marca com o texto em curvas.
Pedido do Lindson (03/11): "refaça a logo e o manual de marca" + "siga o mesmo padrão premium do Dublê, sempre".
Copiado de: (1) os cantos de enquadramento do logo atual da RT (o que a marca já tem de reconhecível);
(2) o método da marca do Dublê (wordmark minúsculo geométrico em Geist + um único acento);
(3) o ponto vermelho de gravação (REC) das câmeras, que é literalmente "tempo real".
uso: python3 marca.py <pasta das fontes Geist> -> marca/*.svg"""
import os, sys
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

FONTES = sys.argv[1] if len(sys.argv) > 1 else '.'
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'marca'); os.makedirs(OUT, exist_ok=True)
C = dict(preto='#05070B', grafite='#11161F', branco='#F4F7FB', azul='#2E9BFF', indigo='#4338F0', rec='#FF3B3B')


def texto(fonte, s, tam, x=0, y=0, track=0.0):
    """Texto -> path SVG (y = linha de base). track em fração do tamanho."""
    f = TTFont(os.path.join(FONTES, fonte)); gs = f.getGlyphSet(); cmap = f.getBestCmap(); upm = f['head'].unitsPerEm
    esc = tam / upm; d = []; cx = x
    for ch in s:
        g = cmap.get(ord(ch))
        if g is None: continue
        pen = SVGPathPen(gs); tp = TransformPen(pen, (esc, 0, 0, -esc, cx, y)); gs[g].draw(tp)
        d.append(pen.getCommands()); cx += gs[g].width * esc + track * tam
    return ' '.join(d), cx - x - track * tam


def cantos(x, y, w, h, perna, esp, cor):
    """Os 4 cantos de enquadramento (visor da câmera)."""
    p = []
    for (cx, cy, sx, sy) in [(x, y, 1, 1), (x + w, y, -1, 1), (x, y + h, 1, -1), (x + w, y + h, -1, -1)]:
        p.append(f'M{cx} {cy + sy * perna}V{cy}H{cx + sx * perna}')
    return f'<path d="{" ".join(p)}" fill="none" stroke="{cor}" stroke-width="{esp}" stroke-linecap="square"/>'


def simbolo(fundo=None, quadro=C['branco'], r=C['branco'], t=C['azul'], rec=C['rec'], tam=240):
    """Símbolo: visor com 'rt' dentro e o ponto REC no canto de cima."""
    dr, wr = texto('Geist-700.ttf', 'r', 118, 0, 0, -.02)
    dt, wt = texto('Geist-700.ttf', 't', 118, 0, 0, -.02)
    larg = wr + wt - 4; x0 = 120 - larg / 2
    dr, _ = texto('Geist-700.ttf', 'r', 118, x0, 156); dt, _ = texto('Geist-700.ttf', 't', 118, x0 + wr - 4, 156)
    bg = f'<rect width="240" height="240" rx="52" fill="{fundo}"/>' if fundo else ''
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 240" width="{tam}" height="{tam}">{bg}'
            f'{cantos(38, 38, 164, 164, 38, 12, quadro)}<path d="{dr}" fill="{r}"/><path d="{dt}" fill="{t}"/>'
            f'<circle cx="182" cy="62" r="10.5" fill="{rec}"/></svg>')


def palavra(c1=C['branco'], c2=C['azul'], rec=C['rec'], tag=True, ctag=None):
    """Wordmark 'realtime': 'real' + 'time' em duas cores; o pingo do i é o ponto REC."""
    T = 120
    d1, w1 = texto('Geist-600.ttf', 'real', T, 0, 120, -.035)
    dt, wt = texto('Geist-600.ttf', 't', T, w1 + T * -.035, 120, -.035)
    xi = w1 + T * -.035 + wt + T * -.035
    di, wi = texto('Geist-600.ttf', 'ı', T, xi, 120, -.035)          # i sem pingo
    xm = xi + wi + T * -.035
    dm, wm = texto('Geist-600.ttf', 'me', T, xm, 120, -.035)
    W = xm + wm
    cx = xi + wi / 2
    svg = [f'<path d="{d1}" fill="{c1}"/>', f'<path d="{dt} {di} {dm}" fill="{c2}"/>', f'<circle cx="{cx:.1f}" cy="30" r="12.5" fill="{rec}"/>']
    H = 150
    if tag:
        dg, wg = texto('GeistMono-500.ttf', 'FULL JOBS', 26, 4, 178, .32)
        svg.append(f'<path d="{dg}" fill="{ctag or c1}" fill-opacity=".72"/>'); H = 190
    return W, H, ''.join(svg)


def wordmark(**k):
    W, H, s = palavra(**k)
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-6 0 {W + 12:.0f} {H}" width="{W + 12:.0f}" height="{H}">{s}</svg>'


def horizontal(c1=C['branco'], c2=C['azul'], quadro=C['branco'], **k):
    W, H, s = palavra(c1=c1, c2=c2, **k)
    sim = simbolo(quadro=quadro, r=c1, t=c2).split('>', 1)[1].rsplit('</svg>', 1)[0]
    LW = 200 + 36 + W
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {LW:.0f} 200" width="{LW:.0f}" height="200">'
            f'<g transform="translate(-20 -20)">{sim}</g><g transform="translate(236 {100 - H / 2 + 8:.0f})">{s}</g></svg>')


def vertical(c1=C['branco'], c2=C['azul'], quadro=C['branco'], **k):
    W, H, s = palavra(c1=c1, c2=c2, **k)
    sim = simbolo(quadro=quadro, r=c1, t=c2).split('>', 1)[1].rsplit('</svg>', 1)[0]
    LW = max(W, 240) + 20
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {LW:.0f} {250 + H}" width="{LW:.0f}" height="{250 + H}">'
            f'<g transform="translate({LW / 2 - 120:.0f} 0)">{sim}</g><g transform="translate({(LW - W) / 2:.0f} 250)">{s}</g></svg>')


if __name__ == '__main__':
    arqs = {
        'simbolo.svg': simbolo(),
        'simbolo-app.svg': simbolo(fundo=C['preto']),
        'simbolo-azul.svg': simbolo(fundo=C['azul'], quadro=C['branco'], r=C['branco'], t=C['preto'], rec=C['branco']),
        'simbolo-mono-branco.svg': simbolo(quadro=C['branco'], r=C['branco'], t=C['branco'], rec=C['branco']),
        'simbolo-mono-preto.svg': simbolo(quadro=C['preto'], r=C['preto'], t=C['preto'], rec=C['preto']),
        'wordmark.svg': wordmark(),
        'wordmark-claro.svg': wordmark(c1=C['preto'], c2='#1F7BE0'),
        'assinatura-horizontal.svg': horizontal(),
        'assinatura-horizontal-claro.svg': horizontal(c1=C['preto'], c2='#1F7BE0', quadro=C['preto']),
        'assinatura-horizontal-mono-branco.svg': horizontal(c1=C['branco'], c2=C['branco'], quadro=C['branco'], rec=C['branco'], ctag=C['branco']),
        'assinatura-vertical.svg': vertical(),
        'favicon.svg': simbolo(fundo=C['preto'], tam=64),
    }
    for n, s in arqs.items():
        open(os.path.join(OUT, n), 'w').write(s)
    print(len(arqs), 'arquivos em', OUT)
