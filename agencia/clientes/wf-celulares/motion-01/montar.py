# Junta quadros + voz APROVADA pelo Lindson (Giuseppe Multilingual +4%, agencia/processos/vozes-ia.md) + SFX + trilha Mixkit com ducking · conta Leandro · 10/11/2026
# Uso: python3 montar.py  (precisa de tmp/v<N>/ do render.js). SSL_CERT_FILE e HTTPS_PROXY para o edge-tts no ambiente.
import os, json, subprocess
D = os.path.dirname(os.path.abspath(__file__)); S = os.path.join(D, '..', 'video-processo', 'som'); T = os.path.join(D, 'tmp')
V = json.load(open(os.path.join(D, 'produtos.json')))
run = lambda a: subprocess.run(['ffmpeg', '-v', 'error', '-y'] + a, check=True)
riser = os.path.join(T, 'riser.wav')  # riser sintetizado (varredura + ruído), sobe até o preço
run(['-f', 'lavfi', '-i', "aevalsrc='0.25*sin(2*PI*(200+900*t*t/4)*t)*t/2.2':d=2.2:s=44100", '-f', 'lavfi', '-i', 'anoisesrc=d=2.2:c=pink:a=0.12',
     '-filter_complex', '[1]afade=t=in:d=2.1,highpass=f=2000[n];[0][n]amix=2,afade=t=out:st=2.1:d=0.1', riser])
for i, p in enumerate(V):
    n = p['n']; vz = os.path.join(T, f'voz{n}.wav')
    mp3 = vz.replace('.wav', '.mp3')
    subprocess.run(['edge-tts', '--proxy', os.environ.get('HTTPS_PROXY', ''), '--voice', 'it-IT-GiuseppeMultilingualNeural', '--rate=+4%', '--text', p['voz'], '--write-media', mp3], check=True)
    run(['-i', mp3, '-af', 'highpass=f=80,equalizer=f=180:t=q:w=1:g=2,acompressor=threshold=-20dB:ratio=3:makeup=2,loudnorm=I=-15:TP=-1', '-ar', '44100', vz])
    out = os.path.join(D, f"wf-motion-{n:02d}-{p['slug']}.mp4")
    ms = lambda s: f'{int(s*1000)}|{int(s*1000)}'
    fc = (f"[0:v]tmix=frames=2,noise=alls=6:allf=t,format=yuv420p[v];"
          f"[1:a]adelay={ms(.7)},apad,aformat=channel_layouts=stereo[vz];[vz]asplit[vz1][vz2];"
          f"[2:a]atrim=start={20+i*31},asetpts=PTS-STARTPTS,atrim=0:14,volume=0.4,afade=t=in:d=0.5,afade=t=out:st=12.5:d=1.5[tr];"
          f"[tr][vz2]sidechaincompress=threshold=0.03:ratio=8:attack=20:release=300[trd];"
          f"[3:a]volume=.5,adelay={ms(.2)}[w1];[4:a]volume=.5,adelay={ms(10.35)}[w2];[5:a]volume=.6,adelay={ms(5.95)}[im];[6:a]volume=.7,adelay={ms(3.85)}[ri];"
          f"[vz1][trd][w1][w2][im][ri]amix=inputs=6:normalize=0,atrim=0:14,alimiter=limit=.95[a]")
    run(['-framerate', '30', '-i', os.path.join(T, f'v{n}', '%04d.jpg'), '-i', vz, '-i', os.path.join(S, 'trilha.mp3'),
         '-i', os.path.join(S, 'whoosh.mp3'), '-i', os.path.join(S, 'whoosh.mp3'), '-i', os.path.join(S, 'impacto.mp3'), '-i', riser,
         '-filter_complex', fc, '-map', '[v]', '-map', '[a]', '-t', '14', '-c:v', 'libx264', '-crf', '23', '-preset', 'medium', '-maxrate', '7M', '-bufsize', '14M',
         '-c:a', 'aac', '-b:a', '160k', '-movflags', '+faststart', out])
    run(['-ss', '8.5', '-i', out, '-frames:v', '1', '-q:v', '3', os.path.join(D, f"capa-{n:02d}.jpg")])
    print('ok', out, os.path.getsize(out) // 1024, 'KB', flush=True)
