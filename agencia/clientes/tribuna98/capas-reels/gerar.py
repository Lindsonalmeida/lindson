# Capas de Reels do Tribuna 98 (1080x1920) · conta Leandro, 16/11/2026
# Uso: edite capas.json (n, tag, l1, l2 = manchete em 2 linhas, foto = recorte em recortes/) e rode:
#   python3 gerar.py && node render.js && python3 previa.py
# Composicoes alternam sozinhas A -> B -> C pela ordem (o grid nunca repete lado a lado):
#   A "Telejornal" copia a capa vertical do Politico/Axios: fundo azul royal com luz, apresentador grande, manchete gorda embaixo com 2a linha em tarja amarela.
#   B "Palavra atras" copia as capas do Brut (FR) e do Metropoles (BR): fundo amarelo, palavra gigante azul passando por tras do Thiago.
#   C "Dossie" copia o The Guardian/BBC News (UK) e Le Monde: azul quase preto, foto com faixa lateral, etiqueta da editoria e lower third.
# Area segura: tudo o que importa fica entre y=420 e y=1500 (recorte 1:1 do grid) e o rosto entre y=480 e y=1000.
import json, os
from PIL import Image
D = os.path.dirname(os.path.abspath(__file__))
C = json.load(open(os.path.join(D, 'capas.json'), encoding='utf-8'))
# ajuste fino por foto: largura do recorte na tela (px) e deslocamento horizontal
AJ = json.load(open(os.path.join(D, 'ajustes.json'))) if os.path.exists(os.path.join(D, 'ajustes.json')) else {}

def foto(c, topo, cx):
    f = c['foto']; im = Image.open(os.path.join(D, 'recortes', f + '.png'))
    w0, h0 = im.size; aj = AJ.get(f, {})
    w = aj.get('w', 1150); h = h0 * w / w0
    x = cx - w / 2 + aj.get('dx', 0)
    top = topo + aj.get('dy', 0)
    # a base do recorte sempre sai da tela (nunca aparece borda reta)
    if top + h < 1960: top = 1960 - h
    return f'<img class="p" src="recortes/{f}.png" style="left:{x:.0f}px;top:{top:.0f}px;width:{w:.0f}px">'

LOGO = '<img class="logo" src="../marca/logo.png">'
def A(c):
    return f'''<div class="c A"><div class="luz"></div><div class="vaz">TRIBUNA</div>{foto(c,470,600)}
<div class="sombra"></div><div class="top">{LOGO}<span class="tag">{c['tag']}</span></div>
<div class="h"><div class="l1">{c['l1']}</div><div class="l2"><span>{c['l2']}</span></div></div>
<div class="rod">THIAGO AZEVEDO · @TRIBUNA98_</div><div class="grao"></div></div>'''
def B(c):
    return f'''<div class="c B"><div class="gig" style="font-size:{min(330,int(2300/len(c['tag'])))}px">{c['tag']}</div>{foto(c,520,540)}
<div class="sombraB"></div><div class="top">{LOGO.replace('class="logo"','class="logo azul"')}</div>
<div class="h"><div class="l1">{c['l1']}</div><div class="l2"><span>{c['l2']}</span></div></div>
<div class="rod">THIAGO AZEVEDO · TRIBUNA 98</div><div class="grao"></div></div>'''
def Cc(c):
    return f'''<div class="c C"><div class="faixa"></div><div class="num">{c['n']}</div>{foto(c,480,650)}
<div class="sombra"></div><div class="top">{LOGO}</div>
<div class="h"><span class="tag2">● {c['tag']}</span><div class="l1">{c['l1']}</div><div class="l2">{c['l2']}</div>
<div class="lt"><b>THIAGO AZEVEDO</b> · informação, política e bastidores</div></div><div class="grao"></div></div>'''
L = [A, B, Cc]
CSS = open(os.path.join(D, 'estilo.css'), encoding='utf-8').read()
html = '<!doctype html><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Anton&family=Manrope:wght@500;800&display=swap" rel="stylesheet"><style>' + CSS + '</style>'
nomes = []
for i, c in enumerate(C):
    nome = f"capa-{c['n']}"; nomes.append(nome)
    html += f'<div id="{nome}">{L[i % 3](c)}</div>'
open(os.path.join(D, 'pecas.html'), 'w', encoding='utf-8').write(html)
json.dump(nomes, open(os.path.join(D, 'nomes.json'), 'w'))
print(len(nomes), 'capas montadas')
