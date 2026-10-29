"""Lote 3 do Passaporte: longos 05 a 09 (16-20 min), roteiros em ../roteiros/<id>.json.
python3 lote3.py -> acrescenta/atualiza em pintura.json e longos.json (capas claras, pouco texto, cores quentes/ciano, sem vermelho)"""
import json, os, glob
D = os.path.dirname(os.path.abspath(__file__)); RAIZ = os.path.join(D, '..')
novos = [json.load(open(f)) for f in sorted(glob.glob(RAIZ + '/roteiros/longo-*.json'))]
def grava(arq, itens):
    f = f'{RAIZ}/{arq}'; d = json.load(open(f)); ids = {v['id'] for v in itens}
    json.dump([v for v in d if v['id'] not in ids] + itens, open(f, 'w'), ensure_ascii=False, indent=1)
pint, lg = [], []
for v in novos:
    pint.append({k: v[k] for k in ('id', 'formato', 'titulo', 'legenda', 'comentario', 'titulo_tela', 'cenas')})
    cp = v['capa']
    lg.append(dict(id=v['id'], titulo=v['titulo'], formato='longo', legenda=v['legenda'], comentario=v['comentario'],
                   capaA=dict(texto=cp['A'], cor='#FFB547', estilo='clara'), capaB=dict(texto=cp['B'], cor='#3FD0D4', estilo='clara'),
                   gravA=cp['gravA'], gravB=cp['gravB']))
grava('pintura.json', pint); grava('longos.json', lg)
for v in novos: print(v['id'], len(v['cenas']), 'cenas', sum(len(c['txt'].split()) for c in v['cenas']), 'palavras', '|', v['titulo'])
