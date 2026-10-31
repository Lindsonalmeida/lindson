"""Conversa com o ouvinte: insere em cada roteiro do pintura.json os momentos em que o narrador fala direto com quem assiste
(check-in, pergunta para comentar ligada ao que acabou de aprender, seguir, salvar, mandar para alguém) e o balão na tela.
Cada fala é única daquele vídeo. Rodar de novo é seguro: tira as falas antigas antes de pôr as novas.
python3 conversa.py"""
import json, os
D = os.path.dirname(os.path.abspath(__file__)); ARQ = os.path.join(D, '..', 'pintura.json')

# INS: (inserir antes da cena nº, gravura, movimento, fala, tipo, texto do balão) — índices do roteiro original
INS = {
 'pv-01': [(4, '085', 'out', 'Para um segundo. Você já foi traído por alguém que comia na sua mesa? Se já, você entende essa noite. Deixa um coração aqui embaixo, só isso.', 'comenta', 'Já passou por isso? Deixa um coração'),
           (9, '092', 'cima', 'Se essa semana mexeu com você, segue o Passaporte. Toda semana tem uma nova parada da Bíblia explicada assim.', 'segue', 'Toda semana, uma nova parada')],
 'short-01': [(4, '049', 'in', 'Até aqui faz sentido? Então me conta nos comentários: qual livro você tentou ler e travou?', 'comenta', 'Qual livro te travou?')],
 'short-02': [(5, '063', 'esq', 'Você já leu algum Evangelho inteiro? Responde aqui: sim, ou ainda não. Sem vergonha nenhuma.', 'comenta', 'Já leu um Evangelho inteiro?')],
 'short-03': [(6, '053', 'dir', 'Tá comigo até aqui? Levítico parecia só regra, né? Se mudou alguma coisa na sua cabeça, escreve: mudou.', 'checkin', 'Escreve: mudou')],
 'short-04': [(4, '046', 'out', 'Seja sincero comigo: em que dia do plano você parou? Escreve o número aqui. Ninguém vai te julgar.', 'comenta', 'Em que dia você parou?')],
 'short-05': [(5, '063', 'in', 'Qual dessas você vai testar hoje: sentado, em voz alta ou mais cedo? Escolhe uma e me conta.', 'comenta', 'Sentado, em voz alta ou mais cedo?')],
 'short-06': [(6, '024', 'esq', 'Você tem alguém na vida que é tipo Rute pra você? Marca essa pessoa aqui nos comentários.', 'comenta', 'Marca a sua Rute')],
 'short-07': [(7, '044', 'in', 'Pensa nessa pergunta antes de passar pro próximo vídeo. Se quiser, responde aqui embaixo.', 'comenta', 'Quem você não quer ver perdoado?')],
 'short-08': [(4, '053', 'out', 'Até aqui são três paradas. Tá conseguindo guardar? Escreve um, dois, três nos comentários, e vamos pra parte mais importante.', 'checkin', 'Escreve: 1, 2, 3')],
 'short-09': [(5, '061', 'dir', 'Você pulava essas listas? Fala a verdade. Quase todo mundo pula. Comenta: pulava.', 'comenta', 'Você pulava as listas?')],
 'short-10': [(4, '053', 'in', 'Respira. Até aqui ficou menos assustador? Escreve: menos medo. Agora vem a melhor parte.', 'checkin', 'Escreve: menos medo')],
 'short-11': [(4, '021', 'out', 'Para aqui um segundo. Você também já brincou com um limite que sabia que não devia? Responde só pra você, ou escreve aqui: já.', 'comenta', 'Já brincou com um limite?')],
 'short-12': [(6, '036', 'esq', 'Me conta: você tem um horário fixo com Deus? Manhã, tarde ou noite? Escreve aqui o seu.', 'comenta', 'Manhã, tarde ou noite?')],
 'short-13': [(5, '049', 'in', 'Hoje é dia de qual capítulo? Olha o calendário e escreve o número aqui. Vamos ler juntos.', 'comenta', 'Hoje é dia de qual capítulo?')],
 'short-14': [(5, '063', 'in', 'Antes da resposta de Jesus, pensa: você seria quem nessa história? O sacerdote, o levita ou o samaritano? Responde aqui.', 'comenta', 'Você seria quem nessa história?')],
 'short-15': [(5, '053', 'out', 'Agora imagina estar no lugar de José. Você perdoaria? Escreve sim ou não. A resposta dele vem agora.', 'comenta', 'Você perdoaria?')],
 'short-16': [(7, '061', 'in', 'E você, como está hoje, de verdade? Se estiver cansado, escreve só: tô cansado. A gente ora por você.', 'comenta', 'Como você está hoje?')],
 'short-17': [(4, '053', 'dir', 'Tá acompanhando? Os ossos já têm pele, mas falta uma coisa. Escreve o que você acha que falta, e eu te mostro.', 'comenta', 'O que falta nesses ossos?')],
 'short-18': [(5, '053', 'esq', 'Respira. Esse capítulo é pesado mesmo. Tá comigo até aqui? Escreve: tô junto. Agora vem a virada.', 'checkin', 'Escreve: tô junto')],
 'short-19': [(6, '053', 'in', 'E você? Qual é o vento que está tirando o seu foco agora? Escreve uma palavra só.', 'comenta', 'Qual é o seu vento?')],
 'short-20': [(5, '049', 'out', 'Qual desses salmos você precisa hoje? Escreve o número aqui, e lê ele ainda hoje.', 'comenta', 'Qual salmo você precisa hoje?')],
 'longo-01': [(11, '053', 'esq', 'Primeira parada feita. Tá comigo até aqui? Se a ideia da biblioteca fez sentido pra você, escreve nos comentários: biblioteca. E bora pro mapa.', 'checkin', 'Escreve: biblioteca'),
              (25, '063', 'out', 'Antes da grande história, me conta: em qual dessas regiões você mais lê hoje? Lei, Profetas, Evangelhos ou Cartas? Escreve aqui.', 'comenta', 'Qual região você mais lê?'),
              (36, '092', 'in', 'Se até aqui esse vídeo já clareou alguma coisa pra você, segue o canal. Toda semana tem uma parada nova.', 'segue', 'Uma parada nova por semana'),
              (48, '053', 'dir', 'Respira um pouco. Foi bastante coisa, né? Se bateu cansaço, tudo bem: salva o vídeo e volta depois. Se tá firme, vamos pra última parada.', 'salva', 'Cansou? Salva e volta depois')],
 'longo-02': [(18, '053', 'in', 'Primeira rota apresentada. Tá fazendo sentido até aqui? Se a Primeira Viagem é a sua cara, escreve: primeira. Mas espera as outras duas antes de decidir.', 'checkin', 'Escreve: primeira'),
              (24, '063', 'esq', 'Quem aqui já tentou ler na ordem das páginas e parou no meio? Levanta a mão nos comentários. Escreve: eu.', 'comenta', 'Já parou no meio? Escreve: eu'),
              (36, '092', 'out', 'Se você está gostando de ver a Bíblia como viagem, segue o canal. Toda semana a gente atravessa um trecho junto.', 'segue', 'Toda semana, um trecho juntos'),
              (44, '053', 'dir', 'Me conta uma coisa: você já largou a leitura por culpa? Escreve só: já larguei. Você não está sozinho nessa.', 'comenta', 'Já largou por culpa?')],
 'longo-04': [(8, '053', 'esq', 'Antes de começar: qual Evangelho você acha que é a sua cara? Chuta aqui nos comentários. No fim você confere.', 'comenta', 'Chuta: qual é o seu?'),
              (16, '063', 'out', 'Mateus fechado. Tá comigo até aqui? Escreve: rei. Agora vem o mais rápido dos quatro.', 'checkin', 'Escreve: rei'),
              (32, '092', 'in', 'Três Evangelhos vistos. Se está valendo a pena, segue o canal, que ainda vem a resposta do título.', 'segue', 'Ainda vem a resposta'),
              (42, '053', 'dir', 'Você já reparou alguma diferença lendo os Evangelhos? Conta aqui qual foi. Essas descobertas ajudam muita gente.', 'comenta', 'Qual diferença você já notou?'),
              (49, '061', 'in', 'Tem alguém que quer começar a ler a Bíblia e não sabe por onde? Manda esse vídeo. Essa ordem pode ajudar.', 'manda', 'Manda pra quem quer começar')],
}
# balão em cenas que já falam com o ouvinte (e troca da fala quando melhora a conversa)
MARCA = {
 'short-02': {6: ('salva', 'Lê Marcos 1 hoje', 'Salva esse vídeo e volta amanhã pra me contar se leu Marcos 1.')},
 'short-04': {6: ('segue', 'Amanhã tem mais uma parada', 'Segue o canal. Amanhã tem mais uma parada pra você continuar sem culpa.')},
 'short-06': {7: ('manda', 'Manda pra sua Rute', 'Manda esse vídeo pra essa pessoa. Ela vai gostar de saber.')},
 'short-07': {7: ('segue', 'Próxima viagem: outro profeta', 'Segue o canal pra próxima viagem.')},
 'short-09': {6: ('salva', 'Salva pra quando chegar em 1 Crônicas', 'Salva esse vídeo. Quando chegar em 1 Crônicas, você vai lembrar dele.')},
 'short-10': {7: ('segue', 'Não perde a próxima viagem', 'Segue o Passaporte pra não perder a próxima viagem pela Bíblia.')},
 'short-11': {6: ('segue', 'Segue pra próxima viagem', None)},
 'short-13': {6: ('salva', 'Lê o capítulo de hoje', None)},
 'short-14': {6: ('segue', 'Segue pra próxima viagem', None)},
 'short-16': {7: ('manda', 'Manda pra quem está cansado', None)},
 'short-19': {7: ('salva', 'Salva pra lembrar amanhã', None)},
 'short-20': {6: ('salva', 'Salva pra quando precisar', None)},
 'longo-01': {4: ('segue', 'Primeira viagem? Se inscreve', None), 55: ('comenta', 'Fez as 3 perguntas? Conta aqui', None)},
 'longo-02': {4: ('segue', 'Se inscreve antes de embarcar', None), 52: ('comenta', 'VOU EMBARCAR + sua rota', None)},
}
# gancho com pergunta aberta (fechada mais adiante no vídeo)
ABRE = {
 'pv-01': 'Domingo. Jerusalém recebe Jesus com ramos nas mãos e gritos de hosana. Em cinco dias, essa mesma cidade ia gritar outra coisa.',
 'short-01': 'Você lê a Bíblia e não entende nada? Calma. O problema pode não ser você. E no fim eu te dou a pergunta que muda a leitura.',
 'short-11': 'Sansão matou um leão com as próprias mãos. E mesmo assim perdeu tudo. Fica até o fim que eu te conto onde estava a fraqueza dele.',
 'short-15': 'José era o filho preferido de Jacó. Ganhou até uma túnica especial. Os irmãos não aguentaram. E o fim dessa história ninguém esperava.',
}

d = json.load(open(ARQ))
PROPRIOS = {os.path.basename(f)[:-5] for f in __import__('glob').glob(os.path.join(D, '..', 'roteiros', 'longo-*.json'))}  # já trazem a conversa
for v in d:
    if v['id'] in PROPRIOS: continue
    k = v['id']; cs = [c for c in v['cenas'] if not c.get('conv')]
    for c in cs:
        if 'txt0' in c: c['txt'] = c.pop('txt0')
        c.pop('interage', None)
    for i, (tp, bal, novo) in MARCA.get(k, {}).items():
        cs[i]['interage'] = dict(tipo=tp, txt=bal)
        if novo: cs[i]['txt0'] = cs[i]['txt']; cs[i]['txt'] = novo
    if k in ABRE: cs[0]['txt0'] = cs[0]['txt']; cs[0]['txt'] = ABRE[k]
    for i, g, mov, fala, tp, bal in sorted(INS.get(k, []), key=lambda x: -x[0]):
        cs.insert(i, dict(gravura=g, mov=mov, txt=fala, interage=dict(tipo=tp, txt=bal), conv=True))
    v['cenas'] = cs
json.dump(d, open(ARQ, 'w'), ensure_ascii=False, indent=1)
print(sum(1 for v in d for c in v['cenas'] if c.get('interage')), 'momentos de conversa em', len(d), 'vídeos')
