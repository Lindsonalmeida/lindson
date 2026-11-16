# Recorte por chroma key das fotos reais da RT (fundo verde do estúdio). conta Leandro 16/11/2026.
import numpy as np,glob,os,json
from PIL import Image,ImageFilter
out={}
for f in sorted(glob.glob('../instagram-v3/fotos/rt-*.jpg')):
  im=np.asarray(Image.open(f).convert('RGB')).astype(float);r,g,b=im[...,0],im[...,1],im[...,2]
  k=g-np.maximum(r,b)
  verde=(k>28)&(g>70)
  frac=verde.mean();nome=os.path.basename(f)[:-4]
  if frac<.25: out[nome]=0;continue
  a=np.clip(1-(k-12)/30,0,1);a[g<50]=1
  # despill
  g2=np.minimum(g,np.maximum(r,b)*1.02);im[...,1]=g2
  A=Image.fromarray((a*255).astype('uint8')).filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(1))
  o=Image.fromarray(im.astype('uint8')).convert('RGBA');o.putalpha(A)
  bb=o.getbbox();o=o.crop(bb);o.save(f'recortes/{nome}.png');out[nome]=1
json.dump(out,open('recortes.json','w'))
print(out)
