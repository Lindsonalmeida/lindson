# Põe as 19 artes de feed nas Aprovações do painel da Dra. Jaci (privado CentralLindsonALmeida/painel/jaci.html) (conta Leandro, 04/11/2026).
# Imagens em alta (2160x2700) em painel/jaci/feed/ (protegidas pelo login da Central); o botão Baixar arte baixa a alta.
# Uso: python3 subir-painel.py /home/user/centrallindsonalmeida
import json, sys, os, shutil
R = sys.argv[1]; T = json.load(open('textos.json')); P = f'{R}/painel/jaci.html'
os.makedirs(f'{R}/painel/jaci/feed', exist_ok=True)
s = open(P).read(); i = s.index('const APROV=') + len('const APROV='); a, fim = json.JSONDecoder().raw_decode(s[i:])
a = [x for x in a if not x.get('id', '').startswith('feed-')]
for c in T:
    shutil.copy(f'feed/{c["id"]}.jpg', f'{R}/painel/jaci/feed/{c["id"]}.jpg')
    a.append({'id': 'feed-' + c['id'], 't': 'Post de feed', 'titulo': f'{c["data"][4:]} · {c["serif"].replace("_", "").replace("**", "")}',
              'data': f'Postar em {c["data"]}', 'linha': c['linha'], 'st': 'aguardando', 'img': f'/painel/jaci/feed/{c["id"]}.jpg', 'legenda': c['legenda']})
s = s[:i] + json.dumps(a, ensure_ascii=False) + s[i + fim:]
open(P, 'w').write(s); print(len(a), 'itens nas Aprovações')
