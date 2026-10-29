"""Conversa com o ouvinte nos vídeos longos do Raposa e Leão.
python3 conversa_longos.py [NN ...]  -> longos/NN/roteiro.json a partir de longos/NN/roteiro_v1.json (original guardado)
Cada vídeo tem falas próprias: check-in, pergunta para os comentários, convite a seguir no momento de valor,
salvar ou mandar para alguém. Também troca os textos que eram iguais em todos (inscreva, compromisso e fim)."""
import json, os, shutil, sys
D = os.path.dirname(os.path.abspath(__file__)); RAIZ = os.path.join(D, '..')
IMG = sorted([f'../img/{f}' for f in os.listdir(RAIZ + '/img') if f.endswith('.jpg')] + [f'../img/hist/{f}' for f in os.listdir(RAIZ + '/img/hist')])

def cv(tipo, txt, h, x): return dict(tela=dict(t='conversa', tipo=tipo, h=h, x=x), txt=txt)
L = {}
# antes: [(índice no roteiro original, segmento)]; troca: {tipo de tela: (texto falado, campos da tela)}
L['01'] = dict(antes=[
    (10, cv('checkin', 'Antes da lição dois, uma pergunta rápida: hoje você está mais pra raposa ou pra leão? Guarda essa resposta, porque as próximas lições vão mexer com ela.', 'Raposa ou leão?', 'GUARDEI')),
    (19, cv('comenta', 'Pausa pra você. Das três lições até aqui, qual delas você já viu acontecer na sua vida? Escreve o número nos comentários: um, dois ou três.', 'Qual você já viveu?', 'A LIÇÃO 3')),
    (23, cv('segue', 'Se essas lições estão fazendo sentido pra você, aproveita e se inscreve no canal agora. Ainda tem três lições pela frente, e a próxima derruba uma frase que todo mundo repete.', 'Ainda tem<br>3 lições', 'TOCA AQUI')),
    (30, cv('checkin', 'Tá comigo até aqui? Se tá, escreve tô junto nos comentários. Falta só a última, e ela é sobre o que você faz quando tudo está calmo.', 'Tá comigo?', 'TÔ JUNTO')),
    (35, cv('manda', 'Antes de terminar, pensa numa pessoa que precisava ouvir pelo menos uma dessas lições hoje. Manda esse vídeo pra ela.', 'Quem precisa<br>ouvir isso?', 'MANDA PRA ELA'))])
L['02'] = dict(antes=[
    (10, cv('checkin', 'Deixa eu te perguntar uma coisa: você se reconheceu nesse primeiro erro? Se sim, fica até o fim, porque a saída está na última parte.', 'Se reconheceu?', 'ME RECONHECI')),
    (19, cv('comenta', 'Até agora foram três erros. Qual deles você mais comete? Comenta: um, dois ou três. Sem vergonha, todo mundo comete algum.', 'Qual você<br>mais comete?', 'O ERRO 2')),
    (27, cv('segue', 'Se você é uma pessoa boa cansada de sair perdendo, se inscreve no canal. Agora vem a parte mais importante do vídeo.', 'Agora, a parte<br>mais importante', 'TOCA AQUI')),
    (32, cv('comenta', 'Me responde nos comentários: o que você vai fazer diferente a partir de amanhã, sem deixar de ser uma pessoa boa?', 'O que muda<br>amanhã?', 'PARAR DE DAR TUDO'))])
L['03'] = dict(antes=[
    (10, cv('checkin', 'Tá conseguindo acompanhar a subida dele? Guarda o nome Ramiro de Orco, porque a próxima parte é das mais fortes dessa história.', 'Guarda<br>esse nome', 'GUARDEI')),
    (15, cv('comenta', 'E aí, o que você achou da jogada de Cesena? Inteligente ou cruel demais? Escreve nos comentários.', 'Inteligente<br>ou cruel?', 'OS DOIS')),
    (21, cv('segue', 'Se você gosta de histórias reais como essa, se inscreve no canal. Agora vem a queda, e ela ensina mais do que a subida.', 'Agora,<br>a queda', 'TOCA AQUI')),
    (28, cv('checkin', 'Respira um segundo. Tudo que ele construiu caiu em poucos meses. Antes das lições, pensa: o que na sua vida depende de força emprestada?', 'Força<br>emprestada?', 'PENSEI'))])
L['04'] = dict(antes=[
    (10, cv('checkin', 'Duas regras até aqui. Tá anotando? Se não, pega um papel agora, porque ainda vêm mais oito.', 'Pega um papel', 'ANOTANDO')),
    (17, cv('comenta', 'Treino vence talento. Você concorda? Responde nos comentários: concordo ou discordo, e diz o porquê.', 'Concorda?', 'CONCORDO')),
    (23, cv('segue', 'Metade das regras já foi. Se elas estão servindo pra você, se inscreve no canal, e vamos pra regra sete.', 'Metade<br>já foi', 'TOCA AQUI')),
    (29, cv('checkin', 'Qual dessas regras você mais quebra no dia a dia? Pensa nela enquanto a gente fecha as últimas.', 'Qual você<br>mais quebra?', 'A REGRA 2'))])
L['05'] = dict(antes=[
    (8, cv('checkin', 'Surpreso? É o mesmo Maquiavel do Príncipe. Fica comigo, que vai ficar ainda mais interessante.', 'O mesmo<br>Maquiavel?', 'SURPRESO')),
    (12, cv('comenta', 'Na sua casa ou no seu trabalho, discussão fortalece ou destrói? Conta nos comentários.', 'Fortalece<br>ou destrói?', 'DEPENDE DA REGRA')),
    (21, cv('segue', 'Se você está descobrindo um Maquiavel que não conhecia, se inscreve no canal. Ainda faltam duas lições e a pergunta final.', 'Faltam<br>2 lições', 'TOCA AQUI')),
    (29, cv('checkin', 'Pausa rápida: qual dessas lições você vai levar pra sua vida? Guarda a resposta, que agora vem a pergunta que muita gente faz.', 'Qual você leva?', 'VOLTAR ÀS ORIGENS'))])
L['06'] = dict(antes=[
    (16, cv('checkin', 'Tá comigo até aqui? Faz o teste de cabeça: a pessoa que mais te aconselha pensa mais em você ou nela mesma?', 'Ela pensa<br>em quem?', 'FIZ O TESTE')),
    (28, cv('comenta', 'Me conta nos comentários: você tem alguém que te fala a verdade sem medo? Se tem, escreve só: eu tenho.', 'Você tem<br>essa pessoa?', 'EU TENHO')),
    (38, cv('checkin', 'Essa lição incomoda, eu sei. Se você se reconheceu um pouco nela, tudo bem. Reconhecer é o primeiro passo.', 'Se reconheceu?', 'UM POUCO'))],
    troca=dict(
        inscreva=('Antes de seguir, me diz uma coisa: tem alguém na sua vida que só concorda com você? Guarda esse nome. E se você quer aprender a se proteger disso, se inscreve no canal agora.', dict(tag='GUARDA ESSE NOME', s='E se inscreve para aprender a se proteger.')),
        compromisso=('Agora, um compromisso só seu. Escolhe as cinco pessoas que mais te aconselham e faz o teste ainda esta semana. Se você vai fazer, escreve nos comentários: vou fazer o teste.', dict(h='Comenta: <b>VOU FAZER O TESTE</b>', digita='VOU FAZER O TESTE')),
        fim=('Bajulação é um veneno doce, e agora você tem o antídoto. Se esse vídeo te ajudou, se inscreve no Raposa e Leão e manda pra alguém que vive cercado de gente que só diz sim.', dict(s='Mande para quem vive cercado de sim.'))))
L['07'] = dict(antes=[
    (8, cv('checkin', 'Tá fazendo sentido? Agora vem a parte que ninguém conta, e é ela que separa o líder respeitado do tirano.', 'A parte que<br>ninguém conta', 'TÔ AQUI')),
    (12, cv('comenta', 'Pensa num chefe, num pai ou numa mãe que você respeitou muito. Era temido, amado ou os dois? Conta nos comentários.', 'Temido, amado<br>ou os dois?', 'OS DOIS')),
    (18, cv('checkin', 'Aníbal ou Cipião: com qual dos dois você se parece mais hoje? Responde pra você mesmo.', 'Aníbal ou<br>Cipião?', 'CIPIÃO'))],
    troca=dict(
        inscreva=('Antes da resposta completa, me diz: no seu trabalho, você é mais amado ou mais temido? Guarda isso. E se inscreve no canal, porque a resposta de Maquiavel vai te surpreender.', dict(tag='AMADO OU TEMIDO?', s='Guarda a resposta e se inscreve.')),
        compromisso=('Agora é com você. Escreve hoje as suas três regras inegociáveis, aquelas que ninguém atravessa. Se você vai escrever, comenta: minhas três regras.', dict(h='Comenta: <b>MINHAS 3 REGRAS</b>', digita='MINHAS 3 REGRAS')),
        fim=('Maquiavel não ensina a ser cruel. Ensina a não ser fraco. Se essa resposta te ajudou, se inscreve no Raposa e Leão e me conta nos comentários qual lição você vai usar primeiro.', dict(s='Qual lição você vai usar primeiro?'))))
L['08'] = dict(antes=[
    (8, cv('checkin', 'Tá visualizando o rio? Agora olha pra sua vida: onde estão os seus diques?', 'Onde estão<br>seus diques?', 'PRECISO DE MAIS')),
    (13, cv('comenta', 'Me conta nos comentários qual crise te pegou sem dique. Pode ser só uma palavra: emprego, saúde, dinheiro.', 'Qual crise<br>te pegou?', 'DINHEIRO')),
    (19, cv('checkin', 'Essa última lição é forte, né? O jeito que te trouxe até aqui pode não ser o que te leva adiante. Respira e pensa nisso.', 'O que precisa<br>mudar?', 'PENSEI'))],
    troca=dict(
        inscreva=('Antes de continuar, responde só pra você: na última crise que você passou, você estava preparado? Se a resposta for não, esse vídeo é pra você. Se inscreve no canal pra não perder as próximas lições.', dict(tag='VOCÊ ESTAVA PREPARADO?', s='Se inscreve e continua comigo.')),
        compromisso=('Agora, o seu compromisso. Qual dique você vai começar esta semana: reserva, habilidade ou relacionamento? Escreve nos comentários o nome do seu dique.', dict(h='Comenta: <b>MEU DIQUE É…</b>', digita='MEU DIQUE É A RESERVA')),
        fim=('A sorte é um rio. Você decide se vai ser a planície ou o dique. Se esse vídeo te fez pensar, se inscreve no Raposa e Leão e salva ele pra rever na próxima tempestade.', dict(s='Salve para a próxima tempestade.'))))
L['09'] = dict(antes=[
    (8, cv('checkin', 'Dá pra imaginar uma cidade inteira queimando os próprios objetos de valor? Tá acompanhando? Agora começa a queda.', 'Agora,<br>a queda', 'TÔ ACOMPANHANDO')),
    (13, cv('comenta', 'Você já viu alguém muito admirado cair de uma hora pra outra? Conta nos comentários, sem citar nomes.', 'Já viu alguém<br>cair assim?', 'JÁ, NO TRABALHO')),
    (19, cv('checkin', 'Profeta desarmado. Guarda essa expressão, porque ela serve pra muita coisa na sua vida.', 'Profeta<br>desarmado', 'GUARDEI'))],
    troca=dict(
        inscreva=('Antes de contar essa história, um pedido: se você gosta de histórias reais que ensinam sobre poder, se inscreve no canal. E presta atenção no jovem que assistiu a tudo da praça.', dict(tag='PRESTA ATENÇÃO NELE', s='Histórias reais que ensinam sobre poder.')),
        compromisso=('E agora o seu compromisso: qual projeto seu hoje depende só de entusiasmo? Escreve nos comentários: vou dar estrutura, e diz qual é o projeto.', dict(h='Comenta: <b>VOU DAR ESTRUTURA</b>', digita='VOU DAR ESTRUTURA')),
        fim=('Savonarola tinha a voz. Faltou a estrutura. Se essa história te ensinou algo, manda pra alguém que tem uma ótima ideia e nenhum plano. E se inscreve no Raposa e Leão.', dict(s='Mande para quem tem ideia sem plano.'))))
L['10'] = dict(antes=[
    (8, cv('checkin', 'Tá vendo como ele subiu? Agora segura, porque a queda foi rápida.', 'Agora,<br>a queda', 'SEGUREI')),
    (12, cv('comenta', 'Você já perdeu algo que parecia garantido? Se quiser, conta nos comentários. Quem passou por isso vai se identificar.', 'Já perdeu<br>algo assim?', 'MEU EMPREGO')),
    (18, cv('checkin', 'Essa parte é forte. Um homem na pior fase da vida, vestindo a melhor roupa pra estudar. Você faria isso?', 'Você faria isso?', 'FARIA'))],
    troca=dict(
        inscreva=('Essa é uma história de recomeço. Se você está passando por uma fase difícil, fica até o fim, e se inscreve no canal pra acompanhar as próximas.', dict(tag='FASE DIFÍCIL?', s='Fica até o fim.')),
        compromisso=('E agora é a sua vez. Se você está numa fase de perda ou de recomeço, separa a sua hora de estudo a partir de amanhã. Se você vai separar, escreve nos comentários: minha hora começa amanhã.', dict(h='Comenta: <b>MINHA HORA COMEÇA AMANHÃ</b>', digita='MINHA HORA COMEÇA AMANHÃ')),
        fim=('Maquiavel perdeu tudo e escreveu o livro que o tornou eterno. Se essa história te deu força, salva esse vídeo pra assistir de novo num dia difícil, e se inscreve no Raposa e Leão.', dict(s='Salve para um dia difícil.'))))
L['11'] = dict(antes=[
    (7, cv('checkin', 'Faz sentido até aqui? O primeiro erro é o mais fácil de ver. O segundo é mais traiçoeiro.', 'Agora, o erro<br>traiçoeiro', 'FAZ SENTIDO')),
    (11, cv('comenta', 'O líder que você pensou no começo cometeu qual dos dois erros: ódio ou desprezo? Escreve nos comentários.', 'Ódio ou<br>desprezo?', 'DESPREZO')),
    (17, cv('checkin', 'Impressionante, né? Imperadores fortes caindo pelos mesmos dois motivos. Agora, a defesa.', 'Agora,<br>a defesa', 'QUERO SABER'))],
    troca=dict(
        inscreva=('Antes do primeiro erro: pensa num líder que você viu cair. Guarda esse exemplo, e se inscreve no canal pra entender o que aconteceu com ele.', dict(tag='PENSE NUM LÍDER QUE CAIU', s='Guarda o exemplo e se inscreve.')),
        compromisso=('Agora, o compromisso. Faz hoje a revisão das duas perguntas sobre você mesmo. Se você vai fazer, escreve nos comentários: vou me revisar.', dict(h='Comenta: <b>VOU ME REVISAR</b>', digita='VOU ME REVISAR')),
        fim=('Evite o ódio, evite o desprezo, e fica muito mais difícil alguém te derrubar. Se você lidera alguém, em casa ou no trabalho, manda esse vídeo pra outra pessoa que lidera. E se inscreve no Raposa e Leão.', dict(s='Mande para quem lidera.'))))

def aplica(nn):
    P = f'{RAIZ}/longos/{nn}'; v1 = P + '/roteiro_v1.json'
    if not os.path.exists(v1): shutil.copy(P + '/roteiro.json', v1)
    r = json.load(open(v1)); seg = r['seg']; cfg = L[nn]
    for tp, (txt, campos) in cfg.get('troca', {}).items():
        for g in seg:
            if g['tela']['t'] == tp: g['txt'] = txt; g['tela'].update(campos)
    for n, (i, s) in enumerate(sorted(cfg['antes'], key=lambda x: -x[0])):
        s = json.loads(json.dumps(s)); s['tela']['img'] = IMG[(int(nn) * 5 + n * 3) % len(IMG)]; seg.insert(i, s)
    json.dump(r, open(P + '/roteiro.json', 'w'), ensure_ascii=False, indent=1)
    print(nn, len(seg), 'segmentos,', sum(1 for g in seg if g['tela']['t'] == 'conversa'), 'conversas')

for nn in (sys.argv[1:] or sorted(L)): aplica(nn)
