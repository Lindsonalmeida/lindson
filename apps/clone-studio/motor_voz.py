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
    """Tira o silêncio do começo e do fim de cada frase e as sobras do modelo: chiado e estalo
    soltos no fim (pedaço curto de som separado da fala por um silêncio). Corrigido em 03/11 a
    pedido do Lindson ("tem umas pausas e ruídos, deixe a voz limpa e fluida")."""
    fr = 441; n = len(a) // fr                                  # quadros de 10 ms
    if n < 3: return a
    e = np.sqrt(np.mean(a[:n * fr].reshape(n, fr) ** 2, axis=1)); lim = max(e.max() * 10 ** (-32 / 20), 1e-5)
    on = e > lim
    trechos, i = [], 0                                          # trechos contínuos de fala
    while i < n:
        if on[i]:
            j = i
            while j < n and on[j]: j += 1
            trechos.append([i, j]); i = j
        else: i += 1
    if not trechos: return a
    juntos = [trechos[0]]                                       # junta o que tem menos de 250 ms de silêncio
    for t in trechos[1:]:
        if t[0] - juntos[-1][1] < 25: juntos[-1][1] = t[1]
        else: juntos.append(t)
    fala = [t for t in juntos if t[1] - t[0] >= 15]             # descarta estalo solto (< 150 ms)
    if not fala: fala = [max(juntos, key=lambda t: t[1] - t[0])]
    ini, fim = max(0, fala[0][0] - 2) * fr, min(n, fala[-1][1] + 3) * fr
    b = a[ini:fim].copy(); f = min(len(b) // 4, int(.012 * S))  # 12 ms de entrada e saída suaves
    if f: b[:f] *= np.linspace(0, 1, f); b[-f:] *= np.linspace(1, 0, f)
    return b


def _respiro(rng, dur):
    n = int(dur * S); x = rng.standard_normal(n)
    b, c = butter(2, [350 / (S / 2), 2600 / (S / 2)], 'band'); x = lfilter(b, c, x)
    u = np.linspace(0, 1, n); env = np.sin(np.pi * u) ** 1.6 * (0.6 + 0.4 * u)
    return (x * env / (np.abs(x).max() + 1e-9) * 10 ** (-34 / 20)).astype(np.float32)


def estudio(a):
    """Voz limpa (03/11): tira chiado, graves e presença, de-esser e compressão leve, SEM eco/ambiência."""
    d = tempfile.mkdtemp(); i, o = os.path.join(d, 'i.wav'), os.path.join(d, 'o.wav')
    sf.write(i, a, S)
    flt = ('highpass=f=70,afftdn=nr=12:nf=-50:tn=1,equalizer=f=160:t=q:w=1:g=2,equalizer=f=3200:t=q:w=1.4:g=1.4,'
           'deesser=i=0.35,acompressor=threshold=-20dB:ratio=2.2:attack=6:release=140:makeup=2')
    subprocess.run([ffmpeg(), '-y', '-loglevel', 'error', '-i', i, '-af', flt, '-ar', str(S), '-ac', '1', o], check=True)
    b, _ = sf.read(o)
    return (b / (np.abs(b).max() + 1e-9) * .95).astype(np.float32)


def narrar(txt, amostra, expressao=0.5, semente=0, humanizar=True, progresso=None, respirar=False):
    """txt -> áudio float32 44,1 kHz mono com a voz da amostra (wav de 10 s a 2 min, voz limpa).
    Padrão do Lindson (03/11): voz limpa e fluida, pausas curtas entre frases, sem respiração
    artificial e sem eco. `respirar=True` volta a pôr o respiro antes de frase longa."""
    m = modelo(); rng = np.random.default_rng(int(hashlib.md5(f'{semente}|{txt}'.encode()).hexdigest()[:8], 16))
    fs = frases(txt) if humanizar else [txt.strip()]
    out = []
    for n, f in enumerate(fs):
        if progresso: progresso((n, len(fs)), desc=f'Frase {n + 1} de {len(fs)}')
        ex = expressao + (rng.uniform(-.08, .08) if humanizar else 0)
        if f.endswith('!'): ex += .1
        w = m.generate(f, language_id='pt', audio_prompt_path=amostra, exaggeration=float(np.clip(ex, .25, 1)))
        a = _apara(_reamostra(w.squeeze().cpu().numpy(), m.sr))
        if respirar and n and len(f.split()) >= 12 and rng.random() < .7:
            out.append(_respiro(rng, rng.uniform(.22, .32)))
        out.append(a)
        if humanizar and n < len(fs) - 1:
            pa = {'?': rng.uniform(.30, .38), '!': rng.uniform(.22, .28), ':': rng.uniform(.14, .2), '…': rng.uniform(.32, .4)}.get(f[-1], rng.uniform(.18, .26))
            out.append(np.zeros(int(pa * S), np.float32))
    a = np.concatenate(out) if out else np.zeros(1, np.float32)
    a = np.concatenate([np.zeros(int(.08 * S), np.float32), a, np.zeros(int(.12 * S), np.float32)])
    return estudio(a)
