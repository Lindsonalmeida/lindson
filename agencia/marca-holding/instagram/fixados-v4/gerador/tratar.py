# Tratamento de cor da foto herói na paleta Barzakh (oliva + ouro), grão fino. Uso: tratar.py entrada saida cx cy escala
import sys, numpy as np
from PIL import Image, ImageFilter
src,out=sys.argv[1],sys.argv[2]; cx,cy,zoom=float(sys.argv[3]),float(sys.argv[4]),float(sys.argv[5])
im=Image.open(src).convert('RGB'); W,H=im.size
cw=W/zoom; ch=cw*1440/3240
if ch>H: ch=H; cw=ch*3240/1440
x0=min(max(cx*W-cw/2,0),W-cw); y0=min(max(cy*H-ch/2,0),H-ch)
print('ampliacao', round(3240/cw,3))
im=im.crop((int(x0),int(y0),int(x0+cw),int(y0+ch))).resize((3240,1440),Image.LANCZOS)
a=np.asarray(im).astype(np.float32)/255
L=(0.3*a[...,0]+0.59*a[...,1]+0.11*a[...,2])
# mapa de tons: obsidiana -> oliva -> ouro -> marfim
stops=np.array([[0,14,15,18],[0.30,58,48,30],[0.55,110,88,52],[0.80,207,174,116],[1,246,236,214]],np.float32)
g=np.stack([np.interp(L,stops[:,0],stops[:,i]) for i in (1,2,3)],-1)/255
r=0.82*g+0.18*a*np.array([1.0,0.92,0.75])
# vinheta suave
yy,xx=np.mgrid[0:1440,0:3240]; v=1-0.38*(((xx-1620)/1900)**2+((yy-700)/1100)**2); r*=np.clip(v,0.55,1)[...,None]
r+=np.random.default_rng(7).normal(0,0.022,(1440,3240,1)).astype(np.float32)
Image.fromarray((np.clip(r,0,1)*255).astype(np.uint8)).save(out,quality=94)
