"""Grade de abertura do Instagram: 3 posts 1080x1440 que formam uma imagem só (3240x1440). Conta Pedro, 18/11/2026."""
import os, json
from base import *
R = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')); T = f'{R}/_tmp'; os.makedirs(T, exist_ok=True)
O = f'{R}/instagram/abertura'; os.makedirs(O, exist_ok=True)
W, H = 3240, 1440
corpo = f'''<div class="esc" style="width:{W}px;height:{H}px;position:relative;overflow:hidden;background:radial-gradient(60% 90% at 72% 40%,#22242a,#0B0C0E 70%)">
<div style="position:absolute;left:1180px;top:-330px;width:2100px;height:2100px;filter:drop-shadow(0 40px 80px rgba(0,0,0,.6))">{simb(2, '#B8955A', '#1c1e23')}</div>
<div style="position:absolute;left:1180px;top:-330px;width:2100px;height:2100px;background:radial-gradient(30% 30% at 75% 35%,rgba(184,149,90,.35),transparent 70%);mix-blend-mode:screen"></div>
<div style="position:absolute;left:2650px;top:0;width:500px;height:{H}px;background:linear-gradient(200deg,rgba(255,226,170,.22),transparent 55%);transform:skewX(-18deg)"></div>
<div style="position:absolute;left:110px;top:120px"><img src="{LOGO_N}" style="height:74px"></div>
<div style="position:absolute;left:110px;top:430px;width:940px">
<p class="mono" style="color:#B8955A;font-size:28px">Grupo de tecnologia · São Luís, MA</p>
<h1 style="font-size:196px;line-height:.92;margin-top:30px">Estrutura<br>para <em style="color:#B8955A">o que<br>vem.</em></h1></div>
<div style="position:absolute;left:110px;bottom:120px;display:flex;gap:56px" class="mono">
<span style="color:#2E4BFF;font-size:26px">■ Labs</span><span style="color:#E8461E;font-size:26px">■ Barzakh</span><span style="color:#F0A202;font-size:26px">■ Media</span><span style="color:#0E8C66;font-size:26px">■ Ventures</span></div>
<div style="position:absolute;left:0;right:0;bottom:0">{FAIXA.replace('6px','12px')}</div><div class="grao"></div></div>'''
p = f'{T}/abertura.html'; open(p, 'w').write(doc(W, H, corpo))
json.dump([dict(html=p, png=f'{T}/abertura.png', w=W, h=H)], open(f'{T}/l-ab.json', 'w'))
