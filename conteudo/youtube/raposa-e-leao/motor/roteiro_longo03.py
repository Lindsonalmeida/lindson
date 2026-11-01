"""Raposa e Leão longo-03 (César Bórgia) refeito no formato novo (16-20 min), a partir de longos/03/roteiro.json (o original fica lá como histórico).
python3 roteiro_longo03.py -> ../roteiros/longo-03.json"""
import json, os
D = os.path.dirname(os.path.abspath(__file__)); R = os.path.join(D, '..')
B, AV, J2, J2M = 'borgia.jpg', 'hist/pope_alexander_vi.jpg', 'acervo/julio_ii_raffaello.jpg', 'hist/pope_julius_ii.jpg'
M, M2, MP = 'maquiavel.jpg', 'maquiavel2.jpg', 'acervo/portrait_of_niccol_machiavelli_by_santi_di_tito.jpg'
L, LX, CAS, EMB = 'lorenzo.jpg', 'acervo/leao_x_raffaello.jpg', 'acervo/castiglione_raffaello.jpg', 'acervo/embaixadores_holbein.jpg'
PZ, REL, MUL = 'acervo/bernardo_bellotto_the_piazza_della_signoria_in_f.jpg', 'hist/bonfire_of_the_vanities.jpg', 'acervo/multidao_bruegel.jpg'
GRA = 'acervo/carlos_viii_florenca_bezzuoli.jpg'  # Pradilla bloqueado na Wikimedia
_, COR, JUD, PRI = None, 'acervo/coroacao_napoleao_david.jpg', 'acervo/beijo_judas_giotto.jpg', 'acervo/prisao_cristo_caravaggio.jpg'
CES, CASS, CMG = 'cesar.jpg', 'acervo/cesar_assassinato_camuccini.jpg', 'acervo/cesar_assassinato_camuccini.jpg'  # Gérôme bloqueado na Wikimedia
VER = 'acervo/the_battle_of_alexander_at_issus_by_albrecht_alt.jpg'  # Royer bloqueado na Wikimedia
_, ZAM, ISS = None, 'acervo/hannibal_and_scipio_africanus.jpg', 'acervo/albrecht_altdorfer_schlacht_bei_issus_alte_pinak.jpg'
FER, FI, SAV, GIU = 'hist/ferdinand_ii_of_aragon.jpg', 'acervo/ferdinand_of_aragon_isabella_of_castile.jpg', 'hist/girolamo_savonarola.jpg', 'acervo/botticelli_giuliano_de_medici_accademia_carrara.jpg'
OST, MIL, ROM, CAR = 'acervo/batalha_ostia_raffaello.jpg', 'acervo/batalha_ponte_milvio_raffaello.jpg', 'acervo/romanos_decadencia_couture.jpg', 'hist/caracalla.jpg'
POL, MEQ = 'acervo/batalha_ponte_milvio_raffaello.jpg', 'hist/marcus_equestre.jpg'  # Gérôme bloqueado na Wikimedia

C = []  # (gravura, txt, extras)
def c(g, t, **x): C.append((g, t, x))
cap = lambda n, t: {'cap': {'sup': f'LIÇÃO {n}', 'txt': t}}
v = lambda t, ref: {'verso': t, 'ref': ref}

# ABERTURA: gancho + 3 loops (Cesena, a frase dita a Maquiavel, o único erro)
c(B, "Ele tinha o dinheiro do papa, um exército, um ducado inteiro e a admiração de Maquiavel. Em poucos meses, perdeu tudo. E não foi por falta de inteligência.")
c(AV, "César Bórgia é o homem que Maquiavel mais usa como exemplo em O Príncipe. Para muita gente, ele é o príncipe do livro em carne e osso.")
c(MP, "Só que o mesmo Maquiavel que elogia Bórgia mostra, no mesmo capítulo, o ponto exato em que ele errou. E esse erro, você talvez esteja cometendo agora.")
c(MUL, "Nesta história tem três coisas que eu vou te entregar. A primeira: o que o povo de uma cidade encontrou numa manhã de dezembro, no meio da praça.")
c(EMB, "A segunda: uma frase que o próprio Bórgia disse a Maquiavel, olho no olho, quando tudo já estava desmoronando. Maquiavel anotou e colocou no livro.")
c(J2, "E a terceira, a mais importante: o único erro, segundo Maquiavel, que derrubou tudo. Ele cabe numa linha. Mas essa eu só abro no final.")

# LIÇÃO 1
c(REL, "Antes de qualquer conquista, a gente precisa entender de onde esse homem veio. Porque a força dele tinha um dono, e esse dono não era ele.", **cap(1, 'O filho do papa'))
c(AV, "César nasceu por volta de 1475, filho de Rodrigo Bórgia, um cardeal espanhol muito rico. Em 1492, Rodrigo foi eleito papa e escolheu o nome de Alexandre sexto.")
c(COR, "Um ano depois, o pai fez César cardeal, ainda moço. Era o caminho mais seguro para o poder na Itália da época. Mas César não queria a batina.")
c(CAR, "Em 1497, o irmão dele, Juan, foi assassinado em Roma e o corpo apareceu no rio Tibre. Muita gente desconfiou de César. Prova nunca houve, e os historiadores discordam até hoje.")
c(GRA, "Em 1498, César fez algo raríssimo: largou o cargo de cardeal. No mesmo ano, o rei da França, Luís doze, deu a ele o título de duque de Valentinois.")
c(CES, "Por isso a Itália passou a chamá-lo de Valentino. E ao nome dele ficou ligado um lema antigo: ou César, ou nada. Ou tudo, ou coisa nenhuma.")
c(FI, "Agora repara no cenário. A Itália era um quebra-cabeça de cidades e senhores pequenos, sempre brigando, e com reis estrangeiros da França e da Espanha entrando para mandar.")
c(B, "Num lugar assim, um jovem com o dinheiro do pai papa, o apoio do rei da França e nenhuma vergonha de ambição tinha uma chance que quase ninguém tem.")
c(M2, "Guarda essa imagem: um rapaz com tudo nas mãos, mas quase nada que fosse realmente dele. É exatamente isso que Maquiavel vai cobrar mais adiante.")

# LIÇÃO 2
c(ZAM, "Em 1499, o exército francês desceu para a Itália e tomou Milão. César foi junto. E com tropas emprestadas do rei, começou a sua própria guerra.", **cap(2, 'Subir com a força dos outros'))
c(MIL, "O alvo era a Romanha, uma região no centro da Itália que pertencia, no papel, à Igreja. Na prática, cada cidade tinha um senhorzinho que fazia o que queria.")
c(SAV, "Ímola caiu. Em Forlì, ele encontrou Caterina Sforza, uma senhora valente que resistiu dentro da fortaleza. No começo de 1500, a fortaleza caiu e ela foi presa.")
c(REL, "Maquiavel lembra dela no capítulo vinte, quando fala de fortalezas. Os muros não a salvaram, porque o povo de Forlì não estava do lado dela. Muro sem gente leal não segura nada.")
c(OST, "Depois vieram Pesaro, Rímini e Faenza. Cidade por cidade, o pedaço de mapa foi mudando de cor. Em 1501, o pai deu a ele o título de duque da Romanha.")
c(MP, "Parece uma subida perfeita. Mas Maquiavel olha para isso com outro olho. Para ele, Bórgia subiu do jeito mais perigoso que existe.", **v('Quem se torna príncipe só pela sorte chega com pouco esforço, mas se mantém com muito.', 'O PRÍNCIPE, CAP. VII'))
c(L, "No capítulo sete, ele explica: quem ganha o poder pela sorte e pelas armas dos outros depende de duas coisas que não controla. A vontade de quem deu e a sorte.")
c(VER, "E os sinais vieram rápido. As tropas dos Orsini, que lutavam para ele, andaram devagar no ataque a Bolonha. E o rei da França mandou ele parar quando quis entrar na Toscana.")
c(MEQ, "Ou seja: o exército não era dele, a permissão não era dele e o dinheiro também não. Bórgia mandava em tudo, desde que os outros deixassem.")
c(CAS, "E Maquiavel conta que Bórgia percebeu isso. Decidiu não depender mais das armas e da sorte de ninguém. Foi aí que o jogo dele mudou.")
c(MUL, "Traz para a sua vida. Um emprego que depende de um só chefe. Uma empresa que vive de um só cliente. Um projeto que só anda com o dinheiro de outra pessoa.")
c(M2, "Tudo isso é poder emprestado. Funciona muito bem, até o dia em que o dono pede de volta. Guarda essa ideia, porque ela volta no fim com força total.",
  interage={'tipo': 'checkin', 'txt': 'Poder emprestado. Tá comigo?'}, conv=True)

# LIÇÃO 3: quebra de padrão — Maquiavel dentro da corte
c(EMB, "Agora uma virada nesta história. Quem conta tudo isso não leu sobre Bórgia em livro. Maquiavel esteve frente a frente com ele, mais de uma vez.", **cap(3, 'Maquiavel na corte do duque'))
c(PZ, "Em junho de 1502, Bórgia tomou a cidade de Urbino de surpresa. Florença ficou com medo de ser a próxima e mandou dois enviados conversar com ele.")
c(MP, "Um deles era o bispo Francesco Soderini. O outro, o secretário Nicolau Maquiavel, então com uns trinta e poucos anos.")
c(B, "Nos relatórios para Florença, Maquiavel descreve um homem rápido, reservado e muito confiante, que falava pouco dos próprios planos e agia antes que os outros entendessem.")
c(ISS, "No outono daquele ano, Maquiavel volta, agora sozinho, e passa meses acompanhando a corte de Bórgia. Foram meses de cartas quase diárias para o governo de Florença.")
c(GIU, "Na mesma época, Leonardo da Vinci trabalhava para Bórgia como engenheiro militar e desenhou um mapa de Ímola. Muitos acreditam que os dois se conheceram ali, mas nenhum documento prova.")
c(CES, "Imagina a cena: um dos maiores artistas do Renascimento e o pensador político mais famoso da época, na mesma corte, servindo ou observando o mesmo homem perigoso.")
c(M, "O que importa é isto: grande parte do que está em O Príncipe nasceu de quem viu de perto. Por isso, quando Maquiavel fala de Bórgia, ele fala como testemunha.",
  **v('Não sei de lição melhor para um príncipe novo do que o exemplo das ações do duque.', 'O PRÍNCIPE, CAP. VII'))

# LIÇÃO 4: Cesena (fecha o loop 1)
c(MUL, "E agora eu fecho a primeira promessa: a manhã de dezembro na praça. Para entender, a gente volta para a Romanha logo depois da conquista.", **cap(4, 'A manhã na praça de Cesena'))
c(POL, "Os antigos senhores tinham deixado a região sem lei. Era roubo, briga e abuso para todo lado. O povo não confiava em ninguém.")
c(CAR, "Bórgia escolheu um homem duro e rápido, Ramiro de Lorqua, e deu a ele poder total. Em pouco tempo, a Romanha estava em ordem.")
c(PZ, "Só que a ordem veio no chicote. E Bórgia sabia que todo aquele rigor tinha criado ódio. Um ódio que, cedo ou tarde, ia sobrar para ele.")
c(CAS, "Primeiro, ele montou um tribunal no meio da província, com um juiz respeitado, e cada cidade com o seu advogado. A justiça passou a ter rosto e regra.")
c(PRI, "Depois, no fim de 1502, numa manhã, o povo de Cesena encontrou Ramiro morto e exposto na praça, com uma faca ensanguentada ao lado.")
c(ROM, "Repara que Bórgia não escondeu nada. Ele fez questão de que todo mundo visse. O recado não era só sobre Ramiro. Era para a cidade inteira.")
c(B, "Maquiavel conta isso no capítulo sete sem enfeite nenhum. E descreve a reação do povo com duas palavras que dizem tudo.",
  **v('Aquele espetáculo deixou o povo, ao mesmo tempo, satisfeito e atordoado.', 'O PRÍNCIPE, CAP. VII'))
c(REL, "A mensagem era clara: se houve crueldade, não veio do duque, veio do ministro. A culpa ficou com Ramiro. O alívio, com Bórgia.")
c(LX, "Maquiavel transforma isso em regra no capítulo dezenove: o líder deixa para os outros o que gera ódio e faz pessoalmente o que gera gratidão.",
  **v('O príncipe deve deixar para os outros o que traz ódio e fazer ele mesmo o que traz gratidão.', 'O PRÍNCIPE, CAP. XIX'))
c(M2, "Agora, cuidado. Não é para você imitar a crueldade. É para enxergar o mecanismo e se proteger dele, porque ele ainda acontece todo dia.")
c(EMB, "Sabe aquele gestor que manda você dar a notícia ruim e depois aparece para dar a boa? Ou a empresa que joga a culpa no funcionário da ponta?")
c(MUL, "É Cesena em versão moderna. Quando você for o Ramiro da história, perceba cedo. E quando você liderar, assuma a parte pesada, em vez de terceirizar o desgaste.",
  interage={'tipo': 'comenta', 'txt': 'Já te usaram de escudo?'}, conv=True)

# LIÇÃO 5: armas próprias e crueldade (meio: CTA ~40%)
c(MIL, "Lembra que Bórgia decidiu não depender mais da força dos outros? Pois é aqui que ele faz isso de verdade.", **cap(5, 'As próprias armas'))
c(ZAM, "No capítulo treze, Maquiavel mostra os três degraus de Bórgia. Primeiro, tropas auxiliares do rei da França. Depois, soldados contratados, os Orsini e os Vitelli.")
c(B, "Por fim, homens dele, pagos por ele, leais a ele. E Maquiavel faz uma observação que vale para qualquer líder.",
  **v('Ele nunca foi tão respeitado como quando todos viram que era o dono das próprias armas.', 'O PRÍNCIPE, CAP. XIII'))
c(PZ, "Ele também conquistou os nobres de Roma que seguiam os Orsini e os Colonna. Deu salário, cargo e honra. Em pouco tempo, eles eram dele, e não mais das famílias rivais.")
c(MUL, "Repara na diferença. Antes, ele pedia favor. Agora, ele pagava salário. Quem vive de favor obedece quando quer. Quem faz parte da casa defende a casa.")
c(MP, "E aqui vem a parte que deixa muita gente desconfortável. No capítulo dezessete, Maquiavel fala da fama de cruel que Bórgia tinha.",
  **v('César Bórgia era tido como cruel; mas essa crueldade pôs ordem na Romanha e a uniu em paz.', 'O PRÍNCIPE, CAP. XVII'))
c(SAV, "E compara com Florença, que, para não parecer cruel, deixou a cidade de Pistoia se destruir em brigas internas. A falsa bondade, diz ele, matou mais gente.")
c(CAS, "Traduzindo para hoje: o líder que nunca corrige ninguém para não parecer duro acaba deixando o time se destruir. Firmeza na hora certa protege mais do que omissão.",
  cta='Segue o <b>Raposa e Leão</b><br>e veja a playlist <b>Personagens do poder</b>', interage={'tipo': 'segue', 'txt': 'Segue pra ver a queda'}, conv=True)
c(LX, "Se essa história está te ajudando a enxergar o poder de outro jeito, segue o canal, porque daqui para a frente ela fica ainda mais tensa.")

# LIÇÃO 6: Senigália
c(OST, "Em outubro de 1502, os próprios capitães de Bórgia se reuniram num castelo chamado Magione. Eram os Orsini, Vitellozzo Vitelli e outros. E juraram derrubá-lo.", **cap(6, 'A armadilha de Senigália'))
c(VER, "Os conspiradores tomaram fortalezas e Urbino se revoltou. Bórgia estava sozinho com pouca tropa. A reação óbvia seria atacar com raiva. Ele fez o contrário.")
c(L, "Conseguiu ajuda da França, reorganizou seus homens e, ao mesmo tempo, abriu conversa com os traidores. Ofereceu acordo, como se nada tivesse acontecido.")
c(JUD, "Maquiavel conta que ele soube disfarçar tão bem o que pensava que os Orsini aceitaram a paz. Ganharam dinheiro, roupas e cavalos de presente.")
c(GRA, "E em 31 de dezembro de 1502, ele chamou os chefes para um encontro na cidade de Senigália. Eles foram, confiantes.")
c(PRI, "Lá dentro, Bórgia mandou prendê-los. Vitellozzo Vitelli e Oliverotto da Fermo foram estrangulados naquela mesma noite. Pouco depois, outros dois Orsini tiveram o mesmo fim.")
c(ROM, "E esse Oliverotto tem uma história própria no capítulo oito. Ele tinha tomado a cidade de Fermo matando o tio e os principais cidadãos num banquete que ele mesmo ofereceu.")
c(CMG, "Um ano depois, caiu na armadilha de alguém mais frio do que ele. Maquiavel separa aqui crueldade bem usada da mal usada, e isso é muito mal entendido.",
  **v('Crueldades bem usadas são as feitas de uma vez, por necessidade, e que depois não se repetem.', 'O PRÍNCIPE, CAP. VIII'))
c(AV, "E tem um detalhe curioso. No capítulo dezoito, o capítulo da raposa e do leão, o exemplo de enganador que Maquiavel escolhe não é César. É o pai dele.",
  **v('Alexandre sexto nunca fez outra coisa senão enganar, e sempre achou quem se deixasse enganar.', 'O PRÍNCIPE, CAP. XVIII'))
c(B, "Em Senigália, o filho mostrou as duas faces do capítulo dezoito. A raposa, para perceber a armadilha e preparar outra. O leão, para agir quando a hora chegou.")
c(M2, "A lição de proteção aqui é simples: quem traiu uma vez e volta sorrindo com presente não mudou de lado só porque o clima ficou bom.")
c(EMB, "Na sua vida, isso quer dizer prestar atenção em atitudes, não em palavras. Paz verdadeira vem com fatos. E desconfiança não é paranoia quando a pessoa já mostrou quem é.")

# LIÇÃO 7: os quatro planos e a queda (fecha o loop 2)
c(COR, "Agora Bórgia estava no auge. E ele sabia que tudo dependia de um homem velho: o pai, o papa. Então montou um plano para o dia em que ele morresse.", **cap(7, 'O dia que ele não previu'))
c(MP, "Maquiavel lista quatro peças desse plano no capítulo sete. Primeira: acabar com as famílias dos senhores que ele tinha tirado do poder, para nenhum novo papa usá-las contra ele.")
c(PZ, "Segunda: ganhar os nobres de Roma, para segurar o próximo papa. Terceira: ter o maior número possível de cardeais do lado dele, porque são eles que elegem o papa.")
c(ISS, "Quarta: conquistar tanto território antes da morte do pai que pudesse aguentar o primeiro golpe sozinho. Quando o pai morreu, três já estavam feitas e a quarta, quase.")
c(MUL, "Parece um plano completo, né? Repara: ele previu a morte do pai. Previu inimigos, cardeais, Roma. Mas faltou um cenário. E esse cenário chegou em agosto de 1503.")
c(AV, "Em 18 de agosto de 1503, o papa Alexandre sexto morreu. E ao mesmo tempo César caiu gravemente doente, de cama, sem conseguir agir.")
c(CES, "E aqui eu fecho a segunda promessa. Meses depois, em Roma, o próprio Bórgia disse a Maquiavel a frase que resume a vida dele.",
  **v('Ele me disse que tinha pensado em tudo para a morte do pai, menos que ele mesmo estaria à beira da morte.', 'O PRÍNCIPE, CAP. VII'))
c(M, "Pensa no peso disso. O homem mais calculista da Itália planejou para o dia ruim. Só não planejou para o pior dia, quando duas coisas dão errado juntas.")
c(CMG, "O papa seguinte, Pio terceiro, durou menos de um mês. Bórgia, ainda fraco, precisava de um papa amigo na nova eleição. E foi aí que ele fez o que fez.")
c(J2, "Ele apoiou o cardeal Giuliano della Rovere, um velho inimigo da família Bórgia, que tinha sido prejudicado e perseguido durante o papado de Alexandre.")
c(J2M, "Della Rovere prometeu coisas, Bórgia acreditou, e em novembro de 1503 ele virou o papa Júlio segundo. Maquiavel estava em Roma nessa época, como enviado de Florença.")
c(FER, "O resto foi rápido. Bórgia foi preso, perdeu as fortalezas da Romanha e acabou mandado para a Espanha, nas terras de Fernando de Aragão, em 1504.")
c(FI, "Em 1506, fugiu do castelo de Medina del Campo. Foi para Navarra, o reino do cunhado, e lutou por ele. Em março de 1507, morreu numa emboscada perto de Viana.")
c(B, "Tinha por volta de trinta e um anos. O homem do lema ou César ou nada terminou sem ducado, sem exército e sem o pai.")
c(M2, "Respira um pouco aqui. Pensa em tudo que você construiu hoje. Se a pessoa ou a coisa em que você mais se apoia sumisse amanhã, o que ficaria de pé?",
  interage={'tipo': 'salva', 'txt': 'Salva: qual é o seu plano B?'}, conv=True)

# LIÇÃO 8: o único erro (loop maior) e o que levar
c(MP, "Agora a terceira promessa, a maior. Maquiavel elogiou quase tudo em Bórgia. Disse que não saberia o que criticar nas ações dele. Quase tudo.", **cap(8, 'O único erro'))
c(J2, "Porque no final do capítulo sete ele aponta um erro só. Não foi a doença, nem a morte do pai. Foi a escolha do papa: Bórgia ajudou a eleger alguém que ele já tinha ferido.")
c(AV, "Repara na ironia. Em Senigália, ele foi a raposa que enxergou a armadilha dos outros. Na eleição do papa, faltou justamente a raposa. A armadilha estava na cara, e ele entrou.")
c(LX, "Ele podia ter barrado a eleição. Com os cardeais espanhóis do lado dele, tinha força para isso. Mas confiou na promessa de quem tinha motivo para se vingar.")
c(J2M, "E aí vem a linha que eu te prometi lá no começo, a frase que fecha a história do Valentino.",
  **v('Quem acredita que benefícios novos fazem os grandes esquecerem ofensas antigas se engana.', 'O PRÍNCIPE, CAP. VII'))
c(B, "Maquiavel completa: o duque errou nessa escolha, e ela foi a causa da sua ruína final. Anos de trabalho, perdidos numa única confiança mal colocada.",
  **v('Errou o duque nessa escolha, e ela foi a causa da sua ruína final.', 'O PRÍNCIPE, CAP. VII'))
c(EMB, "Traz para hoje. Um sócio que você passou para trás e agora promete parceria. Um colega que você humilhou e agora vai decidir a sua promoção.")
c(MUL, "Uma gentileza nova não apaga uma ferida antiga. Não é vingança, é memória. E entregar o seu futuro na mão de quem tem motivo para te prejudicar é repetir Bórgia.")
c(CAS, "E o outro lado também vale, e é o mais bonito: se você feriu alguém, não espere que um presente resolva. Repare de verdade, ou não deposite nela o seu destino.")
c(J2M, "E vale para você também: confiança se dá aos poucos, para quem mostrou com fatos que merece. Não para quem só tem a promessa e um motivo guardado para te cobrar.")
c(M, "Uma última coisa, para ser justo com Maquiavel. Admirar a habilidade de alguém não é aprovar o que ele fez. No capítulo oito, ele mesmo deixa isso claro.",
  **v('Não se pode chamar de virtude matar cidadãos, trair amigos, não ter fé nem piedade.', 'O PRÍNCIPE, CAP. VIII'))
c(SAV, "Esse tipo de caminho, diz ele, pode dar poder, mas não dá glória. Bórgia é estudado justamente por mostrar a força e o limite do cálculo frio.")
c(PZ, "Então, juntando tudo: a sorte abre a porta, mas só a base própria te mantém lá dentro. Não confunda força emprestada com força sua.")
c(L, "Deixe a culpa onde ela pertence, e assuma o peso quando for você que lidera. Leia as atitudes, não os presentes. E planeje também para o pior dia.")
c(GIU, "E nunca coloque a sua sorte na mão de quem você feriu. Essa é a linha que Bórgia esqueceu e que Maquiavel fez questão de escrever.",
  interage={'tipo': 'manda', 'txt': 'Manda pra quem depende de um só'}, conv=True)
c(MP, "No próximo vídeo da playlist Personagens do poder, você vai conhecer outro nome que Maquiavel estudou de perto. Até a próxima lição, raposa.",
  cta='Até a próxima <b>lição</b>,<br>raposa', selo='RAPOSA<br>E LEÃO')

MOVS = ['in', 'out', 'esq', 'dir', 'cima']
cenas = []
for i, (g, t, x) in enumerate(C):
    cenas.append({'gravura': g, 'mov': MOVS[(i * 2 + i // 5) % 5], 'txt': t, **x})

v = {
    'id': 'longo-03', 'canal': 'raposa', 'formato': 'longo',
    'titulo': 'César Bórgia: o único erro do príncipe de Maquiavel',
    'legenda': "César Bórgia é o homem que Maquiavel mais usa como exemplo em O Príncipe. Filho do papa Alexandre VI, conquistou a Romanha com tropas emprestadas, trocou-as por armas próprias, fez a ordem na praça de Cesena e montou a armadilha de Senigália. Maquiavel viu tudo de perto, como enviado de Florença.\n\n"
                "Em poucos meses, Bórgia perdeu tudo. Neste vídeo você descobre a frase que ele mesmo disse a Maquiavel, o único erro que o capítulo VII aponta e o que essa história ensina para se proteger no trabalho, nos negócios e na família.\n\n"
                "⏱️ Capítulos\n{CAPITULOS}\n\n"
                "📜 Fonte: Nicolau Maquiavel, O Príncipe, caps. VII, VIII, XIII, XVII, XVIII e XIX; relatórios da legação de Maquiavel junto ao duque Valentino (1502-1503). As citações aparecem em paráfrase curta.\n\n"
                "🦊🦁 Raposa e Leão: Maquiavel e as leis do poder aplicadas à vida real.\n\n"
                "▶️ Playlist recomendada: Personagens do poder\n\n"
                "#CésarBórgia #Maquiavel #OPríncipe #Renascimento #HistóriaDaItália",
    'comentario': "📌 Bórgia entregou o próprio destino na mão de quem ele tinha ferido. Na sua vida, de quem ou do que você depende demais hoje? Continue na playlist Personagens do poder ⬇️",
    'titulo_tela': {'sup': 'RAPOSA E LEÃO', 'txt': 'César Bórgia<br>o único erro', 'dur': 3.2},
    'capa': {'A': 'Um só erro', 'B': 'Perdeu tudo', 'gravA': 'borgia.jpg', 'gravB': 'acervo/julio_ii_raffaello.jpg'},
    'cenas': cenas,
}
json.dump(v, open(R + '/roteiros/longo-03.json', 'w'), ensure_ascii=False, indent=1)
pal = [len(x['txt'].split()) for x in cenas]
print(len(cenas), 'cenas', sum(pal), 'palavras', 'min/max', min(pal), max(pal),
      'caps', sum('cap' in x for x in cenas), 'versos', sum('verso' in x for x in cenas), 'interage', sum('interage' in x for x in cenas),
      'imagens', len({x['gravura'] for x in cenas}))
for i in range(1, len(cenas)):
    assert cenas[i]['gravura'] != cenas[i - 1]['gravura'], i
for x in cenas:
    assert os.path.exists(R + '/img/' + x['gravura']) or x['gravura'].startswith('acervo/'), x['gravura']
