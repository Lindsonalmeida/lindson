"""v6 advogado (conta Zuleide, 16/11/2026). Pedido do Lindson: "amplie minhas fotos para maior autoridade, nada no meu rosto, letras mais masculinas".
Mantém v5 (luxo editorial, preto + champagne, sem fitas/selos/neon). Refs iguais à v5: R1 Legora (foto dominante), R2 Freshfields (manchete grande à esquerda), R3 Jaeger-LeCoultre (caixa alta espaçada).
Mudanças: recorte cintura/peito para cima guiado pelo rosto (Haar), ampliação Lanczos 2-pass + unsharp; manchete Oswald caixa alta, assinatura Cinzel; texto só abaixo do rosto, checado por código."""
import os,json,subprocess,cv2
from PIL import Image,ImageFilter
D=os.path.dirname(os.path.abspath(__file__)); C=os.path.abspath(f'{D}/../v3/cenas-gemini'); T=f'{D}/_tmp'; os.makedirs(T,exist_ok=True)
CH='#D9C08C'
P={'ADV-1':('l','Advogado, te procuram','E só acham<br>a <em>sombra?</em>','Manda ADV no WhatsApp'),
 'ADV-2':('l','Advogado sério na lei,','e <em>invisível</em><br>no Google?','Dentro do Provimento 205'),
 'ADV-3':('c','Advogado, estudou anos.','O cliente<br><em>te acha?</em>','Manda ADV no WhatsApp'),
 'ADV-4':('r','Advogado, seu marketing','joga xadrez<br>ou <em>damas?</em>','Estratégia antes do anúncio'),
 'CAPA-ADV':('c','Advogado de São Luís','Dá pra anunciar<br><em>sem ferir</em> a OAB?','▶ Assista')}
cas=cv2.CascadeClassifier(os.environ.get('HAAR','/tmp/claude-0/-home-user/90050ae9-6cfe-5d35-9728-99eedbe6040e/scratchpad/hc.xml'))
def face(n):
    g=cv2.cvtColor(cv2.imread(f'{C}/{n}.jpg'),cv2.COLOR_BGR2GRAY); f=cas.detectMultiScale(g,1.1,6,minSize=(50,50))
    return max(f,key=lambda r:r[2]*r[3])
def crop(n,H):
    im=Image.open(f'{C}/{n}.jpg'); W0,H0=im.size; x,y,w,h=face(n)
    cw=min(W0,w*4.6); ch=cw*H/1080
    if ch>H0: ch=H0; cw=ch*1080/H
    top=y-h*.55; y0=max(0,min(top-ch*.10,H0-ch)); x0=max(0,min(x+w/2-cw/2,W0-cw))
    c=im.crop((round(x0),round(y0),round(x0+cw),round(y0+ch)))
    c=c.resize((540,int(540*H/1080)),Image.LANCZOS).resize((1080,H),Image.LANCZOS).filter(ImageFilter.UnsharpMask(1.6,70,2))
    p=f'{T}/{n}-{H}.jpg'; c.save(p,quality=95); k=1080/cw
    fb=[(x-x0)*k,(top-y0)*k,(x+w-x0)*k,(y+h*1.25-y0)*k]  # cabeça inteira (cabelo ao queixo)
    return p,fb
def html(H,img,lay,fina,man,cta):
    al={'l':'left','c':'center','r':'right'}[lay]; fs=H*(.066 if H>1500 else .074)
    return f"""<html><head><link href="https://fonts.googleapis.com/css2?family=Oswald:wght@400;500;600&family=Cinzel:wght@500;600&family=Inter:wght@500;600&display=block" rel="stylesheet"><style>*{{margin:0;box-sizing:border-box}}
body{{width:1080px;height:{H}px;overflow:hidden;position:relative;background:#000}}
.bg{{position:absolute;inset:0;background:url('file://{img}') center/cover;filter:saturate(.66) contrast(1.08) brightness(.97) sepia(.14)}}
.sh{{position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.45),transparent 9%,transparent 52%,rgba(0,0,0,.8) 70%,#000 96%)}}
.gr{{position:absolute;inset:0;opacity:.06;mix-blend-mode:overlay;background:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='200' height='200'><filter id='n'><feTurbulence baseFrequency='.9' numOctaves='2'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>")}}
.hd{{position:absolute;top:{H*.035:.0f}px;left:70px;right:70px;display:flex;justify-content:space-between;font:600 17px Inter;letter-spacing:.34em;color:#fff;text-transform:uppercase}}
.hd b{{color:{CH}}}
.t{{position:absolute;left:80px;right:80px;bottom:{H*.11:.0f}px;text-align:{al};color:#F4EFE6}}
.f{{font:600 {H*.02:.0f}px Inter;letter-spacing:.26em;text-transform:uppercase;color:{CH};margin-bottom:{H*.014:.0f}px}}
.m{{display:inline-block;white-space:nowrap;font:600 {fs:.0f}px/1.02 Oswald;text-transform:uppercase;letter-spacing:.01em;text-shadow:0 4px 40px rgba(0,0,0,.7)}}
.m em{{font-style:normal;color:{CH}}}
.c{{display:flex;justify-content:{ {'l':'flex-start','c':'center','r':'flex-end'}[lay]};align-items:center;gap:22px;margin-top:{H*.022:.0f}px;font:600 {H*.0155:.0f}px Inter;letter-spacing:.3em;text-transform:uppercase;white-space:nowrap}}
.c:before{{content:'';width:70px;height:1px;background:{CH}}}
.s{{position:absolute;bottom:{H*.03:.0f}px;left:0;right:0;text-align:center;color:#fff;font:600 21px Cinzel;letter-spacing:.32em}}
.s span{{display:block;margin-top:6px;font:500 12px Inter;letter-spacing:.34em;color:{CH}}}
</style></head><body><div class="bg"></div><div class="sh"></div><div class="gr"></div>
<div class="hd"><span><b>Advocacia</b></span><span>São Luís · MA</span></div>
<div class="t"><div class="f">{fina}</div><div class="m">{man}</div><div class="c">{cta}</div></div>
<div class="s">LINDSON ALMEIDA<span>MARKETING PARA ADVOGADOS</span></div><script>const g=document.querySelector('.m');let z=parseFloat(getComputedStyle(g).fontSize);while(g.scrollWidth>920&&z>40){{z-=3;g.style.fontSize=z+'px'}}</script></body></html>"""
J=[];F={}
for n,a in P.items():
    for H,suf in ((1920,'9x16'),(1350,'4x5')):
        if n=='CAPA-ADV' and H==1350: continue
        img,fb=crop(n,H); o=f"{D}/artes/{'ADV-capa-reels' if n=='CAPA-ADV' else n}-{suf}-v6.jpg"
        t=f'{T}/{len(J)}.html'; open(t,'w').write(html(H,img,*a)); J.append([t,H,o]); F[o]=fb
open(f'{T}/j.json','w').write(json.dumps(J)); subprocess.run(['node',f'{D}/render.js',f'{T}/j.json'],check=True,cwd='/home/user/lindson')
ok=True
for o,fb in F.items():
    m=40; z=[fb[0]-m,fb[1]-m,fb[2]+m,fb[3]+m]; bx=json.load(open(o+'.box.json')); os.remove(o+'.box.json')
    bad=[b for b in bx if not(b[2]<z[0] or b[0]>z[2] or b[3]<z[1] or b[1]>z[3])]
    print(os.path.basename(o),'rosto',[round(v) for v in fb],'OK' if not bad else f'CRUZA {bad}'); ok&=not bad
import shutil; shutil.rmtree(T)
ns=list(P)[:4]+['ADV-capa-reels']; w,h=300,533; S=Image.new('RGB',(5*(w+20)+20,h+20+375+40),'#111')
for j,n in enumerate(ns):
    S.paste(Image.open(f'{D}/artes/{n}-9x16-v6.jpg').resize((w,h)),(20+j*(w+20),20))
    if n!='ADV-capa-reels': S.paste(Image.open(f'{D}/artes/{n}-4x5-v6.jpg').resize((w,375)),(20+j*(w+20),h+40))
S.save(f'{D}/folha-adv-v6.jpg',quality=88); assert ok
