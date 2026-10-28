"""Capas no estilo Pintura Viva: gravura de Doré em tom de vela, título grande e selo do Passaporte.
python3 capas_pv.py -> ../capas/pv/<id>.jpg (Shorts 1080x1920) e <id>-A.jpg / <id>-B.jpg (longos 1280x720)"""
import json, os, re, base64, subprocess, sys
D = os.path.dirname(os.path.abspath(__file__)); RAIZ = os.path.join(D, '..'); OUT = RAIZ + '/capas/pv'; os.makedirs(OUT, exist_ok=True)
sys.path.insert(0, '/home/user/lindson/conteudo/produtos/passaporte'); from icones import icone
uri = lambda f: 'data:image/jpeg;base64,' + base64.b64encode(open(f, 'rb').read()).decode()
GRAV = {'pv-01': '091', 'short-01': '053', 'short-02': '064', 'short-03': '018', 'short-04': '092', 'short-05': '083', 'short-06': '028', 'short-07': '068',
        'short-08': '093', 'short-09': '013', 'short-10': '099', 'longo-01-A': '020', 'longo-01-B': '053', 'longo-02-A': '092', 'longo-02-B': '001'}
sh = {v['id']: v for v in json.load(open(RAIZ + '/shorts.json'))}; lg = {v['id']: v for v in json.load(open(RAIZ + '/longos.json'))}
CAPAS = [('pv-01', 'short', {'texto': 'A semana que mudou o mundo', 'destaque': 'mudou', 'icone': 'assets/Latin cross/Flat/latin_cross_flat.svg'})]
CAPAS += [(k, 'short', v['capa']) for k, v in sh.items()]
for k, v in lg.items(): CAPAS += [(k + '-A', 'A', v['capaA']), (k + '-B', 'B', v['capaB'])]

def titulo(c):
    t = c['texto']; d = c.get('destaque', '')
    return t.replace(d, f'<em>{d}</em>', 1) if d else t
CSS = '''<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700;900&family=Manrope:wght@800&family=Special+Elite&display=swap" rel="stylesheet"><style>
*{margin:0;box-sizing:border-box}body{background:#0A0C14;overflow:hidden}
.c{position:relative;overflow:hidden;background:#0A0C14}
.g{position:absolute;background-size:cover;filter:grayscale(1) sepia(.85) contrast(1.35) brightness(.88) saturate(1.3)}
.vin{position:absolute;inset:0;background:radial-gradient(ellipse at 50% 40%,rgba(0,0,0,0) 35%,rgba(5,6,12,.85) 100%)}
.luz{position:absolute;inset:0;background:radial-gradient(circle at 70% 25%,rgba(255,200,120,.28),rgba(0,0,0,0) 45%);mix-blend-mode:screen}
h1{font-family:Manrope;font-weight:800;text-transform:uppercase;color:#EFE6D2;line-height:.98;letter-spacing:-.01em;text-shadow:0 6px 30px #000,0 0 4px #000}
h1 em{font-style:normal;color:#F2D58A}
.mk{font:400 22px 'Special Elite';letter-spacing:.3em;color:rgba(239,230,210,.75)}
.selo{position:absolute;border-radius:50%;background:#EFE6D2;border:8px dashed #D7263D;display:grid;place-items:center;transform:rotate(-10deg);box-shadow:0 10px 30px rgba(0,0,0,.6)}
.selo img{width:68%}
.fio{height:4px;background:#C9A227;border-radius:4px}
</style>'''
def html(kind, c, grav):
    img = uri(f'{RAIZ}/dore/{grav}.jpg'); ic = icone(c['icone']) if c.get('icone') else ''
    if kind == 'short':
        return f'''<div class="c" style="width:1080px;height:1920px"><div class="g" style="inset:-40px;background-image:url({img});background-position:50% 35%"></div><div class="luz"></div><div class="vin"></div>
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(10,12,20,.55),rgba(10,12,20,0) 18%,rgba(10,12,20,0) 45%,rgba(10,12,20,.92) 80%)"></div>
<div class="mk" style="position:absolute;top:80px;width:100%;text-align:center">PASSAPORTE DA BÍBLIA</div>
<div class="selo" style="width:260px;height:260px;right:70px;top:820px">{f'<img src="{ic}">' if ic else ''}</div>
<div style="position:absolute;left:70px;right:70px;bottom:250px"><div class="fio" style="width:140px;margin-bottom:34px"></div><h1 style="font-size:132px">{titulo(c)}</h1></div></div>'''
    if kind == 'A':
        return f'''<div class="c" style="width:1280px;height:720px"><div class="g" style="left:430px;right:-20px;top:-20px;bottom:-20px;background-image:url({img});background-position:50% 30%"></div><div class="luz"></div>
<div style="position:absolute;inset:0;background:linear-gradient(90deg,#0A0C14 30%,rgba(10,12,20,.75) 46%,rgba(10,12,20,0) 70%)"></div><div class="vin" style="opacity:.6"></div>
<div class="mk" style="position:absolute;left:64px;top:56px;font-size:19px">PASSAPORTE DA BÍBLIA</div>
<div style="position:absolute;left:64px;top:150px;width:690px"><h1 style="font-size:104px">{titulo(c)}</h1><div class="fio" style="width:130px;margin-top:30px"></div></div>
<div class="selo" style="width:230px;height:230px;right:70px;bottom:60px">{f'<img src="{ic}">' if ic else ''}</div></div>'''
    return f'''<div class="c" style="width:1280px;height:720px"><div class="g" style="inset:-20px;background-image:url({img});background-position:50% 40%"></div><div class="luz"></div><div class="vin"></div>
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(10,12,20,.15),rgba(10,12,20,.88) 70%)"></div>
<div class="selo" style="width:210px;height:210px;left:64px;top:60px">{f'<img src="{ic}">' if ic else ''}</div>
<div class="mk" style="position:absolute;right:64px;top:64px;font-size:19px">PASSAPORTE DA BÍBLIA</div>
<div style="position:absolute;left:64px;right:64px;bottom:70px"><h1 style="font-size:108px">{titulo(c)}</h1></div></div>'''

pages = []
for k, kind, c in CAPAS:
    st = f'/tmp/claude-0/-home-user/5acf6937-9ac6-56e0-bc29-78bef210dc8b/scratchpad/capa_{k}.html'
    open(st, 'w').write('<!doctype html><html><head><meta charset="utf-8">' + CSS + '</head><body>' + html(kind, c, GRAV[k]) + '</body></html>')
    pages.append((st, f'{OUT}/{k}.jpg', 1080 if kind == 'short' else 1280, 1920 if kind == 'short' else 720))
js = "const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();for(const [f,o,w,h] of " + json.dumps(pages) + "){const p=await b.newPage({viewport:{width:w,height:h}});await p.goto('file://'+f,{waitUntil:'networkidle'});await p.evaluate(()=>document.fonts.ready);await p.screenshot({path:o,type:'jpeg',quality:92});await p.close()}await b.close()})()"
subprocess.run(['node', '-e', js], check=True)
print(len(pages), 'capas em', OUT)
