# Monta o vídeo longo de uma faixa do Pagode Fiado (conta Pedro, sessão GOMINHO, 18/11/2026).
# Uso: python3 montar.py <faixa> <pasta_trabalho>
# Precisa em <pasta>: audio/<faixa>.wav, fotos/<id>.jpg (Wikimedia, ver CREDITOS-FOTOS.md), ov<faixa>/*.png (overlays.py + render.js)
import json, sys, os, subprocess, wave, struct, math, random
import numpy as np
from PIL import Image, ImageFilter
K, W = sys.argv[1], sys.argv[2]
AQUI = os.path.dirname(os.path.abspath(__file__))
F = json.load(open(AQUI + '/faixas.json'))[K]
FPS = 30; TOT = round(F['dur'] + 1.5, 2); FIM = F['dur'] - 6.5; XF = 0.6
ov = f'{W}/ov{K}'; tmp = f'{W}/tmp{K}'; os.makedirs(tmp, exist_ok=True)
# 1) fotos tratadas (16:9, âmbar e verde, vinheta)
def tratar(src, dst):
    im = Image.open(src).convert('RGB'); w, h = im.size; r = 16 / 9
    if w / h > r: nw = int(h * r); im = im.crop(((w - nw) // 2, 0, (w - nw) // 2 + nw, h))
    else: nh = int(w / r); im = im.crop((0, (h - nh) // 2, w, (h - nh) // 2 + nh))
    im = im.resize((2304, 1296), Image.LANCZOS)
    a = np.asarray(im).astype(np.float32) / 255
    lum = a.mean(2, keepdims=True)
    a = a * 0.82 + lum * 0.18                               # menos saturação
    sh = np.array([0.10, 0.42, 0.33]); hi = np.array([1.0, 0.78, 0.45])  # sombra verde-azulejo, luz âmbar
    a = a * 0.8 + (sh * (1 - lum) + hi * lum) * a * 0.35
    a = np.clip((a - 0.5) * 1.08 + 0.47, 0, 1)
    yy, xx = np.mgrid[0:1296, 0:2304]; d = np.sqrt(((xx - 1152) / 1152) ** 2 + ((yy - 648) / 648) ** 2)
    a *= np.clip(1.15 - 0.45 * d, 0.45, 1)[..., None]
    Image.fromarray((a * 255).astype(np.uint8)).save(dst, quality=93)
cortes = F['cortes'] + [TOT]
clips = []
for i, fid in enumerate(F['fotos']):
    dst = f'{tmp}/f{i:02d}.jpg'
    if not os.path.exists(dst): tratar(f'{W}/fotos/{fid}.jpg', dst)
    dur = cortes[i + 1] - cortes[i] + (XF if i < len(F['fotos']) - 1 else 0)
    n = int(round(dur * FPS)) + 2
    zin = i % 2 == 0
    z = f"1+0.12*on/{n}" if zin else f"1.12-0.12*on/{n}"
    px = "iw/2-(iw/zoom/2)" + (f"+40*on/{n}" if i % 3 == 0 else f"-40*on/{n}" if i % 3 == 1 else "")
    c = f'{tmp}/c{i:02d}.mp4'
    if not os.path.exists(c): subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-loop', '1', '-i', dst, '-vf',
        f"scale=4608:-1,zoompan=z='{z}':x='{px}':y='ih/2-(ih/zoom/2)':d={n}:s=1920x1080:fps={FPS},format=yuv420p",
        '-frames:v', str(n), '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '16', c], check=True)
    clips.append((c, dur))
# 2) junta as fotos com fusão
ins, fl, off, last = [], [], 0, '0:v'
for i, (c, d) in enumerate(clips): ins += ['-i', c]
for i in range(1, len(clips)):
    off += clips[i - 1][1] - XF
    fl.append(f"[{last}][{i}:v]xfade=transition={'fade' if i % 2 else 'smoothleft'}:duration={XF}:offset={off:.3f}[x{i}]"); last = f'x{i}'
base = f'{tmp}/base.mp4'
if not os.path.exists(base): subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', *ins, '-filter_complex', ';'.join(fl), '-map', f'[{last}]', '-t', str(TOT),
    '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '16', base], check=True)
# 3) SFX: whoosh nos cortes + leve ambiente de bar no começo
sr = 44100; n = int(TOT * sr); sfx = np.zeros(n, np.float32); rng = np.random.default_rng(7)
for t in F['cortes'][1:] + [FIM]:
    L = int(0.9 * sr); s0 = int((t - 0.55) * sr)
    if s0 < 0 or s0 + L > n: continue
    nz = rng.standard_normal(L).astype(np.float32)
    k = np.linspace(0, 1, L); f = 0.02 + 0.25 * np.sin(np.pi * k)
    y = np.zeros(L, np.float32); acc = 0
    for j in range(L): acc += f[j] * (nz[j] - acc); y[j] = acc
    sfx[s0:s0 + L] += y * np.sin(np.pi * k) ** 2 * 0.22
amb = rng.standard_normal(int(10 * sr)).astype(np.float32); acc = 0
for j in range(len(amb)): acc += 0.03 * (amb[j] - acc); amb[j] = acc
sfx[:len(amb)] += amb * np.clip(np.linspace(1.6, 0, len(amb)), 0, 1) * 0.5
with wave.open(f'{tmp}/sfx.wav', 'w') as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr); w.writeframes((np.clip(sfx, -1, 1) * 32767).astype('<i2').tobytes())
# 4) camadas: moldura, letra, carimbos, abertura, fim, luz nos cortes — compostas em Python e enviadas cruas ao ffmpeg
lay = []  # (png, ini, fim, fade)
lay.append(('abertura', 0, F['letra'][0][0] - 0.3, 0.6))
lay.append(('moldura', F['letra'][0][0] - 0.6, FIM + 0.3, 0.6))
for i, (a, b, t) in enumerate(F['letra']): lay.append((f'l{i:02d}', a - 0.15, min(b, FIM), 0.22))
for i, (a, t) in enumerate(F['partes']): lay.append((f'p{i}', a, a + 3.2, 0.22))
for t in F['cortes'][1:]: lay.append(('luz', t - 0.45, t + 0.55, 0.45))
lay.append(('fim', FIM, TOT, 0.6))
png = {p: np.asarray(Image.open(f'{ov}/{p}.png').convert('RGBA')).astype(np.float32) / 255 for p, *_ in lay}
saida = f'{W}/pagode-fiado-{K}-longo.mp4'
cmd = ['ffmpeg', '-y', '-loglevel', 'error', '-i', base, '-f', 'rawvideo', '-pix_fmt', 'rgba', '-s', '1920x1080', '-r', str(FPS), '-i', '-',
       '-i', f'{W}/audio/{K}.wav', '-i', f'{tmp}/sfx.wav', '-filter_complex',
       f"[0:v][1:v]overlay=0:0:shortest=1,noise=alls=4:allf=t,format=yuv420p,fade=in:st=0:d=0.8,fade=out:st={TOT - 1:.2f}:d=1[vout];"
       f"[2:a]volume=0.85[m];[3:a]aresample=44100,pan=stereo|c0=c0|c1=c0[s];[m][s]amix=inputs=2:normalize=0,afade=t=out:st={TOT - 1.2:.2f}:d=1.2,alimiter=limit=0.93[aout]",
       '-map', '[vout]', '-map', '[aout]', '-t', str(TOT), '-c:v', 'libx264', '-preset', 'medium', '-crf', '20', '-maxrate', '14M', '-bufsize', '28M',
       '-r', str(FPS), '-c:a', 'aac', '-b:a', '256k', '-movflags', '+faststart', saida]
pr = subprocess.Popen(cmd, stdin=subprocess.PIPE)
vazio = np.zeros((1080, 1920, 4), np.float32); cache = {}
for f in range(int(TOT * FPS) + 1):
    t = f / FPS; at = []
    for p, a, b, fd in lay:
        if a <= t <= b:
            al = min(1, (t - a) / fd, (b - t) / fd); at.append((p, round(max(al, 0), 2)))
    key = tuple(at)
    if key not in cache:
        if len(cache) > 40: cache.clear()
        out = vazio.copy()
        for p, al in at:
            src = png[p]; sa = src[..., 3:4] * al
            out[..., :3] = src[..., :3] * sa + out[..., :3] * (1 - sa); out[..., 3:4] = sa + out[..., 3:4] * (1 - sa)
        cache[key] = (np.clip(out, 0, 1) * 255).astype(np.uint8).tobytes()
    pr.stdin.write(cache[key])
pr.stdin.close(); pr.wait()
print('ok', saida)
