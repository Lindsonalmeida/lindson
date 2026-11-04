# Narração sincronizada e fluida: cada frase começa junto com a cena dela e é esticada (até 18% mais lenta)
# ou acelerada (até 25%) para preencher a cena sem pausa longa. Uso: python sinc.py falas.json saida_dir
import json, subprocess, sys, os, imageio_ffmpeg
FF = imageio_ffmpeg.get_ffmpeg_exe(); V = sys.executable
falas = json.load(open(sys.argv[1])); out = sys.argv[2]; os.makedirs(out, exist_ok=True)
env = dict(os.environ, SSL_CERT_FILE='/root/.ccr/ca-bundle.crt')
def dur(p):
    r = subprocess.run([FF, '-i', p], capture_output=True, text=True).stderr
    h, m, s = r.split('Duration: ')[1].split(',')[0].split(':'); return float(s) + 60 * float(m)
novas = []
for i, (t, txt, *_ ) in enumerate(falas):
    raw = os.path.join(out, f'raw{i}.mp3')
    subprocess.run([V, '-m', 'edge_tts', '--proxy', os.environ['HTTPS_PROXY'], '--voice', 'pt-BR-AntonioNeural', '--rate=+0%', '--pitch=-1Hz',
                    '--text', txt, '--write-media', raw], env=env, check=True, capture_output=True, timeout=60)
    # tira o silêncio do começo e do fim
    cut = os.path.join(out, f'cut{i}.wav')
    subprocess.run([FF, '-v', 'error', '-y', '-i', raw, '-af', 'silenceremove=start_periods=1:start_threshold=-45dB,areverse,silenceremove=start_periods=1:start_threshold=-45dB,areverse', cut], check=True)
    L = dur(cut); fim = falas[i + 1][0] if i + 1 < len(falas) else 39.6
    janela = fim - t - 0.25
    f = L / janela if janela > 0 else 1
    f = min(max(f, 0.82), 1.25)  # atempo: <1 desacelera, >1 acelera
    dst = os.path.join(out, f'{i}.mp3')
    subprocess.run([FF, '-v', 'error', '-y', '-i', cut, '-af', f'atempo={f:.3f}', dst], check=True)
    novas.append([t + 0.05, txt, '+0%', '-1Hz']); print(i, 'cena', round(janela, 2), 'fala', round(L, 2), 'atempo', round(f, 2))
json.dump(novas, open(os.path.join(out, 'falas.json'), 'w'), ensure_ascii=False)
