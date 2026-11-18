#!/usr/bin/env python3
"""Canais dark dentro da Central (conta Leandro, 09/11/2026): monta /painel/canais no repositório privado.

Pedido do Lindson (09/11/2026): "exclua os apps externos dos canais dark e converta eles para dentro da central".
Substitui os apps de postagem (artifacts do claude.ai) do Passaporte da Bíblia e do Raposa e Leão.

Lê deste repositório (os mesmos dados dos geradores antigos):
  passaporte/pintura.json, passaporte/tempos.json, passaporte/ativos.json (app antigo) e ativos-novo.json (app atual)  ← motor/app_pv.py
  raposa-e-leao/shorts/NN/publicar.json, longos/NN/publicar*.json, raposa-e-leao/tempos.json e ativos*.json         ← motor/app_rl.py
Gera no privado (clone em ../centrallindsonalmeida, ao lado deste):
  painel/canais.html                 → a página (canais.html desta pasta + movimento.js do modelo), só o admin abre
  painel/canais/dados.js             → window.__CANAIS={...} (.js porque o site bloqueia .json)
  painel/canais/<canal>/capas/*.jpg  → capas (JPEG ≤ 300 KB)
  painel/canais/<canal>/videos/*.mp4 → vídeos ≤ 20 MB ainda não postados (só se o total couber no limite)
E aqui: MIGRACAO.md (cada arquivo: migrado, link antigo ou sem acesso).

Mídia: os arquivos vêm dos apps antigos (assets /_blob/<id>). Baixe com o Artifact tool (action read, url do app, path = id)
e passe a pasta onde eles caíram em --cache (procura <id>.* em qualquer subpasta). O que já está no privado é reaproveitado.

Uso:
  python3 montar-canais.py --manifesto saida.json        # lista dos assets que faltam baixar (app, id, chave)
  python3 montar-canais.py --cache <pasta> [--videos]    # monta tudo; --videos copia os vídeos mesmo acima do limite
  [--privado /caminho/do/privado]
"""
import glob, json, os, re, shutil, sys
from io import BytesIO

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.abspath(os.path.join(AQUI, '..', '..', '..'))
YT = os.path.join(RAIZ, 'conteudo', 'youtube')
PRIV = os.path.abspath(os.path.join(RAIZ, '..', 'centrallindsonalmeida'))
arg = lambda k: sys.argv[sys.argv.index(k) + 1] if k in sys.argv else None
if arg('--privado'): PRIV = os.path.abspath(arg('--privado'))
CACHE = arg('--cache')
LIMITE_VIDEO = 20 * 1024 * 1024      # Cloudflare Pages aceita até 25 MB por arquivo
LIMITE_TOTAL = 300 * 1024 * 1024     # acima disso, não copia vídeo nenhum sem --videos (o repositório não deve inchar)
LIMITE_CAPA = 300 * 1024

APPS = {
    'passaporte': {'novo': 'https://claude.ai/artifact/CT3Z4M3yrzGrqCt3nh95ak', 'antigo': 'https://claude.ai/artifact/1aUURghpLqrWgTQmkvBcG4'},
    'raposa': {'novo': 'https://claude.ai/artifact/2k4SSuvALdqXDcXnBQMVZH', 'antigo': 'https://claude.ai/artifact/LSTErmeSra3qxFKBJMLiTC'},
}
# o que já saiu (MEMORIA-DO-LINDSON.md, 09/11/2026): o painel começa com eles marcados; o Lindson desmarca se precisar
JA = {
    'passaporte': {**{k: 'postado' for k in ['pv-01'] + [f'short-{i:02d}' for i in range(1, 11)]},
                   **{f'short-{i:02d}': 'programado no Metricool' for i in range(11, 21)}},
    'raposa': {f'short-{i:02d}': 'postado' for i in range(1, 11)},
}


def jl(p, padrao=None):
    return json.load(open(p, encoding='utf-8')) if os.path.exists(p) else padrao


def mapa_ativos(canal):
    """chave → (url do app, id do asset). O app atual (ativos-novo) vence o antigo (ativos)."""
    pasta = os.path.join(YT, 'passaporte' if canal == 'passaporte' else 'raposa-e-leao')
    out = {}
    for arq, app in [('ativos.json', 'antigo'), ('ativos-novo.json', 'novo')]:
        for k, v in jl(os.path.join(pasta, arq), {}).items():
            if isinstance(v, str) and v.startswith('/_blob/'): out[k] = (APPS[canal][app], v.split('/')[-1])
            else: out[k + '#txt'] = v  # durações ('longo-01-dur' → '19:42')
    return out


def dur(at, k):
    return at.get(k + '-dur#txt', '')


# ---------- Passaporte (mesma lógica de passaporte/motor/app_pv.py) ----------
def itens_passaporte():
    at, R = mapa_ativos('passaporte'), os.path.join(YT, 'passaporte')
    ordem = ['pv-01'] + [f'short-{i:02d}' for i in range(1, 21)] + [f'longo-{i:02d}' for i in range(1, 13)]
    spec = {v['id']: v for v in jl(R + '/pintura.json', [])}
    tempos = jl(R + '/tempos.json', {})
    out = []
    for k in [x for x in ordem if x in spec]:
        v = spec[k]; longo = v['formato'] == 'longo'
        capas = [(f'Capa {x}', f'{k}-{x}.jpg') for x in 'ABC'] if longo else [('Capa', f'{k}.jpg')]
        capas = [dict(nome=n, arq=a, fonte=at.get(a)) for n, a in capas if at.get(a)]
        vid = at.get(f'{k}-app.mp4')
        if not capas and not vid: continue  # longos 10-12 ainda sem arquivo: entram quando subirem
        cap = '\n'.join(f'{a} {b}' for a, b in tempos.get(k, []))
        out.append(dict(id=k, tipo='longo' if longo else 'short', titulo=v['titulo'], legenda=v['legenda'].replace('{CAPITULOS}', cap),
                        comentario=v.get('comentario', ''), dur=dur(at, k),
                        capas=capas, video=dict(arq=f'passaporte-{k}.mp4', fonte=vid) if vid else None))
    return out


# ---------- Raposa e Leão (mesma lógica de raposa-e-leao/motor/app_rl.py) ----------
def itens_raposa():
    at, R = mapa_ativos('raposa'), os.path.join(YT, 'raposa-e-leao')
    src = open(os.path.join(R, 'motor', 'app_rl.py'), encoding='utf-8').read()
    ns = {}; exec(re.search(r"TAGS = .*?\n}\n", src, re.S).group(0), ns)  # TAGS, FONTE e L15 (textos dos longos 01-05) do gerador antigo
    TAGS, FONTE, L15 = ns['TAGS'], ns['FONTE'], ns['L15']

    def publicar_md(f):
        s = open(f, encoding='utf-8').read()
        tit = re.search(r'\*\*Título[^\n]*\n(.+)', s).group(1).strip()
        desc = re.search(r'\*\*Descrição:\*\*\n(.*?)\n\*\*Na hora', s, re.S).group(1).strip()
        com = re.search(r'Comentário fixado: "(.+?)"\s*$', s, re.M)
        return tit, desc, com.group(1) if com else ''
    agenda = {}  # Shorts 31+ (14/11/2026): agenda e arquivos finais no próprio repositório
    for f in glob.glob(R + '/shorts/PUBLICAR-*.md'):
        for m in re.finditer(r'^\| (\d\d) \| (\d\d/\d\d) \| (\d\dh) \|', open(f, encoding='utf-8').read(), re.M): agenda[m.group(1)] = f'{m.group(2)} às {m.group(3)}'
    out = []
    for d in sorted(glob.glob(R + '/shorts/[0-9][0-9]')):
        n = d.split('/')[-1]; k = f'short-{n}'
        if os.path.exists(d + '/publicar.json'): p = jl(d + '/publicar.json'); tit, desc, com = p['titulo'], p['legenda'], p['comentario']
        elif os.path.exists(d + '/PUBLICAR.md'): tit, desc, com = publicar_md(d + '/PUBLICAR.md')
        else: continue
        vid = at.get(f'{k}.mp4')
        out.append(dict(id=k, tipo='short', titulo=tit, legenda=desc, comentario=com, dur=dur(at, k),
                        capas=[dict(nome='Capa', arq=f'{k}.jpg', fonte=at.get(f'{k}.jpg'))] if at.get(f'{k}.jpg') else [],
                        video=dict(arq=f'raposa-e-leao-{k}.mp4', fonte=vid) if vid else None))
        if int(n) >= 31:
            it = out[-1]; it['agenda'] = agenda.get(n, '')
            if not it['capas'] and os.path.exists(d + '/capa.jpg'): it['capas'] = [dict(nome='Capa', arq=f'{k}.jpg', fonte=(APPS['raposa']['novo'], ''), local=d + '/capa.jpg')]
            if not it['video'] and os.path.exists(d + '/video.mp4'): it['video'] = dict(arq=f'raposa-e-leao-{k}.mp4', fonte=(APPS['raposa']['novo'], ''), local=d + '/video.mp4')
    tp_all = jl(os.path.join(R, 'tempos.json'), {})
    for d in sorted(glob.glob(R + '/longos/[0-9][0-9]'), key=lambda x: (not os.path.exists(x + '/publicar_novo.json'), x)):
        n = d.split('/')[-1]; k = f'longo-{n}'; rot = jl(d + '/roteiro.json', {})
        if os.path.exists(d + '/publicar.json'): p = jl(d + '/publicar.json'); tit, leg, com = p['titulo'], p['legenda'], p['comentario']
        elif n in L15:
            intro, fonte, com = L15[n]; tit = rot['titulo']
            leg = f'{intro}\n\nEm cada lição tem uma aplicação prática para o trabalho, os negócios e as relações.\n\n📜 Fonte: Nicolau Maquiavel, {fonte}\n{FONTE}\n\n{TAGS}'
        elif os.path.exists(d + '/publicar_novo.json'):
            p = jl(d + '/publicar_novo.json'); tit, leg, com = p['titulo'], p['legenda'], p['comentario']
            leg = leg.replace('{CAPITULOS}', '\n'.join(f'{x} {y}' for x, y in tp_all.get(k, [])) or '(os capítulos entram quando o vídeo ficar pronto)')
        else: continue
        capas = [dict(nome=f'Capa {x}', arq=f'{k}-{x}.jpg', fonte=at.get(f'{k}-{x}.jpg')) for x in 'ABC' if at.get(f'{k}-{x}.jpg')]
        if not capas: capas = [dict(nome=f'Capa {x}', arq=f'{k}-{x}.jpg', fonte=(APPS['raposa']['novo'], ''), local=f'{R}/capas/{k}-{x}.jpg') for x in 'ABC' if os.path.exists(f'{R}/capas/{k}-{x}.jpg')]
        vid = at.get(f'{k}.mp4')
        video = dict(arq=f'raposa-e-leao-{k}.mp4', fonte=vid) if vid else None
        if not video and os.path.exists(d + '/video-720.mp4'): video = dict(arq=f'raposa-e-leao-{k}.mp4', fonte=(APPS['raposa']['novo'], ''), local=d + '/video-720.mp4')  # longos 17+ (conta Leandro): versão ≤ 20 MB, fora do Git
        out.append(dict(id=k, tipo='longo', titulo=tit, legenda=leg, comentario=com, dur=dur(at, k) or jl(d + '/publicar.json', {}).get('dur', ''), capas=capas, video=video))
        if jl(d + '/publicar.json', {}).get('agenda'): out[-1]['agenda'] = jl(d + '/publicar.json')['agenda']
    return out


# ---------- Pagode Fiado e materiais de cada canal (conta Leandro, 16/11/2026) ----------
# Pedido do Lindson (16/11/2026): "crie no painel uma aba de cliente só dos canais dark, e coloque dentro os 3 canais".
# Aprovações (arte + legenda, Aprovar / Pedir ajuste) e Materiais (produto, kits, brand book) lidos do privado.
def legendas_md(f):
    """**NN · Título** seguido das linhas da legenda até a linha em branco → {NN: (título, legenda)}."""
    out = {}
    if not os.path.exists(f): return out
    for m in re.finditer(r'^\*\*(\d\d) · (.+?)\*\*\n(.*?)(?:\n\s*\n|\Z)', open(f, encoding='utf-8').read(), re.M | re.S):
        out[m.group(1)] = (m.group(2).strip(), m.group(3).strip())
    return out


def pagode():
    P = os.path.join(PRIV, 'painel', 'pagode'); leg = legendas_md(os.path.join(P, 'frases-v1', 'LEGENDAS.md'))
    aprov = [dict(id=f'frase-{n}', titulo=t, legenda=l, img=f'/painel/pagode/frases-v1/frase-{n}.jpg', serie='Frases v1 · feed 4:5')
             for n, (t, l) in sorted(leg.items()) if os.path.exists(os.path.join(P, 'frases-v1', f'frase-{n}.jpg'))]
    # brand book: está em dados/ (o site bloqueia), então a prévia e o PDF vêm para painel/canais/pagode/brand-book/
    bb_o, bb_d = os.path.join(PRIV, 'dados', 'agencia', 'pagode-fiado', 'brand-book'), os.path.join(PRIV, 'painel', 'canais', 'pagode', 'brand-book')
    for a in ('brand-book-pagode.pdf', 'previa-capa.jpg', 'previa-folha.jpg'):
        if os.path.exists(os.path.join(bb_o, a)):
            os.makedirs(bb_d, exist_ok=True)
            shutil.copyfile(os.path.join(bb_o, a), os.path.join(bb_d, a))
    mat = [dict(titulo='Brand book do Pagode Fiado', sub='Identidade do canal: paleta mesa de bar, Shrikhand e Work Sans, caderno do fiado.', st='aguardando aprovação',
                imgs=['/painel/canais/pagode/brand-book/previa-capa.jpg', '/painel/canais/pagode/brand-book/previa-folha.jpg'],
                links=[dict(nome='Baixar o PDF', url='/painel/canais/pagode/brand-book/brand-book-pagode.pdf')])]
    if os.path.exists(os.path.join(RAIZ, 'agencia', 'clientes', 'pagode-fiado', 'playlists-v1', 'README.md')):
        mat.append(dict(titulo='Playlists v1 · clássicos + Pagode Fiado', sub='5 playlists de curadoria (Sexta de Resenha, Sofrência de Domingo, Pagode Romântico 2026, Anos 90 e 2000, Pagode de Boteco): 3 clássicos oficiais e 1 faixa do Pagode Fiado. Só links oficiais, sem reupload.', st='travado: falta criar o canal e os perfis do Pagode',
                        texto='Plano completo no repositório: agencia/clientes/pagode-fiado/playlists-v1/README.md (conta Zuleide, 16/11). Conferir cada faixa no canal oficial ao adicionar.', links=[]))
    LV = os.path.join(PRIV, 'painel', 'canais', 'pagode', 'longos-v1')
    for k, t in (('05', 'Bilhete na Geladeira'), ('07', 'Visualizou e Não Voltou')):
        if os.path.exists(os.path.join(LV, f'pagode-fiado-{k}-longo.mp4')):
            mat.append(dict(titulo=f'Longo {k} · {t}', sub='Faixa inteira (~3 min, 16:9) com letra sincronizada, fotos de boteco e roda de samba, quadro FIADO e fecho "Pendura na conta". Título, descrição e tags em agencia/clientes/pagode-fiado/longos-v1/publicar.json.', st='aguardando aprovação',
                            imgs=[f'/painel/canais/pagode/longos-v1/capa-{k}.jpg'],
                            links=[dict(nome='Assistir / baixar o vídeo', url=f'/painel/canais/pagode/longos-v1/pagode-fiado-{k}-longo.mp4')]))
    avisos = ['Notícias v1: reprovado pelo Lindson em 16/11. A equipe está refazendo a v2; não aparece aqui para aprovar.'] if os.path.isdir(os.path.join(P, 'noticias-v1')) else []
    return aprov, mat, avisos


def materiais_passaporte():
    B = '/painel/canais/passaporte'; L = os.path.join(PRIV, 'painel', 'canais', 'passaporte')
    m = []
    if os.path.isdir(L + '/produto-hubla'):
        m.append(dict(titulo='Produto Hubla · Volume 1', sub='Guia em PDF de 19 páginas A4 (gravuras de Doré). Antes de vender: preencher o revisor teológico na última página.', st='aguardando aprovação',
                      imgs=[B + '/produto-hubla/previa-capa.png'], links=[dict(nome='Baixar o PDF', url=B + '/produto-hubla/passaporte-da-biblia-v1.pdf'), dict(nome='Página de venda', url=B + '/produto-hubla/')]))
    if os.path.isdir(L + '/instagram'):
        im = sorted(glob.glob(L + '/instagram/*.png'))
        m.append(dict(titulo='Kit Instagram @passaportedabiblia', sub='Foto de perfil e capas dos destaques na identidade do canal. Nada publicado: você aplica no app.', st='aguardando aprovação',
                      imgs=[B + '/instagram/' + os.path.basename(x) for x in im], links=[dict(nome='Baixar ' + os.path.basename(x)[:-4].replace('-', ' '), url=B + '/instagram/' + os.path.basename(x)) for x in im]))
    if os.path.exists(L + '/tiktok/README.md'):
        t = open(L + '/tiktok/README.md', encoding='utf-8').read()
        bio = re.search(r'> (.+)', t)
        m.append(dict(titulo='Kit TikTok @passaportedabiblia', sub='Mesmo perfil do YouTube e do Instagram (mesma foto). Nada publicado: você aplica no app.', st='aguardando aprovação',
                      imgs=[B + '/instagram/foto-perfil.png'] if os.path.exists(L + '/instagram/foto-perfil.png') else [], texto=('Bio: ' + bio.group(1).strip()) if bio else '', links=[]))
    return m


PG_APROV, PG_MAT, PG_AVISOS = pagode()
CANAIS = [
    dict(id='passaporte', nome='Passaporte da Bíblia', sub='Gravuras de Doré com narração. Shorts todo dia e um longo por semana (Metricool, marca 7990533).', itens=itens_passaporte(),
         aprov=[], materiais=materiais_passaporte(), avisos=[]),
    dict(id='raposa', nome='Raposa e Leão', sub='Maquiavel e as leis do poder. Shorts de 2 em 2 h pelo YouTube Studio; longos de 16 a 20 min.', itens=itens_raposa(),
         aprov=[], materiais=[], avisos=[]),
    dict(id='pagode', nome='Pagode Fiado', sub='Canal dark de música: seis amigos no Bar do Seu Tião, toda sexta. "Pendura na conta."', itens=[],
         aprov=PG_APROV, materiais=PG_MAT, avisos=PG_AVISOS),
]


def no_cache(blob):
    if not CACHE: return None
    achou = glob.glob(os.path.join(CACHE, '**', blob + '.*'), recursive=True)
    return achou[0] if achou else None


def capa_jpeg(orig, dest):
    from PIL import Image
    im = Image.open(orig).convert('RGB')
    larg = 1280 if im.width >= im.height else 720
    if im.width > larg: im = im.resize((larg, round(im.height * larg / im.width)), Image.LANCZOS)
    for q in (86, 80, 74, 68, 60, 52):
        b = BytesIO(); im.save(b, 'JPEG', quality=q, optimize=True, progressive=True)
        if b.tell() <= LIMITE_CAPA: break
    os.makedirs(os.path.dirname(dest), exist_ok=True); open(dest, 'wb').write(b.getvalue())


def montar():
    linhas, pend, tot_vid, manif = [], [], 0, []
    base = os.path.join(PRIV, 'painel', 'canais')
    # 1 · capas
    for c in CANAIS:
        for v in c['itens']:
            v['pre'] = JA.get(c['id'], {}).get(v['id'], '')
            for cp in v['capas']:
                app, blob = cp.pop('fonte'); rel = f"{c['id']}/capas/{cp['arq']}"; dest = os.path.join(base, rel); loc = cp.pop('local', None)
                if loc and (not os.path.exists(dest) or os.path.getmtime(loc) > os.path.getmtime(dest)): capa_jpeg(loc, dest)
                if not os.path.exists(dest) and no_cache(blob): capa_jpeg(no_cache(blob), dest)
                if os.path.exists(dest): cp['url'] = '/painel/canais/' + rel; st = 'migrado'
                else: cp['url'] = None; cp['app'] = app; st = 'link antigo'; manif.append(dict(canal=c['id'], chave=cp['arq'], app=app, id=blob))
                linhas.append((c['nome'], v['id'], cp['nome'], st, app, blob, os.path.getsize(dest) if os.path.exists(dest) else 0))
    # 2 · vídeos: só os ainda não postados e ≤ 20 MB, se o total couber
    cand = []
    for c in CANAIS:
        for v in c['itens']:
            if not v['video']: continue
            app, blob = v['video'].pop('fonte'); v['video']['app'] = app
            rel = f"{c['id']}/videos/{v['id']}.mp4"; dest = os.path.join(base, rel); loc = v['video'].pop('local', None)
            if loc:  # arquivo final no repositório (Shorts 31+): sempre vem para a Central, fora do limite de 300 MB
                if not os.path.exists(dest) or os.path.getsize(dest) != os.path.getsize(loc): os.makedirs(os.path.dirname(dest), exist_ok=True); shutil.copyfile(loc, dest)
                v['video']['url'] = '/painel/canais/' + rel; tot_vid += os.path.getsize(dest)
                linhas.append((c['nome'], v['id'], 'Vídeo', 'migrado', app, 'repositório', os.path.getsize(dest))); continue
            f = no_cache(blob)
            tam = os.path.getsize(dest) if os.path.exists(dest) else (os.path.getsize(f) if f else None)
            motivo, est = '', False
            if v['pre']: motivo = f"já {v['pre']}"
            elif tam is None:  # ainda não baixado: estima pelo tamanho típico do app (longo ~19 MB, short ~5 MB) para conferir o limite
                manif.append(dict(canal=c['id'], chave=v['id'] + '.mp4', app=app, id=blob)); tam, est = (19.5 if v['tipo'] == 'longo' else 5) * 2**20, True
            elif tam > LIMITE_VIDEO: motivo = f'{tam / 2**20:.1f} MB (passa de 20 MB)'
            cand.append((c, v, rel, dest, f, tam, motivo, app, blob, est))
    total = sum(x[5] for x in cand if not x[6])
    copiar = total <= LIMITE_TOTAL or '--videos' in sys.argv
    for c, v, rel, dest, f, tam, motivo, app, blob, est in cand:
        if not motivo and not copiar: motivo = f'aguardando OK (total ~{total / 2**20:.0f} MB passa de 300 MB)'
        elif not motivo and est and not os.path.exists(dest): motivo = 'não baixado'
        if not motivo and not os.path.exists(dest):
            os.makedirs(os.path.dirname(dest), exist_ok=True); shutil.copyfile(f, dest)
        if not motivo and os.path.exists(dest): v['video']['url'] = '/painel/canais/' + rel; st = 'migrado'; tot_vid += tam
        else: v['video']['url'] = None; st = 'link antigo' + (f' ({motivo})' if motivo else '')
        if 'aguardando' in motivo: pend.append((c['nome'], v['id'], tam, est))
        linhas.append((c['nome'], v['id'], 'Vídeo', st, app, blob, tam if st == 'migrado' else 0))
    return linhas, pend, total, tot_vid, manif


def escrever(linhas, pend, total, tot_vid):
    base = os.path.join(PRIV, 'painel', 'canais'); os.makedirs(base, exist_ok=True)
    dados = dict(atualizado=__import__('datetime').date.today().strftime('%d/%m/%Y'), apps=APPS,
                 canais=[{k: c[k] for k in ('id', 'nome', 'sub', 'itens', 'aprov', 'materiais', 'avisos')} for c in CANAIS])
    js = '// Gerado por conteudo/youtube/canais-central/montar-canais.py (repositório lindson). Não edite à mão.\nwindow.__CANAIS=' + \
         json.dumps(dados, ensure_ascii=False).replace('</', '<\\/') + ';\n'
    open(os.path.join(base, 'dados.js'), 'w', encoding='utf-8').write(js)
    html = open(os.path.join(AQUI, 'canais.html'), encoding='utf-8').read()
    mov = open(os.path.join(RAIZ, 'agencia', 'sistema-clientes', 'prototipo', 'movimento.js'), encoding='utf-8').read()
    html = html.replace('<!--MOVIMENTO-->', '<script>\n' + mov + '\n</script>', 1)
    open(os.path.join(PRIV, 'painel', 'canais.html'), 'w', encoding='utf-8').write(html)
    # tabela da migração
    n = lambda st, t=None: sum(1 for l in linhas if l[3].startswith(st) and (t is None or (l[2] == 'Vídeo') == (t == 'v')))
    md = ['# Migração dos apps dos canais dark para a Central (conta Leandro, 09/11/2026)', '',
          'Gerado por `montar-canais.py`. Página nova: https://lindsonalmeida.pages.dev/painel/canais (só o admin).', '',
          f'- Capas migradas: **{n("migrado", "c")}** · capas no link antigo: **{n("link antigo", "c")}**',
          f'- Vídeos migrados: **{n("migrado", "v")}** ({tot_vid / 2**20:.0f} MB) · vídeos no link antigo: **{n("link antigo", "v")}**',
          f'- Vídeos ainda não postados e ≤ 20 MB somam **{total / 2**20:.0f} MB** (limite combinado: 300 MB).', '']
    if pend:
        md += ['## Vídeos aguardando o OK do Lindson (passam do limite de 300 MB juntos)', '',
               'Ficam tocando no app antigo até ele decidir. Para trazer: `python3 montar-canais.py --cache <pasta> --videos`.', '',
               'Os Shorts 11 a 30 do Raposa também estão no repositório público em `raposa-e-leao/shorts/NN/video.mp4` (versão da agenda do YouTube Studio, ~4 MB cada).', '',
               '| Canal | Vídeo | Tamanho |', '|---|---|---|'] + [f'| {a} | {b} | {"~" if e else ""}{t / 2**20:.1f} MB{" (estimado)" if e else ""} |' for a, b, t, e in pend] + ['']
    md += ['## Cada arquivo', '', '| Canal | Item | Arquivo | Situação | App de origem | Asset | Tamanho na Central |', '|---|---|---|---|---|---|---|']
    md += [f'| {a} | {b} | {c} | {d} | {e.split("/")[-1]} | `{f}` | {(g / 1024):.0f} KB |' for a, b, c, d, e, f, g in linhas]
    # quais apps podem ser apagados
    md += ['', '## Apps antigos: podem ser apagados?', '', 'Nenhum app foi apagado. Apagar é irreversível e só com o OK do Lindson depois de conferir a Central.', '']
    for c in CANAIS:
        if c['id'] not in APPS: continue
        for app in ('antigo', 'novo'):
            url = APPS[c['id']][app]; sob = [l for l in linhas if l[4] == url and not l[3].startswith('migrado') and 'já ' not in l[3]]
            ja = [l for l in linhas if l[4] == url and 'já ' in l[3]]
            ok = 'pode apagar (tudo dele já está na Central' + (f'; {len(ja)} vídeos já postados ficam só no YouTube/Metricool' if ja else '') + ')' if not sob else f'**ainda não**: {len(sob)} arquivos só existem nele'
            md.append(f'- {c["nome"]} · app {app} {url}: {ok}')
    open(os.path.join(AQUI, 'MIGRACAO.md'), 'w', encoding='utf-8').write('\n'.join(md) + '\n')


if __name__ == '__main__':
    linhas, pend, total, tot_vid, manif = montar()
    if arg('--manifesto'):
        json.dump(manif, open(arg('--manifesto'), 'w'), ensure_ascii=False, indent=0); print(len(manif), 'assets a baixar')
        print('vídeos candidatos (não postados, ≤20 MB; os não baixados entram pela estimativa):', f'{total / 2**20:.0f} MB')
        sys.exit()
    escrever(linhas, pend, total, tot_vid)
    print('capas migradas:', sum(1 for l in linhas if l[2] != 'Vídeo' and l[3] == 'migrado'), '· vídeos migrados:', sum(1 for l in linhas if l[2] == 'Vídeo' and l[3] == 'migrado'),
          f'({tot_vid / 2**20:.0f} MB) · candidatos {total / 2**20:.0f} MB · pendentes {len(pend)}')
