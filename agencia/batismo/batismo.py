import subprocess,os,sys
D='/tmp/claude-0/-home-user/c1fb54f8-61bf-52aa-9049-035c33a63c60/scratchpad/drive'; S=os.path.dirname(D)
F=S+'/fonts'; W,H,FPS=1080,1920,30
def run(c): subprocess.run(c,check=True)
def dur(f): return float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f]))
GRADE="eq=contrast=1.07:saturation=1.15:gamma=1.02,colorbalance=rs=0.035:gs=0.01:bs=-0.035:rh=0.02:bh=-0.02,vignette=PI/5"
os.makedirs(D+'/seg',exist_ok=True)

def clip(name,src,t0,t1,speed=1.0,flash_at=None):
    """trecho do vídeo, 1080x1920, cor emocional; speed<1 = câmera lenta com interpolação"""
    out=f'{D}/seg/{name}.mp4'
    vf=f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},{GRADE}"
    af="aresample=48000,aformat=channel_layouts=stereo"
    if speed!=1.0:
        vf+=f",setpts=PTS/{speed},minterpolate=fps={FPS}:mi_mode=mci:mc_mode=aobmc:vsbmc=1"
        af+=f",atempo={speed}"
    vf+=f",fps={FPS}"
    if flash_at is not None:   # clarão de luz no momento em que sai da água
        vf+=f",eq=brightness='if(between(t,{flash_at},{flash_at+0.9}),0.55*exp(-3*(t-{flash_at})),0)':eval=frame"
    run(['ffmpeg','-v','error','-y','-ss',str(t0),'-t',str(t1-t0),'-i',f'{D}/{src}','-vf',vf,'-af',af,'-c:v','libx264','-crf','17','-preset','fast','-pix_fmt','yuv420p','-c:a','aac','-b:a','192k',out])
    return out

def photo(name,src,L):
    out=f'{D}/seg/{name}.mp4'; n=int(L*FPS)+2
    run(['ffmpeg','-v','error','-y','-loop','1','-framerate',str(FPS),'-t',str(L),'-i',f'{D}/{src}','-f','lavfi','-t',str(L),'-i','anullsrc=r=48000:cl=stereo',
         '-filter_complex',f"[0:v]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},scale={W*2}:{H*2},zoompan=z='1.0+0.12*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s={W}x{H}:fps={FPS},{GRADE},setsar=1[v]",
         '-map','[v]','-map','1:a','-c:v','libx264','-crf','17','-pix_fmt','yuv420p','-c:a','aac','-shortest',out])
    return out

def ass(caps,titles,path):
    def ts(t): h=int(t//3600);m=int(t%3600//60);s=t%60;return f'{h}:{m:02d}:{s:05.2f}'
    hdr=('[Script Info]\nPlayResX: 1080\nPlayResY: 1920\nScriptType: v4.00+\n[V4+ Styles]\n'
     'Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding\n'
     'Style: C,Montserrat,58,&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,-1,0,0,0,100,100,0,0,1,3,2,2,90,90,330,1\n'
     'Style: T,Montserrat Black,120,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,-1,-1,0,0,100,100,2,0,1,0,6,5,60,60,0,1\n'
     'Style: S,Montserrat,46,&H0066D4FF,&H0066D4FF,&H00000000,&H00000000,-1,0,0,0,100,100,8,0,1,0,3,5,60,60,0,1\n'
     'Style: V,Montserrat,56,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,-1,-1,0,0,100,100,0,0,1,0,3,5,110,110,0,1\n'
     '[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n')
    ev=[]
    for a,b,t in caps: ev.append(f'Dialogue: 0,{ts(a)},{ts(b)},C,,0,0,0,,{{\\fad(150,150)}}{t}')
    for a,b,st,t,pos in titles: ev.append(f'Dialogue: 1,{ts(a)},{ts(b)},{st},,0,0,0,,{{\\fad(500,600)\\pos({pos[0]},{pos[1]})}}{t}')
    open(path,'w').write(hdr+'\n'.join(ev)+'\n')

def sfx():
    # whoosh, subida (riser) e impacto grave, sintetizados
    run(['ffmpeg','-v','error','-y','-f','lavfi','-i','anoisesrc=d=0.7:c=pink:a=0.5','-af','highpass=f=300,lowpass=f=6000,afade=t=in:d=0.35,afade=t=out:st=0.35:d=0.35,volume=0.6','-ar','48000','-ac','2',f'{D}/seg/whoosh.wav'])
    run(['ffmpeg','-v','error','-y','-f','lavfi','-i','anoisesrc=d=2.5:c=white:a=0.4','-af',"highpass=f=200,lowpass=f=2500,afade=t=in:d=2.3:curve=exp,afade=t=out:st=2.35:d=0.15,volume=0.5",'-ar','48000','-ac','2',f'{D}/seg/riser.wav'])
    run(['ffmpeg','-v','error','-y','-f','lavfi','-i','sine=f=48:d=2','-f','lavfi','-i','anoisesrc=d=0.4:c=brown:a=0.8','-filter_complex','[0]volume=1.4,afade=t=out:st=0.1:d=1.8[a];[1]lowpass=f=400,afade=t=out:d=0.4[b];[a][b]amix=2:normalize=0','-ar','48000','-ac','2',f'{D}/seg/impact.wav'])

def build(nome,segs,music,moff,mus_env,caps,titles,flash_t,out):
    # segs: lista de arquivos; transição com luz quente entre cenas
    starts=[];t=0
    for s in segs: starts.append(t); t+=dur(s)
    T=t
    ins=[];fc='';
    for i,s in enumerate(segs):
        ins+=['-i',s]; fl=',fade=t=in:st=0:d=0.25:color=white' if i else ',fade=t=in:st=0:d=0.8'
        fc+=f'[{i}:v]setpts=PTS-STARTPTS,setsar=1{fl}[v{i}];[{i}:a]asetpts=PTS-STARTPTS[a{i}];'
    fc+=''.join(f'[v{i}][a{i}]' for i in range(len(segs)))+f'concat=n={len(segs)}:v=1:a=1[cv][ca];'
    n=len(segs)
    ins+=['-ss',str(moff),'-i',music]; mi=n; n+=1
    # envelope da música: lista (t, vol) interpolada linear
    expr='0'
    for (a,va),(b,vb) in zip(mus_env,mus_env[1:]):
        expr=f"if(between(t,{a},{b}),{va}+({vb}-{va})*(t-{a})/{max(b-a,0.01)},{expr})"
    fc+=f"[{mi}:a]aresample=48000,aformat=channel_layouts=stereo,atrim=0:{T},volume='{expr}':eval=frame,afade=t=out:st={T-3}:d=3[mu];"
    mix=['[ca]','[mu]']
    for k,st in enumerate(starts[1:]):
        ins+=['-i',f'{D}/seg/whoosh.wav']; d=max(0,int(st*1000)-250); fc+=f'[{n}:a]adelay={d}|{d}[w{k}];'; mix.append(f'[w{k}]'); n+=1
    ins+=['-i',f'{D}/seg/riser.wav']; d=int((flash_t-2.4)*1000); fc+=f'[{n}:a]adelay={d}|{d}[ri];'; mix.append('[ri]'); n+=1
    ins+=['-i',f'{D}/seg/impact.wav']; d=int(flash_t*1000); fc+=f'[{n}:a]adelay={d}|{d}[im];'; mix.append('[im]'); n+=1
    fc+=''.join(mix)+f'amix=inputs={len(mix)}:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11[aout];'
    # brilho dourado (light leak) suave sobre tudo + grão
    fc+=(f"color=c=0xffb347:s={W}x{H}:r={FPS}:d={T}[lk];[lk]format=rgba,geq=r='255':g='170':b='70':a='70*pow(max(0,1-hypot(X-{W}*(0.5+0.4*sin(T*0.35)),Y-{H}*0.15)/{W}),2)'[lk2];"
         f"[cv][lk2]overlay=shortest=1,noise=alls=7:allf=t,ass={out}.ass:fontsdir={F}[vout]")
    ass(caps,titles,out+'.ass')
    run(['ffmpeg','-v','error','-y',*ins,'-filter_complex',fc,'-map','[vout]','-map','[aout]','-t',f'{T}','-r',str(FPS),'-c:v','libx264','-crf','18','-preset','medium','-pix_fmt','yuv420p','-c:a','aac','-b:a','192k','-movflags','+faststart',out])
    print('ok',out,round(T,2))
