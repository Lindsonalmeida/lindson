"""Sobe as artes da marca do Lindson para a aba "Minha rede social → Artes" do admin da Central (conta Pedro, 04/11/2026).
- Imagens (têm o rosto dele) vão para o repositório PRIVADO: painel/admin-rede/<id>.jpg. O _middleware de /painel só deixa o admin abrir
  essa pasta (o 2º trecho do caminho, "admin-rede", não é cliente nenhum).
- A lista com título, data, telas e legenda SEO vai para agencia/marca-lindson/artes-aprovadas.json (público, sem imagem), lido pelo montar-site.py.
Uso: python3 subir-painel.py   (depois: montar-site.py e copiar painel/admin.html para o privado)"""
import json, os, re
from PIL import Image
D = os.path.dirname(os.path.abspath(__file__)); ML = os.path.dirname(D)
PRIV = '/home/user/centrallindsonalmeida/painel/admin-rede'
# (data, título, [telas], chave da legenda no LEGENDAS.md)
POSTS = [
 ('08/11', 'Apresentação · Prazer, Lindson (fixar)', ['a1p'], 'a1'),
 ('08/11', 'Apresentação · Do perfil ao WhatsApp (fixar)', ['a2'], 'a2'),
 ('09/11', 'Reels · Post de bom dia não vende nada', ['r1p'], 'r1'),
 ('10/11', 'Carrossel · Arrume sua bio em 3 passos', ['c1_1', 'c1_2', 'c1_3', 'c1_4', 'c1_5'], 'c1'),
 ('11/11', 'Reels · Um mês de vídeos em um dia', ['r2'], 'r2'),
 ('12/11', 'Reels · Mini site da Rafael Imports', ['r3'], 'r3'),
 ('13/11', 'Post · Avaliação gratuita do perfil', ['p1p'], 'p1'),
 ('14/11', 'Carrossel · Eu mudei a minha marca', ['c2yp', 'c2_2', 'c2_3', 'c2_4'], 'c2'),
 ('15/11', 'Reels · Mito: precisa postar todo dia', ['r4'], 'r4'),
 ('16/11', 'Reels · Responder só o preço faz o cliente sumir', ['s2_r5'], 's2_r5'),
 ('17/11', 'Carrossel · 5 coisas que todo perfil que vende tem', ['s2_c3_1', 's2_c3_2', 's2_c3_3', 's2_c3_4', 's2_c3_5'], 's2_c3'),
 ('18/11', 'Reels · A diária da Desentupidora SF', ['s2_r6'], 's2_r6'),
 ('19/11', 'Reels · O site da Desentupidora SF', ['s2_r7'], 's2_r7'),
 ('20/11', 'Post · Me manda seu anúncio que eu reviso', ['s2_p2'], 's2_p2'),
 ('21/11', 'Carrossel · Antes × depois: a bio da Dra. Jaci', ['s2_c4_1', 's2_c4_2', 's2_c4_3', 's2_c4_4'], 's2_c4'),
 ('22/11', 'Reels · Dancinha não vende serviço', ['s2_r8'], 's2_r8'),
 ('23/11', 'Reels · Seu concorrente pior está levando seu cliente', ['m1'], 'm1'),
 ('24/11', 'Carrossel · O que responder quando perguntam o preço (capa)', ['m2'], 'm2'),
 ('25/11', 'Reels · Os 3 passos do primeiro mês comigo', ['m3'], 'm3'),
 ('26/11', 'Reels · O painel que meus clientes usam', ['m4'], 'm4'),
 ('27/11', 'Post · 3 roteiros do seu nicho, de graça', ['m5'], 'm5'),
 ('28/11', 'Carrossel · Perfil sem e com destaques (capa)', ['m6'], 'm6'),
 ('29/11', 'Reels · O que a campanha política me ensinou', ['m7'], 'm7'),
 ('30/11', 'Reels · Impulsionar não é anunciar', ['m8'], 'm8'),
 ('01/12', 'Carrossel · Checklist do Natal (capa)', ['m9'], 'm9'),
 ('02/12', 'Reels · Bastidor: cliente novo', ['m10'], 'm10'),
 ('perfil', 'Foto de perfil', ['perfil-pf'], None),
 ('perfil', 'Capas de destaques: Comece aqui, Avaliação, Clientes, Bastidor, Mini site, Contato', ['perfil-h1', 'perfil-h2', 'perfil-h3', 'perfil-h4', 'perfil-h5', 'perfil-h6'], None),
]
# legendas: blocos "## DD/MM · chave · ..." até o próximo "---"
txt = open(os.path.join(D, 'LEGENDAS.md')).read()
LEG = {}
for m in re.finditer(r'^## [^\n]*?· (\w+) ·[^\n]*\n(.*?)(?=\n---|\Z)', txt, flags=re.S | re.M):
    LEG[m.group(1)] = m.group(2).strip()
os.makedirs(PRIV, exist_ok=True)
saida = []
for data, titulo, telas, chave in POSTS:
    for t in telas:
        im = Image.open(os.path.join(D, 'artes', t + '.png')).convert('RGB')
        im.save(os.path.join(PRIV, t + '.jpg'), quality=88, optimize=True, progressive=True)
    leg = LEG.get(chave, '') if chave else ''
    if chave and not leg: raise SystemExit('sem legenda para ' + chave)
    saida.append({'data': data, 'titulo': titulo, 'img': '/painel/admin-rede/' + telas[0] + '.jpg', 'arquivo': telas[0] + '.jpg',
                  'telas': ['/painel/admin-rede/' + t + '.jpg' for t in telas], 'legenda': leg})
json.dump(saida, open(os.path.join(ML, 'artes-aprovadas.json'), 'w'), ensure_ascii=False, indent=1)
print(len(saida), 'posts ·', sum(len(p[2]) for p in POSTS), 'imagens')
