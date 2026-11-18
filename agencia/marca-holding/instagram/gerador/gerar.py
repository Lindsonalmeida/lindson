from PIL import Image,ImageDraw,ImageFont,ImageFilter
import os
R='/home/user/lindson/agencia/'
AN=R+'marca-lindson/projeto-designer/pinterest/Anton-Regular.ttf'
FR=R+'marca-holding/v2/fase3/site/f/fraunces-sb.ttf'
FI=R+'marca-holding/v2/fase3/site/f/fraunces-it.ttf'
MO=R+'marca-holding/v2/fase2/site-bio/f/mono.ttf'
F=lambda p,s:ImageFont.truetype(p,s)
OURO=(201,162,90);PRETO=(12,12,14)
H=[("CASES","01",(43,58,143)),("PROCESSO","02",(46,125,80)),("PACOTES","03",(201,162,90)),("BASTIDOR","04",(214,96,60)),("DÚVIDAS","05",(124,92,214)),("CONTATO","06",(40,150,170))]
def icone(d,cx,cy,r,cor):
    # arco (portal) + monolito: a passagem
    d.arc([cx-r,cy-r,cx+r,cy+r],180,360,fill=OURO,width=max(4,r//14))
    d.line([cx-r,cy,cx-r,cy+r*1.1],fill=OURO,width=max(4,r//14));d.line([cx+r,cy,cx+r,cy+r*1.1],fill=OURO,width=max(4,r//14))
    d.rectangle([cx-r*.16,cy-r*.45,cx+r*.16,cy+r*1.1],fill=OURO)
    d.line([cx-r*1.35,cy+r*1.1,cx+r*1.35,cy+r*1.1],fill=OURO,width=max(3,r//20))
def glow(img,cx,cy,rad,cor):
    g=Image.new('RGB',img.size,PRETO);ImageDraw.Draw(g).ellipse([cx-rad,cy-rad,cx+rad,cy+rad],fill=cor)
    g=g.filter(ImageFilter.GaussianBlur(rad*.6));return Image.blend(img,g,.55)
os.makedirs('capas',exist_ok=True)
circ=[]
for nome,n,cor in H:
    im=Image.new('RGB',(1080,1920),PRETO);im=glow(im,540,900,380,cor);d=ImageDraw.Draw(im)
    icone(d,540,880,170,cor)
    f=F(AN,120);w=d.textlength(nome,font=f);d.text((540-w/2,1180),nome,font=f,fill=(245,240,230))
    m=F(MO,30);t=f"{n} · BARZAKH";w=d.textlength(t,font=m);d.text((540-w/2,1340),t,font=m,fill=OURO)
    m2=F(MO,26);t="UM ESTÚDIO AL KÁNTARA";w=d.textlength(t,font=m2);d.text((540-w/2,1780),t,font=m2,fill=(150,140,120))
    im.save(f'capas/destaque-{n}-{nome.lower().replace("ú","u")}-1080x1920.jpg',quality=92)
    c=Image.new('RGB',(1080,1080),PRETO);c=glow(c,540,540,420,cor);dc=ImageDraw.Draw(c);icone(dc,540,500,230,cor)
    mask=Image.new('L',(1080,1080),0);ImageDraw.Draw(mask).ellipse([0,0,1079,1079],fill=255)
    out=Image.new('RGBA',(1080,1080));out.paste(c,(0,0),mask);out.save(f'capas/destaque-{n}-circulo.png');circ.append((nome,c))
# previa
P=R+'marca-lindson/projeto-designer/v3/feed-v3/posts/'
ordem=['12','11','10','09','08','07','06','05','04','03','02','01']  # mais novo primeiro
W=1080;cell=W//3;top=900
im=Image.new('RGB',(W,top+cell*4+40),(0,0,0));d=ImageDraw.Draw(im)
d.text((60,40),"barzakhstudio",font=F(FR,44),fill=(245,240,230))
av=Image.new('RGB',(220,220),PRETO);icone(ImageDraw.Draw(av),110,95,60,OURO)
m=Image.new('L',(220,220),0);ImageDraw.Draw(m).ellipse([0,0,219,219],fill=255);im.paste(av,(60,130),m)
d.ellipse([54,124,286,356],outline=OURO,width=5)
for i,(a,b) in enumerate([("12","publicações"),("—","seguidores"),("—","seguindo")]):
    x=380+i*230;d.text((x,190),a,font=F(FR,46),fill='white');d.text((x,250),b,font=F(MO,24),fill=(190,190,190))
bio=["Barzakh · Identidade visual e branding","A passagem da sua marca. Um estúdio Al Kántara.","Direção criativa: Lindson Almeida · São Luís, MA","Cases reais de marca, embalagem e site ↓","↓ Fale com o estúdio no WhatsApp","lindsonalmeida.pages.dev/site/identidade"]
for i,t in enumerate(bio):d.text((60,390+i*44),t,font=F(FR if i==0 else MO,34 if i==0 else 26),fill=(140,170,255) if i==5 else ((245,240,230) if i==0 else (210,205,195)))
for i,(nome,c) in enumerate(circ):
    x=40+i*172;cc=c.resize((140,140));mm=Image.new('L',(140,140),0);ImageDraw.Draw(mm).ellipse([0,0,139,139],fill=255)
    im.paste(cc,(x,690),mm);d.ellipse([x-5,685,x+145,835],outline=(80,80,80),width=3)
    f=F(MO,20);w=d.textlength(nome.title(),font=f);d.text((x+70-w/2,845),nome.title(),font=f,fill='white')
for k,n in enumerate(ordem):
    p=Image.open(P+n+'.jpg').convert('RGB');pw,ph=p.size;s=min(pw,ph);p=p.crop(((pw-s)//2,(ph-s)//2,(pw+s)//2,(ph+s)//2)).resize((cell-4,cell-4))
    im.paste(p,((k%3)*cell+2,top+(k//3)*cell+2))
im.save('previa.jpg',quality=90)
# refs-3
fs=['pesquisa/01-pentagram-uk.jpg','pesquisa/03-portorocha-us-br.jpg','pesquisa/09-manual-us.jpg']
r=Image.new('RGB',(2160,620),PRETO)
for i,f in enumerate(fs):r.paste(Image.open(f).resize((700,535)),(20+i*713,20))
dr=ImageDraw.Draw(r)
for i,t in enumerate(["PENTAGRAM · UK · cartaz editorial cheio","PORTO ROCHA · US/BR · case em cor chapada","MANUAL · US · serifa grande + cor viva"]):dr.text((20+i*713,570),t,font=F(MO,24),fill=OURO)
r.save('refs-3.jpg',quality=88)
