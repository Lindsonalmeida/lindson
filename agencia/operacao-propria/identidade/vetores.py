# Vetores da Orégano Turbo com o texto em curvas (sem depender de fonte instalada). Conta Leandro, 05/11/2026.
# Uso: python3 vetores.py <pasta com Fraunces.ttf e DMSans.ttf>   → marca-v2/*.svg
# Fontes oficiais do Google Fonts (google/fonts, licença OFL). Precisa de fonttools (pip install fonttools).
import sys, os, math, io
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gerar2 import folha, VERDE, AMARELO, CREME, TOMATE
F = sys.argv[1]; OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'marca-v2'); os.makedirs(OUT, exist_ok=True)
def inst(arq, eixos):
    f = TTFont(os.path.join(F, arq)); return instantiateVariableFont(f, eixos)
DM = inst('DMSans.ttf', {'wght': 700, 'opsz': 14})
FR = inst('Fraunces.ttf', {'wght': 900, 'opsz': 144, 'SOFT': 100, 'WONK': 1})
def glifo(font, ch):
    cmap = font.getBestCmap(); g = cmap.get(ord(ch)); gs = font.getGlyphSet()
    return g, gs, font['hmtx'][g][0] if g else 0
def texto_reto(font, txt, tam, x0=0, y0=0, espaco=0):
    """Texto em linha reta → path SVG (y para baixo)."""
    upm = font['head'].unitsPerEm; s = tam / upm; x = x0; d = []
    for ch in txt:
        g, gs, adv = glifo(font, ch)
        if g:
            pen = SVGPathPen(gs); gs[g].draw(TransformPen(pen, (s, 0, 0, -s, x, y0))); d.append(pen.getCommands())
        x += adv * s + espaco
    return ' '.join(d), x - x0
def texto_circulo(font, txt, tam, cx, cy, r, comprimento=None):
    """Texto em volta do círculo, no sentido horário, começando à esquerda (igual ao textPath do selo)."""
    upm = font['head'].unitsPerEm; s = tam / upm
    larg = [glifo(font, ch)[2] * s for ch in txt]; total = sum(larg)
    circ = comprimento or 2 * math.pi * r; extra = (circ - total) / len(txt)  # espaço distribuído (lengthAdjust=spacing)
    d = []; pos = 0
    for ch, w in zip(txt, larg):
        g, gs, _ = glifo(font, ch); meio = pos + w / 2
        ang = math.pi + meio / r  # começa no lado esquerdo (180°) e segue no sentido horário
        px, py = cx + r * math.cos(ang), cy + r * math.sin(ang); rot = ang + math.pi / 2
        if g:
            c, sn = math.cos(rot), math.sin(rot)
            # glifo: x de -w/2 a w/2, linha de base em 0; escala com y invertido; depois gira e leva para (px, py)
            m = (s * c, s * sn, s * sn, -s * c, px - (w / 2) * c, py - (w / 2) * sn)
            pen = SVGPathPen(gs); gs[g].draw(TransformPen(pen, m)); d.append(pen.getCommands())
        pos += w + extra
    return ' '.join(d)
def folha_g(cor):
    return folha(cor, 9).split('>', 1)[1].rsplit('</svg>', 1)[0]
def selo_svg(fundo, tinta, borda=True, transparente=False):
    r = 91
    letras = texto_circulo(DM, 'ORÉGANO TURBO · MKT PARA PIZZARIAS · ', 17.2, 120, 120 + 5.8, r, 2 * math.pi * r - 6)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 240" width="1200" height="1200">'
            + ('' if transparente else f'<circle cx="120" cy="120" r="118" fill="{fundo}"/>')
            + (f'<circle cx="120" cy="120" r="111" fill="none" stroke="{tinta}" stroke-width="2.4"/><circle cx="120" cy="120" r="72" fill="none" stroke="{tinta}" stroke-width="2.4"/>' if borda else '')
            + f'<path d="{letras}" fill="{tinta}"/>'
            + f'<g transform="translate(66 66) scale(.54)"><g fill="none" stroke="{tinta}" stroke-width="9" stroke-linecap="round" stroke-linejoin="round">{folha_g(tinta)}</g></g></svg>')
def nome_svg(cor):
    d, w = texto_reto(FR, 'orégano turbo', 100, 10, 110, -3.5)
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {int(w) + 20} 140" width="{int(w) * 3}" height="420"><path d="{d}" fill="{cor}"/></svg>'
arquivos = {
    'selo-amarelo-verde.svg': selo_svg(AMARELO, VERDE), 'selo-verde-amarelo.svg': selo_svg(VERDE, AMARELO), 'selo-creme-tomate.svg': selo_svg(CREME, TOMATE, borda=False),
    'selo-carimbo-verde-transparente.svg': selo_svg('none', VERDE, transparente=True), 'selo-carimbo-tomate-transparente.svg': selo_svg('none', TOMATE, transparente=True),
    'nome-verde.svg': nome_svg(VERDE), 'nome-creme.svg': nome_svg(CREME), 'nome-amarelo.svg': nome_svg(AMARELO),
    'personagem-verde.svg': folha(VERDE, 9).replace('viewBox="0 0 200 200"', 'viewBox="0 0 200 200" width="1000" height="1000"'),
    'personagem-amarelo.svg': folha(AMARELO, 9).replace('viewBox="0 0 200 200"', 'viewBox="0 0 200 200" width="1000" height="1000"'),
    'personagem-uau-verde.svg': folha(VERDE, 9, 'uau').replace('viewBox="0 0 200 200"', 'viewBox="0 0 200 200" width="1000" height="1000"'),
    'personagem-piscada-verde.svg': folha(VERDE, 9, 'piscada').replace('viewBox="0 0 200 200"', 'viewBox="0 0 200 200" width="1000" height="1000"'),
}
for n, svg in arquivos.items(): open(os.path.join(OUT, n), 'w').write(svg)
print(len(arquivos), 'vetores em', OUT)
