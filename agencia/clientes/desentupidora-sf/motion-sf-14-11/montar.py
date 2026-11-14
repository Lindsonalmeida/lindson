# Junta quadros (tmp/v<N>/) + voz Antonio + trilha Mixkit #623 com ducking + whoosh em cada corte + impacto no 0 e no CTA
# + riser antes do CTA + tmix (motion blur) + grão · base wf-celulares/motion-02/montar.py (conta Leandro) · conta Zuleide 14/11/2026
import os, sys, json, subprocess
D = os.path.dirname(os.path.abspath(__file__)); S = os.path.join(D, '..', '..', 'wf-celulares', 'video-processo', 'som'); T = os.path.join(D, 'tmp')
R = {r['n']: r for r in json.load(open(os.path.join(D, 'roteiros.json')))}
run = lambda a: subprocess.run(['ffmpeg', '-v', 'error', '-y'] + a, check=True)
riser = os.path.join(T, 'riser.wav')
if not os.path.exists(riser):
    run(['-f', 'lavfi', '-i', "aevalsrc='0.25*sin(2*PI*(200+900*t*t/4)*t)*t/1.6':d=1.6:s=44100", '-f', 'lavfi', '-i', 'anoisesrc=d=1.6:c=pink:a=0.12',
         '-filter_complex', '[1]afade=t=in:d=1.5,highpass=f=2000[n];[0][n]amix=2,afade=t=out:st=1.5:d=0.1', riser])
for n in [int(x) for x in sys.argv[1:]]:
    r = R[n]; j = json.load(open(os.path.join(D, f'v{n}.json'))); dur, cortes, cta = j['dur'], j['cortes'], j['cta']
    ms = lambda s: f'{int(s*1000)}|{int(s*1000)}'
    ins = ['-framerate', '30', '-i', os.path.join(T, f'v{n}', '%04d.jpg'), '-i', os.path.join(D, 'voz', f'{n}.mp3'), '-i', os.path.join(S, 'trilha.mp3'),
           '-i', os.path.join(S, 'impacto.mp3'), '-i', os.path.join(S, 'impacto.mp3'), '-i', riser]
    fc = ["[0:v]tmix=frames=3:weights='1 2 1',noise=alls=7:allf=t,eq=saturation=1.08:contrast=1.04,format=yuv420p[v]",
          "[1:a]aformat=channel_layouts=stereo,adelay=60|60,apad,volume=1.15[vz];[vz]asplit[vz1][vz2]",
          f"[2:a]atrim=start={20+n*13},asetpts=PTS-STARTPTS,atrim=0:{dur},volume=0.42,afade=t=in:d=0.3,afade=t=out:st={dur-0.9}:d=0.9[tr]",
          "[tr][vz2]sidechaincompress=threshold=0.03:ratio=8:attack=15:release=250[trd]",
          "[3:a]volume=0.8[im0]", f"[4:a]volume=0.75,adelay={ms(cta)}[im1]", f"[5:a]volume=0.6,adelay={ms(max(0, cta-1.6))}[ri]"]
    mix = ['[vz1]', '[trd]', '[im0]', '[im1]', '[ri]']
    for i, c in enumerate(cortes[:-1]):
        ins += ['-i', os.path.join(S, 'whoosh.mp3')]
        fc.append(f"[{6+i}:a]volume=0.4,adelay={ms(max(0, c-.15))}[w{i}]"); mix.append(f'[w{i}]')
    fc.append(''.join(mix) + f"amix=inputs={len(mix)}:normalize=0,atrim=0:{dur},alimiter=limit=0.95[a]")
    pasta = os.path.join(D, f'{n:02d}'); os.makedirs(pasta, exist_ok=True)
    out = os.path.join(pasta, f"sf-motion-{n:02d}-{r['slug']}.mp4")
    run(ins + ['-filter_complex', ';'.join(fc), '-map', '[v]', '-map', '[a]', '-t', str(dur), '-c:v', 'libx264', '-crf', '21', '-preset', 'medium', '-threads', '2',
               '-maxrate', '8M', '-bufsize', '16M', '-c:a', 'aac', '-b:a', '160k', '-movflags', '+faststart', out])
    print('ok', out, os.path.getsize(out) // 1024, 'KB', flush=True)
