import subprocess,json
F='/home/user/centrallindsonalmeida/painel/admin-rede/reels-cinema-ia/flow/'
# (ini,fim,clip,src,vel,w,h,x,y)  crop em pixels da fonte 720x1280
S=[(0,3.3,'04-A-v2',4.0,0.8, 534,950,186,40),
   (3.3,6.42,'04-A-v2',5.4,0.8, 450,800,200,70),
   (6.42,12.0,'04-B',0.0,0.95, 720,1280,0,0),
   (12.0,17.66,'04-C-v2',0.0,0.85, 720,1280,0,0),
   (17.66,21.0,'04-C-v2',4.8,0.9, 554,985,110,80),
   (21.0,23.26,'04-B',2.6,0.9, 497,883,170,60),
   (23.26,27.84,'04-D',0.0,0.9, 720,1280,0,0),
   (27.84,32.84,'04-D',3.6,0.86, 600,1067,0,110),
   (32.84,36.0,'04-A-v2',4.4,0.85, 534,950,186,40),
   (36.0,39.3,'04-C-v2',4.0,0.8, 497,883,140,90)]
json.dump(S,open('shots.json','w'))
H=0.25 # sobra no fim p/ transição
for i,(a,b,c,src,v,w,h,x,y) in enumerate(S):
    d=(b-a+H)
    sd=min(d*v,7.93-src)
    vf=f"crop={w}:{h}:{x}:{y},setpts=PTS/{v},minterpolate=fps=30:mi_mode=mci:mc_mode=aobmc:me_mode=bidir:vsbmc=1,scale=1080:1920:flags=lanczos,unsharp=5:5:0.4,tpad=stop_mode=clone:stop_duration=1"
    subprocess.run(['ffmpeg','-v','error','-y','-ss',str(src),'-t',str(sd),'-i',F+c+'.mp4','-an','-vf',vf,'-t',str(d),'-c:v','libx264','-crf','14','-preset','fast',f's{i}.mp4'],check=True)
    print(i,'ok',sd/v,d)
