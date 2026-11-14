# Confere cada citação em italiano do produto contra a tabela de citações conferidas do acervo.
import csv, re, sys, unicodedata
sys.path.insert(0, '.')
import conteudo as C
def norm(s):
    s = unicodedata.normalize('NFD', s.lower()); s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    return re.sub(r'\s+', ' ', re.sub(r'[^a-z ]', ' ', s)).strip()
T = '../../../../referencias/maquiavel/revisao/citacoes-tabela.tsv'
rows = list(csv.DictReader(open(T, encoding='utf-8'), delimiter='\t'))
ok = [(norm(r['citacao'] + ' ' + (r['trecho_original'] or '')), r) for r in rows if r['resultado'].startswith('exata') or 'grafia' in r['resultado'] or 'mão' in r['resultado']]
EXTRA = ["bisogna adunque essere golpe a conoscere e' lacci, e lione a sbigottire e' lupi", "lo troverrà uno ferocissimo lione e una astutissima golpe"]
itens = [(f"S{i+1}", s['it']) for i, s in enumerate(C.S)] + [(f"F{i+1}", f['it']) for i, f in enumerate(C.FALSAS)] + [("X", e) for e in EXTRA]
falhas = 0
for k, q in itens:
    for parte in re.split(r'\(…\)', q):
        n = norm(parte); hit = next((r for t, r in ok if n in t), None)
        if hit: print('OK  ', k, '|', hit['resultado'][:28], '|', hit['obra_encontrada'][:40], '|', hit['arquivo'], hit['linha'])
        else: falhas += 1; print('FALHA', k, '|', parte)
print('falhas:', falhas)
