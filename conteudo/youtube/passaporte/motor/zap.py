"""Zap Bíblico: Short 9:16 em formato de conversa de WhatsApp. python3 zap.py <id> [STEP=24 para prévia] -> ../videos/<id>.mp4"""
import json, sys, os, subprocess, asyncio, time
import numpy as np, soundfile as sf, edge_tts
from scipy.signal import butter, lfilter
D = os.path.dirname(os.path.abspath(__file__)); RAIZ = os.path.join(D, '..')
sys.path.insert(0, '/home/user/lindson/conteudo/produtos/passaporte'); from icones import icone
TMP = '/tmp/claude-0/-home-user/5acf6937-9ac6-56e0-bc29-78bef210dc8b/scratchpad/zap'
vid = sys.argv[1]; STEP = int(os.environ.get('STEP', '1')); FPS = 30
spec = next(v for v in json.load(open(RAIZ + '/zap.json')) if v['id'] == vid)
W = f'{TMP}/{vid}'; os.makedirs(W + '/vz', exist_ok=True)
spec['chat']['icone'] = icone(spec['chat']['icone'])
for p in spec['pessoas'].values(): p['icone'] = icone(p['icone'])
VOZ = {'n': 'pt-BR-FranciscaNeural', 'm': 'pt-BR-AntonioNeural', 'f': 'pt-BR-ThalitaMultilingualNeural'}

S = 44100
async def tts(txt, voz, out):
    c = edge_tts.Communicate(txt, voz, rate='+8%', proxy=os.environ.get('HTTPS_PROXY'), boundary='WordBoundary'); ws = []
    with open(out, 'wb') as f:
        async for ch in c.stream():
            if ch['type'] == 'audio': f.write(ch['data'])
            elif ch['type'] == 'WordBoundary': ws.append([ch['text'], round(ch['offset'] / 1e7, 3)])
    json.dump(ws, open(out[:-4] + '.json', 'w'), ensure_ascii=False)
vozes = []; t = 0.4
for i, c in enumerate(spec['cenas']):
    if c['tipo'] == 'figurinha': c['icone'] = icone(c['icone'])
    fala = c.get('txt') if c['tipo'] in ('narra', 'msg', 'audio', 'sistema', 'versiculo', 'fim') else None
    if not fala: c['ini'] = t; t += .8; continue
    voz = VOZ[spec['pessoas'][c['de']].get('voz', 'm')] if c['tipo'] in ('msg', 'audio') else VOZ['n']
    if c['tipo'] in ('msg', 'audio'): t += .7  # tempo do "digitando…"
    mp = f'{W}/vz/{i:03d}.mp3'; wv = mp[:-4] + '.wav'
    if not os.path.exists(mp[:-4] + '.json'):
        for k in range(6):
            try:
                try: asyncio.run(tts(fala, voz, mp))
                except Exception:
                    if voz == VOZ['f']: asyncio.run(tts(fala, 'pt-BR-FranciscaNeural', mp))
                    else: raise
                break
            except Exception as e: print('tts de novo', i, e); time.sleep(5 + 5 * k)
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', mp, '-ar', str(S), '-ac', '1', wv], check=True)
    a, _ = sf.read(wv); c['ini'] = t; c['dur'] = len(a) / S; c['words'] = [[w, round(t + o, 3)] for w, o in json.load(open(mp[:-4] + '.json'))]
    vozes.append((t, a)); t += len(a) / S + .3
for i, c in enumerate(spec['cenas']): c['fim'] = spec['cenas'][i + 1]['ini'] if i + 1 < len(spec['cenas']) else t + 2.5
TT = round(t + 2.5, 2)

html = open(D + '/zap.html').read().replace('__SPEC__', json.dumps(spec, ensure_ascii=False))
st = f'{W}/stage.html'; open(st, 'w').write(html)
js = f"""const {{chromium}}=require('playwright');const fs=require('fs');
(async()=>{{const b=await chromium.launch();const p=await b.newPage({{viewport:{{width:1080,height:1920}}}});
p.on('pageerror',e=>console.log('ERR',e.message));await p.goto('file://{st}');await p.waitForFunction(()=>window.ready);await p.waitForTimeout(500);
fs.writeFileSync('{W}/sfx.json',JSON.stringify(await p.evaluate(()=>window.SFX)));fs.rmSync('{W}/fr',{{recursive:true,force:true}});fs.mkdirSync('{W}/fr');
const n=Math.floor({TT}*{FPS});for(let f=0;f<n;f+={STEP}){{await p.evaluate(t=>render(t),f/{FPS});await p.screenshot({{path:'{W}/fr/'+String(f).padStart(6,'0')+'.jpg',type:'jpeg',quality:88}})}}
await b.close()}})();"""
open(W + '/r.js', 'w').write(js); subprocess.run(['node', W + '/r.js'], check=True)
if STEP != 1: print('previa', W + '/fr', TT); sys.exit()

N = int(TT * S); rng = np.random.default_rng(7)
def bp(x, lo, hi): b, a = butter(2, [lo / (S / 2), hi / (S / 2)], 'band'); return lfilter(b, a, x)
def tt_(d): return np.arange(int(d * S)) / S
def pop(): t = tt_(.12); f = 900 + 600 * np.exp(-t * 40); return np.sin(2 * np.pi * np.cumsum(f) / S) * np.exp(-t * 30) * .35
def tic(): t = tt_(.1); return np.sin(2 * np.pi * 1500 * t) * np.exp(-t * 45) * .25
def whoosh(): t = tt_(.5); u = t / t[-1]; return bp(rng.standard_normal(len(t)), 400, 3000) * np.sin(np.pi * u) ** 2 * .25
def carimbo(): t = tt_(.45); f = 90 * np.exp(-t * 18) + 45; return (np.sin(2 * np.pi * np.cumsum(f) / S) * np.exp(-t * 12) + bp(rng.standard_normal(len(t)), 200, 2500) * np.exp(-t * 40) * .5) * .8
FX = dict(pop=pop, tic=tic, whoosh=whoosh, carimbo=carimbo)
tm = np.arange(N) / S; mix = np.zeros(N + 3 * S)
# trilha leve: notas dedilhadas
esc = [392.0, 440.0, 493.9, 587.3, 659.3, 587.3, 493.9, 440.0]
for k in range(int(TT / .5)):
    a0 = k * .5; i0 = int(a0 * S); x = tt_(.5); f = esc[k % 8] / (2 if (k // 8) % 2 else 1)
    mix[i0:i0 + len(x)] += np.sin(2 * np.pi * f * x) * np.exp(-x * 7) * .05
for at, n in json.load(open(W + '/sfx.json')):
    x = FX[n](); i = int(at * S); mix[i:i + len(x)] += x
for at, a in vozes: i = int(at * S); mix[i:i + len(a)] += a / np.max(np.abs(a)) * .9
mix = mix[:N]; mix = mix / np.max(np.abs(mix)) * .95; sf.write(W + '/a.wav', mix, S)
os.makedirs(RAIZ + '/videos', exist_ok=True); out = f'{RAIZ}/videos/{vid}.mp4'
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-framerate', str(FPS), '-i', W + '/fr/%06d.jpg', '-i', W + '/a.wav', '-c:v', 'libx264', '-pix_fmt', 'yuv420p',
                '-crf', '22', '-preset', 'medium', '-c:a', 'aac', '-b:a', '128k', '-shortest', '-movflags', '+faststart', out], check=True)
print('ok', out, TT)
