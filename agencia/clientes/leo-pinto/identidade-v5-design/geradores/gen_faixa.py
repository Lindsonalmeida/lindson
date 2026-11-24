import os,json
B={'j':'44ec90885085db7d7a9abefe83e5d8bb','branco':'4b6a8cc8b4c725b9817621a4e89ce996','explosao':'a49a7581d61f7bb01abe3276c0821409'}
fx=json.load(open('facex.json'))['j']
def u(k): return '/_blob/'+B[k]
SH='drop-shadow(10px 0 0 #FFFFFF) drop-shadow(-10px 0 0 #FFFFFF) drop-shadow(0 10px 0 #FFFFFF) drop-shadow(0 -10px 0 #FFFFFF) drop-shadow(7px 7px 0 #FFFFFF) drop-shadow(-7px -7px 0 #FFFFFF) drop-shadow(7px -7px 0 #FFFFFF) drop-shadow(-7px 7px 0 #FFFFFF)'
inner=f'''<div style="position: relative; width: 1080px; height: 420px; font-family: Montserrat, sans-serif">
  <div style="position: absolute; inset: 0; filter: {SH}">
    <div style="position: absolute; left: 270px; top: 70px; width: 770px; transform: rotate(-3deg); display: flex; flex-direction: column; align-items: flex-start">
      <div style="background: #2350F5; color: #FFFFFF; padding: 10px 30px 4px 120px; border-radius: 16px; font-family: Anton, sans-serif; font-size: 84px; line-height: 1; white-space: nowrap">FELIZ ANIVERSÁRIO</div>
      <div style="margin: -4px 0 0 110px; background: #FFC20E; color: #05316E; padding: 8px 34px; border-radius: 50px; font-weight: 900; font-size: 54px">VALMISSANDRO!</div>
      <div style="margin: 10px 0 0 110px; background: #05316E; padding: 10px 24px; border-radius: 14px; display: flex; align-items: center; gap: 16px">
        <span style="font-family: 'Kaushan Script', cursive; font-size: 28px; color: #FFC20E; white-space: nowrap">Prestigiando o aniversário do meu amigo</span>
        <span style="width: 2px; height: 46px; background: rgba(255,255,255,0.4)"></span>
        <img src="{u('branco')}" alt="Logo Leo Pinto" style="width: 80px">
      </div>
    </div>
    <div style="position: absolute; left: 40px; top: 80px; width: 300px; height: 300px; border-radius: 50%; background: radial-gradient(circle at 50% 30%, #FFC20E 0%, #FF7A1A 60%, #E8650C 100%)"></div>
    <div style="position: absolute; left: 40px; top: 0; width: 300px; height: 380px; overflow: hidden; border-radius: 0 0 150px 150px">
      <img src="{u('j')}" alt="Leo Pinto" style="position: absolute; left: {150-fx*290:.0f}px; bottom: -14px; width: 290px">
    </div>
    <img src="{u('explosao')}" alt="" aria-hidden="true" style="position: absolute; left: 270px; top: 20px; width: 100px; transform: rotate(14deg)">
  </div>
</div>'''
FONTS='<link href="https://fonts.googleapis.com/css2?family=Anton&amp;family=Kaushan+Script&amp;family=Montserrat:wght@600;800;900&amp;display=swap" rel="stylesheet">'
dc=f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Faixa story aniversário · Valmissandro</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
{FONTS}
<style>body{{margin:0}}</style>
</helmet>
<div style="width: 1080px; height: 420px; background-image: linear-gradient(45deg, #E9ECF2 25%, transparent 25%), linear-gradient(-45deg, #E9ECF2 25%, transparent 25%), linear-gradient(45deg, transparent 75%, #E9ECF2 75%), linear-gradient(-45deg, transparent 75%, #E9ECF2 75%); background-size: 40px 40px; background-position: 0 0, 0 20px, 20px -20px, -20px 0; background-color: #F7F8FB">
{inner}
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":1080,"height":420}}}}'>
class Component extends DCLogic {{
  renderVals() {{ return {{}}; }}
}}
</script>
</body>
</html>
'''
open('leo-id/project/FaixaValmissandro.dc.html','w').write(dc)
A=os.path.abspath('lindson/agencia/clientes/leo-pinto/identidade-v2/assets');K=os.path.abspath('kit')
loc={'j':os.path.abspath('fotos-v5/j-close-sorrindo.png'),'branco':A+'/logo-mono-branco.png','explosao':K+'/explosao-mapa.svg'}
r=inner
for k,v in loc.items(): r=r.replace(u(k),'file://'+v)
open('render/faixa.html','w').write(f'<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>html,body{{margin:0;background:transparent}}</style></head><body>{r}</body></html>')
