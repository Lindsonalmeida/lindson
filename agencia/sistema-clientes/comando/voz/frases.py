"""Gera frases.txt: todas as falas completas que o responde() da Central de Comando pode dizer (conta Leandro, 10/11/2026).
Cada linha vira um clipe inteiro (voz fluida, sem juntar pedaços). Se mudar uma fala no comando.html, mude aqui e rode:
  python3 frases.py && python3 gerar_voz_vektor.py frases.txt /home/user/centrallindsonalmeida/painel/comando/voz D
"""
import itertools, os
CLI = {'jaci': 'Dra. Jaci', 'tribuna': 'Tribuna 98', 'leo': 'Leo Pinto', 'rt': 'Real Time', 'oregano': 'Orégano Turbo', 'sf': 'Desentupidora SF', 'marca': None, 'outro': None}
de_cli = lambda c: 'da sua marca' if c == 'marca' else 'de outro cliente' if c == 'outro' else 'de ' + CLI[c]
FN = ['Reels', 'Carrossel', 'Post', 'Stories', 'Legenda SEO', 'Arte de data', 'Site / mini site', 'Landing', 'Painel do cliente', 'Estratégia PDF', 'Proposta', 'Contrato', 'Relatório do cliente']
CONTAS = ['Lindson', 'Zuleide', 'Pedro', 'Leandro']
art = lambda c: 'a Zuleide' if c == 'Zuleide' else 'a conta Lindson' if c == 'Lindson' else 'o ' + c
F = []
F += ['Pois não?', 'Escuta pausada.', 'Vektor aqui. Voz ligada.', 'Os detalhes estão na tela.',
      'Vektor aqui. Já existe um pedido igual na fila. Se for outro, diga enviar de novo.',
      'Diga primeiro Vektor, o cliente e o que precisa.',
      'Oi, Lindson! Tô te ouvindo, sim. Me diz o cliente e o que precisa, que eu monto o pedido.',
      'Vektor aqui. Estou ouvindo, Lindson. É só me chamar pelo nome e falar.',
      'Vektor aqui. Nenhuma conta disponível agora. Os pedidos ficam na espera.',
      'Vektor aqui. Diga o que foi feito depois do cliente.', 'Hum, deixa eu ver.', 'Vektor aqui. Resposta enviada.']
for fn, c in itertools.product(FN, CLI):  # envio e montagem
    F += [f'Vektor aqui. Pedido de {fn} {de_cli(c)} enviado; {art(k)} pega.' for k in CONTAS]
    F.append(f'{fn} {de_cli(c)}. Diga enviar para mandar.')
F += [f'Vektor aqui. Pedido de {fn} enviado. Fica na espera até uma conta voltar.' for fn in FN]
F += [f'Abrindo o painel de {CLI[c]}.' for c in ['jaci', 'tribuna', 'leo', 'rt', 'oregano']]
F += [f'Vektor aqui. Anotado nas tarefas feitas {de_cli(c)}.' for c in CLI]
F += [f'Vektor aqui. Resposta enviada para {art(k)}.' for k in CONTAS]
for ab in range(11):
    for n in range(11):
        F.append(f"Vektor aqui. {ab} {'pedido' if ab == 1 else 'pedidos'} na fila, {n} esperando você.")
for n in range(1, 21):
    F.append(f"Vektor aqui. Você tem {n} {'pedido esperando' if n == 1 else 'pedidos esperando'} você.")
for k in range(1, 5):
    for comb in itertools.combinations(CONTAS, k):
        F.append(f"Vektor aqui. Disponíveis agora: {', '.join(comb)}.")
F = list(dict.fromkeys(F))
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'frases.txt'), 'w', encoding='utf-8').write('\n'.join(F) + '\n')
print(len(F), 'frases')

# v6 (conta Leandro, 10/11): frases fixas do modo local (bloco VKF do comando.html) e as falas curtas que se repetem
import json, re
html = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'comando.html'), encoding='utf-8').read()
VKF = json.loads(html.split('/*VKF*/', 1)[1].split('/*FIM-VKF*/', 1)[0])
NOMES = [v for v in CLI.values() if v]
for k, l in VKF.items():
    for f in l:
        if f.endswith(': '): continue
        if '{cli}' in f or '{de}' in f:
            for c in CLI:
                if '{cli}' in f and not CLI[c]: continue
                F.append(f.replace('{cli}', CLI[c] or '').replace('{de}', de_cli(c)))
        else: F.append(f)
for fn, c in itertools.product(FN, CLI):
    F += [f'Pedido de {fn} {de_cli(c)} enviado; {art(k)} pega.' for k in CONTAS] + [f'Mandei {fn} {de_cli(c)} para {art(k)}.' for k in CONTAS]
F += [f'Pedido de {fn} enviado. Fica na espera até uma conta voltar.' for fn in FN]
for oi in ('Bom dia', 'Boa tarde', 'Boa noite'):
    F += [f'{oi}, Lindson.', f'{oi}! Tudo certo por aqui.', f'{oi}, chefe.']
F += ['Quer que eu abra o primeiro?', 'Diga abre o primeiro para ver.', 'Abro algum?', 'A fila está vazia.', 'Fila zerada.', 'Nada aberto.', 'Não tem nenhum pedido na fila.',
      'Pedido aprovado.', 'Aprovei o pedido.', 'Pronto, pedido aprovado e anotado.', 'Quer aprovar?', 'Aprovo esse?', 'Se estiver bom, diga aprova.', 'Aprovo?',
      'Nada depende de você agora.', 'Da sua parte, nada pendente.', 'Ainda espera a sua aprovação.', 'Os pedidos ficam na espera.', 'Nenhuma conta disponível agora.',
      'Nenhuma conta disponível.', 'Nenhuma peça esperando a sua aprovação.', 'Tudo em dia.', 'Não tem nada para aprovar agora.', 'Para pedir ajuste num pedido, toque em Ajuste na fila.',
      'Por voz eu aprovo.', 'As tarefas feitas ainda estão carregando.', 'Diga o que foi feito depois do cliente.', 'O que foi feito? Diga o cliente e a atividade.', 'Mando para a equipe?',
      'Posso mandar?', 'Diga sim para enviar.', 'Confirma que eu mando.', 'Diga sim.', 'Confirma?', 'Mando?', 'Posso?', 'Diga sim para confirmar.']
F = list(dict.fromkeys(F))
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'frases.txt'), 'w', encoding='utf-8').write('\n'.join(F) + '\n')
print(len(F), 'frases')
