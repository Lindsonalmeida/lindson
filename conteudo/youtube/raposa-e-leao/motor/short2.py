"""Raposa e Leão — Short com voz humanizada e conversa com o ouvinte.
python3 short2.py <NN> [--so-voz]
Lê shorts/NN/palavras_v1.json + cenas_v1.json (versão original) e motor/conversa_shorts.py,
monta o texto novo (com as falas ao ouvinte), gera a voz humanizada, reancora as cenas
nas palavras novas e chama short.py (render)."""
import json, os, re, sys, unicodedata, subprocess, difflib
import numpy as np, soundfile as sf
sys.path.insert(0, '/home/user/lindson/conteudo/youtube/comum'); from voz_humana import narrar, S
import voz_humana  # sinal correto quando o valor arredonda para zero ("-0.4" virava "0%", que o serviço recusa)
voz_humana._pct = lambda v: f'{int(round(v)):+d}%'; voz_humana._hz = lambda v: f'{int(round(v)):+d}Hz'
D = os.path.dirname(os.path.abspath(__file__)); RAIZ = os.path.join(D, '..'); sys.path.insert(0, D)
from conversa_shorts import C
NN = sys.argv[1]; P = f'{RAIZ}/shorts/{NN}'; cfg = C[NN]
norm = lambda s: re.sub(r'[^\w]', '', unicodedata.normalize('NFC', s.lower()))

# 1) texto original com pontuação: palavras faladas + pontuação do roteiro (ROTEIROS-SHORTS.md)
old = json.load(open(P + '/palavras_v1.json')); ow = [w for w, _ in old]
md = open(RAIZ + '/ROTEIROS-SHORTS.md').read()
m = re.search(rf'### {NN} —.*?\*\*Narração:\*\* (.+?)\n', md, re.S); mdt = m.group(1).split() if m else []
sm = difflib.SequenceMatcher(None, [norm(x) for x in ow], [norm(x) for x in mdt], autojunk=False); pont = {}
for a, b, n in sm.get_matching_blocks():
    for k in range(n): pont[a + k] = mdt[b + k]
toks = []
for i, w in enumerate(ow):
    t = pont.get(i, w)
    if norm(t) != norm(w): t = w
    toks.append(t)
# trecho falado que não está no roteiro: ponto antes de palavra maiúscula (exceto nomes próprios)
NOMES = {'maquiavel', 'césar', 'bórgia', 'bruto', 'lúcio', 'júnio', 'roma', 'príncipe', 'raposa', 'leão', 'aníbal', 'cipião'}
for i in range(len(toks) - 1):
    if i not in pont and i + 1 not in pont and toks[i + 1][:1].isupper() and norm(toks[i + 1]) not in NOMES and not re.search(r'[.!?…:,]$', toks[i]): toks[i] += '.'
# frases (índices de palavra onde cada frase começa)
ini = [0]
for i, t in enumerate(toks[:-1]):
    if re.search(r'[.!?…]["”]?$', t): ini.append(i + 1)
if not re.search(r'[.!?…]["”]?$', toks[-1]): toks[-1] += '.'

def idx(ref, W):
    w, n = (ref.split('#') + ['1'])[:2]; n = int(n); k = 0
    for i, x in enumerate(W):
        if norm(x) == norm(w):
            k += 1
            if k == n: return i
    raise SystemExit(f'{NN}: palavra não encontrada: {ref}')

cen = json.load(open(P + '/cenas_v1.json')); cs = cen['cenas']
# 2) onde entra a fala do meio: antes da frase em que começa a cena k
blocos = []  # (texto, conversa?, cena de conversa ou None)
ref, tipo, fala, h, x = cfg['meio']   # ref: palavra (a conversa entra antes da frase que a contém)
cs0 = json.load(open(P + '/cenas_v1.json'))['cenas']
if isinstance(ref, int): ref = cs0[ref].get('w') or cs0[ref]['apos']   # número = antes da cena k
p0 = idx(ref, ow); corte = max(s for s in ini if s <= p0)
def inicio(c, j):
    if j == 0: return 0
    return idx(c['w'], ow) if 'w' in c else idx(c['apos'], ow) + 1
starts = [inicio(c, j) for j, c in enumerate(cs)]
k = max(j for j, st in enumerate(starts) if st < corte) + 1   # a conversa entra depois desta cena
def ancoras(c):
    out = [c[q] for q in ('meioW', 'de', 'bom', 'mau', 'fox', 'lion') if q in c] + [it[q] for it in c.get('items', []) for q in ('w', 'riscar') if q in it]
    return out + [c[q]['w'] for q in 'ab' if q in c and 'w' in c[q]]
continua = None
if starts[k - 1] < corte and (k >= len(cs) or starts[k] > corte) and any(idx(a, ow) >= corte for a in ancoras(cs[k - 1])):
    continua = json.loads(json.dumps(cs[k - 1])); continua['w'] = f'{ow[corte]}#{sum(1 for z in ow[:corte + 1] if norm(z) == norm(ow[corte]))}'; continua.pop('apos', None); cs.insert(k, continua)
blocos.append((' '.join(toks[:corte]), False, None))
blocos.append((fala, True, ('meio', tipo, h, x)))
blocos.append((' '.join(toks[corte:]), False, None))
ft, ffala, fh, fx = cfg['fim']; blocos.append((ffala, True, ('fim', ft, fh, fx)))
if '--seco' in sys.argv:
    for b in blocos: print(('  >> ' if b[1] else '     ') + b[0])
    sys.exit()

# 3) voz humanizada por bloco (falas ao ouvinte mais calorosas)
aud, W, t, marca = [], [], .25, {}
aud.append(np.zeros(int(.25 * S), np.float32))
for txt, conv, info in blocos:
    a, ws = narrar(txt, rate=7, pitch=-6, semente=f'rl-short-{NN}', conversa=conv)
    if info: marca[info[0]] = len(W)
    W += [[w, round(t + o, 3)] for w, o in ws]; aud.append(a); t += len(a) / S
    pa = .55 if conv else .4; aud.append(np.zeros(int(pa * S), np.float32)); t += pa
sf.write(P + '/voz.wav', np.concatenate(aud), S); json.dump(W, open(P + '/palavras.json', 'w'), ensure_ascii=False)
if '--so-voz' in sys.argv: print('voz', t); sys.exit()

# 4) reancora as cenas nas palavras novas
nw = [w for w, _ in W]
sm = difflib.SequenceMatcher(None, [norm(x) for x in ow], [norm(x) for x in nw], autojunk=False); mp = {}
for a, b, n in sm.get_matching_blocks():
    for q in range(n): mp[a + q] = b + q
def novo(ref):
    i = idx(ref, ow)
    j = mp.get(i)
    if j is None:  # palavra lida diferente (número, sigla): usa a vizinha mais próxima reconhecida
        prev = [a for a in mp if a < i]; j = mp[max(prev)] + (i - max(prev)) if prev else 0
    w = nw[j]; n = sum(1 for z in nw[:j + 1] if norm(z) == norm(w)); return f'{w}#{n}'
def rean(o, keys):
    for kk in keys:
        if kk in o:
            o[kk] = [novo(r) for r in o[kk]] if isinstance(o[kk], list) else novo(o[kk])
for c in cs:
    rean(c, ['w', 'apos', 'meioW', 'de', 'ate', 'hl', 'bom', 'mau', 'fox', 'lion'])
    for it in c.get('items', []): rean(it, ['w', 'riscar'])
    for kk in 'ab':
        if kk in c: rean(c[kk], ['w'])
# 5) cenas de conversa (retrato em movimento + componente) e fecho variado
IMG = sorted([f'../img/{f}' for f in os.listdir(RAIZ + '/img') if f.endswith('.jpg')] + [f'../img/hist/{f}' for f in os.listdir(RAIZ + '/img/hist')])
n0 = int(NN); im = [IMG[(n0 * 3) % len(IMG)], IMG[(n0 * 3 + 7) % len(IMG)]]
def conversa(qual, tipo, h, x, img):
    j = marca[qual]; w = nw[j]; n = sum(1 for z in nw[:j + 1] if norm(z) == norm(w))
    it = dict(tipo=tipo, txt={'comenta': 'RESPONDE NOS COMENTÁRIOS', 'segue': 'GOSTOU? ENTÃO…'}.get(tipo, x))
    if tipo == 'comenta': it['digita'] = x
    return dict(t='conversa', w=f'{w}#{n}', img=img, h=h, interage=it)
cs.insert(k, conversa('meio', tipo, h, x, im[0]))
ass = cs[-1]; assert ass['t'] == 'assinatura'
cs.insert(len(cs) - 1, conversa('fim', ft, fh, fx, im[1]))
est, frase = cfg['fecho']; lw = nw[-1]; ass['apos'] = f'{lw}#{sum(1 for z in nw if norm(z) == norm(lw))}'; ass['frase'] = frase
if est == 'seguir': ass['interage'] = dict(tipo='segue', txt='NÃO PERCA A PRÓXIMA')
if est == 'pergunta': ass['interage'] = dict(tipo='comenta', txt='DEIXA SUA RESPOSTA', digita='')
cen.update(cenas=cs, abre=cfg['abre'], pulso=cfg['pulso'], batida=cfg['batida'])
json.dump(cen, open(P + '/cenas.json', 'w'), ensure_ascii=False, indent=1)
subprocess.run([sys.executable, D + '/short.py', P], check=True)
