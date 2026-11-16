# Previa do grid 3x3 (recorte 4:5 do perfil, como o Instagram mostra) · conta Leandro
import json,os
from PIL import Image
D=os.path.dirname(os.path.abspath(__file__));N=json.load(open(os.path.join(D,'nomes.json')))
W,H=360,450;G=Image.new('RGB',(3*W+8,((len(N)+2)//3)*H+(len(N)//3)*4),'white')
for i,n in enumerate(N):
    im=Image.open(os.path.join(D,n+'.jpg')).crop((0,285,1080,1635)).resize((W,H),Image.LANCZOS)
    G.paste(im,((i%3)*(W+4),(i//3)*(H+4)))
G.save(os.path.join(D,'previa-grid.jpg'),quality=90);print('ok')
