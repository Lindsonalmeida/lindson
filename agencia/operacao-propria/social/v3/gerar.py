# Kit de rede social v3 do @oreganoturbo · Paollo + Rocco · conta Leandro · 06/11/2026
# Pedido do Lindson (06/11): "não estou gostando da composição das artes para redes sociais. Melhore. Use o agente Paollo."
# Régua: "identidade visual de verdade, impactante, criativa" · "nunca simplista" · "menos espaço em branco, imagens".
# Protagonistas: fotos geradas pelo Lindson no Gemini (identidade/fotos-ia/hd), recortadas com BiRefNet (recortar.py)
# para a letra passar POR TRÁS do produto/pessoa. Em volta, o sistema da marca v4: xadrez, selos, ícones, faixa, tarja, etiqueta.
# Cada peça copia a COMPOSIÇÃO de uma referência da biblioteca (lista no README.md desta pasta).
# Uso: python3 gerar.py && node render.js  → pecas/*.jpg (posts 1080×1350, stories 1080×1920) e previa-feed.jpg
import os, random
random.seed(7)
D = os.path.dirname(os.path.abspath(__file__))

VERDE, TOMATE, CREME, ACAFRAO, CARVAO = '#1E5B3B', '#C8302B', '#F3EEE6', '#F2B33D', '#141311'
VERDE_ESC, CEU = '#123B26', '#0A63A8'
FOTO = lambda n: f'../../identidade/fotos-ia/hd/{n}.jpg'
REC = lambda n: f'recortes/{n}.webp'
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

# ================================================================== 01 · FOTO QUE DÁ FOME (B1, açafrão)
# Copia: HOTWHIZ (boca mordendo, fundo chapado) + "PIZZA gigante atrás" da biblioteca → letra passa POR TRÁS do rosto.
post('p01-foto-que-da-fome',
     BOX(0, 0, 1080, 1350, '#FFB200') + foto('B1-mordida') +
     A(30, 34, BAGEL('Foto', 168, TOMATE, .86, SH(CARVAO, 8))) + A(36, 190, ANTON('que dá', 124, CARVAO, .9)) + A(30, 312, BAGEL('fome.', 168, TOMATE, .86, SH(CARVAO, 8))) +
     frente('B1-mordida') +
     A(46, 560, MONO('Nº01 · foto e vídeo · só pizzarias', 17, CARVAO, f'background:{CREME};padding:10px 14px;transform:rotate(-3deg);box-shadow:6px 6px 0 {CARVAO}')) +
     A(806, 820, f'<div style="transform:rotate(-12deg)">{selo(232, "PIZZA BOA · FOTO BOA · PEDIDO NO ZAP · ", VERDE, CREME)}</div>') +
     A(668, 1108, adesivo('Chama no zap ↗', TOMATE, CREME, -5, 36)) +
     tarja_ass(1258, CARVAO, CREME, 'imagem gerada por IA · @oreganoturbo'))

# ================================================================== 02 · TERÇA TAMBÉM TEM FOME (B2, céu azul)
# Copia: "O nosso delivery está ON" (chave de interface, biblioteca) + Decaf Girl (grande-angular, céu, flash).
chave = (f'<div style="position:relative;width:600px;height:206px;border-radius:103px;background:{VERDE};'
         f'box-shadow:0 0 0 9px {CREME},16px 18px 0 9px rgba(20,19,17,.35)">'
         f'<div style="position:absolute;left:58px;top:24px">{BAGEL("On", 150, CREME, .95)}</div>'
         f'<div style="position:absolute;left:4px;top:-30px">{MONO("delivery", 18, ACAFRAO, f"background:{CARVAO};padding:7px 12px;border-radius:6px")}</div>'
         f'<div style="position:absolute;right:10px;top:10px;width:186px;height:186px;border-radius:50%;background:{CREME};overflow:hidden">'
         f'<img src="{REC("B2-pizza-bb")}" style="position:absolute;left:-60px;top:-30px;width:330px;transform:rotate(-12deg)"></div></div>')
post('p02-terca-tambem-tem-fome',
     BOX(0, 0, 1080, 1350, 'radial-gradient(circle at 70% 4%,#FFFFFF 0,#CFE6FF 5%,rgba(10,99,168,0) 26%),linear-gradient(180deg,#00407F 0%,#0A63A8 55%,#0069A9 100%)') +
     A(36, 34, BAGEL('Terça', 250, CREME, .86, SH(CARVAO, 10))) +
     A(42, 262, ANTON('também<br>tem fome.', 104, ACAFRAO, .9, SH(CARVAO, 6))) +
     IMG(REC('B2-caixa-ceu-bb'), 196, 1350 - 1149, 890, 'filter:drop-shadow(-18px 22px 0 rgba(20,19,17,.25))') +
     A(30, 640, chave, 'transform:rotate(-7deg) scale(.82);transform-origin:0 0') +
     A(40, 880, MONO('Dia fraco também<br>é dia de pizza', 18, CREME, f'line-height:1.4;background:{TOMATE};padding:10px 14px;box-shadow:6px 6px 0 {CARVAO};transform:rotate(-4deg)')) +
     A(840, 420, estrela(220, ACAFRAO, BAGEL('Seg<br>Ter<br>Qua', 44, TOMATE, .92), 10)) +
     A(40, 1100, adesivo('Chama no zap ↗', ACAFRAO, CARVAO, -6, 40)) +
     tarja_ass(1258, VERDE, CREME, 'imagem gerada por IA · @oreganoturbo'))

# ================================================================== 03 · GRADE DE 4 CORES (B3 recortada)
# Copia: grade de 4 cores com a mesma manchete (Peppa Please / Drip Riot, favoritas) + família por cor do Mario hot sauce.
def quadro(x, y, bg, fg, num, rot, dx, dy, tam=700):
    return (BOX(x, y, 540, 675, bg, 'overflow:hidden',
                f'<div class="a" style="inset:0;background:{padrao(fg, .16, 240)}"></div>'
                + IMG(REC('B3-pizza-voando-bb'), dx, dy, tam, f'transform:rotate({rot}deg);{SOMBRA_DURA}')
                + A(30, 26, BAGEL('Só<br>pizzarias.', 66, fg, .88, SH(CARVAO, 5)))
                + A(30, 618, MONO(num, 15, fg, f'background:{CARVAO};color:{CREME};padding:7px 10px'))))
post('p03-grade-so-pizzarias',
     quadro(0, 0, TOMATE, CREME, 'Nº1 · foto que dá fome', -8, -40, 150) +
     quadro(540, 0, ACAFRAO, TOMATE, 'Nº2 · anúncio no bairro', 14, -60, 140) +
     quadro(0, 675, VERDE, ACAFRAO, 'Nº3 · cardápio no zap', 30, -50, 150) +
     quadro(540, 675, CREME, VERDE, 'Nº4 · relatório na segunda', -20, -40, 150) +
     BOX(0, 668, 1080, 14, CARVAO) + BOX(533, 0, 14, 1350, CARVAO) +
     A(430, 565, selo(220, "ORÉGANO TURBO · MARKETING DE VENDAS · ", CARVAO, CREME)) +
     A(612, 1300, MONO('imagem gerada por IA · @oreganoturbo', 12, VERDE, 'opacity:.8')))

# ================================================================== 04 · MENOS APP. MAIS ZAP. (A8 recortada, tomate)
# Copia: manchete em 2 tamanhos ("AQUI / não tem / ERRO", biblioteca) + adesivos girados + faixa em loop (Pizzino).
post('p04-menos-app-mais-zap',
     BOX(0, 0, 1080, 1350, TOMATE) + f'<div class="a" style="inset:0;background:{padrao(CREME, .13, 300)}"></div>' +
     A(44, 40, ANTON('Menos', 92, CREME, .9)) + A(44, 118, BAGEL('app.', 168, ACAFRAO, .9, SH(CARVAO, 8))) +
     A(640, 60, logo(30, CREME)) + A(640, 116, MONO('marketing de vendas<br>para pizzarias', 15, CREME, 'line-height:1.5;opacity:.9')) +
     IMG(REC('A8-adesivo-pedido-saindo'), 238, 346, 842, 'filter:drop-shadow(-20px 24px 0 rgba(20,19,17,.28))') +
     faixa('pedido direto no zap', 300, CREME, VERDE, -3, 100, 58, sep='✦') +
     A(36, 470, adesivo('Cliente<br>é seu', ACAFRAO, CARVAO, -9, 34, '18px 26px', extra='border-radius:28px;line-height:1.02;text-align:center')) +
     A(40, 650, adesivo('Sem comissão<br>no pedido', VERDE, CREME, 6, 26, '16px 22px', extra='border-radius:26px;line-height:1.05;text-align:center')) +
     A(40, 980, ANTON('Mais', 100, CREME, .9, SH(CARVAO, 6))) +
     A(30, 1062, BAGEL('zap.', 250, CREME, .9, SH(CARVAO, 11))) +
     IA(CREME, 640, 1318))

# ================================================================== 05 · RAIO-X R$ 297 (cartaz retrô)
# Copia: cartaz "Retro PIZZA National Day" (retro-13: título gordo, selo de preço em explosão, faixa de rodapé)
# + moldura de xadrez de cantina (Jonny's Pizza, retro-14/16).
itens = ['Instagram', 'iFood', 'Google', 'WhatsApp', 'Concorrentes']
etqs = ''.join(A(x, y, MONO('✓ ' + t, 17, CREME, f'background:{VERDE};padding:9px 12px;transform:rotate({r}deg);box-shadow:5px 5px 0 {CARVAO}'))
               for t, (x, y, r) in zip(itens, [(70, 560, -4), (92, 860, 3), (770, 1000, -3), (830, 560, 4), (70, 1010, 2)]))
post('p05-raio-x-cartaz',
     BOX(0, 0, 1080, 1350, xadrez(TOMATE, CREME, 34)) +
     BOX(40, 40, 1000, 1270, CREME, f'border:6px solid {CARVAO};box-shadow:14px 14px 0 {CARVAO}') + BOX(46, 46, 988, 1258, padrao(TOMATE, .16, 260)) +
     A(60, 64, MONO('Orégano Turbo apresenta · São Luís - MA', 17, CARVAO), 'width:960px;display:flex;justify-content:center') +
     A(60, 104, BAGEL('Raio-X', 236, TOMATE, .9, SH(CARVAO, 9)), 'width:960px;display:flex;justify-content:center') +
     A(60, 318, ANTON('da sua pizzaria', 92, VERDE, .9), 'width:960px;display:flex;justify-content:center') +
     IMG(REC('B2-pizza-bb'), 150, 470, 780, f'transform:rotate(-8deg);{SOMBRA_DURA}') +
     etqs +
     A(690, 380, estrela(300, ACAFRAO, MONO('só', 20, CARVAO, 'letter-spacing:.2em') + BAGEL('R$297', 74, TOMATE, .9), 9)) +
     BOX(40, 1110, 1000, 200, VERDE, f'border:6px solid {CARVAO};display:flex;flex-direction:column;align-items:center;justify-content:center;gap:12px',
         ANTON('Abatido no 1º mês se fechar em 7 dias', 50, CREME, 1) + MONO('Chama no zap · @oreganoturbo', 20, ACAFRAO)) +
     A(100, 1080, MONO('pizza: imagem gerada por IA', 12, CARVAO, 'opacity:.7')))

# ================================================================== 06 · CARDÁPIO DA CASA (verde)
# Copia: cardápio-cartaz de pizzaria (Jonny's Pizza retro-14, menu circular busca-34) + fatia gigante saindo da arte (v4).
linha = lambda n, t, d: (f'<div style="display:flex;align-items:baseline;gap:12px;padding:15px 0;border-bottom:3px dashed rgba(20,19,17,.25)">'
                         f'<span style="font:600 18px \'IBM Plex Mono\';color:{TOMATE}">{n}</span>'
                         f'<span style="font:400 40px/1 Anton;text-transform:uppercase;color:{CARVAO};white-space:nowrap">{t}</span>'
                         f'<span style="flex:1;border-bottom:3px dotted {CARVAO};opacity:.5;transform:translateY(-6px)"></span>'
                         f'<span style="font:600 18px \'IBM Plex Mono\';color:{VERDE};white-space:nowrap">{d}</span></div>')
cardapio = (f'<div style="width:660px;background:{CREME};padding:34px 40px 30px;border:6px solid {CARVAO};box-shadow:16px 16px 0 {CARVAO};transform:rotate(-2deg)">'
            + MONO('O que sai da nossa cozinha', 17, TOMATE, 'margin-bottom:10px')
            + linha('01', 'Foto e vídeo de dar fome', 'NO PLANO')
            + linha('02', 'Anúncio no seu bairro', 'NO PLANO')
            + linha('03', 'Cardápio no zap', 'NO PLANO')
            + linha('04', 'iFood arrumado', 'NO PLANO')
            + linha('05', 'Relatório de segunda', 'NO PLANO')
            + f'<div style="display:flex;align-items:center;justify-content:space-between;margin-top:22px;background:{TOMATE};padding:16px 20px;border:4px solid {CARVAO}">'
            + ANTON('Raio-X da pizzaria', 46, CREME, 1) + BAGEL('R$297', 52, ACAFRAO, 1, SH(CARVAO, 4)) + '</div></div>')
post('p06-cardapio-da-casa',
     BOX(0, 0, 1080, 1350, VERDE) + f'<div class="a" style="inset:0;background:{padrao(CREME, .12, 300)}"></div>' +
     A(44, 34, BAGEL('Cardápio', 172, CREME, .9, SH(CARVAO, 9))) +
     A(48, 206, ANTON('da casa', 96, ACAFRAO, .9)) +
     IMG(V4('pepperoni-fatia'), 590, 300, 760, f'transform:rotate(24deg);{SOMBRA_DURA}') +
     A(46, 360, cardapio) +
     A(780, 1010, f'<div style="transform:rotate(10deg)">{selo(230, "SÓ PIZZARIAS · SÃO LUÍS - MA · ", TOMATE, CREME)}</div>') +
     A(70, 1040, adesivo('Peça pelo zap ↗', ACAFRAO, CARVAO, -5, 44)) +
     A(46, 1206, logo(36, CREME)) +
     A(46, 1270, MONO('Fatia: MVS9966, CC BY 3.0, Wikimedia Commons', 12, CREME, 'opacity:.7')))

# ================================================================== 07 · SÓ PIZZARIAS (A4 avental, símbolo oficial)
# Copia: moldura xadrez + foto inclinada com adesivos (La Verona, busca-26; Antonelli, busca-27; Don Diovanni, retro-20).
post('p07-so-pizzarias-avental',
     BOX(0, 0, 1080, 1350, xadrez(VERDE, CREME, 45)) +
     BOX(66, 52, 948, 1040, f'url(fotos/A4-avental-corrigido.jpg) center 38%/cover',
         f'border:16px solid {CREME};box-shadow:0 0 0 5px {CARVAO},20px 22px 0 5px rgba(20,19,17,.55);transform:rotate(-2deg)') +
     A(720, 70, f'<div style="transform:rotate(14deg)">{selo(250, "MARKETING DE VENDAS PARA PIZZARIAS · ", VERDE, CREME)}</div>') +
     A(96, 120, adesivo('Uniforme<br>de forno', ACAFRAO, CARVAO, -8, 38, '18px 28px', extra='border-radius:30px;line-height:1;text-align:center')) +
     A(-20, 950, f'<div style="width:1120px;background:{TOMATE};border-top:6px solid {CARVAO};border-bottom:6px solid {CARVAO};transform:rotate(-3deg);'
            f'padding:26px 0 30px;display:flex;flex-direction:column;align-items:center;box-shadow:0 16px 0 rgba(20,19,17,.3)">'
            + BAGEL('Só pizzarias.', 150, CREME, .95, SH(CARVAO, 8)) + MONO('Hamburgueria, açaí e sushi: não atendemos.', 20, CREME, 'margin-top:12px') + '</div>') +
     tarja_ass(1258, CARVAO, CREME, 'imagem gerada por IA · @oreganoturbo'))

# ================================================================== 08 · 5 VAGAS DE FUNDADORA (carvão, número gigante atrás)
# Copia: "PIZZA" gigante atrás da pizza (biblioteca) com número no lugar da palavra + pizza voando (Drip Riot, rel-2033-04).
post('p08-5-vagas-fundadoras',
     BOX(0, 0, 1080, 1350, CARVAO) + f'<div class="a" style="inset:0;background:{padrao(CREME, .07, 300)}"></div>' +
     A(48, 40, MONO('Pizzarias fundadoras · 2026', 20, ACAFRAO)) +
     A(-30, -150, BAGEL('5', 1240, ACAFRAO, 1, 'letter-spacing:0')) +
     IMG(REC('B3-pizza-voando-bb'), 410, 250, 760, f'transform:rotate(-10deg);{SOMBRA_DURA}') +
     A(800, 70, ANTON('Só', 150, CREME, .9, SH(TOMATE, 6))) +
     A(44, 1012, ANTON('vagas de<br>fundadora.', 128, CREME, .86, SH(TOMATE, 7))) +
     A(640, 1110, adesivo('Preço do anual<br>no semestral', TOMATE, CREME, -6, 30, '16px 24px', extra='border-radius:26px;line-height:1.05;text-align:center')) +
     faixa('chama no zap · @oreganoturbo', 1262, ACAFRAO, CARVAO, 0, 88, 44, x=-40, w=1200, sep='✦') +
     A(760, 1236, MONO('imagem gerada por IA', 11, CREME, 'opacity:.7')))

# ================================================================== 09 · PIZZA NA CABEÇA (A6 boné, faixas cruzadas)
# Copia: merch com atitude (Crosta boné, busca-33; Pizzino camiseta) + faixas em loop cruzadas (Pizzino, busca-31).
post('p09-pizza-na-cabeca',
     BOX(0, 0, 1080, 1350, '#F7A81F') + f'<div class="a" style="inset:0;background:{padrao(CARVAO, .10, 300)}"></div>' +
     A(36, 26, BAGEL('Pizza na', 150, VERDE, .9, SH(CREME, 7))) +
     A(30, 176, BAGEL('cabeça.', 236, TOMATE, .9, SH(CARVAO, 10))) +
     faixa('só pizzarias', 860, TOMATE, CREME, -7, 104, 64) +
     faixa('marketing de vendas', 1000, VERDE, CREME, 5, 96, 56) +
     IMG(REC('A6-bone-bb'), 190, 380, 800, 'transform:rotate(-6deg);filter:drop-shadow(24px 30px 0 rgba(20,19,17,.28))') +
     A(820, 400, f'<div style="transform:rotate(12deg)">{estrela(210, TOMATE, ANTON("Todo<br>dia", 56, CREME, .9), 0)}</div>') +
     A(40, 470, adesivo('Só penso<br>em pizzaria', VERDE, CREME, -8, 26, '16px 22px', extra='border-radius:24px;line-height:1.05;text-align:center')) +
     tarja_ass(1258, CARVAO, CREME, 'imagem gerada por IA · @oreganoturbo'))

# ================================================================== STORIES (1080×1920)
# S1 · enquete (B2 recortada sobre céu) · copia: Decaf Girl (céu + produto na mão) + figurinha de enquete do Instagram.
enq = (f'<div style="width:880px;background:#fff;border-radius:34px;padding:34px;box-shadow:16px 18px 0 rgba(20,19,17,.35)">'
       + f'<div style="font:800 40px/1.1 \'Inter Tight\';color:{CARVAO};text-align:center;margin-bottom:22px;letter-spacing:-.02em">Qual dia vende menos aí?</div>'
       + ''.join(f'<div style="display:flex;justify-content:space-between;align-items:center;border:3px solid #E4E1DB;border-radius:22px;padding:22px 28px;margin-top:14px;'
                 f'font:700 34px Inter;color:{CARVAO}"><span>{d}</span><span style="width:34px;height:34px;border-radius:50%;border:3px solid {VERDE}"></span></div>'
                 for d in ['Segunda', 'Terça', 'Quarta']) + '</div>')
story('story-1-enquete',
      BOX(0, 0, 1080, 1920, 'linear-gradient(180deg,#003B78 0%,#0A63A8 45%,#0069A9 100%)') +
      A(40, 90, MONO('Enquete · donos de pizzaria', 22, CREME, f'background:{TOMATE};padding:10px 14px;box-shadow:6px 6px 0 {CARVAO}')) +
      A(40, 170, BAGEL('Dia fraco<br>tem nome?', 150, CREME, .9, SH(CARVAO, 9))) +
      IMG(REC('B2-caixa-ceu-bb'), -20, 760, 1200, 'filter:drop-shadow(-18px 22px 0 rgba(20,19,17,.28))') +
      A(100, 520, enq) +
      A(800, 90, f'<div style="transform:rotate(12deg)">{selo(220, "SÓ PIZZARIAS · SÃO LUÍS - MA · ", VERDE, CREME)}</div>') +
      A(40, 1850, MONO('imagem gerada por IA · @oreganoturbo', 14, CREME, 'opacity:.8')))

# S2 · Raio-X (B3 vermelho) · copia: cartaz com explosão de preço (retro-13) + produto voando (Drip Riot).
chk = ''.join(f'<div style="display:flex;gap:16px;align-items:center;margin-top:12px">'
              f'<span style="width:44px;height:44px;border-radius:50%;background:{ACAFRAO};display:grid;place-items:center;font:700 26px Inter;color:{CARVAO}">✓</span>'
              f'<span style="font:400 46px/1 Anton;color:{CREME};text-transform:uppercase">{t}</span></div>' for t in ['Instagram e Google', 'iFood e cardápio', 'WhatsApp', '3 concorrentes do bairro'])
story('story-2-raio-x',
      BOX(0, 0, 1080, 1920, '#D72B1B') + IMG(REC('B3-pizza-voando-bb'), 40, 470, 1000, SOMBRA_DURA) +
      A(40, 90, MONO('Pizzarias de São Luís', 22, CREME)) +
      A(40, 140, BAGEL('Raio-X', 230, CREME, .9, SH(CARVAO, 10))) +
      A(46, 350, ANTON('da sua pizzaria', 96, ACAFRAO, .9, SH(CARVAO, 5))) +
      A(700, 520, estrela(320, ACAFRAO, MONO('só', 22, CARVAO) + BAGEL('R$297', 80, TOMATE, .9), 10)) +
      BOX(0, 1360, 1080, 560, CARVAO, f'border-top:8px solid {ACAFRAO};padding:44px 52px', chk +
          f'<div style="margin-top:30px">{MONO("Abatido no 1º mês se fechar em 7 dias · 5 vagas de fundadora", 18, CREME)}</div>') +
      A(560, 1250, adesivo('Chama no zap ↗', VERDE, CREME, -6, 52, '22px 34px')) +
      faixa('5 vagas de fundadora', 1730, ACAFRAO, CARVAO, -3, 100, 58, x=-60, w=1240) +
      A(52, 1872, MONO('imagem gerada por IA · @oreganoturbo', 14, CREME, 'opacity:.7')))

# S3 · pedido no zap (A8 verde) · copia: conversa de WhatsApp sobre a foto (kit v1 aprovado) + selo do adesivo "PEDIDO SAINDO".
bal = lambda t, eu, h: (f'<div style="align-self:{"flex-end" if eu else "flex-start"};max-width:640px;background:{"#D9FDD3" if eu else "#fff"};'
                        f'border-radius:26px;{"border-top-right-radius:6px" if eu else "border-top-left-radius:6px"};padding:20px 26px 14px;box-shadow:8px 10px 0 rgba(20,19,17,.3)">'
                        f'<div style="font:500 34px/1.3 Inter;color:{CARVAO}">{t}</div><div style="font:500 18px Inter;color:#667;text-align:right;margin-top:4px">{h}</div></div>')
story('story-3-pedido-no-zap',
      BOX(0, 0, 1080, 1920, '#005C3E') + IMG(REC('A8-adesivo-pedido-saindo-bb'), 150, 640, 930, 'filter:drop-shadow(-20px 24px 0 rgba(20,19,17,.3))') +
      A(40, 90, BAGEL('Pedido<br>direto', 168, CREME, .9, SH(CARVAO, 9))) +
      A(40, 400, BAGEL('no zap.', 168, ACAFRAO, .9, SH(CARVAO, 9))) +
      A(60, 640, f'<div style="display:flex;flex-direction:column;gap:18px;width:960px">'
                 + bal('Boa noite! Quero uma calabresa grande', False, '19:42')
                 + bal('Anotado! Já vai pro forno.', True, '19:43 ✓✓') + '</div>') +
      A(60, 1010, MONO('Exemplo ilustrativo', 18, CARVAO, f'background:{ACAFRAO};padding:9px 12px')) +
      BOX(0, 1700, 1080, 220, CARVAO, 'display:flex;flex-direction:column;justify-content:center;padding:0 52px;gap:14px',
          logo(44, CREME) + MONO('Marketing de vendas para pizzarias · imagem gerada por IA', 15, CREME, 'opacity:.85')))

FONTS = ('<link href="https://fonts.googleapis.com/css2?family=Anton&family=Bagel+Fat+One&family=Inter+Tight:wght@700;800'
         '&family=Inter:wght@500;600;700&family=IBM+Plex+Mono:wght@500;600&display=swap" rel="stylesheet">')
GRAO_SVG = ("url(\"data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'><filter id='n'>"
            "<feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2' stitchTiles='stitch'/></filter>"
            "<rect width='300' height='300' filter='url(%23n)' opacity='.55'/></svg>\")")
CSS = ('body{margin:0;background:#777}section.f{position:relative;overflow:hidden;margin:0 0 40px}.a{position:absolute}*{box-sizing:border-box}'
       f'.grao{{position:absolute;inset:0;background:{GRAO_SVG};mix-blend-mode:overlay;opacity:.22;pointer-events:none}}')
open(os.path.join(D, 'pecas.html'), 'w').write(
    f'<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>' +
    ''.join(f'<section class="f" id="{i}" style="width:{w}px;height:{h}px">{c}</section>' for i, w, h, c in P) + '</body></html>')
print(len(P), 'peças')
