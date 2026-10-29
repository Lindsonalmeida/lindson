"""Raposa e Leão — vídeo longo 16:9: python3 longo.py <pasta com roteiro.json>"""
import json,sys,os,subprocess,asyncio,numpy as np,soundfile as sf,edge_tts
from scipy.signal import butter,lfilter
P=os.path.abspath(sys.argv[1]);D=os.path.dirname(os.path.abspath(__file__));nm=os.path.basename(P)
W=f'/tmp/claude-0/-home-user/5acf6937-9ac6-56e0-bc29-78bef210dc8b/scratchpad/lg_{nm}';os.makedirs(W+'/vh',exist_ok=True)
rot=json.load(open(P+'/roteiro.json'));
IM=os.path.join(D,'..','img')
FUNDOS={'06':['palazzo_vecchio','lorenzo','piazza_della_signoria','maquiavel2'],'07':['hannibal','scipio_africanus','cesar','julius_caesar'],'08':['arno','ponte_vecchio','florence'],'09':['girolamo_savonarola','bonfire_of_the_vanities','piazza_della_signoria','palazzo_vecchio'],'10':['florence','palazzo_vecchio','maquiavel2','ponte_vecchio'],'11':['marcus_aurelius','commodus','caracalla','arco_severo','cesar']}
pool=[os.path.relpath(x,D) for n in FUNDOS.get(nm,[]) for x in (IM+'/hist/'+n+'.jpg',IM+'/'+n+'.jpg') if os.path.exists(x)]
for j,g in enumerate(rot['seg']):
    if pool: g['bg']=pool[j%len(pool)]
for g in rot['seg']:
    tl=g['tela']
    if 'img' in tl:
        f=next((x for x in (IM+'/hist/'+tl['img'],IM+'/'+tl['img']) if os.path.exists(x)),None)
        if f: tl['img']=os.path.relpath(f,D)
        elif tl['t']=='imagem': g['tela']={'t':'frase','h':tl['h']+'<br><b>'+tl['s']+'</b>'}
        else: tl['img']='../img/maquiavel.jpg'
S=44100;FPS=int(os.environ.get('FPS','24'))
sys.path.insert(0,'/home/user/lindson/conteudo/youtube/comum');import voz_humana
from voz_humana import narrar
voz_humana._pct=lambda v:f'{int(round(v)):+d}%';voz_humana._hz=lambda v:f'{int(round(v)):+d}Hz'  # sinal correto perto de zero
# voz humanizada por segmento; falas diretas ao ouvinte (conversa, inscreva, compromisso) mais calorosas
CONV=('conversa','inscreva','compromisso')
vozes=[];t=0.6
for i,g in enumerate(rot['seg']):
    wv=f'{W}/vh/{i:03d}.wav';js=wv[:-4]+'.json';ch=json.dumps([g['txt'],g['tela']['t'] in CONV or g.get('conversa',False)])
    if not(os.path.exists(js) and json.load(open(js)).get('k')==ch):
        a,ws=narrar(g['txt'],rate=7,pitch=-6,semente=f'rl-longo-{nm}',conversa=g['tela']['t'] in CONV or g.get('conversa',False))
        sf.write(wv,a,S);json.dump({'k':ch,'w':ws},open(js,'w'),ensure_ascii=False)
    a,_=sf.read(wv);g['ini']=max(0,t-.35);g['words']=[[w,round(t+o,3)] for w,o in json.load(open(js))['w']];vozes.append((t,a));t+=len(a)/S+(.9 if g['tela']['t'] in('capitulo','abertura') else .75 if g['tela']['t'] in CONV else .45)
for i,g in enumerate(rot['seg']):g['fim']=rot['seg'][i+1]['ini'] if i+1<len(rot['seg']) else t+5
T=round(t+5,2);rot['total']=T
html=open(D+'/longo2.html').read().replace('__EMB__',open(D+'/emblema.inc').read()).replace('__IW__',open(D+'/interage.inc').read()).replace('__SPEC__',json.dumps(rot,ensure_ascii=False))
st=f'{D}/_stage_lg_{nm}.html';open(st,'w').write(html)
STEP=int(os.environ.get('STEP','1'));LIM=float(os.environ.get('LIMITE','0'))  # LIMITE=60 -> prévia só do começo
js=f"""const {{chromium}}=require('playwright');const fs=require('fs');
(async()=>{{const b=await chromium.launch();const p=await b.newPage({{viewport:{{width:1920,height:1080}}}});
p.on('pageerror',e=>console.log('ERR',e.message));await p.goto('file://{st}');await p.waitForFunction(()=>window.ready);await p.waitForTimeout(800);
fs.writeFileSync('{W}/sfx.json',JSON.stringify(await p.evaluate(()=>window.SFX)));fs.rmSync('{W}/fr',{{recursive:true,force:true}});fs.mkdirSync('{W}/fr');
const n=Math.floor({LIM or T}*{FPS});for(let f=0;f<n;f+={STEP}){{await p.evaluate(t=>render(t),f/{FPS});await p.screenshot({{path:'{W}/fr/'+String(f).padStart(6,'0')+'.jpg',type:'jpeg',quality:88}})}}
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
def ding():t=tt(1.2);return (np.sin(2*np.pi*880*t)+.5*np.sin(2*np.pi*1320*t))*np.exp(-t*3.5)*.22
FX=dict(boom=boom,punch=punch,whoosh=whoosh,rip=rip,page=page,riser=riser,ding=ding)
tm=np.arange(N)/S;mix=np.zeros(N+4*S)
TONS=[(73.42,65.41,69.3),(65.41,58.27,61.74),(69.3,61.74,65.41),(61.74,55.0,58.27),(77.78,69.3,73.42)][int(nm)%5]
for k,(seg0,root) in enumerate([(0,TONS[0]),(T/3,TONS[1]),(2*T/3,TONS[2])]):
    m=(tm>=seg0)&(tm<seg0+T/3+2);x=np.zeros(N);tt0=tm[m]
    x[m]=sum(a*np.sin(2*np.pi*root*r*tt0+np.sin(tt0*.3*j)) for j,(r,a) in enumerate([(1,.5),(1.5,.25),(2,.18),(2.378,.1)],1))
    fade=np.clip((tm-seg0)/2,0,1)*np.clip((seg0+T/3+2-tm)/2,0,1);mix[:N]+=lp(x*fade,900)*.11
mix[:N]+=lp(rng.standard_normal(N),400)*.015
for at,n in json.load(open(W+'/sfx.json')):
    x=FX[n]();i=int(at*S);mix[i:i+len(x)]+=x*.4
for at,a in vozes:i=int(at*S);mix[i:i+len(a)]+=a/np.max(np.abs(a))*.9
mix=mix[:N];mix=mix/np.max(np.abs(mix))*.95;sf.write(W+'/a.wav',mix,S)
subprocess.run(['ffmpeg','-y','-loglevel','error','-framerate',str(FPS),'-i',W+'/fr/%06d.jpg','-i',W+'/a.wav','-c:v','libx264','-pix_fmt','yuv420p','-crf','23','-preset','slow','-tune','animation','-c:a','aac','-b:a','128k','-shortest','-movflags','+faststart',P+('/previa.mp4' if LIM else '/video.mp4')],check=True)
print('ok',P+'/video.mp4',T)
