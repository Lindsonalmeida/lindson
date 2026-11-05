# Manual da marca Orégano Turbo v3 (séria) em PDF 1080x1350 a partir de pecas-v3/. Conta Leandro, 05/11/2026.
# Uso: python3 gerar3.py && node render3.js && python3 manual3.py && node manual-pdf.js manual3.html oregano-turbo-manual-v3.pdf
import os, base64, io, re
from PIL import Image
D = os.path.dirname(os.path.abspath(__file__)); P = os.path.join(D, 'pecas-v3')
def b64(f):
    b = io.BytesIO(); Image.open(os.path.join(P, f)).convert('RGB').save(b, 'JPEG', quality=86); return 'data:image/jpeg;base64,' + base64.b64encode(b.getvalue()).decode()
pags = sorted(f for f in os.listdir(P) if f.endswith('.png') and 'avatar' not in f)
cred = [l.split('|')[1:5] for l in open(os.path.join(D, 'fotos-v3', 'CREDITOS.md')) if l.startswith('| ') and '.jpg' in l]
html = ['<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@800&family=Inter:wght@400;600&family=IBM+Plex+Mono:wght@500&display=swap" rel="stylesheet"><style>@page{size:1080px 1350px;margin:0}*{margin:0;padding:0;box-sizing:border-box}body{background:#FBF8F3}.p{width:1080px;height:1350px;position:relative;page-break-after:always;overflow:hidden}.p>img{width:1080px;height:1350px;display:block}</style></head><body>']
html += [f'<div class="p"><img src="{b64(f)}"></div>' for f in pags]
html.append('<div class="p" style="padding:80px;font-family:Inter;color:#141311"><div style="font:500 18px \'IBM Plex Mono\';letter-spacing:.16em;color:#8A857C">11 · ARQUIVOS E CRÉDITOS</div>'
  '<div style="font:800 64px/1 \'Inter Tight\';letter-spacing:-.04em;margin-top:30px">Como usar os arquivos</div>'
  '<div style="font:400 24px/1.6 Inter;margin-top:30px">• Foto de perfil: <b>v3-11-avatar.png</b><br>• Símbolo em vetor: <b>marca-v3/simbolo-*.svg</b><br>• Letra do nome: Inter Tight 800, espaçamento −4,5% (Google Fonts, livre)<br>• Números: IBM Plex Mono · Texto: Inter<br>• Nos posts de cliente entra SEMPRE a foto real da pizzaria do cliente.<br>• Números nos mockups são ilustrativos; nunca publicar como resultado.</div>'
  '<div style="font:800 40px \'Inter Tight\';letter-spacing:-.03em;margin-top:60px">Créditos das fotos (Wikimedia Commons)</div><div style="font:400 17px/1.55 Inter;margin-top:20px">'
  + ''.join(f'<div style="margin-bottom:10px"><b>{c[0].strip()}</b> · {c[1].strip()} · {c[2].strip()}<br><span style="color:#8A857C">{c[3].strip()}</span></div>' for c in cred) + '</div></div>')
html.append('</body></html>')
open(os.path.join(D, 'manual3.html'), 'w').write(''.join(html)); print('manual3.html', len(pags) + 1, 'páginas')
