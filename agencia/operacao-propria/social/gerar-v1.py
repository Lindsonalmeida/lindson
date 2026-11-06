# Kit de lançamento do Instagram @oreganoturbo · Paollo (sessão paralela da conta Leandro, 06/11/2026)
# Pedido do Lindson: "artes mais impactantes e que chamem atenção para as vendas" · "pode parecer uma pizzaria" ·
# "nunca me dê coisas simplistas" · "menos espaços em branco, imagens".
# Persona (identidade/BRIEF.md): dono de pizzaria em São Luís, 30-55 anos, vive no balcão e no celular, depende do app
# e do fim de semana, confia em foto real, seriedade e número; quer ver pizza e pedido, não "arte de designer".
# Identidade v3 aprovada (folha com seta, Inter Tight/Inter/IBM Plex Mono, carvão/verde/creme/brasa) + vocabulário de
# pizzaria da biblioteca (letra gorda, xadrez de cantina, selos, comida recortada grande). Qual post copia qual
# referência: TEMPLATE.md. Gera pecas.html -> node render.js -> artes/*.jpg + previa-feed.jpg.
# Fotos: ../identidade/fotos-v3 e fotos-v4 (Wikimedia Commons, créditos nos CREDITOS.md) recortadas em recortes/.
CARVAO, CREME, VERDE, BRASA = '#141311', '#F3EEE6', '#1E5B3B', '#E4572E'
VERDE_E, BRASA_E, QUEIJO, PAPEL = '#123A26', '#A8361A', '#F2B33D', '#FBF8F3'
R = lambda n: f'recortes/{n}.png'
F = lambda n: f'../identidade/{n}.jpg'

def simbolo(t, folha=VERDE, seta=CREME):
    return (f'<svg viewBox="0 0 100 100" width="{t}" height="{t}" style="flex:none">'
            f'<path d="M18 86 C 14 50, 40 18, 86 14 C 86 58, 58 88, 18 86 Z" fill="{folha}"/>'
            f'<path d="M26 76 L44 58 L54 66 L72 40" fill="none" stroke="{seta}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<path d="M60 38 L74 38 L74 52" fill="none" stroke="{seta}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></svg>')

def logo(t=34, cor=CREME, folha=VERDE, seta=CREME, handle=True):
    h = f'<div style="font:500 {t*.42:.0f}px/1 IBM Plex Mono;letter-spacing:.12em;color:{cor};opacity:.8;margin-top:{t*.18:.0f}px">@OREGANOTURBO</div>' if handle else ''
    return (f'<div style="display:flex;align-items:center;gap:{t*.3:.0f}px">{simbolo(t*1.25, folha, seta)}'
            f'<div><div style="font:800 {t}px/.9 Inter Tight;letter-spacing:-.045em;color:{cor};white-space:nowrap">Orégano Turbo</div>{h}</div></div>')

def A(x, y, inner, extra=''):
    return f'<div class="a" style="left:{x}px;top:{y}px;{extra}">{inner}</div>'

def img(src, x, y, w, rot=0, sombra=.5, extra=''):
    sh = f'filter:drop-shadow(0 {w*.05:.0f}px {w*.05:.0f}px rgba(0,0,0,{sombra}));' if sombra else ''
    return f'<img src="{src}" class="a" style="left:{x}px;top:{y}px;width:{w}px;transform:rotate({rot}deg);{sh}{extra}">'

def xadrez(c1, c2, q=40):
    return f'background:repeating-conic-gradient({c1} 0 25%,{c2} 0 50%) 0 0/{q*2}px {q*2}px'

def faixa_xadrez(x, y, w, h, c1, c2, q=40):
    return f'<div class="a" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;{xadrez(c1, c2, q)}"></div>'

def caixa(x, y, w, h, bg, extra=''):
    return f'<div class="a" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:{bg};{extra}"></div>'

def txt(x, y, s, fonte, cor, extra=''):
    return A(x, y, s, f'font:{fonte};color:{cor};{extra}')

def selo_circular(t, frase, cor_txt, cor_bg, centro, rot=0, borda=None, tam_txt=None):
    """Selo redondo com texto em volta (biblioteca: selos e adesivos de cantina)."""
    tt = tam_txt or 11
    b = f'<circle cx="100" cy="100" r="96" fill="none" stroke="{borda}" stroke-width="3"/>' if borda else ''
    return (f'<svg viewBox="0 0 200 200" width="{t}" height="{t}" style="transform:rotate({rot}deg);overflow:visible">'
            f'<circle cx="100" cy="100" r="98" fill="{cor_bg}"/>{b}'
            f'<defs><path id="c{abs(hash(frase))%9999}" d="M100,100 m-76,0 a76,76 0 1,1 152,0 a76,76 0 1,1 -152,0"/></defs>'
            f'<text style="font:800 {tt}px Inter Tight;letter-spacing:.18em;fill:{cor_txt}"><textPath href="#c{abs(hash(frase))%9999}">{frase}</textPath></text>'
            f'<foreignObject x="40" y="40" width="120" height="120"><div xmlns="http://www.w3.org/1999/xhtml" style="width:120px;height:120px;display:grid;place-items:center;text-align:center">{centro}</div></foreignObject></svg>')

def texto_circular(t, frase, cor, tam=28, rot=0):
    """Texto em volta da pizza (biblioteca: post PIZZA com 'peça já a sua')."""
    i = abs(hash(frase)) % 9999
    return (f'<svg viewBox="0 0 1000 1000" width="{t}" height="{t}" style="transform:rotate({rot}deg)"><defs><path id="t{i}" d="M500,500 m-440,0 a440,440 0 1,1 880,0 a440,440 0 1,1 -880,0"/></defs>'
            f'<text style="font:900 {tam}px Inter Tight;letter-spacing:.14em;fill:{cor}"><textPath href="#t{i}" textLength="2740">{frase}</textPath></text></svg>')

def pilula(t, bg, cor, tam=30, extra=''):
    return f'<div style="display:inline-block;background:{bg};color:{cor};font:800 {tam}px/1 Inter Tight;padding:{tam*.7:.0f}px {tam*1.1:.0f}px;border-radius:999px;white-space:nowrap;{extra}">{t}</div>'

def etq(t, cor, tam=18, extra=''):
    return f'<div style="font:500 {tam}px/1 IBM Plex Mono;letter-spacing:.14em;text-transform:uppercase;color:{cor};white-space:nowrap;{extra}">{t}</div>'

ILUSTR = lambda cor='#ffffffaa': etq('Exemplo ilustrativo · não é promessa de resultado', cor, 15)

def iphone(inner, w=440, h=900, bg='#fff', hora='19:42', claro=False):
    c = '#fff' if claro else '#111'
    return (f'<div style="width:{w}px;height:{h}px;border-radius:66px;background:#0b0b0a;padding:14px;box-shadow:0 60px 100px -30px rgba(0,0,0,.7),0 0 0 2px #3a3833 inset">'
            f'<div style="position:relative;width:100%;height:100%;border-radius:54px;overflow:hidden;background:{bg}">'
            f'<div style="position:absolute;left:50%;top:12px;transform:translateX(-50%);width:120px;height:34px;border-radius:20px;background:#0b0b0a;z-index:5"></div>'
            f'<div style="display:flex;justify-content:space-between;padding:20px 36px 0;font:600 17px Inter;color:{c}"><span>{hora}</span><span>●●● ▮</span></div>'
            f'{inner}</div></div>')

def balao(t, eu=False, hora='19:42', tam=19):
    cor = '#d9fdd3' if eu else '#fff'
    return (f'<div style="align-self:{"flex-end" if eu else "flex-start"};max-width:80%;background:{cor};border-radius:14px;padding:11px 14px 7px;'
            f'font:400 {tam}px/1.35 Inter;color:#111;box-shadow:0 1px 1px rgba(0,0,0,.15)">{t}<div style="text-align:right;font-size:12px;color:#667;margin-top:3px">{hora}{" ✓✓" if eu else ""}</div></div>')

def whats(msgs, nome='Cliente · Cohama', foto=None):
    topo = (f'<div style="background:#075e54;padding:16px 20px;display:flex;align-items:center;gap:12px;color:#fff;margin-top:8px">'
            f'<div style="width:46px;height:46px;border-radius:50%;background:{foto or "#9bb"} center/cover"></div>'
            f'<div><div style="font:700 19px Inter">{nome}</div><div style="font:400 14px Inter;opacity:.8">online</div></div></div>')
    corpo = f'<div style="display:flex;flex-direction:column;gap:10px;padding:18px 16px;background:#efe7dd;height:100%">{"".join(msgs)}</div>'
    return topo + corpo

def grao():
    return ('<div class="a grao" style="inset:0"></div>')

def S(id_, w, h, bg, inner):
    return f'<section class="f" id="{id_}" style="width:{w}px;height:{h}px;background:{bg}">{inner}{grao()}</section>'

P = []

# ───────────── FEED ─────────────
# 01 · Palavra gigante atrás da pizza (Pinterest "PIZZA" + Dribbble "Cheesy PIZZA")
P.append(S('post-01-fila', 1080, 1350, BRASA,
  caixa(0, 0, 1080, 1350, f'radial-gradient(circle at 50% 52%,#f0673c 0%,{BRASA} 45%,{BRASA_E} 100%)') +
  txt(-14, 70, 'FILA', '400 640px/0.86 Anton', CREME, 'letter-spacing:-.01em;width:1110px;text-align:center;transform:scaleX(1.18);transform-origin:center') +
  txt(70, 70, 'Sua pizza merece', '400 92px/1 Kaushan Script', CARVAO, 'transform:rotate(-6deg);background:' + QUEIJO + ';padding:6px 26px 14px;border-radius:10px;box-shadow:0 14px 30px rgba(0,0,0,.25)') +
  A(110, 400, texto_circular(860, 'PEDIDO DIRETO NO SEU WHATSAPP ✦ TODO DIA DA SEMANA ✦ MARKETING DE VENDAS PARA PIZZARIAS ✦', CARVAO, 31, -20)) +
  img(R('pepperoni-cima'), 190, 510, 700, 8, .6) +
  caixa(0, 1150, 1080, 200, CARVAO) + faixa_xadrez(0, 1150, 1080, 26, CREME, BRASA, 13) +
  A(70, 1218, logo(36)) +
  A(612, 1222, pilula('Quero mais pedidos →', BRASA, '#fff', 28))))

# 02 · Chave de interface ON/OFF (Pinterest "O nosso delivery está ON" + Dribbble "Mood ON")
def chave(on, y):
    bg, letra, pos = (CREME, VERDE, 'right') if on else ('#2a2925', '#6d6a63', 'left')
    piz = img(R('pepperoni-cima'), 470 if on else 18, 18, 290, 0, .45 if on else 0, '' if on else 'filter:grayscale(1) brightness(.55)')
    lab = txt(70 if on else 360, 52, 'ON' if on else 'OFF', '400 210px/1 Bagel Fat One', letra)
    return A(150, y, f'<div style="position:relative;width:780px;height:326px;border-radius:999px;background:{bg};box-shadow:0 30px 60px -20px rgba(0,0,0,.6),inset 0 -10px 0 rgba(0,0,0,.12)">{lab}{piz}</div>')
P.append(S('post-02-on-off', 1080, 1350, VERDE,
  faixa_xadrez(0, 0, 1080, 120, CREME, VERDE_E, 30) + faixa_xadrez(0, 1230, 1080, 120, CREME, VERDE_E, 30) +
  txt(0, 160, 'Na terça, o seu<br>delivery está', '400 104px/1 Bagel Fat One', CREME, 'width:1080px;text-align:center') +
  chave(True, 395) + chave(False, 760) +
  txt(0, 1110, 'Quem lembra o cliente de pedir, vende todo dia.', '700 34px/1.2 Inter Tight', CREME, 'width:1080px;text-align:center;letter-spacing:-.01em') +
  A(60, 1262, f'<div style="background:{VERDE};padding:10px 22px;border-radius:14px">{logo(30)}</div>') +
  A(700, 1268, pilula('Ligue o seu →', QUEIJO, CARVAO, 26))))

# 03 · Fatias voando + manchete em 2 tamanhos (Pinterest "AQUI NÃO TEM ERRO")
P.append(S('post-03-terca-vazia', 1080, 1350, BRASA,
  caixa(0, 0, 1080, 1350, f'radial-gradient(ellipse at 50% 40%,#f4774a 0%,{BRASA} 40%,#7d2410 100%)') +
  txt(0, 40, 'TERÇA', '400 300px/0.9 Bagel Fat One', CREME, 'width:1080px;text-align:center;letter-spacing:-.02em') +
  img(R('fatia-pepperoni-cima-1'), 640, 330, 330, -28, .55) +
  img(R('pepperoni-fatia'), 330, 300, 420, 32, .6) +
  img(R('fatia-calabresa-0'), 60, 430, 300, 18, .55, 'filter:blur(2px) drop-shadow(0 20px 20px rgba(0,0,0,.4))') +
  img(R('fatia-pepperoni-cima-2'), 720, 640, 260, 50, .5, 'filter:blur(1.5px) drop-shadow(0 20px 20px rgba(0,0,0,.4))') +
  txt(0, 640, 'VAZIA', '400 300px/0.9 Bagel Fat One', CREME, 'width:1080px;text-align:center;letter-spacing:-.02em;text-shadow:0 10px 30px rgba(0,0,0,.25)') +
  txt(0, 960, 'é dinheiro', '900 64px/1 Inter Tight', CARVAO, 'width:1080px;text-align:center;letter-spacing:-.03em') +
  txt(0, 1035, 'NO LIXO', '400 200px/0.9 Anton', CREME, 'width:1080px;text-align:center;letter-spacing:.01em') +
  img(R('fatia-calabresa-2'), 40, 980, 230, -40, .5) +
  A(60, 60, logo(28)) +
  A(800, 1280, etq('Arraste e veja a conta →', CREME, 16))))

# 04 · Cardápio de lousa: "quanto custa uma terça vazia" (Pinterest "Escolha sua pizza" com preço)
itens = [('Aluguel do ponto', 'PAGA IGUAL'), ('Gás do forno aceso', 'PAGA IGUAL'), ('Equipe esperando pedido', 'PAGA IGUAL'),
         ('Motoboy parado na porta', 'PAGA IGUAL'), ('Massa que sobrou', 'VAI PRO LIXO')]
lin = ''.join(f'<div style="display:flex;align-items:baseline;gap:14px;margin-bottom:30px"><span style="font:700 38px Inter Tight;color:{CREME};letter-spacing:-.02em;white-space:nowrap">{a}</span>'
              f'<span style="flex:1;border-bottom:4px dotted #ffffff55;transform:translateY(-8px)"></span>'
              f'<span style="font:400 30px Bagel Fat One;color:{CARVAO};background:{QUEIJO if b == "PAGA IGUAL" else BRASA};padding:8px 16px;border-radius:10px;white-space:nowrap;transform:rotate(-2deg)">{b}</span></div>' for a, b in itens)
P.append(S('post-04-cardapio-terca', 1080, 1350, CARVAO,
  caixa(0, 0, 1080, 1350, 'radial-gradient(circle at 30% 30%,#2b2a26 0%,#141311 70%)') +
  faixa_xadrez(0, 0, 1080, 56, BRASA, CREME, 28) +
  img(R('pizza-close'), 640, 820, 640, -12, .6) +
  txt(70, 110, 'Cardápio da', '400 64px/1 Kaushan Script', QUEIJO) +
  txt(70, 180, 'TERÇA VAZIA', '400 170px/0.9 Anton', CREME, 'letter-spacing:.005em') +
  txt(70, 375, 'Com pedido ou sem pedido, a conta chega:', '500 32px/1.2 Inter', '#d9d4ca') +
  A(70, 460, lin, 'width:900px') +
  caixa(70, 1155, 600, 3, '#ffffff30') +
  txt(70, 1180, 'Pizza boa não basta.<br><span style="color:' + BRASA + '">Quem aparece mais, vende mais.</span>', '800 40px/1.15 Inter Tight', CREME, 'letter-spacing:-.02em') +
  A(70, 1290, logo(26))))

# 05 · Humor de referência pop: "Penso, logo PEÇO" (Pinterest @pizzariavoveva, retrato em domínio público)
P.append(S('post-05-penso-logo-peco', 1080, 1350, BRASA,
  caixa(0, 0, 1080, 1350, f'linear-gradient(180deg,{BRASA} 0%,#c94622 100%)') +
  txt(60, 50, 'PENSO, LOGO', '400 150px/0.9 Anton', CREME) +
  txt(40, 240, 'PEÇO.', '400 400px/0.85 Anton', QUEIJO, 'letter-spacing:-.01em') +
  img(R('descartes'), 300, 470, 860, 0, .45) +
  img(R('pepperoni-fatia'), 820, 1040, 300, -58, .6) +
  A(60, 820, f'<div style="background:{CARVAO};color:{CREME};padding:34px 36px;border-radius:22px;width:420px;box-shadow:0 30px 60px -20px rgba(0,0,0,.6)">'
              f'<div style="font:800 44px/1.05 Inter Tight;letter-spacing:-.03em">O seu cliente também.</div>'
              f'<div style="font:500 28px/1.3 Inter;margin-top:16px;color:#d9d4ca">A pergunta é: ele pede <b style="color:{QUEIJO}">pra você</b> ou pro concorrente que apareceu primeiro?</div></div>') +
  A(60, 1210, f'<div style="background:{CREME};padding:14px 22px;border-radius:14px">{logo(30, CARVAO)}</div>') +
  A(60, 1310, etq('Retrato: Frans Hals, c.1649 · domínio público', '#ffffffaa', 13))))

# 06 · Cartaz retrô com selo de oferta (Pinterest "Noite da Pizza" com HOT OFFER)
P.append(S('post-06-fundadoras', 1080, 1350, CREME,
  caixa(0, 0, 1080, 1350, xadrez(VERDE, CREME, 34)) +
  caixa(60, 60, 960, 1230, CREME, 'border-radius:28px;box-shadow:0 0 0 8px ' + VERDE) +
  etq('São Luís · 2026 · Orégano Turbo', VERDE, 20, 'position:absolute;left:110px;top:110px') +
  txt(100, 150, 'VAGAS DE', '400 150px/0.95 Bagel Fat One', VERDE, 'letter-spacing:-.02em') +
  txt(90, 300, 'FUNDADORA', '400 146px/0.95 Bagel Fat One', BRASA, 'letter-spacing:-.03em;transform:rotate(-3deg);text-shadow:6px 6px 0 ' + CARVAO) +
  img(R('calabresa'), 170, 560, 760, -8, .5) +
  A(700, 470, selo_circular(300, 'SÓ PARA AS 5 PRIMEIRAS ✦ SÓ PARA AS 5 PRIMEIRAS ✦', CREME, BRASA,
        f'<div style="font:400 64px/0.9 Bagel Fat One;color:{CREME}">SÓ<br>5</div><div style="font:800 15px Inter Tight;color:{CREME};letter-spacing:.1em">VAGAS</div>', 12, CREME, 12)) +
  A(100, 1110, f'<div style="background:{VERDE};color:{CREME};padding:26px 32px;border-radius:20px;width:540px">'
               f'<div style="font:800 36px/1.1 Inter Tight;letter-spacing:-.02em">Preço do plano anual<br>no prazo semestral.</div></div>') +
  A(680, 1120, f'<div style="font:400 30px/1.2 Kaushan Script;color:{CARVAO};transform:rotate(-4deg)">Chama no direct:</div>{pilula("FUNDADORA", BRASA, "#fff", 34, "margin-top:10px")}') +
  A(700, 92, logo(24, CARVAO, VERDE, CREME, False))))

# 07 · Celular com pedido chegando no WhatsApp (Pinterest "Hungry? Just click!" + "Cravo")
chat = whats([
  balao('Boa noite! Vi vocês no Instagram 😍', hora='19:41'),
  balao('Quero 1 calabresa grande e 1 refri 2L', hora='19:41'),
  balao('Boa noite! Anotado 🍕 Pix ou cartão?', True, '19:42'),
  balao('Pix! Manda a chave', hora='19:42'),
  f'<div style="align-self:flex-end;width:70%;height:190px;border-radius:14px;background:url({F("fotos-v4/calabresa")}) center/cover;border:6px solid #d9fdd3"></div>',
  balao('Saindo em 35 min ✅', True, '19:43')], 'Juliana · Renascença', F('fotos-v4/queijo-puxando'))
P.append(S('post-07-whatsapp', 1080, 1350, VERDE,
  caixa(0, 0, 1080, 1350, f'radial-gradient(circle at 75% 45%,#2a7a50 0%,{VERDE} 45%,{VERDE_E} 100%)') +
  txt(-30, 900, 'PEDIDO', '400 420px/0.8 Anton', '#ffffff10', 'letter-spacing:-.01em') +
  A(560, 140, iphone(chat, 450, 920, '#efe7dd'), 'transform:rotate(7deg)') +
  A(600, 110, pilula('🔔 Novo pedido', BRASA, '#fff', 30, 'box-shadow:0 20px 40px rgba(0,0,0,.4)'), 'transform:rotate(-4deg);z-index:3') +
  txt(60, 120, 'Pedido<br>direto', '400 190px/0.88 Anton', CREME) +
  txt(60, 470, 'no seu WhatsApp.', '400 66px/1 Kaushan Script', QUEIJO, 'transform:rotate(-4deg)') +
  txt(60, 590, 'Sem aplicativo no meio.<br>O cliente é seu, o contato<br>fica com você.', '600 32px/1.3 Inter', CREME) +
  img(R('pepperoni-inteira'), -120, 880, 640, -10, .6) +
  A(60, 1280, logo(26)) + A(560, 1300, etq('Conversa ilustrativa', '#ffffffaa', 15))))

# 08 · Relatório de segunda (Owner.com: o número do restaurante em close)
dias = [('S', 34), ('T', 22), ('Q', 30), ('Q', 41), ('S', 72), ('S', 96), ('D', 88)]
barras = ''.join(f'<div style="display:flex;flex-direction:column;align-items:center;gap:8px;flex:1"><div style="width:100%;height:{v*2.3:.0f}px;border-radius:10px 10px 4px 4px;background:{BRASA if i == 1 else VERDE}"></div><span style="font:600 18px IBM Plex Mono;color:#6b665d">{d}</span></div>' for i, (d, v) in enumerate(dias))
rel = (f'<div style="width:620px;background:#fff;border-radius:28px;padding:36px 38px;box-shadow:0 50px 90px -30px rgba(20,19,17,.55)">'
       f'<div style="display:flex;justify-content:space-between;align-items:center">{etq("Relatório da semana", "#6b665d", 17)}{simbolo(40)}</div>'
       f'<div style="font:800 36px/1.1 Inter Tight;color:{CARVAO};margin:14px 0 22px;letter-spacing:-.02em">Pizzaria do bairro · 28/10 a 03/11</div>'
       f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:26px">'
       f'<div style="background:{CREME};border-radius:16px;padding:18px 20px"><div style="font:500 18px Inter;color:#6b665d">Pedidos no WhatsApp</div><div style="font:800 56px/1.1 Inter Tight;color:{CARVAO}">142</div></div>'
       f'<div style="background:{CREME};border-radius:16px;padding:18px 20px"><div style="font:500 18px Inter;color:#6b665d">Custo de cada pedido</div><div style="font:800 56px/1.1 Inter Tight;color:{VERDE}">R$ 4,10</div></div></div>'
       f'<div style="display:flex;gap:12px;align-items:flex-end;height:250px">{barras}</div>'
       f'<div style="margin-top:22px;background:#fdebe5;border-radius:14px;padding:16px 18px;font:600 21px/1.35 Inter;color:{BRASA_E}">Terça foi o dia mais fraco. Ação da semana: combo de terça no anúncio do bairro.</div></div>')
P.append(S('post-08-relatorio-segunda', 1080, 1350, CREME,
  caixa(0, 760, 1080, 590, xadrez(CREME, '#e5dccd', 40)) +
  img(R('fatia-pepperoni-cima-0'), 700, 860, 480, 22, .55) + A(800, 262, selo_circular(220, 'TODA SEGUNDA ✦ NÚMERO NA MESA ✦ TODA SEGUNDA ✦ ', CREME, VERDE, f'<div style="font:400 46px/0.9 Bagel Fat One;color:{QUEIJO}">8H</div>', -12, QUEIJO, 12), 'z-index:5') +
  A(200, 380, rel, 'transform:rotate(-3deg) scale(1.08);transform-origin:top left') +
  txt(60, 80, 'SEGUNDA, 8H.', '400 168px/0.9 Anton', CARVAO, 'letter-spacing:.005em') +
  txt(60, 240, 'O número da sua semana<br>chega antes do forno ligar.', '800 46px/1.1 Inter Tight', VERDE, 'letter-spacing:-.025em') +
  A(60, 1280, f'<div style="background:{CREME};padding:6px 14px;border-radius:12px">{logo(26, CARVAO)}</div>') +
  A(520, 1290, f'<div style="background:{CARVAO};padding:10px 16px;border-radius:10px">{etq("Exemplo ilustrativo · não é promessa", CREME, 14)}</div>')))

# 09 · Antes e depois do perfil (sem números) (Dribbble "before/after" de feed + Toast)
def feed(fotos, filtro, bgc, nomec):
    g = ''.join(f'<div style="aspect-ratio:4/5;background:url({F(f)}) center/cover;filter:{filtro}"></div>' for f in fotos)
    return (f'<div style="padding:18px 18px 0;display:flex;align-items:center;gap:14px"><div style="width:70px;height:70px;border-radius:50%;background:{bgc}"></div>'
            f'<div style="font:700 20px Inter;color:{nomec}">pizzaria_do_bairro</div></div>'
            f'<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:3px;margin-top:20px">{g}</div>')
antes = feed(['fotos-v3/bancada', 'fotos-v4/caixa-viagem', 'fotos-v3/caixas', 'fotos-v4/calabresa-porcoes', 'fotos-v3/bancada', 'fotos-v4/caixa-aberta', 'fotos-v3/caixas', 'fotos-v4/queijo-borda', 'fotos-v4/caixa-viagem'],
             'brightness(.42) saturate(.35) contrast(.9) blur(.6px)', '#555', '#222')
depois = feed(['fotos-v4/queijo-puxando', 'fotos-v3/pa-no-forno', 'fotos-v4/pepperoni-fatia', 'fotos-v3/pizza-close', 'fotos-v4/pepperoni-cima', 'fotos-v3/brasa', 'fotos-v4/fatia-puxando', 'fotos-v4/calabresa', 'fotos-v3/forno-pizza'],
              'saturate(1.25) contrast(1.05)', BRASA, '#111')
def rot(t, ok):
    c = VERDE if ok else '#8a857c'
    return f'<div style="display:flex;align-items:center;gap:12px;font:700 26px Inter Tight;color:{CREME if ok else "#bdb7ad"};margin-bottom:12px"><span style="width:36px;height:36px;border-radius:50%;background:{c};display:grid;place-items:center;font-size:22px;color:#fff">{"✓" if ok else "✕"}</span>{t}</div>'
P.append(S('post-09-antes-depois', 1080, 1350, CARVAO,
  caixa(540, 0, 540, 1350, BRASA) +
  txt(0, 60, 'O MESMO FORNO.', '400 120px/0.9 Anton', CREME, 'width:1080px;text-align:center') +
  txt(0, 170, 'OUTRO PERFIL.', '400 120px/0.9 Anton', CREME, 'width:1080px;text-align:center;clip-path:inset(0 50% 0 0)') +
  txt(0, 170, 'OUTRO PERFIL.', '400 120px/0.9 Anton', CARVAO, 'width:1080px;text-align:center;clip-path:inset(0 0 0 50%)') +
  etq('ANTES', '#8a857c', 26, 'position:absolute;left:60px;top:330px') + etq('DEPOIS', CARVAO, 26, 'position:absolute;left:600px;top:330px') +
  A(60, 380, iphone(antes, 420, 600, '#e9e6e0', claro=False), 'transform:rotate(-3deg)') +
  A(600, 380, iphone(depois, 420, 600, '#fff'), 'transform:rotate(3deg)') +
  A(470, 610, f'<div style="width:140px;height:140px;border-radius:50%;background:{QUEIJO};display:grid;place-items:center;font:400 54px Bagel Fat One;color:{CARVAO};box-shadow:0 20px 40px rgba(0,0,0,.4)">VS</div>') +
  A(60, 1040, rot('Foto escura', False) + rot('Só promoção', False) + rot('Sem link de pedido', False)) +
  A(600, 1040, rot('Foto que dá fome', True) + rot('Forno, gente, bastidor', True) + rot('Link de pedido na bio', True)) +
  A(60, 1270, logo(26)) + A(600, 1282, etq('Simulação de perfil · sem números', CARVAO, 15))))

# 10 · Pergunta direta ao dono (Pinterest "Não deixe para amanhã": manchete gigante + pizza saindo do canto)
P.append(S('post-10-pergunta', 1080, 1350, BRASA,
  caixa(0, 0, 1080, 1350, f'linear-gradient(160deg,#ee6a3f 0%,{BRASA} 40%,{BRASA_E} 100%)') +
  txt(560, -80, '?', '400 1300px/1 Bagel Fat One', '#ffffff14') +
  img(R('calabresa'), 430, 830, 860, -15, .6) +
  A(60, 70, logo(28)) +
  txt(60, 190, 'Quantos<br>pedidos<br>você fez na<br>terça<br>passada?', '400 150px/0.92 Bagel Fat One', CREME, 'letter-spacing:-.025em;text-shadow:0 10px 30px rgba(0,0,0,.2)') +
  A(60, 1000, f'<div style="background:{CARVAO};color:{CREME};padding:26px 30px;border-radius:20px;width:470px;box-shadow:0 30px 60px -20px rgba(0,0,0,.6)">'
              f'<div style="font:700 30px/1.25 Inter Tight">Se a resposta te incomodou, a gente precisa conversar.</div>'
              f'<div style="margin-top:18px">{pilula("Responde aqui embaixo ↓", QUEIJO, CARVAO, 24)}</div></div>')))

# 11 · Prova de método em 4 passos (Pinterest "Anatomía de una buena pizza": pizza com setas e notas)
def passo(n, t, d):
    return (f'<div style="display:flex;gap:16px;align-items:flex-start;width:330px"><div style="flex:none;width:66px;height:66px;border-radius:50%;background:{QUEIJO};display:grid;place-items:center;font:400 40px Bagel Fat One;color:{CARVAO}">{n}</div>'
            f'<div><div style="font:800 32px/1.05 Inter Tight;color:{CREME};letter-spacing:-.02em">{t}</div><div style="font:500 22px/1.3 Inter;color:#cfe3d6;margin-top:6px">{d}</div></div></div>')
seta = lambda d: f'<svg width="150" height="90" viewBox="0 0 150 90" style="overflow:visible"><path d="{d}" fill="none" stroke="{CREME}" stroke-width="4" stroke-linecap="round" stroke-dasharray="2 10"/></svg>'
P.append(S('post-11-metodo', 1080, 1350, VERDE,
  caixa(0, 0, 1080, 1350, f'radial-gradient(circle at 50% 58%,#2a7a50 0%,{VERDE} 40%,{VERDE_E} 100%)') +
  faixa_xadrez(0, 1290, 1080, 60, CREME, VERDE_E, 30) +
  etq('Como a Orégano Turbo trabalha', QUEIJO, 20, 'position:absolute;left:0;top:70px;width:1080px;text-align:center') +
  txt(0, 110, '4 passos. Toda semana.', '400 100px/1 Anton', CREME, 'width:1080px;text-align:center') +
  img(R('pepperoni-cima'), 240, 440, 600, 0, .6) +
  A(240, 440, '<svg width="600" height="590" viewBox="0 0 460 452"><line x1="230" y1="0" x2="230" y2="452" stroke="' + CREME + '" stroke-width="6"/><line x1="0" y1="226" x2="460" y2="226" stroke="' + CREME + '" stroke-width="6"/></svg>') +
  A(50, 270, passo(1, 'Raio-X', 'O que trava o pedido no seu Instagram, cardápio e WhatsApp.')) +
  A(700, 270, passo(2, 'Anúncio no bairro', 'Quem mora perto vê a sua pizza na hora da fome.')) +
  A(50, 1040, passo(3, 'Pedido no WhatsApp', 'O cliente chama você direto, sem app no meio.')) +
  A(700, 1040, passo(4, 'Número na segunda', 'Quanto entrou, quanto custou, o que muda.')) +
  A(200, 410, seta('M20 10 C 60 30, 90 60, 120 86')) + A(730, 410, seta('M130 10 C 90 30, 60 60, 30 86'), '') +
  A(200, 950, seta('M20 80 C 60 60, 90 30, 120 4')) + A(730, 950, seta('M130 80 C 90 60, 60 30, 30 4')) +
  A(380, 1210, logo(26))))

# 12 · Chamada para o Raio-X (R$ 297) (Toast "Built for Busy" + efeito raio-x na pizza)
P.append(S('post-12-raio-x', 1080, 1350, CARVAO,
  caixa(0, 0, 1080, 1350, 'radial-gradient(circle at 62% 46%,#232a2c 0%,#141311 65%)') +
  A(380, 230, f'<div style="position:relative;width:700px;height:690px">'
              f'<img src="{R("pepperoni-cima")}" style="position:absolute;inset:0;width:700px;filter:drop-shadow(0 40px 40px rgba(0,0,0,.6))">'
              f'<img src="{R("pepperoni-cima")}" style="position:absolute;inset:0;width:700px;filter:grayscale(1) invert(1) sepia(1) hue-rotate(150deg) saturate(3) brightness(.95) contrast(1.4);clip-path:inset(0 0 0 50%)">'
              f'<div style="position:absolute;left:346px;top:-30px;width:8px;height:750px;background:#7ff3ff;box-shadow:0 0 30px 10px #39d5ff88"></div></div>') +
  txt(60, 70, 'RAIO-X', '400 250px/0.85 Anton', CREME, 'letter-spacing:.01em') +
  txt(70, 285, 'da sua pizzaria', '400 72px/1 Kaushan Script', BRASA, 'transform:rotate(-4deg)') +
  A(60, 450, ''.join(f'<div style="font:700 30px/1 Inter Tight;color:{CREME};margin-bottom:22px;display:flex;gap:14px;align-items:center"><span style="width:14px;height:14px;background:#7ff3ff;border-radius:50%;box-shadow:0 0 12px #7ff3ff"></span>{t}</div>' for t in ['Instagram', 'Cardápio e iFood', 'Anúncio', 'WhatsApp'])) +
  A(60, 960, f'<div style="background:{BRASA};border-radius:26px;padding:30px 36px;width:560px;box-shadow:0 30px 60px -20px rgba(228,87,46,.6)">'
              f'<div style="font:400 120px/0.9 Bagel Fat One;color:{CREME}">R$ 297</div>'
              f'<div style="font:700 26px/1.3 Inter Tight;color:{CREME};margin-top:12px">Abatido no 1º mês se você fechar<br>com a gente em até 7 dias.</div></div>') +
  A(680, 1050, pilula('Manda RAIO-X no direct', QUEIJO, CARVAO, 26)) +
  A(60, 1270, logo(28))))

# ───────────── CARROSSEL ─────────────
def tag_erro(n, bg, cor):
    return f'<div style="display:inline-flex;align-items:center;gap:12px;background:{bg};color:{cor};font:400 34px Bagel Fat One;padding:12px 26px;border-radius:999px">ERRO {n}<span style="font:600 22px IBM Plex Mono;opacity:.7">/5</span></div>'
def rodape_c(n, cor=CREME, folha=VERDE, seta=CREME):
    return A(60, 1272, logo(24, cor, folha, seta, False)) + A(900, 1282, etq(f'{n}/7 →', cor, 20))

C = []
C.append(S('carrossel-1-capa', 1080, 1350, CARVAO,
  f'<div class="a" style="inset:0;background:url({F("fotos-v3/pizza-close")}) 40% center/cover"></div>' +
  caixa(0, 0, 1080, 1350, 'linear-gradient(180deg,rgba(20,19,17,.2) 0%,rgba(20,19,17,.35) 35%,rgba(20,19,17,.96) 72%)') +
  txt(50, 330, '5', '400 900px/0.8 Anton', BRASA, 'text-shadow:0 30px 60px rgba(0,0,0,.5)') +
  txt(450, 560, 'ERROS', '400 230px/0.85 Anton', CREME) +
  txt(60, 1000, 'que deixam a sua pizzaria<br><span style="background:' + BRASA + ';padding:0 14px">sem pedido na terça</span>', '800 66px/1.18 Inter Tight', CREME, 'letter-spacing:-.03em') +
  A(60, 70, logo(30)) + A(760, 82, pilula('Arrasta →', QUEIJO, CARVAO, 26)) + rodape_c(1)))

C.append(S('carrossel-2-foto-escura', 1080, 1350, CREME,
  txt(560, -60, '01', '400 640px/1 Anton', '#e6dccb') +
  A(60, 70, tag_erro(1, CARVAO, CREME)) +
  txt(60, 170, 'Foto escura<br>de pizza.', '400 150px/0.9 Anton', CARVAO) +
  A(60, 480, f'<div style="width:470px;height:560px;border-radius:24px;background:url({F("fotos-v4/caixa-aberta")}) center/cover;filter:brightness(.4) saturate(.3);box-shadow:0 30px 60px -20px rgba(0,0,0,.5)"></div>', 'transform:rotate(-3deg)') +
  A(550, 460, f'<div style="width:470px;height:600px;border-radius:24px;background:url({F("fotos-v4/queijo-puxando")}) center/cover;filter:saturate(1.3) contrast(1.05);box-shadow:0 30px 60px -20px rgba(0,0,0,.5)"></div>', 'transform:rotate(3deg)') +
  A(90, 510, pilula('✕ tira a fome', '#5e5a53', CREME, 26)) + A(590, 490, pilula('✓ dá fome', VERDE, CREME, 26)) +
  txt(60, 1110, 'O cliente decide com os olhos, em 2 segundos. Luz de janela, close no queijo, fundo limpo.', '600 32px/1.3 Inter', CARVAO, 'width:960px') +
  rodape_c(2, CARVAO, VERDE, CREME)))

promo = ''.join(f'<div style="font:400 150px/0.92 Anton;color:{CREME};opacity:{.08 + i*.03:.2f};white-space:nowrap">PROMOÇÃO PROMOÇÃO</div>' for i in range(9))
C.append(S('carrossel-3-so-promocao', 1080, 1350, BRASA,
  A(-60, 0, promo) +
  A(60, 70, tag_erro(2, CARVAO, CREME)) +
  A(90, 330, f'<div style="width:900px;background:{CARVAO};border-radius:30px;padding:56px 60px;box-shadow:0 40px 80px -20px rgba(0,0,0,.6)">'
             f'<div style="font:400 120px/0.9 Anton;color:{CREME}">Só posta<br><span style="color:{QUEIJO}">promoção.</span></div>'
             f'<div style="font:500 34px/1.35 Inter;color:#d9d4ca;margin-top:30px">O cliente aprende a esperar o desconto e só pede quando tem. Mostre o forno, a massa, quem faz e o pedido saindo.</div></div>') +
  img(R('fatia-pepperoni-cima-1'), 700, 890, 360, 20, .6) +
  rodape_c(3)))

bio = (f'<div style="padding:30px 26px 0"><div style="display:flex;align-items:center;gap:20px"><div style="width:110px;height:110px;border-radius:50%;background:url({F("fotos-v4/pepperoni-cima")}) center/cover;border:4px solid {BRASA}"></div>'
       f'<div style="display:flex;gap:22px;font:700 20px Inter;color:#111;text-align:center"><div>212<br><span style="font-weight:400;font-size:15px">posts</span></div><div>3,1 mil<br><span style="font-weight:400;font-size:15px">seguidores</span></div></div></div>'
       f'<div style="font:700 20px Inter;margin-top:18px;color:#111">Pizzaria do Bairro</div><div style="font:400 18px/1.4 Inter;color:#111">🍕 A melhor pizza da região<br>📍 São Luís · MA<br>🛵 Delivery todos os dias</div>'
       f'<div style="position:relative;margin-top:10px;height:44px"><div style="position:absolute;left:-22px;top:-14px;width:290px;height:70px;border:5px solid {BRASA};border-radius:50%;transform:rotate(-4deg)"></div>'
       f'<span style="font:400 18px Inter;color:#aaa">(nenhum link)</span></div>'
       f'<div style="display:flex;gap:8px;margin-top:16px"><div style="flex:1;background:#efefef;border-radius:10px;padding:12px;text-align:center;font:600 16px Inter">Seguir</div><div style="flex:1;background:#efefef;border-radius:10px;padding:12px;text-align:center;font:600 16px Inter">Mensagem</div></div>'
       f'<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:3px;margin:22px -26px 0">' + ''.join(f'<div style="aspect-ratio:1;background:url({F(x)}) center/cover"></div>' for x in ['fotos-v4/calabresa', 'fotos-v3/pizza-close', 'fotos-v4/queijo-borda', 'fotos-v4/pepperoni-inteira', 'fotos-v3/forno-pizza', 'fotos-v4/caixa-aberta', 'fotos-v4/pepperoni-fatia', 'fotos-v3/brasa', 'fotos-v4/queijo-puxando', 'fotos-v4/pepperoni-cima', 'fotos-v3/pa-no-forno', 'fotos-v4/caixa-viagem']) + '</div></div>')
C.append(S('carrossel-4-sem-link', 1080, 1350, VERDE,
  caixa(0, 0, 1080, 1350, f'radial-gradient(circle at 30% 50%,#2a7a50 0%,{VERDE} 45%,{VERDE_E} 100%)') +
  A(60, 150, iphone(bio, 470, 960, '#fff'), 'transform:rotate(-5deg)') +
  A(250, 560, f'<div style="font:400 52px/1 Kaushan Script;color:{QUEIJO};background:{CARVAO};padding:8px 26px 14px;border-radius:14px;transform:rotate(-8deg);box-shadow:0 16px 30px rgba(0,0,0,.4)">cadê o link?</div>') +
  A(590, 70, tag_erro(3, CREME, VERDE)) +
  txt(590, 180, 'Sem link<br>de pedido<br>na bio.', '400 128px/0.9 Anton', CREME) +
  txt(590, 690, 'O cliente com fome não vai procurar o seu número. Um link direto pro WhatsApp ou cardápio, em cima de tudo.', '600 32px/1.32 Inter', '#e1efe6', 'width:440px') +
  rodape_c(4)))

chat2 = whats([balao('Boa noite, ainda tá entregando?', hora='19:42'),
               f'<div style="align-self:center;background:#e1f3fb;border-radius:8px;padding:6px 12px;font:600 14px Inter;color:#556">1 hora depois</div>',
               balao('Boa noite! Sim, o que vai querer?', True, '20:51'),
               balao('Já pedi em outro lugar 😕', hora='20:52')], 'Rafael · Cohama')
C.append(S('carrossel-5-demora', 1080, 1350, CARVAO,
  txt(470, 820, '04', '400 640px/0.8 Anton', '#24221f') +
  A(60, 70, tag_erro(4, BRASA, CREME)) +
  txt(60, 180, 'Responder<br><span style="color:' + BRASA + '">1 hora</span> depois.', '400 150px/0.9 Anton', CREME) +
  A(540, 470, iphone(chat2, 480, 760, '#efe7dd'), 'transform:rotate(5deg)') + txt(60, 900, '69 min', '400 150px/1 Bagel Fat One', BRASA) + txt(64, 1060, 'esperando resposta', '400 52px/1 Kaushan Script', QUEIJO, 'transform:rotate(-3deg)') +
  A(60, 620, f'<div style="width:440px;font:600 32px/1.32 Inter;color:#d9d4ca">Fome não espera. Quem responde primeiro leva o pedido.<br><br><span style="color:{QUEIJO};font-weight:800">Resposta pronta salva a noite.</span></div>') +
  A(60, 1190, etq('Conversa ilustrativa', '#8a857c', 16)) +
  rodape_c(5)))

sem = [('SEG', 18), ('TER', 10), ('QUA', 16), ('QUI', 34), ('SEX', 80), ('SÁB', 100), ('DOM', 92)]
cal = ''.join(f'<div style="flex:1;display:flex;flex-direction:column;align-items:center;justify-content:flex-end;gap:12px;height:560px">'
              f'<div style="width:100%;height:{v*4.6:.0f}px;border-radius:18px;background:{BRASA if v > 50 else "#d6cdbd"};position:relative;overflow:hidden">'
              + (f'<img src="{R("fatia-pepperoni-cima-0")}" style="position:absolute;left:50%;top:14px;width:90px;transform:translateX(-50%) rotate(20deg)">' if v > 50 else '') +
              f'</div><span style="font:400 30px Bagel Fat One;color:{CARVAO if v > 50 else "#9a9285"}">{d}</span></div>' for d, v in sem)
C.append(S('carrossel-6-so-fim-de-semana', 1080, 1350, CREME,
  caixa(0, 0, 1080, 400, VERDE) + faixa_xadrez(0, 400, 1080, 30, CREME, VERDE, 15) +
  A(60, 70, tag_erro(5, CREME, VERDE)) +
  txt(60, 170, 'Só aparecer no fim de semana.', '400 104px/0.95 Anton', CREME, 'width:960px') +
  A(60, 480, f'<div style="display:flex;gap:14px;width:960px">{cal}</div>') +
  txt(60, 1110, 'Quem posta e anuncia só na sexta some da cabeça do cliente na terça.', '700 34px/1.25 Inter Tight', CARVAO, 'width:900px;letter-spacing:-.01em') +
  A(60, 1215, etq('Movimento ilustrativo', '#8a857c', 15)) +
  rodape_c(6, CARVAO, VERDE, CREME)))

C.append(S('carrossel-7-chamada', 1080, 1350, BRASA,
  caixa(0, 0, 1080, 1350, f'radial-gradient(circle at 70% 70%,#f0673c 0%,{BRASA} 40%,{BRASA_E} 100%)') +
  img(R('calabresa'), 380, 640, 860, 12, .6) +
  txt(60, 80, 'Quantos desses<br>estão na sua<br>pizzaria?', '400 124px/0.95 Bagel Fat One', CREME, 'letter-spacing:-.025em') +
  txt(60, 520, 'O Raio-X mostra.', '400 74px/1 Kaushan Script', CARVAO, 'transform:rotate(-4deg)') +
  A(60, 680, f'<div style="background:{CARVAO};border-radius:24px;padding:30px 34px;width:430px;box-shadow:0 30px 60px -20px rgba(0,0,0,.6)">'
             f'<div style="font:400 92px/0.9 Bagel Fat One;color:{QUEIJO}">R$ 297</div>'
             f'<div style="font:600 24px/1.35 Inter;color:{CREME};margin-top:14px">Abatido no 1º mês se fechar em até 7 dias.</div>'
             f'<div style="margin-top:22px">{pilula("Manda RAIO-X no direct", BRASA, "#fff", 24)}</div></div>') +
  rodape_c(7)))

# ───────────── STORIES ─────────────
ST = []
ST.append(S('story-1-enquete', 1080, 1920, BRASA,
  caixa(0, 0, 1080, 1920, f'radial-gradient(circle at 50% 60%,#f0673c 0%,{BRASA} 40%,{BRASA_E} 100%)') +
  faixa_xadrez(0, 0, 1080, 90, CREME, BRASA, 45) +
  A(60, 170, logo(30)) +
  txt(0, 300, 'A sua terça é…', '400 150px/1 Bagel Fat One', CREME, 'width:1080px;text-align:center;letter-spacing:-.02em') +
  img(R('pepperoni-cima'), 190, 520, 700, 10, .6) +
  A(140, 1260, f'<div style="width:800px;background:#fff;border-radius:34px;padding:34px;box-shadow:0 30px 60px -20px rgba(0,0,0,.5)">'
               f'<div style="font:800 30px Inter Tight;color:#111;text-align:center;margin-bottom:22px">Responda com sinceridade 👇</div>'
               f'<div style="background:#f2f2f2;border-radius:18px;padding:26px;text-align:center;font:800 40px Inter Tight;color:{VERDE};margin-bottom:16px">🔥 FORNO CHEIO</div>'
               f'<div style="background:#f2f2f2;border-radius:18px;padding:26px;text-align:center;font:800 40px Inter Tight;color:{BRASA}">😴 FORNO PARADO</div></div>') +
  A(0, 1640, etq('Coloque a figurinha de ENQUETE em cima do cartão', '#ffffffaa', 16), 'width:1080px;text-align:center')))

caixinha = (f'<div style="width:820px;border-radius:34px;overflow:hidden;box-shadow:0 30px 60px -20px rgba(0,0,0,.6)">'
            f'<div style="background:{BRASA};padding:34px 30px;text-align:center;font:800 40px/1.15 Inter Tight;color:#fff">Qual a sua maior dúvida pra vender mais pizza?</div>'
            f'<div style="background:#fff;padding:36px;text-align:center;font:500 30px Inter;color:#999">Escreva aqui…</div></div>')
ST.append(S('story-2-caixinha', 1080, 1920, VERDE,
  caixa(0, 0, 1080, 1920, f'radial-gradient(circle at 50% 40%,#2a7a50 0%,{VERDE} 45%,{VERDE_E} 100%)') +
  txt(-20, 1300, 'PERGUNTA', '400 300px/0.8 Anton', '#ffffff10') +
  img(R('fatia-pepperoni-cima-1'), 700, 200, 330, -25, .6) +
  img(R('pepperoni-fatia'), 40, 1380, 360, 30, .6) +
  img(R('fatia-calabresa-2'), 740, 1450, 300, 40, .55) +
  A(60, 170, logo(30)) +
  txt(60, 330, 'ME<br>PERGUNTA', '400 220px/0.88 Anton', CREME) +
  txt(60, 740, 'sobre vender mais pizza', '400 70px/1 Kaushan Script', QUEIJO, 'transform:rotate(-4deg)') +
  txt(60, 860, 'Anúncio, Instagram, iFood, WhatsApp. Respondo as melhores aqui nos stories.', '600 36px/1.3 Inter', CREME, 'width:900px') +
  A(130, 1080, caixinha) +
  A(0, 1660, etq('Coloque a figurinha de PERGUNTAS em cima do cartão', '#ffffffaa', 16), 'width:1080px;text-align:center')))

ST.append(S('story-3-raio-x', 1080, 1920, CARVAO,
  caixa(0, 0, 1080, 1920, 'radial-gradient(circle at 50% 45%,#232a2c 0%,#141311 65%)') +
  A(60, 170, logo(30)) +
  txt(0, 300, 'A sua pizzaria<br>passa no', '800 80px/1 Inter Tight', CREME, 'width:1080px;text-align:center;letter-spacing:-.03em') +
  txt(0, 470, 'RAIO-X?', '400 270px/0.9 Anton', CREME, 'width:1080px;text-align:center') +
  A(190, 760, f'<div style="position:relative;width:700px;height:690px">'
              f'<img src="{R("pepperoni-cima")}" style="position:absolute;inset:0;width:700px;filter:drop-shadow(0 40px 40px rgba(0,0,0,.6))">'
              f'<img src="{R("pepperoni-cima")}" style="position:absolute;inset:0;width:700px;filter:grayscale(1) invert(1) sepia(1) hue-rotate(150deg) saturate(3) brightness(.95) contrast(1.4);clip-path:inset(50% 0 0 0)">'
              f'<div style="position:absolute;left:-30px;top:342px;width:760px;height:8px;background:#7ff3ff;box-shadow:0 0 30px 10px #39d5ff88"></div></div>') +
  A(140, 1470, f'<div style="width:800px;background:{BRASA};border-radius:30px;padding:30px;text-align:center;box-shadow:0 30px 60px -20px rgba(228,87,46,.6)">'
               f'<div style="font:400 110px/0.9 Bagel Fat One;color:{CREME}">R$ 297</div>'
               f'<div style="font:700 26px/1.3 Inter Tight;color:{CREME};margin-top:10px">Abatido no 1º mês se fechar em até 7 dias</div></div>') +
  A(0, 1700, f'<div style="width:1080px;text-align:center">{pilula("Responde este story com RAIO-X", QUEIJO, CARVAO, 32)}</div>')))

CSS = ('*{margin:0;padding:0;box-sizing:border-box}body{background:#777;display:flex;flex-wrap:wrap;gap:40px;padding:40px}'
       '.f{position:relative;overflow:hidden;flex:none}.a{position:absolute}img.a{display:block;height:auto}'
       '.grao{pointer-events:none;mix-blend-mode:overlay;opacity:.22;background:url("data:image/svg+xml;utf8,'
       '<svg xmlns=%27http://www.w3.org/2000/svg%27 width=%27300%27 height=%27300%27><filter id=%27n%27><feTurbulence type=%27fractalNoise%27 baseFrequency=%27.9%27 numOctaves=%272%27/></filter>'
       '<rect width=%27100%25%27 height=%27100%25%27 filter=%27url(%23n)%27/></svg>")}')
FONTES = ('<link href="https://fonts.googleapis.com/css2?family=Anton&family=Bagel+Fat+One&family=IBM+Plex+Mono:wght@500;600'
          '&family=Inter:wght@400;500;600;700&family=Inter+Tight:wght@500;700;800;900&family=Kaushan+Script&display=block" rel="stylesheet">')
html = f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">{FONTES}<style>{CSS}</style></head><body>{"".join(P + C + ST)}</body></html>'
import os
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pecas-v1.html'), 'w').write(html)
print(len(P), 'posts,', len(C), 'telas de carrossel,', len(ST), 'stories')
