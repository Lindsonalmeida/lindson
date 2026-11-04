# Motion v1 do Leo · trilha + efeitos sonoros (conta Pedro, 04/11/2026).
# Lê as deixas geradas dos dados de cada vídeo (cues-vN.json, escritas pelo render.js), sintetiza os efeitos aqui mesmo
# (numpy, nada baixado), mistura com a música do Kevin MacLeod (CC BY 4.0), abaixa a música sob os impactos (ducking),
# normaliza para -14 LUFS (loudnorm em 2 passadas, pico real <= -1,5 dBTP) e troca o áudio do MP4 (AAC 192k 48 kHz).
# Uso: python3 audio.py <pasta-saida> v1 [v2 v3 v4]      (FFMPEG no ambiente; músicas em <pasta-saida>/assets/musica)
import sys, os, json, subprocess, wave, numpy as np

SR = 48000
DUR = 40.0
N = int(SR * DUR)
FF = os.environ.get('FFMPEG', 'ffmpeg')
# música por vídeo: arquivo, título (crédito) e início do trecho em segundos
MUSICA = {
    'v1': ('Inspired.mp3', 'Inspired', 0.0),
    'v2': ('Wholesome.mp3', 'Wholesome', 0.0),
    'v3': ('Feelin_Good.mp3', 'Feelin Good', 0.0),
    'v4': ('Carefree.mp3', 'Carefree', 0.0),
}
# nível de pico de cada efeito em relação ao pico da música (dB) — faixa pedida: -12 a -18 dB
NIVEL = {'boom': -12, 'whoosh': -15, 'riser': -15, 'chime': -14, 'pop': -18, 'key': -18}


def db(x): return 10 ** (x / 20)


def lowpass_var(x, fc):
    """passa-baixa de 1 polo com corte variando no tempo (fc em Hz por amostra)"""
    a = np.exp(-2 * np.pi * np.asarray(fc) / SR); y = np.empty_like(x); s = 0.0
    for i in range(len(x)):
        s = (1 - a[i]) * x[i] + a[i] * s; y[i] = s
    return y


def norm(x): m = np.max(np.abs(x)); return x / m if m > 0 else x


def env_ar(n, att, rel_pow=1.0):
    """envelope em sino: sobe até 'att' (fração) e desce"""
    t = np.linspace(0, 1, n); e = np.where(t < att, (t / att) ** 1.5, ((1 - t) / (1 - att)) ** (1.6 * rel_pow)); return e


def whoosh(d, rng, air=False, zoom=False):
    n = int(SR * max(.35, min(1.3, d + .25)))
    x = rng.standard_normal(n)
    t = np.linspace(0, 1, n)
    fc = 300 + 5200 * np.sin(np.pi * np.clip(t / .85, 0, 1)) ** 2 if not air else 200 + 1800 * np.sin(np.pi * t) ** 2
    y = lowpass_var(x, fc) - .6 * lowpass_var(x, fc * .25)          # banda: tira um pouco do grave
    y = norm(y) * env_ar(n, .55)
    if zoom:   # zoom-through ganha um tom que sobe
        ph = np.cumsum(2 * np.pi * (120 + 520 * t ** 2) / SR); y = y * .8 + .35 * np.sin(ph) * env_ar(n, .7)
    return norm(y) * (.6 if air else 1)


def pop(rng, k):
    n = int(SR * .09); t = np.arange(n) / SR
    f0 = 820 * (1 + .06 * ((k * 7) % 5 - 2))                           # leve variação de altura entre palavras
    f = f0 * np.exp(-t * 18) + 260
    y = np.sin(np.cumsum(2 * np.pi * f / SR)) * np.exp(-t * 55)
    y[:int(SR * .004)] += rng.standard_normal(int(SR * .004)) * .25 * np.linspace(1, 0, int(SR * .004))
    return norm(y)


def key(rng):
    n = int(SR * .06); t = np.arange(n) / SR
    click = rng.standard_normal(n) * np.exp(-t * 900)
    click = click - lowpass_var(click, np.full(n, 1500.0))            # passa-alta: estalo seco
    body = np.sin(2 * np.pi * (170 + rng.uniform(-20, 20)) * t) * np.exp(-t * 90) * .35
    return norm(click * rng.uniform(.75, 1) + body)


def boom(rng):
    n = int(SR * 1.1); t = np.arange(n) / SR
    f = 42 + 58 * np.exp(-t * 9)
    y = np.sin(np.cumsum(2 * np.pi * f / SR)) * np.exp(-t * 3.6)
    hit = lowpass_var(rng.standard_normal(n), np.full(n, 900.0)) * np.exp(-t * 40) * 3
    return norm(y + .5 * norm(hit) * np.exp(-t * 30))


def riser(d, rng):
    n = int(SR * d); t = np.linspace(0, 1, n)
    nz = lowpass_var(rng.standard_normal(n), 400 + 6000 * t ** 2)
    ph = np.cumsum(2 * np.pi * (180 + 900 * t ** 2.2) / SR)
    tone = (np.sin(ph) + .4 * np.sin(2 * ph)) * .25
    y = (norm(nz) * .8 + tone) * t ** 2.4
    y[-int(SR * .03):] *= np.linspace(1, 0, int(SR * .03))
    return norm(y)


def chime():
    n = int(SR * 1.8); t = np.arange(n) / SR; y = np.zeros(n)
    for f, a, dk in ((1318.5, 1, 2.6), (1760, .7, 3.2), (2637, .35, 4.5), (3520, .15, 6)):
        y += a * np.sin(2 * np.pi * f * t) * np.exp(-t * dk)
    y *= np.minimum(1, t / .006)
    return norm(y)


def pan(y, p):
    """p em -1..1 (escalar ou vetor) com lei de potência constante"""
    p = np.broadcast_to(np.asarray(p, float), y.shape); a = (p + 1) * np.pi / 4
    return np.stack([y * np.cos(a), y * np.sin(a)], 1)


def music(path, start):
    raw = subprocess.run([FF, '-v', 'error', '-ss', str(start), '-t', str(DUR), '-i', path, '-f', 'f32le', '-ac', '2', '-ar', str(SR), '-'], capture_output=True, check=True).stdout
    m = np.frombuffer(raw, np.float32).reshape(-1, 2).astype(np.float64)
    out = np.zeros((N, 2)); out[:min(N, len(m))] = m[:N]
    t = np.arange(N) / SR
    out *= np.clip(t / .5, 0, 1)[:, None] * np.clip((DUR - t) / 1.5, 0, 1)[:, None]     # fade-in 0,5 s e fade-out 1,5 s
    return out / np.max(np.abs(out)) * db(-1)


def write_wav(path, x):
    x = np.clip(x, -1, 1); w = wave.open(path, 'wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((x * 32767).astype('<i2').tobytes()); w.close()


def loudnorm(src, dst):
    a = subprocess.run([FF, '-hide_banner', '-i', src, '-af', 'loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json', '-f', 'null', '-'], capture_output=True, text=True).stderr
    j = json.loads(a[a.rindex('{'):a.rindex('}') + 1])
    af = (f"loudnorm=I=-14:TP=-1.5:LRA=11:measured_I={j['input_i']}:measured_TP={j['input_tp']}:measured_LRA={j['input_lra']}"
          f":measured_thresh={j['input_thresh']}:offset={j['target_offset']}:linear=true:print_format=summary")
    subprocess.run([FF, '-v', 'error', '-y', '-i', src, '-af', af, '-ar', str(SR), '-c:a', 'pcm_s16le', dst], check=True)


def one(out, v):
    cues = json.load(open(f'{out}/cues-{v}.json'))
    arq, titulo, ini = MUSICA[v]
    mus = music(f'{out}/assets/musica/{arq}', ini)
    sfx = np.zeros((N, 2)); duck = np.ones(N)
    rng = np.random.default_rng(int(v[1]) * 101)
    cont = {}
    for i, c in enumerate(cues):
        k, t0 = c['k'], c['t']; cont[k] = cont.get(k, 0) + 1
        if k == 'whoosh':
            y = whoosh(c.get('d', .4), rng, c.get('air'), c.get('zoom')); g = c.get('g', 1)
            t0 -= .12                                              # o pico do som cai no meio do movimento
            st = pan(y, np.linspace(-.5, .5, len(y)) if c.get('dir', 'x') == 'x' else 0)
            lvl = NIVEL['whoosh'] + 20 * np.log10(max(g, .2))
        elif k == 'pop': st = pan(pop(rng, i), ((i * 37) % 9 - 4) / 12); lvl = NIVEL['pop'] + 20 * np.log10(c.get('g', 1))
        elif k == 'key': st = pan(key(rng), rng.uniform(-.2, .2)); lvl = NIVEL['key']
        elif k == 'boom': st = pan(boom(rng), 0); lvl = NIVEL['boom']
        elif k == 'riser': st = pan(riser(c.get('d', 1.8), rng), 0); lvl = NIVEL['riser']
        elif k == 'chime': st = pan(chime(), .1); lvl = NIVEL['chime']
        else: continue
        a = max(0, int(t0 * SR)); b = min(N, a + len(st)); sfx[a:b] += st[:b - a] * db(lvl)
        # ducking: a música abaixa sob os efeitos fortes e volta suave
        dk = {'boom': -6, 'riser': -3, 'chime': -3}.get(k, -3.5 if (k == 'whoosh' and c.get('g', 0) >= .9) else 0)
        if dk:
            L = int(SR * (.6 if k != 'riser' else c.get('d', 1.8))); att = int(SR * .02)
            e = np.ones(L); e[:att] = np.linspace(1, db(dk), att); e[att:] = db(dk) + (1 - db(dk)) * (np.linspace(0, 1, L - att) ** 2 if k != 'riser' else 0)
            if k == 'riser': e[att:] = np.linspace(1, db(dk), L - att)
            aa = max(0, int(c['t'] * SR) - (0 if k != 'riser' else 0)); bb = min(N, aa + L); duck[aa:bb] = np.minimum(duck[aa:bb], e[:bb - aa])
    mix = mus * duck[:, None] + sfx
    mix /= max(1.0, np.max(np.abs(mix)) / db(-1))
    tmp = f'{out}/.{v}-mix.wav'; fin = f'{out}/.{v}-mix-norm.wav'
    write_wav(tmp, mix); loudnorm(tmp, fin)
    mp4 = f'{out}/leo-motion-{v}.mp4'; nov = f'{out}/.{v}-som.mp4'
    subprocess.run([FF, '-v', 'error', '-y', '-i', mp4, '-i', fin, '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-ar', str(SR),
                    '-t', str(DUR), '-movflags', '+faststart', nov], check=True)
    os.replace(nov, mp4); os.remove(tmp); os.remove(fin)
    print(v, titulo, cont)


if __name__ == '__main__':
    for v in sys.argv[2:]: one(sys.argv[1], v)
