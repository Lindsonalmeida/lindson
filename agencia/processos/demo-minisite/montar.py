"""Monta o vídeo de demonstração do mini site (tela de iPhone) a partir da gravação.
python3 montar.py <roteiro.json> <saida.mp4>   (grava antes com gravar.js)"""
import json, os, sys, subprocess, urllib.request
import numpy as np, soundfile as sf
from scipy.signal import butter, lfilter
D = os.path.dirname(os.path.abspath(__file__))
rot, saida = sys.argv[1], sys.argv[2]; R = json.load(open(rot))
TMP = '/tmp/claude-0/-home-user/5acf6937-9ac6-56e0-bc29-78bef210dc8b/scratchpad/demo/' + os.path.basename(rot)[:-5]
os.makedirs(TMP, exist_ok=True)
subprocess.run(['node', D + '/gravar.js', rot, TMP + '/g'], check=True)
G = json.load(open(TMP + '/g/tempos.json')); T, FIM = G['tempos'], G['fim']; ev = json.load(open(TMP + '/g/eventos.json'))
with open(TMP + '/lista.txt', 'w') as f:
    for i, t in enumerate(T):
        d = (T[i + 1] if i + 1 < len(T) else FIM) - t
        f.write(f"file '{TMP}/g/q/{i:05d}.jpg'\nduration {max(d, 0.001):.4f}\n")
    f.write(f"file '{TMP}/g/q/{len(T) - 1:05d}.jpg'\n")
# barra de status e barra do Safari (PNG transparente por cima da gravação)
ui = f'''<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Inter:wght@500;600;700&display=swap" rel="stylesheet"><style>
*{{margin:0;box-sizing:border-box}}body{{width:1080px;height:1920px;background:transparent;font-family:Inter,system-ui,sans-serif;position:relative}}
.st{{position:absolute;left:0;right:0;top:0;height:132px;background:#000;color:#fff;display:flex;align-items:center;justify-content:space-between;padding:22px 70px 0 96px}}
.st b{{font:600 46px Inter;letter-spacing:-.5px}}.ic{{display:flex;gap:16px;align-items:center}}
.sf{{position:absolute;left:0;right:0;bottom:0;height:200px;background:rgba(18,18,20,.94);backdrop-filter:blur(20px);display:flex;flex-direction:column;align-items:center;padding-top:22px;gap:26px}}
.url{{width:960px;height:96px;border-radius:48px;background:rgba(255,255,255,.14);color:#fff;display:flex;align-items:center;justify-content:center;gap:14px;font:500 38px Inter}}
.url small{{font-size:34px;opacity:.6}}
.home{{width:400px;height:14px;border-radius:7px;background:#fff}}
</style></head><body>
<div class="st"><b>9:41</b><div class="ic">
<svg width="62" height="38" viewBox="0 0 62 38"><rect x="0" y="26" width="10" height="12" rx="3" fill="#fff"/><rect x="17" y="18" width="10" height="20" rx="3" fill="#fff"/><rect x="34" y="9" width="10" height="29" rx="3" fill="#fff"/><rect x="51" y="0" width="10" height="38" rx="3" fill="#fff"/></svg>
<svg width="54" height="38" viewBox="0 0 54 38"><path d="M27 34l7-8a10 10 0 0 0-14 0z" fill="#fff"/><path d="M11 17a23 23 0 0 1 32 0l-5 6a15 15 0 0 0-22 0z" fill="#fff"/><path d="M2 8a36 36 0 0 1 50 0l-5 6a28 28 0 0 0-40 0z" fill="#fff"/></svg>
<svg width="92" height="42" viewBox="0 0 92 42"><rect x="2" y="2" width="78" height="38" rx="11" fill="none" stroke="#fff" stroke-opacity=".5" stroke-width="3"/><rect x="8" y="8" width="62" height="26" rx="7" fill="#fff"/><rect x="84" y="14" width="6" height="14" rx="3" fill="#fff" fill-opacity=".5"/></svg></div></div>
<div class="sf"><div class="url"><small>🔒</small>{R['endereco']}</div><div class="home"></div></div></body></html>'''
open(TMP + '/ui.html', 'w').write(ui)
subprocess.run(['node', '-e', f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage({{viewport:{{width:1080,height:1920}}}});await p.goto('file://{TMP}/ui.html',{{waitUntil:'networkidle'}});await p.evaluate(()=>document.fonts.ready);await p.screenshot({{path:'{TMP}/ui.png',omitBackground:true}});await b.close()}})()"], check=True)
# áudio: a trilha do próprio site (se o roteiro toca "Ativar som") ou uma batida leve; clique em cada toque
S = 44100; N = int(FIM * S); mix = np.zeros(N + S)
mus = [e for e in ev if e['tipo'] == 'musica']
if mus:
    mp = TMP + '/musica.mp3'; urllib.request.urlretrieve(mus[0]['arq'], mp)
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', mp, '-ar', str(S), '-ac', '1', TMP + '/musica.wav'], check=True)
    a, _ = sf.read(TMP + '/musica.wav'); a = np.tile(a, 3); i0 = int(mus[0]['t'] * S); seg = a[:N - i0]
    env = np.minimum(1, np.arange(len(seg)) / (S * .3)) * np.minimum(1, (len(seg) - np.arange(len(seg))) / (S * 1.5)); mix[i0:i0 + len(seg)] += seg * env * .8
else:
    tm = np.arange(N) / S; bpm = 104; bt = 60 / bpm
    for k in range(int(FIM / bt)):  # bumbo + chimbal + acorde suave
        i = int(k * bt * S); x = np.arange(int(.35 * S)) / S
        if k % 2 == 0: kk = np.sin(2 * np.pi * np.cumsum(55 + 90 * np.exp(-x * 30)) / S) * np.exp(-x * 9) * .55; mix[i:i + len(kk)] += kk[:len(mix) - i]
        hh = np.random.default_rng(k).standard_normal(int(.05 * S)) * np.exp(-np.arange(int(.05 * S)) / S * 80) * .08; j = i + int(bt / 2 * S); mix[j:j + len(hh)] += hh[:max(0, len(mix) - j)]
    ac = [(220, 277.2, 329.6), (196, 246.9, 293.7), (174.6, 220, 261.6), (196, 246.9, 293.7)]
    for k in range(int(FIM / (4 * bt)) + 1):
        a0 = k * 4 * bt; m = (tm >= a0) & (tm < a0 + 4 * bt); x = tm[m] - a0
        mix[:N][m] += sum(np.sin(2 * np.pi * f * x) for f in ac[k % 4]) * np.minimum(1, x * 4) * np.exp(-x * .5) * .05
    b_, a_ = butter(2, 5000 / (S / 2)); mix = lfilter(b_, a_, mix)
for e in ev:
    if e['tipo'] == 'toque':
        x = np.arange(int(.04 * S)) / S; c = np.sin(2 * np.pi * 2200 * x) * np.exp(-x * 160) * .25; i = int(e['t'] * S); mix[i:i + len(c)] += c
mix = mix[:N]; mix = mix / max(1e-6, np.max(np.abs(mix))) * .9; sf.write(TMP + '/a.wav', mix, S)
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', TMP + '/lista.txt', '-i', TMP + '/ui.png', '-i', TMP + '/a.wav',
                '-filter_complex', '[0:v]fps=30,scale=1080:-2,format=yuv420p[g];color=c=black:s=1080x1920:r=30[f];[f][g]overlay=0:132:shortest=1[a];[a][1:v]overlay=0:0,format=yuv420p[v]',
                '-map', '[v]', '-map', '2:a', '-c:v', 'libx264', '-crf', '21', '-preset', 'medium', '-c:a', 'aac', '-b:a', '160k', '-t', f'{FIM:.2f}', '-movflags', '+faststart', saida], check=True)
print('ok', saida, round(FIM, 1), 's')
