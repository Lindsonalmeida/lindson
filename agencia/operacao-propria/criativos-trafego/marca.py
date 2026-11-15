# Uso: python3 gerar.py && node render.js && python3 previa.py
import os, random
random.seed(7)
D = os.path.dirname(os.path.abspath(__file__))

VERDE, TOMATE, CREME, ACAFRAO, CARVAO = '#1E5B3B', '#C8302B', '#F3EEE6', '#F2B33D', '#141311'
VERDE_ESC, CEU = '#123B26', '#0A63A8'
FOTO = lambda n: f'../../identidade/fotos-ia/hd/{n}.jpg'
REC = lambda n: f'../v3/recortes/{n}.webp'
V4 = lambda n: f'../../identidade/recortes-v4/{n}.png'

# ------------------------------------------------------------------ marca (mesmo desenho da v3/v4, gerar4.py)
def simbolo(tam, folha=VERDE, seta=CREME):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="{tam}" height="{tam}" style="display:block">'
            f'<path d="M18 86 C 14 50, 40 18, 86 14 C 86 58, 58 88, 18 86 Z" fill="{folha}"/>'
            f'<path d="M26 76 L44 58 L54 66 L72 40" fill="none" stroke="{seta}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<path d="M60 38 L74 38 L74 52" fill="none" stroke="{seta}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></svg>')

def logo(tam, cor=CREME, folha=None, seta=None):
    folha = folha or cor; seta = seta or (VERDE if cor == CREME else CREME)
    return (f'<div style="display:flex;align-items:center;gap:{tam * .26:.0f}px">{simbolo(tam * 1.15, folha, seta)}'
            f'<div style="font:800 {tam}px/0.9 \'Inter Tight\';letter-spacing:-.045em;color:{cor};white-space:nowrap">Orégano Turbo</div></div>')

def selo(tam, texto, bg=VERDE, fg=CREME, centro=None, fs=12.5):
    gid = 'g' + str(random.randint(0, 10 ** 9))
    centro = centro or simbolo(tam * .42, fg, bg)
    return (f'<div style="position:relative;width:{tam}px;height:{tam}px;border-radius:50%;background:{bg};box-shadow:0 0 0 {tam * .03:.0f}px {CREME},14px 16px 0 rgba(0,0,0,.28)">'
            f'<svg viewBox="0 0 200 200" width="{tam}" height="{tam}" style="position:absolute;inset:0">'
            f'<defs><path id="{gid}" d="M100 100 m-76 0 a76 76 0 1 1 152 0 a76 76 0 1 1 -152 0"/></defs>'
            f'<circle cx="100" cy="100" r="93" fill="none" stroke="{fg}" stroke-width="2.4"/><circle cx="100" cy="100" r="58" fill="none" stroke="{fg}" stroke-width="2.4"/>'
            f'<text font-family="IBM Plex Mono" font-weight="600" font-size="{fs}" letter-spacing="2.4" fill="{fg}"><textPath href="#{gid}">{texto}</textPath></text></svg>'
            f'<div style="position:absolute;inset:0;display:grid;place-items:center">{centro}</div></div>')

IC = {
 'fatia': '<path d="M16 24 Q50 8 84 24 L50 90 Z"/><path d="M14 22 Q50 4 86 22"/><circle cx="40" cy="36" r="6"/><circle cx="60" cy="42" r="5"/><circle cx="50" cy="62" r="5"/>',
 'folha': '<path d="M18 86 C 14 50, 40 18, 86 14 C 86 58, 58 88, 18 86 Z"/><path d="M28 74 L44 58 L54 66 L70 44"/><path d="M60 42 L71 42 L71 53"/>',
 'tomate': '<circle cx="50" cy="58" r="30"/><path d="M50 28 L40 16 M50 28 L60 16 M50 28 L50 12 M50 28 L34 26 M50 28 L66 26"/>',
 'pa': '<circle cx="50" cy="36" r="26"/><path d="M50 62 L50 94"/><circle cx="44" cy="32" r="4"/><circle cx="58" cy="40" r="4"/>',
 'pizza': '<circle cx="50" cy="50" r="36"/><circle cx="50" cy="50" r="28"/><path d="M50 14 L50 86 M14 50 L86 50 M25 25 L75 75 M75 25 L25 75"/>',
 'chama': '<path d="M50 90 C 24 90 20 62 38 44 C 38 58 46 60 50 52 C 50 36 60 24 56 10 C 76 26 82 50 76 66 C 72 82 62 90 50 90 Z"/>',
 'celular': '<rect x="30" y="10" width="40" height="80" rx="8"/><path d="M44 80 L56 80"/><path d="M40 34 L48 42 L62 28"/>',
 'caixa': '<path d="M12 40 L50 24 L88 40 L50 56 Z"/><path d="M12 40 L12 64 L50 80 L88 64 L88 40"/><path d="M50 56 L50 80"/>',
 'manjericao': '<path d="M50 90 C 50 70 50 50 50 30"/><path d="M50 60 C 30 60 22 46 24 34 C 40 34 50 44 50 60 Z"/><path d="M50 48 C 70 48 78 34 76 22 C 60 22 50 32 50 48 Z"/>',
}
def padrao(cor=CREME, op=.14, tam=300, w=4):
    pos = [('fatia', 30, 20, -18), ('tomate', 200, 30, 12), ('folha', 120, 130, 0), ('pa', 280, 150, 28), ('chama', 20, 200, 8),
           ('pizza', 190, 230, 0), ('manjericao', 300, 290, -20), ('celular', 90, 290, 10), ('caixa', 290, 40, -8)]
    g = ''.join(f'<g transform="translate({x} {y}) rotate({r} 30 30) scale(.6)">{IC[n]}</g>' for n, x, y, r in pos)
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{tam}" height="{tam}" viewBox="0 0 360 360"><g fill="none" stroke="{cor}" stroke-opacity="{op}" '
           f'stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round">{g}</g></svg>')
    return "url('data:image/svg+xml;utf8," + svg.replace('#', '%23').replace('"', '%22').replace('<', '%3C').replace('>', '%3E') + "')"

xadrez = lambda a, b, t=60: f'repeating-conic-gradient({a} 0 25%,{b} 0 50%) 0 0/{t * 2}px {t * 2}px'

# ------------------------------------------------------------------ peças de layout
A = lambda x, y, inner, extra='': f'<div class="a" style="left:{x}px;top:{y}px;{extra}">{inner}</div>'
BOX = lambda x, y, w, h, bg, extra='', inner='': f'<div class="a" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:{bg};{extra}">{inner}</div>'
IMG = lambda src, x, y, w, extra='': f'<img class="a" src="{src}" style="left:{x}px;top:{y}px;width:{w}px;height:auto;{extra}">'
SOMBRA_DURA = 'filter:drop-shadow(18px 22px 0 rgba(20,19,17,.30)) saturate(1.06) contrast(1.04)'
BAGEL = lambda t, s, cor, lh=.9, extra='': f'<div style="font:400 {s}px/{lh} \'Bagel Fat One\';letter-spacing:-.01em;color:{cor};text-transform:uppercase;white-space:nowrap;{extra}">{t}</div>'
ANTON = lambda t, s, cor, lh=.88, extra='': f'<div style="font:400 {s}px/{lh} Anton;letter-spacing:-.005em;color:{cor};text-transform:uppercase;white-space:nowrap;{extra}">{t}</div>'
MONO = lambda t, s, cor, extra='': f'<div style="font:600 {s}px/1.15 \'IBM Plex Mono\';letter-spacing:.14em;color:{cor};text-transform:uppercase;white-space:nowrap;{extra}">{t}</div>'
TXT = lambda t, s, cor, extra='': f'<div style="font:600 {s}px/1.25 Inter;color:{cor};{extra}">{t}</div>'
SH = lambda c=CARVAO, d=8: f'text-shadow:{d}px {d}px 0 {c}'

def foto(n, x=-4, y=0, w=1088):
    """Foto e recorte usam a MESMA caixa: a letra fica entre os dois e passa por trás do produto."""
    return IMG(FOTO(n), x, y, w)
def frente(n, x=-4, y=0, w=1088, extra=''):
    return IMG(REC(n), x, y, w, extra)

def adesivo(t, bg, fg, rot=0, s=30, pad='14px 24px', borda=CREME, extra=''):
    """Adesivo de vinil com borda de corte (die-cut) e sombra dura."""
    return (f'<div style="transform:rotate({rot}deg);background:{bg};color:{fg};padding:{pad};border-radius:999px;'
            f'box-shadow:0 0 0 7px {borda},10px 12px 0 7px rgba(20,19,17,.28);font:400 {s}px/1 \'Bagel Fat One\';'
            f'text-transform:uppercase;white-space:nowrap;letter-spacing:.01em;{extra}">{t}</div>')

def estrela(tam, bg, inner, rot=0, pontas=14):
    import math
    pts = []
    for i in range(pontas * 2):
        r = 50 if i % 2 == 0 else 41
        a = math.pi * i / pontas - math.pi / 2
        pts.append(f'{50 + r * math.cos(a):.2f}% {50 + r * math.sin(a):.2f}%')
    return (f'<div style="position:relative;width:{tam}px;height:{tam}px;transform:rotate({rot}deg);filter:drop-shadow(12px 14px 0 rgba(20,19,17,.3))">'
            f'<div style="position:absolute;inset:-8px;background:{CREME};clip-path:polygon({",".join(pts)})"></div>'
            f'<div style="position:absolute;inset:0;background:{bg};clip-path:polygon({",".join(pts)})"></div>'
            f'<div style="position:absolute;inset:0;display:grid;place-items:center;text-align:center">{inner}</div></div>')

def faixa(t, y, bg, fg, rot=0, h=96, s=60, x=-120, w=1400, fonte='Anton', sep='✦'):
    item = f'<span style="padding:0 26px">{t}</span><span style="opacity:.9">{sep}</span>'
    ff = "'Bagel Fat One'" if fonte == 'Bagel' else 'Anton'
    return (f'<div class="a" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:{bg};transform:rotate({rot}deg);'
            f'display:flex;align-items:center;overflow:hidden;box-shadow:0 12px 0 rgba(20,19,17,.25);border-top:5px solid {CARVAO};border-bottom:5px solid {CARVAO}">'
            f'<div style="font:400 {s}px/1 {ff};color:{fg};text-transform:uppercase;white-space:nowrap;letter-spacing:.01em">{item * 12}</div></div>')

def tarja_ass(y, bg=CARVAO, fg=CREME, direita='@oreganoturbo', h=92):
    """Assinatura de todas as peças: tarja com logo, @ e chamada."""
    return BOX(0, y, 1080, h, bg, 'display:flex;align-items:center;justify-content:space-between;padding:0 52px;',
               logo(34, fg) + MONO(direita, 19, fg))

IA = lambda cor=CREME, x=52, y=None, extra='': A(x, y, MONO('imagem ilustrativa · gerada por IA', 12, cor, 'opacity:.75;letter-spacing:.12em'), extra)
GRAO = '<div class="grao"></div>'
# Agrega da pesquisa de 08/11: cheese pull em fundo escuro (p01), ingredientes flutuando como capa de Reels (p03),
# carrossel de processo "Como funciona" em 7 telas (p06/c1–c7), tipografia gigante (p08, p10), humor de pizzaiolo (p10, p12).
# Foto: cada foto do kit aparece UMA vez só na v5 (a v4 repetia B2, B3 e A8). As peças novas são tipográficas.
TINTA = '#0F0E0C'
GRID = []   # ordem do feed (prévia 3×4)

def comanda(n, x=None, y=40, cor=CARVAO, papel=CREME, rot=3, txt='só pizzarias', s=64):
    """Etiqueta da campanha: comanda de pedido com picote."""
    picote = f'radial-gradient(circle at 8px 0,transparent 7px,{papel} 7.5px) -8px 0/16px 100% repeat-x'
    html = (f'<div style="transform:rotate({rot}deg);filter:drop-shadow(8px 10px 0 rgba(20,19,17,.30))">'
            f'<div style="height:10px;background:{picote}"></div>'
            f'<div style="background:{papel};padding:12px 22px 16px;text-align:center">'
            + MONO('Orégano Turbo · pedido', 14, cor, 'letter-spacing:.16em')
            + f'<div style="font:400 {s}px/1 \'Bagel Fat One\';color:{TOMATE};margin:4px 0 2px">Nº{n:02d}</div>'
            + MONO(txt, 14, cor, 'letter-spacing:.16em') + '</div></div>')
    return A(min(x if x is not None else 790, 786), y, html)

ZAP = lambda bg=TOMATE, fg=CREME, rot=-5, s=40: adesivo('Chama no zap ↗', bg, fg, rot, s)
FONTS = ('<link href="https://fonts.googleapis.com/css2?family=Anton&family=Bagel+Fat+One&family=Inter+Tight:wght@700;800'
         '&family=Inter:wght@500;600;700;800&family=IBM+Plex+Mono:ital,wght@0,500;0,600;1,600&display=swap" rel="stylesheet">')
GRAO_SVG = ("url(\"data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'><filter id='n'>"
            "<feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2' stitchTiles='stitch'/></filter>"
            "<rect width='300' height='300' filter='url(%23n)' opacity='.55'/></svg>\")")
CSS = ('body{margin:0;background:#777}section.f{position:relative;overflow:hidden;margin:0 0 40px}.a{position:absolute}*{box-sizing:border-box}'
       f'.grao{{position:absolute;inset:0;background:{GRAO_SVG};mix-blend-mode:overlay;opacity:.22;pointer-events:none}}')
