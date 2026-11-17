# Prévia do kit do canal (conta Zuleide, 17/11/2026)
import os
from PIL import Image, ImageDraw
B=os.path.dirname(os.path.abspath(__file__)); P=os.path.join(B,'pecas')
def o(n,w): im=Image.open(os.path.join(P,n)).convert('RGBA'); return im.resize((w,int(im.height*w/im.width)))
c=Image.new('RGB',(2000,2050),(10,10,10))
b=o('banner.jpg',1300); c.paste(b,(40,40)); ImageDraw.Draw(c).rectangle((40+257,40+258,40+1043,40+473),outline=(245,197,24),width=2)
pf=o('perfil.jpg',300); m=Image.new('L',pf.size,0); ImageDraw.Draw(m).ellipse((0,0,300,300),fill=255); c.paste(pf,(1400,60),m)
c.paste(o('marca-dagua.png',150),(1760,130),o('marca-dagua.png',150))
c.paste(o('bumper.jpg',600),(1380,420))
th=['thumb-1-papo-reto','thumb-2-raio-x','thumb-3-bastidores','thumb-4-vendas','thumb-5-ia','thumb-6-negocio-local']
for i,t in enumerate(th): c.paste(o(t+'.jpg',600),(40+(i%2)*640,830+(i//2)*360))
c.paste(o('capa-short.jpg',640),(1320,840))
c.convert('RGB').save(os.path.join(B,'previa.jpg'),quality=85)
