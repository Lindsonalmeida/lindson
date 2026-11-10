# Junta quadros (tmp/v<N>/) + voz Antonio +4% (voz/<N>.mp3, desde o quadro 0) + impacto no 0 + whoosh em cada corte
# + riser antes do preço + trilha Mixkit com ducking · conta Leandro · 10/11/2026
import os, json, re, subprocess
D = os.path.dirname(os.path.abspath(__file__)); S = os.path.join(D, '..', 'video-processo', 'som'); T = os.path.join(D, 'tmp')
R = {r['n']: r for r in json.load(open(os.path.join(D, 'roteiros.json')))}
run = lambda a: subprocess.run(['ffmpeg', '-v', 'error', '-y'] + a, check=True)
riser = os.path.join(T, 'riser.wav')
run(['-f', 'lavfi', '-i', "aevalsrc='0.25*sin(2*PI*(200+900*t*t/4)*t)*t/1.6':d=1.6:s=44100", '-f', 'lavfi', '-i', 'anoisesrc=d=1.6:c=pink:a=0.12',
     '-filter_complex', '[1]afade=t=in:d=1.5,highpass=f=2000[n];[0][n]amix=2,afade=t=out:st=1.5:d=0.1', riser])
for n, r in R.items():
    dur = json.load(open(os.path.join(D, f'v{n}.json')))['dur']
    cortes = [float(x) for x in re.findall(r'\["\w+", ([\d.]+)\]', open(os.path.join(D, f'v{n}.html')).read().split('const S=')[1].split(',L=')[0])][1:]
    ms = lambda s: f'{int(s*1000)}|{int(s*1000)}'
    ins = ['-framerate', '30', '-i', os.path.join(T, f'v{n}', '%04d.jpg'), '-i', os.path.join(D, 'voz', f'{n}.mp3'), '-i', os.path.join(S, 'trilha.mp3'),
           '-i', os.path.join(S, 'impacto.mp3'), '-i', riser]
    fc = [f"[0:v]tmix=frames=2,noise=alls=6:allf=t,format=yuv420p[v]",
          f"[1:a]aformat=channel_layouts=stereo,apad[vz];[vz]asplit[vz1][vz2]",
          f"[2:a]atrim=start={40+n*17},asetpts=PTS-STARTPTS,atrim=0:{dur},volume=0.45,afade=t=out:st={dur-0.8}:d=0.8[tr]",
          f"[tr][vz2]sidechaincompress=threshold=0.03:ratio=8:attack=15:release=250[trd]",
          f"[3:a]volume=0.8[im0]", f"[4:a]volume=0.7,adelay={ms(7.4)}[ri]"]
    mix = ['[vz1]', '[trd]', '[im0]', '[ri]']
    for i, c in enumerate(cortes):
        ins += ['-i', os.path.join(S, 'whoosh.mp3')]
        fc.append(f"[{5+i}:a]volume=0.35,adelay={ms(max(0, c-.12))}[w{i}]"); mix.append(f'[w{i}]')
    fc.append(''.join(mix) + f"amix=inputs={len(mix)}:normalize=0,atrim=0:{dur},alimiter=limit=0.95[a]")
    out = os.path.join(D, f"wf-motion2-{n:02d}-{r['slug']}.mp4")
    run(ins + ['-filter_complex', ';'.join(fc), '-map', '[v]', '-map', '[a]', '-t', str(dur), '-c:v', 'libx264', '-crf', '23', '-preset', 'medium',
               '-maxrate', '7M', '-bufsize', '14M', '-c:a', 'aac', '-b:a', '160k', '-movflags', '+faststart', out])
    run(['-i', out, '-frames:v', '1', '-q:v', '3', os.path.join(D, f'capa-{n:02d}.jpg')])
    print('ok', out, os.path.getsize(out) // 1024, 'KB', flush=True)
# folha dos 3 primeiros segundos (1 quadro a cada 0,25 s) de cada vídeo
ins = sum([['-t', '3', '-i', os.path.join(D, f"wf-motion2-{n:02d}-{R[n]['slug']}.mp4")] for n in R], [])
fc = ';'.join(f'[{i}:v]fps=4,scale=135:240,tile=12x1[r{i}]' for i in range(5)) + ';' + ''.join(f'[r{i}]' for i in range(5)) + 'vstack=5'
run(ins + ['-filter_complex', fc, '-frames:v', '1', os.path.join(D, 'folha-3s.jpg')])
