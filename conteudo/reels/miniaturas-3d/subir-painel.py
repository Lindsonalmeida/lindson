"""Sobe os Reels miniaturas 3D para a aba Artes do admin da Central (regra 15/11 "tudo no painel"), como stories-sites/subir-painel.py.
Vídeo comprimido até ~10 MB e capa em painel/admin-rede/reels-3d/ (privado); item em agencia/marca-lindson/artes-aprovadas.json com a legenda do ROTEIROS.md.
Uso: python3 subir-painel.py  (depois: montar-site.py). Conta Leandro, 15/11/2026."""
import json, os, re, subprocess, shutil
D = os.path.dirname(os.path.abspath(__file__)); ML = os.path.join(D, '..', '..', '..', 'agencia', 'marca-lindson')
PRIV = os.environ.get('PRIV', '/home/user/centrallindsonalmeida'); OUT = os.path.join(PRIV, 'painel', 'admin-rede', 'reels-3d'); os.makedirs(OUT, exist_ok=True)
R = json.load(open(os.path.join(D, 'roteiros.json'))); md = open(os.path.join(D, 'ROTEIROS.md')).read(); itens = []
for r in R:
    src = os.path.join(PRIV, 'dados', 'agencia', 'reels-3d', r['id'] + '.mp4')
    if not os.path.exists(src): continue
    dst = os.path.join(OUT, r['id'] + '.mp4'); d = float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', src]))
    kb = int(9.3 * 8192 / d) - 160
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', src, '-c:v', 'libx264', '-b:v', f'{kb}k', '-maxrate', f'{kb}k', '-bufsize', f'{2*kb}k', '-c:a', 'aac', '-b:a', '128k', '-movflags', '+faststart', dst], check=True)
    shutil.copy(os.path.join(D, 'capas', r['id'] + '.jpg'), os.path.join(OUT, r['id'] + '.jpg'))
    m = re.search(r'## ' + r['id'] + r' ·.*?\*\*Legenda[^*]*\*\*\s*(.*?)(?=\n---|\Z)', md, re.S)
    leg = (m.group(1).strip().replace('**', '') if m else r['titulo']) + '\n\n(Reels miniaturas 3D, voz 6 do Lindson, conta Leandro, 15/11/2026)'
    itens.append({'data': 'reels', 'titulo': f"Reels 3D {r['id']} · {r['titulo']}", 'img': f"/painel/admin-rede/reels-3d/{r['id']}.jpg", 'arquivo': r['id'] + '.jpg',
                  'telas': [f"/painel/admin-rede/reels-3d/{r['id']}.mp4"], 'legenda': leg})
arq = os.path.join(ML, 'artes-aprovadas.json'); L = json.load(open(arq)); T = {i['titulo'] for i in itens}
L = [a for a in L if a.get('titulo') not in T and not str(a.get('titulo', '')).startswith('Reels 3D ')] + itens
json.dump(L, open(arq, 'w'), ensure_ascii=False, indent=1); print(len(itens), 'Reels 3D na aba Artes')
