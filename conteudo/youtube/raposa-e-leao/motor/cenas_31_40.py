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
S['31']=[St([I('Por que tanta gente',300,100),I('perde tudo',460,210,c='red',w='perde',a='slam'),I('de uma hora<br>para outra?',800,100,f='cg',w='hora')],bg='glow:rgba(142,27,27,.35):40'),
 St([I("<span class='gold'>01</span> Caem de você",400,100,x='l',w='caem'),I("<span class='gold'>02</span> Te pesam",580,100,x='l',w='pesam'),I("<span class='gold'>03</span> Te apertam",760,100,x='l',w='apertam',a='slam')],w='Maquiavel',bg='num:XIII'),
 St([I('Dinheiro emprestado',360,80,f='cg',c='dim',w='dinheiro'),I('Cliente único',480,80,f='cg',c='dim',w='cliente'),I('Sócio que faz tudo',600,80,f='cg',c='dim',w='sócio'),I('falha ou cobra caro',820,110,box='red',w='falha')],w='Dinheiro'),
 St([I('Sem armas próprias',380,110,w='armas#2'),I('ninguém está seguro',560,90,f='cg',w='ninguém'),I('Construa<br>o que é seu',800,170,c='gold',w='construa',a='slam')],w='Ele',bg=FOTO),FIM('seu')]
S['32']=[St([I('Todo mundo jura',340,120),I('estar do seu lado',520,100,f='cg',w='lado'),I('Até precisar',760,170,c='red',w='até',a='slam')],bg=FOTO.replace('640','1000')),
 dict(t='pagina',w='Maquiavel',tag='O PRÍNCIPE · CAP. IX',titulo='Quando a morte<br>está longe',ty=300,de='quando',ate='você',hl=['prometem','longe'],y=760,s=74),
 Duo('Quando#2',D('Fase boa','todos prometem',G,w='quando#2'),D('Crise','todos somem',R,w='somem')),
 St([I('Conte apoio',400,130,w='conte'),I('pelo que fizeram',580,110,c='gold',w='fizeram'),I('quando custou',760,110,box='gold',w='custou',a='slam')],w='Não'),FIM('coisa')]
S['33']=[St([I('O erro que',320,110),I('quebra',450,240,c='red',w='quebra',a='slam'),I('acontece quando<br>tudo vai bem',780,90,f='cg',w='bem')],bg='glow:rgba(142,27,27,.3):45'),
 St([I('Na bonança,',380,130,c='gold',w='bonança'),I('conte com a',560,90,f='cg',w='com'),I('tempestade',700,170,c='red',w='tempestade',a='slam')],w='Maquiavel',bg='num:XXIV'),
 Duo('O#2',D('Caixa cheio','cliente compra',G,w='caixa'),D('Ninguém guarda','nada',R,w='ninguém'),dir='h'),
 St([I('A reserva se faz',400,110,w='reserva'),I('no sol',580,230,c='gold',w='sol',a='slam'),I('e não na chuva',880,90,f='cg',c='dim',w='chuva')],w='Quando#2',bg=FOTO),FIM('chuva')]
S['34']=[St([I('Não foi o mercado',340,110),I('que te quebrou',500,150,c='red',w='quebrou',a='slam'),I('caiu · mudou · piorou',760,90,f='cg',c='dim',w='caiu')],bg='glow:rgba(142,27,27,.3):40'),
 St([I('Não acusem',360,130,w='acusem'),I('a sorte',520,130,c='dim',w='fortuna',riscar='fortuna'),I('a própria',720,110,w='própria'),I('inércia',860,220,c='gold',w='inércia',a='slam')],w='Maquiavel',bg='num:XXIV'),
 St([I('Tiveram tempos calmos',420,100,w='tiveram'),I('e não se prepararam',600,110,box='red',w='prepararam')],w='Eles',bg=FOTO.replace('640','900')),
 St([I('O que eu deixei<br>de fazer',400,130,c='gold',w='deixei'),I('quando dava<br>para fazer?',720,110,f='cg',w='dava')],w='Antes'),FIM('fazer#2')]
S['35']=[St([I('O bom líder',340,120),I('quase nunca',500,100,f='cg',w='quase'),I('dá a notícia ruim',680,150,c='red',w='ruim',a='slam')],bg=FOTO),
 Duo('Os',D('O que pesa','deixa com outros',R,w='pesam'),D('O que é favor','faça você',G,w='favor'),dir='h'),
 St([I('Cobrança e corte',380,110,c='dim',w='cobrança'),I('= regra clara',540,90,f='cg',w='regra'),I('Elogio e prêmio',760,110,c='gold',w='elogio'),I('= da sua boca',920,90,f='cg',w='boca',a='slam')],w='A#2',bg='num:XIX'),
 St([I('O respeito',420,130,w='respeito'),I('fica com você',620,150,c='gold',w='fica',a='slam')],w='Assim'),FIM('sua#2')]
S['36']=[St([I('Quem só treina',340,120),I('na crise',500,130,w='crise'),I('já perdeu',700,220,c='red',w='perdeu',a='slam')],bg='glow:rgba(201,162,39,.25):40'),
 dict(t='pagina',w='Maquiavel',tag='O PRÍNCIPE · CAP. XIV',titulo='Regra do príncipe',ty=300,de='na#2',ate='guerra',hl=['paz','guerra'],y=760,s=80),
 St([I('Quem só estuda na crise',400,90,f='cg',w='quem#2'),I('já chega',580,120,w='chega#2'),I('atrasado',740,200,box='red',w='atrasado',a='slam')],w='Quem#2',bg='num:XIV'),
 Duo('O',D('Vendedor','treina antes da venda',G,w='vendedor'),D('Atleta','treina fora do jogo',P,w='atleta')),
 St([I('A calma é tempo de',400,100,w='calma'),I('se preparar',560,170,c='gold',w='preparar',a='slam'),I('e não de descansar',800,90,f='cg',c='dim',w='descansar')],w='calma'),FIM('descansar')]
S['37']=[St([I('Malvisto',340,170,c='red'),I('por um motivo',520,100,f='cg',w='motivo'),I('falava a verdade',720,150,c='gold',w='como',a='slam')],bg=FOTO),
 Duo('Escreveu',D('Verdade efetiva','o que acontece',G,w='verdade'),D('Imaginação','o que você queria',R,w='imaginação')),
 St([I('O negócio imaginado',400,90,f='cg',c='dim',w='negócio'),I('A carreira imaginada',540,90,f='cg',c='dim',w='carreira'),I('O casamento imaginado',680,90,f='cg',c='dim',w='casamento')],w='Muita',bg='num:XV'),
 St([I('Decisão boa nasce do',380,100,w='decisão'),I('mundo real',560,210,c='gold',w='real',a='slam'),I('e não do ideal',860,90,f='cg',c='dim',w='ideal')],w='Ele#2'),FIM('ideal')]
S['38']=[St([I('Odiado',340,230,c='red'),I('fazendo tudo certo?',640,110,w='certo')],bg='glow:rgba(142,27,27,.35):40'),
 dict(t='pagina',w='Maquiavel',tag='O PRÍNCIPE · CAP. XIX',titulo='O aviso',ty=300,de='o#1',ate='más',hl=['boas','más'],y=760,s=80),
 St([I('Quem muda as regras',400,110,w='muda'),I('incomoda quem vivia',600,100,f='cg',w='incomoda'),I('do jeito errado',780,150,box='red',w='errado',a='slam')],w='Quem'),
 St([I('Faça o bem.',400,150,c='gold',w='faça'),I('Mas saiba de quem<br>se proteger',640,110,w='proteger',a='slam')],w='Não',bg=FOTO.replace('640','900')),FIM('proteger')]
S['39']=[St([I('Quem vai ser',340,120),I('leal',500,260,c='gold',w='leal',a='slam'),I('a você?',820,110,w='você')],bg=FOTO),
 Duo('Maquiavel',D('Benefício que recebe','prende',P,w='recebem'),D('Benefício que faz','prende também',G,w='fazem'),dir='h'),
 St([I('Quem já te ajudou',400,110,w='ajudou'),I('investiu em você',580,130,c='gold',w='investiu',a='slam')],w='Quem#2',bg='num:X'),
 St([I('Quem se sacrificou',380,110,w='sacrificou'),I('fica mais ligado',560,110,c='gold',w='ligado'),I('Honre quem<br>investiu',780,150,box='gold',w='honre',a='slam')],w='Quem#3'),FIM('causa')]
S['40']=[Duo('Sorte',D('Sorte','',P,w='sorte'),D('Talento','',G,w='talento')),
 St([I('São os dois,',400,150,w='dois'),I('juntos',580,240,c='gold',w='juntos',a='slam')],w='Maquiavel',bg='num:VI'),
 St([I('Sem ocasião',380,120,w='ocasião'),I('o valor se apaga',540,90,f='cg',c='dim',w='apagado'),I('Sem valor',740,120,w='valor#2'),I('a ocasião vem em vão',900,90,f='cg',c='red',w='vão',a='slam')],w='Sobre'),
 St([I('A chance vai aparecer.',380,100,w='oportunidade'),I('Você vai estar',600,110,w='você'),I('pronto?',760,220,c='gold',w='pronto',a='slam')],w='oportunidade',bg=FOTO),FIM('vier')]
tons=[61.74,65.41,69.3,73.42,77.78,82.41,58.27]
for i,(n,c) in enumerate(S.items()):json.dump({'tom':tons[(i+3)%7],'cenas':c},open(f'shorts/{n}/cenas_v1.json','w'),ensure_ascii=False,indent=1)
print(len(S))
