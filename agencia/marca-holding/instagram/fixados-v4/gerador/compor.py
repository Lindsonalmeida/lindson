# Uso: compor.py foto saida y largura [x] [cor]
# Monta o painel 3240x1440 (foto tratada + símbolo plano em ouro + frase contínua) e corta 01-03. Uso: compor.py foto.jpg pasta_saida simbolo_y simbolo_w
# Composição copiada de: John Pawson (UK, foto de arquitetura em tela cheia, 1 linha de texto), Aesop (AU, serifa editorial calma), Snøhetta (NO, imagem herói contínua).
import sys, subprocess, os, base64
foto,outd=os.path.abspath(sys.argv[1]),os.path.abspath(sys.argv[2]); sy=int(sys.argv[3]); sw=int(sys.argv[4]); sx=int(sys.argv[5]) if len(sys.argv)>5 else 1620; cor=sys.argv[6] if len(sys.argv)>6 else '#CFAE74'
os.makedirs(outd,exist_ok=True)
G='#CFAE74'; M='#EEEAE2'
sym=open('/home/user/lindson/agencia/marca-holding/apresentacao-barzakh/assets/barzakh-simbolo-bronze.svg').read().replace('#B4935A',cor).replace('width="240" height="240"',f'width="{sw}" height="{sw}"')
lbl="font:500 22px 'JetBrains Mono';letter-spacing:.32em;color:%s;text-transform:uppercase"%M
def post(i,cx,word,top,bot):
    return f'''<div style="position:absolute;left:{cx-460}px;width:920px;top:96px;{lbl};display:flex;justify-content:space-between;opacity:.9">{top}</div>
<div style="position:absolute;left:{cx-460}px;width:920px;bottom:236px;text-align:center;font:400 168px/1 'Fraunces';font-variation-settings:'opsz' 144;letter-spacing:-.02em;color:{M};text-shadow:0 4px 40px rgba(14,15,18,.55)">{word}</div>
<div style="position:absolute;left:{cx-460}px;width:920px;bottom:150px;height:1px;background:{G};opacity:.75"></div>
<div style="position:absolute;left:{cx-460}px;width:920px;bottom:96px;{lbl};color:{G};display:flex;justify-content:space-between">{bot}</div>'''
html=f'''<html><head><link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300..600;1,9..144,300..600&family=JetBrains+Mono:wght@500&display=block" rel="stylesheet"></head>
<body style="margin:0"><div style="width:3240px;height:1440px;position:relative;overflow:hidden;background:#0E0F12 url(file://{foto}) center/cover">
<div style="position:absolute;inset:0;background:linear-gradient(0deg,rgba(14,15,18,.72) 0%,rgba(14,15,18,0) 42%),linear-gradient(180deg,rgba(14,15,18,.45) 0%,rgba(14,15,18,0) 18%)"></div>
<div style="position:absolute;left:{sx-sw//2}px;top:{sy-sw//2}px;width:{sw}px;height:{sw}px;filter:drop-shadow(0 10px 50px rgba(14,15,18,.6))">{sym}</div>
{post(1,540,'A passagem','<span>Barzakh</span><span>01 · Conceito</span>','<span>Um estúdio Al Kántara</span><span>São Luís · MA</span>')}
{post(2,1620,'<i>da sua</i>','<span>Identidade visual</span><span>02 · Entrega</span>','<span>Marca · Sistema · Aplicações</span>')}
{post(3,2700,'marca.','<span>@barzakhstudio</span><span>03 · Contato</span>','<span>Agende pelo WhatsApp</span><span>Link na bio</span>')}
</div></body></html>'''
open(outd+'/painel.html','w').write(html)
subprocess.run(['node','-e',f'''const {{chromium}}=require('/opt/node-tools/node_modules/playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage({{viewport:{{width:3240,height:1440}}}});await p.goto('file://{outd}/painel.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(1500);await p.screenshot({{path:'{outd}/painel.png'}});await b.close()}})()'''],check=True)
from PIL import Image
im=Image.open(outd+'/painel.png').convert('RGB'); im.save(outd+'/painel.jpg',quality=93)
for k in range(3): im.crop((k*1080,0,k*1080+1080,1440)).save(f'{outd}/0{k+1}.jpg',quality=93)
os.remove(outd+'/painel.png'); os.remove(outd+'/painel.html')
