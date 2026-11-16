"""Copia coordenacao/fila.json para o quadro do admin (window.__FILA no painel/admin.html do privado). Rode em toda rodada de coordenação (conta Leandro, 16/11/2026).
python3 coordenacao/sync_painel.py [/caminho/do/centrallindsonalmeida]"""
import json, os, sys
AQUI = os.path.dirname(os.path.abspath(__file__)); PRIV = sys.argv[1] if len(sys.argv) > 1 else '/home/user/centrallindsonalmeida'
f = json.load(open(os.path.join(AQUI, 'fila.json')))
blob = 'window.__FILA=' + json.dumps({'atualizado': f.get('atualizado', ''), 'itens': [{k: i.get(k, '') for k in ('id', 'cli', 'tarefa', 'equipe', 'status')} for i in f['itens']]}, ensure_ascii=False).replace('</', '<\\/') + ';\n'
p = os.path.join(PRIV, 'painel', 'admin.html'); s = open(p).read(); a = s.index('window.__FILA='); b = s.index(';\n', a) + 2
open(p, 'w').write(s[:a] + blob + s[b:]); print('quadro do admin atualizado:', len(f['itens']), 'itens')
