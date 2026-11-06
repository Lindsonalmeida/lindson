# Identidade visual Orégano Turbo · v4 IMPACTO (Paollo · conta Leandro, sessão paralela, 06/11/2026)
# Pedido do Lindson (06/11): "identidade visual aprovada. apenas melhore para ter mais impacto, conexão, visual
# impactantes, imagens, menos espaços em branco" · "pode parecer uma pizzaria" · "nunca me dê coisas simplistas".
# Base = v3 aprovada (gerar3.py): nome, símbolo da folha com seta, Inter Tight / Inter / IBM Plex Mono,
# carvão #141311, verde #1E5B3B, creme #F3EEE6, brasa #E4572E. A v4 SOMA (TEMPLATE.md, seção v4):
#  · Anton (condensada pesada) só nas manchetes · tomate #D42A1F (campo grande) e açafrão #F2B33D (selo/preço)
#  · xadrez de cantina verde/creme e tomate/creme · padrão de ícones em traço · selos redondos
#  · comida RECORTADA (BiRefNet, recortar4.py → recortes-v4/) saindo da arte, fatias flutuando, queijo puxando
# Composição copiada de (pesquisa v4): Pinterest "Love at first slice" (fatia gigante com queijo cruzando a letra),
# "PULL" (palavra gigante + queijo puxando), "Metto Monday" (letra ocupando a página toda), caixa "agata" (padrão
# de ícones em traço na caixa), avental verde "Flan de Lyon", selos verdes "El arte de hacer pizza"; biblioteca:
# "PIZZA" gigante atrás da pizza, "AQUI NÃO TEM ERRO" (fatias voando), "Delivery ON" (xadrez nas bordas);
# apresentação de case: Colletivo (ficha técnica, foto sangrada, contexto curto).
# Gera pecas4.html → node render4.js → pecas-v4/*.png (1080×1350; avatar 1080×1080).
import os
CARVAO, CREME, VERDE, BRASA, CINZA, PAPEL = '#141311', '#F3EEE6', '#1E5B3B', '#E4572E', '#8A857C', '#FBF8F3'
TOMATE, ACAFRAO, VERDE_CL, VERDE_ESC, KRAFT = '#D42A1F', '#F2B33D', '#7CC596', '#123B26', '#C9A57A'
FOTO = lambda n: f'fotos-v4/{n}.jpg' if os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), f'fotos-v4/{n}.jpg')) else f'fotos-v3/{n}.jpg'
REC = lambda n: f'recortes-v4/{n}.png'

# ---------------------------------------------------------------- marca (igual à v3 aprovada)
def simbolo(tam, folha=VERDE, seta=CREME):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="{tam}" height="{tam}" style="display:block">'
            f'<path d="M18 86 C 14 50, 40 18, 86 14 C 86 58, 58 88, 18 86 Z" fill="{folha}"/>'
            f'<path d="M26 76 L44 58 L54 66 L72 40" fill="none" stroke="{seta}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<path d="M60 38 L74 38 L74 52" fill="none" stroke="{seta}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></svg>')

def logo(tam, cor=CARVAO, folha=VERDE, seta=CREME, sub=True):
    s = f'<div style="display:flex;align-items:center;gap:{tam * .28}px">{simbolo(tam * 1.15, folha, seta)}<div>'
    s += f'<div style="font:800 {tam}px/0.9 \'Inter Tight\';letter-spacing:-.045em;color:{cor};white-space:nowrap">Orégano Turbo</div>'
    if sub: s += f'<div style="font:500 {tam * .2}px/1 \'IBM Plex Mono\';letter-spacing:.16em;color:{cor};opacity:.75;margin-top:{tam * .2}px;white-space:nowrap">MARKETING DE VENDAS PARA PIZZARIAS</div>'
    return s + '</div></div>'

def circulo(palavra, cor=ACAFRAO, pad=.07, w=5):
    return (f'<span style="position:relative;display:inline-block">{palavra}<svg viewBox="0 0 200 80" preserveAspectRatio="none" '
            f'style="position:absolute;left:-{pad * 100}%;top:-14%;width:{100 + pad * 200}%;height:128%;overflow:visible">'
            f'<path d="M30 14 C 90 0, 190 6, 194 38 C 198 70, 80 80, 20 66 C -10 56, 6 22, 60 10" fill="none" stroke="{cor}" stroke-width="{w}" stroke-linecap="round" vector-effect="non-scaling-stroke"/></svg></span>')

# ---------------------------------------------------------------- ícones em traço (padrão da marca)
IC = {
 'fatia': '<path d="M16 24 Q50 8 84 24 L50 90 Z"/><path d="M14 22 Q50 4 86 22"/><circle cx="40" cy="36" r="6"/><circle cx="60" cy="42" r="5"/><circle cx="50" cy="62" r="5"/>',
 'folha': '<path d="M18 86 C 14 50, 40 18, 86 14 C 86 58, 58 88, 18 86 Z"/><path d="M28 74 L44 58 L54 66 L70 44"/><path d="M60 42 L71 42 L71 53"/>',
 'tomate': '<circle cx="50" cy="58" r="30"/><path d="M50 28 L40 16 M50 28 L60 16 M50 28 L50 12 M50 28 L34 26 M50 28 L66 26"/>',
 'pa': '<circle cx="50" cy="36" r="26"/><path d="M50 62 L50 94"/><circle cx="44" cy="32" r="4"/><circle cx="58" cy="40" r="4"/>',
 'pizza': '<circle cx="50" cy="50" r="36"/><circle cx="50" cy="50" r="28"/><path d="M50 14 L50 86 M14 50 L86 50 M25 25 L75 75 M75 25 L25 75"/>',
 'chama': '<path d="M50 90 C 24 90 20 62 38 44 C 38 58 46 60 50 52 C 50 36 60 24 56 10 C 76 26 82 50 76 66 C 72 82 62 90 50 90 Z"/>',
 'celular': '<rect x="30" y="10" width="40" height="80" rx="8"/><path d="M44 80 L56 80"/><path d="M40 34 L48 42 L62 28"/>',
 'seta': '<path d="M14 80 L40 54 L54 66 L84 30"/><path d="M66 30 L84 30 L84 48"/>',
 'caixa': '<path d="M12 40 L50 24 L88 40 L50 56 Z"/><path d="M12 40 L12 64 L50 80 L88 64 L88 40"/><path d="M50 56 L50 80"/>',
 'manjericao': '<path d="M50 90 C 50 70 50 50 50 30"/><path d="M50 60 C 30 60 22 46 24 34 C 40 34 50 44 50 60 Z"/><path d="M50 48 C 70 48 78 34 76 22 C 60 22 50 32 50 48 Z"/>',
}
def icone(n, tam=80, cor=CREME, w=5):
    return f'<svg viewBox="0 0 100 100" width="{tam}" height="{tam}" style="display:block" fill="none" stroke="{cor}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round">{IC[n]}</svg>'

def padrao_url(cor=CREME, op=1, tam=360, w=4):
    """Tile SVG com ícones em traço girados (caixa 'agata' + Pizzino). Vira background-image."""
    pos = [('fatia', 30, 20, -18), ('tomate', 200, 30, 12), ('folha', 120, 130, 0), ('pa', 280, 150, 28), ('chama', 20, 200, 8),
           ('pizza', 190, 230, 0), ('manjericao', 300, 290, -20), ('seta', 90, 290, 0), ('caixa', 290, 40, -8)]
    g = ''.join(f'<g transform="translate({x} {y}) rotate({r} 30 30) scale(.6)">{IC[n]}</g>' for n, x, y, r in pos)
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{tam}" height="{tam}" viewBox="0 0 360 360"><g fill="none" stroke="{cor}" stroke-opacity="{op}" '
           f'stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round">{g}</g></svg>')
    return "url('data:image/svg+xml;utf8," + svg.replace('#', '%23').replace('"', '%22').replace('<', '%3C').replace('>', '%3E') + "')"

def xadrez(a=VERDE, b=CREME, t=60):
    return f'repeating-conic-gradient({a} 0 25%,{b} 0 50%) 0 0/{t * 2}px {t * 2}px'

def selo(tam, texto, bg=VERDE, fg=CREME, centro=None, borda=None, fs=None, gid='s'):
    """Selo redondo com texto em volta (selos 'El arte de hacer pizza')."""
    import random
    gid = gid + str(random.randint(0, 10 ** 8))
    fs = fs or 11.5
    centro = centro or simbolo(tam * .42, fg, bg)
    return (f'<div style="position:relative;width:{tam}px;height:{tam}px;border-radius:50%;background:{bg};{f"box-shadow:0 0 0 {tam * .025}px {borda};" if borda else ""}">'
            f'<svg viewBox="0 0 200 200" width="{tam}" height="{tam}" style="position:absolute;inset:0">'
            f'<defs><path id="{gid}" d="M100 100 m-76 0 a76 76 0 1 1 152 0 a76 76 0 1 1 -152 0"/></defs>'
            f'<circle cx="100" cy="100" r="94" fill="none" stroke="{fg}" stroke-width="2"/><circle cx="100" cy="100" r="58" fill="none" stroke="{fg}" stroke-width="2"/>'
            f'<text font-family="IBM Plex Mono" font-weight="500" font-size="{fs}" letter-spacing="2.2" fill="{fg}"><textPath href="#{gid}">{texto}</textPath></text></svg>'
            f'<div style="position:absolute;inset:0;display:grid;place-items:center">{centro}</div></div>')

# ---------------------------------------------------------------- utilitários de layout
ETQ = lambda t, cor=CREME, extra='': f'<div style="white-space:nowrap;font:500 18px/1 \'IBM Plex Mono\';letter-spacing:.16em;text-transform:uppercase;color:{cor};{extra}">{t}</div>'
A = lambda x, y, inner, w=None, extra='': f'<div class="a" style="left:{x}px;top:{y}px;{f"width:{w}px;" if w else ""}{extra}">{inner}</div>'
BOX = lambda x, y, w, h, bg, extra='', inner='': f'<div class="a" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:{bg};{extra}">{inner}</div>'
ANTON = lambda t, s, cor=CREME, lh=.86, extra='': f'<div style="font:400 {s}px/{lh} Anton;text-transform:uppercase;letter-spacing:-.005em;color:{cor};{extra}">{t}</div>'
TIGHT = lambda t, s, cor=CREME, extra='': f'<div style="font:800 {s}px/.98 \'Inter Tight\';letter-spacing:-.045em;color:{cor};{extra}">{t}</div>'
TXT = lambda t, s=24, cor=CREME, extra='': f'<div style="font:400 {s}px/1.45 Inter;color:{cor};{extra}">{t}</div>'
def rec(n, x, y, w, rot=0, sombra=.55, extra=''):
    """Comida recortada com a receita do Rocco: sombra DURA de flash (deslocada 12–30 px, 40%, desfoque 3 px),
    contraste e saturação +10%, brilho de flash por cima."""
    d = max(12, min(30, w * .03))
    return (f'<img class="a" src="{REC(n)}" style="left:{x}px;top:{y}px;width:{w}px;height:auto;transform:rotate({rot}deg);'
            f'filter:drop-shadow({d:.0f}px {d * 1.1:.0f}px 3px rgba(0,0,0,{min(sombra, .42)})) saturate(1.12) contrast(1.1) brightness(1.04);{extra}">')
def voa(n, x, y, w, rot=0, blur=0):
    """Ingrediente voando (calabresa, azeitona, manjericão), com desfoque de movimento opcional."""
    return (f'<img class="a" src="{REC("ing-" + n)}" style="left:{x}px;top:{y}px;width:{w}px;height:auto;transform:rotate({rot}deg);'
            f'filter:drop-shadow({w * .08:.0f}px {w * .1:.0f}px 2px rgba(0,0,0,.35)) saturate(1.15) contrast(1.08){f" blur({blur}px)" if blur else ""}">')
FLASH = 'radial-gradient(circle at 28% 18%,rgba(255,255,255,.22),rgba(255,255,255,0) 46%)'
def fundo_foto(n, escuro=.55, pos='center', grad=None):
    g = grad or f'linear-gradient(180deg,rgba(20,19,17,{escuro * .55}) 0%,rgba(20,19,17,{escuro}) 50%,rgba(20,19,17,.95) 100%)'
    return f'<div class="a" style="inset:0;background:{g},url({FOTO(n)}) {pos}/cover"></div>'
def faixa_xadrez(y, h=60, a=VERDE, b=CREME, t=30):
    return BOX(0, y, 1080, h, xadrez(a, b, t))
def rodape(n, cor=CREME, num=''):
    e = lambda t: f'<div style="white-space:nowrap;font:500 14px/1 \'IBM Plex Mono\';letter-spacing:.14em;text-transform:uppercase;color:{cor};opacity:.85">{t}</div>'
    return A(60, 1300, f'<div style="display:flex;justify-content:space-between;align-items:center;width:960px;gap:30px">{e("Orégano Turbo · v4")}{e(n)}</div>')
def cabeca(num, titulo, cor=CREME):
    return A(60, 56, f'<div style="display:flex;align-items:center;gap:18px">{simbolo(40, cor, "transparent" if False else (CARVAO if cor == CREME else CREME))}{ETQ(f"{num} · {titulo}", cor)}</div>')

def iphone(inner, w=420, h=860, bg='#fff'):
    return (f'<div style="width:{w}px;height:{h}px;border-radius:64px;background:#0b0b0a;padding:14px;box-shadow:0 60px 100px -30px rgba(0,0,0,.7),0 0 0 2px #3a3833 inset">'
            f'<div style="position:relative;width:100%;height:100%;border-radius:52px;overflow:hidden;background:{bg}">'
            f'<div style="position:absolute;left:50%;top:12px;transform:translateX(-50%);width:118px;height:34px;border-radius:20px;background:#0b0b0a;z-index:5"></div>'
            f'<div style="display:flex;justify-content:space-between;padding:18px 34px 0;font:600 16px \'Inter\';color:{"#fff" if bg in (CARVAO, "#075e54") else "#111"}"><span>19:42</span><span>●●● ▮</span></div>'
            f'{inner}</div></div>')
def balao(txt, eu=False, hora='19:4'):
    cor = '#d9fdd3' if eu else '#fff'
    return (f'<div style="align-self:{"flex-end" if eu else "flex-start"};max-width:80%;background:{cor};border-radius:12px;padding:10px 12px 6px;'
            f'font:400 16px/1.35 \'Inter\';color:#111;box-shadow:0 1px 1px rgba(0,0,0,.12)">{txt}<div style="text-align:right;font-size:11px;color:#667">{hora}{" ✓✓" if eu else ""}</div></div>')

P = []
PAD_CREME = padrao_url(CREME, .16)
PAD_VERDE = padrao_url(VERDE, .14)
PAD_TOM = padrao_url('#ffffff', .14)

# =================================================================== 01 · CAPA-CAMPANHA (Rocco: cor chapada + flash + produto enorme + ingredientes voando)
P.append(('v4-01-capa', 1080, 1350, ACAFRAO,
  BOX(0, 0, 1080, 1350, f'{FLASH},{ACAFRAO}') +
  A(60, 56, logo(38, CARVAO, VERDE, ACAFRAO, sub=False)) + A(770, 70, ETQ('Identidade v4 · 2026', CARVAO)) +
  A(44, 130, ANTON('Mais<br>pedidos.', 292, CARVAO, .84)) +
  voa('calabresa-2', 860, 150, 150, 20, 4) + voa('manjericao-3', 900, 330, 150, -30) + voa('azeitona-1', 690, 420, 90, 10) +
  rec('calabresa', 250, 560, 940, -14, .42) +
  voa('calabresa-4', 40, 760, 190, -10) + voa('manjericao-1', 70, 990, 170, 25) + voa('azeitona-2', 230, 1190, 80, -20, 3) +
  voa('calabresa-6', 900, 1130, 170, 30, 5) + voa('manjericao-4', 640, 1180, 140, 60, 2) + voa('calabresa-1', 600, 470, 110, 0, 6) +
  A(60, 640, TIGHT(f'Menos {circulo("achismo.", TOMATE)}', 60, CARVAO), 520) +
  A(820, 980, selo(210, 'SÓ PIZZARIAS · SÃO LUÍS · MARANHÃO · ', TOMATE, CREME, borda=CREME, fs=15.5), extra='transform:rotate(12deg)')))

# =================================================================== 01b · CAPA FORNO (versão escura)
P.append(('v4-01b-capa-forno', 1080, 1350, CARVAO,
  fundo_foto('brasa', .5, 'center', 'linear-gradient(180deg,rgba(20,19,17,.55),rgba(20,19,17,.35) 40%,rgba(20,19,17,.92) 78%)') +
  A(60, 60, logo(40, CREME, VERDE_CL, CARVAO, sub=False)) + A(760, 74, ETQ('Identidade v4 · 2026')) +
  A(48, 150, ANTON('Mais<br>pedidos.', 300, CREME, .84)) +
  rec('calabresa', 450, 560, 800, -12, .8) +
  A(60, 900, TIGHT(f'Menos<br>{circulo("achismo.")}', 96, CREME, 'text-shadow:0 6px 30px rgba(0,0,0,.6)'), 520) +
  A(60, 1110, TXT('Marketing de vendas só para pizzarias. Anúncio, Instagram e WhatsApp trabalhando para o forno não parar.', 26, CREME, 'opacity:.92;width:380px;text-shadow:0 2px 12px rgba(0,0,0,.8)')) +
  A(800, 1040, selo(220, 'SÓ PIZZARIAS · SÃO LUÍS · MARANHÃO · ', TOMATE, CREME, borda=CREME, fs=15.5)) +
  faixa_xadrez(1290, 60, VERDE, CREME, 30)))

# =================================================================== 02 · LOGO (versões)
tile = lambda x, y, w, h, bg, inner, extra='': BOX(x, y, w, h, bg, f'display:grid;place-items:center;overflow:hidden;{extra}', inner)
P.append(('v4-02-logo', 1080, 1350, VERDE,
  BOX(0, 0, 1080, 1350, f'{PAD_CREME},{VERDE}', 'background-size:360px 360px') +
  cabeca('02', 'Logo e versões') +
  A(60, 120, ANTON('Uma folha<br>que sobe.', 132, CREME, .88)) +
  A(640, 150, TXT('A folha de orégano é o tempero que fecha a pizza. A nervura é a seta das vendas subindo. A v4 mantém a marca aprovada e põe forno, cor e comida em volta dela.', 23, CREME, 'width:380px')) +
  tile(60, 430, 960, 360, CREME, logo(88, CARVAO), 'border-radius:22px;box-shadow:0 30px 60px -30px rgba(0,0,0,.6)') +
  tile(60, 810, 470, 200, CARVAO, logo(36, CREME, VERDE_CL, CARVAO, sub=False), 'border-radius:22px') +
  tile(550, 810, 470, 200, TOMATE, logo(36, CREME, CREME, TOMATE, sub=False), 'border-radius:22px') +
  tile(60, 1030, 228, 228, CREME, simbolo(130), 'border-radius:22px') +
  tile(304, 1030, 228, 228, ACAFRAO, simbolo(130, CARVAO, ACAFRAO), 'border-radius:22px') +
  tile(548, 1030, 228, 228, xadrez(VERDE, CREME, 19), f'<div style="width:150px;height:150px;border-radius:50%;background:{VERDE};display:grid;place-items:center">{simbolo(96, CREME, VERDE)}</div>', 'border-radius:22px') +
  tile(792, 1030, 228, 228, f'url({FOTO("pizza-close")}) center/cover', simbolo(130, CREME, CARVAO), 'border-radius:22px') +
  rodape('Mínimo: símbolo 24 px · nome 120 px', CREME)))

# =================================================================== 03 · LOGO SOBRE FOTO
P.append(('v4-03-logo-foto', 1080, 1350, CARVAO,
  BOX(0, 0, 1080, 760, f'linear-gradient(180deg,rgba(20,19,17,.2),rgba(20,19,17,.55)),url({FOTO("pa-no-forno")}) 40% center/cover') +
  cabeca('03', 'Logo sobre foto') +
  A(80, 520, logo(84, CREME, CREME, CARVAO)) +
  BOX(0, 760, 540, 590, f'linear-gradient(0deg,rgba(20,19,17,.7),rgba(20,19,17,.1) 60%),url({FOTO("queijo-puxando")}) center/cover') +
  A(40, 1180, logo(40, CREME, ACAFRAO, CARVAO, sub=False)) +
  BOX(540, 760, 540, 590, f'{PAD_TOM},{TOMATE}', 'background-size:300px 300px') +
  rec('pepperoni-fatia', 640, 800, 340, 18, .5) +
  A(580, 1180, logo(40, CREME, CREME, TOMATE, sub=False)) +
  A(80, 650, ETQ('Foto escura: logo creme · foto clara: véu carvão de 40% antes do logo', CREME, 'opacity:.85'))))

# =================================================================== 04 · CORES
cor_bl = lambda x, w, bg, fg, nome, hx, uso, pct: BOX(x, 0, w, 1350, bg, 'overflow:hidden', A(26, 1000, f'<div style="color:{fg}"><div style="font:400 44px/.9 Anton;text-transform:uppercase">{nome}</div><div style="font:500 16px/1.6 \'IBM Plex Mono\';margin-top:14px">{hx}<br>{uso}<br>{pct}</div></div>', w - 40))
P.append(('v4-04-cores', 1080, 1350, CARVAO,
  cor_bl(0, 280, CARVAO, CREME, 'Carvão<br>do forno', CARVAO, 'fundo · texto', '35%') +
  cor_bl(280, 260, VERDE, CREME, 'Verde<br>orégano', VERDE, 'marca · campo', '25%') +
  cor_bl(540, 200, TOMATE, CREME, 'Tomate', TOMATE, 'campo de oferta', '15% · NOVA') +
  cor_bl(740, 170, CREME, CARVAO, 'Creme<br>massa', CREME, 'papel', '15%') +
  cor_bl(910, 90, ACAFRAO, CARVAO, '', '', '', '') + cor_bl(1000, 80, BRASA, CREME, '', '', '', '') +
  A(840, 700, f'<div style="transform:rotate(-90deg);transform-origin:left top;white-space:nowrap;font:500 16px \'IBM Plex Mono\';color:{CARVAO}">AÇAFRÃO {ACAFRAO} · SELO E PREÇO · 5% · NOVA</div>', None, 'left:928px;top:980px') +
  A(0, 0, f'<div style="transform:rotate(-90deg);transform-origin:left top;white-space:nowrap;font:500 16px \'IBM Plex Mono\';color:{CREME}">BRASA {BRASA} · SÓ BOTÃO · 5%</div>', None, 'left:1016px;top:980px') +
  cabeca('04', 'Cores') +
  rec('pepperoni-inteira', 260, 470, 720, 0, .7) +
  A(60, 130, ANTON('Cor de<br>forno<br>aceso.', 150, CREME, .86, 'text-shadow:0 6px 30px rgba(0,0,0,.4)')) +
  rodape('2 a 3 cores fortes por peça, sempre chapadas', CREME)))

# =================================================================== 05 · LETRAS
P.append(('v4-05-letras', 1080, 1350, TOMATE,
  BOX(0, 0, 1080, 1350, f'{PAD_TOM},{TOMATE}', 'background-size:360px 360px') +
  cabeca('05', 'Letras') +
  A(36, 110, ANTON('Pizza', 470, CREME, .82, 'letter-spacing:-.01em')) +
  rec('queijo-puxando', 300, 150, 760, -4, .6) +
  BOX(0, 640, 1080, 710, CARVAO) +
  A(60, 680, ETQ('Manchete · Anton · caixa alta · só 1 a 4 palavras', ACAFRAO)) +
  A(60, 720, ANTON('Forno cheio na terça', 112, CREME, .9)) +
  A(60, 860, ETQ('Título · Inter Tight 800 · −4,5%', VERDE_CL)) +
  A(60, 900, TIGHT('Pizza boa não vende sozinha.', 64, CREME)) +
  A(60, 1010, ETQ('Texto · Inter 400', VERDE_CL)) +
  A(60, 1046, TXT('Frase curta, de WhatsApp. O dono lê entre um pedido e outro.', 26, '#d9d3c7', 'width:520px')) +
  A(640, 1010, ETQ('Número · IBM Plex Mono', VERDE_CL)) +
  A(640, 1040, f'<div style="font:500 92px/1 \'IBM Plex Mono\';letter-spacing:-.04em;color:{ACAFRAO}">R$ 39,90</div>') +
  A(640, 1140, ETQ('preço de exemplo', CINZA)) +
  rodape('Anton entra no v4; Inter Tight segue no sistema', CREME)))

# =================================================================== 06 · PADRÕES E SELOS
P.append(('v4-06-padroes-selos', 1080, 1350, VERDE,
  BOX(0, 0, 540, 540, xadrez(VERDE, CREME, 45)) +
  BOX(540, 0, 540, 540, f'{PAD_CREME},{VERDE}', 'background-size:270px 270px') +
  BOX(0, 540, 540, 540, f'{padrao_url(VERDE, .9, w=4)},{CREME}', 'background-size:270px 270px') +
  BOX(540, 540, 540, 540, xadrez(TOMATE, CREME, 45)) +
  A(40, 40, f'<div style="background:{CARVAO};padding:14px 18px;border-radius:12px">{ETQ("06 · Padrões e selos")}</div>') +
  A(70, 120, selo(380, 'MARKETING DE VENDAS PARA PIZZARIAS · SÃO LUÍS MA · ', VERDE, CREME, borda=CREME, fs=10.6)) +
  A(640, 110, selo(330, 'SÓ PIZZARIAS · SÓ PIZZARIAS · SÓ PIZZARIAS · ', CARVAO, ACAFRAO, centro=icone('fatia', 120, ACAFRAO, 6), borda=ACAFRAO, fs=13)) +
  A(90, 640, selo(330, 'RELATÓRIO TODA SEGUNDA · NÚMERO NA MESA · ', ACAFRAO, CARVAO, centro=ANTON('SEG', 86, CARVAO), borda=CARVAO, fs=11.2)) +
  A(640, 630, selo(350, 'VAGAS PARA 5 PIZZARIAS FUNDADORAS · ', TOMATE, CREME, centro=ANTON('5<br><span style="font-size:30px">vagas</span>', 110, CREME, .8, 'text-align:center'), borda=CREME, fs=12.5)) +
  BOX(0, 1080, 1080, 270, CARVAO) +
  A(60, 1110, ''.join(f'<div style="display:inline-block;margin-right:30px">{icone(n, 70, c)}</div>' for n, c in [('fatia', CREME), ('tomate', TOMATE), ('folha', VERDE_CL), ('pa', CREME), ('chama', ACAFRAO), ('pizza', CREME), ('manjericao', VERDE_CL), ('seta', ACAFRAO), ('caixa', CREME), ('celular', CREME)])) +
  A(60, 1210, TXT('Xadrez de cantina em verde ou tomate · ícones em traço único (5 px) · selos com texto em volta, sempre redondos.', 22, '#d9d3c7', 'width:960px')) +
  rodape('Textura da marca', CREME)))

# =================================================================== 07 · FOTOGRAFIA
ft = lambda x, y, w, h, n, pos='center', rot='': BOX(x, y, w, h, f'url({FOTO(n)}) {pos}/cover', f'filter:saturate(1.12) contrast(1.06);{rot}')
P.append(('v4-07-fotografia', 1080, 1350, CARVAO,
  ft(0, 0, 680, 700, 'queijo-puxando') + ft(684, 0, 396, 348, 'brasa') + ft(684, 352, 396, 348, 'pepperoni-cima') +
  ft(0, 704, 396, 380, 'pa-no-forno', '30% center') + ft(400, 704, 680, 380, 'fatia-puxando') +
  cabeca('07', 'Fotografia') +
  A(40, 560, ANTON('Comida grande.<br>Luz de forno.', 76, CREME, .9, 'text-shadow:0 4px 30px rgba(0,0,0,.6)')) +
  BOX(0, 1084, 1080, 266, CARVAO) +
  A(60, 1110, f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:40px;width:960px;font:400 21px/1.45 Inter;color:{CREME}">'
     f'<div><div style="font:400 34px Anton;color:{VERDE_CL};text-transform:uppercase">Sempre</div>queijo puxando, fatia saindo da pizza, forno aceso, caixa abrindo. Comida recortada e maior que a página. Sombra profunda, tom quente.</div>'
     f'<div><div style="font:400 34px Anton;color:{TOMATE};text-transform:uppercase">Nunca</div>ilustração no lugar da pizza, gente sorrindo para a câmera, filtro colorido. No post do cliente, a foto é a pizza DELE.</div></div>') +
  rodape('Fotos CC · créditos no manual', CINZA)))

# =================================================================== 08 · CAIXA DE PIZZA (mockup 3D em CSS)
def caixa3d(W=560, H=70, tampa_bg=None, rot='rotateX(58deg) rotateZ(-34deg)', lado=VERDE, conteudo='', aberta=False, dentro=''):
    tampa_bg = tampa_bg or f'{PAD_CREME},{VERDE}'
    face = lambda st, inner='': f'<div style="position:absolute;{st};backface-visibility:hidden">{inner}</div>'
    lados = (face(f'left:0;bottom:0;width:{W}px;height:{H}px;transform-origin:bottom;transform:rotateX(-90deg);background:linear-gradient(0deg,rgba(0,0,0,.28),rgba(0,0,0,.05)),{lado}',
                  f'<div style="height:100%;display:flex;align-items:center;justify-content:space-between;padding:0 24px;font:500 15px \'IBM Plex Mono\';letter-spacing:.2em;color:{CREME}"><span>@OREGANOTURBO</span><span>PEDIDO SAINDO →</span></div>') +
             face(f'right:0;top:0;width:{H}px;height:{W}px;transform-origin:right;transform:rotateY(90deg);background:linear-gradient(90deg,rgba(0,0,0,.38),rgba(0,0,0,.18)),{lado}'))
    if not aberta:
        top = face(f'inset:0;transform:translateZ({H}px);background:{tampa_bg};background-size:280px 280px;box-shadow:inset 0 0 0 6px rgba(0,0,0,.08)', conteudo)
    else:
        top = (face(f'inset:0;transform:translateZ(2px);background:{KRAFT};box-shadow:inset 0 0 60px rgba(0,0,0,.35)', dentro) +
               f'<div style="position:absolute;left:0;top:-{W}px;width:{W}px;height:{W}px;transform-origin:bottom;transform:translateZ({H}px) rotateX(-78deg);transform-style:preserve-3d">'
               + face(f'inset:0;background:{tampa_bg};background-size:280px 280px', conteudo)
               + face(f'inset:0;transform:rotateY(180deg);background:{KRAFT};box-shadow:inset 0 0 80px rgba(0,0,0,.3)') + '</div>'
               + face(f'left:0;top:0;width:{W}px;height:{H}px;transform-origin:top;transform:rotateX(90deg);background:linear-gradient(0deg,rgba(0,0,0,.15),rgba(0,0,0,.35)),{KRAFT}'))
    return (f'<div style="width:{W}px;height:{W}px;position:relative;transform-style:preserve-3d;transform:{rot}">'
            f'<div style="position:absolute;inset:-40px;background:rgba(0,0,0,.55);filter:blur(40px);transform:translateZ(-1px) translate(40px,40px)"></div>{lados}{top}</div>')
tampa_logo = (f'<div style="position:absolute;inset:0;display:grid;place-items:center">'
              f'<div style="width:330px;height:330px;border-radius:50%;background:{CREME};display:grid;place-items:center;box-shadow:0 0 0 10px {VERDE},0 0 0 16px {CREME}">'
              f'<div style="text-align:center">{simbolo(110, VERDE, CREME)}<div style="font:800 40px/.9 \'Inter Tight\';letter-spacing:-.045em;color:{CARVAO};margin-top:12px">Orégano<br>Turbo</div></div></div></div>'
              f'<div style="position:absolute;left:0;right:0;bottom:0;height:56px;background:{xadrez(TOMATE, CREME, 14)}"></div>')
dentro = f'<img src="{REC("calabresa")}" style="position:absolute;left:4%;top:4%;width:92%;height:92%;object-fit:contain;filter:drop-shadow(0 6px 10px rgba(0,0,0,.4))">'
P.append(('v4-08-mockup-caixa', 1080, 1350, TOMATE,
  BOX(0, 0, 1080, 1350, f'{PAD_TOM},{TOMATE}', 'background-size:360px 360px') +
  cabeca('08', 'Mockup · caixa de pizza') +
  A(60, 110, ANTON('A caixa<br>é o anúncio<br>que volta.', 104, CREME, .88)) +
  A(640, 600, f'<div style="perspective:2400px">{caixa3d(420, 60, aberta=True, dentro=dentro, conteudo=tampa_logo, rot="rotateX(56deg) rotateZ(-24deg)")}</div>', extra='') +
  A(60, 800, f'<div style="perspective:2400px">{caixa3d(440, 62, conteudo=tampa_logo, rot="rotateX(58deg) rotateZ(-40deg)")}</div>') +
  A(60, 730, f'<div style="perspective:2400px">{caixa3d(440, 62, conteudo=tampa_logo, rot="rotateX(58deg) rotateZ(-40deg)")}</div>') +
  A(60, 440, TXT('Tampa com o padrão de ícones e o selo no centro. Lateral com o @ e "pedido saindo". Faixa xadrez fecha a caixa como lacre.', 22, CREME, 'width:430px')) +
  A(800, 1020, selo(200, 'TAMPA · LATERAL · LACRE · ADESIVO · ', CARVAO, ACAFRAO, centro=icone('caixa', 70, ACAFRAO, 6), borda=CREME, fs=14)) +
  BOX(0, 1250, 1080, 100, CARVAO, '', A(60, 36, ETQ('Caixa 35 × 35 cm · impressão 2 cores + kraft', CREME)))))

# =================================================================== 09 · UNIFORME (camiseta + avental)
def camiseta(w, cor=CARVAO, frente=''):
    return (f'<div style="position:relative;width:{w}px;height:{w * 1.06}px;filter:drop-shadow(0 40px 50px rgba(0,0,0,.55))">'
            f'<svg viewBox="0 0 500 530" width="{w}" height="{w * 1.06}" style="position:absolute;inset:0"><defs><linearGradient id="dobra" x1="0" x2="1">'
            f'<stop offset="0" stop-color="#000" stop-opacity=".25"/><stop offset=".25" stop-color="#fff" stop-opacity=".06"/><stop offset=".55" stop-color="#000" stop-opacity=".08"/><stop offset=".8" stop-color="#fff" stop-opacity=".05"/><stop offset="1" stop-color="#000" stop-opacity=".3"/></linearGradient></defs>'
            f'<path d="M170 20 C200 44 300 44 330 20 L470 80 L430 200 L380 180 L385 515 L115 515 L120 180 L70 200 L30 80 Z" fill="{cor}"/>'
            f'<path d="M170 20 C200 44 300 44 330 20 L470 80 L430 200 L380 180 L385 515 L115 515 L120 180 L70 200 L30 80 Z" fill="url(#dobra)"/>'
            f'<path d="M172 22 C205 64 295 64 328 22" fill="none" stroke="rgba(255,255,255,.18)" stroke-width="8"/></svg>'
            f'<div style="position:absolute;left:0;right:0;top:{w * .26}px;display:grid;place-items:center">{frente}</div></div>')
def avental(w, cor=VERDE, frente=''):
    return (f'<div style="position:relative;width:{w}px;height:{w * 1.4}px;filter:drop-shadow(0 40px 50px rgba(0,0,0,.55))">'
            f'<svg viewBox="0 0 400 560" width="{w}" height="{w * 1.4}" style="position:absolute;inset:0"><defs><linearGradient id="av" x1="0" x2="1">'
            f'<stop offset="0" stop-color="#000" stop-opacity=".3"/><stop offset=".35" stop-color="#fff" stop-opacity=".07"/><stop offset=".7" stop-color="#000" stop-opacity=".05"/><stop offset="1" stop-color="#000" stop-opacity=".35"/></linearGradient></defs>'
            f'<path d="M130 10 C130 -20 270 -20 270 10" fill="none" stroke="{CREME}" stroke-width="10"/>'
            f'<path d="M120 10 L280 10 L285 150 C300 190 360 200 380 210 L370 550 L30 550 L20 210 C40 200 100 190 115 150 Z" fill="{cor}"/>'
            f'<path d="M20 214 L-40 230 M380 214 L440 230" stroke="{CREME}" stroke-width="10"/>'
            f'<rect x="110" y="370" width="180" height="120" rx="8" fill="{CREME}"/><rect x="110" y="370" width="180" height="120" rx="8" fill="url(#xd)"/>'
            f'<defs><pattern id="xd" width="30" height="30" patternUnits="userSpaceOnUse"><rect width="15" height="15" fill="{TOMATE}"/><rect x="15" y="15" width="15" height="15" fill="{TOMATE}"/></pattern></defs>'
            f'<path d="M120 10 L280 10 L285 150 C300 190 360 200 380 210 L370 550 L30 550 L20 210 C40 200 100 190 115 150 Z" fill="url(#av)"/>'
            f'<path d="M110 370 L290 370" stroke="rgba(0,0,0,.25)" stroke-width="4"/></svg>'
            f'<div style="position:absolute;left:0;right:0;top:{w * .5}px;display:grid;place-items:center">{frente}</div></div>')
def bone(w, cor=TOMATE):
    h = w * .72
    return (f'<div style="position:relative;width:{w}px;height:{h}px;filter:drop-shadow(18px 22px 3px rgba(0,0,0,.4))">'
            f'<svg viewBox="0 0 300 216" width="{w}" height="{h}" style="position:absolute;inset:0"><defs><radialGradient id="bn" cx=".35" cy=".3" r=".8">'
            f'<stop offset="0" stop-color="#fff" stop-opacity=".25"/><stop offset=".6" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".35"/></radialGradient></defs>'
            f'<path d="M40 150 C 30 60 90 14 160 14 C 230 14 262 70 258 150 Z" fill="{cor}"/><path d="M40 150 C 30 60 90 14 160 14 C 230 14 262 70 258 150 Z" fill="url(#bn)"/>'
            f'<path d="M150 16 C 140 60 138 110 146 150" stroke="rgba(0,0,0,.2)" stroke-width="3" fill="none"/><circle cx="160" cy="16" r="7" fill="{cor}"/>'
            f'<path d="M30 146 C 80 140 230 140 290 160 C 300 176 270 196 220 196 C 150 196 60 186 26 168 C 18 160 20 150 30 146 Z" fill="{VERDE}"/>'
            f'<path d="M30 146 C 80 140 230 140 290 160" stroke="rgba(0,0,0,.25)" stroke-width="4" fill="none"/></svg>'
            f'<div style="position:absolute;left:{w * .33}px;top:{h * .26}px;transform:rotate(-4deg)">{simbolo(w * .26, CREME, cor)}</div></div>')
P.append(('v4-09-mockup-uniforme', 1080, 1350, CARVAO,
  fundo_foto('bancada', .7, 'center', 'linear-gradient(180deg,rgba(20,19,17,.82),rgba(20,19,17,.7) 50%,rgba(20,19,17,.95))') +
  cabeca('09', 'Mockup · camiseta e avental') +
  A(60, 110, ANTON('Vestiu,<br>virou<br>marca.', 140, CREME, .86)) +
  A(30, 520, camiseta(520, CREME, f'<div style="text-align:center;margin-top:-20px">{ANTON("Só<br>pizzarias.", 70, TOMATE, .84)}<div style="margin:10px auto 0;width:fit-content">{selo(120, "ORÉGANO TURBO · SÃO LUÍS · ", VERDE, CREME, fs=14)}</div><div style="font:500 10px \'IBM Plex Mono\';letter-spacing:.2em;color:{CARVAO};margin-top:8px">COSTAS</div></div>'), extra='transform:rotate(-5deg)') +
  A(560, 230, avental(440, VERDE, f'<div style="text-align:center">{selo(170, "MARKETING DE VENDAS PARA PIZZARIAS · ", CREME, VERDE, fs=11)}</div>'), extra='transform:rotate(4deg)') +
  A(400, 1010, bone(330, TOMATE), extra='transform:rotate(-8deg)') +
  rodape('Camiseta (costas) · avental · boné', CREME)))

# =================================================================== 10 · COPO, SACOLA, ADESIVO
def copo(w, bg=CREME, pad=None, inner=''):
    h = w * 1.35
    return (f'<div style="position:relative;width:{w}px;height:{h}px;filter:drop-shadow(0 40px 40px rgba(0,0,0,.5))">'
            f'<div style="position:absolute;left:{w * .02}px;top:0;width:{w * .96}px;height:{w * .1}px;border-radius:50%;background:#fff;z-index:2;box-shadow:inset 0 -6px 10px rgba(0,0,0,.2)"></div>'
            f'<div style="position:absolute;left:0;top:{w * .05}px;width:{w}px;height:{h - w * .05}px;clip-path:polygon(0 0,100% 0,86% 100%,14% 100%);'
            f'background:linear-gradient(90deg,rgba(0,0,0,.35),rgba(255,255,255,.12) 30%,rgba(0,0,0,0) 55%,rgba(0,0,0,.3)),{pad or bg};background-size:auto,220px 220px;display:grid;place-items:center">{inner}</div></div>')
def sacola(w, inner=''):
    h = w * 1.25
    return (f'<div style="position:relative;width:{w}px;height:{h}px;filter:drop-shadow(0 40px 40px rgba(0,0,0,.5))">'
            f'<svg viewBox="0 0 400 500" width="{w}" height="{h}" style="position:absolute;inset:0"><path d="M130 110 C130 20 270 20 270 110" fill="none" stroke="#8a6a44" stroke-width="12"/></svg>'
            f'<div style="position:absolute;left:0;top:{h * .2}px;width:{w}px;height:{h * .8}px;background:linear-gradient(90deg,rgba(0,0,0,.18),rgba(255,255,255,.08) 40%,rgba(0,0,0,.2)),{KRAFT};'
            f'display:grid;place-items:center">{inner}</div>'
            f'<div style="position:absolute;left:0;top:{h * .2}px;width:{w}px;height:{w * .07}px;background:rgba(0,0,0,.12)"></div></div>')
P.append(('v4-10-mockup-copo-sacola', 1080, 1350, VERDE,
  BOX(0, 0, 1080, 1350, xadrez(VERDE, VERDE_ESC, 45)) +
  BOX(0, 0, 1080, 1350, 'radial-gradient(circle at 50% 55%,rgba(30,91,59,0) 0,rgba(10,30,20,.65) 85%)') +
  cabeca('10', 'Mockup · copo, sacola e adesivo') +
  A(60, 110, ANTON('Do balcão<br>até a porta.', 130, CREME, .86)) +
  A(80, 470, copo(300, VERDE, f'{PAD_CREME},{VERDE}', f'<div style="transform:translateY(-20px)">{simbolo(110, CREME, VERDE)}</div>')) +
  A(310, 600, copo(250, CREME, f'{padrao_url(VERDE, .9)},{CREME}', f'<div style="background:{CREME};padding:10px;border-radius:50%">{simbolo(80)}</div>')) +
  A(570, 360, sacola(440, f'<div style="text-align:center">{logo(30, CARVAO, VERDE, CREME, sub=False)}<div style="margin-top:30px;display:grid;place-items:center">{selo(170, "PEDIU, CHEGOU · BOM APETITE · ", TOMATE, CREME, centro=icone("fatia", 64, CREME, 6), fs=12.5)}</div></div>')) +
  A(80, 1040, selo(200, 'FEITO PARA VENDER · @OREGANOTURBO · ', ACAFRAO, CARVAO, borda=CREME, fs=12.5), extra='transform:rotate(-12deg)') +
  A(310, 1080, f'<div style="background:{CREME};border-radius:16px;padding:22px 26px;box-shadow:0 20px 40px -10px rgba(0,0,0,.6);transform:rotate(4deg)">{ANTON("Pedido saindo", 50, TOMATE)}<div style="font:500 13px \'IBM Plex Mono\';letter-spacing:.16em;color:{CARVAO};margin-top:8px">ADESIVO DE LACRE · 8 × 4 CM</div></div>') +
  rec('pepperoni-fatia', 800, 1000, 230, -30, .6) +
  rodape('Copo, sacola kraft, adesivo de lacre', CREME)))

# =================================================================== 11 · CARTÃO + PROPOSTA
cartao_f = f'<div style="width:420px;height:240px;border-radius:14px;background:{PAD_CREME},{VERDE};background-size:200px 200px;padding:30px;display:flex;flex-direction:column;justify-content:space-between;box-shadow:0 30px 60px -20px rgba(0,0,0,.7)">{simbolo(64, CREME, VERDE)}<div style="font:800 34px/1 \'Inter Tight\';letter-spacing:-.04em;color:{CREME}">Orégano Turbo</div></div>'
cartao_v = f'<div style="width:420px;height:240px;border-radius:14px;background:{CREME};padding:30px;display:flex;flex-direction:column;justify-content:space-between;box-shadow:0 30px 60px -20px rgba(0,0,0,.7);border-bottom:22px solid transparent;background-clip:padding-box;position:relative"><div><div style="font:700 24px Inter;color:{CARVAO}">Lindson Almeida</div><div style="font:400 15px Inter;color:{CINZA};margin-top:4px">Estrategista de vendas para pizzarias</div></div><div style="font:500 14px/1.7 \'IBM Plex Mono\';color:{CARVAO}">@oreganoturbo<br>WhatsApp: link na bio<br>São Luís · MA</div><div style="position:absolute;left:0;right:0;bottom:-22px;height:22px;background:{xadrez(TOMATE, CREME, 11)};border-radius:0 0 14px 14px"></div></div>'
proposta = (f'<div style="width:520px;height:680px;background:{CARVAO};border-radius:8px;position:relative;overflow:hidden;box-shadow:0 50px 90px -24px rgba(0,0,0,.75)">'
            f'<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(20,19,17,.2),rgba(20,19,17,.95) 72%),url({FOTO("forno-pizza")}) center/cover"></div>'
            f'<div style="position:absolute;left:36px;top:36px">{logo(22, CREME, VERDE_CL, CARVAO, sub=False)}</div>'
            f'<div style="position:absolute;right:30px;top:120px">{selo(130, "RAIO-X · DIAGNÓSTICO · RAIO-X · ", TOMATE, CREME, centro=icone("pizza", 50, CREME, 6), fs=13)}</div>'
            f'<div style="position:absolute;left:36px;bottom:40px;right:36px"><div style="font:500 13px \'IBM Plex Mono\';letter-spacing:.18em;color:{ACAFRAO}">RAIO-X DO DELIVERY · PIZZARIA DO EXEMPLO</div>'
            f'<div style="font:400 66px/.9 Anton;text-transform:uppercase;color:{CREME};margin-top:14px">Onde estão os pedidos que você está perdendo</div></div></div>')
P.append(('v4-11-mockup-cartao-proposta', 1080, 1350, TOMATE,
  BOX(0, 0, 1080, 1350, f'url({FOTO("calabresa")}) center/cover', 'filter:blur(2px) brightness(.55) saturate(1.2)') +
  BOX(0, 0, 1080, 1350, 'linear-gradient(180deg,rgba(20,19,17,.7),rgba(20,19,17,.2) 50%,rgba(20,19,17,.8))') +
  cabeca('11', 'Mockup · cartão e proposta') +
  A(60, 110, ANTON('O que chega<br>na mão do dono.', 110, CREME, .88)) +
  A(500, 380, proposta, extra='transform:rotate(5deg)') +
  A(70, 450, cartao_f, extra='transform:rotate(-8deg)') + A(100, 780, cartao_v, extra='transform:rotate(4deg)') +
  rec('pepperoni-fatia', 330, 1020, 260, 40, .7) +
  rodape('Na capa da proposta, a foto da pizzaria do cliente', CREME)))

# =================================================================== 12 · CELULAR: WhatsApp + relatório
chat = (f'<div style="background:#075e54;color:#fff;padding:20px 20px 14px;display:flex;align-items:center;gap:12px;margin-top:10px">'
        f'<div style="width:42px;height:42px;border-radius:50%;background:{TOMATE};display:grid;place-items:center;font:400 20px Anton;color:{CREME}">P</div>'
        f'<div><div style="font:600 18px \'Inter\'">Pizzaria do Exemplo</div><div style="font:400 13px \'Inter\';opacity:.8">online</div></div></div>'
        f'<div style="background:#efeae2;height:100%;padding:16px 14px;display:flex;flex-direction:column;gap:10px">'
        + balao('Boa noite! Vi o anúncio da calabresa. Ainda dá pra pedir?', hora='19:38')
        + balao('Dá sim! Média ou grande? Entrega em 40 min.', True, '19:38')
        + balao('Grande, metade calabresa metade frango.', hora='19:39')
        + balao('Anotado ✅ Total R$ 54,90. Pix ou cartão?', True, '19:39')
        + f'<div style="align-self:center;background:#fff3c4;font:500 13px \'Inter\';padding:6px 12px;border-radius:8px;color:#5a4a00">Pedido vindo do anúncio (exemplo)</div></div>')
lin = lambda r, v, c=CREME: f'<div style="display:flex;justify-content:space-between;padding:12px 0;border-bottom:1px solid #2c2a26;font:400 16px \'Inter\';color:#bdb7ab"><span>{r}</span><span style="font:500 17px \'IBM Plex Mono\';color:{c}">{v}</span></div>'
barras = ''.join(f'<div style="flex:1;height:{h}px;background:{ACAFRAO if i == 6 else "#3b3a35"};border-radius:6px 6px 0 0"></div>' for i, h in enumerate([40, 52, 48, 66, 74, 92, 120]))
rel = (f'<div style="padding:26px 26px 0;color:{CREME}">'
       f'<div style="display:flex;align-items:center;gap:10px">{simbolo(30, VERDE_CL, CARVAO)}<div style="font:700 17px \'Inter\'">Relatório de segunda</div></div>'
       f'<div style="font:500 12px \'IBM Plex Mono\';color:{ACAFRAO};margin-top:18px;letter-spacing:.12em">EXEMPLO ILUSTRATIVO</div>'
       f'<div style="font:400 92px/1 Anton;margin-top:8px">128</div><div style="font:400 15px \'Inter\';color:#bdb7ab">pedidos que vieram do anúncio</div>'
       f'<div style="display:flex;gap:8px;align-items:flex-end;height:120px;margin-top:20px">{barras}</div>'
       + lin('Investido no anúncio', 'R$ 900') + lin('Vendido pelo anúncio', 'R$ 3.690', VERDE_CL) + lin('Retorno', '4,1×', VERDE_CL)
       + f'<div style="margin-top:16px;background:{VERDE};border-radius:14px;padding:14px 16px;font:500 15px/1.4 \'Inter\'">Esta semana: repetir o anúncio da calabresa.</div></div>')
P.append(('v4-12-mockup-celular', 1080, 1350, VERDE,
  BOX(0, 0, 1080, 1350, f'{PAD_CREME},{VERDE}', 'background-size:360px 360px') +
  BOX(0, 820, 1080, 530, TOMATE) + BOX(0, 820, 1080, 40, xadrez(TOMATE, CREME, 20)) +
  cabeca('12', 'Mockup · WhatsApp e relatório') +
  A(60, 110, ANTON('Anúncio<br>vira<br>mensagem.<br>Mensagem<br>vira<br>pedido.', 74, CREME, .9)) +
  rec('queijo-puxando', -60, 640, 560, -8, .6) +
  A(450, 120, iphone(chat, 360, 760, '#075e54'), extra='transform:rotate(-5deg)') +
  A(700, 420, iphone(rel, 340, 760, CARVAO), extra='transform:rotate(6deg)') +
  A(60, 1200, ETQ('Conversa e números ilustrativos · não é promessa de resultado', CREME)) +
  rodape('Cópia: Owner.com (v3) + fatia flutuando (v4)', CREME)))

# =================================================================== 13 · INSTAGRAM (perfil + grade)
mini = lambda bg, inner, extra='': f'<div style="aspect-ratio:4/5;background:{bg};position:relative;overflow:hidden;{extra}">{inner}</div>'
mi = lambda n, x, y, w, r=0: f'<img src="{REC(n)}" style="position:absolute;left:{x}%;top:{y}%;width:{w}%;transform:rotate({r}deg);filter:drop-shadow(0 4px 6px rgba(0,0,0,.5))">'
mt = lambda t, s, c=CREME, pos='left:7%;top:6%', extra='': f'<div style="position:absolute;{pos};font:400 {s}px/.86 Anton;text-transform:uppercase;color:{c};{extra}">{t}</div>'
grade = ''.join([
  mini(TOMATE, mt('Terça<br>fraca?', 30) + mi('pepperoni-fatia', 30, 38, 70, -20)),
  mini(f'url({FOTO("queijo-puxando")}) center/cover', mt('Puxa<br>pedido', 30, CREME, 'left:7%;bottom:8%')),
  mini(VERDE, mt('4,1×', 52, ACAFRAO, 'left:7%;top:28%') + mt('exemplo', 11, CREME, 'left:8%;top:62%', 'font-family:IBM Plex Mono')),
  mini(xadrez(VERDE, CREME, 10), f'<div style="position:absolute;inset:14%;background:{CARVAO};display:grid;place-items:center">{mt("Pizza boa<br>não vende<br>sozinha", 17, CREME, "position:static")}</div>'),
  mini(CARVAO, mi('calabresa', 6, 22, 88) + mt('Pizza', 40, CREME, 'left:7%;top:4%')),
  mini(ACAFRAO, mt('3 erros<br>no seu<br>WhatsApp', 24, CARVAO)),
  mini(f'url({FOTO("pa-no-forno")}) 40% center/cover', mt('Forno<br>cheio', 30, CREME, 'left:7%;bottom:8%')),
  mini(CREME, mt('Relatório<br>de segunda', 20, VERDE) + f'<div style="position:absolute;left:8%;bottom:10%;font:400 46px Anton;color:{CARVAO}">128</div>'),
  mini(TOMATE, f'<div style="position:absolute;inset:0;display:grid;place-items:center">{selo(84, "5 VAGAS · FUNDADORAS · ", CREME, TOMATE, centro=ANTON("5", 34, TOMATE), fs=15)}</div>'),
])
perfil = (f'<div style="padding:16px 18px 0;font-family:Inter;color:#111">'
          f'<div style="font:700 19px Inter;margin:6px 0 14px">oreganoturbo ⌄</div>'
          f'<div style="display:flex;align-items:center;gap:22px"><div style="width:96px;height:96px;border-radius:50%;background:{VERDE};display:grid;place-items:center;flex:none;box-shadow:0 0 0 3px #fff,0 0 0 5px {TOMATE}">{simbolo(60, CREME, VERDE)}</div>'
          f'<div style="display:flex;gap:22px;text-align:center;font:400 14px Inter"><div><b style="font-size:18px">9</b><br>posts</div><div><b style="font-size:18px">—</b><br>seguidores</div><div><b style="font-size:18px">—</b><br>seguindo</div></div></div>'
          f'<div style="font:600 15px Inter;margin-top:12px">Orégano Turbo | Mkt Pizzarias</div>'
          f'<div style="font:400 14px/1.4 Inter;margin-top:2px">Marketing de vendas só para pizzarias 🍕<br>Anúncio, Instagram e WhatsApp<br>Relatório toda segunda · São Luís/MA<br><span style="color:#00376b">Diagnóstico grátis do seu delivery ↓</span></div>'
          f'<div style="display:flex;gap:14px;margin:14px 0 10px">' + ''.join(f'<div style="text-align:center;font:400 11px Inter"><div style="width:58px;height:58px;border-radius:50%;border:2px solid #ddd;padding:3px"><div style="width:100%;height:100%;border-radius:50%;background:{c};display:grid;place-items:center">{icone(i, 30, f, 7)}</div></div>{n}</div>' for c, f, i, n in [(TOMATE, CREME, 'fatia', 'Método'), (VERDE, CREME, 'seta', 'Planos'), (ACAFRAO, CARVAO, 'celular', 'Pedidos'), (CARVAO, CREME, 'pizza', 'Raio-X')]) +
          f'</div></div><div style="display:grid;grid-template-columns:repeat(3,1fr);gap:2px">{grade}</div>')
P.append(('v4-13-instagram', 1080, 1350, CARVAO,
  BOX(0, 0, 1080, 1350, f'{padrao_url(CREME, .08)},{CARVAO}', 'background-size:360px 360px') +
  BOX(0, 0, 520, 1350, TOMATE) +
  cabeca('13', 'Aplicação · Instagram') +
  A(60, 110, ANTON('Um feed<br>com cheiro<br>de forno.', 92, CREME, .88)) +
  A(60, 520, TXT('Nove composições que se revezam: palavra gigante, comida voando, número, xadrez, cardápio. Nunca duas iguais lado a lado.', 23, CREME, 'width:400px')) +
  A(60, 760, ''.join(f'<div style="display:flex;gap:14px;align-items:center;margin-bottom:14px"><div style="width:24px;height:24px;border-radius:6px;background:{c};box-shadow:0 0 0 2px {CREME}"></div><span style="font:500 21px Inter;color:{CREME}">{t}</span></div>' for c, t in [(TOMATE, 'Oferta / chamada'), (VERDE, 'Número / prova'), (ACAFRAO, 'Dica direta'), (CARVAO, 'Foto real + manchete')])) +
  A(250, 960, selo(210, 'NOVE POSTS · NOVE COMPOSIÇÕES · ', VERDE, CREME, borda=CREME, fs=13.5)) +
  rec('pepperoni-fatia', 40, 980, 260, -24, .6) +
  A(560, 120, iphone(perfil, 460, 1060)) +
  rodape('Grade de 9 · perfil @oreganoturbo', CREME)))

# =================================================================== 14 · POST A — "Terça fraca?" (fatias voando · AQUI NÃO TEM ERRO)
P.append(('v4-14-post-terca', 1080, 1350, TOMATE,
  BOX(0, 0, 1080, 1350, f'radial-gradient(circle at 60% 55%,#e8452f 0,{TOMATE} 45%,#9c160f 100%)') +
  A(60, 60, logo(34, CREME, CREME, TOMATE, sub=False)) +
  A(54, 150, ANTON('Terça', 330, CREME, .84)) +
  A(64, 440, ANTON('fraca?', 170, ACAFRAO, .84)) +
  rec('pepperoni-fatia', 560, 430, 500, -28, .55) +
  rec('pepperoni-fatia', 760, 120, 300, 150, .55) +
  rec('queijo-puxando', -90, 650, 640, 8, .55) +
  voa('calabresa-2', 470, 640, 120, 10, 5) + voa('manjericao-4', 400, 1010, 120, -40) + voa('calabresa-6', 900, 1000, 150, 20) + voa('azeitona-1', 560, 960, 80, 0, 3) +
  A(60, 1090, TIGHT('Dia fraco tem conserto.', 46, CREME, 'text-shadow:0 4px 20px rgba(0,0,0,.5)'), 620) +
  A(60, 1190, f'<div style="display:inline-block;background:{CREME};color:{TOMATE};font:700 28px Inter;padding:22px 36px;border-radius:999px;box-shadow:0 12px 30px -8px rgba(0,0,0,.5)">Diagnóstico grátis →</div>') +
  A(860, 1150, selo(170, 'SÓ PIZZARIAS · SÓ PIZZARIAS · ', VERDE, CREME, borda=CREME, fs=15))))

# =================================================================== 15 · POST B — "PIZZA" gigante atrás da pizza
P.append(('v4-15-post-pizza', 1080, 1350, VERDE,
  BOX(0, 0, 1080, 1350, f'{PAD_CREME},{VERDE}', 'background-size:360px 360px') +
  BOX(0, 0, 1080, 70, xadrez(VERDE, CREME, 35)) + BOX(0, 1280, 1080, 70, xadrez(VERDE, CREME, 35)) +
  A(-20, 120, ANTON('Pizza', 560, CREME, .8, 'letter-spacing:-.02em;opacity:.97')) +
  voa('manjericao-3', 40, 420, 150, -20) + voa('calabresa-3', 900, 330, 140, 15, 4) +
  rec('calabresa', 120, 340, 840, 10, .75) +
  voa('azeitona-3', 80, 860, 90, 30) + voa('manjericao-1', 880, 820, 150, 40) + voa('calabresa-5', 700, 300, 110, 0, 6) +
  A(60, 1010, TIGHT(f'Pizza boa<br>não vende {circulo("sozinha.", ACAFRAO)}', 84, CREME)) +
  A(60, 1205, logo(30, CREME, CREME, VERDE, sub=False)) +
  A(820, 1000, selo(190, 'MARKETING PARA PIZZARIAS · ', TOMATE, CREME, borda=CREME, fs=14.5)) +
  ''))

# =================================================================== 16 · AVATAR
P.append(('v4-16-avatar', 1080, 1080, VERDE,
  BOX(0, 0, 1080, 1080, f'radial-gradient(circle at 50% 50%,#24704a 0,{VERDE} 55%,{VERDE_ESC} 100%)') +
  A(0, 0, f'<div style="width:1080px;height:1080px;display:grid;place-items:center">{simbolo(640, CREME, VERDE)}</div>')))

# =================================================================== 17 · LINGUAGEM DE CAMPANHA (régua do Lindson, 06/11: grade de 4 cores, produto com atitude)
q = lambda x, y, bg, palavra, cor, img, ix, iy, iw, ir, sub: (BOX(x, y, 540, 640, bg, 'overflow:hidden',
      A(30, 26, ANTON(palavra, 210, cor, .84)) + f'<img src="{REC(img)}" style="position:absolute;left:{ix}px;top:{iy}px;width:{iw}px;transform:rotate({ir}deg);filter:drop-shadow(0 30px 30px rgba(0,0,0,.45)) saturate(1.15) contrast(1.05)">'
      ))
P.append(('v4-17-campanha', 1080, 1350, CARVAO,
  q(0, 0, ACAFRAO, 'Puxa.', CARVAO, 'queijo-puxando', 40, 230, 560, -6, 'O queijo chama') +
  q(540, 0, VERDE, 'Pede.', CREME, 'pepperoni-fatia', 170, 170, 360, 24, 'A fatia vende') +
  q(0, 640, TOMATE, 'Chega.', CREME, 'pepperoni-cima', 90, 240, 470, -10, 'A caixa abre') +
  q(540, 640, CREME, 'Volta.', VERDE, 'pizza-close', 60, 250, 520, 8, 'O cliente repete') +
  BOX(0, 1280, 1080, 70, CARVAO, '', A(60, 26, f'<div style="display:flex;justify-content:space-between;width:960px">{ETQ("17 · Linguagem de campanha", CREME)}{ETQ("Foto com flash + cor chapada", ACAFRAO)}</div>')) +
  A(400, 520, selo(240, 'ORÉGANO TURBO · SÓ PIZZARIAS · ', CARVAO, CREME, borda=CREME, fs=14.5))))

FONTS = '<link href="https://fonts.googleapis.com/css2?family=Anton&family=Inter+Tight:wght@600;700;800&family=Inter:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">'
GRAO = "url(\"data:image/svg+xml;utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='300'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='300' height='300' filter='url(%23n)'/%3E%3C/svg%3E\")"
CSS = 'body{margin:0;background:#888}section.f::after{content:"";position:absolute;inset:0;background:' + GRAO + ';opacity:.07;mix-blend-mode:overlay;pointer-events:none;z-index:50}section.f{position:relative;overflow:hidden;margin:0 0 40px}.a{position:absolute}*{box-sizing:border-box}img{height:auto}'
d = os.path.dirname(os.path.abspath(__file__))
so = os.environ.get('SO')
open(os.path.join(d, 'pecas4.html'), 'w').write(
    f'<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>'
    + ''.join(f'<section class="f" id="{i}" style="width:{w}px;height:{h}px;background:{bg}">{c}</section>' for i, w, h, bg, c in P if not so or so in i) + '</body></html>')
print(len(P), 'pranchas → pecas4.html')
