# Página do álbum completo no painel: toca as 11 faixas v2 em sequência (sem duplicar arquivos), com capítulos.
# O arquivo único 1080p (~2,3 GB) não cabe no site nem no Drive cheio: sai do montar-album.py quando houver onde guardar.
# Uso: python3 album-painel.py <pasta_destino_no_privado>
import sys, os, json, html
dst = sys.argv[1]; AQUI = os.path.dirname(os.path.abspath(__file__)); L = json.load(open(AQUI + '/letras.json'))
ks = sorted(L); caps = open(AQUI + '/album-capitulos.txt').read().split('Capítulos:\n')[1].split('\n\n')[0].splitlines()
lis = ''.join(f'<li data-i="{i}">{html.escape(c)}</li>' for i, c in enumerate(caps))
fx = json.dumps([f'pagode-fiado-{k}-v2.mp4' for k in ks])
pg = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Álbum Copo Americano</title>
<link href="https://fonts.googleapis.com/css2?family=Shrikhand&family=Caveat+Brush&family=Work+Sans:wght@500;700;800&display=swap" rel="stylesheet">
<style>:root{{--y:#F2B705;--p:#111;--c:#F3E9D2}}*{{box-sizing:border-box;margin:0}}
body{{background:var(--p);color:var(--c);font-family:'Work Sans',sans-serif;padding:28px 16px 60px}}main{{max-width:980px;margin:auto}}
small{{font:800 13px 'Work Sans';letter-spacing:.3em;color:var(--y)}}h1{{font:400 clamp(34px,7vw,62px)/1 Shrikhand;margin:10px 0 8px}}p{{color:#cfc6b4;line-height:1.5}}
video{{width:100%;aspect-ratio:16/9;background:#000;border-radius:14px;margin:22px 0 10px;display:block}}
ol{{list-style:none;padding:0;margin-top:16px;display:grid;grid-template-columns:1fr 1fr;gap:6px 24px}}@media(max-width:640px){{ol{{grid-template-columns:1fr}}}}
li{{cursor:pointer;padding:8px 12px;border-radius:8px;color:#cfc6b4}}li:hover{{background:#1d1d1d}}li.on{{background:var(--y);color:var(--p);font-weight:700}}
.cad{{background:var(--c);color:var(--p);font:400 26px 'Caveat Brush';padding:6px 18px;display:inline-block;transform:rotate(-1.5deg);margin-top:18px}}</style></head>
<body><main><small>AO VIVO NO BAR DO SEU TIÃO</small><h1>Copo Americano · Álbum completo</h1>
<p>As 11 faixas aprovadas em sequência (~38 min). Toque numa faixa para pular. Para o YouTube, o arquivo único em 1080p é montado sem perda pelo montar-album.py.</p>
<video id="v" controls playsinline preload="metadata"></video><ol id="l">{lis}</ol><div class="cad">Pendura na conta.</div></main>
<script>const F={fx};let i=0;const v=document.getElementById('v'),ls=[...document.querySelectorAll('li')];
function toca(n,auto){{i=n;v.src=F[i];ls.forEach((x,j)=>x.classList.toggle('on',j==i));if(auto)v.play()}}
v.addEventListener('ended',()=>{{if(i+1<F.length)toca(i+1,true)}});ls.forEach((x,j)=>x.onclick=()=>toca(j,true));toca(0,false)</script></body></html>'''
open(f'{dst}/album.html', 'w').write(pg); print('ok')
