import json
I = dict(MS='acervo/portrait_of_niccol_machiavelli_by_santi_di_tito.jpg', PZ='acervo/bernardo_bellotto_the_piazza_della_signoria_in_f.jpg',
 ZAMA='acervo/batalha_ostia_raffaello.jpg', L10='acervo/leao_x_raffaello.jpg', M='maquiavel.jpg', ARC='hist/arco_severo.jpg',
 MAR='hist/marcus_aurelius.jpg', MEQ='hist/marcus_equestre.jpg', BON='hist/bonfire_of_the_vanities.jpg', ALX='hist/alexander_the_great.jpg',
 EMB='acervo/embaixadores_holbein.jpg', ISS='acervo/albrecht_altdorfer_schlacht_bei_issus_alte_pinak.jpg', MUL='acervo/multidao_bruegel.jpg',
 CAR='hist/caracalla.jpg', COM='hist/commodus.jpg', NAP='acervo/carlos_viii_florenca_bezzuoli.jpg', POL='acervo/batalha_ponte_milvio_raffaello.jpg',
 CCA='acervo/sermao_bruegel.jpg', FI='acervo/ferdinand_of_aragon_isabella_of_castile.jpg', GRA='acervo/smk_spaakone_wijck.jpg',
 DEC='acervo/smk_efter_stormen_friedrich.jpg', VER='acervo/smk_uvejr_gaard_juel.jpg', CA='acervo/castiglione_raffaello.jpg',
 GI='acervo/botticelli_giuliano_de_medici_accademia_carrara.jpg', LO='lorenzo.jpg', BO='borgia.jpg', CMG='acervo/cesar_morte_gerome.jpg',
 FER='hist/ferdinand_ii_of_aragon.jpg', HAN='hist/hannibal.jpg', J2='acervo/julio_ii_raffaello.jpg', JUD='acervo/beijo_judas_giotto.jpg',
 PRI='acervo/prisao_cristo_caravaggio.jpg', AL6='hist/pope_alexander_vi.jpg')
C = []
def c(img, mov, txt, **k): C.append(dict(gravura=I[img], mov=mov, txt=txt, **k))
def cap(n, t): return {'cap': {'sup': f'LIÇÃO {n}', 'txt': t}}
def v(t, r): return {'verso': t, 'ref': r}
c('MS','in','Todo mundo fala de O Príncipe. Mas Maquiavel escreveu outro livro, bem maior, que ele mesmo levou mais a sério. E quase ninguém leu. É nele que está a frase que mais se parece com os fins justificam os meios.')
c('PZ','out','Esse livro tem um nome comprido: Discursos sobre a primeira década de Tito Lívio. Três livros, cento e quarenta e dois capítulos, sobre como Roma antiga ficou livre e grande por séculos.')
c('ZAMA','esq','E hoje eu vou te mostrar as lições mais fortes dele, uma por uma, do jeito que você usa no trabalho, nos negócios e dentro de casa. Sem enrolação e sem decoreba.')
c('L10','dir','Mas tem três coisas que eu vou guardar para o caminho. A primeira: para quem Maquiavel dedicou esse livro. Não foi para um príncipe. E o motivo diz muito sobre ele.')
c('M','cima','A segunda: a história de um homem bom que perdeu tudo por ser paciente demais. Esse homem foi o chefe do próprio Maquiavel, e o livro explica por que ele caiu.')
c('ARC','in','E a terceira, a maior: a tal frase dos fins e dos meios. Ela não está em O Príncipe do jeito que te contaram. Está aqui, num capítulo sobre a fundação de Roma. Essa fica para o final.')
c('MAR','out','Primeiro, quem foi Tito Lívio. Um historiador romano que escreveu a história de Roma desde a fundação da cidade. Uma obra enorme, dividida em blocos de dez livros. Cada bloco se chama década.')
c('MEQ','esq','A primeira década, os dez primeiros livros, conta os primeiros séculos de Roma: os reis, a queda do último rei, o nascimento da república e as guerras contra os povos vizinhos.')
c('MS','dir','E esse livro estava na casa de Maquiavel desde cedo. O pai dele, Bernardo, anotou num caderno que recebeu um exemplar de Tito Lívio como pagamento por montar um índice da obra.')
c('BON','cima','Ou seja: o menino cresceu com Roma dentro de casa. Anos depois, já adulto, sem cargo e longe do poder, ele voltou a esse livro e começou a conversar com ele.')
c('ALX','in','No prefácio, ele faz uma crítica que vale até hoje. As pessoas pagam caro por um caco de estátua antiga e enfeitam a casa com ele. Mas ninguém tenta imitar o que os antigos faziam de grande.',
  **v('Muitos pagam caro por um pedaço de estátua antiga, mas ninguém imita as virtudes dos antigos.', 'DISCURSOS, LIVRO I, PROÊMIO'))
c('EMB','out','É como admirar um campeão e nunca copiar o treino dele. Maquiavel queria o contrário: tirar da história regras práticas para viver e governar hoje. É isso que a gente vai fazer.')
c('ISS','esq','Ele mesmo compara a tarefa a procurar mares e terras desconhecidas. Diz que abrir um caminho novo é perigoso, porque as pessoas preferem criticar a elogiar. E mesmo assim ele decidiu ir.')
c('MUL','dir','Lição um. E ela vai contra tudo que se diz de Maquiavel. No capítulo cinquenta e oito do primeiro livro, ele defende o povo contra os príncipes.', **cap(1, 'O povo erra menos'))
c('PZ','cima','A ideia da época era simples: o povo é volúvel, muda de opinião toda hora e não sabe o que quer. Maquiavel responde que isso vale muito mais para os príncipes do que para o povo.',
  **v('Um povo bem ordenado é mais prudente, mais estável e julga melhor do que um príncipe.', 'DISCURSOS, LIVRO I, CAP. 58'))
c('CAR','in','O argumento dele é de quem viu o poder de perto. Um príncipe sem freio faz loucuras que um povo sem freio quase nunca faz. E quando o povo erra, alguém de respeito consegue convencê-lo a voltar atrás.')
c('COM','out','Agora, quando um príncipe mau erra, ninguém tem coragem de falar com ele. O único remédio que sobra é a força. Por isso, para Maquiavel, o erro do príncipe é sempre mais perigoso.')
c('NAP','esq','E ele vai mais longe. Diz que não é à toa que se compara a voz do povo à voz de Deus. A opinião de muita gente, junta, costuma prever as coisas com uma precisão impressionante.',
  **v('Não é sem razão que se compara a voz do povo à voz de Deus.', 'DISCURSOS, LIVRO I, CAP. 58'))
c('BON','dir','Ele dá um exemplo concreto: na hora de escolher quem vai ocupar um cargo, o povo escolhe muito melhor do que um príncipe. Dificilmente o povo coloca no alto uma pessoa de fama ruim.')
c('L10','cima','Traduzindo para a sua vida: decisão importante tomada por uma pessoa só, sem ninguém para dizer não, é um risco. Na empresa, na igreja, na família. Quem não escuta ninguém erra sozinho e erra grande.')
c('POL','in','Mas repara no detalhe que muita gente pula. Ele fala de um povo bem ordenado, com leis. Multidão sem regra, para ele, é tão perigosa quanto tirano sem freio. A força está na regra, não no grito.')
c('M','out','E aí, esse Maquiavel você conhecia? O homem que todo mundo pinta como professor de tirano escrevendo que o povo julga melhor do que o rei. Fica comigo, que daqui pra frente fica melhor.',
  interage={'tipo': 'checkin', 'txt': 'Esse Maquiavel você conhecia?'})
c('CCA','esq','Lição dois. Uma briga que, segundo ele, salvou Roma. Em toda cidade, diz Maquiavel, existem dois humores: o dos grandes, que querem mandar, e o do povo, que não quer ser oprimido.', **cap(2, 'A briga que fez Roma livre'))
c('ARC','dir','Em Roma, o senado e o povo viviam em atrito. Muitos escritores achavam isso uma vergonha. Maquiavel diz o contrário: foi desse atrito, colocado dentro das leis, que nasceu a liberdade romana.',
  **v('Todas as leis feitas em favor da liberdade nascem da desunião entre o povo e os grandes.', 'DISCURSOS, LIVRO I, CAP. 4'))
c('MAR','cima','Um exemplo: depois de um desses conflitos, o povo ganhou os tribunos da plebe, autoridades que existiam para protegê-lo dos abusos dos poderosos. A briga virou instituição. Não virou guerra.')
c('EMB','in','É uma ideia madura. Lugar onde ninguém discorda não é lugar unido. Muitas vezes é lugar onde as pessoas têm medo de falar. E o medo cala o problema, mas não resolve.')
c('FI','out','Me conta uma coisa nos comentários: na sua casa ou no seu trabalho, quando alguém discorda, a conversa melhora a decisão ou vira briga pessoal? Escreve aí, que eu leio.',
  interage={'tipo': 'comenta', 'txt': 'Discordar aí melhora ou vira briga?'})
c('MS','esq','A diferença, para Maquiavel, está nas regras. Discordar com hora, lugar e alguém que decide no final fortalece. Discordar sem regra nenhuma vira facção, e facção destrói qualquer casa.')
c('GRA','dir','Lição três. Agora uma quebra de expectativa. Todo mundo repete que o dinheiro é o nervo da guerra. Maquiavel abre um capítulo inteiro só para dizer que isso é mentira.', **cap(3, 'Ouro não ganha guerra'))
c('ISS','cima','O título do capítulo dez do segundo livro já diz tudo: o dinheiro não é o nervo da guerra, como pensa a maioria. O nervo, para ele, são bons soldados, gente leal e preparada.',
  **v('O dinheiro não é o nervo da guerra, como diz a opinião comum.', 'DISCURSOS, LIVRO II, CAP. 10'))
c('DEC','in','E ele conta uma cena antiga. Creso, um rei riquíssimo, mostrou seus tesouros a Sólon, o sábio de Atenas. Sólon respondeu que, se viesse alguém com ferro melhor, levaria todo aquele ouro.')
c('VER','out','A lógica é fria e certa. Bons soldados encontram ouro. Mas ouro nem sempre encontra bons soldados. Quem só tem dinheiro, e nenhuma gente de confiança, está apenas guardando o prêmio do próximo que chegar.')
c('CA','esq','Leva isso para hoje. Uma empresa com caixa e sem equipe é frágil. Uma família com dinheiro e sem união briga pela herança. O que segura de verdade é gente boa, treinada e comprometida.')
c('GI','dir','E aqui eu fecho a primeira promessa. Lembra da dedicatória? Maquiavel não dedicou esse livro a nenhum príncipe, nem aos Médici. Dedicou a dois amigos: Zanobi Buondelmonti e Cosimo Rucellai.')
c('LO','cima','E explicou o motivo. Disse que escolheu não quem já era príncipe, mas quem merecia ser, pelas suas qualidades. Gente que não podia dar nada a ele, a não ser amizade e boa conversa.',
  **v('Escolhi não os que são príncipes, mas os que, pelas suas qualidades, mereceriam ser.', 'DISCURSOS, DEDICATÓRIA'))
c('PZ','in','Esses dois faziam parte de um grupo que se reunia nos jardins da família Rucellai, em Florença, para discutir política e história. Foi ali, entre amigos, que muitas dessas ideias foram lidas e debatidas.')
c('BO','out','Repara no contraste. O Príncipe foi escrito para agradar um poderoso e conseguir emprego. Os Discursos foram escritos para quem ele respeitava. Talvez por isso aqui ele fale com mais liberdade.')
c('MS','esq','Se você está descobrindo um Maquiavel que ninguém te mostrou, segue o canal agora, porque essa série vai fundo. E ainda faltam seis lições, inclusive a do homem bom que caiu por paciência.',
  interage={'tipo': 'segue', 'txt': 'Segue pro Maquiavel escondido'}, cta='Siga o <b>Raposa e Leão</b><br>e veja a playlist Maquiavel na prática')
c('ARC','dir','Lição quatro. O terceiro livro começa com uma ideia que serve para tudo que você constrói: empresa, casamento, igreja, até a sua própria rotina.', **cap(4, 'Volte ao começo'))
c('DEC','cima','Tudo que é vivo, diz ele, vai se gastando com o tempo. As pessoas esquecem por que começaram, os costumes relaxam e o que era forte vai ficando mole, devagar, sem ninguém perceber.',
  **v('Para que uma república viva muito tempo, é preciso trazê-la de volta ao seu princípio com frequência.', 'DISCURSOS, LIVRO III, CAP. 1'))
c('MEQ','in','O remédio é voltar ao princípio. Lembrar a regra que fez aquilo dar certo no começo. E ele chega a dizer que o ideal seria não passar mais de dez anos sem um desses retornos.')
c('MAR','out','Em Roma, segundo Maquiavel, isso acontecia de dois jeitos. Por leis que obrigavam todo mundo a lembrar das regras antigas. E pelo exemplo de homens bons, que inspiravam os outros só com o modo de viver.')
c('M','esq','Na prática, faz isso com você mesmo. De tempos em tempos, pergunta: por que eu comecei? Quais eram as minhas regras? O que me fez crescer e eu parei de fazer?')
c('CMG','dir','Quem nunca faz essa pergunta vai se afastando aos poucos. E um dia olha no espelho, ou olha para a própria empresa, e não reconhece mais o que construiu.')
c('PZ','cima','Lição cinco. E aqui eu fecho a segunda promessa: o homem bom que perdeu tudo por ser paciente demais. O capítulo nove do terceiro livro explica o que aconteceu com ele.', **cap(5, 'Mude com os tempos'))
c('FER','in','A tese é esta: as pessoas acertam quando o jeito delas combina com o momento, e erram quando o momento muda e elas continuam iguais. Para ter boa sorte sempre, seria preciso mudar junto com os tempos.',
  **v('Quem quer ter sempre boa sorte precisa mudar de jeito conforme os tempos.', 'DISCURSOS, LIVRO III, CAP. 9'))
c('HAN','out','O primeiro exemplo é Roma contra Aníbal. Fábio Máximo, um general cauteloso, evitou batalhas e desgastou o inimigo aos poucos. Naquele momento, a paciência dele salvou a cidade.')
c('ZAMA','esq','Depois veio Cipião, ousado, que levou a guerra para a África e venceu. Maquiavel diz que, se Fábio fosse rei de Roma, talvez perdesse aquela guerra, porque não saberia mudar de estilo.')
c('BON','dir','Agora o segundo exemplo, que dói. Piero Soderini, o chefe do governo de Florença, o homem a quem Maquiavel serviu por anos. Soderini era humano, paciente, conciliador. E isso fez dele um bom líder por um tempo.')
c('L10','cima','Ele prosperou enquanto os tempos pediam calma. Mas quando chegou a hora de ser firme, não conseguiu mudar. Em 1512, a república caiu, os Médici voltaram e Soderini foi para o exílio.')
c('M','in','Maquiavel diz que ele não mudou por dois motivos. Primeiro, porque ninguém vai contra a própria natureza com facilidade. Segundo, porque quem sempre se deu bem de um jeito não se convence a tentar outro.')
c('J2','out','E no mesmo capítulo ele cita o oposto: o papa Júlio Segundo, impetuoso em tudo. Deu certo porque os tempos combinavam com ele. Em O Príncipe, ele completa: se viessem tempos de cautela, Júlio teria caído.')
c('EMB','esq','A lição para você: o que te trouxe até aqui talvez não te leve adiante. O vendedor que cresceu no boca a boca, o pai do filho pequeno, o líder da fase de crise. Cada fase pede um jeito.')
c('MUL','dir','E repara no argumento a favor das repúblicas: como têm muitos líderes diferentes, elas podem pôr no comando o perfil certo para cada momento. Uma pessoa sozinha fica presa ao próprio temperamento.')
c('CA','cima','Por isso, monte uma equipe que não seja feita de cópias suas. Se você é cauteloso, tenha alguém ousado por perto. Se é ousado, escute quem pede calma. É assim que você muda sem deixar de ser você.')
c('GRA','in','Lição seis. Essa parece estranha, mas é uma das mais úteis: saber parar depois de vencer. Muita gente perde tudo não na derrota, mas no dia seguinte à vitória.', **cap(6, 'Saiba parar de vencer'))
c('VER','out','O capítulo vinte e sete do segundo livro é direto: quem é prudente se contenta com a vitória. Quem quer arrancar mais do que já ganhou, na maioria das vezes, acaba perdendo.',
  **v('Aos príncipes e repúblicas prudentes deve bastar vencer, porque, quando não basta, quase sempre se perde.', 'DISCURSOS, LIVRO II, CAP. 27'))
c('ISS','esq','O motivo é humano. Quando você aperta demais quem já perdeu, tira dele qualquer saída. E gente sem saída luta com uma força que não tinha antes. A vitória vira guerra de novo.')
c('POL','dir','No capítulo anterior, ele junta outro aviso: humilhar e debochar do adversário gera ódio, e não traz vantagem nenhuma. Quem humilha ganha um inimigo para o resto da vida.',
  **v('O desprezo e o insulto geram ódio contra quem os usa, sem nenhuma utilidade.', 'DISCURSOS, LIVRO II, CAP. 26'))
c('FI','cima','Junta as duas ideias e você tem uma regra de ouro para negociação, discussão de casal ou disputa no trabalho. Ganhou? Garanta o que ganhou. Não exagere na conta e não pise em quem perdeu.')
c('MS','in','Essa aqui vale guardar. Salva o vídeo, porque na próxima discussão que você ganhar vai bater aquela vontade de humilhar. E é bem nessa hora que você precisa lembrar de Maquiavel.',
  interage={'tipo': 'salva', 'txt': 'Salva pra próxima discussão'})
c('JUD','out','O adversário tratado com dignidade pode virar aliado amanhã. O humilhado vira o inimigo que vai esperar a sua primeira fraqueza. E ele sempre espera.')
c('BO','esq','Lição sete. Agora aparece o lado frio que todo mundo associa ao nome dele. E eu vou te mostrar por que ele é útil, mas para se proteger, não para enganar ninguém.', **cap(7, 'Promessa arrancada não vale'))
c('PRI','dir','O capítulo quarenta e dois do terceiro livro tem um título curto e duro: promessas feitas por força não precisam ser cumpridas. Quem promete com a faca no pescoço, assim que puder, desfaz a promessa.',
  **v('As promessas feitas por força não devem ser cumpridas.', 'DISCURSOS, LIVRO III, CAP. 42'))
c('EMB','cima','Maquiavel não está mandando ninguém mentir. Ele está descrevendo como as pessoas funcionam. E lembra que, quando acaba a força que obrigou a promessa, acaba também a vontade de cumpri-la.')
c('FER','in','Por isso, a lição é para quem negocia. Acordo arrancado na pressão não é acordo. É só uma trégua. Se você forçou o outro lado a aceitar, prepare-se, porque ele vai romper na primeira chance.')
c('GI','out','O acordo que dura é aquele em que o outro lado também sai com alguma coisa. No trabalho, no aluguel, na sociedade, no casamento. Ninguém defende por muito tempo um trato que só serve ao outro.')
c('AL6','esq','E aqui tem uma ponte com O Príncipe. No capítulo dezoito, ele diz que o líder esperto não cumpre a palavra quando ela se volta contra ele. Muitos param de ler aí. É um erro.')
c('M','dir','Porque o mesmo Maquiavel, lido inteiro, mostra que confiança é capital. Quem quebra a palavra a toda hora fica sem crédito. A frieza dele descreve o mundo como ele é, não pede que você vire o pior dele.')
c('MEQ','cima','Lição oito. Uma lição de caráter, e quase ninguém sabe que ela é de Maquiavel. O capítulo trinta e um do terceiro livro fala de como os grandes se comportam na sorte e no azar.', **cap(8, 'O mesmo na sorte e no azar'))
c('MAR','in','A frase central é esta: as repúblicas fortes e os homens excelentes mantêm o mesmo ânimo em qualquer situação. Não se enchem de orgulho quando ganham, nem se desesperam quando perdem.',
  **v('As repúblicas fortes e os homens excelentes mantêm o mesmo ânimo em qualquer fortuna.', 'DISCURSOS, LIVRO III, CAP. 31'))
c('ARC','out','O exemplo dele é Camilo, um líder romano. Maquiavel conta que Camilo não se envaideceu na vitória nem se abateu no exílio. Continuou o mesmo homem, com a mesma firmeza, nos dois extremos.')
c('COM','esq','E ele mostra o contrário também: gente que, quando a sorte sorri, fica arrogante, e quando a sorte vira, cai na covardia. Esse tipo de pessoa perde tudo justamente quando mais precisa de calma.')
c('LO','dir','Pensa em quem você admira de verdade. Aposto que é alguém que não mudou quando ganhou dinheiro, nem desmoronou quando perdeu. Essa estabilidade é a maior força que um líder pode ter.')
c('MS','cima','E o próprio Maquiavel viveu isso. Escreveu esse livro depois de perder o cargo, de ser preso e de ir morar no campo. Em vez de amargar, transformou a queda em obra. É o conselho dele vivido na pele.')
c('M','in','Se você conhece alguém passando por uma fase ruim, que perdeu emprego ou negócio, manda esse vídeo pra essa pessoa. Às vezes, ouvir que dá para cair sem deixar de ser quem é ajuda muito.',
  interage={'tipo': 'manda', 'txt': 'Manda pra quem tá na pior'})
c('ALX','out','Lição nove, a última. E chegou a hora da maior promessa: a frase que mais se parece com os fins justificam os meios. Ela está no capítulo nove do primeiro livro. E o contexto muda tudo.', **cap(9, 'Um funda, muitos conservam'))
c('MEQ','esq','O capítulo fala de Rômulo, o fundador de Roma, que, segundo a tradição, matou o irmão Remo e depois aceitou a morte do colega Tito Tácio. Maquiavel pergunta: um homem desses pode servir de exemplo?')
c('CCA','dir','E a resposta dele é a frase famosa: se o fato o acusa, o resultado o desculpa. Ou seja, um ato ruim pode ser julgado pelo que ele produziu. É daqui que muita gente tirou os fins justificam os meios.',
  **v('Se o fato o acusa, o resultado o desculpa.', 'DISCURSOS, LIVRO I, CAP. 9'))
c('MAR','cima','Mas leia a frase que vem logo depois, que quase ninguém cita. Ele diz que deve ser condenado quem usa a violência para destruir, e não quem usa para consertar. O critério é o bem comum, não o interesse próprio.')
c('NAP','in','E tem mais. Ele diz que o fundador prudente não deixa o poder de herança para os filhos. Uma coisa pode ser fundada por um só, mas só dura se depois ficar nas mãos de muitos.')
c('PZ','out','Repara como isso muda tudo. A frase que virou desculpa de tirano está num capítulo que termina defendendo que o poder seja dividido. É o oposto do que te contaram.',
  **v('O que é organizado por um só não dura se fica nos ombros dele, mas sim quando fica aos cuidados de muitos.', 'DISCURSOS, LIVRO I, CAP. 9'))
c('MS','esq','E a expressão os fins justificam os meios, exatamente assim, não aparece em nenhum livro dele. É um resumo que surgiu depois. E os estudiosos até hoje discordam sobre o quanto ela representa o que ele pensava.')
c('LO','dir','Então, os dois livros se contradizem? Muita gente acha que sim. Mas lidos juntos, eles se encaixam. O Príncipe fala do momento de fundar ou salvar algo em crise. Os Discursos falam de como fazer isso durar.')
c('BON','cima','Fundar pede um. Durar pede muitos. Essa é a ponte entre os dois livros. E é por isso que, para entender Maquiavel de verdade, não dá para ler só a metade famosa.')
c('MUL','in','Recapitulando o que você levou hoje. O povo bem ordenado julga melhor do que um só. Discordar com regra fortalece. Ouro não ganha guerra, gente boa ganha. E volte ao começo de tempos em tempos.')
c('ZAMA','out','Mude quando o tempo mudar. Pare depois de vencer e não humilhe ninguém. Acordo forçado não dura. Seja o mesmo na sorte e no azar. E quem funda sozinho precisa entregar a obra a muitos.')
c('EMB','esq','Qual dessas lições você precisava ouvir hoje? Deixa o número dela nos comentários. Eu quero saber qual bateu mais forte em você, e por quê.')
c('M','dir','Se você leu só O Príncipe, conhece metade de Maquiavel. A outra metade está aqui, num livro escrito para amigos, sobre leis, liberdade e um povo bem organizado. Por isso ele continua atual depois de cinco séculos.')
c('MS','in','No próximo vídeo da playlist Maquiavel na prática, a gente entra no teste dele para saber em quem confiar, com as conspirações que esse mesmo livro analisa. Até a próxima lição, raposa.',
  cta='Próximo: <b>em quem confiar</b><br>Até a próxima lição, raposa', selo='RAPOSA<br>E LEÃO')

for i in sorted([11, 43, 61, 86], reverse=True): del C[i]
legenda = ('Maquiavel escreveu um livro maior e mais importante do que O Príncipe, e quase ninguém leu: os Discursos sobre a primeira década de Tito Lívio. Neste vídeo você conhece as 9 lições mais fortes dessa obra, escrita para dois amigos e não para um príncipe.\n\n'
 'O povo que julga melhor do que o rei, a briga que fez Roma livre, por que o dinheiro não é o nervo da guerra, voltar ao começo, mudar com os tempos (e a queda de Piero Soderini), saber parar depois de vencer, a promessa arrancada à força, o mesmo ânimo na sorte e no azar e a verdadeira origem da ideia de que os fins justificam os meios. Tudo aplicado ao trabalho, aos negócios e à família.\n\n'
 '⏱️ Capítulos\n{CAPITULOS}\n\n'
 '📜 Fonte: Nicolau Maquiavel, Discursos sobre a primeira década de Tito Lívio: dedicatória; livro I, proêmio e caps. 4, 9 e 58; livro II, caps. 10, 26 e 27; livro III, caps. 1, 9, 31 e 42. O Príncipe, caps. XVIII e XXV. As citações aparecem em paráfrase curta.\n\n'
 '🦊🦁 Raposa e Leão: Maquiavel e as leis do poder aplicadas à vida real.\n\n'
 '▶️ Playlist recomendada: Maquiavel na prática\n\n'
 '#Maquiavel #DiscursosSobreTitoLívio #OPríncipe #RomaAntiga #Liderança')
d = dict(id='longo-05', canal='raposa', formato='longo', titulo='O livro de Maquiavel que ninguém lê',
 legenda=legenda,
 comentario='📌 Das 9 lições dos Discursos, qual você mais precisa hoje: voltar ao começo, mudar com os tempos ou saber parar depois de vencer? Continue na playlist Maquiavel na prática ⬇️',
 titulo_tela={'sup': 'RAPOSA E LEÃO', 'txt': 'O livro que<br>ninguém lê', 'dur': 3.2},
 capa={'A': 'O outro livro', 'B': 'Ninguém leu', 'gravA': 'maquiavel.jpg', 'gravB': 'cesar.jpg'}, cenas=C)
R = '/home/user/lindson/conteudo/youtube/raposa-e-leao'
json.dump(d, open(R + '/roteiros/longo-05.json', 'w'), ensure_ascii=False, indent=1)
ws = [len(x['txt'].split()) for x in C]
print(len(C), 'cenas', sum(ws), 'palavras', min(ws), max(ws), 'caps', sum('cap' in x for x in C), 'versos', sum('verso' in x for x in C),
      'interage', sum('interage' in x for x in C), 'imgs', len({x['gravura'] for x in C}), 'cta em', [i for i, x in enumerate(C) if 'cta' in x])
print([ (i, w) for i, w in enumerate(ws) if w < 15 or w > 45])
print('repetidas seguidas', [i for i in range(1, len(C)) if C[i]['gravura'] == C[i-1]['gravura']])
