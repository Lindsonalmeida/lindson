# Kit de lançamento do Instagram @oreganoturbo · v2 CAMPANHA (Paollo + Rocco, sessão paralela da conta Leandro, 06/11/2026)
# Direção nova do Lindson (06/11): "isso é o que chamo de identidade visual de verdade, impactante, criativa" (Decaf Girl/
# Misato, HOTWHIZ, Mario hot sauce, McDonald's "Here for the sauce", Drip Riot). As artes viram CAMPANHA DE MARCA DE COMIDA:
# produto enorme recortado sobre cor chapada saturada, sombra dura de flash, ingredientes voando, manchete gorda inclinada
# de até 5 palavras, zero espaço vazio. Receita: agencia/processos/direcao-de-arte-campanha-comida.md (seção 2).
# Checklist do Rocco em cada arte: produto > 50%, 1 cor dominante, luz de flash, manchete até 5 palavras, zero espaço vazio.
# Persona (identidade/BRIEF.md): dono de pizzaria em São Luís, 30-55 anos; confia em foto de pizza, conta simples, seriedade.
# Cores: identidade v4 (v3 aprovada + tomate e açafrão). Gera pecas.html -> node render.js -> artes/*.jpg + previa-feed.jpg.
# A versão 1 (antes da direção de campanha) está em gerar-v1.py e artes-v1/.
CARVAO, CREME, VERDE, BRASA = '#141311', '#F3EEE6', '#1E5B3B', '#E4572E'
TOMATE, ACAFRAO, VERDE_E = '#D42A1F', '#F2B33D', '#123B26'
R = lambda n: f'recortes/{n}.png'
F = lambda n: f'../identidade/{n}.jpg'

def simbolo(t, folha=VERDE, seta=CREME):
    return (f'<svg viewBox="0 0 100 100" width="{t}" height="{t}" style="flex:none">'
            f'<path d="M18 86 C 14 50, 40 18, 86 14 C 86 58, 58 88, 18 86 Z" fill="{folha}"/>'
            f'<path d="M26 76 L44 58 L54 66 L72 40" fill="none" stroke="{seta}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<path d="M60 38 L74 38 L74 52" fill="none" stroke="{seta}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></svg>')

def logo(t=34, cor=CREME, folha=VERDE, seta=CREME, handle=True):
    h = f'<div style="font:500 {t*.42:.0f}px/1 IBM Plex Mono;letter-spacing:.12em;color:{cor};opacity:.85;margin-top:{t*.18:.0f}px">@OREGANOTURBO</div>' if handle else ''
    return (f'<div style="display:flex;align-items:center;gap:{t*.3:.0f}px">{simbolo(t*1.25, folha, seta)}'
            f'<div><div style="font:800 {t}px/.9 Inter Tight;letter-spacing:-.045em;color:{cor};white-space:nowrap">Orégano Turbo</div>{h}</div></div>')

def A(x, y, inner, extra=''):
    return f'<div class="a" style="left:{x}px;top:{y}px;{extra}">{inner}</div>'

def flash(w, op=.42):
    """Sombra dura de flash: silhueta deslocada 18-30 px para baixo/direita, pouco desfoque (receita do Rocco)."""
    d = max(18, min(30, round(w * .03)))
    return f'drop-shadow({d}px {d + 4}px 2px rgba(0,0,0,{op})) saturate(1.12) contrast(1.08)'

def img(src, x, y, w, rot=0, op=.42, blur=0, extra=''):
    f = flash(w, op) + (f' blur({blur}px)' if blur else '')
    return f'<img src="{src}" class="a" style="left:{x}px;top:{y}px;width:{w}px;transform:rotate({rot}deg);filter:{f};{extra}">'

def voando(lista):
    """Ingredientes voando: (nome, x, y, w, rot, blur)."""
    return ''.join(img(R(n), x, y, w, r, .35, b) for n, x, y, w, r, b in lista)

def xadrez(c1, c2, q=40):
    return f'background:repeating-conic-gradient({c1} 0 25%,{c2} 0 50%) 0 0/{q*2}px {q*2}px'

def faixa_xadrez(x, y, w, h, c1, c2, q=40):
    return f'<div class="a" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;{xadrez(c1, c2, q)}"></div>'

def caixa(x, y, w, h, bg, extra=''):
    return f'<div class="a" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:{bg};{extra}"></div>'

def txt(x, y, s, fonte, cor, extra=''):
    return A(x, y, s, f'font:{fonte};color:{cor};{extra}')

def manchete(x, y, s, tam, cor, rot=-4, sombra=None, fonte='Anton', lh=.86, extra=''):
    """Manchete gorda, inclinada, com sombra dura chapada (cartaz de comida)."""
    sh = f'text-shadow:{tam*.035:.0f}px {tam*.035:.0f}px 0 {sombra};' if sombra else ''
    return A(x, y, s, f'font:400 {tam}px/{lh} {fonte};color:{cor};transform:rotate({rot}deg);transform-origin:left top;letter-spacing:-.01em;{sh}{extra}')

def selo(t, frase, cor_txt, cor_bg, centro=None, rot=0, borda=None, fs=12):
    """Selo redondo da marca com texto em volta e o símbolo no centro (identidade v4)."""
    i = abs(hash(frase + str(t))) % 99999
    b = f'<circle cx="100" cy="100" r="92" fill="none" stroke="{borda}" stroke-width="2.5"/>' if borda else ''
    c = centro or f'<div style="width:120px;height:120px;display:grid;place-items:center">{simbolo(76, cor_txt, cor_bg)}</div>'
    return (f'<svg viewBox="0 0 200 200" width="{t}" height="{t}" style="transform:rotate({rot}deg);overflow:visible;filter:drop-shadow(10px 12px 0 rgba(0,0,0,.28))">'
            f'<circle cx="100" cy="100" r="99" fill="{cor_bg}"/>{b}'
            f'<defs><path id="s{i}" d="M100,100 m-74,0 a74,74 0 1,1 148,0 a74,74 0 1,1 -148,0"/></defs>'
            f'<text style="font:800 {fs}px Inter Tight;letter-spacing:.2em;fill:{cor_txt}"><textPath href="#s{i}">{frase}</textPath></text>'
            f'<foreignObject x="40" y="40" width="120" height="120"><div xmlns="http://www.w3.org/1999/xhtml" style="width:120px;height:120px;display:grid;place-items:center;text-align:center">{c}</div></foreignObject></svg>')

def texto_circular(t, frase, cor, tam=28, rot=0):
    i = abs(hash(frase)) % 9999
    return (f'<svg viewBox="0 0 1000 1000" width="{t}" height="{t}" style="transform:rotate({rot}deg)"><defs><path id="t{i}" d="M500,500 m-440,0 a440,440 0 1,1 880,0 a440,440 0 1,1 -880,0"/></defs>'
            f'<text style="font:900 {tam}px Inter Tight;letter-spacing:.14em;fill:{cor}"><textPath href="#t{i}" textLength="2740">{frase}</textPath></text></svg>')

def pilula(t, bg, cor, tam=30, extra=''):
    return f'<div style="display:inline-block;background:{bg};color:{cor};font:800 {tam}px/1 Inter Tight;padding:{tam*.7:.0f}px {tam*1.1:.0f}px;border-radius:999px;white-space:nowrap;box-shadow:8px 10px 0 rgba(0,0,0,.25);{extra}">{t}</div>'

def etq(t, cor, tam=18, extra=''):
    return f'<div style="font:500 {tam}px/1 IBM Plex Mono;letter-spacing:.14em;text-transform:uppercase;color:{cor};white-space:nowrap;{extra}">{t}</div>'

def iphone(inner, w=440, h=900, bg='#fff', hora='19:42', claro=False):
    c = '#fff' if claro else '#111'
    return (f'<div style="width:{w}px;height:{h}px;border-radius:66px;background:#0b0b0a;padding:14px;box-shadow:26px 30px 0 rgba(0,0,0,.35),0 0 0 2px #3a3833 inset">'
            f'<div style="position:relative;width:100%;height:100%;border-radius:54px;overflow:hidden;background:{bg}">'
            f'<div style="position:absolute;left:50%;top:12px;transform:translateX(-50%);width:120px;height:34px;border-radius:20px;background:#0b0b0a;z-index:5"></div>'
            f'<div style="display:flex;justify-content:space-between;padding:20px 36px 0;font:600 17px Inter;color:{c}"><span>{hora}</span><span>●●● ▮</span></div>'
            f'{inner}</div></div>')

def balao(t, eu=False, hora='19:42', tam=20):
    cor = '#d9fdd3' if eu else '#fff'
    return (f'<div style="align-self:{"flex-end" if eu else "flex-start"};max-width:82%;background:{cor};border-radius:14px;padding:11px 14px 7px;'
            f'font:400 {tam}px/1.35 Inter;color:#111;box-shadow:0 1px 1px rgba(0,0,0,.15)">{t}<div style="text-align:right;font-size:12px;color:#667;margin-top:3px">{hora}{" ✓✓" if eu else ""}</div></div>')

def whats(msgs, nome='Cliente · Cohama', foto=None):
    topo = (f'<div style="background:#075e54;padding:16px 20px;display:flex;align-items:center;gap:12px;color:#fff;margin-top:8px">'
            f'<div style="width:46px;height:46px;border-radius:50%;background:{foto or "#9bb"} center/cover"></div>'
            f'<div><div style="font:700 19px Inter">{nome}</div><div style="font:400 14px Inter;opacity:.8">online</div></div></div>')
    return topo + f'<div style="display:flex;flex-direction:column;gap:10px;padding:18px 16px;background:#efe7dd;height:100%">{"".join(msgs)}</div>'

def S(id_, w, h, bg, inner):
    return f'<section class="f" id="{id_}" style="width:{w}px;height:{h}px;background:{bg}">{inner}<div class="a grao" style="inset:0"></div></section>'

CAL = lambda j: f'ing-calabresa-{j}'
AZ = lambda j: f'ing-azeitona-{j}'
P = []

# 01 · Palavra gigante atrás do produto (Rocco formato 4) · tomate
P.append(S('post-01-fila', 1080, 1350, TOMATE,
  txt(-30, 150, 'FILA', '400 640px/0.84 Anton', CREME, 'width:1140px;text-align:center;letter-spacing:-.015em;transform:scaleX(1.12)') +
  manchete(56, 60, 'Sua pizza merece', 76, CARVAO, -5, None, 'Bagel Fat One', 1, f'background:{ACAFRAO};padding:10px 28px 18px;border-radius:12px;box-shadow:12px 14px 0 rgba(0,0,0,.3)') +
  A(40, 420, texto_circular(1000, 'PEDIDO DIRETO NO SEU WHATSAPP ✦ TODO DIA DA SEMANA ✦ MARKETING DE VENDAS PARA PIZZARIAS ✦', CARVAO, 30, -18)) +
  img(R('pepperoni-cima'), 120, 520, 840, 10) +
  voando([(CAL(0), 40, 470, 150, -20, 0), (AZ(1), 930, 520, 80, 30, 2), (CAL(3), 900, 1120, 170, 25, 3), (AZ(2), 70, 1160, 70, 0, 0)]) +
  A(820, 380, selo(210, 'SÓ PIZZARIAS ✦ SÃO LUÍS ✦ MARANHÃO ✦ ', CREME, CARVAO, None, -12, CREME, 14)) +
  A(56, 1262, f'<div style="background:{CARVAO};padding:12px 22px;border-radius:14px">{logo(30)}</div>')))

# 02 · Interface ON com a pizza de bolinha (Pinterest "O nosso delivery está ON") · verde
P.append(S('post-02-delivery-on', 1080, 1350, VERDE,
  faixa_xadrez(0, 0, 1080, 90, CREME, VERDE_E, 45) + faixa_xadrez(0, 1260, 1080, 90, CREME, VERDE_E, 45) +
  manchete(60, 150, 'Terça. Seu<br>delivery está', 128, CREME, -3, VERDE_E, 'Bagel Fat One', .95) +
  A(-40, 520, f'<div style="position:relative;width:1160px;height:560px;border-radius:999px;background:{CREME};box-shadow:26px 30px 0 rgba(0,0,0,.35),inset 0 -18px 0 rgba(0,0,0,.1)">'
              f'<div style="position:absolute;left:120px;top:70px;font:400 400px/1 Bagel Fat One;color:{VERDE}">ON</div></div>') +
  img(R('pepperoni-cima'), 560, 470, 620, 15, .45) +
  voando([(AZ(0), 470, 470, 80, 20, 2), (CAL(1), 980, 1060, 130, 30, 3), (AZ(3), 520, 1100, 70, -10, 0)]) +
  A(60, 1120, pilula('Ou está OFF? →', ACAFRAO, CARVAO, 34)) +
  A(660, 1140, logo(30))))

# 03 · Produto voando com ingredientes (Rocco formato 1, Drip Riot / "AQUI NÃO TEM ERRO") · açafrão
P.append(S('post-03-terca-vazia', 1080, 1350, ACAFRAO,
  manchete(40, 90, 'TERÇA<br>VAZIA', 230, CARVAO, -4, TOMATE, 'Anton', .88) +
  img(R('pepperoni-fatia'), 500, 200, 540, 28, .45) +
  img(R('fatia-pepperoni-cima-1'), 640, 40, 260, -30, .4, 2) +
  img(R('fatia-calabresa-0'), -40, 560, 380, 16, .4) +
  img(R('fatia-pepperoni-cima-2'), 600, 700, 380, 52, .4) +
  img(R('fatia-calabresa-2'), 300, 640, 300, -38, .4, 3) +
  voando([(CAL(2), 940, 120, 120, 0, 3), (CAL(4), 900, 640, 140, 40, 0), (AZ(0), 420, 560, 70, 10, 2), (AZ(2), 120, 930, 80, 0, 0), (CAL(0), 560, 960, 110, -20, 4)]) +
  manchete(40, 1000, 'é dinheiro', 80, CARVAO, -4, None, 'Bagel Fat One', 1) +
  manchete(40, 1080, 'NO LIXO.', 230, TOMATE, -4, CARVAO, 'Anton', .9) +
  A(800, 1265, logo(26, CARVAO, VERDE, CREME, False))))

# 04 · Cartaz da paleta em faixas com o produto na frente (Rocco formato 8): "o cardápio da terça vazia"
faixas = [(TOMATE, CREME, 'ALUGUEL', 'paga igual'), (ACAFRAO, CARVAO, 'GÁS DO FORNO', 'paga igual'), (VERDE, CREME, 'EQUIPE PARADA', 'paga igual'),
          (CREME, CARVAO, 'MOTOBOY NA PORTA', 'paga igual'), (BRASA, CREME, 'MASSA QUE SOBROU', 'vai pro lixo')]
fx = ''.join(caixa(0, 230 + i * 190, 1080, 190, bg) + txt(60, 262 + i * 190, f'{t}<span style="font:400 40px Kaushan Script;margin-left:18px;opacity:.9">{s}</span>', '400 96px/1 Anton', c, 'white-space:nowrap')
             for i, (bg, c, t, s) in enumerate(faixas))
P.append(S('post-04-cardapio-terca', 1080, 1350, CARVAO,
  fx + caixa(0, 1180, 1080, 170, CARVAO) +
  manchete(60, 40, 'O cardápio da<br>terça vazia', 92, CREME, -2, None, 'Bagel Fat One', .98) +
  img(R('pizza-close'), 660, -170, 560, -14, .45) +
  A(870, 1160, selo(170, 'COM PEDIDO OU SEM PEDIDO ✦ ', CARVAO, ACAFRAO, f'<div style="font:400 40px/0.9 Bagel Fat One;color:{CARVAO}">A<br>conta<br>vem</div>', 10, CARVAO, 11.5)) +
  txt(60, 1205, 'Pizza boa não basta.<br><span style="color:' + ACAFRAO + '">Quem aparece mais, vende mais.</span>', '800 38px/1.12 Inter Tight', CREME, 'letter-spacing:-.02em') +
  A(560, 1290, logo(24, CREME, VERDE, CREME, False))))

# 05 · Produto fora do lugar (Rocco formato 9): Descartes com a fatia · tomate
P.append(S('post-05-penso-logo-peco', 1080, 1350, TOMATE,
  manchete(50, 95, 'PENSO, LOGO', 150, CREME, -3) +
  manchete(30, 250, 'PEÇO.', 430, ACAFRAO, -3, CARVAO) +
  img(R('descartes'), 270, 460, 900, 0, .45) +
  img(R('pepperoni-fatia'), 760, 960, 380, -58, .45) +
  voando([(CAL(3), 60, 700, 140, 20, 3), (AZ(1), 230, 660, 70, 0, 0)]) +
  A(50, 850, f'<div style="background:{CARVAO};color:{CREME};padding:30px 34px;border-radius:22px;width:400px;box-shadow:16px 18px 0 rgba(0,0,0,.3);transform:rotate(-2deg)">'
              f'<div style="font:800 44px/1.02 Inter Tight;letter-spacing:-.03em">O seu cliente também.</div>'
              f'<div style="font:600 27px/1.28 Inter;margin-top:14px;color:#ddd">Ele pede <b style="color:{ACAFRAO}">pra você</b> ou pra quem apareceu primeiro?</div></div>') +
  A(50, 1230, f'<div style="background:{CREME};padding:12px 20px;border-radius:14px">{logo(28, CARVAO)}</div>') +
  A(50, 1318, etq('Retrato: Frans Hals, c.1649 · domínio público', '#ffffffcc', 13))))

# 06 · Cartaz retrô com selo de oferta (Pinterest "Noite da Pizza") + pizza enorme vista de cima · creme com xadrez verde
P.append(S('post-06-fundadoras', 1080, 1350, CREME,
  caixa(0, 0, 1080, 1350, xadrez(VERDE, CREME, 36)) +
  caixa(46, 46, 988, 1258, CREME, 'border-radius:30px;box-shadow:0 0 0 8px ' + VERDE) +
  manchete(80, 80, 'VAGAS DE', 140, VERDE, -3, None, 'Bagel Fat One', .95) +
  manchete(70, 220, 'FUNDADORA', 150, TOMATE, -3, CARVAO, 'Bagel Fat One', .95) +
  img(R('calabresa'), 60, 420, 980, -8, .4) +
  voando([(AZ(0), 880, 420, 80, 20, 0), (CAL(1), 70, 980, 130, -15, 2)]) +
  A(700, 360, selo(300, 'SÓ PARA AS 5 PRIMEIRAS ✦ SÓ PARA AS 5 PRIMEIRAS ✦ ', CREME, TOMATE,
        f'<div style="font:400 66px/0.86 Bagel Fat One;color:{CREME}">SÓ<br>5</div><div style="font:800 15px Inter Tight;color:{CREME};letter-spacing:.1em">VAGAS</div>', 12, CREME, 12)) +
  A(80, 1130, f'<div style="background:{VERDE};color:{CREME};padding:22px 28px;border-radius:18px;width:520px;box-shadow:10px 12px 0 rgba(0,0,0,.25)">'
               f'<div style="font:800 34px/1.1 Inter Tight;letter-spacing:-.02em">Preço do plano anual<br>no prazo semestral.</div></div>') +
  A(650, 1150, pilula('Direct: FUNDADORA', ACAFRAO, CARVAO, 28)) +
  A(700, 1248, logo(22, CARVAO, VERDE, CREME, False))))

# 07 · Mão segurando a fatia contra a cor (Rocco formato 3, HOTWHIZ) + celular com o pedido · verde
chat = whats([
  balao('Boa noite! Vi vocês no Instagram 😍', hora='19:41'),
  balao('Quero 1 calabresa grande e 1 refri 2L', hora='19:41'),
  balao('Anotado 🍕 Pix ou cartão?', True, '19:42'),
  balao('Pix! Manda a chave', hora='19:42'),
  balao('Saindo em 35 min ✅', True, '19:43')], 'Juliana · Renascença', F('fotos-v4/queijo-puxando'))
P.append(S('post-07-menos-app-mais-zap', 1080, 1350, VERDE,
  manchete(50, 95, 'MENOS APP.', 180, CREME, -4, VERDE_E) +
  manchete(50, 260, 'MAIS ZAP.', 180, ACAFRAO, -4, VERDE_E) +
  A(600, 430, iphone(chat, 430, 800, '#efe7dd'), 'transform:rotate(8deg)') +
  A(610, 400, pilula('🔔 Novo pedido', TOMATE, '#fff', 30), 'transform:rotate(-5deg);z-index:3') +
  img(R('queijo-puxando'), -120, 560, 860, -8, .45) +
  A(50, 1150, f'<div style="background:{CARVAO};color:{CREME};padding:20px 26px;border-radius:16px;font:700 30px/1.2 Inter Tight;box-shadow:10px 12px 0 rgba(0,0,0,.3)">Pedido direto no seu WhatsApp.<br><span style="color:{ACAFRAO}">O cliente fica com você.</span></div>') +
  A(50, 1300, etq('Conversa ilustrativa', '#ffffffbb', 14)) + A(720, 1290, logo(24, CREME, CREME, VERDE, False))))

# 08 · Antes × depois do perfil, sem números · carvão | açafrão
def feed(fotos, filtro, bgc):
    g = ''.join(f'<div style="aspect-ratio:4/5;background:url({F(f)}) center/cover;filter:{filtro}"></div>' for f in fotos)
    return (f'<div style="padding:18px 18px 0;display:flex;align-items:center;gap:14px"><div style="width:70px;height:70px;border-radius:50%;background:{bgc}"></div>'
            f'<div style="font:700 20px Inter;color:#111">pizzaria_do_bairro</div></div>'
            f'<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:3px;margin-top:20px">{g}</div>')
antes = feed(['fotos-v3/bancada', 'fotos-v4/caixa-viagem', 'fotos-v3/caixas', 'fotos-v4/calabresa-porcoes', 'fotos-v3/bancada', 'fotos-v4/caixa-aberta', 'fotos-v3/caixas', 'fotos-v4/queijo-borda', 'fotos-v4/caixa-viagem', 'fotos-v3/bancada', 'fotos-v3/caixas', 'fotos-v4/caixa-aberta'],
             'brightness(.42) saturate(.3) contrast(.9) blur(.6px)', '#555')
depois = feed(['fotos-v4/queijo-puxando', 'fotos-v3/pa-no-forno', 'fotos-v4/pepperoni-fatia', 'fotos-v3/pizza-close', 'fotos-v4/pepperoni-cima', 'fotos-v3/brasa', 'fotos-v4/fatia-puxando', 'fotos-v4/calabresa', 'fotos-v3/forno-pizza', 'fotos-v4/pepperoni-inteira', 'fotos-v4/caixa-aberta', 'fotos-v4/queijo-borda'],
              'saturate(1.25) contrast(1.05)', TOMATE)
def rot(t, ok, cor):
    c = VERDE if ok else '#6d6a63'
    return f'<div style="display:flex;align-items:center;gap:12px;font:800 27px Inter Tight;color:{cor};margin-bottom:12px"><span style="width:38px;height:38px;border-radius:50%;background:{c};display:grid;place-items:center;font-size:22px;color:#fff">{"✓" if ok else "✕"}</span>{t}</div>'
P.append(S('post-08-antes-depois', 1080, 1350, CARVAO,
  caixa(540, 0, 540, 1350, ACAFRAO) +
  manchete(30, 95, 'O MESMO FORNO.', 118, CREME, -3) +
  txt(0, 210, 'OUTRO PERFIL.', '400 118px/0.9 Anton', CREME, 'width:1080px;text-align:center;clip-path:inset(0 50% 0 0);transform:rotate(-3deg)') +
  txt(0, 210, 'OUTRO PERFIL.', '400 118px/0.9 Anton', CARVAO, 'width:1080px;text-align:center;clip-path:inset(0 0 0 50%);transform:rotate(-3deg)') +
  A(40, 390, iphone(antes, 460, 700, '#e9e6e0'), 'transform:rotate(-5deg)') +
  A(580, 370, iphone(depois, 460, 700, '#fff'), 'transform:rotate(4deg)') +
  img(R('fatia-pepperoni-cima-0'), 820, 900, 300, 30, .4) +
  A(455, 640, f'<div style="width:170px;height:170px;border-radius:50%;background:{TOMATE};display:grid;place-items:center;font:400 66px Bagel Fat One;color:{CREME};box-shadow:12px 14px 0 rgba(0,0,0,.35);transform:rotate(-8deg)">VS</div>') +
  A(50, 1110, rot('Foto escura', False, '#cfcac0') + rot('Só promoção', False, '#cfcac0') + rot('Sem link de pedido', False, '#cfcac0')) +
  A(590, 1110, rot('Foto que dá fome', True, CARVAO) + rot('Forno e bastidor', True, CARVAO) + rot('Link de pedido', True, CARVAO)) +
  A(50, 1300, logo(22, CREME, VERDE, CREME, False)) + A(590, 1306, etq('Simulação · sem números', CARVAO, 14))))

# 09 · Relatório de segunda em close (Owner.com) + fatia enorme · açafrão
dias = [('S', 34), ('T', 22), ('Q', 30), ('Q', 41), ('S', 72), ('S', 96), ('D', 88)]
barras = ''.join(f'<div style="display:flex;flex-direction:column;align-items:center;gap:8px;flex:1"><div style="width:100%;height:{v*2.5:.0f}px;border-radius:10px 10px 4px 4px;background:{TOMATE if i == 1 else VERDE}"></div><span style="font:600 19px IBM Plex Mono;color:#6b665d">{d}</span></div>' for i, (d, v) in enumerate(dias))
rel = (f'<div style="width:720px;background:#fff;border-radius:30px;padding:40px 42px;box-shadow:28px 32px 0 rgba(0,0,0,.3)">'
       f'<div style="display:flex;justify-content:space-between;align-items:center">{etq("Relatório da semana · exemplo ilustrativo", "#6b665d", 16)}{simbolo(44)}</div>'
       f'<div style="font:800 40px/1.1 Inter Tight;color:{CARVAO};margin:14px 0 22px;letter-spacing:-.02em">Pizzaria do bairro · 28/10 a 03/11</div>'
       f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:26px">'
       f'<div style="background:{CREME};border-radius:16px;padding:18px 22px"><div style="font:500 19px Inter;color:#6b665d">Pedidos no WhatsApp</div><div style="font:800 66px/1.1 Inter Tight;color:{CARVAO}">142</div></div>'
       f'<div style="background:{CREME};border-radius:16px;padding:18px 22px"><div style="font:500 19px Inter;color:#6b665d">Custo de cada pedido</div><div style="font:800 66px/1.1 Inter Tight;color:{VERDE}">R$ 4,10</div></div></div>'
       f'<div style="display:flex;gap:12px;align-items:flex-end;height:260px">{barras}</div>'
       f'<div style="margin-top:22px;background:#fdebe5;border-radius:14px;padding:16px 18px;font:600 22px/1.35 Inter;color:#A8361A">Terça foi o dia mais fraco. Ação: combo de terça no anúncio do bairro.</div></div>')
P.append(S('post-09-segunda-8h', 1080, 1350, ACAFRAO,
  manchete(40, 95, 'SEGUNDA, 8H.', 185, CARVAO, -3, CREME) +
  A(120, 380, rel, 'transform:rotate(-4deg)') +
  img(R('pepperoni-fatia'), 760, 860, 380, -30, .45) +
  A(820, 300, selo(200, 'TODA SEGUNDA ✦ NÚMERO NA MESA ✦ ', CREME, VERDE, f'<div style="font:400 50px/0.9 Bagel Fat One;color:{ACAFRAO}">8H</div>', -12, ACAFRAO, 12)) +
  A(40, 1262, f'<div style="background:{CARVAO};padding:12px 22px;border-radius:14px">{logo(28)}</div>') +
  A(420, 1300, etq('Exemplo ilustrativo · não é promessa de resultado', CARVAO, 14))))

# 10 · Grade de 4 cores com a mesma manchete e a comida (Rocco formato 5, McDonald's "Here for the sauce")
q = [(TOMATE, CREME, 'QUANTOS', 'pepperoni-fatia', 430, -25), (ACAFRAO, CARVAO, 'PEDIDOS', 'fatia-pepperoni-cima-1', 400, 20),
     (VERDE, CREME, 'NA', 'calabresa', 520, -10), (CREME, TOMATE, 'TERÇA?', 'fatia-calabresa-2', 420, 35)]
grade = ''
for i, (bg, c, t, p, w, r) in enumerate(q):
    x, y = (i % 2) * 540, (i // 2) * 675
    grade += caixa(x, y, 540, 675, bg) + img(R(p), x + 540 - w * .82, y + 675 - w * .78, w, r, .42)
    grade += txt(x + 34, y + (60 if i < 2 else 190), t, f'400 {130 if len(t) > 6 else 160 if len(t) > 3 else 230}px/0.9 Anton', c, 'transform:rotate(-4deg);transform-origin:left top')
P.append(S('post-10-quantos-pedidos', 1080, 1350, CARVAO,
  grade +
  A(410, 545, selo(260, 'TERÇA PASSADA ✦ RESPONDE AQUI ✦ ', CREME, CARVAO,
        f'<div style="font:400 30px/1 Bagel Fat One;color:{ACAFRAO}">Quantos<br>pedidos?</div>', -8, ACAFRAO, 14)) +
  A(40, 1280, f'<div style="background:{CARVAO};padding:10px 18px;border-radius:12px">{logo(24, CREME, VERDE, CREME, False)}</div>')))

# 11 · Pizza vista de cima com setas e notas (Pinterest "Anatomía de una buena pizza") · verde
def passo(n, t, d):
    return (f'<div style="display:flex;gap:14px;align-items:flex-start;width:340px"><div style="flex:none;width:68px;height:68px;border-radius:50%;background:{ACAFRAO};display:grid;place-items:center;font:400 42px Bagel Fat One;color:{CARVAO};box-shadow:6px 7px 0 rgba(0,0,0,.3)">{n}</div>'
            f'<div><div style="font:800 34px/1.02 Inter Tight;color:{CREME};letter-spacing:-.02em">{t}</div><div style="font:500 22px/1.28 Inter;color:#d8eadf;margin-top:6px">{d}</div></div></div>')
seta = lambda d: f'<svg width="150" height="90" viewBox="0 0 150 90" style="overflow:visible"><path d="{d}" fill="none" stroke="{ACAFRAO}" stroke-width="5" stroke-linecap="round" stroke-dasharray="2 11"/></svg>'
P.append(S('post-11-4-passos', 1080, 1350, VERDE,
  manchete(40, 90, '4 PASSOS.', 160, CREME, -3, VERDE_E) +
  manchete(700, 70, 'Toda<br>semana.', 74, ACAFRAO, -6, None, 'Bagel Fat One', .95) +
  img(R('pepperoni-cima'), 170, 400, 740, 0, .45) +
  A(170, 400, '<svg width="740" height="728" viewBox="0 0 460 452"><line x1="230" y1="-6" x2="230" y2="458" stroke="' + CREME + '" stroke-width="4"/><line x1="-6" y1="226" x2="466" y2="226" stroke="' + CREME + '" stroke-width="4"/></svg>') +
  A(30, 300, passo(1, 'Raio-X', 'O que trava o seu pedido.')) +
  A(720, 300, passo(2, 'Anúncio no bairro', 'Sua pizza na hora da fome.')) +
  A(30, 1110, passo(3, 'Pedido no Zap', 'Direto, sem app no meio.')) +
  A(720, 1110, passo(4, 'Número na segunda', 'Quanto entrou e o que muda.')) +
  voando([(AZ(2), 960, 600, 80, 0, 2), (CAL(4), -30, 700, 150, 20, 3)]) +
  A(400, 1290, logo(22, CREME, CREME, VERDE, False))))

# 12 · Raio-X: produto enorme meio foto, meio raio-x + preço · carvão
P.append(S('post-12-raio-x', 1080, 1350, CARVAO,
  A(240, 250, f'<div style="position:relative;width:960px;height:946px">'
              f'<img src="{R("pepperoni-cima")}" style="position:absolute;inset:0;width:960px;filter:{flash(960, .6)}">'
              f'<img src="{R("pepperoni-cima")}" style="position:absolute;inset:0;width:960px;filter:grayscale(1) invert(1) sepia(1) hue-rotate(150deg) saturate(3) brightness(.95) contrast(1.4);clip-path:inset(0 0 0 50%)">'
              f'<div style="position:absolute;left:476px;top:-40px;width:9px;height:1030px;background:#7ff3ff;box-shadow:0 0 34px 12px #39d5ff99"></div></div>') +
  manchete(40, 110, 'RAIO-X', 270, CREME, -3, TOMATE) +
  manchete(56, 380, 'da sua pizzaria', 76, ACAFRAO, -6, None, 'Kaushan Script', 1) +
  A(50, 520, ''.join(f'<div style="font:800 32px/1 Inter Tight;color:{CREME};margin-bottom:22px;display:flex;gap:14px;align-items:center"><span style="width:16px;height:16px;background:#7ff3ff;border-radius:50%;box-shadow:0 0 14px #7ff3ff"></span>{t}</div>' for t in ['Instagram', 'Cardápio e iFood', 'Anúncio', 'WhatsApp'])) +
  A(40, 960, f'<div style="background:{TOMATE};border-radius:26px;padding:28px 34px;width:520px;box-shadow:16px 18px 0 rgba(0,0,0,.45);transform:rotate(-3deg)">'
              f'<div style="font:400 130px/0.9 Bagel Fat One;color:{CREME}">R$ 297</div>'
              f'<div style="font:700 25px/1.3 Inter Tight;color:{CREME};margin-top:10px">Abatido no 1º mês se fechar<br>com a gente em até 7 dias.</div></div>') +
  A(600, 1250, pilula('Manda RAIO-X no direct', ACAFRAO, CARVAO, 28)) +
  A(40, 1276, logo(26))))

# ───────────── CARROSSEL ─────────────
def tag_erro(n, bg, cor):
    return f'<div style="display:inline-flex;align-items:center;gap:12px;background:{bg};color:{cor};font:400 36px Bagel Fat One;padding:12px 28px;border-radius:999px;box-shadow:8px 10px 0 rgba(0,0,0,.25);transform:rotate(-3deg)">ERRO {n}<span style="font:600 22px IBM Plex Mono;opacity:.7">/5</span></div>'
def rodape_c(n, cor=CREME, folha=VERDE, seta=CREME):
    return A(50, 1282, logo(24, cor, folha, seta, False)) + A(900, 1290, etq(f'{n}/7 →', cor, 20))

C = []
C.append(S('carrossel-1-capa', 1080, 1350, TOMATE,
  txt(-10, 120, '5', '400 1180px/0.8 Anton', ACAFRAO, 'text-shadow:30px 30px 0 rgba(0,0,0,.25)') +
  img(R('pepperoni-fatia'), 360, 300, 640, 28, .45) +
  voando([(CAL(0), 820, 220, 160, 20, 0), (AZ(1), 300, 260, 80, 0, 2), (CAL(2), 900, 940, 150, -20, 3)]) +
  manchete(40, 100, 'ERROS', 190, CREME, -4, CARVAO) +
  A(40, 1010, f'<div style="background:{CARVAO};color:{CREME};padding:24px 30px;border-radius:20px;font:800 54px/1.1 Inter Tight;letter-spacing:-.03em;box-shadow:14px 16px 0 rgba(0,0,0,.3);transform:rotate(-2deg)">que deixam a sua pizzaria<br><span style="color:{ACAFRAO}">sem pedido na terça</span></div>') +
  A(780, 70, pilula('Arrasta →', ACAFRAO, CARVAO, 28)) + rodape_c(1)))

C.append(S('carrossel-2-foto-escura', 1080, 1350, CREME,
  txt(560, -70, '01', '400 660px/1 Anton', '#e6dccb') +
  A(50, 50, tag_erro(1, CARVAO, CREME)) +
  manchete(50, 180, 'Foto escura.', 160, CARVAO, -3, ACAFRAO) +
  A(40, 450, f'<div style="width:480px;height:600px;border-radius:24px;background:url({F("fotos-v4/caixa-aberta")}) center/cover;filter:brightness(.4) saturate(.3);box-shadow:20px 24px 0 rgba(0,0,0,.3)"></div>', 'transform:rotate(-4deg)') +
  A(560, 420, f'<div style="width:480px;height:640px;border-radius:24px;background:url({F("fotos-v4/queijo-puxando")}) center/cover;filter:saturate(1.3) contrast(1.05);box-shadow:20px 24px 0 rgba(0,0,0,.3)"></div>', 'transform:rotate(3deg)') +
  A(80, 480, pilula('✕ tira a fome', '#5e5a53', CREME, 26)) + A(600, 450, pilula('✓ dá fome', VERDE, CREME, 26)) +
  txt(50, 1110, 'O cliente decide com os olhos, em 2 segundos. Luz de janela, close no queijo, fundo limpo.', '700 32px/1.3 Inter', CARVAO, 'width:980px') +
  rodape_c(2, CARVAO, VERDE, CREME)))

promo = ''.join(f'<div style="font:400 150px/0.92 Anton;color:{CREME};opacity:{.1 + i*.03:.2f};white-space:nowrap">PROMOÇÃO PROMOÇÃO</div>' for i in range(9))
C.append(S('carrossel-3-so-promocao', 1080, 1350, BRASA,
  A(-60, 0, promo) +
  A(50, 50, tag_erro(2, CARVAO, CREME)) +
  A(60, 280, f'<div style="width:960px;background:{CARVAO};border-radius:30px;padding:52px 56px;box-shadow:24px 28px 0 rgba(0,0,0,.35);transform:rotate(-2deg)">'
             f'<div style="font:400 130px/0.9 Anton;color:{CREME}">Só posta<br><span style="color:{ACAFRAO}">promoção.</span></div>'
             f'<div style="font:500 34px/1.35 Inter;color:#ddd;margin-top:28px;width:560px">O cliente aprende a esperar o desconto. Mostre o forno, a massa, quem faz e o pedido saindo.</div></div>') +
  img(R('fatia-pepperoni-cima-1'), 600, 700, 520, 22, .45) +
  voando([(CAL(1), 120, 1000, 150, 0, 3), (AZ(3), 520, 1120, 80, 20, 0)]) +
  rodape_c(3)))

bio = (f'<div style="padding:30px 26px 0"><div style="display:flex;align-items:center;gap:20px"><div style="width:110px;height:110px;border-radius:50%;background:url({F("fotos-v4/pepperoni-cima")}) center/cover;border:4px solid {TOMATE}"></div>'
       f'<div style="display:flex;gap:22px;font:700 20px Inter;color:#111;text-align:center"><div>212<br><span style="font-weight:400;font-size:15px">posts</span></div><div>3,1 mil<br><span style="font-weight:400;font-size:15px">seguidores</span></div></div></div>'
       f'<div style="font:700 20px Inter;margin-top:18px;color:#111">Pizzaria do Bairro</div><div style="font:400 18px/1.4 Inter;color:#111">🍕 A melhor pizza da região<br>📍 São Luís · MA<br>🛵 Delivery todos os dias</div>'
       f'<div style="position:relative;margin-top:10px;height:44px"><div style="position:absolute;left:-22px;top:-14px;width:290px;height:70px;border:5px solid {TOMATE};border-radius:50%;transform:rotate(-4deg)"></div>'
       f'<span style="font:400 18px Inter;color:#aaa">(nenhum link)</span></div>'
       f'<div style="display:flex;gap:8px;margin-top:16px"><div style="flex:1;background:#efefef;border-radius:10px;padding:12px;text-align:center;font:600 16px Inter">Seguir</div><div style="flex:1;background:#efefef;border-radius:10px;padding:12px;text-align:center;font:600 16px Inter">Mensagem</div></div>'
       f'<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:3px;margin:22px -26px 0">' + ''.join(f'<div style="aspect-ratio:1;background:url({F(x)}) center/cover"></div>' for x in ['fotos-v4/calabresa', 'fotos-v3/pizza-close', 'fotos-v4/queijo-borda', 'fotos-v4/pepperoni-inteira', 'fotos-v3/forno-pizza', 'fotos-v4/caixa-aberta', 'fotos-v4/pepperoni-fatia', 'fotos-v3/brasa', 'fotos-v4/queijo-puxando', 'fotos-v4/pepperoni-cima', 'fotos-v3/pa-no-forno', 'fotos-v4/caixa-viagem']) + '</div></div>')
C.append(S('carrossel-4-sem-link', 1080, 1350, VERDE,
  A(40, 160, iphone(bio, 500, 1020, '#fff'), 'transform:rotate(-6deg)') +
  A(220, 560, f'<div style="font:400 56px/1 Kaushan Script;color:{ACAFRAO};background:{CARVAO};padding:8px 26px 14px;border-radius:14px;transform:rotate(-8deg);box-shadow:12px 14px 0 rgba(0,0,0,.35)">cadê o link?</div>') +
  A(590, 50, tag_erro(3, CREME, VERDE)) +
  manchete(590, 190, 'Bio<br>sem<br>link.', 170, CREME, -3, VERDE_E) +
  txt(590, 720, 'Com fome, ninguém procura o seu número. Link direto pro WhatsApp ou cardápio, em cima de tudo.', '700 32px/1.3 Inter', '#e6f1ea', 'width:450px') +
  img(R('fatia-calabresa-1'), 700, 1000, 340, 20, .45) +
  rodape_c(4)))

chat2 = whats([balao('Boa noite, ainda tá entregando?', hora='19:42'),
               f'<div style="align-self:center;background:#e1f3fb;border-radius:8px;padding:6px 12px;font:600 14px Inter;color:#556">1 hora depois</div>',
               balao('Boa noite! Sim, o que vai querer?', True, '20:51'),
               balao('Já pedi em outro lugar 😕', hora='20:52')], 'Rafael · Cohama')
C.append(S('carrossel-5-demora', 1080, 1350, CARVAO,
  A(50, 50, tag_erro(4, TOMATE, CREME)) +
  manchete(50, 180, 'Respondeu<br><span style="color:' + TOMATE + '">1 hora</span> depois.', 150, CREME, -3) +
  A(560, 470, iphone(chat2, 480, 760, '#efe7dd'), 'transform:rotate(6deg)') +
  manchete(50, 560, '69 min', 170, ACAFRAO, -4, TOMATE, 'Bagel Fat One', 1) +
  manchete(56, 760, 'esperando resposta', 52, CREME, -4, None, 'Kaushan Script', 1) +
  txt(50, 880, 'Fome não espera. Quem responde primeiro leva o pedido. Resposta pronta salva a noite.', '700 32px/1.3 Inter', '#ddd', 'width:470px') +
  img(R('pepperoni-fatia'), 280, 1040, 240, -60, .5) +
  A(50, 1240, etq('Conversa ilustrativa', '#8a857c', 15)) +
  rodape_c(5)))

sem = [('SEG', 18), ('TER', 10), ('QUA', 16), ('QUI', 34), ('SEX', 80), ('SÁB', 100), ('DOM', 92)]
cal = ''.join(f'<div style="flex:1;display:flex;flex-direction:column;align-items:center;justify-content:flex-end;gap:12px;height:690px">'
              f'<div style="width:100%;height:{v*5.4:.0f}px;border-radius:18px;background:{TOMATE if v > 50 else "#e2d4b8"};position:relative;overflow:visible;box-shadow:8px 10px 0 rgba(0,0,0,.18)">'
              + (f'<img src="{R("fatia-pepperoni-cima-0")}" style="position:absolute;left:50%;top:-60px;width:150px;transform:translateX(-50%) rotate(20deg);filter:{flash(150)}">' if v > 50 else '') +
              f'</div><span style="font:400 32px Bagel Fat One;color:{CARVAO if v > 50 else "#9a8f78"}">{d}</span></div>' for d, v in sem)
C.append(S('carrossel-6-so-sabado', 1080, 1350, ACAFRAO,
  A(50, 50, tag_erro(5, CARVAO, ACAFRAO)) +
  manchete(50, 170, 'Só aparece<br>no sábado.', 130, CARVAO, -3, CREME) +
  A(50, 420, f'<div style="display:flex;gap:14px;width:980px">{cal}</div>') +
  txt(50, 1170, 'Quem posta e anuncia só na sexta some da cabeça do cliente na terça.', '800 34px/1.2 Inter Tight', CARVAO, 'width:900px;letter-spacing:-.01em') +
  A(760, 1250, etq('Movimento ilustrativo', CARVAO, 14)) +
  rodape_c(6, CARVAO, VERDE, CREME)))

C.append(S('carrossel-7-chamada', 1080, 1350, TOMATE,
  img(R('calabresa'), 300, 520, 1000, 12, .45) +
  voando([(AZ(0), 260, 520, 90, 0, 2), (CAL(3), 160, 1180, 160, -20, 3)]) +
  manchete(40, 110, 'Quantos erros<br>a sua tem?', 120, CREME, -4, CARVAO, 'Bagel Fat One', .95) +
  manchete(56, 410, 'O Raio-X mostra.', 70, ACAFRAO, -5, None, 'Kaushan Script', 1) +
  A(40, 640, f'<div style="background:{CARVAO};border-radius:24px;padding:28px 32px;width:440px;box-shadow:16px 18px 0 rgba(0,0,0,.35);transform:rotate(-3deg)">'
             f'<div style="font:400 100px/0.9 Bagel Fat One;color:{ACAFRAO}">R$ 297</div>'
             f'<div style="font:600 24px/1.35 Inter;color:{CREME};margin-top:12px">Abatido no 1º mês se fechar em até 7 dias.</div>'
             f'<div style="margin-top:20px">{pilula("Manda RAIO-X no direct", TOMATE, "#fff", 24)}</div></div>') +
  rodape_c(7)))

# ───────────── STORIES ─────────────
ST = []
ST.append(S('story-1-enquete', 1080, 1920, TOMATE,
  faixa_xadrez(0, 0, 1080, 90, CREME, TOMATE, 45) +
  A(50, 160, logo(30)) +
  manchete(50, 320, 'A sua<br>terça é…', 190, CREME, -4, CARVAO, 'Bagel Fat One', .92) +
  img(R('pepperoni-cima'), 100, 640, 960, 10, .45) +
  voando([(CAL(0), 40, 640, 160, -20, 0), (AZ(1), 900, 700, 90, 20, 2), (CAL(4), 880, 1280, 170, 30, 3)]) +
  A(140, 1390, f'<div style="width:800px;background:#fff;border-radius:34px;padding:30px;box-shadow:20px 24px 0 rgba(0,0,0,.3)">'
               f'<div style="font:800 30px Inter Tight;color:#111;text-align:center;margin-bottom:20px">Responda com sinceridade 👇</div>'
               f'<div style="background:#f2f2f2;border-radius:18px;padding:24px;text-align:center;font:800 42px Inter Tight;color:{VERDE};margin-bottom:14px">🔥 FORNO CHEIO</div>'
               f'<div style="background:#f2f2f2;border-radius:18px;padding:24px;text-align:center;font:800 42px Inter Tight;color:{TOMATE}">😴 FORNO PARADO</div></div>') +
  A(0, 1760, etq('Figurinha de ENQUETE em cima do cartão', '#ffffffcc', 16), 'width:1080px;text-align:center')))

caixinha = (f'<div style="width:820px;border-radius:34px;overflow:hidden;box-shadow:20px 24px 0 rgba(0,0,0,.3)">'
            f'<div style="background:{TOMATE};padding:34px 30px;text-align:center;font:800 40px/1.15 Inter Tight;color:#fff">Qual a sua maior dúvida pra vender mais pizza?</div>'
            f'<div style="background:#fff;padding:36px;text-align:center;font:500 30px Inter;color:#999">Escreva aqui…</div></div>')
ST.append(S('story-2-caixinha', 1080, 1920, VERDE,
  img(R('queijo-puxando'), 120, 820, 980, -6, .45) +
  A(50, 160, logo(30)) +
  manchete(50, 320, 'ME<br>PERGUNTA', 220, CREME, -4, VERDE_E) +
  manchete(56, 730, 'sobre vender mais pizza', 64, ACAFRAO, -5, None, 'Kaushan Script', 1) +
  A(130, 1320, caixinha) +
  voando([(CAL(1), 40, 860, 170, 20, 0), (AZ(2), 900, 760, 90, 0, 2)]) +
  txt(0, 1680, 'Anúncio, Instagram, iFood, WhatsApp.<br>Respondo as melhores aqui.', '700 34px/1.3 Inter', CREME, 'width:1080px;text-align:center') +
  A(0, 1820, etq('Figurinha de PERGUNTAS em cima do cartão', '#ffffffcc', 16), 'width:1080px;text-align:center')))

ST.append(S('story-3-raio-x', 1080, 1920, CARVAO,
  A(50, 160, logo(30)) +
  manchete(50, 300, 'Passa no', 110, CREME, -4, None, 'Bagel Fat One', 1) +
  manchete(40, 420, 'RAIO-X?', 310, CREME, -4, TOMATE) +
  A(60, 720, f'<div style="position:relative;width:960px;height:946px">'
              f'<img src="{R("pepperoni-cima")}" style="position:absolute;inset:0;width:960px;filter:{flash(960, .6)}">'
              f'<img src="{R("pepperoni-cima")}" style="position:absolute;inset:0;width:960px;filter:grayscale(1) invert(1) sepia(1) hue-rotate(150deg) saturate(3) brightness(.95) contrast(1.4);clip-path:inset(50% 0 0 0)">'
              f'<div style="position:absolute;left:-40px;top:468px;width:1040px;height:9px;background:#7ff3ff;box-shadow:0 0 34px 12px #39d5ff99"></div></div>') +
  A(140, 1470, f'<div style="width:800px;background:{TOMATE};border-radius:30px;padding:28px;text-align:center;box-shadow:18px 20px 0 rgba(0,0,0,.45);transform:rotate(-2deg)">'
               f'<div style="font:400 120px/0.9 Bagel Fat One;color:{CREME}">R$ 297</div>'
               f'<div style="font:700 26px/1.3 Inter Tight;color:{CREME};margin-top:10px">Abatido no 1º mês se fechar em até 7 dias</div></div>') +
  A(0, 1730, f'<div style="width:1080px;text-align:center">{pilula("Responde este story com RAIO-X", ACAFRAO, CARVAO, 32)}</div>')))

CSS = ('*{margin:0;padding:0;box-sizing:border-box}body{background:#777;display:flex;flex-wrap:wrap;gap:40px;padding:40px}'
       '.f{position:relative;overflow:hidden;flex:none}.a{position:absolute}img.a{display:block;height:auto}'
       '.grao{pointer-events:none;mix-blend-mode:overlay;opacity:.14;background:url("data:image/svg+xml;utf8,'
       '<svg xmlns=%27http://www.w3.org/2000/svg%27 width=%27300%27 height=%27300%27><filter id=%27n%27><feTurbulence type=%27fractalNoise%27 baseFrequency=%27.9%27 numOctaves=%272%27/></filter>'
       '<rect width=%27100%25%27 height=%27100%25%27 filter=%27url(%23n)%27/></svg>")}')
FONTES = ('<link href="https://fonts.googleapis.com/css2?family=Anton&family=Bagel+Fat+One&family=IBM+Plex+Mono:wght@500;600'
          '&family=Inter:wght@400;500;600;700&family=Inter+Tight:wght@500;700;800;900&family=Kaushan+Script&display=block" rel="stylesheet">')
html = f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">{FONTES}<style>{CSS}</style></head><body>{"".join(P + C + ST)}</body></html>'
import os
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pecas.html'), 'w').write(html)
print(len(P), 'posts,', len(C), 'telas de carrossel,', len(ST), 'stories')
