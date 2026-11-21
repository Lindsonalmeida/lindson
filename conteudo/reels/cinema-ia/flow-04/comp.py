import json,subprocess,numpy as np,cv2,os,sys
from PIL import Image,ImageDraw,ImageFont,ImageFilter
FPS=30;Wd,Hd=1080,1920
S=json.load(open('shots.json'));W=json.load(open('w2.json'))
T=S[-1][1]; N=int(round(T*FPS))
ANTON='../wt-cinema/conteudo/reels/cinema-ia/motor/Anton.ttf'
fx={}
def font(sz):
    if sz not in fx: fx[sz]=ImageFont.truetype(ANTON,sz)
    return fx[sz]
fi=ImageFont.truetype('/usr/share/fonts/opentype/inter/Inter-Bold.otf',26)
# correções de legenda
fix={'por':'pro','a':None}
words=[]
for i,(w,a,b) in enumerate(W):
    t=w
    if t=='por' and W[i+1][0].startswith('concorrente'): t='pro'
    if t=='a' and i+1<len(W) and W[i+1][0]=='site' and W[i-1][0].lower()=='comenta': continue
    if t.lower().startswith('site') and W[i-1][0].lower() in('comenta','a'): t='SITE'
    words.append([t,a,b])
def tw(k):
    for w,a,b in words:
        if k in w.lower(): return a
TIT=[(0,'TE PROCURAM NO','GOOGLE',2.1,(60,235,255)),
 (6.42,'ERRO 1 · PERFIL PELA','METADE',7.66,(255,205,40)),
 (12.0,'PERFIL COMPLETO =','2,7×',[a for w,a,b in words if w.startswith('2,7')][0],(255,205,40)),
 (17.66,'ERRO 2 · AVALIAÇÃO SEM','RESPOSTA',18.94,(255,205,40)),
 (23.26,'ERRO 3 · ENDEREÇO','ERRADO',25.1,(255,60,50)),
 (27.84,'HOJE MESMO','COMPLETE',30.26,(255,205,40)),
 (32.84,'COMENTA','SITE',33.36,(60,235,255)),
 (36.0,'SEU CLIENTE','TE ACHA?',38.82,(255,205,40))]
TIT=[t+((TIT[i+1][0] if i+1<len(TIT) else T),) for i,t in enumerate(TIT)]
# grupos de legenda (até 3 palavras, quebra em pontuação)
grp=[];cur=[]
for w in words:
    cur.append(w)
    if len(cur)==3 or w[0][-1] in ',.?' : grp.append(cur);cur=[]
if cur: grp.append(cur)
def ease(x): x=min(max(x,0),1); return 1-(1-x)**3
def neon_layer(txt,sz,col,a):
    f=font(sz); bb=f.getbbox(txt); w=bb[2]+40; h=bb[3]+60
    L=Image.new('RGBA',(w+80,h+80),(0,0,0,0)); d=ImageDraw.Draw(L)
    d.text((40,30),txt,font=f,fill=col+(255,))
    g=L.filter(ImageFilter.GaussianBlur(22)); g2=L.filter(ImageFilter.GaussianBlur(7))
    out=Image.new('RGBA',L.size,(0,0,0,0))
    for gg,k in ((g,1.0),(g2,1.0)): out=Image.alpha_composite(out,gg)
    core=Image.new('RGBA',L.size,(0,0,0,0)); ImageDraw.Draw(core).text((40,30),txt,font=f,fill=(255,255,240,255))
    # núcleo claro com borda colorida
    out=Image.alpha_composite(out,L); 
    inner=core.filter(ImageFilter.GaussianBlur(1)); arr=np.array(inner); arr[...,3]=(arr[...,3]*0.55).astype(np.uint8)
    out=Image.alpha_composite(out,Image.fromarray(arr))
    if a<1: o=np.array(out); o[...,3]=(o[...,3]*a).astype(np.uint8); out=Image.fromarray(o)
    return out
cache={}
def overlay(t):
    O=Image.new('RGBA',(Wd,Hd),(0,0,0,0)); d=ImageDraw.Draw(O)
    for (t0,l1,l2,tn,col,t1) in TIT:
        if not(t0<=t<t1): continue
        a=ease((t-t0-0.12)/0.25); ao=1-ease((t-(t1-0.12))/0.12)
        a=min(a,ao)
        if a<=0: continue
        y=1180
        f1=font(92); w1=f1.getlength(l1); dy=int((1-a)*30)
        d.text(((Wd-w1)/2+3,y+dy+4),l1,font=f1,fill=(0,0,0,int(140*a)))
        d.text(((Wd-w1)/2,y+dy),l1,font=f1,fill=(245,245,240,int(255*a)))
        if t>=tn-0.05:
            p=ease((t-tn+0.05)/0.22); sz=230 if len(l2)<=8 else 190
            k=(l2,sz,col,round(min(a,p),2))
            if k not in cache: cache[k]=neon_layer(l2,sz,col,min(a,p))
            L=cache[k]; sc=1.18-0.18*p
            L2=L.resize((int(L.width*sc),int(L.height*sc)),Image.BICUBIC) if sc!=1 else L
            # pisca de neon (2 quadros) logo ao acender
            if 0.05<t-tn<0.12: 
                arr=np.array(L2);arr[...,3]=(arr[...,3]*0.5).astype(np.uint8);L2=Image.fromarray(arr)
            O.alpha_composite(L2,(int((Wd-L2.width)/2),int(y+100-(L2.height-L.height)/2)))
    # legenda
    for g in grp:
        if g[0][1]-0.05<=t<g[-1][2]+0.15 :
            f=font(64); txt=[w for w,a,b in g]; sp=f.getlength(' ')
            tot=sum(f.getlength(w.upper()) for w in txt)+sp*(len(txt)-1); x=(Wd-tot)/2; y=1640
            for w,a,b in g:
                if t<a-0.05: x+=f.getlength(w.upper())+sp; continue
                act=a-0.05<=t<b+0.05 or (w==g[-1][0] and t>=a)
                c=(255,214,40,255) if act else (255,255,255,255)
                d.text((x,y),w.upper(),font=f,fill=c,stroke_width=5,stroke_fill=(0,0,0,220))
                x+=f.getlength(w.upper())+sp
            break
    s='L I N D S O N   A L M E I D A'; d.text(((Wd-fi.getlength(s))/2,1846),s,font=fi,fill=(255,255,255,170))
    return np.array(O)
# gradiente inferior
gy=np.linspace(0,1,Hd)[:,None]; grad=np.clip((gy-0.52)/0.48,0,1)**1.4*0.62
vig=None
def readers():
    for i,s in enumerate(S):
        p=subprocess.Popen(['ffmpeg','-v','error','-i',f's{i}.mp4','-f','rawvideo','-pix_fmt','bgr24','-'],stdout=subprocess.PIPE)
        yield i,p
cuts=[s[0] for s in S[1:]]
TR={3.3:'punch',6.42:'whip',12.0:'punch',17.66:'whip',21.0:'punch',23.26:'whip',27.84:'punch',32.84:'whip',36.0:'punch'}
json.dump(TR,open('tr.json','w'))
frames={}
def shot_frames(i):
    p=subprocess.Popen(['ffmpeg','-v','error','-i',f's{i}.mp4','-f','rawvideo','-pix_fmt','bgr24','-'],stdout=subprocess.PIPE)
    out=[]
    while True:
        b=p.stdout.read(Wd*Hd*3)
        if len(b)<Wd*Hd*3: break
        out.append(np.frombuffer(b,np.uint8).reshape(Hd,Wd,3))
    return out
only=os.environ.get('QUADROS')
enc=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','bgr24','-s',f'{Wd}x{Hd}','-r','30','-i','-','-c:v','libx264','-crf','17','-preset','medium','-pix_fmt','yuv420p','video.mp4'],stdin=subprocess.PIPE)
rng=np.random.default_rng(1); grains=[(rng.normal(0,1,(Hd//2,Wd//2)).astype(np.float32)) for _ in range(6)]
yy,xx=np.mgrid[0:Hd,0:Wd]; vig=(1-0.38*(((xx-Wd/2)/(Wd*0.75))**2+((yy-Hd/2)/(Hd*0.72))**2)).clip(0.55,1)[...,None].astype(np.float32)
mult=(vig*(1-grad[...,None])).astype(np.float32)
prev=None;cur=None;ci=-1
def zoomf(img,z,dx=0,dy=0):
    if abs(z-1)<1e-3 and dx==0 and dy==0: return img
    M=np.float32([[z,0,(1-z)*Wd/2+dx],[0,z,(1-z)*Hd/2+dy]])
    return cv2.warpAffine(img,M,(Wd,Hd),flags=cv2.INTER_LINEAR,borderMode=cv2.BORDER_REFLECT)
def mblur(img,k,horiz=True):
    if k<3: return img
    ker=np.zeros((k,k),np.float32)
    if horiz: ker[k//2,:]=1/k
    else: ker[:,k//2]=1/k
    return cv2.filter2D(img,-1,ker)
for n in range(N):
    t=n/FPS
    i=max(j for j,s in enumerate(S) if s[0]<=t+1e-6)
    if i!=ci:
        prev=cur; prev_i=ci; cur=shot_frames(i); ci=i
    s=S[i]; k=int(round((t-s[0])*FPS)); k=min(k,len(cur)-1)
    dur=s[1]-s[0]; u=(t-s[0])/dur
    img=zoomf(cur[k],1.0+0.045*u)
    tr=TR.get(s[0]) if i>0 else None; nt=6
    if tr and k<nt and prev is not None:
        q=(k+1)/(nt+1); e=q*q*(3-2*q)
        pk=min(int(round((S[i-1][1]-S[i-1][0])*FPS))+k,len(prev)-1)
        pim=zoomf(prev[pk],1.045)
        if tr=='whip':
            sh=int(e*Wd*0.6); a=mblur(np.roll(pim,-sh,1),int(9+60*np.sin(np.pi*min(q*1.4,1))))
            b=mblur(np.roll(img,int((1-e)*Wd*0.6),1),int(9+60*np.sin(np.pi*max(q*1.4-0.4,0)/1.0)))
            img=cv2.addWeighted(a,1-e,b,e,0)
        else:
            z=1.0+0.14*(1-e); b=zoomf(img,z)
            bl=int(31*(1-e))|1
            if bl>3: b=cv2.addWeighted(b,0.6,cv2.GaussianBlur(b,(bl,bl),0),0.4,0)
            a=min(1,e*1.8); img=cv2.addWeighted(pim,1-a,b,a,0)
            # tremor curto
            img=zoomf(img,1.0,dx=int((rng.random()-0.5)*14*(1-e)),dy=int((rng.random()-0.5)*14*(1-e)))
    f=img.astype(np.float32)*mult
    g=cv2.resize(grains[n%6],(Wd,Hd),interpolation=cv2.INTER_LINEAR)[...,None]*5.0
    f=f+g
    ov=overlay(t); al=ov[...,3:4].astype(np.float32)/255
    f=f*(1-al)+ov[...,2::-1][...,:3].astype(np.float32)*al
    out=np.clip(f,0,255).astype(np.uint8)
    enc.stdin.write(out.tobytes())
    if n%60==0: print(n,N,flush=True)
enc.stdin.close(); enc.wait()
