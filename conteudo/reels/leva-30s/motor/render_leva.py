"""Renderiza a leva inteira (ou só alguns ids) para conteudo/reels/leva-30s/render/ (motor v2, 08/11/2026).

  python3 render_leva.py                      # os 10, voz provisória  -> NN-slug-v1-voz-provisoria.mp4
  python3 render_leva.py --voz duble          # os 10, voz clonada do Lindson (precisa da ref.wav) -> NN-slug-v2.mp4
  python3 render_leva.py L30-03 L30-07        # só esses

Para cada Reels: vídeo, capa (cor do xadrez), folha de conferência com 6 quadros. No fim: previa-feed-reels.jpg.
"""
import argparse, json, os, re, shutil, subprocess, sys, unicodedata
from PIL import Image, ImageDraw, ImageFont

M = os.path.dirname(os.path.abspath(__file__)); LEVA = os.path.dirname(M); OUT = os.path.join(LEVA, 'render')
ap = argparse.ArgumentParser(); ap.add_argument('ids', nargs='*'); ap.add_argument('--voz', default='provisoria')
a = ap.parse_args()
rot = json.load(open(os.path.join(LEVA, 'roteiros.json')))['reels']
ids = a.ids or [r['id'] for r in rot]
os.makedirs(OUT + '/conferencia', exist_ok=True)
SUF = '-v1-voz-provisoria' if a.voz != 'duble' else '-v2'


SLUG = {'L30-01': 'pov-perfil-3-segundos', 'L30-02': 'bio-que-espanta', 'L30-03': 'ninguem-le-a-legenda', 'L30-04': 'cliente-sumiu',
        'L30-05': 'mito-do-site', 'L30-06': 'tier-list-posts', 'L30-07': 'link-do-whatsapp', 'L30-08': 'bastidor-semana',
        'L30-09': 'gancho-2-segundos', 'L30-10': 'desafio-7-dias'}


def slug(t):
    t = unicodedata.normalize('NFD', t.lower()); t = ''.join(c for c in t if unicodedata.category(c) != 'Mn')
    return '-'.join(re.sub(r'[^a-z0-9 ]', ' ', t).split()[:5])


for r in rot:
    if r['id'] not in ids: continue
    nome = f"{r['ordem']:02d}-{SLUG.get(r['id']) or slug(r['titulo'])}"; tmp = f'/tmp/reel2-out/{r["id"]}'
    shutil.rmtree(tmp, ignore_errors=True)
    subprocess.run([sys.executable, os.path.join(M, 'reel.py'), r['id'], '--voz', a.voz, '--saida', tmp, '--work', f'/tmp/reel2-work/{r["id"]}'], check=True)
    shutil.copy(f'{tmp}/{r["id"]}.mp4', f'{OUT}/{nome}{SUF}.mp4')
    shutil.copy(f'{tmp}/capa.jpg', f'{OUT}/{nome}-capa.jpg')
    shutil.copy(f'{tmp}/capa-4x5.jpg', f'{OUT}/conferencia/{nome}-capa-4x5.jpg')
    # folha de conferência: capa + 6 quadros
    qs = sorted(os.listdir(f'{tmp}/quadros')); ims = [Image.open(f'{tmp}/capa.jpg')] + [Image.open(f'{tmp}/quadros/{q}') for q in qs]
    cw, ch = 360, 640; fl = Image.new('RGB', (cw * len(ims), ch + 40), (20, 20, 20)); d = ImageDraw.Draw(fl)
    for i, (im, rot_) in enumerate(zip(ims, ['capa'] + [q.split('-', 1)[1][:-4] for q in qs])):
        fl.paste(im.resize((cw, ch)), (i * cw, 0)); d.text((i * cw + 8, ch + 12), rot_, fill=(245, 197, 24))
    fl.save(f'{OUT}/conferencia/{nome}-quadros.jpg', quality=85)
    print('OK', nome)

# prévia do feed (grade 3 colunas, ordem de postagem: o mais recente em cima à esquerda)
caps = sorted([f for f in os.listdir(OUT) if f.endswith('-capa.jpg')])
if caps:
    cw, ch = 360, 450; cols = 3; rows = (len(caps) + cols - 1) // cols
    g = Image.new('RGB', (cols * cw + (cols - 1) * 6, rows * ch + (rows - 1) * 6), (255, 255, 255))
    for i, f in enumerate(reversed(caps)):
        im = Image.open(os.path.join(OUT, f)).crop((0, 285, 1080, 1635)).resize((cw, ch))
        g.paste(im, ((i % cols) * (cw + 6), (i // cols) * (ch + 6)))
    g.save(os.path.join(OUT, 'previa-feed-reels.jpg'), quality=88)
    print('feed:', os.path.join(OUT, 'previa-feed-reels.jpg'))
