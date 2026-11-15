# Kit do canal do YouTube da Orégano Turbo · Paollo, conta Zuleide, 15/11/2026
# Sistema v4 (tomate, verde, creme, carvão, açafrão em detalhe, Bagel Fat One, xadrez). Modelos: TEMPLATE.md
# Uso: python3 gerar.py && NODE_PATH=$(npm root -g) node render.js && python3 previa.py
import os
D = os.path.dirname(os.path.abspath(__file__))
VERDE, TOMATE, CREME, ACAFRAO, CARVAO = '#1E5B3B', '#C8302B', '#F3EEE6', '#F2B33D', '#141311'
F = lambda n: f'fotos/{n}.jpg'
R = lambda n: f'recortes/{n}.png'
BAGEL = '../reels/motor/fontes/bagel.ttf'
ANTON = '../../../conteudo/youtube/raposa-e-leao/produto/fonts/Anton-Regular.ttf'

def simbolo(t, folha=VERDE, seta=CREME):
    return (f'<svg viewBox="0 0 100 100" width="{t}" height="{t}" style="display:block">'
            f'<path d="M18 86 C 14 50, 40 18, 86 14 C 86 58, 58 88, 18 86 Z" fill="{folha}"/>'
            f'<path d="M26 76 L44 58 L54 66 L72 40" fill="none" stroke="{seta}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<path d="M60 38 L74 38 L74 52" fill="none" stroke="{seta}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></svg>')
def logo(t, cor=CREME, folha=None, seta=None):
    folha = folha or cor; seta = seta or (VERDE if cor == CREME else CREME)
    return (f'<div style="display:flex;align-items:center;gap:{t*.26:.0f}px">{simbolo(t*1.15, folha, seta)}'
            f'<div style="font:800 {t}px/0.9 Inter;letter-spacing:-.045em;color:{cor};white-space:nowrap">Orégano Turbo</div></div>')
xadrez = lambda a, b, t=60: f'repeating-conic-gradient({a} 0 25%,{b} 0 50%) 0 0/{t*2}px {t*2}px'
def comanda(n, t=1, bg=CREME, fg=CARVAO):
    return (f'<div style="background:{bg};color:{fg};padding:{14*t:.0f}px {22*t:.0f}px;border:{3*t:.0f}px dashed {fg};font:700 {22*t:.0f}px/1 \'IBM Plex Mono\',monospace;'
            f'letter-spacing:.08em;transform:rotate(-4deg);box-shadow:{10*t:.0f}px {12*t:.0f}px 0 rgba(0,0,0,.35)">PEDIDO Nº {n}</div>')
def tarja(txt, fs, bg=TOMATE, fg=CREME, rot=-2):
    return f'<div style="display:inline-block;background:{bg};color:{fg};font:400 {fs}px/1 Anton;padding:{fs*.18:.0f}px {fs*.35:.0f}px;transform:rotate({rot}deg);letter-spacing:.02em">{txt}</div>'
A = lambda x, y, inner, ex='': f'<div style="position:absolute;left:{x}px;top:{y}px;{ex}">{inner}</div>'

S = []
def sec(id, w, h, bg, inner):
    S.append(f'<section class="f" id="{id}" style="width:{w}px;height:{h}px;background:{bg}">{inner}</section>')

# 1) BANNER 2560x1440 · área segura central 1546x423 (x 507-2053, y 508-931): logo, manchete e selo dentro dela
fx, fy = 507, 508
sec('banner-2560x1440', 2560, 1440, CARVAO,
    f'<div style="position:absolute;inset:0;background:url({F(3343622)}) center 60%/cover;filter:saturate(1.15) contrast(1.05)"></div>'
    f'<div style="position:absolute;inset:0;background:linear-gradient(90deg,{CARVAO} 0%,rgba(20,19,17,.92) 40%,rgba(20,19,17,.2) 72%,rgba(20,19,17,.5) 100%)"></div>'
    f'<div style="position:absolute;left:0;right:0;top:0;height:120px;background:{xadrez(TOMATE, CREME, 60)}"></div>'
    f'<div style="position:absolute;left:0;right:0;bottom:0;height:120px;background:{xadrez(TOMATE, CREME, 60)}"></div>'
    + A(fx, fy, logo(40, CREME, ACAFRAO, CARVAO))
    + A(fx, fy + 70, f'<div style="font:400 104px/0.92 Bagel;color:{CREME};letter-spacing:-.01em">Marketing que enche<br><span style="color:{ACAFRAO}">o forno</span> da pizzaria</div>')
    + A(fx, fy + 290, f'<div style="font:600 30px/1.2 Inter;color:{CREME};opacity:.92">Só pizzarias · Shorts todo dia · aula nova toda quinta</div>')
    + A(1740, fy + 20, f'<div style="width:280px;height:280px;border-radius:50%;background:{TOMATE};display:grid;place-items:center;text-align:center;transform:rotate(8deg);box-shadow:0 0 0 10px {CREME},18px 20px 0 rgba(0,0,0,.4)">'
      f'<div style="font:400 66px/0.9 Bagel;color:{CREME}">SÓ<br>PIZZA<br>RIAS</div></div>')
    + A(1560, fy + 300, comanda('YT-01', 1.1)))

# 2) FOTO DE PERFIL 800x800 (o YouTube corta em círculo; símbolo lido a 40 px)
sec('perfil-800', 800, 800, VERDE,
    f'<div style="position:absolute;inset:0;background:{xadrez("#174A30", VERDE, 50)}"></div>'
    f'<div style="position:absolute;left:80px;top:80px;width:640px;height:640px;border-radius:50%;background:{TOMATE};box-shadow:0 0 0 18px {CREME}"></div>'
    + A(190, 170, simbolo(420, CREME, TOMATE)))

# 3) MARCA-D'ÁGUA 150x150 (PNG transparente)
sec('marca-dagua-150', 150, 150, 'transparent',
    f'<div style="position:absolute;left:8px;top:8px;width:134px;height:134px;border-radius:50%;background:{TOMATE};box-shadow:0 0 0 5px {CREME}"></div>' + A(30, 28, simbolo(90, CREME, TOMATE)))

# 4) THUMBNAIL LONGO 1 · forno e chama, tarja + manchete gorda (Restaurant Boss + Toast)
sec('thumb-longo-1-dia-fraco', 1280, 720, CARVAO,
    f'<div style="position:absolute;right:0;top:0;width:680px;height:720px;background:url({F(14978624)}) center 35%/cover"></div>'
    f'<div style="position:absolute;inset:0;background:linear-gradient(90deg,{CARVAO} 42%,rgba(20,19,17,0) 72%)"></div>'
    f'<div style="position:absolute;left:0;top:0;bottom:0;width:26px;background:{xadrez(TOMATE, CREME, 13)}"></div>'
    + A(70, 66, tarja('TERÇA PARADA?', 64, ACAFRAO, CARVAO, -3))
    + A(70, 190, f'<div style="font:400 128px/0.88 Bagel;color:{CREME}">5 ações<br>que <span style="color:{TOMATE}">enchem</span><br>o forno</div>')
    + A(76, 620, f'<div style="font:700 30px Inter;color:{CREME};opacity:.9">sem dar desconto</div>')
    + A(1010, 612, f'<div style="background:{CREME};border-radius:14px;padding:10px 14px">{logo(22, CARVAO, VERDE, CREME)}</div>'))

# 5) THUMBNAIL LONGO 2 · fatia recortada em cor chapada, palavra gigante atrás (Pizza Hut BR + favoritas)
sec('thumb-longo-2-taxa-do-app', 1280, 720, TOMATE,
    A(-10, 60, f'<div style="font:400 440px/0.8 Bagel;color:#A92420;letter-spacing:-.03em;white-space:nowrap">APP</div>')
    + A(150, -1180, f'<img src="{R(4109050)}" style="width:2200px;filter:drop-shadow(24px 30px 0 rgba(0,0,0,.3))">')
    + A(60, 66, tarja('TAXA DO APP', 70, CARVAO, CREME, -3))
    + A(60, 420, f'<div style="font:400 108px/0.9 Bagel;color:{CREME}">Traga o cliente<br>pro <span style="color:{ACAFRAO}">seu zap</span></div>')
    + A(1010, 612, f'<div style="background:{CREME};border-radius:14px;padding:10px 14px">{logo(22, CARVAO, VERDE, CREME)}</div>'))

# 6) CAPA DE SHORT 1080x1920 · gente comendo, texto no topo, rodapé livre para a interface
sec('capa-short-1080x1920', 1080, 1920, VERDE,
    f'<div style="position:absolute;inset:0;background:url({F(32230550)}) 30% center/cover"></div>'
    f'<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(20,19,17,.9) 0%,rgba(20,19,17,.15) 48%,rgba(20,19,17,0) 70%,rgba(20,19,17,.8) 100%)"></div>'
    + A(80, 200, tarja('DONO DE PIZZARIA', 74, TOMATE, CREME, -3))
    + A(80, 340, f'<div style="font:400 140px/0.88 Bagel;color:{CREME}">A pergunta<br>que aumenta<br>o <span style="color:{ACAFRAO}">pedido</span></div>')
    + A(80, 1500, comanda('20', 1.6))
    + A(80, 1660, logo(44)))

html = ('<!doctype html><meta charset="utf-8"><style>'
        f'@font-face{{font-family:Bagel;src:url({BAGEL})}}@font-face{{font-family:Anton;src:url({ANTON})}}'
        'body{margin:0;background:transparent}section.f{position:relative;overflow:hidden;margin:0 0 40px}</style>' + ''.join(S))
open(os.path.join(D, 'pecas.html'), 'w').write(html)
print(len(S), 'peças')
