# Redes v3 · Leo Pinto (conta Pedro, 18/11/2026). Substitui as artes de redes da v2 ("péssimas").
# Referências (referencias/redes-v3/): A = Labour UK "Hope Again/Budget in full" (manchete condensada gigante + bloco de cor + pessoa recortada),
# B = GQ "Men of the Year" US/BR (capa de revista: retrato dominante, manchete empilhada atrás/na frente),
# C = Renaissance FR (cartaz de meeting: foto inteira tratada + bloco de legenda). Regras do Leo: sem grafismo, logo direto, situação, sem promessa.
from base import CSS, logo, c
F = '../assets/fotos-v3'
def ft(n): return f'{F}/{n}.png'
P = {}
CSS3 = CSS + """
.H{font-family:Barlow,sans-serif;font-weight:800;text-transform:uppercase;line-height:.82;letter-spacing:-.01em}
.p{position:absolute;filter:contrast(1.08) saturate(1.02) drop-shadow(0 30px 40px rgba(0,0,0,.55))}
.rim{filter:contrast(1.1) saturate(1.04) drop-shadow(0 0 1px rgba(255,255,255,.5)) drop-shadow(0 34px 44px rgba(0,0,0,.6))}
.k{position:absolute;font-family:Barlow;font-weight:600;letter-spacing:.24em;text-transform:uppercase;font-size:22px}
.ch{position:absolute;left:0;right:0;bottom:0}
.tag{display:inline-block;background:var(--ou);color:var(--pr);padding:0 .12em}
"""
def chao(cor, h=420): return f'<div class="ch" style="height:{h}px;background:linear-gradient(transparent,{cor} 70%)"></div>'
def fim(): return '<div class="vin"></div><div class="grao" style="opacity:.6"></div>'
def L(var, x, y, w, side='left'): return f'<img class="box" src="{logo(var)}" style="{side}:{x}px;bottom:{y}px;width:{w}px">'

# POST 1 · capa de revista (ref B, GQ Men of the Year): palavra gigante ATRÁS do Leo, foto dominante
P['r3-post-capa'] = (1080, 1350, f'''<div class="box" style="inset:0;background:radial-gradient(circle at 50% 35%,#1b2a4a,var(--pr) 70%)"></div>
<div class="H box" style="left:0;right:0;top:110px;text-align:center;font-size:250px;color:var(--la)">PRESENÇA</div>
<img class="p rim" src="{ft('d-bracos-cruzados-branca')}" style="left:50%;transform:translateX(-50%);bottom:0;width:880px">
{chao(c('preto'),460)}
<div class="k" style="left:60px;top:60px;color:var(--br)">Vereador · São João Batista</div>
<div class="H box" style="left:60px;bottom:230px;font-size:118px;color:var(--br)">que <span class="tag">resolve.</span></div>
{L('branco',60,48,250)}<div class="k" style="right:60px;bottom:66px;color:#bbb;font-size:18px">Mandato 2025–2028</div>{fim()}''')

# POST 2 · bloco laranja Labour (ref A): manchete gigante 3 linhas, Leo invadindo o bloco
P['r3-post-bloco'] = (1080, 1350, f'''<div class="box" style="inset:0;background:var(--la)"></div>
<div class="box" style="left:0;right:0;bottom:0;height:430px;background:var(--ma2)"></div>
<div class="H box" style="left:56px;top:70px;font-size:205px;color:var(--pr)">Palavra<br>dada.<br><span style="color:var(--br)">Obra</span><br><span style="color:var(--br)">feita.</span></div>
<img class="p" src="{ft('b-punho')}" style="right:-260px;bottom:0;width:980px">
<div class="box" style="left:60px;bottom:250px;width:400px;font:600 25px/1.4 Mont;color:var(--br)">Indicação, cobrança técnica e acompanhamento até a entrega, junto com a Prefeitura.</div>
{L('branco',60,56,240)}{fim()}''')

# POST 3 · foto inteira tratada + legenda (ref C, Renaissance): close duotom marinho, frase em serifa grande
P['r3-post-frase'] = (1080, 1350, f'''<div class="box" style="inset:0;background:var(--ma)"></div>
<img class="p" src="{ft('j-close-sorrindo')}" style="right:-120px;top:0;width:1150px;filter:grayscale(1) contrast(1.25) brightness(1.05);mix-blend-mode:luminosity;opacity:.95">
<div class="box" style="inset:0;background:linear-gradient(90deg,var(--ma2) 0%,rgba(2,26,61,.85) 38%,transparent 70%)"></div>
{chao(c('marinho2'),520)}
<div class="H box" style="left:60px;top:70px;font-size:420px;color:var(--la);line-height:.7">“</div>
<div class="ci box" style="left:60px;bottom:270px;width:900px;font-size:92px;font-weight:900;line-height:1.02">Vereador bom<br>não some depois<br><span style="color:var(--ou)">da eleição.</span></div>
{L('branco',60,60,230)}<div class="k" style="right:60px;bottom:78px;color:var(--br);font-size:18px">Leo Pinto</div>{fim()}''')

# CARROSSEL 4 telas, cada uma com layout próprio
P['r3-car-1'] = (1080, 1350, f'''<div class="box" style="inset:0;background:var(--pr)"></div>
<div class="box" style="left:0;top:0;width:560px;bottom:0;background:var(--la)"></div>
<img class="p rim" src="{ft('f-punhos')}" style="left:300px;bottom:0;width:820px">
<div class="k" style="left:56px;top:64px;color:var(--pr)">Prestação de contas · 1/4</div>
<div class="H box" style="left:56px;top:170px;font-size:128px;color:var(--pr);z-index:2">O que<br>o mandato<br><span style="color:var(--br)">entregou</span></div>
{chao('rgba(8,9,12,.95)',260)}{L('branco',56,50,220)}<div class="k" style="right:56px;bottom:70px;color:var(--ou)">Arraste →</div>{fim()}''')
P['r3-car-2'] = (1080, 1350, f'''<div class="box" style="inset:0;background:var(--br)"></div>
<div class="H box" style="left:40px;top:-40px;font-size:760px;color:var(--la)">01</div>
<div class="box" style="left:60px;top:700px;width:960px"><div class="k" style="position:static;color:var(--la2)">Indicação aprovada · povoado · data</div>
<div class="H" style="font-size:132px;color:var(--pr);margin-top:22px">Nome da obra<br>ou do serviço</div>
<div style="font:400 30px/1.45 Mont;color:#333;margin-top:30px;width:860px">O que foi feito, onde e quando, com a foto real da entrega.</div></div>
<div class="k" style="left:60px;bottom:66px;color:#999;font-size:17px">Exemplo ilustrativo do modelo</div>{L('marinho',60,40,190,'right')}''')
P['r3-car-3'] = (1080, 1350, f'''<div class="box" style="inset:0;background:var(--ma2)"></div>
<div class="box" style="left:60px;top:60px;right:60px;height:700px;overflow:hidden;outline:3px solid var(--ou);outline-offset:-3px;background:radial-gradient(circle at 60% 40%,#2350F5,#021A3D)"><img src="{ft('h-close-amarela')}" style="position:absolute;right:-40px;bottom:0;width:900px"><div class="k" style="left:24px;bottom:20px;color:#fff;font-size:16px;background:rgba(0,0,0,.5);padding:6px 10px">Aqui entra a foto real da entrega</div></div>
<div class="H box" style="left:60px;top:810px;font-size:130px;color:var(--ou)">Antes da obra,<br><span style="color:var(--br)">o olho técnico.</span></div>
<div class="box" style="left:60px;top:1080px;width:900px;font:400 30px/1.45 Mont;color:#cfd6e6">Visita técnica, ofício e acompanhamento junto com a Prefeitura, do pedido até a entrega.</div>
{L('mono',60,40,170,'right')}''')
P['r3-car-4'] = (1080, 1350, f'''<div class="box" style="inset:0;background:var(--la)"></div>
<img class="p" src="{ft('i-maos-abertas-branca')}" style="left:50%;transform:translateX(-50%);bottom:0;width:700px">
{chao('rgba(180,80,12,.98)',500)}
<div class="H box" style="left:0;right:0;top:70px;text-align:center;font-size:150px;color:var(--pr)">Tem um pedido<br><span style="color:var(--br)">no seu povoado?</span></div>
<div class="box" style="left:0;right:0;bottom:250px;text-align:center"><span class="H tag" style="font-size:70px">Chama no direct</span></div>
{L('branco',0,40,220,'left').replace('left:0px','left:50%;transform:translateX(-50%)')}{fim()}''')

# STORY e REELS (9:16)
P['r3-story'] = (1080, 1920, f'''<div class="box" style="inset:0;background:radial-gradient(circle at 50% 30%,#22355e,var(--pr) 70%)"></div>
<div class="H box" style="left:-20px;top:120px;font-size:400px;color:var(--la);line-height:.78">LEO<br>NA<br>RUA</div>
<img class="p rim" src="{ft('e-celular')}" style="right:-120px;bottom:0;width:1050px">
{chao(c('preto'),620)}
<div class="H box" style="left:70px;bottom:420px;font-size:120px">Hoje no<br><span class="tag">povoado</span></div>
<div class="k" style="left:70px;bottom:350px;color:#ccc">Nome do povoado · horário</div>{L('branco',70,110,260)}{fim()}''')
P['r3-reels'] = (1080, 1920, f'''<div class="box" style="inset:0;background:var(--la)"></div>
<div class="box" style="left:0;right:0;bottom:0;height:820px;background:var(--pr)"></div>
<img class="p rim" src="{ft('a-close-laranja')}" style="left:50%;transform:translateX(-50%);top:420px;width:1300px">
<div class="H box" style="left:0;right:0;top:110px;text-align:center;font-size:200px;color:var(--pr)">Pediu?</div>
{chao(c('preto'),560)}
<div class="H box" style="left:0;right:0;bottom:330px;text-align:center;font-size:190px"><span class="tag">Tá feito.</span></div>
{L('branco',0,90,240).replace('left:0px','left:50%;transform:translateX(-50%)')}{fim()}''')

# 4 QUADROS · vinheta forte: número gigante + nome do quadro numa barra amarela fixa no topo, cor própria de cada quadro
Q = [('q1', '01', 'Leo no', 'Povoado', 'Segunda', 'la', 'c-maos-juntas-laranja', 'pr'),
     ('q2', '02', 'Pediu?', 'Tá feito.', 'Terça', 'ma', 'g-maos-juntas-amarela', 'br'),
     ('q3', '03', 'Olho de', 'Engenheiro', 'Quinta', 'pr', 'h-close-amarela', 'br'),
     ('q4', '04', 'Gente da', 'Baixada', 'Sexta', 'ro', 'd-bracos-cruzados-branca', 'br')]
for q, n, t1, t2, dia, bg, f, tx in Q:
    P['r3-quadro-' + q] = (1080, 1350, f'''<div class="box" style="inset:0;background:var(--{bg})"></div>
<img class="p rim" src="{ft(f)}" style="right:-200px;bottom:0;width:{1000 if 'close' not in f else 1080}px">
<div class="H box" style="left:46px;top:150px;font-size:400px;color:transparent;-webkit-text-stroke:4px var(--ou);z-index:3">{n}</div>
<div class="box" style="left:0;top:0;right:0;height:110px;background:var(--ou);display:flex;align-items:center;justify-content:space-between;padding:0 56px"><span class="H" style="font-size:64px;color:var(--pr)">Quadro {n}</span><span class="k" style="position:static;color:var(--pr)">{dia} · Reels</span></div>
{chao('rgba(8,9,12,.96)',560)}
<div class="H box" style="left:56px;bottom:250px;font-size:160px;color:var(--{tx if bg!='pr' else 'br'})"><span style="color:var(--br)">{t1}</span><br><span style="color:var(--{'la' if bg!='la' else 'ou'})">{t2}</span></div>
{L('branco',56,56,220)}{fim()}''')

html = f'<!doctype html><meta charset="utf-8"><style>{CSS3}.t{{position:relative;overflow:hidden;margin:20px}}</style>' + ''.join(
    f'<div class="t" id="{k}" style="width:{w}px;height:{h}px">{v}</div>' for k, (w, h, v) in P.items())
open('redes3.html', 'w').write(html)
print(len(P))
