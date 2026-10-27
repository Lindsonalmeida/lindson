"""Capas verticais (1080x1920) dos 30 Shorts. python3 shorts-thumbs.py -> shorts-thumbs.html; renderiza em shorts/NN/capa.png"""
s=open('identidade.html').read()
head=s[:s.index('<section')];script=s[s.index('<script>'):]
css='''<style>
.sv{width:1080px;height:1920px;position:relative;overflow:hidden;background:#0B0A08}
.sv .im{position:absolute;background-size:cover;background-position:center 20%;filter:grayscale(1) contrast(1.2) brightness(.85)}
.sv .glow{position:absolute;border-radius:50%;mix-blend-mode:screen}
.sv h1{position:absolute;left:70px;right:70px;font:400 190px/.9 Anton;text-transform:uppercase;color:#EFE6D2;text-shadow:0 8px 40px rgba(0,0,0,.9)}
.sv h1 b{font-weight:400;color:#E2BE4A}.sv h1 em{font-style:normal;background:#8E1B1B;padding:0 .1em;display:inline-block;line-height:1}
.sv .tg{position:absolute;font:700 40px Cinzel;letter-spacing:.2em;color:#0B0A08;background:#C9A227;padding:14px 30px}
.sv .emb{position:absolute;width:130px;height:130px}
.sv .num{position:absolute;font:900 120px Cinzel;color:rgba(201,162,39,.9)}
.sv .sub{position:absolute;left:70px;right:70px;font:italic 600 64px/1.15 'Cormorant Garamond';color:#cdbf9f}
</style>'''
I={'maq':'img/maquiavel.jpg','maq2':'img/maquiavel2.jpg','ces':'img/cesar.jpg','bor':'img/borgia.jpg','lor':'img/lorenzo.jpg','car':'img/hist/caracalla.jpg','mar':'img/hist/marcus_aurelius.jpg','com':'img/hist/commodus.jpg','han':'img/hist/hannibal.jpg','sav':'img/hist/girolamo_savonarola.jpg','ale':'img/hist/alexander_the_great.jpg','pap':'img/hist/pope_alexander_vi.jpg','fer':'img/hist/ferdinand_ii_of_aragon.jpg','arn':'img/hist/arno.jpg','pal':'img/hist/palazzo_vecchio.jpg','jul':'img/hist/pope_julius_ii.jpg'}
EMB='<svg class="emb" style="right:60px;top:80px"><use href="#emb"/></svg>'
def L1(n,img,tag,h,sub=''):  # rosto em cima, texto embaixo
    return f'''<section class="p sv grao" id="s{n}"><div class="glow" style="left:90px;top:120px;width:900px;height:900px;background:radial-gradient(circle,rgba(217,98,43,.5),transparent 65%)"></div>
<div class="im" style="left:0;right:0;top:0;height:1150px;background-image:url({I[img]});-webkit-mask-image:linear-gradient(180deg,#000 55%,transparent)"></div>
<div class="tg" style="left:70px;top:110px">{tag}</div><h1 style="top:930px">{h}</h1>{f'<div class="sub" style="top:1420px">{sub}</div>' if sub else ''}{EMB}</section>'''
def L2(n,img,tag,h,sub=''):  # texto em cima, rosto embaixo
    return f'''<section class="p sv grao" id="s{n}"><div class="glow" style="left:90px;top:900px;width:900px;height:900px;background:radial-gradient(circle,rgba(201,162,39,.45),transparent 65%)"></div>
<div class="im" style="left:0;right:0;bottom:0;height:1100px;background-image:url({I[img]});-webkit-mask-image:linear-gradient(0deg,#000 50%,transparent)"></div>
<div style="position:absolute;inset:0;background:linear-gradient(0deg,rgba(11,10,8,.85),transparent 25%)"></div>
<div class="tg" style="left:70px;top:230px">{tag}</div><h1 style="top:340px">{h}</h1>{EMB}</section>'''
def L3(n,img,tag,big,h,fs=620):  # palavra/número gigante ao fundo
    return f'''<section class="p sv grao" id="s{n}"><div class="im" style="inset:0;background-image:url({I[img]});opacity:.45"></div>
<div style="position:absolute;inset:0;background:radial-gradient(ellipse at 50% 45%,transparent 20%,rgba(11,10,8,.95) 75%)"></div>
<div style="position:absolute;left:0;right:0;top:300px;text-align:center;font:400 {fs}px/1 Anton;color:rgba(201,162,39,.85);text-shadow:0 10px 60px #000">{big}</div>
<div class="tg" style="left:70px;top:150px">{tag}</div><h1 style="top:1060px;text-align:center">{h}</h1>{EMB}</section>'''
def L4(n,img,tag,riscado,h):  # frase riscada + verdade
    return f'''<section class="p sv grao" id="s{n}"><div class="im" style="inset:0;background-image:url({I[img]});opacity:.55"></div>
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(11,10,8,.9) 0%,rgba(11,10,8,.4) 40%,rgba(11,10,8,.95) 75%)"></div>
<div class="tg" style="left:70px;top:200px">{tag}</div>
<div style="position:absolute;left:70px;right:70px;top:340px;font:italic 600 110px/1.05 'Cormorant Garamond';color:#9b8f76">“{riscado}”<i style="position:absolute;left:-2%;top:45%;width:104%;height:22px;background:#E0453C;transform:rotate(-4deg)"></i></div>
<h1 style="top:900px">{h}</h1>{EMB}</section>'''
def L5(n,a,b,ta,tb,tag,h):  # duelo
    return f'''<section class="p sv grao" id="s{n}"><div class="im" style="left:0;width:540px;top:0;height:1920px;background-image:url({I[a]});filter:grayscale(1) brightness(.6)"></div><div class="im" style="right:0;width:540px;top:0;height:1920px;background-image:url({I[b]});filter:sepia(.5) brightness(.75)"></div>
<div style="position:absolute;left:536px;top:0;bottom:0;width:8px;background:#E2BE4A"></div>
<div style="position:absolute;inset:0;background:radial-gradient(ellipse at 50% 50%,rgba(11,10,8,.9) 25%,transparent 60%)"></div>
<div class="tg" style="left:50%;transform:translateX(-50%);top:150px;white-space:nowrap">{tag}</div>
<div style="position:absolute;left:40px;top:330px;font:400 110px Anton;color:#EE8040">{ta}</div><div style="position:absolute;right:40px;top:330px;font:400 110px Anton;color:#E2BE4A;text-align:right">{tb}</div>
<h1 style="top:760px;text-align:center">{h}</h1>{EMB}</section>'''
def L6(n,img,tag,cit,h):  # citação em pergaminho
    return f'''<section class="p sv grao" id="s{n}"><div class="im" style="inset:0;background-image:url({I[img]});opacity:.5"></div><div style="position:absolute;inset:0;background:rgba(11,10,8,.55)"></div>
<div class="tg" style="left:70px;top:170px">{tag}</div>
<div style="position:absolute;left:80px;right:80px;top:320px;background:#EFE6D2;color:#1b140c;padding:60px 64px;transform:rotate(-2deg);box-shadow:0 30px 80px #000;font:italic 600 80px/1.1 'Cormorant Garamond'">“{cit}”</div>
<h1 style="top:1000px">{h}</h1>{EMB}</section>'''
P='O PRÍNCIPE · CAP. ';DI='DISCURSOS · ';AG='A ARTE DA GUERRA'
T=[
L4(1,'maq',P+'18','Os fins justificam os meios','Ele <em>nunca</em><br>disse <b>isso</b>'),
L5(2,'maq2','ces','RAPOSA','LEÃO',P+'18','Seja os <b>dois</b>'),
L1(3,'ces',P+'17','Temido<br>ou <b>amado</b>?'),
L6(4,'car',P+'17','Esquecem a morte do pai antes da perda do patrimônio','A frase mais <em>fria</em>'),
L3(5,'bor',P+'8','1×','O mal de <em>uma vez</em>.<br>O bem aos <b>poucos</b>.'),
L2(6,'lor',P+'22','Te julgam<br>pelo seu<br><b>círculo</b>'),
L1(7,'pap',P+'21','Neutro<br>= <em>perdedor</em>'),
L5(8,'han','com','VOCÊ','ELE',P+'3','Cuidado com<br>quem você<br><b>fortalece</b>'),
L3(9,'mar',P+'3','?','No começo<br><em>ninguém</em> <b>vê</b>'),
L2(10,'maq',P+'18','Todos veem<br>o que você<br><b>parece</b>'),
L1(11,'sav',P+'6','O <b>novo</b><br>tem <em>inimigos</em>'),
L6(12,'lor',P+'23','Os bons conselhos nascem da prudência do príncipe','Quem só<br>concorda te<br><em>derruba</em>'),
L3(13,'arn',P+'25','50%','A sorte<br>é um <b>rio</b>',430),
L1(14,'sav',P+'6','Ideia sem<br>força <em>morre</em>'),
L2(15,'bor',P+'7','Favor <em>não</em><br>apaga a<br><b>ferida</b>'),
L4(16,'ale',P+'16','Seja generoso com todos','Generoso<br>demais =<br><em>arruinado</em>'),
L3(17,'maq2',P+'22','3','Qual mente<br>é a <b>sua</b>?'),
L1(18,'com',DI+'III.2','O mais<br>esperto se<br>faz de <b>bobo</b>'),
L6(19,'fer',DI+'I.51','O que fizer por necessidade, faça parecer escolha','Faça parecer<br><b>escolha</b>'),
L5(20,'car','maq','AMEAÇA','PEDE',DI+'I.44','Nunca os<br><em>dois</em> juntos'),
L2(21,'jul',DI+'I.32','Favor<br>obrigado não<br>tem <em>valor</em>'),
L1(22,'car',DI+'II.26','Deboche<br>só te <em>custa</em>'),
L1(23,'han',DI+'II.27','A vitória<br>que vira<br><em>derrota</em>'),
L4(24,'lor',DI+'III.35','Ideia boa, leva o mérito','Quem propõe<br>leva a <em>culpa</em>'),
L1(25,'ale',DI+'III.48','Fácil<br>demais?<br><em>Desconfie</em>'),
L5(26,'mar','maq2','MUITOS','POUCOS',AG,'Ouça muitos.<br>Decida com<br><b>poucos</b>'),
L2(27,'ces',AG,'Disciplina<br>vence<br><em>fúria</em>'),
L6(28,'pap',DI+'II.10','Bons soldados acham dinheiro','Dinheiro<br>não compra<br><b>vitória</b>'),
L3(29,'jul',DI+'III.9','↻','O que te trouxe<br><em>não</em> te <b>leva</b>',520),
L1(30,'maq',DI+'III.1','Volte à<br><b>origem</b>'),
]
open('shorts-thumbs.html','w').write(head.replace('</style></head>','</style>'+css+'</head>')+''.join(T)+script)
