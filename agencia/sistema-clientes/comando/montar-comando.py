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
    for e in linhas:
        if (HOJE - dt.date.fromisoformat(e['iso'])).days <= 6:
            semana[contas_em(e['conta'])[0]] += 1
    return linhas[:40], semana


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
        if cs: out.append({'desde': c[0], 'conta': limpa(c[1], 60), 'contas': cs, 'oque': limpa(c[2], 150)})
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


def main():
    pl, pdata = placar()
    ent, sem = registro()
    estado = {'gerado': dt.datetime.now().strftime('%d/%m/%Y %H:%M'), 'placar': pl, 'placar_data': pdata, 'entregas': ent,
              'entregas_semana': sem, 'andamento': andamento(), 'agenda': agenda()}
    if not os.path.isdir(PRIV):
        sys.exit(f'Privado não encontrado em {PRIV}. Clone CentralLindsonALmeida ao lado deste repositório ou use --privado.')
    os.makedirs(os.path.join(PRIV, 'painel', 'comando'), exist_ok=True)
    js = '// Gerado por agencia/sistema-clientes/comando/montar-comando.py (repositório lindson). Não edite à mão.\nwindow.__ESTADO=' + json.dumps(estado, ensure_ascii=False).replace('</', '<\\/') + ';\n'
    open(os.path.join(PRIV, 'painel', 'comando', 'estado.js'), 'w', encoding='utf-8').write(js)
    html = open(os.path.join(AQUI, 'comando.html'), encoding='utf-8').read()
    mov = open(os.path.join(RAIZ, 'agencia', 'sistema-clientes', 'prototipo', 'movimento.js'), encoding='utf-8').read()
    html = html.replace('<script>\n/* ===== Central de Comando', '<script src="/painel/comando/estado.js"></script>\n<script>\n/* ===== Central de Comando', 1)
    html = html.replace('<!--MOVIMENTO-->', '<script>\n' + mov + '\n</script>')
    open(os.path.join(PRIV, 'painel', 'comando.html'), 'w', encoding='utf-8').write(html)
    print(f"ok · placar {len(pl)} projetos · {len(ent)} entregas · {len(estado['andamento'])} em andamento · semana {sem}")


if __name__ == '__main__':
    main()
