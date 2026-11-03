# v14.8 · 25/12 copiando o modelo "SOU PEDRO" enviado pelo Lindson.
# v14.7 · aprovados pelo Lindson (03/11): 15/11, 20/11, 11/12 (ficha técnica) e 31/12. Refeitos: 25/12 e 01/01.
# v14.6 · cada data copia um modelo específico do Designi (busca por data, 03/11; capturas em referencias/). 15/11 aprovado igual.
# v14.5 · regra do Lindson (03/11): nunca criar do zero, copiar o que já existe. Cada post copia a composição de um modelo enviado por ele (ver comentário de cada post).
# v14.4 · 15/11 aprovado pelo Lindson (igual à v14.3); 20/11 a 01/01 refeitos em linguagem de big player: bento grid, ficha técnica com anotações,
# minimalismo premium, interface de story, contagem estilo Wrapped. Recorte: borda cortada da foto sempre fora da arte (checado). Conta Lindson, 03/11.
# base: v14.3 · datas comemorativas (engenharia reversa Designi + Behance, 03/11: Anton nos títulos, Leo maior, cartão na frente do peito, cenário real com véu)
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
def ASSINA(fundo, pid=''):
    lg = 'logo-marinho.png' if fundo in (AMARELO, MESH_LAR) else 'logo.png'
    return ('<div class="a pill"><img src="assets/avatar.jpg">@_leonardopinto</div>' +
            (f'<img class="a logo" src="assets/{lg}">' if pid != 'p4-25-12' else ''))
def foto(arq, cx, olhos_y, olho_rec, cx_rec, esc, extra=''):
    im = _I.open(f'{d}/assets/{arq}'); w, h = im.size; import numpy as _n; al = _n.array(im.getchannel('A')) > 40
    x0, y0 = cx - cx_rec*esc, olhos_y - olho_rec*esc; x1, y1 = x0 + w*esc, y0 + h*esc
    def visivel(idx, ini, fim): return any(0 <= ini + k*esc <= fim for k in _n.where(idx)[0])  # algum pixel dessa borda cai dentro da arte?
    for nome, cond in [('base', y1 < 1350 and visivel(al[-1], x0, 1080)), ('direita', x1 < 1080 and visivel(al[:, -1], y0, 1350)),
                       ('esquerda', x0 > 0 and visivel(al[:, 0], y0, 1350)), ('topo', y0 > 0 and visivel(al[0], x0, 1080))]:
        assert not cond, f'CORTE APARENTE: {arq} tem borda cortada na {nome} dentro da arte'
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
GLASS = 'background:linear-gradient(135deg,rgba(255,255,255,.20),rgba(255,255,255,.06));border:1.5px solid rgba(255,255,255,.30);backdrop-filter:blur(22px);-webkit-backdrop-filter:blur(22px);border-radius:34px;box-shadow:0 30px 60px -34px rgba(2,12,50,.6),inset 0 1px 0 rgba(255,255,255,.35)'
CHIP = lambda t, cor='#fff', fundo='rgba(255,255,255,.16)', extra='': f'<div class="chip" style="color:{cor};background:{fundo};{extra}"><i></i>{t}</div>'
MESH_AZUL = (f'radial-gradient(700px 600px at 85% 90%,rgba(255,122,26,.55),transparent 60%),radial-gradient(800px 700px at 10% 10%,#4C7DFF,transparent 60%),'
             f'radial-gradient(900px 900px at 60% 40%,{ROY},transparent 70%),linear-gradient(160deg,#1539BE,#071A55)')
MESH_LAR = (f'radial-gradient(700px 650px at 15% 10%,#FFD25A,transparent 60%),radial-gradient(800px 700px at 90% 85%,#E8590C,transparent 60%),'
            f'radial-gradient(700px 600px at 95% 10%,rgba(35,80,245,.35),transparent 60%),linear-gradient(160deg,#FF9A22,{LAR})')
# 2 · 20/11 · AZUL · cópia do modelo Designi "20 de novembro · Ser preto é ser resistência, é ser gigante": retrato P&B inteiro, texto à esquerda no escuro
P.append(('p2-20-11', AZUL, f"""<img class="a" src="assets/banco-retrato.jpg" style="inset:0;width:1080px;height:1350px;object-fit:cover;object-position:70% 30%;filter:grayscale(1) contrast(1.05)">
<div class="a" style="inset:0;background:#0B2A8A;mix-blend-mode:multiply;opacity:.35"></div>
<div class="a" style="inset:0;background:linear-gradient(90deg,rgba(4,14,46,.92) 0,rgba(4,14,46,.6) 42%,rgba(4,14,46,0) 70%)"></div>
<div class="a" style="left:84px;top:300px">{H('20', 300, '#fff', 'line-height:.8')}<div class="L" style="font-size:24px;color:#fff;margin-top:14px">de novembro</div></div>
<div class="a" style="left:84px;top:640px;width:560px">{H('Orgulho da', 104, '#fff', 'line-height:.9')}{H('nossa gente', 104, '#fff', 'line-height:.9;' + GRAD)}
 <div class="K" style="font-size:52px;color:#fff;margin-top:14px">respeito, memória e luta</div></div>
<div class="a L" style="left:84px;top:1060px;font-size:19px;color:rgba(255,255,255,.85)">Dia de Zumbi e da Consciência Negra</div>"""))
# 3 · 11/12 · LARANJA · FOTO · APROVADO pelo Lindson (03/11) · FICHA TÉCNICA: palavra gigante atrás do Leo + anotações com linha e ponto (linguagem de produto/tecnologia)
P.append(('p3-11-12', MESH_LAR, f"""
<div class="a" style="left:0;width:1080px;top:250px;text-align:center">{H('Engenheiro', 200, MAR, 'line-height:.86;letter-spacing:-.005em')}</div>
{foto('leo-02-fino.png', 540, 620, 270, 561, .80)}
<div class="a" style="left:84px;top:150px">{CHIP('11 de dezembro · Dia do Engenheiro', MAR, 'rgba(255,255,255,.75)')}</div>
<svg class="a" style="left:0;top:0" width="1080" height="1350"><g stroke="#fff" stroke-width="2.5" fill="none" stroke-linecap="round">
 <path d="M300 700 L190 700 L150 660"/><path d="M790 800 L1010 800"/><path d="M360 960 L210 960"/></g>
 <g fill="#fff"><circle cx="300" cy="700" r="9"/><circle cx="790" cy="800" r="9"/><circle cx="360" cy="960" r="9"/></g></svg>
<div class="a" style="left:70px;top:600px">{CHIP('Formação', MAR, 'rgba(255,255,255,.9)')}<div class="H" style="font-size:44px;color:#fff;margin-top:8px;text-shadow:0 4px 14px rgba(120,40,0,.35)">Engenharia</div></div>
<div class="a" style="left:760px;top:680px;width:260px;text-align:right">{CHIP('Mandato', MAR, 'rgba(255,255,255,.9)')}<div class="H" style="font-size:44px;color:#fff;margin-top:8px;text-shadow:0 4px 14px rgba(120,40,0,.35)">Vereador</div></div>
<div class="a" style="left:70px;top:860px">{CHIP('Cidade', MAR, 'rgba(255,255,255,.9)')}<div class="H" style="font-size:40px;color:#fff;margin-top:8px;text-shadow:0 4px 14px rgba(120,40,0,.35)">São João Batista</div></div>
<div class="a" style="left:470px;top:1110px;width:540px;{GLASS};padding:24px 30px"><div class="K" style="font-size:46px;color:#fff">olho de engenheiro</div><div class="M" style="font-size:22px;color:#fff;margin-top:6px">a serviço do povo</div></div>"""))
# 4 · 25/12 · AZUL · FOTO · cópia do modelo "SOU PEDRO" enviado pelo Lindson (03/11, Designi): frase repetida 3× em duas cores atrás da pessoa,
#   pessoa no centro cortada no peito, faixa clara na base e a logo dentro da cápsula (laranja por fora, marinho por dentro)
P.append(('p4-25-12', AZUL, f"""
<div class="a" style="left:0;width:1080px;top:160px;text-align:center">{''.join(f'<div class="H" style="font-size:228px;line-height:.86;letter-spacing:-.005em"><span style="{GRAD}">Feliz</span><span style="color:#fff">Natal</span></div>' for _ in range(3))}</div>
<div class="a" style="left:0;top:1010px;width:1080px;height:340px;background:linear-gradient(180deg,#E9EEF8,#FFFFFF);box-shadow:0 -24px 40px -20px rgba(2,12,50,.45)"></div>
{foto('leo-08-fino.png', 540, 600, 260, 580, .84)}
<div class="a" style="left:190px;top:1110px;width:700px;height:170px;border-radius:999px;background:linear-gradient(90deg,#FFB020,{LAR});padding:16px;box-shadow:0 24px 40px -20px rgba(120,40,0,.6)">
 <div style="width:100%;height:100%;border-radius:999px;background:linear-gradient(90deg,{MAR},#0B3486);display:flex;align-items:center;justify-content:center;gap:26px">
  <img src="assets/logo.png" style="height:112px"><div class="M" style="font-size:20px;line-height:1.5;color:#fff;text-align:left">Feliz Natal,<br>São João Batista</div></div></div>"""))
# 5 · 31/12 · LARANJA · cópia do modelo Designi "Qual a marca da sua primeira bike?": palavra gigante atrás, cartão "Conta pra gente!" com lista numerada
P.append(('p5-31-12', AMARELO, f"""
<div class="a" style="left:-30px;top:880px;width:1140px;text-align:center">{H('2027', 620, 'rgba(255,255,255,.18)', 'line-height:.8')}</div>
<div class="a" style="left:0;width:1080px;top:150px;text-align:center"><div class="L" style="font-size:22px;color:{MAR}">31 de dezembro</div>
 {H('O que o seu bairro', 96, '#fff', 'margin-top:12px;text-shadow:0 8px 24px rgba(120,40,0,.35)')}<div style="margin-top:6px">{cx('precisa em 2027?', MAR, '#fff', 64, 'font-family:Anton;letter-spacing:.01em')}</div></div>
<div class="a" style="left:150px;top:520px;width:780px;background:#fff;border-radius:36px;overflow:hidden;box-shadow:0 40px 70px -30px rgba(120,40,0,.6)">
 <div class="H" style="background:{ROY};color:#fff;text-align:center;font-size:52px;padding:18px 0 14px">Conta pra gente!</div>
 <div style="padding:26px 34px 30px;display:flex;flex-direction:column;gap:14px">{''.join(f'<div class="op"><b>{n}</b>{t}</div>' for n, t in zip('1234', ['Saúde perto de casa', 'Ruas e estradas', 'Educação e juventude', 'Emprego e renda']))}</div></div>
<div class="a" style="left:0;width:1080px;top:1100px;text-align:center"><span class="K" style="font-size:50px;color:#fff;text-shadow:0 4px 16px rgba(120,40,0,.4)">comenta o número aqui embaixo</span></div>"""))
# 6 · 01/01 · AZUL · cópia do modelo Designi "um feliz Ano Novo 2026" / "feliz 2025 galera" (balões dourados de número, texto central)
P.append(('p6-01-01', AZUL, f"""<img class="a" src="assets/banco-baloes.jpg" style="inset:0;width:1080px;height:1350px;object-fit:cover;object-position:30% 75%">
<div class="a" style="inset:0;background:{ROY};mix-blend-mode:multiply;opacity:.40"></div>
<div class="a" style="inset:0;background:linear-gradient(180deg,rgba(7,26,85,.88) 0,rgba(7,26,85,.55) 38%,rgba(7,26,85,.10) 62%,rgba(7,26,85,.85) 100%)"></div>
<div class="a" style="left:0;width:1080px;top:190px;text-align:center"><div class="K" style="font-size:110px;color:#fff;line-height:1">um feliz</div>
 {H('Ano novo', 210, '#fff', 'line-height:.84;margin-top:-6px')}
 {H('2027', 330, '#fff', 'line-height:.84;margin-top:6px;filter:drop-shadow(0 16px 28px rgba(2,12,50,.5));' + GRAD)}</div>
<div class="a" style="left:0;width:1080px;top:960px;text-align:center"><div class="L" style="font-size:20px;color:#fff">São João Batista</div>
 <div class="M" style="margin:18px auto 0;width:640px;font-size:26px;line-height:1.5;color:rgba(255,255,255,.92);text-transform:none;font-weight:600;letter-spacing:.01em">Que seja um ano de saúde, trabalho e união pra nossa cidade.</div></div>"""))
secs = ''.join(f'<section class="f" id="{i}" style="background:{bg}">{c}{ASSINA(bg, i)}<div class="a" style="inset:0;background-image:url(&quot;{GRAO}&quot;);opacity:.10;mix-blend-mode:overlay;pointer-events:none"></div></section>' for i, bg, c in P)
html = f"""<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Anton&family=Kaushan+Script&family=Montserrat:wght@600;700;800;900&display=swap" rel="stylesheet">
<style>*{{margin:0;padding:0;box-sizing:border-box}} body{{background:#222}}
.f{{position:relative;width:1080px;height:1350px;overflow:hidden;margin-bottom:20px}} .a{{position:absolute}}
.K{{font-family:'Kaushan Script';line-height:1.08}} .B,.box,.num,.rep,.vert{{font-family:Montserrat;font-weight:900;text-transform:uppercase;letter-spacing:-.02em}}
.L,.M{{font-family:Montserrat;font-weight:700;text-transform:uppercase;letter-spacing:.3em}} .M{{letter-spacing:.08em}}
.box{{display:inline-block;white-space:nowrap;padding:10px 22px 4px;line-height:1;box-shadow:0 20px 34px -20px rgba(2,12,50,.7)}} .tilt{{transform:rotate(-3deg);transform-origin:left center}}
.num{{line-height:.8}} .bento{{position:absolute;overflow:hidden}}
.chip{{display:inline-flex;align-items:center;gap:10px;padding:10px 18px;border-radius:999px;font-family:Montserrat;font-weight:800;font-size:18px;letter-spacing:.16em;text-transform:uppercase;white-space:nowrap;backdrop-filter:blur(10px)}} .chip i{{width:9px;height:9px;border-radius:50%;background:{LAR};box-shadow:0 0 0 4px rgba(255,122,26,.25)}}
.rap{{display:flex;align-items:center;gap:10px;border:2px solid {ROY};border-radius:999px;padding:8px 16px 8px 8px;font-family:Montserrat;font-weight:800;font-size:20px;color:{MAR};text-transform:uppercase}} .rap b{{display:grid;place-items:center;width:34px;height:34px;border-radius:50%;background:{ROY};color:#fff;font-size:18px}}
.pil{{padding:16px 34px;font-family:Montserrat;font-weight:800;font-size:26px;letter-spacing:.14em;color:#fff;text-transform:uppercase}} .H{{font-family:Anton;text-transform:uppercase;line-height:.9;white-space:nowrap;letter-spacing:.005em}} .rep{{font-size:148px;line-height:.96;color:rgba(255,255,255,.16)}}
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
