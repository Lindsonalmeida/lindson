"""Monta roteiros/<id>.json a partir das cenas escritas à mão em fonte/<id>.py (conta Zuleide, Peter, 09/11/2026).
Cada cena é uma tupla (gravura, txt, extras). O mov é escolhido aqui, com sequência própria de cada vídeo,
sem repetir o movimento da cena anterior (variação de template entre vídeos)."""
import json, os, zlib

MOVS = ['in', 'out', 'esq', 'dir', 'cima']


def monta(meta, cenas, ordem_mov):
    seq = [MOVS[i] for i in ordem_mov]
    out, ant = [], None
    for i, c in enumerate(cenas):
        g, txt = c[0], c[1]
        extra = c[2] if len(c) > 2 else {}
        mov = extra.pop('mov', None) or seq[i % len(seq)]
        if mov == ant:
            mov = seq[(i + 2) % len(seq)]
        ant = mov
        cena = {'gravura': g, 'mov': mov, 'txt': txt}
        cena.update(extra)
        if 'interage' in cena:
            cena['conv'] = True
        out.append(cena)
    d = dict(meta)
    d['cenas'] = out
    raiz = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
    arq = os.path.join(raiz, meta['id'] + '.json')
    json.dump(d, open(arq, 'w'), ensure_ascii=False, indent=1)
    pal = sum(len(c['txt'].split()) for c in out)
    gr = len({c['gravura'] for c in out})
    rep = [i for i in range(1, len(out)) if out[i]['gravura'] == out[i - 1]['gravura']]
    curtas = [(i, len(c['txt'].split())) for i, c in enumerate(out) if not 15 <= len(c['txt'].split()) <= 45]
    n = lambda k: sum(1 for c in out if k in c)
    print(meta['id'], len(out), 'cenas', pal, 'palavras', gr, 'gravuras', 'caps', n('cap'), 'versos', n('verso'),
          'interage', n('interage'), 'cta', n('cta'), '| rep', rep, '| fora 15-45', curtas,
          '| reticencias', sum(c['txt'].count('...') + c['txt'].count('…') for c in out))
    return d
