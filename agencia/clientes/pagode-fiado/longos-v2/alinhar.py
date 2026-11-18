# Alinha a letra oficial (letras.json) com as palavras transcritas (<faixa>.words.json) e grava <faixa>.tempos.json
# com início/fim de cada linha cantada e de cada palavra (para o karaokê). Uso: python3 alinhar.py <pasta_audio> <faixas...>
import sys, json, os, re, unicodedata, difflib
AQUI = os.path.dirname(os.path.abspath(__file__)); L = json.load(open(AQUI + '/letras.json'))
def norm(s):
    s = unicodedata.normalize('NFD', s.lower()); s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    return re.sub(r'[^a-z0-9 ]', ' ', s).split()
def sim(a, b):
    if a == b: return 2.0
    r = difflib.SequenceMatcher(None, a, b).ratio()
    return 1.2 if r >= .75 else (.4 if r >= .6 else -1.0)
def alinha(k, P):
    linhas = L[k]['linhas']; ws = json.load(open(f'{P}/{k}.words.json'))
    O = [(i, j, w) for i, (_, _, t) in enumerate(linhas) for j, w in enumerate(norm(t))]
    A = []
    for s in ws:
        for (a, b, w, p) in s['w']:
            for x in norm(w): A.append((a, b, x))
    n, m = len(O), len(A); G_O, G_A = -.6, -.35
    S = [[0.0] * (m + 1) for _ in range(n + 1)]; T = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1): S[i][0] = S[i - 1][0] + G_O; T[i][0] = 1
    for j in range(1, m + 1): S[0][j] = 0.0; T[0][j] = 2      # palavras extras antes da letra (introdução): sem custo
    for i in range(1, n + 1):
        oi = O[i - 1][2]; Si, Sp = S[i], S[i - 1]; Ti = T[i]
        for j in range(1, m + 1):
            d = Sp[j - 1] + sim(oi, A[j - 1][2]); u = Sp[j] + G_O; l = Si[j - 1] + (G_A if i < n else 0.0)
            if d >= u and d >= l: Si[j] = d; Ti[j] = 0
            elif u >= l: Si[j] = u; Ti[j] = 1
            else: Si[j] = l; Ti[j] = 2
    i, j = n, m; par = {}
    while i > 0 and j > 0:
        t = T[i][j]
        if t == 0:
            if sim(O[i - 1][2], A[j - 1][2]) > 0: par[i - 1] = j - 1
            i -= 1; j -= 1
        elif t == 1: i -= 1
        else: j -= 1
    out = []; usados = set(par.values())
    for li, (parte, quem, txt) in enumerate(linhas):
        idx = [x for x in range(n) if O[x][0] == li]; ok = [x for x in idx if x in par]
        if not idx or len(ok) < max(1, .34 * len(idx)): continue
        t0 = A[par[ok[0]]][0]; t1 = A[par[ok[-1]]][1]
        out.append(dict(li=li, parte=parte, quem=quem, txt=txt, ini=t0, fim=t1, cob=round(len(ok) / len(idx), 2),
                        pal=[[O[x][1], A[par[x]][0], A[par[x]][1]] for x in ok]))
    # repetições cantadas a mais que a letra: trechos da transcrição sem par que lembram uma linha
    seg_livres = []
    for s in ws:
        idx = [x for x in range(len(A)) if s['s'] - .05 <= A[x][0] <= s['e'] + .05]
        if idx and not any(x in usados for x in idx) and s['e'] - s['s'] > .8: seg_livres.append(s)
    for s in seg_livres:
        tn = ' '.join(norm(s['t'])); best = (0, None, 1)
        for li in range(len(linhas)):
            for q in (1, 2):
                if li + q > len(linhas): continue
                alvo = ' '.join(' '.join(norm(linhas[x][2])) for x in range(li, li + q))
                r = difflib.SequenceMatcher(None, tn, alvo).ratio() - (.02 if q == 2 else 0)
                if r > best[0]: best = (r, li, q)
        if best[0] < .62: continue
        r, li, q = best; wsg = [(a, b) for (a, b, w, p) in s['w'] for _ in norm(w)] or [(s['s'], s['e'])]
        n1 = len(norm(linhas[li][2])); tot = sum(len(norm(linhas[x][2])) for x in range(li, li + q))
        cortes = [0, round(len(wsg) * n1 / tot) if q == 2 else len(wsg), len(wsg)]
        for z in range(q):
            ws_ = wsg[cortes[z]:cortes[z + 1]] or wsg[-1:]
            parte, quem, txt = linhas[li + z]
            out.append(dict(li=li + z, parte=parte, quem=quem, txt=txt, ini=ws_[0][0], fim=min(ws_[-1][1], ws_[0][0] + 6.5), cob=round(r, 2), pal=[], extra=True))
    out.sort(key=lambda x: x['ini'])
    # linhas que faltaram no meio de um bloco (ex.: 2ª linha do refrão mal transcrita): ocupam o intervalo entre as vizinhas
    extra = []
    for a, b in zip(out, out[1:]):
        falt = [li for li in range(a['li'] + 1, b['li']) if not a.get('extra') and not b.get('extra')]
        gap = b['ini'] - a['fim']
        if falt and len(falt) <= 3 and gap >= 1.2 * len(falt):
            passo = min(gap / len(falt), 3.4); base = b['ini'] - passo * len(falt)   # encosta na linha seguinte (o trecho que faltou vem logo antes)
            for q, li in enumerate(falt):
                parte, quem, txt = linhas[li]
                extra.append(dict(li=li, parte=parte, quem=quem, txt=txt, ini=round(base + q * passo + .05, 2), fim=round(base + (q + 1) * passo - .1, 2), cob=0, pal=[], extra=True))
    out += extra; out.sort(key=lambda x: x['ini'])
    # limpeza: linha longa demais (casou palavra solta lá na frente) e duplicatas encavaladas
    limpo = []
    for o in out:
        o['fim'] = min(o['fim'], o['ini'] + 1.2 + .62 * len(norm(o['txt'])))
        if limpo and o['ini'] < limpo[-1]['ini'] + .5:
            if o.get('extra'): continue
            if limpo[-1].get('extra'): limpo.pop()
        limpo.append(o)
    out = limpo
    for o in out: o['pal'] = [x for x in o['pal'] if x[1] <= o['fim'] + .3]
    # tempos por palavra (karaokê): as que não casaram são interpoladas pelo tamanho
    for o in out:
        pw = norm(o['txt']); tm = {p: (a, b) for p, a, b in o['pal']}
        tot = sum(len(w) for w in pw) or 1; acc = 0; res = []
        for p, w in enumerate(pw):
            if p in tm: a, b = tm[p]
            else:
                a = o['ini'] + (o['fim'] - o['ini']) * acc / tot; b = o['ini'] + (o['fim'] - o['ini']) * (acc + len(w)) / tot
            res.append([round(a, 2), round(b, 2)]); acc += len(w)
        for p in range(1, len(res)):
            if res[p][0] < res[p - 1][0]: res[p][0] = res[p - 1][0]
        o['pal'] = res
    json.dump(out, open(f'{P}/{k}.tempos.json', 'w'), ensure_ascii=False, indent=0)
    return out
if __name__ == '__main__':
    for k in sys.argv[2:]:
        o = alinha(k, sys.argv[1]); print(f'== {k} {L[k]["titulo"]}: {len(o)} linhas de {len(L[k]["linhas"])}')
        for x in o: print(f"  {x['ini']:6.1f}-{x['fim']:6.1f} {x['cob']:.2f}{' +' if x.get('extra') else '  '} [{x['quem']}] {x['txt']}")
