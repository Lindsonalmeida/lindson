# Kit de rede social v5 do @oreganoturbo · Rocco (campanha) + Paollo (pizzaria) · conta Zuleide · 08/11/2026
# Pedido do Lindson (08/11): "use pra agregar e melhorar tudo que for possível. Use nossos agentes." Base: v4 (../v4) sobre a v3 aprovada.
# Base: kit v3 aprovado ("ESSE É O PADRÃO", ../v3). Pesquisa: ../../biblioteca-pizzaria/PESQUISA-08-11-IDENTIDADES-E-SOCIAL.md
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

P = []  # (id, w, h, html)
post = lambda i, h: P.append((i, 1080, 1350, h + GRAO))
story = lambda i, h: P.append((i, 1080, 1920, h + GRAO))
# ================================================================== v5 · o que muda (Rocco na campanha, Paollo no vocabulário de pizzaria)
# Mantém da v4: comanda "PEDIDO Nº" como conceito, paleta fixa, Bagel Fat One nas manchetes, texto nunca cobrindo a pizza.
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
outline = lambda t, s, cor, w=4, op=1, extra='': (f'<div style="font:400 {s}px/.85 \'Bagel Fat One\';color:transparent;-webkit-text-stroke:{w}px {cor};'
                                                 f'opacity:{op};text-transform:uppercase;white-space:nowrap;{extra}">{t}</div>')
def feed(i, h): post(i, h); GRID.append(i)
carr = lambda i, h: P.append((i, 1080, 1350, h + GRAO))
FUNDO = lambda cor, pad=CREME, op=.08: BOX(0, 0, 1080, 1350, cor) + f'<div class="a" style="inset:0;background:{padrao(pad, op, 300)}"></div>'
picote = lambda papel, t=9: f'<div style="height:{t + 3}px;background:radial-gradient(circle at {t}px 0,transparent {t - 1}px,{papel} {t - .5}px) -{t}px 0/{2 * t}px 100% repeat-x"></div>'

# ================================================================== 01 · FOTO QUE DÁ FOME · cheese pull em fundo escuro (B1)
# Pesquisa §2 nº2 (cheese pull, luz lateral, fundo preto) + HOTWHIZ (boca mordendo, flash). O queijo vira o herói contra o preto.
feed('p01-foto-que-da-fome',
     BOX(0, 0, 1080, 1350, TINTA) +
     f'<div class="a" style="inset:0;background:radial-gradient(ellipse 60% 55% at 72% 42%,rgba(242,179,61,.38) 0,rgba(200,48,43,.16) 45%,transparent 75%)"></div>' +
     f'<div class="a" style="left:0;top:0;width:14px;height:1350px;background:{TOMATE}"></div>' +
     A(40, 40, MONO('Pedido nº01 · cheese pull', 18, ACAFRAO)) +
     A(34, 80, BAGEL('Foto que dá', 116, CREME, .9)) +
     A(22, 172, BAGEL('fome.', 250, TOMATE, .84, 'letter-spacing:-.02em')) +
     frente('B1-mordida', x=50, y=300, w=1060, extra='-webkit-mask-image:linear-gradient(to bottom,transparent 0,#000 24%);filter:contrast(1.08) saturate(1.12) drop-shadow(-30px 0 60px rgba(242,179,61,.25))') +
     comanda(1, x=40, y=440, rot=-5, txt='queijo esticando') +
     A(640, 1120, ZAP(TOMATE, CREME, -5, 40)) +
     A(40, 650, MONO('foto e vídeo de pizzaria<br>gravados na sua cozinha', 20, CREME, f'line-height:1.45;background:{TINTA};padding:12px 16px;border-left:6px solid {ACAFRAO}')) +
     tarja_ass(1258, CREME, CARVAO, 'imagem gerada por IA · @oreganoturbo'))

# ================================================================== 02 · TERÇA TAMBÉM TEM FOME (B2 caixa) · melhoria: semana inteira na lateral, sem vazio
# Pinterest nº3 (texto enorme, produto cortado na borda) + Decaf Girl (produto na mão em direção à câmera).
dias = [('Seg', 1), ('Ter', 1), ('Qua', 1), ('Qui', 0), ('Sex', 0), ('Sáb', 0), ('Dom', 0)]
semana = ''.join(f'<div style="display:flex;align-items:center;gap:12px;height:96px;border-bottom:3px solid {CARVAO}">'
                 f'<span style="font:400 54px/1 \'Bagel Fat One\';color:{TOMATE if f else VERDE};text-transform:uppercase;width:150px">{d}</span>'
                 + (MONO('dia fraco', 15, CREME, f'background:{TOMATE};padding:6px 8px') if f else MONO('cheio', 15, VERDE, 'opacity:.7')) + '</div>' for d, f in dias)
feed('p02-terca-tambem-tem-fome',
     FUNDO(CREME, TOMATE, .09) +
     A(30, 34, BAGEL('Terça', 300, TOMATE, .84, SH(TINTA, 10))) +
     A(40, 322, BAGEL('também tem fome.', 64, VERDE, .9)) +
     A(40, 420, f'<div style="width:330px;border-top:3px solid {CARVAO}">{semana}</div>') +
     IMG(REC('B2-caixa-ceu-bb'), 330, 400, 820, 'filter:drop-shadow(-22px 26px 0 rgba(20,19,17,.24)) saturate(1.06)') +
     comanda(2, x=786, y=300, rot=5, txt='dia fraco') +
     A(40, 1130, ZAP(TOMATE, CREME, -4, 40)) +
     tarja_ass(1258, VERDE, CREME, 'imagem gerada por IA · @oreganoturbo'))

# ================================================================== 03 · CAPA DE REELS · PIZZA NO AR (B3, ingredientes flutuando)
# Pesquisa §2 nº8 (ingredientes explodindo em volta, fundo de 1 cor, capa de Reels) + Pinterest nº4 (nome girando em volta)
# + Drip Riot (produto voando). Fundo verde = complementar ao vermelho da pizza. Área segura do grid: y 285–1635.
gid = 'anel03'
anel = (f'<svg viewBox="0 0 1000 1000" width="1040" height="1040"><defs><path id="{gid}" d="M500 500 m-440 0 a440 440 0 1 1 880 0 a440 440 0 1 1 -880 0"/></defs>'
        f'<text font-family="Bagel Fat One" font-size="62" letter-spacing="5" fill="{CREME}"><textPath href="#{gid}">SÓ PIZZARIAS ✦ SÓ PIZZARIAS ✦ SÓ PIZZARIAS ✦ SÓ PIZZARIAS ✦ </textPath></text></svg>')
play = (f'<div style="width:120px;height:120px;border-radius:50%;background:{TOMATE};box-shadow:0 0 0 8px {CREME},10px 12px 0 8px rgba(20,19,17,.3);display:grid;place-items:center">'
        f'<div style="width:0;height:0;border-left:44px solid {CREME};border-top:28px solid transparent;border-bottom:28px solid transparent;margin-left:12px"></div></div>')
story('p03-reels-pizza-no-ar',
      BOX(0, 0, 1080, 1920, VERDE) +
      f'<div class="a" style="inset:0;background:radial-gradient(circle at 50% 54%,#2E8A58 0,{VERDE} 45%,{VERDE_ESC} 100%)"></div>' +
      A(-80, 40, outline('Pizza pizza', 250, CREME, 4, .22)) + A(-200, 1660, outline('Pizza pizza', 250, CREME, 4, .22)) +
      A(48, 300, MONO('Reels · imagem gerada por IA', 22, VERDE, f'background:{CREME};padding:10px 14px;box-shadow:6px 6px 0 {TINTA}')) +
      A(40, 356, BAGEL('Pizza', 210, CREME, .86, SH(TINTA, 10))) +
      A(400, 520, BAGEL('no ar.', 190, ACAFRAO, .86, SH(TINTA, 8))) +
      A(20, 700, anel, 'transform:rotate(-12deg)') +
      IMG(REC('B3-pizza-voando-bb'), 130, 720, 820, f'transform:rotate(-8deg);{SOMBRA_DURA}') +
      A(900, 1640, play) +
      comanda(3, x=820, y=290, rot=5, txt='aperta o play') +
      BOX(0, 1760, 1080, 160, CARVAO, 'display:flex;align-items:center;justify-content:space-between;padding:0 52px', logo(40, CREME) + MONO('@oreganoturbo', 20, CREME)))

# ================================================================== 04 · MENOS APP. MAIS ZAP. (A8) · melhoria: adesivo "taxa do app" riscado no lugar do vazio
feed('p04-menos-app-mais-zap',
     FUNDO(TOMATE, CREME, .11) +
     A(44, 40, BAGEL('Menos', 110, CREME, .9)) + A(36, 140, BAGEL('app.', 190, ACAFRAO, .9, SH(TINTA, 9))) +
     comanda(4, x=830, y=40) +
     IMG(REC('A8-adesivo-pedido-saindo'), 238, 346, 842, 'filter:drop-shadow(-20px 24px 0 rgba(20,19,17,.28))') +
     faixa('pedido direto no zap', 360, CREME, VERDE, -3, 100, 58, sep='✦') +
     A(36, 520, adesivo('<s style="text-decoration-thickness:6px">Taxa do app</s>', CARVAO, CREME, -8, 34, '18px 26px')) +
     A(40, 650, adesivo('Cliente<br>é seu', CREME, TOMATE, 5, 40, '20px 30px', extra='border-radius:30px;line-height:1.02;text-align:center')) +
     A(40, 830, adesivo('Sem comissão<br>no pedido', VERDE, CREME, -5, 30, '18px 24px', extra='border-radius:26px;line-height:1.05;text-align:center')) +
     A(40, 1000, BAGEL('Mais', 110, CREME, .9, SH(TINTA, 6))) +
     A(30, 1080, BAGEL('zap.', 230, CREME, .9, SH(TINTA, 11))) +
     IA(CREME, 600, 1316))

# ================================================================== 05 · RAIO-X (fatia escaneada, carvão)
# Pinterest nº9 (fundo preto, lettering amarelo e branco). Ideia nova: a faixa do scanner passa pela fatia e mostra a "radiografia".
ESC = 'filter:grayscale(1) invert(1) contrast(1.35) brightness(1.05) sepia(.25)'
fatia = lambda extra='': IMG(V4('pepperoni-fatia'), 540, 420, 760, f'transform:rotate(18deg);{extra}')
itens5 = ['Instagram e Google', 'iFood e cardápio', 'WhatsApp', '3 concorrentes do bairro', 'Plano de 30 dias']
lista5 = ''.join(f'<div style="display:flex;align-items:center;gap:14px;padding:12px 0;border-bottom:2px dashed rgba(20,19,17,.25)">'
                 f'<span style="font:600 19px \'IBM Plex Mono\';color:{TOMATE}">{i + 1:02d}</span>'
                 f'<span style="font:700 28px/1.05 Inter;color:{CARVAO}">{t}</span></div>' for i, t in enumerate(itens5))
ticket5 = (f'<div style="width:480px;transform:rotate(-2deg);filter:drop-shadow(14px 16px 0 rgba(0,0,0,.5))">' + picote(CREME) +
           f'<div style="background:{CREME};padding:22px 34px 26px">' + MONO('Comanda nº05 · o que eu olho', 17, TOMATE) + lista5 +
           f'<div style="display:flex;justify-content:space-between;align-items:center;margin-top:18px">'
           + BAGEL('R$ 297', 64, TOMATE, 1) + MONO('abatido no<br>1º mês se<br>fechar em<br>7 dias', 15, CARVAO, 'line-height:1.5;text-align:right') + '</div></div></div>')
feed('p05-raio-x-scanner',
     FUNDO(TINTA, CREME, .05) +
     fatia(f'filter:drop-shadow(18px 22px 0 rgba(0,0,0,.55)) saturate(1.1)') +
     f'<div class="a" style="left:0;top:720px;width:1080px;height:230px;overflow:hidden">'
     f'<img src="{V4("pepperoni-fatia")}" style="position:absolute;left:540px;top:-300px;width:760px;transform:rotate(18deg);{ESC}"></div>' +
     BOX(450, 712, 700, 8, ACAFRAO, 'box-shadow:0 0 24px 6px rgba(242,179,61,.7)') + BOX(450, 950, 700, 8, ACAFRAO, 'box-shadow:0 0 24px 6px rgba(242,179,61,.7)') +
     A(930, 740, MONO('scan', 20, ACAFRAO)) +
     A(40, 40, MONO('Pizzarias de São Luís - MA', 20, ACAFRAO)) +
     A(30, 76, BAGEL('Raio-X', 270, CREME, .86)) +
     A(40, 310, BAGEL('da sua pizzaria.', 86, ACAFRAO, .9)) +
     comanda(5, x=830, y=40, rot=4, txt='diagnóstico') +
     A(36, 450, ticket5) +
     A(40, 1010, adesivo('Entregue em vídeo', VERDE, CREME, -4, 34, '14px 24px')) +
     A(60, 1130, ZAP(TOMATE, CREME, -3, 40)) +
     tarja_ass(1258, VERDE, CREME, 'fatia: MVS9966, CC BY 3.0 · @oreganoturbo'))

# ================================================================== 06 · CARROSSEL "COMO FUNCIONA" (7 telas; a capa entra no feed)
# Pesquisa §2 nº3 (carrossel de processo: da bolinha de massa até a fatia) + Impasto (um conceito: cada passo é uma comanda).
# Cada tela tem composição diferente: pilha de comandas · número gigante · filme · radar · celular · recibo · comanda gigante.
passos = [('01', 'Raio-X', TOMATE), ('02', 'Gravação', VERDE), ('03', 'Anúncio no bairro', TOMATE), ('04', 'Pedido no zap', VERDE), ('05', 'Relatório de segunda', TOMATE)]
def mini_comanda(n, t, cor, rot):
    return (f'<div style="width:620px;transform:rotate({rot}deg);filter:drop-shadow(10px 12px 0 rgba(20,19,17,.28))">' + picote('#fff') +
            f'<div style="background:#fff;padding:14px 26px;display:flex;align-items:center;gap:22px;border-left:14px solid {cor}">'
            f'<span style="font:400 66px/1 \'Bagel Fat One\';color:{cor}">{n}</span>'
            f'<span style="font:800 44px/1 \'Inter Tight\';color:{CARVAO};letter-spacing:-.02em">{t}</span></div></div>')
pilha = ''.join(A(0, i * 128, mini_comanda(n, t, c, [-3, 2, -2, 3, -1][i])) for i, (n, t, c) in enumerate(passos))
SETA = lambda bg=CARVAO, fg=CREME: adesivo('Arrasta →', bg, fg, -4, 34, '14px 26px')
PAG = lambda k, cor: A(940, 1290, MONO(f'{k}/7', 22, cor))
carr('c1-capa-como-funciona',
     FUNDO(CREME, VERDE, .09) +
     BOX(0, 0, 1080, 30, xadrez(TOMATE, CREME, 15)) +
     A(36, 60, BAGEL('Como', 170, VERDE, .86)) +
     A(30, 200, BAGEL('funciona.', 196, TOMATE, .86, SH(TINTA, 9))) +
     A(44, 410, MONO('o método Orégano em 5 pedidos', 24, CARVAO, f'background:{ACAFRAO};padding:10px 14px')) +
     A(330, 510, pilha) +
     A(40, 520, outline('5', 640, VERDE, 6, .9, 'line-height:.8')) +
     comanda(6, x=830, y=60, rot=5, txt='como funciona') +
     A(60, 1170, SETA()) +
     PAG(1, CARVAO) +
     A(40, 1300, MONO('@oreganoturbo · só pizzarias', 16, CARVAO, 'opacity:.75')))
GRID.append('c1-capa-como-funciona')

chk = lambda t, cor_ck, cor_t, s=40: (f'<div style="display:flex;gap:18px;align-items:center;margin-top:16px">'
                                      f'<span style="flex:none;width:52px;height:52px;border-radius:50%;background:{cor_ck};display:grid;place-items:center;font:800 28px Inter;color:{CARVAO}">✓</span>'
                                      f'<span style="font:700 {s}px/1.05 Inter;color:{cor_t}">{t}</span></div>')
carr('c2-passo-1-raio-x',
     FUNDO(TINTA, CREME, .05) +
     A(380, -120, outline('01', 900, TOMATE, 8, 1, 'line-height:1')) +
     A(44, 50, MONO('Passo 01 · diagnóstico', 22, ACAFRAO)) +
     A(36, 100, BAGEL('Raio-X.', 220, CREME, .86)) +
     A(44, 330, TXT('Antes de anunciar, eu olho a pizzaria inteira.', 38, CREME, 'width:640px;line-height:1.2')) +
     A(44, 470, ''.join(chk(t, ACAFRAO, CREME) for t in ['Instagram e Google', 'iFood e cardápio', 'WhatsApp', '3 concorrentes do bairro', 'Plano de 30 dias'])) +
     BOX(0, 1010, 1080, 230, TOMATE, f'border-top:6px solid {ACAFRAO};display:flex;align-items:center;gap:34px;padding:0 44px',
         BAGEL('R$ 297', 120, CREME, 1, SH(TINTA, 7)) + MONO('abatido no 1º mês<br>se fechar em 7 dias<br>entrega em vídeo', 22, CREME, 'line-height:1.5')) +
     A(44, 1280, MONO('Orégano Turbo · como funciona', 16, CREME, 'opacity:.7')) + PAG(2, CREME))

cenas = ['queijo esticando', 'forno aceso', 'caixa saindo', 'massa no ar', 'motoboy na rua', 'mesa cheia']
quadro = lambda t: (f'<div style="flex:none;width:300px;height:220px;background:{CREME};border:5px solid {CARVAO};display:flex;flex-direction:column;justify-content:space-between;padding:16px 18px">'
                    + MONO('cena', 16, TOMATE) + f'<div style="font:400 40px/.95 \'Bagel Fat One\';color:{CARVAO};text-transform:uppercase">{t}</div></div>')
filme = lambda ts: (f'<div style="display:flex;gap:22px;padding:34px 30px;background:{CARVAO};width:max-content;'
                    f'background-image:repeating-linear-gradient(90deg,{CREME} 0 26px,transparent 26px 52px),repeating-linear-gradient(90deg,{CREME} 0 26px,transparent 26px 52px);'
                    f'background-size:100% 14px,100% 14px;background-position:0 10px,0 calc(100% - 10px);background-repeat:no-repeat">' + ''.join(quadro(t) for t in ts) + '</div>')
carr('c3-passo-2-gravacao',
     FUNDO(TOMATE, CREME, .10) +
     A(44, 50, MONO('Passo 02 · gravação', 22, CREME, f'background:{CARVAO};padding:9px 13px')) +
     A(36, 106, BAGEL('Uma manhã', 150, CREME, .86, SH(TINTA, 8))) +
     A(36, 236, BAGEL('na sua cozinha.', 108, ACAFRAO, .86, SH(TINTA, 7))) +
     A(-10, 450, filme(['queijo esticando', 'forno aceso', 'caixa saindo', 'cardápio na mesa']), 'transform:rotate(-5deg)') +
     A(-310, 790, filme(['pizzaiolo', 'massa no ar', 'motoboy na rua', 'mesa cheia']), 'transform:rotate(-5deg)') +
     A(44, 1150, TXT('Foto e vídeo com a SUA pizza, o SEU forno e a SUA equipe. Nada de foto de banco.', 34, CREME, 'width:960px;line-height:1.25')) +
     A(44, 1280, MONO('Orégano Turbo · como funciona', 16, CREME, 'opacity:.8')) + PAG(3, CREME))

aneis = ''.join(f'<div class="a" style="left:{540 - r}px;top:{760 - r}px;width:{2 * r}px;height:{2 * r}px;border-radius:50%;border:4px {"solid" if i == 0 else "dashed"} rgba(243,238,230,{.9 - i * .18})"></div>'
                for i, r in enumerate([150, 270, 390, 510]))
pin = (f'<div style="display:flex;flex-direction:column;align-items:center">'
       f'<div style="width:150px;height:150px;border-radius:50% 50% 50% 0;transform:rotate(-45deg);background:{TOMATE};border:6px solid {CREME};box-shadow:10px 12px 0 rgba(20,19,17,.35);display:grid;place-items:center">'
       f'<div style="transform:rotate(45deg)">{simbolo(70, CREME, TOMATE)}</div></div></div>')
carr('c4-passo-3-anuncio',
     FUNDO(VERDE, CREME, .07) + aneis +
     A(44, 50, MONO('Passo 03 · anúncio', 22, VERDE, f'background:{CREME};padding:9px 13px')) +
     A(36, 104, BAGEL('Anúncio no', 130, CREME, .86, SH(TINTA, 7))) +
     A(36, 220, BAGEL('seu bairro.', 150, ACAFRAO, .86, SH(TINTA, 8))) +
     A(465, 650, pin) +
     A(560, 600, adesivo('sua pizzaria', CREME, VERDE, 4, 30, '10px 20px')) +
     A(60, 470, MONO('quem mora perto', 20, CREME, 'opacity:.9')) + A(760, 1010, MONO('na hora da fome', 20, CREME, 'opacity:.9')) +
     BOX(40, 1090, 1000, 150, CREME, f'border:5px solid {CARVAO};box-shadow:12px 12px 0 {TINTA};display:flex;align-items:center;gap:28px;padding:0 30px;transform:rotate(-1.5deg)',
         BAGEL('PZ01', 84, TOMATE, 1) + TXT('Cada anúncio leva um código. Assim dá para saber de onde veio cada pedido.', 28, CARVAO, 'line-height:1.25')) +
     A(44, 1280, MONO('Orégano Turbo · como funciona', 16, CREME, 'opacity:.8')) + PAG(4, CREME))

balz = lambda t, eu, h, s=28: (f'<div style="align-self:{"flex-end" if eu else "flex-start"};max-width:330px;background:{"#D9FDD3" if eu else "#fff"};'
                               f'border-radius:20px;padding:14px 18px 10px;box-shadow:0 2px 0 rgba(0,0,0,.08)">'
                               f'<div style="font:500 {s}px/1.25 Inter;color:{CARVAO}">{t}</div><div style="font:500 15px Inter;color:#667;text-align:right;margin-top:4px">{h}</div></div>')
cel = (f'<div style="width:440px;height:840px;background:{CARVAO};border-radius:64px;padding:18px;box-shadow:22px 24px 0 rgba(20,19,17,.3)">'
       f'<div style="width:100%;height:100%;border-radius:48px;overflow:hidden;background:#ECE5DD;display:flex;flex-direction:column">'
       f'<div style="background:{VERDE};padding:46px 24px 18px;display:flex;align-items:center;gap:14px">'
       f'<div style="width:54px;height:54px;border-radius:50%;background:{TOMATE};display:grid;place-items:center">{simbolo(30, CREME, TOMATE)}</div>'
       f'<div><div style="font:700 24px Inter;color:#fff">Sua Pizzaria</div><div style="font:500 16px Inter;color:#cfe">online</div></div></div>'
       f'<div style="flex:1;display:flex;flex-direction:column;gap:14px;padding:22px 18px">'
       + balz('Vi o anúncio! Quero uma calabresa grande. Código <b>PZ01</b>', False, '19:42')
       + balz('Anotado! Já vai pro forno 🔥', True, '19:43 ✓✓')
       + balz('Manda o pix?', False, '19:43') + balz('Chave no cardápio. Sai em 40 min.', True, '19:44 ✓✓') + '</div></div></div>')
carr('c5-passo-4-pedido-no-zap',
     FUNDO(CREME, TOMATE, .08) +
     A(44, 50, MONO('Passo 04 · pedido', 22, CREME, f'background:{TOMATE};padding:9px 13px')) +
     A(36, 104, BAGEL('O pedido', 130, VERDE, .86)) +
     A(36, 216, BAGEL('cai no', 130, VERDE, .86)) +
     A(36, 330, BAGEL('seu zap.', 136, TOMATE, .86, SH(TINTA, 8))) +
     A(610, 470, cel, 'transform:rotate(4deg)') +
     A(44, 560, ''.join(chk(t, ACAFRAO, CARVAO, 32) for t in ['Cardápio com link', 'Sem taxa de app', 'Cliente fica seu', 'Código do anúncio'])) +
     A(44, 940, adesivo('Sem comissão', VERDE, CREME, -6, 40, '16px 28px')) +
     A(44, 1070, MONO('conversa: exemplo ilustrativo', 18, CARVAO, f'background:{ACAFRAO};padding:8px 12px')) +
     A(44, 1280, MONO('Orégano Turbo · como funciona · 5/7', 16, CARVAO, 'opacity:.75')))

lin = lambda a, b, s=34: (f'<div style="display:flex;justify-content:space-between;align-items:baseline;padding:14px 0;border-bottom:3px dotted rgba(20,19,17,.35)">'
                          f'<span style="font:600 {s}px Inter;color:{CARVAO}">{a}</span><span style="font:400 {s + 8}px \'Bagel Fat One\';color:{TOMATE}">{b}</span></div>')
recibo = (f'<div style="width:700px;transform:rotate(3deg);filter:drop-shadow(18px 20px 0 rgba(0,0,0,.5))">' + picote(CREME, 12) +
          f'<div style="background:{CREME};padding:30px 44px 34px;position:relative">'
          + MONO('Relatório · segunda-feira', 20, TOMATE) + f'<div style="font:800 46px/1.1 \'Inter Tight\';color:{CARVAO};margin:8px 0 10px">Sua Pizzaria · semana 06</div>'
          + lin('Pedidos com código PZ', '38') + lin('Dia mais forte', 'Sexta') + lin('Dia mais fraco', 'Terça') + lin('Ajuste da semana', 'Anúncio terça')
          + f'<div style="position:absolute;right:20px;bottom:-110px;transform:rotate(-8deg);border:5px solid {TOMATE};color:{TOMATE};padding:10px 16px;font:700 22px/1.2 \'IBM Plex Mono\';letter-spacing:.1em;text-transform:uppercase;background:rgba(243,238,230,.9);text-align:center">exemplo ilustrativo<br><span style="font-size:15px">não é promessa de resultado</span></div>'
          + '</div>' + picote(CREME, 12).replace('circle at', 'circle at').replace('height:', 'transform:scaleY(-1);height:') + '</div>')
carr('c6-passo-5-relatorio',
     FUNDO(TINTA, CREME, .05) +
     A(44, 50, MONO('Passo 05 · relatório', 22, ACAFRAO)) +
     A(36, 100, BAGEL('O número', 150, CREME, .86)) +
     A(36, 230, BAGEL('na mesa.', 150, ACAFRAO, .86)) +
     A(190, 440, recibo) +
     A(44, 1150, TXT('Toda segunda você vê de onde veio cada pedido. E a gente ajusta o que precisa.', 32, CREME, 'width:980px;line-height:1.25')) +
     A(44, 1280, MONO('Orégano Turbo · como funciona', 16, CREME, 'opacity:.7')) + PAG(6, CREME))

gran = (f'<div style="width:860px;transform:rotate(-3deg);filter:drop-shadow(20px 22px 0 rgba(20,19,17,.4))">' + picote(CREME, 14) +
        f'<div style="background:{CREME};padding:30px 50px 40px;text-align:center">'
        + MONO('Orégano Turbo · pedido nº06 · comece por aqui', 20, CARVAO)
        + f'<div style="font:400 150px/1 \'Bagel Fat One\';color:{TOMATE};margin:16px 0 4px;text-transform:uppercase">Raio-X</div>'
        + f'<div style="font:400 110px/1 \'Bagel Fat One\';color:{VERDE}">R$ 297</div>'
        + MONO('abatido no 1º mês se fechar em 7 dias', 22, CARVAO, 'margin-top:14px')
        + f'<div style="border-top:3px dashed rgba(20,19,17,.35);margin:24px 0 18px"></div>'
        + MONO('5 vagas de fundadora:<br>preço do anual no semestral', 22, TOMATE, 'line-height:1.5') + '</div></div>')
carr('c7-cta-comece-pelo-raio-x',
     FUNDO(TOMATE, CREME, .10) +
     A(36, 50, BAGEL('Começa', 170, CREME, .86, SH(TINTA, 9))) +
     A(36, 196, BAGEL('pelo Raio-X.', 130, ACAFRAO, .86, SH(TINTA, 7))) +
     A(110, 420, gran) +
     A(80, 1080, ZAP(CARVAO, CREME, -4, 50)) +
     A(620, 1100, adesivo('Só pizzarias', VERDE, CREME, 6, 36)) +
     tarja_ass(1258, CARVAO, CREME, '@oreganoturbo · 7/7'))

# ================================================================== 07 · SÓ PIZZARIAS (A4 avental) · melhoria: faixa mais alta, "Hamburgueria? Não." como piada
feed('p07-so-pizzarias-avental',
     BOX(0, 0, 1080, 1350, xadrez(VERDE, CREME, 45)) +
     BOX(66, 52, 948, 1000, f'url(../v3/fotos/A4-avental-corrigido.jpg) center 38%/cover',
         f'border:16px solid {CREME};box-shadow:0 0 0 5px {CARVAO},20px 22px 0 5px rgba(20,19,17,.55);transform:rotate(-2deg)') +
     comanda(7, x=800, y=90, rot=6, txt='uniforme de forno') +
     A(96, 120, adesivo('Uniforme<br>de forno', TOMATE, CREME, -8, 40, '18px 28px', extra='border-radius:30px;line-height:1;text-align:center')) +
     A(-20, 900, f'<div style="width:1120px;background:{TOMATE};border-top:6px solid {CARVAO};border-bottom:6px solid {CARVAO};transform:rotate(-3deg);'
            f'padding:24px 0 28px;display:flex;flex-direction:column;align-items:center;box-shadow:0 16px 0 rgba(20,19,17,.3)">'
            + BAGEL('Só pizzarias.', 156, CREME, .95, SH(CARVAO, 8)) + MONO('Hamburgueria, açaí e sushi: a gente indica um amigo.', 22, CREME, 'margin-top:12px') + '</div>') +
     A(640, 1150, adesivo('Hamburgueria? Não.', CARVAO, CREME, 4, 30, '12px 22px')) +
     tarja_ass(1258, CARVAO, CREME, 'imagem gerada por IA · @oreganoturbo'))

# ================================================================== 08 · 5 VAGAS DE FUNDADORA · tipografia gigante + 5 comandas (sem foto: a B3 ficou só no Reels)
# Pesquisa §2 nº7 (tipografia gigante) + Impasto (o conceito: cada vaga é uma comanda em aberto).
vaga = lambda k, rot: (f'<div style="width:300px;transform:rotate({rot}deg);filter:drop-shadow(10px 12px 0 rgba(20,19,17,.35))">' + picote(CREME) +
                       f'<div style="background:{CREME};padding:12px 20px 16px;display:flex;align-items:center;justify-content:space-between">'
                       + MONO(f'vaga', 16, CARVAO) + f'<span style="font:400 54px/1 \'Bagel Fat One\';color:{TOMATE}">{k:02d}</span>'
                       + f'<span style="width:34px;height:34px;border:4px solid {VERDE};border-radius:6px"></span></div></div>')
feed('p08-5-vagas-fundadoras',
     FUNDO(TOMATE, CREME, .08) +
     A(-40, -190, BAGEL('5', 1300, CREME, 1, f'letter-spacing:0;{SH(TINTA, 18)}')) +
     A(44, 44, MONO('Pizzarias fundadoras · 2026', 22, CREME, f'background:{CARVAO};padding:9px 13px')) +
     comanda(8, x=830, y=40, rot=4, txt='fundadoras') +
     A(690, 300, ''.join(f'<div style="margin-bottom:18px">{vaga(k, r)}</div>' for k, r in zip(range(1, 6), [4, -3, 5, -2, 3]))) +
     A(40, 1000, BAGEL('vagas de', 110, CREME, .9, SH(TINTA, 7))) +
     A(40, 1090, BAGEL('fundadora.', 140, ACAFRAO, .9, SH(TINTA, 8))) +
     A(690, 970, adesivo('Preço do anual<br>no semestral', VERDE, CREME, -6, 30, '16px 24px', extra='border-radius:26px;line-height:1.05;text-align:center')) +
     faixa('chama no zap · @oreganoturbo', 1262, CARVAO, CREME, 0, 88, 44, x=-40, w=1200, sep='✦'))

# ================================================================== 09 · PIZZA NA CABEÇA (A6 boné) · melhoria: fundo verde (o boné creme destaca), faixas inteiras visíveis
feed('p09-pizza-na-cabeca',
     FUNDO(VERDE, CREME, .08) +
     A(36, 30, BAGEL('Pizza na', 150, CREME, .9)) +
     A(30, 170, BAGEL('cabeça.', 236, ACAFRAO, .9, SH(TINTA, 10))) +
     faixa('só pizzarias', 1010, TOMATE, CREME, -6, 104, 64) +
     IMG(REC('A6-bone-bb'), 240, 400, 780, 'transform:rotate(-6deg);filter:drop-shadow(24px 30px 0 rgba(10,30,20,.45))') +
     comanda(9, x=40, y=660, rot=-5, txt='24 horas por dia') +
     A(40, 470, adesivo('Só penso<br>em pizzaria', TOMATE, CREME, -8, 32, '18px 26px', extra='border-radius:26px;line-height:1.05;text-align:center')) +
     tarja_ass(1258, CARVAO, CREME, 'imagem gerada por IA · @oreganoturbo'))

# ================================================================== 10 · MEME · FORNO 400 °C × FEED PARADO (humor de pizzaiolo, tipográfico)
# Pesquisa §2 nº10 (humor e memes, Pizza Da Noi) + Pinterest nº2 ("Não tem ERRO": tipografia pesada em 2 tamanhos).
barra = lambda pct, cor: (f'<div style="width:960px;height:40px;border:5px solid {CARVAO};background:rgba(255,255,255,.25);border-radius:999px;overflow:hidden">'
                          f'<div style="width:{pct}%;height:100%;background:{cor}"></div></div>')
feed('p10-meme-forno-feed',
     BOX(0, 0, 1080, 1350, TINTA) +
     BOX(30, 30, 1020, 600, TOMATE, f'border:6px solid {CARVAO};transform:rotate(-1deg)',
         A(40, 30, BAGEL('Forno:', 120, CREME, .9)) + A(40, 150, BAGEL('400°C', 300, ACAFRAO, .86, SH(TINTA, 12))) + A(24, 500, barra(100, ACAFRAO))) +
     BOX(30, 650, 1020, 560, CREME, f'border:6px solid {CARVAO};transform:rotate(1deg)',
         A(40, 30, BAGEL('Feed:', 120, CARVAO, .9)) + A(40, 160, BAGEL('parado desde', 104, VERDE, .9)) + A(40, 260, BAGEL('março.', 170, VERDE, .9)) +
         A(24, 460, barra(4, TOMATE))) +
     comanda(10, x=830, y=40, rot=6, txt='verdade de balcão') +
     A(600, 1130, adesivo('O forno é com você.<br>O feed é com a gente.', VERDE, CREME, -4, 26, '16px 24px', extra='border-radius:24px;line-height:1.15;text-align:center')) +
     tarja_ass(1258, CARVAO, CREME, '@oreganoturbo · só pizzarias'))

# ================================================================== 11 · CARDÁPIO DA CASA (v4 p06 melhorada: vira cardápio de cantina, sem foto, letra grande)
# Jonny's Pizza (cardápio-cartaz) + Menu circular @nekrasova.designs (pontilhado) + Paollo: xadrez de toalha de cantina.
sabores = [('Foto de dar fome', 'gravada na sua cozinha: queijo, forno, caixa saindo'),
           ('Anúncio no bairro', 'quem mora perto vê a sua pizza na hora da fome'),
           ('Cardápio no zap', 'link de pedido direto, sem taxa de app'),
           ('iFood arrumado', 'fotos, descrições, combos e destaques'),
           ('Relatório de segunda', 'de onde veio cada pedido, toda semana')]
menu = ''.join(f'<div style="padding:16px 0;border-bottom:3px dashed rgba(20,19,17,.25)">'
               f'<div style="display:flex;align-items:baseline;gap:14px"><span style="font:600 20px \'IBM Plex Mono\';color:{TOMATE}">{i + 1:02d}</span>'
               f'<span style="font:400 50px/1 \'Bagel Fat One\';color:{VERDE};text-transform:uppercase;white-space:nowrap">{n}</span>'
               f'<span style="flex:1;border-bottom:4px dotted {CARVAO};opacity:.4;transform:translateY(-8px)"></span>'
               f'<span style="font:600 17px \'IBM Plex Mono\';color:{TOMATE};white-space:nowrap">NO PLANO</span></div>'
               f'<div style="font:500 26px/1.2 Inter;color:{CARVAO};margin:6px 0 0 44px">{d}</div></div>' for i, (n, d) in enumerate(sabores))
feed('p11-cardapio-da-casa',
     BOX(0, 0, 1080, 1350, CREME) +
     BOX(0, 0, 1080, 60, xadrez(TOMATE, CREME, 30)) +
     A(36, 82, BAGEL('Cardápio', 180, VERDE, .86)) +
     A(44, 250, BAGEL('da casa.', 110, TOMATE, .86, SH(TINTA, 6))) +
     comanda(11, x=830, y=236, rot=5, txt='sabores do plano', s=52) +
     A(40, 380, f'<div style="width:1000px">{menu}</div>') +
     BOX(40, 1080, 1000, 120, VERDE, f'border:5px solid {CARVAO};box-shadow:10px 10px 0 {CARVAO};display:flex;align-items:center;justify-content:space-between;padding:0 34px',
         BAGEL('Entrada: Raio-X', 54, CREME, 1) + BAGEL('R$ 297', 70, ACAFRAO, 1, SH(TINTA, 4))) +
     BOX(0, 1230, 1080, 120, xadrez(TOMATE, CREME, 30)) +
     BOX(0, 1258, 1080, 92, CARVAO, 'display:flex;align-items:center;justify-content:space-between;padding:0 52px', logo(34, CREME) + MONO('chama no zap · @oreganoturbo', 19, CREME)))

# ================================================================== 12 · DICIONÁRIO DO PIZZAIOLO (humor de balcão, tipográfico)
# Pesquisa §2 nº10 (humor e trocadilho) + Can Pizza (marca "rebelde" com a personalidade do produto).
verb = [('Meia a meia', 's.f.', 'O cliente que quer tudo e não decide nada.'),
        ('Dia fraco', 's.m.', 'Segunda, terça e quarta. Forno aceso, telefone mudo.'),
        ('Taxa do app', 's.f.', 'O sócio que você nunca chamou para a sociedade.'),
        ('Feed parado', 's.m.', 'Pizza boa que ninguém viu passar.'),
        ('Orégano Turbo', 's.m.', 'Marketing de vendas só para pizzarias. Ver também: zap.')]
dic = ''.join(f'<div style="padding:15px 0;border-bottom:3px solid rgba(20,19,17,.15)">'
              f'<span style="font:400 46px/1 \'Bagel Fat One\';color:{TOMATE if i < 4 else VERDE};text-transform:uppercase">{p}</span>'
              f'<span style="font:600 italic 22px \'IBM Plex Mono\';color:{CARVAO};opacity:.6;margin-left:12px">{c}</span>'
              f'<div style="font:600 30px/1.22 Inter;color:{CARVAO};margin-top:6px">{d}</div></div>' for i, (p, c, d) in enumerate(verb))
feed('p12-dicionario-do-pizzaiolo',
     FUNDO(TOMATE, CREME, .10) +
     A(36, 40, BAGEL('Dicionário', 152, CREME, .86, SH(TINTA, 9))) +
     A(44, 196, BAGEL('do pizzaiolo.', 96, ACAFRAO, .86, SH(TINTA, 6))) +
     comanda(12, x=830, y=200, rot=6, txt='verbete') +
     A(40, 330, f'<div style="width:1000px;background:{CREME};border:6px solid {CARVAO};box-shadow:16px 16px 0 {TINTA};padding:16px 40px 20px;transform:rotate(-1deg)">{dic}</div>') +
     tarja_ass(1258, CARVAO, CREME, 'salva e manda pro sócio · @oreganoturbo'))

# ================================================================== STORIES (tipográficos: as fotos já foram usadas no feed)
semana_s = ''.join(A(-20 + i * 30, 1180 + i * 210, outline(d, 300, CREME if i != 1 else ACAFRAO, 6, .9 if i == 1 else .45)) for i, d in enumerate(['Seg', 'Ter', 'Qua']))
enq = (f'<div style="width:900px;background:#fff;border-radius:34px;padding:38px;box-shadow:16px 18px 0 rgba(20,19,17,.35)">'
       + f'<div style="font:800 46px/1.1 \'Inter Tight\';color:{CARVAO};text-align:center;margin-bottom:24px;letter-spacing:-.02em">Qual dia vende menos aí?</div>'
       + ''.join(f'<div style="display:flex;justify-content:space-between;align-items:center;border:3px solid #E4E1DB;border-radius:22px;padding:24px 30px;margin-top:14px;'
                 f'font:700 38px Inter;color:{CARVAO}"><span>{d}</span><span style="width:38px;height:38px;border-radius:50%;border:4px solid {VERDE}"></span></div>'
                 for d in ['Segunda', 'Terça', 'Quarta']) + '</div>')
story('s1-enquete-dia-fraco',
      BOX(0, 0, 1080, 1920, VERDE) + f'<div class="a" style="inset:0;background:{padrao(CREME, .07, 300)}"></div>' + semana_s +
      A(40, 110, MONO('Enquete · donos de pizzaria', 24, CREME, f'background:{TOMATE};padding:10px 14px;box-shadow:6px 6px 0 {TINTA}')) +
      A(36, 190, BAGEL('Dia fraco', 180, CREME, .88, SH(TINTA, 9))) +
      A(36, 350, BAGEL('tem nome?', 180, ACAFRAO, .88, SH(TINTA, 9))) +
      A(90, 620, enq) +
      comanda(13, x=760, y=1260, rot=5, txt='enquete') +
      A(600, 1520, adesivo('Responde aí ↑', TOMATE, CREME, -5, 44, '16px 30px')) +
      A(40, 1840, MONO('@oreganoturbo · só pizzarias', 18, CREME, 'opacity:.85')))

chk_s = ''.join(chk(t, ACAFRAO, CARVAO, 44) for t in ['Instagram e Google', 'iFood e cardápio', 'WhatsApp', '3 concorrentes', 'Plano de 30 dias'])
story('s2-raio-x',
      BOX(0, 0, 1080, 1920, TINTA) + f'<div class="a" style="inset:0;background:{padrao(CREME, .05, 300)}"></div>' +
      A(260, 120, outline('X', 1500, TOMATE, 10, .55, 'line-height:1')) +
      A(40, 110, MONO('Pizzarias de São Luís', 24, ACAFRAO)) +
      A(30, 160, BAGEL('Raio-X', 270, CREME, .86)) +
      A(40, 400, BAGEL('da sua pizzaria.', 92, ACAFRAO, .9)) +
      A(60, 590, f'<div style="width:960px;transform:rotate(-2deg);filter:drop-shadow(16px 18px 0 rgba(0,0,0,.5))">' + picote(CREME, 12) +
               f'<div style="background:{CREME};padding:34px 44px 40px">' + MONO('Comanda nº14 · o que eu olho', 22, TOMATE) + chk_s +
               f'<div style="border-top:3px dashed rgba(20,19,17,.3);margin:30px 0 22px"></div>'
               f'<div style="display:flex;align-items:center;gap:26px">{BAGEL("R$ 297", 120, TOMATE, 1)}'
               + MONO('abatido no 1º mês<br>se fechar em 7 dias', 22, CARVAO, 'line-height:1.5') + '</div></div></div>') +
      A(40, 1500, adesivo('5 vagas de fundadora', VERDE, CREME, -4, 44, '16px 30px')) +
      A(560, 1640, ZAP(TOMATE, CREME, -6, 52)) +
      comanda(14, x=780, y=1420, rot=5, txt='raio-x') +
      A(40, 1860, MONO('@oreganoturbo · só pizzarias', 18, CREME, 'opacity:.75')))

bal = lambda t, eu, h: (f'<div style="align-self:{"flex-end" if eu else "flex-start"};max-width:680px;background:{"#D9FDD3" if eu else "#fff"};'
                        f'border-radius:28px;{"border-top-right-radius:6px" if eu else "border-top-left-radius:6px"};padding:22px 28px 14px;box-shadow:8px 10px 0 rgba(20,19,17,.3)">'
                        f'<div style="font:500 38px/1.3 Inter;color:{CARVAO}">{t}</div><div style="font:500 20px Inter;color:#667;text-align:right;margin-top:4px">{h}</div></div>')
cupom = (f'<div style="width:760px;transform:rotate(3deg);filter:drop-shadow(16px 18px 0 rgba(20,19,17,.35))">' + picote('#fff', 12) +
         f'<div style="background:#fff;padding:30px 44px 36px;font:600 30px/1.6 \'IBM Plex Mono\';color:{CARVAO}">'
         + f'<div style="text-align:center;font:400 64px/1 \'Bagel Fat One\';color:{TOMATE};margin-bottom:12px">PEDIDO Nº15</div>'
         + '<div style="display:flex;justify-content:space-between"><span>1× calabresa G</span><span>forno</span></div>'
         + '<div style="display:flex;justify-content:space-between"><span>canal</span><span>WhatsApp</span></div>'
         + '<div style="display:flex;justify-content:space-between"><span>código</span><span>PZ01</span></div>'
         + f'<div style="display:flex;justify-content:space-between;color:{TOMATE}"><span>taxa de app</span><span>R$ 0,00</span></div></div></div>')
story('s3-pedido-no-zap',
      BOX(0, 0, 1080, 1920, TOMATE) + f'<div class="a" style="inset:0;background:{padrao(CREME, .10, 300)}"></div>' +
      A(40, 100, BAGEL('Pedido', 200, CREME, .88, SH(TINTA, 10))) +
      A(40, 270, BAGEL('direto', 200, CREME, .88, SH(TINTA, 10))) +
      A(40, 440, BAGEL('no zap.', 200, ACAFRAO, .88, SH(TINTA, 10))) +
      comanda(15, x=820, y=90, rot=5, txt='pedido saindo') +
      A(60, 720, f'<div style="display:flex;flex-direction:column;gap:20px;width:960px">'
                 + bal('Boa noite! Quero uma calabresa grande', False, '19:42')
                 + bal('Anotado! Já vai pro forno.', True, '19:43 ✓✓') + '</div>') +
      A(150, 1100, cupom) +
      A(60, 1560, MONO('Exemplo ilustrativo', 22, CARVAO, f'background:{CREME};padding:10px 14px')) +
      BOX(0, 1700, 1080, 220, CARVAO, 'display:flex;flex-direction:column;justify-content:center;padding:0 52px;gap:14px',
          logo(48, CREME) + MONO('Marketing de vendas · só pizzarias', 18, CREME, 'opacity:.85')))

FONTS = ('<link href="https://fonts.googleapis.com/css2?family=Anton&family=Bagel+Fat+One&family=Inter+Tight:wght@700;800'
         '&family=Inter:wght@500;600;700;800&family=IBM+Plex+Mono:ital,wght@0,500;0,600;1,600&display=swap" rel="stylesheet">')
GRAO_SVG = ("url(\"data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'><filter id='n'>"
            "<feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2' stitchTiles='stitch'/></filter>"
            "<rect width='300' height='300' filter='url(%23n)' opacity='.55'/></svg>\")")
CSS = ('body{margin:0;background:#777}section.f{position:relative;overflow:hidden;margin:0 0 40px}.a{position:absolute}*{box-sizing:border-box}'
       f'.grao{{position:absolute;inset:0;background:{GRAO_SVG};mix-blend-mode:overlay;opacity:.22;pointer-events:none}}')
open(os.path.join(D, 'pecas.html'), 'w').write(
    f'<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>' +
    ''.join(f'<section class="f" id="{i}" style="width:{w}px;height:{h}px">{c}</section>' for i, w, h, c in P) + '</body></html>')
open(os.path.join(D, 'grid.txt'), 'w').write('\n'.join(GRID[:2] + ['p03-reels-pizza-no-ar'] + GRID[2:]))
print(len(P), 'peças')
