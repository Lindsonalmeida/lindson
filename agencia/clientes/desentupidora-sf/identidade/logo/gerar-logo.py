# Gera a família da logo da Desentupidora SF em SVG (vetor), a partir do desenho original.
import os,sys,json
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from glyphs import text_path,width
BI='Montserrat-BlackItalic.ttf';BD='Montserrat-Bold.ttf'
NAVY='#061a4a';NAVY2='#0a2a6e';ROYAL='#1d5fd0';SKY='#3fa9ff';ORANGE='#ff8a00';OFF='#f4f8ff';WHITE='#ffffff';BLACK='#111111'
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),'arquivos','svg');os.makedirs(OUT,exist_ok=True)

SHIELD_O="M200 52 C 238 76 292 86 338 84 L 338 236 C 338 322 282 376 200 414 C 118 376 62 322 62 236 L 62 84 C 108 86 162 76 200 52 Z"
SHIELD_I="M200 78 C 234 98 280 107 316 106 L 316 236 C 316 308 270 352 200 386 C 130 352 84 308 84 236 L 84 106 C 120 107 166 98 200 78 Z"
DROP="M200 0 C 214 26 236 44 236 70 C 236 90 220 106 200 106 C 180 106 164 90 164 70 C 164 44 186 26 200 0 Z"
DROP_HI="M186 62 C 186 50 192 40 198 32 C 196 44 194 54 196 66 C 194 74 186 72 186 62 Z"
WAVE="M18 300 C 70 262 120 300 186 296 C 262 292 300 238 384 226 C 330 262 300 318 232 330 C 150 346 92 300 18 300 Z"
WAVE2="M40 318 C 90 300 130 328 190 324 C 250 320 292 286 352 270 C 310 300 276 336 222 342 C 150 352 100 318 40 318 Z"

def defs(uid):
    return f'''<defs>
<linearGradient id="silver{uid}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffffff"/><stop offset=".45" stop-color="#c9d3e3"/><stop offset=".55" stop-color="#8b97ad"/><stop offset="1" stop-color="#e6ebf3"/></linearGradient>
<linearGradient id="inner{uid}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{NAVY2}"/><stop offset="1" stop-color="{NAVY}"/></linearGradient>
<linearGradient id="letters{uid}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#7cc6ff"/><stop offset=".5" stop-color="{SKY}"/><stop offset="1" stop-color="{ROYAL}"/></linearGradient>
<linearGradient id="drop{uid}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#9ad6ff"/><stop offset="1" stop-color="{ROYAL}"/></linearGradient>
<linearGradient id="wave{uid}" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{ROYAL}"/><stop offset=".6" stop-color="{SKY}"/><stop offset="1" stop-color="#9ad6ff"/></linearGradient>
<radialGradient id="badge{uid}" cx=".5" cy=".42" r=".6"><stop offset="0" stop-color="#16408f"/><stop offset="1" stop-color="{NAVY}"/></radialGradient>
</defs>'''

def sf_letters(size=148,cy=282):
    w=width('SF',BI,size,-4);d,_=text_path('SF',BI,size,200-w/2+6,cy,-4);return d

def symbol(scheme,uid='a',tx=0,ty=0,s=1.0):
    """scheme: 'color' | ('mono',cor,fundo)"""
    L=sf_letters()
    if scheme=='color':
        body=(f'<path d="{SHIELD_O}" fill="url(#silver{uid})"/><path d="{SHIELD_I}" fill="url(#inner{uid})"/>'
              f'<path d="{L}" fill="url(#letters{uid})" stroke="{NAVY}" stroke-width="2"/>'
              f'<path d="{WAVE}" fill="url(#wave{uid})" stroke="{NAVY}" stroke-width="5" stroke-linejoin="round"/>'
              f'<path d="{WAVE2}" fill="{WHITE}" opacity=".9"/>'
              f'<path d="{DROP}" fill="url(#drop{uid})" stroke="{NAVY}" stroke-width="5"/><path d="{DROP_HI}" fill="#fff" opacity=".85"/>')
    else:
        _,c,bg=scheme
        m=f'mk{uid}{abs(hash(c))%9999}'
        body=(f'<mask id="{m}" maskUnits="userSpaceOnUse" x="-20" y="-20" width="440" height="460">'
              f'<path d="{SHIELD_O}" fill="#fff"/><path d="{SHIELD_I}" fill="#000"/><path d="{L}" fill="#fff"/>'
              f'<path d="{WAVE}" fill="#fff" stroke="#000" stroke-width="10" stroke-linejoin="round" paint-order="stroke"/>'
              f'<path d="{WAVE2}" fill="#000"/>'
              f'<path d="{DROP}" fill="#fff" stroke="#000" stroke-width="10" paint-order="stroke"/><path d="{DROP_HI}" fill="#000"/></mask>'
              f'<rect x="-20" y="-20" width="440" height="460" fill="{c}" mask="url(#{m})"/>')
    return f'<g transform="translate({tx},{ty}) scale({s})">{body}</g>'

def word(txt,font,size,x,y,fill,track=0,anchor='start'):
    w=width(txt,font,size,track)
    if anchor=='middle': x-=w/2
    d,_=text_path(txt,font,size,x,y,track);return f'<path d="{d}" fill="{fill}"/>',w

def svg(w,h,inner,uid='a',bg=None):
    b=f'<rect width="{w}" height="{h}" fill="{bg}"/>' if bg else ''
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">{defs(uid)}{b}{inner}</svg>'

# cores por versão: (simbolo, cor do nome, cor do apoio, fundo-para-recortes)
VERS={
 'colorida':('color',NAVY,ORANGE,WHITE),
 'negativa':('color',WHITE,ORANGE,NAVY),
 'mono-azul':(('mono',NAVY,WHITE),NAVY,NAVY,WHITE),
 'mono-branca':(('mono',WHITE,NAVY),WHITE,WHITE,NAVY),
 'preta':(('mono',BLACK,WHITE),BLACK,BLACK,WHITE),
}
def fix(sc,bg):  # o mono precisa saber a cor de fundo para os recortes
    return sc if sc=='color' else ('mono',sc[1],bg)

files=[]
def save(name,s):
    open(os.path.join(OUT,name+'.svg'),'w').write(s);files.append(name)

for v,(sc,cn,ca,bgc) in VERS.items():
    # símbolo
    save(f'simbolo-{v}',svg(400,420,symbol(fix(sc,bgc),v),v))
    # horizontal
    S=0.56; sym=symbol(fix(sc,bgc),v,0,-12,S)
    n1,w1=word('DESENTUPIDORA',BI,74,248,118,cn,-1)
    n2,w2=word('SF',BI,74,248+w1+18,118,ca if v!='mono-azul' and v!='preta' and v!='mono-branca' else cn,-1)
    t,wt=word('DESENTUPIMENTO · SÃO LUÍS - MA',BD,22,252,166,cn,6.2)
    bar=f'<rect x="252" y="138" width="{w1+18+w2-4}" height="4" fill="{ca}"/>'
    W=int(248+w1+18+w2+10)
    save(f'horizontal-{v}',svg(W,210,sym+n1+n2+bar+t,v))
    # vertical
    n1,w1=word('DESENTUPIDORA',BI,64,0,0,cn,-1)
    W=max(int(w1)+40,420); cx=W/2
    sym=symbol(fix(sc,bgc),v,cx-200*0.82,0,0.82)
    n1,_=word('DESENTUPIDORA',BI,64,cx,420,cn,-1,'middle')
    n2,_=word('SF',BI,30,cx,0,cn,0,'middle')
    t,_=word('SÃO LUÍS · MA',BD,22,cx,468,ca,8,'middle')
    save(f'vertical-{v}',svg(W,490,sym+n1+t,v))

# selo circular (versão plana da logo original)
def selo(uid,ring=SKY):
    sym=symbol('color',uid,256-200*0.74,54,0.74)
    n,_=word('DESENTUPIDORA',BI,36,256,426,WHITE,-1,'middle')
    t,_=word('SÃO LUÍS · MA',BD,14,256,452,ORANGE,6,'middle')
    return (f'<circle cx="256" cy="256" r="252" fill="#e9eef6"/><circle cx="256" cy="256" r="240" fill="url(#badge{uid})"/>'
            f'<circle cx="256" cy="256" r="226" fill="none" stroke="{ring}" stroke-width="4"/>{sym}{n}{t}')
save('selo-colorido',svg(512,512,selo('s'),'s'))
# ícone de perfil e favicon
save('icone-perfil',svg(512,512,f'<circle cx="256" cy="256" r="256" fill="url(#badges2)"/>'+symbol('color','s2',256-200*0.9,52,0.9),'s2'))
fav=(f'<rect width="64" height="64" rx="14" fill="{NAVY}"/>'+symbol(('mono',WHITE,NAVY),'f',32-200*0.13,5,0.13))
save('favicon',svg(64,64,fav,'f'))
json.dump(files,open(os.path.join(OUT,'..','lista.json'),'w'))
print(len(files),'svgs')
