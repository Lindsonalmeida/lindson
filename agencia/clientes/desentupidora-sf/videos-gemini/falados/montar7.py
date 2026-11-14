import subprocess,sys,os,json,difflib,re
S='/tmp/claude-0/-home-user/c1fb54f8-61bf-52aa-9049-035c33a63c60/scratchpad'; C=S+'/cl'; A=S+'/av'
OUT='/home/user/lindson/agencia/clientes/desentupidora-sf/videos-gemini'
FPS=25
def run(c): subprocess.run(c,check=True)
def dur(f): return float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f]))
def ts(t): h=int(t//3600);m=int(t%3600//60);s=t%60;return f'{h}:{m:02d}:{s:05.2f}'
def bed(name):
    base=name.split('_')[-1]
    d={'pl5':'sep3','sl':'sep3','p2':'sep2'}.get(name.split('_')[0] if '_' in name else '','sep')
    return f'{C}/{d}/out/htdemucs/{base}/no_vocals.wav'
SCRIPTS=json.load(open(A+'/scripts.json'))
_wm=None
def words(clip):
    global _wm
    cache=f'{A}/{clip}.words.json'
    if os.path.exists(cache): return json.load(open(cache))
    import whisper,warnings;warnings.filterwarnings('ignore')
    if _wm is None: _wm=whisper.load_model('small')
    r=_wm.transcribe(f'{A}/{clip}.mp4',language='pt',word_timestamps=True)
    ww=[(w['word'].strip(),w['start'],w['end']) for s in r['segments'] for w in s['words']]
    toks=SCRIPTS[clip].split()
    norm=lambda x:re.sub(r'[^a-zà-ú0-9]','',x.lower())
    sm=difflib.SequenceMatcher(a=[norm(t) for t in toks],b=[norm(w[0]) for w in ww])
    tim=[None]*len(toks)
    for a,b,n in sm.get_matching_blocks():
        for k in range(n): tim[a+k]=(ww[b+k][1],ww[b+k][2])
    # interpola os que não casaram
    st=ww[0][1] if ww else 0.2; en=ww[-1][2] if ww else dur(f'{A}/{clip}.mp4')-0.2
    i=0
    while i<len(toks):
        if tim[i] is None:
            j=i
            while j<len(toks) and tim[j] is None: j+=1
            a=tim[i-1][1] if i>0 else st; b=tim[j][0] if j<len(toks) else en
            n=j-i; step=(b-a)/n
            for k in range(n): tim[i+k]=(a+k*step,a+(k+1)*step)
            i=j
        else: i+=1
    res=[(t,a,b) for t,(a,b) in zip(toks,tim)]
    json.dump(res,open(cache,'w'),ensure_ascii=False); return res

def build(v,plan,hook):
    segs=[];t=0;caps=[];card_at=None
    for el in plan:
        if el[0]=='av':
            clip,cuts=el[1],el[2]; d=dur(f'{A}/{clip}.mp4')
            ws=words(clip); i=0
            while i<len(ws):
                w,a,b=ws[i]
                if w=='Esse' and i+1<len(ws) and ws[i+1][0].startswith('Efe'):
                    caps.append(('SF'+ws[i+1][0][3:],t+a,t+ws[i+1][2])); i+=2; continue
                caps.append((w,t+a,t+b)); i+=1
            segs.append(('av',clip,d,cuts,t));
            if len(el)>3 and el[3]=='card': card_at=t+0.5
            t+=d
        else:
            segs.append(('b',el[1],el[2],None,t)); t+=el[2]
    T=t+0.8
    # vídeo
    ins=[];fc='';n=0;labels=[]
    for k,(kind,name,d,cuts,t0) in enumerate(segs):
        if kind=='av':
            ins+=['-i',f'{A}/{name}.mp4']; base=n; n+=1
            fc+=f'[{base}:v]scale=1080:1920,setsar=1,fps={FPS},trim=0:{d:.3f},setpts=PTS-STARTPTS[a{k}];'
            cur=f'a{k}'
            for j,(shot,f0,f1) in enumerate(cuts or []):
                ins+=['-i',f'{C}/{shot}.mp4']; bi=n; n+=1
                s0,s1=d*f0,d*f1
                fc+=f'[{bi}:v]scale=1097:1920,crop=1080:1920,setsar=1,setpts=(PTS-STARTPTS)*{FPS}/24,fps={FPS},trim=0:{s1-s0:.3f},setpts=PTS-STARTPTS+{s0:.3f}/TB[c{k}{j}];'
                fc+=f"[{cur}][c{k}{j}]overlay=enable='between(t,{s0:.3f},{s1:.3f})':eof_action=pass[o{k}{j}];"; cur=f'o{k}{j}'
            if k==len(segs)-1:
                fc+=f'[{cur}]tpad=stop_mode=clone:stop_duration=0.8[e{k}];'; cur=f'e{k}'
            fl=',fade=t=in:st=0:d=0.08:color=white' if k else ''
            fc+=f'[{cur}]null{fl}[s{k}];'
        else:
            ins+=['-i',f'{C}/{name}.mp4']; bi=n; n+=1
            fc+=f'[{bi}:v]scale=1097:1920,crop=1080:1920,setsar=1,setpts=(PTS-STARTPTS)*{FPS}/24,fps={FPS},trim=0:{d:.3f},setpts=PTS-STARTPTS,fade=t=in:st=0:d=0.08:color=white[s{k}];'
        labels.append(f'[s{k}]')
    fc+=''.join(labels)+f'concat=n={len(segs)}:v=1:a=0[cv]'
    run(['ffmpeg','-v','error','-y',*ins,'-filter_complex',fc,'-map','[cv]','-c:v','libx264','-crf','16','-preset','fast','-pix_fmt','yuv420p',f'{A}/cv{v}.mp4'])
    # áudio: fala do próprio avatar + fundo das cenas + whoosh nos cortes
    ai=[];af='';mix=[];n=0
    for k,(kind,name,d,cuts,t0) in enumerate(segs):
        ms=int(t0*1000)
        if kind=='av':
            ai+=['-i',f'{A}/{name}.mp4']; af+=f'[{n}:a]aresample=48000,aformat=channel_layouts=stereo,adelay={ms}|{ms}[x{n}];'; mix.append(f'[x{n}]'); n+=1
            for j,(shot,f0,f1) in enumerate(cuts or []):
                s0=int((t0+d*f0)*1000); L=d*(f1-f0)
                ai+=['-i',bed(shot)]; af+=f'[{n}:a]aresample=48000,aformat=channel_layouts=stereo,atrim=0:{L:.3f},volume=0.35,adelay={s0}|{s0}[x{n}];'; mix.append(f'[x{n}]'); n+=1
        else:
            ai+=['-i',bed(name)]; af+=f'[{n}:a]aresample=48000,aformat=channel_layouts=stereo,atrim=0:{d:.3f},volume=0.7,adelay={ms}|{ms}[x{n}];'; mix.append(f'[x{n}]'); n+=1
        if k:
            ai+=['-i',f'{C}/whoosh.wav']; w=max(0,ms-180); af+=f'[{n}:a]aresample=48000,volume=0.55,adelay={w}|{w}[x{n}];'; mix.append(f'[x{n}]'); n+=1
    ai=['-f','lavfi','-t',f'{T:.3f}','-i','anullsrc=r=48000:cl=stereo']+ai
    af=re.sub(r'\[(\d+):a\]',lambda m:f'[{int(m.group(1))+1}:a]',af)
    af+='[0:a]'+''.join(mix)+f'amix=inputs={len(mix)+1}:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000[a]'
    run(['ffmpeg','-v','error','-y',*ai,'-filter_complex',af,'-map','[a]','-c:a','pcm_s16le',f'{A}/ca{v}.wav'])
    # legenda palavra por palavra (some quando entra o cartão)
    groups=[];g=[]
    for w in caps:
        if card_at and w[1]>=card_at: break
        g.append(w)
        if len(g)==3 or w[0][-1] in '.,?!:': groups.append(g);g=[]
    if g: groups.append(g)
    ev=[]
    for gi,g in enumerate(groups):
        nxt=groups[gi+1][0][1] if gi+1<len(groups) else g[-1][2]+0.3
        gend=min(g[-1][2]+0.25,nxt)
        for wi,w in enumerate(g):
            a=w[1]; b=g[wi+1][1] if wi+1<len(g) else gend
            txt=' '.join(('{\\c&H00008AFF&}'+x[0]+'{\\c&H00FFFFFF&}') if j==wi else x[0] for j,x in enumerate(g))
            txt=txt.replace('Esse Efe','SF').replace('Esse','SF') if False else txt
            ev.append(f'Dialogue: 0,{ts(a)},{ts(max(b,a+0.05))},L,,0,0,0,,{txt}')
    ass=('[Script Info]\nPlayResX: 1080\nPlayResY: 1920\nScriptType: v4.00+\n[V4+ Styles]\n'
         'Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding\n'
         'Style: L,Montserrat,88,&H00FFFFFF,&H00FFFFFF,&H1A4A1A06,&H1A4A1A06,-1,0,0,0,100,100,0,0,3,14,0,2,60,60,560,1\n'
         '[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n'+'\n'.join(ev)+'\n')
    open(f'{A}/leg{v}.ass','w').write(ass)
    oi=['-i',f'{A}/cv{v}.mp4','-i',f'{A}/ca{v}.wav','-loop','1','-framerate',str(FPS),'-i',f'{S}/selo.png','-loop','1','-framerate',str(FPS),'-i',f'{S}/gancho{hook}.png','-loop','1','-framerate',str(FPS),'-i',f'{S}/fim.png']
    ca=card_at or (T-4)
    fc=(f"[0:v]ass={A}/leg{v}.ass:fontsdir={S}/fonts[l];[3]fade=t=out:st=2.3:d=0.3:alpha=1[g];[4]fade=t=in:st={ca:.2f}:d=0.35:alpha=1[f];"
        f"[l][2]overlay=0:15:shortest=1[x0];[x0][g]overlay=0:15:enable='lt(t,2.6)':shortest=1[x1];[x1][f]overlay=0:15:enable='gte(t,{ca:.2f})':shortest=1[vv]")
    run(['ffmpeg','-v','error','-y',*oi,'-filter_complex',fc,'-map','[vv]','-map','1:a','-t',f'{T:.3f}','-r',str(FPS),'-c:v','libx264','-crf','19','-preset','medium','-pix_fmt','yuv420p','-c:a','aac','-b:a','192k','-movflags','+faststart',f'{OUT}/sf-falado-{v}.mp4'])
    print('ok',v,round(T,2))

PLANS={
 '1':([('av','v1_cli1',[]),('b','pl5_v1c3',2.4),('av','v1_tec',[('pl5_v1c4',0.45,0.9)]),('b','pl5_v1c5',2.6),('av','v1_cli2',[]),('av','v1_num',[],'card')],1),
 '2':([('av','v2_t1',[('v2c1',0.5,1.0)]),('av','v2_t2',[('v2c2',0.25,0.6),('v2c3',0.6,1.0)]),('av','v2_t3',[('v2c4',0.45,1.0)]),('b','p2_v2c5',2.6),('av','coz_num',[],'card')],2),
 '3':([('av','v3_m1',[]),('av','v3_q1',[('p2_v3c2',0.45,1.0)]),('b','v3c4',2.6),('av','v3_m2',[]),('b','pl5_v3c5',2.2),('av','v3_num',[],'card')],3),
 '4':([('av','v4_d1',[]),('b','sl_v4c1',2.0),('av','v4_k1',[('pl5_v4c3',0.3,0.62),('p2_v4c4',0.62,1.0)]),('av','v4_d2',[]),('b','pl5_v4c5',2.2),('av','coz_num',[],'card')],4)}
for v in sys.argv[1]:
    p,h=PLANS[v]; build(v,p,h)
