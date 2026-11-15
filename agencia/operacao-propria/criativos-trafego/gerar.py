# 10 criativos de tráfego (Meta Ads) da Orégano Turbo · Paollo (pizzaria) + Rocco (campanha) + Sobral/Hormozi (ângulo e oferta)
# Pedido do Lindson (15/11/2026): "crie 10 criativos de alta conversão para o Orégano Turbo. use nossos agentes".
# Base visual: kit social v5 (marca.py = mesmas peças do v5/gerar.py). Uso: python3 gerar.py && node render.js && python3 folha.py
import os, json
from marca import *

FT = lambda i: f'fotos/{i}.jpg'
P = []

def foto_box(i, w, h, pos='center', extra='', borda=CREME, rot=0):
    """Foto em moldura (nunca recorte): a borda é a moldura, sem borda de recorte solta."""
    return (f'<div style="width:{w};height:{h};flex:{ "1 1 auto" if h=="auto" else "none"};min-height:0;transform:rotate({rot}deg);'
            f'border:10px solid {borda};box-shadow:16px 18px 0 rgba(20,19,17,.32);background:url({FT(i)}) {pos}/cover;{extra}"></div>')

def tarja(bg=CARVAO, fg=CREME, cta='Chama no zap ↗', cta_bg=TOMATE):
    return (f'<div style="position:relative;flex:none;display:flex;align-items:center;justify-content:space-between;padding:0 48px;height:112px;background:{bg}">'
            + logo(34, fg) + adesivo(cta, cta_bg, CREME, -3, 30, '12px 22px', borda=fg) + '</div>')

def corpo(bg, inner, H, deco='', pad='56px 56px 40px', gap=28):
    return (f'<div style="position:absolute;inset:0;background:{bg};display:flex;flex-direction:column">{deco}'
            f'<div style="position:relative;flex:1 1 auto;min-height:0;display:flex;flex-direction:column;gap:{gap}px;padding:{pad}">{inner}</div>')

def xad(h, a=TOMATE, b=CREME, t=30):
    return f'<div style="flex:none;height:{h}px;background:{xadrez(a, b, t)};border-bottom:5px solid {CARVAO}"></div>'

B = lambda t, s, cor, lh=.9, extra='': BAGEL(t, s, cor, lh, 'white-space:normal;' + extra)

# ---------------------------------------------------------------- 01 · dor do dia fraco (carvão · foto no topo + semana)
def c01(H):
    alto = H > 1400
    dias = ''.join(f'<div style="flex:1;text-align:center;padding:14px 0;background:{TOMATE if d in "TER QUA" else "#2a2825"};'
                   f'border:3px solid {CREME if d in "TER QUA" else "#3a3733"};font:400 34px/1 \'Bagel Fat One\';color:{CREME}">{d}</div>'
                   for d in ['SEG', 'TER', 'QUA', 'QUI', 'SEX', 'SÁB', 'DOM'])
    inner = (MONO('Dono de pizzaria · São Luís', 20, ACAFRAO)
             + B('Terça à noite:<br><span style="color:' + TOMATE + '">forno quente,</span><br>salão vazio?', 104 if alto else 92, CREME)
             + foto_box('29626981', '100%', 'auto', 'center 60%')
             + f'<div style="display:flex;gap:8px;flex:none">{dias}</div>'
             + TXT('O fim de semana enche sozinho. O meio da semana precisa de anúncio no bairro, oferta certa e pedido direto no zap.', 30 if alto else 27, CREME, 'opacity:.92')
             + A(800, 22, adesivo('dia fraco?', ACAFRAO, CARVAO, 6, 26)))
    return corpo(CARVAO, inner, H) + tarja(TINTA) + '</div>'

# ---------------------------------------------------------------- 02 · taxa do app (tomate · foto dividida na diagonal)
def c02(H):
    alto = H > 1400
    hf = 1020 if alto else 700
    inner = (f'<div style="position:relative;flex:none;height:{hf}px;margin:-56px -56px 0;clip-path:polygon(0 0,100% 0,100% 82%,0 100%);'
             f'background:url({FT("3915857")}) center/cover"></div>'
             + B('O app come uma<br>fatia de cada pedido.', 100 if alto else 88, CREME, .92, SH(TINTA, 6))
             + TXT('Ensinamos seu cliente a pedir <b>direto no seu WhatsApp</b>: cardápio no link da bio, anúncio no bairro e atendimento rápido. O app continua, mas deixa de ser o único caminho.', 30 if alto else 27, CREME)
             + '<div style="display:flex;gap:40px;padding:10px 0 0 10px;flex:none">' + adesivo('<s>taxa do app</s>', CREME, TOMATE, -5, 40, '16px 28px', borda=CARVAO) + adesivo('pedido direto ✓', VERDE, CREME, 4, 34) + '</div>')
    return corpo(TOMATE, inner, H) + tarja(CARVAO, CREME, 'Quero vender direto ↗', VERDE) + '</div>'

# ---------------------------------------------------------------- 03 · feed parado (verde · celular)
def c03(H):
    alto = H > 1400
    cel_h = 900 if alto else 640
    tela = (f'<div style="width:{cel_h * .5:.0f}px;height:{cel_h}px;border-radius:52px;background:{TINTA};padding:16px;box-shadow:22px 26px 0 rgba(0,0,0,.35);transform:rotate(-5deg);flex:none">'
            f'<div style="width:100%;height:100%;border-radius:38px;overflow:hidden;background:#fff;display:flex;flex-direction:column">'
            f'<div style="padding:14px 16px;font:700 18px Inter;color:#111;display:flex;gap:10px;align-items:center"><span style="width:34px;height:34px;border-radius:50%;background:{TOMATE}"></span>suapizzaria</div>'
            f'<div style="flex:1;background:url({FT("27927612")}) center/cover"></div>'
            f'<div style="padding:12px 16px;font:600 16px Inter;color:#111">♥ ◯ ➤<br><span style="font-weight:500;color:#555">Ver cardápio · Pedir no WhatsApp</span></div></div></div>')
    lado = ('<div style="display:flex;flex-direction:column;gap:22px;justify-content:center">'
            + adesivo('último post: março', TOMATE, CREME, 6, 28)
            + MONO('foto que dá fome', 20, ACAFRAO) + MONO('vídeo do forno', 20, ACAFRAO) + MONO('post que vende', 20, ACAFRAO) + MONO('toda semana', 20, ACAFRAO) + '</div>')
    inner = (MONO('Feed parado = pizzaria esquecida', 20, ACAFRAO)
             + B('Sua pizza é linda.<br><span style="color:' + ACAFRAO + '">Seu feed</span> não mostra.', 96 if alto else 84, CREME)
             + f'<div style="flex:1 1 auto;min-height:0;display:flex;gap:44px;align-items:center;justify-content:center">{tela}{lado}</div>'
             + TXT('A gente grava na sua pizzaria e posta por você. O forno é com você. O feed é com a gente.', 30 if alto else 27, CREME, 'opacity:.92'))
    deco = f'<div class="a" style="inset:0;background:{padrao(CREME, .08)}"></div>'
    return corpo(VERDE, inner, H, deco) + tarja(VERDE_ESC) + '</div>'

# ---------------------------------------------------------------- 04 · prova de processo (creme · passos numerados)
def c04(H):
    alto = H > 1400
    passos = [('Raio-X', 'olhamos seu Instagram, Google, iFood e o bairro'), ('Gravação', 'foto e vídeo na sua pizzaria, com o forno aceso'),
              ('Anúncio', 'no raio de entrega, nos dias fracos'), ('Zap', 'pedido direto, com resposta pronta'), ('Segunda', 'relatório simples do que veio')]
    lista = ''.join(f'<div style="display:flex;gap:20px;align-items:center;background:#fff;border:4px solid {CARVAO};padding:{16 if alto else 10}px 20px;box-shadow:8px 8px 0 {CARVAO}">'
                    f'<span style="font:400 54px/1 \'Bagel Fat One\';color:{TOMATE};width:70px">{i + 1:02d}</span>'
                    f'<span><b style="font:400 34px/1 \'Bagel Fat One\';color:{VERDE};text-transform:uppercase">{t}</b><br>'
                    f'<span style="font:600 22px/1.2 Inter;color:{CARVAO}">{d}</span></span></div>' for i, (t, d) in enumerate(passos))
    inner = (MONO('Como a Orégano Turbo trabalha', 20, TOMATE)
             + B('Do forno<br>ao <span style="color:' + TOMATE + '">pedido no zap.</span>', 100 if alto else 86, CARVAO)
             + f'<div style="flex:1 1 auto;min-height:0;display:flex;gap:30px">'
             + f'<div style="flex:1.15;display:flex;flex-direction:column;gap:{18 if alto else 12}px;justify-content:center">{lista}</div>'
             + f'<div style="flex:.85;display:flex">{foto_box("11447751", "100%", "100%", "center", "", CARVAO, 2)}</div></div>'
             + TXT('5 passos, todo mês, só com pizzaria.', 30, CARVAO))
    return xad(44) + corpo(CREME, inner, H, pad='96px 56px 40px').replace('position:absolute;inset:0', 'position:absolute;inset:44px 0 0 0') + tarja() + '</div>'

# ---------------------------------------------------------------- 05 · oferta Raio-X (carvão · comanda gigante sobre foto escura)
def c05(H):
    alto = H > 1400
    picote = f'radial-gradient(circle at 10px 0,transparent 9px,{CREME} 9.5px) -10px 0/20px 100% repeat-x'
    itens = ['Instagram e Google', 'iFood e preço', 'as 3 concorrentes do bairro', 'dias fracos e oferta', 'plano de 30 dias']
    lis = ''.join(f'<div style="display:flex;justify-content:space-between;border-bottom:2px dashed #bbb;padding:{10 if alto else 7}px 0;font:600 26px Inter;color:{CARVAO}"><span>{t}</span><span style="color:{VERDE}">✓</span></div>' for t in itens)
    com = (f'<div style="width:580px;transform:rotate(-3deg);filter:drop-shadow(18px 20px 0 rgba(0,0,0,.45))"><div style="height:14px;background:{picote}"></div>'
           f'<div style="background:{CREME};padding:26px 40px 30px">' + MONO('Orégano Turbo · pedido nº01', 18, CARVAO)
           + f'<div style="font:400 120px/1 \'Bagel Fat One\';color:{TOMATE};margin:8px 0">RAIO-X</div>' + MONO('da sua pizzaria · entregue em vídeo', 16, CARVAO) + lis
           + f'<div style="display:flex;justify-content:space-between;align-items:end;margin-top:16px"><span style="font:700 22px/1.2 Inter;color:{CARVAO}">abatido no 1º mês<br>se fechar em 7 dias</span>'
           f'<span style="font:400 88px/1 \'Bagel Fat One\';color:{VERDE}">R$&nbsp;297</span></div></div></div>')
    inner = (B('Antes de gastar<br>com anúncio, <span style="color:' + ACAFRAO + '">raio-X.</span>', 80, CREME)
             + f'<div style="flex:1 1 auto;min-height:0;display:flex;align-items:center;justify-content:flex-end">{com}</div>'
             + TXT('Você recebe o diagnóstico em vídeo e decide se continua com a gente.', 28, CREME, 'opacity:.92'))
    deco = (f'<div class="a" style="left:-60px;top:{300 if alto else 260}px;width:440px;height:{900 if alto else 700}px;background:url({FT("35017349")}) center/cover;'
            f'border:10px solid {CREME};transform:rotate(4deg);box-shadow:16px 18px 0 rgba(0,0,0,.4)"></div>')
    return corpo(CARVAO, inner, H, deco) + tarja(TINTA, CREME, 'Quero meu Raio-X ↗') + '</div>'

# ---------------------------------------------------------------- 06 · 5 vagas de fundadora (tomate · número gigante)
def c06(H):
    alto = H > 1400
    vagas = ''.join(f'<div style="flex:1;background:{CREME};border:4px solid {CARVAO};text-align:center;padding:10px 0;transform:rotate({(-1) ** k * 3}deg)">'
                    + MONO('vaga', 14, CARVAO) + f'<div style="font:400 46px/1 \'Bagel Fat One\';color:{TOMATE}">{k:02d}</div></div>' for k in range(1, 6))
    inner = (MONO('Condição de fundadora · Orégano Turbo', 22, CREME) + B('Só para as<br>primeiras.', 110 if alto else 0, ACAFRAO, .9, '' if alto else 'display:none')
             + f'<div style="flex:1 1 auto;min-height:0;display:flex;gap:24px;align-items:center">'
             f'<div style="font:400 {640 if alto else 520}px/.8 \'Bagel Fat One\';color:{CREME};text-shadow:14px 14px 0 {TINTA};flex:none">5</div>'
             f'<div style="display:flex;flex-direction:column;gap:20px">' + B('vagas de<br>pizzaria<br>fundadora', 78, CREME)
             + foto_box('7142953', '420px', '300px' if not alto else '420px', 'center', '', CREME, -4) + '</div></div>'
             + f'<div style="display:flex;gap:12px;flex:none">{vagas}</div>'
             + TXT('As 5 primeiras pizzarias pagam o preço do plano anual no prazo do semestral. Em troca: depoimento, se você quiser. Quando fechar a 5ª, acabou.', 29 if alto else 26, CREME))
    return corpo(TOMATE, inner, H) + tarja(CARVAO, CREME, 'Garantir minha vaga ↗', VERDE) + '</div>'

# ---------------------------------------------------------------- 07 · comparação (verde · tabela X vs ✓)
def c07(H):
    alto = H > 1400
    linhas = [('Atende pizzaria, salão de beleza e loja de pneu', 'Só pizzaria'), ('Post genérico de banco de imagem', 'Foto e vídeo do SEU forno'),
              ('Anúncio para a cidade inteira', 'Anúncio no raio de entrega'), ('Some depois que você paga', 'Relatório toda segunda')]
    tab = ''.join(f'<div style="display:grid;grid-template-columns:1fr 1fr;border-bottom:3px solid {CARVAO}">'
                  f'<div style="padding:{20 if alto else 13}px 18px;font:600 23px/1.2 Inter;color:#6b665e;text-decoration:line-through">✕ {a}</div>'
                  f'<div style="padding:{20 if alto else 13}px 18px;font:800 24px/1.2 Inter;color:{VERDE};background:#E9F1EA">✓ {b}</div></div>' for a, b in linhas)
    cab = (f'<div style="display:grid;grid-template-columns:1fr 1fr">'
           f'<div style="padding:14px 18px;background:#ddd5c6;font:400 30px \'Bagel Fat One\';color:{CARVAO}">AGÊNCIA DE TUDO</div>'
           f'<div style="padding:14px 18px;background:{TOMATE};font:400 30px \'Bagel Fat One\';color:{CREME}">ORÉGANO TURBO</div></div>')
    inner = (B('Agência de tudo<br>não entende <span style="color:' + ACAFRAO + '">forno.</span>', 96 if alto else 82, CREME)
             + foto_box('1878346', '100%', 'auto', 'center 70%')
             + f'<div style="flex:none;background:{CREME};border:5px solid {CARVAO};box-shadow:14px 14px 0 {TINTA}">{cab}{tab}</div>')
    return corpo(VERDE, inner, H) + tarja(CARVAO) + '</div>'

# ---------------------------------------------------------------- 08 · objeção (creme · conversa de WhatsApp)
def c08(H):
    alto = H > 1400
    bal = lambda t, eu, h: (f'<div style="align-self:{"flex-end" if eu else "flex-start"};max-width:78%;background:{"#DCF8C6" if eu else "#fff"};'
                            f'border-radius:22px;padding:16px 22px;box-shadow:0 4px 0 rgba(0,0,0,.12);font:500 {32 if alto else 27}px/1.3 Inter;color:{CARVAO}">{t}'
                            f'<div style="font:500 15px Inter;color:#777;text-align:right;margin-top:4px">{h}</div></div>')
    conversa = (f'<div style="flex:1 1 auto;min-height:0;display:flex;flex-direction:column;gap:18px;justify-content:space-evenly;background:#EFE6D8;border:5px solid {CARVAO};padding:26px;box-shadow:14px 14px 0 {CARVAO}">'
                + bal('Já impulsionei post e não veio pedido nenhum.', False, '21:14')
                + bal('Impulsionar é apertar um botão. Anúncio de pizzaria precisa de 3 coisas: foto que dá fome, raio de entrega certo e o pedido caindo no zap.', True, '21:15 ✓✓')
                + bal('E se mesmo assim não vier?', False, '21:15')
                + bal('A gente não promete número. Mostra toda segunda o que entrou e ajusta junto com você.', True, '21:16 ✓✓') + '</div>')
    inner = (f'<div style="display:flex;gap:26px;align-items:center;flex:none">'
             + foto_box('31094831', '250px', '300px' if alto else '250px', 'center 40%', '', CARVAO, -5)
             + B('"Já tentei<br>e não deu<br><span style="color:' + TOMATE + '">nada."</span>', 84 if alto else 74, CARVAO) + '</div>'
             + conversa + MONO('conversa de exemplo · não é promessa de resultado', 16, CARVAO, 'opacity:.75'))
    return corpo(CREME, inner, H, f'<div class="a" style="inset:0;background:{padrao(VERDE, .07)}"></div>') + tarja(VERDE, CREME, 'Tirar minha dúvida ↗') + '</div>'

# ---------------------------------------------------------------- 09 · autoridade/especialista (tomate · palavra gigante com a foto dentro)
def c09(H):
    alto = H > 1400
    inner = (MONO('Marketing de vendas · só pizzarias · São Luís', 20, CREME)
             + f'<div style="flex:none;font:400 {370 if alto else 300}px/.8 \'Bagel Fat One\';letter-spacing:-.03em;background:url({FT("27359003")}) center 45%/cover;'
               f'-webkit-background-clip:text;color:transparent;-webkit-text-stroke:5px {CREME};margin:56px -10px 0">SÓ<br>PIZZA</div>'
             + B('A gente não faz<br>açaí, sushi nem<br>hamburgueria.', 86 if alto else 60, CREME, .95, SH(TINTA, 5))
             + (('<div style="display:flex;flex-wrap:wrap;gap:34px 30px;padding:20px 6px;flex:none">' + ''.join(adesivo('<s>'+t+'</s>', CREME, CARVAO, r, 34, borda=CARVAO) for t, r in [('açaí', -6), ('sushi', 4), ('hambúrguer', -3), ('pet shop', 5)])
                  + adesivo('pizzaria ✓', VERDE, CREME, -4, 40) + '</div>') if alto else '')
             + f'<div style="flex:1 1 auto"></div>'
             + (f'<div style="flex:none;margin:0 -56px;height:240px;background:{xadrez(TOMATE, CREME, 40)};border-top:5px solid {CARVAO};border-bottom:5px solid {CARVAO}"></div>' if alto else '')
             + TXT('Cardápio, dia fraco, taxa de app, rodízio, borda recheada: todo dia é o mesmo assunto. O seu.', 28, CREME))
    deco = A(720, 120, estrela(220, ACAFRAO, f'<div style="font:400 34px/1 \'Bagel Fat One\';color:{CARVAO}">100%<br>pizzaria</div>', 10))
    return corpo(TOMATE, inner, H, f'<div class="a" style="inset:0;background:{padrao(CREME, .1)}"></div>' + deco) + tarja(CARVAO, CREME, 'Falar com especialista ↗', VERDE) + '</div>'

# ---------------------------------------------------------------- 10 · chamada direta (verde · polaroid inclinada + adesivos)
def c10(H):
    alto = H > 1400
    pol = (f'<div style="background:#fff;padding:22px 22px 80px;transform:rotate(6deg);box-shadow:20px 22px 0 rgba(0,0,0,.35);position:relative">'
           f'<div style="width:{520 if alto else 380}px;height:{760 if alto else 440}px;background:url({FT("4109048")}) center 30%/cover"></div>'
           f'<div style="position:absolute;bottom:20px;left:0;right:0;text-align:center;font:400 34px \'Bagel Fat One\';color:{TOMATE}">a SUA pizza aqui</div></div>')
    inner = (B('Dono de pizzaria<br>em <span style="color:' + ACAFRAO + '">São Luís:</span>', 92 if alto else 80, CREME)
             + B('isso é pra você.', 70 if alto else 60, CREME, .9, 'opacity:.9')
             + f'<div style="flex:1 1 auto;min-height:0;display:flex;align-items:center;gap:30px">{pol}'
             + '<div style="display:flex;flex-direction:column;gap:30px">' + adesivo('foto que dá fome', TOMATE, CREME, -6, 30)
             + adesivo('anúncio no bairro', CREME, VERDE, 4, 30, borda=CARVAO) + adesivo('pedido no zap', ACAFRAO, CARVAO, -3, 30) + '</div></div>'
             + TXT('Manda "PIZZA" no WhatsApp e a gente marca o seu Raio-X.', 32 if alto else 29, CREME, 'font-weight:800'))
    return corpo(VERDE, inner, H, f'<div class="a" style="inset:0;background:{xadrez(VERDE, VERDE_ESC, 40)};opacity:.5"></div>') + tarja(TINTA, CREME, 'Mandar "PIZZA" ↗') + '</div>'

FUNCS = [c01, c02, c03, c04, c05, c06, c07, c08, c09, c10]
for n, f in enumerate(FUNCS, 1):
    for nome, H in (('feed', 1350), ('story', 1920)):
        P.append((f'c{n:02d}-{nome}', 1080, H, f(H) + GRAO))

open(os.path.join(D, 'pecas.html'), 'w').write(
    f'<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>' +
    ''.join(f'<section class="f" id="{i}" style="width:{w}px;height:{h}px">{c}</section>' for i, w, h, c in P) + '</body></html>')
print(len(P), 'peças')
