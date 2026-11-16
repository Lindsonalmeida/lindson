"""v5 advogado (conta Zuleide, 16/11/2026) · direção do Lindson: "clean e rico, sem nada de pobre" = luxo editorial.
Pesquisa: referencias/ + TEMPLATE.md. Combina as 3 escolhidas:
 R1 Legora (SE): foto cinematográfica dominante, frase curta, CTA discreto.
 R2 Freshfields (UK): manchete serifada grande, alinhada à esquerda, ritmo editorial.
 R3 Jaeger-LeCoultre (CH): grade fria/neutra, caixa alta espaçada, assinatura de relojoaria.
1 cor de acento (champagne), 3 níveis (linha fina · manchete · CTA), grão leve, vinheta. Composição varia só no alinhamento/posição.
Copy = v4c aprovada pelos agentes (sem promessa, Provimento 205). python3 gerar_v5.py"""
import os,json,subprocess
D=os.path.dirname(os.path.abspath(__file__)); C=os.path.abspath(f'{D}/../v3/cenas-gemini')
CH='#D9C08C'
# nome: (pos Y da cena 4:5, layout, linha fina, manchete, cta)
P={'ADV-1':('-330px','bl','Advogado, te procuram','E só acham<br>a <i>sombra?</i>','Manda ADV no WhatsApp'),
 'ADV-2':('-190px','tl','Advogado sério na lei,','e <i>invisível</i><br>no Google?','Dentro do Provimento 205'),
 'ADV-3':('-60px','bc','Advogado, estudou anos.','O cliente<br><i>te acha?</i>','Manda ADV no WhatsApp'),
 'ADV-4':('-110px','tr','Advogado, seu marketing','joga xadrez<br>ou <i>damas?</i>','Estratégia antes do anúncio')}
CAPA=('50%','bc','Advogado de São Luís','Dá pra anunciar<br><i>sem ferir</i> a OAB?','▶ Assista')
def html(H,cena,pos,lay,fina,man,cta):
    v,hz=lay[0],lay[1]; al={'l':'left','c':'center','r':'right'}[hz]
    vt=f"top:{H*.13:.0f}px" if v=='t' else f"bottom:{H*.115:.0f}px"
    sh=('linear-gradient(180deg,rgba(0,0,0,.88),rgba(0,0,0,.35) 38%,transparent 55%,transparent 80%,rgba(0,0,0,.7))' if v=='t'
        else 'linear-gradient(180deg,rgba(0,0,0,.55),transparent 16%,transparent 48%,rgba(0,0,0,.82) 70%,#000 97%)')
    fs=H*(.072 if H>1500 else .082)
    return f"""<html><head><link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,600;1,500&family=Inter:wght@400;500;600&display=block" rel="stylesheet"><style>*{{margin:0;box-sizing:border-box}}
body{{width:1080px;height:{H}px;overflow:hidden;position:relative;background:#000}}
.bg{{position:absolute;inset:0;background:url('file://{C}/{cena}.jpg') 50% {pos}/{'cover' if pos=='50%' else '100% auto'};filter:saturate(.62) contrast(1.08) brightness(.95) sepia(.16)}}
.sh{{position:absolute;inset:0;background:{sh}}}
.vg{{position:absolute;inset:0;background:radial-gradient(ellipse at 50% 42%,transparent 50%,rgba(0,0,0,.55))}}
.gr{{position:absolute;inset:0;opacity:.07;mix-blend-mode:overlay;background:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='200' height='200'><filter id='n'><feTurbulence baseFrequency='.9' numOctaves='2'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>")}}
.fr{{position:absolute;inset:34px;border:1px solid {CH}55}}
.hd{{position:absolute;top:{H*.045:.0f}px;left:76px;right:76px;display:flex;justify-content:space-between;font:500 19px Inter;letter-spacing:.34em;color:#fff;text-transform:uppercase}}
.hd b{{font-weight:600;color:{CH}}}
.t{{position:absolute;left:84px;right:84px;{vt};text-align:{al};color:#F4EFE6}}
.f{{font:500 {H*.0215:.0f}px Inter;letter-spacing:.26em;text-transform:uppercase;color:{CH};margin-bottom:{H*.016:.0f}px}}
.m{{white-space:nowrap;font:500 {fs:.0f}px/1.0 'Playfair Display';letter-spacing:-.01em;text-shadow:0 4px 40px rgba(0,0,0,.6)}}
.m i{{color:{CH};font-weight:500}}
.c{{white-space:nowrap;display:inline-flex;align-items:center;gap:22px;margin-top:{H*.026:.0f}px;font:600 {H*.0158:.0f}px Inter;letter-spacing:.3em;text-transform:uppercase}}
.c:before{{content:'';width:70px;height:1px;background:{CH}}}
.s{{position:absolute;bottom:{H*.035:.0f}px;left:0;right:0;text-align:center;color:#fff;font:600 17px Inter;letter-spacing:.42em}}
.s span{{display:block;margin-top:8px;font:400 13px Inter;letter-spacing:.3em;color:{CH}}}
</style></head><body><div class="bg"></div><div class="sh"></div><div class="vg"></div><div class="gr"></div><div class="fr"></div>
<div class="hd"><span><b>N.º {cena[-1] if cena[-1].isdigit() else 'R'}</b> &nbsp;Advocacia</span><span>São Luís · MA</span></div>
<div class="t"><div class="f">{fina}</div><div class="m">{man}</div><div class="c">{cta}</div></div>
<div class="s">LINDSON ALMEIDA<span>MARKETING PARA ADVOGADOS</span></div><script>const g=document.querySelector('.m');let z=parseFloat(getComputedStyle(g).fontSize);while(g.scrollWidth>912&&z>40){{z-=3;g.style.fontSize=z+'px'}}</script></body></html>"""
J=[]
def shot(h,H,out):
    t=f'{D}/_h{len(J)}.html';open(t,'w').write(h);J.append([t,H,out])
for n,a in P.items():
    shot(html(1920,n,'50%',*a[1:]),1920,f'{D}/artes/{n}-9x16-v5.jpg'); shot(html(1350,n,*a),1350,f'{D}/artes/{n}-4x5-v5.jpg')
shot(html(1920,'CAPA-ADV',*CAPA),1920,f'{D}/artes/ADV-capa-reels-9x16-v5.jpg')
open(f'{D}/_j.json','w').write(json.dumps(J));subprocess.run(['node',f'{D}/render.js',f'{D}/_j.json'],check=True,cwd='/home/user/lindson')
for t,_,_ in J: os.remove(t)
os.remove(f'{D}/_j.json')
from PIL import Image
w,h=300,533;ns=list(P)+['ADV-capa-reels'];S=Image.new('RGB',(5*(w+20)+20,h+20+375+40),'#111')
for j,n in enumerate(ns):
    S.paste(Image.open(f'{D}/artes/{n}-9x16-v5.jpg').resize((w,h)),(20+j*(w+20),20))
    if n in P: S.paste(Image.open(f'{D}/artes/{n}-4x5-v5.jpg').resize((w,375)),(20+j*(w+20),h+40))
S.save(f'{D}/folha-adv-v5.jpg',quality=88)
