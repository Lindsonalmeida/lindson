# 3 stories por dia, 30 dias (16/11 a 15/12/2026) · Dra. Jaci Cunha · conta Lindson, fila cad2-jaci-2 (parte 1)
# Segue as linhas de estrategia/LINHAS-EDITORIAIS-NOV.md: manhã = acolhimento/bastidor (arte), tarde = dúvida/autoridade
# (arte educativa), noite = chamada para avaliação. Seg agenda da semana · Qua caixinha · Sex enquete (estes 3 com figurinha,
# que só funcionam postando pelo app: ficam marcados "manual"). CFO: sem preço, "grátis", promessa, procedimento sendo feito.
import json, datetime, os
D = os.path.dirname(os.path.abspath(__file__))
INI = datetime.date(2026, 11, 16)
DIAS = ['seg', 'ter', 'qua', 'qui', 'sex', 'sáb', 'dom']

MANHA = [  # acolhimento e bastidores (arte com foto real da clínica ou da Dra., nunca repetida)
    ('Bom dia de Zé Doca', 'A clínica já está pronta para te receber. Hoje tem avaliação com hora marcada.'),
    ('Aqui você é ouvida', 'A primeira coisa que eu faço numa avaliação é perguntar: o que te incomoda?'),
    ('Seu horário é seu', 'Atendimento com hora marcada, no tempo certo para você.'),
    ('Por trás do jaleco', 'Cirurgiã-dentista, CRO-MA 8514. Cuido de sorrisos e do equilíbrio do rosto.'),
    ('Materiais com procedência', 'Pergunte na avaliação de onde vem cada produto. Você tem direito de saber.'),
    ('Biossegurança', 'Cuidado com a esterilização em cada atendimento. Segurança vem antes de tudo.'),
    ('Em frente à Praça do Viva', 'Av. Militar, Zé Doca. Fácil de chegar, fácil de achar.'),
    ('Um novo conceito', 'Beleza, saúde e bem-estar no mesmo cuidado.'),
    ('Natural é o objetivo', 'Realçar o que já é seu, sem mudar quem você é.'),
    ('Sem pressa', 'A avaliação leva o tempo que você precisar para tirar todas as dúvidas.'),
]
TARDE = [  # dúvidas e autoridade (arte educativa: pergunta grande + resposta curta)
    ('Botox deixa a cara parada?', 'Quando a dose é planejada para o seu rosto, a expressão continua sua. Isso se decide na avaliação.'),
    ('Dentista pode fazer harmonização?', 'Pode. A harmonização orofacial é especialidade reconhecida pelo Conselho Federal de Odontologia.'),
    ('Bioestimulador ou preenchimento?', 'Um estimula o seu colágeno; o outro repõe volume. Qual é o seu caso, só a avaliação diz.'),
    ('Preenchimento labial fica exagerado?', 'Fica do jeito que for planejado. Aqui o limite é o que combina com o seu rosto.'),
    ('Dói?', 'Usamos anestésico e técnica cuidadosa. Na avaliação eu explico cada sensação, antes de qualquer decisão.'),
    ('Posso trabalhar no mesmo dia?', 'Na maioria dos casos, sim. As orientações de cuidado você recebe por escrito.'),
    ('Por que eu às vezes digo não', 'Nem todo pedido é indicado. Dizer não também é cuidar de você.'),
    ('Quanto tempo dura?', 'Varia de pessoa para pessoa e de produto para produto. Eu explico o seu caso na avaliação.'),
    ('Sorri de boca fechada nas fotos?', 'Talvez o primeiro passo seja uma avaliação odontológica. Começa por aí.'),
    ('O que é harmonização orofacial?', 'Cuidar do equilíbrio entre rosto e sorriso, respeitando os seus traços.'),
    ('Tenho medo de agulha', 'É mais comum do que você imagina. Me conta na avaliação: a gente vai no seu tempo.'),
    ('Idade certa para começar?', 'Não existe idade certa, existe indicação certa. A avaliação mostra o que faz sentido agora.'),
]
NOITE = [  # chamada para avaliação (arte com botão "Chame no WhatsApp")
    'Avaliações desta semana: ainda há horários. Chame no WhatsApp (98) 98567-2646.',
    'Quer entender o que é indicado para você? Comece pela avaliação. Link na bio.',
    'Quem quer estar bem nas festas começa agora. Agende sua avaliação pelo WhatsApp.',
    'Mande "AVALIAÇÃO" no WhatsApp (98) 98567-2646 e a equipe te responde.',
    'Vem de cidade vizinha? Marque com antecedência e venha com tudo certo.',
    'Ficou com dúvida? Responda este story que eu te explico.',
]
SEG = ('Agenda da semana', 'Os horários de avaliação desta semana estão abertos. Toque no link e garanta o seu.', 'figurinha de link (drajacicunha.pages.dev/avaliacao)')
QUA = ('Caixinha de perguntas', 'Pergunte o que quiser sobre harmonização ou sorriso. Respondo aqui nos stories.', 'figurinha de perguntas')
SEX = ('Enquete', None, 'figurinha de enquete')
ENQUETES = [('Você já fez avaliação de harmonização?', 'Já fiz · Ainda não'), ('O que mais te incomoda?', 'Olheiras · Lábios'),
            ('Medo de agulha?', 'Tenho · Não tenho'), ('Prefere atendimento', 'De manhã · À tarde'), ('Sorri nas fotos?', 'Sempre · De boca fechada')]

dias = []
for i in range(30):
    d = INI + datetime.timedelta(days=i); w = d.weekday(); m = MANHA[i % len(MANHA)]; t = TARDE[i % len(TARDE)]; n = NOITE[i % len(NOITE)]
    s = [{'hora': '08:30', 'linha': 'Acolhimento', 'titulo': m[0], 'texto': m[1], 'formato': 'arte com foto real (não repetir)', 'modo': 'automático'},
         {'hora': '13:00', 'linha': 'Dúvidas e autoridade', 'titulo': t[0], 'texto': t[1], 'formato': 'arte educativa', 'modo': 'automático'},
         {'hora': '19:30', 'linha': 'Chamada', 'titulo': 'Avaliação', 'texto': n, 'formato': 'arte com botão WhatsApp', 'modo': 'automático'}]
    if w == 0: s[2] = {'hora': '19:30', 'linha': 'Agenda', 'titulo': SEG[0], 'texto': SEG[1], 'formato': SEG[2], 'modo': 'manual (figurinha)'}
    if w == 2: s[1] = {'hora': '13:00', 'linha': 'Dúvidas', 'titulo': QUA[0], 'texto': QUA[1], 'formato': QUA[2], 'modo': 'manual (figurinha)'}
    if w == 4:
        q = ENQUETES[(i // 7) % len(ENQUETES)]
        s[1] = {'hora': '13:00', 'linha': 'Interação', 'titulo': SEX[0], 'texto': f'{q[0]} ({q[1]})', 'formato': SEX[2], 'modo': 'manual (figurinha)'}
    dias.append({'data': d.strftime('%d/%m'), 'dia': DIAS[w], 'stories': s})
json.dump(dias, open(os.path.join(D, 'stories.json'), 'w'), ensure_ascii=False, indent=1)

md = ['# Dra. Jaci · 3 stories por dia, 30 dias (16/11 a 15/12/2026)', '',
      'Conta Lindson, 15/11/2026, fila `cad2-jaci-2` (parte 1: roteiro). Linhas de `../estrategia/LINHAS-EDITORIAIS-NOV.md`.',
      '- **08:30 acolhimento** (foto real, nunca repetida: registrar em `../FOTOS-USADAS.md`) · **13:00 dúvida/autoridade** · **19:30 chamada para avaliação**.',
      '- **Automático:** artes sem figurinha, agendadas (Meta Business Suite ou Metricool). **Manual:** seg agenda (link), qua caixinha, sex enquete: figurinha só funciona postando pelo app.',
      '- **CFO:** sem preço, "grátis", promessa de resultado ou procedimento sendo feito; CRO-MA 8514 na assinatura de toda arte.', '']
for x in dias:
    md.append(f"## {x['dia']} {x['data']}")
    for s in x['stories']: md.append(f"- **{s['hora']} · {s['linha']} · {s['titulo']}:** {s['texto']} _({s['formato']}, {s['modo']})_")
    md.append('')
open(os.path.join(D, 'ROTEIRO.md'), 'w').write('\n'.join(md))
print(len(dias), 'dias', sum(len(x['stories']) for x in dias), 'stories', sum(1 for x in dias for s in x['stories'] if s['modo'] == 'automático'), 'automáticos')
