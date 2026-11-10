# Prancha final WF Celulares · caminho B (conta Leandro, 10/11/2026)
from PIL import Image, ImageDraw
import os
d=os.path.dirname(os.path.abspath(__file__));P=lambda n:Image.open(f'{d}/pecas-final/{n}.jpg').convert('RGB')
W=3000;im=Image.new('RGB',(W,8000),'#000')
def put(n,x,y,w):
    t=P(n);t=t.resize((w,round(t.height*w/t.width)));im.paste(t,(x,y));return t.height
lg=Image.open(f'{d}/logo-b/wf-logo-b-cor.png');lg.thumbnail((900,1080));im.paste(lg,((W-lg.width)//2,60),lg)
y=1200;w=(W-40)//3
for i,n in enumerate(['10-post-produto','11-post-assistencia','12-post-prova']):hh=put(n,i*(w+20),y,w)
y+=hh+20;dw=(W-120)//7
for i,n in enumerate(['03-avatar']+sorted(f[:-4] for f in os.listdir(f'{d}/pecas-final') if 'destaque' in f)):
    t=P(n).resize((dw,dw));m=Image.new('L',(dw,dw),0);ImageDraw.Draw(m).ellipse((0,0,dw,dw),255);im.paste(t,(i*(dw+20),y),m)
y+=dw+20;w2=(W-20)//2;h=put('13-fachada',0,y,w2);put('14-cartao-etiqueta',w2+20,y,w2)
a=P('03-avatar').resize((110,110));m=Image.new('L',(110,110),0);ImageDraw.Draw(m).ellipse((0,0,110,110),255);im.paste(a,(W-150,60),m)
im.crop((0,0,W,y+h)).save(f'{d}/prancha-final.jpg',quality=88)
