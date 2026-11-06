# Artes TIPOGRÁFICAS das semanas 1 e 2 do calendário do @oreganoturbo (dias 1 a 14, 19 peças)
# Paollo (conta Leandro), 06/11/2026. Fonte das pautas: ../../calendario.json (coluna imagem = "TIPO").
# Padrão: kit v3 aprovado pelo Lindson ("AGORA SIM, ESSE É O PADRÃO"), ../../../v3/.
# Regra "imagem só uma vez": as fotos acabaram (../../../FOTOS-USADAS.md), então NENHUMA foto aqui.
# O impacto vem do sistema da marca: manchete gorda gigante, cor chapada, xadrez, selos, estrela, adesivos,
# faixas em loop, ícones em traço, celular / WhatsApp / calculadora / relatório desenhados em HTML.
# As funções de marca (símbolo, logo, selo, padrão de ícones, xadrez, adesivo, estrela, faixa, tarja, letras)
# são as MESMAS do v3/gerar.py: o bloco de funções é lido de lá e executado aqui (sem gerar nada no v3).
# Uso: python3 gerar_s12.py && node render.js && python3 previa.py
import os, re, math
D = os.path.dirname(os.path.abspath(__file__))
V3 = os.path.normpath(os.path.join(D, '../../../v3/gerar.py'))
src = open(V3, encoding='utf-8').read()
exec(src[:src.index('# ================================================================== 01')])  # funções do v3
exec(src[src.index('GRAO_SVG = '):src.index("open(os.path.join(D, 'pecas.html')")])  # CSS e grão do v3

WA_VERDE, WA_BALAO, WA_FUNDO = '#075E54', '#D9FDD3', '#EFE7DC'
P = []
post = lambda i, h: P.append((i, 1080, 1350, h + GRAO))
story = lambda i, h: P.append((i, 1080, 1920, h + GRAO))
pad = lambda cor, op=.13, tam=300: f'<div class="a" style="inset:0;background:{padrao(cor, op, tam)}"></div>'
ILU = lambda cor=CARVAO, bg=ACAFRAO, s=16: MONO('Exemplo ilustrativo', s, cor, f'background:{bg};padding:8px 12px;box-shadow:5px 5px 0 {CARVAO}')
GIRA = lambda deg, inner: f'<div style="transform:rotate({deg}deg)">{inner}</div>'

def icone(n, tam=80, cor=CREME, w=6):
    return (f'<svg viewBox="0 0 100 100" width="{tam}" height="{tam}" style="display:block"><g fill="none" stroke="{cor}" stroke-width="{w}" '
            f'stroke-linecap="round" stroke-linejoin="round">{IC[n]}</g></svg>')

IC.update({
 'olho': '<path d="M8 50 Q50 10 92 50 Q50 90 8 50 Z"/><circle cx="50" cy="50" r="14"/>',
 'relogio': '<circle cx="50" cy="50" r="38"/><path d="M50 26 L50 50 L66 60"/>',
 'zap': '<path d="M50 12 A38 38 0 1 1 26 80 L12 88 L18 72 A38 38 0 0 1 50 12 Z"/><path d="M38 34 C 36 46 48 60 62 64 L68 56 L60 50 L55 54 C 50 52 46 48 44 43 L48 38 L42 30 Z"/>',
 'preco': '<path d="M14 48 L48 14 L86 14 L86 52 L52 86 Z"/><circle cx="70" cy="30" r="6"/>',
 'regua': '<rect x="10" y="34" width="80" height="32" rx="4"/><path d="M24 34 L24 48 M38 34 L38 52 M52 34 L52 48 M66 34 L66 52 M80 34 L80 48"/>',
 'mais': '<circle cx="50" cy="50" r="38"/><path d="M50 32 L50 68 M32 50 L68 50"/>',
 'camera': '<rect x="10" y="28" width="80" height="56" rx="10"/><circle cx="50" cy="56" r="16"/><path d="M34 28 L40 16 L60 16 L66 28"/>',
 'moto': '<circle cx="24" cy="70" r="12"/><circle cx="78" cy="70" r="12"/><path d="M24 70 L44 70 L56 46 L72 46 L78 70 M50 46 L44 30 L32 30"/>',
 'gota': '<path d="M50 12 C 64 34 76 48 76 62 A26 26 0 0 1 24 62 C 24 48 36 34 50 12 Z"/>',
 'copo': '<path d="M26 18 L74 18 L66 90 L34 90 Z"/><path d="M28 36 L72 36"/><path d="M56 18 L64 4"/>',
 'coracao': '<path d="M50 84 C 10 58 12 24 34 22 C 44 21 50 30 50 36 C 50 30 56 21 66 22 C 88 24 90 58 50 84 Z"/>',
})

def celular(inner, w=520, h=1040, bg='#fff', rot=0, extra=''):
    """iPhone desenhado: moldura carvão, ilha, tela com conteúdo."""
    return (f'<div style="position:relative;width:{w}px;height:{h}px;border-radius:{w * .14:.0f}px;background:{CARVAO};padding:{w * .035:.0f}px;'
            f'transform:rotate({rot}deg);box-shadow:0 0 0 6px {CREME},22px 26px 0 6px rgba(20,19,17,.35);{extra}">'
            f'<div style="position:relative;width:100%;height:100%;border-radius:{w * .11:.0f}px;background:{bg};overflow:hidden">{inner}'
            f'<div style="position:absolute;left:50%;top:{w * .03:.0f}px;width:{w * .3:.0f}px;height:{w * .07:.0f}px;margin-left:-{w * .15:.0f}px;border-radius:99px;background:{CARVAO}"></div>'
            f'</div></div>')

def wa_topo(nome, sub='online', s=1.0):
    return (f'<div style="background:{WA_VERDE};padding:{70 * s:.0f}px {24 * s:.0f}px {18 * s:.0f}px;display:flex;align-items:center;gap:{14 * s:.0f}px">'
            f'<div style="font:700 {30 * s:.0f}px Inter;color:#fff">‹</div>'
            f'<div style="width:{58 * s:.0f}px;height:{58 * s:.0f}px;border-radius:50%;background:{CREME};display:grid;place-items:center">{simbolo(40 * s, VERDE, CREME)}</div>'
            f'<div><div style="font:700 {26 * s:.0f}px/1.1 Inter;color:#fff">{nome}</div><div style="font:500 {17 * s:.0f}px Inter;color:#cfe">{sub}</div></div></div>')

def balao(t, eu, hora, s=1.0, maxw=82):
    return (f'<div style="align-self:{"flex-end" if eu else "flex-start"};max-width:{maxw}%;background:{WA_BALAO if eu else "#fff"};'
            f'border-radius:{20 * s:.0f}px;{"border-top-right-radius:4px" if eu else "border-top-left-radius:4px"};padding:{14 * s:.0f}px {18 * s:.0f}px {8 * s:.0f}px;'
            f'box-shadow:0 2px 0 rgba(0,0,0,.12)"><div style="font:500 {25 * s:.0f}px/1.32 Inter;color:{CARVAO}">{t}</div>'
            f'<div style="font:500 {14 * s:.0f}px Inter;color:#667;text-align:right;margin-top:4px">{hora}</div></div>')

def wa_tela(baloes, s=1.0, nome='Pizzaria do Bairro', sub='online'):
    return (wa_topo(nome, sub, s) +
            f'<div style="position:absolute;left:0;right:0;top:{150 * s:.0f}px;bottom:0;background:{WA_FUNDO} {padrao("#8a7f6e", .18, 220)};'
            f'padding:{24 * s:.0f}px {18 * s:.0f}px;display:flex;flex-direction:column;gap:{14 * s:.0f}px">{baloes}</div>')

def copia_cola(rot=-8, s=40, bg=ACAFRAO, fg=CARVAO):
    """Adesivo 'copia e cola' com tesoura e borda tracejada de recorte."""
    return (f'<div style="transform:rotate({rot}deg);background:{bg};padding:18px 30px;border:5px dashed {fg};border-radius:22px;'
            f'box-shadow:0 0 0 8px {CREME},12px 14px 0 8px rgba(20,19,17,.3);display:flex;align-items:center;gap:14px">'
            f'<span style="font:400 {s * 1.1:.0f}px/1 Inter;color:{fg}">✂</span>{BAGEL("Copia e cola", s, fg, 1)}</div>')

def checkbox(ok=True, tam=54, bg=ACAFRAO, fg=CARVAO):
    return (f'<div style="width:{tam}px;height:{tam}px;flex:none;border-radius:12px;background:{bg};border:4px solid {fg};display:grid;place-items:center;'
            f'font:800 {tam * .62:.0f}px/1 Inter;color:{fg}">{"✓" if ok else "✕"}</div>')

def xis(tam=140, cor=TOMATE, rot=-8):
    return (f'<svg viewBox="0 0 100 100" width="{tam}" height="{tam}" style="display:block;transform:rotate({rot}deg);filter:drop-shadow(6px 7px 0 rgba(20,19,17,.35))">'
            f'<path d="M18 18 L82 82 M82 18 L18 82" stroke="{CREME}" stroke-width="30" stroke-linecap="round"/>'
            f'<path d="M18 18 L82 82 M82 18 L18 82" stroke="{cor}" stroke-width="18" stroke-linecap="round"/></svg>')

def enquete(pergunta, opcoes, w=900, cor_topo=TOMATE):
    ops = ''.join(f'<div style="display:flex;justify-content:space-between;align-items:center;border:3px solid #E4E1DB;border-radius:24px;padding:24px 30px;margin-top:14px;'
                  f'font:700 38px Inter;color:{CARVAO}"><span>{o}</span><span style="width:38px;height:38px;border-radius:50%;border:4px solid {VERDE}"></span></div>' for o in opcoes)
    return (f'<div style="width:{w}px;background:#fff;border-radius:38px;overflow:hidden;box-shadow:0 0 0 8px {CREME},18px 20px 0 8px rgba(20,19,17,.35)">'
            f'<div style="background:{cor_topo};padding:30px 34px;font:800 46px/1.1 \'Inter Tight\';letter-spacing:-.02em;color:{CREME};text-align:center">{pergunta}</div>'
            f'<div style="padding:12px 34px 34px">{ops}</div></div>')

def rodape_zap(y, bg=CARVAO, fg=CREME, chamada='Chama no zap ↗', cor_chamada=ACAFRAO, h=110, w=1080):
    return BOX(0, y, w, h, bg, f'display:flex;align-items:center;justify-content:space-between;padding:0 52px;border-top:6px solid {CARVAO}',
               f'<div>{logo(36, fg)}<div style="margin-top:8px">{MONO("@oreganoturbo · só pizzarias", 15, fg, "opacity:.85")}</div></div>'
               + f'<div style="background:{cor_chamada};padding:16px 26px;border-radius:999px;box-shadow:0 0 0 5px {fg}">{BAGEL(chamada, 34, CARVAO if cor_chamada in (ACAFRAO, CREME) else CREME, 1)}</div>')

def arco_forno(w=760, h=620, cor=CARVAO, boca=TOMATE):
    """Arco do forno a lenha com tijolos e chama (símbolo de pizzaria)."""
    tij = ''.join(f'<path d="M{50 + 46 * math.cos(math.pi - a):.1f} {56 - 46 * math.sin(a):.1f} L{50 + 34 * math.cos(math.pi - a):.1f} {56 - 34 * math.sin(a):.1f}" '
                  f'stroke="{CREME}" stroke-width="1.6"/>' for a in [math.pi * i / 10 for i in range(1, 10)])
    return (f'<svg viewBox="0 0 100 82" width="{w}" height="{h}" style="display:block;overflow:visible">'
            f'<path d="M2 82 L2 56 A48 48 0 0 1 98 56 L98 82 Z" fill="{cor}"/>'
            f'<path d="M16 82 L16 56 A34 34 0 0 1 84 56 L84 82 Z" fill="{boca}"/>'
            f'{tij}'
            f'<path d="M50 80 C 34 80 31 66 41 56 C 41 64 46 66 48 61 C 48 52 54 45 52 37 C 63 46 67 59 63 68 C 61 76 56 80 50 80 Z" fill="{ACAFRAO}" stroke="{CARVAO}" stroke-width="1.4"/>'
            f'<path d="M50 80 C 44 80 42 74 46 69 C 47 73 50 73 51 70 C 52 66 55 64 55 60 C 59 66 59 72 57 76 C 55 79 53 80 50 80 Z" fill="{CREME}"/>'
            f'<rect x="0" y="79" width="100" height="3" fill="{CREME}"/></svg>')

# ================================================================ d01 08h · BOM DIA, FORNO. (story, tomate + arco do forno)
# Copia: arco do forno a lenha com chama (Bella Pizza, biblioteca) + cartaz retrô de título gordo (retro-13) + xadrez de cantina.
story('d01-08h-bom-dia-forno',
      BOX(0, 0, 1080, 1920, TOMATE) + pad(CREME, .12) +
      BOX(0, 0, 1080, 150, xadrez(CREME, TOMATE, 38), f'border-bottom:8px solid {CARVAO}') +
      A(40, 196, MONO('Seg · 09/11 · 08h · abre o forno', 22, CREME, f'background:{CARVAO};padding:10px 14px;box-shadow:6px 6px 0 rgba(0,0,0,.25)')) +
      A(30, 260, BAGEL('Bom dia,', 200, CREME, .9, SH(CARVAO, 10))) +
      A(24, 452, BAGEL('forno.', 300, ACAFRAO, .9, SH(CARVAO, 13))) +
      A(160, 820, arco_forno(760, 620)) +
      A(40, 760, GIRA(-10, estrela(250, ACAFRAO, ANTON('Bora<br>vender', 58, TOMATE, .9)))) +
      A(790, 760, GIRA(12, selo(240, 'SEGUNDA COMEÇA NO BALCÃO · ', VERDE, CREME))) +
      faixa('bom dia, pizzaria', 1440, CREME, VERDE, -4, 104, 62) +
      A(46, 1592, ANTON('Segunda começa<br>no balcão.', 92, CREME, .92, SH(CARVAO, 6))) +
      A(640, 1640, adesivo('Bora vender ↗', ACAFRAO, CARVAO, -6, 42)) +
      tarja_ass(1828, CARVAO, CREME, '@oreganoturbo · só pizzarias'))

# ================================================================ d02 19h · 5 FOTOS QUE TIRAM A FOME (feed, verde, cartões com X)
# Copia: checklist em cartões girados (polaroids) com carimbo de X vermelho (Pizzino, busca-31: adesivos girados) + padrão de ícones.
def polaroid(n, palavra, tela, rot, w=300):
    return (f'<div style="width:{w}px;background:{CREME};padding:16px 16px 18px;transform:rotate({rot}deg);border:4px solid {CARVAO};box-shadow:12px 14px 0 rgba(20,19,17,.4)">'
            f'<div style="position:relative;height:{w * .62:.0f}px;background:{tela};overflow:hidden;border:3px solid {CARVAO}">'
            f'<div style="position:absolute;inset:0;display:grid;place-items:center">{icone("pizza", w * .42, "rgba(243,238,230,.55)", 5)}</div></div>'
            f'<div style="display:flex;align-items:baseline;gap:10px;margin-top:12px">{MONO(f"Nº{n}", 15, TOMATE)}{ANTON(palavra, 44, CARVAO, .9)}</div></div>')
fotos5 = [('1', 'Escura', 'linear-gradient(160deg,#2a221c,#0c0a09)', -6, 40, 370),
          ('2', 'De longe', f'{CREME} radial-gradient(circle at 50% 55%,#b8543b 0 6%,transparent 7%)', 5, 380, 350),
          ('3', 'Sem queijo', 'linear-gradient(160deg,#9c6b3d,#6e4524)', -3, 720, 390),
          ('4', 'Fria', 'linear-gradient(160deg,#8fa3ad,#55666f)', 4, 70, 750),
          ('5', 'Cortada', f'linear-gradient(90deg,#b8543b 0 38%,{CREME} 38%)', -5, 420, 770)]
cards5 = ''.join(A(x, y, polaroid(n, p, t, r)) + A(x + 190, y - 34, xis(130, TOMATE, r * 2)) for n, p, t, r, x, y in fotos5)
post('d02-19h-5-fotos-que-tiram-a-fome',
     BOX(0, 0, 1080, 1350, VERDE) + pad(CREME, .1) +
     A(40, 34, BAGEL('5 fotos', 168, ACAFRAO, .88, SH(CARVAO, 9))) +
     A(46, 196, ANTON('que tiram a fome.', 100, CREME, .9, SH(CARVAO, 6))) +
     A(830, 24, GIRA(10, selo(210, 'EVITE · EVITE · EVITE · EVITE · ', TOMATE, CREME, centro=xis(90, CARVAO, 0)))) +
     cards5 +
     faixa('escura ✕ de longe ✕ sem queijo ✕ fria ✕ cortada', 1120, TOMATE, CREME, -2, 86, 48, sep='✕') +
     A(770, 790, GIRA(-8, f'<div style="background:{ACAFRAO};border:5px solid {CARVAO};padding:22px 26px;box-shadow:12px 14px 0 {CARVAO};width:270px">'
                      + BAGEL('Salva', 54, TOMATE, .9) + TXT('e confere antes de postar a próxima.', 22, CARVAO, 'margin-top:8px') + '</div>')) +
     rodape_zap(1240, CARVAO, CREME, 'Quer foto que dá fome? ↗'))

# ================================================================ d03 08h · RESPONDE ASSIM: (story, açafrão + celular de WhatsApp)
# Copia: conversa de WhatsApp desenhada (kit v1 e story 3 v3) + adesivo "copia e cola" girado (Pizzino) + faixa xadrez.
chat_entrega = wa_tela(
    balao('Boa noite! Qual o valor da entrega pro Cohatrac?', False, '19:41', 1.05) +
    balao('Boa noite! Pro Cohatrac a entrega fica <b>R$ __</b> e chega quentinha em até <b>__ min</b>. Já quer que eu anote o seu pedido?', True, '19:41 ✓✓', 1.05) +
    balao('Quero sim! Uma calabresa grande', False, '19:42', 1.05), 1.0)
story('d03-08h-responde-assim',
      BOX(0, 0, 1080, 1920, ACAFRAO) + pad(CARVAO, .09) +
      BOX(0, 1180, 1080, 740, xadrez(TOMATE, CREME, 40)) +
      A(40, 120, MONO('Dica pronta · WhatsApp da pizzaria', 22, CREME, f'background:{VERDE};padding:10px 14px;box-shadow:6px 6px 0 {CARVAO}')) +
      A(30, 186, BAGEL('Responde', 196, TOMATE, .9, SH(CARVAO, 10))) +
      A(34, 380, BAGEL('assim:', 196, CARVAO, .9, SH(CREME, 8))) +
      A(470, 580, GIRA(-5, f'<div style="width:560px;background:{CREME};border:5px solid {CARVAO};box-shadow:10px 12px 0 {CARVAO};padding:18px 22px">'
                       + MONO('Pergunta que mais chega:', 15, TOMATE) + ANTON('"Qual o valor<br>da entrega?"', 56, CARVAO, .95, 'margin-top:8px') + '</div>')) +
      A(70, 800, celular(chat_entrega, 640, 900, WA_FUNDO, -3)) +
      A(560, 1330, copia_cola(8, 44)) +
      A(640, 1500, GIRA(-4, f'<div style="width:380px;background:{VERDE};border:5px solid {CARVAO};box-shadow:10px 12px 0 {CARVAO};padding:20px 22px">'
                        + ANTON('Troque o bairro, o valor e o tempo.', 40, CREME, 1, 'white-space:normal') + '</div>')) +
      A(640, 1740, ILU()) +
      tarja_ass(1828, CARVAO, CREME, '@oreganoturbo · chama no zap'))

# ================================================================ d03 19h · A CONTA DO PEDIDO (feed, cardápio-cartaz 2 colunas + estrela)
# Copia: cardápio-cartaz retrô (Jonny's Pizza retro-14, menu busca-34) com duas colunas e explosão de total (Retro Pizza retro-13).
def coluna(titulo, cor, linhas, total, total_cor):
    li = ''.join(f'<div style="display:flex;align-items:baseline;gap:10px;padding:14px 0;border-bottom:3px dashed rgba(20,19,17,.22)">'
                 f'<span style="font:400 34px/1 Anton;text-transform:uppercase;color:{CARVAO};white-space:nowrap">{a}</span>'
                 f'<span style="flex:1;border-bottom:3px dotted {CARVAO};opacity:.45;transform:translateY(-6px)"></span>'
                 f'<span style="font:600 26px \'IBM Plex Mono\';color:{c};white-space:nowrap">{b}</span></div>' for a, b, c in linhas)
    return (f'<div style="width:450px;background:{CREME};border:6px solid {CARVAO};box-shadow:14px 14px 0 {CARVAO}">'
            f'<div style="background:{cor};padding:18px 24px;border-bottom:6px solid {CARVAO}">{BAGEL(titulo, 74, CREME, .95, SH(CARVAO, 5))}</div>'
            f'<div style="padding:8px 26px 22px">{li}'
            f'<div style="margin-top:18px">{MONO("Fica com você", 16, TOMATE)}</div>{BAGEL(total, 72, total_cor, 1)}</div></div>')
post('d03-19h-a-conta-do-pedido',
     BOX(0, 0, 1080, 1350, xadrez(VERDE, CREME, 34)) +
     BOX(36, 36, 1008, 1278, CREME, f'border:6px solid {CARVAO};box-shadow:14px 14px 0 {CARVAO}') + BOX(42, 42, 996, 1266, padrao(VERDE, .13, 260)) +
     A(36, 70, MONO('Dinheiro do delivery · a mesma pizza', 18, CARVAO), 'width:1008px;display:flex;justify-content:center') +
     A(36, 106, BAGEL('A conta', 190, TOMATE, .9, SH(CARVAO, 9)), 'width:1008px;display:flex;justify-content:center') +
     A(80, 300, ANTON('do pedido', 110, VERDE, .9)) +
     A(76, 470, GIRA(-2, coluna('No app', TOMATE, [('Pizza grande', 'R$ 60,00', CARVAO), ('Comissão (20%)', '− R$ 12,00', TOMATE), ('Cliente', 'do app', TOMATE)], 'R$ 48,00', TOMATE))) +
     A(556, 500, GIRA(2, coluna('No zap', VERDE, [('Pizza grande', 'R$ 60,00', CARVAO), ('Comissão', 'R$ 0,00', VERDE), ('Cliente', 'seu', VERDE)], 'R$ 60,00', VERDE))) +
     A(800, 250, estrela(230, ACAFRAO, MONO('diferença', 16, CARVAO) + BAGEL('+R$12', 56, TOMATE, .95) + MONO('por pedido', 14, CARVAO), 10)) +
     A(64, 1040, ILU(CREME, CARVAO)) +
     A(64, 1094, TXT('Números de exemplo, para fazer a conta. Taxa de cartão e entrega entram nos dois lados.', 21, CARVAO, 'width:520px;line-height:1.3')) +
     A(640, 1060, adesivo('Faz a sua conta ↗', TOMATE, CREME, -5, 36)) +
     BOX(42, 1204, 996, 104, VERDE, f'border-top:6px solid {CARVAO};display:flex;align-items:center;justify-content:space-between;padding:0 34px',
         logo(34, CREME) + MONO('chama no zap · @oreganoturbo', 18, ACAFRAO)))

# ================================================================ d04 08h · SEGUNDA, 8H. (story, carvão + celular com relatório)
# Copia: tela de bloqueio com notificação + painel de números (interface, "delivery está ON" da biblioteca) + palavra gigante atrás.
barras = [('S', 38), ('T', 22), ('Q', 30), ('Q', 46), ('S', 88), ('S', 100), ('D', 72)]
graf = ''.join(f'<div style="display:flex;flex-direction:column;align-items:center;gap:8px;flex:1"><div style="width:100%;height:{v * 1.7:.0f}px;'
               f'background:{TOMATE if i < 3 else VERDE};border-radius:8px 8px 0 0"></div>{MONO(d, 14, CARVAO, "letter-spacing:0")}</div>' for i, (d, v) in enumerate(barras))
relatorio = (
    f'<div style="position:absolute;inset:0;background:linear-gradient(180deg,{VERDE_ESC},{VERDE})"></div>'
    f'<div style="position:absolute;left:0;right:0;top:70px;text-align:center">{ANTON("08:00", 150, CREME, 1)}{MONO("segunda-feira, 16 de novembro", 15, CREME, "opacity:.8;margin-top:6px")}</div>'
    f'<div style="position:absolute;left:22px;right:22px;top:300px;background:rgba(243,238,230,.96);border-radius:26px;padding:18px 20px;display:flex;gap:14px;align-items:center">'
    f'<div style="width:56px;height:56px;border-radius:14px;background:{VERDE};display:grid;place-items:center;flex:none">{simbolo(38, CREME, VERDE)}</div>'
    f'<div><div style="font:700 19px Inter;color:{CARVAO}">Orégano Turbo · agora</div><div style="font:500 19px/1.3 Inter;color:{CARVAO}">Seu relatório da semana chegou.</div></div></div>'
    f'<div style="position:absolute;left:22px;right:22px;top:420px;bottom:30px;background:{CREME};border-radius:26px;padding:22px 22px">'
    f'{MONO("Relatório de segunda · ilustrativo", 14, TOMATE)}'
    f'<div style="display:flex;gap:12px;margin-top:14px">'
    + ''.join(f'<div style="flex:1;background:{bg};border-radius:16px;padding:12px 14px">{MONO(t, 12, fg, "letter-spacing:.06em")}{BAGEL(v, 44, fg, 1)}</div>'
              for t, v, bg, fg in [('pedidos no zap', '42', VERDE, CREME), ('código + pedido', 'PZ14', ACAFRAO, CARVAO)]) +
    f'</div><div style="display:flex;align-items:flex-end;gap:8px;height:200px;margin-top:22px">{graf}</div>'
    f'<div style="margin-top:14px;font:600 18px/1.35 Inter;color:{CARVAO}">Próxima semana: reforçar <b style="color:{TOMATE}">terça</b>.</div></div>')
story('d04-08h-segunda-8h',
      BOX(0, 0, 1080, 1920, CARVAO) + pad(CREME, .07) +
      A(-40, 470, BAGEL('8h', 900, VERDE, .9, 'letter-spacing:-.02em;opacity:.95')) +
      A(40, 120, MONO('Método Orégano · toda semana', 22, CARVAO, f'background:{ACAFRAO};padding:10px 14px')) +
      A(30, 186, BAGEL('Segunda,', 190, CREME, .9, SH(TOMATE, 9))) +
      A(36, 380, ANTON('o relatório chega<br>no seu celular.', 88, ACAFRAO, .92)) +
      A(470, 620, celular(relatorio, 560, 1110, VERDE, 4)) +
      A(40, 1060, GIRA(-10, selo(240, 'RELATÓRIO DE SEGUNDA · 08H · ', TOMATE, CREME, centro=icone('relogio', 90, CREME, 7)))) +
      A(40, 1360, adesivo('Sem planilha', ACAFRAO, CARVAO, -6, 36)) +
      A(60, 1470, adesivo('Leitura de<br>2 minutos', VERDE, CREME, 5, 32, '16px 24px', extra='border-radius:26px;line-height:1.05;text-align:center')) +
      A(40, 1640, ILU(CARVAO, CREME)) +
      tarja_ass(1828, TOMATE, CREME, '@oreganoturbo · chama no zap'))

# ================================================================ d04 19h · COMBO DE TERÇA (feed, açafrão, 3 cartões numerados + faixa)
# Copia: grade de cartões numerados (menu busca-34) + faixa em loop (Pizzino busca-31) + número gigante (biblioteca).
def cartao_combo(n, titulo, sub, bg, fg, ic, rot):
    return (f'<div style="width:316px;height:600px;background:{bg};border:6px solid {CARVAO};box-shadow:14px 16px 0 {CARVAO};transform:rotate({rot}deg);'
            f'position:relative;overflow:hidden;padding:22px 22px 26px;display:flex;flex-direction:column">'
            f'<div style="display:flex;justify-content:space-between;align-items:flex-start">{BAGEL(n, 170, fg, .85, SH(CARVAO, 6) if bg != CREME else "")}{icone(ic, 96, fg, 6)}</div>'
            f'{MONO("Combo nº" + n, 16, fg, "margin-top:10px")}<span style="flex:1"></span>'
            f'{ANTON(titulo, 58, fg, .95, "white-space:normal")}<div style="margin-top:14px">{TXT(sub, 21, fg, "line-height:1.3")}</div></div>')
post('d04-19h-combo-de-terca',
     BOX(0, 0, 1080, 1350, ACAFRAO) + pad(CARVAO, .09) +
     A(36, 30, BAGEL('Combo', 210, TOMATE, .86, SH(CARVAO, 10))) +
     A(44, 236, ANTON('de terça.', 120, CARVAO, .9)) +
     A(560, 254, MONO('3 ideias que não<br>desvalorizam a sua pizza', 17, CREME, f'line-height:1.45;background:{CARVAO};padding:12px 16px;transform:rotate(-3deg)')) +
     A(820, 36, GIRA(12, estrela(220, VERDE, ANTON('Sem<br>baixar<br>preço', 42, CREME, .9)))) +
     faixa('valor no combo, não no desconto', 400, CARVAO, ACAFRAO, -2, 92, 52) +
     A(40, 530, cartao_combo('1', 'Pizza + borda recheada', 'Mais sabor no mesmo pedido. O cliente sente que ganhou.', TOMATE, CREME, 'pizza', -3)) +
     A(382, 550, cartao_combo('2', 'Grande + refri da casa', 'Pra família da terça. Um pedido, mesa feita.', VERDE, CREME, 'copo', 2)) +
     A(724, 530, cartao_combo('3', 'Pizza + doce de brinde', 'Brinde pequeno, pizza no preço cheio.', CREME, CARVAO, 'coracao', -2)) +
     rodape_zap(1240, CARVAO, CREME, 'Monta o seu ↗', TOMATE))

# ================================================================ d05 19h · PENSO, LOGO PEÇO. (feed, tomate, manchete gigante + citação)
# Copia: capa de livro / citação tipográfica (aspas gigantes) + manchete em 2 tamanhos ("AQUI / não tem / ERRO") — sem personagem.
post('d05-19h-penso-logo-peco',
     BOX(0, 0, 1080, 1350, TOMATE) + pad(CREME, .1) +
     A(-20, -90, f'<div style="font:400 700px/1 \'Bagel Fat One\';color:{ACAFRAO};opacity:.95">“</div>') +
     A(46, 70, MONO('Filosofia de balcão · nº 1', 20, CREME, f'background:{CARVAO};padding:10px 14px')) +
     A(370, 150, BAGEL('Penso,', 196, CREME, .9, SH(CARVAO, 10))) +
     A(28, 448, ANTON('logo', 124, CARVAO, .9)) +
     BOX(290, 370, 760, 320, CREME, f'border:6px solid {CARVAO};box-shadow:16px 18px 0 {CARVAO};transform:rotate(-3deg);display:grid;place-items:center',
         BAGEL('peço.', 230, TOMATE, .9, SH(CARVAO, 8))) +
     A(600, 720, MONO('— seu cliente, sexta, 19h47', 20, CREME)) +
     A(40, 800, f'<div style="width:640px;background:{VERDE};border:6px solid {CARVAO};box-shadow:14px 14px 0 {CARVAO};padding:28px 30px">'
                + ANTON('Ele pede pra você ou pra quem apareceu primeiro?', 62, CREME, .98, 'white-space:normal') + '</div>') +
     A(740, 860, GIRA(12, selo(270, 'QUEM APARECE PRIMEIRO VENDE · ', ACAFRAO, CARVAO, centro=icone('celular', 100, CARVAO, 7)))) +
     faixa('aparece no bairro', 1120, CREME, TOMATE, -3, 92, 54) +
     rodape_zap(1240, CARVAO, CREME, 'Chama no zap ↗'))

# ================================================================ d06 08h · SEXTA LOTA. E SEGUNDA? (story, xadrez verde + caixinha)
# Copia: xadrez de cantina em tela cheia (La Verona busca-26, Jonny's retro-14) + figurinha de caixinha de perguntas do Instagram.
caixinha = (f'<div style="width:900px;background:#fff;border-radius:40px;overflow:hidden;box-shadow:0 0 0 8px {CARVAO},20px 22px 0 8px rgba(20,19,17,.4)">'
            f'<div style="background:{TOMATE};padding:40px 40px 34px;text-align:center">'
            f'<div style="width:96px;height:96px;margin:-6px auto 18px;border-radius:50%;background:{CREME};display:grid;place-items:center;box-shadow:0 0 0 5px {CARVAO}">{simbolo(64, VERDE, CREME)}</div>'
            f'<div style="font:800 54px/1.1 \'Inter Tight\';letter-spacing:-.02em;color:{CREME}">Qual o seu dia<br>mais fraco?</div></div>'
            f'<div style="padding:38px 40px 44px"><div style="background:#EEECE8;border-radius:24px;padding:34px;font:600 38px Inter;color:#8B877F;text-align:center">Escreve aqui…</div></div></div>')
story('d06-08h-sexta-lota-e-segunda',
      BOX(0, 0, 1080, 1920, xadrez(VERDE, CREME, 60)) +
      A(30, 110, f'<div style="background:{CARVAO};padding:18px 34px 22px;transform:rotate(-3deg);box-shadow:14px 14px 0 rgba(20,19,17,.35)">'
                 + BAGEL('Sexta lota.', 150, CREME, .95) + '</div>') +
      A(20, 340, f'<div style="background:{ACAFRAO};padding:14px 30px 24px;border:7px solid {CARVAO};transform:rotate(2deg);box-shadow:16px 16px 0 {CARVAO}">'
                 + BAGEL('E segunda?', 150, TOMATE, .95, SH(CARVAO, 9)) + '</div>') +
      A(90, 720, caixinha) +
      A(760, 600, GIRA(14, estrela(250, TOMATE, ANTON('Seg<br>Ter<br>Qua', 56, CREME, .9)))) +
      A(70, 1340, f'<svg width="220" height="160" viewBox="0 0 220 160"><path d="M20 20 C 60 130, 150 140, 190 70" fill="none" stroke="{CARVAO}" stroke-width="14" stroke-linecap="round"/>'
                  f'<path d="M160 60 L194 66 L186 100" fill="none" stroke="{CARVAO}" stroke-width="14" stroke-linecap="round" stroke-linejoin="round"/></svg>') +
      A(300, 1380, f'<div style="background:{CREME};border:6px solid {CARVAO};box-shadow:12px 12px 0 {CARVAO};padding:22px 28px;transform:rotate(-2deg);width:700px">'
                   + ANTON('Responde aí. A gente lê todas.', 62, VERDE, .95, 'white-space:normal') + '</div>') +
      faixa('dia fraco tem conserto', 1640, TOMATE, CREME, -3, 100, 60) +
      tarja_ass(1828, CARVAO, CREME, '@oreganoturbo · só pizzarias'))

# ================================================================ d06 19h · 3 ERROS NO LINK DA BIO (feed, verde, celular + setas + X)
# Copia: celular desenhado com anotações em setas (estilo "erro × acerto" de carrossel educativo) + adesivos girados (Pizzino).
perfil = (f'<div style="padding:66px 26px 0">'
          f'<div style="display:flex;align-items:center;gap:22px"><div style="width:120px;height:120px;border-radius:50%;background:{TOMATE};display:grid;place-items:center;'
          f'box-shadow:0 0 0 5px #fff,0 0 0 9px {ACAFRAO}">{icone("pizza", 80, CREME, 6)}</div>'
          + ''.join(f'<div style="text-align:center;flex:1"><div style="font:800 28px Inter;color:{CARVAO}">{a}</div><div style="font:500 17px Inter;color:#555">{b}</div></div>'
                    for a, b in [('214', 'posts'), ('3,1 mil', 'seguidores'), ('180', 'seguindo')]) + '</div>'
          f'<div style="font:800 26px Inter;color:{CARVAO};margin-top:18px">Pizzaria do Bairro</div>'
          f'<div style="font:500 22px/1.4 Inter;color:{CARVAO}">A melhor pizza da região</div>'
          f'<div style="font:600 22px Inter;color:#00376B;margin-top:4px">🔗 linktr.ee/pizzariadobairro</div>'
          f'<div style="display:flex;gap:10px;margin-top:18px"><div style="flex:1;background:#EFEFEF;border-radius:12px;padding:14px;text-align:center;font:700 20px Inter">Seguir</div>'
          f'<div style="flex:1;background:#EFEFEF;border-radius:12px;padding:14px;text-align:center;font:700 20px Inter">Mensagem</div></div>'
          f'<div style="margin-top:26px;background:#F4F2EE;border-radius:20px;padding:20px 20px 10px">{MONO("ao tocar no link:", 14, "#777")}'
          + ''.join(f'<div style="margin-top:12px;background:#fff;border:3px solid #DDD;border-radius:16px;padding:18px;text-align:center;font:700 22px Inter;color:#999">{t}</div>'
                    for t in ['Promoções', 'Siga a gente', 'Nossa história']) + '</div>'
          f'<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:4px;margin-top:22px">'
          + ''.join(f'<div style="height:150px;background:{c}"></div>' for c in ['#d8cfc2', '#c9bba7', '#e0d6c8'] * 2) + '</div></div>')
def erro(n, t, sub, rot):
    return (f'<div style="width:330px;background:{CREME};border:6px solid {CARVAO};box-shadow:12px 12px 0 {CARVAO};transform:rotate({rot}deg);padding:18px 20px 20px;position:relative">'
            f'<div style="position:absolute;right:-34px;top:-40px">{xis(100, TOMATE, 0)}</div>'
            f'{MONO("Erro nº" + n, 15, TOMATE)}{BAGEL(t, 50, TOMATE, .95, "margin-top:6px;white-space:normal")}{TXT(sub, 20, CARVAO, "margin-top:8px;line-height:1.3")}</div>')
seta = lambda d: f'<svg width="100" height="60" viewBox="0 0 100 60" style="display:block;overflow:visible"><path d="{d}" fill="none" stroke="{ACAFRAO}" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/></svg>'
post('d06-19h-3-erros-no-link-da-bio',
     BOX(0, 0, 1080, 1350, VERDE) + pad(CREME, .1) +
     A(36, 30, BAGEL('3 erros', 190, ACAFRAO, .88, SH(CARVAO, 10))) +
     A(44, 212, ANTON('no link da bio.', 110, CREME, .9, SH(CARVAO, 6))) +
     A(330, 360, celular(perfil, 420, 860, '#fff', 0)) +
     A(20, 400, erro('1', 'Sem cardápio', 'O cliente quer ver sabor e preço. Não acha.', -4)) +
     A(20, 720, erro('2', 'Sem zap', 'Sem botão do WhatsApp, ele volta pro app.', 3)) +
     A(730, 520, erro('3', 'Sem horário', 'Abre hoje? Até que horas? Ele não sabe.', 4)) +
     A(285, 618, seta('M0 20 C 30 20 50 30 80 40 M60 22 L82 40 L58 52')) +
     A(345, 900, seta('M0 30 C 30 30 50 22 80 14 M58 4 L82 14 L64 34')) +
     A(705, 745, seta('M90 10 C 60 14 40 24 10 36 M24 16 L8 38 L34 46')) +
     A(760, 820, GIRA(-8, f'<div style="background:{ACAFRAO};border:5px solid {CARVAO};box-shadow:10px 12px 0 {CARVAO};padding:20px 22px;width:280px">'
                      + MONO('O certo', 15, TOMATE) + ANTON('Cardápio, zap e horário no 1º toque.', 40, CARVAO, 1, 'white-space:normal') + '</div>')) +
     A(46, 1060, MONO('Perfil fictício · exemplo ilustrativo', 15, CREME, f'background:{CARVAO};padding:8px 12px')) +
     rodape_zap(1240, CARVAO, CREME, 'Arruma a sua bio ↗', ACAFRAO))

# ================================================================ d08 08h · BOM DIA, MASSA. (story, açafrão + bola de massa gigante)
# Copia: palavra dentro do produto ("PIZZA gigante atrás", biblioteca) + produto em close de cor chapada (Drip Riot) feito em forma.
massa = (f'<div style="position:relative;width:980px;height:820px">'
         f'<div style="position:absolute;inset:0;border-radius:50% 50% 46% 46%/56% 56% 44% 44%;background:radial-gradient(circle at 34% 28%,#FFFDF7 0,{CREME} 30%,#E3D3B6 78%,#CDB894 100%);'
         f'box-shadow:0 0 0 8px {CARVAO},24px 30px 0 8px rgba(20,19,17,.3)"></div>'
         + ''.join(f'<div style="position:absolute;left:{x}px;top:{y}px;width:{r}px;height:{r}px;border-radius:50%;background:#fff;opacity:.85"></div>'
                   for x, y, r in [(180, 140, 14), (240, 190, 9), (690, 160, 12), (760, 230, 8), (420, 110, 10), (300, 640, 10), (640, 660, 13), (140, 480, 8), (840, 470, 9)]) +
         f'<div style="position:absolute;inset:0;display:grid;place-items:center;text-align:center">'
         f'<div>{BAGEL("Massa.", 250, TOMATE, .9, SH(CARVAO, 10))}{MONO("fermentou? então bora.", 26, CARVAO, "margin-top:20px")}</div></div></div>')
story('d08-08h-bom-dia-massa',
      BOX(0, 0, 1080, 1920, ACAFRAO) + pad(TOMATE, .12) +
      BOX(0, 0, 1080, 150, xadrez(TOMATE, ACAFRAO, 38), f'border-bottom:8px solid {CARVAO}') +
      A(40, 196, MONO('Seg · 16/11 · 08h · semana nova', 22, CREME, f'background:{VERDE};padding:10px 14px;box-shadow:6px 6px 0 {CARVAO}')) +
      A(30, 262, BAGEL('Bom dia,', 230, VERDE, .9, SH(CARVAO, 11))) +
      BOX(0, 1150, 1080, 420, xadrez(TOMATE, CREME, 50), f'border-top:8px solid {CARVAO};border-bottom:8px solid {CARVAO}') +
      A(50, 600, massa) +
      A(780, 520, GIRA(14, selo(240, 'MASSA DESCANSADA · FORNO QUENTE · ', TOMATE, CREME, centro=icone('pa', 90, CREME, 7)))) +
      A(30, 1360, GIRA(-8, estrela(240, VERDE, ANTON('Bora!', 70, CREME, .9)))) +
      A(330, 1470, f'<div style="background:{CARVAO};border:6px solid {CREME};box-shadow:12px 12px 0 rgba(20,19,17,.35);padding:22px 28px;transform:rotate(-2deg);width:700px">'
                   + ANTON('Quem abre o forno cedo, vende mais tarde.', 54, CREME, .98, 'white-space:normal') + '</div>') +
      faixa('bom dia, pizzaria', 1690, TOMATE, CREME, 3, 96, 56) +
      tarja_ass(1828, VERDE, CREME, '@oreganoturbo · só pizzarias'))

# ================================================================ d08 19h · RESPOSTA PRONTA: "TÁ CARO" (feed, tomate, chat largo + copia e cola)
# Copia: conversa de WhatsApp sobre fundo chapado (kit v1 aprovado) + aspas e manchete em 2 tamanhos + adesivo de recorte.
chat_caro = (wa_topo('Cliente · Renan', 'digitando…', .9) +
             f'<div style="position:absolute;left:0;right:0;top:132px;bottom:0;background:{WA_FUNDO} {padrao("#8a7f6e", .18, 220)};padding:22px 20px;display:flex;flex-direction:column;gap:14px">'
             + balao('Tá caro, viu', False, '20:12', .95)
             + balao('Entendo! Aqui <b>[a massa descansa 24h e o queijo vai até a borda]</b>. Se quiser, a <b>média</b> no mesmo sabor serve 2 pessoas e fica mais em conta. Anoto pra você?', True, '20:13 ✓✓', .95, 88)
             + balao('Manda a média então', False, '20:13', .95)
             + balao('Anotado! Média saindo do forno.', True, '20:14 ✓✓', .95) + '</div>')
post('d08-19h-resposta-pronta-ta-caro',
     BOX(0, 0, 1080, 1350, TOMATE) + pad(CREME, .1) +
     A(40, 40, MONO('Resposta pronta · nº 2', 19, CARVAO, f'background:{ACAFRAO};padding:10px 14px;box-shadow:6px 6px 0 {CARVAO}')) +
     A(30, 96, BAGEL('“Tá', 230, CREME, .86, SH(CARVAO, 11))) +
     A(30, 300, BAGEL('caro.”', 168, ACAFRAO, .86, SH(CARVAO, 11))) +
     A(40, 520, ANTON('Copie e cole<br>no seu WhatsApp.', 66, CREME, .95)) +
     A(590, 70, celular(chat_caro, 460, 960, WA_FUNDO, 4)) +
     A(30, 730, f'<div style="width:530px;background:{CREME};border:6px solid {CARVAO};box-shadow:12px 12px 0 {CARVAO};padding:24px 26px;transform:rotate(-2deg)">'
                + MONO('Por que funciona', 15, TOMATE)
                + ''.join(f'<div style="display:flex;gap:14px;align-items:center;margin-top:14px">{checkbox(True, 44, ACAFRAO)}{ANTON(t, 36, CARVAO, 1)}</div>'
                          for t in ['Não briga com o cliente', 'Mostra o porquê', 'Dá uma saída']) + '</div>') +
     A(500, 1060, copia_cola(-7, 42)) +
     A(46, 1196, MONO('Troque o que está entre [ ] · exemplo ilustrativo', 14, CREME, 'opacity:.9')) +
     rodape_zap(1240, CARVAO, CREME, 'Chama no zap ↗', ACAFRAO))

# ================================================================ d09 08h · QUANTO VALE UM CLIENTE QUE VOLTA? (story, verde + calculadora)
# Copia: objeto desenhado gigante (calculadora) como "produto na mão" das favoritas + fita de conta (comanda) + estrela de total.
teclas = ['7', '8', '9', '÷', '4', '5', '6', '×', '1', '2', '3', '−', '0', ',', '=', '+']
calc = (f'<div style="width:560px;background:{CARVAO};border-radius:56px;padding:40px 36px 44px;box-shadow:0 0 0 8px {CREME},24px 28px 0 8px rgba(20,19,17,.4);transform:rotate(-5deg)">'
        f'<div style="background:#C9D8B8;border-radius:22px;padding:20px 26px;text-align:right;border:5px solid #0b0a09">'
        f'{MONO("por ano · ilustrativo", 14, VERDE_ESC, "letter-spacing:.08em")}<div style="font:400 120px/1 Anton;color:{VERDE_ESC}">2.400</div></div>'
        f'<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-top:28px">'
        + ''.join(f'<div style="height:96px;border-radius:24px;background:{TOMATE if k in "=" else (ACAFRAO if k in "÷×−+" else "#2C2A27")};display:grid;place-items:center;'
                  f'font:400 50px Anton;color:{CARVAO if k in "÷×−+" else CREME};box-shadow:0 6px 0 #000">{k}</div>' for k in teclas) + '</div></div>')
fita = (f'<div style="width:420px;background:{CREME};padding:26px 28px 34px;border:5px solid {CARVAO};box-shadow:12px 12px 0 {CARVAO};transform:rotate(4deg);'
        f'clip-path:polygon(0 0,100% 0,100% 96%,90% 100%,80% 96%,70% 100%,60% 96%,50% 100%,40% 96%,30% 100%,20% 96%,10% 100%,0 96%)">'
        + MONO('A conta', 16, TOMATE)
        + ''.join(f'<div style="display:flex;justify-content:space-between;align-items:baseline;border-bottom:3px dashed rgba(20,19,17,.25);padding:12px 0">'
                  f'{ANTON(a, 38, CARVAO, 1)}<span style="font:600 26px \'IBM Plex Mono\';color:{VERDE}">{b}</span></div>'
                  for a, b in [('Pedido médio', 'R$ 50'), ('Pedidos/mês', '× 4'), ('Meses', '× 12')])
        + f'<div style="display:flex;justify-content:space-between;align-items:baseline;padding-top:14px">{ANTON("Por ano", 44, TOMATE, 1)}{BAGEL("R$ 2.400", 44, TOMATE, 1)}</div></div>')
story('d09-08h-quanto-vale-um-cliente-que-volta',
      BOX(0, 0, 1080, 1920, VERDE) + pad(CREME, .1) +
      A(40, 120, MONO('Dinheiro do delivery · faz a conta', 22, CARVAO, f'background:{ACAFRAO};padding:10px 14px;box-shadow:6px 6px 0 {CARVAO}')) +
      A(36, 186, ANTON('Quanto vale', 120, CREME, .9)) +
      A(30, 300, BAGEL('um cliente', 160, ACAFRAO, .9, SH(CARVAO, 9))) +
      A(30, 460, BAGEL('que volta?', 160, CREME, .9, SH(TOMATE, 9))) +
      A(-10, 700, calc) +
      A(600, 760, fita) +
      A(650, 1150, GIRA(10, estrela(290, ACAFRAO, MONO('1 cliente', 18, CARVAO) + BAGEL('R$2.400', 56, TOMATE, .95) + MONO('por ano', 16, CARVAO), 0))) +
      A(40, 1490, f'<div style="width:1000px;background:{CREME};border:6px solid {CARVAO};box-shadow:12px 12px 0 {CARVAO};padding:22px 28px;transform:rotate(-1.5deg)">'
                  + ANTON('Ele não vale um pedido. Vale o ano inteiro.', 58, VERDE, .98, 'white-space:normal') + '</div>') +
      A(40, 1720, ILU(CARVAO, ACAFRAO, 15)) +
      tarja_ass(1828, CARVAO, CREME, '@oreganoturbo · chama no zap'))

# ================================================================ d10 19h · LEGENDA PRONTA PRA TERÇA (feed, carvão + comanda gigante)
# Copia: comanda de pedido como cartão de texto (cardápio-cartaz retro-14) + selo girado + adesivo de recorte.
comanda = (f'<div style="width:800px;background:{CREME};border:6px solid {CARVAO};box-shadow:18px 18px 0 {TOMATE};transform:rotate(-2.5deg);position:relative">'
           f'<div style="background:{ACAFRAO};border-bottom:6px solid {CARVAO};padding:16px 28px;display:flex;justify-content:space-between;align-items:center">'
           f'{MONO("Comanda nº 0217 · legenda", 17, CARVAO)}{MONO("ter · 19h", 17, TOMATE)}</div>'
           f'<div style="padding:28px 34px 30px;background:repeating-linear-gradient(180deg,transparent 0 55px,rgba(20,19,17,.10) 55px 57px)">'
           f'<div style="font:400 64px/1.02 Anton;color:{TOMATE};text-transform:uppercase">Terça também é dia de pizza.</div>'
           f'<div style="font:600 32px/1.5 \'IBM Plex Mono\';color:{CARVAO};margin-top:18px;letter-spacing:-.01em">Saiu do forno agora: <b style="background:{ACAFRAO}">[sabor da casa]</b>, '
           f'massa fininha e borda dourada.<br><br>Pede pelo zap que a gente já separa a sua.<br>Link na bio.</div>'
           f'<div style="margin-top:22px;display:flex;gap:10px;flex-wrap:wrap">'
           + ''.join(f'<span style="font:600 20px \'IBM Plex Mono\';color:{VERDE};background:rgba(30,91,59,.1);padding:6px 10px;border-radius:8px">{h}</span>'
                     for h in ['#pizzaria', '#pizzasaoluis', '#tercadepizza']) + '</div></div></div>')
post('d10-19h-legenda-pronta-pra-terca',
     BOX(0, 0, 1080, 1350, CARVAO) + pad(CREME, .07) +
     BOX(0, 0, 70, 1350, xadrez(TOMATE, CREME, 35)) + BOX(1010, 0, 70, 1350, xadrez(TOMATE, CREME, 35)) +
     A(100, 30, BAGEL('Legenda', 170, ACAFRAO, .88, SH(TOMATE, 9))) +
     A(106, 210, ANTON('pronta pra terça.', 100, CREME, .9)) +
     A(820, 290, GIRA(12, selo(190, 'COPIE · COLE · POSTE · ', TOMATE, CREME, centro=icone('celular', 70, CREME, 7)))) +
     A(130, 360, comanda) +
     A(560, 1090, copia_cola(-6, 42, TOMATE, CREME)) +
     A(120, 1150, MONO('Troque o que está entre [ ]', 17, CREME, f'background:{VERDE};padding:9px 12px;transform:rotate(-2deg)')) +
     rodape_zap(1240, TOMATE, CREME, 'Quer mais? Zap ↗', ACAFRAO))

# ================================================================ d11 08h · SEU IFOOD TEM FOTO? (story, tomate + tela de cardápio vazia + enquete)
# Copia: tela de app com buracos onde deveria ter foto (interface desenhada, biblioteca "delivery ON") + figurinha de enquete.
itens_app = ''.join(f'<div style="display:flex;gap:16px;align-items:center;padding:16px 0;border-bottom:2px solid #eee">'
                    f'<div style="flex:1"><div style="font:700 24px Inter;color:{CARVAO}">{n}</div><div style="font:500 17px/1.3 Inter;color:#777;margin-top:4px">Molho, mussarela e…</div>'
                    f'<div style="font:700 20px Inter;color:{CARVAO};margin-top:6px">R$ ••,••</div></div>'
                    f'<div style="width:120px;height:110px;border-radius:16px;background:repeating-linear-gradient(45deg,#E9E6E1 0 12px,#F4F2EE 12px 24px);'
                    f'border:3px dashed #BDB7AE;display:grid;place-items:center;font:800 46px Inter;color:#B5AFA6">?</div></div>'
                    for n in ['Calabresa', 'Frango c/ catupiry', 'Portuguesa', 'Marguerita'])
tela_app = (f'<div style="padding:80px 24px 0"><div style="font:800 30px \'Inter Tight\';color:{CARVAO}">Pizzaria do Bairro</div>'
            f'<div style="font:500 17px Inter;color:#777;margin:4px 0 14px">Pizzas · 40-50 min</div>{itens_app}</div>')
story('d11-08h-seu-ifood-tem-foto',
      BOX(0, 0, 1080, 1920, TOMATE) + pad(CREME, .1) +
      A(40, 120, MONO('Enquete · donos de pizzaria', 22, CARVAO, f'background:{ACAFRAO};padding:10px 14px;box-shadow:6px 6px 0 {CARVAO}')) +
      A(30, 184, BAGEL('Seu iFood', 186, CREME, .9, SH(CARVAO, 10))) +
      A(30, 370, BAGEL('tem foto?', 186, ACAFRAO, .9, SH(CARVAO, 10))) +
      A(560, 590, celular(tela_app, 480, 900, '#fff', 6)) +
      A(40, 640, GIRA(-8, f'<div style="background:{CREME};border:6px solid {CARVAO};box-shadow:12px 12px 0 {CARVAO};padding:22px 24px;width:470px">'
                       + MONO('Sem foto, o cliente', 16, TOMATE) + ANTON('rola a tela e passa reto.', 56, CARVAO, .95, 'white-space:normal;margin-top:10px') + '</div>')) +
      A(70, 960, GIRA(-6, selo(230, 'FOTO VENDE ANTES DA PIZZA · ', VERDE, CREME, centro=icone('camera', 90, CREME, 7)))) +
      A(90, 1260, enquete('Seu cardápio no app tem foto?', ['Sim, em tudo', 'Não', 'Mais ou menos'], 900, CARVAO)) +
      A(46, 1770, MONO('Tela fictícia · exemplo ilustrativo', 14, CREME, 'opacity:.85')) +
      tarja_ass(1828, CARVAO, CREME, '@oreganoturbo · só pizzarias'))

# ================================================================ d12 08h · RAIO-X NA SEXTA. (story, creme cartaz + estrela de preço)
# Copia: cartaz "Retro PIZZA National Day" (retro-13: título gordo, explosão de preço) + moldura xadrez (Jonny's retro-14) + botão de zap.
chk_rx = ''.join(f'<div style="display:flex;gap:16px;align-items:center;margin-top:14px">{checkbox(True, 52, VERDE, CREME)}{ANTON(t, 46, CARVAO, 1)}</div>'
                 for t in ['Instagram e Google', 'iFood e cardápio', 'WhatsApp', 'Concorrentes'])
story('d12-08h-raio-x-na-sexta',
      BOX(0, 0, 1080, 1920, xadrez(TOMATE, CREME, 36)) +
      BOX(40, 40, 1000, 1840, CREME, f'border:7px solid {CARVAO};box-shadow:16px 16px 0 {CARVAO}') + BOX(47, 47, 986, 1826, padrao(TOMATE, .13, 260)) +
      A(40, 150, MONO('Orégano Turbo apresenta · sexta · 20/11', 20, CARVAO), 'width:1000px;display:flex;justify-content:center') +
      A(40, 196, BAGEL('Raio-X', 280, TOMATE, .9, SH(CARVAO, 11)), 'width:1000px;display:flex;justify-content:center') +
      A(40, 460, ANTON('na sexta.', 150, VERDE, .9), 'width:1000px;display:flex;justify-content:center') +
      A(610, 650, estrela(390, ACAFRAO, '<div>' + MONO('só', 26, CARVAO, 'letter-spacing:.2em') + BAGEL('R$297', 84, TOMATE, .9, SH(CARVAO, 4)) + '</div>', 10)) +
      A(90, 680, f'<div style="width:470px">{MONO("O que a gente olha", 18, TOMATE)}{chk_rx}</div>') +
      A(90, 1110, GIRA(-3, f'<div style="background:{VERDE};border:6px solid {CARVAO};box-shadow:12px 12px 0 {CARVAO};padding:22px 28px;width:900px">'
                        + ANTON('Abatido no 1º mês<br>se fechar em 7 dias.', 64, CREME, .98) + '</div>')) +
      A(110, 1320, adesivo('5 vagas de fundadora', TOMATE, CREME, 4, 46, '20px 34px')) +
      A(140, 1480, f'<div style="width:800px;background:#25D366;border-radius:999px;padding:30px 36px;display:flex;align-items:center;justify-content:center;gap:20px;'
                   f'box-shadow:0 0 0 8px {CARVAO},14px 16px 0 8px rgba(20,19,17,.35)">{icone("zap", 74, CARVAO, 8)}{BAGEL("Fala com a gente", 58, CARVAO, 1)}</div>') +
      A(140, 1640, MONO('toca no link da bio · @oreganoturbo', 20, CARVAO), 'width:800px;display:flex;justify-content:center') +
      A(110, 1730, logo(44, VERDE, VERDE, CREME)) +
      A(800, 1650, GIRA(-10, selo(190, 'SÓ PIZZARIAS · SÃO LUÍS - MA · ', TOMATE, CREME))))

# ================================================================ d12 19h · CHECKLIST DO CARDÁPIO DIGITAL (feed, verde escuro + ícones em traço)
# Copia: lista de cardápio com ícones em traço (menu busca-34 + padrão de ícones da marca) + selo e manchete em 2 tamanhos.
itens6 = [('camera', 'Foto em cada sabor'), ('preco', 'Preço que dá pra ver'), ('regua', 'Tamanhos claros: P, M, G'),
          ('mais', 'Bordas e adicionais'), ('zap', 'Botão do zap'), ('relogio', 'Horário e taxa de entrega')]
cores6 = [TOMATE, ACAFRAO, CREME, TOMATE, ACAFRAO, CREME]
lista6 = ''.join(f'<div style="display:flex;align-items:center;gap:22px;background:{CREME};border:5px solid {CARVAO};box-shadow:9px 9px 0 {CARVAO};padding:14px 22px 14px 14px;'
                 f'transform:rotate({[-1.2, .9, -.6, 1.1, -.9, .7][i]}deg)">'
                 f'<div style="width:92px;height:92px;flex:none;border-radius:20px;background:{VERDE};display:grid;place-items:center;border:4px solid {CARVAO}">{icone(ic, 62, cores6[i] if cores6[i] != CREME else CREME, 7)}</div>'
                 f'<span style="font:600 22px \'IBM Plex Mono\';color:{TOMATE}">0{i + 1}</span>{ANTON(t, 44, CARVAO, 1)}<span style="flex:1"></span>{checkbox(True, 54, ACAFRAO)}</div>'
                 for i, (ic, t) in enumerate(itens6))
post('d12-19h-checklist-do-cardapio-digital',
     BOX(0, 0, 1080, 1350, VERDE_ESC) + pad(ACAFRAO, .1) +
     A(36, 26, BAGEL('Checklist', 176, ACAFRAO, .88, SH(CARVAO, 9))) +
     A(42, 190, ANTON('do cardápio digital', 92, CREME, .9)) +
     A(800, 300, GIRA(12, selo(220, '6 ITENS · PEDE MAIS RÁPIDO · ', TOMATE, CREME, centro=icone('celular', 80, CREME, 7)))) +
     A(46, 310, MONO('6 itens que fazem o cliente pedir mais rápido', 18, CARVAO, f'background:{CREME};padding:9px 12px;transform:rotate(-2deg)')) +
     A(46, 390, f'<div style="width:760px;display:flex;flex-direction:column;gap:16px">{lista6}</div>') +
     A(800, 880, GIRA(-8, f'<div style="background:{TOMATE};border:5px solid {CARVAO};box-shadow:10px 12px 0 {CARVAO};padding:20px 22px;width:240px">'
                      + BAGEL('Salva', 54, CREME, .9) + TXT('e confere o seu hoje.', 21, CREME, 'margin-top:6px') + '</div>')) +
     rodape_zap(1240, ACAFRAO, CARVAO, 'Revisa o meu ↗', VERDE))

# ================================================================ d13 19h · 5 VAGAS. NÃO VAI TER 6. (feed, tomate, cartaz retrô + 5 ingressos)
# Copia: cartaz retrô com selo (retro-13 / Don Diovanni retro-20) + "número gigante" (p08) virado em 5 ingressos + carimbo de X no 6.
def ingresso(n, bg, fg, rot):
    return (f'<div style="width:178px;height:280px;background:{bg};border:5px solid {CARVAO};box-shadow:9px 10px 0 {CARVAO};transform:rotate({rot}deg);'
            f'display:flex;flex-direction:column;align-items:center;justify-content:space-between;padding:16px 8px;'
            f'-webkit-mask:radial-gradient(circle at 0 50%,transparent 16px,#000 17px) left/51% 100% no-repeat,radial-gradient(circle at 100% 50%,transparent 16px,#000 17px) right/51% 100% no-repeat">'
            f'{MONO("Vaga", 14, fg)}{BAGEL(n, 120, fg, .9)}{MONO("fundadora", 12, fg, "letter-spacing:.06em")}</div>')
tick = ''.join(A(60 + i * 196, 600 + (i % 2) * 24, ingresso(str(i + 1), bg, fg, r))
               for i, (bg, fg, r) in enumerate([(ACAFRAO, CARVAO, -5), (VERDE, CREME, 3), (CREME, TOMATE, -2), (ACAFRAO, CARVAO, 4), (VERDE, CREME, -3)]))
post('d13-19h-5-vagas-nao-vai-ter-6',
     BOX(0, 0, 1080, 1350, TOMATE) + pad(CREME, .1) +
     BOX(30, 30, 1020, 1180, 'transparent', f'border:6px solid {CREME};outline:6px solid {CARVAO};outline-offset:6px') +
     A(30, 60, MONO('Condição de fundadora · 2026', 19, CREME), 'width:1020px;display:flex;justify-content:center') +
     A(30, 100, BAGEL('5 vagas.', 210, CREME, .9, SH(CARVAO, 11)), 'width:1020px;display:flex;justify-content:center') +
     A(30, 330, f'<div style="display:flex;align-items:center;gap:22px;justify-content:center">{ANTON("Não vai ter", 130, ACAFRAO, .9, SH(CARVAO, 6))}'
                f'<div style="position:relative">{BAGEL("6", 180, CREME, .85, SH(CARVAO, 8))}<div style="position:absolute;left:-26px;top:70px;width:170px;height:26px;background:{CARVAO};border:5px solid {CREME};transform:rotate(-28deg)"></div></div></div>',
       'width:1020px') +
     tick +
     A(760, 860, GIRA(12, selo(240, 'SÓ 5 PIZZARIAS · SÃO LUÍS - MA · ', CARVAO, CREME))) +
     A(60, 960, adesivo('Preço do anual<br>no contrato de 6 meses', ACAFRAO, CARVAO, -4, 40, '20px 32px', extra='border-radius:30px;line-height:1.05;text-align:center')) +
     A(60, 1130, MONO('Raio-X R$ 297 · abatido no 1º mês se fechar em 7 dias', 17, CREME)) +
     rodape_zap(1240, CARVAO, CREME, 'Garante a sua ↗', ACAFRAO))

# ================================================================ d14 08h · RESUMO DA SEMANA. (story, verde escuro + 3 comandas empilhadas)
# Copia: pilha de cartões numerados girados (Pizzino, adesivos) + número de fundo gigante + selo "salva".
def ficha(n, t, sub, bg, fg, rot):
    return (f'<div style="width:900px;background:{bg};border:6px solid {CARVAO};box-shadow:14px 16px 0 {CARVAO};transform:rotate({rot}deg);padding:26px 30px;'
            f'display:flex;gap:28px;align-items:center;position:relative;overflow:hidden">'
            f'<div style="flex:none">{BAGEL(n, 190, fg, .85)}</div>'
            f'<div>{MONO(sub, 16, fg)}{ANTON(t, 64, fg, .95, "white-space:normal;margin-top:8px")}</div></div>')
story('d14-08h-resumo-da-semana',
      BOX(0, 0, 1080, 1920, VERDE_ESC) + pad(CREME, .08) +
      BOX(0, 0, 1080, 150, xadrez(VERDE, CREME, 38), f'border-bottom:8px solid {CARVAO}') +
      A(40, 196, MONO('Dom · 22/11 · o que rolou aqui', 22, CARVAO, f'background:{ACAFRAO};padding:10px 14px')) +
      A(30, 262, BAGEL('Resumo', 236, CREME, .9, SH(TOMATE, 11))) +
      A(36, 480, ANTON('da semana.', 140, ACAFRAO, .9)) +
      A(90, 700, ficha('1', 'Resposta pronta pro “tá caro”', 'seg · copia e cola', TOMATE, CREME, -3)) +
      A(90, 1000, ficha('2', 'Legenda pronta pra terça', 'qua · copia e cola', ACAFRAO, CARVAO, 2)) +
      A(90, 1300, ficha('3', 'Checklist do cardápio digital', 'sex · 6 itens', CREME, VERDE, -2)) +
      A(800, 430, GIRA(12, estrela(220, TOMATE, ANTON('Salva<br>tudo', 54, CREME, .9)))) +
      A(60, 1580, adesivo('Manda pro seu sócio ↗', CREME, VERDE, -4, 44, borda=CARVAO)) +
      faixa('salva · manda · usa', 1700, ACAFRAO, CARVAO, 2, 90, 52) +
      tarja_ass(1828, CARVAO, CREME, '@oreganoturbo · só pizzarias'))

# ================================================================ d14 19h · 3 COMBOS QUE VENDEM NO FRIO (feed, carvão chuvoso + cartas em leque)
# Copia: cartas em leque (menu de cartões) sobre fundo noturno com chuva em traço + vapor; difere da grade reta do d04.
chuva = ("url('data:image/svg+xml;utf8," + (f'<svg xmlns="http://www.w3.org/2000/svg" width="120" height="120"><g stroke="{CREME}" stroke-opacity=".16" stroke-width="4" stroke-linecap="round">'
         '<path d="M20 10 L8 40"/><path d="M80 30 L68 60"/><path d="M50 70 L38 100"/><path d="M110 80 L98 110"/></g></svg>').replace('#', '%23').replace('"', '%22').replace('<', '%3C').replace('>', '%3E') + "')")
def carta(n, nome, t, sub, bg, fg, ic, rot, ox):
    return (f'<div class="a" style="left:{ox}px;top:560px;width:340px;height:500px;background:{bg};border:6px solid {CARVAO};box-shadow:14px 16px 0 rgba(0,0,0,.45);'
            f'transform:rotate({rot}deg);transform-origin:50% 120%;padding:24px 24px;overflow:hidden">'
            f'<div style="display:flex;justify-content:space-between;align-items:center">{MONO("nº" + n, 18, fg)}{icone(ic, 70, fg, 7)}</div>'
            f'{BAGEL(nome, 62, fg, .95, "margin-top:20px;white-space:normal")}'
            f'<div style="margin-top:14px">{ANTON(t, 40, fg, 1, "white-space:normal")}</div>'
            f'<div style="margin-top:12px">{TXT(sub, 20, fg, "line-height:1.3")}</div>'
            f'<div style="position:absolute;right:-10px;bottom:-60px">{BAGEL(n, 260, fg, 1, "opacity:.22")}</div></div>')
vapor = f'<svg width="300" height="200" viewBox="0 0 300 200"><g fill="none" stroke="{CREME}" stroke-width="12" stroke-linecap="round" opacity=".85">' \
        '<path d="M60 190 C 30 150 90 120 60 80 C 40 50 70 30 60 10"/><path d="M150 190 C 120 150 180 120 150 80 C 130 50 160 30 150 10"/><path d="M240 190 C 210 150 270 120 240 80 C 220 50 250 30 240 10"/></g></svg>'
post('d14-19h-3-combos-que-vendem-no-frio',
     BOX(0, 0, 1080, 1350, f'{chuva},{CARVAO}') +
     A(36, 30, BAGEL('3 combos', 168, CREME, .88, SH(TOMATE, 10))) +
     A(42, 222, ANTON('que vendem', 100, ACAFRAO, .9)) +
     A(42, 316, BAGEL('no frio.', 150, ACAFRAO, .9, SH(TOMATE, 8))) +
     A(680, 300, vapor) +
     A(850, 250, GIRA(12, selo(190, 'NOITE DE CHUVA · NOITE DE PIZZA · ', TOMATE, CREME, centro=icone('gota', 80, CREME, 7)))) +
     carta('1', 'Chuva', 'Grande + refri 2L', 'Pra ver filme em casa.', TOMATE, CREME, 'pizza', -8, 80) +
     carta('2', 'Sofá', 'Média + pizza doce broto', 'Salgada e doce, um pedido só.', ACAFRAO, CARVAO, 'coracao', 0, 370) +
     carta('3', 'Família', '2 grandes + borda recheada', 'A mesa toda servida.', VERDE, CREME, 'caixa', 8, 660) +
     A(46, 1150, MONO('Ideias sem preço: o valor é o da sua casa', 16, CREME, f'background:{VERDE};padding:9px 12px')) +
     rodape_zap(1240, ACAFRAO, CARVAO, 'Monta comigo ↗', TOMATE))

FONTS = ('<link href="https://fonts.googleapis.com/css2?family=Anton&family=Bagel+Fat+One&family=Inter+Tight:wght@700;800'
         '&family=Inter:wght@500;600;700;800&family=IBM+Plex+Mono:wght@500;600&display=swap" rel="stylesheet">')
open(os.path.join(D, 'pecas.html'), 'w').write(
    f'<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>' +
    ''.join(f'<section class="f" id="{i}" style="width:{w}px;height:{h}px">{c}</section>' for i, w, h, c in P) + '</body></html>')
print(len(P), 'peças')
