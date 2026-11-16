# Padrão escuro da Barzakh (conta Leandro, 16/11/2026), a partir da peça APROVADA pelo Lindson:
# marca/aprovado/placa-arco-monolito-ouro.png (placa em arco grafite no concreto, monolito em ouro escovado,
# brilho Lápis difuso, BARZAKH em Instrument Serif dourada espaçada, "UM ESTÚDIO AL KÁNTARA" em JetBrains Mono).
# Ouro, concreto, arco, grão e luz de janela copiados de marca/gerador/manual.py (mockup 5.8).
import base64
B = '/home/user/lindson/agencia/marca-lindson/projeto-designer/v3/marca'
S = B + '/logos/svg'
OB, MA, GR, PE, BR, LA = '#0A0C10', '#EEEAE2', '#22262E', '#8A8F98', '#B4935A', '#2B3A8F'
GRAF = '#1b1d22'
CONCRETO = 'file://' + B + '/gerador/trat/ando-pedra.jpg'
APROVADA = B + '/aprovado/placa-arco-monolito-ouro.png'
OURO = 'linear-gradient(115deg,#7a5e2f 0%,#d9bd84 22%,#8c6c38 40%,#e8d3a2 55%,#94733d 72%,#c9a86c 100%)'
FONTS = 'https://fonts.googleapis.com/css2?family=Inter+Tight:wght@300;400;500;600;700;800&family=Instrument+Serif:ital@0;1&family=JetBrains+Mono:wght@400;500&display=swap'

def mask(n):
    return "url('data:image/svg+xml;base64," + base64.b64encode(open(f'{S}/barzakh-{n}.svg').read().encode()).decode() + "')"

NOISE = "url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='220' height='220'%3E%3Cfilter id='n'%3E%3CfeTurbulence baseFrequency='.85' numOctaves='3'/%3E%3C/filter%3E%3Crect width='220' height='220' filter='url(%23n)' opacity='.6'/%3E%3C/svg%3E\")"
PAPER = "url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='300'%3E%3Cfilter id='p'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.55' numOctaves='4'/%3E%3CfeColorMatrix values='0 0 0 0 .5 0 0 0 0 .45 0 0 0 0 .4 0 0 0 .55 0'/%3E%3C/filter%3E%3Crect width='300' height='300' filter='url(%23p)'/%3E%3C/svg%3E\")"
CSS = f"""
.grain{{position:relative}}.grain:after{{content:'';position:absolute;inset:0;background-image:{NOISE};opacity:.09;mix-blend-mode:overlay;pointer-events:none;z-index:6}}
.paper{{background-image:{PAPER}}}
.conc{{background:url({CONCRETO}) center/cover}}
.win{{position:absolute;inset:-20%;background:repeating-linear-gradient(100deg,transparent 0 130px,rgba(0,0,0,.55) 130px 170px,transparent 170px 300px);filter:blur(10px);transform:skewY(-8deg);mix-blend-mode:multiply;pointer-events:none}}
.beam{{position:absolute;background:radial-gradient(ellipse at center,rgba(70,96,230,.55),rgba(43,58,143,.22) 40%,transparent 70%);filter:blur(30px);pointer-events:none}}
.foil{{background:{OURO};-webkit-mask-size:contain;-webkit-mask-repeat:no-repeat;-webkit-mask-position:center;mask-size:contain;mask-repeat:no-repeat;mask-position:center;filter:drop-shadow(0 1px 0 rgba(255,240,200,.35)) drop-shadow(0 -1px 1px rgba(0,0,0,.6))}}
.ouro{{background:{OURO};-webkit-background-clip:text;background-clip:text;color:transparent}}
.dk{{background:{OB};color:{MA}}}
"""

def mono(w, x=0, y=0, extra=''):
    """Símbolo monolito em ouro escovado (máscara)."""
    return f'<div class="foil" style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{w}px;-webkit-mask-image:{mask("monolito-mono-branco")};mask-image:{mask("monolito-mono-branco")};{extra}"></div>'

def mono_inline(w):
    return f'<div class="foil" style="width:{w}px;height:{w}px;flex:none;-webkit-mask-image:{mask("monolito-mono-branco")};mask-image:{mask("monolito-mono-branco")}"></div>'

def placa(s=1.0):
    """A placa aprovada, desenhada em 680x680 e escalada por s. Retorna (html, largura, altura)."""
    W = 680
    inner = (f'<div style="position:absolute;inset:0;border-radius:340px 340px 0 0;background:linear-gradient(160deg,#2a2c31,#141519);box-shadow:inset 0 0 0 1px rgba(255,255,255,.06),0 50px 90px rgba(0,0,0,.7);overflow:hidden">'
             f'<div class="paper" style="position:absolute;inset:0;opacity:.6"></div><div class="beam" style="left:120px;top:250px;width:440px;height:300px;opacity:.75"></div>'
             f'{mono(340, 170, 110)}'
             f'<div class="foil" style="position:absolute;left:150px;top:470px;width:380px;height:80px;-webkit-mask-image:{mask("logotipo-mono-branco")};mask-image:{mask("logotipo-mono-branco")}"></div>'
             f'<div style="position:absolute;left:0;right:0;top:580px;text-align:center;font:400 13px JetBrains Mono;letter-spacing:.2em;color:{BR}">UM ESTÚDIO AL KÁNTARA</div></div>')
    return f'<div style="position:relative;width:{W*s}px;height:{W*s}px"><div style="position:absolute;left:0;top:0;width:{W}px;height:{W}px;transform:scale({s});transform-origin:0 0">{inner}</div></div>'

def parede(w, h, luz=.85):
    """Concreto + sombra de janela, como no manual."""
    return f'<div class="conc" style="position:absolute;inset:0"></div><div class="win" style="opacity:{luz}"></div><div style="position:absolute;inset:0;background:radial-gradient(ellipse at 50% 40%,transparent 30%,rgba(10,12,16,.65))"></div>'

def cartao(w, h, verso=False):
    if not verso:
        return (f'<div class="paper" style="position:relative;width:{w}px;height:{h}px;background-color:#101218;border-radius:4px;overflow:hidden;box-shadow:0 2px 2px rgba(0,0,0,.4),0 26px 40px rgba(0,0,0,.55)">'
                f'<div class="beam" style="left:{w*.2}px;top:{h*.2}px;width:{w*.6}px;height:{h*.6}px;opacity:.5"></div>{mono(h*.6, w/2-h*.3, h*.2)}</div>')
    return (f'<div class="paper" style="position:relative;width:{w}px;height:{h}px;background-color:#16181d;color:{MA};border-radius:4px;overflow:hidden;box-shadow:0 2px 2px rgba(0,0,0,.4),0 26px 40px rgba(0,0,0,.55);padding:{h*.12}px">'
            f'<div style="font:400 {h*.13}px Instrument Serif">Lindson Almeida</div><div style="font:500 {h*.045}px JetBrains Mono;letter-spacing:.16em;margin-top:6px;color:{BR}">DIREÇÃO CRIATIVA</div>'
            f'<div style="position:absolute;left:{h*.12}px;bottom:{h*.12}px;font-size:{h*.058}px;line-height:1.5;opacity:.8">@barzakhstudio<br>São Luís · Maranhão</div>'
            f'<div class="foil" style="position:absolute;right:{h*.12}px;bottom:{h*.12}px;width:{h*.42}px;height:{h*.1}px;-webkit-mask-image:{mask("logotipo-mono-branco")};mask-image:{mask("logotipo-mono-branco")}"></div></div>')

def timbrado(w):
    h = w * 1.414
    return (f'<div class="paper" style="position:relative;width:{w}px;height:{h}px;background-color:#15171c;color:{MA};box-shadow:0 30px 50px rgba(0,0,0,.6);padding:{w*.09}px;overflow:hidden">'
            f'<div style="display:flex;gap:{w*.03}px;align-items:center">{mono_inline(w*.12)}<div class="foil" style="width:{w*.3}px;height:{w*.06}px;-webkit-mask-image:{mask("logotipo-mono-branco")};mask-image:{mask("logotipo-mono-branco")}"></div></div>'
            f'<div style="margin-top:{w*.12}px">' + ''.join(f'<div style="height:3px;background:rgba(238,234,226,.12);margin:{w*.03}px 0;width:{v}%"></div>' for v in [92, 88, 95, 70, 90, 85, 60, 93, 80, 50]) + '</div>'
            f'<div style="position:absolute;left:{w*.09}px;right:{w*.09}px;bottom:{w*.06}px;border-top:1px solid {BR};padding-top:6px;display:flex;justify-content:space-between;font-family:JetBrains Mono;font-size:{w*.022}px;letter-spacing:.1em;color:{BR}"><span>BARZAKH · UM ESTÚDIO AL KÁNTARA</span><span>@BARZAKHSTUDIO</span></div></div>')

def envelope(w):
    h = w * .5
    return (f'<div class="paper" style="position:relative;width:{w}px;height:{h}px;background-color:#1d2340;box-shadow:0 26px 50px rgba(0,0,0,.6);overflow:hidden">'
            f'<div style="position:absolute;inset:0;background:linear-gradient(160deg,transparent 49.5%,rgba(0,0,0,.3) 50%,transparent 51%),linear-gradient(20deg,transparent 49.5%,rgba(0,0,0,.3) 50%,transparent 51%)"></div>'
            f'{mono(h*.34, w*.82-h*.17, h*.56)}</div>')

def rodape_pin(titulo, sub, h=190):
    """Faixa escura de rodapé do pin: Obsidiana/grafite com grão, título serifa marfim, monolito em ouro."""
    return (f'<div class="grain paper" style="position:absolute;left:0;right:0;bottom:0;height:{h}px;background-color:{GRAF};border-top:1px solid rgba(180,147,90,.35);padding:0 56px;display:flex;justify-content:space-between;align-items:center;gap:30px;overflow:hidden">'
            f'<div class="beam" style="right:-60px;top:-40px;width:360px;height:280px;opacity:.55"></div>'
            f'<div style="position:relative;min-width:0"><div style="font:400 50px/1.05 Instrument Serif;color:{MA}">{titulo}</div><div style="margin-top:12px;font:500 14px JetBrains Mono;letter-spacing:.18em;text-transform:uppercase;color:{BR}">{sub}</div></div>'
            f'<div style="position:relative;text-align:center;flex:none">{mono_inline(78)}<div style="margin-top:10px;font:500 12px JetBrains Mono;letter-spacing:.2em;color:{BR}">BARZAKH</div></div></div>')
