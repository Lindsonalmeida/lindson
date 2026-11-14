import cv2,numpy as np,sys,subprocess
# Troca a logo gerada por IA no peito pela logo original, seguindo o peito
# com busca por modelo + suavização forte (sem tremer).
src,out=sys.argv[1],sys.argv[2]
logo=cv2.imread('/home/user/lindsonalmeida/grupossf/img/logo.jpg').astype(np.float32)
c=cv2.VideoCapture(src); fps=c.get(5); W=int(c.get(3)); H=int(c.get(4))
frames=[]
while True:
    ok,f=c.read()
    if not ok: break
    frames.append(f)
f0=frames[0]
# acha o círculo azul do peito: região do tronco
g=cv2.cvtColor(f0,cv2.COLOR_BGR2GRAY)
y1,y2=int(H*0.38),int(H*0.62); x1,x2=int(W*0.45),int(W*0.85)
circ=cv2.HoughCircles(cv2.medianBlur(g[y1:y2,x1:x2],5),cv2.HOUGH_GRADIENT,1,40,param1=90,param2=30,minRadius=int(W*0.025),maxRadius=int(W*0.07))
if circ is None: raise SystemExit('logo não encontrada')
# escolhe o círculo mais azul
best=None
for cx,cy,r in circ[0]:
    cx,cy,r=int(cx+x1),int(cy+y1),int(r)
    patch=f0[cy-r//2:cy+r//2,cx-r//2:cx+r//2]
    blue=(patch[...,0].astype(int)-patch[...,2].astype(int)).mean()
    if best is None or blue>best[3]: best=(cx,cy,r,blue)
cx,cy,r,_=best
T=cv2.cvtColor(f0[cy-r:cy+r,cx-r:cx+r],cv2.COLOR_BGR2GRAY)
pos=[(cx,cy)]
for f in frames[1:]:
    px,py=pos[-1]; m=int(r*1.2)
    sx,sy=max(0,px-r-m),max(0,py-r-m)
    win=cv2.cvtColor(f[sy:py+r+m,sx:px+r+m],cv2.COLOR_BGR2GRAY)
    res=cv2.matchTemplate(win,T,cv2.TM_CCOEFF_NORMED); _,mv,_,ml=cv2.minMaxLoc(res)
    pos.append((sx+ml[0]+r,sy+ml[1]+r) if mv>0.4 else (px,py))
P=np.array(pos,np.float32)
k=9; ker=np.ones(k)/k
Ps=np.stack([np.convolve(np.pad(P[:,i],(k//2,k//2),mode='edge'),ker,mode='valid') for i in range(2)],1)
tmp=out+'.tmp.mp4'; vw=cv2.VideoWriter(tmp,cv2.VideoWriter_fourcc(*'mp4v'),fps,(W,H))
d=2*r+16
a=np.zeros((d,d),np.float32); cv2.circle(a,(d//2,d//2),d//2-1,1.0,-1); a=cv2.GaussianBlur(a,(0,0),1.0)[...,None]
lgb=cv2.resize(logo,(d,d))
for f,(x,y) in zip(frames,Ps):
    x0,y0=int(round(x))-d//2,int(round(y))-d//2
    roi=f[y0:y0+d,x0:x0+d].astype(np.float32)
    sh=cv2.GaussianBlur(cv2.cvtColor(roi.astype(np.uint8),cv2.COLOR_BGR2GRAY).astype(np.float32),(0,0),d/6)
    sh=np.clip(sh/max(sh.mean(),1),0.85,1.12)[...,None]
    f[y0:y0+d,x0:x0+d]=np.clip(lgb*sh*a+roi*(1-a),0,255).astype(np.uint8)
    vw.write(f)
vw.release()
subprocess.run(['ffmpeg','-v','error','-y','-i',tmp,'-i',src,'-map','0:v','-map','1:a','-c:v','libx264','-crf','16','-preset','fast','-pix_fmt','yuv420p','-c:a','copy',out],check=True)
print('ok',src,'r=',r,'jitter_px=',float(np.abs(np.diff(Ps,axis=0)).max()))
