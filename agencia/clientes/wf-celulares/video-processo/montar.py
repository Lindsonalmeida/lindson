# Monta o vídeo "processo WF Celulares" (~60 s, 1080×1920) · conta Leandro · 10/11/2026
# Estilo: edit-ia-pro nº 5 Motion explicativo + nº 9 Antes e depois; motion #163 zoom, #166 corte na batida, #169 flash,
# #152 light leak, #35 grão, #25 parallax leve, #28 mockup de celular, grade do feed montando.
# Áudio: narração (voz/bN.wav), SFX Mixkit nos cortes, trilha Mixkit com ducking (sidechain).
# Uso: python3 montar.py [voz|voz-edge]
import os, sys, subprocess, json
D = os.path.dirname(os.path.abspath(__file__)); VZ = os.path.join(D, sys.argv[1] if len(sys.argv) > 1 else 'voz')
SOM = os.path.join(D, 'som'); TMP = os.path.join(D, 'tmp'); os.makedirs(TMP, exist_ok=True)
FPS, XF = 30, 0.35
run = lambda a: subprocess.run(['ffmpeg', '-v', 'error', '-y'] + a, check=True)
dur = lambda f: float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', f]))
V = [dur(os.path.join(VZ, f'b{i}.wav')) for i in range(1, 8)]
CENAS = ['01-antes', '02-engenharia', '03-logo', '04-laudo', '05-manual', 'feed', '07-cta']
T = [v + 1.8 for v in V]; T[5] += 3; T[-1] += 2.5

def clip(img, d, out, zoom=0.06, shake=False):
    n = int(d * FPS)
    z = f"zoompan=z='1+{zoom}*on/{n}':x='iw/2-(iw/zoom/2)+{'8*sin(on*2.1)*max(0,1-on/10)' if shake else '0'}':y='ih/2-(ih/zoom/2)':d={n}:s=1080x1920:fps={FPS}"
    run(['-loop', '1', '-i', img, '-vf', f'scale=2160:3840,{z},format=yuv420p', '-t', f'{d}', '-r', str(FPS), out])

partes = []
for i, (c, d) in enumerate(zip(CENAS, T)):
    out = os.path.join(TMP, f'{i}.mp4')
    if c == 'feed':  # grade montando: 9 passos curtos + segura no fim
        passo = (d * .7) / 9; sub = []
        for k in range(1, 10):
            o = os.path.join(TMP, f'f{k}.mp4'); clip(os.path.join(D, 'cenas', f'06-feed-{k}.jpg'), passo if k < 9 else passo + d * .3 + XF, o, .01); sub.append(o)
        open(os.path.join(TMP, 'f.txt'), 'w').write(''.join(f"file '{s}'\n" for s in sub))
        run(['-f', 'concat', '-safe', '0', '-i', os.path.join(TMP, 'f.txt'), '-c', 'copy', out])
    else:
        clip(os.path.join(D, 'cenas', c + '.jpg'), d + XF, out, .08 if c != '03-logo' else .14, shake=c in ('03-logo', '07-cta'))
    partes.append(out)

# xfade em cadeia: flash branco (#169) no logo e no CTA, zoom nos demais
trans = ['zoomin', 'fadewhite', 'smoothleft', 'zoomin', 'smoothup', 'fadewhite']
ins = sum([['-i', p] for p in partes], [])
f, last = [], '0:v'
for i in range(1, len(partes)):
    o = f'x{i}'; f.append(f'[{last}][{i}:v]xfade=transition={trans[i-1]}:duration={XF}:offset={sum(T[:i]):.3f}[{o}]'); last = o
total = sum(T) + XF
# light leak (#152) + grão (#35) + leve desfoque de movimento (tmix)
f.append(f"gradients=s=1080x1920:c0=0xff8a3d:c1=0x000000:x0=0:y0=0:x1=900:y1=1400:speed=0.02:d={total:.2f}:r={FPS},format=yuv420p,colorchannelmixer=aa=1[leak]")
f.append(f"[{last}]tmix=frames=2,noise=alls=7:allf=t[base]")
f.append("[base][leak]blend=all_mode=screen:all_opacity=0.10,format=yuv420p[v]")
# áudio: voz em sequência, SFX nos cortes, trilha com ducking
cortes = [sum(T[:i]) for i in range(len(T))]
ai = len(partes); aud = []; idx = ai
voz_in = []
for i in range(7):
    ins += ['-i', os.path.join(VZ, f'b{i+1}.wav')]
    f.append(f'[{idx}:a]adelay={int((cortes[i] + .25) * 1000)}|{int((cortes[i] + .25) * 1000)},apad[vz{i}]'); voz_in.append(f'[vz{i}]'); idx += 1
f.append(''.join(voz_in) + f'amix=inputs=7:normalize=0,atrim=0:{total:.2f}[voz]')
sfx = []
for i, c in enumerate(cortes[1:], 1):
    arq = 'impacto.mp3' if i in (2, 6) else 'whoosh.mp3'
    ins += ['-i', os.path.join(SOM, arq)]
    f.append(f'[{idx}:a]volume=0.55,adelay={int(max(0, c - .2) * 1000)}|{int(max(0, c - .2) * 1000)},apad[s{i}]'); sfx.append(f'[s{i}]'); idx += 1
ins += ['-i', os.path.join(SOM, 'trilha.mp3')]
f.append(f'[{idx}:a]atrim=0:{total:.2f},volume=0.35,afade=t=out:st={total-2:.2f}:d=2[tr]')
f.append('[voz]asplit=2[voz1][voz2]')
f.append('[tr][voz2]sidechaincompress=threshold=0.03:ratio=8:attack=20:release=300[trd]')
f.append(f'[voz1][trd]' + ''.join(sfx) + f'amix=inputs={2+len(sfx)}:normalize=0,atrim=0:{total:.2f},alimiter=limit=0.95[a]')
run(ins + ['-filter_complex', ';'.join(f), '-map', '[v]', '-map', '[a]', '-t', f'{total:.2f}', '-c:v', 'libx264', '-crf', '21', '-preset', 'medium',
           '-c:a', 'aac', '-b:a', '160k', '-movflags', '+faststart', os.path.join(D, 'wf-processo-60s.mp4')])
print('duração', round(total, 1), 's')
