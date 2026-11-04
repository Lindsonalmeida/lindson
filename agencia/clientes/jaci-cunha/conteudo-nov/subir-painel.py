# Põe o feed de novembro (19 posts) e de dezembro (4 carrosséis + 6 posts) nas Aprovações do painel da Dra. Jaci
# (privado CentralLindsonALmeida/painel/jaci.html) (conta Leandro, 04/11/2026). Imagens em alta (2160x2700) em painel/jaci/feed/,
# protegidas pelo login da Central; o botão Baixar arte baixa a alta. Itens antigos com id feed-* são trocados.
# Uso (na pasta jaci-cunha): python3 conteudo-nov/subir-painel.py /home/user/centrallindsonalmeida
import json, sys, os, shutil
R = sys.argv[1]; P = f'{R}/painel/jaci.html'; D = f'{R}/painel/jaci/feed'; os.makedirs(D, exist_ok=True)
s = open(P).read(); i = s.index('const APROV=') + len('const APROV='); a, fim = json.JSONDecoder().raw_decode(s[i:])
a = [x for x in a if not x.get('id', '').startswith('feed-')]
lim = lambda t: t.replace('_', '').replace('**', '')
def copia(pasta, nome): shutil.copy(f'{pasta}/feed/{nome}.jpg', f'{D}/{nome}.jpg'); return f'/painel/jaci/feed/{nome}.jpg'
itens = []
for pasta in ('conteudo-nov', 'conteudo-dez'):
    for c in json.load(open(f'{pasta}/textos.json')):
        itens.append((c['pos'], {'id': 'feed-' + c['id'], 't': 'Post de feed', 'titulo': f'{c["data"][4:]} · {lim(c["serif"])}', 'data': f'Postar em {c["data"]}',
                                  'linha': c['linha'], 'st': 'aguardando', 'img': copia(pasta, c['id']), 'legenda': c['legenda']}))
    if os.path.exists(f'{pasta}/carrosseis.json'):
        for k, c in json.load(open(f'{pasta}/carrosseis.json')).items():
            n = len(c['telas'])
            itens.append((c['pos'], {'id': 'feed-' + k, 't': f'Carrossel · {n} telas', 'titulo': f'{c["data"][4:]} · {c.get("titulo") or lim(c["telas"][0]["serif"])}', 'data': f'Postar em {c["data"]}',
                                     'linha': c['linha'], 'st': 'aguardando', 'img': copia(pasta, f'{k}-1'), 'telas': [copia(pasta, f'{k}-{j}') for j in range(2, n + 1)], 'legenda': c['legenda']}))
a += [x for _, x in sorted(itens, key=lambda t: t[0])]
s = s[:i] + json.dumps(a, ensure_ascii=False) + s[i + fim:]
open(P, 'w').write(s); print(len(a), 'itens nas Aprovações')
