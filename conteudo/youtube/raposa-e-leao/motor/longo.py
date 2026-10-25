"""Raposa e Leão — vídeo longo 16:9: python3 longo.py <pasta com roteiro.json>"""
import json,sys,os,subprocess,asyncio,numpy as np,soundfile as sf,edge_tts
from scipy.signal import butter,lfilter
P=os.path.abspath(sys.argv[1]);D=os.path.dirname(os.path.abspath(__file__));nm=os.path.basename(P)
W=f'/tmp/claude-0/-home-user/11370c4d-a43e-5ddc-930a-0de2e05453c2/scratchpad/lg_{nm}';os.makedirs(W+'/vz',exist_ok=True)
rot=json.load(open(P+'/roteiro.json'));S=44100;FPS=int(os.environ.get('FPS','24'))
async def tts(txt,out):
    c=edge_tts.Communicate(txt,'pt-BR-AntonioNeural',rate='+7%',pitch='-6Hz',proxy=os.environ.get('HTTPS_PROXY'),boundary='WordBoundary')
    ws=[]
    with open(out,'wb') as f:
        async for ch in c.stream():
            if ch['type']=='audio':f.write(ch['data'])
            elif ch['type']=='WordBoundary':ws.append([ch['text'],round(ch['offset']/1e7,3)])
    json.dump(ws,open(out[:-4]+'.json','w'),ensure_ascii=False)
vozes=[];t=0.6
for i,g in enumerate(rot['seg']):
    mp=f'{W}/vz/{i:03d}.mp3';wv=mp[:-4]+'.wav'
    if not os.path.exists(mp[:-4]+'.json'):
        asyncio.run(tts(g['txt'],mp));subprocess.run(['ffmpeg','-y','-loglevel','error','-i',mp,'-ar',str(S),'-ac','1',wv],check=True)
    a,_=sf.read(wv);g['ini']=max(0,t-.35);g['words']=[[w,round(t+o,3)] for w,o in json.load(open(mp[:-4]+'.json'))];vozes.append((t,a));t+=len(a)/S+(.9 if g['tela']['t'] in('capitulo','abertura') else .45)
for i,g in enumerate(rot['seg']):g['fim']=rot['seg'][i+1]['ini'] if i+1<len(rot['seg']) else t+3
T=round(t+3,2);rot['total']=T
html=open(D+'/longo.html').read().replace('__EMB__',open(D+'/emblema.inc').read()).replace('__SPEC__',json.dumps(rot,ensure_ascii=False))
st=f'{D}/_stage_lg_{nm}.html';open(st,'w').write(html)
STEP=int(os.environ.get('STEP','1'))
js=f"""const {{chromium}}=require('playwright');const fs=require('fs');
(async()=>{{const b=await chromium.launch();const p=await b.newPage({{viewport:{{width:1920,height:1080}}}});
p.on('pageerror',e=>console.log('ERR',e.message));await p.goto('file://{st}');await p.waitForFunction(()=>window.ready);await p.waitForTimeout(800);
fs.writeFileSync('{W}/sfx.json',JSON.stringify(await p.evaluate(()=>window.SFX)));fs.rmSync('{W}/fr',{{recursive:true,force:true}});fs.mkdirSync('{W}/fr');
const n=Math.floor({T}*{FPS});for(let f=0;f<n;f+={STEP}){{await p.evaluate(t=>render(t),f/{FPS});await p.screenshot({{path:'{W}/fr/'+String(f).padStart(6,'0')+'.jpg',type:'jpeg',quality:88}})}}
await b.close()}})();"""
open(W+'/r.js','w').write(js);subprocess.run(['node',W+'/r.js'],check=True,env={**os.environ,'NODE_PATH':subprocess.check_output(['npm','root','-g']).decode().strip()})
if STEP!=1:print('preview',W+'/fr',T);sys.exit()
N=int(T*S);rng=np.random.default_rng(5)
def lp(x,f):b,a=butter(2,f/(S/2));return lfilter(b,a,x)
def bp(x,lo,hi):b,a=butter(2,[lo/(S/2),hi/(S/2)],'band');return lfilter(b,a,x)
def tt(d):return np.arange(int(d*S))/S
def boom():t=tt(1.6);f=48+70*np.exp(-t*14);return np.sin(2*np.pi*np.cumsum(f)/S)*np.exp(-t*2.6)*.8
def punch():t=tt(.35);f=140*np.exp(-t*22)+50;return np.sin(2*np.pi*np.cumsum(f)/S)*np.exp(-t*10)*.7
def whoosh():t=tt(.7);u=t/t[-1];return bp(rng.standard_normal(len(t)),300,2800)*np.sin(np.pi*u)**2*.35
def rip():t=tt(.4);return bp(rng.standard_normal(len(t)),1200,7000)*(np.abs(np.sin(t*70))**.6)*np.exp(-t*4)*.4
def page():t=tt(.5);return bp(rng.standard_normal(len(t)),900,5000)*np.exp(-((t-.15)**2)/.006)*.35
def riser():t=tt(.6);u=t/t[-1];return bp(rng.standard_normal(len(t)),600,6000)*u**2*.4
FX=dict(boom=boom,punch=punch,whoosh=whoosh,rip=rip,page=page,riser=riser)
tm=np.arange(N)/S;mix=np.zeros(N+4*S)
for k,(seg0,root) in enumerate([(0,73.42),(T/3,65.41),(2*T/3,69.3)]):
    m=(tm>=seg0)&(tm<seg0+T/3+2);x=np.zeros(N);tt0=tm[m]
    x[m]=sum(a*np.sin(2*np.pi*root*r*tt0+np.sin(tt0*.3*j)) for j,(r,a) in enumerate([(1,.5),(1.5,.25),(2,.18),(2.378,.1)],1))
    fade=np.clip((tm-seg0)/2,0,1)*np.clip((seg0+T/3+2-tm)/2,0,1);mix[:N]+=lp(x*fade,900)*.11
mix[:N]+=lp(rng.standard_normal(N),400)*.015
for at,n in json.load(open(W+'/sfx.json')):
    x=FX[n]();i=int(at*S);mix[i:i+len(x)]+=x*.4
for at,a in vozes:i=int(at*S);mix[i:i+len(a)]+=a/np.max(np.abs(a))*.9
mix=mix[:N];mix=mix/np.max(np.abs(mix))*.95;sf.write(W+'/a.wav',mix,S)
subprocess.run(['ffmpeg','-y','-loglevel','error','-framerate',str(FPS),'-i',W+'/fr/%06d.jpg','-i',W+'/a.wav','-c:v','libx264','-pix_fmt','yuv420p','-crf','20','-preset','medium','-c:a','aac','-b:a','192k','-shortest','-movflags','+faststart',P+'/video.mp4'],check=True)
print('ok',P+'/video.mp4',T)
