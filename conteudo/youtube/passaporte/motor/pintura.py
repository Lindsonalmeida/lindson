"""Estilo "Pintura Viva": gravuras de Doré com profundidade 3D, luz de vela e narração.
python3 pintura.py <arquivo.json> <id> [STEP=24 prévia] -> ../videos/<id>.mp4"""
import json, sys, os, io, base64, subprocess, asyncio, time
import numpy as np, soundfile as sf, edge_tts, cv2, onnxruntime as ort
from scipy.signal import butter, lfilter
from PIL import Image, ImageFilter
D = os.path.dirname(os.path.abspath(__file__)); RAIZ = os.path.join(D, '..'); DORE = RAIZ + '/dore'
TMP = '/tmp/claude-0/-home-user/5acf6937-9ac6-56e0-bc29-78bef210dc8b/scratchpad'
MODELO = TMP + '/modelos/depth.onnx'
arq, vid = sys.argv[1], sys.argv[2]; STEP = int(os.environ.get('STEP', '1')); FPS = 30
spec = next(v for v in json.load(open(arq)) if v['id'] == vid)
curto = spec.get('formato', 'short') == 'short'; W_, H_ = (1080, 1920) if curto else (1920, 1080)
W = f'{TMP}/pv/{vid}'; os.makedirs(W + '/vz', exist_ok=True); os.makedirs(DORE + '/prof', exist_ok=True)

_s = None
def profundidade(n):
    f = f'{DORE}/prof/{n}.png'
    if not os.path.exists(f):
        global _s
        _s = _s or ort.InferenceSession(MODELO, providers=['CPUExecutionProvider'])
        im = cv2.imread(f'{DORE}/{n}.jpg')[:, :, ::-1]
        x = cv2.resize(im, (518, 518)).astype(np.float32) / 255; x = ((x - [.485, .456, .406]) / [.229, .224, .225]).transpose(2, 0, 1)[None].astype(np.float32)
        d = _s.run(None, {'pixel_values': x})[0][0]; d = (d - d.min()) / (d.max() - d.min())
        d = cv2.GaussianBlur(cv2.resize(d, (im.shape[1], im.shape[0])), (0, 0), 3)
        cv2.imwrite(f, (d * 255).astype(np.uint8))
    return f
def data(path, scale=None, q=90):
    im = Image.open(path).convert('RGB')
    if scale: im = im.resize((int(im.width * scale), int(im.height * scale)), Image.LANCZOS).filter(ImageFilter.UnsharpMask(2, 60, 2))
    b = io.BytesIO(); im.save(b, 'JPEG', quality=q); return 'data:image/jpeg;base64,' + base64.b64encode(b.getvalue()).decode()
for c in spec['cenas']:
    c['img'] = data(f"{DORE}/{c['gravura']}.jpg", 2.2); c['dep'] = data(profundidade(c['gravura']), 1.0, 85)

S = 44100
sys.path.insert(0, os.path.join(RAIZ, '..', 'comum')); from voz_humana import narrar
import zlib; SEM = zlib.crc32(vid.encode()); rng0 = np.random.default_rng(SEM)
os.makedirs(W + '/vz2', exist_ok=True)
# a narração começa logo (gancho nos primeiros segundos); o título de abertura aparece por cima da 1ª cena
vozes = []; t = .35
for i, c in enumerate(spec['cenas']):
    wv = f'{W}/vz2/{i:03d}.wav'; js = wv[:-4] + '.json'
    if not os.path.exists(js):
        a, ws = narrar(c['txt'], rate=-4, pitch=-5, semente=SEM, conversa=bool(c.get('interage')))
        sf.write(wv, a, S); json.dump(ws, open(js, 'w'), ensure_ascii=False)
    a, _ = sf.read(wv); c['ini'] = max(0, t - .5); c['words'] = [[w, round(t + o, 3)] for w, o in json.load(open(js))]
    vozes.append((t, a)); t += len(a) / S + rng0.uniform(.45, .75) + (.7 if (c.get('interage') or {}).get('tipo') in ('comenta', 'checkin') else 0)
spec['cenas'][0]['ini'] = 0
for i, c in enumerate(spec['cenas']): c['fim'] = spec['cenas'][i + 1]['ini'] if i + 1 < len(spec['cenas']) else t + 2.5
TT = round(t + 2.5, 2)
if not curto:
    import tempos; tempos.salva(vid, tempos.capitulos(spec, [c['ini'] for c in spec['cenas']]))
spec['titulo_tela']['fim'] = spec['titulo_tela'].get('dur', 2.6)

spec['estilo'] = dict(abre=SEM % 3, fecha=SEM // 3 % 3)
SUB = dict(GR='.07' if curto else '.02', W=W_, H=H_, FT=104 if curto else 96, FS=30, FV=76 if curto else 58, FR=30, VY=1180 if curto else 640, FC=62 if curto else 50, CY=1560 if curto else 900, MY=70 if curto else 34, IY=200 if curto else 70, IW=960 if curto else 780, IF=56 if curto else 36, IS=27 if curto else 21, T2=300 if curto else 120, FT2=96 if curto else 84, T3=520 if curto else 260, FT3=84 if curto else 72)
html = open(D + '/pintura.html').read()
for k, v in SUB.items(): html = html.replace(f'__{k}__', str(v))
st = f'{W}/stage.html'; open(st, 'w').write(html.replace('__SPEC__', json.dumps(spec, ensure_ascii=False)))
js = f"""const {{chromium}}=require('playwright');const fs=require('fs');
(async()=>{{const b=await chromium.launch({{args:['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader']}});const p=await b.newPage({{viewport:{{width:{W_},height:{H_}}}}});
p.on('pageerror',e=>console.log('ERR',e.message));p.on('console',m=>console.log(m.text()));await p.goto('file://{st}');await p.waitForFunction(()=>window.ready,null,{{timeout:120000}});await p.waitForTimeout(500);
if(!process.env.RETOMAR)fs.rmSync('{W}/fr',{{recursive:true,force:true}});fs.mkdirSync('{W}/fr',{{recursive:true}});
const n=Math.floor({TT}*{FPS});for(let f=0;f<n;f+={STEP}){{const q='{W}/fr/'+String(f).padStart(6,'0')+'.jpg';if(process.env.RETOMAR&&fs.existsSync(q)&&fs.statSync(q).size>20000)continue;await p.evaluate(t=>render(t),f/{FPS});await p.screenshot({{path:'{W}/fr/'+String(f).padStart(6,'0')+'.jpg',type:'jpeg',quality:90}})}}
await b.close()}})();"""
open(W + '/r.js', 'w').write(js); subprocess.run(['node', W + '/r.js'], check=True)
if STEP != 1: print('previa', W + '/fr', TT); sys.exit()

# trilha: cordas graves e coro sintético + batidas nas trocas de cena
N = int(TT * S); tm = np.arange(N) / S; rng = np.random.default_rng(11); mix = np.zeros(N + 3 * S)
def lp(x, f): b, a = butter(2, f / (S / 2)); return lfilter(b, a, x)
PROG = [[(73.42, 110.0, 146.8, 174.6), (65.41, 98.0, 130.8, 164.8), (58.27, 87.31, 116.5, 146.8), (65.41, 98.0, 130.8, 155.6)],
        [(65.41, 98.0, 130.8, 155.6), (51.91, 77.78, 103.8, 130.8), (58.27, 87.31, 116.5, 146.8), (49.0, 73.42, 98.0, 116.5)],
        [(55.0, 82.41, 110.0, 130.8), (73.42, 110.0, 146.8, 174.6), (49.0, 73.42, 98.0, 123.5), (65.41, 98.0, 130.8, 164.8)],
        [(61.74, 92.5, 123.5, 146.8), (55.0, 82.41, 110.0, 138.6), (49.0, 73.42, 98.0, 123.5), (55.0, 82.41, 110.0, 130.8)]]
acordes = PROG[SEM % len(PROG)]; PASSO = (5, 6, 7, 8)[SEM // 7 % 4]
for k in range(int(TT / PASSO) + 1):
    a0 = k * PASSO; m = (tm >= a0) & (tm < a0 + PASSO + 1); x = tm[m] - a0; env = np.minimum(1, x / 2) * np.minimum(1, (PASSO + 1 - x) / 1.5)
    sinal = sum(np.sin(2 * np.pi * f * x + .3 * np.sin(x * 5 + j)) + .35 * np.sin(4 * np.pi * f * x) for j, f in enumerate(acordes[k % 4]))
    mix[:N][m] += sinal * env * .045
mix[:N] = lp(mix[:N], 1800)
def boom(): x = np.arange(int(1.4 * S)) / S; f = 42 + 50 * np.exp(-x * 9); return np.sin(2 * np.pi * np.cumsum(f) / S) * np.exp(-x * 2.8) * .9
for c in spec['cenas'][1:]: i = int(c['ini'] * S); b = boom() * .5; mix[i:i + len(b)] += b
b = boom(); mix[:len(b)] += b
def plim(): x = np.arange(int(.9 * S)) / S; return (np.sin(2 * np.pi * 1046 * x) + .5 * np.sin(2 * np.pi * 1568 * x)) * np.exp(-x * 6) * .22
for c in spec['cenas']:
    if c.get('interage'): i = int((c['ini'] + .55) * S); b = plim(); mix[i:i + len(b)] += b
for at, a in vozes: i = int(at * S); mix[i:i + len(a)] += a / np.max(np.abs(a)) * .95
mix = mix[:N]; mix = mix / np.max(np.abs(mix)) * .95; sf.write(W + '/a.wav', mix, S)
os.makedirs(RAIZ + '/videos', exist_ok=True); out = f'{RAIZ}/videos/{vid}.mp4'
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-framerate', str(FPS), '-i', W + '/fr/%06d.jpg', '-i', W + '/a.wav', '-c:v', 'libx264', '-pix_fmt', 'yuv420p',
                '-crf', '20', '-preset', 'medium', '-c:a', 'aac', '-b:a', '160k', '-shortest', '-movflags', '+faststart', out], check=True)
print('ok', out, TT)
