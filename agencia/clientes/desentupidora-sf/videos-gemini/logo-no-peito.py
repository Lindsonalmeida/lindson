import cv2,numpy as np,sys,subprocess
src,out,x,y,w,h=sys.argv[1],sys.argv[2],*map(int,sys.argv[3:7])
logo=cv2.imread('/home/user/lindsonalmeida/grupossf/img/logo.jpg').astype(np.float32)
c=cv2.VideoCapture(src); fps=c.get(5); W=int(c.get(3)); H=int(c.get(4))
tmp=out+'.tmp.mp4'; vw=cv2.VideoWriter(tmp,cv2.VideoWriter_fourcc(*'mp4v'),fps,(W,H))
ok,f=c.read(); tr=cv2.TrackerCSRT_create(); tr.init(f,(x,y,w,h)); box=(x,y,w,h)
while ok:
    g,b=tr.update(f)
    if g: box=b
    bx,by,bw,bh=[int(v) for v in box]
    reg=f[max(0,by):by+bh,max(0,bx):bx+bw]
    hsv=cv2.cvtColor(reg,cv2.COLOR_BGR2HSV) if reg.size else None
    orange=((hsv[...,0]>=5)&(hsv[...,0]<=25)&(hsv[...,1]>110)).mean() if hsv is not None else 0
    if g and orange>=0.15:
        # 1) apaga o logo da IA com inpaint suave
        m=np.zeros((H,W),np.uint8); cv2.rectangle(m,(bx-4,by-4),(bx+bw+4,by+bh+4),255,-1)
        x0,y0,x1,y1=max(0,bx-40),max(0,by-40),min(W,bx+bw+40),min(H,by+bh+40)
        f[y0:y1,x0:x1]=cv2.inpaint(f[y0:y1,x0:x1],m[y0:y1,x0:x1],9,cv2.INPAINT_TELEA)
        # 2) logo redondo com a luz do tecido
        d=int(bh*0.95); d=max(40,min(d,int(bw*0.9)))
        cx,cy=bx+bw//2,by+bh//2; lx,ly=cx-d//2,cy-d//2
        if lx>=0 and ly>=0 and lx+d<=W and ly+d<=H:
            roi=f[ly:ly+d,lx:lx+d].astype(np.float32)
            gray=cv2.GaussianBlur(cv2.cvtColor(roi.astype(np.uint8),cv2.COLOR_BGR2GRAY).astype(np.float32),(0,0),d/8)
            shade=np.clip(gray/max(gray.mean(),1),0.75,1.2)[...,None]
            lg=cv2.resize(logo,(d,d))*shade
            a=np.zeros((d,d),np.float32); cv2.circle(a,(d//2,d//2),d//2-2,1.0,-1); a=cv2.GaussianBlur(a,(0,0),1.2)[...,None]*0.95
            f[ly:ly+d,lx:lx+d]=np.clip(lg*a+roi*(1-a),0,255).astype(np.uint8)
    vw.write(f); ok,f=c.read()
vw.release()
subprocess.run(['ffmpeg','-v','error','-y','-i',tmp,'-i',src,'-map','0:v','-map','1:a?','-c:v','libx264','-crf','16','-preset','fast','-pix_fmt','yuv420p','-r','24','-c:a','copy',out],check=True)
