# Pinterest v3 · por cliente (conta Pedro, 16/11/2026). Pedido do Lindson sobre a v2: "monte por cliente".
# 7 pastas (1 por cliente), 6 pins cada. Mesmo padrão estético da v2 (só o trabalho, legenda pequena):
#  capa  = Mucho: logo sozinho na cor da marca (referência Mucho / Pentagram case cover)
#  hero  = Pentagram/Porto Rocha: mockup realista (celular, notebook, impresso) em palco com sombra
#  mosaico = Koto/Studio Dumbar: aplicações em grade com calha fina
#  detalhe = Collins/Koto: cartela de cores impressa (chips) com a letra da marca
#  uso   = DesignStudio: peça em uso / foto real em tela cheia
# Real Time e Legislativo refeitos com mockups (celular, notebook, brand book impresso), sem slide do Behance.
# Uso: python3 gerar.py [filtro]  (precisa do repo privado em /home/user/centrallindsonalmeida)
import os, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps
H=os.path.dirname(os.path.abspath(__file__)); R=os.path.abspath(os.path.join(H,'../../../../..'))
PV=os.environ.get('PRIVADO','/home/user/centrallindsonalmeida/dados/clientes-arquivos/')
def F(p):
    if p.startswith('@'): return os.path.join(PV,p[1:])
    if p.startswith('$'): return os.path.join(H,'assets',p[1:])
    return os.path.join(R,p)
INTER=os.path.join(H,'..','Inter.ttf')
def I(s,w=400):
    f=ImageFont.truetype(INTER,s)
    try: f.set_variation_by_axes([w])
    except Exception: pass
    return f
W,HH=1000,1500
def op(p): return Image.open(F(p))
def fit(im,w,h,ax=.5,ay=.5):
    im=im.convert('RGB'); r=max(w/im.width,h/im.height); im=im.resize((round(im.width*r)+1,round(im.height*r)+1),Image.LANCZOS)
    x=int((im.width-w)*ax); y=int((im.height-h)*ay); return im.crop((x,y,x+w,y+h))
def grain(c,a=.03):
    n=Image.effect_noise(c.size,48).convert('RGB'); return Image.blend(c,n,a)
def lum(c): return (c[0]*.3+c[1]*.59+c[2]*.11)
def stage(bg):
    """palco: cor da marca com luz suave vinda de cima (fundo infinito de estúdio)"""
    c=Image.new('RGB',(W,HH),bg); hi=tuple(min(255,int(v*1.25+12)) for v in bg); lo=tuple(int(v*.62) for v in bg)
    m=Image.new('L',(W,HH),0); ImageDraw.Draw(m).ellipse((-300,-500,W+300,HH*.75),fill=255); m=m.filter(ImageFilter.GaussianBlur(260))
    c=Image.composite(Image.new('RGB',(W,HH),hi),c,m)
    v=Image.new('L',(W,HH),0); ImageDraw.Draw(v).rectangle((0,HH*.78,W,HH),fill=200); v=v.filter(ImageFilter.GaussianBlur(160))
    return Image.composite(Image.new('RGB',(W,HH),lo),c,v)
def cap(c,cliente,tipo,ia=False,top=False,dark=None):
    d=ImageDraw.Draw(c); y=46 if top else HH-78
    if dark is None:
        reg=c.crop((0,y-10,W,y+40)).resize((1,1)).getpixel((0,0)); dark=lum(reg)<140
    if not top and dark:
        g=Image.new('L',(1,240)); [g.putpixel((0,i),int(150*(i/239)**1.6)) for i in range(240)]
        c.paste((0,0,0),(0,HH-240,W,HH),g.resize((W,240)))
    col=(245,243,238) if dark else (20,20,20); sub=(200,198,192) if dark else (95,95,95)
    d.text((56,y),cliente,font=I(26,600),fill=col)
    d.text((56+d.textlength(cliente,font=I(26,600))+14,y),tipo,font=I(26,400),fill=sub)
    t='Lindson Almeida Studio'; d.text((W-56-d.textlength(t,font=I(22,500)),y+3),t,font=I(22,500),fill=sub)
    if ia: d.text((56,y-34 if not top else y+40),'mockup · imagem gerada por IA',font=I(17,400),fill=sub)
    return c
def shadow(c,box,r,blur=40,op=150,dy=34):
    sh=Image.new('L',c.size,0); x0,y0,x1,y1=box
    ImageDraw.Draw(sh).rounded_rectangle((x0+6,y0+dy,x1+6,y1+dy),r,fill=op); sh=sh.filter(ImageFilter.GaussianBlur(blur))
    c.paste((0,0,0),(0,0),sh)
def rmask(size,r):
    m=Image.new('L',size,0); ImageDraw.Draw(m).rounded_rectangle((0,0,size[0]-1,size[1]-1),r,fill=255); return m
# ---------- dispositivos ----------
def phone_img(screen,w=470,ay=0.0):
    """iPhone desenhado: corpo titânio, borda preta, ilha dinâmica e reflexo"""
    h=int(w*2.06); r=int(w*.17); b=int(w*.045)
    ph=Image.new('RGBA',(w,h),(0,0,0,0)); d=ImageDraw.Draw(ph)
    d.rounded_rectangle((0,0,w-1,h-1),r,fill=(58,58,62)); d.rounded_rectangle((3,3,w-4,h-4),r-3,fill=(150,150,156))
    d.rounded_rectangle((6,6,w-7,h-7),r-6,fill=(12,12,13))
    sw,sh=w-2*b,h-2*b; screen=screen.convert('RGB')
    if screen.width/screen.height>.62:
        im=screen.resize((sw,int(screen.height*sw/screen.width)),Image.LANCZOS); scr=Image.new('RGB',(sw,sh),im.getpixel((2,2))); scr.paste(im,(0,(sh-im.height)//2))
    else: scr=fit(screen,sw,sh,.5,ay)
    ph.paste(scr,(b,b),rmask((sw,sh),r-b))
    iw=int(w*.27); d.rounded_rectangle(((w-iw)//2,b+int(w*.03),(w+iw)//2,b+int(w*.03)+int(w*.075)),40,fill=(0,0,0))
    gl=Image.new('L',(w,h),0); ImageDraw.Draw(gl).polygon([(0,0),(w*.62,0),(0,h*.42)],fill=34); gl=gl.filter(ImageFilter.GaussianBlur(30))
    m=Image.new('L',(w,h),0); m.paste(gl,(0,0),rmask((w,h),r)); ph.paste((255,255,255),(0,0),m)
    return ph
def laptop_img(screen,w=900):
    sw=int(w*.86); shh=int(sw*10/16); bz=int(w*.018)
    lid=Image.new('RGBA',(sw+2*bz,shh+2*bz+int(w*.012)),(0,0,0,0)); d=ImageDraw.Draw(lid)
    d.rounded_rectangle((0,0,lid.width-1,lid.height-1),22,fill=(150,152,158)); d.rounded_rectangle((3,3,lid.width-4,lid.height-1),20,fill=(14,14,15))
    lid.paste(fit(screen,sw,shh,.5,0),(bz,bz))
    base=Image.new('RGBA',(w,int(w*.035)),(0,0,0,0)); d=ImageDraw.Draw(base)
    d.rounded_rectangle((0,0,w-1,base.height-1),12,fill=(186,188,194)); d.rectangle((0,0,w,6),fill=(214,216,220))
    d.rounded_rectangle((w//2-80,0,w//2+80,9),6,fill=(150,152,158))
    out=Image.new('RGBA',(w,lid.height+base.height),(0,0,0,0)); out.paste(lid,((w-lid.width)//2,0),lid); out.paste(base,(0,lid.height),base)
    return out
def place(c,obj,x,y,rot=0,blur=46,op=165,dy=40,r=60):
    if rot: obj=obj.rotate(rot,resample=Image.BICUBIC,expand=True)
    a=obj.split()[3]; sh=Image.new('L',c.size,0); sh.paste(a.point(lambda v:op if v>10 else 0),(x+8,y+dy))
    c.paste((0,0,0),(0,0),sh.filter(ImageFilter.GaussianBlur(blur))); c.paste(obj,(x,y),obj); return c
def paper(img,w,border=0,r=6):
    im=img.convert('RGB'); h=int(im.height*w/im.width); im=im.resize((w,h),Image.LANCZOS)
    p=Image.new('RGBA',(w+2*border,h+2*border),(248,247,244,255)); p.paste(im,(border,border))
    # leve dobra/brilho de papel
    g=Image.new('L',p.size,0); ImageDraw.Draw(g).rectangle((0,0,p.width//2,p.height),fill=18); g=g.filter(ImageFilter.GaussianBlur(120))
    p.paste((255,255,255),(0,0),g); p.putalpha(rmask(p.size,r)); return p
# ---------- composições ----------
def CAPA(logo,cliente,bg,w=600,crop=None,feather=False,tipo='Identidade visual'):
    c=stage(bg); lg=op(logo)
    if crop: lg=lg.crop(crop)
    lg=lg.convert('RGBA'); lg=lg.resize((w,int(lg.height*w/lg.width)),Image.LANCZOS)
    if feather:
        m=Image.new('L',lg.size,0); ImageDraw.Draw(m).rectangle((30,24,lg.width-30,lg.height-24),fill=255); lg.putalpha(m.filter(ImageFilter.GaussianBlur(24)))
    c.paste(lg,((W-w)//2,(HH-lg.height)//2-50),lg)
    return cap(grain(c,.025),cliente,tipo)
def HERO_PHONE(screen,cliente,tipo,bg,ay=0,ia=False,rot=-4):
    c=stage(bg); ph=phone_img(op(screen),500,ay); place(c,ph,(W-ph.width)//2-20,170,rot=rot)
    return cap(grain(c,.02),cliente,tipo,ia=ia,top=True)
def DUO_PHONE(s1,s2,cliente,tipo,bg,ay=(0,0)):
    c=stage(bg); a=phone_img(op(s1),420,ay[0]); b=phone_img(op(s2),420,ay[1])
    place(c,a,70,300,rot=5); place(c,b,470,150,rot=-5)
    return cap(grain(c,.02),cliente,tipo,top=True)
def LAPTOP(screen,phone,cliente,tipo,bg,ay=0):
    c=stage(bg); lp=laptop_img(op(screen),940); place(c,lp,30,430,dy=30,op=140)
    if phone: ph=phone_img(op(phone),250,ay); place(c,ph,690,700,rot=0,blur=30,dy=26)
    return cap(grain(c,.02),cliente,tipo,top=True)
def PRINT(img,cliente,tipo,bg,w=700,rot=-6,crop=None,second=None,ia=False):
    c=stage(bg); im=op(img)
    if crop: im=im.crop(crop)
    if second:
        s=op(second[0]); s=s.crop(second[1]) if second[1] else s
        p2=paper(s,w-60); place(c,p2,W-p2.width-40,640,rot=7,op=120,blur=34,dy=22)
    p=paper(im,w); place(c,p,60 if second else (W-p.width)//2-30,260,rot=rot,op=150,blur=38,dy=28)
    return cap(grain(c,.025),cliente,tipo,ia=ia,top=True)
def MOSAIC(srcs,cliente,tipo,bg=(14,14,14),layout='c',ia=False):
    c=Image.new('RGB',(W,HH),bg); g=10
    L={'a':[(0,0,W,760),(0,770,495,HH),(505,770,W,HH)],
       'b':[(0,0,495,740),(505,0,W,740),(0,750,W,HH)],
       'c':[(0,0,495,495),(505,0,W,495),(0,505,495,1000),(505,505,W,1000),(0,1010,W,HH)],
       'd':[(0,0,W,620),(0,630,330,1060),(340,630,660,1060),(670,630,W,1060),(0,1070,W,HH)]}[layout]
    for s,b in zip(srcs,L):
        src,ax,ay=(s if isinstance(s,tuple) else (s,.5,.5))
        c.paste(fit(op(src),b[2]-b[0],b[3]-b[1],ax,ay),b[:2])
    return cap(grain(c,.02),cliente,tipo,ia=ia)
def CHIPS(cores,cliente,bg,letra,logo=None):
    """cartela de cores impressa (estilo Pantone) + nome das letras"""
    c=stage(bg); n=len(cores); cw=520; ch=150
    for i,(nome,hx,pct) in enumerate(cores):
        col=tuple(int(hx[k:k+2],16) for k in (1,3,5))
        card=Image.new('RGBA',(cw,ch+70),(250,249,246,255)); d=ImageDraw.Draw(card)
        d.rectangle((0,0,cw,ch),fill=col); d.text((22,ch+14),nome,font=I(24,600),fill=(25,25,25))
        d.text((22,ch+42),f'{hx.upper()}  ·  {pct}',font=I(18,400),fill=(110,110,110))
        x=150+(i%2)*40; y=190+i*(ch+92)
        place(c,card,int(x+i*28),int(y),rot=(-3 if i%2 else 2),op=120,blur=22,dy=14,r=4)
    d=ImageDraw.Draw(c); dark=lum(bg)<140; col=(240,238,232) if dark else (25,25,25)
    d.text((56,HH-150),letra,font=I(28,500),fill=col)
    return cap(grain(c,.025),cliente,'Cores e letras')
def FULL(src,cliente,tipo,ax=.5,ay=.5,ia=False,crop=None):
    im=op(src)
    if crop: im=im.crop(crop)
    return cap(grain(fit(im,W,HH,ax,ay)),cliente,tipo,ia=ia)
def STAGE(src,cliente,tipo,bg,w=820,crop=None,ia=False,radius=0):
    c=stage(bg); im=op(src).convert('RGB')
    if crop: im=im.crop(crop)
    im=im.resize((w,int(im.height*w/im.width)),Image.LANCZOS)
    if im.height>1180: im=im.crop((0,0,w,1180))
    x=(W-w)//2; y=(HH-im.height)//2+20; shadow(c,(x,y,x+w,y+im.height),radius+8)
    c.paste(im,(x,y),rmask(im.size,radius)); return cap(grain(c,.02),cliente,tipo,ia=ia,top=True)
# ---------- clientes ----------
OI='agencia/operacao-propria/identidade/'; WF='agencia/clientes/wf-celulares/identidade/pecas-final/'
JF='agencia/clientes/jaci-cunha/conteudo-nov/feed/'; JS='@jaci-site/img/'; JD='agencia/clientes/jaci-cunha/instagram-destaques/out/'
LV='agencia/clientes/leo-pinto/'; RT='agencia/clientes/rt-full-jobs/'; CU='@curso/'; DB='apps/clone-studio/identidade/'
CLIENTES={
 'oregano-turbo':('Orégano Turbo',(30,91,59),[
  ('capa',lambda n,b:CAPA(OI+'kit-mockup/logo-horizontal-creme.png',n,b,w=700)),
  ('fachada',lambda n,b:FULL(OI+'fotos-ia/A10-fachada.jpg',n,'Fachada',ia=True)),
  ('campanha',lambda n,b:MOSAIC([OI+'fotos-ia/B2-caixa-ceu.jpg',(OI+'fotos-ia/B5-motoboy.jpg',.5,.3),OI+'fotos-ia/B7-moca-carro.jpg'],n,'Campanha',layout='a',ia=True)),
  ('cores',lambda n,b:CHIPS([('Tomate','#C8302B','60%'),('Verde manjericão','#1E5B3B','25%'),('Creme','#F3EEE6','10%'),('Açafrão','#F2B33D','5%')],n,(20,19,17),'Bagel Fat One · Inter · IBM Plex Mono')),
  ('uniforme',lambda n,b:FULL(OI+'fotos-ia/A4-avental.jpg',n,'Uniforme',ia=True)),
  ('embalagem',lambda n,b:FULL(OI+'fotos-ia/A8-adesivo-pedido-saindo.jpg',n,'Embalagem',ia=True)),
 ]),
 'wf-celulares':('WF Celulares',(10,12,16),[
  ('capa',lambda n,b:CAPA('agencia/clientes/wf-celulares/identidade/logo-b/wf-logo-b-branca.png',n,b,w=440)),
  ('instagram',lambda n,b:HERO_PHONE(WF+'10-post-produto.jpg',n,'Instagram',(196,198,202),rot=-4)),
  ('aplicacoes',lambda n,b:MOSAIC([WF+'11-post-assistencia.jpg',WF+'12-post-prova.jpg',WF+'03-avatar.jpg',WF+'04-destaque-lacrados.jpg',(WF+'14-cartao-etiqueta.jpg',.5,.5)],n,'Aplicações',layout='c',ia=True)),
  ('cores',lambda n,b:CHIPS([('Preto','#0A0C10','60%'),('Azul WF','#2F6BFF','20%'),('Titânio','#8E8E93','15%'),('Branco gelo','#F5F5F7','5%')],n,(214,214,218),'SF Pro Display · Inter')),
  ('fachada',lambda n,b:STAGE(WF+'13-fachada.jpg',n,'Fachada',(10,10,11),w=1000,crop=(330,0,1590,1080),ia=True)),
  ('papelaria',lambda n,b:STAGE(WF+'14-cartao-etiqueta.jpg',n,'Papelaria',(10,10,11),w=1000,crop=(300,0,1620,1080),ia=True)),
 ]),
 'jaci-cunha':('Dra. Jaci Cunha',(107,22,32),[
  ('capa',lambda n,b:CAPA(JS+'monograma.webp',n,b,w=520,crop=(20,40,280,380),feather=True,tipo='Monograma')),
  ('instagram',lambda n,b:HERO_PHONE(JF+'r03.jpg',n,'Instagram',(235,201,195),rot=4)),
  ('feed',lambda n,b:MOSAIC([(JF+'r06.jpg',.5,.3),JF+'r10.jpg',JF+'r02.jpg',JF+'r12.jpg',(JF+'r05.jpg',.5,.35)],n,'Feed',bg=(43,7,13),layout='c')),
  ('cores',lambda n,b:CHIPS([('Bordô','#6B1620','55%'),('Vinho','#2B070D','25%'),('Dourado','#C9A46A','10%'),('Rosé','#EBC9C3','10%')],n,(43,7,13),'Cormorant Garamond itálica · Montserrat')),
  ('retrato',lambda n,b:FULL(JF+'r09.jpg',n,'Direção de arte',ay=.3)),
  ('destaques',lambda n,b:DUO_PHONE(JD+'01-avaliacao-1.jpg',JF+'r12.jpg',n,'Destaques e posts',(43,7,13))),
 ]),
 'leo-pinto':('Leo Pinto',(35,80,245),[
  ('capa',lambda n,b:CAPA(LV+'instagram-v12-feed/marca/logo_principal.png',n,(18,46,160),w=600)),
  ('apresentacao',lambda n,b:STAGE(LV+'instagram-v13-apresentacao/leo-v13-3-direita.jpg',n,'Instagram',(232,230,224),w=800)),
  ('feed',lambda n,b:MOSAIC([LV+'instagram-v13-apresentacao/leo-v13-1-esquerda.jpg',LV+'instagram-v13-apresentacao/leo-v13-2-meio.jpg',LV+'instagram-v14-datas/p1-15-11.jpg'],n,'Feed',layout='b')),
  ('cores',lambda n,b:CHIPS([('Laranja','#FF7A1A','55%'),('Azul royal','#2350F5','30%'),('Branco','#FFFFFF','15%')],n,(16,22,48),'Montserrat Black · Montserrat')),
  ('celular',lambda n,b:HERO_PHONE(LV+'instagram-v14-datas/p2-20-11.jpg',n,'Datas comemorativas',(255,122,26),rot=-4)),
  ('datas',lambda n,b:DUO_PHONE(LV+'instagram-v14-datas/p3-11-12.jpg',LV+'instagram-v14-datas/p4-25-12.jpg',n,'Datas comemorativas',(18,46,160))),
 ]),
 'real-time':('Real Time Full Jobs',(5,7,11),[
  ('capa',lambda n,b:CAPA('$rt-logo.png',n,b,w=720)),
  ('mini-site',lambda n,b:HERO_PHONE('@rt-full-jobs/mini-site-prints/celular-390-topo.png',n,'Mini site',(46,155,255),rot=-4)),
  ('site',lambda n,b:LAPTOP('@rt-full-jobs/mini-site-prints/desktop-1280-topo.png','@rt-full-jobs/mini-site-prints/celular-390-topo.png',n,'Site e celular',(17,22,31))),
  ('cores',lambda n,b:CHIPS([('Preto set','#05070B','60%'),('Branco luz','#F4F7FB','25%'),('Azul real','#2E9BFF','10%'),('REC','#FF3B3B','5%')],n,(17,22,31),'Geist · Manrope · Geist Mono')),
  ('instagram',lambda n,b:MOSAIC([RT+'instagram-v2/artes/post-01.jpg',RT+'instagram-v2/artes/post-03.jpg',RT+'instagram-v2/artes/post-02.jpg',RT+'instagram-v2/artes/post-05.jpg',(RT+'identidade/v1/fotos/set.jpg',.5,.3)],n,'Instagram',bg=(5,7,11),layout='c')),
  ('brand-book',lambda n,b:PRINT('@rt-full-jobs/brand-book/previa-capa.jpg',n,'Brand book',(196,200,206),w=820,rot=-5,second=('@rt-full-jobs/brand-book/previa-folha.jpg',None))),
 ]),
 'processo-legislativo':('Curso Processo Legislativo',(18,53,40),[
  ('capa',lambda n,b:CAPA('$pl-simbolo.png',n,b,w=560,tipo='Símbolo')),
  ('site',lambda n,b:LAPTOP(CU+'site/prints/site-1440-topo.png',CU+'site/prints/site-390-topo.png',n,'Site e celular',(14,34,26))),
  ('carrossel',lambda n,b:DUO_PHONE(CU+'identidade-premium/carrossel-01.png',CU+'identidade-premium/carrossel-02.png',n,'Carrossel',(239,230,212))),
  ('cores',lambda n,b:CHIPS([('Verde plenário','#123528','60%'),('Verde folha','#1D4A39','20%'),('Dourado','#C8A96B','10%'),('Papel','#EFE6D4','10%')],n,(14,34,26),'Instrument Serif · Inter')),
  ('stories',lambda n,b:MOSAIC([CU+'identidade-hemiciclo/story-01.png',CU+'identidade-hemiciclo/story-02.png',CU+'identidade-hemiciclo/story-03.png'],n,'Stories',bg=(14,34,26),layout='b')),
  ('brand-book',lambda n,b:PRINT(CU+'brand-book/previa-capa.jpg',n,'Brand book',(214,206,190),w=820,rot=-5,second=(CU+'brand-book/previa-folha.jpg',None))),
 ]),
 'duble':('Dublê',(14,13,22),[
  ('capa',lambda n,b:CAPA('$db-logo.png',n,b,w=620,tipo='Identidade de app')),
  ('app',lambda n,b:LAPTOP(DB+'tela-v2-1.png',DB+'tela-v2-celular.png',n,'App web e celular',(28,24,48))),
  ('celular',lambda n,b:HERO_PHONE(DB+'tela-v2-celular.png',n,'App no celular',(139,124,255),rot=4)),
  ('cores',lambda n,b:CHIPS([('Grafite','#0B0B10','60%'),('Painel','#15151C','20%'),('Violeta Dublê','#8B7CFF','15%'),('Linha','#2A2A35','5%')],n,(222,220,232),'Manrope · Geist Mono')),
  ('telas',lambda n,b:MOSAIC([DB+'tela-v2-3.png',DB+'tela-v2-4.png',DB+'tela-v2-6.png'],n,'Telas',bg=(14,13,22),layout='a')),
  ('previa',lambda n,b:STAGE(DB+'previa-app.png',n,'Interface',(28,24,48),w=900,radius=18)),
 ]),
}
if __name__=='__main__':
    only=sys.argv[1] if len(sys.argv)>1 else ''; out=os.path.join(H,'pins'); os.makedirs(out,exist_ok=True)
    PR=os.environ.get('PRANCHAS',os.path.join(H,'pranchas')); os.makedirs(PR,exist_ok=True)
    for slug,(nome,bg,pins) in CLIENTES.items():
        if only and only not in slug: continue
        ims=[]
        for i,(k,f) in enumerate(pins,1):
            im=f(nome,bg).convert('RGB'); fn=f'{slug}-{i:02d}-{k}.jpg'; im.save(os.path.join(out,fn),quality=90); ims.append(im)
        tw,th=330,495; pr=Image.new('RGB',(tw*6+70,th+120),(232,230,226)); d=ImageDraw.Draw(pr)
        d.text((10,24),nome,font=I(34,600),fill=(20,20,20)); d.text((10,68),'Pasta no Pinterest · Lindson Almeida Studio',font=I(20,400),fill=(100,100,100))
        for i,im in enumerate(ims): pr.paste(im.resize((tw,th),Image.LANCZOS),(10+i*(tw+10),110))
        pr.save(os.path.join(PR,slug+'.png'))
