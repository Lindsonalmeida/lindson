"""Conversa com o ouvinte nos Shorts do Raposa e Leão (uma fala própria para cada vídeo, nada de bordão copiado).
meio: (antes da cena k, tipo, fala, texto grande na tela, texto do componente)
fim:  (tipo, fala, texto grande na tela, texto do componente)
tipo: checkin | comenta | segue | salva | manda   (em "comenta", o componente mostra a resposta sendo digitada)
fecho: (estilo da assinatura: classico | seguir | pergunta, frase)
abre: zoom | flash | tremor   ·   pulso: segundos entre batidas   ·   batida: reto | duplo | espacado"""
C = {}
C['01'] = dict(meio=(1, 'comenta', 'Você também achava que essa frase era dele? Responde aí: sim ou não.', 'Achava que<br>era dele?', 'SIM, ACHAVA'),
               fim=('comenta', 'E você, já foi julgado pelo resultado, e não pela intenção? Me conta aqui embaixo.', 'Já te julgaram<br>assim?', 'JÁ, NO TRABALHO'),
               fecho=('seguir', 'O mundo olha o resultado.'), abre='flash', pulso=1.25, batida='reto')
C['02'] = dict(meio=(3, 'checkin', 'Pensa rápido: hoje você é mais raposa ou mais leão? Guarda a resposta, que eu já te mostro o que fazer.', 'Mais raposa ou<br>mais leão?', 'PENSEI'),
               fim=('comenta', 'Escreve aqui embaixo: raposa ou leão. Qual dos dois está faltando em você?', 'Qual falta<br>em você?', 'FALTA O LEÃO'),
               fecho=('classico', 'Esperteza e força. As duas.'), abre='zoom', pulso=.95, batida='duplo')
C['03'] = dict(meio=(3, 'checkin', 'Até aqui faz sentido pra você? Agora vem a parte que quase todo mundo esquece.', 'Faz sentido<br>até aqui?', 'TÔ ACOMPANHANDO'),
               fim=('comenta', 'Na sua vida, quem é mais respeitado: o chefe temido ou o chefe amado? Conta nos comentários.', 'Temido ou<br>amado?', 'O TEMIDO, SEM ÓDIO'),
               fecho=('pergunta', 'Respeito sim. Ódio nunca.'), abre='tremor', pulso=1.6, batida='espacado')
C['04'] = dict(meio=(3, 'checkin', 'Já viu uma amizade acabar por causa de dinheiro? Se já viu, você sabe que é verdade.', 'Já viu isso<br>acontecer?', 'JÁ VI'),
               fim=('salva', 'Salva esse vídeo e lembra dele na próxima vez que alguém mexer no que é seu. Ou você no que é dos outros.', 'Guarda essa<br>lição', 'SALVA ESSE'),
               fecho=('classico', 'O bolso tem memória longa.'), abre='flash', pulso=1.1, batida='reto')
C['05'] = dict(meio=(4, 'checkin', 'Pensa agora numa notícia ruim que você está adiando. Pensou? Então escuta isso.', 'Qual notícia você<br>está adiando?', 'PENSEI EM UMA'),
               fim=('comenta', 'Qual notícia ruim você vai dar de uma vez essa semana? Se for encarar, escreve: vou falar.', 'Vai encarar?', 'VOU FALAR'),
               fecho=('seguir', 'Uma lição de Maquiavel em cada vídeo.'), abre='zoom', pulso=1.25, batida='duplo')
C['06'] = dict(meio=(2, 'checkin', 'Olha em volta agora. Quem são as cinco pessoas mais perto de você?', 'Quem está<br>perto de você?', 'OLHEI'),
               fim=('manda', 'Manda esse vídeo pra pessoa que deixa o seu círculo mais forte. Ela merece saber disso.', 'Quem fortalece<br>o seu círculo?', 'MANDA PRA ELA'),
               fecho=('classico', 'Diga-me quem te cerca.'), abre='tremor', pulso=1.6, batida='reto')
C['07'] = dict(meio=(2, 'checkin', 'Já ficou no meio de uma briga e saiu perdendo dos dois lados? Pois é.', 'Já passou<br>por isso?', 'JÁ PASSEI'),
               fim=('comenta', 'E você, costuma ficar em cima do muro? Responde com sinceridade: sim ou não.', 'Em cima<br>do muro?', 'NÃO MAIS'),
               fecho=('pergunta', 'Escolha um lado. Com cabeça.'), abre='flash', pulso=.95, batida='espacado')
C['08'] = dict(meio=(2, 'checkin', 'Tá comigo? Isso não é pra você virar desconfiado de todo mundo. É pra ajudar do jeito certo.', 'Ajudar do<br>jeito certo', 'ENTENDI'),
               fim=('comenta', 'Você já ajudou alguém a crescer e depois ficou de fora? Conta como foi aqui embaixo.', 'Já te<br>aconteceu?', 'JÁ, COM UM SÓCIO'),
               fecho=('seguir', 'Siga e não entregue a chave.'), abre='zoom', pulso=1.1, batida='duplo')
C['09'] = dict(meio=(2, 'checkin', 'Qual desses três está acontecendo com você agora? Escolhe um, só na sua cabeça.', 'Qual desses<br>é o seu?', 'ESCOLHI'),
               fim=('segue', 'Segue o Raposa e Leão pra aprender a enxergar o problema enquanto ele ainda é pequeno.', 'Veja antes<br>de todo mundo', 'SIGA O CANAL'),
               fecho=('classico', 'Cure a febre no começo.'), abre='tremor', pulso=1.25, batida='reto')
C['10'] = dict(meio=(2, 'checkin', 'Seja sincero: o seu perfil hoje mostra o quanto você é bom no que faz?', 'Seu perfil<br>mostra isso?', 'AINDA NÃO'),
               fim=('comenta', 'Qual detalhe pode estar te fazendo parecer amador? Escreve um só aqui embaixo.', 'Um detalhe só', 'A FOTO DO PERFIL'),
               fecho=('pergunta', 'Pareça o que você é.'), abre='flash', pulso=1.6, batida='duplo')
C['11'] = dict(meio=(2, 'checkin', 'Já tentou mudar alguma coisa e todo mundo ficou contra? Então presta atenção no que vem agora.', 'Já te<br>aconteceu?', 'JÁ'),
               fim=('salva', 'Salva esse vídeo pro dia em que a resistência aparecer. Porque ela vai aparecer.', 'Pro dia da<br>resistência', 'SALVA ESSE'),
               fecho=('seguir', 'Mude. E segure firme.'), abre='zoom', pulso=.95, batida='reto')
C['12'] = dict(meio=(2, 'checkin', 'Até aqui, tudo certo? Agora vem o como, que é o mais importante.', 'Agora,<br>o como', 'TUDO CERTO'),
               fim=('comenta', 'Quem é a pessoa que te fala a verdade mesmo quando dói? Escreve só a primeira letra do nome dela.', 'Quem te fala<br>a verdade?', 'M'),
               fecho=('classico', 'Ouça poucos. Decida sozinho.'), abre='tremor', pulso=1.1, batida='espacado')
C['13'] = dict(meio=(2, 'checkin', 'E aí, qual é o seu dique hoje? Guarda essa pergunta.', 'Qual é o<br>seu dique?', 'GUARDEI'),
               fim=('comenta', 'Escreve aqui um dique que você vai começar a construir essa semana. Reserva, preparo ou contatos?', 'Seu dique<br>da semana', 'RESERVA'),
               fecho=('seguir', 'Construa na calmaria.'), abre='flash', pulso=1.25, batida='duplo')
C['14'] = dict(meio=(2, 'checkin', 'Tá entendendo a ideia? Força aqui não é briga. É estrutura.', 'Força =<br>estrutura', 'FAZ SENTIDO'),
               fim=('comenta', 'Qual ideia sua morreu por falta de estrutura? Conta pra mim nos comentários.', 'Qual ideia<br>morreu?', 'MINHA LOJA'),
               fecho=('pergunta', 'Ideia boa precisa de braço.'), abre='zoom', pulso=1.6, batida='reto')
C['15'] = dict(meio=(2, 'checkin', 'Já reparou como tem gente que sorri, mas não esquece?', 'Sorri, mas<br>não esquece', 'JÁ REPAREI'),
               fim=('segue', 'Se essa lição te fez pensar em alguém, segue o canal. Tem mais Maquiavel aplicado à vida real.', 'Pensou em<br>alguém?', 'SIGA O CANAL'),
               fecho=('classico', 'Favor não apaga ferida.'), abre='tremor', pulso=.95, batida='duplo')
C['16'] = dict(meio=(2, 'checkin', 'Conhece alguém assim? Que gasta pra impressionar e depois aperta quem está perto?', 'Conhece alguém<br>assim?', 'CONHEÇO'),
               fim=('comenta', 'Generosidade que cabe no bolso. Você concorda ou discorda? Escreve aí.', 'Concorda?', 'CONCORDO'),
               fecho=('seguir', 'Generoso, sim. Falido, não.'), abre='flash', pulso=1.1, batida='espacado')
C['17'] = dict(meio=('notícia', 'checkin', 'Rapidinho: em qual desses você se encaixa hoje? Responde só pra você.', 'Qual é o<br>seu tipo?', 'JÁ SEI'),
               fim=('comenta', 'Comenta um, dois ou três: qual tipo você quer ser daqui a um ano?', 'Daqui a<br>um ano?', 'O TIPO 1'),
               fecho=('pergunta', 'Só não seja o terceiro.'), abre='zoom', pulso=1.25, batida='reto')
C['18'] = dict(meio=(2, 'checkin', 'Imagina a paciência desse homem. Você aguentaria?', 'Você<br>aguentaria?', 'NÃO SEI'),
               fim=('salva', 'Salva esse pra lembrar: nem toda hora é hora de mostrar tudo o que você sabe.', 'Nem toda hora<br>é hora', 'SALVA ESSE'),
               fecho=('seguir', 'Quem é subestimado, avança.'), abre='tremor', pulso=1.6, batida='duplo')
C['19'] = dict(meio=(2, 'checkin', 'Percebe a diferença? A mesma situação, dois resultados.', 'Percebe a<br>diferença?', 'PERCEBI'),
               fim=('manda', 'Manda pra alguém que vive cedendo de cara fechada. Vai ajudar.', 'Conhece<br>alguém assim?', 'MANDA PRA ELE'),
               fecho=('classico', 'Ceda como quem decide.'), abre='flash', pulso=.95, batida='reto')
C['20'] = dict(meio=(2, 'checkin', 'Já recebeu um pedido assim? Dá vontade de fazer o contrário, né?', 'Já recebeu<br>um assim?', 'JÁ RECEBI'),
               fim=('comenta', 'Você costuma pedir ou ameaçar quando quer algo? Sem vergonha, conta aqui.', 'Pede ou<br>ameaça?', 'EU AMEAÇAVA'),
               fecho=('pergunta', 'Ou pede, ou age.'), abre='zoom', pulso=1.1, batida='duplo')
C['21'] = dict(meio=(1, 'checkin', 'Já fez algo obrigado e ninguém agradeceu? Agora você sabe o porquê.', 'Agora faz<br>sentido?', 'FAZ'),
               fim=('comenta', 'O que você vai entregar antes de te cobrarem essa semana? Escreve aqui pra se comprometer.', 'Antes da<br>cobrança', 'O RELATÓRIO'),
               fecho=('seguir', 'Dê antes de pedirem.'), abre='tremor', pulso=1.25, batida='espacado')
C['22'] = dict(meio=(2, 'checkin', 'Pensa em alguém que vive debochando. Essa pessoa é respeitada de verdade?', 'Respeitado<br>de verdade?', 'NÃO É'),
               fim=('segue', 'Se você também prefere vencer calado, segue o Raposa e Leão.', 'Vença calado', 'SIGA O CANAL'),
               fecho=('classico', 'O forte não humilha.'), abre='flash', pulso=1.6, batida='reto')
C['23'] = dict(meio=(3, 'checkin', 'Já viu alguém perder tudo por querer só mais um pouco? É exatamente isso.', 'Já viu<br>isso?', 'JÁ VI'),
               fim=('comenta', 'Qual vitória sua você precisa garantir agora, em vez de arriscar? Me conta.', 'Qual<br>vitória?', 'MEU EMPREGO NOVO'),
               fecho=('pergunta', 'Ganhou? Garanta.'), abre='zoom', pulso=.95, batida='duplo')
C['24'] = dict(meio=(2, 'checkin', 'Faz sentido? Isso explica por que tanta gente boa fica calada em reunião.', 'Faz<br>sentido?', 'EXPLICA MUITO'),
               fim=('salva', 'Salva pra próxima reunião em que você tiver uma ideia diferente.', 'Pra próxima<br>reunião', 'SALVA ESSE'),
               fecho=('seguir', 'Proponha com calma.'), abre='tremor', pulso=1.1, batida='reto')
C['25'] = dict(meio=(2, 'checkin', 'Tá ligado como isso aparece no dia a dia? A promoção boa demais. O sócio fácil demais.', 'Bom demais<br>pra ser verdade', 'TÔ LIGADO'),
               fim=('comenta', 'Qual foi a isca mais óbvia em que você já caiu? Conta aqui, ninguém vai julgar.', 'Sua isca', 'UM GOLPE NO PIX'),
               fecho=('classico', 'Fácil demais? Desconfie.'), abre='flash', pulso=1.25, batida='espacado')
C['26'] = dict(meio=(2, 'checkin', 'Você costuma contar seus planos antes da hora? Pensa nisso um segundo.', 'Conta antes<br>da hora?', 'CONTO'),
               fim=('segue', 'Segue o canal pra mais estratégia como essa, direto do Maquiavel pra sua vida.', 'Mais estratégia', 'SIGA O CANAL'),
               fecho=('classico', 'Escute aberto. Decida fechado.'), abre='zoom', pulso=1.6, batida='duplo')
C['27'] = dict(meio=('raiva', 'checkin', 'E você, se considera mais disciplinado ou mais explosivo? Responde pra você mesmo.', 'Disciplina<br>ou fúria?', 'EXPLOSIVO'),
               fim=('comenta', 'Qual treino você vai repetir todo dia a partir de hoje? Escreve aqui e cumpre.', 'Seu treino<br>diário', 'LER 10 PÁGINAS'),
               fecho=('pergunta', 'Repetição vence talento.'), abre='tremor', pulso=.95, batida='reto')
C['28'] = dict(meio=(2, 'checkin', 'Concorda com ele até aqui? Muita gente pensa o contrário.', 'Concorda?', 'CONCORDO'),
               fim=('manda', 'Manda esse vídeo pra alguém que tem um negócio. Essa lição vale muito.', 'Quem tem<br>um negócio?', 'MANDA PRA ELE'),
               fecho=('seguir', 'Gente boa primeiro.'), abre='flash', pulso=1.1, batida='duplo')
C['29'] = dict(meio=(2, 'checkin', 'Você é mais cauteloso ou mais ousado? Guarda a resposta.', 'Cauteloso<br>ou ousado?', 'CAUTELOSO'),
               fim=('comenta', 'O que te trouxe até aqui e que você vai precisar mudar? Escreve aqui embaixo.', 'O que vai<br>mudar?', 'MEU MEDO'),
               fecho=('classico', 'Mude com os tempos.'), abre='zoom', pulso=1.25, batida='reto')
C['30'] = dict(meio=(3, 'checkin', 'Lembra por que você começou o que faz hoje? Pensa nisso agora.', 'Lembra por que<br>começou?', 'LEMBREI'),
               fim=('comenta', 'Escreve em uma palavra por que você começou. Quero ler.', 'Em uma<br>palavra', 'FAMÍLIA'),
               fecho=('pergunta', 'Volte às origens.'), abre='flash', pulso=1.6, batida='espacado')
