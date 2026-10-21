"""Gera Reels em motion design: python3 build.py <spec.json> <saida.mp4>"""
import json,sys,os,subprocess,numpy as np,soundfile as sf
from scipy.signal import butter,lfilter
from kokoro_onnx import Kokoro
D=os.path.dirname(os.path.abspath(__file__));W=sys.argv[3] if len(sys.argv)>3 else '/tmp/reelwork'
TTS=os.environ.get('TTS','/tmp/claude-0/-home-user/11370c4d-a43e-5ddc-930a-0de2e05453c2/scratchpad/tts')
spec=json.load(open(sys.argv[1]));out=sys.argv[2];os.makedirs(W,exist_ok=True)
SR=24000;k=Kokoro(TTS+'/kokoro-v1.0.onnx',TTS+'/voices-v1.0.bin')
segs=[];t=0.35;voc=[]
for i,s in enumerate(spec['scenes']):
    a,sr=k.create(s['say'],voice=spec.get('voice','pm_alex'),speed=spec.get('speed',1.05),lang='pt-br');d=len(a)/sr
    lead=0.35 if i else 0.0;s=dict(s);s['s']=t;s['vs']=t+lead;s['vd']=d;t=s['vs']+d+s.get('hold',0.35);s['e']=t
    ws=s['cap'].split();tot=sum(len(w)+2 for w in ws);acc=0;s['words']=[]
    for w in ws:s['words'].append([w,round(s['vs']+d*acc/tot,3)]);acc+=len(w)+2
    segs.append(s);voc.append((s['vs'],a))
for i in range(len(segs)-1):segs[i]['e']=segs[i+1]['s']
segs[-1]['e']=t+1.2;T=segs[-1]['e']
html=open(D+'/'+spec.get('stage','motion.html')).read().replace('__TL__',json.dumps({'segs':segs,'total':T},ensure_ascii=False))
open(W+'/stage.html','w').write(html)
js=f"""const {{chromium}}=require('playwright');const fs=require('fs');
(async()=>{{const b=await chromium.launch({{executablePath:'/opt/pw-browsers/chromium'}});const p=await b.newPage({{viewport:{{width:1080,height:1920}}}});
p.on('pageerror',e=>console.log('ERR',e.message));await p.goto('file://{W}/stage.html');await p.waitForFunction(()=>window.ready);await p.waitForTimeout(800);
fs.writeFileSync('{W}/sfx.json',JSON.stringify(await p.evaluate(()=>window.SFX)));fs.rmSync('{W}/fr',{{recursive:true,force:true}});fs.mkdirSync('{W}/fr');
const n=Math.floor({T}*30);const stp={int(os.environ.get('STEP','1'))};for(let f=0;f<n;f+=stp){{await p.evaluate(t=>render(t),f/30);await p.screenshot({{path:'{W}/fr/'+String(f).padStart(5,'0')+'.jpg',type:'jpeg',quality:88}})}}
await b.close()}})();"""
open(W+'/r.js','w').write(js);subprocess.run(['node',W+'/r.js'],check=True,env={**os.environ,'NODE_PATH':subprocess.check_output(['npm','root','-g']).decode().strip()})
if os.environ.get('STEP','1')!='1':print('preview');sys.exit()
# ---------- áudio ----------
S=44100;N=int(T*S)+S;rng=np.random.default_rng(7)
def bp(x,lo,hi):b,a=butter(2,[lo/(S/2),hi/(S/2)],'band');return lfilter(b,a,x)
def lp(x,f):b,a=butter(2,f/(S/2));return lfilter(b,a,x)
def env(n,dec):t=np.arange(n)/S;return np.exp(-t*dec)
def boom():n=int(.8*S);t=np.arange(n)/S;f=55+90*np.exp(-t*18);return np.sin(2*np.pi*np.cumsum(f)/S)*np.exp(-t*4)+rng.standard_normal(n)*np.exp(-t*40)*.25
def punch():n=int(.25*S);t=np.arange(n)/S;f=160*np.exp(-t*25)+60;return np.sin(2*np.pi*np.cumsum(f)/S)*np.exp(-t*14)*.8+lp(rng.standard_normal(n),3000)*np.exp(-t*30)*.4
def whoosh():n=int(.45*S);u=np.arange(n)/n;return bp(rng.standard_normal(n),400,3500)*np.sin(np.pi*u)**1.5*.8
def pop():n=int(.12*S);t=np.arange(n)/S;f=900*np.exp(-t*12)+300;return np.sin(2*np.pi*np.cumsum(f)/S)*np.exp(-t*30)*.55
def ding():n=int(1.1*S);t=np.arange(n)/S;return (np.sin(2*np.pi*1320*t)+.5*np.sin(2*np.pi*1980*t)+.3*np.sin(2*np.pi*2640*t))*np.exp(-t*3.5)*.33
def buzz():n=int(.35*S);t=np.arange(n)/S;x=np.sign(np.sin(2*np.pi*110*t))*.3+np.sign(np.sin(2*np.pi*116*t))*.3;return lp(x,900)*np.minimum(1,t/.01)*np.exp(-t*5)
def riser():n=int(1.2*S);u=np.arange(n)/n;return bp(rng.standard_normal(n),500,6000)*u**2*.9
def tick():n=int(.04*S);t=np.arange(n)/S;return rng.standard_normal(n)*np.exp(-t*150)*.3
def vinheta():
    n=int(1.4*S);t=np.arange(n)/S;y=np.zeros(n)
    for j,f in enumerate([392,523,659,784]):
        a=int(j*.12*S);tt=t[:n-a];y[a:]+=np.sign(np.sin(2*np.pi*f*tt))*.18*np.exp(-tt*3)
    return lp(y,4000)+np.pad(boom(),(0,max(0,n-int(.8*S))))[:n]*.6
def notif():n=int(.3*S);t=np.arange(n)/S;f=np.where(t<.1,880,1320);return np.sin(2*np.pi*f*t)*np.exp(-((t%.1)*20))*.35
def typ():
    y=np.zeros(int(.5*S))
    for j in range(6):i=int(j*.07*S);y[i:i+len(tick())]+=tick()*1.4
    return y
def hum():n=int(2.2*S);t=np.arange(n)/S;return (np.sin(2*np.pi*60*t)+.4*np.sin(2*np.pi*120*t))*.12*np.minimum(1,t/.3)
def glitch():n=int(.18*S);return bp(rng.standard_normal(n),800,6000)*.5
def clock():n=int(.08*S);t=np.arange(n)/S;return bp(rng.standard_normal(n),2000,6000)*np.exp(-t*80)*.8
def crowd():n=int(2*S);u=np.arange(n)/n;return bp(rng.standard_normal(n),300,1800)*.25*np.sin(np.pi*u)
def rewind():n=int(1*S);t=np.arange(n)/S;f=1800*np.exp(-t*2.5)+200;return np.sign(np.sin(2*np.pi*np.cumsum(f)/S))*.12+bp(rng.standard_normal(n),1000,5000)*.15
def bell():n=int(1.2*S);t=np.arange(n)/S;return (np.sin(2*np.pi*2093*t)+.6*np.sin(2*np.pi*3136*t))*np.exp(-t*4)*.3
def off():n=int(.6*S);t=np.arange(n)/S;f=1200*np.exp(-t*8)+60;return np.sin(2*np.pi*np.cumsum(f)/S)*np.exp(-t*5)*.4
def beep():n=int(.25*S);t=np.arange(n)/S;return np.sin(2*np.pi*1000*t)*.3
def rip():n=int(.45*S);t=np.arange(n)/S;return bp(rng.standard_normal(n),1500,9000)*(np.abs(np.sin(t*90))**.5)*np.exp(-t*3)*.7
def stampbig():return np.pad(punch(),(0,int(.55*S)))+boom()[:int(.8*S)]*.8
def pen():n=int(1*S);t=np.arange(n)/S;return bp(rng.standard_normal(n),2500,8000)*(.5+.5*np.abs(np.sin(t*25)))*.35
def pin():n=int(.1*S);t=np.arange(n)/S;f=1600*np.exp(-t*20)+500;return np.sin(2*np.pi*np.cumsum(f)/S)*np.exp(-t*40)*.6
def sq(f,d,v=.25):n=int(d*S);t=np.arange(n)/S;return np.sign(np.sin(2*np.pi*f*t))*v*np.exp(-t*3)
def seq(fs,d):return np.concatenate([sq(f,d) for f in fs])
def coin():return np.concatenate([sq(988,.07),sq(1319,.3)*np.exp(-np.arange(int(.3*S))/S*8)])
def jump():n=int(.25*S);t=np.arange(n)/S;f=300+1400*t/.25;return np.sign(np.sin(2*np.pi*np.cumsum(f)/S))*.2
def powerup():return seq([523,659,784,1047,784,1047,1319,1568],.06)
def gameover():return seq([784,659,523,392,330,262],.16)
def blip():return sq(660,.08)
def scratch():n=int(.5*S);t=np.arange(n)/S;w=np.sin(2*np.pi*np.cumsum(900+700*np.sin(t*40))/S);return bp(rng.standard_normal(n),600,4000)*.4*np.abs(w)*np.exp(-t*3)
def shutter():y=np.zeros(int(.2*S));c=clock();y[:len(c)]+=c;y[int(.09*S):int(.09*S)+len(c)]+=c;return y
FX=dict(coin=(coin,.6),jump=(jump,.6),powerup=(powerup,.6),gameover=(gameover,.7),blip=(blip,.5),scratch=(scratch,.9),shutter=(shutter,.8),slam=(stampbig,.7),vinheta=(vinheta,.8),swoosh=(whoosh,.5),notif=(notif,.8),stamp=(punch,.8),hit=(boom,.7),type=(typ,.7),hum=(hum,.8),glitch=(glitch,.6),tick=(clock,.7),crowd=(crowd,.8),cut=(punch,.6),silence=(lambda:np.zeros(10),0),rewind=(rewind,.8),bell=(bell,.8),off=(off,.8),beep=(beep,.6),rip=(rip,.8),stampbig=(stampbig,.9),pen=(pen,.8),pin=(pin,.7),postit=(pop,.5),paper=(whoosh,.35),boom=(boom,.75),punch=(punch,.6),whoosh=(whoosh,.5),pop=(pop,.6),ding=(ding,.7),buzz=(buzz,.55),riser=(riser,.5))
sfx=np.zeros(N)
def add(buf,sig,at,g):
    i=int(at*S);j=min(N,i+len(sig))
    if 0<=i<j:buf[i:j]+=sig[:j-i]*g
for at,kind in json.load(open(W+'/sfx.json')):f,g=FX.get(kind,(pop,.4));add(sfx,f(),at,g)
mus=np.zeros(N);beat=60/spec.get('bpm',104);ch=spec.get('chords',[220.0,174.61,261.63,196.0])
chip=spec.get('music')=='chip'
for b in range(int(T/beat)+1) if chip else []:
    at=b*beat;r=ch[(b//4)%4];add(mus,np.concatenate([sq(f,beat/4,.12) for f in [r*2,r*2.52,r*3,r*4]]),at,1);add(mus,sq(r/2,beat*.9,.2),at,1)
    if b%2:add(mus,tick()*.8,at,1)
for b in range(int(T/beat)+1) if not chip else []:
    at=b*beat;i=int(at*S);add(mus,boom()[:int(.35*S)]*.5,at,1);add(mus,tick()*.6,at+beat/2,1)
    root=ch[(b//4)%4]/2;n=int(beat*S);t=np.arange(n)/S;add(mus,lp(((t*root)%1*2-1),500)*np.exp(-t*2)*.35,at,1)
    if b%2==0:
        n2=int(beat*2*S);t2=np.arange(n2)/S;r=ch[(b//4)%4];add(mus,sum(np.sin(2*np.pi*f*t2) for f in [r,r*1.26,r*1.5])*.04*np.minimum(1,t2/.3),at,1)
v=np.zeros(N)
for at,a in voc:a2=np.interp(np.arange(0,len(a),SR/S),np.arange(len(a)),a);add(v,a2,at,1)
ms=spec.get('musicFrom',0);mstart=segs[ms]['s'] if ms else 0;mus[:int(mstart*S)]*=0.0
mus*=spec.get('musicVol',1.0)
w=int(.15*S);e=np.convolve(np.abs(v),np.ones(w)/w,'same');duck=1-.6*np.clip(e/(e.max()*.3+1e-9),0,1)
fade=np.ones(N);fo=int(1.2*S);fade[-fo:]=np.linspace(1,0,fo)
mix=np.tanh((v*1.7+mus*duck*.5+sfx*.6)*fade*1.1)*.92;sf.write(W+'/mix.wav',mix[:int(T*S)],S)
subprocess.run(['ffmpeg','-y','-loglevel','error','-framerate','30','-i',W+'/fr/%05d.jpg','-i',W+'/mix.wav','-c:v','libx264','-pix_fmt','yuv420p','-crf','19','-c:a','aac','-b:a','192k','-shortest','-movflags','+faststart',out],check=True)
print(out,round(T,1))
