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

# v2 (15/11, reprovada a v1 por fugir do Instagram): mesma identidade do feed aprovado (perfil/previa-perfil.jpg, social/v4):
# fundo verde-escuro com xadrez verde, manchete Bagel tomate com contorno creme, tarja creme, comanda Nº, botão "CHAMA NO ZAP »".
VESC = '#174A30'
FUNDO = f'{xadrez(VESC, VERDE, 40)}'
def manchete(txt, fs, cor=TOMATE, sub=None, subfs=None):
    h = f'<div style="font:400 {fs}px/0.86 Bagel;color:{cor};-webkit-text-stroke:{fs*.045:.0f}px {CREME};paint-order:stroke fill;text-shadow:{fs*.05:.0f}px {fs*.06:.0f}px 0 {CARVAO}">{txt}</div>'
    if sub: h += f'<div style="font:400 {subfs}px/1 Bagel;color:{ACAFRAO};margin-top:{subfs*.2:.0f}px">{sub}</div>'
    return h
def zap(fs=26):
    return f'<div style="display:inline-block;background:{TOMATE};color:{CREME};font:800 {fs}px Inter;padding:{fs*.55:.0f}px {fs*1.1:.0f}px;border-radius:999px;box-shadow:0 0 0 {fs*.15:.0f}px {CREME}">CHAMA NO ZAP »</div>'
def selo_n(n, t=150):
    return (f'<div style="width:{t}px;height:{t}px;border-radius:50%;background:{CREME};display:grid;place-items:center;transform:rotate(-8deg);box-shadow:{t*.06:.0f}px {t*.07:.0f}px 0 rgba(0,0,0,.35)">'
            f'<div style="font:400 {t*.36:.0f}px/1 Bagel;color:{TOMATE}">Nº{n}</div></div>')
CARD = lambda w, h, inner, ex='': f'<div style="width:{w}px;height:{h}px;background:{CREME};border-radius:18px;overflow:hidden;box-shadow:14px 16px 0 rgba(0,0,0,.35);{ex}">{inner}</div>'

# 1) BANNER 2560x1440 · área segura 1546x423 (x 507-2053, y 508-931)
fx, fy = 507, 508
sec('banner-2560x1440', 2560, 1440, VERDE,
    f'<div style="position:absolute;inset:0;background:{FUNDO}"></div>'
    f'<div style="position:absolute;left:0;right:0;top:0;height:80px;background:{xadrez(TOMATE, CREME, 40)}"></div>'
    f'<div style="position:absolute;left:0;right:0;bottom:0;height:80px;background:{xadrez(TOMATE, CREME, 40)}"></div>'
    + A(fx, fy, logo(38))
    + A(fx, fy + 66, manchete('MARKETING SÓ', 118, TOMATE))
    + A(fx, fy + 176, manchete('PARA PIZZARIAS.', 118, CREME))
    + A(fx, fy + 312, f'<div style="display:flex;gap:26px;align-items:center">{zap(30)}<div style="font:700 28px Inter;color:{CREME}">Shorts todo dia · aula nova toda quinta</div></div>')
    + A(1560, fy - 40, f'<div style="transform:rotate(5deg)">' + CARD(440, 500, f'<div style="height:400px;background:url({F(3343622)}) center/cover"></div><div style="padding:16px 22px;font:700 24px \'IBM Plex Mono\',monospace;color:{CARVAO}">PEDIDO Nº YT-01</div>') + '</div>')
    + A(1900, fy + 300, selo_n('01', 160)))

# 3) MARCA-D'ÁGUA 150x150 · o mesmo avatar do Instagram
sec('marca-dagua-150', 150, 150, 'transparent', f'<img src="../social/perfil/avatar-1080.png" style="width:150px;height:150px;border-radius:50%;display:block">')

# 4) THUMB LONGO 1 · composição "Terça também tem fome" do feed (manchete tomate + tarja + foto em cartão)
sec('thumb-longo-1-dia-fraco', 1280, 720, VERDE,
    f'<div style="position:absolute;inset:0;background:{FUNDO}"></div>'
    + A(720, 60, f'<div style="transform:rotate(4deg)">' + CARD(500, 560, f'<div style="height:480px;background:url({F(14978624)}) center 40%/cover"></div><div style="padding:14px 20px;font:700 22px \'IBM Plex Mono\',monospace;color:{CARVAO}">SEG · TER · QUA</div>') + '</div>')
    + A(60, 60, manchete('TERÇA', 190, TOMATE))
    + A(66, 250, manchete('PARADA?', 100, CREME))
    + A(66, 400, f'<div style="font:400 58px/1.05 Bagel;color:{ACAFRAO}">5 ações que<br>enchem o forno</div>')
    + A(66, 580, zap(24))
    + A(1110, 540, selo_n('02', 140)))

# 5) THUMB LONGO 2 · composição "A conta do pedido" do feed (cartões NO APP × NO ZAP)
sec('thumb-longo-2-taxa-do-app', 1280, 720, VERDE,
    f'<div style="position:absolute;inset:0;background:{FUNDO}"></div>'
    + A(60, 50, manchete('TAXA DO APP', 132, TOMATE))
    + A(66, 200, manchete('TRAGA PRO SEU ZAP.', 78, CREME))
    + A(60, 340, f'<div style="transform:rotate(-3deg)">' + CARD(330, 300, f'<div style="background:{TOMATE};color:{CREME};font:400 46px Bagel;padding:14px 22px">NO APP</div><div style="padding:18px 22px;font:600 22px/1.7 \'IBM Plex Mono\',monospace;color:{CARVAO}">pedido ✓<br>comissão ✗<br>cliente é do app</div>') + '</div>')
    + A(430, 360, f'<div style="transform:rotate(3deg)">' + CARD(330, 300, f'<div style="background:{VERDE};color:{CREME};font:400 46px Bagel;padding:14px 22px">NO ZAP</div><div style="padding:18px 22px;font:600 22px/1.7 \'IBM Plex Mono\',monospace;color:{CARVAO}">pedido ✓<br>sem comissão ✓<br>cliente é seu</div>') + '</div>')
    + A(720, -40, f'<img src="{R(4109050)}" style="width:1700px;margin-left:-480px;margin-top:-880px">', 'width:620px;height:800px;overflow:hidden')
    + A(1080, 40, selo_n('03', 140)))

# 6) CAPA DE SHORT 1080x1920 · composição "Foto que dá fome" do feed
sec('capa-short-1080x1920', 1080, 1920, VERDE,
    f'<div style="position:absolute;inset:0;background:{FUNDO}"></div>'
    f'<div style="position:absolute;left:0;right:0;top:760px;bottom:0;background:url({F(32230550)}) 30% center/cover"></div>'
    f'<div style="position:absolute;left:0;right:0;top:740px;height:40px;background:{xadrez(TOMATE, CREME, 20)}"></div>'
    + A(70, 170, manchete('A PERGUNTA', 128, TOMATE))
    + A(76, 330, manchete('QUE AUMENTA', 110, CREME))
    + A(76, 460, manchete('O PEDIDO.', 150, TOMATE))
    + A(830, 520, selo_n('20', 180))
    + A(70, 1620, zap(40))
    + A(70, 1760, logo(44)))

html = ('<!doctype html><meta charset="utf-8"><style>'
        f'@font-face{{font-family:Bagel;src:url({BAGEL})}}@font-face{{font-family:Anton;src:url({ANTON})}}'
        'body{margin:0;background:transparent}section.f{position:relative;overflow:hidden;margin:0 0 40px}</style>' + ''.join(S))
open(os.path.join(D, 'pecas.html'), 'w').write(html)
print(len(S), 'peças')
