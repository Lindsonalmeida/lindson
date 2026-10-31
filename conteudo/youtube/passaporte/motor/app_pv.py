"""Gera a página do app de postagem do Passaporte da Bíblia a partir de pintura.json e do mapa de arquivos enviados.
python3 app_pv.py [ativos.json] -> scratchpad/passaporte-app/index.html"""
import json, os, sys, re
D = os.path.dirname(os.path.abspath(__file__)); RAIZ = os.path.join(D, '..')
OUT = '/tmp/claude-0/-home-user/5acf6937-9ac6-56e0-bc29-78bef210dc8b/scratchpad/passaporte-app'; os.makedirs(OUT, exist_ok=True)
ativos = json.load(open(sys.argv[1])) if len(sys.argv) > 1 and os.path.exists(sys.argv[1]) else {}
ORDEM = ['pv-01'] + [f'short-{i:02d}' for i in range(1, 21)] + [f'longo-{i:02d}' for i in range(1, 10)]
spec = {v['id']: v for v in json.load(open(RAIZ + '/pintura.json'))}
TEMPOS = json.load(open(RAIZ + '/tempos.json')) if os.path.exists(RAIZ + '/tempos.json') else {}
itens = []
SO = [x for x in os.environ.get('IDS', '').split(',') if x]  # IDS=longo-06,longo-07 limita o app a esses vídeos
for k in [x for x in ORDEM if x in spec and (not SO or x in SO)]:
    v = spec[k]; longo = v['formato'] == 'longo'
    capas = [{'nome': 'Capa A', 'arq': f'{k}-A.jpg'}, {'nome': 'Capa B', 'arq': f'{k}-B.jpg'}, {'nome': 'Capa C', 'arq': f'{k}-C.jpg'}] if longo else [{'nome': 'Capa', 'arq': f'{k}.jpg'}]
    for c in capas: c['url'] = ativos.get(c['arq'])
    capas = [c for c in capas if c['url'] or not c['arq'].endswith('-C.jpg')]
    itens.append({'id': k, 'tipo': 'longo' if longo else 'short', 'titulo': v['titulo'], 'legenda': v['legenda'].replace('{CAPITULOS}', '\n'.join(f'{a} {b}' for a, b in TEMPOS.get(k, []))), 'comentario': v.get('comentario', ''),
                  'video': ativos.get(f'{k}-app.mp4'), 'arqVideo': f'passaporte-{k}.mp4', 'capas': capas, 'dur': ativos.get(f'{k}-dur', '')})
html = open(D + '/app_pv.html').read().replace('__DADOS__', json.dumps(itens, ensure_ascii=False))
open(OUT + '/index.html', 'w').write(html); print(OUT + '/index.html', sum(1 for i in itens if i['video']), 'vídeos com arquivo')
