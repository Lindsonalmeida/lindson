# Pins Pinterest 1000x1500 (conta Pedro, 16/11/2026). Composições copiadas de:
# A = Koto (capa com imagem grande + bloco de título), B = Porto Rocha (tipografia gigante),
# C = Pentagram board (colagem de aplicações), D = Collins (full-bleed + tarja), E = Brand New (antes/depois em faixas).
import os, csv, random
from PIL import Image, ImageDraw, ImageFont, ImageFilter
H=os.path.dirname(os.path.abspath(__file__)); B=os.path.join(H,'..','behance')
Y=(245,197,24); K=(10,10,10); W=(245,245,240)
A=lambda s:ImageFont.truetype(os.path.join(H,'Anton-Regular.ttf'),s)
I=lambda s:ImageFont.truetype(os.path.join(H,'Inter.ttf'),s)
PORT='https://lindsonalmeida.pages.dev/site/portfolio/'
CASES={'leo-pinto':('LEO PINTO','Identidade visual','política local'),
 'oregano-turbo':('ORÉGANO TURBO','Marca para pizzaria','pizzaria'),
 'real-time':('REAL TIME','Rebranding','produtora audiovisual'),
 'wf-celulares':('WF CELULARES','Identidade visual','loja de iPhone'),
 'processo-legislativo':('PROCESSO LEGISLATIVO','Identidade de curso','curso online'),
 'duble':('DUBLÊ','Identidade de app','aplicativo de voz')}
TIT=[('IDENTIDADE','VISUAL'),('MARCA QUE','VENDE'),('BRAND','BOOK'),('ANTES DA','MARCA FORTE'),('SISTEMA','DE MARCA')]
def fit(im,w,h):
    r=max(w/im.width,h/im.height); im=im.resize((int(im.width*r)+1,int(im.height*r)+1),Image.LANCZOS)
    x=(im.width-w)//2; y=(im.height-h)//2; return im.crop((x,y,x+w,y+h))
def grain(c):
    n=Image.effect_noise(c.size,40).convert('RGB'); return Image.blend(c,n,0.05)
def head(d,l1,l2,x,y,size,c1=W,c2=Y):
    d.text((x,y),l1,font=A(size),fill=c1); d.text((x,y+int(size*1.05)),l2,font=A(size),fill=c2)
def sig(d,dark=True):
    c=Y if dark else K
    d.text((60,1420),'LINDSON ALMEIDA STUDIO',font=A(34),fill=c)
    d.text((620,1430),'SÃO LUÍS · MA',font=I(24),fill=(W if dark else K))
def tag(d,x,y,t,bg=Y,fg=K):
    f=I(26); w=d.textlength(t,font=f); d.rectangle((x,y,x+w+36,y+48),fill=bg); d.text((x+18,y+9),t,font=f,fill=fg)
def comp(k,mods,name,sub,t):
    c=Image.new('RGB',(1000,1500),K); d=ImageDraw.Draw(c)
    if k==0:  # A Koto
        c.paste(fit(mods[0],1000,563),(0,0)); c.paste(fit(mods[5],1000,563),(0,573)); tag(d,60,1080,sub.upper())
        head(d,t[0],t[1],60,1140,100); d.text((620,1150),name[:14],font=A(44),fill=W)
    elif k==1:  # B Porto Rocha, fundo amarelo, tipografia gigante + cartão com sombra dura
        c.paste(Y,(0,0,1000,1500)); d=ImageDraw.Draw(c)
        head(d,t[0],t[1],50,40,190,K,K)
        im=fit(mods[1],820,620); d.rectangle((110,560,950,1200),fill=K); c.paste(im,(90,540))
        d.text((60,1250),name,font=A(70),fill=K)
    elif k==2:  # C colagem
        c.paste(fit(mods[2],1000,560),(0,0)); c.paste(fit(mods[3],490,420),(0,570)); c.paste(fit(mods[4],500,420),(500,570))
        d.rectangle((0,1000,1000,1500),fill=K); tag(d,60,1030,'CASE · '+sub.upper())
        head(d,name if len(name)<14 else name.split()[0],t[1],60,1100,120)
    elif k==3:  # D full-bleed + tarja
        c.paste(fit(mods[3],1000,563),(0,150)); c.paste(fit(mods[6],1000,563),(0,713))
        ov=Image.new('L',(1000,1500)); od=ImageDraw.Draw(ov)
        for y in range(1500): od.line((0,y,1000,y),fill=int(min(1,max(0,(y-1000)/250))*235))
        c=Image.composite(Image.new('RGB',c.size,K),c,ov); d=ImageDraw.Draw(c)
        d.text((60,980),t[0],font=A(130),fill=W); f=A(130); w=d.textlength(t[1],font=f)
        d.rectangle((50,1125,80+w,1270),fill=Y); d.text((65,1120),t[1],font=f,fill=K)
        d.text((60,60),name,font=A(60),fill=Y)
    else:  # E antes/depois em faixas
        d.text((60,50),'DO ZERO AO',font=A(120),fill=W); d.text((60,180),'SISTEMA',font=A(120),fill=Y)
        c.paste(fit(mods[4],1000,480),(0,350)); c.paste(fit(mods[0],1000,480),(0,860))
        tag(d,40,370,'01 · CONCEITO'); tag(d,40,880,'02 · APLICAÇÃO'); d.text((60,1350),name,font=A(50),fill=W)
    sig(d, k!=1); return grain(c)
rows=[];n=0
for slug,(name,sub,nicho) in CASES.items():
    fs=[f for f in sorted(os.listdir(os.path.join(B,slug))) if f[:2] in('01','02','03','04','05','06','07','08','09')]
    mods=[Image.open(os.path.join(B,slug,f)).convert('RGB') for f in fs]
    for k in range(5):
        n+=1; m=mods[k:]+mods[:k]; t=TIT[(k+(n-1)//5)%5]
        fn=f'{n:02d}-{slug}-{k+1}.jpg'; comp(k,m,name,sub,t).save(os.path.join(H,'pins',fn),quality=90)
        title=[f'{sub} {name.title()} | identidade visual para {nicho}',f'Brand book e manual de marca: case {name.title()}',
               f'Ideias de logo e paleta de cores para {nicho}',f'Antes e depois de marca: {name.title()}',f'Sistema visual completo para {nicho} | Lindson Almeida Studio'][k][:100]
        desc=(f'Case {name.title()}: {sub.lower()} criada pelo Lindson Almeida Studio, estúdio de design em São Luís (MA). '
              f'Logo, paleta de cores, tipografia, brand book e aplicações reais para {nicho}. Inspiração de identidade visual e branding brasileiro. Veja o portfólio completo.')[:500]
        rows.append([title,os.path.join('pins',fn),'Cases de identidade visual' if k<3 else ['Antes e depois de marcas','Brand book e manual de marca'][k-3],desc,PORT,
                     f'identidade visual, branding, logo, {nicho}, design gráfico'])
with open(os.path.join(H,'PINS.csv'),'w',newline='') as f:
    w=csv.writer(f); w.writerow(['Title','Media URL','Pinterest board','Description','Link','Keywords']); w.writerows(rows)
# prancha
ims=[Image.open(os.path.join(H,r[1])).resize((200,300)) for r in rows]
p=Image.new('RGB',(10*200+11*10,3*300+4*10),K)
for i,im in enumerate(ims): p.paste(im,(10+(i%10)*210,10+(i//10)*310))
p.save(os.path.join(H,'prancha.jpg'),quality=88)
