# Narração de IA (narrador, não imita o Leo) frase a frase, encaixada no tempo de cada cena.
# Uso: python narra.py <video_sem_audio.mp4> <musica.mp3> <inicio_musica> <cortes> <falas.json> <saida.mp4>
import json, subprocess, sys, os, numpy as np, imageio_ffmpeg, asyncio, edge_tts
FF = imageio_ffmpeg.get_ffmpeg_exe(); SR = 48000
vid, mus, ini, cortes, falas_p, out = sys.argv[1:7]
falas = json.load(open(falas_p))  # [[t_inicio, "texto", "rate", "pitch"], ...]
D = os.path.dirname(os.path.abspath(out))
def pcm(path):
    raw = subprocess.run([FF, '-v', 'error', '-i', path, '-f', 's16le', '-ac', '1', '-ar', str(SR), '-'], capture_output=True).stdout
    return np.frombuffer(raw, np.int16).astype(np.float32) / 32768
async def gera(i, txt, rate, pitch):
    c = edge_tts.Communicate(txt, 'pt-BR-AntonioNeural', rate=rate, pitch=pitch, proxy=os.environ.get('HTTPS_PROXY'))
    p = os.path.join(D, f'_f{i}.mp3'); await c.save(p); return p
async def todas():
    return await asyncio.gather(*[gera(i, f[1], f[2], f[3]) for i, f in enumerate(falas)])
pre = os.environ.get('PRE')
paths = [os.path.join(pre, f'{i}.mp3') for i in range(len(falas))] if pre else asyncio.run(todas())
N = int(40 * SR); voz = np.zeros(N)
fim_ant = 0
for (t, *_), p in zip(falas, paths):
    a = pcm(p); nz = np.where(np.abs(a) > 0.01)[0]
    a = a[max(nz[0] - int(.03 * SR), 0):nz[-1] + int(.08 * SR)] if len(nz) else a
    i = max(int(t * SR), fim_ant + int(.12 * SR)); j = min(i + len(a), N); voz[i:j] += a[:j - i]; fim_ant = i + len(a)
    print('fala', t, '->', round(i / SR, 2), 'até', round(fim_ant / SR, 2))
    if i + len(a) > N + 0.1 * SR: print('AVISO fala passou do fim:', t)
voz *= 0.95 / max(np.abs(voz).max(), 1e-6)
# trilha + SFX do mix2 (já com cortes) e abaixa tudo sob a voz
sfxwav = os.path.join(D, '_sfx.wav')
sfxwav = os.environ.get('BASE') or sfxwav
if not os.environ.get('BASE'): subprocess.run([sys.executable, os.path.join(os.path.dirname(__file__), 'mix2.py'), mus, sfxwav, ini, cortes], check=True, capture_output=True)
base = pcm(sfxwav); base = base[:N] if len(base) >= N else np.pad(base, (0, N - len(base)))
k = int(.25 * SR); c = np.cumsum(np.insert((np.abs(voz) > 0.02).astype(float), 0, 0)); envv = np.zeros(N); idx = np.arange(N); lo = np.clip(idx - k // 2, 0, N); hi = np.clip(idx + k // 2, 0, N); envv = (c[hi] - c[lo]) / k
duck = 1 - 0.62 * np.clip(envv * 3, 0, 1)
mix = base * duck * 0.9 + voz * 1.0
mix /= max(1.0, np.abs(mix).max() / 0.9)
import wave
w = wave.open(os.path.join(D, '_mix.wav'), 'wb'); w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
w.writeframes((mix * 32767).astype(np.int16).tobytes()); w.close()
subprocess.run([FF, '-v', 'error', '-y', '-i', vid, '-i', os.path.join(D, '_mix.wav'), '-map', '0:v', '-map', '1:a', '-c:v', 'copy',
                '-c:a', 'aac', '-b:a', '192k', '-af', 'loudnorm=I=-14:TP=-1.5:LRA=11', '-ar', '48000', '-ac', '2', '-movflags', '+faststart', '-shortest', out], check=True)
print('ok', out)
