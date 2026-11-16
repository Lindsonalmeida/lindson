# Hero shot por código (estilo "Advantage+ background" da Meta): produto recortado sobre
# mesa de set escura, luz de produto recortada, contra-luz azul da marca, sombra de contato e reflexo.
# Uso: python3 cena.py <recorte.png> <saida.png> <W> <H> <cena: mesa|concreto|azul> <altura_produto> <y_base>
# Conta Zuleide, 16/11/2026.
import sys, numpy as np
from PIL import Image, ImageFilter, ImageEnhance
src,out,W,H,cena,ph,yb=sys.argv[1],sys.argv[2],int(sys.argv[3]),int(sys.argv[4]),sys.argv[5],int(sys.argv[6]),int(sys.argv[7])
rng=np.random.default_rng(7)
yy,xx=np.mgrid[0:H,0:W].astype(np.float32)
hz=yb-int(ph*0.10)  # linha do horizonte da mesa um pouco acima da base
# parede de fundo: escura com spot suave
cx=W/2
if cena=='azul': cor_fundo=np.array([14,26,48]); cor_spot=np.array([46,155,255])
elif cena=='concreto': cor_fundo=np.array([22,21,20]); cor_spot=np.array([120,112,100])
else: cor_fundo=np.array([12,12,13]); cor_spot=np.array([70,90,130])
d=np.sqrt(((xx-cx)/(W*0.42))**2+((yy-(hz-ph*0.45))/(ph*0.9))**2)
spot=np.clip(1-d,0,1)**1.6
img=cor_fundo[None,None,:]*(0.55+0.45*(yy/H))[...,None]+cor_spot[None,None,:]*spot[...,None]*0.75
# mesa
mesa=yy>=hz
t=np.clip((yy-hz)/(H-hz+1),0,1)
if cena=='concreto':
    n=rng.normal(0,1,(H//4+1,W//4+1)).astype(np.float32)
    n=np.array(Image.fromarray(((n*30)+128).clip(0,255).astype(np.uint8)).resize((W,H),Image.BICUBIC).filter(ImageFilter.GaussianBlur(1.2)),np.float32)-128
    base=np.array([46,44,42])
else:
    n=np.zeros((H,W),np.float32); base=np.array([18,18,20])
dm=np.sqrt(((xx-cx)/(W*0.55))**2+((yy-yb)/(ph*0.55))**2)
luzmesa=np.clip(1-dm,0,1)**1.5
mesa_rgb=base[None,None,:]*(1-0.6*t)[...,None]+n[...,None]*0.35+luzmesa[...,None]*np.array([60,62,66])
img=np.where(mesa[...,None],mesa_rgb,img)
# filete de luz na borda da mesa
edge=np.exp(-((yy-hz)/2.2)**2)*np.clip(1-np.abs(xx-cx)/(W*0.5),0,1)
img+=edge[...,None]*np.array([90,110,140])*0.6
fundo=Image.fromarray(img.clip(0,255).astype(np.uint8))
# produto
p=Image.open(src).convert('RGBA'); bb=p.getbbox(); p=p.crop(bb)
pw=int(p.width*ph/p.height); p=p.resize((pw,ph),Image.LANCZOS)
p=ImageEnhance.Contrast(p).enhance(1.06)
x0=int(cx-pw/2); y0=yb-ph
# reflexo (piso brilhante, exceto concreto = fosco e curto)
ref=p.transpose(Image.FLIP_TOP_BOTTOM)
a=np.array(ref.split()[3],np.float32)
k=0.30 if cena!='concreto' else 0.12
grad=np.clip(1-np.arange(ref.height)/(ref.height*(0.45 if cena!='concreto' else 0.2)),0,1)[:,None]
ref.putalpha(Image.fromarray((a*grad*k).astype(np.uint8)))
ref=ref.filter(ImageFilter.GaussianBlur(3 if cena!='concreto' else 6))
fundo=fundo.convert('RGBA'); fundo.alpha_composite(ref,(x0,yb-2))
# sombra de contato (elipse escura e curta) + sombra ambiente
sh=Image.new('L',(W,H),0); s=np.zeros((H,W),np.float32)
e=((xx-cx)/(pw*0.42))**2+((yy-(yb-4))/(ph*0.025))**2; s+=np.clip(1-e,0,1)*230
e2=((xx-cx)/(pw*0.62))**2+((yy-(yb+6))/(ph*0.07))**2; s+=np.clip(1-e2,0,1)**2*140
sh=Image.fromarray(s.clip(0,255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(10))
preto=Image.new('RGBA',(W,H),(0,0,0,255)); preto.putalpha(sh); fundo.alpha_composite(preto)
# contra-luz (rim) na silhueta
al=p.split()[3]; P=60
alp=Image.new('L',(pw+2*P,ph+2*P),0); alp.paste(al,(P,P))
glow=Image.new('RGBA',alp.size,(46,155,255,0) if cena!='concreto' else (255,225,190,0))
gm=alp.filter(ImageFilter.GaussianBlur(26)); glow.putalpha(gm.point(lambda v:int(v*0.30)))
G=Image.new('RGBA',(W,H),(0,0,0,0)); G.alpha_composite(glow,(x0-P,y0-P-8)); fundo=Image.alpha_composite(fundo,G)
pass
# luz de produto recortada: leve brilho de cima na metade superior do produto
L=np.zeros((H,W),np.float32); L+=np.clip(1-np.abs(yy-(y0+ph*0.15))/(ph*0.5),0,1)*np.clip(1-np.abs(xx-(cx-pw*0.15))/(pw*0.7),0,1)
L=Image.fromarray((L*28).astype(np.uint8)); br=Image.new('RGBA',(W,H),(255,255,255,0)); br.putalpha(Image.fromarray(np.minimum(np.array(L),np.array(al.point(lambda v:255) if False else L)))) 
mask=Image.new('L',(W,H),0); mask.paste(al,(x0,y0)); br.putalpha(Image.fromarray((np.array(L,np.float32)*np.array(mask,np.float32)/255).astype(np.uint8)))
pass
# vinheta + grão
f=np.array(fundo.convert('RGB'),np.float32)
v=np.clip(1-0.55*(((xx-cx)/(W*0.75))**2+((yy-H/2)/(H*0.75))**2),0.35,1)
f*=v[...,None]; f+=rng.normal(0,5,(H,W,1))
Image.fromarray(f.clip(0,255).astype(np.uint8)).save(out)
