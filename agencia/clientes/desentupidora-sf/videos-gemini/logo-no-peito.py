import cv2,numpy as np,sys,subprocess
src,out,x,y,w,h=sys.argv[1],sys.argv[2],*map(int,sys.argv[3:7])
logo=cv2.imread('/home/user/lindsonalmeida/grupossf/img/logo.jpg')
c=cv2.VideoCapture(src); fps=c.get(5); W=int(c.get(3)); H=int(c.get(4))
tmp=out+'.tmp.mp4'; vw=cv2.VideoWriter(tmp,cv2.VideoWriter_fourcc(*'mp4v'),fps,(W,H))
ok,f=c.read(); tr=cv2.TrackerCSRT_create(); tr.init(f,(x,y,w,h)); box=(x,y,w,h); lost=0
while ok:
    g,b=tr.update(f)
    if g: box=b
    bx,by,bw,bh=[int(v) for v in box]
    hsv=cv2.cvtColor(f[max(0,by):by+bh,max(0,bx):bx+bw],cv2.COLOR_BGR2HSV) if bw>0 and bh>0 else None
    orange=((hsv[...,0]>=5)&(hsv[...,0]<=25)&(hsv[...,1]>110)).mean() if hsv is not None and hsv.size else 0
    if not g or orange<0.15:
        vw.write(f); ok,f=c.read(); continue
    cx,cy=bx+bw//2,by+bh//2; d=int(max(bw,bh)*0.95)
    # tinge patch: cobre o logo da IA com o laranja do peito
    ring=f[max(0,by-12):by-2, bx:bx+bw].reshape(-1,3)
    col=np.median(ring,0) if len(ring) else np.array([0,120,240])
    pad=6; cv2.rectangle(f,(bx-pad,by-pad),(bx+bw+pad,by+bh+pad),col.tolist(),-1)
    f[max(0,by-pad-8):by+bh+pad+8, max(0,bx-pad-8):bx+bw+pad+8]=cv2.GaussianBlur(f[max(0,by-pad-8):by+bh+pad+8, max(0,bx-pad-8):bx+bw+pad+8],(9,9),0)
    lg=cv2.resize(logo,(d,d)); m=np.zeros((d,d),np.float32); cv2.circle(m,(d//2,d//2),d//2-1,1.0,-1); m=cv2.GaussianBlur(m,(5,5),0)[...,None]
    x0,y0=cx-d//2,cy-d//2
    if 0<=x0 and 0<=y0 and x0+d<=W and y0+d<=H:
        roi=f[y0:y0+d,x0:x0+d].astype(np.float32)
        f[y0:y0+d,x0:x0+d]=(lg*m*0.97+roi*(1-m*0.97)).astype(np.uint8)
    vw.write(f); ok,f=c.read()
vw.release()
subprocess.run(['ffmpeg','-v','error','-y','-i',tmp,'-i',src,'-map','0:v','-map','1:a?','-c:v','libx264','-crf','17','-preset','fast','-pix_fmt','yuv420p','-c:a','copy',out],check=True)
