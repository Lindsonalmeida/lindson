# Conferência de cada longo v2: áudio idêntico ao mp3 aprovado (amostra a amostra), duração, formato e tamanho do painel.
# Uso: python3 verificar.py <pasta_trabalho> <pasta_painel>
import sys, os, subprocess, json, numpy as np
W, P = sys.argv[1], sys.argv[2]
def pcm(f): return np.frombuffer(subprocess.run(['ffmpeg', '-v', 'error', '-i', f, '-map', '0:a', '-f', 's16le', '-ac', '2', '-ar', '48000', '-'], capture_output=True).stdout, np.int16).reshape(-1, 2).astype(np.int32)
def pr(f, q): return subprocess.run(['ffprobe', '-v', 'error'] + q + ['-of', 'csv=p=0', f], capture_output=True, text=True).stdout.strip()
ok = True
for k in [f'{i:02d}' for i in range(11)]:
    v = f'{W}/pagode-fiado-{k}-v2.mp4'
    if not os.path.exists(v): print(k, 'FALTA'); ok = False; continue
    a, b = pcm(f'{W}/audio/{k}.mp3'), pcm(v); n = min(len(a), len(b)); dif = int(np.abs(a[:n] - b[:n]).max())
    vs = pr(v, ['-select_streams', 'v', '-show_entries', 'stream=width,height,r_frame_rate']); tam = os.path.getsize(f'{P}/pagode-fiado-{k}-v2.mp4') / 1048576 if os.path.exists(f'{P}/pagode-fiado-{k}-v2.mp4') else 0
    st = 'OK' if dif == 0 and (len(a) - n) < 4800 and vs.startswith('1920,1080') and 0 < tam < 20 else 'ERRO'
    ok &= st == 'OK'
    print(f'{k} {st} áudio_dif={dif} sobra={(len(a) - n) / 48:.0f}ms vídeo={vs} painel={tam:.1f}MB')
print('TUDO OK' if ok else 'HÁ PROBLEMAS')
