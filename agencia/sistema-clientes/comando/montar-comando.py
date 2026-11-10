#!/usr/bin/env python3
"""Central de Comando (conta Leandro, 09/11/2026): monta /painel/comando no repositório privado.

Lê deste repositório:
  PLACAR-DOS-PROJETOS.md        → placar (% por projeto e o que depende do Lindson ⏳)
  REGISTRO-DAS-CONTAS.md        → últimas entregas e entregas por conta nos últimos 7 dias
  QUADRO-DA-EQUIPE.md           → "Em andamento" (o que cada conta está fazendo)
  agencia/marca-lindson/agenda-status.json (se existir) → agenda do @lindsonalmeida_
Gera no privado (clone em ../centrallindsonalmeida, ao lado deste):
  painel/comando/estado.js      → window.__ESTADO={...}  (.js porque a guarda do site bloqueia .json)
  painel/comando.html           → a página (comando.html + movimento.js do modelo), só o admin abre

Toda conta roda este script ao terminar uma entrega e faz push no privado (README.md desta pasta).
Uso: python3 agencia/sistema-clientes/comando/montar-comando.py [--privado /caminho/do/privado]
"""
import datetime as dt, json, os, re, sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.abspath(os.path.join(AQUI, '..', '..', '..'))
PRIV = os.path.abspath(os.path.join(RAIZ, '..', 'centrallindsonalmeida'))
if '--privado' in sys.argv: PRIV = os.path.abspath(sys.argv[sys.argv.index('--privado') + 1])
CONTAS = ['Lindson', 'Zuleide', 'Pedro', 'Leandro']
HOJE = dt.date.today()


def limpa(s, n=180):
    s = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', s)
    s = s.replace('**', '').replace('`', '').replace('~~', '').strip()
    s = re.sub(r'\s+', ' ', s)
    return s if len(s) <= n else s[:n - 1].rstrip() + '…'


def ler(p):
    p = os.path.join(RAIZ, p)
    return open(p, encoding='utf-8').read() if os.path.exists(p) else ''


def data_br(s):
    m = re.match(r'\s*(\d{1,2})/(\d{1,2})(?:/(\d{4}))?', s)
    if not m: return None
    try: return dt.date(int(m.group(3) or HOJE.year), int(m.group(2)), int(m.group(1)))
    except ValueError: return None


def contas_em(txt):
    return [c for c in CONTAS if re.search(r'\b' + c + r'\b', txt)]


# 1 · placar
def placar():
    txt, out, data = ler('PLACAR-DOS-PROJETOS.md'), [], ''
    m = re.search(r'atualizado em (\d{2}/\d{2}/\d{4})', txt)
    if m: data = m.group(1)
    for bloco in re.split(r'\n(?=### )', txt):
        cab = re.match(r'### (.+)', bloco)
        if not cab: continue
        h = cab.group(1)
        m = re.search(r'(\d+) de (\d+) \((\d+)%\)', h)
        if not m: continue
        nome = limpa(re.sub(r'[^\w\s.À-ú-]', '', re.sub(r'\(.*?\)', '', h.split('·')[0])).strip(), 40)
        dono = [limpa(re.sub(r'^\d+\.\s*⏳\s*', '', l.strip()), 120) for l in bloco.splitlines() if re.match(r'\s*\d+\.\s*⏳', l)]
        out.append({'nome': nome, 'pct': int(m.group(3)), 'feito': int(m.group(1)), 'total': int(m.group(2)), 'pagante': 'pagante' in h and 'não paga' not in h, 'dono': dono})
    return out, data


# palavras que ligam um texto do REGISTRO ou do QUADRO a um cliente e a uma função (para o distribuidor)
CLI_KW = {'jaci': ['jaci'], 'tribuna': ['tribuna'], 'leo': ['leo pinto', 'leo:', ' leo ', 'do leo', 'vereador'], 'rt': ['real time', 'rt full', 'realtime'], 'sf': ['desentupidora', 'grupo sf', 'gruposf'], 'wf': ['wf celulares', 'wf-celulares', ' wf '],
          'oregano': ['oregano'], 'marca': ['@lindsonalmeida', 'marca pessoal', 'site do lindson', 'marca do lindson', 'marca-lindson', 'reels do lindson', 'bio do lindson']}
FN_KW = {'reels': ['reels', 'reel '], 'carrossel': ['carross'], 'post': ['post', 'artes', 'feed'], 'stories': ['stories', 'story', 'destaque'], 'legenda': ['legenda'],
         'data': ['data comemorativa', 'datas', 'saudac', 'aniversario'], 'site': ['site', 'mini site', ' bio'], 'landing': ['landing', 'pagina de venda'],
         'painel': ['painel'], 'estrategia': ['estrategia'], 'proposta': ['proposta'], 'contrato': ['contrato'], 'relatorio': ['relatorio', 'analise']}


def sem_acento(s):
    import unicodedata
    return ''.join(c for c in unicodedata.normalize('NFD', s.lower()) if unicodedata.category(c) != 'Mn')


def acha(txt, kw):
    t = ' ' + sem_acento(txt) + ' '
    return [k for k, ws in kw.items() if any(w in t for w in ws)]


# 2 · registro (a linha mais recente fica embaixo)
def registro():
    linhas = []
    for l in ler('REGISTRO-DAS-CONTAS.md').splitlines():
        if not l.startswith('|'): continue
        c = [x.strip() for x in l.strip().strip('|').split('|')]
        if len(c) < 4: continue
        d = data_br(c[0])
        if not d or not contas_em(c[1]): continue
        linhas.append({'data': d.strftime('%d/%m/%Y'), 'iso': d.isoformat(), 'conta': limpa(c[1], 40), 'oque': limpa(c[2], 200), 'onde': limpa(c[3], 120), 'situacao': limpa(c[4] if len(c) > 4 else '', 80)})
    linhas.reverse()  # mais recente primeiro
    semana = {c: 0 for c in CONTAS}
    esp = {c: {'cli': {}, 'func': {}} for c in CONTAS}
    for e in linhas:
        conta = contas_em(e['conta'])[0]
        if (HOJE - dt.date.fromisoformat(e['iso'])).days <= 6:
            semana[conta] += 1
        for k in acha(e['oque'] + ' ' + e['onde'], CLI_KW): esp[conta]['cli'][k] = esp[conta]['cli'].get(k, 0) + 1
        for k in acha(e['oque'], FN_KW): esp[conta]['func'][k] = esp[conta]['func'].get(k, 0) + 1
    return linhas[:40], semana, esp


# 3 · quadro, seção "Em andamento"
def andamento():
    txt = ler('QUADRO-DA-EQUIPE.md')
    m = re.search(r'## Em andamento\n(.*?)(\n## |\Z)', txt, re.S)
    out = []
    for l in (m.group(1) if m else '').splitlines():
        c = [x.strip() for x in l.strip().strip('|').split('|')]
        if len(c) < 3 or c[0] in ('Desde', '---') or set(c[0]) <= set('-'): continue
        # "Leandro → **Pedro**": a conta depois da seta é quem está com o item agora
        quem = c[1].split('→')[-1] if '→' in c[1] else c[1]
        cs = contas_em(quem) or contas_em(c[1])
        d = data_br(c[0])
        if cs: out.append({'desde': c[0], 'conta': limpa(c[1], 60), 'contas': cs, 'oque': limpa(c[2], 150), 'clis': acha(c[2], CLI_KW),
                           'recente': bool(d and (HOJE - d).days <= 3)})
    return out


# 4 · agenda do @lindsonalmeida_
def agenda():
    p = os.path.join(RAIZ, 'agencia', 'marca-lindson', 'agenda-status.json')
    if not os.path.exists(p): return None
    d = json.load(open(p, encoding='utf-8'))
    posts = d.get('posts') or []
    st = {}
    for x in posts: st[x.get('status') or 'sem status'] = st.get(x.get('status') or 'sem status', 0) + 1
    agora = dt.datetime.now(dt.timezone.utc)
    prox = None
    for x in sorted(posts, key=lambda x: x.get('quando') or ''):
        try: q = dt.datetime.fromisoformat(x.get('quando'))
        except (TypeError, ValueError): continue
        if x.get('status') in ('agendado', 'aguardando aprovação') and q > agora:
            prox = {'titulo': limpa(x.get('titulo', ''), 80), 'quando': q.strftime('%d/%m %H:%M'), 'status': x.get('status')}
            break
    return {'total': len(posts), 'por_status': st, 'proximo': prox}


# 5 · última atividade de cada conta (commits com "(conta X" nos dois repositórios)
def atividade():
    import subprocess
    out = {}
    for repo in (RAIZ, PRIV):
        try:
            log = subprocess.run(['git', '-C', repo, 'log', '--all', '--since=21 days', '--format=%cI\t%s'], capture_output=True, text=True, timeout=30).stdout
        except Exception:
            continue
        for l in log.splitlines():
            if '\t' not in l: continue
            quando, msg = l.split('\t', 1)
            for c in CONTAS:
                if re.search(r'conta ' + c + r'\b', msg) and (c not in out or quando > out[c]['em']):
                    out[c] = {'em': quando, 'msg': limpa(msg, 90)}
    return out


# 6 · peças de cada cliente para aprovar (lista APROV dos painéis), sem prova social/antes e depois
def pecas():
    out = {}
    for cli in ('jaci', 'tribuna', 'leo', 'rt', 'oregano', 'sf', 'wf'):
        p = os.path.join(PRIV, 'painel', cli + '.html')
        if not os.path.exists(p): continue
        s = open(p, encoding='utf-8').read()
        i = s.find('APROV=[')
        if i < 0: continue
        try: lista, _ = json.JSONDecoder().raw_decode(s[i + 6:])
        except ValueError: continue
        itens = []
        for x in lista:
            img = x.get('img') or ''  # auditoria 10/11: imagem em data: (base64) não entra no filtro, senão "tcle"/"prova" sorteados no base64 somem com peças do Leo e da Real Time
            t = sem_acento((x.get('titulo') or '') + ' ' + ('' if img.startswith('data:') else img))
            if any(w in t for w in ('prova', 'antes e depois', 'antes-depois', 'tcle', 'paciente')): continue
            if not x.get('img'): continue
            itens.append({'titulo': x.get('titulo', ''), 't': x.get('t', ''), 'img': x['img'], 'telas': (x.get('telas') or [])[:10], 'data': x.get('data', ''), 'st': x.get('st', 'aguardando')})
        out[cli] = itens
    return out


# 7 · vídeos já entregues e no ar (portfólio do site), para prévia ao passar o dedo
def videos():
    out = []
    for n, nome in (('leo-motion-1', 'Leo Pinto · motion 1'), ('leo-motion-3', 'Leo Pinto · motion 3'), ('leo-motion-4', 'Leo Pinto · motion 4')):
        if os.path.exists(os.path.join(PRIV, 'site', 'media', n + '.mp4')):
            out.append({'nome': nome, 'mp4': '/site/media/' + n + '.mp4', 'poster': '/site/media/' + n + '.jpg'})
    return out


def agenda_posts():
    p = os.path.join(RAIZ, 'agencia', 'marca-lindson', 'agenda-status.json')
    if not os.path.exists(p): return []
    posts = json.load(open(p, encoding='utf-8')).get('posts') or []
    return [{'seq': x.get('seq'), 'titulo': limpa(x.get('titulo', ''), 70), 'formato': x.get('formato_rotulo') or x.get('formato'),
             'quando': (x.get('quando') or '')[:16].replace('T', ' '), 'status': x.get('status')} for x in posts]


def vektor_ctx(estado):
    # contexto compacto do VEKTOR (v4, conta Zuleide, 09/11/2026): vai para functions/_vektor_ctx.js no privado e entra no prompt de /api/vektor.
    # Sem as peças (imagens) e sem segredo; a fila e a equipe ao vivo o servidor lê do KV na hora.
    ctx = {'gerado': estado['gerado'],
           'placar': [{'nome': x.get('nome'), 'pct': x.get('pct'), 'pagante': x.get('pagante'), 'falta_lindson': [limpa(d, 90) for d in (x.get('dono') or [])[:3]]} for x in estado['placar']],
           'andamento': [{'desde': a.get('desde'), 'conta': a.get('conta'), 'oque': limpa(a.get('oque', ''), 170)} for a in estado['andamento'][:14]],
           'entregas': [{'data': e.get('data'), 'conta': e.get('conta'), 'oque': limpa(e.get('oque', ''), 140)} for e in estado['entregas'][:14]],
           'entregas_semana': estado['entregas_semana'], 'atividade': estado['atividade'], 'agenda_instagram': agenda_posts()}
    js = ('// Gerado por agencia/sistema-clientes/comando/montar-comando.py (repositório lindson). Não edite à mão.\n'
          'export const CTX = ' + json.dumps(ctx, ensure_ascii=False) + ';\n')
    open(os.path.join(PRIV, 'functions', '_vektor_ctx.js'), 'w', encoding='utf-8').write(js)


def main():
    if not os.path.isdir(PRIV):
        sys.exit(f'Privado não encontrado em {PRIV}. Clone CentralLindsonALmeida ao lado deste repositório ou use --privado.')
    pl, pdata = placar()
    ent, sem, esp = registro()
    anda = andamento()
    perfil = {'esp': esp, 'andamento': [{'conta': a['contas'][-1], 'cli': c, 'oque': a['oque']} for a in anda if a['recente'] for c in a['clis']]}
    estado = {'gerado': dt.datetime.now().strftime('%d/%m/%Y %H:%M'), 'placar': pl, 'placar_data': pdata, 'entregas': ent,
              'entregas_semana': sem, 'andamento': anda, 'agenda': agenda(), 'agenda_posts': agenda_posts(), 'atividade': atividade(), 'pecas': pecas(), 'videos': videos(), 'perfil': perfil}
    base = os.path.join(PRIV, 'painel', 'comando')
    os.makedirs(os.path.join(base, 'media'), exist_ok=True)
    js = '// Gerado por agencia/sistema-clientes/comando/montar-comando.py (repositório lindson). Não edite à mão.\nwindow.__ESTADO=' + json.dumps(estado, ensure_ascii=False).replace('</', '<\\/') + ';\n'
    open(os.path.join(base, 'estado.js'), 'w', encoding='utf-8').write(js)
    import shutil
    md = os.path.join(AQUI, 'v2', 'media')
    for f in (os.listdir(md) if os.path.isdir(md) else []):
        shutil.copy(os.path.join(md, f), os.path.join(base, 'media', f))
    html = open(os.path.join(AQUI, 'comando.html'), encoding='utf-8').read()
    mov = open(os.path.join(RAIZ, 'agencia', 'sistema-clientes', 'prototipo', 'movimento.js'), encoding='utf-8').read()
    dist = open(os.path.join(PRIV, 'functions', '_distribuir.js'), encoding='utf-8').read().replace('export ', '')
    html = html.replace('<!--ESTADO-->', '<script src="/painel/comando/estado.js"></script>', 1)
    html = html.replace('/*DISTRIBUIR*/', dist, 1)
    pron = os.path.join(AQUI, 'voz', 'pronuncia.json')  # dicionário de pronúncia do VEKTOR (só no que é falado)
    if os.path.exists(pron): html = html.replace('/*PRONUNCIA*/[]', json.dumps(json.load(open(pron, encoding='utf-8')), ensure_ascii=False), 1)
    html = html.replace('<!--MOVIMENTO-->', '<script>\n' + mov + '\n</script>')
    open(os.path.join(PRIV, 'painel', 'comando.html'), 'w', encoding='utf-8').write(html)
    vektor_ctx(estado)
    app = os.path.join(AQUI, 'v4', 'app')  # ícones e manifesto do app (v4, conta Zuleide)
    for f in (os.listdir(app) if os.path.isdir(app) else []):
        shutil.copy(os.path.join(app, f), os.path.join(base, f))
    print(f"ok · placar {len(pl)} · {len(ent)} entregas · {len(anda)} em andamento · peças {sum(len(v) for v in estado['pecas'].values())} · atividade {list(estado['atividade'])}")


if __name__ == '__main__':
    main()
