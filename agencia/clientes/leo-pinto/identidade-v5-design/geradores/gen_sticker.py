import os,json
B={'j':'44ec90885085db7d7a9abefe83e5d8bb','branco':'4b6a8cc8b4c725b9817621a4e89ce996','explosao':'a49a7581d61f7bb01abe3276c0821409','grao':'0d6937214ecd9461e974df4e404afe1b'}
fx=json.load(open('facex.json'))['j']
def u(k): return '/_blob/'+B[k]
inner=f'''<div style="position: relative; width: 1080px; height: 1080px; font-family: Montserrat, sans-serif">
  <div style="position: absolute; inset: 0; filter: drop-shadow(0 0 0 #FFFFFF) drop-shadow(10px 0 0 #FFFFFF) drop-shadow(-10px 0 0 #FFFFFF) drop-shadow(0 10px 0 #FFFFFF) drop-shadow(0 -10px 0 #FFFFFF) drop-shadow(7px 7px 0 #FFFFFF) drop-shadow(-7px -7px 0 #FFFFFF) drop-shadow(7px -7px 0 #FFFFFF) drop-shadow(-7px 7px 0 #FFFFFF) drop-shadow(0 18px 24px rgba(0,0,0,0.35))">
    <div style="position: absolute; left: 330px; top: 60px; width: 420px; height: 420px; border-radius: 50%; background: radial-gradient(circle at 50% 30%, #FFC20E 0%, #FF7A1A 60%, #E8650C 100%)"></div>
    <div style="position: absolute; left: 330px; top: -60px; width: 420px; height: 540px; overflow: hidden; border-radius: 0 0 210px 210px">
      <img src="{u('j')}" alt="Leo Pinto" style="position: absolute; left: {210-fx*400:.0f}px; bottom: -20px; width: 400px">
    </div>
    <img src="{u('explosao')}" alt="" aria-hidden="true" style="position: absolute; left: 700px; top: 70px; width: 150px; transform: rotate(14deg)">
    <div style="position: absolute; left: 90px; top: 470px; width: 900px; transform: rotate(-5deg); display: flex; flex-direction: column; align-items: center">
      <div style="background: #2350F5; color: #FFFFFF; padding: 14px 40px 8px; border-radius: 18px; font-family: Anton, sans-serif; font-size: 118px; line-height: 1; white-space: nowrap">FELIZ ANIVERSÁRIO</div>
      <div style="margin-top: -6px; background: #FFC20E; color: #05316E; padding: 10px 44px; border-radius: 60px; font-weight: 900; font-size: 74px; letter-spacing: 0.01em">VALMISSANDRO!</div>
      <div style="margin-top: 14px; background: #05316E; color: #FFFFFF; padding: 14px 34px; border-radius: 16px; display: flex; align-items: center; gap: 22px">
        <span style="font-family: 'Kaushan Script', cursive; font-size: 36px; color: #FFC20E">Prestigiando o aniversário do meu amigo</span>
        <span style="width: 2px; height: 64px; background: rgba(255,255,255,0.4)"></span>
        <img src="{u('branco')}" alt="Logo Leo Pinto" style="width: 110px">
      </div>
    </div>
  </div>
</div>'''
FONTS='<link href="https://fonts.googleapis.com/css2?family=Anton&amp;family=Kaushan+Script&amp;family=Montserrat:wght@600;800;900&amp;display=swap" rel="stylesheet">'
dc=f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Figurinha aniversário · Valmissandro</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
{FONTS}
<style>body{{margin:0}}</style>
</helmet>
<div style="width: 1080px; height: 1080px; background-image: linear-gradient(45deg, #E9ECF2 25%, transparent 25%), linear-gradient(-45deg, #E9ECF2 25%, transparent 25%), linear-gradient(45deg, transparent 75%, #E9ECF2 75%), linear-gradient(-45deg, transparent 75%, #E9ECF2 75%); background-size: 40px 40px; background-position: 0 0, 0 20px, 20px -20px, -20px 0; background-color: #F7F8FB">
{inner}
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":1080,"height":1080}}}}'>
class Component extends DCLogic {{
  renderVals() {{ return {{}}; }}
}}
</script>
</body>
</html>
'''
open('leo-id/project/FigurinhaValmissandro.dc.html','w').write(dc)
A=os.path.abspath('lindson/agencia/clientes/leo-pinto/identidade-v2/assets');K=os.path.abspath('kit')
loc={'j':os.path.abspath('fotos-v5/j-close-sorrindo.png'),'branco':A+'/logo-mono-branco.png','explosao':K+'/explosao-mapa.svg','grao':K+'/grao.png'}
r=inner
for k,v in loc.items(): r=r.replace(u(k),'file://'+v)
open('render/figurinha.html','w').write(f'<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>html,body{{margin:0;background:transparent}}</style></head><body>{r}</body></html>')
