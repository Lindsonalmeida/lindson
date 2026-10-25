import json
def I(h,y,s=100,f='ant',c='',w=None,a=None,box=None,x=None,riscar=None,d=None,tag=False):
    o=dict(h=h,y=y,s=s,f='tag' if tag else f,c=c)
    for k,v in dict(w=w,a=a,box=box,x=x,riscar=riscar,d=d).items():
        if v is not None:o[k]=v
    if w is None and d is None:o['d']=0
    return o
def St(items,w=None,bg=None,apos=None):
    o=dict(t='stack',items=items)
    if w:o['w']=w
    if bg:o['bg']=bg
    return o
def Duo(w,a,b,dir='v',meio=None,meioW=None):
    o=dict(t='duo',w=w,dir=dir,a=a,b=b)
    if meio:o['meio']=meio;o['meioW']=meioW
    return o
def D(k,s,c,w=None,bar=None):
    o=dict(k=k,s=s,c=c)
    if w:o['w']=w
    if bar:o['bar']=bar
    return o
FIM=lambda apos:dict(t='assinatura',apos=apos)
G='#E2BE4A';R='#E0453C';E='#EE8040';P='#EFE6D2'
FOTO='foto:top:640px;bottom:-320px'
S={}
S['08']=[St([I('A regra que quase<br>ninguém conhece',300,110),I('Quem torna outro<br>poderoso',620,130,c='gold',w='quem'),I('trabalha para a<br>própria ruína',900,120,box='red',w='ruína',a='slam')],bg='glow:rgba(142,27,27,.3):45'),
 Duo('Porque',D('Você','dá esperteza e força',G),D('Ele','passa a desconfiar de você',R,w='desconfiar'),meio='DEPOIS',meioW='forte'),
 St([I('Ajudar',420,200,c='gold',w='ajudar'),I('é bom.',650,100,f='cg',w='bom'),I('Entregar a chave<br>da sua casa,',880,110,w='entregar'),I('não.',1120,220,c='red',w='não',a='slam')],w='Ajudar'),FIM('não')]
S['09']=[dict(t='pagina',tag='O PRÍNCIPE · CAP. III',titulo='O problema é<br>uma febre',ty=300,de='No',ate='curar#2',hl=['difícil','impossível'],y=760,s=74),
 St([I('O dinheiro que some aos poucos',420,64,f='cg',c='dim',w='dinheiro'),I('O cliente que esfria',560,64,f='cg',c='dim',w='cliente'),I('A relação que desgasta',700,64,f='cg',c='dim',w='relação')],w='O#2',bg='num:III'),
 St([I('Quem só age quando<br>todo mundo vê',380,110,w='quem'),I('Chega tarde.',760,200,box='red',w='tarde',a='slam')],w='Quem',bg=FOTO.replace('640','900')),FIM('tarde')]
S['10']=[St([I('Todos veem o que<br>você parece',260,120,w='todos'),I('Poucos sentem<br>o que você é',560,120,c='gold',w='poucos')],bg=FOTO),
 Duo('As',D('Olhos','é assim que te julgam',G,w='olhos'),D('Mãos','quase ninguém olha',P,w='mãos'),dir='h'),
 St([I('Bom no que faz',380,110,w='bom'),I('+',540,110,f='cin',c='gold',w='se'),I('cara de amador',680,120,box='red',w='amador',a='slam'),I('= ninguém compra',900,90,f='cg',c='dim',w='primeira')],w='Não#2'),
 St([I('A primeira impressão',460,110,w='primeira'),I('decide se vai existir<br>uma segunda',680,90,f='cg',c='gold',w='decide')],w='primeira',bg='num:1ª'),FIM('segunda')]
S['11']=[St([I('Nada é mais',360,110),I('perigoso',520,230,c='red',w='perigoso',a='slam'),I('do que implantar<br>algo novo',820,100,f='cg',w='implantar')],bg='glow:rgba(142,27,27,.35):40'),
 Duo('Quem',D('Antigo','vira seu inimigo na hora',R,w='antigo'),D('Novo','te defende só um pouco',G,w='novo#2',bar='steps')),
 St([I('Vai mudar algo?',380,120,w='mudar'),I('Espere',620,130,f='cg',c='dim',w='espere'),I('resistência',760,170,c='gold',w='resistência',a='slam'),I('Ela não é sinal<br>de que você errou.',1040,80,f='cg',w='sinal')],w='Se'),FIM('errado')]
S['12']=[St([I('Como se proteger<br>do bajulador',230,110),I('Ouvir a verdade não te ofende.',560,70,f='cg',c='gold',w='verdade')],bg=FOTO),
 St([I('Mas tem um detalhe',300,f='tag',d=0,s=40),I('Todo mundo falando<br>a qualquer hora',480,110,w='todo'),I('= perdem o respeito',780,110,c='red',w='respeito',a='slam')],w='Mas',bg='num:XXIII'),
 St([I("<span class='gold'>01</span> Escolha poucos sábios",380,90,x='l',w='escolha'),I("<span class='gold'>02</span> Pergunte",530,90,x='l',w='pergunte'),I("<span class='gold'>03</span> Ouça",680,90,x='l',w='ouça'),I("<span class='gold'>04</span> Decida sozinho",830,90,x='l',w='decida',a='slam')],w='Então'),FIM('sozinho')]
S['13']=[St([I('A sorte',380,230,c='gold'),I('é um rio que,<br>quando enche,',680,100,f='cg',w='rio'),I('arrasta tudo',940,150,box='red',w='arrasta',a='slam')],bg='glow:rgba(76,141,255,.18):45'),
 Duo('Mas',D('Tempo bom','construa o dique',G,w='construiu',bar='steps'),D('Tempestade','o dique segura',P,w='limita',bar='full')),
 St([I('Reserva',360,150,w='reserva'),I('Preparo',530,150,w='preparo'),I('Contatos',700,150,w='contatos'),I('se faz na calmaria',920,100,f='cg',c='gold',w='calmaria'),I('Na tempestade é tarde.',1080,90,c='red',w='tempestade')],w='Reserva'),FIM('tarde')]
S['14']=[St([I('Profetas armados',360,130,c='gold'),I('venceram',540,110,w='venceram'),I('Desarmados',800,130,c='red',w='desarmados'),I('se arruinaram',980,110,w='arruinaram')],bg='num:VI'),
 St([I('Não é só espada.',260,90,f='cg',c='dim',w='espada'),I('É ter meios de<br>sustentar o que<br>você começou',380,110,c='gold',w='meios')],w='Maquiavel',bg=FOTO),
 St([I('Ideia sem recurso',380,100,w='recurso',riscar='dura'),I('sem estrutura',540,100,w='estrutura'),I('sem gente',700,100,w='gente'),I('não dura',900,170,box='red',w='dura',a='slam')],w='Uma'),
 Duo('Convencer',D('Convencer','é fácil',P,w='convencer'),D('Manter','é que exige força',G,w='manter')),FIM('força')]
S['15']=[St([I('Um favor',420,200),I('apaga uma<br>ofensa antiga?',680,110,f='cg',w='ofensa'),I('Não.',1000,220,c='red',w='engana',a='slam')],bg='glow:rgba(142,27,27,.3):45'),
 St([I('César Bórgia',300,f='tag',d=0,s=40),I('caiu por confiar<br>em quem ele<br>mesmo feriu',460,120,w='confiar')],w='César',bg='num:VII'),
 St([I('Aceita o favor.',420,110,w='aceita'),I('Agradece.',580,110,w='agradece'),I('E lembra.',800,200,c='gold',w='lembra',a='slam')],w='A'),
 St([I('Antes de confiar em<br>quem você machucou,',240,90,f='cg',c='dim',w='antes'),I('pense<br>duas vezes',420,150,c='gold',w='pense')],w='Antes',bg=FOTO),FIM('vezes')]
S['16']=[St([I('Generoso para<br>ser visto?',320,140),I('É uma armadilha.',660,120,box='red',w='armadilha',a='slam')],bg='num:XVI'),
 Duo('Quem',D('Gasta tudo','para parecer generoso',G,w='gasta',bar='full'),D('Cobra mais','de quem está perto',R,w='cobrar'),meio='ÓDIO',meioW='ódio'),
 St([I('Fama de econômico',400,110,w='econômico'),I('má fama, sem ódio',580,90,f='cg',c='dim',w='má'),I('Generosidade de<br>verdade cabe no<br>seu bolso',820,110,c='gold',w='generosidade')],w='Ele'),FIM('bolso')]
S['17']=[St([I('3',240,520,c='gold'),I('tipos de mente',820,120,w='tipos')],bg='glow:rgba(201,162,39,.2):35'),
 St([I("<span class='gold'>1</span> entende sozinha",300,96,x='l',w='primeira'),I('excelente',405,64,f='cg',c='gold',x='l',w='excelente'),I("<span class='gold'>2</span> entende se explicam",540,96,x='l',w='segunda'),I('boa',645,64,f='cg',x='l',w='boa'),I("<span class='gold'>3</span> não entende nada",780,96,x='l',w='terceira'),I('inútil',885,64,f='cg',c='red',x='l',w='inútil')],w='A'),
 St([I('Boa notícia:',380,f='tag',d=0,s=40),I('Não precisa<br>ser o 1º',560,150,w='precisa'),I('Basta não<br>ser o 3º',900,150,box='gold',w='basta',a='slam')],w='A#4'),FIM('terceiro')]
S['18']=[St([I('Bruto',220,230,c='gold'),I('passou anos se<br>fingindo de tolo',520,100,f='cg',w='fingindo')],bg=FOTO.replace('640','800')),
 St([I('Ninguém desconfiava',380,110,w='ninguém'),I('Derrubou o rei',620,130,c='gold',w='derrubou'),I('Fundou a república',800,110,w='fundou',a='slam')],w='Ninguém',bg='num:509 a.C.'),
 St([I('Às vezes é sábio',380,110,w='às'),I('parecer menos',560,170,box='gold',w='parecer',a='slam'),I('Quem é subestimado se<br>move sem ser vigiado.',900,80,f='cg',w='subestimado')],w='Maquiavel'),FIM('vigiado')]
S['19']=[St([I('Obrigado a ceder?',360,130),I('Faça parecer',620,110,w='parecer'),I('escolha',760,220,c='gold',w='escolha',a='slam')],bg='num:I.51'),
 Duo('Quem',D('Cede reclamando','parece fraco e perde o mérito',R,w='reclamando'),D('Cede decidindo','mantém autoridade e gratidão',G,w='decidido')),
 St([I('A situação é a mesma.',420,80,f='cg',c='dim',w='situação'),I('O que muda<br>é a postura.',580,150,c='gold',w='muda',a='slam')],w='A#2',bg=FOTO.replace('640','900')),FIM('postura')]
S['20']=[St([I('O erro:',340,f='tag',d=0,s=40),I('ameaçar',500,190,c='red',w='ameaçar'),I('e pedir',740,190,w='pedir'),I('na mesma frase',980,90,f='cg',c='dim',w='frase')]),
 St([I('“Me dá isso,',420,120,f='cg',w='me'),I('senão…”',600,180,c='red',w='senão',a='slam'),I('= avisa o perigo e dá<br>tempo para se proteger',900,70,f='cg',c='dim',w='avisa')],w='Me',bg='glow:rgba(142,27,27,.35):40'),
 Duo('Se',D('Vai pedir?','peça',G,w='pedir#2'),D('Vai agir?','aja',E,w='agir'),dir='h',meio='NUNCA OS DOIS',meioW='misturar'),FIM('dois#2')]
S['21']=[St([I('Só dá quando<br>é obrigado?',340,140),I('Ninguém agradece.',700,120,box='red',w='agradece',a='slam')],bg=FOTO.replace('640','1000')),
 St([I('Não espere a pressão',380,110,w='espere'),I('Aumento',600,120,c='gold',w='aumento'),I('Bônus',750,120,c='gold',w='bônus'),I('Desculpas',900,120,c='gold',w='desculpas'),I('valem o dobro antes da cobrança',1100,70,f='cg',w='dobro')],w='Maquiavel',bg='num:2×'),FIM('cobrança')]
S['22']=[dict(t='pagina',tag='DISCURSOS · II.26',titulo='Insultar e debochar',ty=300,de='gera',ate='nenhuma',hl=['ódio','nenhuma'],y=740,s=76),
 Duo('O#1',D('Deboche','não enfraquece o outro',R,w='deboche'),D('Ele fica','mais cuidadoso e motivado',P,w='cuidadoso')),
 St([I('O forte de verdade',380,110,w='forte'),I('não humilha.',560,120,f='cg',c='dim',w='humilhar'),I('Vence calado.',800,190,c='gold',w='vence',a='slam')],w='O#3'),FIM('calado')]
S['23']=[St([I('Perderam tudo',360,170,c='red'),I('depois de vencer',620,110,f='cg',w='vencer')],bg='glow:rgba(142,27,27,.35):40'),
 St([I('Por quê?',380,110,w='por'),I('Não souberam',560,150,w='souberam'),I('parar',760,250,c='gold',w='parar',a='slam')],w='Por'),
 Duo('Maquiavel',D('Prudente','se contenta com a vitória',G,w='prudente'),D('Ganancioso','cria um inimigo desesperado',R,w='desesperado')),
 St([I('Ganhou?',420,200,w='ganhou'),I('Garanta o<br>que ganhou.',700,150,box='gold',w='garanta',a='slam')],w='Ganhou',bg=FOTO.replace('640','1100')),FIM('ganhou#3')]
S['24']=[St([I('Ser o primeiro<br>a sugerir',340,130),I('é perigoso',640,170,c='red',w='perigoso',a='slam')],bg='num:III.35'),
 Duo('Se',D('Deu certo','o mérito é de todos',G,w='certo'),D('Deu errado','a culpa é só sua',R,w='errado')),
 St([I("<span class='gold'>01</span> Proponha com calma",400,90,x='l',w='calma'),I("<span class='gold'>02</span> Sem paixão",560,90,x='l',w='paixão'),I("<span class='gold'>03</span> Comprometa os outros",720,90,x='l',w='comprometam')],w='Maquiavel'),FIM('comprometam')]
S['25']=[St([I('Erro fácil demais?',360,130),I('Desconfie.',620,220,c='gold',w='desconfie',a='slam')],bg=FOTO.replace('640','1000')),
 St([I('É isca.',400,240,c='red',w='isca'),I('Exércitos inteiros<br>caíram em emboscadas<br>perseguindo quem “fugia”',780,74,f='cg',w='exércitos')],w='Muitas',bg='num:III.48'),
 St([I('Parece fácil?',400,130,w='parece'),I('Pergunte por quê',620,130,c='gold',w='pergunte'),I('antes de avançar',800,100,f='cg',w='avançar')],w='Se'),FIM('avançar')]
S['26']=[dict(t='pagina',tag='A ARTE DA GUERRA',titulo='Regra de guerra',ty=300,de='sobre',ate='poucos',hl=['muitos','poucos'],y=740,s=78),
 Duo('Ouvir',D('Ouvir muitos','te dá visão',G,w='ouvir'),D('Contar a muitos','entrega seu próximo passo',R,w='contar'),dir='h'),
 St([I('Escute',400,170,w='escute'),I('aberto.',580,110,f='cg',c='dim',w='aberto'),I('Decida',780,170,c='gold',w='decida'),I('fechado.',960,110,f='cg',c='gold',w='fechado',a='slam')],w='Escute'),FIM('fechado')]
S['27']=[Duo('A',D('Disciplina','vale mais',G,w='disciplina'),D('Fúria','vale menos',R,w='fúria')),
 St([I('A natureza cria',340,100,w='natureza'),I('poucos fortes',480,130,c='dim',w='poucos'),I('O treino cria',720,100,w='treino'),I('muitos',860,200,c='gold',w='muitos',a='slam')],w='E',bg='num:VII'),
 St([I('Raiva',360,150,c='red',w='raiva'),I('= energia por um dia',540,80,f='cg',w='energia'),I('Disciplina',780,150,c='gold',w='disciplina#2'),I('= resultado por anos',960,80,f='cg',w='resultado',a='slam')],w='A#2'),FIM('anos')]
S['28']=[St([I('Dinheiro é o<br>nervo da guerra?',340,130),I('Maquiavel discordou.',700,90,f='cg',c='red',w='discordou')],bg='num:R$'),
 Duo('Ele',D('Bons soldados','acham dinheiro',G,w='soldados'),D('Dinheiro','nem sempre acha bons soldados',R,w='nem')),
 St([I('Invista primeiro',420,130,w='invista'),I('em quem faz',600,190,box='gold',w='quem',a='slam')],w='Gente',bg=FOTO.replace('640','1000')),FIM('faz')]
S['29']=[St([I('O mesmo jeito<br>de agir',300,130),I('dá certo numa época',600,80,f='cg',c='gold',w='certo'),I('e afunda em outra',720,80,f='cg',c='red',w='afunda')],bg='num:XXV'),
 Duo('Quem',D('Tempo calmo','o cauteloso brilha',G,w='brilha'),D('Mudança','o cauteloso quebra',R,w='quebra')),
 St([I('Mude com<br>os tempos',360,170,c='gold',w='mudar'),I('O que te trouxe até aqui',760,80,f='cg',w='trouxe'),I('talvez não te leve adiante',880,80,f='cg',c='dim',w='talvez')],w='Ele'),FIM('adiante')]
S['30']=[St([I('Por que tudo',300,120),I('apodrece',460,230,c='red',w='apodrecem'),I('com o tempo?',740,100,f='cg',w='tempo')],bg='glow:rgba(142,27,27,.3):40'),
 St([I('Volte à',300,120,w='voltar'),I('origem',450,240,c='gold',w='origens',a='slam')],w='Maquiavel',bg='num:III.1'),
 St([I("<span class='gold'>?</span> Por que começou",380,90,x='l',w='começou'),I("<span class='gold'>?</span> Quais eram as regras",540,90,x='l',w='regras'),I("<span class='gold'>?</span> O que te fez crescer",700,90,x='l',w='crescer')],w='Lembrar'),
 St([I('Quem se afasta da origem',240,80,f='cg',c='dim',w='quem'),I('não se<br>reconhece<br>mais',380,150,c='gold',w='reconhece')],w='Quem',bg=FOTO),FIM('mais')]
tons=[61.74,65.41,69.3,73.42,77.78,82.41,58.27]
for i,(n,c) in enumerate(S.items()):json.dump({'tom':tons[i%7],'cenas':c},open(f'shorts/{n}/cenas.json','w'),ensure_ascii=False,indent=1)
print(len(S))
