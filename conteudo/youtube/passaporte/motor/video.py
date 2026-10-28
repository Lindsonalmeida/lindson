"""Passaporte da Bíblia — gera um vídeo (Short 9:16 ou longo 16:9) a partir de shorts.json / longos.json.
python3 video.py <arquivo.json> <id> [STEP=24 para prévia]  ->  ../videos/<id>.mp4"""
import json, sys, os, glob, re, base64, io, subprocess, asyncio, time
import numpy as np, soundfile as sf, edge_tts
from scipy.signal import butter, lfilter
from PIL import Image
D = os.path.dirname(os.path.abspath(__file__)); RAIZ = os.path.join(D, '..')
PROD = '/home/user/lindson/conteudo/produtos/passaporte'
sys.path.insert(0, PROD); from icones import icone
TMP = '/tmp/claude-0/-home-user/5acf6937-9ac6-56e0-bc29-78bef210dc8b/scratchpad/pv'
arq, vid = sys.argv[1], sys.argv[2]; STEP = int(os.environ.get('STEP', '1')); FPS = 24
spec = next(v for v in json.load(open(arq)) if v['id'] == vid)
W_, H_ = (1080, 1920) if spec['formato'] == 'short' else (1920, 1080)
W = f'{TMP}/{vid}'; os.makedirs(W + '/vz', exist_ok=True)

REG = {'Lei': '#D9573B', 'Históricos': '#E9A23B', 'Poéticos': '#E2668E', 'Profetas Maiores': '#3F9A55', 'Profetas Menores': '#9CC152',
       'Evangelhos e Atos': '#3B8EDB', 'Cartas': '#8466C4', 'Apocalipse': '#8E2C48'}
GUIAS = {g['livro']: g for f in glob.glob(PROD + '/dados/guias_*.json') for g in json.load(open(f))}
ICS = json.load(open(PROD + '/dados/icones.json'))

# pinturas de fundo escolhidas pelo assunto do trecho
PINT = {k: f'{RAIZ}/pinturas/{k}.jpg' for k in [os.path.basename(p)[:-4] for p in glob.glob(RAIZ + '/pinturas/*.jpg')]}
CHAVES = [('noe', r'No[ée]|arca|dil[úu]vio'), ('moises', r'Mois[ée]s|Lev[íi]tico|Lei|Êxodo|Sinai|tábuas'), ('davi', r'Davi|Salmo|Golias'),
          ('abraao', r'Abra[ãa]o|Isaque|Jac[óo]|G[êe]nesis'), ('salomao', r'Salom[ãa]o|Prov[ée]rbios|sabedoria'), ('pedro', r'Pedro|Marcos'),
          ('paulo', r'Paulo|Romanos|cartas?\b|Filipenses|Tiago'), ('apocalipse', r'Apocalipse|Jo[ãa]o viu|Patmos|fim dos tempos'),
          ('criacao', r'cria[çc][ãa]o|Ad[ãa]o|Eva|queda'), ('santa_ceia', r'ceia|disc[íi]pulos'), ('ressurreicao', r'ressurrei|t[úu]mulo vazio|ressuscit'),
          ('batismo', r'batism|Jo[ãa]o Batista'), ('sermao', r'Jesus|Evangelho'), ('emaus', r'caminho|viagem|rota'), ('madalena', r'Maria|mulher'),
          ('fuga_egito', r'Egito|Jos[ée]\b'), ('pastor', r'pastor|ovelha|Rute|campo')]
_cache = {}
def pintura(k):
    if k not in _cache:
        im = Image.open(PINT[k]).convert('RGB'); im.thumbnail((1400, 1400)); b = io.BytesIO(); im.save(b, 'JPEG', quality=78)
        _cache[k] = 'data:image/jpeg;base64,' + base64.b64encode(b.getvalue()).decode()
    return _cache[k]
def escolhe(txt, i):
    for k, rx in CHAVES:
        if k in PINT and re.search(rx, txt, re.I): return k
    pool = sorted(PINT); return pool[i % len(pool)]

ult = None
for i, g in enumerate(spec['seg']):
    T = g['tela']
    if T.get('icone'): T['icone'] = icone(T['icone'])
    if T['t'] == 'livro':
        L = GUIAS[T['livro']]; ic = ICS.get(L['livro'], {})
        T['dados'] = dict(n=L['n'], livro=L['livro'], caps=L['caps'], regiao=L['regiao'], frase=L['frase'], paradas=L['paradas'],
                          cor=REG[L['regiao']], fg='#1F2544' if L['regiao'] in ('Históricos', 'Profetas Menores') else '#fff', hero=icone(ic.get('hero')))
    k = escolhe(g['txt'] + ' ' + json.dumps(T, ensure_ascii=False)[:300], i)
    if k == ult: k = sorted(PINT)[(sorted(PINT).index(k) + 1) % len(PINT)]
    g['bg'] = pintura(k); ult = k
spec['cor'] = spec.get('capa', spec.get('capaA', {})).get('cor', '#3B8EDB')

# voz
S = 44100
async def tts(txt, out):
    c = edge_tts.Communicate(txt, 'pt-BR-FranciscaNeural', rate='+6%', proxy=os.environ.get('HTTPS_PROXY'), boundary='WordBoundary'); ws = []
    with open(out, 'wb') as f:
        async for ch in c.stream():
            if ch['type'] == 'audio': f.write(ch['data'])
            elif ch['type'] == 'WordBoundary': ws.append([ch['text'], round(ch['offset'] / 1e7, 3)])
    json.dump(ws, open(out[:-4] + '.json', 'w'), ensure_ascii=False)
vozes = []; t = 0.5
for i, g in enumerate(spec['seg']):
    mp = f'{W}/vz/{i:03d}.mp3'; wv = mp[:-4] + '.wav'
    if not os.path.exists(mp[:-4] + '.json'):
        for k in range(6):
            try: asyncio.run(tts(g['txt'], mp)); break
            except Exception as e: print('tts de novo', i, e); time.sleep(5 + 5 * k)
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', mp, '-ar', str(S), '-ac', '1', wv], check=True)
    a, _ = sf.read(wv); g['ini'] = max(0, t - .3); g['words'] = [[w, round(t + o, 3)] for w, o in json.load(open(mp[:-4] + '.json'))]
    vozes.append((t, a)); t += len(a) / S + (.7 if g['tela']['t'] in ('capitulo', 'abertura', 'livro') else .35)
for i, g in enumerate(spec['seg']): g['fim'] = spec['seg'][i + 1]['ini'] if i + 1 < len(spec['seg']) else t + 2.5
TT = round(t + 2.5, 2); spec['total'] = TT

curto = spec['formato'] == 'short'
SUB = dict(W=W_, H=H_, PADB=260 if curto else 150, F1=118 if curto else 104, F2=66 if curto else 54, F2B=96 if curto else 74, F3=40 if curto else 34,
           F4=34 if curto else 30, F5=26 if curto else 24, FN=150 if curto else 130, NUM=300 if curto else 260, CK=72 if curto else 64,
           HERO=230 if curto else 210, BIGC=600 if curto else 400, FC=58 if curto else 48, CAPY=1560 if curto else 930, MARCAY=70 if curto else 40)
html = open(D + '/video.html').read()
for k, v in SUB.items(): html = html.replace(f'__{k}__', str(v))
html = html.replace('__SPEC__', json.dumps(spec, ensure_ascii=False))
st = f'{W}/stage.html'; open(st, 'w').write(html)
js = f"""const {{chromium}}=require('playwright');const fs=require('fs');
(async()=>{{const b=await chromium.launch();const p=await b.newPage({{viewport:{{width:{W_},height:{H_}}}}});
p.on('pageerror',e=>console.log('ERR',e.message));await p.goto('file://{st}');await p.waitForFunction(()=>window.ready);await p.waitForTimeout(600);
fs.writeFileSync('{W}/sfx.json',JSON.stringify(await p.evaluate(()=>window.SFX)));fs.rmSync('{W}/fr',{{recursive:true,force:true}});fs.mkdirSync('{W}/fr');
const n=Math.floor({TT}*{FPS});for(let f=0;f<n;f+={STEP}){{await p.evaluate(t=>render(t),f/{FPS});await p.screenshot({{path:'{W}/fr/'+String(f).padStart(6,'0')+'.jpg',type:'jpeg',quality:88}})}}
await b.close()}})();"""
open(W + '/r.js', 'w').write(js); subprocess.run(['node', W + '/r.js'], check=True)
if STEP != 1: print('previa', W + '/fr', TT); sys.exit()

# trilha e efeitos
N = int(TT * S); rng = np.random.default_rng(3)
def lp(x, f): b, a = butter(2, f / (S / 2)); return lfilter(b, a, x)
def bp(x, lo, hi): b, a = butter(2, [lo / (S / 2), hi / (S / 2)], 'band'); return lfilter(b, a, x)
def tt_(d): return np.arange(int(d * S)) / S
def carimbo(): t = tt_(.45); f = 90 * np.exp(-t * 18) + 45; return (np.sin(2 * np.pi * np.cumsum(f) / S) * np.exp(-t * 12) + bp(rng.standard_normal(len(t)), 200, 2500) * np.exp(-t * 40) * .5) * .8
def whoosh(): t = tt_(.55); u = t / t[-1]; return bp(rng.standard_normal(len(t)), 400, 3000) * np.sin(np.pi * u) ** 2 * .25
def tic(): t = tt_(.12); return np.sin(2 * np.pi * 1200 * t) * np.exp(-t * 40) * .25
FX = dict(carimbo=carimbo, whoosh=whoosh, tic=tic)
tm = np.arange(N) / S; mix = np.zeros(N + 3 * S)
acordes = [(261.6, 329.6, 392.0), (220.0, 261.6, 329.6), (174.6, 220.0, 261.6), (196.0, 246.9, 293.7)]
for k in range(int(TT / 4) + 1):
    a0 = k * 4; m = (tm >= a0) & (tm < a0 + 4.5); x = tm[m] - a0
    env = np.minimum(1, x / .8) * np.exp(-x * .35)
    mix[:N][m] += sum(np.sin(2 * np.pi * f * x) * .5 + np.sin(4 * np.pi * f * x) * .12 for f in acordes[k % 4]) * env * .035
for at, n in json.load(open(W + '/sfx.json')):
    x = FX[n](); i = int(at * S); mix[i:i + len(x)] += x
for at, a in vozes: i = int(at * S); mix[i:i + len(a)] += a / np.max(np.abs(a)) * .9
mix = mix[:N]; mix = mix / np.max(np.abs(mix)) * .95; sf.write(W + '/a.wav', mix, S)
os.makedirs(RAIZ + '/videos', exist_ok=True); out = f'{RAIZ}/videos/{vid}.mp4'
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-framerate', str(FPS), '-i', W + '/fr/%06d.jpg', '-i', W + '/a.wav', '-c:v', 'libx264', '-pix_fmt', 'yuv420p',
                '-crf', '22', '-preset', 'medium', '-c:a', 'aac', '-b:a', '128k', '-shortest', '-movflags', '+faststart', out], check=True)
print('ok', out, TT)
