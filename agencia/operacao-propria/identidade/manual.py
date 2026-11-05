# Manual da marca Orégano Turbo v2 em PDF (páginas 4:5, 1080x1350) a partir das peças renderizadas. Conta Leandro, 05/11/2026.
# Uso: python3 gerar2.py && node render2.js && python3 manual.py && node manual-pdf.js
import os, base64
D = os.path.dirname(os.path.abspath(__file__)); P = os.path.join(D, 'pecas-v2')
b64 = lambda f: 'data:image/png;base64,' + base64.b64encode(open(os.path.join(P, f), 'rb').read()).decode()
pags = ['v2-01-capa.png', 'v2-02-logo.png', 'v2-03-cores-letras.png', 'v2-04-personagem.png', 'v2-06-padroes.png', 'v2-05-aplicacoes.png', 'v2-post-exemplo.png']
html = ['<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght,SOFT,WONK@9..144,900,100,1&family=DM+Sans:wght@400;500;700&display=swap" rel="stylesheet"><style>@page{size:1080px 1350px;margin:0}*{margin:0;padding:0;box-sizing:border-box}body{background:#F4EBD9}.p{width:1080px;height:1350px;position:relative;page-break-after:always;overflow:hidden}.p>img{width:1080px;height:1350px;display:block}.rot{font:700 18px "DM Sans";letter-spacing:.28em;text-transform:uppercase;color:#13452B}</style></head><body>']
html += [f'<div class="p"><img src="{b64(f)}"></div>' for f in pags]
dest = sorted(f for f in os.listdir(P) if f.startswith('v2-destaque-'))
html.append('<div class="p" style="padding:80px"><div class="rot">Instagram · foto de perfil e capas de destaque</div>'
            f'<div style="display:flex;gap:40px;align-items:center;margin-top:50px"><img src="{b64("v2-avatar.png")}" style="width:300px;height:300px;border-radius:50%">'
            '<div style="font:400 26px/1.5 \'DM Sans\';color:#0F1F17"><b>@oreganoturbo</b><br>Orégano Turbo | Mkt Pizzarias<br>O toque final que acelera a sua pizzaria 🌿🏁<br>Pedido direto no WhatsApp, todo dia da semana</div></div>'
            '<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:28px;margin-top:60px">' +
            ''.join(f'<div style="text-align:center"><img src="{b64(f)}" style="width:200px;height:200px;border-radius:50%;object-fit:cover;border:5px solid #fff;box-shadow:0 10px 24px rgba(0,0,0,.18)"><div style="font:500 20px \'DM Sans\';margin-top:10px;color:#0F1F17">{f[13:-4].replace("-", " ").split(" ", 1)[1]}</div></div>' for f in dest) +
            '</div><div style="position:absolute;left:80px;bottom:80px;width:920px;font:400 21px/1.5 \'DM Sans\';color:#0F1F17">Arquivos para subir: <b>v2-avatar.png</b> (foto de perfil) e <b>v2-destaque-*.png</b> (1080x1920, capas de destaque). Vetores para gráfica, com texto em curvas: pasta <b>marca-v2/</b>.</div></div>')
html.append('</body></html>')
open(os.path.join(D, 'manual.html'), 'w').write(''.join(html)); print('manual.html', len(pags) + 1, 'páginas')
