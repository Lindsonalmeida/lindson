# Criativos de tráfego v2 · Orégano Turbo · Paollo + Rocco · 15/11/2026
# v1 reprovada pelo Lindson: "eu quero mais fome, mais imagens, menos cor e fundo sem nada" + "compare com o público".
# v2: pizza protagonista (foto 60–80% da arte, sangrando), 1 a 7 fotos por peça, base escura/foto, cor da marca só em detalhe.
# Uso: python3 gerar2.py && NODE_PATH=$(npm root -g) node render.js (lê pecas-v2.html e salva em pecas-v2/ via RENDER_V2=1)
import os
from marca import *

FT = lambda i: f'fotos/{i}.jpg'
QUENTE = 'saturate(1.18) contrast(1.06) brightness(1.02) sepia(.06)'
P = []

def fundo(i, pos='center', extra=''):
    return f'<div class="a" style="inset:0;background:url({FT(i)}) {pos}/cover;filter:{QUENTE};{extra}"></div>'
def scrim(lado, alt, forca=.94):
    d = 'to bottom' if lado == 'top' else 'to top'
    return (f'<div class="a" style="left:0;right:0;{lado}:0;height:{alt}px;'
            f'background:linear-gradient({d},rgba(12,11,9,{forca}) 0%,rgba(12,11,9,{forca * .85}) 45%,rgba(12,11,9,0) 100%)"></div>')
def pol(i, w, h, rot=0, pos='center', borda=CREME, extra=''):
    return (f'<div style="width:{w}px;height:{h}px;flex:none;transform:rotate({rot}deg);border:8px solid {borda};'
            f'box-shadow:14px 16px 0 rgba(0,0,0,.45);background:url({FT(i)}) {pos}/cover;filter:{QUENTE};{extra}"></div>')
def vapor():
    return ('<div class="a" style="inset:0;pointer-events:none;background:radial-gradient(ellipse 40% 18% at 50% 40%,rgba(255,240,220,.10),transparent 70%),'
            'radial-gradient(ellipse 30% 14% at 38% 30%,rgba(255,240,220,.08),transparent 70%);mix-blend-mode:screen"></div>')
def tarja(cta='Chama no zap ↗', cta_bg=TOMATE):
    return (f'<div class="a" style="left:0;right:0;bottom:0;height:112px;background:{TINTA};display:flex;align-items:center;'
            f'justify-content:space-between;padding:0 48px;border-top:4px solid {TOMATE}">'
            + logo(34, CREME) + adesivo(cta, cta_bg, CREME, -3, 30, '12px 22px') + '</div>')
B = lambda t, s, cor=CREME, lh=.9, extra='': BAGEL(t, s, cor, lh, 'white-space:normal;text-shadow:0 4px 18px rgba(0,0,0,.6);' + extra)
TX = lambda t, s=27, extra='': TXT(t, s, CREME, 'text-shadow:0 2px 10px rgba(0,0,0,.7);' + extra)
AM = lambda t: f'<span style="color:{ACAFRAO}">{t}</span>'
TM = lambda t: f'<span style="color:{TOMATE}">{t}</span>'
CREDITO = lambda: A(52, None, MONO('fotos: Pexels', 11, CREME, 'opacity:.5'), 'bottom:122px')

# 01 · dia fraco: forno a lenha em tela cheia + sequência de 2 fotos
def c01(H):
    al = H > 1400
    return (fundo('29626981', 'center 70%') + vapor() + scrim('top', 560 if al else 470) + scrim('bottom', 520 if al else 420)
            + A(56, 52, MONO('Dono de pizzaria · São Luís', 20, ACAFRAO)) + A(800, 36, adesivo('dia fraco?', TOMATE, CREME, 6, 26))
            + A(56, 96, B('Terça à noite:<br>' + TM('forno quente,') + '<br>salão vazio?', 104 if al else 90), 'width:980px')
            + A(56, H - (520 if al else 420), '<div style="display:flex;gap:18px;align-items:flex-end">'
                + pol('3343627', 300, 220, -4) + pol('16386277', 300, 220, 3)
                + '<div style="display:flex;flex-direction:column;gap:6px;margin-left:24px">'
                + ''.join(f'<span style="font:400 30px/1 \'Bagel Fat One\';color:{TOMATE if d in ("TER", "QUA") else CREME};opacity:{1 if d in ("TER", "QUA") else .55}">{d}</span>' for d in ('SEG', 'TER', 'QUA')) + '</div></div>')
            + A(56, H - 190, TX('O fim de semana enche sozinho. O meio da semana precisa de anúncio no bairro e pedido no zap.', 26), 'width:960px')
            + tarja())

# 02 · taxa do app: close de pepperoni em tela cheia + 2 detalhes
def c02(H):
    al = H > 1400
    return (fundo('3915857', 'center 40%') + scrim('bottom', 760 if al else 600) + scrim('top', 220, .7)
            + A(56, 52, MONO('Pizzaria em São Luís · delivery', 20, CREME))
            + A(56, H - (880 if al else 570), '<div style="display:flex;gap:16px">' + pol('13730501', 230, 170, -3) + pol('16055182', 230, 170, 2) + '</div>')
            + A(56, H - (600 if al else 380), B('O app come uma<br>' + TM('fatia') + ' de cada pedido.', 92 if al else 78), 'width:980px')
            + A(56, H - (240 if al else 200), '<div style="display:flex;gap:30px;align-items:center">' + adesivo('<s>taxa do app</s>', CREME, TOMATE, -4, 34, borda=CARVAO)
                + TX('Pedido direto no <b>seu WhatsApp</b>.', 28) + '</div>')
            + A(760, 70 + (200 if al else 120), adesivo('fatia do app?', ACAFRAO, CARVAO, 8, 28)) + CREDITO() + tarja('Quero vender direto ↗', VERDE))

# 03 · feed parado: fundo de pizza escura + celular com feed de 6 fotos que dão fome
def c03(H):
    al = H > 1400
    grade = ''.join(f'<div style="aspect-ratio:1;background:url({FT(i)}) center/cover;filter:{QUENTE}"></div>' for i in
                    ('7780261', '31450871', '40135596', '842519', '30504703', '32291145'))
    ch = 980 if al else 760
    cel = (f'<div style="width:{ch * .5:.0f}px;height:{ch}px;border-radius:50px;background:{TINTA};padding:14px;box-shadow:24px 28px 0 rgba(0,0,0,.5);transform:rotate(-4deg)">'
           f'<div style="width:100%;height:100%;border-radius:38px;overflow:hidden;background:#fff;display:flex;flex-direction:column">'
           f'<div style="padding:14px 16px;font:700 18px Inter;color:#111;display:flex;gap:10px;align-items:center"><span style="width:34px;height:34px;border-radius:50%;background:{TOMATE}"></span>suapizzaria</div>'
           f'<div style="flex:1.2;background:url({FT("27927612")}) center/cover;filter:{QUENTE}"></div>'
           f'<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:3px;padding:3px 0">{grade}</div></div></div>')
    return (fundo('31094832', 'center', 'filter:brightness(.55) saturate(1.2)') + scrim('top', 400)
            + A(56, 52, MONO('Feed parado = pizzaria esquecida', 20, ACAFRAO))
            + A(56, 96, B('Sua pizza é linda.<br>' + AM('Seu feed') + ' não mostra.', 88 if al else 74), 'width:980px')
            + A(80, 420 if al else 290, cel)
            + A(640, (720 if al else 560), '<div style="display:flex;flex-direction:column;gap:22px">' + adesivo('último post: março', TOMATE, CREME, 6, 26)
                + adesivo('foto que dá fome', CREME, CARVAO, -4, 26, borda=CARVAO) + adesivo('toda semana', ACAFRAO, CARVAO, 3, 26) + '</div>')
            + A(56, H - 190, TX('A gente grava na sua pizzaria e posta por você.', 27), 'width:960px') + tarja())

# 04 · processo: forno no fundo + 5 passos, cada um com a sua foto
def c04(H):
    al = H > 1400
    passos = [('5903389', 'Raio-X', 'Instagram, Google, iFood e bairro'), ('1566837', 'Gravação', 'na sua pizzaria, forno aceso'),
              ('36707034', 'Anúncio', 'no raio de entrega, dia fraco'), ('17403900', 'Zap', 'pedido direto, resposta pronta'),
              ('20154166', 'Segunda', 'relatório simples do que veio')]
    hh = 230 if al else 168
    lis = ''.join(f'<div style="display:flex;gap:20px;align-items:center;background:rgba(15,14,12,.82);border-left:8px solid {TOMATE};padding:10px;backdrop-filter:blur(4px)">'
                  + pol(i, int(hh * 1.35), hh - 20, 0, 'center', CREME, 'box-shadow:none;border-width:4px')
                  + f'<div><span style="font:400 46px/1 \'Bagel Fat One\';color:{TOMATE}">{k + 1:02d}</span> '
                  f'<span style="font:400 40px/1 \'Bagel Fat One\';color:{CREME};text-transform:uppercase">{t}</span>'
                  f'<div style="font:600 22px/1.2 Inter;color:{CREME};opacity:.85;margin-top:6px">{d}</div></div></div>'
                  for k, (i, t, d) in enumerate(passos))
    return (fundo('11447751', 'center', 'filter:brightness(.6) saturate(1.2)') + scrim('top', 330)
            + A(56, 52, MONO('Como a Orégano Turbo trabalha', 20, ACAFRAO))
            + A(56, 96, B('Do forno ao ' + TM('pedido no zap.'), 66), 'width:980px')
            + A(56, 290 if al else 230, f'<div style="display:flex;flex-direction:column;gap:{20 if al else 12}px;width:968px">{lis}</div>')
            + tarja())

# 05 · Raio-X: cheese pull em tela cheia + comanda
def c05(H):
    al = H > 1400
    picote = f'radial-gradient(circle at 10px 0,transparent 9px,{CREME} 9.5px) -10px 0/20px 100% repeat-x'
    itens = ['Instagram e Google', 'iFood e preço', '3 concorrentes do bairro', 'dias fracos', 'plano de 30 dias']
    lis = ''.join(f'<div style="display:flex;justify-content:space-between;border-bottom:2px dashed #bbb;padding:6px 0;font:600 22px Inter;color:{CARVAO}"><span>{t}</span><span style="color:{VERDE}">✓</span></div>' for t in itens)
    com = (f'<div style="width:470px;transform:rotate(-4deg);filter:drop-shadow(16px 18px 0 rgba(0,0,0,.5))"><div style="height:14px;background:{picote}"></div>'
           f'<div style="background:{CREME};padding:20px 30px 24px">' + MONO('pedido nº01', 16, CARVAO)
           + f'<div style="font:400 92px/1 \'Bagel Fat One\';color:{TOMATE};margin:4px 0">RAIO-X</div>' + MONO('entregue em vídeo', 14, CARVAO) + lis
           + f'<div style="display:flex;justify-content:space-between;align-items:end;margin-top:12px"><span style="font:700 17px/1.2 Inter;color:{CARVAO}">abatido no 1º mês<br>se fechar em 7 dias</span>'
           f'<span style="font:400 70px/1 \'Bagel Fat One\';color:{VERDE}">R$&nbsp;297</span></div></div></div>')
    return (fundo('35017349', '30% center') + scrim('top', 420) + f'<div class="a" style="top:0;bottom:0;right:0;width:640px;background:linear-gradient(to left,rgba(12,11,9,.93) 55%,rgba(12,11,9,0))"></div>'
            + A(56, 56, B('Antes de gastar com<br>anúncio, ' + AM('raio-X.'), 80 if al else 72), 'width:980px')
            + A(560, 230 if al else H - 880, com)
            + A(56, H - 190, TX('Diagnóstico em vídeo. Você decide se continua.', 27), 'width:960px;') + tarja('Quero meu Raio-X ↗'))

# 06 · 5 vagas: "5" gigante feito de pizza + 5 fotos (uma por vaga)
def c06(H):
    al = H > 1400
    vagas = ''.join(f'<div style="flex:1;display:flex;flex-direction:column;gap:6px;transform:rotate({(-1) ** k * 2}deg)">'
                    + f'<div style="height:{240 if al else 150}px;background:url({FT(i)}) center/cover;filter:{QUENTE};border:6px solid {CREME}"></div>'
                    + f'<div style="background:{CREME};text-align:center;font:400 30px/1.2 \'Bagel Fat One\';color:{TOMATE}">VAGA {k:02d}</div></div>'
                    for k, i in enumerate(('9993754', '27819672', '17402721', '13185303', '6068713'), 1))
    return (fundo('37417637', 'center', 'filter:brightness(.35) blur(2px)')
            + A(56, 52, MONO('Condição de fundadora · Orégano Turbo', 20, ACAFRAO))
            + A(30, 70, f'<div style="font:400 {760 if al else 620}px/.82 \'Bagel Fat One\';background:url({FT("7142953")}) center/cover;'
                         f'-webkit-background-clip:text;color:transparent;-webkit-text-stroke:6px {CREME};filter:drop-shadow(14px 14px 0 rgba(0,0,0,.6))">5</div>')
            + A(500, 180 if al else 150, B('vagas de<br>pizzaria<br>' + AM('fundadora'), 82 if al else 72))
            + A(500, 470 if al else 420, TX('Preço do plano anual<br>no prazo do semestral.<br>Fechou a 5ª, acabou.', 28))
            + A(56, H - (470 if al else 330), f'<div style="display:flex;gap:14px;width:968px">{vagas}</div>')
            + tarja('Garantir minha vaga ↗', VERDE))

# 07 · comparação: forno em tela cheia + foto comparada + tabela escura
def c07(H):
    al = H > 1400
    linhas = [('Pizzaria, salão e loja de pneu', 'Só pizzaria'), ('Foto de banco genérica', 'Foto do SEU forno'),
              ('Anúncio pra cidade inteira', 'No raio de entrega'), ('Some depois que você paga', 'Relatório toda segunda')]
    tab = ''.join(f'<div style="display:grid;grid-template-columns:1fr 1fr;border-top:2px solid rgba(243,238,230,.18)">'
                  f'<div style="padding:{16 if al else 11}px 16px;font:600 22px/1.2 Inter;color:#a59f95;text-decoration:line-through">✕ {a}</div>'
                  f'<div style="padding:{16 if al else 11}px 16px;font:800 23px/1.2 Inter;color:{CREME}"><span style="color:{ACAFRAO}">✓</span> {b}</div></div>' for a, b in linhas)
    cab = (f'<div style="display:grid;grid-template-columns:1fr 1fr"><div style="padding:12px 16px;font:400 26px \'Bagel Fat One\';color:#a59f95">AGÊNCIA DE TUDO</div>'
           f'<div style="padding:12px 16px;font:400 26px \'Bagel Fat One\';color:{CREME};background:{TOMATE}">ORÉGANO TURBO</div></div>')
    return (fundo('1878346', 'center 60%') + vapor() + scrim('top', 400) + scrim('bottom', 640 if al else 560)
            + A(56, 56, B('Agência de tudo<br>não entende ' + AM('forno.'), 90 if al else 78), 'width:980px')
            + A(780, 330 if al else 270, pol('9419406', 240, 300, 5))
            + A(56, H - (560 if al else 480), f'<div style="width:968px;background:rgba(15,14,12,.85);border:3px solid {CREME};backdrop-filter:blur(4px)">{cab}{tab}</div>')
            + CREDITO() + tarja())

# 08 · objeção: fatia com refrigerante em tela cheia + conversa na faixa escura
def c08(H):
    al = H > 1400
    bal = lambda t, eu: (f'<div style="align-self:{"flex-end" if eu else "flex-start"};max-width:80%;background:{"#DCF8C6" if eu else "#fff"};'
                         f'border-radius:20px;padding:12px 18px;box-shadow:0 6px 0 rgba(0,0,0,.25);font:500 {25 if al else 22}px/1.28 Inter;color:{CARVAO}">{t}</div>')
    conv = (f'<div style="width:968px;display:flex;flex-direction:column;gap:12px">'
            + bal('Já impulsionei post e não veio pedido.', False)
            + bal('Impulsionar é apertar um botão. Pizzaria precisa de foto que dá fome, raio de entrega certo e pedido caindo no zap.', True)
            + bal('A gente não promete número: mostra toda segunda o que entrou.', True) + '</div>')
    return (fundo('31094831', 'center 12%') + scrim('top', 360) + scrim('bottom', 760 if al else 640)
            + A(56, 56, B('"Já tentei e não<br>deu ' + TM('nada.') + '"', 92 if al else 80), 'width:980px')
            + A(56, H - (620 if al else 530), conv)
            + A(56, H - 150, MONO('conversa de exemplo · não é promessa de resultado', 14, CREME, 'opacity:.7'))
            + tarja('Tirar minha dúvida ↗', VERDE))

# 09 · só pizza: palavra gigante com foto dentro sobre pizza escura
def c09(H):
    al = H > 1400
    return (fundo('37417637', 'center', 'filter:brightness(.42) saturate(1.2)') + scrim('top', 300, .7) + scrim('bottom', 500)
            + A(56, 52, MONO('Marketing de vendas · só pizzarias · São Luís', 20, ACAFRAO))
            + A(40, 140 if al else 110, f'<div style="font:400 {380 if al else 320}px/.8 \'Bagel Fat One\';letter-spacing:-.03em;background:url({FT("27359003")}) center 45%/cover;'
                 f'-webkit-background-clip:text;color:transparent;-webkit-text-stroke:5px {CREME};filter:drop-shadow(0 10px 30px rgba(0,0,0,.6))">SÓ<br>PIZZA</div>')
            + A(56, H - (470 if al else 400), B('A gente não faz açaí,<br>sushi nem ' + TM('hamburgueria.'), 66 if al else 58))
            + A(56, H - (260 if al else 210), '<div style="display:flex;gap:18px">' + ''.join(adesivo(f'<s>{t}</s>', CREME, CARVAO, r, 24, '10px 18px', borda=CARVAO) for t, r in (('açaí', -5), ('sushi', 4), ('hambúrguer', -3)))
                + adesivo('pizzaria ✓', TOMATE, CREME, 4, 28, '10px 20px') + '</div>')
            + A(760, 70, estrela(200, ACAFRAO, f'<div style="font:400 30px/1 \'Bagel Fat One\';color:{CARVAO}">100%<br>pizzaria</div>', 10))
            + tarja('Falar com especialista ↗', VERDE))

# 10 · chamada direta: cheese pull na mão em tela cheia + 2 polaroids
def c10(H):
    al = H > 1400
    return (fundo('31587842', 'center 40%') + scrim('top', 420) + scrim('bottom', 620 if al else 520)
            + A(56, 52, B('Dono de pizzaria<br>em ' + AM('São Luís:'), 90 if al else 78))
            + A(56, H - (560 if al else 470), '<div style="display:flex;gap:18px;align-items:flex-end">' + pol('18126737', 250, 190, -5) + pol('7241485', 250, 190, 4)
                + '<div style="display:flex;flex-direction:column;gap:16px;margin-left:10px">' + adesivo('foto que dá fome', TOMATE, CREME, -4, 24, '10px 18px')
                + adesivo('anúncio no bairro', CREME, CARVAO, 3, 24, '10px 18px', borda=CARVAO) + adesivo('pedido no zap', ACAFRAO, CARVAO, -2, 24, '10px 18px') + '</div></div>')
            + A(56, H - 250, B('isso é pra você.', 60 if al else 52))
            + A(56, H - 160, TX('Manda <b>"PIZZA"</b> no WhatsApp e marcamos o seu Raio-X.', 25))
            + tarja('Mandar "PIZZA" ↗'))

for n, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1):
    for nome, H in (('feed', 1350), ('story', 1920)):
        P.append((f'c{n:02d}-{nome}', 1080, H, f'<div class="a" style="inset:0;background:{TINTA}">' + f(H) + '</div>' + GRAO))

open(os.path.join(D, 'pecas-v2.html'), 'w').write(
    f'<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>' +
    ''.join(f'<section class="f" id="{i}" style="width:{w}px;height:{h}px">{c}</section>' for i, w, h, c in P) + '</body></html>')
print(len(P), 'peças v2')
