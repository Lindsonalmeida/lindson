# paleta .ase/.json e quadros da animação do logo (conta Pedro, 16/11/2026)
import json,struct,os,sys
B=os.path.abspath(os.path.dirname(__file__)+'/..'); sys.path.insert(0,B+'/gerador'); os.chdir(B)
cores={'Tinta':'#0B0C0E','Calcário':'#EFEAE1','Pedra':'#8E8A82','Grafite':'#1A1C20','Latão':'#B8955A','Labs':'#2E4BFF','Studio':'#E8461E','Media':'#F0A202','Ventures':'#0E8C66'}
json.dump({'proporcao':'60 Tinta / 25 Calcário / 15 apoio; latão só detalhe','cores':cores},open('paleta/alkantara-paleta.json','w'),ensure_ascii=False,indent=1)
out=b'ASEF'+struct.pack('>HHI',1,0,len(cores))
for n,h in cores.items():
    r,g,b=[int(h[i:i+2],16)/255 for i in (1,3,5)]
    nm=(n+'\0').encode('utf-16-be'); body=struct.pack('>H',len(nm)//2)+nm+b'RGB '+struct.pack('>fff',r,g,b)+struct.pack('>H',2)
    out+=struct.pack('>HI',1,len(body))+body
open('paleta/alkantara-paleta.ase','wb').write(out)
from PIL import Image,ImageDraw
from simbolo import pecas
OUT=sys.argv[1]; W,H=1920,1080; ps=pecas(); off=[(-500,0),(300,-400),(500,0),(300,400)]
wm=Image.open('logos/png/alkantara-wordmark-negativo.png').convert('RGBA'); wm=wm.resize((int(wm.width*130/wm.height),130))
for f in range(72):
    t=f/24; im=Image.new('RGB',(W,H),'#0B0C0E'); d=ImageDraw.Draw(im); s=14; ox,oy=W/2-12*s,300
    k=1-(1-min(1,t/0.9))**4
    for i,p in enumerate(ps):
        dx,dy=off[i]; c=(239,234,225)
        if t>1.3:
            g=max(0,1-abs((t-1.3)*3-i*.3)); c=tuple(int(a*(1-g)+b*g) for a,b in zip((184,149,90),(245,220,170)))
        d.polygon([(ox+x*s+dx*(1-k),oy+y*s+dy*(1-k)) for x,y in p.exterior.coords],fill=c)
    if t>1.9:
        a=min(1,(t-1.9)/0.4); w2=wm.copy(); w2.putalpha(w2.getchannel('A').point(lambda v:int(v*a)))
        im.paste(w2,(int(W/2-w2.width/2),int(690+30*(1-a))),w2)
    im.save(f'{OUT}/{f:03d}.png')
