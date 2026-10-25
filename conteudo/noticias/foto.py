"""Prepara a foto da notícia: python3 -I foto.py <entrada.jpg> <saida.jpg>
Recorta bordas pretas, melhora nitidez/cor, detecta rostos e imprime o foco em JSON {"x":..,"y":..,"rostos":n,"ok":bool,"motivo":..}."""
import sys,json,numpy as np,cv2
from PIL import Image,ImageEnhance,ImageOps
im=Image.open(sys.argv[1]).convert('RGB')
# corta faixas pretas/brancas das bordas (letterbox)
a=np.asarray(im).astype(int);g=a.mean(2)
rows=np.where(g.std(1)>6)[0];cols=np.where(g.std(0)>6)[0]
if len(rows) and len(cols):im=im.crop((cols[0],rows[0],cols[-1]+1,rows[-1]+1))
ok=True;motivo=''
if im.width<700:ok=False;motivo='pequena'
arr=np.asarray(im.convert('L'))
if cv2.Laplacian(arr,cv2.CV_64F).var()<30:ok=False;motivo='borrada'
if arr.std()<25:ok=False;motivo='sem contraste (logo/grafico?)'
im=ImageEnhance.Sharpness(im).enhance(1.15);im=ImageEnhance.Contrast(im).enhance(1.05);im=ImageEnhance.Color(im).enhance(1.08)
im.thumbnail((1600,1600))
g=cv2.cvtColor(np.asarray(im),cv2.COLOR_RGB2GRAY);H,W=g.shape
import os
M=os.environ.get('YUNET',os.path.join(os.path.dirname(os.path.abspath(__file__)),'modelo','yunet.onnx'))
fs=[]
try:
    det=cv2.FaceDetectorYN.create(M,'',(W,H),0.75,0.3,5000)
    _,res=det.detect(cv2.cvtColor(np.asarray(im),cv2.COLOR_RGB2BGR))
    if res is not None:fs=[tuple(int(v) for v in r[:4]) for r in res]
except Exception as e:print('aviso rosto:',e,file=sys.stderr)
if fs:
    x0=min(f[0] for f in fs);y0=min(f[1] for f in fs);x1=max(f[0]+f[2] for f in fs);y1=max(f[1]+f[3] for f in fs)
    if (x1-x0)>H*0.8*0.85:  # rostos não cabem juntos no corte 4:5: foca o maior
        b=max(fs,key=lambda f:f[2]*f[3]);x0,y0,x1,y1=b[0],b[1],b[0]+b[2],b[1]+b[3]
    foco={'x':round((x0+x1)/2/W,3),'y':round(((y0+y1)/2)/H,3)}
else:foco={'x':.5,'y':.4}
im.save(sys.argv[2],quality=88)
print(json.dumps({**foco,'rostos':len(fs),'ok':ok,'motivo':motivo,'w':im.width,'h':im.height}))
