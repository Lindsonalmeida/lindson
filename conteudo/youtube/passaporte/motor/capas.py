"""Capas dos vídeos do Passaporte da Bíblia: Shorts 1080x1920 e longos A/B 1280x720.
python3 capas.py -> ../capas/<id>.png (longos: <id>-A.png e <id>-B.png)"""
import json, os, sys, re, glob, subprocess
D = os.path.dirname(os.path.abspath(__file__)); RAIZ = os.path.join(D, '..')
sys.path.insert(0, '/home/user/lindson/conteudo/produtos/passaporte'); from icones import icone
import base64, io
from PIL import Image
def pint(k):
    im = Image.open(f'{RAIZ}/pinturas/{k}.jpg').convert('RGB'); im.thumbnail((1600, 1600)); b = io.BytesIO(); im.save(b, 'JPEG', quality=82)
    return 'data:image/jpeg;base64,' + base64.b64encode(b.getvalue()).decode()
PK = sorted(os.path.basename(p)[:-4] for p in glob.glob(RAIZ + '/pinturas/*.jpg'))
CH = [('noe', 'No[ée]|arca'), ('moises', 'Lev|Mois|Lei'), ('davi', 'Davi|Salmo'), ('pedro', 'Marcos|Pedro'), ('apocalipse', 'Apocalipse'), ('pastor', 'Rute'),
      ('criacao', 'Bíblia inteira|6 paradas|mapa'), ('abraao', 'nomes|lista|genealog'), ('sermao', 'entend|começ'), ('emaus', 'atras|sono|culpa')]
def escolhe(txt, i):
    for k, rx in CH:
        if k in PK and re.search(rx, txt, re.I): return k
    return PK[i % len(PK)]
def destaca(txt, d):
    return txt.replace(d, f'<b>{d}</b>', 1) if d and d in txt else txt

CSS = '''<style>*{margin:0;box-sizing:border-box}body{background:#444;display:flex;flex-wrap:wrap;gap:30px;padding:30px}
.cp{position:relative;overflow:hidden;background:#1F2544}
.pt{position:absolute;inset:0;background-size:cover;background-position:center 25%;filter:saturate(1.15) contrast(1.05)}
.gr{position:absolute;inset:0}
.ic{position:absolute;border-radius:50%;background:#FFF7E8;display:grid;place-items:center;box-shadow:0 20px 50px rgba(0,0,0,.45);border:14px solid #fff}
.ic img{width:70%;height:70%}
.tx{position:absolute;font:800 var(--fs)/0.95 'Baloo 2';color:#fff;text-transform:uppercase;-webkit-text-stroke:var(--st) #1F2544;paint-order:stroke fill;text-shadow:0 10px 30px rgba(0,0,0,.5)}
.tx b{color:var(--c);font-weight:800}
.selo{position:absolute;border:8px dashed #D7263D;color:#D7263D;background:rgba(255,247,232,.92);border-radius:50%;display:grid;place-items:center;text-align:center;font:800 var(--ss) 'Baloo 2';transform:rotate(-10deg);line-height:1}
.marca{position:absolute;font:400 26px 'Special Elite';letter-spacing:.2em;color:#FFF7E8;background:#1F2544;padding:10px 18px;border-radius:8px}
</style>'''
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Baloo+2:wght@800&family=Special+Elite&display=swap" rel="stylesheet">'

def short(v, i):
    c = v['capa']; k = escolhe(v['titulo'] + c['texto'], i)
    return f'''<section class="cp" id="{v['id']}" style="width:1080px;height:1920px;--c:{c['cor'] if c['cor']!='#1F2544' else '#E9A23B'};--fs:150px;--st:16px;--ss:44px">
<div class="pt" style="background-image:url({pint(k)})"></div><div class="gr" style="background:linear-gradient(180deg,rgba(31,37,68,.55),rgba(31,37,68,.05) 35%,rgba(31,37,68,.85) 62%,#1F2544)"></div>
<div class="marca" style="left:50%;transform:translateX(-50%);top:120px">PASSAPORTE DA BÍBLIA</div>
<div class="ic" style="left:290px;top:420px;width:500px;height:500px">{f'<img src="{icone(c["icone"])}">' if c.get('icone') else ''}</div>
<div class="tx" style="left:60px;right:60px;top:1080px;text-align:center">{destaca(c['texto'], c.get('destaque'))}</div>
<div class="selo" style="right:70px;top:300px;width:230px;height:230px">EXPLI-<br>CADO</div></section>'''

def longo(v, i, lado):
    c = v['capa' + lado]; k = escolhe(v['titulo'] + c['texto'], i + (3 if lado == 'B' else 0)); cor = '#E9A23B'
    if lado == 'A':
        return f'''<section class="cp" id="{v['id']}-A" style="width:1280px;height:720px;--c:{cor};--fs:118px;--st:12px;--ss:30px">
<div class="pt" style="background-image:url({pint(k)});left:520px"></div><div class="gr" style="background:linear-gradient(90deg,#1F2544 38%,rgba(31,37,68,.2) 75%)"></div>
<div class="ic" style="right:60px;top:150px;width:420px;height:420px">{f'<img src="{icone(c["icone"])}">' if c.get('icone') else ''}</div>
<div class="tx" style="left:50px;top:90px;width:700px">{destaca(c['texto'], c.get('destaque'))}</div>
<div class="marca" style="left:50px;bottom:40px">PASSAPORTE DA BÍBLIA</div></section>'''
    return f'''<section class="cp" id="{v['id']}-B" style="width:1280px;height:720px;background:#D7263D;--c:#FFF7E8;--fs:124px;--st:12px;--ss:30px">
<div class="pt" style="background-image:url({pint(k)});opacity:.35;mix-blend-mode:multiply"></div>
<div class="tx" style="left:60px;right:380px;top:110px">{destaca(c['texto'], c.get('destaque'))}</div>
<div class="ic" style="right:60px;bottom:70px;width:320px;height:320px">{f'<img src="{icone(c["icone"])}">' if c.get('icone') else ''}</div>
<div class="selo" style="right:300px;top:40px;width:190px;height:190px;font-size:34px">ROTA<br>GRÁTIS</div>
<div class="marca" style="left:60px;bottom:40px">PASSAPORTE DA BÍBLIA</div></section>'''

sh = json.load(open(RAIZ + '/shorts.json')); lg = json.load(open(RAIZ + '/longos.json'))
partes = [short(v, i) for i, v in enumerate(sh)] + [longo(v, i, l) for i, v in enumerate(lg) for l in 'AB']
open(D + '/capas.html', 'w').write(f'<!doctype html><html><head><meta charset="utf-8">{FONTS}{CSS}</head><body>' + ''.join(partes) + '</body></html>')
ids = [v['id'] for v in sh] + [f"{v['id']}-{l}" for v in lg for l in 'AB']
os.makedirs(RAIZ + '/capas', exist_ok=True)
js = f"""const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage({{viewport:{{width:1200,height:2000}}}});
await p.goto('file://{D}/capas.html',{{waitUntil:'networkidle'}});await p.evaluate(()=>document.fonts.ready);
for(const id of {json.dumps(ids)})await (await p.$('#'+id)).screenshot({{path:'{RAIZ}/capas/'+id+'.png'}});await b.close()}})();"""
open(D + '/_capas.js', 'w').write(js); subprocess.run(['node', D + '/_capas.js'], check=True); print('ok', len(ids), 'capas')
