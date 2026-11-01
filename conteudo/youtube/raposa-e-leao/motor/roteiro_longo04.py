"""Raposa e Leão · longo-04 refeito (31/10) no formato novo de cenas (BRIEF.md), 16-20 min.
Mesmo tema e base do original (longos/04/roteiro.json, guardado como histórico): as regras gerais do livro VII de A Arte da Guerra.
python3 roteiro_longo04.py -> ../roteiros/longo-04.json (e mostra cenas, palavras e checagens)"""
import json, os
D = os.path.dirname(os.path.abspath(__file__)); R = os.path.join(D, '..')

# apelidos das imagens (só arquivos de img/acervo/MAPA.md)
I = dict(M='maquiavel.jpg', MS='acervo/portrait_of_niccol_machiavelli_by_santi_di_tito.jpg', L='lorenzo.jpg', B='borgia.jpg',
         AVI='hist/pope_alexander_vi.jpg', J2='acervo/julio_ii_raffaello.jpg', J2M='hist/pope_julius_ii.jpg', LX='acervo/leao_x_raffaello.jpg',
         GB='acervo/botticelli_giuliano_de_medici_accademia_carrara.jpg', CAS='acervo/castiglione_raffaello.jpg', SAV='hist/girolamo_savonarola.jpg',
         FER='hist/ferdinand_ii_of_aragon.jpg', FI='acervo/ferdinand_of_aragon_isabella_of_castile.jpg', EMB='acervo/embaixadores_holbein.jpg',
         PZ='acervo/bernardo_bellotto_the_piazza_della_signoria_in_f.jpg', REL='hist/bonfire_of_the_vanities.jpg', MUL='acervo/multidao_bruegel.jpg',
         GRA='acervo/rendicao_granada_pradilla.jpg', NAP='acervo/coroacao_napoleao_david.jpg', JUD='acervo/beijo_judas_giotto.jpg',
         CAR='acervo/prisao_cristo_caravaggio.jpg', CC='acervo/cesar_assassinato_camuccini.jpg', CG='acervo/cesar_morte_gerome.jpg',
         PV='acervo/pollice_verso_gerome.jpg', ROM='acervo/romanos_decadencia_couture.jpg', VER='acervo/vercingetorix_royer.jpg',
         ZAM='acervo/hannibal_and_scipio_africanus.jpg', ISS='acervo/albrecht_altdorfer_schlacht_bei_issus_alte_pinak.jpg',
         ISS2='acervo/the_battle_of_alexander_at_issus_by_albrecht_alt.jpg', ALX='hist/alexander_the_great.jpg', CES='cesar.jpg',
         CARA='hist/caracalla.jpg', COM='hist/commodus.jpg', MA='hist/marcus_aurelius.jpg', MAE='hist/marcus_equestre.jpg',
         HAN='hist/hannibal.jpg', OST='acervo/batalha_ostia_raffaello.jpg', BPM='acervo/batalha_ponte_milvio_raffaello.jpg', C8='acervo/carlos_viii_florenca_bezzuoli.jpg', SER='acervo/sermao_bruegel.jpg', CHE='acervo/smk_stormflod_vernet.jpg', TEM='acervo/smk_storm_bakhuizen.jpg', NAU='acervo/smk_skibbrud_dahl.jpg', ABR='acervo/smk_efter_regn_skovgaard.jpg', POR='acervo/smk_havn_bakhuizen.jpg', SOR='acervo/smk_spaakone_wijck.jpg', RAI='acervo/smk_uvejr_dietrich.jpg', SOL='acervo/smk_uvejr_gaard_juel.jpg', DES='acervo/smk_efter_stormen_friedrich.jpg', ARC='hist/arco_severo.jpg', MOS='hist/moses.jpg')
MOV = ['in', 'out', 'esq', 'dir', 'cima', 'out', 'in', 'dir', 'esq', 'cima', 'in', 'esq', 'out', 'cima', 'dir']
cenas = []

def c(img, txt, **x):
    cenas.append(dict(gravura=I[img], mov=MOV[len(cenas) % len(MOV)], txt=txt, **x))

def cap(n, t): return {'sup': f'LIÇÃO {n}', 'txt': t}
LVII = 'A ARTE DA GUERRA, LIVRO VII'

# ── gancho e loops
c('ISS', 'O homem que escreveu o manual de guerra mais lido do Renascimento perdeu a única guerra que organizou. E foi depois dessa derrota que ele escreveu as regras que você vai ouvir hoje.')
c('M', 'Esse homem é Nicolau Maquiavel. Todo mundo conhece O Príncipe. Quase ninguém sabe que ele escreveu um livro inteiro sobre guerra, e que no fim desse livro existe uma lista de regras gerais.')
c('OST', 'Ele escreveu para generais. Mas essas regras servem para qualquer disputa: uma vaga de emprego, uma negociação, um concorrente que abriu do lado da sua loja, até uma briga de família por herança.')
c('B', 'Eu separei as dez mais úteis. E tem duas coisas que eu vou te contar no caminho. A primeira: qual foi a guerra que o próprio Maquiavel perdeu, e qual dessas regras ele quebrou.')
c('ALX', 'A segunda, a maior, fica para o final: tem uma regra no livro que vale por todas as outras juntas. Se você só lembrar de uma coisa deste vídeo, vai ser dela.')
# ── 1 o livro
c('PZ', 'Volta comigo para Florença. O livro se chama A Arte da Guerra. Saiu impresso em 1521, e foi um dos poucos livros de Maquiavel publicados enquanto ele ainda estava vivo.', cap=cap(1, 'O manual que ninguém lê'))
c('EMB', 'O Príncipe e os Discursos, os dois mais famosos, só foram impressos depois da morte dele. Ou seja: esse manual de guerra foi o livro que Maquiavel quis mostrar ao mundo com o próprio nome.')
c('CAS', 'E ele escreveu em forma de conversa. A cena se passa num jardim de Florença, os Orti Oricellari, da família Rucellai, onde jovens se reuniam para discutir política e história antiga.')
c('MA', 'Quem fala quase o tempo todo é um comandante experiente, Fabrizio Colonna, um militar de verdade daquela época. Os jovens perguntam, ele responde, e assim o livro vai do recrutamento até a batalha.')
c('MAE', 'São sete livros. E no sétimo, quando a conversa está acabando, Fabrizio faz uma coisa que todo bom professor faz: ele resume tudo numa lista curta de regras gerais.', verso='Quero deixar-vos algumas regras gerais, que vos serão muito familiares.', ref=LVII)
c('REL', 'É dessa lista que vêm as regras deste vídeo. Eu vou citar cada uma com fidelidade, em português simples, e depois mostrar como ela funciona hoje, fora do campo de batalha.')
c('MS', 'Antes, um aviso que Maquiavel daria: regra de disputa serve para se proteger e para vencer com inteligência. Não é para destruir pessoas. Quem usa estratégia para pisar nos outros cria inimigos que não precisava.')
# ── 2 regras 1 e 2
c('BPM', 'Regra número um, a mais simples de todas: o que ajuda o inimigo te prejudica, e o que te ajuda prejudica o inimigo.', cap=cap(2, 'Quem ganha com isso?'),
  verso='O que ajuda o inimigo te prejudica; o que te ajuda prejudica o inimigo.', ref=LVII)
c('SER', 'Parece óbvio. Mas repara quantas decisões a gente toma sem fazer a pergunta mais básica de qualquer disputa: no fim das contas, quem sai fortalecido com isso?')
c('EMB', 'Um exemplo: você dá um desconto enorme para fechar uma venda rápida. O cliente ganha. Mas quem mais ganha? Talvez o concorrente, porque agora o mercado inteiro aprende a esperar aquele preço.')
c('MUL', 'Ou no trabalho: você reclama do chefe no grupo da empresa. Na hora alivia. Mas quem ganha com aquela mensagem? Às vezes é o colega que quer a sua vaga e guarda o print.')
c('CARA', 'Então a primeira regra vira uma pergunta que cabe no bolso. Antes de agir numa disputa, pergunte: isso me fortalece, ou fortalece quem disputa comigo?')
c('FER', 'Regra número dois: nenhum plano é melhor do que aquele que fica escondido do adversário até você executar.', verso='Nenhum plano é melhor do que aquele que fica escondido do inimigo até ser executado.', ref=LVII)
c('FI', 'Fernando de Aragão, um rei que Maquiavel admirava e temia, era mestre nisso. No capítulo vinte e um de O Príncipe, ele conta como Fernando mantinha todos ocupados e surpresos com novas empreitadas.')
c('EMB', 'Hoje isso vale para lançamento de produto, para troca de emprego, para negociação de salário. Quem anuncia o que vai fazer dá ao outro lado o presente mais valioso de uma disputa: tempo para se preparar.')
c('L', 'Mas atenção: esconder o plano não é mentir. É escolher a hora de revelar. Muita ideia boa morre porque foi contada cedo demais, para gente demais, antes de estar pronta para andar sozinha.')
c('JUD', 'E repara que a primeira e a segunda regra conversam. Quando você conta o plano antes da hora, quem é que ganha? Exatamente. Quem disputa com você.')
c('CAS', 'Pensa aí: qual plano seu você contou cedo demais e alguém atrapalhou? Ou copiou? Conta nos comentários. Eu leio, e muita gente vai se reconhecer na sua história.',
  interage={'tipo': 'comenta', 'txt': 'Contou cedo e se deu mal?'}, conv=True)
# ── 3 regra 3 ocasião
c('J2', 'Regra número três: saber reconhecer a ocasião na guerra e agarrá-la ajuda mais do que qualquer outra coisa.', cap=cap(3, 'A porta que abre uma vez'),
  verso='Saber conhecer a ocasião e agarrá-la ajuda mais do que qualquer outra coisa.', ref=LVII)
c('J2M', 'Maquiavel repete essa ideia em vários livros. Em O Príncipe, no capítulo seis, ele diz que os grandes fundadores só brilharam porque a ocasião apareceu. Mas sem a capacidade deles, a ocasião teria passado em vão.')
c('MOS', 'Um dos exemplos que ele usa é Moisés. O povo de Israel precisava estar oprimido no Egito para querer segui-lo. A ocasião deu a matéria, mas foi a virtude dele que deu forma a essa matéria.', verso='Sem a ocasião, a virtude se apagaria; sem a virtude, a ocasião viria em vão.', ref='O PRÍNCIPE, CAP. VI')
c('ABR', 'Traduzindo para hoje: a sorte traz a porta, mas quem passa por ela é quem já estava pronto antes. Quando a oportunidade aparece, não dá mais tempo de se preparar.')
c('PZ', 'Então como ficar pronto para a ocasião? Primeiro, prepare-se antes: estude, junte reserva, treine a habilidade. Segundo, observe o que mudou ao seu redor, porque toda ocasião nasce de uma mudança.')
c('MUL', 'E terceiro: quando a porta abrir, aja rápido. Oportunidade que espera demais vira oportunidade de outra pessoa. Ela não fica parada te esperando decidir.')
# ── 4 regra 4 treino
c('ARC', 'Regra número quatro, a minha preferida: a natureza gera poucos homens valentes, e o esforço e o treino fazem muitos.', cap=cap(4, 'Treino vence talento'),
  verso='A natureza gera poucos homens valentes; o esforço e o treino fazem muitos.', ref=LVII)
c('SOR', 'E logo em seguida ele completa: na guerra, a disciplina pode mais do que a fúria. Para Maquiavel, não existe coragem de um dia que substitua a repetição de todos os dias.', verso='Na guerra, a disciplina pode mais do que a fúria.', ref=LVII)
c('MA', 'Ele leva isso tão a sério que, em O Príncipe, no capítulo catorze, diz que o governante deve se exercitar para a guerra mais na paz do que na própria guerra.', verso='Nunca deve tirar o pensamento do exercício da guerra, e na paz deve exercitá-lo mais do que na guerra.', ref='O PRÍNCIPE, CAP. XIV')
c('SOL', 'Muita gente começa um projeto movida por raiva ou empolgação. Funciona por uma semana. Depois a empolgação passa, a raiva esfria, e só a disciplina segura o projeto de pé.')
c('MAE', 'E essa é talvez a regra mais encorajadora do livro inteiro. Se a natureza faz poucos fortes e o treino faz muitos, então quase tudo pode ser aprendido: vender, falar em público, liderar, negociar.')
c('MS', 'O que separa as pessoas, quase sempre, não é o dom de nascença. É a quantidade de vezes que cada uma repetiu a coisa chata quando ninguém estava olhando.')
c('COM', 'Tá comigo até aqui? Já são quatro regras. Se você tá anotando, ótimo. Se não tá, pausa um segundo e pega um papel, porque agora vem a história que eu te prometi lá no começo.',
  interage={'tipo': 'checkin', 'txt': 'Quatro regras. Tá anotando?'}, conv=True)
# ── 5 a guerra que Maquiavel perdeu (fecha o loop 1) + regras 5 e 6
c('PZ', 'Antes de escrever sobre guerra, Maquiavel tentou fazer uma. Como secretário da república de Florença, ele convenceu a cidade a criar uma milícia de cidadãos, em vez de pagar soldados de aluguel.', cap=cap(5, 'A guerra que ele perdeu'))
c('B', 'A ideia vinha da experiência. Ele tinha visto mercenários que recebiam e não lutavam. Em O Príncipe, nos capítulos doze e treze, ele diz que essas tropas são inúteis e perigosas.', verso='As armas mercenárias e auxiliares são inúteis e perigosas.', ref='O PRÍNCIPE, CAP. XII')
c('SAV', 'A milícia teve um primeiro sucesso: participou do cerco que fez Pisa se render a Florença em 1509. Maquiavel estava orgulhoso. Parecia a prova de que a ideia dele funcionava.')
c('FER', 'Mas em 1512 veio o teste de verdade. Tropas espanholas, enviadas pela liga do papa com Fernando de Aragão, marcharam sobre a cidade de Prato, bem perto de Florença.')
c('CAR', 'A milícia de Maquiavel não aguentou. Os soldados recuaram, Prato foi saqueada, a república de Florença caiu e os Médici voltaram ao poder. Maquiavel perdeu o cargo, e logo depois foi preso.')
c('BPM', 'E aí está a resposta que eu te prometi. Ele quebrou justamente a regra quatro, a do treino. Era uma milícia nova, de cidadãos com pouco preparo, colocada contra soldados experientes de carreira.')
c('MS', 'Ele estava certo na ideia, ter armas próprias. Mas faltou tempo de treino, e a disciplina ainda não pesava mais do que o medo. Anos depois, ele pôs essa lição no papel.')
c('GB', 'Isso é o que eu mais admiro nele: ele não escondeu a derrota. Pegou o próprio fracasso e transformou em regra. Quem escreve sobre o próprio erro ensina mais do que quem só conta vitória.')
c('HAN', 'Agora a regra número cinco: dificilmente é vencido quem sabe conhecer as próprias forças e as forças do inimigo.', verso='Dificilmente é vencido quem sabe conhecer as próprias forças e as do inimigo.', ref=LVII)
c('OST', 'A maioria das derrotas nasce de uma de duas ilusões: achar que você é mais forte do que é, ou achar que o outro é mais fraco do que parece. Prato foi as duas coisas ao mesmo tempo.')
c('EMB', 'Então, antes de entrar numa disputa, responda três perguntas. Quanto tempo e dinheiro você aguenta? Quanto o outro lado aguenta? E quem precisa mais vencer?')
c('C8', 'Essas três respostas dizem mais sobre o resultado do que a coragem de qualquer um dos lados. Quem precisa mais vencer, quase sempre, aceita qualquer acordo primeiro.')
c('ISS2', 'E isso leva direto à regra número seis, sobre os mantimentos. Maquiavel diz que é melhor vencer o inimigo pela fome do que pelo ferro, porque na batalha a sorte pesa mais do que a virtude.',
  verso='É melhor vencer o inimigo pela fome do que pelo ferro; na vitória pelo ferro, a sorte pode mais que a virtude.', ref=LVII)
c('HAN', 'Pensa em Aníbal na Itália. Os romanos tentaram enfrentá-lo de frente e perderam. Então Fábio Máximo, o Contemporizador, mudou o jogo: evitava a batalha e cansava o inimigo. Maquiavel comenta esse caso nos Discursos.', ref='DISCURSOS, LIVRO III, CAP. 9', verso='Fábio procedia com cautela, e o tempo era favorável a esse modo.')
c('DES', 'Hoje, mantimento é caixa, é tempo, é saúde, é gente do seu lado. Muitas disputas não são perdidas para o adversário. São perdidas por falta de fôlego para continuar.')
c('MUL', 'Quem abre um negócio sem reserva para os primeiros meses está indo para a guerra sem pão. Pode ter a melhor ideia do mundo, e mesmo assim perder sem nenhum concorrente encostar nele.')
# ── corredor de sessão (~40%)
c('M', 'Se essas regras já te fizeram pensar diferente sobre alguma disputa da sua vida, segue o canal e abre a playlist Maquiavel na prática. Agora vem a parte em que o plano dá errado.',
  cta='Segue o <b>Raposa e Leão</b><br>e veja a playlist <b>Maquiavel na prática</b>', interage={'tipo': 'segue', 'txt': 'Segue pra próxima regra'}, conv=True)
# ── 6 regras 7 e 8
c('TEM', 'Regra número sete, e essa dói no orgulho: mude o plano assim que perceber que o inimigo já o descobriu.', cap=cap(6, 'Quando o plano vaza'),
  verso='Muda de plano quando perceberes que o inimigo o previu.', ref=LVII)
c('NAU', 'Insistir num caminho que o outro já previu é andar direto para a armadilha. E aqui mora um erro muito humano: a gente se apega ao plano porque gastou tempo e orgulho nele.')
c('AVI', 'Mudar de rota não é fraqueza. Em O Príncipe, no capítulo vinte e cinco, Maquiavel diz que é feliz quem ajusta o modo de agir aos tempos, e infeliz quem não consegue mudar quando os tempos mudam.', verso='É feliz quem combina o seu modo de proceder com a qualidade dos tempos.', ref='O PRÍNCIPE, CAP. XXV')
c('RAI', 'E ele acrescenta, ainda no livro sete: coisas novas e repentinas assustam os exércitos. As conhecidas, quase não assustam. Por isso ele manda acostumar a tropa com pequenos confrontos antes do grande.')
c('POR', 'Na vida real: teste a sua ideia pequeno antes de apostar alto. Um produto com poucos clientes, um projeto com um mês de prazo. O pequeno te ensina sem quebrar você.')
c('LX', 'Regra número oito, uma das mais inteligentes do livro: consulte muitos sobre o que você deveria fazer, e converse com poucos sobre o que você vai fazer de fato.',
  verso='Aconselha-te com muitos sobre o que deves fazer; o que depois decidires fazer, comunica a poucos.', ref=LVII)
c('EMB', 'Ouvir muitos te dá visão. Contar o plano a muitos te tira a surpresa. São duas coisas diferentes, e quase todo mundo confunde as duas.')
c('L', 'Os Médici entendiam isso como ninguém. Ouviam artistas, banqueiros, filósofos, embaixadores. Mas as decisões que importavam eram tomadas num círculo muito pequeno.')
c('MUL', 'Pensa numa empresa que discute uma mudança grande com todo mundo e anuncia antes de estar pronta. O concorrente fica sabendo, o mercado reage, e a vantagem some antes do primeiro passo.')
c('CAS', 'Então, a fórmula: escute aberto, decida fechado. E repara que a regra oito protege a regra dois. É assim que um plano fica escondido sem você precisar desconfiar de todo mundo.')
c('J2', 'Em O Príncipe, no capítulo vinte e três, ele vai além: o governante sábio escolhe poucas pessoas que podem dizer a verdade a ele. E só sobre o que ele perguntar.', verso='O príncipe prudente escolhe homens sábios, e só a eles dá liberdade de lhe dizer a verdade.', ref='O PRÍNCIPE, CAP. XXIII')
c('GB', 'Você conhece alguém que conta todos os planos para todo mundo e depois não entende por que nada sai do papel? Manda esse vídeo para essa pessoa. É um favor que você faz.',
  interage={'tipo': 'manda', 'txt': 'Manda pra quem conta tudo'}, conv=True)
# ── 7 regras 9 e 10
c('ISS', 'Regra número nove: os acidentes repentinos são difíceis de remediar; os que foram pensados antes se resolvem com facilidade.', cap=cap(7, 'O imprevisto e o dinheiro'),
  verso='Os acidentes repentinos com dificuldade se remedeiam; os pensados antes, com facilidade.', ref=LVII)
c('CARA', 'É por isso que os bons estrategistas gastam mais tempo imaginando o que pode dar errado do que sonhando com o que vai dar certo. Parece pessimismo, mas é o contrário. É paz.')
c('CHE', 'Em O Príncipe, ele usa a imagem do rio. A fortuna é como um rio que, quando enche, alaga tudo. Mas, nos tempos calmos, dá para construir diques e barragens.', verso='Nos tempos calmos, os homens podem fazer barragens e diques.', ref='O PRÍNCIPE, CAP. XXV')
c('MAE', 'Um exercício simples, antes de qualquer projeto importante. Escreva o que pode dar errado. Para cada risco, um plano B. E escolha um sinal que te avise cedo de que algo saiu do trilho.')
c('REL', 'Com isso, o acidente repentino vira problema previsto. E problema previsto, como diz a regra, se resolve com facilidade. Você não elimina o risco, mas tira dele o susto.')
c('FI', 'E chegamos à regra número dez, sobre o que realmente sustenta uma disputa. Maquiavel lista quatro coisas: gente, ferro, dinheiro e pão. Esse é o nervo da guerra.')
c('ISS2', 'Mas ele diz que as duas primeiras valem mais, porque gente e ferro encontram dinheiro e pão, e dinheiro e pão não encontram gente e ferro.',
  verso='Homens, ferro, dinheiro e pão são o nervo da guerra; mas os dois primeiros são mais necessários.', ref=LVII)
c('B', 'Nos Discursos, ele repete com outras palavras: o dinheiro não é o nervo da guerra, como diz a opinião comum. Bons soldados acham ouro, mas o ouro nem sempre acha bons soldados.',
  verso='Bons soldados acham o ouro; mas o ouro nem sempre acha bons soldados.', ref='DISCURSOS, LIVRO II, CAP. 10')
c('EMB', 'Para um negócio, isso muda a ordem das prioridades. Primeiro, as pessoas certas e as ferramentas certas. Com gente boa e bons meios, o dinheiro aparece. Com dinheiro e gente errada, ele some rapidinho.')
c('L', 'E para a sua vida também. A sua habilidade e as pessoas leais ao seu lado são o seu ferro e a sua gente. Isso ninguém te tira numa crise. O dinheiro pode ir e voltar.')
c('CES', 'E você, em qual dessas dez regras você mais tropeça hoje? A do plano contado cedo, a do treino ou a da reserva? Escreve o número dela aqui nos comentários.',
  interage={'tipo': 'comenta', 'txt': 'Qual regra você mais quebra?'}, conv=True)
# ── 8 a regra que vale por todas (fecha o loop maior)
c('MOS', 'Agora a promessa maior, a regra que vale por todas as outras. Repara numa coisa: as dez regras têm um ponto em comum. Todas favorecem quem pensa no longo prazo.', cap=cap(8, 'A regra que vale por todas'))
c('BPM', 'Esconder o plano, guardar mantimentos, treinar antes, prever o imprevisto, investir em gente. São atitudes de quem quer vencer a guerra, e não apenas ganhar uma batalha bonita.')
c('MS', 'E por trás de todas está a ideia que Maquiavel defende a vida inteira: ter armas próprias. Não depender da sorte, nem da boa vontade dos outros, para se defender.')
c('BPM', 'Em O Príncipe, no capítulo treze, ele é direto: sem armas próprias, nenhum principado está seguro. Fica inteiramente nas mãos da sorte, porque não tem força para se defender na adversidade.', verso='Sem armas próprias, nenhum principado está seguro; fica todo entregue à fortuna.', ref='O PRÍNCIPE, CAP. XIII')
c('HAN', 'Essa é a regra que vale por todas. Treino é arma própria. Reserva é arma própria. Gente leal é arma própria. Um plano guardado é arma própria. Tudo aponta para o mesmo lugar.')
c('C8', 'Arma própria, hoje, é a sua habilidade, a sua carteira de clientes, a sua reserva de dinheiro, a sua reputação. Se tudo depende de um único chefe, de um único cliente, ou de uma única plataforma, a sua arma é emprestada.')
c('M', 'E quem vive de arma emprestada perde a disputa no dia em que o dono pede a arma de volta. Foi isso que Maquiavel aprendeu em Prato, do jeito mais doloroso possível.')
c('MAE', 'E sabe como o livro termina? Fabrizio, já velho, lamenta que a sorte nunca lhe deu um estado para pôr essas ideias em prática. É Maquiavel falando de si mesmo pela boca do personagem.')
c('REL', 'Mas logo em seguida vem uma frase cheia de esperança. Ele diz que a Itália parece ter nascido para ressuscitar as coisas mortas, como já fez com a poesia, a pintura e a escultura.',
  verso='Esta província parece nascida para ressuscitar as coisas mortas, como se viu na poesia, na pintura e na escultura.', ref=LVII)
c('GB', 'Pensa no peso disso. Um homem que perdeu o cargo, foi preso e viu a sua milícia fugir termina o livro dizendo que o que está morto pode voltar. É a última lição: derrota não é fim de linha.')
c('MS', 'Resumindo as dez: veja quem ganha, esconda o plano, agarre a ocasião, treine, meça as forças, guarde mantimentos, mude o plano descoberto, ouça muitos e decida com poucos, preveja o imprevisto e invista em gente.')
c('ALX', 'E por trás de todas, construa as suas armas próprias. Quem planeja resolve fácil. Quem improvisa paga caro. Isso valia para Florença em 1521 e vale para a sua vida agora.')
c('L', 'No próximo vídeo da playlist Maquiavel na prática, você vai ver o livro de Maquiavel que quase ninguém lê, e que mostra um lado dele que não aparece em O Príncipe. Até a próxima lição, raposa.',
  cta='Próximo: o Maquiavel <b>que ninguém conhece</b>', selo='RAPOSA<br>E LEÃO')

LEG = '''Maquiavel não escreveu só O Príncipe. Em 1521 ele publicou A Arte da Guerra, um manual em forma de conversa que termina com uma lista de regras gerais para vencer disputas. Neste vídeo você conhece as 10 regras mais úteis desse livro, citadas com fidelidade.

E vê como cada uma funciona hoje: no trabalho, nos negócios, numa negociação ou numa briga de família. Mais a guerra que o próprio Maquiavel perdeu em 1512, a regra que ele quebrou e a regra que vale por todas as outras.

⏱️ Capítulos
{CAPITULOS}

📜 Fonte: Nicolau Maquiavel, A Arte da Guerra (livro VII, regras gerais e conclusão); O Príncipe (caps. VI, XII, XIII, XIV, XXI, XXIII e XXV); Discursos sobre a primeira década de Tito Lívio (livro II, cap. 10; livro III, cap. 9).

🦊🦁 Raposa e Leão: Maquiavel e as leis do poder aplicadas à vida real.

▶️ Playlist recomendada: Maquiavel na prática

#Maquiavel #ArteDaGuerra #Estratégia #Negócios #DesenvolvimentoPessoal'''

v = dict(id='longo-04', canal='raposa', formato='longo', titulo='Maquiavel: 10 regras de guerra que ninguém lê', legenda=LEG,
         comentario='📌 Das 10 regras de guerra de Maquiavel, qual você mais quebra hoje: contar o plano cedo, pular o treino ou ficar sem reserva? Continue na playlist Maquiavel na prática ⬇️',
         titulo_tela={'sup': 'RAPOSA E LEÃO', 'txt': 'As regras<br>da guerra', 'dur': 3.2},
         capa={'A': 'Vença sem lutar', 'B': 'Manual esquecido', 'gravA': 'hist/alexander_the_great.jpg', 'gravB': 'maquiavel.jpg'},
         cenas=cenas)
json.dump(v, open(R + '/roteiros/longo-04.json', 'w'), ensure_ascii=False, indent=1)

# checagens
pal = [len(x['txt'].split()) for x in cenas]
print('cenas', len(cenas), 'palavras', sum(pal), 'min/max por cena', min(pal), max(pal))
print('caps', sum('cap' in x for x in cenas), 'versos', sum('verso' in x for x in cenas), 'interage', sum('interage' in x for x in cenas), 'imagens', len({x['gravura'] for x in cenas}))
print('fora 15-45:', [(i, p) for i, p in enumerate(pal) if not 15 <= p <= 45])
print('repetidas seguidas:', [i for i in range(1, len(cenas)) if cenas[i]['gravura'] == cenas[i - 1]['gravura']])
print('faltam no disco:', sorted({x['gravura'] for x in cenas if not os.path.exists(R + '/img/' + x['gravura'])}))
print('título', len(v['titulo'].split()), 'palavras')
