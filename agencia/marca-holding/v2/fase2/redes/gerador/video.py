"""Motor de vídeo Al Kántara (conta Pedro, 16/11/2026): voz Thalita (edge-tts), letreiro Fraunces, foto P&B com push-in,
K com a pedra da divisão acesa, SFX (impacto, whoosh nos cortes), VFX (flash de entrada, tremor no impacto, luz vazando latão,
grão, transição xfade), trilha sintetizada (drone + pulso) com ducking. Uso: python3 -I video.py <spec.json> <saida.mp4>
spec: {w,h,div,blocos:[{fala,letreiro,foto?}],fim?}"""
import json, os, sys, subprocess, asyncio, html as H
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base import *
import certifi
certifi.where = lambda: '/root/.ccr/ca-bundle.crt'
import edge_tts
SP, OUT = sys.argv[1], sys.argv[2]; S = json.load(open(SP))
W, Hh, D = S['w'], S['h'], S['div']; c = COR[D]; V = W < Hh
R = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')); T = f"{R}/_tmp/v-{os.path.basename(OUT)[:-4]}"; os.makedirs(T, exist_ok=True)
SFX = '/home/user/lindson/conteudo/reels/leva-30s/banco/sfx'
def run(a): subprocess.run(['ffmpeg', '-nostdin', '-y', '-v', 'error'] + a, check=True)
dur = lambda p: float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', p]))
async def tts(t, p): await edge_tts.Communicate(t, 'pt-BR-ThalitaMultilingualNeural', rate='+6%').save(p)
B = S['blocos']; N = len(B)
# 1) vozes
dv = []
for i, b in enumerate(B):
    p = f'{T}/v{i}.mp3'
    if not os.path.exists(p): asyncio.run(tts(b['fala'], p))
    dv.append(dur(p))
dc = [d + 0.35 for d in dv]
# 2) camadas
lista = []
fs = 150 if V else 112
for i, b in enumerate(B):
    ft = b.get('foto')
    bgw, bgh = int(W * 1.12), int(Hh * 1.12)
    if ft and not (i == N - 1):
        bg = f'<div style="width:{bgw}px;height:{bgh}px;position:relative;background:#0B0C0E"><div style="position:absolute;inset:0;background:url(file://{R}/fotos/{ft}.jpg) center/cover;filter:grayscale(1) contrast(1.2) brightness(.55)"></div><div style="position:absolute;inset:0;background:{c};mix-blend-mode:soft-light;opacity:.55"></div><div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(11,12,14,.3),rgba(11,12,14,.1) 40%,rgba(11,12,14,.9))"></div></div>'
    elif i == N - 1:
        bg = f'<div style="width:{bgw}px;height:{bgh}px;background:radial-gradient(circle at 50% 40%,#1d1f24,#0B0C0E 60%)"></div>'
    else:
        lado = ['right:-28%;top:6%', 'left:-30%;top:20%', 'right:-20%;bottom:-8%', 'left:20%;top:-30%'][i % 4]
        bg = f'<div style="width:{bgw}px;height:{bgh}px;position:relative;background:radial-gradient(circle at 70% 30%,#1b1d22,#0B0C0E 65%);overflow:hidden"><div style="position:absolute;{lado};width:{int(min(bgw,bgh)*1.1)}px;opacity:.45">{simb(IDX[D], c, "#17191d")}</div></div>'
    fim = (i == N - 1)
    lt = b['letreiro']
    if fim and 'link na bio' in lt.lower(): lt = 'Fale com a *gente.*'
    if '*' not in lt:
        ws = lt.split(); k = 1 if len(ws) < 4 else 2; lt = ' '.join(ws[:-k]) + ' *' + ' '.join(ws[-k:]) + '*' if len(ws) > 1 else '*' + lt + '*'
    letr = it(lt)
    if i == 0: fs0 = fs * 1.12
    else: fs0 = fs
    pos = f'left:{int(W*.067)}px;right:{int(W*.067)}px;bottom:{int(Hh*(.24 if V else .16))}px' if not fim else f'left:{int(W*.067)}px;right:{int(W*.067)}px;top:50%;transform:translateY(-30%);text-align:center'
    extra = f'<p class="mono" style="margin-top:34px;color:#EFEAE1;display:inline-block;padding:20px 30px;border:2px solid {c};border-radius:999px;font-size:{26 if V else 22}px">{H.escape(S.get("fim","Link na bio · alkantaragroup.pages.dev"))}</p>' if fim else ''
    simf = f'<div style="position:absolute;left:50%;top:{int(Hh*.16)}px;transform:translateX(-50%);width:{int(W*.32)}px">{simb(IDX[D], c, "#24262b")}</div>' if fim else ''
    fg = f'''<div style="width:{W}px;height:{Hh}px;position:relative;color:#EFEAE1">
<div style="position:absolute;left:{int(W*.067)}px;right:{int(W*.067)}px;top:{int(Hh*.05)}px;display:flex;justify-content:space-between;align-items:center"><img src="{LOGO_N}" style="height:{40 if V else 44}px"><span class="mono" style="color:{c};font-size:{22 if V else 20}px">{NOME[D].split(" · ")[0]}</span></div>{simf}
<div style="position:absolute;{pos}"><h1 style="font-size:{fs0 if not fim else fs*.8:.0f}px;line-height:.95;text-shadow:0 6px 30px rgba(0,0,0,.85),0 0 4px rgba(0,0,0,.6)">{letr.replace("<em>", f'<em style="color:{c if D!="grupo" else "#B8955A"}">')}</h1>{extra}</div>
<div style="position:absolute;left:{int(W*.067)}px;right:{int(W*.067)}px;bottom:{int(Hh*.06)}px;display:flex;gap:10px">{"".join(f'<i style="flex:1;height:5px;background:{c if k<=i else "rgba(239,234,225,.2)"}"></i>' for k in range(N))}</div></div>'''
    for nm, body, w, h, tr in [(f'b{i}', bg, bgw, bgh, False), (f'f{i}', fg, W, Hh, True)]:
        hp = f'{T}/{nm}.html'; open(hp, 'w').write(doc(w, h, body, 'body{background:transparent}' if tr else '')); lista.append(dict(html=hp, png=f'{T}/{nm}.png', w=w, h=h, transp=tr))
json.dump(lista, open(f'{T}/l.json', 'w'))
subprocess.run(['node', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'shots.js'), f'{T}/l.json'], check=True, env=dict(os.environ, NODE_PATH='/opt/node-tools/node_modules'))
# 3) cenas
FPS = 30
for i in range(N):
    d = dc[i] + 0.4; n = int(d * FPS)
    sx = "(iw-ow)/2+if(lt(t,0.3),18*sin(t*90),0)" if i == 0 else "(iw-ow)/2"
    vf = (f"[0:v]scale={int(W*1.12)}:{int(Hh*1.12)},zoompan=z='1+0.06*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={n}:s={int(W*1.12)}x{int(Hh*1.12)}:fps={FPS},"
          f"crop={W}:{Hh}:x='{sx}':y='(ih-oh)/2'[bg];"
          f"[1:v]format=rgba,fade=in:st=0.1:d=0.35:alpha=1[fg];[bg][fg]overlay=x=0:y='if(lt(t,0.45),70*(1-t/0.45),0)'[a];"
          f"color=c=white:s={W}x{Hh}:d={d:.2f},format=rgba,fade=out:st=0:d=0.18:alpha=1[fl];[a][fl]overlay[b];"
          f"color=c={c}:s={W}x{Hh}:d={d:.2f},format=rgba,geq=r='r(X,Y)':g='g(X,Y)':b='b(X,Y)':a='if(lt(T,0.9),90*(1-T/0.9),0)*exp(-((X-{W}*0.9)*(X-{W}*0.9)+(Y-{Hh}*0.1)*(Y-{Hh}*0.1))/({W}*{W}*0.18))'[lk];[b][lk]overlay,noise=alls=4:allf=t,format=yuv420p[v]")
    run(['-loop', '1', '-t', f'{d:.2f}', '-i', f'{T}/b{i}.png', '-loop', '1', '-t', f'{d:.2f}', '-i', f'{T}/f{i}.png', '-filter_complex', vf, '-map', '[v]', '-r', str(FPS), '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '20', '-t', f'{d:.2f}', f'{T}/c{i}.mp4'])
# 4) junta com xfade (0.4 s)
tr = ['slideleft', 'fadeblack', 'slideup', 'circleopen', 'smoothleft', 'fadeblack']
ins = sum([['-i', f'{T}/c{i}.mp4'] for i in range(N)], []); fc = ''; prev = '[0:v]'; off = 0; cuts = []
for i in range(1, N):
    off += dc[i-1]; cuts.append(off)
    fc += f"{prev}[{i}:v]xfade=transition={tr[i % len(tr)]}:duration=0.4:offset={off:.2f}[x{i}];"; prev = f'[x{i}]'
total = sum(dc) + 0.4
run(ins + ['-filter_complex', fc.rstrip(';') if N > 1 else '[0:v]null[x0]', '-map', prev if N > 1 else '[x0]', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '25', '-maxrate', '5M', '-bufsize', '10M', '-pix_fmt', 'yuv420p', f'{T}/video.mp4'])
# 5) áudio
run(['-f', 'lavfi', '-i', f"aevalsrc='0.09*sin(2*PI*55*t)+0.06*sin(2*PI*82.4*t)*(0.6+0.4*sin(2*PI*0.1*t))+0.04*sin(2*PI*110*t)+0.035*sin(2*PI*164.8*t)*(0.5+0.5*sin(2*PI*0.07*t))+0.22*sin(2*PI*48*t)*exp(-9*mod(t,0.75))':s=44100:d={total:.2f}", '-af', 'lowpass=f=1800,afade=in:d=1,afade=out:st=' + f'{total-1.5:.2f}' + ':d=1.5', f'{T}/trilha.wav'])
a = ['-i', f'{T}/trilha.wav']; fca = []; vz = []; st = 0.15
for i in range(N):
    a += ['-i', f'{T}/v{i}.mp3']; ms = int(st * 1000); fca.append(f'[{i+1}:a]adelay={ms}|{ms},volume=1.5[v{i}]'); vz.append(f'[v{i}]'); st += dc[i]
k = N + 1; sf = []
a += ['-i', f'{SFX}/impacto-intro.mp3']; fca.append(f'[{k}:a]volume=0.55[s{k}]'); sf.append(f'[s{k}]'); k += 1
for j, ct in enumerate(cuts):
    a += ['-i', f"{SFX}/{['whoosh-rapido.mp3', 'whoosh-cinematico.mp3'][j % 2]}"]; ms = int(max(0, ct - 0.2) * 1000)
    fca.append(f'[{k}:a]adelay={ms}|{ms},volume=0.45[s{k}]'); sf.append(f'[s{k}]'); k += 1
fca.append(f"{''.join(vz)}amix=inputs={N}:normalize=0,asplit[vA][vB]")
fca.append("[0:a]volume=0.8[tr];[tr][vA]sidechaincompress=threshold=0.02:ratio=12:attack=15:release=400[duck]")
fca.append(f"[duck][vB]{''.join(sf)}amix=inputs={2+len(sf)}:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11[out]")
run(a + ['-filter_complex', ';'.join(fca), '-map', '[out]', '-ar', '44100', f'{T}/audio.m4a'])
run(['-i', f'{T}/video.mp4', '-i', f'{T}/audio.m4a', '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '160k', '-shortest', '-movflags', '+faststart', OUT])
print(OUT, round(total, 1), 's')
