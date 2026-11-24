# Barzakh · case Leo Pinto v2 · painel contínuo 3240x1440. Identidade do Leo = apresentação v13 versão 3 (aprovada 02/11): degradê royal→marinho, mapa de SJB translúcido,
# retrato leo-14 (polo amarela) grande, LEO/PINTO em blocos, Montserrat Black com "povo" em degradê, cores do partido. Moldura Barzakh (rótulos mono, fio dourado) dos fixados-v4.
import subprocess,os,json
from PIL import Image
R='/home/user/repos/lindson/agencia/clientes/leo-pinto'; F=R+'/identidade-v2/assets'; O=os.path.abspath('.')
MAR,ROY,SOL,LAR='#05316E','#2350F5','#FFC20E','#FF7A1A'; G='#FFC20E'; W_='#F6F4EF'
M=json.load(open(R+'/instagram-v13-apresentacao/mapa-sjb.json')); MW=1900; MS=MW/1000; MX,MY=1500,260
lbl="font:600 22px 'JetBrains Mono';letter-spacing:.3em;color:%s;text-transform:uppercase"%W_
def post(cx,word,top,bot):
    return f'''<div style="position:absolute;left:{cx-460}px;width:920px;top:96px;{lbl};display:flex;justify-content:space-between">{top}</div>
<div style="position:absolute;left:{cx-460}px;width:920px;bottom:206px;text-align:center;font:900 150px/1 'Montserrat';letter-spacing:-.02em;color:#fff;filter:drop-shadow(0 10px 30px rgba(2,12,50,.6))">{word}</div>
<div style="position:absolute;left:{cx-460}px;width:920px;bottom:150px;height:2px;background:{G}"></div>
<div style="position:absolute;left:{cx-460}px;width:920px;bottom:96px;{lbl};color:{G};display:flex;justify-content:space-between">{bot}</div>'''
chips=''.join(f'<div style="display:flex;align-items:center;gap:10px"><i style="width:36px;height:36px;border-radius:50%;background:{c};box-shadow:0 0 0 2px rgba(255,255,255,.5)"></i><span>{c}</span></div>' for c in [LAR,SOL,ROY,MAR])
povo=f'<span style="background:linear-gradient(180deg,#FFE066,{SOL} 50%,{LAR});-webkit-background-clip:text;background-clip:text;color:transparent">povo.</span>'
PW=1640; PH=int(1223*PW/1600); PX=1080-PW//2+40; PY=1440-PH+10
mask="radial-gradient(ellipse 52% 75% at 50% 42%,#000 62%,transparent 100%)"
html=f'''<html><head><link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@700;900&family=JetBrains+Mono:wght@600&display=block" rel="stylesheet"></head>
<body style="margin:0"><div style="width:3240px;height:1440px;position:relative;overflow:hidden;
background:radial-gradient(1500px 1100px at 1080px 560px,#4A78FF 0,#2E5BFA 26%,{ROY} 46%,#1539BE 70%,#0B2A8A 88%,#082063 100%)">
<svg width="3240" height="1440" style="position:absolute;inset:0"><defs><linearGradient id="mg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#8CC0FF" stop-opacity=".40"/><stop offset="1" stop-color="#5A86FF" stop-opacity=".16"/></linearGradient></defs>
<g transform="translate({MX+50},{MY+44}) scale({MS})"><polygon points="{M['pts']}" fill="none" stroke="#9CC4FF" stroke-opacity=".32" stroke-width="{3.5/MS}"/></g>
<g transform="translate({MX},{MY}) scale({MS})"><polygon points="{M['pts']}" fill="url(#mg)" stroke="#BFD8FF" stroke-opacity=".45" stroke-width="{2.6/MS}"/></g></svg>
<img src="file://{F}/fotos-v4/h-close-amarela.png" style="position:absolute;left:{PX}px;top:{PY}px;width:{PW}px;-webkit-mask-image:{mask};mask-image:{mask};filter:drop-shadow(0 30px 50px rgba(2,12,50,.45))">
<div style="position:absolute;left:0;right:0;bottom:0;height:560px;background:linear-gradient(0deg,rgba(8,32,99,.92),rgba(8,32,99,0))"></div>
<div style="position:absolute;left:1640px;top:300px;font:900 104px/1 'Montserrat';display:flex;flex-direction:column;align-items:flex-start;gap:14px">
 <span style="background:{SOL};color:{MAR};padding:6px 26px">LEO</span><span style="background:#fff;color:{ROY};padding:6px 26px">PINTO</span></div>
<div style="position:absolute;left:1650px;top:580px;font:700 30px 'Montserrat';letter-spacing:.32em;color:#fff;text-transform:uppercase">Vereador · SJB</div>
<div style="position:absolute;left:2270px;top:820px;width:860px;display:flex;justify-content:space-between;{lbl};font-size:20px;letter-spacing:.12em">{chips}</div>
<img src="file://{F}/logo.png" style="position:absolute;left:2420px;top:250px;width:560px;filter:drop-shadow(0 14px 24px rgba(2,12,50,.4))">
<div style="position:absolute;inset:0;background:url(file://{F}/grao.png);opacity:.10;mix-blend-mode:overlay"></div>
{post(540,'Do povo','<span>Barzakh · Case</span><span>01 · Retrato</span>','<span>Vereador Leo Pinto</span><span>São João Batista · MA</span>')}
{post(1620,'para o','<span>Identidade visual</span><span>02 · Nome</span>','<span>Montserrat · Cor do partido</span>')}
{post(2700,povo,'<span>@barzakhstudio</span><span>03 · Sistema</span>','<span>Sua marca é a próxima</span><span>Link na bio</span>')}
</div></body></html>'''
open(O+'/painel.html','w').write(html)
subprocess.run(['node','-e',f'''const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage({{viewport:{{width:3240,height:1440}}}});await p.goto('file://{O}/painel.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(1500);await p.screenshot({{path:'{O}/painel.png'}});await b.close()}})()'''],check=True)
im=Image.open(O+'/painel.png').convert('RGB'); im.save(O+'/painel.jpg',quality=93)
for k in range(3): im.crop((k*1080,0,k*1080+1080,1440)).save(f'{O}/0{k+1}.jpg',quality=93)
os.remove(O+'/painel.png'); os.remove(O+'/painel.html')
