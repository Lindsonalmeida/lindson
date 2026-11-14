import sys; sys.path.insert(0,'.')
from batismo import *
sfx()
OUT='/home/user/lindson/agencia/batismo'; os.makedirs(OUT,exist_ok=True)
# ---------- PEDRÃO ----------
a=photo('p_foto','IMG_9165.JPG.jpeg',3.6)
b=clip('p_pastor','IMG_9162.MOV',2.6,30.8)
c=clip('p_perguntas','IMG_9168.MOV',0,11.1)
d1=clip('p_mergulho1','IMG_9169.MOV',0,1.4)
d2=clip('p_mergulho2','IMG_9169.MOV',1.4,4.7,speed=0.5,flash_at=5.4)
d3=clip('p_mergulho3','IMG_9169.MOV',4.7,7.2)
e=clip('p_festa','IMG_9173.MOV',1.0,20.9)
segs=[a,b,c,d1,d2,d3,e]
st=[0];[st.append(st[-1]+dur(s)) for s in segs]
B,C,D1,D2,E=st[1],st[2],st[3],st[4],st[6]
flash=D2+5.4
caps=[(B+7.6-2.6,B+8.6-2.6,'Que alegria!'),(B+10.2-2.6,B+11.9-2.6,'Quebrando um pouquinho o protocolo...'),
 (B+11.9-2.6,B+14.1-2.6,'O Pedrão, a gente se conhece há um bom tempo'),(B+14.1-2.6,B+15.8-2.6,'do Velho Testamento'),
 (B+16.8-2.6,B+18.0-2.6,'E é tão bom ver'),(B+19.7-2.6,B+23.2-2.6,'como Deus tem alcançado famílias, vidas,'),
 (B+24.4-2.6,B+25.5-2.6,'transformado pessoas'),(B+25.5-2.6,B+27.6-2.6,'É tão bom ver histórias de perto'),
 (B+27.6-2.6,B+30.6-2.6,'de amigos que se conheceram antes de Cristo'),
 (C+0.6,C+4.4,'Você reconhece que a Bíblia é a Palavra de Deus?'),(C+5.2,C+6.6,'Você quer se batizar?'),
 (C+7.3,C+9.2,'Meu irmão, conforme a tua confissão de fé,'),(C+9.2,C+11.1,'nós te batizamos em nome do Pai, do Filho...'),
 (D1,D1+1.4,'...e do Espírito Santo.'),
 (E+3.0,E+8.2,'Glória a Deus! Obrigado, Jesus!'),(E+10.1,E+13.7,'Aleluia!'),(E+16.2,E+18.7,'Glória a Deus!')]
T=st[-1]
titles=[(0.3,3.6,'S','O BATISMO DO',(540,830)),(0.5,3.6,'T','PEDRÃO',(540,960)),
 (flash+0.2,flash+4.2,'T','NOVA\\NCRIATURA',(540,760)),
 (T-5.5,T,'V','"Se alguém está em Cristo, nova criatura é;\\Nas coisas velhas já passaram,\\Neis que tudo se fez novo."',(540,900)),
 (T-5.5,T,'S','2 CORÍNTIOS 5:17',(540,1160))]
env=[(0,0.55),(B-0.2,0.55),(B+0.6,0.10),(D1-0.5,0.12),(flash-2.5,0.35),(flash,0.95),(E,0.85),(T,0.9)]
build('pedrao',segs,'mus/88.mp3',18,env,caps,titles,flash,f'{OUT}/batismo-pedrao.mp4')
env0=[(0,0),(T,0)]
build('pedrao',segs,'mus/88.mp3',18,env0,caps,titles,flash,f'{OUT}/batismo-pedrao-SEM-MUSICA.mp4')
# ---------- ESPOSA ----------
a=photo('e_foto','IMG_9172.JPG.jpeg',3.6)
b=clip('e_pastor','IMG_9162.MOV',25.3,30.9)
c=clip('e_confissao','IMG_9170.MOV',0,22.4)
d=clip('e_mergulho','IMG_9170.MOV',22.4,25.8,speed=0.5,flash_at=5.6)
e=clip('e_festa','IMG_9173.MOV',1.0,20.9)
segs=[a,b,c,d,e]
st=[0];[st.append(st[-1]+dur(s)) for s in segs]
B,C,Dm,E=st[1],st[2],st[3],st[4]
flash=Dm+5.6
caps=[(B+0.2,B+2.3,'É tão bom ver histórias de perto'),(B+2.3,B+5.3,'de amigos que se conheceram antes de Cristo'),
 (C+0.2,C+5.2,'Você reconhece que Jesus Cristo foi à cruz do Calvário e ressuscitou ao terceiro dia?'),
 (C+7.2,C+10.1,'Você reconhece Jesus como seu único Senhor e Salvador?'),(C+11.6,C+14.0,'Você reconhece que a Bíblia é a Palavra de Deus?'),
 (C+14.9,C+16.6,'Você deseja se batizar?'),(C+16.6,C+18.6,'Conforme a tua profissão de fé,'),
 (C+18.6,C+22.4,'nós te batizamos em nome do Pai, do Filho e do Espírito Santo.'),
 (E+3.0,E+8.2,'Glória a Deus! Obrigado, Jesus!'),(E+10.1,E+13.7,'Aleluia!'),(E+16.2,E+18.7,'Glória a Deus!')]
T=st[-1]
titles=[(0.3,3.6,'S','UMA NOVA HISTÓRIA',(540,830)),(0.5,3.6,'T','ELA DISSE\\NSIM',(540,1000)),
 (flash+0.2,flash+4.2,'T','NOVA\\NCRIATURA',(540,760)),
 (T-5.5,T,'V','"Se alguém está em Cristo, nova criatura é;\\Nas coisas velhas já passaram,\\Neis que tudo se fez novo."',(540,900)),
 (T-5.5,T,'S','2 CORÍNTIOS 5:17',(540,1160))]
env=[(0,0.55),(B-0.2,0.5),(B+0.5,0.10),(Dm-0.3,0.15),(flash-2.5,0.35),(flash,0.95),(E,0.85),(T,0.9)]
build('esposa',segs,'mus/655.mp3',60,env,caps,titles,flash,f'{OUT}/batismo-esposa.mp4')
build('esposa',segs,'mus/655.mp3',60,env0,caps,titles,flash,f'{OUT}/batismo-esposa-SEM-MUSICA.mp4')
