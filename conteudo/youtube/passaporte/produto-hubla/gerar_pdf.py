# Passaporte da Bíblia · v1 (Evangelhos e Atos) · conta Zuleide 16/11/2026
# uso: python3 gerar_pdf.py  -> passaporte-da-biblia-v1.pdf
import os, sys
from PIL import Image, ImageOps, ImageEnhance
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import ImageReader
AQ=os.path.dirname(os.path.abspath(__file__)); DORE=os.path.join(AQ,'..','dore')
TMP=sys.argv[1] if len(sys.argv)>1 else '/tmp'
F='/mnt/skills/examples/canvas-design/canvas-fonts/'
for n,f in [('T','Gloock-Regular.ttf'),('R','CrimsonPro-Regular.ttf'),('B','CrimsonPro-Bold.ttf'),('I','CrimsonPro-Italic.ttf'),('M','DMMono-Regular.ttf')]:
    pdfmetrics.registerFont(TTFont(n,F+f))
PET=HexColor('#0E2A30'); PET2=HexColor('#16404A'); AMB=HexColor('#E3A33C'); CRE=HexColor('#F4E8D0'); TIN=HexColor('#2A2118'); CIA=HexColor('#5FC7C9')
W,H=A4; M=48
def tint(n):
    out=os.path.join(TMP,f'pv_{n}.jpg')
    if not os.path.exists(out):
        im=ImageOps.grayscale(Image.open(os.path.join(DORE,f'{n}.jpg')))
        im=ImageEnhance.Contrast(im).enhance(1.15)
        im=ImageOps.colorize(im,black='#081B20',white='#F2C27A',mid='#7A6440')
        im.thumbnail((900,1200)); im.save(out,quality=78)
    return out
c=canvas.Canvas(os.path.join(AQ,'passaporte-da-biblia-v1.pdf'),pagesize=A4)
c.setTitle('Passaporte da Bíblia · v1'); c.setAuthor('Passaporte da Bíblia')
pg=[0]
def wrap(t,font,size,width):
    ls=[];
    for par in t.split('\n'):
        l=''
        for w in par.split():
            x=(l+' '+w).strip()
            if pdfmetrics.stringWidth(x,font,size)<=width: l=x
            else: ls.append(l); l=w
        ls.append(l)
    return ls
def txt(t,x,y,font='R',size=12,color=TIN,width=W-2*M,lead=1.35):
    c.setFont(font,size); c.setFillColor(color)
    for l in wrap(t,font,size,width): c.drawString(x,y,l); y-=size*lead
    return y
def fundo(cor=CRE):
    c.setFillColor(cor); c.rect(0,0,W,H,fill=1,stroke=0)
def rodape(escuro=False):
    pg[0]+=1; c.setFont('M',8); c.setFillColor(AMB if escuro else PET2)
    c.drawString(M,24,'PASSAPORTE DA BÍBLIA'); c.drawRightString(W-M,24,f'{pg[0]:02d}')
def cab(rotulo,titulo,sub=None):
    fundo(); c.setFillColor(PET); c.rect(0,H-130,W,130,fill=1,stroke=0)
    c.setFont('M',9); c.setFillColor(AMB); c.drawString(M,H-50,rotulo.upper())
    c.setFont('T',30); c.setFillColor(CRE); c.drawString(M,H-88,titulo)
    if sub: c.setFont('I',13); c.setFillColor(CIA); c.drawString(M,H-112,sub)
    return H-170
def img(n,x,y,w,h):
    im=Image.open(tint(n)); iw,ih=im.size; r=max(w/iw,h/ih)
    c.saveState(); p=c.beginPath(); p.rect(x,y,w,h); c.clipPath(p,stroke=0,fill=0)
    c.drawImage(ImageReader(tint(n)),x+(w-iw*r)/2,y+(h-ih*r)/2,iw*r,ih*r); c.restoreState()
# 1 capa
img('057',0,0,W,H); c.setFillColor(PET); c.setFillAlpha(0.55); c.rect(0,0,W,H*0.48,fill=1,stroke=0); c.setFillAlpha(1)
c.setFont('M',10); c.setFillColor(AMB); c.drawString(M,H-60,'PASSAPORTE DA BÍBLIA · VOLUME 1')
c.setFont('T',54); c.setFillColor(CRE); c.drawString(M,330,'Passaporte'); c.drawString(M,272,'da Bíblia')
c.setFont('T',24); c.setFillColor(AMB); c.drawString(M,226,'Evangelhos e Atos')
txt('Cada livro vira uma viagem que você entende. Uma página por destino, sem pressa e sem culpa.',M,190,'I',15,CRE,W-2*M-60)
c.setFont('M',8); c.setFillColor(CRE); c.drawString(M,40,'Gravura: Gustave Doré (domínio público) · Natividade'); pg[0]+=1; c.showPage()
# 2 bem-vindo
y=cab('Antes de embarcar','Bem-vindo a bordo','Como usar este passaporte em 3 passos')
for i,(t,d) in enumerate([('Escolha uma rota','Na página 7 há três caminhos. Se nunca leu, comece pela Rota Primeira Viagem: ela começa em Marcos, o Evangelho mais curto.'),('Leia com o guia aberto','Antes de abrir o livro na sua Bíblia, leia o Guia de Destino dele: em 1 frase, quem você vai encontrar, as paradas e a parte difícil.'),('Carimbe e anote','Terminou? Marque a data no canto do carimbo, escreva o que Deus te mostrou e pinte o selo na página 14.')]):
    c.setFillColor(AMB); c.circle(M+20,y-14,20,fill=1,stroke=0); c.setFont('T',22); c.setFillColor(PET); c.drawCentredString(M+20,y-22,str(i+1))
    c.setFont('T',18); c.setFillColor(PET); c.drawString(M+56,y-12,t); y=txt(d,M+56,y-34,'R',13,TIN,W-2*M-60)-26
c.setFillColor(PET); c.roundRect(M,90,W-2*M,y-110,10,fill=1,stroke=0)
txt('Este é o Volume 1: os 5 livros que abrem o Novo Testamento (Mateus, Marcos, Lucas, João e Atos). Os outros 61 guias chegam nos próximos volumes, no mesmo formato.',M+20,y-50,'I',14,CRE,W-2*M-40)
rodape(); c.showPage()
# 3 identidade
y=cab('Documento do viajante','Minha identidade de viajante')
for campo in ['Nome do viajante','Data de partida','Rota escolhida','Meu motivo para viajar','Quem vai viajar comigo (família, célula, amigo)']:
    c.setFont('M',9); c.setFillColor(PET2); c.drawString(M,y,campo.upper()); c.setStrokeColor(PET2); c.setLineWidth(0.6)
    for k in range(2 if 'motivo' in campo else 1): c.line(M,y-26-k*28,W-M,y-26-k*28)
    y-=70 if 'motivo' in campo else 52
c.setDash(4,4); c.setStrokeColor(AMB); c.setLineWidth(1.5); c.rect(W-M-150,90,150,180); c.setDash()
c.setFont('M',8); c.setFillColor(PET2); c.drawCentredString(W-M-75,175,'FOTO OU DESENHO')
txt('Assinatura do viajante',M,110,'I',12,PET2); c.line(M,100,W-M-180,100); rodape(); c.showPage()
# 4 mapa
y=cab('Mapa-múndi','As 8 regiões da Bíblia','66 livros · 1.189 capítulos (edição evangélica)')
reg=[('Lei','Gênesis a Deuteronômio',5,187,'#D9573B'),('Históricos','Josué a Ester',12,249,'#E9A23B'),('Poéticos','Jó a Cantares',5,243,'#E2668E'),('Profetas Maiores','Isaías a Daniel',5,183,'#3F9A55'),('Profetas Menores','Oseias a Malaquias',12,67,'#9CC152'),('Evangelhos e Atos','Mateus a Atos',5,117,'#3B8EDB'),('Cartas','Romanos a Judas',21,121,'#8466C4'),('Apocalipse','o último destino',1,22,'#8E2C48')]
bw=(W-2*M-16)/2; bh=118
for i,(n,a,l,ch,cor) in enumerate(reg):
    x=M+(i%2)*(bw+16); yy=y-(i//2+1)*(bh+12)
    c.setFillColor(PET if i!=5 else PET2); c.roundRect(x,yy,bw,bh,10,fill=1,stroke=0)
    c.setFillColor(HexColor(cor)); c.rect(x,yy+bh-8,bw,8,fill=1,stroke=0)
    c.setFont('T',19); c.setFillColor(CRE); c.drawString(x+16,yy+bh-40,n)
    c.setFont('I',12); c.setFillColor(CIA); c.drawString(x+16,yy+bh-60,a)
    c.setFont('M',10); c.setFillColor(AMB); c.drawString(x+16,yy+18,f'{l} LIVRO{"S" if l>1 else ""} · {ch} CAPÍTULOS')
    if i==5: c.setFont('M',8); c.setFillColor(AMB); c.drawRightString(x+bw-14,yy+bh-36,'VOLUME 1 >')
txt('Antigo Testamento: 39 livros, 929 capítulos. Novo Testamento: 27 livros, 260 capítulos. A edição católica tem 73 livros e chega em volume próprio.',M,80,'I',11,PET2)
rodape(); c.showPage()
# 5 grande historia
y=cab('A grande história','A Bíblia em 6 capítulos','O fio que liga os 66 livros')
gh=[('1 · Criação','Deus faz tudo e vê que é bom.','Gn 1–2','001'),('2 · Queda','O ser humano escolhe o próprio caminho e a ruptura entra no mundo.','Gn 3','002'),('3 · Promessa e povo','Deus chama Abraão e forma um povo para abençoar todas as nações.','Gn 12; Êx 19','007'),('4 · Jesus','A promessa ganha rosto: Jesus vive, morre e ressuscita.','Evangelhos','088'),('5 · Igreja','O Espírito vem e a mensagem sai de Jerusalém para o mundo.','Atos','093'),('6 · Tudo novo','Deus restaura a criação. Sem lágrima, sem morte.','Ap 21–22','041')]
for i,(t,d,r,n) in enumerate(gh):
    yy=y-(i+1)*104+10; img(n,M,yy,110,90)
    c.setFont('T',17); c.setFillColor(PET); c.drawString(M+126,yy+66,t)
    txt(d,M+126,yy+44,'R',12.5,TIN,W-2*M-140); c.setFont('M',9); c.setFillColor(AMB); c.drawString(M+126,yy+6,r)
rodape(); c.showPage()
# 6 terrenos
y=cab('Leitura','Os 7 tipos de terreno','Cada parte da Bíblia se lê de um jeito')
ter=[('Lei','Regras de um povo antigo. Pergunte: que princípio de Deus está por trás disso?'),('História','Fatos contados com começo, meio e fim. Nem tudo que aparece é aprovado por Deus: observe as consequências.'),('Poesia','Sentimento em verso. Leia devagar, em voz alta, e deixe as imagens falarem.'),('Profecia','Recado de Deus para um momento. Descubra primeiro para quem foi escrito.'),('Evangelho','A vida de Jesus contada por testemunhas. Observe o que Ele faz e com quem anda.'),('Carta','Conselho para uma igreja real com problemas reais. Procure o problema e a resposta.'),('Apocalíptico','Visões cheias de símbolos. Não decifre cada detalhe: segure a mensagem central, Deus vence.')]
for t,d in ter:
    c.setFillColor(AMB); c.rect(M,y-30,4,38,fill=1,stroke=0); c.setFont('T',16); c.setFillColor(PET); c.drawString(M+16,y-6,t)
    y=txt(d,M+16,y-24,'R',12.5,TIN,W-2*M-20)-16
rodape(); c.showPage()
# 7 rotas
y=cab('Por onde começar','Escolha sua rota')
rot=[('Rota Primeira Viagem','Para quem nunca leu ou travou.',['Marcos','João','Atos','Lucas','Mateus'],AMB),('Rota Clássica','Do começo ao fim, na ordem da sua Bíblia.',['Gênesis','Êxodo','...','Judas','Apocalipse'],CIA),('Rota da História','Na ordem aproximada dos acontecimentos.',['Gênesis','Jó','Êxodo','...','Apocalipse'],HexColor('#D9573B'))]
for nome,d,est,cor in rot:
    c.setFont('T',19); c.setFillColor(PET); c.drawString(M,y,nome); c.setFont('I',12.5); c.setFillColor(PET2); c.drawString(M,y-18,d)
    yl=y-62; c.setStrokeColor(cor); c.setLineWidth(6); c.line(M+10,yl,W-M-10,yl)
    for k,e in enumerate(est):
        x=M+10+k*(W-2*M-20)/(len(est)-1); c.setFillColor(CRE); c.setStrokeColor(PET); c.setLineWidth(2.5); c.circle(x,yl,9,fill=1,stroke=1)
        c.setFont('M',9); c.setFillColor(PET); c.drawCentredString(x,yl-26,e.upper())
    y-=150
txt('Dica: a Rota Primeira Viagem começa por Marcos porque é o Evangelho mais curto (16 capítulos) e o mais direto. Em uma semana, com 2 ou 3 capítulos por dia, você termina o primeiro destino.',M,y+10,'I',13,PET2)
rodape(); c.showPage()
# 8 regras
fundo(PET); img('053',0,H*0.52,W,H*0.48)
c.setFont('M',9); c.setFillColor(AMB); c.drawString(M,H*0.52-40,'REGRAS DO VIAJANTE SEM CULPA')
yy=H*0.52-80
for r in ['O passaporte não vence. Não tem data para acabar.','Atrasou? Volte de onde parou, nunca do dia 1.','Um capítulo também é viagem.','Não entendeu um trecho? Anote a dúvida e siga. Ela vira assunto para a próxima conversa.','Ler junto vale o dobro: família, célula ou um amigo.']:
    c.setFillColor(AMB); c.circle(M+5,yy+5,4,fill=1,stroke=0); yy=txt(r,M+20,yy,'T',16,CRE,W-2*M-24)-12
rodape(True); c.showPage()
# guias
G=[dict(n=40,nome='Mateus',cap=28,autor='Mateus, o cobrador de impostos',ep='aprox. décadas de 60 a 80 d.C. (varia entre estudiosos)',img='063',frase='Jesus é o Rei prometido, e o Reino dele já começou.',quem=['Jesus','José e Maria','Os magos','Pedro'],par=[('O nascimento do Rei','Mt 1–2'),('O Sermão do Monte','Mt 5–7'),('Pedro anda sobre as águas','Mt 14:22-33'),('As parábolas do Reino','Mt 13'),('A cruz e o túmulo vazio','Mt 27–28'),('A Grande Comissão','Mt 28:18-20')],liga='Capítulo 4 · Jesus: a promessa feita a Abraão e Davi se cumpre.',vers='Mt 6:33',verst='Busque primeiro o Reino de Deus, e o resto virá junto.',dica='O capítulo 1 começa com uma genealogia. Não trave: leia os nomes como a prova de que Jesus vem da família da promessa e siga para o versículo 18.'),
dict(n=41,nome='Marcos',cap=16,autor='Marcos, companheiro de Pedro (tradição)',ep='aprox. década de 60 d.C. (varia entre estudiosos)',img='064',frase='Jesus age rápido: cura, ensina, enfrenta e entrega a vida.',quem=['Jesus','Pedro','Os doze','A multidão'],par=[('O batismo no Jordão','Mc 1:9-11'),('Jesus acalma a tempestade','Mc 4:35-41'),('A filha de Jairo','Mc 5:21-43'),('"Quem vocês dizem que eu sou?"','Mc 8:27-30'),('A última ceia','Mc 14:12-26'),('O túmulo vazio','Mc 16:1-8')],liga='Capítulo 4 · Jesus: o servo que dá a vida.',vers='Mc 10:45',verst='O Filho do Homem veio para servir e dar a vida por muitos.',dica='Marcos usa muito a palavra "logo". O ritmo é de ação: leia de 2 a 3 capítulos de uma vez para sentir a pressa da história.'),
dict(n=42,nome='Lucas',cap=24,autor='Lucas, o médico (tradição)',ep='aprox. décadas de 60 a 80 d.C. (varia entre estudiosos)',img='073',frase='Jesus veio buscar quem estava de fora: pobre, doente, mulher, estrangeiro.',quem=['Jesus','Maria','Zaqueu','O filho pródigo'],par=[('O anúncio a Maria','Lc 1:26-38'),('O nascimento em Belém','Lc 2:1-20'),('O bom samaritano','Lc 10:25-37'),('A ovelha, a moeda e o filho perdidos','Lc 15'),('Zaqueu na árvore','Lc 19:1-10'),('O caminho de Emaús','Lc 24:13-35')],liga='Capítulo 4 · Jesus: a boa notícia é para todos os povos.',vers='Lc 19:10',verst='O Filho do Homem veio buscar e salvar o que estava perdido.',dica='Os capítulos 9 a 19 são uma longa viagem até Jerusalém. Leia como diário de estrada: cada parada traz uma lição.'),
dict(n=43,nome='João',cap=21,autor='João, o discípulo amado (tradição)',ep='aprox. décadas de 90 d.C. (varia entre estudiosos)',img='080',frase='Jesus é Deus que se fez gente para que você creia e tenha vida.',quem=['Jesus','Nicodemos','A samaritana','Lázaro'],par=[('No princípio era a Palavra','Jo 1:1-18'),('Água em vinho em Caná','Jo 2:1-11'),('A conversa no poço','Jo 4:1-42'),('Lázaro sai do túmulo','Jo 11'),('Jesus lava os pés','Jo 13'),('Tomé toca as feridas','Jo 20:24-29')],liga='Capítulo 4 · Jesus: a Palavra que criou tudo agora mora entre nós.',vers='Jo 3:16',verst='Deus amou tanto o mundo que deu o seu Filho, para que quem crê tenha vida eterna.',dica='Os capítulos 14 a 17 são uma conversa longa e profunda. Leia meio capítulo por dia e anote uma frase que tocar você.'),
dict(n=44,nome='Atos',cap=28,autor='Lucas, continuação do Evangelho',ep='aprox. décadas de 60 a 80 d.C. (varia entre estudiosos)',img='095',frase='O Espírito chega e a mensagem de Jesus sai de Jerusalém para o mundo.',quem=['Pedro','Estêvão','Paulo','Barnabé'],par=[('A ascensão','At 1:6-11'),('Pentecostes','At 2'),('Estêvão, o primeiro mártir','At 7'),('Saulo no caminho de Damasco','At 9:1-19'),('Pedro solto pelo anjo','At 12:1-17'),('O naufrágio a caminho de Roma','At 27')],liga='Capítulo 5 · Igreja: o povo de Deus se abre para todas as nações.',vers='At 1:8',verst='Vocês vão receber poder do Espírito Santo e serão minhas testemunhas até os confins da terra.',dica='A partir do capítulo 13 começam as viagens de Paulo. Acompanhe com um mapa: cada cidade depois ganha uma carta.')]
for g in G:
    fundo(); img(g['img'],W-M-200,H-330,200,250)
    c.setFillColor(HexColor('#3B8EDB')); c.rect(0,H-64,W,64,fill=1,stroke=0); c.setFillColor(PET); c.rect(0,H-70,W,6,fill=1,stroke=0)
    c.setFont('M',9); c.setFillColor(CRE); c.drawString(M,H-30,f"DESTINO Nº {g['n']}/66 · EVANGELHOS E ATOS · {g['cap']} CAPÍTULOS"); c.drawString(M,H-48,('AUTOR (TRADIÇÃO): '+g['autor']).upper()[:80])
    c.setFont('T',46); c.setFillColor(PET); c.drawString(M,H-130,g['nome'])
    c.setFont('M',8); c.setFillColor(PET2); c.drawString(M,H-150,'ÉPOCA: '+g['ep'].upper())
    c.setFillColor(PET); c.roundRect(M,H-260,W-2*M-216,92,12,fill=1,stroke=0); c.setFont('M',8); c.setFillColor(AMB); c.drawString(M+14,H-186,'EM 1 FRASE')
    txt(g['frase'],M+14,H-206,'T',14,CRE,W-2*M-246)
    c.setFont('M',8); c.setFillColor(PET2); c.drawString(M,H-288,'QUEM VOCÊ VAI ENCONTRAR'); x=M
    for q in g['quem']:
        wq=pdfmetrics.stringWidth(q,'B',11)+20; c.setFillColor(AMB); c.roundRect(x,H-314,wq,20,10,fill=1,stroke=0); c.setFont('B',11); c.setFillColor(PET); c.drawString(x+10,H-308,q); x+=wq+8
    c.setFont('M',8); c.setFillColor(PET2); c.drawString(M,H-350,'O ROTEIRO'); y=H-376
    c.setDash(2,3); c.setStrokeColor(PET2); c.setLineWidth(1.2); c.line(M+7,y,M+7,y-5*30); c.setDash()
    for t,r in g['par']:
        c.setFillColor(AMB); c.setStrokeColor(PET); c.circle(M+7,y+4,6,fill=1,stroke=1); c.setFont('B',13); c.setFillColor(TIN); c.drawString(M+24,y,t)
        c.setFont('M',9); c.setFillColor(PET2); c.drawRightString(W-M,y,r); y-=30
    y-=6; c.setFont('M',8); c.setFillColor(PET2); c.drawString(M,y,'LIGA COM A GRANDE HISTÓRIA'); y=txt('> '+g['liga'],M,y-18,'I',12.5,TIN)-10
    c.setFillColor(HexColor('#EAD8B4')); c.roundRect(M,y-62,W-2*M,64,10,fill=1,stroke=0); c.setFont('M',8); c.setFillColor(PET2); c.drawString(M+14,y-16,'VERSÍCULO DE BOLSO · '+g['vers']+' (paráfrase; leia na sua Bíblia)')
    txt(g['verst'],M+14,y-36,'T',13,PET,W-2*M-28); y-=84
    c.setFont('M',8); c.setFillColor(PET2); c.drawString(M,y,'DICA DE TRAVESSIA'); txt(g['dica'],M,y-18,'R',12,TIN,W-2*M-170)
    cx=W-M-62; c.setDash(3,3); c.setStrokeColor(AMB); c.setLineWidth(2); c.circle(cx,112,56,stroke=1,fill=0); c.setDash()
    c.setFont('M',8); c.setFillColor(PET2); c.drawCentredString(cx,118,'LI EM'); c.drawCentredString(cx,100,'___/___/___')
    c.drawString(M,78,'O QUE DEUS ME MOSTROU'); c.setStrokeColor(PET2); c.setLineWidth(0.5); c.line(M,60,cx-70,60); c.line(M,42,cx-70,42)
    rodape(); c.showPage()
# selos
y=cab('Progresso','Página de selos','Pinte um selo a cada livro terminado')
liv='Gn Êx Lv Nm Dt Js Jz Rt 1Sm 2Sm 1Rs 2Rs 1Cr 2Cr Ed Ne Et Jó Sl Pv Ec Ct Is Jr Lm Ez Dn Os Jl Am Ob Jn Mq Na Hc Sf Ag Zc Ml Mt Mc Lc Jo At Rm 1Co 2Co Gl Ef Fp Cl 1Ts 2Ts 1Tm 2Tm Tt Fm Hb Tg 1Pe 2Pe 1Jo 2Jo 3Jo Jd Ap'.split()
cores=[0]*5+[1]*12+[2]*5+[3]*5+[4]*12+[5]*5+[6]*21+[7]
for i,l in enumerate(liv):
    x=M+28+(i%8)*((W-2*M-56)/7); yy=y-24-(i//8)*58
    c.setStrokeColor(HexColor(reg[cores[i]][4])); c.setLineWidth(2.2); c.setDash(2,2); c.circle(x,yy,22,stroke=1,fill=0); c.setDash()
    c.setFont('M',10); c.setFillColor(PET); c.drawCentredString(x,yy-4,l)
rodape(); c.showPage()
# niveis
y=cab('Gamificação','Níveis de viajante')
for i,(n,d) in enumerate([('Turista','Terminou o primeiro livro.'),('Explorador','Terminou os 4 Evangelhos.'),('Peregrino','Terminou o Novo Testamento.'),('Navegador','Terminou o Antigo Testamento.'),('Embaixador da Palavra','Terminou os 66 livros.')]):
    yy=y-i*104; c.setFillColor(PET if i%2==0 else PET2); c.roundRect(M+i*18,yy-80,W-2*M-i*18,84,12,fill=1,stroke=0)
    c.setFont('T',36); c.setFillColor(AMB); c.drawString(M+i*18+18,yy-56,f'{i+1}'); c.setFont('T',20); c.setFillColor(CRE); c.drawString(M+i*18+64,yy-36,n)
    c.setFont('I',13); c.setFillColor(CIA); c.drawString(M+i*18+64,yy-58,d)
rodape(); c.showPage()
# diario
y=cab('Para imprimir quantas vezes quiser','Diário de bordo')
c.setFont('M',9); c.setFillColor(PET2); c.drawString(M,y,'DATA ___/___/___      LIVRO E CAPÍTULOS _______________________'); y-=40
for campo,nl in [('O que li',3),('O que entendi',4),('O que Deus me mostrou',4),('Uma oração',3)]:
    c.setFont('T',16); c.setFillColor(PET); c.drawString(M,y,campo); y-=10; c.setStrokeColor(PET2); c.setLineWidth(0.5)
    for k in range(nl): y-=26; c.line(M,y,W-M,y)
    y-=30
rodape(); c.showPage()
# certificado
fundo(PET); img('093',0,0,W,H); c.setFillColor(PET); c.setFillAlpha(0.72); c.rect(0,0,W,H,fill=1,stroke=0); c.setFillAlpha(1)
c.setStrokeColor(AMB); c.setLineWidth(2); c.rect(30,30,W-60,H-60); c.setLineWidth(0.6); c.rect(38,38,W-76,H-76)
c.setFont('M',10); c.setFillColor(AMB); c.drawCentredString(W/2,H-120,'CERTIFICADO DE VIAGEM')
c.setFont('T',36); c.setFillColor(CRE); c.drawCentredString(W/2,H-180,'Evangelhos e Atos')
c.setFont('I',15); c.setFillColor(CRE); c.drawCentredString(W/2,H-260,'Certificamos que')
c.setStrokeColor(AMB); c.line(110,H-320,W-110,H-320)
c.drawCentredString(W/2,H-360,'percorreu Mateus, Marcos, Lucas, João e Atos,'); c.drawCentredString(W/2,H-382,'117 capítulos da grande história.')
c.line(110,180,260,180); c.line(W-260,180,W-110,180); c.setFont('M',8); c.setFillColor(AMB); c.drawCentredString(185,166,'DATA'); c.drawCentredString(W-185,166,'ASSINATURA')
pg[0]+=1; c.showPage()
# proximo passo
y=cab('Seu próximo passo','A viagem continua')
txt('O Volume 1 te levou pelos 5 primeiros livros do Novo Testamento. Para seguir viagem:',M,y,'R',13.5,TIN)
for t,d in [('Passaporte completo (66 livros)','Os guias de todos os livros, mapa grandão, Kit Travessia e cartela sem data.'),('Canal Passaporte da Bíblia no YouTube','Um vídeo por livro, com as gravuras de Doré, para assistir antes de ler.'),('Ler em grupo','Use o Diário de bordo na sua célula: cada um lê o mesmo destino na semana e conta o que Deus mostrou.')]:
    y-=70; c.setFillColor(PET); c.roundRect(M,y-30,W-2*M,64,10,fill=1,stroke=0); c.setFont('T',16); c.setFillColor(AMB); c.drawString(M+16,y+12,t); txt(d,M+16,y-8,'R',12,CRE,W-2*M-32)
rodape(); c.showPage()
# ficha
y=cab('Ficha técnica','Créditos e direitos')
y=txt('Textos: Passaporte da Bíblia. Versículos de bolso em paráfrase própria: confira sempre o texto na sua tradução preferida. Datas são aproximadas e variam entre estudiosos; autoria indicada segundo a tradição.',M,y,'R',12.5)-14
y=txt('Imagens: gravuras de Gustave Doré (1832-1883) para a Bíblia ilustrada de 1866, em domínio público, com tratamento de cor próprio.',M,y,'R',12.5)-14
y=txt('Revisão teológica: [PREENCHER antes de vender: nome do revisor].',M,y,'B',12.5)-14
y=txt('Uso pessoal e do seu grupo. Pode imprimir quantas vezes quiser. Não é permitido revender ou distribuir o arquivo.',M,y,'R',12.5)
rodape(); c.showPage(); c.save(); print('ok',pg[0])
