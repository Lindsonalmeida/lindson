import os,re,sys
B={'a':'32c68de29b69f82d8ee19fdc287d2453','b':'524f3380b05c62bf38854f41ce25b4b2','e':'ee0ad8dc0bf3d0291f8325387e02bd0d','d':'c3357d47e75df924a41d045838fd09cc','g':'98a31f57cd9166acb88bbaa9d8d46b25','j':'44ec90885085db7d7a9abefe83e5d8bb','i':'8359f0fa823839f1387b8c57a48e76c5',
'logo':'2a696bde95d71051362aafcf100235c7','marinho':'0be5df6e9319d2d93875d4d656f6eac7','branco':'4b6a8cc8b4c725b9817621a4e89ce996','linha':'417a1405ea25f8160a8bf837c8e94e0c','explosao':'a49a7581d61f7bb01abe3276c0821409','estrela':'d256608bf4ece24f46d4f5bc654c1821','grao':'0d6937214ecd9461e974df4e404afe1b','mapa':'437886afe927b44b60cb5e054bdfe4ff'}
def u(k): return '/_blob/'+B[k]
FONTS='<link href="https://fonts.googleapis.com/css2?family=Anton&amp;family=Kaushan+Script&amp;family=Montserrat:ital,wght@0,400;0,500;0,600;0,700;0,800;0,900;1,800;1,900&amp;display=swap" rel="stylesheet">'
def page(title,body,extra_css=''):
  return f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
{FONTS}
<style>
body{{margin:0}}
.grao{{background-image:url({u('grao')});background-size:420px;mix-blend-mode:multiply;opacity:.5}}
{extra_css}
</style>
</helmet>
<div style="width: 1080px; height: 1350px; position: relative; overflow: hidden; font-family: Montserrat, sans-serif; color: #FFFFFF; {body[0]}">
  <div style="position: absolute; left: -260px; top: 520px; width: 760px; height: 1200px; border-radius: 380px; background: rgba(0,0,0,0.10); transform: rotate(-28deg)"></div>
  <div style="position: absolute; right: -300px; top: -360px; width: 760px; height: 1200px; border-radius: 380px; background: rgba(255,255,255,0.08); transform: rotate(-28deg)"></div>
  <img src="{u('mapa')}" alt="" aria-hidden="true" style="position: absolute; left: 140px; top: 260px; width: 860px; opacity: 0.06">
{body[1]}
  <div class="grao" style="position: absolute; inset: 0; pointer-events: none"></div>
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":1080,"height":1350}}}}'>
class Component extends DCLogic {{
  renderVals() {{ return {{}}; }}
}}
</script>
</body>
</html>
'''
AT='<div style="position: absolute; left: 0; right: 0; top: 48px; text-align: center; font-weight: 700; font-size: 22px; letter-spacing: 0.34em; color: {c}">@_LEONARDOPINTO</div>'
posts={}
# 1 TAMO JUNTO
posts['Post1TamoJunto']=('Post · Tamo junto',('background: radial-gradient(circle at 50% 35%, #3A66FF 0%, #2350F5 45%, #05316E 100%)',f'''
  <div style="position: absolute; left: -60px; top: -170px; font-family: Anton, sans-serif; font-size: 1500px; line-height: 1; color: #1A44D8; opacity: 0.9">#</div>
  <img src="{u('mapa')}" alt="" aria-hidden="true" style="position: absolute; left: 90px; top: 220px; width: 900px; opacity: 0.08">
  <img src="{u('logo')}" alt="Logo Leo Pinto" style="position: absolute; left: 420px; top: 96px; width: 240px">
  <img src="{u('g')}" alt="Leo Pinto com as mãos juntas" style="position: absolute; left: 50%; transform: translateX(-50%); bottom: 240px; height: 760px">
  <div style="position: absolute; left: 0; right: 0; bottom: 0; height: 520px; background: linear-gradient(180deg, rgba(5,49,110,0) 0%, #05316E 55%)"></div>
  <div style="position: absolute; left: 0; right: 0; bottom: 210px; text-align: center; font-family: Anton, sans-serif; font-size: 200px; line-height: 0.9; text-transform: uppercase"><span style="color: #FFC20E">#</span>TAMO JUNTO</div>
  <div style="position: absolute; left: 0; right: 0; bottom: 140px; display: flex; justify-content: center"><span style="background: #FF7A1A; padding: 8px 26px; font-weight: 900; font-size: 44px; letter-spacing: 0.04em; text-transform: uppercase; color: #FFFFFF">com o Leo</span></div>
  {AT.format(c='#FFFFFF').replace('top: 48px','bottom: 60px; top: auto')}
'''))
# 2 #tôcom
posts['Post2TocomLeo']=('Post · #tôcom Leo',('background: radial-gradient(circle at 70% 60%, #3A66FF 0%, #2350F5 50%, #05316E 100%)',f'''
  <div style="position: absolute; right: -200px; top: 360px; width: 700px; height: 1100px; border-radius: 350px; background: #1A44D8; opacity: 0.8; transform: rotate(20deg)"></div>
  <img src="{u('b')}" alt="Leo Pinto com o punho erguido" style="position: absolute; right: 0; bottom: 0; height: 860px">
  <div style="position: absolute; left: 0; right: 0; bottom: 0; height: 300px; background: linear-gradient(180deg, rgba(5,49,110,0), #05316E 75%)"></div>
  <div style="position: absolute; left: 80px; top: 120px; display: flex; align-items: center; gap: 18px">
    <span style="font-family: Anton, sans-serif; font-size: 230px; line-height: 0.8; color: #FFC20E">#</span>
    <div style="display: flex; flex-direction: column"><span style="font-weight: 400; font-size: 84px; line-height: 1">tôcom</span><span style="font-weight: 900; font-size: 92px; line-height: 0.95; letter-spacing: -0.01em">LEO PINTO</span></div>
  </div>
  <div style="position: absolute; left: 80px; top: 420px; width: 520px; font-size: 30px; font-weight: 500; line-height: 1.45; color: rgba(255,255,255,0.88)">Vereador de São João Batista.<br>Perto de você, todo mandato.</div>
  <div style="position: absolute; left: 70px; top: 560px; transform: rotate(-6deg); display: flex; flex-direction: column; align-items: flex-start">
    <span style="font-family: 'Kaushan Script', cursive; font-size: 54px; color: #FFFFFF; margin-left: 20px">voz do povo</span>
    <span style="background: #FFC20E; padding: 8px 24px 2px; font-family: Anton, sans-serif; font-size: 80px; line-height: 1; color: #05316E">SEMPRE PERTO</span>
  </div>
   <img src="{u('branco')}" alt="Logo Leo Pinto" style="position: absolute; left: 80px; bottom: 56px; width: 200px">
  <div style="position: absolute; right: 60px; bottom: 70px; font-weight: 700; font-size: 20px; letter-spacing: 0.3em">@_LEONARDOPINTO</div>
'''))
# 3 Presente nos povoados
posts['Post3Presente']=('Post · Presente nos povoados',('background: radial-gradient(circle at 30% 40%, #FFC20E 0%, #FF9A2A 40%, #FF7A1A 100%)',f'''
  <div style="position: absolute; left: -200px; top: -100px; width: 640px; height: 1100px; border-radius: 320px; background: #FFB21E; opacity: 0.7; transform: rotate(18deg)"></div>
  <img src="{u('mapa')}" alt="" aria-hidden="true" style="position: absolute; left: 380px; top: 120px; width: 700px; opacity: 0.18">
  <img src="{u('d')}" alt="Leo Pinto de braços cruzados" style="position: absolute; left: -220px; bottom: 0; height: 860px">
  <div style="position: absolute; left: 0; right: 0; bottom: 0; height: 200px; background: linear-gradient(180deg, rgba(5,49,110,0), #05316E 80%)"></div>
  <div style="position: absolute; right: 64px; top: 70px"><span style="background: #05316E; padding: 10px 22px; font-weight: 800; font-size: 24px; color: #FFC20E">#TôComLéoPinto</span></div>
  <div style="position: absolute; right: 64px; top: 170px; display: flex; flex-direction: column; align-items: flex-end; font-family: Anton, sans-serif; line-height: 0.88; text-transform: uppercase">
    <span style="font-size: 128px; color: #FFFFFF">Presente</span>
    <span style="font-size: 128px; color: #FFFFFF">nos</span>
    <span style="font-size: 128px; background: #05316E; color: #FFC20E; padding: 8px 18px 0">povoados!</span>
  </div>
  <div style="position: absolute; right: 64px; top: 640px; width: 420px; background: #FFFFFF; border-radius: 22px; padding: 30px 34px; box-sizing: border-box; color: #05316E; font-size: 26px; font-weight: 600; line-height: 1.4; box-shadow: 0 30px 50px -20px rgba(5,49,110,0.5)">Cada canto de São João Batista merece atenção. Perto pra ouvir, junto pra fazer.</div>
  <div style="position: absolute; right: 64px; top: 860px; background: #05316E; border-radius: 40px; padding: 18px 34px; font-weight: 800; font-size: 26px; color: #FFC20E">Confira a agenda →</div>
  <img src="{u('branco')}" alt="Logo Leo Pinto" style="position: absolute; right: 64px; bottom: 44px; width: 190px">
  <div style="position: absolute; left: 60px; bottom: 64px; font-weight: 700; font-size: 20px; letter-spacing: 0.3em">@_LEONARDOPINTO</div>
'''))
# 4 juntos somos + fortes
posts['Post4Juntos']=('Post · Juntos somos mais fortes',('background: radial-gradient(circle at 75% 45%, #3A66FF 0%, #2350F5 45%, #05316E 100%)',f'''
  <img src="{u('estrela')}" alt="" aria-hidden="true" style="position: absolute; right: -160px; top: 120px; width: 760px; opacity: 0.16">
  <img src="{u('i')}" alt="Leo Pinto de mãos abertas" style="position: absolute; right: -40px; bottom: 0; height: 940px">
  <div style="position: absolute; left: 0; right: 0; bottom: 0; height: 420px; background: linear-gradient(180deg, rgba(5,49,110,0), #05316E 60%)"></div>
  {AT.format(c='#FFFFFF')}
  <div style="position: absolute; left: 64px; top: 190px; font-family: 'Kaushan Script', cursive; font-size: 190px; line-height: 1; color: #FFC20E; transform: rotate(-8deg)">juntos</div>
  <div style="position: absolute; left: 70px; top: 420px; font-family: Anton, sans-serif; font-size: 150px; line-height: 0.9; text-transform: uppercase">somos<br><span style="color: #FF7A1A">+</span> fortes</div>
  <img src="{u('explosao')}" alt="" aria-hidden="true" style="position: absolute; left: 600px; top: 250px; width: 130px">
  <div style="position: absolute; left: 70px; bottom: 210px; width: 460px; font-size: 28px; font-weight: 600; line-height: 1.4">Mandato e prefeitura lado a lado pelo povo de São João Batista.</div>
  <img src="{u('branco')}" alt="Logo Leo Pinto" style="position: absolute; left: 70px; bottom: 50px; width: 190px">
'''))
# 5 Mandato que entrega - lista
items=''.join(f'''
    <div style="display: flex; gap: 26px; align-items: flex-start; padding: 26px 0; border-top: 2px solid rgba(255,255,255,0.18)">
      <span style="font-family: Anton, sans-serif; font-size: 96px; line-height: 0.85; color: #FFC20E">0{i}</span>
      <div style="display: flex; flex-direction: column; gap: 8px"><span style="font-weight: 900; font-size: 36px; line-height: 1.05; text-transform: uppercase">[Entrega {i}]</span><span style="font-size: 22px; line-height: 1.4; color: rgba(255,255,255,0.78)">[Povoado · o que mudou para as pessoas]</span></div>
    </div>''' for i in range(1,5))
posts['Post5Mandato']=('Post · Mandato que entrega',('background: radial-gradient(circle at 80% 20%, #3A66FF 0%, #2350F5 40%, #05316E 100%)',f'''
  <div style="position: absolute; left: -380px; top: 640px; transform: rotate(-90deg); font-family: Anton, sans-serif; font-size: 300px; line-height: 1; color: #FFFFFF; opacity: 0.1; white-space: nowrap">MANDATO</div>
  <img src="{u('mapa')}" alt="" aria-hidden="true" style="position: absolute; right: -120px; top: 120px; width: 700px; opacity: 0.08">
  {AT.format(c='#FFFFFF').replace('text-align: center','text-align: right; padding-right: 80px')}
  <div style="position: absolute; left: 260px; right: 80px; top: 150px">
    <div style="font-weight: 700; font-size: 24px; letter-spacing: 0.3em; text-transform: uppercase; color: #FFC20E">Prestação de contas</div>
    <div style="font-family: Anton, sans-serif; font-size: 120px; line-height: 0.92; text-transform: uppercase; margin: 14px 0 30px">Mandato<br><span style="color: #FF7A1A">que entrega</span></div>
    {items}
  </div>
  <div style="position: absolute; left: 260px; bottom: 64px; font-size: 22px; font-weight: 600; color: rgba(255,255,255,0.8)">Em parceria com a Prefeitura</div>
  <img src="{u('branco')}" alt="Logo Leo Pinto" style="position: absolute; right: 80px; bottom: 44px; width: 180px">
'''))
# 6 frase com foto nas letras
css6=f".foto-txt{{background:url({u('g')}) center 30%/100% auto no-repeat,linear-gradient(#2350F5,#2350F5);-webkit-background-clip:text;background-clip:text;color:transparent}}"
posts['Post6Frase']=('Post · Frase',('background: radial-gradient(circle at 50% 40%, #FFFFFF 0%, #EAF0FF 50%, #C9D8FF 100%)',f'''
  <img src="{u('mapa')}" alt="" aria-hidden="true" style="position: absolute; left: 90px; top: 300px; width: 900px; opacity: 0.25; filter: brightness(0.6) sepia(1) hue-rotate(180deg) saturate(4)">
  {AT.format(c='#2350F5')}
  <div style="position: absolute; left: 70px; right: 70px; top: 330px; font-family: Anton, sans-serif; text-transform: uppercase; line-height: 0.9; color: #2350F5">
    <div style="font-size: 150px; white-space: nowrap">“Fazer política</div>
    <div class="foto-txt" style="font-size: 236px; line-height: 0.95; white-space: nowrap">é cuidar</div>
    <div style="font-size: 150px; margin-top: 56px; white-space: nowrap"><span style="background: #FF7A1A; color: #FFFFFF; padding: 0 20px">de gente.”</span></div>
  </div>
  <img src="{u('marinho')}" alt="Logo Leo Pinto" style="position: absolute; left: 70px; bottom: 44px; width: 180px">
''',),)
CSS={'Post6Frase':css6}
A=os.path.abspath('lindson/agencia/clientes/leo-pinto/identidade-v2/assets');F=os.path.abspath('fotos-v5');FA=os.path.abspath('fotos-limpas');K=os.path.abspath('kit')
loc={'a':FA+'/a-close-laranja.png','e':F+'/e-celular.png','b':F+'/b-punho.png','d':F+'/d-bracos-cruzados-branca.png','g':F+'/g-maos-juntas-amarela.png','j':F+'/j-close-sorrindo.png','i':F+'/i-maos-abertas-branca.png','logo':A+'/logo.png','marinho':A+'/logo-marinho.png','branco':A+'/logo-mono-branco.png','linha':K+'/mapa-linha.svg','explosao':K+'/explosao-mapa.svg','estrela':K+'/estrela-ciano.svg','grao':K+'/grao.png','mapa':K+'/mapa-camada.svg'}
inv={'/_blob/'+v:'file://'+loc[k] for k,v in B.items()}
for name,(title,body) in posts.items():
  s=page(title,body,CSS.get(name,''))
  open(f'leo-id/project/{name}.dc.html','w').write(s)
  r=s.replace('<script src="./support.js"></script>','')
  for a,b in inv.items(): r=r.replace(a,b)
  open(f'render/{name}.html','w').write(r)
print(list(posts))
