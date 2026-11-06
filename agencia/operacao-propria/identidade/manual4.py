# Manual da marca Orégano Turbo v4 (impacto) em PDF 1080x1350 a partir de pecas-v4/. Paollo · conta Leandro, 06/11/2026.
# Base: manual3.py. Abre com a "ficha técnica" no jeito de apresentar case do Colletivo (foto sangrada, título, ficha, contexto).
# Uso: python3 gerar4.py && node render4.js && python3 manual4.py && node manual-pdf.js manual4.html oregano-turbo-manual-v4.pdf
import os, base64, io
from PIL import Image
D = os.path.dirname(os.path.abspath(__file__)); P = os.path.join(D, 'pecas-v4')
def b64(f, base=P):
    b = io.BytesIO(); Image.open(os.path.join(base, f)).convert('RGB').save(b, 'JPEG', quality=86); return 'data:image/jpeg;base64,' + base64.b64encode(b.getvalue()).decode()
pags = sorted(f for f in os.listdir(P) if f.endswith('.png') and 'avatar' not in f)
cred = []
for pasta in ('fotos-v3', 'fotos-v4'):
    cred += [l.split('|')[1:5] for l in open(os.path.join(D, pasta, 'CREDITOS.md')) if l.startswith('| ') and '.jpg' in l]
F = '<link href="https://fonts.googleapis.com/css2?family=Anton&family=Inter+Tight:wght@800&family=Inter:wght@400;600&family=IBM+Plex+Mono:wght@500&display=swap" rel="stylesheet">'
html = [f'<!doctype html><html><head><meta charset="utf-8">{F}<style>@page{{size:1080px 1350px;margin:0}}*{{margin:0;padding:0;box-sizing:border-box}}body{{background:#141311}}.p{{width:1080px;height:1350px;position:relative;page-break-after:always;overflow:hidden}}.p>img{{width:1080px;height:1350px;display:block}}'
        '.et{font:500 16px "IBM Plex Mono";letter-spacing:.16em;text-transform:uppercase}.lin{display:flex;justify-content:space-between;border-bottom:1px solid #3a3833;padding:12px 0;font:400 19px Inter}</style></head><body>']
html.append(f'<div class="p"><img src="{b64(pags[0])}"></div>')
# ficha técnica (Colletivo)
ficha = [('Projeto', 'Identidade visual v4 · impacto'), ('Cliente', 'Orégano Turbo (operação própria)'), ('Ano', '2026'), ('Setor', 'Marketing de vendas para pizzarias'),
         ('Território', 'São Luís · Maranhão'), ('Entregas', 'Logo, cores, letras, padrões, selos, foto, caixa, uniforme, copo, sacola, cartão, proposta, Instagram, posts')]
html.append('<div class="p" style="background:#1E5B3B;color:#F3EEE6;padding:80px">'
  f'<div style="position:absolute;inset:0 0 auto 0;height:520px;background:linear-gradient(180deg,rgba(20,19,17,.1),rgba(20,19,17,.85)),url({b64("queijo-puxando.jpg", os.path.join(D, "fotos-v4"))}) center/cover"></div>'
  '<div style="position:relative;margin-top:300px;font:400 150px/.86 Anton;text-transform:uppercase">Orégano<br>Turbo v4</div>'
  '<div style="position:relative;display:grid;grid-template-columns:1fr 1fr;gap:60px;margin-top:70px">'
  '<div><div class="et" style="color:#F2B33D">Ficha técnica</div><div style="margin-top:16px">' + ''.join(f'<div class="lin"><span style="opacity:.7">{a}</span><b style="text-align:right;max-width:300px">{b}</b></div>' for a, b in ficha) + '</div></div>'
  '<div><div class="et" style="color:#F2B33D">Uma pitada de contexto</div><div style="font:400 21px/1.55 Inter;margin-top:16px">A v3 (séria) foi aprovada. O Lindson pediu mais impacto, mais imagem, menos espaço vazio e cara de pizzaria. A v4 mantém nome, símbolo, letras e cores da v3 e soma comida recortada, Anton nas manchetes, tomate e açafrão, xadrez de cantina, padrão de ícones e selos redondos.</div></div></div></div>')
html += [f'<div class="p"><img src="{b64(f)}"></div>' for f in pags[1:]]
html.append('<div class="p" style="padding:80px;font-family:Inter;color:#F3EEE6;background:#141311"><div class="et" style="color:#7CC596">18 · Arquivos e créditos</div>'
  '<div style="font:400 90px/.9 Anton;text-transform:uppercase;margin-top:30px">Como usar</div>'
  '<div style="font:400 22px/1.6 Inter;margin-top:26px">• Foto de perfil: <b>v4-16-avatar.png</b> · símbolo em vetor: <b>marca-v3/simbolo-*.svg</b> (não mudou)<br>• Manchete: Anton, caixa alta, 1 a 4 palavras · título: Inter Tight 800 · texto: Inter · número: IBM Plex Mono<br>• Comida recortada: <b>recortes-v4/</b> (BiRefNet, <b>recortar4.py</b>)<br>• Nos posts de cliente entra SEMPRE a foto real da pizzaria do cliente.<br>• Números e conversas dos mockups são ilustrativos; nunca publicar como resultado.</div>'
  '<div style="font:400 44px Anton;text-transform:uppercase;margin-top:44px">Créditos das fotos (Wikimedia Commons)</div><div style="font:400 15px/1.5 Inter;margin-top:16px;columns:2;column-gap:40px">'
  + ''.join(f'<div style="margin-bottom:10px;break-inside:avoid"><b>{c[0].strip()}</b> · {c[1].strip()} · {c[2].strip()}<br><span style="color:#8A857C;font-size:12px;word-break:break-all">{c[3].strip()}</span></div>' for c in cred) + '</div><div style="position:absolute;left:0;right:0;bottom:0;height:120px;background:repeating-conic-gradient(#1E5B3B 0 25%,#F3EEE6 0 50%) 0 0/80px 80px"></div></div>')
html.append('</body></html>')
open(os.path.join(D, 'manual4.html'), 'w').write(''.join(html)); print('manual4.html', len(pags) + 2, 'páginas')
