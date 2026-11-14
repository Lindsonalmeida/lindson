# Semana 1 dos Reels da Orégano Turbo (14/11/2026, conta Zuleide, agente Paollo + Rocco + Social media + Copy).
# Gera roteiros.json + motor/producao/OT-NN.json a partir das fichas abaixo. Motor: motor/reel.py (adaptado do
# conteudo/reels/leva-30s/motor, identidade Orégano v4). Voz: pt-BR-AntonioNeural +4% (aprovada). Nunca a voz do Lindson.
import json, os, re
H = os.path.dirname(os.path.abspath(__file__))
FOTOS = json.load(open(os.path.join(H, 'fotos', 'lista.json')))
TRILHAS = ['pop-track-03-108bpm.mp3', 'trap-electro-vibes-112bpm.mp3', 'midnight-funk-117bpm.mp3']
DIAS = ['16/11', '17/11', '18/11', '19/11', '20/11', '21/11', '22/11']; HORAS = ['12:10', '19:10', '23:40']

# cena: (tipo, narração, texto na tela, extras)
def F(n, t, **k): return ('fotofull', n, t, k)
def I(n, t, **k): return ('impacto', n, t, k)
def Q(n, t, **k): return ('frase', n, t, k)
def B(n, t, clip, **k): return ('banco', n, t, dict(clip=clip, **k))
def LI(n, tit, itens, em, **k): return ('lista', n, [], dict(titulo=tit, itens=itens, tempos_em=em, **k))
def CH(n, nome, msgs, em, **k): return ('chat', n, [], dict(nome=nome, msgs=msgs, tempos_em=em, **k))
def C(n, etiquetas): return ('cta', n, [], dict(etiquetas=etiquetas, vfx=['leak']))

R = [
 # ---------------- DIA 1 ----------------
 dict(t='conteudo', linha='História da pizza', titulo='A pizza Margherita nasceu de um pedido da rainha (ou quase)', palavra='RAINHA', capa=('1889', 'A pizza que nasceu', 'pra uma rainha'),
  entrega='Te mando 5 histórias de sabores pra usar no seu cardápio.', cenas=[
  F('Essa pizza tem nome de rainha.', ['Nome de', 'rainha'], hl=[1], hit=['rainha'], vfx=['punch']),
  I('Conta a história que em 1889, em Nápoles, um pizzaiolo fez uma pizza pra rainha Margherita.', ['Nápoles', '1889'], hl=[1], hit=['1889']),
  LI('Tomate, mussarela e manjericão. As cores da bandeira da Itália.', 'As 3 cores', [['1', 'Tomate'], ['2', 'Mussarela'], ['3', 'Manjericão']], ['tomate', 'mussarela', 'manjericão']),
  Q('Se é lenda ou fato, ninguém prova. Mas a história vende até hoje.', ['A história', 'vende'], carimbo='LENDA OU FATO', carimboAt='prova'),
  B('Seu sabor da casa também pode ter uma história.', ['Sua pizza', 'tem história?'], 'celular-noite-digitando', hl=[1]),
  C('Comenta RAINHA que eu te mando cinco histórias de sabores pra usar no cardápio.', ['5 histórias', 'Cardápio']),
  I('Cliente lembra de história.', ['Cliente lembra', 'de história'], hl=[1])]),
 dict(t='conteudo', linha='Humor de dono', titulo='POV: é terça-feira e a pizzaria está parada', palavra='TERÇA', capa=('TERÇA', 'POV: terça-feira', 'e o forno ligado'),
  entrega='Te mando 3 ideias de ação para dia fraco (sem desconto).', cenas=[
  F('POV: é terça-feira. O forno tá quente e o telefone tá mudo.', ['POV:', 'terça-feira'], hl=[1], hit=['mudo'], vfx=['punch']),
  B('Você abre o iFood de cinco em cinco minutos.', ['De 5 em 5', 'minutos'], 'rolando-feed-cama', hl=[1]),
  I('E pensa: fim de semana eu compenso.', ['Fim de semana', 'eu compenso'], hl=[1], hit=['compenso']),
  Q('Só que dia fraco não se resolve no sábado. Se resolve com motivo pra pedir na terça.', ['Motivo pra', 'pedir na terça'], carimbo='DIA FRACO', carimboAt='terça'),
  LI('Sabor da semana, combo da família, pizza do dia na lista do WhatsApp.', 'Motivos', [['1', 'Sabor da semana'], ['2', 'Combo família'], ['3', 'Lista do zap']], ['sabor', 'combo', 'lista']),
  C('Comenta TERÇA que eu te mando três ideias pra dia fraco sem dar desconto.', ['3 ideias', 'Sem desconto']),
  I('Marca quem conhece essa terça.', ['Marca quem', 'conhece'], hl=[1])]),
 dict(t='venda', linha='Raio-X', titulo='O Raio-X da pizzaria: o que a gente olha em 10 minutos', palavra='RAIO-X', capa=('RAIO-X', 'O que eu olho primeiro', 'na sua pizzaria'),
  entrega='Te mando como pedir o Raio-X da sua pizzaria.', cenas=[
  F('Antes de falar em anúncio, eu olho três coisas na sua pizzaria.', ['3 coisas', 'antes do anúncio'], hl=[0], hit=['três'], vfx=['punch']),
  LI('A foto do cardápio. O caminho até o pedido. E quanto tempo o cliente espera resposta no WhatsApp.', 'O Raio-X', [['1', 'Foto do cardápio'], ['2', 'Caminho do pedido'], ['3', 'Resposta no zap']], ['foto', 'caminho', 'quanto']),
  I('Se uma delas trava, o anúncio vira dinheiro jogado fora.', ['Dinheiro', 'jogado fora'], hl=[0], hit=['fora']),
  B('Por isso o primeiro passo é o Raio-X, e não o anúncio.', ['Primeiro', 'o Raio-X'], 'empreendedora-notebook', hl=[1]),
  Q('Você recebe o que mudar, em ordem, sem enrolação.', ['O que mudar,', 'em ordem'], carimbo='SÓ PIZZARIAS', carimboAt='ordem'),
  C('Comenta RAIO-X que eu te explico como pedir o da sua pizzaria.', ['Raio-X', 'Só pizzarias']),
  I('Só trabalhamos com pizzaria.', ['Só', 'pizzaria'], hl=[1])]),
 # ---------------- DIA 2 ----------------
 dict(t='conteudo', linha='Dados do setor', titulo='40 mil pizzarias no Brasil: o que esse número diz para você', palavra='MERCADO', capa=('40 MIL', 'Pizzarias no Brasil.', 'E a sua?'),
  entrega='Te mando as fontes e os números do setor numa imagem.', cenas=[
  F('O Brasil tem mais de quarenta mil pizzarias.', ['40.332', 'pizzarias'], hl=[0], hit=['quarenta'], vfx=['punch']),
  I('Segundo a Apubra, quase todas fazem delivery: noventa e oito por cento.', ['98%', 'fazem delivery'], hl=[0], hit=['oito']),
  I('E setenta e cinco por cento usam aplicativo pra pegar pedido.', ['75%', 'usam app'], hl=[0], hit=['cinco']),
  Q('Ou seja: o cliente tem muita opção na mesma tela.', ['Muita opção', 'na mesma tela'], carimbo='CONCORRÊNCIA', carimboAt='tela'),
  B('O que faz ele escolher você é foto, nome do sabor e confiança.', ['Foto, sabor', 'e confiança'], 'maos-digitando-celular', hl=[0]),
  C('Comenta MERCADO que eu te mando os números com as fontes.', ['Fonte: Apubra', 'Galunion']),
  I('Salva pra mostrar pro sócio.', ['Salva', 'pro sócio'], hl=[0])]),
 dict(t='conteudo', linha='Técnica de massa', titulo='Massa que encolhe no disco: 3 motivos', palavra='MASSA', capa=('MASSA', 'Sua massa encolhe', 'quando abre?'),
  entrega='Te mando o checklist da massa que não encolhe.', cenas=[
  F('Sua massa encolhe quando você abre no disco?', ['A massa', 'encolhe?'], hl=[1], hit=['encolhe'], vfx=['punch']),
  I('Quase sempre é o glúten tenso.', ['Glúten', 'tenso'], hl=[1], hit=['tenso']),
  LI('Pouco descanso depois de bolear. Massa gelada demais. Ou sova longa demais.', '3 motivos', [['1', 'Pouco descanso'], ['2', 'Massa gelada'], ['3', 'Sova demais']], ['descanso', 'gelada', 'sova']),
  Q('Deixa a bolinha voltar pra temperatura ambiente antes de abrir.', ['Temperatura', 'ambiente'], carimbo='DESCANSO', carimboAt='abrir'),
  B('E abre com a ponta dos dedos, do centro pra borda.', ['Do centro', 'pra borda'], 'maos-digitando-celular', hl=[1]),
  C('Comenta MASSA que eu te mando o checklist da massa que não encolhe.', ['Checklist', 'Massa']),
  I('Manda pro seu pizzaiolo.', ['Manda pro', 'pizzaiolo'], hl=[1])]),
 dict(t='venda', linha='Método', titulo='Pedido direto no WhatsApp: como funciona o método Orégano Turbo', palavra='MÉTODO', capa=('ZAP', 'Pedido direto', 'no seu WhatsApp'),
  entrega='Te mando o passo a passo do método em 4 telas.', cenas=[
  F('Imagina o pedido chegando direto no seu WhatsApp, sem taxa de aplicativo.', ['Direto', 'no seu zap'], hl=[1], hit=['WhatsApp'], vfx=['punch']),
  LI('São quatro passos. Anúncio gravado na sua pizzaria. Pedido no WhatsApp. Um código em cada anúncio. E relatório toda segunda.', '4 passos', [['1', 'Anúncio na pizzaria'], ['2', 'Pedido no zap'], ['3', 'Código no anúncio'], ['4', 'Relatório segunda']], ['anúncio', 'pedido', 'código', 'relatório'], compacto=True),
  I('O código mostra de qual anúncio veio cada pedido.', ['De onde veio', 'cada pedido'], hl=[1], hit=['pedido']),
  CH('Exemplo de pedido com código.', 'Cliente (exemplo)', [['ele', 'Quero a calabresa grande. Código TERÇA10 (ilustrativo)'], ['eu', 'Anotado! Sai em 40 min 🍕']], ['exemplo', 'código']),
  B('Sem achismo. Você vê o que funcionou.', ['Sem', 'achismo'], 'empresario-mensagens', hl=[1]),
  C('Comenta MÉTODO que eu te mando o passo a passo.', ['4 passos', 'Só pizzarias']),
  I('Feito só pra pizzaria.', ['Só pra', 'pizzaria'], hl=[1])]),
 # ---------------- DIA 3 ----------------
 dict(t='conteudo', linha='Forno', titulo='Por que a pizza napolitana assa em 90 segundos', palavra='FORNO', capa=('90s', 'Pizza pronta', 'em 90 segundos'),
  entrega='Te mando a tabela de temperatura e tempo por tipo de forno.', cenas=[
  F('Tem pizza que assa em noventa segundos.', ['90', 'segundos'], hl=[0], hit=['noventa'], vfx=['punch', 'leak']),
  I('A napolitana tradicional assa em forno a lenha acima de quatrocentos graus.', ['+400 °C'], hl=[0], hit=['quatrocentos']),
  Q('Por isso a borda fica alta e com aquelas pintinhas pretas.', ['Borda alta', 'e pintada'], carimbo='LEOPARDO', carimboAt='pintinhas'),
  LI('Em forno elétrico ou a gás, a temperatura é menor e o tempo aumenta.', 'Cada forno', [['L', 'Lenha: muito alto'], ['G', 'Gás: médio'], ['E', 'Elétrico: médio']], ['elétrico', 'temperatura', 'tempo']),
  B('O segredo é ajustar a massa ao forno que você tem.', ['Massa certa', 'pro seu forno'], 'cidade-noite', hl=[0]),
  C('Comenta FORNO que eu te mando a tabela de temperatura e tempo.', ['Tabela', 'Forno']),
  I('Qual é o seu forno?', ['Qual é', 'seu forno?'], hl=[1])]),
 dict(t='conteudo', linha='Resposta pronta', titulo='Cliente reclamou da demora: a resposta que acalma', palavra='DEMORA', capa=('DEMORA', 'Cliente reclamou', 'da demora?'),
  entrega='Te mando 5 respostas prontas para reclamação.', cenas=[
  CH('O cliente mandou: cadê minha pizza? Já faz uma hora!', 'Cliente', [['ele', 'Cadê minha pizza?? Já faz 1 hora!'], ['ele', '😡']], ['cadê', 'hora']),
  I('A pior resposta é: tá saindo.', ['Tá saindo'], hl=[0], hit=['saindo'], vfx=['glitch'], som_hit='glitch-quebra'),
  Q('Ele quer três coisas: desculpa, tempo real e uma atenção.', ['Desculpa e', 'tempo real'], carimbo='3 COISAS', carimboAt='atenção'),
  CH('Manda assim: desculpa a demora, sua pizza saiu agora e chega em quinze minutos. Vai um refri por nossa conta.', 'Cliente', [['eu', 'Desculpa a demora! Sua pizza saiu agora e chega em 15 min. Vai um refri por nossa conta 🥤'], ['ele', 'Ah, beleza, obrigado! (ilustrativo)']], ['desculpa', 'refri']),
  B('Resposta boa vira avaliação boa.', ['Vira', 'avaliação'], 'respondendo-whatsapp', hl=[1]),
  C('Comenta DEMORA que eu te mando cinco respostas prontas pra reclamação.', ['5 respostas', 'Prontas']),
  I('Salva e manda pro atendimento.', ['Manda pro', 'atendimento'], hl=[1])]),
 dict(t='venda', linha='Chamada para diagnóstico', titulo='3 sinais de que sua pizzaria precisa de um diagnóstico', palavra='SINAIS', capa=('SINAIS', '3 sinais de que', 'sua pizzaria travou'),
  entrega='Te mando como pedir o Raio-X da sua pizzaria.', cenas=[
  F('Três sinais de que sua pizzaria precisa de um diagnóstico.', ['3 sinais'], hl=[0], hit=['três'], vfx=['punch']),
  I('Um: você posta e o pedido não muda.', ['Posta e', 'nada muda'], hl=[1], hit=['muda']),
  I('Dois: quase todo pedido vem do aplicativo.', ['Tudo vem', 'do app'], hl=[1], hit=['aplicativo']),
  I('Três: você não sabe de onde veio o cliente da semana.', ['De onde', 'ele veio?'], hl=[1], hit=['semana']),
  B('Não é falta de esforço. É falta de olhar de fora.', ['Olhar', 'de fora'], 'escritorio-entediado', hl=[1]),
  C('Comenta SINAIS que eu te explico como pedir o Raio-X da sua pizzaria.', ['Raio-X', 'Diagnóstico']),
  I('Quantos sinais você tem?', ['Quantos', 'você tem?'], hl=[1])]),
 # ---------------- DIA 4 ----------------
 dict(t='conteudo', linha='Gestão', titulo='CMV de pizzaria: a conta que muita gente não faz', palavra='CMV', capa=('CMV', 'Você sabe quanto', 'custa sua pizza?'),
  entrega='Te mando a planilha simples de ficha técnica.', cenas=[
  F('Você sabe quanto custa a sua pizza de calabresa?', ['Quanto custa', 'sua pizza?'], hl=[1], hit=['calabresa'], vfx=['punch']),
  I('Isso é o CMV: o custo da mercadoria vendida.', ['CMV'], hl=[0], hit=['CMV']),
  Q('Em food service, a meta costuma ficar entre vinte e cinco e trinta e cinco por cento do preço.', ['25% a 35%', 'do preço'], carimbo='REFERÊNCIA', carimboAt='preço'),
  LI('Pesa massa, molho, queijo, recheio e caixa. Soma tudo.', 'Ficha técnica', [['1', 'Massa e molho'], ['2', 'Queijo e recheio'], ['3', 'Caixa']], ['massa', 'queijo', 'caixa']),
  B('Sem ficha técnica, o preço é chute.', ['Preço', 'no chute'], 'empreendedora-notebook', hl=[1]),
  C('Comenta CMV que eu te mando a planilha de ficha técnica.', ['Planilha', 'Grátis']),
  I('Faz a conta hoje.', ['Faz a conta', 'hoje'], hl=[1])]),
 dict(t='conteudo', linha='Curiosidade', titulo='A pizza napolitana é patrimônio da humanidade', palavra='UNESCO', capa=('UNESCO', 'O pizzaiolo virou', 'patrimônio'),
  entrega='Te mando 5 curiosidades de pizza para postar.', cenas=[
  F('A arte do pizzaiolo napolitano é patrimônio da humanidade.', ['Patrimônio', 'da humanidade'], hl=[0], hit=['patrimônio'], vfx=['punch', 'leak']),
  I('A Unesco reconheceu em dois mil e dezessete.', ['UNESCO', '2017'], hl=[1], hit=['dezessete']),
  Q('Não é a pizza em si. É o gesto: abrir, girar e assar.', ['O gesto', 'do pizzaiolo'], carimbo='TÉCNICA', carimboAt='assar'),
  B('E isso diz muito: cliente gosta de ver a mão do pizzaiolo.', ['A mão do', 'pizzaiolo'], 'cafe-instagram', hl=[1]),
  I('Bastidor é conteúdo.', ['Bastidor', 'é conteúdo'], hl=[0], hit=['conteúdo']),
  C('Comenta UNESCO que eu te mando cinco curiosidades pra postar.', ['5 curiosidades', 'Pra postar']),
  I('Mostra seu pizzaiolo.', ['Mostra seu', 'pizzaiolo'], hl=[1])]),
 dict(t='venda', linha='Raio-X', titulo='Taxa do aplicativo: como trazer o cliente pro seu canal', palavra='TAXA', capa=('TAXA', 'Quanto o app', 'leva de você?'),
  entrega='Te mando como pedir o Raio-X e ver o seu caso.', cenas=[
  F('Cada pedido no aplicativo leva um pedaço da sua margem.', ['Um pedaço', 'da margem'], hl=[0], hit=['margem'], vfx=['punch']),
  I('O app traz cliente novo. Isso é bom.', ['App traz', 'cliente novo'], hl=[1]),
  Q('O erro é deixar o cliente que voltou pedindo só pelo app.', ['O cliente', 'que voltou'], carimbo='ERRO', carimboAt='app'),
  LI('Cartão na caixa, cardápio digital e lista do WhatsApp trazem ele pro seu canal.', 'Seu canal', [['1', 'Cartão na caixa'], ['2', 'Cardápio digital'], ['3', 'Lista do zap']], ['cartão', 'cardápio', 'lista']),
  B('No Raio-X a gente mostra por onde começar no seu caso.', ['Por onde', 'começar'], 'empresario-mensagens', hl=[1]),
  C('Comenta TAXA que eu te explico como pedir o Raio-X.', ['Raio-X', 'Seu canal']),
  I('O cliente é seu.', ['O cliente', 'é seu'], hl=[1])]),
 # ---------------- DIA 5 ----------------
 dict(t='conteudo', linha='Ferramenta grátis', titulo='Google Meu Negócio: a vitrine grátis da pizzaria', palavra='GOOGLE', capa=('GOOGLE', 'Pizzaria perto', 'de mim'),
  entrega='Te mando o checklist do perfil no Google.', cenas=[
  F('Quando alguém pesquisa pizzaria perto de mim, quem aparece?', ['Pizzaria', 'perto de mim'], hl=[1], hit=['mim'], vfx=['punch']),
  I('É o Google Meu Negócio. E é grátis.', ['Grátis'], hl=[0], hit=['grátis']),
  LI('Horário certo, fotos reais das pizzas, link do cardápio e resposta em toda avaliação.', 'Checklist', [['1', 'Horário certo'], ['2', 'Fotos reais'], ['3', 'Link do cardápio'], ['4', 'Responder avaliação']], ['horário', 'fotos', 'link', 'resposta'], compacto=True),
  Q('Horário errado faz o cliente desistir antes de ligar.', ['Horário', 'errado'], carimbo='CUIDADO', carimboAt='desistir'),
  B('Leva dez minutos pra arrumar.', ['10 minutos'], 'maos-digitando-celular', hl=[0]),
  C('Comenta GOOGLE que eu te mando o checklist do perfil.', ['Checklist', 'Grátis']),
  I('Arruma hoje à noite.', ['Arruma', 'hoje'], hl=[1])]),
 dict(t='conteudo', linha='Bastidor', titulo='Bastidor: o que a gente grava numa pizzaria em 1 hora', palavra='GRAVAR', capa=('1 HORA', 'O que dá pra gravar', 'na sua cozinha'),
  entrega='Te mando a lista de 10 cenas para gravar no celular.', cenas=[
  F('Com uma hora na cozinha dá pra gravar conteúdo de um mês.', ['1 hora', '= 1 mês'], hl=[0], hit=['mês'], vfx=['punch', 'leak']),
  LI('Massa sendo aberta. Queijo puxando. Pizza entrando no forno. E a caixa fechando.', 'As cenas', [['1', 'Massa abrindo'], ['2', 'Queijo puxando'], ['3', 'Forno'], ['4', 'Caixa fechando']], ['massa', 'queijo', 'forno', 'caixa'], compacto=True),
  I('Grava sempre na vertical, com luz de frente.', ['Vertical', 'luz de frente'], hl=[0]),
  Q('Não precisa aparecer falando. A pizza fala.', ['A pizza', 'fala'], carimbo='SEM ROSTO', carimboAt='fala'),
  B('Corta em vídeos de dez segundos e posta um por dia.', ['Um por dia'], 'trabalho-e-redes', hl=[0]),
  C('Comenta GRAVAR que eu te mando a lista de dez cenas.', ['10 cenas', 'No celular']),
  I('Grava no sábado.', ['Grava no', 'sábado'], hl=[1])]),
 dict(t='venda', linha='Método', titulo='O relatório de segunda: o que o dono recebe toda semana', palavra='RELATÓRIO', capa=('SEGUNDA', 'O relatório que', 'chega toda segunda'),
  entrega='Te mando um modelo do relatório (com números ilustrativos).', cenas=[
  F('Toda segunda o dono da pizzaria recebe uma página.', ['Toda', 'segunda'], hl=[1], hit=['segunda'], vfx=['punch']),
  LI('Quanto investiu. Quantos pedidos vieram de cada anúncio. E o que muda na semana.', 'O relatório', [['R$', 'Investimento'], ['Nº', 'Pedidos por anúncio'], ['→', 'O que muda']], ['investiu', 'pedidos', 'muda']),
  I('Uma página. Sem gráfico difícil.', ['1 página'], hl=[0], hit=['página']),
  Q('Quem decide é você, olhando o número.', ['Você decide'], carimbo='TRANSPARENTE', carimboAt='número'),
  B('É assim que trabalhamos com pizzaria.', ['Só com', 'pizzaria'], 'empreendedora-notebook', hl=[1]),
  C('Comenta RELATÓRIO que eu te mando um modelo com números ilustrativos.', ['Modelo', 'Ilustrativo']),
  I('Sem achismo.', ['Sem', 'achismo'], hl=[1])]),
 # ---------------- DIA 6 ----------------
 dict(t='conteudo', linha='Insumo', titulo='Mussarela que solta água: o que fazer', palavra='QUEIJO', capa=('QUEIJO', 'Pizza encharcada', 'tem solução'),
  entrega='Te mando o guia rápido de queijo para pizza.', cenas=[
  F('Pizza encharcada no meio? Pode ser o queijo.', ['Pizza', 'encharcada?'], hl=[1], hit=['queijo'], vfx=['punch']),
  I('Queijo com muita umidade solta água no forno.', ['Solta água'], hl=[0], hit=['forno']),
  LI('Escorre bem, rala ou fatia antes, e guarda gelado e seco.', 'O que fazer', [['1', 'Escorrer'], ['2', 'Ralar antes'], ['3', 'Guardar seco']], ['escorre', 'rala', 'guarda']),
  Q('E não exagera no molho por baixo.', ['Menos', 'molho'], carimbo='EQUILÍBRIO', carimboAt='baixo'),
  B('Pizza que chega mole vira avaliação ruim.', ['Avaliação', 'ruim'], 'rolando-feed-cama', hl=[1]),
  C('Comenta QUEIJO que eu te mando o guia rápido de queijo.', ['Guia', 'Queijo']),
  I('Manda pra cozinha.', ['Manda pra', 'cozinha'], hl=[1])]),
 dict(t='conteudo', linha='Humor de dono', titulo='Coisas que todo dono de pizzaria já ouviu', palavra='OUVI', capa=('JÁ OUVI', 'Coisas que todo', 'pizzaiolo já ouviu'),
  entrega='Te mando o meme em alta para postar no seu perfil.', cenas=[
  CH('Coisas que todo dono de pizzaria já ouviu.', 'Clientes', [['ele', 'Dá pra fazer meia calabresa, meia doce e borda de outra?'], ['ele', 'Faz um desconto que eu divulgo pros amigos 😅']], ['ouviu', 'pizzaria']),
  I('Meia calabresa, meia chocolate, e borda de outra.', ['Meia', 'meia meia'], hl=[1], hit=['chocolate']),
  I('Faz um desconto que eu divulgo.', ['Eu divulgo'], hl=[0], hit=['divulgo']),
  I('E o clássico: tá chegando?', ['Tá', 'chegando?'], hl=[1], hit=['chegando']),
  B('E você ali, sorrindo, com o forno a mil.', ['Forno', 'a mil'], 'sorrindo-no-celular', hl=[1]),
  C('Comenta OUVI e me conta a pior que você já ouviu.', ['Conta aqui', 'A pior']),
  I('Marca seu pizzaiolo.', ['Marca seu', 'pizzaiolo'], hl=[1])]),
 dict(t='venda', linha='Chamada para diagnóstico', titulo='Raio-X ao vivo: o perfil de pizzaria que não vende', palavra='PERFIL', capa=('PERFIL', 'Seu perfil espanta', 'ou chama pedido?'),
  entrega='Te mando como pedir o Raio-X do seu perfil.', cenas=[
  F('Seu perfil chama pedido ou espanta cliente?', ['Chama pedido', 'ou espanta?'], hl=[1], hit=['espanta'], vfx=['punch']),
  LI('Bio sem link de pedido. Foto escura. E nenhum sabor com preço.', 'O que espanta', [['✕', 'Bio sem link'], ['✕', 'Foto escura'], ['✕', 'Sem preço']], ['bio', 'foto', 'preço']),
  I('O cliente decide em segundos.', ['Em', 'segundos'], hl=[1], hit=['segundos']),
  Q('E ele não volta pra dar segunda chance.', ['Sem segunda', 'chance'], carimbo='3 SEGUNDOS', carimboAt='chance'),
  B('No Raio-X eu te mostro o que corrigir primeiro.', ['O que', 'corrigir'], 'rolando-pagina-venda', hl=[1]),
  C('Comenta PERFIL que eu te explico como pedir o Raio-X.', ['Raio-X', 'Perfil']),
  I('Só pizzarias.', ['Só', 'pizzarias'], hl=[1])]),
 # ---------------- DIA 7 ----------------
 dict(t='conteudo', linha='Dados do setor', titulo='As melhores pizzarias do mundo em 2026 têm isto em comum', palavra='RANKING', capa=('TOP 50', 'O que as melhores', 'do mundo fazem'),
  entrega='Te mando as 5 lições do ranking 50 Top Pizza.', cenas=[
  F('O ranking 50 Top Pizza avalia a pizzaria inteira, não só a pizza.', ['50 Top', 'Pizza'], hl=[1], hit=['inteira'], vfx=['punch', 'leak']),
  I('Em 2026, o Brasil tem seis pizzarias na lista mundial.', ['6 do Brasil'], hl=[0], hit=['seis']),
  LI('Pizza assinatura, marketing forte, nota do cliente, bebida e sobremesa.', 'Em comum', [['1', 'Pizza assinatura'], ['2', 'Marketing'], ['3', 'Nota do cliente'], ['4', 'Bebida e doce']], ['assinatura', 'marketing', 'nota', 'sobremesa'], compacto=True),
  Q('Você não precisa estar no ranking pra copiar o método.', ['Copia o', 'método'], carimbo='LIÇÃO', carimboAt='método'),
  B('Começa pela sua pizza assinatura.', ['Sua pizza', 'assinatura'], 'cafe-instagram', hl=[1]),
  C('Comenta RANKING que eu te mando as cinco lições.', ['5 lições', 'Top Pizza']),
  I('Qual é a sua assinatura?', ['Qual é a', 'sua?'], hl=[1])]),
 dict(t='conteudo', linha='Gestão', titulo='Upsell no WhatsApp: a pergunta que aumenta o pedido', palavra='UPSELL', capa=('+ R$', 'A pergunta que', 'aumenta o pedido'),
  entrega='Te mando 5 frases de upsell para o atendimento.', cenas=[
  CH('O cliente pediu uma calabresa grande no WhatsApp.', 'Cliente', [['ele', 'Uma calabresa grande, por favor'], ['eu', 'Anotado! 🍕']], ['calabresa', 'WhatsApp']),
  I('A maioria responde só anotado e pronto.', ['Anotado', 'e pronto'], hl=[1], hit=['pronto']),
  CH('Tenta assim: quer colocar borda de catupiry? Ou um refri gelado junto?', 'Cliente', [['eu', 'Quer colocar borda de catupiry? Ou um refri gelado junto? 🥤'], ['ele', 'Coloca a borda! (ilustrativo)']], ['borda', 'refri']),
  Q('Uma opção clara. Sem empurrar.', ['Sem', 'empurrar'], carimbo='UMA OPÇÃO', carimboAt='empurrar'),
  B('É atenção, não insistência.', ['Atenção'], 'respondendo-whatsapp', hl=[0]),
  C('Comenta UPSELL que eu te mando cinco frases prontas.', ['5 frases', 'Atendimento']),
  I('Testa no sábado.', ['Testa no', 'sábado'], hl=[1])]),
 dict(t='conteudo', linha='Dia da Pizza', titulo='Dia da Pizza é 10 de julho: comece a planejar agora', palavra='CALENDÁRIO', capa=('10/07', 'As datas que', 'vendem pizza'),
  entrega='Te mando o calendário de datas da pizzaria.', cenas=[
  F('Toda pizzaria precisa de um calendário de datas.', ['Calendário', 'de datas'], hl=[0], hit=['calendário'], vfx=['punch']),
  I('A maior é o Dia da Pizza, dez de julho.', ['10 de julho'], hl=[0], hit=['julho']),
  LI('Mas tem Copa, final de campeonato, Dia dos Pais e a noite da sexta.', 'Outras datas', [['⚽', 'Jogo e final'], ['♥', 'Dia dos Pais'], ['★', 'Sexta à noite']], ['Copa', 'Pais', 'sexta']),
  Q('Data boa se prepara com duas semanas de antecedência.', ['2 semanas', 'antes'], carimbo='PLANEJA', carimboAt='antecedência'),
  B('Estoque, equipe e conteúdo prontos antes.', ['Tudo pronto', 'antes'], 'cidade-noite', hl=[0]),
  C('Comenta CALENDÁRIO que eu te mando o calendário de datas.', ['Calendário', 'Pizzaria']),
  I('Salva esse vídeo.', ['Salva', 'esse vídeo'], hl=[0])]),
]

roteiros = dict(leva='Reels Orégano Turbo · semana 1', criado='2026-11-14', conta='Zuleide (Paollo)', reels=[])
os.makedirs(os.path.join(H, 'motor', 'producao'), exist_ok=True)
fi = 0
for k, r in enumerate(R):
    nn = k + 1; rid = f'OT-{nn:02d}'
    cenas_r, cenas_p = [], []
    for tipo, narr, tela, ex in r['cenas']:
        cenas_r.append(dict(narracao=narr, texto_tela=' '.join(tela), texto_tela_palavras=tela or ['·']))
        p = dict(tipo=tipo, texto=tela, **{x: y for x, y in ex.items()})
        if tipo in ('fotofull', 'cta'):
            p['foto'] = FOTOS[fi]['id'] + '.jpg'; p.setdefault('_cred', FOTOS[fi]['pagina']); fi += 1
        if tipo == 'impacto': p.setdefault('size', 200); p.setdefault('top', 640); p.setdefault('flash', True)
        if tipo == 'banco': p.setdefault('size', 170); p.setdefault('top', 560); p.setdefault('vfx', ['punch'])
        if tipo == 'frase': p.setdefault('size', 170); p.setdefault('top', 560)
        if tipo == 'fotofull': p.setdefault('top', 470); p.setdefault('size', 180)
        cenas_p.append(p)
    # blocos de voz (até ~220 caracteres, quebra em frase)
    frases = re.split(r'(?<=[.?!])\s+', ' '.join(c['narracao'] for c in cenas_r)); blocos = ['']
    for f in frases:
        if len(blocos[-1]) + len(f) + 1 > 220: blocos.append('')
        blocos[-1] = (blocos[-1] + ' ' + f).strip()
    capa_foto = next(p['foto'] for p in cenas_p if p['tipo'] in ('fotofull', 'cta'))
    pal, man, cx = r['capa']
    roteiros['reels'].append(dict(id=rid, ordem=nn, post=dict(data=DIAS[k // 3], hora=HORAS[k % 3]), titulo=r['titulo'], tipo=r['t'],
        linha_editorial=r['linha'], capa_cor='preto', cta_palavra=r['palavra'], entrega_no_video=r['entrega'], blocos_voz=blocos, cenas=cenas_r))
    json.dump(dict(_nota='Ficha OT (14/11/2026). Fotos Pexels (licença livre) em ../fotos/.', beat_sync=True, voz_rate='+4%', voz_max=27.5,
                   trilha=TRILHAS[k % 3], trilha_ini=[2, 20, 8][k % 3],
                   capa=dict(foto=capa_foto, palavra=pal, manchete=man, caixa=cx, rotulo=r['linha'], wordTop=330, wordSize=420, headTop=1290, tagTop=1225, auto=False, fx=0, fy=0, fw=1080),
                   cenas=cenas_p), open(os.path.join(H, 'motor', 'producao', rid + '.json'), 'w'), ensure_ascii=False, indent=1)
json.dump(roteiros, open(os.path.join(H, 'roteiros.json'), 'w'), ensure_ascii=False, indent=1)
print(len(R), 'reels;', fi, 'fotos;', sum(r['t'] == 'venda' for r in R), 'de venda')
