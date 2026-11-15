# Sobe OT-22..30 no painel Orégano (privado centrallindsonalmeida): vídeo comprimido, capas e itens "aguardando" em APROV e P.
# Edita só as listas por inserção (não roda montador). Conta Zuleide, 15/11/2026.
import json, os, subprocess, sys
H = os.path.dirname(os.path.abspath(__file__)); C = '/home/user/centrallindsonalmeida'; PR = os.path.join(C, 'painel/oregano/reels')
R = json.load(open(os.path.join(H, 'roteiros.json')))['reels'][21:]
DS = {'23/11': 'seg', '24/11': 'ter', '25/11': 'qua'}
ap, pp = [], []
for r in R:
    n = r['id'][3:]; d = os.path.join(H, 'semana-2', n); v = os.path.join(d, r['id'] + '.mp4')
    if not os.path.exists(v): print('falta', v); continue
    vo = os.path.join(PR, r['id'] + '.mp4')
    if not os.path.exists(vo):
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', v, '-c:v', 'libx264', '-crf', '27', '-preset', 'medium', '-maxrate', '2.4M', '-bufsize', '4M', '-c:a', 'aac', '-b:a', '128k', '-movflags', '+faststart', vo], check=True)
    subprocess.run(['cp', os.path.join(d, 'capa.jpg'), os.path.join(PR, r['id'] + '-capa.jpg')])
    subprocess.run(['convert', os.path.join(d, 'capa.jpg'), '-resize', '540x', '-quality', '80', os.path.join(PR, r['id'] + '-capa-p.jpg')])
    leg = open(os.path.join(d, 'legenda-seo.txt')).read()
    dur = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', vo], capture_output=True, text=True).stdout)
    tit = f"{r['id']} · {r['titulo']}"; dt, hr = r['post']['data'], r['post']['hora']
    ap.append({'t': 'Reels · ' + ('venda' if r['tipo'] == 'venda' else 'conteúdo'), 'titulo': tit, 'curto': r['titulo'], 'data': f"Postar {DS[dt]} {dt} às {hr}",
               'linha': r['linha_editorial'], 'st': 'aguardando', 'por': 'aguardando o Lindson (semana 2, conta Zuleide, 15/11)',
               'img': f"/painel/oregano/reels/{r['id']}-capa-p.jpg", 'capa': f"/painel/oregano/reels/{r['id']}-capa.jpg",
               'video': f"/painel/oregano/reels/{r['id']}.mp4", 'baixar': f"/painel/oregano/reels/{r['id']}.mp4", 'legenda': leg})
    pp.append({'id': r['id'].lower(), 'titulo': r['titulo'], 'legenda': leg, 'dur': f"0:{round(dur):02d}", 'agenda': f"{dt} às {hr.replace(':', 'h')}",
               'tema': r['linha_editorial'], 'capa': f"/painel/oregano/reels/{r['id']}-capa.jpg", 'video': f"/painel/oregano/reels/{r['id']}.mp4"})
f = os.path.join(C, 'painel/oregano.html'); L = open(f).read().split('\n')
# APROV (linha "const APROV=")
i = next(k for k, x in enumerate(L) if x.startswith('const APROV='))
A = json.loads(L[i][len('const APROV='):].rstrip().rstrip(';')); ids = {x['titulo'] for x in ap}
A = [x for x in A if x.get('titulo') not in ids]
pos = max(k for k, x in enumerate(A) if x.get('titulo', '').startswith('OT-21')) + 1
A[pos:pos] = ap; L[i] = 'const APROV=' + json.dumps(A, ensure_ascii=False) + ';'
# P (lista de posts com copiar/baixar)
j = next(k for k, x in enumerate(L) if 'const P=[{"id": "ot-01"' in x); s = L[j]; a = s.index('const P=') + 8
P, e = json.JSONDecoder().raw_decode(s[a:]); P = [x for x in P if x['id'] not in {y['id'] for y in pp}] + pp
L[j] = s[:a] + json.dumps(P, ensure_ascii=False) + s[a + e:]
open(f, 'w').write('\n'.join(L)); print('ok', len(ap))
