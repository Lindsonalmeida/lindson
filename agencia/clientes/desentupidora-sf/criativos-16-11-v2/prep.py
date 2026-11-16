# Pós-produção das fotos (conta Pedro 16/11): recorte BiRefNet, rim light, color grading navy/laranja, grão.
import numpy as np, cv2, subprocess, sys
from PIL import Image
D='fotos/'
def grade(a, sh=(6,26,74), hi=(255,190,120), amt=.35):
    a=a.astype(np.float32)/255; L=a.mean(2,keepdims=True)
    tint=np.array(sh)/255*(1-L)+np.array(hi)/255*L
    out=a*(1-amt)+ (a*tint*1.6)*amt
    out=np.clip((out-.5)*1.12+.5,0,1)  # contraste
    return (out*255).astype(np.uint8)
def grain(a,s=7):
    n=np.random.normal(0,s,a.shape[:2])[...,None]; return np.clip(a.astype(np.float32)+n,0,255).astype(np.uint8)
# t1: técnico recortado + rim light laranja à direita e azul céu à esquerda
subprocess.run([sys.executable,'/home/user/lindson/agencia/marca-lindson/ferramentas/recorte2.py',D+'t1b.webp',D+'t1-cut.png'],check=True)
im=np.asarray(Image.open(D+'t1-cut.png').convert('RGBA')).copy()
rgb=grade(im[...,:3],amt=.25); a=im[...,3].astype(np.float32)/255
inner=a-cv2.GaussianBlur(a,(0,0),9)  # borda interna
for dx,col in ((14,(255,138,0)),(-14,(63,169,255))):
    sh=np.roll(a,dx,1); rim=np.clip(a-sh,0,1); rim=cv2.GaussianBlur(rim,(0,0),5)*a
    rgb=np.clip(rgb.astype(np.float32)+rim[...,None]*np.array(col)*1.3,0,255).astype(np.uint8)
Image.fromarray(np.dstack([grain(rgb,5),im[...,3]]),'RGBA').save(D+'t1-final.png')
# t2, t3: grading + grão + vinheta
for n in ('t2','t3'):
    x=np.asarray(Image.open(D+n+'.webp').convert('RGB')); x=grade(x,amt=.4)
    h,w=x.shape[:2]; Y,X=np.ogrid[:h,:w]; v=1-.55*(((X-w/2)/(w/1.3))**2+((Y-h/2)/(h/1.3))**2)
    x=(x*np.clip(v,0,1)[...,None]).astype(np.uint8); Image.fromarray(grain(x,6)).save(D+n+'-final.jpg',quality=94)
# grão para sobrepor no HTML
g=np.clip(128+np.random.normal(0,40,(512,512)),0,255).astype(np.uint8); Image.fromarray(g).save(D+'grao.png')
