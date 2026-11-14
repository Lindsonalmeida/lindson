import subprocess,os,sys
S=sys.argv[1]; OUT='/home/user/lindson/agencia/clientes/desentupidora-sf/videos-gemini'
dur={}
for l in open(S+'/vo/falas.tsv',encoding='utf-8'):
    k=l.split('\t')[0]; dur[k]=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f'{S}/vo/{k}.wav']))
off={k:0.4 for k in dur}; off.update({'v2c5':0.3,'v1c5a':0.3,'v1c5b':3.7,'v4c5a':0.2,'v4c5b':3.3})
def run(c): subprocess.run(c,check=True)
for v in '1234':
    parts=[]
    for c in '12345':
        s=f'v{v}c{c}'; ls=f'{S}/cl/ls_{s}.mp4'; vid=ls if os.path.exists(ls) else f'{S}/cl/{s}.mp4'
        bed=f'{S}/cl/sep/out/htdemucs/{s}/no_vocals.wav'; voz=f'{S}/vo/t_{s}.wav'
        vf='scale=1097:1920,crop=1080:1920,setsar=1,fps=30'+(',fade=t=in:st=0:d=0.15:color=white' if c!='1' else '')
        fa=f"[1:a]aresample=48000,volume=0.8[b];[2:a]aresample=48000,aformat=channel_layouts=stereo,volume=1.6[vz];[3:a]aresample=48000{'[w]' if c!='1' else ',anullsink'};[b][vz]{'[w]' if c!='1' else ''}amix=inputs={3 if c!='1' else 2}:duration=first:normalize=0[a]"
        o=f'{S}/cl/q{v}_{c}.mp4'; parts.append(o)
        run(['ffmpeg','-v','error','-y','-i',vid,'-i',bed,'-i',voz,'-i',f'{S}/cl/whoosh.wav','-filter_complex',f'[0:v]{vf}[v];{fa}','-map','[v]','-map','[a]','-t','8','-c:v','libx264','-crf','18','-preset','fast','-c:a','aac','-b:a','192k',o])
    open(f'{S}/cl/m{v}.txt','w').write(''.join(f"file '{p}'\n" for p in parts))
    run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',f'{S}/cl/m{v}.txt','-c','copy',f'{S}/cl/k{v}.mp4'])
    ins=['-i',f'{S}/cl/k{v}.mp4','-loop','1','-i',f'{S}/selo.png','-loop','1','-i',f'{S}/gancho{v}.png','-loop','1','-i',f'{S}/fim.png']
    fc='[2]fade=t=out:st=2.6:d=0.3:alpha=1[g];[3]fade=t=in:st=36.6:d=0.4:alpha=1[f];[0:v][1]overlay=0:15:shortest=1[x0];[x0][g]overlay=0:15:enable=\'lt(t,3)\':shortest=1[x1]'
    n=4; last='x1'
    for k in [k for k in dur if k.startswith(f'v{v}')]:
        c=int(k[3]); a=(c-1)*8+off[k]; b=a+dur[k]
        ins+=['-loop','1','-i',f'{S}/leg_{k}.png']
        fc+=f";[{last}][{n}]overlay=0:15:enable='between(t,{a+0.2:.2f},{b:.2f})':shortest=1[y{n}]"; last=f'y{n}'; n+=1
    fc+=f";[{last}][f]overlay=0:15:enable='gte(t,36.6)':shortest=1[v]"
    run(['ffmpeg','-v','error','-y',*ins,'-filter_complex',fc,'-map','[v]','-map','0:a','-af','loudnorm=I=-14:TP=-1.5:LRA=11','-t','40','-c:v','libx264','-crf','20','-preset','medium','-pix_fmt','yuv420p','-c:a','aac','-b:a','192k','-ar','48000','-movflags','+faststart',f'{OUT}/sf-video-{v}-v2.mp4'])
    print('ok',v)
