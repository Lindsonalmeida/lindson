# Sobe o kit do canal do YouTube no painel da Orégano (/painel/oregano, aba Aprovações, no topo):
# imagens, textos com "Copiar legenda" e botão Baixar. Aplica direto no oregano.html já publicado (não roda o montador inteiro,
# porque o HTML no ar tem edições à mão). Idempotente. Uso: python3 subir_painel.py [pasta do privado]. Conta Zuleide, 15/11/2026.
import json, os, re, shutil, sys
YT = os.path.dirname(os.path.abspath(__file__))
PRIV = sys.argv[1] if len(sys.argv) > 1 else os.path.join(YT, '..', '..', '..', '..', 'centrallindsonalmeida')
YO = os.path.join(PRIV, 'painel', 'oregano', 'youtube'); os.makedirs(YO, exist_ok=True)
txt = open(os.path.join(YT, 'TEXTOS.md')).read(); est = open(os.path.join(YT, 'ESTRATEGIA.md')).read()
shutil.copy(os.path.join(YT, 'TEXTOS.md'), os.path.join(YO, 'textos-youtube.txt'))
bloco = lambda ini: txt.split(ini, 1)[1].split('\n## ', 1)[0].strip()
pecas = [('previa.jpg', 'Prévia do kit + estratégia do canal', est),
         ('pecas/banner-2560x1440.jpg', 'Banner 2560x1440 + descrição do canal', bloco('## Descrição do canal')),
         ('pecas/perfil-800.jpg', 'Foto de perfil 800x800 + nome e @', bloco('## Nome e @')),
         ('pecas/marca-dagua-150.png', "Marca-d'água 150x150 + links do canal", bloco('## Links do canal')),
         ('pecas/thumb-longo-1-dia-fraco.jpg', 'Thumb longo 1 + 4 ideias de longos', bloco('## 4 vídeos longos')),
         ('pecas/thumb-longo-2-taxa-do-app.jpg', 'Thumb longo 2 + palavras-chave', bloco('## Palavras-chave do canal')),
         ('pecas/capa-short-1080x1920.jpg', 'Capa de Short + roteiro do trailer', bloco('## Roteiro do trailer')),
         (None, 'Títulos e descrições SEO dos 21 Shorts', bloco('## Shorts'))]
yt = []
for arq, tit, leg in pecas:
    it = {'t': 'YouTube', 'yt': 1, 'titulo': 'YouTube · ' + tit, 'data': 'Kit do canal v2 (identidade do Instagram) · 15/11 · conta Zuleide', 'linha': 'Canal do YouTube',
          'st': 'pendente', 'por': 'aguardando o Lindson', 'legenda': leg}
    if arq:
        nome = os.path.basename(arq); shutil.copy(os.path.join(YT, arq), os.path.join(YO, nome)); it['img'] = it['baixar'] = f'/painel/oregano/youtube/{nome}'
    else:
        it['baixar'] = '/painel/oregano/youtube/textos-youtube.txt'
    yt.append(it)
p = os.path.join(PRIV, 'painel', 'oregano.html'); s = open(p).read()
s = re.sub(r'\{"t": "YouTube", "yt": 1, .*?\},(?=\{)', '', s)  # tira a versão anterior
i = s.index('const APROV=') + len('const APROV=') + 1
s = s[:i] + ','.join(json.dumps(x, ensure_ascii=False) for x in yt) + ',' + s[i:]
B = '<div class="post">${p.baixar?`<a class="btn lin" href="${p.baixar}" download style="margin:10px 12px;display:block;text-align:center">⬇ Baixar</a>`:\'\'}'
a = '<div class="post">${p.video?'
if B not in s:
    assert a in s, 'o modelo mudou'; s = s.replace(a, B + '${p.video?', 1)
open(p, 'w').write(s); print(len(yt), 'itens do YouTube no painel')
