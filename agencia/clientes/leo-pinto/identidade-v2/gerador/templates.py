# Templates de redes, peças de campanha/papelaria (artes chapadas) · Leo Pinto v2 (conta Pedro, 18/11/2026)
# Cada peça cita a referência que copia (composição), regra "nada se cria, tudo se copia".
from base import CSS, logo, foto, c

A_SIM = '../assets/simbolo-sol.png'
P = {}  # id -> (w, h, html)

def fundo(cor, luz='rgba(255,122,26,.35)', x='62%', y='38%'):
    return f'<div class="box" style="inset:0;background:radial-gradient(circle at {x} {y},{luz},transparent 55%),{cor}"></div>'

def fim(): return '<div class="vin"></div><div class="grao"></div>'

# 1 · POST MANCHETE (ref: Obama "Hope" -> retrato de liderança + 1 palavra; Aston Martin -> preto profundo, foto dramática)
P['post-manchete'] = (1080, 1350, f'''
{fundo(c('preto'))}
<div class="ci box" style="left:60px;top:70px;font-size:40px;color:var(--ou);letter-spacing:.32em;font-weight:500">Vereador · São João Batista</div>
<img class="foto" src="{foto('d-bracos-cruzados-branca')}" style="right:-230px;bottom:0;width:800px">
<div class="box" style="left:60px;top:520px;width:600px">
 <div class="bc" style="font-size:150px;color:var(--br)">Presença</div>
 <div class="bc" style="font-size:150px;color:var(--la)">que resolve.</div>
</div>
<div class="hz" style="left:60px;width:420px;top:930px"></div>
<div class="box" style="left:60px;top:960px;width:430px;font:400 26px/1.45 Mont;color:#cfcac2">O mandato inteiro na rua, ao lado da Prefeitura, mostrando o que foi feito.</div>
<img class="box" src="{logo('branco')}" style="left:52px;bottom:60px;width:300px">
{fim()}''')

# 2 · POST LARANJA (xadrez; ref: Rolex -> cor de marca absoluta chapada + tipografia de autoridade)
P['post-laranja'] = (1080, 1350, f'''
<div class="box" style="inset:0;background:radial-gradient(circle at 70% 30%,#ff9a45,transparent 60%),var(--la)"></div>
<div class="bc box" style="left:-20px;top:120px;font-size:430px;color:var(--la2);opacity:.55;white-space:nowrap">MANDATO</div>
<img class="foto" src="{foto('b-punho')}" style="left:240px;bottom:0;width:1000px;filter:contrast(1.12) saturate(.95) drop-shadow(0 40px 60px rgba(60,20,0,.55))">
<div class="box" style="left:60px;top:70px" ><div class="lab" style="color:var(--pr)">Mandato que entrega</div></div>
<div class="box" style="left:60px;bottom:250px;width:520px">
 <div class="ci" style="font-size:96px;color:var(--pr);font-weight:900">Palavra</div>
 <div class="ci" style="font-size:96px;color:var(--br);font-weight:900">dada,</div>
 <div class="ci" style="font-size:96px;color:var(--pr);font-weight:900">obra feita.</div>
</div>
<div class="hz" style="left:60px;width:960px;bottom:200px;background:var(--pr)"></div>
<img class="box" src="{logo('marinho')}" style="left:52px;bottom:40px;width:250px">
<div class="lab box" style="right:60px;bottom:70px;color:var(--pr);font-size:18px">Em parceria com a Prefeitura</div>
<div class="grao"></div>''')

# 3 · POST FRASE (ref: Ralph Lauren Purple Label -> retrato em close, serifa romana centralizada, simetria)
P['post-frase'] = (1080, 1350, f'''
{fundo(c('marinho2'), 'rgba(35,80,245,.45)', '50%', '30%')}
<img class="foto" src="{foto('j-close-sorrindo')}" style="left:50%;transform:translateX(-50%);top:40px;width:820px">
<div class="box" style="left:0;right:0;top:660px;height:690px;background:linear-gradient(transparent,var(--pr) 30%)"></div>
<div class="box" style="left:80px;right:80px;top:880px;text-align:center">
 <div class="ci" style="font-size:66px;line-height:1.08">"Vereador bom<br>não some depois<br><span style="color:var(--la)">da eleição."</span></div>
</div>
<div class="hz" style="left:470px;width:140px;top:1160px"></div>
<img class="box" src="{logo('branco')}" style="left:50%;transform:translateX(-50%);bottom:50px;width:220px">
{fim()}''')

# 4-6 · CARROSSEL (ref: Pentagram/Collins -> sistema editorial; cada tela muda a composição)
P['carrossel-1'] = (1080, 1350, f'''
{fundo(c('preto'), 'rgba(255,194,14,.28)', '30%', '35%')}
<img class="foto" src="{foto('f-punhos')}" style="left:-170px;bottom:0;width:700px">
<div class="box" style="right:60px;top:90px;text-align:right"><div class="lab" style="color:var(--ou)">Prestação de contas · 01/05</div></div>
<div class="box" style="right:60px;top:300px;width:600px;text-align:right">
 <div class="bc" style="font-size:136px">O que</div><div class="bc" style="font-size:136px">o mandato</div><div class="bc" style="font-size:136px;color:var(--la)">entregou</div>
</div>
<div class="hz" style="right:60px;width:300px;top:800px"></div>
<div class="box" style="right:60px;top:830px;font:600 28px Mont;color:#cfcac2">arraste para o lado</div>
<img class="box" src="{logo('branco')}" style="right:60px;bottom:60px;width:240px">
{fim()}''')
P['carrossel-2'] = (1080, 1350, f'''
<div class="box" style="inset:0;background:var(--br)"></div>
<div class="bc box" style="left:40px;top:10px;font-size:620px;color:transparent;-webkit-text-stroke:3px var(--la);line-height:.8">02</div>
<div class="box" style="left:70px;top:560px;width:940px">
 <div class="lab" style="color:var(--la2)">Indicação aprovada · data do registro</div>
 <div class="ci" style="font-size:84px;color:var(--pr);margin-top:26px;font-weight:900">Nome da obra<br>ou do serviço</div>
 <div style="height:3px;width:200px;background:var(--pr);margin:40px 0"></div>
 <div style="font:400 32px/1.5 Mont;color:#2a2a2a;width:820px">Povoado, data e o que foi feito, com foto da entrega. Texto sempre com fato que o Leo confirmou; nada de número sem fonte.</div>
</div>
<div class="box" style="left:70px;bottom:60px;font:600 20px Barlow;letter-spacing:.2em;color:var(--la2)">EXEMPLO ILUSTRATIVO DO MODELO</div>
<img class="box" src="{logo('marinho')}" style="right:60px;bottom:40px;width:220px">''')
P['carrossel-3'] = (1080, 1350, f'''
{fundo(c('laranja'), 'rgba(255,194,14,.45)', '50%', '20%')}
<img class="foto" src="{foto('i-maos-abertas-branca')}" style="left:50%;transform:translateX(-50%);bottom:0;width:680px;filter:contrast(1.1) drop-shadow(0 40px 60px rgba(60,20,0,.5))">
<div class="box" style="left:0;right:0;top:90px;text-align:center">
 <div class="ci" style="font-size:76px;color:var(--pr);font-weight:900">Tem um pedido<br>no seu povoado?</div>
 <div class="lab" style="color:var(--br);margin-top:26px;font-size:26px">Manda no direct · o Leo responde</div>
</div>
<img class="box" src="{logo('marinho')}" style="left:60px;bottom:40px;width:220px">
<div class="grao"></div>''')

# 7 · STORY (ref: Aston Martin -> preto, foto escura, faixa reta, CTA discreto)
P['story'] = (1080, 1920, f'''
{fundo(c('preto'), 'rgba(255,122,26,.40)', '50%', '42%')}
<div class="ci box" style="left:0;right:0;top:190px;text-align:center;font-size:34px;letter-spacing:.4em;color:var(--ou);font-weight:500">Hoje na agenda</div>
<img class="foto" src="{foto('e-celular')}" style="left:50%;transform:translateX(-50%);top:330px;width:1080px">
<div class="box" style="left:0;right:0;top:1300px;height:620px;background:linear-gradient(transparent,var(--pr) 35%)"></div>
<div class="box" style="left:70px;right:70px;top:1420px;text-align:center"><div class="bc" style="font-size:150px">Leo no <span style="color:var(--la)">Povoado</span></div>
<div class="hz" style="position:relative;width:200px;margin:34px auto"></div>
<div class="lab" style="font-size:26px">Segunda · 20h45 · no Reels</div></div>
<img class="box" src="{logo('branco')}" style="left:50%;transform:translateX(-50%);bottom:90px;width:240px">
{fim()}''')

# 8 · CAPA DE REELS (ref: Macron 2017 -> retrato frontal, nome grande, simetria)
P['reels'] = (1080, 1920, f'''
{fundo(c('marinho2'), 'rgba(255,122,26,.42)', '50%', '30%')}
<div class="bc box" style="left:0;right:0;top:120px;text-align:center;font-size:330px;color:rgba(255,255,255,.07)">ENGENHEIRO</div>
<img class="foto" src="{foto('a-close-laranja')}" style="left:50%;transform:translateX(-50%);top:300px;width:1180px">
<div class="box" style="left:0;right:0;top:1180px;height:740px;background:linear-gradient(transparent,var(--pr) 30%)"></div>
<div class="box" style="left:70px;right:70px;top:1340px;text-align:center">
 <div class="lab" style="color:var(--ou);font-size:28px">Quadro semanal · quinta</div>
 <div class="ci" style="font-size:118px;margin-top:20px;font-weight:900">Olho de<br><span style="color:var(--la)">Engenheiro</span></div></div>
<img class="box" src="{logo('branco')}" style="left:50%;transform:translateX(-50%);bottom:90px;width:240px">
{fim()}''')

# 9-12 · 4 QUADROS SEMANAIS (capas feed 4:5, xadrez laranja/escuro, cada uma com composição própria)
Q = [('q1', 'Leo no', 'Povoado', 'Segunda · 20h45 · Reels', 'g-maos-juntas-amarela', 'laranja', 'Leo na rua'),
     ('q2', 'Pediu?', 'Tá feito.', 'Terça · 12h45 · Carrossel', 'd-bracos-cruzados-branca', 'escuro', 'Mandato que entrega'),
     ('q3', 'Olho de', 'Engenheiro', 'Quinta · 20h45 · Reels', 'h-close-amarela', 'laranja', 'A cidade que eu sonho'),
     ('q4', 'Gente da', 'Baixada', 'Sexta · 12h45 · Reels', 'c-maos-juntas-laranja', 'escuro', 'Nossa Baixada')]
for i, (k, t1, t2, dia, f, cor, linha) in enumerate(Q):
    esc = cor == 'escuro'
    bg = fundo(c('preto'), 'rgba(255,122,26,.38)', '65%', '35%') if esc else \
        '<div class="box" style="inset:0;background:radial-gradient(circle at 65% 30%,#ff9a45,transparent 60%),var(--la)"></div>'
    tc, ac = ('var(--br)', 'var(--la)') if esc else ('var(--pr)', 'var(--br)')
    lado = 'right:-200px' if i % 2 == 0 else 'left:-200px'
    tx = 'left:60px' if i % 2 == 0 else 'right:60px;text-align:right'
    num = f'<div class="bc box" style="{tx.split(";")[0]};top:40px;font-size:300px;color:transparent;-webkit-text-stroke:3px {"rgba(255,255,255,.18)" if esc else "rgba(8,9,12,.25)"}">0{i+1}</div>'
    P['quadro-' + k] = (1080, 1350, f'''{bg}{num}
<img class="foto" src="{foto(f)}" style="{lado};bottom:0;width:740px;{'' if esc else 'filter:contrast(1.1) drop-shadow(0 40px 60px rgba(60,20,0,.5))'}">
<div class="box" style="{tx};top:430px;width:560px">
 <div class="lab" style="color:{'var(--ou)' if esc else 'var(--pr)'}">Quadro semanal · {linha}</div>
 <div class="ci" style="font-size:92px;color:{tc};margin-top:24px;font-weight:900">{t1}</div>
 <div class="ci" style="font-size:92px;color:{ac};font-weight:900">{t2}</div>
</div>
<div class="hz" style="{tx.split(";")[0]};width:520px;bottom:260px;background:{'var(--ou)' if esc else 'var(--pr)'}"></div>
<div class="lab box" style="{tx};bottom:200px;color:{tc};font-size:24px">{dia}</div>
<img class="box" src="{logo('branco' if esc else 'marinho')}" style="{tx.split(";")[0]};bottom:40px;width:230px">
{fim() if esc else '<div class="grao"></div>'}''')

# 13 · AVATAR / PERFIL (ref: Rolex coroa -> símbolo isolado com aro metálico)
P['avatar'] = (1080, 1080, f'''
{fundo(c('laranja'), 'rgba(255,194,14,.55)', '50%', '30%')}
<img class="foto" src="{foto('h-close-amarela')}" style="left:50%;transform:translateX(-50%);top:60px;width:1100px;filter:contrast(1.1) drop-shadow(0 30px 50px rgba(60,20,0,.5))">
<div class="box" style="inset:0;border-radius:50%;box-shadow:inset 0 0 0 26px var(--pr)"></div>''')

# 14 · OUTDOOR 3:1 (ref: Obama 2008 -> slogan único + retrato + marca, horizonte reto)
P['outdoor'] = (2700, 900, f'''
{fundo(c('preto'), 'rgba(255,122,26,.45)', '80%', '40%')}
<div class="box" style="left:0;top:0;bottom:0;width:1560px;background:var(--la)"></div>
<img class="foto" src="{foto('d-bracos-cruzados-branca')}" style="right:80px;bottom:0;width:900px">
<div class="box" style="left:90px;top:110px;width:1400px"><div class="bc" style="font-size:240px;color:var(--pr)">Presença</div><div class="bc" style="font-size:240px;color:var(--br)">que resolve.</div></div>
<div class="hz" style="left:90px;width:1380px;top:650px;background:var(--pr)"></div>
<img class="box" src="{logo('branco')}" style="left:1640px;top:90px;width:300px">
<div class="lab box" style="left:90px;bottom:90px;color:var(--pr);font-size:30px">Vereador · São João Batista · MA</div>
{fim()}''')

# 15 · BANNER DE EVENTO (ref: Aston Martin + Macron -> painel de palco simétrico)
P['banner'] = (2000, 1000, f'''
{fundo(c('marinho2'), 'rgba(35,80,245,.5)', '50%', '40%')}
<div class="ci box" style="left:0;right:0;top:130px;text-align:center;font-size:150px;font-weight:900;letter-spacing:.06em">Prestação<br>de contas</div>
<div class="hz" style="left:700px;width:600px;top:500px"></div>
<div class="lab box" style="left:0;right:0;top:540px;text-align:center;font-size:36px;color:var(--ou)">Mandato do vereador · em parceria com a Prefeitura</div>
<img class="box" src="{logo('branco')}" style="left:50%;transform:translateX(-50%);bottom:70px;width:440px">
{fim()}''')

# 16 · CARTÃO DE VISITA (frente e verso) e 17 · SANTINHO DE MANDATO (sem número, sem voto)
P['cartao-frente'] = (1050, 600, f'<div class="box" style="inset:0;background:var(--pr)"></div><img class="box" src="{logo("branco")}" style="left:50%;top:50%;transform:translate(-50%,-55%);width:520px"><div class="hz" style="left:265px;width:520px;bottom:90px"></div>{fim()}')
P['cartao-verso'] = (1050, 600, f'''<div class="box" style="inset:0;background:var(--la)"></div>
<div class="box" style="left:70px;top:90px"><div class="ci" style="font-size:58px;color:var(--pr);font-weight:900">Leo Pinto</div><div class="lab" style="color:var(--br);margin-top:12px;font-size:22px">Vereador · São João Batista</div></div>
<div class="hz" style="left:70px;width:120px;top:250px;background:var(--pr)"></div>
<div class="box" style="left:70px;top:290px;font:600 24px/1.9 Mont;color:var(--pr)">Gabinete · Câmara Municipal<br>WhatsApp do gabinete<br>@ oficial do Instagram</div>
<img class="box" src="{A_SIM}" style="right:60px;bottom:60px;width:170px">''')
P['santinho'] = (700, 1000, f'''
{fundo(c('preto'), 'rgba(255,122,26,.45)', '50%', '35%')}
<img class="foto" src="{foto('g-maos-juntas-amarela')}" style="left:50%;transform:translateX(-50%);top:70px;width:760px">
<div class="box" style="left:0;right:0;top:560px;height:440px;background:linear-gradient(transparent,var(--pr) 30%)"></div>
<div class="box" style="left:0;right:0;top:640px;text-align:center"><div class="bc" style="font-size:96px">Presença que</div><div class="bc" style="font-size:96px;color:var(--la)">resolve.</div></div>
<img class="box" src="{logo('branco')}" style="left:50%;transform:translateX(-50%);bottom:40px;width:200px">{fim()}''')

# 18 · PAPEL TIMBRADO A4 e 19 · CRACHÁ
P['timbrado'] = (1240, 1754, f'''<div class="box" style="inset:0;background:#fff"></div>
<div class="box" style="left:0;top:0;width:1240px;height:16px;background:var(--la)"></div>
<img class="box" src="{logo('marinho')}" style="left:100px;top:90px;width:260px">
<div class="lab box" style="right:100px;top:150px;color:var(--ma);font-size:18px">Gabinete do Vereador</div>
<div class="box" style="left:100px;top:420px;width:1040px">{''.join(f'<div style="height:14px;background:#ececec;margin:0 0 26px;width:{w}%"></div>' for w in [92,100,96,88,100,94,70,0,100,98,90,100,60])}</div>
<div class="hz" style="left:100px;width:1040px;bottom:150px;background:var(--ma)"></div>
<div class="box" style="left:100px;bottom:90px;font:400 18px Mont;color:#555">Câmara Municipal de São João Batista · MA</div>''')
P['cracha'] = (600, 900, f'''<div class="box" style="inset:0;background:var(--pr)"></div>
<div class="box" style="left:0;top:0;right:0;height:300px;background:var(--la)"></div>
<img class="box" src="{logo('marinho')}" style="left:50%;transform:translateX(-50%);top:60px;width:300px">
<div class="box" style="left:0;right:0;top:420px;text-align:center"><div class="ci" style="font-size:52px;font-weight:900">Nome da<br>pessoa</div><div class="hz" style="position:relative;width:90px;margin:26px auto"></div><div class="lab" style="color:var(--ou)">Equipe do gabinete</div></div>
<div class="box" style="left:0;right:0;bottom:50px;text-align:center;font:400 16px Mont;color:#999">nome ilustrativo</div>{fim()}''')

# 20 · CAMISETA (estampa peito + costas)
P['camiseta'] = (1200, 1200, f'<div class="box" style="inset:0;background:transparent"></div><img class="box" src="{logo("branco")}" style="left:50%;top:44%;transform:translate(-50%,-50%);width:900px"><div class="hz" style="left:150px;width:900px;top:800px"></div><div class="lab box" style="left:0;right:0;top:830px;text-align:center;font-size:44px;color:var(--ou)">Presença que resolve</div>')


def html():
    out = [f'<!doctype html><meta charset="utf-8"><style>{CSS}.t{{position:relative;overflow:hidden;margin:20px}}</style>']
    for k, (w, h, inner) in P.items():
        out.append(f'<div class="t" id="{k}" style="width:{w}px;height:{h}px">{inner}</div>')
    return '\n'.join(out)

if __name__ == '__main__':
    open('templates.html', 'w').write(html())
    print(len(P), 'pecas')
