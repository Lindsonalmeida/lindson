import json
C = []
def c(g, m, t, **k): C.append(dict(gravura=g, mov=m, txt=t, **k))

# ABERTURA: gancho + 3 loops
c("borgia.jpg","in","Esse homem pensou em tudo. Montou exército, conquistou cidades, eliminou rivais e preparou um plano para cada desastre possível. E perdeu tudo por causa de uma única pessoa em quem resolveu confiar.")
c("acervo/portrait_of_niccol_machiavelli_by_santi_di_tito.jpg","out","Quem viu isso de perto foi Nicolau Maquiavel. E o que ele aprendeu olhando gente poderosa ganhar e cair virou um livro curto, de vinte e seis capítulos, chamado O Príncipe.")
c("hist/girolamo_savonarola.jpg","esq","Um livro que a Igreja colocou na lista de obras proibidas em 1559 e que fez do nome do autor um xingamento. Mesmo assim, nunca deixou de ser lido por quem manda.")
c("maquiavel.jpg","dir","Hoje eu vou te passar oito lições desse livro. Não para você virar uma pessoa fria. É para você parar de ser pego de surpresa pelas pessoas, no trabalho, nos negócios e dentro de casa.")
c("acervo/castiglione_raffaello.jpg","cima","E no caminho eu te devo três coisas. A primeira: a frase mais famosa ligada a Maquiavel. Você vai descobrir se ele escreveu ou não escreveu aquilo.")
c("acervo/embaixadores_holbein.jpg","in","A segunda: um teste simples, de uma linha, que Maquiavel deixou para você saber se alguém do seu lado trabalha para você ou para ele mesmo.")
c("borgia.jpg","out","E a terceira, a maior: quem é esse homem da primeira cena, e qual foi o erro que derrubou ele. Essa fica para o final, porque é a lição que mais protege você.")
c("acervo/bernardo_bellotto_the_piazza_della_signoria_in_f.jpg","esq","Antes, um minuto sobre o autor. Maquiavel serviu à república de Florença por catorze anos, de 1498 a 1512. Foi secretário e diplomata e negociou com reis, papas e generais.")
c("acervo/prisao_cristo_caravaggio.jpg","dir","Quando os Médici voltaram ao poder, ele perdeu o cargo. Em 1513, acusado de participar de uma conspiração, foi preso e torturado na corda. Saiu sem emprego, sem dinheiro e sem futuro.")
c("maquiavel2.jpg","cima","E foi nesse fundo do poço que ele escreveu. Por isso o livro tem um tom tão direto. Não é sobre como o mundo deveria ser. É sobre como as pessoas agem quando o poder está em jogo.",
  verso="Pareceu-me mais conveniente ir atrás da verdade efetiva das coisas do que da imaginação delas.", ref="O PRÍNCIPE, CAP. XV")

# LIÇÃO 1
c("acervo/hannibal_and_scipio_africanus.jpg","in","Maquiavel diz que existem dois jeitos de lutar. Um é pela lei, que é próprio das pessoas. O outro é pela força, que é próprio dos animais. E como a lei muitas vezes não basta, é preciso conhecer os dois.",
  cap={"sup":"LIÇÃO 1","txt":"Seja raposa e leão"})
c("hist/hannibal.jpg","out","Aí vem a imagem que dá nome a este canal. O leão não se defende das armadilhas. A raposa não se defende dos lobos. Quem só é forte cai na armadilha. Quem só é esperto vira comida de lobo.",
  verso="É preciso ser raposa para conhecer as armadilhas e leão para assustar os lobos.", ref="O PRÍNCIPE, CAP. XVIII")
c("acervo/multidao_bruegel.jpg","esq","Traduzindo para a sua vida. Tem gente que é só leão. Grita, impõe, bate na mesa. Funciona até a primeira pessoa mais esperta aparecer e fazer ela assinar o que não leu.")
c("acervo/romanos_decadencia_couture.jpg","dir","E tem gente que é só raposa. Percebe tudo, entende o jogo, mas não consegue dizer um não. Vê o abuso chegando e mesmo assim deixa passar, para não criar clima.")
c("maquiavel.jpg","cima","Ser raposa, hoje, é ler o contrato antes de assinar, desconfiar da proposta boa demais e reparar em quem só aparece quando precisa de você.")
c("hist/marcus_equestre.jpg","in","Ser leão é dizer não sem pedir desculpa, cobrar o que foi combinado e deixar claro onde fica o seu limite. Uma coisa não anula a outra. Uma protege a outra.")
c("acervo/vercingetorix_royer.jpg","out","Repara numa coisa. Maquiavel não manda escolher um dos dois. Ele manda usar cada um na hora certa. O erro não é ser raposa ou ser leão. O erro é ser um só, o tempo todo.")
c("acervo/castiglione_raffaello.jpg","esq","Pensa no dono de um pequeno negócio. Com o cliente novo, ele é raposa: escuta, pergunta, entende o que a pessoa quer de verdade. Com o cliente que some sem pagar, ele precisa ser leão.")
c("hist/alexander_the_great.jpg","dir","E agora uma pergunta só para você. Hoje, na sua vida, você está mais para raposa ou mais para leão? Responde aí na sua cabeça e guarda, porque as próximas lições vão mexer com essa resposta.",
  interage={"tipo":"checkin","txt":"Raposa ou leão, hoje?"}, conv=True)

# LIÇÃO 2
c("hist/caracalla.jpg","cima","Capítulo dezessete, a pergunta mais famosa do livro: é melhor ser amado ou temido? Quase todo mundo conta a resposta pela metade. E a metade que falta é a mais importante.",
  cap={"sup":"LIÇÃO 2","txt":"Temido, nunca odiado"})
c("cesar.jpg","in","Maquiavel diz que o ideal seria ser as duas coisas. Como é difícil juntar as duas, se for preciso escolher, ele acha mais seguro ser temido. E explica o motivo sem rodeio.")
c("acervo/beijo_judas_giotto.jpg","out","As pessoas, diz ele, rompem o laço do afeto quando isso é conveniente para elas. Já o receio das consequências não falha. Ou seja, o carinho dos outros depende deles. O respeito ao seu limite depende de você.",
  verso="O amor é mantido por um vínculo de obrigação que os homens rompem quando lhes convém; o temor é mantido pelo medo do castigo, que nunca falha.", ref="O PRÍNCIPE, CAP. XVII")
c("acervo/pollice_verso_gerome.jpg","esq","Mas aqui está a metade esquecida. Ele escreve temido, mas nunca odiado. Para ele, ser odiado é um dos maiores perigos que existem. E ensina como evitar o ódio.")
c("hist/commodus.jpg","dir","A regra é não tocar no que é dos outros. Nos bens, na família, na dignidade. Ele chega a dizer uma frase dura: as pessoas esquecem mais depressa a morte do pai do que a perda do patrimônio.",
  verso="Os homens esquecem mais depressa a morte do pai do que a perda do patrimônio.", ref="O PRÍNCIPE, CAP. XVII")
c("acervo/coroacao_napoleao_david.jpg","cima","Leva isso para uma equipe. O chefe que quer ser amigo de todo mundo e nunca cobra nada é atropelado na primeira crise. Ninguém leva a sério a regra que nunca é cumprida.")
c("hist/caracalla.jpg","in","E o chefe que humilha, grita em público e mexe no que é da equipe vira odiado. O ódio é paciente. Espera uma brecha, uma falha, um dia ruim, e cobra a conta.")
c("acervo/embaixadores_holbein.jpg","out","O que funciona é o caminho do meio. Regra clara, cobrança justa, respeito pelo que é de cada um. Isso não gera paixão. Gera uma coisa que dura mais: confiança no seu limite.")
c("lorenzo.jpg","dir","Me conta uma coisa nos comentários. Você já teve um chefe que era só amigo, ou um que era só medo? Qual dos dois te ensinou mais? Quero ler a sua história.",
  interage={"tipo":"comenta","txt":"Chefe amigo ou chefe medo?"}, conv=True)

# LIÇÃO 3
c("hist/arco_severo.jpg","cima","Agora uma lição que quase ninguém conhece. Ela está no capítulo oito, onde Maquiavel fala de quem chegou ao poder pelo crime. E o exemplo dele é um homem de Siracusa chamado Agátocles.",
  cap={"sup":"LIÇÃO 3","txt":"O duro de uma vez só"})
c("acervo/cesar_assassinato_camuccini.jpg","in","Agátocles tomou o poder matando os senadores e os ricos da cidade. Maquiavel conta isso e faz questão de julgar: matar cidadãos e trair amigos não pode ser chamado de virtude. Dá poder, mas não dá glória.",
  verso="Pode-se conquistar o poder desse modo, mas não a glória.", ref="O PRÍNCIPE, CAP. VIII")
c("acervo/romanos_decadencia_couture.jpg","out","Então por que ele fala disso? Porque quer entender uma coisa: por que alguns governantes duros se seguraram no poder e outros caíram rápido. A resposta dele vale até hoje, longe de qualquer crime.")
c("hist/bonfire_of_the_vanities.jpg","esq","A diferença estava no jeito de fazer o que era duro. Quem faz o duro todo de uma vez, e depois para, consegue virar a página. Quem espalha a dureza aos poucos vive cercado de ressentimento.")
c("acervo/multidao_bruegel.jpg","dir","E o bem é o contrário. O benefício deve ser dado aos poucos, para ser sentido e lembrado. Benefício entregue todo de uma vez é esquecido em pouco tempo.",
  verso="As ofensas devem ser feitas todas juntas; os benefícios, pouco a pouco, para que sejam mais saboreados.", ref="O PRÍNCIPE, CAP. VIII")
c("acervo/embaixadores_holbein.jpg","cima","Pensa numa empresa que precisa cortar gastos. Se corta um pouco todo mês, durante um ano, a equipe vive doze meses de medo. Ninguém trabalha direito esperando a próxima notícia ruim.")
c("maquiavel.jpg","in","Agora pensa no líder que faz o ajuste necessário de uma vez, explica o porquê e diz claramente que acabou. A dor é parecida. O desgaste é muito menor.")
c("acervo/castiglione_raffaello.jpg","out","Na família também. A conversa difícil que você adia e solta em pedaços, um pouco em cada almoço de domingo, machuca mais do que a conversa inteira, feita uma vez, com calma e respeito.")
c("lorenzo.jpg","esq","E repara como essa lição muda o jeito de enxergar as pessoas. Quem te dá tudo de uma vez, no começo, pode estar comprando a sua confiança. Quem te trata bem aos poucos e sempre costuma ser mais firme.")
c("acervo/portrait_of_niccol_machiavelli_by_santi_di_tito.jpg","dir","Se essas três primeiras lições já mudaram alguma coisa na sua cabeça, segue o Raposa e Leão e abre a playlist O Príncipe explicado. Porque agora vem a lição da frase mais famosa.",
  cta="Segue o <b>Raposa e Leão</b><br>e veja a playlist <b>O Príncipe explicado</b>", interage={"tipo":"segue","txt":"Segue pras próximas cinco"}, conv=True)

# LIÇÃO 4 + fecha loop 1
c("acervo/coroacao_napoleao_david.jpg","cima","Volta ao capítulo dezoito. Maquiavel escreve que as pessoas, em geral, julgam mais pelos olhos do que pelas mãos. Porque ver, todo mundo vê. Tocar, só alguns conseguem.",
  cap={"sup":"LIÇÃO 4","txt":"O que você parece"})
c("acervo/leao_x_raffaello.jpg","in","Em outras palavras: quase todos vão conhecer a sua imagem. Pouquíssimos vão conhecer quem você é de verdade. E é pela imagem que a maioria vai decidir se confia em você.",
  verso="Todos veem o que pareces, poucos sentem o que és.", ref="O PRÍNCIPE, CAP. XVIII")
c("acervo/castiglione_raffaello.jpg","out","Isso não é um convite para ser falso. É um aviso para quem é bom e esconde isso. Você pode ser excelente no que faz e, se parece amador, a maioria nunca vai descobrir.")
c("hist/moses.jpg","esq","Pensa no profissional caprichoso que atende pelo celular sem foto, sem endereço, sem resposta no horário combinado. Ele perde o cliente para alguém pior, só porque o outro parece mais confiável.")
c("acervo/beijo_judas_giotto.jpg","dir","E tem o lado da defesa. Se todo mundo julga pela aparência, quem quer te enganar também sabe disso. O golpista caprichou na aparência antes de caprichar em qualquer outra coisa.")
c("maquiavel2.jpg","cima","Então use as duas mãos. Cuide do que você mostra, para o seu valor ser visto. E desconfie do que os outros mostram, até ter tocado no que eles entregam de fato.")
c("hist/girolamo_savonarola.jpg","in","E aqui eu fecho a primeira promessa. A frase mais famosa ligada a Maquiavel é os fins justificam os meios. Você já ouviu isso mil vezes, sempre com o nome dele junto.")
c("acervo/portrait_of_niccol_machiavelli_by_santi_di_tito.jpg","out","Essa frase, com essas palavras, não aparece em nenhum livro dele. Nem no Príncipe, nem nos Discursos, nem na Arte da Guerra. É um resumo que colaram nele depois.")
c("hist/pope_alexander_vi.jpg","esq","O que ele escreveu, neste mesmo capítulo dezoito, é outra coisa. Nas ações dos homens, e mais ainda dos governantes, onde não existe tribunal acima deles, o que se olha é o resultado.",
  verso="Nas ações de todos os homens, e sobretudo dos príncipes, onde não há tribunal a que recorrer, olha-se o resultado.", ref="O PRÍNCIPE, CAP. XVIII")
c("acervo/multidao_bruegel.jpg","dir","Isso é uma observação sobre como o povo julga, não uma licença para fazer qualquer coisa. E faz todo sentido com a lição de hoje: as pessoas olham o que você entregou, não o que você pretendia.")

# LIÇÃO 5 + fecha loop 2
c("lorenzo.jpg","in","Capítulo vinte e dois. Maquiavel diz que a primeira forma de avaliar a inteligência de um governante é olhar as pessoas que ele tem em volta. Se são capazes e leais, ele é sábio.",
  cap={"sup":"LIÇÃO 5","txt":"Diga quem te cerca"})
c("acervo/leao_x_raffaello.jpg","out","Se não são, a primeira falha dele foi justamente essa escolha. Ou seja, as pessoas não te julgam só pelo que você faz. Te julgam por quem você deixa ficar perto.",
  verso="A primeira conjectura que se faz da inteligência de um senhor é ver os homens que ele tem ao redor.", ref="O PRÍNCIPE, CAP. XXII")
c("acervo/embaixadores_holbein.jpg","esq","E aqui eu fecho a segunda promessa: o teste de uma linha. Quando você perceber que a pessoa pensa mais nela do que em você, e busca o próprio proveito em tudo, ela nunca vai ser alguém de confiança.")
c("maquiavel.jpg","dir","É só isso. Repara nas pequenas coisas. Na hora de dividir o mérito, de quem é o nome que aparece? Na hora do problema, quem some primeiro? Nas decisões, o conselho dela sempre puxa vantagem para o lado dela?")
c("acervo/castiglione_raffaello.jpg","cima","E Maquiavel é justo também com o outro lado. Ele diz que, para manter alguém bom e leal, é preciso honrar essa pessoa, dividir as honras e não deixar faltar nada. Lealdade se cuida.")
c("hist/marcus_aurelius.jpg","in","Esse teste vale para sócio, para funcionário, para amigo de negócio. Se você quiser usar ele depois, salva este vídeo. É o tipo de coisa que a gente esquece justo quando mais precisa.",
  interage={"tipo":"salva","txt":"Salva o teste de uma linha"}, conv=True)
c("acervo/julio_ii_raffaello.jpg","out","No capítulo seguinte, o vinte e três, vem o perigo que mora dentro de casa: os bajuladores. Maquiavel diz que as cortes vivem cheias deles, porque todo mundo gosta de ouvir que está certo.")
c("hist/pope_julius_ii.jpg","esq","E a solução dele é curiosa. Não é ouvir todo mundo, porque quem deixa qualquer um falar qualquer coisa perde o respeito. É escolher poucas pessoas sérias e dar a elas liberdade para dizer a verdade.")
c("borgia.jpg","dir","Mais uma frase que vale ouro. Bons conselhos nascem da prudência de quem pede, e não o contrário. Quem não sabe pensar sozinho não é salvo nem pelo melhor conselheiro do mundo.",
  verso="Os bons conselhos, venham de onde vierem, nascem da prudência do príncipe, e não a prudência do príncipe dos bons conselhos.", ref="O PRÍNCIPE, CAP. XXIII")
c("acervo/coroacao_napoleao_david.jpg","cima","Então olha para a sua roda. Tem alguém aí que te diz a verdade quando dói? Se ninguém nunca discorda de você, talvez não seja porque você está sempre certo.")

# LIÇÃO 6
c("acervo/hannibal_and_scipio_africanus.jpg","in","Capítulo vinte e um. Quando duas pessoas ou dois grupos brigam perto de você, a tentação é não escolher nenhum lado. Parece a escolha mais segura. Maquiavel diz que quase sempre é a mais perigosa.",
  cap={"sup":"LIÇÃO 6","txt":"Em cima do muro"})
c("acervo/albrecht_altdorfer_schlacht_bei_issus_alte_pinak.jpg","out","O raciocínio é simples. Quem vencer não vai querer como amigo alguém que não ajudou na hora difícil. E quem perder não vai te acolher, porque você não estendeu a mão. Você fica sozinho dos dois lados.")
c("hist/ferdinand_ii_of_aragon.jpg","esq","E ele observa uma coisa sobre quem pede o quê. Quem não é seu amigo vai pedir que você fique neutro. Quem é seu amigo vai pedir que você se posicione.",
  verso="Quem não é teu amigo pedirá a tua neutralidade; quem é teu amigo pedirá que te declares.", ref="O PRÍNCIPE, CAP. XXI")
c("acervo/vercingetorix_royer.jpg","dir","Os indecisos, escreve ele, para fugir do perigo de hoje, quase sempre escolhem ficar neutros, e quase sempre se arruínam. Adiar a escolha não apaga o risco. Só deixa a conta para depois.")
c("acervo/multidao_bruegel.jpg","cima","Agora, cuidado para não entender errado. Isso não quer dizer entrar em toda briga de grupo de família. Quer dizer que, quando a escolha é inevitável, ficar no muro custa mais caro do que decidir.")
c("acervo/embaixadores_holbein.jpg","in","Pensa numa briga entre dois sócios de uma empresa, e você é o funcionário de confiança dos dois. Agradar os dois para sempre é impossível. Escolher com critério, e com honestidade, é a única saída que dura.")

# LIÇÃO 7
c("acervo/smk_flod_ruysdael.jpg","esq","Penúltima lição, capítulo vinte e cinco. Maquiavel enfrenta uma pergunta antiga: quanto da nossa vida depende da sorte? E a resposta dele é mais animadora do que parece.",
  cap={"sup":"LIÇÃO 7","txt":"A sorte é um rio"})
c("acervo/smk_flod_bjerg_vernet.jpg","dir","Ele diz que a sorte decide talvez metade das nossas ações. A outra metade, ou quase isso, fica nas nossas mãos. Nem tudo é destino. Nem tudo é mérito.",
  verso="A fortuna é árbitro de metade das nossas ações, mas deixa a outra metade, ou quase, para nós.", ref="O PRÍNCIPE, CAP. XXV")
c("acervo/smk_stormflod_vernet.jpg","cima","Aí vem a imagem do rio. Quando o rio enche, arrasta árvores, casas e plantações. Todo mundo foge, ninguém consegue segurar a água naquela hora.")
c("acervo/smk_flod_klipper_doughty.jpg","in","Mas, quando o tempo está calmo, dá para construir diques e barreiras. Aí, quando a cheia vem, a água corre por um canal ou chega com bem menos força. O estrago depende do que você fez antes.")
c("acervo/smk_uvejr_gaard_juel.jpg","out","Na vida real, o dique é a reserva de dinheiro guardada no mês bom. É aprender uma habilidade nova antes de perder o emprego. É cuidar das amizades quando você ainda não precisa de nada.")
c("acervo/smk_storm_bakhuizen.jpg","esq","E tem um aviso escondido nesse capítulo. Maquiavel diz que muita gente se dá bem num tempo e se dá mal no outro, só porque não muda o próprio jeito quando os tempos mudam.")
c("acervo/smk_efter_regn_skovgaard.jpg","dir","Ou seja, o que te salvou ontem pode te afundar amanhã. O jeito de ser que te fez crescer pode ser exatamente o que precisa mudar agora. Sorte também é saber ler o tempo.")
c("acervo/smk_uvejr_dietrich.jpg","cima","E é aqui que entra o homem da primeira cena. Porque ele fez exatamente isso: construiu diques para todas as enchentes que conseguiu imaginar. Menos uma.")

# LIÇÃO 8 + fecha loop maior
c("borgia.jpg","in","O nome dele é César Bórgia, filho do papa Alexandre Sexto. É o personagem que Maquiavel mais estuda no capítulo sete, e um dos poucos que ele chega a apresentar como modelo de príncipe novo.",
  cap={"sup":"LIÇÃO 8","txt":"Ferida velha, favor novo"})
c("hist/pope_alexander_vi.jpg","out","Com o apoio do pai, Bórgia conquistou cidades na Romanha e montou tropas próprias. Maquiavel conheceu ele de perto, em missões como diplomata de Florença. Viu como ele planejava cada passo.")
c("acervo/beijo_judas_giotto.jpg","esq","Mas tudo dependia de uma coisa: ter um papa amigo. Em 1503, o pai dele morreu. E Bórgia, que tinha se preparado para isso, estava ele mesmo gravemente doente na mesma época.")
c("acervo/portrait_of_niccol_machiavelli_by_santi_di_tito.jpg","dir","Maquiavel conta que o próprio Bórgia disse a ele, no dia em que o novo papa foi eleito, que tinha pensado em tudo o que poderia acontecer na morte do pai, menos em estar ele mesmo à beira da morte.")
c("acervo/julio_ii_raffaello.jpg","cima","Só que o erro fatal veio depois. O novo papa foi o cardeal Giuliano della Rovere, que virou Júlio Segundo. E Bórgia apoiou essa eleição. Um homem que ele e a família tinham ofendido por anos.")
c("hist/pope_julius_ii.jpg","in","Bórgia acreditou que favores novos iam apagar ofensas antigas. Que, ajudando o rival agora, o passado ia ficar para trás. Não ficou. Em pouco tempo ele perdeu as terras, foi preso e nunca mais se levantou.")
c("acervo/prisao_cristo_caravaggio.jpg","out","A conclusão de Maquiavel é uma das frases mais úteis do livro inteiro, e é por ela que eu guardei essa história para o fim.",
  verso="Quem acredita que, nas grandes personagens, os benefícios novos fazem esquecer as ofensas antigas se engana.", ref="O PRÍNCIPE, CAP. VII")
c("acervo/castiglione_raffaello.jpg","esq","Traduzindo: um presente hoje não apaga uma humilhação de ontem. A pessoa que você magoou de verdade pode sorrir, aceitar sua ajuda e continuar guardando aquilo. Só esperando a hora.")
c("lorenzo.jpg","dir","E isso protege você dos dois lados. Primeiro, cuidado com quem você ofende, porque favor nenhum garante perdão. Segundo, quando você magoar alguém, não tente comprar a paz. Peça desculpa de verdade e repare o que for possível.")
c("hist/marcus_aurelius.jpg","cima","E na hora de confiar, olha para trás antes de olhar para o presente. O que essa pessoa já viveu com você? Existe uma ferida ali que nunca foi conversada? O presente bonito não responde a essa pergunta.")
c("acervo/multidao_bruegel.jpg","in","Pensa em alguém que precisava ouvir isso hoje, alguém prestes a confiar em quem já machucou ou foi machucado por ela. Manda este vídeo para essa pessoa. Pode evitar um erro de Bórgia.",
  interage={"tipo":"manda","txt":"Manda pra quem vai confiar"}, conv=True)

# FECHO
c("acervo/bernardo_bellotto_the_piazza_della_signoria_in_f.jpg","out","Recapitulando as oito lições. Seja raposa e leão. Seja respeitado, nunca odiado. Faça o duro de uma vez e o bem aos poucos. Cuide do que você parece e desconfie do que os outros parecem.")
c("acervo/embaixadores_holbein.jpg","esq","Olhe quem te cerca e faça o teste de uma linha. Não fique no muro quando a escolha for inevitável. Construa diques no tempo bom. E nunca acredite que favor novo apaga ferida velha.")
c("maquiavel2.jpg","dir","Maquiavel não te ensina a ser mau. Ele te ensina a não ser ingênuo. E quem entende como as pessoas agem pode escolher jogar limpo sem ser passado para trás.")
c("acervo/portrait_of_niccol_machiavelli_by_santi_di_tito.jpg","cima","No próximo vídeo da playlist O Príncipe explicado, você vai ver o livro inteiro, do capítulo um ao vinte e seis, sem enrolação. Até a próxima lição, raposa.",
  cta="Próximo: <b>O Príncipe sem enrolação</b><br>Até a próxima lição, raposa", selo="RAPOSA<br>E LEÃO")

caps = [x['cap']['txt'] for x in C if 'cap' in x]
r = dict(id="longo-01", canal="raposa", formato="longo",
 titulo="8 lições de Maquiavel para enxergar as pessoas",
 legenda=("O Príncipe, de Maquiavel, foi proibido pela Igreja e virou sinônimo de maldade. Mas quem lê de verdade encontra outra coisa: um manual para não ser enganado pelas pessoas no trabalho, nos negócios e na família.\n\n"
  "Neste vídeo você aprende 8 lições de Maquiavel: a raposa e o leão, ser temido sem ser odiado, o duro de uma vez, a aparência, o teste de quem te cerca, os bajuladores, o perigo de ficar em cima do muro, a sorte como um rio e o erro que derrubou César Bórgia.\n\n"
  "⏱️ Capítulos\n{CAPITULOS}\n\n"
  "📜 Fonte: Nicolau Maquiavel, O Príncipe, caps. VII, VIII, XV, XVII, XVIII, XXI, XXII, XXIII e XXV.\n\n"
  "🦊🦁 Raposa e Leão: Maquiavel e as leis do poder aplicadas à vida real.\n\n"
  "▶️ Playlist recomendada: O Príncipe explicado\n\n"
  "#Maquiavel #OPríncipe #InteligênciaEmocional #RelacionamentosNoTrabalho #DesenvolvimentoPessoal"),
 comentario="📌 Das 8 lições, qual você precisava ter aprendido antes: o teste de uma linha ou a de que favor novo não apaga ferida velha? Continue na playlist O Príncipe explicado ⬇️",
 titulo_tela={"sup":"RAPOSA E LEÃO","txt":"8 lições para<br>enxergar pessoas","dur":3.2},
 capa={"A":"Pensou em tudo","B":"Quem te cerca?","gravA":"borgia.jpg","gravB":"acervo/castiglione_raffaello.jpg"},
 cenas=C)
json.dump(r, open('/home/user/lindson/conteudo/youtube/raposa-e-leao/roteiros/longo-01.json','w'), ensure_ascii=False, indent=1)
w = [len(x['txt'].split()) for x in C]
print(len(C), sum(w), min(w), max(w), len(caps), sum('verso' in x for x in C), sum('interage' in x for x in C), len({x['gravura'] for x in C}))
for i in range(1, len(C)):
    if C[i]['gravura'] == C[i-1]['gravura']: print('REPETE', i, C[i]['gravura'])

# troca pelas obras do acervo que existem (Wikimedia bloqueada): mesmo tema, sem repetir a vizinha
import os
T = {10:'acervo/batalha_ostia_raffaello.jpg',13:'acervo/sermao_bruegel.jpg',16:'acervo/batalha_ponte_milvio_raffaello.jpg',22:'hist/pope_alexander_vi.jpg',
     24:'acervo/carlos_viii_florenca_bezzuoli.jpg',29:'acervo/batalha_ponte_milvio_raffaello.jpg',30:'acervo/carlos_viii_florenca_bezzuoli.jpg',
     38:'acervo/sermao_bruegel.jpg',57:'acervo/sandro_botticelli_giuliano_de_medici_gem_ldegale.jpg',58:'acervo/batalha_ostia_raffaello.jpg',61:'hist/arco_severo.jpg'}
for i, g in T.items():
    C[i]['gravura_original'] = C[i]['gravura']; C[i]['gravura'] = g
json.dump(r, open('/home/user/lindson/conteudo/youtube/raposa-e-leao/roteiros/longo-01.json','w'), ensure_ascii=False, indent=1)
R = '/home/user/lindson/conteudo/youtube/raposa-e-leao/img/'
print('faltam', [x['gravura'] for x in C if not os.path.exists(R + x['gravura'])])
print('repete', [i for i in range(1, len(C)) if C[i]['gravura'] == C[i-1]['gravura']], 'distintas', len({x['gravura'] for x in C}))
