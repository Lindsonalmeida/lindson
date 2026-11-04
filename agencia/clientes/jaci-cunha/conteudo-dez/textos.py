# Feed de dezembro/2026 da Dra. Jaci (conta Leandro, 04/11/2026): 4 carrosséis (terças) + 6 posts, com as 14 fotos que sobraram.
# Regras: CFO (sem preço, "grátis", promessa, antes e depois, depoimento inventado; CRO-MA 8514), foto real só na 1ª e na última tela do carrossel,
# uma foto por conteúdo (../FOTOS-USADAS.md), xadrez claro/escuro continuando a grade de novembro (pos 24 em diante, par = escuro).
import json
ASS = "\n\nDra. Jaci Cunha · Cirurgiã-dentista · CRO-MA 8514\n📍 Av. Militar, em frente à Praça do Viva · Zé Doca/MA"
CARR, POST = {}, []
def car(id, data, linha, capa_foto, capa_comp, fim_foto, telas, legenda):
    CARR[id] = dict(data=data, linha=linha, capa_foto=capa_foto, capa_comp=capa_comp, fim_foto=fim_foto, telas=telas, legenda=legenda.strip() + ASS)
def post(id, data, linha, foto, comp, topo, serif, sans, legenda):
    POST.append(dict(id=id, data=data, linha=linha, tipo='post', foto=foto, comp=comp, topo=topo, serif=serif, sans=sans, roteiro=[], legenda=legenda.strip() + ASS))

car('c5', 'ter 01/12', 'Época', 'IMG_3032', 'faixas', 'IMG_3016', [
  dict(tipo='capa', topo='Dezembro chegou', serif='e as festas também...', sans='O QUE FAZER / ANTES DAS **FESTAS**'),
  dict(tipo='texto', titulo='O rosto precisa de tempo', texto='Muitos procedimentos pedem **alguns dias** para o rosto se acomodar. Deixar para a véspera tira a sua tranquilidade.'),
  dict(tipo='lista', titulo='Na avaliação, eu te digo:', itens=['O que dá para fazer **antes das festas**', 'O que é melhor deixar para **janeiro**', 'Os cuidados de cada procedimento', 'O que esperar (varia de pessoa para pessoa)']),
  dict(tipo='mito', mito='Dá para fazer **tudo** na semana do Natal.', verdade='Cada procedimento tem o seu tempo. O ideal é **planejar com antecedência**.'),
  dict(tipo='texto', titulo='A agenda de dezembro enche', texto='Fim de ano é a época mais procurada da clínica. Marque a sua **avaliação** com calma.'),
  dict(tipo='fim', serif='Cuidar com antecedência é cuidar com segurança.', sans='**Chame no WhatsApp** para sua avaliação')], """
HARMONIZAÇÃO FACIAL ANTES DAS FESTAS: O QUE FAZER EM DEZEMBRO

Dezembro chegou, e com ele as festas, as fotos com a família e as confraternizações. É também o mês em que mais chegam mensagens pedindo procedimento "para esta semana". Então vamos conversar sobre o que dá para fazer com segurança antes das festas.

📌 O rosto precisa de tempo
Muitos procedimentos da harmonização orofacial pedem alguns dias para o rosto se acomodar. Fazer na véspera tira a sua tranquilidade e o tempo de seguir os cuidados.

📌 O que eu te explico na avaliação
O que faz sentido fazer antes das festas, o que é melhor deixar para janeiro, os cuidados de cada procedimento e o que esperar, lembrando que o resultado varia de pessoa para pessoa.

📌 Mito ou verdade: dá para fazer tudo na semana do Natal?
Mito. Cada procedimento tem o seu tempo. O ideal é planejar com antecedência.

💡 Exemplo
Uma paciente queria fazer dois procedimentos juntos, três dias antes de uma festa. Conversamos e fizemos um agora e o outro em janeiro. Ela aproveitou a festa tranquila.

✅ Conclusão
Cuidar com antecedência é cuidar com segurança. A agenda de dezembro é a mais procurada do ano.

Chame no WhatsApp para sua avaliação.

#harmonizacaofacial #festasdefimdeano #esteticacomseguranca #zedoca #maranhao""")

car('c6', 'ter 08/12', 'Dúvidas', 'jaci-preto-rennova-sorrindo', 'balao', 'IMG_3011', [
  dict(tipo='capa', topo='As **PERGUNTAS** que você não faz:', serif='lábios', sans='O QUE **NINGUÉM** RESPONDE.'),
  dict(tipo='texto', titulo='1. Vai ficar exagerado?', texto='O volume é planejado para o **seu rosto**. Natural é respeitar o formato da sua boca.'),
  dict(tipo='texto', titulo='2. Incha?', texto='Pode haver **inchaço passageiro**. Eu explico todos os cuidados antes, por escrito.'),
  dict(tipo='texto', titulo='3. Quanto dura?', texto='Varia de pessoa para pessoa e do **produto** usado. Desconfie de quem promete prazo exato.'),
  dict(tipo='lista', titulo='Antes de preencher os lábios:', itens=['Avaliação do **rosto e do sorriso**', 'Saúde da boca em dia', 'Produto com **registro na Anvisa**', 'Expectativa conversada com calma']),
  dict(tipo='fim', serif='Lábio bonito é lábio que combina com você.', sans='**Chame no WhatsApp** para sua avaliação')], """
PREENCHIMENTO LABIAL: AS PERGUNTAS QUE VOCÊ PENSA MAS NÃO FAZ

O preenchimento labial é um dos procedimentos mais procurados da harmonização orofacial. E também um dos que mais geram dúvida. Separei as perguntas que muita gente pensa, mas tem vergonha de fazer.

📌 1. Vai ficar exagerado?
Não precisa. O volume é planejado para o seu rosto e para o formato da sua boca. Resultado natural é o que respeita os seus traços.

📌 2. Incha?
Pode haver um inchaço passageiro nos primeiros dias. Antes do procedimento, eu explico todos os cuidados e passo as orientações por escrito.

📌 3. Quanto tempo dura?
Varia de pessoa para pessoa e também do produto usado. Desconfie de quem promete um prazo exato para todo mundo.

📌 O que vem antes
Avaliação do rosto e do sorriso, saúde da boca em dia, produto com registro na Anvisa e uma conversa sincera sobre o que você espera.

💡 Exemplo
Muita paciente chega com a foto de uma famosa. Na avaliação, a gente adapta a ideia ao formato da boca dela. É assim que fica natural.

✅ Conclusão
Lábio bonito é lábio que combina com você. Ficou com dúvida? Pergunta aqui nos comentários.

Chame no WhatsApp para sua avaliação.

#preenchimentolabial #labiosnaturais #harmonizacaoorofacial #zedoca #maranhao""")

car('c7', 'ter 15/12', 'Dúvidas', 'IMG_3015', 'fio', 'IMG_3049', [
  dict(tipo='capa', topo='O que você precisa saber sobre', serif='Pele e sorriso nas festas', sans='COMO **CUIDAR**?'),
  dict(tipo='lista', titulo='Pele:', itens=['**Protetor solar** todo dia, com reaplicação', 'Água ao longo do dia', 'Tirar a maquiagem antes de dormir, mesmo cansada']),
  dict(tipo='lista', titulo='Sorriso:', itens=['Escovar depois dos **doces**', '**Fio dental** todos os dias', 'Cuidado com gelo e caroço']),
  dict(tipo='mito', mito='Um dia sem protetor **não faz diferença**.', verdade='O sol do Maranhão pede **protetor todo dia**, com reaplicação.'),
  dict(tipo='texto', titulo='Fez procedimento há pouco?', texto='Siga **as orientações** que eu passei por escrito e, na dúvida, me chame.'),
  dict(tipo='fim', serif='Festa boa é festa com cuidado.', sans='**Chame no WhatsApp** para sua avaliação')], """
CUIDADOS COM A PELE E O SORRISO NAS FESTAS DE FIM DE ANO

Fim de ano é sol, viagem, doce, festa até tarde e pouca hora de sono. Tudo isso aparece na pele e no sorriso. Por isso eu separei cuidados simples para você aproveitar as festas e começar o ano bem.

📌 Pele
Protetor solar todos os dias, com reaplicação, inclusive em casa de praia e no interior. Água ao longo do dia. E tirar a maquiagem antes de dormir, mesmo cansada.

📌 Sorriso
Escovar os dentes depois dos doces, usar fio dental todos os dias e ter cuidado com gelo e caroço de fruta, que podem quebrar dente e restauração.

📌 Mito ou verdade: um dia sem protetor não faz diferença?
Mito. O sol do Maranhão é forte o ano inteiro e pede protetor todo dia.

📌 Fez procedimento recente?
Siga as orientações que eu passei por escrito. Na dúvida, me chame antes de fazer qualquer coisa diferente.

💡 Exemplo
Uma paciente fez um procedimento e ia para a praia no dia seguinte. Combinamos os cuidados antes, e ela aproveitou sem susto.

✅ Conclusão
Festa boa é festa com cuidado. Salve este post e mande para quem vai viajar.

Chame no WhatsApp para sua avaliação.

#cuidadoscomapele #saudebucal #protetorsolar #zedoca #maranhao""")

car('c8', 'ter 22/12', 'Acolhimento', 'IMG_3048', 'cafe', 'IMG_3019', [
  dict(tipo='capa', topo='Antes do ano acabar:', serif='O que 2026 me ensinou', sans='sobre **cuidar** de pessoas, e não só de rostos'),
  dict(tipo='texto', titulo='1. Escutar vem primeiro', texto='Toda boa avaliação começa com uma **conversa sem pressa**.'),
  dict(tipo='texto', titulo='2. Dizer não também é cuidado', texto='Recusar um pedido que não combina com você é **respeito**.'),
  dict(tipo='texto', titulo='3. Natural é fazer certo', texto='Natural não é fazer pouco: é fazer **certo pra você**.'),
  dict(tipo='texto', titulo='4. Obrigada', texto='A cada paciente que confiou em mim e na equipe em 2026: **muito obrigada**.'),
  dict(tipo='fim', serif='Que 2027 seja de cuidado com você.', sans='**Chame no WhatsApp** para sua avaliação')], """
O QUE 2026 ME ENSINOU SOBRE CUIDAR DE PESSOAS

O ano está acabando, e eu quis parar um pouco para olhar para trás. Foram muitas avaliações, muitas conversas e muitas histórias aqui na clínica em Zé Doca. E eu aprendi coisas que vou levar para 2027.

📌 1. Escutar vem primeiro
Toda boa avaliação começa com uma conversa sem pressa. É ouvindo que eu entendo o que você deseja de verdade.

📌 2. Dizer não também é cuidado
Recusar um pedido que não combina com o seu rosto ou com o seu momento é respeito com você.

📌 3. Natural é fazer certo
Natural não é fazer pouco. É fazer certo pra você, respeitando os seus traços.

📌 4. Obrigada
A cada paciente que confiou em mim e na equipe em 2026: muito obrigada.

💡 Exemplo
Uma das mensagens mais bonitas do ano foi de uma paciente que escreveu só para dizer que se sentiu ouvida. É isso que eu quero continuar fazendo.

✅ Conclusão
Que 2027 seja um ano de cuidado com você. Me conta nos comentários: o que 2026 te ensinou?

Chame no WhatsApp para sua avaliação.

#retrospectiva2026 #gratidao #harmonizacaoorofacial #zedoca #maranhao""")

post('p1', 'sáb 05/12', 'Época', 'IMG_3027', 'tablet', 'DEZEMBRO', 'agenda', 'de **dezembro** aberta', """
AGENDA DE DEZEMBRO ABERTA: AVALIAÇÃO DE HARMONIZAÇÃO EM ZÉ DOCA

A agenda de dezembro da clínica está aberta. E como todo ano, é o mês mais procurado. Por isso eu quero te ajudar a se organizar.

📌 Por que marcar agora
Quem marca a avaliação no começo do mês tem tempo de planejar com calma, fazer o que for indicado e seguir os cuidados antes das festas.

📌 Como é a avaliação
A gente conversa sobre o que você deseja, eu analiso o seu rosto e o seu sorriso e explico o que combina com você, os cuidados e o que esperar. O resultado varia de pessoa para pessoa.

📌 Como marcar
É só chamar no WhatsApp. A equipe te passa os horários e a localização da clínica.

💡 Exemplo
Muitas pacientes deixam para a última semana e acabam sem horário. Marque a sua avaliação com antecedência e venha com calma.

✅ Conclusão
Dezembro é para aproveitar, não para correr. Marca aquela amiga que sempre deixa tudo para depois.

Chame no WhatsApp para sua avaliação.

#agendaaberta #harmonizacaofacial #avaliacaofacial #zedoca #maranhao""")

post('p2', 'sáb 12/12', 'Odonto', 'IMG_3033', 'faixa', 'Antes das fotos de fim de ano:', 'Clareamento dental?', 'primeiro, **avaliação** da saúde do seu sorriso', """
CLAREAMENTO DENTAL ANTES DAS FESTAS: O QUE SABER PRIMEIRO

Fim de ano é época de foto. E muita gente lembra do clareamento dental justamente agora. Antes de qualquer coisa, eu preciso te contar o que vem primeiro.

📌 Primeiro, a saúde do sorriso
Antes do clareamento, eu avalio a saúde da sua boca: gengiva, cáries, restaurações e sensibilidade. Clarear um dente que precisa de outro cuidado não é o caminho.

📌 Cada caso tem um caminho
Existem formas diferentes de clareamento, e a indicação depende da avaliação. O resultado varia de pessoa para pessoa.

📌 Cuidado com o "clareamento caseiro"
Produtos e receitas sem orientação podem causar sensibilidade e machucar a gengiva. Clareamento é tratamento e precisa de acompanhamento.

💡 Exemplo
Uma paciente queria clarear para o Natal. Na avaliação, vimos que precisava cuidar de uma restauração antes. Fizemos na ordem certa, com segurança.

✅ Conclusão
Sorriso bonito é sorriso saudável. Antes de clarear, avalie.

Chame no WhatsApp para sua avaliação.

#clareamentodental #odontologiaestetica #dentista #zedoca #maranhao""")

post('p3', 'sáb 19/12', 'Autoridade', 'IMG_3045', 'frases', 'O que eu mais desejo pra você:', 'natural, sempre', 'a tendência que **nunca** sai de moda', """
HARMONIZAÇÃO NATURAL: A TENDÊNCIA QUE NUNCA SAI DE MODA

Todo ano aparece uma tendência nova na estética. Um formato de lábio, um tipo de contorno, um "efeito" que viraliza. E todo ano eu repito a mesma coisa: o que nunca sai de moda é o natural.

📌 Por que fugir da tendência
O que está em alta hoje pode não combinar com o seu rosto, e daqui a um tempo pode parecer datado. O seu rosto não precisa seguir a moda.

📌 O que é natural para mim
É respeitar os seus traços, a sua idade e o seu jeito de se expressar. É você se olhar no espelho e se reconhecer.

📌 Segurança em primeiro lugar
Natural também é escolher com calma: avaliação, produto com registro na Anvisa e profissional habilitado. O resultado varia de pessoa para pessoa.

💡 Exemplo
Uma paciente chegou pedindo o lábio que estava em alta. Na conversa, entendemos que ela queria só mais definição. Saiu com um plano do jeito dela.

✅ Conclusão
Natural, sempre. Com segurança e do seu jeito.

Chame no WhatsApp para sua avaliação.

#harmonizacaonatural #belezanatural #esteticafacial #zedoca #maranhao""")

post('p4', 'sex 25/12', 'Natal', 'IMG_3043', 'fio', '25 de dezembro', 'Feliz Natal', 'COM **CARINHO**, DRA. JACI E EQUIPE', """
FELIZ NATAL: UMA MENSAGEM DA DRA. JACI E DA EQUIPE

Hoje é Natal, e a nossa mensagem é de gratidão. Obrigada a cada paciente, seguidora e família que confiou na clínica este ano.

📌 O que o Natal lembra
Que cuidar é um gesto de amor: com quem a gente ama e com a gente mesma.

📌 O nosso desejo
Que a sua noite seja leve, com a família reunida, boa conversa e muitos sorrisos, daqueles de boca aberta nas fotos.

📌 Um cuidado de presente
Se você exagerar nos doces, lembra de escovar os dentes antes de dormir. A dentista aqui não podia deixar de avisar.

💡 Exemplo
Este ano, muitas pacientes viraram amigas. É por elas e por vocês que a gente abre as portas com carinho todos os dias.

✅ Conclusão
Feliz Natal, com carinho, Dra. Jaci e equipe. Em janeiro, a gente se vê: chame no WhatsApp para sua avaliação.

#feliznatal #natal2026 #clinicadrajacicunha #zedoca #maranhao""")

post('p5', 'qua 30/12', 'Acolhimento', 'IMG_3034', 'invertido', 'FIM DE ANO', 'Recesso e agenda de janeiro', 'confira os **horários** no WhatsApp', """
RECESSO DE FIM DE ANO E AGENDA DE JANEIRO DA CLÍNICA

O ano está fechando, e a equipe também vai descansar um pouco para voltar com tudo em 2027. Por isso, fique atenta aos horários de fim de ano.

📌 Recesso
Os dias de atendimento e de recesso de fim de ano estão no WhatsApp da clínica. É só chamar que a equipe te passa tudo.

📌 Agenda de janeiro
Janeiro é um ótimo mês para começar o ano cuidando de você, com calma e sem a correria das festas. A agenda de avaliações já pode ser reservada.

📌 Fez procedimento em dezembro?
Siga as orientações por escrito. Se tiver qualquer dúvida no recesso, mande mensagem no WhatsApp.

💡 Exemplo
Muitas pacientes preferem deixar para janeiro os procedimentos que pedem mais tempo de recuperação. É uma ótima escolha.

✅ Conclusão
Descanse, aproveite e conte com a gente em 2027.

Chame no WhatsApp para sua avaliação.

#recesso #agendajaneiro #harmonizacaofacial #zedoca #maranhao""")

post('p6', 'qui 31/12', 'Réveillon', 'IMG_3029', 'balao', 'Que venha **2027**:', '2027', 'com **cuidado**, sempre', """
FELIZ 2027: QUE O NOVO ANO SEJA DE CUIDADO COM VOCÊ

Último dia do ano. Hora de agradecer o que passou e desejar o que vem. E o meu desejo para você é simples: que 2027 seja um ano de cuidado com você.

📌 Cuidar não é vaidade
É saúde, autoestima e respeito com a sua história. Do sorriso à pele, cuidar de você é um presente que você se dá.

📌 Para começar bem
Que tal colocar na lista de metas uma consulta de rotina com o dentista? A saúde da boca diz muito sobre a saúde do corpo.

📌 Obrigada, 2026
Obrigada a cada paciente e seguidora que fez parte deste ano com a clínica em Zé Doca.

💡 Exemplo
Muitas pacientes me contam que a meta do ano era "voltar a sorrir nas fotos". Que 2027 seja o seu ano de sorrir de boca aberta.

✅ Conclusão
Feliz 2027, com cuidado, sempre.

Chame no WhatsApp para sua avaliação.

#feliz2027 #anonovo #autocuidado #zedoca #maranhao""")

ORDEM = ['c5', 'p1', 'c6', 'p2', 'c7', 'p3', 'c8', 'p4', 'p5', 'p6']   # continua a grade de novembro (23 posts): começa no 24 (par = escuro)
for p in POST: p['pos'] = 24 + ORDEM.index(p['id']); p['tom'] = 'claro' if p['pos'] % 2 else 'escuro'
for k, c in CARR.items(): c['pos'] = 24 + ORDEM.index(k); c['tom'] = 'claro' if c['pos'] % 2 else 'escuro'
json.dump(POST, open('textos.json', 'w'), ensure_ascii=False, indent=1)
json.dump(CARR, open('carrosseis.json', 'w'), ensure_ascii=False, indent=1)
fotos = [p['foto'] for p in POST] + [c['capa_foto'] for c in CARR.values()] + [c['fim_foto'] for c in CARR.values()]
assert len(fotos) == len(set(fotos)) == 14, fotos
for x in POST + list(CARR.values()):
    l = x['legenda']; assert len(l) <= 2200 and not any(w in l.lower() for w in ['grátis', 'gratuit', 'r$', 'garant', 'promoç'])
md = ['# Dra. Jaci · feed de dezembro/2026 (conta Leandro, 04/11/2026)\n\nOrdem na grade: ' + ' → '.join(ORDEM) + '\n']
for k in ORDEM:
    x = CARR.get(k) or next(p for p in POST if p['id'] == k)
    md.append(f"\n## {k} · {x['data']} · {x['linha']} · {'Carrossel 6 telas' if k in CARR else 'Post'} · tom {x['tom']}\n")
    if k in CARR:
        md.append(f"Fotos: capa {x['capa_foto']} · última tela {x['fim_foto']} (meio sem foto, tipográfico)\n\n" + ''.join(f"- Tela {i+1} ({t['tipo']}): " + ' / '.join(str(v) for kk, v in t.items() if kk != 'tipo') + '\n' for i, t in enumerate(x['telas'])))
    else: md.append(f"Foto: {x['foto']} · {x['topo']} / {x['serif']} / {x['sans']}\n")
    md.append(f"\n**Legenda** ({len(x['legenda'])} caracteres)\n\n```\n{x['legenda']}\n```\n")
open('TEXTOS.md', 'w').write(''.join(md)); print('ok', len(POST), len(CARR))
