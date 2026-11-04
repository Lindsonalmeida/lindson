# Narração fluida: gera o texto inteiro do vídeo numa fala só (sem cortes entre frases) e ajusta a velocidade
# para a voz terminar perto de 38 s. Uso: python fluida.py falas.json saida_dir
import json, subprocess, sys, os, imageio_ffmpeg
FF = imageio_ffmpeg.get_ffmpeg_exe(); V = sys.executable
falas = json.load(open(sys.argv[1])); out = sys.argv[2]; os.makedirs(out, exist_ok=True)
texto = ' '.join(f[1] for f in falas)
def gera(rate, p):
    env = dict(os.environ, SSL_CERT_FILE='/root/.ccr/ca-bundle.crt')
    subprocess.run([V, '-m', 'edge_tts', '--proxy', os.environ['HTTPS_PROXY'], '--voice', 'pt-BR-AntonioNeural', f'--rate={rate:+d}%', '--pitch=-1Hz',
                    '--text', texto, '--write-media', p], env=env, check=True, capture_output=True, timeout=60)
    r = subprocess.run([FF, '-i', p], capture_output=True, text=True).stderr
    h, m, s = r.split('Duration: ')[1].split(',')[0].split(':'); return float(s) + 60 * float(m)
p = os.path.join(out, '0.mp3'); rate = 0
d = gera(rate, p)
for _ in range(3):
    if 31 <= d <= 38.3: break
    rate = int(round(rate + (d / 37.0 - 1) * 100)); rate = max(-6, min(25, rate)); d = gera(rate, p)
json.dump([[0.25, texto, f'{rate:+d}%', '-1Hz']], open(os.path.join(out, 'falas.json'), 'w'), ensure_ascii=False)
print('rate', rate, 'dur', round(d, 2))
