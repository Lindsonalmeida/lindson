# Capa do YouTube (1280x720) de um longo do Pagode Fiado, na composição "Capa de vídeo" do brand book.
# Uso: python3 capa.py <faixa> <pasta>  (usa <pasta>/tmp<faixa>/f00.jpg ou a foto indicada) -> <pasta>/ov<faixa>/capa.json para render.js
import json, sys, os, base64, html
K, W = sys.argv[1], sys.argv[2]; AQUI = os.path.dirname(os.path.abspath(__file__))
F = json.load(open(AQUI + '/faixas.json'))[K]
LOGO = open(AQUI + '/../../../processos/brand-book-premium/pagode-fiado/logo.svg').read(); LOGO = LOGO[LOGO.index('<svg'):]
foto = f"{W}/tmp{K}/f{F.get('capa_foto', 2):02d}.jpg"
b = 'data:image/jpeg;base64,' + base64.b64encode(open(foto, 'rb').read()).decode()
pal = F['titulo'].split(); a, z = ' '.join(pal[:-1]), pal[-1]
h = f"""<html><head><style>@import url('https://fonts.googleapis.com/css2?family=Shrikhand&family=Work+Sans:wght@800&family=Caveat+Brush&display=block');
*{{margin:0;box-sizing:border-box}}html,body{{width:1920px;height:1080px;overflow:hidden}}.logo svg{{width:100%;height:auto;display:block}}</style></head><body>
<div style="position:absolute;inset:0;background:url({b}) center/cover;filter:brightness(.9) saturate(1.1)"></div>
<div style="position:absolute;inset:0;background:linear-gradient(90deg,#111111f2 0,#111111d9 40%,#11111140 70%,transparent)"></div>
<div style="position:absolute;left:90px;top:96px;font:800 34px 'Work Sans';letter-spacing:.3em;color:#F2B705">FAIXA {K} · AO VIVO</div>
<div style="position:absolute;left:84px;top:170px;width:1150px;font:400 200px/0.92 Shrikhand;color:#F3E9D2;text-shadow:0 10px 30px #000">{html.escape(a)}<br><span style="color:#F2B705">{html.escape(z)}</span></div>
<div style="position:absolute;left:96px;bottom:110px;font:400 64px 'Caveat Brush';color:#F3E9D2;background:#C0392B;padding:4px 30px;transform:rotate(-2deg)">pendura na conta</div>
<div class="logo" style="position:absolute;right:70px;bottom:70px;width:300px;transform:rotate(4deg);box-shadow:0 20px 50px #000a;border-radius:20px;overflow:hidden">{LOGO}</div>
</body></html>"""
json.dump([dict(nome='capa', html=h)], open(f'{W}/ov{K}/capa/paginas.json', 'w') if os.makedirs(f'{W}/ov{K}/capa', exist_ok=True) is None else None)
print('ok')
