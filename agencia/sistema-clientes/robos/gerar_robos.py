#!/usr/bin/env python3
# Gera robos.json: inventário de todos os robôs e automações da agência para a aba "Robôs" do admin da Central.
# Pedido do Lindson (22/11/2026): "conseguimos montar um app de organização pros robôs? pra visualizar em um único lugar?" (conta Leandro, Builder).
# Fontes: o CATÁLOGO abaixo (o que cada robô é), o git do repositório lindson (última execução pelos commits que o robô deixa),
# gatilhos.json (retrato das rotinas agendadas do Claude: a coordenação atualiza) e, com --testar, um teste das rotas da Central
# (só o código HTTP; nenhum segredo é lido nem gravado). No navegador, a aba ainda lê ao vivo /api/sdr?robo=1 e /api/agenda-ig.
# Uso: python3 gerar_robos.py [--repo /home/user/lindson] [--testar]
import json, os, re, subprocess, sys, urllib.request
from datetime import datetime, timezone
D = os.path.dirname(os.path.abspath(__file__))
GH = 'https://github.com/Lindsonalmeida/lindson/blob/claude/global-agent-installation-vdyowf/'
CENTRAL = 'https://lindsonalmeida.pages.dev'

# agenda: {"min": minuto, "horas": [..] ou "cada": N horas, "de"/"ate": janela, "dias": [0=dom..6]} no horário de São Luís (UTC-3).
CATALOGO = [
  # Vendas e prospecção
  dict(id='sdr1', nome='Robô SDR 1', grupo='Vendas', oque='Manda a mensagem de prospecção no WhatsApp, 1 lead por vez, e conversa com quem responde (follow-ups).',
       onde='PC do Lindson', dono='Pedro', freq='a cada 4–9 min, 09:00–18:00, todos os dias (30/dia)', agenda=dict(janela=['09:00', '18:00']),
       fonte='vivo:sdr1', link='#sdr', arquivo='agencia/prospeccao/robo-sdr/README.md', max_h=0.4),
  dict(id='sdr2', nome='Robô SDR 2', grupo='Vendas', oque='Segundo número do time de SDR: só os leads dele, saudação e pergunta variadas.',
       onde='PC do Lindson', dono='Pedro', freq='a cada 5–10 min, 09:20–17:40, todos os dias (30/dia)', agenda=dict(janela=['09:20', '17:40']),
       fonte='vivo:sdr2', link='#sdr', arquivo='agencia/processos/time-sdr-whatsapp.md', max_h=0.4),
  dict(id='sdr3', nome='Robô SDR 3', grupo='Vendas', oque='Terceiro número do time de SDR.',
       onde='PC do Lindson', dono='Pedro', freq='a cada 5–11 min, 09:40–17:20, todos os dias (30/dia)', agenda=dict(janela=['09:40', '17:20']),
       fonte='vivo:sdr3', link='#sdr', arquivo='agencia/processos/time-sdr-whatsapp.md', max_h=0.4),
  dict(id='leads-sdr', nome='Pesquisa de leads do SDR', grupo='Vendas', oque='Põe leads novos (WhatsApp celular + Instagram, nota 80+) na lista do time de SDR quando ela acaba.',
       onde='Nuvem Claude', dono='Leandro (coordenação) · Pedro', freq='quando a lista acaba', fonte=r'gitc:^SDR: [0-9]+ |^SDR Orégano|leads novos',
       link='#sdr', arquivo='agencia/operacao-propria/sdr/PUBLICO-ALVO.md', max_h=24 * 7),
  dict(id='sdr-oregano', nome='SDR Orégano (pizzarias)', grupo='Vendas', oque='Lista diária de pizzarias com mensagem pronta no painel da Orégano Turbo; envio pelo botão WhatsApp (cadência).',
       onde='Nuvem Claude + Central', dono='Zuleide', freq='diária (leads); envio manual', fonte=r'git:SDR Orégano', link='/painel/oregano#sdr',
       arquivo='agencia/sistema-clientes/oregano-turbo/montar-sdr.py', max_h=48, vivo='sdr-oregano'),
  # Postagem
  dict(id='rt-post', nome='Real Time · postar 3x ao dia', grupo='Postagem', oque='Pega o próximo post APROVADO da Real Time e publica no Instagram pelo Windsor; marca como postado no painel.',
       onde='Nuvem Claude', dono='Leandro', freq='09:58, 13:58 e 17:58', agenda=dict(min=58, horas=[9, 13, 17]), fonte='gatilho:rt-post',
       link='/painel/rt', arquivo='agencia/processos/automacao-operacao.md', depende='automacao'),
  dict(id='robo-ig', nome='Robô do Instagram @lindsonalmeida_', grupo='Postagem', oque='Publica sozinho a agenda do Instagram do Lindson pela API oficial (post, carrossel, Reels), 4 h entre posts.',
       onde='PC do Lindson', dono='Pedro', freq='a cada 15 min, 08:00–21:00', agenda=dict(janela=['08:00', '21:00'], cada_min=15), fonte='vivo:agenda-ig',
       link='#rede', arquivo='agencia/marca-lindson/robo-instagram/README.md', max_h=48),
  # Equipe (rotinas agendadas das contas)
  dict(id='coordenacao', nome='Coordenação das equipes', grupo='Equipe', oque='Lê o quadro A fazer e os cadernos, divide o trabalho na fila, cobra quem não confirmou e sincroniza o quadro do admin.',
       onde='Nuvem Claude', dono='Leandro', freq='a cada 2 h, 08:07–22:07', agenda=dict(min=7, horas=list(range(8, 23, 2))), fonte=r'git:^Coordenação: rodada',
       link='/painel/comando#afazer', arquivo='coordenacao/COORDENACAO.md', max_h=6, depende='automacao'),
  dict(id='rodada-lindson', nome='Rodada da equipe Lindson (fila)', grupo='Equipe', oque='Pega o próximo item livre da fila da equipe Lindson, faz, sobe no painel do cliente e fecha.',
       onde='Nuvem Claude', dono='Leandro (rotina) · equipe Lindson', freq='a cada 2 h (:36)', agenda=dict(min=36, cada=2), fonte='gatilho:rodada-lindson',
       link='/painel/comando#afazer', arquivo='coordenacao/PROMPT-EQUIPE.md', trabalho=r'git:^Fila: Lindson', depende='automacao'),
  dict(id='agregacao-zuleide', nome='Agregação horária', grupo='Equipe', oque='Verifica de hora em hora o que entrou no repositório e agrega aos agentes e à memória.',
       onde='Nuvem Claude', dono='Zuleide', freq='de hora em hora (:50)', agenda=dict(min=50, cada=1), fonte=r'git:^Agregação: verificação', link='#quadro',
       arquivo='MENTE-COLETIVA.md', max_h=3),
  dict(id='filas-equipes', nome='Rodadas das equipes Zuleide e Pedro', grupo='Equipe', oque='Cada equipe pega o próximo item dela na fila da coordenação a cada 2 h.',
       onde='Nuvem Claude', dono='Zuleide · Pedro', freq='a cada 2 h', fonte=r'git:^[Ff]ila: (Zuleide|Pedro)', link='/painel/comando#afazer',
       arquivo='coordenacao/PROMPT-EQUIPE.md', max_h=24),
  # Central (Cloudflare)
  dict(id='vektor', nome='VEKTOR (gerente por voz)', grupo='Central', oque='Conversa por voz e texto com o Lindson na Central de Comando e cria pedidos para as equipes (Workers AI).',
       onde='Cloudflare', dono='Leandro · Zuleide', freq='sob demanda', fonte='sob-demanda', link='/painel/comando', arquivo='agencia/sistema-clientes/comando/README.md'),
  dict(id='noticias', nome='Notícias do nicho', grupo='Central', oque='Busca notícias do nicho de cada cliente (Google Notícias, reserva Bing) e guarda 3 h.',
       onde='Cloudflare', dono='Lindson (conta)', freq='sob demanda, cache de 3 h', fonte='sob-demanda', link='/painel/jaci#noticias', arquivo='agencia/sistema-clientes/site/README.md'),
  dict(id='lembretes', nome='Lembretes da agenda no WhatsApp (Mova Street)', grupo='Central', oque='Avisa contato e responsável no WhatsApp (D-1 às 18h e 2 h antes).',
       onde='Cloudflare + agendador externo', dono='Leandro', freq='a cada 15 min (quando ligado)', fonte='parado', link='/painel/mova-street',
       arquivo='agencia/sistema-clientes/mova-street/README.md', status='parado',
       motivo='Desligado: faltam na Cloudflare o provedor de WhatsApp (WA_API_URL, WA_TOKEN) e a senha do agendador (AGENDA_CRON), e um agendador a cada 15 min.'),
  # Rotinas antigas desligadas
  dict(id='bombou', nome='Notícias BOMBOU', grupo='Parados', oque='Notícias virais do Maranhão e do Brasil para o @bombouof (5 + 5 a cada 3 h).', onde='Nuvem Claude', dono='Leandro',
       freq='a cada 3 h', fonte='gatilho:bombou', status='parado', motivo='Desligada em 26/10 (limite de uso da conta na última execução).', arquivo='MENTE-COLETIVA.md'),
  dict(id='captacao', nome='Captação por cidades', grupo='Parados', oque='Leads de todos os tipos de negócio, cidade por cidade, no app Recomeço 90.', onde='Nuvem Claude', dono='Leandro',
       freq='a cada 3 h', fonte='gatilho:captacao', status='parado', motivo='Desligada em 26/10 (limite de uso); substituída pelo time de SDR.', arquivo='agencia/prospeccao/ROTINA.md'),
  dict(id='roteiros', nome='Roteiros diários de Reels', grupo='Parados', oque='5 roteiros de Reels de 30 s por dia no app Recomeço 90.', onde='Nuvem Claude', dono='Leandro',
       freq='diária 05:41', fonte='gatilho:roteiros', status='parado', motivo='Desligada em 22/10: os 300 roteiros do Teste 01 foram gerados de uma vez.', arquivo='conteudo/esteira/ROTINA.md'),
]

def git_ultimo(repo, padrao):
    try:
        s = subprocess.run(['git', '-C', repo, 'log', '--all', '-E', '--grep=' + padrao, '-1', '--format=%cI|%s'], capture_output=True, text=True, timeout=60).stdout.strip()
        if s: d, m = s.split('|', 1); return d, m[:140]
    except Exception: pass
    return None, None

def testar():
    # Só o código HTTP das rotas que as automações usam sem login (o proxy da sessão injeta a credencial salva). Nada é guardado além do código.
    out = {}
    for k, u in {'automacao': '/api/automacao?cli=rt', 'sdr': '/api/sdr?robo=1'}.items():
        try:
            resp = urllib.request.urlopen(urllib.request.Request(CENTRAL + u, headers={'User-Agent': 'central-robos'}), timeout=20); out[k] = resp.status
            if k == 'sdr':  # só sinal de vida e estado de cada número (sem leads, sem token)
                out['robos'] = {n: {'visto': v.get('visto'), 'estado': v.get('estado'), 'pausado': v.get('pausado'), 'enviados': v.get('enviados')} for n, v in (json.load(resp).get('robos') or {}).items()}
        except urllib.error.HTTPError as e: out[k] = e.code
        except Exception: out[k] = 0
    return out

def main():
    a = sys.argv[1:]
    repo = a[a.index('--repo') + 1] if '--repo' in a else os.path.abspath(os.path.join(D, '..', '..', '..'))
    central = a[a.index('--central') + 1] if '--central' in a else '/home/user/centrallindsonalmeida'
    gat = json.load(open(os.path.join(D, 'gatilhos.json'), encoding='utf-8')) if os.path.exists(os.path.join(D, 'gatilhos.json')) else {}
    antigo = {}
    try: antigo = json.load(open(os.path.join(D, 'robos.json'), encoding='utf-8'))
    except Exception: pass
    rotas = testar() if '--testar' in a else antigo.get('rotas', {})
    agora = datetime.now(timezone.utc)
    lista = []
    for r in CATALOGO:
        r = dict(r); f = r['fonte']; r['ultima'] = None; r['ultima_msg'] = ''
        if f.startswith('git:'):
            r['ultima'], r['ultima_msg'] = git_ultimo(repo, f[4:])
        elif f.startswith('gitc:'):
            r['ultima'], r['ultima_msg'] = git_ultimo(central, f[5:])
        elif f.startswith('vivo:sdr') and rotas.get('robos', {}).get(f[5:]):
            v = rotas['robos'][f[5:]]; r['ultima'] = v.get('visto'); r['ultima_msg'] = v.get('estado', '')
        elif f.startswith('gatilho:'):
            g = gat.get('gatilhos', {}).get(f[8:], {})
            r['ultima'] = g.get('ultima'); r['ultima_msg'] = g.get('resultado', ''); r['ligado'] = g.get('ligado', True)
        if r.get('trabalho'):
            d, m = git_ultimo(repo, r.pop('trabalho')[4:]); r['trabalho_em'] = d; r['trabalho_msg'] = m
        # situação calculada (a aba recalcula ao vivo para SDR e robô do Instagram)
        if not r.get('status'):
            r['status'], r['motivo'] = 'ativo', ''
            if r.get('depende') == 'automacao' and rotas.get('automacao') == 401:
                r['status'] = 'erro'
                r['motivo'] = 'A Central recusa a chave AUTOMACAO_TOKEN (API 401): ' + ('não lê as aprovações nem marca o postado.' if r['id'] == 'rt-post' else 'não lê nem atualiza o quadro A fazer da Central (usa só a fila do repositório).')
            if r.get('ultima') and r.get('max_h'):
                h = (agora - datetime.fromisoformat(r['ultima'])).total_seconds() / 3600
                if h > r['max_h']:
                    if r['status'] == 'ativo': r['status'] = 'atencao'
                    r['motivo'] = (r['motivo'] + ' ' if r['motivo'] else '') + f'Sem sinal há {round(h / 24, 1) if h >= 48 else round(h)} {"dias" if h >= 48 else "h"} (esperado a cada {r["max_h"]} h ou menos).'
            if r['fonte'] == 'vivo:agenda-ig':
                r['status'] = 'atencao'; r['motivo'] = 'Sem confirmação de que está instalado no PC (precisa do token da Meta e do IG_ROBO_TOKEN). A aba confere ao vivo na fila /api/agenda-ig.'
            if r['id'] == 'rodada-lindson' and r.get('trabalho_em'):
                h = (agora - datetime.fromisoformat(r['trabalho_em'])).total_seconds() / 3600
                if h > 48 and r['status'] == 'ativo': r['status'] = 'atencao'
                if h > 48: r['motivo'] = (r['motivo'] + ' ' if r['motivo'] else '') + f'Dispara a cada 2 h, mas não pega item da fila desde {datetime.fromisoformat(r["trabalho_em"]).strftime("%d/%m")}.'
        r['arquivo_url'] = GH + r['arquivo'] if r.get('arquivo') else ''
        lista.append(r)
    saida = {'gerado': agora.isoformat(timespec='seconds'), 'rotas': rotas, 'gatilhos_em': gat.get('atualizado'), 'robos': lista}
    json.dump(saida, open(os.path.join(D, 'robos.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    c = {}
    for r in lista: c[r['status']] = c.get(r['status'], 0) + 1
    print(len(lista), 'robôs ·', c, '· rotas', rotas)

if __name__ == '__main__': main()
