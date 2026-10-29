"""Narração humanizada para os canais (Passaporte da Bíblia e Raposa e Leão).
A voz neural sai "crua" de uma vez só, num ritmo de máquina. Aqui cada frase é gerada separada, com:
- variação leve de velocidade e tom por frase (pergunta sobe, frase curta desacelera, exclamação acelera);
- pausas de tamanho natural conforme a pontuação, e pausa maior depois de pergunta ao ouvinte;
- respiração suave antes de frases longas;
- tratamento de estúdio (graves, presença, de-esser, compressão e ambiência curta).
narrar(texto, voz, rate, pitch, semente) -> (áudio float32 44,1 kHz mono, [[palavra, segundo], ...])"""
import asyncio, hashlib, json, os, re, subprocess, time
import numpy as np, soundfile as sf, edge_tts
from scipy.signal import butter, lfilter

S = 44100
CACHE = '/tmp/claude-0/-home-user/5acf6937-9ac6-56e0-bc29-78bef210dc8b/scratchpad/vozcache'; os.makedirs(CACHE, exist_ok=True)

def frases(txt):
    partes = re.split(r'(?<=[.!?…:])\s+', txt.strip())
    return [p for p in partes if p.strip()]

async def _gera(txt, voz, rate, pitch, mp3):
    cm = edge_tts.Communicate(txt, voz, rate=rate, pitch=pitch, proxy=os.environ.get('HTTPS_PROXY'), boundary='WordBoundary'); ws = []
    with open(mp3, 'wb') as f:
        async for ch in cm.stream():
            if ch['type'] == 'audio': f.write(ch['data'])
            elif ch['type'] == 'WordBoundary': ws.append([ch['text'], ch['offset'] / 1e7])
    return ws

def _frase(txt, voz, rate, pitch):
    k = hashlib.sha1(f'{voz}|{rate}|{pitch}|{txt}'.encode()).hexdigest()[:20]; wav, js = f'{CACHE}/{k}.wav', f'{CACHE}/{k}.json'
    if not os.path.exists(js):
        for n in range(6):
            try: ws = asyncio.run(_gera(txt, voz, rate, pitch, wav[:-4] + '.mp3')); break
            except Exception as e: print('voz de novo', e); time.sleep(4 + 4 * n)
        else: raise RuntimeError('sem voz para: ' + txt)
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', wav[:-4] + '.mp3', '-ar', str(S), '-ac', '1', wav], check=True); os.remove(wav[:-4] + '.mp3')
        json.dump(ws, open(js, 'w'), ensure_ascii=False)
    a, _ = sf.read(wav); return a.astype(np.float32), json.load(open(js))

def _apara(a):
    """Tira o silêncio do começo e do fim (o gerador deixa sobra)."""
    fr = 441; n = len(a) // fr
    if n < 3: return a, 0.0
    e = np.sqrt(np.mean(a[:n * fr].reshape(n, fr) ** 2, axis=1)); lim = max(e.max() * 10 ** (-38 / 20), 1e-5)
    on = np.where(e > lim)[0]
    if not len(on): return a, 0.0
    i0 = max(0, on[0] - 2) * fr; i1 = min(n, on[-1] + 4) * fr
    return a[i0:i1], i0 / S

def _respiro(rng, dur):
    n = int(dur * S); x = rng.standard_normal(n)
    b, c = butter(2, [350 / (S / 2), 2600 / (S / 2)], 'band'); x = lfilter(b, c, x)
    u = np.linspace(0, 1, n); env = np.sin(np.pi * u) ** 1.6 * (0.6 + 0.4 * u)
    return (x * env / (np.abs(x).max() + 1e-9) * 10 ** (-34 / 20)).astype(np.float32)

def _pct(v): return f'{"+" if v >= 0 else ""}{int(round(v))}%'
def _hz(v): return f'{"+" if v >= 0 else ""}{int(round(v))}Hz'

def narrar(txt, voz='pt-BR-AntonioNeural', rate=0, pitch=0, semente=0, conversa=False):
    """rate em %, pitch em Hz (valores-base do canal). conversa=True quando a fala é direta ao ouvinte (mais calorosa)."""
    rng = np.random.default_rng(int(hashlib.md5(f'{semente}|{txt}'.encode()).hexdigest()[:8], 16))
    out, words, t = [], [], 0.0
    fs = frases(txt)
    for n, f in enumerate(fs):
        nw = len(f.split()); r = rate + rng.uniform(-3.5, 3.5); p = pitch + rng.uniform(-2.5, 2.5)
        if f.endswith('?'): p += 4; r -= 2
        elif f.endswith('!'): r += 3; p += 2
        if nw <= 4: r -= 5                      # frase curta = peso, mais devagar
        if conversa: r -= 3; p += 1.5
        a, ws = _frase(f, voz, _pct(r), _hz(p)); a, cut = _apara(a)
        if n and nw >= 12 and rng.random() < .7:   # respiração antes de frase longa
            br = _respiro(rng, rng.uniform(.22, .32)); out.append(br); t += len(br) / S
        words += [[w, round(float(max(t, t + o - cut)), 3)] for w, o in ws]
        out.append(a); t += len(a) / S
        if n < len(fs) - 1:
            fim = f[-1]; pa = {'?': rng.uniform(.55, .75), '!': rng.uniform(.32, .45), ':': rng.uniform(.22, .32), '…': rng.uniform(.6, .8)}.get(fim, rng.uniform(.3, .46))
            if f.rstrip(',').endswith(','): pa = rng.uniform(.18, .26)
            out.append(np.zeros(int(pa * S), np.float32)); t += pa
    a = np.concatenate(out) if out else np.zeros(1, np.float32)
    return estudio(a), words

def estudio(a):
    """Graves e presença, de-esser, compressão leve e uma ambiência curta (sala pequena)."""
    tmp = f'{CACHE}/_e{os.getpid()}'; sf.write(tmp + 'i.wav', a, S)
    flt = ('highpass=f=70,equalizer=f=160:t=q:w=1:g=2.2,equalizer=f=3200:t=q:w=1.4:g=1.6,deesser=i=0.35,'
           'acompressor=threshold=-20dB:ratio=2.4:attack=6:release=140:makeup=2,aecho=0.85:0.5:23|41:0.07|0.04')
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', tmp + 'i.wav', '-af', flt, '-ar', str(S), '-ac', '1', tmp + 'o.wav'], check=True)
    b, _ = sf.read(tmp + 'o.wav'); os.remove(tmp + 'i.wav'); os.remove(tmp + 'o.wav')
    return (b / (np.abs(b).max() + 1e-9) * .95).astype(np.float32)

if __name__ == '__main__':
    import sys
    a, w = narrar(sys.argv[1], rate=-4, pitch=-5, conversa='--conversa' in sys.argv)
    sf.write(sys.argv[2], a, S); print(len(a) / S, 's', w[:6])
