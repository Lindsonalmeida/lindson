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
        vid = at.get(f'{k}.mp4')
        out.append(dict(id=k, tipo='longo', titulo=tit, legenda=leg, comentario=com, dur=dur(at, k), capas=capas,
                        video=dict(arq=f'raposa-e-leao-{k}.mp4', fonte=vid) if vid else None))
    return out


CANAIS = [
    dict(id='passaporte', nome='Passaporte da Bíblia', sub='Gravuras de Doré com narração. Shorts todo dia e um longo por semana (Metricool, marca 7990533).', itens=itens_passaporte()),
    dict(id='raposa', nome='Raposa e Leão', sub='Maquiavel e as leis do poder. Shorts de 2 em 2 h pelo YouTube Studio; longos de 16 a 20 min.', itens=itens_raposa()),
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
                app, blob = cp.pop('fonte'); rel = f"{c['id']}/capas/{cp['arq']}"; dest = os.path.join(base, rel)
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
            rel = f"{c['id']}/videos/{v['id']}.mp4"; dest = os.path.join(base, rel); f = no_cache(blob)
            tam = os.path.getsize(dest) if os.path.exists(dest) else (os.path.getsize(f) if f else None)
            motivo = ''
            if v['pre']: motivo = f"já {v['pre']}"
            elif tam is None: motivo = 'não baixado'; manif.append(dict(canal=c['id'], chave=v['id'] + '.mp4', app=app, id=blob))
            elif tam > LIMITE_VIDEO: motivo = f'{tam / 2**20:.1f} MB (passa de 20 MB)'
            cand.append((c, v, rel, dest, f, tam, motivo, app, blob))
    total = sum(t for _, _, _, _, _, t, m, _, _ in cand if not m)
    copiar = total <= LIMITE_TOTAL or '--videos' in sys.argv
    for c, v, rel, dest, f, tam, motivo, app, blob in cand:
        if not motivo and not copiar: motivo = f'aguardando OK (total {total / 2**20:.0f} MB passa de 300 MB)'
        if not motivo and not os.path.exists(dest):
            os.makedirs(os.path.dirname(dest), exist_ok=True); shutil.copyfile(f, dest)
        if not motivo and os.path.exists(dest): v['video']['url'] = '/painel/canais/' + rel; st = 'migrado'; tot_vid += tam
        else: v['video']['url'] = None; st = 'link antigo' + (f' ({motivo})' if motivo else '')
        if 'aguardando' in motivo: pend.append((c['nome'], v['id'], tam))
        linhas.append((c['nome'], v['id'], 'Vídeo', st, app, blob, tam or 0))
    return linhas, pend, total, tot_vid, manif


def escrever(linhas, pend, total, tot_vid):
    base = os.path.join(PRIV, 'painel', 'canais'); os.makedirs(base, exist_ok=True)
    dados = dict(atualizado=__import__('datetime').date.today().strftime('%d/%m/%Y'), apps=APPS,
                 canais=[{k: c[k] for k in ('id', 'nome', 'sub', 'itens')} for c in CANAIS])
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
               '| Canal | Vídeo | Tamanho |', '|---|---|---|'] + [f'| {a} | {b} | {t / 2**20:.1f} MB |' for a, b, t in pend] + ['']
    md += ['## Cada arquivo', '', '| Canal | Item | Arquivo | Situação | App de origem | Asset | Tamanho na Central |', '|---|---|---|---|---|---|---|']
    md += [f'| {a} | {b} | {c} | {d} | {e.split("/")[-1]} | `{f}` | {(g / 1024):.0f} KB |' for a, b, c, d, e, f, g in linhas]
    # quais apps podem ser apagados
    md += ['', '## Apps antigos: podem ser apagados?', '', 'Nenhum app foi apagado. Apagar é irreversível e só com o OK do Lindson depois de conferir a Central.', '']
    for c in CANAIS:
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
        print('vídeos candidatos (não postados, ≤20 MB, já baixados):', f'{total / 2**20:.0f} MB')
        sys.exit()
    escrever(linhas, pend, total, tot_vid)
    print('capas migradas:', sum(1 for l in linhas if l[2] != 'Vídeo' and l[3] == 'migrado'), '· vídeos migrados:', sum(1 for l in linhas if l[2] == 'Vídeo' and l[3] == 'migrado'),
          f'({tot_vid / 2**20:.0f} MB) · candidatos {total / 2**20:.0f} MB · pendentes {len(pend)}')
