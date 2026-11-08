# Artes TIPOGRÁFICAS das semanas 3 e 4 (dias 15 a 28, 23/11 a 06/12/2026) do @oreganoturbo · Paollo · conta Leandro · 06/11/2026
# Base: kit v3 aprovado ("AGORA SIM, ESSE É O PADRÃO"), ../../../v3/gerar.py. As funções de marca de lá (símbolo, logo, selo,
# padrão de ícones, xadrez, adesivo, estrela, faixa em loop, tarja) são CARREGADAS daquele arquivo, não copiadas.
# Regra do Lindson (06/11): cada foto só uma vez e as fotos acabaram → estas peças NÃO usam foto. O impacto vem do sistema
# da marca: manchete gorda gigante, cor chapada, xadrez, selos girados, estrela, adesivos, faixas, celular/relógio/cardápio desenhados.
# Uso: python3 gerar_s34.py && node render.js && python3 previa.py
import os, re, math
D = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(D, '..', 'sistema_v4.py'), encoding='utf-8').read())   # sistema v4 (08/11, conta Zuleide): lê ../../../v4/gerar.py
D = os.path.dirname(os.path.abspath(__file__))
FONTS = FONTS.replace('&family=Inter:', '&family=Kaushan+Script&family=Inter:')
BRANCO, ZAPV, ZAPB = '#FFFFFF', '#008069', '#D9FDD3'

# ------------------------------------------------------------------ peças novas do sistema (desenhadas em HTML/SVG)
FIT = lambda html, w, extra='': f'<div data-w="{w}" style="width:{w}px;{extra}">{html}</div>'   # encolhe a letra até caber em w
KAU = lambda t, s, cor, extra='': BAGEL(t, s * .72, cor, 1, extra)   # v4: manuscrito saiu, Bagel em toda manchete
FUNDO = lambda bg, cor, op=.12, t=300: BOX(0, 0, 1080, 2000, bg) + f'<div class="a" style="inset:0;background:{padrao(cor, op, t)}"></div>'

def celular(w, h, tela, rot=0, sombra='22px 26px 0 6px rgba(20,19,17,.38)'):
    r = w * .13
    return (f'<div style="position:relative;width:{w}px;height:{h}px;border-radius:{r:.0f}px;background:{CARVAO};padding:{w * .032:.0f}px;'
            f'box-shadow:0 0 0 7px {CREME},{sombra};transform:rotate({rot}deg)">'
            f'<div style="position:relative;width:100%;height:100%;border-radius:{r * .78:.0f}px;overflow:hidden;background:#EFE7DE">{tela}'
            f'<div style="position:absolute;left:50%;top:14px;width:{w * .3:.0f}px;height:{w * .06:.0f}px;margin-left:-{w * .15:.0f}px;border-radius:99px;background:{CARVAO}"></div>'
            f'</div></div>')

def wa_tela(nome, sub, corpo, fs=1.0, inicial=None):
    inicial = inicial or nome[0]
    return (f'<div style="position:absolute;inset:0;background:#EFE7DE {padrao(CARVAO, .07, 240)}"></div>'
            f'<div style="position:absolute;left:0;top:0;right:0;height:{150 * fs:.0f}px;background:{ZAPV};display:flex;align-items:flex-end;gap:{16 * fs:.0f}px;padding:0 {24 * fs:.0f}px {18 * fs:.0f}px">'
            f'<span style="font:600 {38 * fs:.0f}px Inter;color:#fff">‹</span>'
            f'<span style="width:{66 * fs:.0f}px;height:{66 * fs:.0f}px;border-radius:50%;background:{ACAFRAO};display:grid;place-items:center;font:800 {32 * fs:.0f}px \'Inter Tight\';color:{CARVAO}">{inicial}</span>'
            f'<span><div style="font:700 {32 * fs:.0f}px/1.1 Inter;color:#fff">{nome}</div><div style="font:500 {20 * fs:.0f}px/1.3 Inter;color:#D7F0E8">{sub}</div></span></div>'
            f'<div style="position:absolute;left:0;right:0;top:{170 * fs:.0f}px;padding:0 {22 * fs:.0f}px;display:flex;flex-direction:column;gap:{16 * fs:.0f}px">{corpo}</div>')

def bolha(t, eu, hora, fs=30, maxw=80, sombra='0 2px 0 rgba(0,0,0,.12)'):
    return (f'<div style="align-self:{"flex-end" if eu else "flex-start"};max-width:{maxw}%;background:{ZAPB if eu else BRANCO};'
            f'border-radius:{fs * .8:.0f}px;{"border-top-right-radius:6px" if eu else "border-top-left-radius:6px"};padding:{fs * .55:.0f}px {fs * .75:.0f}px {fs * .35:.0f}px;box-shadow:{sombra}">'
            f'<div style="font:500 {fs}px/1.32 Inter;color:{CARVAO}">{t}</div>'
            f'<div style="font:500 {fs * .55:.0f}px Inter;color:#667781;text-align:right;margin-top:4px">{hora}{" <span style=color:#53BDEB>✓✓</span>" if eu else ""}</div></div>')

chip = lambda t, fs=22: (f'<div style="align-self:center;background:#fff;color:#54656F;font:600 {fs}px Inter;padding:{fs * .4:.0f}px {fs * .9:.0f}px;'
                         f'border-radius:12px;box-shadow:0 2px 0 rgba(0,0,0,.08);text-transform:uppercase;letter-spacing:.04em">{t}</div>')
marca = lambda t: f'<span style="background:{ACAFRAO};padding:0 6px;border-radius:6px;font-weight:700">{t}</span>'

def enquete(perg, ops, w=900, fs=40, rot=0, marca_i=None):
    o = ''.join(f'<div style="display:flex;justify-content:space-between;align-items:center;border:3px solid #E4E1DB;border-radius:22px;padding:{fs * .5:.0f}px 28px;margin-top:14px;'
                f'font:700 {fs * .85:.0f}px Inter;color:{CARVAO}"><span>{d}</span><span style="width:36px;height:36px;border-radius:50%;border:3px solid {VERDE}"></span></div>'
                for d in ops)
    return (f'<div style="width:{w}px;background:#fff;border-radius:36px;padding:36px;box-shadow:0 0 0 8px {CREME},18px 20px 0 8px rgba(20,19,17,.35);transform:rotate({rot}deg)">'
            f'<div style="font:800 {fs}px/1.12 \'Inter Tight\';color:{CARVAO};text-align:center;margin-bottom:20px;letter-spacing:-.02em">{perg}</div>{o}</div>')

def relogio(tam, aro=TOMATE, face=CREME, ponteiro=CARVAO, hh=10, mm=10):
    tk = ''.join(f'<line x1="{100 + 58 * math.sin(math.radians(a)):.1f}" y1="{122 - 58 * math.cos(math.radians(a)):.1f}" x2="{100 + (48 if a % 90 else 42) * math.sin(math.radians(a)):.1f}" '
                 f'y2="{122 - (48 if a % 90 else 42) * math.cos(math.radians(a)):.1f}" stroke="{ponteiro}" stroke-width="{6 if a % 90 == 0 else 3}" stroke-linecap="round"/>' for a in range(0, 360, 30))
    ah, am = math.radians((hh % 12) * 30 + mm * .5), math.radians(mm * 6)
    return (f'<svg viewBox="0 0 200 230" width="{tam}" height="{tam * 1.15:.0f}" style="display:block;overflow:visible;filter:drop-shadow(16px 18px 0 rgba(20,19,17,.3))">'
            f'<path d="M30 70 A36 36 0 0 1 80 26 Z" fill="{aro}" stroke="{CARVAO}" stroke-width="5" stroke-linejoin="round"/>'
            f'<path d="M170 70 A36 36 0 0 0 120 26 Z" fill="{aro}" stroke="{CARVAO}" stroke-width="5" stroke-linejoin="round"/>'
            f'<path d="M48 196 L34 222 M152 196 L166 222" stroke="{CARVAO}" stroke-width="9" stroke-linecap="round"/>'
            f'<circle cx="100" cy="122" r="84" fill="{aro}" stroke="{CARVAO}" stroke-width="6"/>'
            f'<circle cx="100" cy="122" r="66" fill="{face}" stroke="{CARVAO}" stroke-width="4"/>{tk}'
            f'<line x1="100" y1="122" x2="{100 + 32 * math.sin(ah):.1f}" y2="{122 - 32 * math.cos(ah):.1f}" stroke="{ponteiro}" stroke-width="8" stroke-linecap="round"/>'
            f'<line x1="100" y1="122" x2="{100 + 50 * math.sin(am):.1f}" y2="{122 - 50 * math.cos(am):.1f}" stroke="{TOMATE if aro != TOMATE else VERDE}" stroke-width="5" stroke-linecap="round"/>'
            f'<circle cx="100" cy="122" r="8" fill="{CARVAO}"/><rect x="92" y="18" width="16" height="22" rx="4" fill="{CARVAO}"/></svg>')

def risco(w, cor=TOMATE, esp=12, rot=-4):
    """Risco de caneta sobre a palavra."""
    return f'<div style="width:{w}px;height:{esp}px;background:{cor};border-radius:{esp}px;transform:rotate({rot}deg);box-shadow:3px 4px 0 rgba(20,19,17,.25)"></div>'

def pino(tam=34, cor=CREME):
    return (f'<svg viewBox="0 0 24 24" width="{tam}" height="{tam}"><path d="M15 3 L21 9 L18 10 L14 14 L15 19 L13 21 L9 17 L4 22 L3 21 L8 16 L4 12 L6 10 L11 11 L15 7 Z" '
            f'fill="{cor}" stroke="{CARVAO}" stroke-width="1.4" stroke-linejoin="round"/></svg>')

def icone(n, tam, cor, w=6):
    return (f'<svg viewBox="0 0 100 100" width="{tam}" height="{tam}" style="display:block"><g fill="none" stroke="{cor}" stroke-width="{w}" '
            f'stroke-linecap="round" stroke-linejoin="round">{IC[n]}</g></svg>')

ASS = lambda y, bg=CARVAO, fg=CREME, t='chama no zap · @oreganoturbo': tarja_ass(y, bg, fg, t)
ASS_STORY = lambda bg=CARVAO, fg=CREME, t='chama no zap · @oreganoturbo': tarja_ass(1820, bg, fg, t, 100)
SEL = lambda tam, txt, bg, fg, rot, centro=None, fs=12.5: f'<div style="transform:rotate({rot}deg)">{selo(tam, txt, bg, fg, centro, fs)}</div>'

POS = {'d16-08h-copia-e-cola': (800, 60, 4), 'd22-12h-cliente-te-esqueceu': (800, 16, 4), 'd26-08h-melhor-dia-pra-pizza': (790, 900, 4)}  # lugar fixo da comanda (x, y, rot) quando o automático não serve
def salvar(nome, larg, alt, html):
    P.append((nome, larg, alt, html + COMANDA(nome, POS.get(nome)) + GRAO))
feed = lambda n, h: salvar(n, 1080, 1350, h)
stor = lambda n, h: salvar(n, 1080, 1920, h)
COMP = {}  # nome → composição (vai para o README)

# ================================================================== d15 12h · TERÇA VAZIA CUSTA CARO. (tomate · comanda dos custos)
# Copia: cardápio-cartaz (Jonny's retro-14 / "Escolha sua pizza") virado COMANDA de custos + manchete em 2 tamanhos ("AQUI / não tem / ERRO").
lin = lambda a, b, c=TOMATE: (f'<div style="display:flex;align-items:baseline;gap:10px;padding:12px 0;border-bottom:3px dashed rgba(20,19,17,.22)">'
                              f'<span style="font:400 30px/1 \'Bagel Fat One\';text-transform:uppercase;color:{CARVAO};white-space:nowrap">{a}</span>'
                              f'<span style="flex:1;border-bottom:4px dotted {CARVAO};opacity:.45;transform:translateY(-6px)"></span>'
                              f'<span style="font:600 19px \'IBM Plex Mono\';color:{c};white-space:nowrap;letter-spacing:.06em">{b}</span></div>')
serra = 'radial-gradient(circle at 12px 0,transparent 12px,' + CREME + ' 13px) -12px 100%/24px 24px repeat-x'
comanda = (f'<div style="width:520px;background:{CREME};padding:30px 34px 60px;box-shadow:18px 20px 0 rgba(20,19,17,.38);position:relative;'
           f'-webkit-mask:linear-gradient(#000,#000) top/100% calc(100% - 22px) no-repeat,radial-gradient(circle at 13px 22px,transparent 12px,#000 13px) bottom/26px 22px repeat-x">'
           + f'<div style="display:flex;justify-content:space-between;align-items:center">{MONO("Comanda Nº 0003", 17, CARVAO)}{simbolo(46, VERDE, CREME)}</div>'
           + MONO('Terça · 18h às 23h', 17, TOMATE, 'margin:6px 0 10px')
           + BAGEL('Custo fixo', 54, VERDE, 1, 'margin:4px 0 6px')
           + lin('Aluguel', 'PAGA IGUAL') + lin('Gás do forno', 'PAGA IGUAL') + lin('Equipe', 'PAGA IGUAL')
           + lin('Motoboy parado', 'PAGA IGUAL')
           + lin('Pedidos', 'POUCOS', VERDE)
           + f'<div style="margin-top:22px;background:{TOMATE};padding:16px 20px;border:4px solid {CARVAO};display:flex;justify-content:space-between;align-items:center">'
           + ANTON('Total', 50, CREME, 1) + BAGEL('Caro.', 56, ACAFRAO, 1, SH(CARVAO, 4)) + '</div></div>')
feed('d15-12h-terca-vazia-custa-caro',
     FUNDO(TOMATE, CREME, .12) +
     A(40, 26, BAGEL('Terça', 236, CREME, .86, SH(CARVAO, 10))) +
     A(44, 236, BAGEL('vazia', 236, ACAFRAO, .86, SH(CARVAO, 10))) +
     A(52, 470, ANTON('custa', 104, CARVAO, .9, f'background:{CREME};padding:6px 18px 2px;transform:rotate(-3deg);box-shadow:8px 8px 0 {CARVAO}')) +
     A(340, 478, BAGEL('caro.', 120, CREME, .9, SH(CARVAO, 7))) +
     A(560, 600, comanda, 'transform:rotate(5deg) scale(.92);transform-origin:0 0') +
     A(46, 690, ANTON('Aluguel, gás<br>e equipe<br>pagam igual.', 66, CREME, .98)) +
     A(44, 940, adesivo('O forno<br>liga igual', ACAFRAO, CARVAO, -8, 36, '18px 26px', extra='border-radius:28px;line-height:1.02;text-align:center')) +
     A(340, 935, SEL(170, 'DOR DO DONO · SÓ PIZZARIAS · ', VERDE, CREME, 14, centro=icone('chama', 60, CREME, 7))) +
     A(44, 1140, adesivo('Bora encher<br>a terça? ↗', VERDE, CREME, -4, 34, '16px 26px', extra='border-radius:28px;line-height:1.02;text-align:center')) +
     ASS(1258))
COMP['d15-12h-terca-vazia-custa-caro'] = 'Comanda de custos (cardápio-cartaz virado nota da terça, Jonny\'s retro-14) + manchete em 2 tamanhos + selo girado; tomate com padrão de ícones'

# ================================================================== d16 08h · Copia e cola: (story açafrão · conversa no celular desenhado)
# Copia: conversa de WhatsApp do kit (story-3 v3) + Decaf Girl (produto enorme na frente da câmera: aqui o celular).
conv16 = (chip('hoje') +
          bolha(f'Oi, {marca("Ana")}! Tudo bem? Faz um tempinho que você não pede com a gente.', True, '17:02', 34) +
          bolha(f'Hoje a {marca("calabresa")} tá saindo quentinha do forno. Quer que eu separe uma pra você?', True, '17:02', 34) +
          bolha('Se preferir, te mando o cardápio aqui mesmo.', True, '17:03', 34))
stor('d16-08h-copia-e-cola',
     FUNDO(CREME, TOMATE, .10) +
     A(44, 70, MONO('Dica pronta · cliente que sumiu', 22, CREME, f'background:{TOMATE};padding:10px 14px;box-shadow:6px 6px 0 {CARVAO}')) +
     A(36, 140, BAGEL('Copia', 250, TOMATE, .86, SH(CARVAO, 11))) +
     A(40, 360, BAGEL('e cola:', 220, VERDE, .86, SH(CARVAO, 10))) +
     A(130, 640, celular(820, 1230, wa_tela('Ana · cliente', 'último pedido há 40 dias', conv16, 1.0)), 'transform:rotate(-4deg)') +
     A(800, 1330, SEL(230, 'MENSAGEM PRA CLIENTE QUE SUMIU · ', VERDE, CREME, 12, centro=icone('celular', 80, CREME, 7))) +
     A(40, 1490, adesivo('Troque o nome<br>e o sabor', TOMATE, CREME, -8, 40, '20px 30px', extra='border-radius:30px;line-height:1.02;text-align:center')) +
     A(530, 1560, adesivo('Copiou? Manda hoje ↗', VERDE, CREME, 5, 38)) +
     faixa('copia e cola ✦ manda hoje', 1660, CREME, VERDE, -3, 104, 62, x=-60, w=1240, sep='✦') +
     ASS_STORY())
COMP['d16-08h-copia-e-cola'] = 'Celular desenhado com a conversa do WhatsApp (mensagem pronta) + manchete gorda em 2 cores + selo e adesivos + faixa em loop; creme'

# ================================================================== d17 08h · Você responde em quanto tempo? (story tomate · relógio gigante + enquete)
stor('d17-08h-responde-em-quanto-tempo',
     FUNDO(TOMATE, CREME, .11) +
     A(140, 470, f'<div style="transform:rotate(-10deg)">{relogio(860, ACAFRAO, CREME, CARVAO, 10, 50)}</div>') +
     A(44, 70, ANTON('Você responde', 132, CREME, .9, SH(CARVAO, 6))) +
     A(44, 200, ANTON('em quanto', 132, CREME, .9, SH(CARVAO, 6))) +
     A(36, 320, BAGEL('tempo?', 250, ACAFRAO, .86, SH(CARVAO, 11))) +
     A(24, 560, f'<div style="transform:rotate(-12deg)">{estrela(250, VERDE, MONO("seja", 20, CREME) + BAGEL("sincero", 40, ACAFRAO, .9), 0)}</div>') +
     A(90, 1170, enquete('Cliente mandou “oi”. Você responde em:', ['1 minuto', '10 minutos', '1 hora'], 900, 42, -2)) +
     faixa('cliente com fome não espera', 1700, CARVAO, ACAFRAO, -3, 100, 56, x=-60, w=1240) +
     ASS_STORY(VERDE))
COMP['d17-08h-responde-em-quanto-tempo'] = 'Relógio despertador gigante desenhado atrás + figurinha de enquete + estrela girada + faixa em loop; tomate'

# ================================================================== d18 19h · RESPOSTA PRONTA: "DEMORA?" (feed creme · bolha gigante + relógio)
feed('d18-19h-resposta-pronta-demora',
     BOX(0, 0, 1080, 1350, xadrez(VERDE, CREME, 30)) +
     BOX(30, 30, 1020, 1210, CREME, f'border:6px solid {CARVAO};box-shadow:12px 12px 0 {CARVAO}') + BOX(36, 36, 1008, 1198, padrao(VERDE, .12, 260)) +
     A(70, 64, ANTON('Resposta pronta:', 92, VERDE, .9)) +
     A(56, 180, f'<div style="position:relative;background:#fff;border:6px solid {CARVAO};border-radius:60px 60px 60px 8px;padding:26px 46px 16px;transform:rotate(-4deg);box-shadow:16px 16px 0 {CARVAO}">'
                + FIT(BAGEL('“Demora?”', 196, TOMATE, .9, SH(CARVAO, 7)), 820) + MONO('cliente · 20:14', 16, '#667781', 'text-align:right;margin-top:6px') + '</div>') +
     A(690, 520, f'<div style="transform:rotate(12deg)">{relogio(330, TOMATE, CREME, CARVAO, 8, 25)}</div>') +
     A(70, 560, f'<div style="width:640px;background:{ZAPB};border:5px solid {CARVAO};border-radius:44px 8px 44px 44px;padding:30px 36px 20px;transform:rotate(2deg);box-shadow:14px 14px 0 {VERDE}">'
                + TXT(f'Oi! Sua pizza entrou no forno agora. Fica pronta em {marca("uns 25 minutos")} e eu te aviso quando sair pra entrega.', 37, CARVAO, 'font-weight:600;line-height:1.3')
                + MONO('você · 20:15 ✓✓', 16, '#3F7F5F', 'text-align:right;margin-top:10px') + '</div>') +
     A(76, 975, adesivo('Diga o tempo', TOMATE, CREME, -5, 34)) +
     A(400, 1000, adesivo('Avise quando sair', VERDE, CREME, 4, 34)) +
     A(150, 1100, adesivo('Nunca deixe sem resposta', ACAFRAO, CARVAO, -2, 34)) +
     A(770, 1110, adesivo('Copie e cole ↗', CARVAO, ACAFRAO, 6, 30)) +
     A(70, 1205, MONO('Ajuste o tempo pro seu forno · exemplo ilustrativo', 14, VERDE)) +
     tarja_ass(1258, VERDE, CREME, 'chama no zap · @oreganoturbo'))
COMP['d18-19h-resposta-pronta-demora'] = 'Bolha de conversa gigante com a pergunta + resposta pronta + relógio desenhado + 3 adesivos de regra; moldura de xadrez verde, miolo creme'

# ================================================================== d20 08h · Black Friday? Aqui não tem desconto. (story carvão × tomate)
stor('d20-08h-black-friday-sem-desconto',
     BOX(0, 0, 1080, 1060, CARVAO) + f'<div class="a" style="left:0;top:0;width:1080px;height:1060px;background:{padrao(CREME, .06, 300)}"></div>' +
     BOX(0, 1060, 1080, 900, TOMATE) + f'<div class="a" style="left:0;top:1060px;width:1080px;height:900px;background:{padrao(CREME, .1, 300)}"></div>' +
     A(48, 70, MONO('Sábado, 28/11 · Black Friday', 22, ACAFRAO)) +
     A(36, 120, BAGEL('Black', 270, CREME, .86)) +
     A(36, 360, BAGEL('Friday?', 250, ACAFRAO, .86)) +
     A(48, 640, ANTON('Aqui não tem', 130, CREME, .9)) +
     A(40, 800, BAGEL('desconto.', 178, CREME, .9, SH(TOMATE, 8))) +
     A(10, 885, risco(1060, TOMATE, 28, -5)) +
     A(48, 1110, ANTON('Tem', 150, CREME, .9, SH(CARVAO, 7))) +
     A(40, 1270, BAGEL('5 vagas', 200, ACAFRAO, .88, SH(CARVAO, 10))) +
     A(44, 1470, ANTON('de fundadora.', 110, CREME, .9, SH(CARVAO, 6))) +
     A(700, 1030, f'<div style="transform:rotate(14deg)">{estrela(330, ACAFRAO, MONO("em vez de desconto", 14, CARVAO) + BAGEL("condição<br>de<br>fundadora", 38, TOMATE, .95, "margin-top:6px"), 0, 16)}</div>') +
     faixa('sem desconto ✦ com condição de fundadora', 1660, CREME, CARVAO, -3, 100, 52, x=-60, w=1240) +
     ASS_STORY())
COMP['d20-08h-black-friday-sem-desconto'] = 'Story dividido carvão × tomate: manchete empilhada, "desconto" riscado a caneta, estrela de condição e faixa em loop'

# ================================================================== d20 12h · BLACK FRIDAY SEM DESCONTO. (feed cartaz preto + estrela amarela)
etq = (f'<div style="position:relative;width:300px;height:170px;background:{TOMATE};border:6px solid {CARVAO};border-radius:14px 60px 60px 14px;'
       f'box-shadow:12px 12px 0 rgba(0,0,0,.45);display:grid;place-items:center;clip-path:polygon(0 0,100% 0,100% 100%,0 100%)">'
       f'<span style="position:absolute;right:30px;top:62px;width:34px;height:34px;border-radius:50%;background:{CARVAO}"></span>'
       + BAGEL('−0%', 96, CREME, .9, 'margin-right:60px') + '</div>')
feed('d20-12h-black-friday-cartaz',
     FUNDO(CARVAO, CREME, .06) +
     faixa('black friday ✦ black friday', 36, ACAFRAO, CARVAO, -3, 92, 52, x=-60, w=1240) +
     A(48, 170, ANTON('Black Friday', 130, CREME, .9)) +
     A(36, 300, BAGEL('Sem', 330, ACAFRAO, .84)) +
     A(36, 590, BAGEL('desconto.', 178, CREME, .9, SH(TOMATE, 8))) +
     A(560, 760, f'<div style="transform:rotate(10deg)">{estrela(480, ACAFRAO, MONO("em vez de", 18, CARVAO) + BAGEL("condição<br>de<br>fundadora", 62, TOMATE, .92, "margin:8px 0") + MONO("5 vagas", 22, CARVAO), 0, 16)}</div>') +
     A(56, 820, etq, 'transform:rotate(-10deg)') +
     A(56, 1030, ANTON('Preço do anual<br>no semestral.', 66, CREME, .98)) +
     A(56, 1186, MONO('Só pra 5 pizzarias fundadoras', 17, ACAFRAO)) +
     tarja_ass(1258, ACAFRAO, CARVAO, 'chama no zap · @oreganoturbo'))
COMP['d20-12h-black-friday-cartaz'] = 'Cartaz preto de oferta: faixa em loop no topo, "SEM" gigante, etiqueta de preço "−0%", estrela amarela com a condição de fundadora'

# ================================================================== d21 08h · Resumo da semana. (story verde · 3 cartões numerados)
cart = lambda n, t, bg, fn, ft, rot: (f'<div style="width:980px;height:330px;background:{bg};border:6px solid {CARVAO};box-shadow:14px 14px 0 {CARVAO};transform:rotate({rot}deg);'
                                      f'display:flex;align-items:center;gap:30px;padding:0 40px">' + BAGEL(n, 250, fn, .9, SH(CARVAO, 8)) +
                                      f'<div style="font:400 47px/1 \'Bagel Fat One\';text-transform:uppercase;color:{ft}">{t}</div></div>')
stor('d21-08h-resumo-da-semana',
     FUNDO(VERDE, CREME, .1) +
     A(44, 70, MONO('Domingo · 3 coisas pra fazer hoje', 22, CARVAO, f'background:{ACAFRAO};padding:10px 14px;box-shadow:6px 6px 0 {CARVAO}')) +
     A(36, 140, BAGEL('Resumo', 250, CREME, .86, SH(CARVAO, 11))) +
     A(44, 360, ANTON('da semana.', 150, ACAFRAO, .9, SH(CARVAO, 6))) +
     A(760, 300, SEL(230, 'RESUMO DE DOMINGO · SÓ PIZZARIAS · ', TOMATE, CREME, -12)) +
     A(50, 580, cart('1', 'Mande mensagem pra<br>5 clientes que sumiram', CREME, TOMATE, CARVAO, -2)) +
     A(50, 950, cart('2', 'Salve a resposta<br>pronta do “demora?”', ACAFRAO, VERDE, CARVAO, 1.5)) +
     A(50, 1320, cart('3', 'Confira link, cardápio<br>e foto antes de abrir', TOMATE, ACAFRAO, CREME, -1.5)) +
     A(560, 1690, adesivo('Feito? Me conta ↗', ACAFRAO, CARVAO, -5, 40)) +
     ASS_STORY())
COMP['d21-08h-resumo-da-semana'] = '3 cartões numerados com número gordo gigante, girados em sentidos alternados + selo + adesivo; verde'

# ================================================================== d21 19h · CHECKLIST DE SÁBADO (feed xadrez tomate · prancheta desenhada)
itens21 = [('Link do zap na bio funcionando', 1), ('Cardápio com preço atualizado', 1), ('Foto do dia postada até 17h', 1),
           ('Story do forno aceso', 0), ('Resposta do “demora?” salva', 0), ('Motoboy confirmado', 0)]
ck = ''.join(f'<div style="display:flex;align-items:center;gap:20px;padding:13px 0;border-bottom:3px dashed rgba(20,19,17,.2)">'
             f'<span style="position:relative;flex:none;width:56px;height:56px;border:5px solid {CARVAO};border-radius:10px;background:#fff">'
             + (f'<svg viewBox="0 0 60 60" width="84" height="84" style="position:absolute;left:-6px;top:-24px"><path d="M8 32 L24 48 L56 6" fill="none" stroke="{TOMATE}" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/></svg>' if f else '')
             + f'</span><span style="font:400 34px/1.05 \'Bagel Fat One\';text-transform:uppercase;color:{CARVAO}">{t}</span></div>' for t, f in itens21)
prancheta = (f'<div style="position:relative;width:880px;height:1050px;background:{VERDE};border:6px solid {CARVAO};border-radius:40px;box-shadow:20px 22px 0 rgba(20,19,17,.45);padding:70px 40px 40px">'
             f'<div style="width:100%;height:100%;background:{CREME};border:5px solid {CARVAO};padding:34px 40px">'
             + f'<div style="display:flex;align-items:flex-end;gap:20px">{BAGEL("Checklist", 120, TOMATE, .9, SH(CARVAO, 6))}</div>'
             + ANTON('de sábado · antes de abrir', 56, VERDE, 1, 'margin:6px 0 10px') + ck + KAU('Bora pro forno!', 64, TOMATE, 'margin-top:26px;transform:rotate(-3deg)') + '</div>'
             f'<div style="position:absolute;left:290px;top:-38px;width:300px;height:110px;background:{ACAFRAO};border:6px solid {CARVAO};border-radius:22px 22px 40px 40px;'
             f'display:grid;place-items:center;box-shadow:8px 8px 0 rgba(20,19,17,.35)"><span style="width:90px;height:30px;border-radius:99px;background:{CARVAO}"></span></div></div>')
feed('d21-19h-checklist-de-sabado',
     BOX(0, 0, 1080, 1350, xadrez(TOMATE, CREME, 45)) +
     A(100, 90, prancheta, 'transform:rotate(-2.5deg)') +
     A(36, 30, adesivo('Sábado é final de campeonato', CARVAO, ACAFRAO, -4, 32)) +
     A(790, 950, SEL(250, 'SALVE ESTE POST · USE TODO SÁBADO · ', TOMATE, CREME, 12, centro=icone('pizza', 90, CREME, 6))) +
     ASS(1258))
COMP['d21-19h-checklist-de-sabado'] = 'Prancheta desenhada com checklist marcado a caneta sobre xadrez de cantina tomate + selo "salve este post" + adesivo'

# ================================================================== d22 12h · O CLIENTE TE ESQUECEU? (feed açafrão · celular com conversa antiga)
conv22 = (chip('12 de agosto') +
          bolha('Boa noite! Quero uma portuguesa grande', False, '19:40', 27) +
          bolha('Anotado, Ana! Já vai pro forno.', True, '19:41', 27) +
          bolha('Chegou quentinha, obrigada!', False, '20:22', 27) +
          f'<div style="height:40px"></div>' + chip('hoje') +
          f'<div style="align-self:center;margin-top:10px;font:600 22px Inter;color:#54656F;background:#FFF3C4;padding:10px 18px;border-radius:12px">nenhuma mensagem desde agosto</div>')
feed('d22-12h-cliente-te-esqueceu',
     FUNDO(CREME, VERDE, .10) +
     A(44, 30, ANTON('O cliente te', 112, CARVAO, .9)) +
     A(36, 136, FIT(BAGEL('esqueceu?', 210, TOMATE, .86, SH(CARVAO, 10)), 1010)) +
     A(520, 400, celular(540, 1000, wa_tela('Ana · cliente', 'visto por último em agosto', conv22, .86)), 'transform:rotate(7deg)') +
     A(40, 440, f'<div style="background:{VERDE};padding:26px 30px;border:6px solid {CARVAO};box-shadow:12px 12px 0 {CARVAO};transform:rotate(-4deg)">'
                + MONO('ou será que', 20, ACAFRAO) + ANTON('você esqueceu<br>dele?', 82, CREME, .95, 'margin-top:8px') + '</div>') +
     A(56, 790, adesivo('Ninguém volta<br>sem convite', TOMATE, CREME, -6, 40, '20px 30px', extra='border-radius:30px;line-height:1.02;text-align:center')) +
     A(110, 980, SEL(200, 'CLIENTE QUE SUMIU · DOR DO DONO · ', CARVAO, ACAFRAO, -10, centro=icone('caixa', 70, ACAFRAO, 7))) +
     A(60, 1210, MONO('conversa ilustrativa', 13, CARVAO)) +
     ASS(1258))
COMP['d22-12h-cliente-te-esqueceu'] = 'Celular desenhado com conversa antiga parada desde agosto + manchete gigante + bloco "ou você esqueceu dele?" + adesivo e selo; creme'

# ================================================================== d22 19h · MENSAGEM DE VOLTA PRO CLIENTE (feed verde · bolhas gigantes sem celular)
feed('d22-19h-mensagem-de-volta',
     FUNDO(VERDE, CREME, .1, 260) +
     A(40, 26, BAGEL('Mensagem', 170, CREME, .86, SH(CARVAO, 9))) +
     A(44, 196, BAGEL('de volta', 170, ACAFRAO, .86, SH(CARVAO, 9))) +
     A(46, 370, ANTON('pro cliente', 100, CREME, .9)) +
     A(640, 360, adesivo('Copie e cole ↗', TOMATE, CREME, 6, 40)) +
     A(60, 520, f'<div style="display:flex;flex-direction:column;gap:26px;width:960px">'
                + bolha(f'Oi, {marca("Ana")}! Aqui é da {marca("Pizzaria do Bairro")}. Sentimos sua falta por aqui.', True, '18:05', 40, 88, f'14px 14px 0 {CARVAO}')
                + bolha(f'Essa semana a {marca("portuguesa")} tá saindo caprichada. Quer que eu reserve uma pra sexta?', True, '18:05', 40, 88, f'14px 14px 0 {CARVAO}')
                + '</div>') +
     A(40, 1000, MONO('Sem spam:', 20, ACAFRAO)) +
     A(36, 1050, adesivo('1 mensagem só', CREME, VERDE, -4, 34)) +
     A(380, 1070, adesivo('Pelo nome', ACAFRAO, CARVAO, 3, 34)) +
     A(640, 1040, adesivo('Com um motivo', TOMATE, CREME, -3, 34)) +
     A(56, 1180, MONO('Troque o nome, a pizzaria e o sabor', 16, CREME, 'opacity:.85')) +
     tarja_ass(1258, TOMATE, CREME, 'chama no zap · @oreganoturbo'))
COMP['d22-19h-mensagem-de-volta'] = 'Bolhas de WhatsApp gigantes direto no fundo (sem celular) + manchete em 3 linhas + 3 adesivos "sem spam"; verde com padrão'

# ================================================================== d23 08h · Você posta todo dia? (story · parede de palavra + enquete)
parede = ''.join(f'<div style="font:400 164px/0.95 \'Bagel Fat One\';text-transform:uppercase;white-space:nowrap;color:{"transparent" if i % 2 else TOMATE};'
                 f'-webkit-text-stroke:4px {TOMATE};margin-left:{-120 * (i % 3)}px">todo dia todo dia todo dia</div>' for i in range(8))
stor('d23-08h-voce-posta-todo-dia',
     BOX(0, 0, 1080, 1920, CREME) +
     A(-60, 560, f'<div style="transform:rotate(-8deg);opacity:.9">{parede}</div>') +
     BOX(0, 0, 1080, 640, TOMATE, f'border-bottom:8px solid {CARVAO}', f'<div class="a" style="inset:0;background:{padrao(CREME, .1, 300)}"></div>') +
     A(44, 80, ANTON('Você posta', 160, CREME, .9, SH(CARVAO, 7))) +
     A(36, 250, BAGEL('todo dia?', 210, ACAFRAO, .86, SH(CARVAO, 10))) +
     A(760, 470, SEL(240, 'SEM JULGAMENTO · SÓ PIZZARIAS · ', VERDE, CREME, 10)) +
     A(90, 900, enquete('Seja sincero: você posta todo dia?', ['Sim, todo dia', 'Às vezes', 'Quase nunca'], 900, 44, 2)) +
     ASS_STORY(VERDE))
COMP['d23-08h-voce-posta-todo-dia'] = 'Parede de palavra repetida ("TODO DIA", cheia e contorno, estilo "HOT SAUCE" das favoritas) + enquete + bloco tomate com manchete + selo'

# ================================================================== d23 12h · O QUE UM PEDIDO A MAIS POR DIA FAZ (feed tomate · número gigante + calendário)
dias = ''.join(f'<div style="height:62px;display:grid;place-items:center;position:relative;font:600 15px \'IBM Plex Mono\';color:{CARVAO}">'
               f'<span style="position:absolute;left:5px;top:3px;opacity:.6">{d}</span>'
               f'<span style="width:46px;height:46px;border-radius:50%;background:{VERDE if d % 2 else TOMATE};color:{CREME};display:grid;place-items:center;font:400 20px Anton;transform:rotate({(d * 37) % 20 - 10}deg)">+1</span></div>'
               for d in range(1, 31))
cal = (f'<div style="width:520px;background:{CREME};border:6px solid {CARVAO};box-shadow:16px 16px 0 {CARVAO}">'
       f'<div style="background:{VERDE};padding:18px 24px;display:flex;justify-content:space-between;align-items:center;border-bottom:6px solid {CARVAO}">'
       + BAGEL('Um mês', 54, CREME, 1) + MONO('30 dias', 18, ACAFRAO) + '</div>'
       + '<div style="display:grid;grid-template-columns:repeat(7,1fr);gap:4px;padding:14px">'
       + ''.join(f'<div style="text-align:center;font:600 14px \'IBM Plex Mono\';color:{TOMATE}">{d}</div>' for d in 'STQQSSD') + dias + '</div></div>')
feed('d23-12h-um-pedido-a-mais-por-dia',
     FUNDO(TOMATE, CREME, .11) +
     A(44, 34, ANTON('O que', 90, CREME, .9)) +
     A(36, 112, BAGEL('1 pedido', 170, ACAFRAO, .86, SH(CARVAO, 9))) +
     A(44, 280, ANTON('a mais por dia faz?', 96, CREME, .9)) +
     A(530, 410, cal, 'transform:rotate(4deg)') +
     A(20, 400, BAGEL('+30', 330, ACAFRAO, .9, SH(CARVAO, 12))) +
     A(50, 715, ANTON('pedidos<br>no mês.', 110, CREME, 1.05, SH(CARVAO, 6))) +
     A(60, 990, adesivo('Não é promessa: é a conta', ACAFRAO, CARVAO, -3, 30)) +
     BOX(0, 1100, 1080, 250, CARVAO, f'border-top:8px solid {ACAFRAO};padding:30px 52px 0',
         f'<div style="display:flex;align-items:baseline;gap:18px">' + ANTON('Ticket de R$ 50 × 30 =', 54, CREME, 1) + BAGEL('R$ 1.500', 64, ACAFRAO, 1) + '</div>'
         + MONO('a mais no mês · exemplo ilustrativo', 18, CREME, 'margin-top:12px;opacity:.85')) +
     A(52, 1270, logo(34, CREME)) + A(808, 1286, MONO('@oreganoturbo', 19, CREME)) +
     A(830, 900, SEL(190, 'CONTA ILUSTRATIVA · NÃO É PROMESSA · ', VERDE, CREME, 10, centro=icone('caixa', 70, CREME, 7))))
COMP['d23-12h-um-pedido-a-mais-por-dia'] = 'Número gigante "+30" + calendário desenhado com um "+1" em cada dia + barra da conta (ilustrativo); tomate'

# ================================================================== d24 08h · Dica rápida: (story açafrão · perfil com 3 posts fixados)
tile = lambda bg, fg, t, pin: (f'<div style="position:relative;aspect-ratio:4/5;background:{bg};display:grid;place-items:center;text-align:center;overflow:hidden">'
                               + (f'<div style="font:400 40px/.95 \'Bagel Fat One\';text-transform:uppercase;color:{fg}">{t}</div>' if t else '')
                               + (f'<div style="position:absolute;right:8px;top:8px">{pino(34, CREME)}</div>' if pin else '') + '</div>')
perfil = (f'<div style="position:absolute;inset:0;background:#fff"></div>'
          f'<div style="position:absolute;left:0;right:0;top:70px;padding:0 28px">'
          f'<div style="display:flex;align-items:center;gap:30px">'
          f'<div style="width:150px;height:150px;border-radius:50%;background:{VERDE};display:grid;place-items:center;box-shadow:0 0 0 6px #fff,0 0 0 10px {TOMATE}">{simbolo(90, CREME, VERDE)}</div>'
          + ''.join(f'<div style="text-align:center"><div style="font:800 34px Inter;color:{CARVAO}">{a}</div><div style="font:500 20px Inter;color:#555">{b}</div></div>' for a, b in [('128', 'posts'), ('2.340', 'seguidores'), ('310', 'seguindo')])
          + '</div>'
          f'<div style="font:700 28px Inter;color:{CARVAO};margin-top:18px">Pizzaria do Bairro</div>'
          f'<div style="font:500 23px/1.35 Inter;color:#333">Forno a lenha · São Luís<br>Peça pelo zap ↓</div>'
          f'<div style="margin-top:16px;background:{VERDE};color:#fff;text-align:center;font:700 26px Inter;padding:16px;border-radius:12px">Pedir no WhatsApp</div>'
          f'<div style="margin:22px -28px 0;display:grid;grid-template-columns:repeat(3,1fr);gap:4px">'
          + tile(TOMATE, CREME, 'Cardá-<br>pio', 1) + tile(VERDE, ACAFRAO, 'Como<br>pedir', 1) + tile(CARVAO, CREME, 'Avalia-<br>ções', 1)
          + ''.join(f'<div style="aspect-ratio:4/5;background:{c};display:grid;place-items:center">{icone(n, 110, f, 6)}</div>' for c, f, n in [('#E8DCC4', TOMATE, 'pizza'), ('#D8E4D6', VERDE, 'fatia'), ('#F2DDB0', CARVAO, 'chama'), ('#E6D3CF', TOMATE, 'tomate'), ('#E8DCC4', VERDE, 'caixa'), ('#D8E4D6', TOMATE, 'manjericao')])
          + '</div></div>')
stor('d24-08h-dica-rapida-fixe-3-posts',
     FUNDO(VERDE, CREME, .10) +
     A(40, 40, BAGEL('Dica', 230, TOMATE, .86, SH(CARVAO, 10))) +
     A(40, 250, BAGEL('rápida:', 230, CREME, .86, SH(CARVAO, 10))) +
     A(44, 480, ANTON('Fixe 3 posts no topo do perfil.', 76, CARVAO, .92, f'background:{CREME};padding:10px 18px 4px;transform:rotate(-2deg);box-shadow:8px 8px 0 {CARVAO}')) +
     A(150, 640, celular(780, 1300, perfil), 'transform:rotate(3deg)') +
     A(30, 1440, adesivo('1º cardápio', TOMATE, CREME, -8, 34)) +
     A(60, 1550, adesivo('2º como pedir', VERDE, CREME, -4, 34)) +
     A(90, 1660, adesivo('3º avaliações', CARVAO, ACAFRAO, -6, 34)) +
     A(780, 60, f'<div style="transform:rotate(12deg)">{estrela(250, TOMATE, ANTON("leva<br>10<br>segundos", 46, CREME, .92), 0)}</div>') +
     ASS_STORY())
COMP['d24-08h-dica-rapida-fixe-3-posts'] = 'Perfil do Instagram desenhado no celular com 3 posts fixados (pino) + adesivos numerados + estrela; verde'

# ================================================================== d24 19h · RAIO-X: O QUE VOCÊ RECEBE (feed creme · cartaz com 5 selos)
def s5(t, sub, bg, fg, rot):
    return SEL(300, f'{sub} · RAIO-X · {sub} · ', bg, fg, rot, centro=BAGEL(t, 44 if len(t) < 9 else 36, fg, .95, 'text-align:center'), fs=12)
feed('d24-19h-raio-x-o-que-recebe',
     BOX(0, 0, 1080, 1350, TINTA) + f'<div class="a" style="inset:0;background:{padrao(CREME, .06, 300)}"></div>' +
     A(40, 26, BAGEL('Raio-X:', 240, CREME, .86)) +
     A(46, 262, ANTON('o que você recebe', 100, ACAFRAO, .9)) +
     A(30, 410, s5('Insta-<br>gram', 'PERFIL E FOTOS', VERDE, CREME, -10)) +
     A(390, 380, s5('Cardápio', 'PREÇO E ORDEM', TOMATE, CREME, 8)) +
     A(750, 420, s5('iFood', 'NOTA E VITRINE', ACAFRAO, CARVAO, -6)) +
     A(160, 740, s5('Anúncio', 'BAIRRO E VERBA', CARVAO, ACAFRAO, 6)) +
     A(520, 760, s5('Google', 'MAPA E AVALIAÇÃO', VERDE_ESC, CREME, -8)) +
     BOX(0, 1090, 1080, 260, VERDE, f'border-top:8px solid {TOMATE};padding:24px 52px 0;display:flex;align-items:center;gap:26px;height:150px',
         BAGEL('R$ 297', 92, CREME, 1, SH(CARVAO, 5)) + MONO('abatido no 1º mês<br>se fechar em 7 dias<br>5 vagas de fundadora', 17, CREME, 'line-height:1.5')) +
     A(52, 1268, logo(34, CREME)) + A(808, 1284, MONO('@oreganoturbo', 19, CREME)) +
     A(800, 930, adesivo('Chama no<br>zap ↗', TOMATE, CREME, -8, 38, '18px 26px', extra='border-radius:28px;line-height:1.02;text-align:center')))
COMP['d24-19h-raio-x-o-que-recebe'] = 'v4: cartaz escuro com 5 selos redondos girados (um por entrega do Raio-X); preço escrito na faixa verde, sem estrela de preço; carvão'

# ================================================================== d25 08h · Bastidor: relatório saindo. (story carvão · relatório no celular)
barras = ''.join(f'<div style="flex:1;display:flex;flex-direction:column;align-items:center;gap:6px"><div style="width:100%;height:{h}px;background:{c};border-radius:8px 8px 0 0"></div>'
                 f'<span style="font:600 16px \'IBM Plex Mono\';color:#555">{d}</span></div>'
                 for d, h, c in zip('STQQSSD', [70, 46, 60, 84, 150, 190, 130], [VERDE, TOMATE, VERDE, VERDE, VERDE, VERDE, VERDE]))
kpi = lambda n, t, c: (f'<div style="background:#fff;border-radius:18px;padding:16px 18px;border:3px solid #E7E2D8"><div style="font:600 17px Inter;color:#666">{t}</div>'
                       f'<div style="font:400 50px/1.1 Anton;color:{c}">{n}</div></div>')
rel = (f'<div style="position:absolute;inset:0;background:{CREME}"></div>'
       f'<div style="position:absolute;left:0;right:0;top:0;height:170px;background:{VERDE};padding:70px 28px 0;display:flex;align-items:center;gap:16px">{simbolo(56, CREME, VERDE)}'
       f'<div><div style="font:700 28px Inter;color:#fff">Relatório de segunda</div><div style="font:500 19px Inter;color:#CFE3D6">Pizzaria exemplo · semana 2</div></div></div>'
       f'<div style="position:absolute;left:24px;right:24px;top:196px;display:grid;grid-template-columns:1fr 1fr;gap:14px">'
       + kpi('R$ 210', 'Investido no anúncio', CARVAO) + kpi('46', 'Pedidos com código', VERDE) + kpi('R$ 4,56', 'Custo por pedido', TOMATE) + kpi('Terça', 'Dia mais fraco', CARVAO)
       + f'<div style="grid-column:1/3;background:#fff;border-radius:18px;padding:16px 18px;border:3px solid #E7E2D8"><div style="font:600 17px Inter;color:#666;margin-bottom:10px">Pedidos por dia</div>'
       f'<div style="display:flex;align-items:flex-end;gap:10px;height:220px">{barras}</div></div>'
       f'<div style="grid-column:1/3;background:{ACAFRAO};border-radius:18px;padding:16px 18px"><div style="font:700 18px Inter;color:{CARVAO}">O que muda nesta semana</div>'
       f'<div style="font:400 28px/1.05 \'Bagel Fat One\';color:{CARVAO};text-transform:uppercase;margin-top:6px">Combo de terça no anúncio do bairro</div></div></div>'
       f'<div style="position:absolute;left:60px;top:900px;transform:rotate(-10deg);border:7px solid {TOMATE};color:{TOMATE};font:400 47px/1 \'Bagel Fat One\';padding:8px 18px;text-transform:uppercase;'
       f'background:rgba(243,238,230,.7)">Exemplo ilustrativo</div>')
stor('d25-08h-bastidor-relatorio-saindo',
     FUNDO(CARVAO, CREME, .06) +
     A(44, 70, ANTON('Bastidor:', 130, ACAFRAO, .9)) +
     A(36, 200, BAGEL('relatório', 196, CREME, .86, SH(TOMATE, 9))) +
     A(36, 400, BAGEL('saindo.', 196, TOMATE, .86, SH(CREME, 6))) +
     A(770, 380, f'<div style="transform:rotate(10deg)">{estrela(270, ACAFRAO, MONO("toda", 20, CARVAO) + BAGEL("Seg<br>8h", 70, TOMATE, .88), 0)}</div>') +
     A(150, 680, celular(780, 1160, rel), 'transform:rotate(-3deg)') +
     faixa('toda segunda ✦ 8h ✦ no seu zap', 1690, ACAFRAO, CARVAO, -3, 100, 56, x=-60, w=1240) +
     ASS_STORY(VERDE))
COMP['d25-08h-bastidor-relatorio-saindo'] = 'Relatório desenhado no celular (cartões de número, gráfico de barras, carimbo "exemplo ilustrativo") + estrela "Seg 8h" + faixa; carvão'

# ================================================================== d25 12h · SEU CARDÁPIO TEM 40 SABORES? (feed açafrão · cardápio riscado)
sab = ['Calabresa', 'Mussarela', 'Portuguesa', 'Frango c/ catupiry', 'Marguerita', 'Quatro queijos', 'Pepperoni', 'Chocolate',
       'Napolitana', 'Toscana', 'Bacon', 'Atum', 'Milho', 'Palmito', 'Lombo', 'Baiana', 'Vegetariana', 'Carne seca', 'Strogonoff', 'Camarão',
       'Brócolis', 'Moda da casa', 'Alho e óleo', 'Escarola', 'Rúcula', 'Abobrinha', 'Romeu e Julieta', 'Banana', 'Prestígio', 'Confete',
       'Doce de leite', 'Morango', 'Siciliana', 'Francesa', 'Mexicana', 'Caipira', 'Peruana', 'Havaiana', 'Paulista', 'Cinco queijos']
ordem = [0, 8, 1, 9, 10, 2, 11, 12, 3, 13, 14, 15, 4, 16, 17, 18, 5, 19, 20, 21, 22, 6, 23, 24, 25, 26, 27, 7, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]
def it25(i):
    t, fica = sab[i], i < 8
    deco = (f'<span style="position:absolute;left:-12px;right:-12px;top:-6px;bottom:-8px;border:4px solid {VERDE};border-radius:50%;transform:rotate(-3deg)"></span>' if fica else
            f'<span style="position:absolute;left:-6px;right:-6px;top:50%;height:6px;background:{TOMATE};border-radius:6px;transform:rotate({(i * 13) % 9 - 4}deg)"></span>')
    return (f'<div style="padding:5px 0"><span style="position:relative;display:inline-block;font:400 24px/1.1 \'Bagel Fat One\';text-transform:uppercase;'
            f'color:{CARVAO if fica else "rgba(20,19,17,.55)"}">{t}{deco}</span></div>')
menu = (f'<div style="width:960px;background:{CREME};border:6px solid {CARVAO};box-shadow:16px 16px 0 {CARVAO};padding:26px 40px 30px">'
        f'<div style="display:flex;justify-content:space-between;align-items:center;border-bottom:4px solid {CARVAO};padding-bottom:12px;margin-bottom:12px">'
        + BAGEL('Cardápio', 58, TOMATE, 1) + MONO('40 sabores · página 1 de 3', 16, CARVAO) + '</div>'
        + '<div style="columns:3;column-gap:34px">' + ''.join(it25(i) for i in ordem) + '</div></div>')
feed('d25-12h-cardapio-40-sabores',
     FUNDO(CREME, TOMATE, .10) +
     A(44, 26, ANTON('Seu cardápio tem', 92, CARVAO, .9)) +
     A(36, 110, FIT(BAGEL('40 sabores?', 190, TOMATE, .86, SH(CARVAO, 10)), 1000)) +
     A(60, 330, menu, 'transform:rotate(-1.5deg)') +
     A(40, 1100, adesivo('Quem escolhe demais, desiste.', TOMATE, CREME, -3, 38)) +
     A(800, 220, f'<div style="transform:rotate(12deg)">{estrela(230, VERDE, MONO("fica com", 18, CREME) + BAGEL("os 8<br>que<br>vendem", 40, ACAFRAO, .9), 0)}</div>') +
     ASS(1258))
COMP['d25-12h-cardapio-40-sabores'] = 'Cardápio-cartaz com 40 sabores riscados a caneta e 8 circulados + estrela "fica com os 8 que vendem" + adesivo; creme'

# ================================================================== d26 08h · Qual o melhor dia pra pizza? (story tomate · tira da semana + enquete)
cols = [('Seg', CREME, TOMATE), ('Ter', ACAFRAO, CARVAO), ('Qua', VERDE, CREME), ('Qui', CREME, VERDE), ('Sex', CARVAO, ACAFRAO), ('Sáb', ACAFRAO, TOMATE), ('Dom', VERDE, ACAFRAO)]
tira = ''.join(f'<div style="width:154px;height:900px;background:{bg};border-right:5px solid {CARVAO};display:flex;flex-direction:column;align-items:center;padding-top:30px;gap:24px">'
               f'<div style="font:400 64px/1 \'Bagel Fat One\';text-transform:uppercase;color:{fg}">{d}</div>{icone("fatia" if i % 2 else "pizza", 90, fg, 6)}'
               f'<div style="font:400 300px/1 Anton;color:{fg};opacity:.18">{i + 1}</div></div>' for i, (d, bg, fg) in enumerate(cols))
stor('d26-08h-melhor-dia-pra-pizza',
     FUNDO(TOMATE, CREME, .1) +
     A(44, 70, ANTON('Qual o melhor', 140, CREME, .9, SH(CARVAO, 7))) +
     A(36, 210, BAGEL('dia pra', 220, ACAFRAO, .86, SH(CARVAO, 10))) +
     A(36, 410, BAGEL('pizza?', 220, CREME, .86, SH(CARVAO, 10))) +
     A(0, 700, f'<div style="display:flex;border-top:6px solid {CARVAO};border-bottom:6px solid {CARVAO}">{tira}</div>') +
     A(720, 400, SEL(250, 'VOTE AÍ · CULTURA DE PIZZARIA · ', VERDE, CREME, 12, centro=icone('chama', 80, CREME, 7))) +
     A(90, 1060, enquete('Pra você, o melhor dia pra pizza é:', ['Sexta', 'Sábado', 'Domingo', 'Segunda (por que não?)'], 900, 42, -2)) +
     faixa('sexta ✦ sábado ✦ domingo ✦ e segunda também', 1690, ACAFRAO, CARVAO, -3, 96, 52, x=-60, w=1240) +
     ASS_STORY())
COMP['d26-08h-melhor-dia-pra-pizza'] = 'Tira da semana em 7 colunas de cor (SEG a DOM com ícones em traço) + enquete de 4 opções + selo; tomate'

# ================================================================== d26 12h · AINDA TEM VAGA? (feed verde-escuro · contador de vagas)
flip = lambda t, bg=CARVAO, fg=ACAFRAO: (f'<div style="position:relative;width:210px;height:290px;background:{bg};border-radius:20px;border:6px solid {CREME};box-shadow:12px 14px 0 rgba(0,0,0,.4);'
                                          f'display:grid;place-items:center;overflow:hidden">' + BAGEL(t, 230, fg, 1) +
                                          f'<div style="position:absolute;left:0;right:0;top:50%;height:6px;background:{CREME};margin-top:-3px"></div></div>')
vaga = lambda n, rot: (f'<div style="width:178px;background:{CREME};border:5px solid {CARVAO};border-radius:16px;padding:14px 0 12px;text-align:center;transform:rotate({rot}deg);'
                       f'box-shadow:8px 8px 0 rgba(0,0,0,.35)">{MONO("vaga", 15, TOMATE)}{BAGEL(f"0{n}", 64, VERDE, 1)}'
                       f'<div style="margin:6px auto 0;width:120px;border:3px dashed {CARVAO};border-radius:10px;font:400 30px/1.3 Anton;color:{CARVAO}">?</div></div>')
feed('d26-12h-ainda-tem-vaga',
     FUNDO(VERDE_ESC, CREME, .07) +
     A(44, 30, ANTON('Ainda tem', 130, CREME, .9)) +
     A(36, 150, BAGEL('vaga?', 320, ACAFRAO, .84, SH(TOMATE, 12))) +
     A(600, 430, f'<div style="display:flex;gap:20px;transform:rotate(-4deg)">{flip("0")}{flip("5", TOMATE, CREME)}</div>') +
     A(620, 760, MONO('vagas de fundadora no total', 17, CREME, f'background:{CARVAO};padding:9px 12px;transform:rotate(-4deg)')) +
     A(46, 860, f'<div style="display:flex;gap:22px">{vaga(1, -4)}{vaga(2, 3)}{vaga(3, -2)}{vaga(4, 4)}{vaga(5, -3)}</div>') +
     A(40, 470, f'<div style="transform:rotate(-8deg)">{estrela(330, TOMATE, MONO("quantas", 20, CREME) + BAGEL("sobram?", 56, ACAFRAO, .9) + MONO("veja no zap", 20, CREME), 0)}</div>') +
     A(46, 1065, ANTON('Condição de fundadora: preço do anual no semestral.', 44, CREME, 1, 'white-space:normal;width:990px')) +
     A(600, 1150, adesivo('Chama no zap ↗', TOMATE, CREME, -4, 38)) +
     tarja_ass(1258, ACAFRAO, CARVAO, 'chama no zap · @oreganoturbo'))
COMP['d26-12h-ainda-tem-vaga'] = 'Contador de vagas desenhado (placar "05" estilo flip + 5 cartões de vaga com "?") + estrela "quantas sobram? veja no zap"; verde-escuro'

# ================================================================== d27 08h · Resumo do mês. (story creme · linha do tempo de 4 semanas)
sem = lambda n, t, bg, fg, rot: (f'<div style="display:flex;align-items:center;gap:26px;transform:rotate({rot}deg)">'
                                 f'<div style="flex:none;width:150px;height:150px;border-radius:50%;background:{bg};border:6px solid {CARVAO};display:grid;place-items:center;box-shadow:8px 8px 0 {CARVAO}">'
                                 + BAGEL(n, 90, fg, 1) + '</div>'
                                 f'<div style="flex:1;background:#fff;border:5px solid {CARVAO};padding:18px 26px;box-shadow:8px 8px 0 {CARVAO}">'
                                 + MONO(f'semana {n}', 16, TOMATE) + f'<div style="font:400 39px/1.02 \'Bagel Fat One\';text-transform:uppercase;color:{CARVAO};margin-top:4px">{t}</div></div>'
                                 f'<div style="flex:none;width:64px;height:64px;border:6px solid {CARVAO};border-radius:12px;background:#fff"></div></div>')
stor('d27-08h-resumo-do-mes',
     BOX(0, 0, 1080, 1920, CREME) + BOX(0, 0, 1080, 2000, padrao(VERDE, .12, 300)) +
     BOX(0, 0, 1080, 120, xadrez(VERDE, CREME, 30), f'border-bottom:6px solid {CARVAO}') +
     A(44, 160, BAGEL('Resumo', 250, VERDE, .86, SH(CARVAO, 10))) +
     A(44, 380, BAGEL('do mês.', 250, TOMATE, .86, SH(CARVAO, 10))) +
     A(48, 640, ANTON('O que mudou no seu perfil?', 82, CARVAO, .95)) +
     A(810, 1540, SEL(230, 'RESUMO DO MÊS · MÉTODO ORÉGANO · ', TOMATE, CREME, 12)) +
     BOX(118, 790, 10, 820, CARVAO) +
     A(44, 780, f'<div style="display:flex;flex-direction:column;gap:46px;width:990px">'
                + sem('1', 'Link do zap na bio', VERDE, CREME, -1) + sem('2', 'Foto que dá fome', ACAFRAO, TOMATE, 1)
                + sem('3', 'Mensagem de volta', TOMATE, CREME, -1) + sem('4', '3 posts fixados', CARVAO, ACAFRAO, 1) + '</div>') +
     A(60, 1650, adesivo('Marque o que você fez ✓', VERDE, CREME, -3, 40)) +
     ASS_STORY())
COMP['d27-08h-resumo-do-mes'] = 'Linha do tempo das 4 semanas com bolas numeradas e caixas de marcar + faixa de xadrez no topo + selo; creme com padrão verde'

# ================================================================== d27 12h · CARROSSEL 10 IDEIAS DE POST PRA PIZZARIA (capa + 2 telas)
feed('d27-12h-10-ideias-de-post-1-capa',
     FUNDO(TOMATE, CREME, .1) +
     A(-30, 120, BAGEL('10', 860, ACAFRAO, .9, SH(CARVAO, 18))) +
     A(44, 40, MONO('Dica pronta · carrossel', 20, CREME, f'background:{VERDE};padding:10px 14px;box-shadow:6px 6px 0 {CARVAO}')) +
     A(40, 760, BAGEL('ideias de post', 136, CREME, .9, SH(CARVAO, 8))) +
     A(46, 900, ANTON('pra pizzaria', 140, CARVAO, .9, f'background:{ACAFRAO};padding:4px 22px 0;transform:rotate(-2deg);box-shadow:10px 10px 0 {CARVAO}')) +
     A(770, 110, SEL(250, 'SALVE E USE · SÓ PIZZARIAS · ', VERDE, CREME, 12, centro=icone('pizza', 90, CREME, 6))) +
     A(60, 1110, adesivo('Salve e use ↓', CREME, TOMATE, -4, 40)) +
     A(640, 1120, adesivo('Arrasta →', CARVAO, ACAFRAO, 5, 40)) +
     tarja_ass(1258, CARVAO, CREME, '1/3 · @oreganoturbo'))
ideia = lambda n, t, ex, bg, fg: (f'<div style="display:flex;align-items:center;gap:26px;background:{bg};border:5px solid {CARVAO};box-shadow:10px 10px 0 {CARVAO};padding:28px 26px">'
                                  + BAGEL(n, 124, fg, .9, f'width:150px;text-align:center;{SH(CARVAO, 5)}') +
                                  f'<div><div style="font:400 50px/1 \'Bagel Fat One\';text-transform:uppercase;color:{fg if bg != CREME else CARVAO}">{t}</div>'
                                  f'<div style="font:600 29px/1.3 Inter;color:{CREME if bg in (VERDE, TOMATE, CARVAO) else CARVAO};margin-top:6px">{ex}</div></div></div>')
feed('d27-12h-10-ideias-de-post-2',
     FUNDO(CREME, VERDE, .1) +
     A(44, 34, BAGEL('Ideias 1 a 5', 120, VERDE, .9, SH(CARVAO, 6))) +
     A(44, 180, f'<div style="display:flex;flex-direction:column;gap:22px;width:990px">'
                + ideia('1', 'Forno acendendo', 'Story das 18h: “forno aceso, pode pedir”.', TOMATE, ACAFRAO)
                + ideia('2', 'Queijo puxando', 'Vídeo curto, câmera lenta, perto da fatia.', ACAFRAO, TOMATE)
                + ideia('3', 'Bastidor da massa', 'Mão na farinha, abrindo o disco.', VERDE, ACAFRAO)
                + ideia('4', 'Enquete de sabor', '“Calabresa ou portuguesa?” no story.', CARVAO, ACAFRAO)
                + ideia('5', 'Cliente fiel do mês', 'Só com autorização dele, por escrito.', CREME, TOMATE) + '</div>') +
     tarja_ass(1258, VERDE, CREME, '2/3 · salve e use · @oreganoturbo'))
nota = lambda n, t, ex, bg, fg, rot: (f'<div style="width:470px;height:300px;background:{bg};border:5px solid {CARVAO};box-shadow:12px 12px 0 {CARVAO};transform:rotate({rot}deg);padding:22px 26px;position:relative">'
                                      f'<div style="position:absolute;left:180px;top:-22px;width:110px;height:36px;background:rgba(243,238,230,.85);border:3px solid rgba(20,19,17,.25);transform:rotate(-4deg)"></div>'
                                      + BAGEL(n, 90, fg, .9, SH(CARVAO, 5)) +
                                      f'<div style="font:400 34px/1 \'Bagel Fat One\';text-transform:uppercase;color:{fg};margin-top:8px">{t}</div>'
                                      f'<div style="font:600 22px/1.3 Inter;color:{fg};margin-top:6px;opacity:.95">{ex}</div></div>')
feed('d27-12h-10-ideias-de-post-3',
     FUNDO(VERDE, CREME, .1) +
     A(44, 30, BAGEL('Ideias 6 a 10', 116, CREME, .9, SH(CARVAO, 6))) +
     A(50, 200, nota('6', 'Combo do dia fraco', 'Terça com borda grátis ou bebida.', ACAFRAO, CARVAO, -3)) +
     A(560, 220, nota('7', 'Borda ou sem borda?', 'Pergunta simples puxa comentário.', TOMATE, CREME, 3)) +
     A(50, 560, nota('8', 'Motoboy saindo', 'Pedido saindo quente, com a caixa.', CREME, CARVAO, 2)) +
     A(560, 580, nota('9', 'Resposta a avaliação', 'Agradeça a nota boa em público.', CARVAO, ACAFRAO, -2)) +
     A(300, 910, nota('10', 'Cardápio fixado', 'Post com preço, fixo no topo.', ACAFRAO, TOMATE, -1)) +
     A(30, 1150, adesivo('Quer ajuda? Chama no zap ↗', TOMATE, CREME, -3, 34)) +
     A(640, 1170, adesivo('Salve ✓', CREME, VERDE, 5, 34)) +
     tarja_ass(1258, CARVAO, CREME, '3/3 · @oreganoturbo'))
COMP['d27-12h-10-ideias-de-post-1-capa'] = 'Capa: número "10" gigante atrás da manchete (palavra gigante atrás) + tarja açafrão girada + selo + adesivos "salve" e "arrasta"; tomate'
COMP['d27-12h-10-ideias-de-post-2'] = 'Tela 2: lista em 5 cartões de cor com número gordo (cardápio de ideias); creme com padrão verde'
COMP['d27-12h-10-ideias-de-post-3'] = 'Tela 3: 5 notas coladas com fita, giradas, em cores alternadas + adesivos de chamada; verde'

# ================================================================== d28 19h · SEMANA QUE VEM TEM MAIS. (feed grade de 4 cores)
def q(x, y, bg, fg, palavra, rot, rotulo, ic, icx, icy, fonte=BAGEL, s=260, lx=30):
    return BOX(x, y, 540, 675, bg, 'overflow:hidden',
               f'<div class="a" style="inset:0;background:{padrao(fg, .14, 240)}"></div>'
               + A(icx, icy, f'<div style="transform:rotate({rot * 4}deg);opacity:.85">{icone(ic, 330, fg, 5)}</div>')
               + A(22, 30, FIT(fonte(palavra, s, fg, .84, SH(CARVAO, 8)), 496, f'transform:rotate({rot}deg)'))
               + A(lx, 616, MONO(rotulo, 15, CREME, f'background:{CARVAO};padding:7px 10px')))
feed('d28-19h-semana-que-vem-tem-mais',
     BOX(0, 0, 1080, 675, TOMATE, 'overflow:hidden', f'<div class="a" style="inset:0;background:{padrao(CREME, .12, 260)}"></div>'
         + A(700, 250, f'<div style="transform:rotate(-14deg);opacity:.85">{icone("fatia", 360, CREME, 5)}</div>')) +
     A(30, 40, FIT(BAGEL('Semana', 270, CREME, .84, SH(CARVAO, 10)), 1020)) +
     A(40, 300, BAGEL('que vem', 150, ACAFRAO, .86, SH(CARVAO, 8))) +
     A(44, 600, MONO('seg a dom · 3 postagens por dia', 15, CREME, f'background:{CARVAO};padding:7px 10px')) +
     q(0, 675, VERDE, CREME, 'Tem', -3, 'dicas · contas · cultura', 'chama', 230, 330, BAGEL, 300) +
     q(540, 675, CREME, TOMATE, 'Mais.', 4, 'dom · resumo da semana', 'pizza', 250, 310, BAGEL, 230, 200) +
     BOX(0, 668, 1080, 14, CARVAO) + BOX(533, 675, 14, 675, CARVAO) +
     A(420, 555, selo(240, 'SIGA @OREGANOTURBO · SÓ PIZZARIAS · ', CARVAO, CREME)) +
     A(560, 1170, adesivo('Siga @oreganoturbo ↗', TOMATE, CREME, -4, 34)))
COMP['d28-19h-semana-que-vem-tem-mais'] = 'v4: faixa tomate inteira com SEMANA gigante + 2 quadros (verde TEM, creme MAIS.); antes era grade de 4 cores com a manchete quebrada em 4 quadros (SEMANA / QUE VEM / TEM / MAIS.), ícone em traço gigante em cada um + selo central (p03 v3, Drip Riot); v4: só cores da paleta (tomate, carvão, verde, creme)'

CSS2 = CSS + 'section.f>.a:first-child{}'
open(os.path.join(D, 'pecas.html'), 'w', encoding='utf-8').write(
    f'<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>{CSS2}</style>{FIT_JS}</head><body>' +
    ''.join(f'<section class="f" id="{i}" style="width:{w}px;height:{h}px">{c}</section>' for i, w, h, c in P) + '</body></html>')
import json
json.dump(COMP, open(os.path.join(D, 'composicoes.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(P), 'peças')
