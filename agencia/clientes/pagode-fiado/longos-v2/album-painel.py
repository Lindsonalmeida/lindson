# Álbum completo no painel: o site aceita até 25 MB por arquivo, então o vídeo (720p) vai em partes
# e a página junta tudo no navegador para assistir e baixar como um arquivo só.
# Uso: python3 album-painel.py <video_720p> <pasta_destino_no_privado>
import sys, os, math, json, html
src, dst = sys.argv[1], sys.argv[2]; os.makedirs(dst, exist_ok=True)
AQUI = os.path.dirname(os.path.abspath(__file__))
for f in os.listdir(dst):
    if f.startswith('album.p'): os.remove(os.path.join(dst, f))
TAM = 23 * 1024 * 1024; dados = open(src, 'rb').read(); n = math.ceil(len(dados) / TAM)
for i in range(n): open(f'{dst}/album.p{i:02d}', 'wb').write(dados[i * TAM:(i + 1) * TAM])
caps = open(AQUI + '/album-capitulos.txt').read().split('Capítulos:\n')[1].split('\n\n')[0].splitlines()
lis = ''.join(f'<li>{html.escape(c)}</li>' for c in caps)
pg = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Álbum Copo Americano</title>
<link href="https://fonts.googleapis.com/css2?family=Shrikhand&family=Caveat+Brush&family=Work+Sans:wght@500;700;800&display=swap" rel="stylesheet">
<style>:root{{--y:#F2B705;--v:#1E6B52;--p:#111;--c:#F3E9D2;--r:#C0392B}}*{{box-sizing:border-box;margin:0}}
body{{background:var(--p);color:var(--c);font-family:'Work Sans',sans-serif;padding:28px 16px 60px}}
main{{max-width:980px;margin:auto}}small{{font:800 13px 'Work Sans';letter-spacing:.3em;color:var(--y)}}
h1{{font:400 clamp(36px,7vw,64px)/1 Shrikhand;margin:10px 0 6px}}p{{color:#cfc6b4;line-height:1.5}}
video{{width:100%;aspect-ratio:16/9;background:#000;border-radius:14px;margin:22px 0 14px;display:block}}
.b{{display:inline-flex;gap:10px;align-items:center;background:var(--y);color:var(--p);font:800 16px 'Work Sans';padding:14px 24px;border-radius:99px;border:0;cursor:pointer;text-decoration:none}}
.b[aria-disabled=true]{{opacity:.5;pointer-events:none}}.bar{{height:8px;background:#2a2a2a;border-radius:9px;overflow:hidden;margin:14px 0}}.bar i{{display:block;height:100%;width:0;background:var(--y)}}
ol{{columns:2;gap:30px;margin-top:20px;padding-left:18px;color:#cfc6b4;font-size:15px;line-height:1.8}}@media(max-width:640px){{ol{{columns:1}}}}
.cad{{background:var(--c);color:var(--p);font:400 26px 'Caveat Brush';padding:6px 18px;display:inline-block;transform:rotate(-1.5deg);margin-top:18px}}</style></head>
<body><main><small>AO VIVO NO BAR DO SEU TIÃO</small><h1>Copo Americano · Álbum completo</h1>
<p>As 11 faixas aprovadas em sequência (~38 min), com capítulos na descrição do YouTube. Versão 720p do painel (o original 1080p sai do mesmo motor).</p>
<video id="v" controls playsinline></video><div class="bar"><i id="pr"></i></div>
<button class="b" id="ver">Carregar o álbum ({n} partes, {len(dados) / 1048576:.0f} MB)</button> <a class="b" id="dl" aria-disabled="true" download="pagode-fiado-album-copo-americano-ao-vivo-720p.mp4">Baixar (1 arquivo)</a>
<div class="cad">Pendura na conta.</div><ol>{lis}</ol></main>
<script>const N={n};document.getElementById('ver').onclick=async e=>{{e.target.disabled=true;const ps=[];
for(let i=0;i<N;i++){{const r=await fetch('album.p'+String(i).padStart(2,'0'));ps.push(await r.arrayBuffer());document.getElementById('pr').style.width=((i+1)/N*100)+'%'}}
const u=URL.createObjectURL(new Blob(ps,{{type:'video/mp4'}}));document.getElementById('v').src=u;const d=document.getElementById('dl');d.href=u;d.setAttribute('aria-disabled','false');e.target.textContent='Pronto'}}</script></body></html>'''
open(f'{dst}/album.html', 'w').write(pg); print(n, 'partes', round(len(dados) / 1048576), 'MB')
