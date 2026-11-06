# Linhas editoriais e calendário de 4 semanas do @oreganoturbo, com 3 postagens por dia (conta Leandro, 06/11/2026).
# Agentes: Marketing Squad (Donald Miller, Pedro Sobral), Copy Squad (ganchos) e Paollo (composição, padrão v3 aprovado).
# Regras do Lindson:
#  - imagem usada UMA única vez; quando acabar, pedir mais a ele (06/11);
#  - sem promessa de resultado (05/11);
#  - preço só os de DECISOES-APROVADAS.md.
# Uso: python3 montar_calendario.py  → CALENDARIO.md, calendario.json e PEDIDO-FOTOS-LOTE-2.txt
import json, os, datetime
D = os.path.dirname(os.path.abspath(__file__))

LINHAS = {
    'L1': ('Dor do dono', 'Dia fraco, comissão do app, foto ruim, cliente que some: o problema que ele sente no caixa.', '20%'),
    'L2': ('Dinheiro do delivery', 'Contas simples na tela, como app × zap e o valor de um cliente que volta. Todo número é exemplo marcado "ilustrativo".', '15%'),
    'L3': ('Dica pronta', 'Copie e cole: resposta de WhatsApp, combo de terça, legenda, checklist de foto e de cardápio.', '25%'),
    'L4': ('Método Orégano', 'Como funciona: gravação, anúncio no bairro, código no pedido, relatório de segunda.', '15%'),
    'L5': ('Cultura de pizzaria', 'Humor, referência pop e orgulho de pizzaiolo: o que faz o dono compartilhar.', '10%'),
    'L6': ('Oferta', 'Raio-X R$ 297, 5 vagas de fundadora e chamada para o diagnóstico no zap.', '15%'),
}

# (dia, hora, formato, linha, manchete, apoio, composição do padrão v3, imagem)
# imagem: 'v3:<arquivo>' = peça aprovada pronta · 'TIPO' = tipográfica, sem foto · 'F<n>' = foto nova a pedir ao Lindson
S1 = [
 (1,'08h','Story','L5','Bom dia, forno.','Segunda começa no balcão. Bora vender.','Story tipográfico: manchete gorda + xadrez + selo','TIPO'),
 (1,'12h','Feed','L1','FOTO QUE DÁ FOME.','A foto vende antes da pizza.','Peça aprovada','v3:p01-foto-que-da-fome.jpg'),
 (1,'19h','Feed','L4','SÓ PIZZARIAS.','Só fazemos isso. Por isso fazemos bem.','Peça aprovada','v3:p03-grade-so-pizzarias.jpg'),
 (2,'08h','Story','L1','Dia fraco tem nome?','Enquete: segunda, terça ou quarta.','Peça aprovada','v3:story-1-enquete.jpg'),
 (2,'12h','Feed','L1','TERÇA também tem fome.','Dia fraco tem conserto.','Peça aprovada','v3:p02-terca-tambem-tem-fome.jpg'),
 (2,'19h','Feed','L3','5 FOTOS QUE TIRAM A FOME','Escura, de longe, sem queijo, fria, cortada. Evite.','Checklist com X vermelho em cartões girados','TIPO'),
 (3,'08h','Story','L3','Responde assim:','"Qual o valor da entrega?" → resposta pronta para copiar.','Conversa de WhatsApp desenhada + "copia e cola"','TIPO'),
 (3,'12h','Feed','L6','RAIO-X DA SUA PIZZARIA','R$ 297, abatido no 1º mês se fechar em 7 dias.','Peça aprovada','v3:p05-raio-x-cartaz.jpg'),
 (3,'19h','Feed','L2','A CONTA DO PEDIDO','App × zap: veja quanto fica com você (exemplo ilustrativo).','Cardápio-cartaz com duas colunas e total em estrela','TIPO'),
 (4,'08h','Story','L4','Segunda, 8h.','O relatório chega no seu celular.','Celular desenhado com relatório (ilustrativo)','TIPO'),
 (4,'12h','Feed','L4','MENOS APP. MAIS ZAP.','Pedido direto, cliente seu.','Peça aprovada','v3:p04-menos-app-mais-zap.jpg'),
 (4,'19h','Feed','L3','COMBO DE TERÇA','3 combos que não desvalorizam a sua pizza.','Grade de 3 cartões numerados + faixa em loop','TIPO'),
 (5,'08h','Story','L6','Raio-X R$ 297','5 vagas de fundadora abertas.','Peça aprovada','v3:story-2-raio-x.jpg'),
 (5,'12h','Feed','L4','CARDÁPIO DA CASA','O que sai da nossa cozinha, todo mês.','Peça aprovada','v3:p06-cardapio-da-casa.jpg'),
 (5,'19h','Feed','L5','PENSO, LOGO PEÇO.','Seu cliente também. Ele pede pra você ou pra quem apareceu primeiro?','Manchete gigante + citação; sem foto de pessoa','TIPO'),
 (6,'08h','Story','L1','Sexta lota. E segunda?','Caixinha: qual o seu dia mais fraco?','Caixinha de perguntas com xadrez','TIPO'),
 (6,'12h','Feed','L6','5 VAGAS DE FUNDADORA.','Preço do anual no contrato de 6 meses.','Peça aprovada','v3:p08-5-vagas-fundadoras.jpg'),
 (6,'19h','Feed','L3','3 ERROS NO LINK DA BIO','Sem cardápio, sem zap, sem horário.','Celular desenhado com 3 setas e X','TIPO'),
 (7,'08h','Story','L4','Pedido direto no zap.','Assim chega o pedido (exemplo ilustrativo).','Peça aprovada','v3:story-3-pedido-no-zap.jpg'),
 (7,'12h','Feed','L5','PIZZA NA CABEÇA.','Só pensamos em pizzaria. Todo dia.','Peça aprovada','v3:p09-pizza-na-cabeca.jpg'),
 (7,'19h','Feed','L4','SÓ PIZZARIAS.','Hamburgueria, açaí e sushi: não atendemos.','Peça aprovada','v3:p07-so-pizzarias-avental.jpg'),
]
# Semanas 2 a 4: as fotos novas (F1…) são pedidas ao Lindson no Gemini (PEDIDO-FOTOS-LOTE-2.txt).
S2_4 = [
 (8,'08h','Story','L5','Bom dia, massa.','Fermentou? Então bora.','Story tipográfico','TIPO'),
 (8,'12h','Feed','L1','O APP FICOU COM A SUA MARGEM.','Parte de cada pedido vai embora.','Palavra gigante atrás do celular na mão','F1'),
 (8,'19h','Feed','L3','RESPOSTA PRONTA: "TÁ CARO"','Copie e cole no seu WhatsApp.','Conversa de WhatsApp + adesivo "copia e cola"','TIPO'),
 (9,'08h','Story','L2','Quanto vale um cliente que volta?','Faça a conta com a gente (ilustrativo).','Calculadora desenhada','TIPO'),
 (9,'12h','Feed','L3','7 FOTOS QUE DÃO FOME','Carrossel: luz, ângulo, queijo, vapor, mão, caixa, fundo.','Carrossel; capa com foto de queijo puxando','F2'),
 (9,'19h','Feed','L1','SEU CLIENTE SUMIU?','Ele pediu uma vez e esqueceu de você.','Manchete em 2 tamanhos + foto de caixa vazia','IA:B8a'),
 (10,'08h','Story','L4','Dia de gravação.','Bastidor: luz, flash, pizza saindo.','Story com foto de bastidor','F4'),
 (10,'12h','Feed','L4','A CAIXA É O ANÚNCIO QUE VOLTA.','O cliente vê a sua marca na mesa dele.','Peça com caixa de pizza da marca','F5'),
 (10,'19h','Feed','L3','LEGENDA PRONTA PRA TERÇA','Copie e cole.','Cartão grande com a legenda + selo','TIPO'),
 (11,'08h','Story','L1','Seu iFood tem foto?','Enquete: sim, não, mais ou menos.','Enquete','TIPO'),
 (11,'12h','Feed','L2','APP × ZAP','A mesma pizza, dois caminhos (ilustrativo).','Foto dividida ao meio','F6'),
 (11,'19h','Feed','L5','DOMINGO É DIA DE PIZZA. TERÇA TAMBÉM.','Quem disse que não?','Grade de 4 cores com a mesma manchete','IA:B7'),
 (12,'08h','Story','L6','Raio-X na sexta.','Fale com a gente no zap.','Story com estrela de preço','TIPO'),
 (12,'12h','Feed','L4','CÓDIGO EM CADA PEDIDO.','Assim a gente sabe qual vídeo vendeu.','Close de pedido com código PZ14','F8'),
 (12,'19h','Feed','L3','CHECKLIST DO CARDÁPIO DIGITAL','6 itens que fazem pedir mais rápido.','Checklist com ícones em traço','TIPO'),
 (13,'08h','Story','L5','Qual borda você pediria?','Enquete: catupiry, cheddar, chocolate.','Enquete com 3 bordas','F9'),
 (13,'12h','Feed','L1','PIZZA BOA NÃO VENDE SOZINHA.','Quem aparece mais vende mais.','Pizza gigante com texto em círculo','IA:B4'),
 (13,'19h','Feed','L6','5 VAGAS. NÃO VAI TER 6.','Condição de fundadora.','Cartaz retrô com selo','TIPO'),
 (14,'08h','Story','L4','Resumo da semana.','O que você aprendeu aqui.','Story tipográfico com 3 itens','TIPO'),
 (14,'12h','Feed','L5','PIZZAIOLO NÃO TIRA FÉRIAS.','Mas o seu anúncio pode trabalhar por você.','Pizzaiolo de avental (de baixo)','F11'),
 (14,'19h','Feed','L3','3 COMBOS QUE VENDEM NO FRIO','Ideias para a sua pizzaria (sem preço).','Grade de 3 cartões','TIPO'),
 (15,'08h','Story','L5','Bom dia, forno aceso.','Segunda de novo.','Story com foto de forno','IA:B8b'),
 (15,'12h','Feed','L1','TERÇA VAZIA CUSTA CARO.','Aluguel, gás e equipe pagam igual.','Cardápio-cartaz dos custos','TIPO'),
 (15,'19h','Feed','L4','COMO FUNCIONA EM 4 PASSOS','Carrossel do método.','Carrossel; capa com foto de mão segurando o celular','F13'),
 (16,'08h','Story','L3','Copia e cola:','Mensagem para cliente que sumiu.','Conversa de WhatsApp','TIPO'),
 (16,'12h','Feed','L2','QUANTO VALE UM CLIENTE QUE VOLTA','A conta na tela (ilustrativo).','Número gigante atrás da pizza','F14'),
 (16,'19h','Feed','L5','PIZZA FRIA NÃO TEM PERDÃO.','Entrega é parte da pizza.','Motoboy de baixo contra o céu','IA:B5'),
 (17,'08h','Story','L1','Você responde em quanto tempo?','Enquete: 1 min, 10 min, 1 hora.','Enquete','TIPO'),
 (17,'12h','Feed','L3','5 COISAS NO PERFIL QUE AFASTAM','Carrossel de erros.','Carrossel; capa com celular de perfil ruim × bom','F16'),
 (17,'19h','Feed','L6','DIAGNÓSTICO NO ZAP.','A gente olha o seu delivery com você.','Celular na mão com o zap aberto','F17'),
 (18,'08h','Story','L4','Bastidor: edição.','Do bruto ao vídeo que dá fome.','Story antes × depois do vídeo','F18'),
 (18,'12h','Feed','L1','FOTO ESCURA NÃO VENDE.','Luz de forno, não de geladeira.','Foto dividida: escura × iluminada','F19'),
 (18,'19h','Feed','L3','RESPOSTA PRONTA: "DEMORA?"','Copie e cole.','Conversa + relógio desenhado','TIPO'),
 (19,'08h','Story','L5','Calabresa ou portuguesa?','Enquete.','Enquete com 2 fatias','F20'),
 (19,'12h','Feed','L4','RELATÓRIO DE SEGUNDA','Quanto investiu, quantos pedidos, o que muda.','Notebook com relatório (ilustrativo)','F21'),
 (19,'19h','Feed','L5','AQUI CADA FATIA VENDE.','Orgulho de quem faz pizza.','Fatias voando + manchete em 2 tamanhos','F22'),
 (20,'08h','Story','L6','Black Friday? Aqui não tem desconto.','Tem 5 vagas de fundadora.','Story tipográfico com selo','TIPO'),
 (20,'12h','Feed','L6','BLACK FRIDAY SEM DESCONTO.','Em vez de desconto, condição de fundadora.','Cartaz preto com estrela amarela','TIPO'),
 (20,'19h','Feed','L1','PROMOÇÃO TODO DIA CANSA.','O cliente aprende a esperar o desconto.','Manchete gigante + pizza com etiqueta rasgada','F23'),
 (21,'08h','Story','L4','Resumo da semana.','3 coisas para fazer hoje.','Story tipográfico','TIPO'),
 (21,'12h','Feed','L5','SÁBADO É FINAL DE CAMPEONATO.','Forno no máximo.','Pizzaiolo colocando pizza no forno','F24'),
 (21,'19h','Feed','L3','CHECKLIST DE SÁBADO','Antes de abrir: link, cardápio, foto do dia.','Checklist','TIPO'),
 (22,'08h','Story','L5','Bom dia, pizzaria.','Última semana do mês.','Story com foto de pizza de cima','F25'),
 (22,'12h','Feed','L1','O CLIENTE TE ESQUECEU?','Ou você esqueceu dele?','Celular com conversa antiga','TIPO'),
 (22,'19h','Feed','L3','MENSAGEM DE VOLTA PRO CLIENTE','Copie e cole (sem spam).','Conversa de WhatsApp','TIPO'),
 (23,'08h','Story','L1','Você posta todo dia?','Enquete.','Enquete','TIPO'),
 (23,'12h','Feed','L2','O QUE UM PEDIDO A MAIS POR DIA FAZ','A conta no mês (ilustrativo).','Número gigante + calendário desenhado','TIPO'),
 (23,'19h','Feed','L4','FOTO E VÍDEO NA SUA PIZZARIA','Uma manhã de gravação, um mês de conteúdo.','Mão do pizzaiolo com farinha','F26'),
 (24,'08h','Story','L3','Dica rápida:','Fixe 3 posts no topo do perfil.','Story tipográfico','TIPO'),
 (24,'12h','Feed','L5','QUEIJO ATÉ O TETO.','Do jeito que o cliente gosta.','Queijo puxando gigante','F27'),
 (24,'19h','Feed','L6','RAIO-X: O QUE VOCÊ RECEBE','Instagram, cardápio, iFood, anúncio e Google.','Cartaz com 5 selos','TIPO'),
 (25,'08h','Story','L4','Bastidor: relatório saindo.','Segunda, 8h.','Celular com relatório','TIPO'),
 (25,'12h','Feed','L1','SEU CARDÁPIO TEM 40 SABORES?','Quem escolhe demais, desiste.','Cardápio-cartaz riscado','TIPO'),
 (25,'19h','Feed','L3','O CARDÁPIO QUE VENDE MAIS RÁPIDO','Carrossel.','Carrossel; capa com foto de cardápio digital no celular','F28'),
 (26,'08h','Story','L5','Qual o melhor dia pra pizza?','Enquete.','Enquete','TIPO'),
 (26,'12h','Feed','L6','AINDA TEM VAGA?','Condição de fundadora: veja no zap.','Contador de vagas desenhado','TIPO'),
 (26,'19h','Feed','L5','PIZZA DE SEGUNDA TAMBÉM É PIZZA.','Bora vender a semana inteira.','Pizza voando com faixa em loop','F29'),
 (27,'08h','Story','L4','Resumo do mês.','O que mudou no seu perfil?','Story tipográfico','TIPO'),
 (27,'12h','Feed','L3','10 IDEIAS DE POST PRA PIZZARIA','Salve e use.','Carrossel tipográfico','TIPO'),
 (27,'19h','Feed','L6','PRIMEIRO PASSO: RAIO-X.','R$ 297, abatido no 1º mês se fechar em 7 dias.','Pizza com estrela de preço','F30'),
 (28,'08h','Story','L5','Domingo de pizza.','Bom trabalho, pizzaiolo.','Story com foto de família comendo pizza','F31'),
 (28,'12h','Feed','L5','DOMINGO É SAGRADO.','E a pizza também.','Mesa com pizza e mãos pegando fatias','F32'),
 (28,'19h','Feed','L4','SEMANA QUE VEM TEM MAIS.','Siga @oreganoturbo.','Grade de 4 cores com manchete','TIPO'),
]
PROMPTS = {
 'F1': 'Close-up of a hand holding a smartphone showing a food delivery app order screen, a slice of pizza in the other hand, solid tomato red #C8302B background, harsh flash, hard shadow, bold campaign photography, 4:5',
 'F2': 'Extreme close-up of a cheese pull from a margherita pizza slice lifted by a hand, steam rising, solid saffron yellow #F2B33D background, harsh direct flash, 4:5',
 'F3': 'An empty open pizza box with only crumbs left, on a dark wooden table at night, single warm lamp, moody cinematic food photography, 4:5',
 'F4': 'Behind the scenes of a food photo shoot in a pizzeria kitchen: smartphone on a small tripod filming a pizza coming out of a wood-fired oven, warm light, editorial photography, 4:5',
 'F5': 'Photorealistic photo of a family table at home with an open white pizza box with a deep green lid printed with a round logo, hands grabbing slices, warm evening light, 4:5',
 'F6': 'A pepperoni pizza cut exactly in half on a split background, left half solid red, right half solid green, hard flash, overhead shot, bold campaign photography, 4:5',
 'F7': 'Top-down photo of a whole calabresa pizza with sliced onions on a solid deep green #1E5B3B background, harsh flash, hard shadow, 4:5',
 'F8': 'Close-up of a pizza box with a small printed order ticket taped on top showing the code "PZ14", kraft paper, hard flash, solid saffron background, 4:5',
 'F9': 'Three pizza slices side by side showing stuffed crusts with creamy cheese, cheddar and chocolate, solid tomato red background, overhead, hard flash, 4:5',
 'F10': 'A whole margherita pizza centered, shot from above on solid cream background, basil leaves, hard flash, sharp shadow, 4:5',
 'F11': 'Brazilian pizza chef in a deep green apron seen from below, holding a pizza peel, wood-fired oven glowing, confident pose, warm cinematic light, 4:5',
 'F12': 'Wood-fired pizza oven at dawn with first flames, a pizzeria still closed, warm and blue light mix, cinematic, 4:5',
 'F13': 'A hand holding a smartphone toward the camera with a WhatsApp chat open, pizzeria counter blurred behind, hard flash, solid green background, 4:5',
 'F14': 'A single pepperoni pizza floating on a solid saffron yellow background, slight tilt, hard flash, crisp shadow, 4:5',
 'F15': 'Delivery rider on a motorcycle holding an insulated pizza bag, shot from low angle against deep blue sky, wide-angle, bold advertising photography, 4:5',
 'F16': 'Two smartphones side by side: one showing a dark messy pizzeria Instagram profile, the other a bright appetizing one, on solid cream background, hard flash, 4:5',
 'F17': 'Close-up of a thumb about to press send on a WhatsApp message, pizza slice in the background, solid green background, flash, 4:5',
 'F18': 'Video editing timeline on a laptop screen showing pizza clips, coffee cup and pizza box beside, night office, warm light, 4:5',
 'F19': 'The same pizza photographed twice side by side: left dark and dull under fluorescent light, right bright under warm flash, split composition, 4:5',
 'F20': 'Two pizza slices facing each other: calabresa and portuguesa, solid red background, hard flash, overhead, 4:5',
 'F21': 'Laptop on a pizzeria counter showing a weekly sales report dashboard with green bars, pizza box and coffee beside it, morning light, 4:5',
 'F22': 'Several pepperoni pizza slices flying in the air with oregano flakes, solid deep green background, high-speed flash photography, 4:5',
 'F23': 'A pizza box with a torn red discount sticker, on a solid saffron background, hard flash, bold campaign photography, 4:5',
 'F24': 'Pizza chef sliding a pizza into a roaring wood-fired oven, sparks, dark background, dramatic warm light, 4:5',
 'F25': 'Overhead shot of a four-cheese pizza on a wooden peel with flour around, solid cream background, hard flash, 4:5',
 'F26': 'Close-up of a pizzaiolo hands stretching dough with flour in the air, dark background, dramatic light, 4:5',
 'F27': 'Extreme close-up of a very long cheese pull from a pizza slice lifted high, solid tomato red background, harsh flash, 4:5',
 'F28': 'Hand holding a smartphone showing a clean digital pizza menu with photos, solid saffron background, hard flash, 4:5',
 'F29': 'A pizza and slices flying with basil and tomatoes on a solid saffron yellow background, high-speed flash, 4:5',
 'F30': 'A whole pepperoni pizza with one slice lifted, solid deep green background, overhead, hard flash, 4:5',
 'F31': 'Brazilian family laughing and sharing a pizza on a Sunday at home, natural light, candid lifestyle photography, 4:5',
 'F32': 'Overhead of a table with two pizzas and many hands reaching for slices, red checkered tablecloth, flash, 4:5',
}

dt0 = datetime.date(2026, 11, 9)
DIAS = ['seg', 'ter', 'qua', 'qui', 'sex', 'sáb', 'dom']
rows = []
for (d, h, fmt, l, man, ap, comp, img) in S1 + S2_4:
    data = dt0 + datetime.timedelta(days=d - 1)
    rows.append(dict(dia=d, data=data.strftime('%d/%m'), semana_dia=DIAS[data.weekday()], hora=h, formato=fmt, linha=l, linha_nome=LINHAS[l][0], manchete=man, apoio=ap, composicao=comp, imagem=img))
json.dump(rows, open(os.path.join(D, 'calendario.json'), 'w'), ensure_ascii=False, indent=1)

md = ['# @oreganoturbo · linhas editoriais e calendário de 4 semanas (09/11 a 06/12/2026) · 3 postagens por dia',
      '',
      'Conta Leandro, 06/11/2026. Agentes: Marketing Squad, Copy Squad e Paollo (arte no padrão aprovado, `../v3/`).',
      '',
      '**Persona:** dono de pizzaria em São Luís, de 30 a 55 anos, que vive no balcão e no celular. Quer mais pedido no dia fraco e menos dependência do app.',
      '',
      '**Ritmo diário:**',
      '- **08h:** story (enquete, caixinha, bastidor ou dica rápida);',
      '- **12h:** post de feed;',
      '- **19h:** post de feed ou carrossel.',
      '',
      '**Regras:**',
      '- **Cada imagem é usada uma única vez** (pedido do Lindson, 06/11). Quando acabar, pedir mais a ele.',
      '- Sem promessa de resultado. Número de exemplo vem marcado "ilustrativo".',
      '- Preço só os aprovados: Raio-X R$ 297; condição de fundadora.',
      '- Imagem de IA leva o aviso "imagem gerada por IA".',
      '', '## Linhas editoriais', '| Linha | % | O que é |', '|---|---|---|']
md += [f'| **{k} · {v[0]}** | {v[2]} | {v[1]} |' for k, v in LINHAS.items()]
md += ['', '## Legenda da coluna "imagem"',
       '- **v3:arquivo:** peça já aprovada, em `../v3/pecas/`.',
       '- **TIPO:** arte tipográfica, sem foto. Usa só o sistema da marca: xadrez, selos, ícones, celular desenhado, cartazes.',
       '- **F1 a F32:** foto nova, a pedir ao Lindson no Gemini. Os pedidos estão em `PEDIDO-FOTOS-LOTE-2.txt`.', '']
sem = 0
for r in rows:
    s = (r['dia'] - 1) // 7 + 1
    if s != sem:
        sem = s; md += ['', f'## Semana {s}', '| Data | Hora | Formato | Linha | Manchete | Apoio | Composição | Imagem |', '|---|---|---|---|---|---|---|---|']
    md.append(f"| {r['semana_dia']} {r['data']} | {r['hora']} | {r['formato']} | {r['linha']} | **{r['manchete']}** | {r['apoio']} | {r['composicao']} | {r['imagem']} |")
open(os.path.join(D, 'CALENDARIO.md'), 'w').write('\n'.join(md) + '\n')

cab = ('PEDIDO PARA O GEMINI · Orégano Turbo · lote 2 (fotos para as semanas 2 a 4 do calendário)\n\n'
       'Gere UMA imagem para CADA item abaixo, na ordem, uma de cada vez, e escreva o código antes de cada uma (ex.: "F1"). Se parar, eu escrevo "continue".\n'
       'Regras para todas:\n'
       '- fotos ultrarrealistas de campanha de comida;\n'
       '- luz dura de flash quando o pedido diz "flash";\n'
       '- cores da marca: verde #1E5B3B, vermelho #C8302B, creme #F3EEE6, açafrão #F2B33D;\n'
       '- sem texto, sem logo e sem marca de outra empresa na imagem (o logo eu coloco depois);\n'
       '- formato 4:5 vertical.\n\n')
open(os.path.join(D, 'PEDIDO-FOTOS-LOTE-2.txt'), 'w').write(cab + ''.join(f'{k}\n{v}\n\n' for k, v in PROMPTS.items()))
tot = len(rows); tipo = sum(r['imagem'] == 'TIPO' for r in rows); v3 = sum(r['imagem'].startswith('v3:') for r in rows)
print(tot, 'postagens ·', v3, 'prontas (v3) ·', tipo, 'tipográficas ·', tot - tipo - v3, 'com foto nova')
