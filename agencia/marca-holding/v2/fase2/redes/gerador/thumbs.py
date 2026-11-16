"""3 thumbnails YouTube 1280x720 (conta Pedro, 16/11/2026): foto P&B + título gigante + K aceso."""
import json, os
from base import *
R = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')); T = f'{R}/_tmp'
YT = json.load(open(f'{R}/youtube/youtube.json')); FT = ['slz-juninos', 'luz-pedra', 'servidores-3']
lista = []
for i, l in enumerate(YT['longos']):
    d = l['divisao']; c = COR[d]
    corpo = f'''<div class="esc" style="width:1280px;height:720px;position:relative;overflow:hidden">
<div style="position:absolute;inset:0;left:420px;background:url(file://{R}/fotos/{FT[i]}.jpg) center/cover;filter:grayscale(1) contrast(1.25) brightness(.75)"></div>
<div style="position:absolute;inset:0;left:420px;background:{c};mix-blend-mode:soft-light;opacity:.7"></div>
<div style="position:absolute;inset:0;background:linear-gradient(90deg,#0B0C0E 34%,rgba(11,12,14,.75) 55%,rgba(11,12,14,0) 85%)"></div>
<div style="position:absolute;right:-90px;bottom:-110px;width:500px">{simb(IDX[d], c, 'rgba(11,12,14,.6)')}</div>
<div style="position:absolute;left:56px;top:52px"><img src="{LOGO_N}" style="height:40px"></div>
<div style="position:absolute;left:52px;bottom:70px;width:760px"><p class="mono" style="color:{c};font-size:22px">{NOME[d]}</p>
<h1 style="font-size:132px;line-height:.9;margin-top:16px;text-shadow:0 6px 30px rgba(0,0,0,.6)">{it(l['titulo_thumb']).replace('<em>', f'<em style="color:{c if d!="ventures" else "#B8955A"}">')}</h1></div>
<div style="position:absolute;left:0;right:0;bottom:0">{FAIXA}</div><div class="grao"></div></div>'''
    p = f'{T}/thumb{i+1}.html'; open(p, 'w').write(doc(1280, 720, corpo)); lista.append(dict(html=p, png=f'{R}/youtube/thumb-{i+1:02d}.jpg', w=1280, h=720))
json.dump(lista, open(f'{T}/lista-th.json', 'w'))
