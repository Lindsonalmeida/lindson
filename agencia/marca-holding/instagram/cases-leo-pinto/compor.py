# Barzakh · case Leo Pinto · painel contínuo 3240x1440 (3 posts 3:4). Modelo copiado: fixados-v4 da Barzakh (John Pawson + Snøhetta: 1 imagem herói contínua, frase contínua, símbolo atravessando a divisa 01|02).
import subprocess,os
from PIL import Image
A='/home/user/repos/lindson/agencia/clientes/leo-pinto/identidade-v2/assets'; O=os.path.abspath('.')
G='#CFAE74'; M='#F3EEE4'
lbl="font:500 22px 'JetBrains Mono';letter-spacing:.32em;color:%s;text-transform:uppercase"%M
def post(cx,word,top,bot):
    return f'''<div style="position:absolute;left:{cx-460}px;width:920px;top:96px;{lbl};display:flex;justify-content:space-between;opacity:.9">{top}</div>
<div style="position:absolute;left:{cx-460}px;width:920px;bottom:236px;text-align:center;font:400 160px/1 'Fraunces';font-variation-settings:'opsz' 144;letter-spacing:-.02em;color:{M};text-shadow:0 4px 40px rgba(2,26,61,.6)">{word}</div>
<div style="position:absolute;left:{cx-460}px;width:920px;bottom:150px;height:1px;background:{G};opacity:.8"></div>
<div style="position:absolute;left:{cx-460}px;width:920px;bottom:96px;{lbl};color:{G};display:flex;justify-content:space-between">{bot}</div>'''
sw=['#FF7A1A','#FFC20E','#2350F5','#05316E']
chips=''.join(f'<div style="display:flex;align-items:center;gap:14px"><i style="width:44px;height:44px;border-radius:50%;background:{c};box-shadow:0 0 0 1px rgba(243,238,228,.35)"></i><span>{c}</span></div>' for c in sw)
html=f'''<html><head><link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300..600;1,9..144,300..600&family=JetBrains+Mono:wght@500&display=block" rel="stylesheet"></head>
<body style="margin:0"><div style="width:3240px;height:1440px;position:relative;overflow:hidden;
background:radial-gradient(ellipse 1500px 900px at 1080px 700px,#FFC20E 0%,#FF7A1A 22%,#B4500C 42%,rgba(5,49,110,0) 70%),linear-gradient(90deg,#05316E 0%,#021A3D 55%,#08090C 100%)">
<div style="position:absolute;left:0;right:0;top:820px;bottom:0;background:linear-gradient(180deg,rgba(35,80,245,.55),#021A3D 55%,#08090C)"></div>
<div style="position:absolute;left:0;right:0;top:818px;height:2px;background:linear-gradient(90deg,transparent,#FFC20E 25%,#FFC20E 45%,transparent 90%);opacity:.8"></div>
<img src="file://{A}/simbolo-sol.png" style="position:absolute;left:{1080-330}px;top:{700-330}px;width:660px;filter:drop-shadow(0 20px 80px rgba(8,9,12,.5))">
<div style="position:absolute;inset:0;background:url(file://{A}/grao.png);opacity:.10;mix-blend-mode:overlay"></div>
<div style="position:absolute;left:1560px;top:340px;width:520px;display:flex;flex-direction:column;gap:30px;{lbl};font-size:26px">{chips}</div>
<img src="file://{A}/logo-mono-branco.png" style="position:absolute;left:{2700-330}px;top:300px;width:660px">
{post(540,'Do sol','<span>Barzakh · Case</span><span>01 · Conceito</span>','<span>Vereador Leo Pinto</span><span>São João Batista · MA</span>')}
{post(1620,'<i>nasce</i>','<span>Identidade visual</span><span>02 · Sistema</span>','<span>Símbolo · Cor · Tipografia</span>')}
{post(2700,'a marca.','<span>@barzakhstudio</span><span>03 · Marca</span>','<span>Sua marca é a próxima</span><span>Link na bio</span>')}
</div></body></html>'''
open(O+'/painel.html','w').write(html)
subprocess.run(['node','-e',f'''const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage({{viewport:{{width:3240,height:1440}}}});await p.goto('file://{O}/painel.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(1500);await p.screenshot({{path:'{O}/painel.png'}});await b.close()}})()'''],check=True)
im=Image.open(O+'/painel.png').convert('RGB'); im.save(O+'/painel.jpg',quality=93)
for k in range(3): im.crop((k*1080,0,k*1080+1080,1440)).save(f'{O}/0{k+1}.jpg',quality=93)
os.remove(O+'/painel.png')
