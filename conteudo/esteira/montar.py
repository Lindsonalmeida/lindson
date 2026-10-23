# Monta os 300 roteiros do Teste 01 a partir do plano e das bases por formato.
import json, re, os, sys
plan = json.load(open('teste-01-reels.json'))
base = {}
for f in ['falado', 'nunca', 'mito']:
    base.update(json.load(open(f'teste-01-base-{f}.json')))
F = {x['id']: x for x in plan['formatos']}
G = plan['ganchos']
nicho = ['#empreendedorismo', '#pequenosnegocios', '#donodenegocio', '#negociolocal', '#marketingdigital', '#instagramparanegocios', '#empreendedorlocal', '#comerciolocal', '#marketingparaempresas', '#vendasnoinstagram']
local = ['#saoluis', '#saoluisma', '#slz', '#maranhao', '#saoluisdomaranhao']
order = ['falado', 'nunca', 'mito']
byf = {f: [c for c in plan['conteudos'] if c['f'] == f] for f in order}
lotes, errs = [], []
for g in range(10):
    rs = []
    for p in range(30):
        k = g * 30 + p; f = order[p % 3]; c = byf[f][p // 3]; b = base[c['id']]; h = b['hooks'][g]
        t = b['tags']
        tags = [t[g % 4], t[(g + 1) % 4], nicho[k % len(nicho)], local[(g + p) % len(local)]]
        leg = b['titulo'] + "\n\n" + b['corpo'] + "\n\n" + " ".join(tags)
        r = {"id": f"teste-01-k{k:03d}", "k": k, "f": f, "fn": F[f]['n'], "c": c['id'], "cn": c['n'], "g": G[g]['id'], "gn": G[g]['n'],
             "gancho": h[0], "tela": h[1], "fala": b['fala'], "cta": b['cta'], "legenda": leg, "grav": b['grav'], "seg": 30}
        w = len((r['gancho'] + ' ' + ' '.join(r['fala']) + ' ' + r['cta']).split())
        if not 66 <= w <= 92: errs.append((r['id'], c['id'], w))
        if len(h[1].split()) > 10: errs.append((r['id'], 'tela', h[1]))
        if len(leg) > 2200: errs.append((r['id'], 'legenda', len(leg)))
        rs.append(r)
    lotes.append({"lote": g + 1, "teste": "teste-01", "g": G[g]['id'], "gn": G[g]['n'], "roteiros": rs})
if errs:
    print(errs); sys.exit(1)
json.dump(lotes, open('teste-01-roteiros.json', 'w'), ensure_ascii=False, indent=1)
out = sys.argv[1] if len(sys.argv) > 1 else None
if out:
    os.makedirs(out, exist_ok=True)
    for L in lotes: json.dump(L, open(f"{out}/lote-{L['lote']:02d}.json", 'w'), ensure_ascii=False)
print("ok", sum(len(L['roteiros']) for L in lotes))
