# v14.3 · datas comemorativas (engenharia reversa Designi + Behance, 03/11: Anton nos títulos, Leo maior, cartão na frente do peito, cenário real com véu)
# base: v14.2 · do Leo Pinto modeladas nas referências do Lindson (Marcelo Tavares, Mara Costa, Givago,
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
H = lambda txt, fs, cor='#fff', extra='': f'<div class="H" style="font-size:{fs}px;color:{cor};{extra}">{txt}</div>'
GRAD = f'background:linear-gradient(180deg,#FFE066,{SOL} 45%,{LAR});-webkit-background-clip:text;background-clip:text;color:transparent'
# 1 · 15/11 · LARANJA · FOTO · Leo grande + cartão-checklist na frente do peito (Designi "checklist da semana")
P.append(('p1-15-11', AMARELO, f"""
<div class="a tilt" style="left:84px;top:150px">{cx('15 de novembro', MAR, '#fff', 34)}</div>
<div class="a L" style="left:92px;top:220px;font-size:20px;line-height:1.5;color:{MAR}">Proclamação<br>da República</div>
{foto('leo-27-original.png', 560, 420, 250, 636, .98)}
<div class="a card" style="left:96px;top:690px;width:800px;transform:rotate(-2deg);padding:28px 36px 30px">
 <div style="display:flex;align-items:baseline;gap:18px"><span class="K" style="font-size:46px;color:{LAR};white-space:nowrap">se liga!</span>{H('O que faz um vereador?', 62, ROY)}</div>
 <div class="lista" style="margin-top:18px;gap:14px">{''.join(f'<div class="li"><b>0{i+1}</b><span>{t}</span></div>' for i, t in enumerate(['Fiscaliza a prefeitura', 'Vota as leis da cidade', 'Leva a demanda do seu bairro']))}</div></div>
<div class="a K" style="left:540px;top:1170px;width:440px;text-align:right;font-size:44px;color:{MAR}">na República,<br>a voz é do povo</div>"""))
# 2 · 20/11 · AZUL · SÓ LOGO · palavra repetida gigante em Anton, inclinada
P.append(('p2-20-11', AZUL, f"""{mapa(520, 760, 640, '#BFD8FF', .16)}
<div class="a" style="left:70px;top:150px;transform:rotate(-4deg);transform-origin:left top">{''.join(H('Orgulho', 236, 'rgba(255,255,255,.14)' if i != 2 else '#fff', 'line-height:.86;' + (GRAD if i == 2 else '')) for i in range(4))}</div>
<div class="a tilt" style="left:84px;top:930px">{cx('da nossa gente', '#fff', ROY, 64)}</div>
<div class="a K" style="left:96px;top:1036px;font-size:58px;color:{SOL}">respeito, memória e luta</div>
<div class="a M" style="left:560px;top:1196px;width:440px;text-align:right;font-size:21px;line-height:1.55;color:#fff">20 de novembro · Dia de Zumbi<br>e da Consciência Negra</div>"""))
# 3 · 11/12 · LARANJA · FOTO + CENÁRIO (obra) · foto real em cima com véu azul, manchete Anton no meio, Leo à direita
P.append(('p3-11-12', AMARELO, f"""<img class="a" src="assets/banco-obra.jpg" style="left:0;top:0;width:1080px;height:820px;object-fit:cover;object-position:40% 50%">
<div class="a" style="left:0;top:0;width:1080px;height:830px;background:linear-gradient(180deg,rgba(21,57,190,.78) 0,rgba(35,80,245,.55) 55%,rgba(255,138,31,0) 100%)"></div>
<div class="a" style="left:0;top:560px;width:1080px;height:300px;background:linear-gradient(180deg,rgba(255,138,31,0),#FF8A1F 80%)"></div>
{foto('leo-02-original.png', 820, 520, 270, 561, .70)}
<div class="a tilt" style="left:84px;top:230px">{cx('11 de dezembro', MAR, '#fff', 36)}</div>
<div class="a" style="left:80px;top:700px">{H('Dia do', 118, '#fff', 'line-height:.86;text-shadow:0 8px 24px rgba(120,40,0,.35)')}{H('Engenheiro', 140, MAR, 'line-height:.86;text-shadow:0 6px 18px rgba(255,170,90,.6)')}</div>
<div class="a K" style="left:90px;top:1010px;width:560px;font-size:48px;color:#fff;text-shadow:0 4px 16px rgba(120,40,0,.4)">olho de engenheiro<br>a serviço do povo</div>"""))
# 4 · 25/12 · AZUL · CENÁRIO (sala de Natal, Pexels 30073590) · véu azul à esquerda, árvore visível à direita
P.append(('p4-25-12', AZUL, f"""<img class="a" src="assets/banco-natal2.jpg" style="inset:0;width:1080px;height:1350px;object-fit:cover;object-position:30% 50%">
<div class="a" style="inset:0;background:linear-gradient(95deg,rgba(8,32,99,.96) 0,rgba(21,57,190,.86) 42%,rgba(35,80,245,.25) 78%,rgba(35,80,245,.05) 100%)"></div>
<div class="a K" style="left:84px;top:220px;font-size:96px;color:{SOL}">feliz</div>
<div class="a" style="left:80px;top:320px">{H('Natal', 300, '#fff', 'line-height:.86;text-shadow:0 12px 40px rgba(2,12,50,.45)')}</div>
<div class="a tilt" style="left:84px;top:610px">{cx('São João Batista!', LAR, '#fff', 56)}</div>
<div class="a M" style="left:96px;width:560px;top:730px;font-size:30px;line-height:1.5;color:#fff;text-transform:none;font-weight:600;letter-spacing:.01em">Que a fé, a família e o amor encham cada casa da nossa cidade.</div>"""))
# 5 · 31/12 · LARANJA · FOTO + CENÁRIO (rua) · cartão-enquete, bloco azul com a rua em duotone atrás do Leo
P.append(('p5-31-12', AMARELO, f"""
<div class="a" style="inset:0;clip-path:polygon(62% 0,100% 0,100% 100%,40% 100%)"><img src="assets/banco-rua.jpg" style="position:absolute;inset:0;width:1080px;height:1350px;object-fit:cover;filter:grayscale(1) contrast(1.1)"><div style="position:absolute;inset:0;background:{ROY};mix-blend-mode:multiply;opacity:.92"></div></div>
{foto('leo-10-original.png', 870, 560, 240, 1000, .70)}
<div class="a card" style="left:76px;top:190px;width:640px;transform:rotate(-2deg)">
 <div style="display:flex;align-items:baseline;gap:14px"><span class="K" style="font-size:46px;color:{LAR}">ei!</span>{H('O que o seu bairro', 64, ROY)}</div>{cx('precisa em 2027?', SOL, MAR, 44, 'margin-top:6px')}
 <div class="opc">{''.join(f'<div class="op"><b>{l}</b>{t}</div>' for l, t in zip('ABCD', ['Saúde perto de casa', 'Ruas e estradas', 'Educação e juventude', 'Emprego e renda']))}</div>
 <div style="margin-top:22px;display:flex;align-items:center;gap:18px">{cx('Comenta a letra', MAR, '#fff', 34)}<span class="K" style="font-size:34px;max-width:190px;line-height:1.05;color:{ROY}">eu quero ouvir você</span></div></div>"""))
# 6 · 01/01 · AZUL · CENÁRIO (fogos, Pexels 14957414) · caixas + número gigante em Anton
P.append(('p6-01-01', AZUL, f"""<img class="a" src="assets/banco-fogos.jpg" style="inset:0;width:1080px;height:1350px;object-fit:cover;object-position:50% 20%">
<div class="a" style="inset:0;background:linear-gradient(180deg,rgba(35,80,245,.45) 0,rgba(21,57,190,.75) 45%,rgba(8,32,99,.95) 100%)"></div>
<div class="a tilt" style="left:84px;top:170px">{cx('Feliz', '#fff', ROY, 86)}<br>{cx('ano novo', LAR, '#fff', 86, 'margin-top:10px')}</div>
<div class="a" style="left:0;width:1080px;text-align:center;top:420px">{H('2027', 440, '#fff', 'line-height:.86;letter-spacing:-.01em;filter:drop-shadow(0 18px 30px rgba(2,12,50,.45));' + GRAD)}</div>
<div class="a K" style="left:0;width:1080px;top:830px;text-align:center;font-size:76px;color:#fff">São João Batista!</div>
<div class="a M" style="left:160px;width:760px;top:950px;text-align:center;font-size:28px;line-height:1.5;color:rgba(255,255,255,.92);text-transform:none;font-weight:600;letter-spacing:.01em">Que seja um ano de saúde, trabalho<br>e união pra nossa cidade.</div>"""))
secs = ''.join(f'<section class="f" id="{i}" style="background:{bg}">{c}{ASSINA(bg)}<div class="a" style="inset:0;background-image:url(&quot;{GRAO}&quot;);opacity:.10;mix-blend-mode:overlay;pointer-events:none"></div></section>' for i, bg, c in P)
html = f"""<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Anton&family=Kaushan+Script&family=Montserrat:wght@600;700;800;900&display=swap" rel="stylesheet">
<style>*{{margin:0;padding:0;box-sizing:border-box}} body{{background:#222}}
.f{{position:relative;width:1080px;height:1350px;overflow:hidden;margin-bottom:20px}} .a{{position:absolute}}
.K{{font-family:'Kaushan Script';line-height:1.08}} .B,.box,.num,.rep,.vert{{font-family:Montserrat;font-weight:900;text-transform:uppercase;letter-spacing:-.02em}}
.L,.M{{font-family:Montserrat;font-weight:700;text-transform:uppercase;letter-spacing:.3em}} .M{{letter-spacing:.08em}}
.box{{display:inline-block;white-space:nowrap;padding:10px 22px 4px;line-height:1;box-shadow:0 20px 34px -20px rgba(2,12,50,.7)}} .tilt{{transform:rotate(-3deg);transform-origin:left center}}
.num{{line-height:.8}} .H{{font-family:Anton;text-transform:uppercase;line-height:.9;white-space:nowrap;letter-spacing:.005em}} .rep{{font-size:148px;line-height:.96;color:rgba(255,255,255,.16)}}
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
