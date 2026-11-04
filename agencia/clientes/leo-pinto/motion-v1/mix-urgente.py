# Mix rápido: trilha (Incompetech, CC BY) + SFX sintetizados nos cortes do vídeo 1 do Leo.
import numpy as np, wave, sys
SR = 48000
rng = np.random.default_rng(7)
def env(n, a, r):
    e = np.ones(n); a = int(a*SR); r = int(r*SR)
    if a: e[:a] = np.linspace(0, 1, a)
    if r: e[-r:] *= np.linspace(1, 0, r)
    return e
def whoosh(d=.45, up=True):
    n = int(d*SR); x = rng.normal(0, 1, n)
    # filtro passa-banda móvel simples: média móvel de tamanho variável
    out = np.zeros(n); k0, k1 = (40, 4) if up else (4, 40)
    ks = np.linspace(k0, k1, n).astype(int)
    c = np.cumsum(np.insert(x, 0, 0))
    for i in range(n):
        k = max(ks[i], 1); j = max(i-k, 0); out[i] = (c[i+1]-c[j])/(i+1-j)
    out = out - np.convolve(out, np.ones(60)/60, 'same')*0.6
    e = np.sin(np.linspace(0, np.pi, n))**1.5
    return out/np.abs(out).max()*e*0.55
def boom(d=.9):
    n = int(d*SR); t = np.arange(n)/SR
    f = 95*np.exp(-t*6)+38
    s = np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-t*4.5)
    s += rng.normal(0, 1, n)*np.exp(-t*40)*0.25
    return s*0.9
def pop(d=.09):
    n = int(d*SR); t = np.arange(n)/SR
    return np.sin(2*np.pi*(900*np.exp(-t*30)+300)*t)*np.exp(-t*55)*0.45
def chime(d=1.6):
    n = int(d*SR); t = np.arange(n)/SR
    s = sum(np.sin(2*np.pi*f*t)*a for f, a in [(1046.5, .5), (1568, .3), (2093, .15)])
    return s*np.exp(-t*2.5)*env(n, .005, .2)*0.35
def riser(d=1.8):
    n = int(d*SR); x = rng.normal(0, 1, n); t = np.arange(n)/SR
    tone = np.sin(2*np.pi*np.cumsum(200+600*(t/d)**2)/SR)
    return (x*0.25+tone*0.5)*(t/d)**2*0.45
def ler_mp3_pcm(path):
    import subprocess, imageio_ffmpeg
    ff = imageio_ffmpeg.get_ffmpeg_exe()
    raw = subprocess.run([ff, '-v', 'error', '-i', path, '-f', 's16le', '-ac', '2', '-ar', str(SR), '-'], capture_output=True).stdout
    return np.frombuffer(raw, np.int16).reshape(-1, 2).astype(np.float32)/32768
mus_path, out_wav, inicio = sys.argv[1], sys.argv[2], float(sys.argv[3])
T = 40.0; N = int(T*SR)
mus = ler_mp3_pcm(mus_path)[int(inicio*SR):int(inicio*SR)+N]
mus = mus*env(N, .5, 1.6)[:, None]*0.55
sfx = np.zeros(N)
def put(sig, t, g=1.0):
    i = int(t*SR); j = min(i+len(sig), N); sfx[i:j] += sig[:j-i]*g
cortes = [float(x) for x in sys.argv[4].split(',')]
duck = np.ones(N)
for k, t in enumerate(cortes[1:], 1):
    put(whoosh(.42, k % 2 == 0), max(t-.32, 0), .8)
for t in [0.15, 0.55, 0.95, 1.35]: put(pop(), t, .7)
imp = cortes[1:-1]
for k, t in enumerate(imp):
    put(boom(.7 if k % 2 else .9), t+.05, .55 if k % 2 else .8)
    for d in (.35, .7): put(pop(), t+d, .45)
fim = cortes[-1]
put(riser(1.8), fim-1.85, .7); put(boom(1.0), fim+.05, .9); put(chime(), fim+.6, .9)
for t in imp[::2]+[fim]:
    i = int(t*SR); n = int(.6*SR); duck[i:i+n] = np.minimum(duck[i:i+n], .55+.45*np.linspace(0, 1, n))
mix = mus*duck[:, None] + sfx[:, None]*0.6
mix = mix/ max(1.0, np.abs(mix).max()/0.89)
pcm = (mix*32767).astype(np.int16)
with wave.open(out_wav, 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())
print('ok', out_wav)
