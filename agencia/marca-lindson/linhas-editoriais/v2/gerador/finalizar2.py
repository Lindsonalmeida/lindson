# Prévia da grade, LEGENDAS.md e painel.json (aba Artes do admin) das linhas editoriais v2 (conta Leandro, 16/11/2026)
import os, sys, json
from PIL import Image, ImageDraw, ImageFont
B = os.path.dirname(os.path.abspath(__file__)); V = os.path.dirname(B); sys.path.insert(0, B)
from conteudo import POSTS
from gerar2 import ORD2 as ORDEM
PRIV = '/home/user/centrallindsonalmeida/painel/admin-rede'
# prévia 3 colunas na ordem de postagem (mais novo no topo, como no Instagram), com a tag da linha
W, H = 360, 450; rows = (len(ORDEM) + 2) // 3
G = Image.new('RGB', (3 * W + 4, rows * (H + 2)), (255, 255, 255)); d = ImageDraw.Draw(G)
try: f = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 15)
except Exception: f = ImageFont.load_default()
for i, pid in enumerate(reversed(ORDEM)):
    P = POSTS[pid]; im = Image.open(os.path.join(V, P['linha'], P['nn'], 'v2-01.jpg')).convert('RGB').resize((W, H))
    x, y = (i % 3) * (W + 2), (i // 3) * (H + 2); G.paste(im, (x, y))
    lab = f"{len(ORDEM)-i:02d} · {P['tag']} · {P['fmt']}"; d.rectangle([x, y + H - 26, x + W, y + H], fill=(0, 0, 0)); d.text((x + 8, y + H - 22), lab, fill=(245, 197, 24), font=f)
G.save(os.path.join(V, 'previa-grade-v2.jpg'), quality=86)
# legendas
md = ['# Legendas · linhas editoriais v2 da marca Lindson (conta Leandro, 16/11/2026)', '', 'Estilo blog SEO. Imagens com foto do Lindson: aviso "imagem gerada por IA" na arte e na legenda.', '']
painel = []
os.makedirs(PRIV, exist_ok=True)
for k, pid in enumerate(ORDEM):
    P = POSTS[pid]; L = P['legenda']; ia = any(s.get('foto') for s in P['telas'])
    t = [f"# {L['titulo']}", '', L['intro'], '']
    for h, b in L['secoes']: t += [f'## {h}', b, '']
    t += [L['conclusao'], '', '👉 ' + L['cta'], '']
    if ia: t += ['(Imagem gerada por IA.)', '']
    t += [' '.join(L['tags'])]
    leg = '\n'.join(t); assert len(leg) <= 2200, pid
    md += [f"## {k+1:02d} · {pid} · {P['tag']} · {P['fmt']} · {P['titulo']}", f"Pasta: `{P['linha']}/{P['nn']}/` · palavra-chave: {L['kw']} · {len(leg)} caracteres", '', '```', leg, '```', '', '---', '']
    telas = []
    for j in range(len(P['telas'])):
        n = f"le2-{pid}-{j+1:02d}"
        Image.open(os.path.join(V, P['linha'], P['nn'], f'v2-{j+1:02d}.jpg')).convert('RGB').save(os.path.join(PRIV, n + '.jpg'), quality=86, optimize=True, progressive=True)
        telas.append('/painel/admin-rede/' + n + '.jpg')
    painel.append({'data': '16/11', 'titulo': f"{P['tag']} {P['nn']} · {P['fmt']} · {P['titulo']}", 'img': telas[0], 'arquivo': os.path.basename(telas[0]),
                   'telas': telas, 'legenda': leg, 'situacao': 'aguardando', 'tag': P['tag']})
open(os.path.join(V, 'LEGENDAS-v2.md'), 'w').write('\n'.join(md))
json.dump(painel, open(os.path.join(V, 'painel-v2.json'), 'w'), ensure_ascii=False, indent=1)
print('ok', len(painel))
