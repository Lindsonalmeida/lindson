import subprocess,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from palavras import W,CUTS,SHOTS
S=sys.argv[1]; C=S+'/cl'; Z=S+'/z'; OUT='/home/user/lindson/agencia/clientes/desentupidora-sf/videos-gemini'
def run(c): subprocess.run(c,check=True)
def dur(f): return float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f]))
def ts(t): h=int(t//3600);m=int(t%3600//60);s=t%60;return f'{h}:{m:02d}:{s:05.2f}'
def bed(name):
    base=name.split('_')[-1]
    d={'pl5':'sep3','sl':'sep3','p2':'sep2'}.get(name.split('_')[0] if '_' in name else '','sep')
    return f'{C}/{d}/out/htdemucs/{base}/no_vocals.wav'
for v in [int(x) for x in sys.argv[2]]:
    nar=f'{Z}/n{v}.wav'; T=round(dur(nar)+1.0,2); cuts=CUTS[v]+[T]; shots=SHOTS[v]
    lens=[cuts[i+1]-cuts[i] for i in range(4)]+[T-cuts[4]]
    # legendas palavra por palavra (ASS)
    words=[(w.rsplit(' ',2)[0],float(w.rsplit(' ',2)[1]),float(w.rsplit(' ',2)[2])) for w in W[v].split('|')]
    groups=[];g=[]
    for w in words:
        g.append(w)
        if len(g)==3 or w[0][-1] in '.,?!:': groups.append(g);g=[]
    if g: groups.append(g)
    ev=[]
    for gi,g in enumerate(groups):
        gend=min(g[-1][2]+0.25, groups[gi+1][0][1] if gi+1<len(groups) else cuts[5])
        for wi,w in enumerate(g):
            a=w[1] if wi else min(w[1], g[0][1]); b=g[wi+1][1] if wi+1<len(g) else gend
            txt=' '.join(('{\\c&H00008AFF&}'+x[0]+'{\\c&H00FFFFFF&}') if j==wi else x[0] for j,x in enumerate(g))
            ev.append(f'Dialogue: 0,{ts(a)},{ts(b)},L,,0,0,0,,{txt}')
    ass=f'''[Script Info]
PlayResX: 1080
PlayResY: 1920
ScriptType: v4.00+
[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: L,Montserrat,92,&H00FFFFFF,&H00FFFFFF,&H1A4A1A06,&H1A4A1A06,-1,0,0,0,100,100,0,0,3,14,0,2,60,60,640,1
[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
'''+'\n'.join(ev)+'\n'
    open(f'{Z}/leg{v}.ass','w').write(ass)
    # vídeo: cortes no começo de cada frase; fundo do cartão = 1ª cena desfocada (em movimento)
    segs=list(zip(shots,lens[:4]))+[(shots[4],cuts[5]-cuts[4]),(shots[0],T-cuts[5])]
    ins=[];fc=''
    for i,(sh,L) in enumerate(segs):
        ins+=['-i',f'{C}/{sh}.mp4']
        fl=',fade=t=in:st=0:d=0.10:color=white' if 0<i<5 else ''
        pad=f',tpad=stop_mode=clone:stop_duration={max(0,L-7.95):.2f}' if L>7.95 else ''
        bl=',boxblur=24:2,eq=brightness=-0.12' if i==5 else ''
        zoom={'sl_v4c2':'crop=620:1100:430:780,'}.get(sh,'')
        fc+=f'[{i}:v]{zoom}scale=1097:1920,crop=1080:1920,setsar=1,fps=24{pad},trim=0:{L:.3f},setpts=PTS-STARTPTS{bl}{fl}[s{i}];'
    fc+='[s0][s1][s2][s3][s4][s5]concat=n=6:v=1:a=0[cv]'
    run(['ffmpeg','-v','error','-y',*ins,'-filter_complex',fc,'-map','[cv]','-c:v','libx264','-crf','16','-preset','fast','-pix_fmt','yuv420p',f'{Z}/cv{v}.mp4'])
    # áudio: narração única + fundo das cenas + whoosh nos cortes
    ai=['-i',nar];af='[0:a]aresample=48000,aformat=channel_layouts=stereo,apad=whole_dur='+f'{T}'+',volume=1.0[n];'
    for i,(sh,L) in enumerate(zip(shots,lens)):
        ai+=['-i',bed(sh)]; af+=f'[{i+1}:a]aresample=48000,aformat=channel_layouts=stereo,atrim=0:{min(L,8):.3f},apad=whole_dur={L:.3f},asetpts=PTS-STARTPTS,volume=0.55[b{i}];'
    af+='[b0][b1][b2][b3][b4]concat=n=5:v=0:a=1[bed];'
    mix=['[n]','[bed]']
    for k,c in enumerate(cuts[1:6]):
        ai+=['-i',f'{C}/whoosh.wav']; d=max(0,int(c*1000)-200); af+=f'[{6+k}:a]aresample=48000,volume=0.7,adelay={d}|{d}[w{k}];'; mix.append(f'[w{k}]')
    af+=''.join(mix)+f'amix=inputs={len(mix)}:duration=first:normalize=0,atrim=0:{T},loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000[a]'
    run(['ffmpeg','-v','error','-y',*ai,'-filter_complex',af,'-map','[a]','-c:a','pcm_s16le',f'{Z}/ca{v}.wav'])
    # final: legendas + logo + gancho + cartão
    oi=['-i',f'{Z}/cv{v}.mp4','-i',f'{Z}/ca{v}.wav','-loop','1','-framerate','24','-i',f'{S}/selo.png','-loop','1','-framerate','24','-i',f'{S}/gancho{v}.png','-loop','1','-framerate','24','-i',f'{S}/fim2.png']
    c5=cuts[5]
    fc=(f"[0:v]ass={Z}/leg{v}.ass:fontsdir={S}/fonts[l];[3]fade=t=out:st=2.4:d=0.3:alpha=1[g];[4]fade=t=in:st={c5:.2f}:d=0.35:alpha=1[f];"
        f"[l][2]overlay=0:15:shortest=1[x0];[x0][g]overlay=0:15:enable='lt(t,2.7)':shortest=1[x1];[x1][f]overlay=0:15:enable='gte(t,{c5:.2f})':shortest=1[vv]")
    run(['ffmpeg','-v','error','-y',*oi,'-filter_complex',fc,'-map','[vv]','-map','1:a','-t',f'{T}','-r','24','-c:v','libx264','-crf','19','-preset','medium','-pix_fmt','yuv420p','-c:a','aac','-b:a','192k','-movflags','+faststart',f'{OUT}/sf-video-{v}-v6.mp4'])
    print('ok',v,T)
