"""Marca o início de cada capítulo (cenas com "cap") de um vídeo já narrado, para a descrição do YouTube.
python3 tempos.py <id> [...] -> ../tempos.json (lê as durações das narrações em scratchpad/pv/<id>/vz)"""
import json, os, sys, soundfile as sf
D = os.path.dirname(os.path.abspath(__file__)); RAIZ = os.path.join(D, '..'); ARQ = RAIZ + '/tempos.json'
TMP = '/tmp/claude-0/-home-user/5acf6937-9ac6-56e0-bc29-78bef210dc8b/scratchpad'
def mmss(t): t = int(t); return f'{t // 60}:{t % 60:02d}'
def capitulos(spec, inis):
    caps = [['0:00', 'Abertura']]
    for c, ini in zip(spec['cenas'], inis):
        if c.get('cap'): caps.append([mmss(ini), c['cap']['txt']])
    return caps
def salva(vid, caps):
    d = json.load(open(ARQ)) if os.path.exists(ARQ) else {}
    d[vid] = caps; json.dump(d, open(ARQ, 'w'), ensure_ascii=False, indent=1)
if __name__ == '__main__':
    specs = {v['id']: v for v in json.load(open(RAIZ + '/pintura.json'))}
    for vid in sys.argv[1:]:
        s = specs[vid]; t = s['titulo_tela'].get('dur', 2.6); inis = []
        for i in range(len(s['cenas'])):
            inis.append(max(0, t - .5)); t += sf.info(f'{TMP}/pv/{vid}/vz/{i:03d}.wav').duration + .55
        salva(vid, capitulos(s, inis)); print(vid, capitulos(s, inis))
