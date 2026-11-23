"""Copia coordenacao/fila.json para o quadro do admin (window.__FILA no painel/admin.html do privado). Rode em toda rodada de coordenação (conta Leandro, 16/11/2026).
Desde 23/11/2026 o montar-site.py já gera o window.__FILA na remontagem; este script só atualiza a fila entre uma remontagem e outra.
Se o admin.html não tiver window.__FILA (remontagem antiga), ele insere antes do window.__QUADRO. Também confere que o admin-quadro.js já lê a fila.
python3 coordenacao/sync_painel.py [/caminho/do/centrallindsonalmeida]"""
import json, os, sys
AQUI = os.path.dirname(os.path.abspath(__file__)); PRIV = sys.argv[1] if len(sys.argv) > 1 else '/home/user/centrallindsonalmeida'
f = json.load(open(os.path.join(AQUI, 'fila.json')))
blob = 'window.__FILA=' + json.dumps({'atualizado': f.get('atualizado', ''), 'itens': [{k: i.get(k, '') for k in ('id', 'cli', 'tarefa', 'equipe', 'status')} for i in f.get('itens', [])]}, ensure_ascii=False).replace('</', '<\\/') + ';\n'
p = os.path.join(PRIV, 'painel', 'admin.html'); s = open(p).read()
if 'window.__FILA=' in s:
    a = s.index('window.__FILA='); b = s.index(';\n', a) + 2; s = s[:a] + blob + s[b:]
elif 'window.__QUADRO=' in s:
    a = s.index('window.__QUADRO='); s = s[:a] + blob + s[a:]
else: sys.exit('admin.html sem window.__QUADRO: remonte com montar-site.py')
if 'window.__FILA' not in s.split(blob, 1)[1]: print('AVISO: o admin-quadro.js deste admin.html ainda não lê a fila; remonte o site')
open(p, 'w').write(s); print('quadro do admin atualizado:', len(f['itens']), 'itens')
