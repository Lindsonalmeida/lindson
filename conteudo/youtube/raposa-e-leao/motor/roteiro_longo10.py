"""Gera roteiros/longo-10.json (Raposa e Leão, formato novo 16-20 min)."""
import json
P = 'acervo/portrait_of_niccol_machiavelli_by_santi_di_tito.jpg'
BEL = 'acervo/bernardo_bellotto_the_piazza_della_signoria_in_f.jpg'
GIU = 'acervo/botticelli_giuliano_de_medici_accademia_carrara.jpg'
GIU2 = 'acervo/sandro_botticelli_giuliano_de_medici_gem_ldegale.jpg'
ISS = 'acervo/albrecht_altdorfer_schlacht_bei_issus_alte_pinak.jpg'
ISS2 = 'acervo/the_battle_of_alexander_at_issus_by_albrecht_alt.jpg'
ZAMA = 'acervo/hannibal_and_scipio_africanus.jpg'
FI = 'acervo/ferdinand_of_aragon_isabella_of_castile.jpg'
JUD = 'acervo/beijo_judas_giotto.jpg'
CAS = 'acervo/castiglione_raffaello.jpg'
GER = 'acervo/jean_l_on_g_r_me_the_death_of_caesar_walters_378.jpg'
LEO = 'acervo/leao_x_raffaello.jpg'
JUL = 'acervo/julio_ii_raffaello.jpg'
EMB = 'acervo/embaixadores_holbein.jpg'
MUL = 'acervo/multidao_bruegel.jpg'
PRI = 'acervo/prisao_cristo_caravaggio.jpg'
GRA = 'acervo/rendicao_granada_pradilla.jpg'
COR = 'acervo/coroacao_napoleao_david.jpg'
OST = 'acervo/batalha_ostia_raffaello.jpg'
MIL = 'acervo/batalha_ponte_milvio_raffaello.jpg'
M, M2, LOR, BOR, CES = 'maquiavel.jpg', 'maquiavel2.jpg', 'lorenzo.jpg', 'borgia.jpg', 'cesar.jpg'
ALE, JU2, SAV, FER, FOG = 'hist/pope_alexander_vi.jpg', 'hist/pope_julius_ii.jpg', 'hist/girolamo_savonarola.jpg', 'hist/ferdinand_ii_of_aragon.jpg', 'hist/bonfire_of_the_vanities.jpg'
ALX, MEQ, MAU, HAN, MOI, ARC, CAR, COM = ('hist/alexander_the_great.jpg', 'hist/marcus_equestre.jpg', 'hist/marcus_aurelius.jpg', 'hist/hannibal.jpg',
                                         'hist/moses.jpg', 'hist/arco_severo.jpg', 'hist/caracalla.jpg', 'hist/commodus.jpg')
MOV = ['in', 'out', 'esq', 'dir', 'cima']

C = []
def c(g, txt, **k):
    C.append(dict(gravura=g, mov=MOV[len(C) % 5], txt=txt, **k))

# ABERTURA — começa dentro da cela, sem contexto
c(PRI, "Fevereiro de 1513. Um homem de quarenta e três anos está pendurado pelos braços numa prisão de Florença. Ele não sabe, mas o livro mais famoso sobre poder vai nascer dessa dor.")
c(M, "O nome dele é Nicolau Maquiavel. Até poucos meses antes, ele era um dos homens mais bem informados da Europa. Agora não tem cargo, não tem salário e está sendo torturado.")
c(BEL, "Hoje eu te conto a vida dele do começo ao fim, sem lenda e sem enfeite. Como ele subiu, como caiu e o que fez no fundo do poço.")
c(BOR, "E eu deixo três perguntas abertas pelo caminho. A primeira: o que César Bórgia confessou para Maquiavel, cara a cara, no dia em que perdeu tudo. Ele mesmo registrou isso no livro.")
c(MOI, "A segunda: um livro que o pai de Maquiavel ganhou em troca de trabalho, quando ele era criança. Esse livro volta na história anos depois, e de um jeito bonito.")
c(MAU, "E a terceira, a maior: o que aconteceu com Maquiavel no dia em que o sonho da vida dele finalmente se realizou. Essa eu guardo para o último capítulo.")

# PARTE 1
c(FOG, "Maquiavel nasceu em Florença, em 3 de maio de 1469. A família tinha nome antigo, mas pouco dinheiro. O pai, Bernardo, era advogado e vivia apertado.",
  cap={"sup": "PARTE 1", "txt": "O menino e o livro do pai"})
c(MOI, "Só que o Bernardo tinha uma paixão: livros. E livro naquela época era caro. Então ele fazia de tudo para ler, até trabalho em troca de um volume.")
c(BEL, "Nos registros que o pai deixou, aparece um caso. Ele montou o índice dos lugares citados numa obra de Tito Lívio, o historiador de Roma. Como pagamento, ficou com um exemplar.")
c(ARC, "Guarda esse livro na cabeça. A história de Roma contada por Tito Lívio. Foi nessa casa simples, cheia de papel, que o menino cresceu ouvindo falar de cônsules e de batalhas.")
c(LOR, "Enquanto isso, quem mandava em Florença era Lorenzo de Médici, o Magnífico. Oficialmente a cidade era uma república. Na prática, a família de banqueiros decidia quase tudo.")
c(MEQ, "Sobre a juventude de Maquiavel, quase não há documento. Os historiadores discutem até onde ele estudou. O que se sabe é que lia latim e conhecia bem os autores antigos.")
c(CAS, "E repara numa coisa: ele não nasceu nobre, não nasceu rico e não tinha padrinho poderoso. Tudo o que ele conseguiu veio de leitura, observação e trabalho.")

# PARTE 2
c(FOG, "Em 1492, Lorenzo morre. Dois anos depois, o rei Carlos Oitavo, da França, entra na Itália com um exército enorme. E o filho de Lorenzo, Piero, entrega fortalezas sem lutar.",
  cap={"sup": "PARTE 2", "txt": "A fogueira na praça"})
c(BEL, "O povo de Florença se revolta, e os Médici são expulsos da cidade em 1494. Quem ocupa o vazio não é um general. É um frade.")
c(SAV, "Girolamo Savonarola. Pregava contra o luxo, anunciava castigos de Deus e enchia a catedral. Por alguns anos, foi a voz mais poderosa de Florença.")
c(FOG, "Os seguidores dele queimavam espelhos, joias, roupas finas e pinturas em grandes fogueiras na praça. Maquiavel tinha uns vinte e poucos anos e assistia a tudo.")
c(ALE, "Mas Savonarola atacou também o papa Alexandre Sexto. Foi excomungado, perdeu apoio na cidade e, em maio de 1498, foi enforcado e queimado na mesma praça das fogueiras.")
c(M2, "Maquiavel tirou dali uma das ideias mais duras do livro que escreveria depois. Quem só tem palavras, quando o povo deixa de acreditar, não tem como segurá-lo.")
c(MOI, "Ele compara Savonarola a Moisés. Moisés tinha força para manter as leis que trouxe. O frade só tinha a pregação. Por isso, os profetas armados venceram e os desarmados se arruinaram.",
  verso="Todos os profetas armados venceram, e os desarmados se arruinaram.", ref="O PRÍNCIPE, CAP. VI")
c(CAS, "Na sua vida, isso quer dizer uma coisa simples. Boa intenção sem estrutura não se sustenta. Ideia sem dinheiro guardado, sem gente e sem processo cai na primeira crise.")

# PARTE 3
c(BEL, "Poucas semanas depois da fogueira de Savonarola, em junho de 1498, Maquiavel é eleito secretário da Segunda Chancelaria de Florença. Ele tinha vinte e nove anos.",
  cap={"sup": "PARTE 3", "txt": "O secretário que via tudo"})
c(EMB, "Logo depois, vira também secretário dos Dez, o conselho que cuidava da guerra e da diplomacia. Era um cargo de funcionário, não de chefe. Mas por ele passava tudo.")
c(FI, "Ele escrevia cartas, relatórios e ordens. E, principalmente, viajava. Em 1500, foi mandado à corte do rei Luís Doze, da França.")
c(M, "Lá ele aprendeu uma lição amarga. Os franceses davam pouca importância a Florença, porque a cidade não tinha exército próprio e pagava para ser protegida.")
c(MUL, "Tá comigo até aqui? Guarda isso: quem depende dos outros para se defender não é levado a sério. Essa frase vai voltar daqui a pouco, e com muita força.",
  interage={"tipo": "checkin", "txt": "Tá comigo nessa viagem?"}, conv=True)
c(BOR, "Em 1502, vem a missão que mais marcou a vida dele. Florença manda Maquiavel até César Bórgia, filho do papa, que estava conquistando cidades na Romanha.")
c(ALE, "Bórgia era jovem, rápido e sem medo. Tinha o dinheiro e as tropas do pai, Alexandre Sexto, e usava tudo isso para montar um Estado próprio no centro da Itália.")
c(BOR, "Maquiavel passou meses perto dele, escrevendo relatórios para Florença. Viu o duque enganar inimigos, dividir alianças e agir quando ninguém esperava.")
c(CAR, "Na Romanha, Bórgia tinha posto um governador duro, Ramiro de Lorqua, para acabar com a bagunça. Funcionou. Mas o povo passou a odiar o governador.")
c(CES, "Então, numa manhã de dezembro de 1502, o corpo de Ramiro apareceu cortado em dois na praça de Cesena. Maquiavel conta que o espetáculo deixou o povo satisfeito e assustado ao mesmo tempo.",
  verso="Aquele espetáculo deixou o povo ao mesmo tempo satisfeito e estupefato.", ref="O PRÍNCIPE, CAP. VII")
c(M2, "Atenção aqui: Maquiavel não está aplaudindo crueldade. Ele está descrevendo o que viu. O livro dele é um relatório, não um manual de maldade.")
c(JUL, "Em 1503, Alexandre Sexto morre. Pouco depois, o novo papa é Júlio Segundo, inimigo antigo dos Bórgia. E Maquiavel está em Roma acompanhando a eleição.")
c(BOR, "E aqui eu fecho a primeira pergunta. Naquele dia, o próprio Bórgia contou a Maquiavel que tinha pensado em tudo para quando o pai morresse. Menos numa coisa.")
c(HAN, "Ele não imaginou que, na hora em que o pai morresse, ele mesmo estaria doente, à beira da morte. A fortuna pegou o duque no único ponto que ele não previu.",
  verso="Pensara em tudo o que podia acontecer com a morte do pai, menos que ele mesmo estaria à morte.", ref="O PRÍNCIPE, CAP. VII")
c(JU2, "Em poucos meses, o homem mais temido da Itália perdeu tudo. Maquiavel, que antes admirava a energia dele, passou a descrevê-lo como alguém que caiu por confiar no inimigo errado.")
c(ALX, "A lição para você: não existe plano que cubra tudo. Por isso, quem é esperto deixa sempre uma reserva, uma saída, um plano para o dia em que o imprevisto chegar.")

# PARTE 4
c(FI, "Agora volta comigo para aquela frase da França: quem depende dos outros não é levado a sério. Maquiavel cansou de ver Florença pagar soldados que fugiam na hora da luta.",
  cap={"sup": "PARTE 4", "txt": "O exército de cidadãos"})
c(ISS, "Os mercenários, dizia ele, são desunidos, ambiciosos e infiéis. Corajosos entre amigos, covardes diante do inimigo. Na paz te roubam, e na guerra te deixam sozinho.",
  verso="Os mercenários são desunidos, ambiciosos, sem disciplina e infiéis.", ref="O PRÍNCIPE, CAP. XII")
c(M, "Então ele propôs algo que parecia loucura para um funcionário: Florença devia ter um exército de cidadãos, gente da própria terra, treinada e chamada quando precisasse.")
c(MEQ, "Ele tinha apoio de Piero Soderini, eleito em 1502 chefe da república por toda a vida. Soderini confiava em Maquiavel, e os inimigos zombavam dele por isso.")
c(BEL, "A milícia saiu do papel. Em fevereiro de 1506, os primeiros soldados desfilaram em Florença. Era o projeto da vida de Maquiavel.")
c(OST, "E em 1509 veio a prova. Pisa, que tinha se rebelado contra Florença anos antes, se rendeu depois de um cerco em que a milícia ajudou. Foi o maior momento da carreira dele.")
c(MAU, "Se até aqui você já entendeu mais sobre Maquiavel do que em anos de frase solta na internet, segue o canal e abre a playlist A vida de Maquiavel. Porque agora vem a queda.",
  cta="Segue o <b>Raposa e Leão</b><br>e veja a playlist <b>A vida de Maquiavel</b>", interage={"tipo": "segue", "txt": "Segue pra ver a queda"}, conv=True)
c(JUL, "Só que a política mudou de novo. O papa Júlio Segundo montou uma liga contra a França. E Florença, aliada dos franceses, ficou do lado perdedor.")
c(FER, "Em agosto de 1512, tropas espanholas da liga, do rei Fernando de Aragão, atacaram Prato, cidade vizinha. A milícia de Maquiavel estava lá. Não segurou.")
c(MIL, "Prato foi saqueada com uma violência que assustou a Itália inteira. Florença entrou em pânico, Soderini fugiu e os Médici voltaram para a cidade depois de dezoito anos.")
c(M2, "O exército de cidadãos falhou no teste mais importante. E o homem que tinha inventado esse exército ficou exposto, sem padrinho, nas mãos dos antigos inimigos.")

# PARTE 5
c(BEL, "Em 7 de novembro de 1512, Maquiavel é demitido. Dias depois, é proibido de sair do território de Florença por um ano e precisa pagar uma fiança alta, que amigos ajudam a bancar.",
  cap={"sup": "PARTE 5", "txt": "A corda"})
c(GIU, "Ele tenta se aproximar dos novos donos do poder. Escreve até para Giuliano de Médici. Mas, para os Médici, ele era o braço direito de Soderini. Gente de confiança do outro lado.")
c(JUD, "Em fevereiro de 1513, descobrem uma conspiração para matar os Médici. Com um dos conspiradores, Pietro Paolo Boscoli, acharam uma lista de nomes. O de Maquiavel estava lá.")
c(PRI, "Não há prova de que ele soubesse do plano. Mesmo assim, foi preso e passou pela corda: braços amarrados nas costas, corpo erguido e solto de uma vez.")
c(CAR, "Num soneto que escreveu da cela para Giuliano de Médici, ele conta seis puxões da corda nos ombros, correntes nas pernas e piolhos do tamanho de borboletas.",
  verso="Tenho, Giuliano, um par de grilhões nas pernas e seis puxões de corda nas costas.", ref="SONETO A GIULIANO DE MÉDICI, 1513")
c(JU2, "Boscoli e o companheiro Agostino Capponi foram executados. Maquiavel, nos versos, fala das orações que ouvia de madrugada pelos condenados. Ele não confessou nada, porque não tinha o que confessar.")
c(LEO, "A saída veio por acaso. Em março de 1513, o cardeal Giovanni de Médici foi eleito papa com o nome de Leão Décimo. Florença festejou e soltou presos. Maquiavel entre eles.")
c(M, "Ele saiu vivo, mas destruído. Quarenta e três anos, ombros machucados, sem emprego, sem dinheiro e malvisto pelos únicos que podiam dar trabalho a ele.")
c(MUL, "E agora te pergunto de verdade: se você perdesse o emprego hoje e ficasse meses parado, o que faria com esse tempo? Escreve aí. Quero ler a sua resposta.",
  interage={"tipo": "comenta", "txt": "O que você faria parado?"}, conv=True)

# PARTE 6
c(MEQ, "Sem saída em Florença, ele vai morar numa pequena propriedade da família em Sant'Andrea in Percussina, perto de San Casciano, a poucas horas da cidade.",
  cap={"sup": "PARTE 6", "txt": "Os tordos e a roupa de corte"})
c(EMB, "O melhor retrato desses meses está nas cartas para o amigo Francesco Vettori, embaixador de Florença em Roma. Os dois trocavam cartas sobre política como quem joga xadrez.")
c(M2, "Numa carta de abril de 1513, ele confessa algo que diz tudo. Não sabia falar de seda, nem de lã, nem de lucro e prejuízo. A sorte só tinha deixado para ele falar do Estado.",
  verso="Não sei raciocinar nem sobre seda, nem sobre lã, nem sobre lucros e perdas; cabe-me raciocinar sobre o Estado.", ref="CARTA A VETTORI, 9/4/1513")
c(MUL, "E em 10 de dezembro de 1513 vem a carta mais famosa. Ele descreve os dias. Até pouco antes, caçava tordos com visgo. Agora acorda com o sol e vai a um bosque que mandou cortar.")
c(MOI, "Fica um tempo com os lenhadores, que sempre tinham alguma briga para contar. Depois senta perto de uma fonte com um livro de Dante, de Petrarca ou de Ovídio debaixo do braço.")
c(FOG, "Na hora do almoço, come com a família o pouco que a terra dá. Depois vai à taverna da estrada e passa a tarde jogando cartas e gamão com o açougueiro, o moleiro e dois forneiros.")
c(COM, "E ele não se faz de santo. Conta que as brigas por uma moeda eram tão altas que se ouviam de San Casciano. Ele mesmo diz que se mete entre aqueles piolhos para tirar o mofo do cérebro.")
c(CAS, "Mas aí chega a noite. Ele tira a roupa suja do dia, veste as roupas que usava nas cortes e entra no escritório. E lá, conversa com os antigos pelos livros.")
c(M, "Ele diz que, nessas quatro horas, não sente tédio, esquece os problemas, não teme a pobreza nem a morte. Se alimenta do único alimento que é só dele, e para o qual nasceu.",
  verso="Me alimento daquele alimento que só é meu, e para o qual nasci.", ref="CARTA A VETTORI, 10/12/1513")
c(ISS2, "E conta que, como Dante dizia que não existe ciência sem guardar o que se entendeu, ele anotou o que aprendeu nessas conversas. E escreveu um livrinho sobre os principados.")
c(BOR, "Esse livrinho é O Príncipe. Todo o material estava ali: a França, a fogueira de Savonarola, os meses ao lado de Bórgia, a milícia, Prato e a própria corda.")
c(CAS, "Repara: ele não escreveu para desabafar. Escreveu para provar que sabia. Na mesma carta, diz que os quinze anos estudando o Estado ele não passou dormindo nem jogando.",
  verso="Os quinze anos em que estive estudando a arte do Estado não os dormi nem os joguei.", ref="CARTA A VETTORI, 10/12/1513")
c(MEQ, "E fala da pobreza sem vergonha. Diz que quem foi fiel e bom por quarenta e três anos não muda de natureza, e que a pobreza dele era a testemunha da sua honestidade.")
c(M2, "Se essa carta mexeu com você, salva esse vídeo. Ele é para assistir de novo no dia em que a vida te deixar parado e você precisar lembrar o que fazer com a noite.",
  interage={"tipo": "salva", "txt": "Salva pro dia difícil"}, conv=True)
c(ALX, "Na prática, a roupa de corte é isso: um horário fixo, sem celular, para estudar quem já resolveu o problema que você enfrenta. E transformar o estudo em algo que outro pode ver.")

# PARTE 7
c(LOR, "O plano era claro. Dar o livro a um Médici para voltar a trabalhar. Ele pensou em Giuliano. Com a morte dele, em 1516, a dedicatória acabou indo para Lorenzo, neto do Magnífico.",
  cap={"sup": "PARTE 7", "txt": "O livro que não abriu a porta"})
c(GIU2, "No fim da dedicatória, tem uma frase que pouca gente nota. Ele pede que Lorenzo, lá do alto, olhe às vezes para baixo e veja quanta má sorte o autor vinha suportando.",
  verso="Se Vossa Magnificência olhar destes lugares baixos, conhecerá quanto suporto uma grande e contínua malignidade da fortuna.", ref="O PRÍNCIPE, DEDICATÓRIA")
c(M, "Não funcionou. O cargo não veio. Não existe nenhum registro de que Lorenzo tenha dado atenção ao livro. Maquiavel continuou no campo, sem posto.")
c(BEL, "Mas ele não parou. Começou a frequentar os encontros nos jardins da família Rucellai, os Orti Oricellari, onde jovens de Florença discutiam história e política.")
c(ARC, "E lá ele lia e comentava, capítulo por capítulo, a história de Roma de Tito Lívio. Lembra do livro que o pai ganhou montando um índice? Ele voltou.")
c(MOI, "Daquelas conversas nasceram os Discursos sobre a primeira década de Tito Lívio, a obra mais longa de Maquiavel. O livro que entrou na casa como pagamento virou a base do pensamento do filho.")
c(MAU, "E fecho a segunda pergunta. Nos Discursos, Maquiavel defende a república, a liberdade e as leis. Quem só conhece O Príncipe acha que ele amava tiranos. Não é bem assim.",
  verso="Não sem razão se compara a voz de um povo à de Deus.", ref="DISCURSOS, LIVRO I, CAP. LVIII")
c(COM, "Ele também virou escritor de sucesso, mas por outro caminho. A peça A Mandrágora, uma comédia ácida sobre enganação, fez Florença inteira rir. Foi a obra mais popular dele em vida.")
c(ISS, "Em 1521, publicou A Arte da Guerra, defendendo de novo o exército de cidadãos. Foi uma das poucas obras políticas dele impressas enquanto ele estava vivo.")
c(EMB, "O Príncipe, não. Ele circulou em cópias feitas à mão entre amigos. Só foi impresso em 1532, cinco anos depois da morte do autor.")
c(CAS, "Pensa nisso: o livro que o fez famoso para sempre não deu a ele nem um emprego. O resultado que importa às vezes chega muito depois do esforço.")

# PARTE 8
c(LEO, "Aos poucos, os Médici aceitaram usar o talento dele. Em 1520, o cardeal Giulio de Médici encomendou a Maquiavel uma história de Florença, com salário.",
  cap={"sup": "PARTE 8", "txt": "A república volta, e ele não"})
c(JUL, "Giulio virou papa Clemente Sétimo, e Maquiavel entregou a ele em Roma os livros das Histórias Florentinas. Depois, foi encarregado de cuidar das muralhas de Florença.")
c(ISS, "Em maio de 1527, o exército do imperador Carlos Quinto saqueia Roma. O papa Médici fica cercado. E em Florença, sem o apoio de Roma, os Médici são expulsos de novo.")
c(BEL, "A república voltou. Exatamente o regime que Maquiavel serviu por catorze anos, que ele defendeu nos Discursos e pelo qual ele foi torturado.")
c(M2, "Agora eu fecho a maior pergunta. No dia em que o sonho se realizou, Maquiavel esperava voltar ao antigo cargo. Afinal, ele era o homem da república.")
c(GIU, "Mas os novos governantes lembraram outra coisa: nos últimos anos, ele tinha trabalhado para os Médici. Para eles, Maquiavel era suspeito. E o posto ficou com outro.")
c(JUD, "Os Médici desconfiaram dele por ser republicano. A república desconfiou dele por ter servido aos Médici. Ele ficou sem lugar nos dois lados.")
c(M, "Poucas semanas depois, em 21 de junho de 1527, Nicolau Maquiavel morreu em Florença, aos cinquenta e oito anos. Foi enterrado na igreja de Santa Croce.")
c(MEQ, "Dois meses antes, numa carta a Vettori, ele tinha escrito uma frase que mostra quem ele era. Disse que amava a sua pátria mais do que a própria alma.",
  verso="Amo a minha pátria mais do que a alma.", ref="CARTA A VETTORI, 16/4/1527")
c(MUL, "Conhece alguém que perdeu o emprego, fechou um negócio ou levou uma rasteira e acha que a vida acabou? Manda esse vídeo. Talvez essa pessoa precise da roupa de corte hoje.",
  interage={"tipo": "manda", "txt": "Manda pra quem caiu"}, conv=True)
c(FOG, "Séculos depois, colocaram no túmulo dele uma frase em latim: para um nome tão grande, nenhum elogio basta. O homem demitido virou o mais lido de Florença.")
c(CAS, "Resumindo a vida dele em lições: aprenda observando quem está acima. Tenha armas próprias. Planeje a reserva para o imprevisto. E use a pior fase para estudar.")
c(ALX, "E a última, que ele aprendeu da pior forma: quem serve a todos os lados sem ter base própria pode acabar sem lugar em nenhum. Construa a sua base.")
c(P, "No próximo vídeo da playlist A vida de Maquiavel, a gente abre O Príncipe capítulo por capítulo, sem enrolação. Até a próxima lição, raposa.",
  cta="Próximo: <b>O Príncipe explicado</b><br>Até a próxima lição, raposa", selo="RAPOSA<br>E LEÃO")

V = dict(
    id='longo-10', canal='raposa', formato='longo',
    titulo='Preso e torturado: como Maquiavel escreveu O Príncipe',
    legenda=("Maquiavel foi demitido, preso e torturado em 1513, e foi nesse fundo do poço que escreveu O Príncipe. Neste vídeo você conhece a vida de Nicolau Maquiavel do começo ao fim: o menino pobre de Florença, a fogueira de Savonarola, os meses ao lado de César Bórgia, o exército de cidadãos e a queda.\n\n"
             "A corda na prisão, as noites com a roupa de corte, a carta a Vettori, os Discursos sobre Tito Lívio e o fim irônico quando a república voltou. E o que a vida dele ensina para quem perdeu o emprego, o negócio ou a posição e precisa recomeçar.\n\n"
             "⏱️ Capítulos\n{CAPITULOS}\n\n"
             "📜 Fonte: Nicolau Maquiavel, O Príncipe (dedicatória e caps. VI, VII e XII); Discursos sobre a primeira década de Tito Lívio (livro I, cap. LVIII); cartas a Francesco Vettori de 9/4/1513, 10/12/1513 e 16/4/1527; soneto a Giuliano de Médici (1513).\n\n"
             "🦊🦁 Raposa e Leão: Maquiavel e as leis do poder aplicadas à vida real.\n\n"
             "▶️ Playlist recomendada: A vida de Maquiavel\n\n"
             "#Maquiavel #OPríncipe #HistóriaDaItália #Recomeço #Florença"),
    comentario='📌 Se você perdesse tudo amanhã, qual seria a sua "roupa de corte": o que você estudaria toda noite? Continue na playlist A vida de Maquiavel ⬇️',
    titulo_tela={"sup": "RAPOSA E LEÃO", "txt": "Preso, torturado<br>e eterno", "dur": 3.2},
    capa={"A": "Preso. Torturado.", "B": "Fundo do poço", "gravA": M2, "gravB": P},
    cenas=C)
if __name__ == '__main__':
    import sys
    out = sys.argv[1] if len(sys.argv) > 1 else '/home/user/lindson/conteudo/youtube/raposa-e-leao/roteiros/longo-10.json'
    json.dump(V, open(out, 'w'), ensure_ascii=False, indent=1)
    ws = [len(x['txt'].split()) for x in C]
    print(len(C), 'cenas', sum(ws), 'palavras', 'min/max', min(ws), max(ws), 'imgs', len({x['gravura'] for x in C}),
          'int', sum('interage' in x for x in C), 'cap', sum('cap' in x for x in C), 'verso', sum('verso' in x for x in C))
    for i in range(1, len(C)):
        if C[i]['gravura'] == C[i - 1]['gravura']: print('REPETIDA', i, C[i]['gravura'])
    print('cta em', [round(i / len(C) * 100) for i, x in enumerate(C) if 'cta' in x])
