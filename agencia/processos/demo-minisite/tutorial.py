"""Vídeo tutorial narrado (tela de iPhone + voz + legendas): python3 tutorial.py <tutorial.json> <saida.mp4>
O JSON tem url, endereco, cor_legenda, voz e passos [{legenda, fala, acoes}]. Cada passo dura pelo menos o tempo da fala.
Usa a voz humanizada dos canais (conteudo/youtube/comum/voz_humana.py) e o gravador (gravar.js + montar.py). Conta Lindson, 01/11/2026."""
import json, os, sys, subprocess
import soundfile as sf
D = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(D, '..', '..', '..', 'conteudo', 'youtube', 'comum'))
import voz_humana as vz
T = json.load(open(sys.argv[1])); saida = sys.argv[2]
# códigos de acesso: nunca no roteiro (repositório público). {CODIGO:jaci} é trocado pelo código do arquivo privado.
_PRIV = os.path.join(D, '..', '..', 'sistema-clientes', 'privado', 'codigos-acesso.json')
def _codigo(cli):
    c = json.load(open(_PRIV)).get('codigos', {})
    v = c.get(cli) or next((x for k, x in c.items() if cli in k.lower()), '')
    return (v if isinstance(v, str) else (v.get('codigo', '') if isinstance(v, dict) else '')).replace('-', '')
for _p in T['passos']:
    for _a in _p.get('acoes', []):
        if isinstance(_a.get('texto'), str) and _a['texto'].startswith('{CODIGO:'): _a['texto'] = _codigo(_a['texto'][8:-1])
TMP = os.environ.get('DEMO_TMP', '/tmp/demo-minisite') + '/tut-' + os.path.basename(sys.argv[1])[:-5]; os.makedirs(TMP, exist_ok=True)
acoes, falas = list(T.get('inicio', [])), []
for i, p in enumerate(T['passos']):
    a, _ = vz.narrar(p['fala'], T.get('voz', 'pt-BR-AntonioNeural'), 0, 0, i, conversa=True)
    try: a = vz.estudio(a)
    except Exception: pass
    w = f'{TMP}/fala{i}.wav'; sf.write(w, a, 44100); falas.append(w); dur = len(a) / 44100
    acoes += [{'legenda': p['legenda']}] + p.get('acoes', []) + [{'ate': round(dur + 0.6, 2)}]
    print(f'passo {i}: {dur:.1f} s')
rot = {k: T[k] for k in ['url', 'endereco', 'cor_legenda', 'antes'] if k in T}; rot['acoes'] = acoes; rot['falas'] = falas
rp = f'{TMP}/{os.path.basename(sys.argv[1])}'; json.dump(rot, open(rp, 'w'), ensure_ascii=False)
subprocess.run(['python3', os.path.join(D, 'montar.py'), rp, saida], check=True)
