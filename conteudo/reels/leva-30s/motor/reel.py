"""Motor v2 da leva de Reels de 30 s do Lindson (@lindsonalmeida_), 08/11/2026.

Lê um Reels do roteiros.json (cenas com tempo, narração, texto de tela, visual, VFX, SFX, música, capa_cor) +
a ficha de produção em producao/<id>.json (que clipe, que foto, que tipo de cena) e renderiza:
  saida/<id>.mp4      1080×1920, 30 fps, H.264 + AAC, ~30 s, -14 LUFS
  saida/capa.jpg      capa 1080×1920 na cor do xadrez (e capa-4x5.jpg = recorte do grid)
  saida/quadros/*.jpg 6 quadros de conferência

Uso:
  python3 reel.py L30-01 [--voz provisoria|duble] [--saida DIR] [--capa amarelo,preto] [--step N]

Herda do motor antigo (conteudo/reels/motor/build.py): HTML desenhado quadro a quadro pelo Playwright,
SFX anotados pela própria cena (window.SFX) e mixagem em numpy. Novidades: vídeos de banco, foto recortada
em parallax, legenda palavra por palavra com tempo real da voz, SFX e trilha reais com crédito, ducking.
"""
import argparse, difflib, json, os, re, shutil, subprocess, sys, unicodedata
import numpy as np, soundfile as sf

M = os.path.dirname(os.path.abspath(__file__)); LEVA = os.path.dirname(M)
BANCO = os.path.join(LEVA, 'banco'); FOTOS = os.environ.get('REEL_FOTOS', os.path.join(LEVA, 'fotos'))  # fotos: FORA do Git
sys.path.insert(0, M); import voz
S = 44100; FPS = 30

ap = argparse.ArgumentParser()
ap.add_argument('id'); ap.add_argument('--voz', default='provisoria'); ap.add_argument('--saida')
ap.add_argument('--capa', default=None, help='cores das capas a gerar (ex.: amarelo,preto); padrão = capa_cor do roteiro')
ap.add_argument('--step', type=int, default=1, help='>1 = prévia rápida (só quadros, sem vídeo)')
ap.add_argument('--work', default=os.environ.get('REEL_WORK', '/tmp/reel2'))
a = ap.parse_args()

rot = json.load(open(os.path.join(LEVA, 'roteiros.json')))
R = next(r for r in rot['reels'] if r['id'] == a.id)
P = json.load(open(os.path.join(M, 'producao', a.id + '.json')))
OUT = a.saida or os.path.join(LEVA, 'saida', a.id); os.makedirs(OUT + '/quadros', exist_ok=True)
W = a.work; shutil.rmtree(W, ignore_errors=True); os.makedirs(W)
for d in ('fontes',): os.symlink(os.path.join(M, d), os.path.join(W, d))


def norm(w):
    w = unicodedata.normalize('NFD', w.lower()); w = ''.join(c for c in w if unicodedata.category(c) != 'Mn')
    w = re.sub(r'[^a-z0-9]', '', w)
    return {'um': '1', 'dois': '2', 'tres': '3', 'quatro': '4', 'cinco': '5', 'seis': '6', 'sete': '7', 'zap': 'whatsapp'}.get(w, w)


# ---------------- 1. voz ----------------
blocos = R['blocos_voz']
rate = P.get('voz_rate', '+10%')
for tent in range(4):
    audio, bw = voz.narrar(blocos, a.voz, **({'rate': rate} if a.voz == 'provisoria' else {}))
    if len(audio) / S <= P.get('voz_max', 28.6) or a.voz != 'provisoria': break
    rate = f'+{int(rate.strip("+%")) + 6}%'
V0 = P.get('voz_ini', 0.25)
bw = [(w, s + V0, e + V0) for w, s, e in bw]
print(f'voz {a.voz}: {len(audio)/S:.1f} s, rate {rate}')

# ---------------- 2. tempo das cenas pelo tempo real da fala ----------------
cenas = R['cenas']; prod = P['cenas']
toks = []  # (cena, palavra exibida)
for k, c in enumerate(cenas):
    for w in c['narracao'].split(): toks.append((k, w))
A = [norm(w) for _, w in toks]; Bn = [norm(w) for w, _, _ in bw]
sm = difflib.SequenceMatcher(a=A, b=Bn, autojunk=False); mapa = {}
for blk in sm.get_matching_blocks():
    for j in range(blk.size): mapa[blk.a + j] = blk.b + j
tw = []  # tempo de cada palavra do roteiro (interpola as que não casaram)
for i in range(len(toks)):
    if i in mapa: tw.append(bw[mapa[i]][1:])
    else: tw.append(None)
for i in range(len(tw)):
    if tw[i] is None:
        prv = next((tw[j][1] for j in range(i - 1, -1, -1) if tw[j]), V0)
        nxt = next((tw[j][0] for j in range(i + 1, len(tw)) if tw[j]), prv + .3)
        tw[i] = (prv + .02, max(prv + .05, (prv + nxt) / 2))
ic = next((k for k, c in enumerate(cenas) if norm(R['cta_palavra']) in [norm(w) for w in c['narracao'].split()]), None)
fim_voz = V0 + len(audio) / S
CAUDA = P.get('cauda', 1.3)
if ic is not None:  # a CTA ganha fôlego: silêncio inserido antes dela e segurado depois da palavra
    i_cta = next(i for i, (kk, _) in enumerate(toks) if kk == ic)
    folga = max(0.0, min(P.get('pausa_cta', 1.2), 30.0 - (fim_voz + CAUDA)))
    i_end = next((i for i, (kk, _) in enumerate(toks) if kk == ic + 1), None)
    if folga > .05 and i_end is not None:
        tc = tw[i_end][0] - .12; ins = int((tc - V0) * S)
        audio = np.concatenate([audio[:ins], np.zeros(int(folga * S), np.float32), audio[ins:]])
        tw = [(x + folga, y + folga) if x >= tc else (x, y) for x, y in tw]
        fim_voz += folga
TOTAL = min(30.5, max(P.get('total_min', 20.0), fim_voz + CAUDA))
segs = []
for k, c in enumerate(cenas):
    idx = [i for i, (kk, _) in enumerate(toks) if kk == k]
    s0 = 0.0 if k == 0 else tw[idx[0]][0] - P.get('antecipa', .16)
    pr = dict(prod[k]) if k < len(prod) else {}
    words = [[toks[i][1], round(tw[i][0], 3)] for i in idx]
    segs.append(dict(pr, s=round(s0, 3), words=words, _idx=idx))
# #166 corte no beat: puxa cada corte para a batida mais próxima da trilha (janela -0,15 s / +0,08 s)
if P.get('beat_sync'):
    try:
        import librosa
        y, sr = librosa.load(os.path.join(BANCO, 'trilha', P['trilha']), sr=22050, offset=P.get('trilha_ini', 0), duration=40)
        _, bt = librosa.beat.beat_track(y=y, sr=sr); beats = librosa.frames_to_time(bt, sr=sr)
        for s in segs[1:]:
            c = min(beats, key=lambda b: abs(b - s['s']))
            if -.15 <= c - s['s'] <= .08: s['s'] = round(float(c), 3)
    except Exception as ex: print('beat sync off:', ex)
for k in range(len(segs) - 1): segs[k]['e'] = segs[k + 1]['s']
segs[-1]['e'] = TOTAL
for k, (s, c) in enumerate(zip(segs, cenas)):
    lt = lambda t: round(t - s['s'], 3)
    nw = [(norm(w), t) for w, t in s['words']]
    def quando(alvo, d=None):
        alvo = norm(alvo)
        for w, t in nw:
            if w == alvo: return lt(t)
        return d
    # manchete: cada palavra entra quando é dita (ou espaçada no começo da cena)
    head, last = [], .08
    for j, w in enumerate(s.get('texto', c['texto_tela_palavras'])):
        t = quando(s.get('ancoras', {}).get(w, w)); t = t if t is not None else last + (.3 if j else 0)
        last = max(t, last); head.append([w, round(last, 3)])
    s['head'] = head
    s['hits'] = [h for h in (quando(x) for x in s.get('hit', [])) if h is not None]
    s['vfx'] = s.get('vfx', [])
    if s['tipo'] == 'cta':
        s['palavra'] = R['cta_palavra']; s['entrega'] = P.get('entrega', R['entrega_no_video'])
        s['pillAt'] = quando(R['cta_palavra'], .8)
        if s.get('foto') and not s.get('lipsync'): shutil.copy(os.path.join(FOTOS, s['foto']), os.path.join(W, os.path.basename(s['foto']))); s['foto'] = os.path.basename(s['foto'])
    if s['tipo'] == 'perfil' and s.get('modo') == 'bio':
        s['riscos'] = s.get('riscos') or [x for x in (quando(y) for y in s.get('riscar_em', [])) if x is not None] or None
    for key in ('extraAt', 'badgeAt', 'freeze', 'riscoAt', 'carimboAt', 'cartaoAt', 'digitarAt'):
        if isinstance(s.get(key), str): s[key] = quando(s[key], None if key == 'freeze' else .3)
    if s.get('tempos_em'):  # itens de lista/conversa entram quando a palavra é dita
        last = .2; ts = []
        for x in s.pop('tempos_em'):
            t = x if isinstance(x, (int, float)) else quando(x); t = t if t is not None else last + .45; last = t; ts.append(round(t, 3))
        s['tempos'] = ts
    if s.get('foto') and s['tipo'] == 'foto':
        shutil.copy(os.path.join(FOTOS, s['foto']), os.path.join(W, os.path.basename(s['foto']))); s['foto'] = os.path.basename(s['foto'])
    # SFX da ficha: [palavra|segundos, som, ganho]
    sx = []
    for at, kind, g in s.get('sons', []):
        t = at if isinstance(at, (int, float)) else quando(at)
        if t is not None: sx.append([t, kind, g])
    for h in s['hits']: sx.append([h, s.get('som_hit', 'impacto-intro'), 1.0])
    if s.get('riser') and s['hits']: sx.append([s['hits'][0], 'riser-tech', .8])
    s['sfx'] = sx
    del s['_idx']

# ---------------- 3. clipes de banco: quadros 30 fps ----------------
clips = {}
for s in segs:
    for key in ('clip', 'lipsync'):
        if s.get(key) and s[key] not in clips:
            src = os.path.join(BANCO, 'video', s[key] + '.mp4') if key == 'clip' else os.path.join(FOTOS, s[key])
            d = os.path.join(W, 'clips', s[key]); os.makedirs(d)
            subprocess.run(['ffmpeg', '-v', 'error', '-i', src, '-vf', 'fps=30,scale=1080:1920', '-q:v', '3', d + '/%04d.jpg'], check=True)
            clips[s[key]] = len(os.listdir(d))
TL = dict(segs=segs, total=TOTAL, clips=clips, rascunho='RASCUNHO · VOZ PROVISÓRIA' if a.voz != 'duble' else '')
json.dump(TL, open(OUT + '/timeline.json', 'w'), ensure_ascii=False, indent=1)
open(W + '/palco.html', 'w').write(open(M + '/palco.html').read().replace('__TL__', json.dumps(TL, ensure_ascii=False)))

# ---------------- 4. capas ----------------
NODE = subprocess.check_output(['npm', 'root', '-g']).decode().strip()
CH = os.environ.get('CHROMIUM', '/opt/pw-browsers/chromium')
cores = (a.capa or R.get('capa_cor', 'amarelo')).split(',')
for cor in cores:
    C = dict(P['capa'], cor=cor); C.update(P['capa'].get(cor, {}))
    from PIL import Image as _I
    _im = _I.open(os.path.join(FOTOS, C['foto'])).convert('RGBA'); _im = _im.crop(_im.getbbox())  # recorte justo: ele grande na capa
    C['foto'] = os.path.basename(C['foto']); _im.save(os.path.join(W, C['foto']))
    if C.get('auto', True):  # largura pelo ombro: ocupa ~100% da largura, cabeça logo abaixo do topo do miolo 4:5
        C['fw'] = int(1080 * 1.12); C['fx'] = int((1080 - C['fw']) / 2); C['fy'] = 330
    open(W + f'/capa-{cor}.html', 'w').write(open(M + '/capa.html').read().replace('__CAPA__', json.dumps(C, ensure_ascii=False)))
js = """const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'%s'});const p=await b.newPage({viewport:{width:1080,height:1920}});
for(const c of %s){await p.goto('file://%s/capa-'+c+'.html');await p.waitForFunction(()=>window.ready);await p.screenshot({path:'%s/capa-'+c+'.png'})}await b.close()})();""" % (CH, json.dumps(cores), W, W)
open(W + '/capa.js', 'w').write(js); subprocess.run(['node', W + '/capa.js'], check=True, env={**os.environ, 'NODE_PATH': NODE})
from PIL import Image
for cor in cores:
    im = Image.open(W + f'/capa-{cor}.png').convert('RGB'); nome = 'capa' if cor == cores[0] else f'capa-{cor}'
    if len(cores) > 1: nome = f'capa-{cor}'
    im.save(OUT + f'/{nome}.jpg', quality=92); im.crop((0, 285, 1080, 1635)).save(OUT + f'/{nome}-4x5.jpg', quality=90)
capa1 = OUT + ('/capa.jpg' if len(cores) == 1 else f'/capa-{R.get("capa_cor", cores[0])}.jpg')
if not os.path.exists(capa1): capa1 = OUT + f'/capa-{cores[0]}.jpg'

# ---------------- 5. quadros ----------------
n = int(round(TOTAL * FPS))
js = """const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const b=await chromium.launch({executablePath:'%s'});const p=await b.newPage({viewport:{width:1080,height:1920}});
p.on('pageerror',e=>console.log('ERR',e.message));await p.goto('file://%s/palco.html');await p.waitForFunction(()=>window.ready);
fs.writeFileSync('%s/sfx.json',JSON.stringify(await p.evaluate(()=>window.SFX)));fs.mkdirSync('%s/fr',{recursive:true});
for(let f=0;f<%d;f+=%d){await p.evaluate(t=>window.render(t),f/30);await p.screenshot({path:'%s/fr/'+String(f).padStart(5,'0')+'.jpg',type:'jpeg',quality:90})}
await b.close()})();""" % (CH, W, W, W, n, a.step, W)
open(W + '/r.js', 'w').write(js); subprocess.run(['node', W + '/r.js'], check=True, env={**os.environ, 'NODE_PATH': NODE})
# 6 quadros de conferência: meio das cenas principais
ii = sorted(set(round(x * (len(segs) - 1) / 5) for x in range(6)))
alvo = P.get('conferir') or [segs[i]['s'] + (segs[i]['e'] - segs[i]['s']) * .7 for i in ii]
for j, t in enumerate(alvo[:6]):
    f = int(t * FPS) // a.step * a.step
    shutil.copy(W + f'/fr/{f:05d}.jpg', OUT + f'/quadros/q{j+1}-{t:05.2f}s.jpg')
if a.step != 1: print('prévia:', OUT); sys.exit()
Image.open(capa1).resize((1080, 1920)).save(W + '/fr/00000.jpg', quality=92)  # 1º quadro = capa (miniatura do Reels)

# ---------------- 6. áudio: voz + trilha com ducking + SFX ----------------
N = int(TOTAL * S) + S


def load(path):
    o = W + '/a.wav'; subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', path, '-ac', '1', '-ar', str(S), o], check=True)
    x, _ = sf.read(o, dtype='float32'); return x


def add(buf, sig, at, g=1.0):
    i = int(at * S)
    if i < 0: sig = sig[-i:]; i = 0
    j = min(len(buf), i + len(sig))
    if j > i: buf[i:j] += sig[:j - i] * g


v = np.zeros(N, np.float32); add(v, audio, V0)
kit = json.load(open(os.path.join(BANCO, 'sfx', 'kit.json')))
fx = np.zeros(N, np.float32)
cortes = [s['s'] for s in segs[1:]]
eventos = [(t, 'whoosh-rapido', .55) for t in cortes] + [tuple(e) for e in json.load(open(W + '/sfx.json'))]
for t, k, g in eventos:
    if k not in kit: print('SFX desconhecido', k); continue
    x = load(os.path.join(BANCO, 'sfx', kit[k]['arquivo'])); x = x / (np.sqrt((x ** 2).mean()) + 1e-9) * .08  # nivela o kit
    add(fx, x, t - kit[k]['pico'], g)
mus = load(os.path.join(BANCO, 'trilha', P['trilha']))[int(P.get('trilha_ini', 0) * S):]
while len(mus) < N: mus = np.concatenate([mus, mus])
mus = mus[:N] / (np.sqrt((mus[:N] ** 2).mean()) + 1e-9) * .1
# ducking: trilha cai ~18 dB sob a voz (ataque 60 ms, soltura 350 ms)
env = np.convolve(np.abs(v), np.ones(int(.05 * S)) / int(.05 * S), 'same'); on = (env > env.max() * .04).astype(np.float32)
g = np.empty_like(on); cur = 0.0
att, rel = 1 - np.exp(-1 / (.06 * S)), 1 - np.exp(-1 / (.35 * S))
for i in range(len(on)):
    cur += (on[i] - cur) * (att if on[i] > cur else rel); g[i] = cur
duck = 10 ** ((-18 * g * P.get('duck', 1.0) + 0) / 20) * 10 ** (-4 / 20)
mus *= duck
for s in segs:  # corte de batida antes do impacto marcado ("drop")
    if s.get('drop'):
        for h in s['hits']:
            i0, i1 = int((s['s'] + h - .32) * S), int((s['s'] + h) * S); mus[i0:i1] *= np.linspace(1, 0, max(1, i1 - i0)) ** 3 * 0 + 0.05
fade = np.ones(N, np.float32); fo = int(1.5 * S); e = int(TOTAL * S); fade[e - fo:e] = np.linspace(1, 0, fo); fade[e:] = 0
mix = (v * 1.0 + mus + fx * .9) * fade
sf.write(W + '/mix.wav', mix[:int(TOTAL * S)], S)
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', W + '/mix.wav', '-af', 'loudnorm=I=-14:TP=-1.5:LRA=11', '-ar', '48000', W + '/mixn.wav'], check=True)
mp4 = OUT + f'/{a.id}.mp4'
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-framerate', '30', '-i', W + '/fr/%05d.jpg', '-i', W + '/mixn.wav', '-c:v', 'libx264', '-preset', 'medium',
                '-crf', '22', '-maxrate', '6M', '-bufsize', '12M', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k', '-shortest', '-movflags', '+faststart', mp4], check=True)
print(mp4, round(TOTAL, 2), 's')
