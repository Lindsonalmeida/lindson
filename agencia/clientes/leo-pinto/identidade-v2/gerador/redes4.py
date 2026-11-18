# Redes v4 · Leo Pinto (conta Pedro, 18/11/2026). Substitui a v3 ("nojo": criada do zero, sem as referências do Lindson).
# Cada peça COPIA a composição de um dos 3 modelos que o próprio Lindson captou:
#  A = instagram-v14-datas/referencias/modelo-natal-sou-pedro.png  (palavra repetida em pilha ATRÁS da pessoa, pessoa enorme na base, faixa do nome embaixo)
#  B = dados/agencia/referencias/carrossel-tweet-noticia/61.webp   (cartão de post com avatar + nome + texto, foto dentro do cartão, fundo neutro)
#  C = identidade-v2/referencias/19-luxury-menswear-behance.jpg    (editorial de moda masculina: foto escura de cinema, serifa romana, fios finos, muito respiro)
# Identidade v2 aprovada: cores do partido, logo, Cinzel + Barlow, fio amarelo-sol, "Presença que resolve.". Sem grafismo extra. Situação, sem promessa.
from base import CSS, logo
F = '../assets/fotos-v4'
def ft(n): return f'{F}/{n}.png'
X = CSS + """
.t{position:relative;overflow:hidden;background:var(--pr)}
.p{width:1080px;height:1350px}.s{width:1080px;height:1920px}
.set{position:absolute;inset:0;background:radial-gradient(ellipse 60% 45% at var(--gx,60%) 38%,rgba(255,122,26,.42),transparent 70%),radial-gradient(ellipse 90% 70% at 50% 100%,#0b2550,transparent 70%),linear-gradient(180deg,#021A3D,#08090C 80%)}
.bk{position:absolute;border-radius:50%;filter:blur(22px)}
.im{position:absolute;filter:brightness(.92) contrast(1.12) saturate(.88) drop-shadow(-12px -6px 28px rgba(255,122,26,.55)) drop-shadow(0 30px 60px rgba(0,0,0,.8))}
.fade{position:absolute;left:0;right:0;bottom:0;background:linear-gradient(180deg,transparent,rgba(8,9,12,.85) 55%,#08090C)}
.side{position:absolute;inset:0;background:linear-gradient(var(--sd,90deg),rgba(8,9,12,.7),transparent 55%)}
.out{color:transparent;-webkit-text-stroke:2px rgba(244,242,238,.55)}
.k{font-family:Barlow;font-weight:600;text-transform:uppercase;letter-spacing:.3em;font-size:22px;position:absolute}
.mt{font-family:Mont;position:absolute}
.lt{background:#F4F2EE;color:#05316E}
.card{position:absolute;background:#fff;border-radius:34px;box-shadow:0 40px 90px rgba(2,26,61,.28);overflow:hidden}
.av{width:96px;height:96px;border-radius:50%;background:#021A3D center 18%/180% no-repeat;border:3px solid var(--la)}
"""
def bok(seed):
    import random; r = random.Random(seed); o = ''
    for _ in range(9):
        s = r.randint(40, 170); o += f'<div class="bk" style="left:{r.randint(-60,1000)}px;top:{r.randint(0,700)}px;width:{s}px;height:{s}px;background:rgba({r.choice(["255,194,14","255,122,26","35,80,245"])},{r.uniform(.12,.3):.2f})"></div>'
    return o
def S(gx='60%', seed=1): return f'<div class="set" style="--gx:{gx}"></div>{bok(seed)}'
def fim(): return '<div class="vin"></div><div class="grao" style="opacity:.09"></div>'
def L(v, x, y, w, extra=''): return f'<img src="{logo(v)}" style="position:absolute;left:{x}px;top:{y}px;width:{w}px;{extra}">'
P = []
def add(i, cls, html): P.append(f'<div class="t {cls}" id="{i}">{html}</div>')

# ---------- POST 1 · ref A (pilha de palavras atrás, pessoa enorme, faixa do nome)
pil = ''.join(f'<div class="ci {"out" if k>1 else ""}" style="font-size:168px;font-weight:900;line-height:.88;color:{"var(--br)" if k<2 else ""}">PRESENÇA</div>' for k in range(5))
add('v4-post-1-presenca', 'p', f'''{S('50%',3)}<div class="box" style="left:-14px;top:150px;width:1110px;text-align:center">{pil}</div>
<img class="im" src="{ft('j-close-sorrindo')}" style="left:110px;top:430px;width:900px">
<div class="fade" style="height:430px"></div>
<div class="k" style="left:60px;top:66px">Vereador · São João Batista · MA</div>
<div class="hz" style="left:60px;right:60px;top:110px;height:2px"></div>
<div class="box" style="left:60px;right:60px;bottom:70px;display:flex;align-items:center;gap:28px">
<div style="background:var(--la);padding:16px 30px 12px;border-radius:999px"><span class="ci" style="font-size:58px;font-weight:900;color:#fff">Leo Pinto</span></div>
<div class="ci" style="font-size:36px;color:var(--ou)">que resolve.</div></div>{fim()}''')

# ---------- POST 2 · ref B (cartão de post, claro)
add('v4-post-2-cartao', 'p lt', f'''<div class="box" style="inset:0;background:radial-gradient(ellipse at 50% 0%,#fff,#E9E4DA)"></div>
<div class="k" style="left:70px;top:60px;color:#05316E">Leo de perto · Nº 02</div>{L('marinho',870,34,140)}
<div class="card" style="left:70px;top:190px;width:940px;height:1090px">
 <div style="display:flex;gap:22px;align-items:center;padding:44px 48px 0"><div class="av" style="background-image:url({ft('h-close-amarela')})"></div>
 <div><div class="mt" style="position:static;font-weight:800;font-size:34px;color:#08090C">Leo Pinto</div><div class="mt" style="position:static;font-size:24px;color:#6b7280">Vereador · São João Batista</div></div></div>
 <div class="mt" style="position:static;padding:30px 48px 0;font-weight:700;font-size:52px;line-height:1.26;color:#08090C">Mandato a gente mostra na rua: com <span style="background:var(--ou);padding:0 8px">data</span>, com o nome do povoado e com quem estava junto.</div>
 <div style="position:absolute;left:48px;right:48px;bottom:48px;height:560px;border-radius:24px;overflow:hidden">{S('70%',8)}<img class="im" src="{ft('h-close-amarela')}" style="left:80px;top:30px;width:820px"><div class="fade" style="height:160px"></div>
 <div class="ci" style="position:absolute;left:30px;bottom:24px;font-size:40px;color:var(--br)">Presença que <span style="color:var(--ou)">resolve.</span></div></div>
</div>''')

# ---------- POST 3 · ref C (editorial masculino)
add('v4-post-3-editorial', 'p', f'''{S('72%',5)}<img class="im" src="{ft('d-bracos-cruzados-branca')}" style="left:300px;top:250px;width:980px"><div class="side"></div><div class="fade" style="height:520px"></div>
<div class="box" style="left:60px;right:60px;top:56px;display:flex;justify-content:space-between" ><span class="k" style="position:static">O horizonte da Baixada</span><span class="k" style="position:static;color:var(--ou)">Nº 03 · Nov 2026</span></div>
<div class="hz" style="left:60px;right:60px;top:100px;height:1px;background:rgba(244,242,238,.4)"></div>
<div class="ci box" style="left:60px;top:150px;font-size:30px;line-height:1.5;color:rgba(244,242,238,.8);width:360px;font-weight:500">Engenheiro.<br>Vereador.<br>Filho da Baixada.</div>
<div class="ci box" style="left:60px;bottom:170px;font-size:118px;font-weight:900;line-height:.95">Presença<br><span style="color:var(--ou)">que resolve.</span></div>
<div class="hz" style="left:60px;width:180px;bottom:130px"></div>{L('branco',60,0,190,'top:auto;bottom:40px')}{fim()}''')

# ---------- CARROSSEL 5 telas (layouts diferentes)
add('v4-car-1', 'p', f'''{S('70%',11)}<img class="im" src="{ft('a-close-laranja')}" style="left:300px;top:640px;width:1000px"><div class="side"></div><div class="fade" style="height:300px"></div>
<div class="ci box out" style="left:40px;top:60px;font-size:300px;font-weight:900;line-height:.8">5</div>
<div class="k" style="left:60px;top:330px;color:var(--ou)">Carrossel · arraste</div>
<div class="ci box" style="left:60px;top:380px;width:640px;font-size:88px;font-weight:900;line-height:.98">Como o mandato chega ao seu <span style="color:var(--la)">povoado</span></div>
<div class="hz" style="left:60px;width:180px;bottom:120px"></div><div class="k" style="left:60px;bottom:70px">Leo Pinto · vereador</div>{fim()}''')
add('v4-car-2', 'p lt', f'''<div class="box" style="inset:0;background:#E9E4DA"></div>
<div class="card" style="left:70px;top:110px;width:940px;height:1130px;padding:56px">
<div style="display:flex;gap:22px;align-items:center"><div class="av" style="background-image:url({ft('a-close-laranja')})"></div><div class="mt" style="position:static;font-weight:800;font-size:32px;color:#08090C">Leo Pinto <span style="font-weight:400;color:#6b7280;font-size:24px">· 1/4</span></div></div>
<div class="ci" style="font-size:360px;font-weight:900;color:var(--la);margin-top:60px;line-height:.8">01</div>
<div class="ci" style="font-size:130px;font-weight:900;color:#05316E;margin-top:40px">Escutar</div>
<div class="mt" style="position:static;font-size:46px;line-height:1.38;color:#1f2937;margin-top:34px">Ir até o povoado, sentar com quem mora lá e anotar o pedido com nome, lugar e data.</div>
<div class="hz" style="position:static;width:160px;margin-top:46px"></div><div class="k" style="left:56px;bottom:50px;color:#05316E">Passo 1 de 4 · arraste</div></div>''')
add('v4-car-3', 'p', f'''<div class="box" style="inset:0;background:linear-gradient(160deg,#05316E,#021A3D 70%)"></div>
<div class="ci box out" style="right:-30px;top:20px;font-size:620px;font-weight:900;line-height:.8;-webkit-text-stroke:3px rgba(255,194,14,.5)">02</div>
<div class="k" style="left:70px;top:70px;color:var(--ou)">Passo 2 de 4</div>
<div class="ci box" style="left:70px;bottom:330px;width:900px;font-size:110px;font-weight:900;line-height:.95">Levar<br>junto com a<br><span style="color:var(--ou)">prefeitura</span></div>
<div class="hz" style="left:70px;right:70px;bottom:270px;height:1px"></div>
<div class="mt box" style="left:70px;bottom:120px;width:860px;font-size:36px;line-height:1.4;color:rgba(244,242,238,.85)">O pedido vira indicação na Câmara e conversa com a secretaria certa, em parceria.</div>{fim()}''')
add('v4-car-4', 'p lt', f'''<div class="box" style="inset:0;background:#F4F2EE"></div><div class="box" style="left:0;top:0;bottom:0;width:360px;background:var(--la)"></div>
<div class="ci box" style="left:40px;top:60px;font-size:250px;font-weight:900;color:#fff;line-height:.8">03</div>
<div class="ci box" style="left:420px;top:90px;font-size:78px;font-weight:900;line-height:.98;color:#05316E">Acompanhar<br>e mostrar</div>
<div class="box" style="left:420px;top:390px;right:70px">
{''.join(f'<div style="border-top:2px solid #05316E;padding:26px 0 26px;display:flex;gap:24px"><span class="lab" style="color:var(--la);font-size:26px;min-width:130px">{a}</span><span class="mt" style="position:static;font-size:34px;color:#1f2937;line-height:1.3">{b}</span></div>' for a,b in [('Pedido','registrado com data e povoado'),('Câmara','indicação apresentada'),('Entrega','feita junto com a prefeitura'),('Volta','o Leo volta e mostra aqui')])}</div>
<div class="k" style="left:420px;bottom:60px;color:#05316E">Presença que resolve.</div>''')
add('v4-car-5', 'p', f'''{S('35%',21)}<img class="im" src="{ft('i-maos-abertas-branca')}" style="left:-60px;top:250px;width:760px"><div class="side" style="--sd:270deg"></div><div class="fade" style="height:300px"></div>
<div class="k" style="right:60px;top:70px;text-align:right">Passo 4 · é com você</div>
<div class="ci box" style="right:60px;top:200px;width:520px;text-align:right;font-size:92px;font-weight:900;line-height:.98">Manda o nome do seu <span style="color:var(--ou)">povoado</span></div>
<div class="box" style="right:60px;top:640px;background:var(--la);border-radius:999px;padding:20px 40px"><span class="bc" style="font-size:48px">Fale no direct</span></div>
{L('branco',0,0,240,'left:auto;right:60px;top:auto;bottom:60px')}{fim()}''')

# ---------- STORY · ref C + adesivo de interface (ref B)
add('v4-story', 's', f'''{S('55%',31)}<img class="im" src="{ft('g-maos-juntas-amarela')}" style="left:-40px;top:520px;width:1160px"><div class="fade" style="height:760px"></div>
<div class="k" style="left:70px;top:200px">Leo de perto</div><div class="hz" style="left:70px;width:140px;top:250px"></div>
<div class="ci box" style="left:70px;top:290px;font-size:100px;font-weight:900;line-height:.95">Obrigado,<br><span style="color:var(--ou)">São João Batista.</span></div>
<div class="card" style="left:120px;right:120px;bottom:330px;padding:34px 40px;border-radius:28px"><div class="mt" style="position:static;font-size:26px;color:#6b7280;font-weight:600;letter-spacing:.1em">RESPONDA AQUI</div><div class="mt" style="position:static;font-size:42px;font-weight:800;color:#05316E;margin-top:10px">De qual povoado você é?</div></div>
{L('branco',0,0,220,'left:430px;top:auto;bottom:150px')}{fim()}''')

# ---------- 4 QUADROS (vinheta = selo da série) + capa de Reels do quadro 1
Q = [('q1','01','Leo no','Povoado','Segunda · 20h45','b-punho','A'),('q2','02','Pediu?','Tá feito.','Terça · 12h45','e-celular','B'),
     ('q3','03','Olho de','Engenheiro','Quinta · 20h45','c-maos-juntas-laranja','C'),('q4','04','Gente da','Baixada','Sexta · 12h45','f-punhos','B2')]
def vinheta(n, dia, cor='var(--ou)'):
    return f'<div class="box" style="display:flex;align-items:center;gap:18px"><span class="ci" style="font-size:44px;font-weight:900;color:{cor}">Nº {n}</span><span style="width:60px;height:2px;background:{cor}"></span><span class="lab" style="font-size:22px;white-space:nowrap">Quadro semanal · {dia}</span></div>'
for q,n,a,b,dia,f,m in Q:
    if m == 'A':
        pil = ''.join(f'<div class="ci {"out" if k else ""}" style="font-size:172px;font-weight:900;line-height:.9">POVOADO</div>' for k in range(4))
        body = f'''{S('50%',41)}<div class="box" style="left:0;top:250px;width:1080px;text-align:center">{pil}</div><img class="im" src="{ft(f)}" style="left:150px;top:440px;width:900px"><div class="fade" style="height:420px"></div>
<div style="position:absolute;left:60px;top:70px">{vinheta(n,dia)}</div><div class="ci box" style="left:60px;bottom:80px;font-size:96px;font-weight:900">{a} <span style="color:var(--la)">{b}</span></div>{fim()}'''
    elif m == 'C':
        body = f'''{S('70%',43)}<img class="im" src="{ft(f)}" style="left:380px;top:230px;width:820px"><div class="side"></div><div class="fade" style="height:420px"></div>
<div style="position:absolute;left:60px;top:70px">{vinheta(n,dia)}</div><div class="hz" style="left:60px;right:60px;top:140px;height:1px;background:rgba(244,242,238,.35)"></div>
<div class="ci box" style="left:60px;top:200px;font-size:40px;font-weight:500;line-height:1.5;color:rgba(244,242,238,.8)">Obra vista<br>de perto.</div>
<div class="ci box" style="left:60px;bottom:90px;font-size:130px;font-weight:900;line-height:.92">{a}<br><span style="color:var(--ou)">{b}</span></div>{fim()}'''
    else:
        bg = '#F4F2EE' if m=='B' else '#E9E4DA'; ac = 'var(--ro)' if m=='B' else 'var(--la)'
        body = f'''<div class="box" style="inset:0;background:{bg}"></div><div style="position:absolute;left:70px;top:60px;color:#05316E">{vinheta(n,dia,ac)}</div>
<div class="card" style="left:70px;top:150px;width:940px;height:1130px"><div style="position:absolute;inset:0 0 400px 0;overflow:hidden">{S('60%',44+len(q))}<img class="im" src="{ft(f)}" style="left:{20 if m=='B' else 110}px;top:40px;width:{900 if m=='B' else 760}px"><div class="fade" style="height:160px"></div></div>
<div style="position:absolute;left:52px;right:52px;bottom:52px"><div class="ci" style="font-size:112px;font-weight:900;color:#05316E;line-height:.92">{a}<br><span style="color:{ac}">{b}</span></div>
<div class="mt" style="position:static;margin-top:22px;font-size:34px;color:#4b5563">{'Pedido do povoado, entrega com data, junto com a prefeitura.' if m=='B' else 'Quem faz a Baixada acontecer, contado por quem vive aqui.'}</div></div></div>'''
    add(f'v4-quadro-{q}', 'p' + (' lt' if m in ('B','B2') else ''), body)
# capa de Reels do quadro 1 (9:16, área segura)
pil = ''.join(f'<div class="ci {"out" if k else ""}" style="font-size:172px;font-weight:900;line-height:.9">POVOADO</div>' for k in range(5))
add('v4-reels-q1', 's', f'''{S('50%',51)}<div class="box" style="left:0;top:380px;width:1080px;text-align:center">{pil}</div><img class="im" src="{ft('b-punho')}" style="left:60px;top:720px;width:1100px"><div class="fade" style="height:700px"></div>
<div style="position:absolute;left:70px;top:250px">{vinheta('01','Segunda · 20h45')}</div><div class="ci box" style="left:70px;bottom:330px;font-size:120px;font-weight:900;line-height:.92">Leo no<br><span style="color:var(--la)">Povoado</span></div>
<div class="hz" style="left:70px;width:160px;bottom:290px"></div>{fim()}''')
open('redes4.html', 'w').write(f'<html><head><meta charset="utf-8"><style>{X}</style></head><body style="display:flex;flex-wrap:wrap;gap:40px">{"".join(P)}</body></html>')
print(len(P))
