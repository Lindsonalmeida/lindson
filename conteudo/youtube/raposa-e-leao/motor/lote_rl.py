"""Raposa e Leão: longos novos (16-20 min) a partir de ../roteiros/longo-*.json, no motor Pintura Viva (identidade Raposa).
python3 lote_rl.py -> ../pintura.json (entrada do motor) e ../longos/NN/publicar_novo.json (textos do app)"""
import json, os, glob
D = os.path.dirname(os.path.abspath(__file__)); R = os.path.join(D, '..')
novos = [json.load(open(f)) for f in sorted(glob.glob(R + '/roteiros/longo-*.json'))]
json.dump([{**{k: v[k] for k in ('id', 'formato', 'titulo', 'legenda', 'comentario', 'titulo_tela', 'cenas')}, 'canal': 'raposa'} for v in novos],
          open(R + '/pintura.json', 'w'), ensure_ascii=False, indent=1)
for v in novos:
    d = f"{R}/longos/{v['id'][-2:]}"; os.makedirs(d, exist_ok=True)
    json.dump(dict(titulo=v['titulo'], legenda=v['legenda'], comentario=v['comentario'], capa=v['capa']), open(d + '/publicar_novo.json', 'w'), ensure_ascii=False, indent=1)
    print(v['id'], len(v['cenas']), 'cenas', sum(len(c['txt'].split()) for c in v['cenas']), 'palavras |', v['titulo'])
