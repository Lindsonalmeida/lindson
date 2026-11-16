# Recorte do busto (feed v2 Barzakh, conta Leandro 16/11/2026). isnet + filtro guiado + descontaminação (base recorte2.py).
import sys, numpy as np, cv2
from PIL import Image
from rembg import remove, new_session
from pymatting import estimate_foreground_ml
ses = new_session('isnet-general-use')
SRC='/home/user/centrallindsonalmeida/membros/img/'
for n in sys.argv[1:]:
    im = Image.open(SRC+n+'.jpg').convert('RGB'); w,h=im.size; im=im.crop((0,0,w,int(h*.62)))
    m = np.asarray(remove(im, session=ses, only_mask=True)).astype(np.float32)/255
    I = np.asarray(im).astype(np.float32)/255
    g = cv2.ximgproc.guidedFilter(guide=(I*255).astype(np.uint8), src=(m*255).astype(np.uint8), radius=3, eps=60).astype(np.float32)/255
    a = np.clip((g-.12)/.76,0,1)
    nl,lab,st,_=cv2.connectedComponentsWithStats((a>.5).astype(np.uint8)); k=1+np.argmax(st[1:,cv2.CC_STAT_AREA])
    a=a*cv2.dilate((lab==k).astype(np.uint8),np.ones((9,9),np.uint8)); a=a*a*(3-2*a); a=cv2.GaussianBlur(a,(0,0),.6); a[a<.03]=0
    F=np.clip(estimate_foreground_ml(I.astype(np.float64),a.astype(np.float64)),0,1)
    out=Image.fromarray((np.dstack([F,a])*255+.5).astype(np.uint8),'RGBA'); out=out.crop(out.getbbox())
    out.save(f'rec/{n}.png'); print(n,out.size,flush=True)
