# v14.2 · datas comemorativas do Leo Pinto modeladas nas referências do Lindson (Marcelo Tavares, Mara Costa, Givago,
# Pedro Henrique e outros, 02/11/2026) dentro do padrão aprovado (v13 v3): assinatura fixa (@ com avatar no topo + logo
# na placa marinho na base esquerda), fundos alternando amarelo/azul em xadrez, caixas de cor inclinadas, número gigante
# atrás do Leo, palavra repetida em contorno, cartões de interface (lista e enquete), Leo sobreposto ao cartão. Conta Lindson.
import sys, json
from PIL import Image as _I
d = sys.argv[1]; M = json.load(open(f'{d}/mapa-sjb.json'))
MAR, ROY, SOL, LAR = '#05316E', '#2350F5', '#FFC20E', '#FF7A1A'
GRAO = ("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'>"
        "<filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='3' stitchTiles='stitch'/>"
        "<feColorMatrix values='0 0 0 0 .5  0 0 0 0 .5  0 0 0 0 .5  0 0 0 .9 0'/></filter><rect width='100%25' height='100%25' filter='url(%23n)'/></svg>")
AMARELO = f'radial-gradient(1000px 900px at 30% 22%,#FFC84A 0,#FFA526 28%,#FF8A1F 52%,{LAR} 74%,#E8590C 100%)'  # laranja é a cor principal (partido), com brilho amarelo
AZUL = f'radial-gradient(1100px 1000px at 40% 30%,#4A78FF 0,#2E5BFA 26%,{ROY} 46%,#1539BE 72%,#082063 100%)'
def mapa(x, y, w, cor='#BFD8FF', op=.30):
    s = w/1000
    return (f'<svg class="a" style="left:0;top:0" width="1080" height="1350"><g transform="translate({x},{y}) scale({s})">'
            f'<polygon points="{M["pts"]}" fill="{cor}" fill-opacity="{op*.5}" stroke="{cor}" stroke-opacity="{op*1.4}" stroke-width="{2/s}" stroke-linejoin="round"/></g></svg>')
def ASSINA(fundo):
    lg = 'logo-marinho.png' if fundo == AMARELO else 'logo.png'
    return ('<div class="a pill"><img src="assets/avatar.jpg">@_leonardopinto</div>'
            f'<img class="a logo" src="assets/{lg}">')
def foto(arq, cx, olhos_y, olho_rec, cx_rec, esc, extra=''):
    w = _I.open(f'{d}/assets/{arq}').size[0]
    return (f'<img class="a" src="assets/{arq}" style="left:{int(cx - cx_rec*esc)}px;top:{int(olhos_y - olho_rec*esc)}px;width:{int(esc*w)}px;'
            f'filter:drop-shadow(0 30px 46px rgba(2,12,50,.42));{extra}">')
def cx(txt, fundo, cor, fs, extra=''): return f'<div class="box" style="background:{fundo};color:{cor};font-size:{fs}px;{extra}">{txt}</div>'
P = []
# 1 · 15/11 · AMARELO · FOTO · cartão-caderno com lista numerada + Leo sobreposto
P.append(('p1-15-11', AMARELO, f"""
<div class="a tilt" style="left:84px;top:150px">{cx('15 de novembro', MAR, '#fff', 34)}</div>
<div class="a L" style="left:92px;top:222px;font-size:22px;color:{MAR}">Proclamação da República</div>
<div class="a card" style="left:76px;top:290px;width:588px;transform:rotate(-2.5deg)">
 {cx('O que faz', ROY, '#fff', 56)}<br>{cx('um vereador?', SOL, MAR, 56, 'margin-top:8px')}
 <div class="lista">{''.join(f'<div class="li"><b>0{i+1}</b><span>{t}</span></div>' for i, t in enumerate(['Fiscaliza a prefeitura', 'Vota as leis da cidade', 'Leva a sua demanda']))}</div></div>
{foto('leo-27-original.png', 830, 610, 250, 636, .70)}
<div class="a K" style="left:96px;top:1000px;width:560px;font-size:54px;color:{MAR}">na República,<br>a voz é do povo</div>"""))
# 2 · 20/11 · AZUL · SÓ LOGO · palavra repetida em contorno
P.append(('p2-20-11', AZUL, f"""{mapa(520, 700, 700, '#BFD8FF', .18)}
<div class="a" style="left:86px;top:170px">{''.join(f'<div class="rep{" cheia" if i == 2 else ""}">Orgulho</div>' for i in range(4))}</div>
<div class="a tilt" style="left:84px;top:800px">{cx('da nossa gente', '#fff', ROY, 64)}</div>
<div class="a K" style="left:96px;top:920px;font-size:62px;color:{SOL}">respeito, memória e luta</div>
<div class="a M" style="left:98px;top:1030px;font-size:24px;line-height:1.55;color:#fff">20 de novembro · Dia de Zumbi<br>e da Consciência Negra</div>"""))
# 3 · 11/12 · AMARELO · FOTO · número gigante atrás do Leo + texto vertical
P.append(('p3-11-12', AMARELO, f"""
<div class="a num" style="left:250px;top:110px;font-size:960px;background:linear-gradient(180deg,#3D6CFF,{ROY} 55%,#1539BE);-webkit-background-clip:text;background-clip:text;color:transparent">11</div>
<div class="a vert" style="left:96px;top:1100px;font-size:64px;color:{ROY}">Dia do Engenheiro</div>
{foto('leo-02-original.png', 660, 600, 270, 561, .68)}
<div class="a tilt" style="left:560px;top:960px;text-align:right">{cx('11 de dezembro', MAR, '#fff', 40)}<br>{cx('a serviço do povo', '#fff', ROY, 40, 'margin-top:8px')}</div>
<div class="a K" style="left:540px;top:250px;width:400px;text-align:right;font-size:52px;color:#fff;text-shadow:0 4px 16px rgba(2,12,50,.45);transform:rotate(-4deg)">olho de<br>engenheiro</div>"""))
# 4 · 25/12 · AZUL · FOTO DE BANCO (luzes de Natal, Pexels 29754763) com véu azul · texto à esquerda
P.append(('p4-25-12', AZUL, f"""<img class="a" src="assets/banco-natal.jpg" style="inset:0;width:1080px;height:1350px;object-fit:cover;object-position:60% 40%">
<div class="a" style="inset:0;background:linear-gradient(100deg,rgba(8,32,99,.94) 0,rgba(21,57,190,.80) 45%,rgba(35,80,245,.35) 100%)"></div>
<div class="a K" style="left:84px;top:220px;width:760px;font-size:200px;line-height:.92;color:#fff;text-shadow:0 12px 40px rgba(2,12,50,.4)">Feliz<br>Natal</div>
<div class="a tilt" style="left:84px;top:660px">{cx('São João Batista!', LAR, '#fff', 60)}</div>
<div class="a M" style="left:96px;width:640px;top:790px;font-size:30px;line-height:1.5;color:#fff;text-transform:none;font-weight:600;letter-spacing:.01em">Que a fé, a família e o amor encham cada casa da nossa cidade.</div>"""))
# 5 · 31/12 · AMARELO · FOTO · cartão de enquete + bloco azul diagonal atrás do Leo
P.append(('p5-31-12', AMARELO, f"""
<div class="a" style="inset:0;clip-path:polygon(62% 0,100% 0,100% 100%,40% 100%);background:{AZUL}"></div>
{foto('leo-10-original.png', 870, 560, 240, 1000, .70)}
<div class="a card" style="left:76px;top:190px;width:640px;transform:rotate(-2deg)">
 <div class="B" style="font-size:44px;color:{ROY}">O que o seu bairro</div>{cx('precisa em 2027?', SOL, MAR, 44, 'margin-top:8px')}
 <div class="opc">{''.join(f'<div class="op"><b>{l}</b>{t}</div>' for l, t in zip('ABCD', ['Saúde perto de casa', 'Ruas e estradas', 'Educação e juventude', 'Emprego e renda']))}</div>
 <div style="margin-top:22px;display:flex;align-items:center;gap:18px">{cx('Comenta a letra', MAR, '#fff', 34)}<span class="K" style="font-size:34px;max-width:190px;line-height:1.05;color:{ROY}">eu quero ouvir você</span></div></div>
"""))
# 6 · 01/01 · AZUL · SÓ LOGO · caixas inclinadas + número gigante
P.append(('p6-01-01', AZUL, f"""<img class="a" src="assets/banco-fogos.jpg" style="inset:0;width:1080px;height:1350px;object-fit:cover;object-position:50% 20%">
<div class="a" style="inset:0;background:linear-gradient(180deg,rgba(35,80,245,.55) 0,rgba(21,57,190,.78) 45%,rgba(8,32,99,.95) 100%)"></div>
<div class="a tilt" style="left:84px;top:180px">{cx('Feliz', '#fff', ROY, 92)}<br>{cx('ano novo', LAR, '#fff', 92, 'margin-top:10px')}</div>
<div class="a num" style="left:0;width:1080px;text-align:center;top:450px;font-size:350px;letter-spacing:-.05em;background:linear-gradient(180deg,#FFE066,{SOL} 50%,{LAR});-webkit-background-clip:text;background-clip:text;color:transparent;filter:drop-shadow(0 18px 30px rgba(2,12,50,.4))">2027</div>
<div class="a K" style="left:0;width:1080px;top:800px;text-align:center;font-size:76px;color:#fff">São João Batista!</div>
<div class="a M" style="left:160px;width:760px;top:920px;text-align:center;font-size:28px;line-height:1.5;color:rgba(255,255,255,.92);text-transform:none;font-weight:600;letter-spacing:.01em">Que seja um ano de saúde, trabalho<br>e união pra nossa cidade.</div>"""))
secs = ''.join(f'<section class="f" id="{i}" style="background:{bg}">{c}{ASSINA(bg)}<div class="a" style="inset:0;background-image:url(&quot;{GRAO}&quot;);opacity:.10;mix-blend-mode:overlay;pointer-events:none"></div></section>' for i, bg, c in P)
html = f"""<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Kaushan+Script&family=Montserrat:wght@600;700;800;900&display=swap" rel="stylesheet">
<style>*{{margin:0;padding:0;box-sizing:border-box}} body{{background:#222}}
.f{{position:relative;width:1080px;height:1350px;overflow:hidden;margin-bottom:20px}} .a{{position:absolute}}
.K{{font-family:'Kaushan Script';line-height:1.08}} .B,.box,.num,.rep,.vert{{font-family:Montserrat;font-weight:900;text-transform:uppercase;letter-spacing:-.02em}}
.L,.M{{font-family:Montserrat;font-weight:700;text-transform:uppercase;letter-spacing:.3em}} .M{{letter-spacing:.08em}}
.box{{display:inline-block;white-space:nowrap;padding:10px 22px 4px;line-height:1;box-shadow:0 20px 34px -20px rgba(2,12,50,.7)}} .tilt{{transform:rotate(-3deg);transform-origin:left center}}
.num{{line-height:.8}} .rep{{font-size:148px;line-height:.96;color:rgba(255,255,255,.16)}}
.rep.cheia{{background:linear-gradient(180deg,#FFE066,{SOL} 55%,{LAR});-webkit-background-clip:text;background-clip:text;color:transparent}}
.vert{{transform:rotate(-90deg);transform-origin:left top;white-space:nowrap;line-height:1}}
.card{{background:#fff;border-radius:30px;padding:40px 38px 36px;box-shadow:0 40px 70px -30px rgba(2,12,50,.55)}}
.lista{{margin-top:30px;display:flex;flex-direction:column;gap:22px}} .li{{display:flex;align-items:center;gap:18px;font-family:Montserrat;font-weight:800;font-size:26px;white-space:nowrap;color:{MAR};text-transform:uppercase}}
.li b{{font-weight:900;font-size:62px;color:{ROY};letter-spacing:-.04em;min-width:86px}}
.opc{{margin-top:26px;display:flex;flex-direction:column;gap:14px}} .op{{display:flex;align-items:center;gap:16px;border:2.5px solid {ROY};border-radius:16px;padding:12px 16px;font-family:Montserrat;font-weight:800;font-size:27px;color:{MAR};text-transform:uppercase}}
.op b{{display:grid;place-items:center;width:44px;height:44px;border-radius:50%;background:{ROY};color:#fff;font-size:24px}}
.pill{{left:76px;top:62px;display:flex;align-items:center;gap:12px;background:rgba(255,255,255,.92);border-radius:999px;padding:6px 20px 6px 6px;font-family:Montserrat;font-weight:700;font-size:21px;color:{MAR};box-shadow:0 10px 20px -12px rgba(2,12,50,.5)}}
.pill img{{width:46px;height:46px;border-radius:50%;object-fit:cover}}
.logo{{left:80px;top:1150px;width:236px;filter:drop-shadow(0 8px 16px rgba(2,12,50,.28))}}
</style></head><body>{secs}</body></html>"""
open(f'{d}/artes.html', 'w').write(html)
