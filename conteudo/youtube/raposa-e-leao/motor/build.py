"""Raposa e Leão — monta um Short: python3 build.py <stage.html> <pasta_do_short>
A pasta precisa ter voz.wav e spec.json (total em segundos). Gera video.mp4 nela."""
import json,sys,os,subprocess,numpy as np,soundfile as sf
from scipy.signal import butter,lfilter
D=os.path.dirname(os.path.abspath(__file__));stage=sys.argv[1];P=os.path.abspath(sys.argv[2])
W='/tmp/claude-0/-home-user/5acf6937-9ac6-56e0-bc29-78bef210dc8b/scratchpad/rl_work_'+os.path.basename(P);os.makedirs(W,exist_ok=True)
spec=json.load(open(P+'/spec.json'));T=spec['total']
html=open(D+'/'+stage).read().replace('__EMB__',open(D+'/emblema.inc').read()).replace('__IW__',open(D+'/interage.inc').read()).replace('__SPEC__',json.dumps(spec,ensure_ascii=False))
open(D+'/_stage_'+os.path.basename(P)+'.html','w').write(html)
STEP=int(os.environ.get('STEP','1'))
js=f"""const {{chromium}}=require('playwright');const fs=require('fs');
(async()=>{{const b=await chromium.launch();const p=await b.newPage({{viewport:{{width:1080,height:1920}}}});
p.on('pageerror',e=>console.log('ERR',e.message));await p.goto('file://{D}/_stage_{os.path.basename(P)}.html');await p.waitForFunction(()=>window.ready);await p.waitForTimeout(600);
fs.writeFileSync('{W}/sfx.json',JSON.stringify(await p.evaluate(()=>window.SFX)));fs.rmSync('{W}/fr',{{recursive:true,force:true}});fs.mkdirSync('{W}/fr');
const n=Math.floor({T}*30);for(let f=0;f<n;f+={STEP}){{await p.evaluate(t=>render(t),f/30);await p.screenshot({{path:'{W}/fr/'+String(f).padStart(5,'0')+'.jpg',type:'jpeg',quality:90}})}}
await b.close()}})();"""
open(W+'/r.js','w').write(js);subprocess.run(['node',W+'/r.js'],check=True,env={**os.environ,'NODE_PATH':subprocess.check_output(['npm','root','-g']).decode().strip()})
if STEP!=1:print('preview em',W+'/fr');sys.exit()
S=44100;N=int(T*S);rng=np.random.default_rng(3)
def lp(x,f):b,a=butter(2,f/(S/2));return lfilter(b,a,x)
def bp(x,lo,hi):b,a=butter(2,[lo/(S/2),hi/(S/2)],'band');return lfilter(b,a,x)
def tt(d):return np.arange(int(d*S))/S
def boom():t=tt(1.6);f=48+70*np.exp(-t*14);return np.sin(2*np.pi*np.cumsum(f)/S)*np.exp(-t*2.6)*.9+lp(rng.standard_normal(len(t)),400)*np.exp(-t*8)*.5
def punch():t=tt(.35);f=140*np.exp(-t*22)+50;return np.sin(2*np.pi*np.cumsum(f)/S)*np.exp(-t*10)*.8+lp(rng.standard_normal(len(t)),2500)*np.exp(-t*28)*.35
def whoosh():t=tt(.7);u=t/t[-1];return bp(rng.standard_normal(len(t)),300,2800)*np.sin(np.pi*u)**2*.55
def rip():t=tt(.4);return bp(rng.standard_normal(len(t)),1200,7000)*(np.abs(np.sin(t*70))**.6)*np.exp(-t*4)*.45
def stamp():return np.concatenate([punch(),np.zeros(int(.2*S))])*1.2
def page():t=tt(.5);return bp(rng.standard_normal(len(t)),900,5000)*np.exp(-((t-.15)**2)/.006)*.4
def riser():t=tt(.6);u=t/t[-1];return bp(rng.standard_normal(len(t)),600,6000)*u**2*.5
def ding():t=tt(1.2);return (np.sin(2*np.pi*880*t)+.5*np.sin(2*np.pi*1320*t))*np.exp(-t*3.5)*.25
FX=dict(ding=ding,boom=boom,punch=punch,whoosh=whoosh,rip=rip,stamp=stamp,page=page,riser=riser)
mix=np.zeros(N+3*S)
# trilha: drone grave em ré menor + pulso lento
t=np.arange(N)/S
R0=spec.get('tom',73.42);dr=sum(a*np.sin(2*np.pi*R0*m*t+np.sin(t*.3*k)) for k,(m,a) in enumerate([(1,.5),(1.5,.25),(2,.18),(2.378,.10),(3,.06)],1))
dr=lp(dr,900)*(.75+.25*np.sin(2*np.pi*t/8))
pulse=np.zeros(N)
# pulso: andamento e desenho variam por vídeo (spec['pulso'] = segundos entre batidas, spec['batida'] = padrão)
PU=spec.get('pulso',1.25);pad=spec.get('batida','reto')
for k,b in enumerate(np.arange(0,T,PU)):
    if pad=='espacado' and k%2:continue
    for off,g in ([(0,1)] if pad!='duplo' else [(0,1),(PU*.25,.55)]):
        i=int((b+off)*S);seg=np.sin(2*np.pi*55*tt(.5))*np.exp(-tt(.5)*7)*.5*g;pulse[i:i+len(seg)]+=seg[:max(0,N-i)]
amb=lp(rng.standard_normal(N),500)*.05
mus=(dr*.5+pulse*.6+amb)*np.minimum(1,t/1.0)*np.minimum(1,(T-t)/1.2)
mix[:N]+=mus*.32
for at,n in json.load(open(W+'/sfx.json')):
    x=FX[n]();i=int(at*S);mix[i:i+len(x)]+=x*.5
v,sr=sf.read(P+'/voz.wav');assert sr==S
v=v/np.max(np.abs(v))*.9;i=0;mix[i:i+len(v)]+=v
# leve ducking da trilha sob a voz já é dado pelo volume baixo; normaliza
mix=mix[:N];mix=mix/np.max(np.abs(mix))*.95
sf.write(W+'/a.wav',mix,S)
subprocess.run(['ffmpeg','-y','-loglevel','error','-framerate','30','-i',W+'/fr/%05d.jpg','-i',W+'/a.wav','-c:v','libx264','-pix_fmt','yuv420p','-crf','18','-preset','medium','-c:a','aac','-b:a','192k','-shortest','-movflags','+faststart',P+'/video.mp4'],check=True)
print('ok',P+'/video.mp4')
