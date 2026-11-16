# Barzakh · feed do Instagram "A Travessia" (conta Leandro, 16/11/2026)
# Padrão APROVADO: marca/aprovado/placa-arco-monolito-ouro.png + book/manual v2 (monolito em ouro escovado,
# concreto, arcos, brilho Lápis, Fraunces + Inter Tight + JetBrains Mono). Helpers: ../../gerador/escuro.py.
# Referências (estudo, nunca cópia) em ../TEMPLATE.md:
#   R1 SOMA (Dubai, Behance) .......... luz rasante em parede, silêncio, texto mínimo -> fundos de concreto e placa
#   R2 The Brand Identity (UK, IG) .... grade de case em mockup + frase, assinatura fixa no rodapé -> moldura Nº/@
#   R3 Furniture studio (Baku, Behance) feed como mosaico contínuo em tons -> mosaicos 01-03 e 10-12
# Uso: PYTHONPATH=<scratchpad>/py python3 feed.py
import os, sys, glob
from PIL import Image
from playwright.sync_api import sync_playwright
V3 = '/home/user/lindson/agencia/marca-lindson/projeto-designer/v3'
sys.path.insert(0, V3 + '/gerador')
import escuro as E
from escuro import OB, MA, BR, LA, GRAF, OURO, mask, mono, mono_inline, ENDOSSO

F = V3 + '/feed'; IMG = F + '/gerador/img'; T = V3 + '/marca/gerador/trat'
PNG = V3 + '/marca/logos/png/ouro'; BB = V3 + '/marca/entregas/paginas-v2/barzakh-branding-book-v2'
RT = V3 + '/behance/real-time'; REF = V3 + '/marca/referencias'
FONT = '/home/user/lindson/agencia/marca-holding/v2/fontes'
u = lambda p: 'file://' + p
CONC, CONCD, SOMBRA, PEDRA = u(T + '/concreto-v2.jpg'), u(T + '/concreto-escuro-v2.jpg'), u(T + '/sombra-noite.jpg'), u(T + '/pedra-v2.jpg')
W, H = 1080, 1350
TINTA = '#2b2112'  # ouro gravado (baixo-relevo)

CSS = E.CSS + f"""
@font-face{{font-family:'Fraunces';src:url('file://{FONT}/Fraunces-Regular.ttf');font-weight:400}}
@font-face{{font-family:'Fraunces';src:url('file://{FONT}/Fraunces-SemiBold.ttf');font-weight:600}}
@font-face{{font-family:'Fraunces';font-style:italic;src:url('file://{FONT}/Fraunces-Italic%5BSOFT,WONK,opsz,wght%5D.ttf')}}
*{{box-sizing:border-box;margin:0;padding:0}} body{{background:#000}}
.pg{{width:{W}px;position:relative;overflow:hidden;font-family:'Inter Tight';color:{MA};margin-bottom:20px}}
.pg:after{{content:'';position:absolute;inset:0;background-image:{E.NOISE};opacity:.10;mix-blend-mode:overlay;pointer-events:none;z-index:9}}
.mn{{font-family:'JetBrains Mono';font-size:17px;letter-spacing:.2em;text-transform:uppercase}}
.fr{{font-family:'Fraunces';font-weight:400;letter-spacing:-.01em}}
.it{{font-style:italic}}
.p{{font-size:27px;line-height:1.5}}
.abs{{position:absolute}}
.arch{{position:absolute;overflow:hidden;box-shadow:inset 0 0 0 2px rgba(201,168,108,.55),0 40px 80px rgba(0,0,0,.55)}}
.grav{{color:{TINTA};text-shadow:0 1px 0 rgba(255,236,190,.55),0 -1px 1px rgba(0,0,0,.35)}}
.brush{{background:{OURO}}}
.brush:before{{content:'';position:absolute;inset:0;background:repeating-linear-gradient(90deg,rgba(255,255,255,.06) 0 1px,transparent 1px 3px,rgba(0,0,0,.05) 3px 4px)}}
"""

# ---------- fundos (os 4 tons do xadrez: D obsidiana · C concreto · O ouro · L Lápis) ----------
def bg(t, h=H, luz=.8):
    if t == 'D':
        return (f'<div class="abs" style="inset:0;background:{OB}"></div><div class="abs" style="inset:0;background:url({SOMBRA}) center/cover;opacity:.28;filter:grayscale(1)"></div>'
                f'<div class="abs" style="inset:0;background:radial-gradient(ellipse at 50% 30%,transparent 20%,rgba(10,12,16,.85))"></div>')
    if t == 'C':
        return (f'<div class="abs" style="inset:0;background:url({CONC}) center/cover;filter:brightness(1.55) contrast(.9) sepia(.12)"></div>'
                f'<div class="win" style="opacity:{luz*.45}"></div><div class="abs" style="inset:0;background:radial-gradient(ellipse at 40% 35%,transparent 35%,rgba(20,20,24,.35))"></div>')
    if t == 'O':
        return (f'<div class="abs brush" style="inset:0"></div><div class="abs" style="inset:0;background:radial-gradient(ellipse at 30% 20%,rgba(255,240,200,.35),transparent 55%),radial-gradient(ellipse at 80% 100%,rgba(60,40,10,.45),transparent 60%)"></div>')
    if t == 'L':
        return (f'<div class="abs" style="inset:0;background:#0b0e1f"></div><div class="abs" style="inset:0;background:url({CONCD}) center/cover;opacity:.55;mix-blend-mode:luminosity"></div>'
                f'<div class="beam" style="left:10%;top:{h*.18}px;width:80%;height:{h*.55}px;opacity:.95"></div>'
                f'<div class="abs" style="inset:0;background:radial-gradient(ellipse at 50% 45%,transparent 30%,rgba(5,6,14,.8))"></div>')

def moldura(n, rotulo, t, total=12):
    """Assinatura fixa (cópia da regra do The Brand Identity: rótulo e rodapé sempre no mesmo lugar). Dentro da área segura 3:4."""
    c = TINTA if t in 'CO' else BR
    c2 = TINTA if t in 'CO' else 'rgba(238,234,226,.7)'
    return (f'<div class="abs mn" style="left:96px;right:96px;top:64px;display:flex;justify-content:space-between;color:{c};z-index:8"><span>{rotulo}</span><span>Nº {n:02d}</span></div>'
            f'<div class="abs mn" style="left:96px;right:96px;bottom:60px;display:flex;justify-content:space-between;align-items:center;color:{c2};font-size:15px;z-index:8"><span>@barzakhstudio</span><span>Barzakh · a passagem da sua marca</span></div>')

def arch(x, y, w, h, img, pos='center', extra=''):
    return f'<div class="arch" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;border-radius:{w/2}px {w/2}px 0 0;background:url({img}) {pos}/cover;{extra}"></div>'

def sec(id_, body, h=H, w=W):
    return f'<section class="pg" id="{id_}" style="height:{h}px;width:{w}px">{body}</section>'

def aneis(cx, cy, rs, cor='rgba(201,168,108,.55)', sw=2):
    """Grafismo: os arcos do monolito, abertos sobre a linha do horizonte."""
    return (f'<svg class="abs" style="left:0;top:0;width:100%;height:100%;z-index:2;pointer-events:none" preserveAspectRatio="none">'
            + ''.join(f'<path d="M{cx-r} {cy} A{r} {r} 0 0 1 {cx+r} {cy}" fill="none" stroke="{cor}" stroke-width="{sw}"/>' for r in rs) + '</svg>')

P = []  # (id, html)

# ================= MOSAICO 1 (posts 01-03: a placa sobre o horizonte) =================
MW = 3 * 1012 + 68; HZ = 1040; CX = MW / 2
def seam(k): return k * 1012 + 34
m1 = (f'<div class="abs" style="left:0;top:0;width:{seam(1)}px;height:{H}px">{bg("O")}</div>'
      f'<div class="abs" style="left:{seam(1)}px;top:0;width:1012px;height:{H}px;overflow:hidden">{bg("C")}</div>'
      f'<div class="abs" style="left:{seam(2)}px;top:0;width:{MW-seam(2)}px;height:{H}px;overflow:hidden">{bg("D")}</div>'
      + aneis(CX, HZ, [600, 760, 940, 1180, 1460], 'rgba(150,115,60,.6)')
      + f'<div class="abs" style="left:0;right:0;top:{HZ}px;height:4px;background:{OURO};z-index:3;box-shadow:0 0 18px rgba(217,189,132,.5)"></div>'
      # esquerda = post 03 (ouro gravado: o nome)
      f'<div class="abs grav" style="left:130px;top:250px;width:820px;z-index:4"><div class="mn" style="color:{TINTA}">bar·zakh · substantivo</div>'
      f'<div class="fr it" style="font-size:190px;line-height:.95;margin-top:30px">Barzakh</div>'
      f'<div class="fr" style="font-size:52px;line-height:1.15;margin-top:36px">o espaço entre dois mundos. O limiar.</div>'
      f'<div class="p" style="margin-top:40px;width:640px;font-weight:500">Onde a marca que o seu negócio tem hoje encontra a marca do tamanho que ele já é.</div></div>'
      f'<div class="abs mn grav" style="left:130px;top:{HZ+60}px;z-index:4">03 · o nome</div>'
      # centro = post 02 (a placa aprovada sobre o concreto)
      f'<div class="abs" style="left:{CX-391}px;top:{HZ-782}px;z-index:4">{E.placa(1.15)}</div>'
      f'<div class="abs mn" style="left:{seam(1)+96}px;top:{HZ+60}px;color:{TINTA};z-index:4">02 · a marca</div>'
      f'<div class="abs fr it" style="left:{seam(1)}px;width:1012px;top:{HZ+120}px;text-align:center;font-size:40px;color:{TINTA};z-index:4">Identidade visual e branding · São Luís</div>'
      # direita = post 01 (obsidiana: a assinatura)
      f'<div class="abs" style="left:{seam(2)+96}px;top:250px;width:800px;z-index:4"><div class="mn" style="color:{BR}">{ENDOSSO(15)}</div>'
      f'<div class="fr" style="font-size:118px;line-height:1.0;margin-top:40px">A passagem<br>da sua <span class="ouro it">marca.</span></div>'
      f'<div class="p" style="margin-top:46px;width:640px;color:rgba(238,234,226,.85)">Logo, cores, letras, voz e a marca aplicada no mundo real. Um estúdio de identidade visual para negócios que já cresceram mais que a própria marca.</div></div>'
      f'<div class="abs mn" style="left:{seam(2)+96}px;top:{HZ+60}px;color:{BR};z-index:4">01 · o começo</div>'
      f'<div class="abs mn" style="left:{seam(2)+96}px;top:{HZ+110}px;color:rgba(238,234,226,.6);z-index:4;font-size:15px">Arraste o perfil: a grade conta a travessia</div>')
P.append(('mosaico1', sec('mosaico1', m1, H, MW)))

# ================= MOSAICO 2 (posts 10-12: o ouro nasce no horizonte) =================
m2 = (f'<div class="abs" style="left:0;top:0;width:{seam(1)}px;height:{H}px;overflow:hidden">{bg("L")}</div>'
      f'<div class="abs" style="left:{seam(1)}px;top:0;width:1012px;height:{H}px;overflow:hidden">{bg("O")}</div>'
      f'<div class="abs" style="left:{seam(2)}px;top:0;width:{MW-seam(2)}px;height:{H}px;overflow:hidden">{bg("C")}</div>'
      + aneis(CX, HZ, [600, 760, 940, 1180, 1460], 'rgba(150,115,60,.6)')
      + f'<div class="abs" style="left:0;right:0;top:{HZ}px;height:4px;background:{OURO};z-index:3;box-shadow:0 0 18px rgba(217,189,132,.5)"></div>'
      # centro = post 11: monolito gigante em baixo-relevo no ouro
      f'<div class="abs" style="left:{CX-420}px;top:{HZ-560}px;width:840px;height:840px;z-index:4;background:linear-gradient(160deg,#5a4520,#2b2112);-webkit-mask:{mask("monolito-mono-branco")} center/contain no-repeat;mask:{mask("monolito-mono-branco")} center/contain no-repeat;filter:drop-shadow(0 2px 0 rgba(255,236,190,.6)) drop-shadow(0 -2px 1px rgba(0,0,0,.4))"></div>'
      f'<div class="abs mn grav" style="left:{seam(1)+96}px;top:200px;z-index:4">11 · do outro lado</div>'
      f'<div class="abs fr grav" style="left:{seam(1)}px;width:1012px;top:300px;text-align:center;font-size:60px;z-index:4">Do improviso <span class="it">à presença.</span></div>'
      # esquerda = post 12 (capa do Reel R2: 6 etapas)
      f'<div class="abs fr ouro" style="left:110px;top:150px;font-size:640px;line-height:1;z-index:4;filter:drop-shadow(0 20px 40px rgba(0,0,0,.6))">6</div>'
      f'<div class="abs" style="left:130px;top:{HZ-300}px;width:760px;z-index:5"><div class="mn" style="color:{BR}">Reel · processo</div>'
      f'<div class="fr" style="font-size:78px;line-height:1.02;margin-top:20px">Como uma marca atravessa em <span class="it ouro">6 etapas.</span></div></div>'
      f'<div class="abs mn" style="left:130px;top:{HZ+60}px;color:rgba(238,234,226,.75);z-index:4;font-size:15px">Briefing · Pesquisa · Conceito · Sistema · Aplicações · Entrega</div>'
      # direita = post 10 (CTA com o case WF em arco)
      + arch(seam(2) + 470, 210, 450, 780, u(IMG + '/wf-cartoes.jpg'), '48% center', 'z-index:4')
      + f'<div class="abs" style="left:{seam(2)+96}px;top:250px;width:380px;z-index:5"><div class="mn" style="color:{TINTA}">10 · o convite</div>'
      f'<div class="fr" style="font-size:76px;line-height:1.02;margin-top:28px;color:{OB}">Sua marca, do outro <span class="it">lado.</span></div>'
      f'<div class="p" style="margin-top:30px;color:{OB};font-size:24px">Conte o seu negócio. A gente mostra o caminho em etapas, com prazo por escrito.</div></div>'
      f'<div class="abs" style="left:{seam(2)+96}px;top:{HZ+70}px;z-index:5;display:flex;align-items:center;gap:18px;background:{OB};color:{MA};padding:20px 30px;font:500 22px Inter Tight">Orçamento no WhatsApp <span style="color:{BR}">↗ link na bio</span></div>')
P.append(('mosaico2', sec('mosaico2', m2, H, MW)))

# ================= POSTS ÚNICOS (04-09) =================
def post04(h=H):  # L · case Real Time (capa do carrossel C1). Cópia: The Brand Identity (mockup grande + manchete curta)
    return (bg('L', h) + arch(150, 190, 780, 760, u(IMG + '/realtime-celular.jpg'), '50% 40%', 'z-index:3')
            + f'<div class="abs" style="left:96px;top:{h-370}px;width:880px;z-index:4"><div class="mn" style="color:#8E9BEA">Case · Real Time · produtora audiovisual</div>'
            f'<div class="fr" style="font-size:64px;line-height:1.05;margin-top:18px">Uma produtora de cinema com uma marca que <span class="it ouro">não mostrava isso.</span></div></div>'
            f'<div class="abs mn" style="right:96px;top:{h-450}px;color:{MA};z-index:4;font-size:15px">arraste →</div>' + moldura(4, 'Travessias', 'L'))

def post05(h=H):  # D · capa do Reel R1. Cópia: SOMA (luz rasante, texto escalado)
    return (bg('D', h) + arch(560, h - 840, 430, 640, u(IMG + '/wf-celular.jpg'), '50% center', 'z-index:3')
            + f'<div class="beam" style="left:420px;top:{h-900}px;width:600px;height:500px;opacity:.6;z-index:2"></div>'
            + f'<div class="abs" style="left:96px;top:190px;width:900px;z-index:4"><div class="mn" style="color:{BR}">Reel · 30 s</div>'
            f'<div class="fr" style="font-size:112px;line-height:.98;margin-top:24px">Sua marca parece <span class="it" style="font-size:54px;color:rgba(238,234,226,.6)">menor</span><br>que o seu <span class="ouro it">negócio?</span></div></div>'
            f'<div class="abs" style="left:96px;top:{h-560}px;width:380px;z-index:4" ><div class="p" style="font-size:25px;color:rgba(238,234,226,.85)">3 sinais de marca improvisada, e o que fazer com cada um.</div></div>' + moldura(5, 'Limiar', 'D'))

ROT = [('Símbolo', 230, 470), ('Logotipo', 840, 480), ('Cores', 170, 760), ('Letras', 870, 790), ('Grafismos', 230, 1010), ('Aplicações', 820, 1040)]
def post06(h=H):  # C · capa do carrossel C2 (anatomia). Cópia: Furniture studio (objeto central + legenda técnica)
    lines = ''.join(f'<line x1="540" y1="700" x2="{x}" y2="{y}" stroke="{TINTA}" stroke-width="1.2" stroke-dasharray="4 6"/>' for _, x, y in ROT)
    labs = ''.join(f'<div class="abs mn" style="left:{x-90}px;top:{y-12}px;width:180px;text-align:center;background:#e2ddd3;color:{OB};padding:10px 0;font-size:15px;z-index:5;box-shadow:0 8px 20px rgba(0,0,0,.18)">{n}</div>' for n, x, y in ROT)
    return (bg('C', h) + f'<svg class="abs" style="inset:0;width:100%;height:100%;z-index:3">{lines}</svg>' + labs
            + f'<div class="abs" style="left:380px;top:540px;width:320px;height:320px;z-index:4;filter:drop-shadow(0 30px 40px rgba(0,0,0,.45))">{mono(320)}</div>'
            + f'<div class="abs" style="left:96px;top:150px;width:900px;z-index:4;color:{OB}"><div class="fr" style="font-size:96px;line-height:1">Anatomia de<br>uma <span class="it">marca.</span></div>'
            f'<div class="p" style="margin-top:20px;font-size:25px;width:900px">Logo sozinho não é identidade. São 6 partes trabalhando juntas.</div></div>' + moldura(6, 'Anatomia da marca', 'C'))

def post07(h=H):  # O · frase gravada no ouro. Cópia: hot stamping do book v2 (Renovo)
    return (bg('O', h) + f'<div class="abs" style="left:-80px;top:120px;width:1240px;height:1240px;opacity:.16;background:{TINTA};-webkit-mask:{mask("simbolo-mono-branco")} center/contain no-repeat;mask:{mask("simbolo-mono-branco")} center/contain no-repeat"></div>'
            + f'<div class="abs grav" style="left:96px;top:250px;width:900px;z-index:4"><div class="fr" style="font-size:118px;line-height:.98">Seu cliente julga a sua marca</div>'
            f'<div class="fr it" style="font-size:118px;line-height:.98;margin-top:10px">antes de ler uma palavra.</div>'
            f'<div style="width:120px;height:3px;background:{TINTA};margin:60px 0 34px"></div><div class="p" style="font-size:27px;width:700px;font-weight:500">A cor, a letra e o cuidado chegam primeiro. O texto chega depois.</div></div>'
            + moldura(7, 'Limiar', 'O'))

def post08(h=H):  # L · case Orégano Turbo em arco alto. Cópia: SOMA (vão alto, luz) + Brand Identity (legenda curta)
    return (bg('L', h) + arch(96, 170, 560, h - 330, u(IMG + '/oregano-embalagem.jpg'), '40% center', 'z-index:3')
            + f'<div class="abs" style="left:700px;top:200px;width:300px;z-index:4"><div class="mn" style="color:#8E9BEA;font-size:15px">Case · Orégano Turbo</div>'
            f'<div class="fr" style="font-size:58px;line-height:1.05;margin-top:24px">A caixa é a mídia mais vista da <span class="it ouro">pizzaria.</span></div>'
            f'<div class="p" style="font-size:22px;margin-top:30px;color:rgba(238,234,226,.8)">Caixa, copo e sacola na mesma marca. Quem recebe o pedido em casa vê a identidade antes de abrir.</div></div>'
            + moldura(8, 'Travessias', 'L'))

def bbpage(i, w, rot, x, y, z):
    return f'<div class="abs" style="left:{x}px;top:{y}px;width:{w}px;height:{w*9/16}px;background:url({u(BB+f"/{i:02d}.jpg")}) center/cover;transform:rotate({rot}deg);box-shadow:0 30px 60px rgba(0,0,0,.7),0 0 0 1px rgba(201,168,108,.3);z-index:{z}"></div>'
def post09(h=H):  # D · bastidor (capa do carrossel C3). Cópia: The Brand Identity (páginas em leque sobre a mesa)
    return (bg('D', h) + f'<div class="win" style="opacity:.5;z-index:2"></div>'
            + bbpage(1, 760, -9, 60, 470, 3) + bbpage(6, 760, 4, 250, 640, 4) + bbpage(9, 700, -2, 180, 860, 5)
            + f'<div class="abs" style="left:96px;top:170px;width:900px;z-index:6"><div class="mn" style="color:{BR}">Bastidor · o brand book da própria Barzakh</div>'
            f'<div class="fr" style="font-size:92px;line-height:1;margin-top:22px">Por dentro de um <span class="it ouro">brand book.</span></div></div>' + moldura(9, 'Bastidores', 'D'))

for n, f in [(4, post04), (5, post05), (6, post06), (7, post07), (8, post08), (9, post09)]:
    P.append((f'p{n:02d}', sec(f'p{n:02d}', f())))

# ================= CARROSSÉIS =================
def tela(k, tot, t):  # contador de carrossel
    c = TINTA if t in 'CO' else BR
    return f'<div class="abs mn" style="right:96px;top:64px;color:{c};z-index:8">{k}/{tot}</div><div class="abs mn" style="left:96px;top:64px;color:{c};z-index:8">Barzakh</div>'
def cta(t, txt='Quer ver como ficaria a sua? Orçamento no WhatsApp, link na bio.'):
    return f'<div class="abs" style="left:96px;right:96px;bottom:70px;z-index:8;display:flex;justify-content:space-between;align-items:center;border-top:1px solid {BR};padding-top:22px"><div class="p" style="font-size:22px;width:640px">{txt}</div>{mono_inline(70)}</div>'

C1 = [  # Real Time (6 telas)
    ('L', post04()),
    ('D', bg('D') + f'<div class="abs" style="inset:0;background:url({u(IMG+"/realtime-fachada.jpg")}) center/cover"></div><div class="abs" style="inset:0;background:linear-gradient(transparent 45%,rgba(10,12,16,.95))"></div>'
          f'<div class="abs" style="left:96px;bottom:150px;width:880px;z-index:4"><div class="mn" style="color:{BR}">01 · o ponto de partida</div><div class="fr" style="font-size:66px;line-height:1.05;margin-top:20px">Equipamento de cinema, presença de amador.</div>'
          f'<div class="p" style="margin-top:20px;font-size:24px;color:rgba(238,234,226,.8)">A marca precisava mostrar o que a produtora já entregava no set.</div></div>' + tela(2, 6, 'D')),
    ('C', bg('C') + f'<div class="abs" style="left:96px;top:170px;width:888px;height:620px;background:url({u(RT+"/02-conceito.jpg")}) center/cover;box-shadow:0 30px 60px rgba(0,0,0,.35);z-index:3"></div>'
          f'<div class="abs fr it" style="left:96px;top:830px;font-size:150px;line-height:1;color:{OB};z-index:4">No ar, agora.</div>'
          f'<div class="abs p" style="left:96px;top:1020px;width:820px;font-size:24px;color:{OB};z-index:4">02 · O conceito: o símbolo vira o visor de uma câmera [rt], com a linguagem do timecode nas aplicações.</div>' + tela(3, 6, 'C')),
    ('L', bg('L') + f'<div class="abs" style="left:96px;top:180px;width:430px;height:900px;background:url({u(RT+"/05-paleta.jpg")}) center/cover;box-shadow:0 30px 60px rgba(0,0,0,.5);z-index:3"></div>'
          f'<div class="abs" style="left:554px;top:180px;width:430px;height:900px;background:url({u(RT+"/06-tipografia.jpg")}) center/cover;box-shadow:0 30px 60px rgba(0,0,0,.5);z-index:3"></div>'
          f'<div class="abs" style="left:96px;top:1110px;z-index:4"><div class="mn" style="color:#8E9BEA">03 · o sistema</div><div class="fr" style="font-size:52px;margin-top:10px">Preto, azul elétrico e <span class="it ouro">uma letra só.</span></div></div>' + tela(4, 6, 'L')),
    ('O', bg('O') + ''.join(f'<div class="abs" style="left:{96+(i%2)*452}px;top:{280+(i//2)*420}px;width:436px;height:400px;background:url({u(IMG+"/"+f)}) center/cover;box-shadow:0 20px 40px rgba(60,40,10,.5);z-index:3"></div>' for i, f in enumerate(['realtime-cartoes.jpg', 'realtime-papelaria.jpg', 'realtime-poster.jpg', 'realtime-embalagem.jpg']))
          + f'<div class="abs grav" style="left:96px;top:150px;z-index:4"><div class="mn" style="color:{TINTA}">04 · aplicações</div><div class="fr" style="font-size:56px;margin-top:10px">A marca no mundo real.</div></div>'
          f'<div class="abs mn grav" style="left:96px;top:1150px;z-index:4;font-size:15px">Cartão · papelaria · pôster · case de equipamento</div>' + tela(5, 6, 'O')),
    ('D', bg('D') + arch(96, 170, 520, 900, u(IMG + '/realtime-cartoes.jpg'), '50% center', 'z-index:3')
          + f'<div class="abs" style="left:660px;top:260px;width:330px;z-index:4"><div class="fr" style="font-size:60px;line-height:1.05">Brand book de <span class="it ouro">17 páginas.</span></div>'
          f'<div class="p" style="font-size:22px;margin-top:24px;color:rgba(238,234,226,.8)">Símbolo, versões, paleta, tipografia, fotografia, tom de voz e aplicações. Case completo no Behance.</div></div>' + cta('D') + tela(6, 6, 'D')),
]
C2 = [  # Anatomia (6 telas)
    ('C', post06()),
    ('D', bg('D') + f'<div class="abs fr" style="left:96px;top:150px;font-size:70px;z-index:4">1 · Símbolo e <span class="it ouro">versões.</span></div>'
          + ''.join(f'<div class="abs" style="left:{96+(i%2)*452}px;top:{300+(i//2)*420}px;width:436px;height:400px;background:#16181d;box-shadow:inset 0 0 0 1px rgba(201,168,108,.3);z-index:3"><div class="abs" style="inset:50px;background:url({u(PNG+"/barzakh-"+k+"-ouro.png")}) center/contain no-repeat"></div><div class="abs mn" style="left:20px;bottom:16px;color:{BR};font-size:13px">{k}</div></div>' for i, k in enumerate(['vertical', 'horizontal', 'simbolo', 'avatar']))
          + f'<div class="abs p" style="left:96px;top:1160px;font-size:22px;color:rgba(238,234,226,.8);z-index:4">Uma marca precisa caber no avatar, na fachada e no carimbo.</div>' + tela(2, 6, 'D')),
    ('O', bg('O') + f'<div class="abs" style="left:96px;right:96px;top:300px;height:760px;display:flex;gap:8px;z-index:3">'
          + ''.join(f'<div style="flex:{fl};position:relative;background:{c};box-shadow:0 20px 40px rgba(60,40,10,.4)"><div class="mn" style="position:absolute;left:14px;bottom:18px;writing-mode:vertical-rl;transform:rotate(180deg);color:{tc};font-size:14px">{n} {fl}%</div></div>' for c, fl, n, tc in [(OB, 60, 'Obsidiana', MA), ('#8A8F98', 20, 'Concreto', OB), (LA, 10, 'Lápis', MA), (OURO, 5, 'Ouro', OB), (MA, 5, 'Marfim', OB)])
          + f'</div><div class="abs grav" style="left:96px;top:150px;z-index:4"><div class="fr" style="font-size:70px">2 · Cores com <span class="it">proporção.</span></div></div>'
          f'<div class="abs p grav" style="left:96px;top:1100px;width:880px;font-size:23px;z-index:4;font-weight:500">Proporção da própria Barzakh. Sem proporção, cada post sai de uma cor.</div>' + tela(3, 6, 'O')),
    ('L', bg('L') + f'<div class="abs fr ouro" style="left:80px;top:150px;font-size:520px;line-height:1;z-index:4">Aa</div>'
          f'<div class="abs" style="left:96px;top:760px;width:880px;z-index:4;border-top:1px solid rgba(238,234,226,.3)">'
          + ''.join(f'<div style="display:flex;justify-content:space-between;align-items:baseline;padding:22px 0;border-bottom:1px solid rgba(238,234,226,.3)"><span style="font:{fs}">{n}</span><span class="mn" style="color:#8E9BEA;font-size:14px">{uso}</span></div>' for n, fs, uso in [('Fraunces', "400 54px Fraunces", 'títulos'), ('Inter Tight', "500 42px Inter Tight", 'texto'), ('JETBRAINS MONO', "400 30px JetBrains Mono", 'rótulos')])
          + f'</div><div class="abs fr" style="left:600px;top:280px;font-size:66px;line-height:1.05;z-index:4;width:380px">3 · <span class="it">Letras.</span></div>' + tela(4, 6, 'L')),
    ('C', bg('C') + aneis(540, 1000, [260, 340, 430, 540, 660], 'rgba(43,33,18,.55)', 2)
          + arch(290, 330, 500, 670, u(IMG + '/leo-papelaria.jpg'), '50% center', 'z-index:3')
          + f'<div class="abs" style="left:0;right:0;top:1000px;height:3px;background:{OURO};z-index:4"></div>'
          f'<div class="abs fr" style="left:96px;top:150px;font-size:70px;color:{OB};z-index:4">4 · <span class="it">Grafismos.</span></div>'
          f'<div class="abs p" style="left:96px;top:1050px;width:880px;font-size:23px;color:{OB};z-index:4">O traço do símbolo vira moldura, padrão e recorte. Melhor que colar o logo em tudo.</div>' + tela(5, 6, 'C')),
    ('D', bg('D') + f'<div class="abs" style="left:96px;top:250px;width:540px;height:760px;background:url({u(IMG+"/duble-outdoor.jpg")}) center/cover;box-shadow:0 30px 60px rgba(0,0,0,.6);z-index:3"></div>'
          f'<div class="abs" style="left:560px;top:420px;width:424px;height:560px;background:url({u(IMG+"/curso-poster.jpg")}) center/cover;box-shadow:0 30px 60px rgba(0,0,0,.7),0 0 0 2px rgba(201,168,108,.5);z-index:4"></div>'
          f'<div class="abs fr" style="left:96px;top:150px;font-size:70px;z-index:4">5 · <span class="it ouro">Aplicações.</span></div>' + cta('D', 'Salve para conferir a sua marca. Quer ajuda com as 6 partes? Orçamento no WhatsApp.') + tela(6, 6, 'D')),
]
REFS = [('01-pentagram-us', 'Pentagram · EUA'), ('02-koto-uk', 'Koto · Reino Unido'), ('03-mucho-es', 'Mucho · Espanha'), ('04-studiodumbar-nl', 'Dumbar · Holanda'), ('06-anagrama-mx', 'Anagrama · México'), ('13-ndc-jp', 'NDC · Japão')]
C3 = [  # Bastidor (5 telas)
    ('D', post09()),
    ('C', bg('C') + f'<div class="abs" style="left:150px;top:260px;width:780px;height:820px;background:#f1ece2;transform:rotate(-2deg);box-shadow:0 30px 60px rgba(0,0,0,.3);padding:70px;z-index:3;color:{OB}">'
          f'<div class="mn" style="font-size:15px;color:#8a6a35">Ficha · persona</div><div class="fr" style="font-size:50px;margin:16px 0 30px">Antes do primeiro traço: <span class="it">para quem?</span></div>'
          + ''.join(f'<div style="font:400 21px/1.45 JetBrains Mono;padding:12px 0;border-bottom:1px dashed #b8ab92">{l}</div>' for l in ['Quem: dona de negócio local, 28 a 50 anos', 'Rotina: atende o dia todo, decide à noite', 'Dor: a marca parece menor que o negócio', 'Valoriza: trabalho real, prazo cumprido', 'Confia: quando vê o case aplicado'])
          + f'</div><div class="abs mn" style="left:96px;top:160px;color:{TINTA};z-index:4">01 · persona</div>' + tela(2, 5, 'C')),
    ('L', bg('L') + ''.join(f'<div class="abs" style="left:{96+(i%3)*300}px;top:{300+(i//3)*400}px;width:284px;height:370px;background:url({u(REF+"/"+f+".jpg")}) top center/cover;box-shadow:0 20px 40px rgba(0,0,0,.6);z-index:3"><div class="abs mn" style="left:0;right:0;bottom:0;background:rgba(10,12,16,.85);color:{MA};font-size:12px;padding:10px 12px;letter-spacing:.12em">{lb}</div></div>' for i, (f, lb) in enumerate(REFS))
          + f'<div class="abs fr" style="left:96px;top:150px;font-size:62px;z-index:4">02 · Pesquisa no <span class="it ouro">mundo inteiro.</span></div>'
          f'<div class="abs p" style="left:96px;top:1120px;width:880px;font-size:22px;color:rgba(238,234,226,.8);z-index:4">Estúdios de 6 países estudados antes deste projeto. Referência é para estudo, nunca para cópia.</div>' + tela(3, 5, 'L')),
    ('O', bg('O') + f'<div class="abs" style="left:96px;top:330px;width:888px;height:500px;background:url({u(BB+"/05.jpg")}) center/cover;box-shadow:0 30px 60px rgba(60,40,10,.6);z-index:3"></div>'
          f'<div class="abs" style="left:96px;top:860px;width:888px;height:250px;background:url({u(BB+"/10.jpg")}) center/cover;box-shadow:0 30px 60px rgba(60,40,10,.6);z-index:3"></div>'
          f'<div class="abs grav" style="left:96px;top:150px;z-index:4"><div class="mn" style="color:{TINTA}">03 · o sistema no papel</div><div class="fr" style="font-size:64px;margin-top:10px">Cada decisão <span class="it">por escrito.</span></div></div>'
          f'<div class="abs p grav" style="left:96px;top:1140px;font-size:22px;z-index:4;font-weight:500">Cores com código, letras, usos proibidos e aplicações.</div>' + tela(4, 5, 'O')),
    ('D', bg('D') + arch(560, 180, 430, 900, u(E.APROVADA), '50% 40%', 'z-index:3')
          + f'<div class="abs" style="left:96px;top:200px;width:430px;z-index:4"><div class="mn" style="color:{BR}">04 · a entrega</div><div class="fr" style="font-size:58px;line-height:1.05;margin-top:20px">O que você <span class="it ouro">recebe.</span></div>'
          + ''.join(f'<div style="display:flex;gap:16px;align-items:center;padding:16px 0;border-bottom:1px solid rgba(180,147,90,.35);font-size:22px"><span class="mn" style="color:{BR};font-size:14px">{i+1:02d}</span>{t}</div>' for i, t in enumerate(['Brand book em PDF', 'Logos em todas as versões', 'Paleta com códigos', 'Letras e grafismos', 'Modelos para Instagram']))
          + '</div>' + cta('D') + tela(5, 5, 'D')),
]
for nome, car in [('c1-realtime', C1), ('c2-anatomia', C2), ('c3-bastidor', C3)]:
    for i, (t, body) in enumerate(car):
        P.append((f'{nome}-{i+1}', sec(f'{nome}-{i+1}', body)))

# ================= CAPAS DOS REELS (9:16, com área 4:5 segura no centro) =================
def reel12(h=1920):
    return (bg('L', h) + aneis(540, 1400, [380, 500, 640, 800], 'rgba(150,115,60,.6)') + f'<div class="abs" style="left:0;right:0;top:1400px;height:4px;background:{OURO};z-index:3"></div>'
            f'<div class="abs fr ouro" style="left:110px;top:330px;font-size:760px;line-height:1;z-index:4">6</div>'
            f'<div class="abs" style="left:96px;top:1080px;width:880px;z-index:5"><div class="mn" style="color:{BR}">Reel · processo</div><div class="fr" style="font-size:88px;line-height:1.02;margin-top:20px">Como uma marca atravessa em <span class="it ouro">6 etapas.</span></div></div>'
            f'<div class="abs mn" style="left:96px;top:1460px;color:rgba(238,234,226,.75);z-index:4;font-size:15px">Briefing · Pesquisa · Conceito · Sistema · Aplicações · Entrega</div>' + moldura(12, 'Bastidores', 'L'))
P.append(('reel-r1', sec('reel-r1', post05(1920), 1920)))
P.append(('reel-r2', sec('reel-r2', reel12(), 1920)))

HTML = f'<html><head><meta charset="utf-8"><link rel="stylesheet" href="{E.FONTS}"><style>{CSS}</style></head><body>' + ''.join(h for _, h in P) + '</body></html>'

def render():
    os.makedirs(F + '/posts', exist_ok=True); os.makedirs(F + '/carrosseis', exist_ok=True); os.makedirs(F + '/reels', exist_ok=True)
    tmp = F + '/gerador/feed.html'; open(tmp, 'w').write(HTML)
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={'width': 3200, 'height': 2000})
        pg.goto('file://' + tmp); pg.wait_for_load_state('networkidle'); pg.wait_for_timeout(1500)
        for id_, _ in P:
            el = pg.query_selector('#' + id_)
            if id_.startswith('mosaico'):
                el.screenshot(path=f'{F}/gerador/{id_}.png')
            elif id_.startswith('p'):
                el.screenshot(path=f'{F}/posts/{id_[1:]}.jpg', type='jpeg', quality=92)
            elif id_.startswith('reel'):
                el.screenshot(path=f'{F}/reels/{id_}-capa-1080x1920.jpg', type='jpeg', quality=92)
            else:
                d = F + '/carrosseis/' + id_.rsplit('-', 1)[0]; os.makedirs(d, exist_ok=True)
                el.screenshot(path=f'{d}/{int(id_.rsplit("-",1)[1]):02d}.jpg', type='jpeg', quality=92)
        b.close()
    # fatiar os mosaicos: cada post mostra 1012 px de miolo na grade 3:4 e tem 34 px de sangria
    for nome, posts in [('mosaico1', [3, 2, 1]), ('mosaico2', [12, 11, 10])]:
        im = Image.open(f'{F}/gerador/{nome}.png').convert('RGB')
        for k, n in enumerate(posts):
            im.crop((k * 1012, 0, k * 1012 + 1080, H)).save(f'{F}/posts/{n:02d}.jpg', quality=92)
        im.resize((im.width // 2, im.height // 2)).save(f'{F}/grade-mosaico-{nome[-1]}.jpg', quality=88)
    # capa do Reel no feed (4:5) = recorte central da 9:16
    for r, n in [('reel-r1', 5), ('reel-r2', None)]:
        pass

if __name__ == '__main__':
    render()

# ================= grade.jpg: simulação do perfil no celular (grade 3:4 de 2025-2026) =================
def grade():
    # cada post 4:5 aparece na grade cortado em 3:4 (miolo de 1012 px): é a área segura usada em todos
    for n in range(1, 13):
        Image.open(f'{F}/posts/{n:02d}.jpg').crop((34, 0, 1046, 1350)).resize((360, 480)).save(f'{F}/gerador/t{n:02d}.jpg', quality=90)
    ordem = list(range(12, 0, -1))  # o mais novo em cima, à esquerda
    tiles = ''.join(f'<img src="file://{F}/gerador/t{n:02d}.jpg" style="width:358px;height:477px;display:block;object-fit:cover">' for n in ordem)
    dest = ''.join(f'<div style="text-align:center;width:150px"><div style="width:118px;height:118px;margin:0 auto;border-radius:50%;padding:4px;box-shadow:0 0 0 2px #3a3d45"><div style="width:100%;height:100%;border-radius:50%;background:{OB};display:flex;align-items:center;justify-content:center">{mono_inline(60)}</div></div><div style="font:500 22px Inter Tight;margin-top:12px">{t}</div></div>' for t in ['Cases', 'Processo', 'Pacotes', 'Bastidor', 'Dúvidas'])
    html = (f'<html><head><meta charset="utf-8"><link rel="stylesheet" href="{E.FONTS}"><style>{CSS}</style></head><body style="background:#0c0d10;margin:0">'
            f'<div id="g" style="width:1180px;padding:50px;background:#0c0d10"><div style="width:1080px;border-radius:70px;background:#000;box-shadow:0 0 0 14px #1d1f24;overflow:hidden;color:#f5f5f5;font-family:Inter Tight">'
            f'<div style="padding:40px 40px 10px;display:flex;justify-content:space-between;font:600 30px Inter Tight"><span>09:41</span><span>barzakhstudio ✓</span><span>☰</span></div>'
            f'<div style="display:flex;align-items:center;gap:50px;padding:30px 40px"><img src="file://{PNG}/barzakh-avatar-ouro.png" style="width:190px;height:190px;border-radius:50%;box-shadow:0 0 0 3px #B4935A">'
            f'<div style="display:flex;gap:60px;font-size:26px;text-align:center"><div><b style="font-size:34px">12</b><br>publicações</div><div style="opacity:.55"><b style="font-size:34px">·</b><br>seguidores</div><div style="opacity:.55"><b style="font-size:34px">·</b><br>seguindo</div></div></div>'
            f'<div style="padding:0 40px;font-size:27px;line-height:1.45"><b>Barzakh | Identidade Visual</b><br>Identidade visual e branding · um estúdio Al Kántara<br>Direção criativa: Lindson Almeida · São Luís, MA<br>↓ Orçamento no WhatsApp<br><span style="color:#9fb3ff">lindsonalmeida.pages.dev/site/identidade</span></div>'
            f'<div style="display:flex;gap:16px;padding:30px 40px"><div style="flex:1;background:#26282e;border-radius:16px;padding:18px;text-align:center;font:600 26px Inter Tight">Seguir</div><div style="flex:1;background:#26282e;border-radius:16px;padding:18px;text-align:center;font:600 26px Inter Tight">Mensagem</div><div style="flex:1;background:#26282e;border-radius:16px;padding:18px;text-align:center;font:600 26px Inter Tight">WhatsApp</div></div>'
            f'<div style="display:flex;justify-content:space-between;padding:10px 40px 30px">{dest}</div>'
            f'<div style="display:grid;grid-template-columns:repeat(3,358px);gap:3px">{tiles}</div></div></div></body></html>')
    open(F + '/gerador/grade.html', 'w').write(html)
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1200, 'height': 3200})
        pg.goto('file://' + F + '/gerador/grade.html'); pg.wait_for_load_state('networkidle'); pg.wait_for_timeout(800)
        pg.query_selector('#g').screenshot(path=F + '/grade.jpg', type='jpeg', quality=90); b.close()
    for n in range(1, 13): os.remove(f'{F}/gerador/t{n:02d}.jpg')

if __name__ == '__main__':
    grade()
