"""Aba "Feitos" do Quadro de atividades (admin da Central): linha do tempo por data e hora (conta Leandro, 11/11/2026).
  python3 montar_feitos.py            -> imprime quantos itens e os 5 mais novos
  from montar_feitos import feitos     -> lista usada pelo montar-site.py (window.__FEITOS)
Fonte: feitos.json (base de 230 itens resumidos em 10/11) + toda linha NOVA do REGISTRO-DAS-CONTAS.md,
com a hora do commit que acrescentou a linha (fuso de São Luís, UTC-3), ou a hora escrita no começo do texto: "[13:08] ...". Nada fica fixo à mão: entrou no REGISTRO, entra aqui."""
import hashlib, json, os, re, subprocess
from datetime import datetime, timedelta, timezone

D = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.abspath(os.path.join(D, '..', '..', '..'))
REG = os.path.join(RAIZ, 'REGISTRO-DAS-CONTAS.md')
SL = timezone(timedelta(hours=-3))
LINHA = re.compile(r'^\| (\d{2})/(\d{2})/(\d{4}) \| ([^|]+)\| ([^|]+)\|')
# cliente pelo assunto (o mesmo cliente escrito sempre do mesmo jeito)
CLI = [('Dra. Jaci Cunha', r'jaci'), ('Leo Pinto', r'\bleo\b|vereador'), ('Orégano Turbo', r'or[eé]gano|pizzari'), ('Real Time', r'real ?time|\brt\b'),
       ('WF Celulares', r'\bwf\b'), ('Curso legislativo', r'curso|legislativ'), ('Desentupidora SF', r'desentup|\bsf\b'), ('Tribuna 98', r'tribuna'),
       ('Raposa e Leão', r'raposa|maquiavel|manual de campo'), ('Central', r'central|painel|comando|vektor'), ('Minha marca', r'.')]

def _cli(t):
    t = t.lower()
    return next(n for n, p in CLI if re.search(p, t))

def _resumo(t):
    t = re.sub(r'`', '', t).strip()
    t = re.sub(r'^[^:]{2,40}:\s*', '', t) if ':' in t[:42] else t  # tira o "Cliente:" do começo
    t = t[0].upper() + t[1:] if t else t
    return t if len(t) <= 170 else t[:167].rsplit(' ', 1)[0] + '…'

def _horas():
    """linha do REGISTRO -> hora do commit que a acrescentou (o mais antigo)."""
    try:
        out = subprocess.run(['git', '-C', RAIZ, 'log', '--reverse', '--since=2026-11-09', '--format=@@%cI', '-p', '--', 'REGISTRO-DAS-CONTAS.md'],
                             capture_output=True, text=True, timeout=120).stdout
    except Exception:
        return {}
    h, quando = {}, None
    for l in out.split('\n'):
        if l.startswith('@@20'): quando = datetime.fromisoformat(l[2:]).astimezone(SL)
        elif l.startswith('+| ') and quando: h.setdefault(l[1:].strip(), quando)
    return h

def feitos():
    base = json.load(open(os.path.join(D, 'feitos.json')))
    vistos, itens = set(base['vistos']), list(base['itens'])
    linhas = [l.strip() for l in open(REG) if LINHA.match(l)] if os.path.exists(REG) else []
    novas = [l for l in linhas if hashlib.sha1(l.encode()).hexdigest()[:12] not in vistos]
    horas = _horas() if novas else {}
    for l in novas:
        dd, mm, aa, conta, txt = LINHA.match(l).groups()
        q = horas.get(l)
        hx = re.match(r'\s*\[(\d{2}:\d{2})\]\s*', txt)  # hora escrita na linha ("[13:08] ..."), para lançar depois do dia
        if hx: txt = txt[hx.end():]
        itens.append({'d': f'{aa}-{mm}-{dd}', 'h': hx.group(1) if hx else q.strftime('%H:%M') if q and q.strftime('%d/%m/%Y') == f'{dd}/{mm}/{aa}' else '',
                      'conta': conta.strip(), 'txt': _resumo(txt), 'cli': _cli(txt)})
    # Tarefas feitas da Central de Comando (regra de 14/11): entram também no quadro, por cliente, dia e hora
    NOMES = {'jaci': 'Dra. Jaci Cunha', 'leo': 'Leo Pinto', 'oregano': 'Orégano Turbo', 'rt': 'Real Time', 'wf': 'WF Celulares', 'sf': 'Desentupidora SF',
             'tribuna': 'Tribuna 98', 'marca': 'Minha marca', 'outro': 'Outros'}
    try:
        import urllib.request
        r = urllib.request.Request('https://lindsonalmeida.pages.dev/api/automacao?fila=feitas', headers={'Authorization': 'Bearer proxy-injected', 'User-Agent': 'montar-feitos'})
        d = json.load(urllib.request.urlopen(r, timeout=30))
        api = d.get('itens') or (d.get('dados') or {}).get('itens') or []
    except Exception:
        api = []
    ja = {(i['d'], i['txt'][:60].lower()) for i in itens}
    for x in api:
        t = _resumo(x.get('atividade') or '')
        if not t or (x.get('data'), t[:60].lower()) in ja: continue
        itens.append({'d': x.get('data') or '', 'h': x.get('hora') or '', 'conta': x.get('por') or x.get('conta') or '',
                      'txt': t, 'cli': NOMES.get(x.get('cli'), _cli(t))})
    return itens

if __name__ == '__main__':
    F = feitos()
    print(len(F), 'itens')
    for f in sorted(F, key=lambda f: (f['d'], f['h']))[-5:]: print(f)
