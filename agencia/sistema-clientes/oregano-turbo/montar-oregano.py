"""Painel da Orégano Turbo na Central (/painel/oregano). Reaproveita o painel que já existe
(../../operacao-propria/social/calendario/montar_painel.py, feito do modelo do sistema) e acrescenta na aba Aprovações
os 21 Reels da semana 1 (player, capa, título para Shorts/Reels, legenda com copiar, dia e hora, baixar vídeo e capa),
no primeiro lugar da fila. Vídeos comprimidos (H.264 CRF 28, AAC 128k) e capas ficam no PRIVADO em painel/oregano/reels/.
Uso: python3 montar-oregano.py [pasta do privado]. Conta Zuleide, 14/11/2026."""
import json, os, sys, shutil, subprocess
from PIL import Image
D = os.path.dirname(os.path.abspath(__file__))
OP = os.path.join(D, '..', '..', 'operacao-propria')
PRIV = sys.argv[1] if len(sys.argv) > 1 else os.path.join(D, '..', '..', '..', '..', 'centrallindsonalmeida')
subprocess.run([sys.executable, os.path.join(OP, 'social', 'calendario', 'montar_painel.py'), PRIV], check=True)
R = os.path.join(OP, 'reels'); OUT = os.path.join(PRIV, 'painel', 'oregano', 'reels'); os.makedirs(OUT, exist_ok=True)
rot = json.load(open(os.path.join(R, 'roteiros.json')))['reels']
DIAS = ['seg', 'ter', 'qua', 'qui', 'sex', 'sáb', 'dom']
import datetime
itens = []
for r in rot:
    n = r['id'][3:]; pasta = os.path.join(R, 'semana-1', n)
    v = os.path.join(OUT, f'OT-{n}.mp4')
    if not os.path.exists(v):
        subprocess.run(['ffmpeg', '-nostdin', '-y', '-v', 'error', '-i', os.path.join(pasta, f'OT-{n}.mp4'), '-c:v', 'libx264', '-preset', 'medium', '-crf', '28',
                        '-threads', '3', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '128k', '-movflags', '+faststart', v], check=True)
    assert os.path.getsize(v) < 25e6, v + ' passou de 25 MB'
    shutil.copy(os.path.join(pasta, 'capa.jpg'), os.path.join(OUT, f'OT-{n}-capa.jpg'))
    im = Image.open(os.path.join(pasta, 'capa.jpg')).convert('RGB'); im.thumbnail((540, 960)); im.save(os.path.join(OUT, f'OT-{n}-capa-p.jpg'), quality=80)
    dd, mm = r['post']['data'].split('/'); dia = DIAS[datetime.date(2026, int(mm), int(dd)).weekday()]
    tit = r['titulo'] if len(r['titulo']) <= 70 else r['titulo'][:67].rsplit(' ', 1)[0] + '…'
    itens.append({'t': 'Reels · ' + ('venda' if r['tipo'] == 'venda' else 'conteúdo'), 'titulo': f"{r['id']} · {tit}", 'curto': tit,
                  'data': f"Postar {dia} {r['post']['data']} às {r['post']['hora']}", 'linha': r['linha_editorial'], 'st': 'aprovado', 'por': 'Lindson (vídeos aprovados em 15/11)',
                  'img': f'/painel/oregano/reels/OT-{n}-capa-p.jpg', 'capa': f'/painel/oregano/reels/OT-{n}-capa.jpg', 'video': f'/painel/oregano/reels/OT-{n}.mp4',
                  'legenda': open(os.path.join(pasta, 'legenda-seo.txt') if os.path.exists(os.path.join(pasta, 'legenda-seo.txt')) else os.path.join(pasta, 'legenda.txt')).read().strip()})
p = os.path.join(PRIV, 'painel', 'oregano.html'); s = open(p).read()
i = s.index('const APROV=') + len('const APROV=') + 1
s = s[:i] + ','.join(json.dumps(x, ensure_ascii=False) for x in itens) + ',' + s[i:]
a = '<div class="post">${p.img?`<img src="${p.img}"'
assert a in s, 'o modelo mudou'
s = s.replace(a, '<div class="post">${p.video?`<video src="${p.video}" poster="${p.img}" controls playsinline preload="none" style="width:100%;aspect-ratio:9/16;object-fit:cover;display:block;background:#000"></video>'
              '<div style="display:flex;gap:8px;margin:10px 12px 0"><a class="btn lin" href="${p.video}" download style="flex:1;text-align:center">⬇ Vídeo</a><a class="btn lin" href="${p.capa}" download style="flex:1;text-align:center">⬇ Capa</a></div>'
              '<div style="margin:10px 12px 0;padding:10px 12px;border:1px solid var(--linha);border-radius:12px"><div style="font:600 10.5px var(--f-dado);letter-spacing:.14em;color:var(--apagado)">TÍTULO PARA SHORTS / REELS</div><div style="font-weight:700;margin:4px 0 8px">${p.curto}</div><button class="btn lin" onclick="navigator.clipboard.writeText(this.previousElementSibling.textContent);window.__toast&&window.__toast(\'Título copiado\')">Copiar título</button></div>`'
              ':p.img?`<img src="${p.img}"', 1)
s = s.replace('<summary style="cursor:pointer;color:var(--amarelo);font-weight:700">Ver legenda</summary>',
              '<summary style="cursor:pointer;color:var(--amarelo);font-weight:700">${p.video?\'Legenda completa\':\'Ver legenda\'}</summary>', 1)
s = s.replace('</style>', '@media(max-width:600px){.posts{grid-template-columns:1fr}}</style>', 1)
open(p, 'w').write(s)
# Tarefas feitas, Postados e Biblioteca (menu lateral, 20/11/2026) continuam no painel remontado
sys.path.insert(0, os.path.join(D, '..', 'site', 'painel-feitas')); import injetar; injetar.injetar(os.path.join(PRIV, 'painel'))
print(len(itens), 'Reels no painel ·', round(sum(os.path.getsize(os.path.join(OUT, f)) for f in os.listdir(OUT)) / 1e6), 'MB em painel/oregano/reels/')
