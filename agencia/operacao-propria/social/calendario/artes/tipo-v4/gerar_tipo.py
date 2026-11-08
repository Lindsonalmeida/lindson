# Artes TIPOGRÁFICAS novas do calendário @oreganoturbo, no sistema v4 · Paollo · conta Zuleide · 08/11/2026
# Pautas que pediam foto do lote 2 (F8, F13, F23, F30) e que viram tipografia SEM perder força, porque o assunto
# delas é a própria comanda / o método / o preço (não a comida):
#   d12 12h CÓDIGO EM CADA PEDIDO.        (era F8)  → comanda gigante com o código PZ14 (exemplo ilustrativo)
#   d15 19h COMO FUNCIONA EM 4 PASSOS     (era F13) → carrossel de 3 telas: 4 comandas, uma por passo
#   d20 19h PROMOÇÃO TODO DIA CANSA.      (era F23) → parede de etiquetas de desconto rasgadas
#   d27 19h PRIMEIRO PASSO: RAIO-X.       (era F30) → "1º" gigante + comanda do Raio-X com o preço escrito
# A F30 pedia "pizza com estrela de preço": é o padrão a evitar da pesquisa de 08/11 (vermelho + pizza + selo de preço).
# Sem foto: nada a registrar em ../../../FOTOS-USADAS.md.
# Uso: python3 gerar_tipo.py && node render.js && python3 previa.py
import os, json
D = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(D, '..', 'sistema_v4.py'), encoding='utf-8').read())   # sistema v4: lê ../../../v4/gerar.py

P, COMP = [], {}
POS = {'d12-12h-codigo-em-cada-pedido': (835, 50, 5), 'd20-19h-promocao-todo-dia-cansa': (690, 590, 5)}
def salvar(nome, larg, alt, html, comp):
    P.append((nome, larg, alt, html + COMANDA(nome, POS.get(nome)) + GRAO)); COMP[nome] = comp
feed = lambda n, h, c: salvar(n, 1080, 1350, h, c)
pad = lambda cor, op=.12, t=300: f'<div class="a" style="inset:0;background:{padrao(cor, op, t)}"></div>'
GIRA = lambda deg, inner: f'<div style="transform:rotate({deg}deg)">{inner}</div>'
def icone(n, tam, cor, w=6):
    return (f'<svg viewBox="0 0 100 100" width="{tam}" height="{tam}" style="display:block"><g fill="none" stroke="{cor}" stroke-width="{w}" '
            f'stroke-linecap="round" stroke-linejoin="round">{IC[n]}</g></svg>')
IC.update({
 'relogio': '<circle cx="50" cy="50" r="38"/><path d="M50 26 L50 50 L66 60"/>',
 'camera': '<rect x="10" y="28" width="80" height="56" rx="10"/><circle cx="50" cy="56" r="16"/><path d="M34 28 L40 16 L60 16 L66 28"/>',
 'alvo': '<circle cx="50" cy="50" r="38"/><circle cx="50" cy="50" r="22"/><circle cx="50" cy="50" r="6"/>',
 'zap': '<path d="M50 12 A38 38 0 1 1 26 80 L12 88 L18 72 A38 38 0 0 1 50 12 Z"/><path d="M38 34 C 36 46 48 60 62 64 L68 56 L60 50 L55 54 C 50 52 46 48 44 43 L48 38 L42 30 Z"/>',
 'grafico': '<path d="M14 86 L86 86"/><path d="M24 86 L24 60 M44 86 L44 44 M64 86 L64 52 M84 86 L84 22"/>',
})
ILU = lambda cor=CARVAO, bg=ACAFRAO, s=15: MONO('Exemplo ilustrativo', s, cor, f'background:{bg};padding:8px 12px;box-shadow:5px 5px 0 {CARVAO}')

def rodape(y, bg=CARVAO, fg=CREME, chamada='Chama no zap ↗', cbg=TOMATE, cfg=CREME, h=110, direita='@oreganoturbo · só pizzarias'):
    return BOX(0, y, 1080, h, bg, f'display:flex;align-items:center;justify-content:space-between;padding:0 52px;border-top:6px solid {CARVAO}',
               f'<div>{logo(36, fg)}<div style="margin-top:8px">{MONO(direita, 15, fg, "opacity:.85")}</div></div>'
               + f'<div style="background:{cbg};padding:16px 26px;border-radius:999px;box-shadow:0 0 0 5px {fg}">{BAGEL(chamada, 34, cfg, 1)}</div>')

def papel(inner, w, rot=0, bg=CREME, pad_='26px 34px 28px', sombra='14px 16px 0 rgba(20,19,17,.4)'):
    """Papel de comanda com picote em cima e embaixo."""
    pic = lambda pos: f'radial-gradient(circle at 9px {pos},transparent 8px,{bg} 8.5px) -9px 0/18px 100% repeat-x'
    return (f'<div style="width:{w}px;transform:rotate({rot}deg);filter:drop-shadow({sombra})">'
            f'<div style="height:12px;background:{pic("0")}"></div><div style="background:{bg};padding:{pad_}">{inner}</div>'
            f'<div style="height:12px;background:{pic("12px")}"></div></div>')

# ================================================================== d12 12h · CÓDIGO EM CADA PEDIDO. (creme · comanda gigante PZ14)
# Copia: a comanda da campanha v4 levada ao tamanho do post (Impasto: um conceito só) + "palavra gigante" (o código PZ14 ocupa a peça,
# como o "PIZZA" atrás da pizza no Pinterest nº1) + passo a passo em adesivos girados (Pizzino).
linha_cmd = lambda a, b: (f'<div style="display:flex;justify-content:space-between;align-items:baseline;gap:18px;padding:12px 0;border-bottom:2px dashed rgba(20,19,17,.25)">'
                          f'{MONO(a, 15, TOMATE)}<span style="font:700 30px/1.1 Inter;color:{CARVAO};text-align:right">{b}</span></div>')
cmd12 = papel(MONO('Orégano Turbo · pedido via zap · 20/11 · 19h42', 15, CARVAO)
              + f'<div style="display:flex;align-items:flex-end;gap:18px;margin:6px 0 4px">{MONO("código", 18, TOMATE, "margin-bottom:34px")}'
              + BAGEL('PZ14', 250, TOMATE, .9, SH(CARVAO, 8)) + '</div>'
              + linha_cmd('Veio do vídeo', 'Calabresa saindo do forno') + linha_cmd('Anúncio', 'Bairro Cohama · 3 km')
              + linha_cmd('Pedido', '1 grande + borda'), 820, -3)
feed('d12-12h-codigo-em-cada-pedido',
     BOX(0, 0, 1080, 1350, CREME) + pad(VERDE, .10) +
     BOX(0, 0, 1080, 28, xadrez(VERDE, CREME, 14)) +
     A(40, 60, BAGEL('Código em', 150, VERDE, .88, SH(CARVAO, 7))) +
     A(40, 200, BAGEL('cada pedido.', 116, TOMATE, .9, SH(CARVAO, 7))) +
     A(60, 400, cmd12) +
     A(40, 1000, f'<div style="display:flex;gap:16px;align-items:center">'
                 + adesivo('1 · vídeo', VERDE, CREME, -5, 34) + adesivo('2 · código', TOMATE, CREME, 4, 34) + adesivo('3 · relatório', CARVAO, CREME, -3, 34) + '</div>') +
     A(44, 1120, TXT('Assim a gente sabe qual vídeo vendeu. E você vê na segunda.', 28, CARVAO, 'width:640px;line-height:1.25')) +
     A(770, 1130, ILU()) +
     rodape(1240),
     'Comanda gigante com o código PZ14 ocupando a peça (conceito "PEDIDO Nº" do v4 em tamanho de cartaz) + linhas da comanda (vídeo, anúncio, pedido) '
     '+ 3 adesivos girados com o caminho vídeo → código → relatório; creme com padrão verde. Exemplo ilustrativo.')

# ================================================================== d15 19h · COMO FUNCIONA EM 4 PASSOS (carrossel, 3 telas)
# Copia: capa com número gigante (palavra gigante atrás, "10 ideias" do s3-4 e Pinterest nº3) + cada passo numa comanda (conceito v4)
# + leque de papéis girados (Pizzino). Telas internas com composição diferente da capa e entre si.
PASSOS = [('Gravação', 'camera', 'Uma manhã na sua pizzaria: foto e vídeo de dar fome.'),
          ('Anúncio no bairro', 'alvo', 'O vídeo roda pra quem mora perto e pede delivery.'),
          ('Código no pedido', 'zap', 'Cada anúncio tem um código. O pedido chega no seu zap com ele.'),
          ('Relatório de segunda', 'grafico', 'Toda segunda, 8h: quanto investiu, quantos pedidos, o que muda.')]
def passo(i, w=880, rot=0, cor=TOMATE):
    t, ic, d = PASSOS[i]
    return papel(f'<div style="display:flex;gap:26px;align-items:center">'
                 f'<div style="flex:none;width:190px;height:190px;border-radius:30px;background:{cor};display:grid;place-items:center;border:6px solid {CARVAO}">'
                 f'{BAGEL(str(i + 1), 160, CREME, 1, SH(CARVAO, 6))}</div>'
                 f'<div style="flex:1">{MONO(f"Passo {i + 1} de 4", 18, TOMATE)}{BAGEL(t, 66, CARVAO, .95, "white-space:normal;margin-top:6px")}'
                 f'{TXT(d, 31, CARVAO, "margin-top:12px;line-height:1.28;font-weight:600")}</div>'
                 f'<div style="flex:none">{icone(ic, 110, VERDE, 7)}</div></div>', w, rot, pad_='38px 40px 40px')
mini = lambda i, rot: papel(MONO(f'passo {i + 1}', 14, TOMATE) + BAGEL(PASSOS[i][0], 34, CARVAO, .95, 'white-space:normal;margin-top:4px'), 260, rot, pad_='16px 20px 18px')
feed('d15-19h-como-funciona-4-passos-1-capa',
     BOX(0, 0, 1080, 1350, VERDE) + pad(CREME, .10) +
     A(40, 40, MONO('Método Orégano · carrossel', 20, CREME, f'background:{TOMATE};padding:9px 13px;box-shadow:6px 6px 0 {CARVAO}')) +
     A(40, 100, BAGEL('Como', 170, CREME, .86, SH(CARVAO, 9))) +
     A(40, 260, BAGEL('funciona', 170, ACAFRAO, .86, SH(CARVAO, 9))) +
     A(560, 360, BAGEL('4', 760, TOMATE, .9, SH(CARVAO, 16))) +
     A(60, 470, BAGEL('passos.', 110, CREME, .9, SH(CARVAO, 7))) +
     A(40, 640, mini(0, -8)) + A(300, 690, mini(1, 5)) + A(70, 880, mini(2, 4)) + A(330, 930, mini(3, -6)) +
     A(690, 1120, adesivo('Arrasta →', CARVAO, CREME, -4, 36)) +
     rodape(1240, CARVAO, CREME, 'Salva ✓', CREME, VERDE, direita='1/3 · @oreganoturbo'),
     'Capa: "4" gigante em tomate atrás das comandas + manchete em 2 cores + 4 mini comandas em leque (um passo em cada) + adesivo "arrasta"; verde')
feed('d15-19h-como-funciona-4-passos-2',
     BOX(0, 0, 1080, 1350, CREME) + pad(TOMATE, .10) +
     A(40, 40, BAGEL('Passos 1 e 2', 120, VERDE, .9, SH(CARVAO, 6))) +
     A(50, 200, passo(0, 980, -2, TOMATE)) +
     A(60, 620, passo(1, 980, 2, VERDE)) +
     A(40, 1090, adesivo('Você não precisa aparecer em vídeo', CARVAO, CREME, -3, 32)) +
     rodape(1240, VERDE, CREME, 'Continua →', CREME, VERDE, direita='2/3 · @oreganoturbo'),
     'Tela 2: 2 comandas grandes empilhadas e giradas (passo 1 gravação, passo 2 anúncio) com número gordo em quadro de cor + ícone em traço; creme com padrão tomate')
feed('d15-19h-como-funciona-4-passos-3',
     BOX(0, 0, 1080, 1350, TOMATE) + pad(CREME, .10) +
     A(40, 40, BAGEL('Passos 3 e 4', 120, CREME, .9, SH(CARVAO, 6))) +
     A(50, 190, passo(2, 980, 2, VERDE)) +
     A(50, 560, passo(3, 980, -2, CARVAO)) +
     A(40, 990, f'<div style="background:{CARVAO};border:6px solid {CREME};box-shadow:12px 12px 0 rgba(20,19,17,.35);padding:22px 28px;transform:rotate(-2deg);width:640px">'
                + MONO('e antes de tudo', 16, ACAFRAO) + BAGEL('Começa pelo Raio-X.', 50, CREME, .95, 'margin-top:6px') + '</div>') +
     A(720, 1030, ZAP(VERDE, CREME, 5, 36)) +
     rodape(1240, CARVAO, CREME, 'Chama no zap ↗', CREME, TOMATE, direita='3/3 · @oreganoturbo'),
     'Tela 3: 2 comandas grandes (passo 3 código, passo 4 relatório) + bloco carvão "Começa pelo Raio-X" + adesivo do zap; tomate (cor invertida em relação à tela 2)')

# ================================================================== d20 19h · PROMOÇÃO TODO DIA CANSA. (creme · etiquetas rasgadas)
# Copia: parede de palavra repetida ("HOT SAUCE" das favoritas, usada no d23 com texto) feita de ETIQUETAS de desconto rasgadas
# + manchete em 2 tamanhos ("AQUI / não tem / ERRO") + cartão "em vez disso". Sem preço de cliente: os % são de exemplo.
def etiqueta(t, rot, bg=TOMATE, fg=CREME, w=230, rasgada=False):
    corte = 'clip-path:polygon(0 0,100% 0,100% 62%,88% 70%,76% 60%,62% 74%,48% 63%,34% 76%,20% 64%,8% 72%,0 66%);' if rasgada else ''
    return (f'<div style="position:relative;width:{w}px;height:{w * .52:.0f}px;transform:rotate({rot}deg);filter:drop-shadow(8px 10px 0 rgba(20,19,17,.30))">'
            f'<div style="position:absolute;inset:0;background:{bg};border-radius:14px 40px 40px 14px;{corte}"></div>'
            f'<div style="position:absolute;right:22px;top:50%;width:22px;height:22px;margin-top:-11px;border-radius:50%;background:{CREME};border:4px solid {CARVAO}"></div>'
            f'<div style="position:absolute;left:20px;top:0;bottom:0;display:flex;align-items:center">{BAGEL(t, w * .26, fg, 1)}</div></div>')
tags = ''.join(A(x, y, etiqueta(t, r, bg, fg, 230, rg)) for x, y, t, r, bg, fg, rg in [
    (40, 420, '-10%', -8, TOMATE, CREME, False), (300, 400, '-20%', 6, VERDE, CREME, True), (560, 430, '-30%', -4, CARVAO, ACAFRAO, False),
    (800, 410, '-40%', 9, TOMATE, CREME, True), (90, 600, '-50%', 5, CARVAO, CREME, True), (360, 590, '-60%', -7, TOMATE, CREME, False)])
feed('d20-19h-promocao-todo-dia-cansa',
     BOX(0, 0, 1080, 1350, CREME) + pad(TOMATE, .10) +
     A(30, 40, FIT(BAGEL('Promoção', 190, TOMATE, .86, SH(CARVAO, 9)), 1020)) +
     A(44, 236, BAGEL('todo dia', 110, VERDE, .9)) +
     A(560, 248, BAGEL('cansa.', 140, CARVAO, .9, SH(TOMATE, 6))) +
     tags +
     A(40, 800, f'<div style="background:{VERDE};border:6px solid {CARVAO};box-shadow:12px 12px 0 {CARVAO};padding:26px 32px;transform:rotate(-2deg);width:620px">'
                + MONO('O cliente aprende', 18, ACAFRAO) + BAGEL('a esperar<br>o desconto.', 72, CREME, .95, 'margin-top:8px') + '</div>') +
     faixa('valor no combo, não no desconto', 1080, TOMATE, CREME, -3, 96, 54) +
     A(690, 770, papel(MONO('em vez disso', 15, TOMATE)
                       + ''.join(f'<div style="display:flex;gap:10px;align-items:center;padding:9px 0;border-bottom:2px dashed rgba(20,19,17,.25)">'
                                 f'<span style="font:800 24px Inter;color:{VERDE}">✓</span><span style="font:700 25px/1.15 Inter;color:{CARVAO}">{t}</span></div>'
                                 for t in ['Combo com valor', 'Borda de presente', 'Cliente que volta']), 340, 4, pad_='18px 22px 20px')) +
     A(44, 1196, MONO('Porcentagens de exemplo', 14, CARVAO, 'opacity:.7')) +
     rodape(1240, CARVAO, CREME, 'Monta comigo ↗', TOMATE, CREME),
     'Parede de 7 etiquetas de desconto (−10% a −70%), algumas rasgadas, giradas em sentidos alternados + manchete em 3 tamanhos + bloco verde '
     '"o cliente aprende a esperar o desconto" + comanda "em vez disso"; creme com padrão tomate')

# ================================================================== d27 19h · PRIMEIRO PASSO: RAIO-X. (verde · "1º" gigante + comanda com o preço)
# Copia: p05 do kit v4 (preço escrito na comanda, sem explosão) + número gigante atrás (Pinterest nº3: texto enorme cortado na borda).
feed('d27-19h-primeiro-passo-raio-x',
     BOX(0, 0, 1080, 1350, VERDE) + pad(CREME, .10) +
     A(560, -60, BAGEL('1º', 860, VERDE_ESC, .9, f'text-shadow:14px 14px 0 {CARVAO}')) +
     A(40, 50, MONO('Pizzarias de São Luís - MA · vagas de fundadora', 18, ACAFRAO)) +
     A(36, 90, BAGEL('Primeiro', 170, CREME, .86, SH(CARVAO, 9))) +
     A(40, 250, BAGEL('passo:', 130, ACAFRAO, .9, SH(CARVAO, 7))) +
     A(40, 390, BAGEL('Raio-X.', 200, CREME, .86, SH(TOMATE, 10))) +
     A(60, 640, TICKET('Comanda nº1 do seu delivery', ['Instagram e Google', 'iFood e cardápio', 'WhatsApp', '3 concorrentes do bairro'], 640, -2, 32, ps=86, ms=15)) +
     A(740, 760, GIRA(8, selo(240, 'PRIMEIRO PASSO · RAIO-X · SÓ PIZZARIAS · ', TOMATE, CREME))) +
     A(720, 1070, adesivo('5 vagas de<br>fundadora', TOMATE, CREME, -6, 34, '16px 24px', extra='border-radius:26px;line-height:1.02;text-align:center')) +
     rodape(1240, CARVAO, CREME, 'Pede no zap ↗', TOMATE, CREME),
     '"1º" gigante em verde-escuro saindo pela borda + manchete em 3 linhas + comanda do Raio-X com o preço escrito (sem estrela de preço, regra v4) + selo e adesivo; verde')

open(os.path.join(D, 'pecas.html'), 'w', encoding='utf-8').write(
    f'<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>{CSS}</style>{FIT_JS}</head><body>' +
    ''.join(f'<section class="f" id="{i}" style="width:{w}px;height:{h}px">{c}</section>' for i, w, h, c in P) + '</body></html>')
json.dump(COMP, open(os.path.join(D, 'composicoes.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(P), 'peças')
