"""Monta os 3 Reels (conta Leandro, 16/11/2026). python3 montar.py <insumos> <banco-sfx-trilha (conteudo/reels/leva-30s/banco)>
Narração: edge-tts pt-BR-AntonioNeural (voz clonada do Lindson no HeyGen sem créditos neste dia). Vídeo: Mixkit. SFX e trilha: Mixkit.
VFX: flash de luz e desfoque de entrada em cada corte, tremor no primeiro impacto, zoom lento, grão e vinheta."""
import json,os,sys,subprocess as sp
D=os.path.dirname(os.path.abspath(__file__)); I,B=sys.argv[1],sys.argv[2]
C=json.load(open(f'{D}/cenas.json')); TR={'ADV':'pop-track-03-108bpm','BARBA':'trap-electro-vibes-112bpm','SORRISO':'midnight-funk-117bpm'}
def run(c): sp.run(c,check=True,stdout=sp.DEVNULL,stderr=open('/tmp/claude-0/-home-user/fabab33e-729e-58f9-992e-e0c09a689812/scratchpad/ff.log','w'))
def dur(f): return float(sp.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f]))
os.makedirs(f'{I}/rl',exist_ok=True)
for k,cenas in C.items():
    segs=[];t=0;sfx=[]
    for i,c in enumerate(cenas):
        a=f'{I}/rl/{k}-{i}.mp3'
        if not os.path.exists(a): run(['python3',f'{I}/../tts.py',c['fala'],a])
        d=dur(a)+0.35; sfx.append((t,c['sfx'])); 
        shake="+if(lt(t,0.35),18*sin(t*90),0)" if i==0 else ""
        vf=(f"scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,"
            f"scale=w='trunc(1080*(1+0.08*t/{d:.2f})/2)*2':h=-2:eval=frame,crop=1080:1920:'(in_w-1080)/2{shake}':'(in_h-1920)/2',"
            f"eq=saturation=0.8:contrast=1.08:brightness='if(lt(t,0.12),0.28,0)':eval=frame,gblur=sigma=18:enable='lt(t,0.18)',"
            f"vignette=PI/4,noise=alls=10:allf=t,fps=30")
        s=f'{I}/rl/{k}-{i}.mp4'
        run(['ffmpeg','-y','-stream_loop','-1','-i',f'{I}/banco/{c["clip"]}.mp4','-loop','1','-i',f'{I}/cenas/{k}-{i}.png','-t',f'{d:.2f}',
             '-filter_complex',f'[0:v]{vf}[v];[1:v]fade=in:st=0.1:d=0.25:alpha=1[o];[v][o]overlay=0:0,format=yuv420p','-an','-c:v','libx264','-crf','21','-preset','veryfast',s])
        segs.append((s,a,t)); t+=d
    lst=f'{I}/rl/{k}.txt'; open(lst,'w').write(''.join(f"file '{s}'\n" for s,_,_ in segs))
    run(['ffmpeg','-y','-f','concat','-safe','0','-i',lst,'-c','copy',f'{I}/rl/{k}-v.mp4'])
    ins=[];flt=[];n=1
    for s,a,t0 in segs: ins+=['-i',a]; flt.append(f'[{n}:a]adelay={int(t0*1000)}|{int(t0*1000)},volume=1.6[n{n}]'); n+=1
    nv=n;n0=1
    for t0,f in sfx: ins+=['-i',f'{B}/sfx/{f}.mp3']; flt.append(f'[{n}:a]adelay={int(max(t0-0.05,0)*1000)}|{int(max(t0-0.05,0)*1000)},volume=0.55[n{n}]'); n+=1
    ins+=['-i',f'{B}/trilha/{TR[k]}.mp3']; flt.append(f'[{n}:a]atrim=0:{t:.2f},volume=0.13,afade=t=out:st={t-1.2:.2f}:d=1.2[tr]')
    voz='[voz]'; flt.append(''.join(f'[n{j}]' for j in range(1,nv))+f'amix=inputs={nv-1}:normalize=0[voz0];[voz0]asplit[voz][sc]')
    flt.append('[tr][sc]sidechaincompress=threshold=0.03:ratio=8:attack=20:release=300[duck]')
    flt.append(''.join(f'[n{j}]' for j in range(nv,n))+f'[voz][duck]amix=inputs={n-nv+2}:normalize=0,alimiter=limit=0.95[a]')
    run(['ffmpeg','-y','-i',f'{I}/rl/{k}-v.mp4',*ins,'-filter_complex',';'.join(flt),'-map','0:v','-map','[a]','-c:v','copy','-c:a','aac','-b:a','160k','-shortest',f'{D}/{k}-reel.mp4'])
    run(['ffmpeg','-y','-ss','0.6','-i',f'{D}/{k}-reel.mp4','-frames:v','1','-q:v','3',f'{D}/{k}-capa.jpg'])
    print(k,round(t,1),'s')
