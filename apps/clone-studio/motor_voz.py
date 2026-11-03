"""Motor de voz do Clone Studio (conta Pedro, 03/11/2026).
Clona a voz de uma amostra (Chatterbox Multilingual, MIT) e humaniza a fala do mesmo jeito que o
conteudo/youtube/comum/voz_humana.py faz nos canais: cada frase sai separada, com variação leve de
expressão, pausa conforme a pontuação, respiração antes de frase longa e tratamento de estúdio.
O código é autocontido para rodar no Windows do Lindson (sem os caminhos fixos da nuvem)."""
import hashlib, os, re, subprocess, tempfile
import numpy as np, soundfile as sf
from scipy.signal import butter, lfilter

S = 44100
_modelo = None


def ffmpeg():
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except Exception:
        return 'ffmpeg'


def dispositivo():
    import torch
    if torch.cuda.is_available(): return 'cuda'
    return 'cpu'


def modelo():
    global _modelo
    if _modelo is None:
        from chatterbox.mtl_tts import ChatterboxMultilingualTTS
        _modelo = ChatterboxMultilingualTTS.from_pretrained(device=dispositivo())
    return _modelo


def frases(txt):
    return [p for p in re.split(r'(?<=[.!?…:])\s+', txt.strip()) if p.strip()]


def _reamostra(a, sr):
    if sr == S: return a.astype(np.float32)
    n = int(len(a) * S / sr)
    return np.interp(np.linspace(0, len(a) - 1, n), np.arange(len(a)), a).astype(np.float32)


def _apara(a):
    """Tira o silêncio do começo e do fim de cada frase."""
    fr = 441; n = len(a) // fr
    if n < 3: return a
    e = np.sqrt(np.mean(a[:n * fr].reshape(n, fr) ** 2, axis=1)); lim = max(e.max() * 10 ** (-38 / 20), 1e-5)
    on = np.where(e > lim)[0]
    if not len(on): return a
    return a[max(0, on[0] - 2) * fr:min(n, on[-1] + 4) * fr]


def _respiro(rng, dur):
    n = int(dur * S); x = rng.standard_normal(n)
    b, c = butter(2, [350 / (S / 2), 2600 / (S / 2)], 'band'); x = lfilter(b, c, x)
    u = np.linspace(0, 1, n); env = np.sin(np.pi * u) ** 1.6 * (0.6 + 0.4 * u)
    return (x * env / (np.abs(x).max() + 1e-9) * 10 ** (-34 / 20)).astype(np.float32)


def estudio(a):
    """Graves e presença, de-esser, compressão leve e ambiência curta (igual ao voz_humana.py)."""
    d = tempfile.mkdtemp(); i, o = os.path.join(d, 'i.wav'), os.path.join(d, 'o.wav')
    sf.write(i, a, S)
    flt = ('highpass=f=70,equalizer=f=160:t=q:w=1:g=2.2,equalizer=f=3200:t=q:w=1.4:g=1.6,deesser=i=0.35,'
           'acompressor=threshold=-20dB:ratio=2.4:attack=6:release=140:makeup=2,aecho=0.85:0.5:23|41:0.07|0.04')
    subprocess.run([ffmpeg(), '-y', '-loglevel', 'error', '-i', i, '-af', flt, '-ar', str(S), '-ac', '1', o], check=True)
    b, _ = sf.read(o)
    return (b / (np.abs(b).max() + 1e-9) * .95).astype(np.float32)


def narrar(txt, amostra, expressao=0.5, semente=0, humanizar=True, progresso=None):
    """txt -> áudio float32 44,1 kHz mono com a voz da amostra (wav de 10 s a 2 min, voz limpa)."""
    m = modelo(); rng = np.random.default_rng(int(hashlib.md5(f'{semente}|{txt}'.encode()).hexdigest()[:8], 16))
    fs = frases(txt) if humanizar else [txt.strip()]
    out = []
    for n, f in enumerate(fs):
        if progresso: progresso((n, len(fs)), desc=f'Frase {n + 1} de {len(fs)}')
        ex = expressao + (rng.uniform(-.08, .08) if humanizar else 0)
        if f.endswith('!'): ex += .1
        w = m.generate(f, language_id='pt', audio_prompt_path=amostra, exaggeration=float(np.clip(ex, .25, 1)))
        a = _apara(_reamostra(w.squeeze().cpu().numpy(), m.sr))
        if humanizar and n and len(f.split()) >= 12 and rng.random() < .7:
            out.append(_respiro(rng, rng.uniform(.22, .32)))
        out.append(a)
        if humanizar and n < len(fs) - 1:
            pa = {'?': rng.uniform(.55, .75), '!': rng.uniform(.32, .45), ':': rng.uniform(.22, .32), '…': rng.uniform(.6, .8)}.get(f[-1], rng.uniform(.3, .46))
            out.append(np.zeros(int(pa * S), np.float32))
    a = np.concatenate(out) if out else np.zeros(1, np.float32)
    return estudio(a) if humanizar else a
