import subprocess,os,sys
S=sys.argv[1]; C=S+'/cl'; OUT='/home/user/lindson/agencia/clientes/desentupidora-sf/videos-gemini'
def run(c): subprocess.run(c,check=True)
def dur(f): return float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f]))
falas=[l.split('\t')[0] for l in open(S+'/vo/falas.tsv',encoding='utf-8')]
off={k:0.4 for k in falas}; off.update({'v2c5':0.3,'v1c5a':0.3,'v1c5b':3.7,'v4c5a':0.2,'v4c5b':3.3})
D={k:dur(f'{S}/vo/{k}.wav') for k in falas}
for v in (sys.argv[2] if len(sys.argv)>2 else '1234'):
    segs=[];beds=[]
    for c in '12345':
        s=f'v{v}c{c}'
        cands=[f'{C}/pl_{s}.mp4',f'{C}/p2_{s}.mp4',f'{C}/ls_{s}.mp4',f'{C}/{s}.mp4']
        vid=next(x for x in cands if os.path.exists(x)); segs.append(vid)
        b2=f'{C}/sep2/out/htdemucs/{s}/no_vocals.wav'; beds.append(b2 if os.path.exists(b2) else f'{C}/sep/out/htdemucs/{s}/no_vocals.wav')
        print(v,c,os.path.basename(vid))
    # vídeo: 5 cenas a 24 fps, flash branco nos cortes
    ins=[];fc=''
    for i,sg in enumerate(segs):
        ins+=['-i',sg]
        fl=',fade=t=in:st=0:d=0.12:color=white' if i else ''
        fc+=f'[{i}:v]trim=0:8,setpts=PTS-STARTPTS,scale=1097:1920,crop=1080:1920,setsar=1,fps=24{fl}[s{i}];'
    fc+=''.join(f'[s{i}]' for i in range(5))+'concat=n=5:v=1:a=0[cv]'
    run(['ffmpeg','-v','error','-y',*ins,'-filter_complex',fc,'-map','[cv]','-c:v','libx264','-crf','16','-preset','fast','-pix_fmt','yuv420p',f'{C}/cv{v}.mp4'])
    # áudio: uma faixa só de 40 s (fundo + vozes + whoosh), sem emendas
    ains=[];af=''
    for i,b in enumerate(beds):
        ains+=['-i',b]; af+=f'[{i}:a]aresample=48000,aformat=channel_layouts=stereo,atrim=0:8,asetpts=PTS-STARTPTS,apad=whole_dur=8,volume=1.1[b{i}];'
    af+=''.join(f'[b{i}]' for i in range(5))+'concat=n=5:v=0:a=1[bed];'
    n=5; mix=['[bed]']
    for k in [k for k in falas if k.startswith(f'v{v}')]:
        t=(int(k[3])-1)*8+off[k]; ains+=['-i',f'{S}/vo/{k}.wav']
        af+=f'[{n}:a]aresample=48000,aformat=channel_layouts=stereo,volume=1.7,adelay={int(t*1000)}|{int(t*1000)}[v{n}];'; mix.append(f'[v{n}]'); n+=1
    for c in range(1,5):
        ains+=['-i',f'{C}/whoosh.wav']; af+=f'[{n}:a]aresample=48000,adelay={c*8000-250}|{c*8000-250}[w{n}];'; mix.append(f'[w{n}]'); n+=1
    af+=''.join(mix)+f'amix=inputs={len(mix)}:duration=first:normalize=0,atrim=0:40,loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000[a]'
    run(['ffmpeg','-v','error','-y',*ains,'-filter_complex',af,'-map','[a]','-c:a','pcm_s16le',f'{C}/ca{v}.wav'])
    # overlays
    oi=['-i',f'{C}/cv{v}.mp4','-i',f'{C}/ca{v}.wav','-loop','1','-framerate','24','-i',f'{S}/selo.png','-loop','1','-framerate','24','-i',f'{S}/gancho{v}.png','-loop','1','-framerate','24','-i',f'{S}/fim.png']
    fc="[3]fade=t=out:st=2.6:d=0.3:alpha=1[g];[4]fade=t=in:st=36.6:d=0.4:alpha=1[f];[0:v][2]overlay=0:15:shortest=1[x0];[x0][g]overlay=0:15:enable='lt(t,3)':shortest=1[x1]"
    last='x1'; n=5
    for k in [k for k in falas if k.startswith(f'v{v}')]:
        a=(int(k[3])-1)*8+off[k]; b=a+D[k]; oi+=['-loop','1','-framerate','24','-i',f'{S}/leg_{k}.png']
        fc+=f";[{last}][{n}]overlay=0:15:enable='between(t,{a+0.2:.2f},{b:.2f})':shortest=1[y{n}]"; last=f'y{n}'; n+=1
    fc+=f";[{last}][f]overlay=0:15:enable='gte(t,36.6)':shortest=1[v]"
    run(['ffmpeg','-v','error','-y',*oi,'-filter_complex',fc,'-map','[v]','-map','1:a','-t','40','-r','24','-c:v','libx264','-crf','19','-preset','medium','-pix_fmt','yuv420p','-c:a','aac','-b:a','192k','-movflags','+faststart',f'{OUT}/sf-video-{v}-v4.mp4'])
    print('ok',v)
