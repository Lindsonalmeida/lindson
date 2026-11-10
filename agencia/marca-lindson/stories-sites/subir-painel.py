"""Sobe os "Stories · Vender sites" para a aba "Minha rede social → Artes" do admin da Central (conta Pedro, 05/11/2026),
do mesmo jeito que ../artes-v2/subir-painel.py: imagens no privado (painel/admin-rede/, só o admin abre), lista em ../artes-aprovadas.json.
As telas de vídeo entram como .mp4 (a aba Artes mostra o vídeo); as paradas como .jpg. A "legenda" é o roteiro de postagem (README).
Uso: python3 subir-painel.py   (depois: montar-site.py e copiar painel/admin.html para o privado)"""
import json, os, re
from PIL import Image
D = os.path.dirname(os.path.abspath(__file__)); ML = os.path.dirname(D)
PRIV = os.environ.get('PRIV', '/home/user/centrallindsonalmeida') + '/painel/admin-rede/stories-sites'
TITULO, VIDEOS = 'Stories · Vender sites', {4, 5, 6, 7}
telas = []
for i in range(1, 11):
    n = f's{i:02d}'
    Image.open(os.path.join(PRIV, n + '.png')).convert('RGB').save(os.path.join(PRIV, n + '.jpg'), quality=90, optimize=True, progressive=True)
    if i in VIDEOS: assert os.path.exists(os.path.join(PRIV, n + '.mp4')), 'falta ' + n + '.mp4 (rode node gerar.js)'
    telas.append(f'/painel/admin-rede/stories-sites/{n}.' + ('mp4' if i in VIDEOS else 'jpg'))
# instruções = tabela da sequência + link + quando postar, em texto simples (vai no "Copiar legenda")
rd = open(os.path.join(D, 'README.md')).read()
seq = re.search(r'## A sequência.*?(?=\n## )', rd, re.S).group(0)
linhas = []
for l in seq.splitlines():
    if l.startswith('|') and not l.startswith('|---') and not l.startswith('| #'):
        c = [x.strip() for x in l.strip('|').split('|')]
        linhas.append(f'TELA {c[0]} ({c[1]}) · {c[3]}\nFigurinha: {c[4]}')
quando = re.search(r'## Quando postar\n(.*?)(?=\n## )', rd, re.S).group(1).strip()
leg = ('Sequência de 10 stories para vender sites (isca SITE, código MS). Postar nesta ordem:\n\n' + '\n\n'.join(linhas).replace('**', '').replace('`', '')
       + '\n\nLink do WhatsApp (tela 10): https://wa.me/5598985621808?text=Oi%2C%20Lindson!%20Quero%20um%20site%20pro%20meu%20neg%C3%B3cio%20(MS)'
       + '\n\nQuando postar:\n' + quando.replace('**', '').replace('`', '')
       + '\n\nVídeos 04 a 07: narração na voz do Lindson, SFX e trilha. Música: Kevin MacLeod (incompetech.com), CC BY 4.0 — pôr o crédito na legenda ou no perfil.')
item = {'data': 'stories', 'titulo': TITULO, 'img': f'/painel/admin-rede/stories-sites/s01.jpg', 'arquivo': 's01.jpg', 'telas': telas, 'legenda': leg}
# 2ª entrada (10/11): um vídeo por cliente, para marcar o cliente (clientes/cliente-<nome>.mp4)
CLI = [('rafael', 'Rafael Imports', '@rafael.imports.slz'), ('sf', 'Desentupidora SF', '@desentupidorasf_slz'), ('tribuna', 'Tribuna 98', '@tribuna98_'),
       ('realtime', 'Real Time', '@realtime_fulljobs'), ('jaci', 'Clínica Dra. Jaci Cunha', '@clinica.drajacicunha')]
PC = os.path.join(PRIV, 'clientes'); itens = [item]
if all(os.path.exists(os.path.join(PC, f'cliente-{n}.mp4')) for n, _, _ in CLI):
    Image.open(os.path.join(PC, 'cliente-rafael.png')).convert('RGB').save(os.path.join(PC, 'cliente-rafael.jpg'), quality=90, optimize=True, progressive=True)
    seccli = re.search(r'## Um vídeo por cliente.*?(?=\n## )', rd, re.S).group(0)
    falas = {}
    for l in seccli.splitlines():
        m = re.match(r'\| cliente-(\w+) \| "(.*?)" \| \*\*(@[^*]+)\*\* \| ([^|]+) \|', l)
        if m: falas[m.group(1)] = (m.group(2), m.group(3), m.group(4).strip())
    leg2 = ('Um vídeo por cliente, para marcar o cliente (figurinha de MENÇÃO no retângulo livre embaixo; a guia mostra o lugar).\n\n'
            + '\n\n'.join(f'{t} · {falas[n][1]} · {falas[n][2]}\nFala: "{falas[n][0]}"' for n, t, _ in CLI)
            + '\n\nPostar um por dia, 18h a 20h, e pedir ao cliente para repostar. Música: Kevin MacLeod (incompetech.com), CC BY 4.0 — pôr o crédito na legenda ou no perfil.')
    itens.append({'data': 'stories', 'titulo': 'Stories · Um vídeo por cliente', 'img': '/painel/admin-rede/stories-sites/clientes/cliente-rafael.jpg', 'arquivo': 'cliente-rafael.jpg',
                  'telas': [f'/painel/admin-rede/stories-sites/clientes/cliente-{n}.mp4' for n, _, _ in CLI], 'legenda': leg2})
json.dump(itens, open(os.path.join(D, 'painel.json'), 'w'), ensure_ascii=False, indent=1)
arq = os.path.join(ML, 'artes-aprovadas.json'); L = json.load(open(arq))
TIT = {i['titulo'] for i in itens}
L = [a for a in L if a.get('titulo') not in TIT] + itens
json.dump(L, open(arq, 'w'), ensure_ascii=False, indent=1)
print(len(L), 'posts na aba Artes ·', ' + '.join(TIT))
