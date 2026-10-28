"""Gera a página do app de postagem do Passaporte da Bíblia a partir de pintura.json e do mapa de arquivos enviados.
python3 app_pv.py [ativos.json] -> scratchpad/passaporte-app/index.html"""
import json, os, sys, re
D = os.path.dirname(os.path.abspath(__file__)); RAIZ = os.path.join(D, '..')
OUT = '/tmp/claude-0/-home-user/5acf6937-9ac6-56e0-bc29-78bef210dc8b/scratchpad/passaporte-app'; os.makedirs(OUT, exist_ok=True)
ativos = json.load(open(sys.argv[1])) if len(sys.argv) > 1 and os.path.exists(sys.argv[1]) else {}
ORDEM = ['pv-01'] + [f'short-{i:02d}' for i in range(1, 11)] + ['longo-01', 'longo-02']
spec = {v['id']: v for v in json.load(open(RAIZ + '/pintura.json'))}
itens = []
for k in ORDEM:
    v = spec[k]; longo = v['formato'] == 'longo'
    capas = [{'nome': 'Capa A', 'arq': f'{k}-A.jpg'}, {'nome': 'Capa B', 'arq': f'{k}-B.jpg'}] if longo else [{'nome': 'Capa', 'arq': f'{k}.jpg'}]
    for c in capas: c['url'] = ativos.get(c['arq'])
    itens.append({'id': k, 'tipo': 'longo' if longo else 'short', 'titulo': v['titulo'], 'legenda': v['legenda'], 'comentario': v.get('comentario', ''),
                  'video': ativos.get(f'{k}-app.mp4'), 'arqVideo': f'passaporte-{k}.mp4', 'capas': capas, 'dur': ativos.get(f'{k}-dur', '')})
html = open(D + '/app_pv.html').read().replace('__DADOS__', json.dumps(itens, ensure_ascii=False))
open(OUT + '/index.html', 'w').write(html); print(OUT + '/index.html', sum(1 for i in itens if i['video']), 'vídeos com arquivo')
