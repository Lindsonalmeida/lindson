# Pins Pinterest v2 1000x1500 (conta Pedro, 16/11/2026). v1 reprovada ("ficou horrível").
# Regra v2: imagem manda, quase nenhum texto, legenda sóbria tipo portfólio de estúdio.
# P = Pentagram/Porto Rocha (uma aplicação em tela cheia, legenda pequena embaixo)
# K = Koto/Studio Dumbar (mosaico de aplicações com calha fina, sem título)
# M = Mucho (logo sozinho na cor da marca, muito respiro)
# S = DesignStudio (peça em palco neutro com sombra, legenda no topo)
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
H=os.path.dirname(os.path.abspath(__file__)); R=os.path.abspath(os.path.join(H,'../../../../..'))
F=lambda p:os.path.join(R,p)
INTER=os.path.join(H,'..','Inter.ttf')
def I(s,w=400):
    f=ImageFont.truetype(INTER,s)
    try: f.set_variation_by_axes([w])
    except Exception: pass
    return f
W,HH=1000,1500
def fit(im,w,h,ax=.5,ay=.5):
    im=im.convert('RGB'); r=max(w/im.width,h/im.height); im=im.resize((round(im.width*r)+1,round(im.height*r)+1),Image.LANCZOS)
    x=int((im.width-w)*ax); y=int((im.height-h)*ay); return im.crop((x,y,x+w,y+h))
def grain(c,a=.035):
    n=Image.effect_noise(c.size,48).convert('RGB'); return Image.blend(c,n,a)
def cap(c,cliente,tipo,dark=True,ia=False,top=False):
    d=ImageDraw.Draw(c); col=(245,243,238) if dark else (20,20,20); sub=(200,198,192) if dark else (90,90,90)
    if not top:
        g=Image.new('L',(1,260)); [g.putpixel((0,i),int(170*(i/259)**1.6)) for i in range(260)]
        if dark: c.paste((0,0,0),(0,HH-260,W,HH),g.resize((W,260)))
        y=HH-78
    else: y=46
    d.text((56,y),cliente,font=I(26,600),fill=col)
    d.text((56+d.textlength(cliente,font=I(26,600))+14,y),tipo,font=I(26,400),fill=sub)
    t='Lindson Almeida Studio'; d.text((W-56-d.textlength(t,font=I(22,500)),y+3),t,font=I(22,500),fill=sub)
    if ia: d.text((56,y-34 if not top else y+40),'mockup · imagem gerada por IA',font=I(17,400),fill=sub)
    return c
def P(src,cliente,tipo,ax=.5,ay=.5,ia=False,crop=None):
    im=Image.open(F(src))
    if crop: im=im.crop(crop)
    return cap(grain(fit(im,W,HH,ax,ay)),cliente,tipo,ia=ia)
def K(srcs,cliente,tipo,bg=(14,14,14),layout='a',ia=False):
    c=Image.new('RGB',(W,HH),bg); g=10
    if layout=='a': boxes=[(0,0,W,760),(0,760+g,495,HH),(495+g,760+g,W,HH)]
    elif layout=='b': boxes=[(0,0,495,740),(505,0,W,740),(0,750,W,HH)]
    else: boxes=[(0,0,495,495),(505,0,W,495),(0,505,495,1000),(505,505,W,1000),(0,1010,W,HH)]
    for s,b in zip(srcs,boxes):
        src,ax,ay=(s if isinstance(s,tuple) else (s,.5,.5))
        c.paste(fit(Image.open(F(src)),b[2]-b[0],b[3]-b[1],ax,ay),b[:2])
    return cap(grain(c,.025),cliente,tipo,ia=ia)
def M(logo,cliente,tipo,bg,dark=True,w=560,crop=None,bgimg=None):
    c=Image.new('RGB',(W,HH),bg)
    if bgimg: c=Image.blend(c,fit(Image.open(F(bgimg)),W,HH),.10)
    lg=Image.open(F(logo));
    if crop: lg=lg.crop(crop)
    if crop and lg.mode!='RGBA': c=Image.new('RGB',(W,HH),lg.convert('RGB').getpixel((3,3)))
    lg=lg.convert('RGBA'); r=w/lg.width; lg=lg.resize((w,int(lg.height*r)),Image.LANCZOS)
    if crop:
        m=Image.new('L',lg.size,0); ImageDraw.Draw(m).rectangle((40,30,lg.width-40,lg.height-30),fill=255); lg.putalpha(m.filter(ImageFilter.GaussianBlur(28)))
    c.paste(lg,((W-w)//2,(HH-lg.height)//2-40),lg)
    return cap(grain(c,.03),cliente,tipo,dark=dark,top=False) if dark else cap(grain(c,.02),cliente,tipo,dark=False)
def S(src,cliente,tipo,bg,dark=True,w=820,crop=None,ia=False,radius=0):
    c=Image.new('RGB',(W,HH),bg); im=Image.open(F(src)).convert('RGB')
    if crop: im=im.crop(crop)
    r=w/im.width; im=im.resize((w,int(im.height*r)),Image.LANCZOS)
    if im.height>1180: im=im.crop((0,0,w,1180))
    x=(W-w)//2; y=(HH-im.height)//2+20
    sh=Image.new('L',(W,HH),0); ImageDraw.Draw(sh).rounded_rectangle((x+10,y+30,x+w+10,y+im.height+40),radius+8,fill=150)
    sh=sh.filter(ImageFilter.GaussianBlur(38)); c.paste((0,0,0),(0,0),sh)
    m=Image.new('L',im.size,0); ImageDraw.Draw(m).rounded_rectangle((0,0,*im.size),radius,fill=255)
    c.paste(im,(x,y),m)
    return cap(grain(c,.025),cliente,tipo,dark=dark,top=True,ia=ia)
OI='agencia/operacao-propria/identidade/'; WF='agencia/clientes/wf-celulares/identidade/pecas-final/'
JF='agencia/clientes/jaci-cunha/conteudo-nov/feed/'; B='agencia/marca-lindson/projeto-designer/behance/'
OT,WFC,JC,LP,RT,PL,DB='Orégano Turbo','WF Celulares','Dra. Jaci Cunha','Leo Pinto','Real Time','Processo Legislativo','Dublê'
PINS=[
 ('01-oregano-fachada',lambda:P(OI+'fotos-ia/A10-fachada.jpg',OT,'Fachada',ia=True)),
 ('02-wf-post',lambda:P(WF+'10-post-produto.jpg',WFC,'Social media')),
 ('03-jaci-feed',lambda:K([(JF+'r03.jpg',.5,.3),JF+'r06.jpg',JF+'r10.jpg',JF+'r02.jpg',JF+'r12.jpg'],JC,'Instagram',bg=(43,7,13),layout='c')),
 ('04-oregano-avental',lambda:P(OI+'fotos-ia/A4-avental.jpg',OT,'Uniforme',ia=True)),
 ('05-realtime-logo',lambda:M(B+'real-time/05-modulo.jpg',RT,'Identidade visual',(12,13,16),w=860,crop=(260,230,1140,530))),
 ('06-leo-post',lambda:S('agencia/clientes/leo-pinto/instagram-v13-apresentacao/leo-v13-3-direita.jpg',LP,'Social media',(232,230,224),dark=False,w=800)),
 ('07-oregano-grid',lambda:K([OI+'fotos-ia/B2-caixa-ceu.jpg',(OI+'fotos-ia/B5-motoboy.jpg',.5,.3),OI+'fotos-ia/B7-moca-carro.jpg'],OT,'Campanha',layout='a',ia=True)),
 ('08-wf-logo',lambda:M('agencia/clientes/wf-celulares/identidade/logo-b/wf-logo-b-branca.png',WFC,'Logo',(8,8,9),w=440)),
 ('09-jaci-retrato',lambda:P(JF+'r09.jpg',JC,'Direção de arte',ay=.3)),
 ('10-duble-app',lambda:S('apps/clone-studio/identidade/tela-v2-celular.png',DB,'Identidade de app',(22,20,34),w=560,radius=56)),
 ('11-oregano-cartao',lambda:P(OI+'fotos-ia/A9-cartao-proposta.jpg',OT,'Papelaria',ia=True)),
 ('12-realtime-foto',lambda:P(B+'real-time/02-modulo.jpg',RT,'Rebranding',crop=(820,0,1400,900))),
 ('13-wf-fachada',lambda:S(WF+'13-fachada.jpg',WFC,'Fachada',(10,10,11),w=1000,crop=(330,0,1590,1080),ia=True)),
 ('14-legislativo-foto',lambda:P(B+'processo-legislativo/02-modulo.jpg',PL,'Identidade de curso',crop=(930,40,1400,900))),
 ('15-oregano-logo',lambda:M(OI+'kit-mockup/logo-horizontal-creme.png',OT,'Logo',(30,91,59),w=700)),
 ('16-jaci-destaques',lambda:K(['agencia/clientes/jaci-cunha/instagram-destaques/out/01-avaliacao-1.jpg','agencia/clientes/jaci-cunha/instagram-destaques/out/02-harmonizacao-1.jpg','agencia/clientes/jaci-cunha/instagram-destaques/out/03-odonto-1.jpg','agencia/clientes/jaci-cunha/instagram-destaques/out/01-avaliacao-2.jpg',(JF+'r05.jpg',.5,.35)],JC,'Destaques',bg=(43,7,13),layout='c')),
 ('17-leo-logo',lambda:M('agencia/clientes/leo-pinto/instagram-v12-feed/marca/logo_principal.png',LP,'Logo',(18,46,160),w=600)),
 ('18-oregano-sacola',lambda:P(OI+'fotos-ia/A8-adesivo-pedido-saindo.jpg',OT,'Embalagem',ia=True)),
 ('19-wf-cartao',lambda:S(WF+'14-cartao-etiqueta.jpg',WFC,'Papelaria',(10,10,11),w=1000,crop=(300,0,1620,1080),ia=True)),
 ('20-duble-logo',lambda:M('apps/clone-studio/identidade/previa.png',DB,'Logo',(14,13,22),w=820,crop=(0,0,735,240))),
 ('21-oregano-bone',lambda:P(OI+'fotos-ia/A6-bone.jpg',OT,'Brindes',ia=True)),
 ('22-realtime-mundo',lambda:S(B+'real-time/09-modulo.jpg',RT,'Aplicações',(16,17,20),w=860,crop=(900,150,1380,700))),
 ('23-legislativo-logo',lambda:M(B+'processo-legislativo/05-modulo.jpg',PL,'Logo',(18,40,30),w=760,crop=(290,200,1040,570))),
 ('24-oregano-mordida',lambda:P(OI+'fotos-ia/B1-mordida.jpg',OT,'Campanha',ia=True)),
]
if __name__=='__main__':
    import sys; o=os.path.join(H,'pins'); only=sys.argv[1] if len(sys.argv)>1 else ''
    for n,f in PINS:
        if only in n: f().save(os.path.join(o,n+'.jpg'),quality=90)
    ims=[Image.open(os.path.join(o,n+'.jpg')) for n,_ in PINS]; tw=250; th=375
    pr=Image.new('RGB',(tw*8+90,th*3+40),(232,230,226))
    for i,im in enumerate(ims): pr.paste(im.resize((tw,th)),(10+(i%8)*(tw+10),10+(i//8)*(th+10)))
    pr.save(os.path.join(H,'prancha.png'))
