# Prévia do perfil: foto de perfil escolhida, bio, 6 destaques do kit e os 3 fixados. Uso: grade.py pasta
import sys, os, subprocess
d=os.path.abspath(sys.argv[1]); H='/home/user/lindson/agencia/marca-holding'
dest=['01-cases','02-processo','03-pacotes','04-bastidor','05-duvidas','06-contato']; nomes=['Cases','Processo','Pacotes','Bastidor','Dúvidas','Contato']
hl=''.join(f'<div style="text-align:center;width:150px"><img src="file://{H}/kit-contas/01-instagram/destaques/destaque-{a}-circulo.jpg" style="width:128px;height:128px;border-radius:50%;border:3px solid #333;padding:4px"><div style="font:400 24px Inter, sans-serif;margin-top:10px">{n}</div></div>' for a,n in zip(dest,nomes))
grid=''.join(f'<div style="position:relative"><img src="file://{d}/0{i}.jpg" style="width:100%;display:block"><svg style="position:absolute;top:14px;right:14px" width="34" height="34" viewBox="0 0 24 24"><path fill="#fff" d="M16 3l5 5-3 1-4 4 1 5-2 1-4-4-5 5-1-1 5-5-4-4 1-2 5 1 4-4z"/></svg></div>' for i in (1,2,3))
html=f'''<html><head><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=block" rel="stylesheet"></head><body style="margin:0;background:#000;color:#fff;font-family:Inter">
<div style="width:1080px;padding:40px 0 0">
<div style="display:flex;align-items:center;gap:60px;padding:0 40px"><img src="file://{H}/instagram/fixados-v2/foto-de-perfil.jpg" style="width:200px;height:200px;border-radius:50%">
<div style="display:flex;gap:70px;font:700 34px Inter;text-align:center"><div>3<div style="font:400 24px Inter">posts</div></div><div>0<div style="font:400 24px Inter">seguidores</div></div><div>0<div style="font:400 24px Inter">seguindo</div></div></div></div>
<div style="padding:24px 40px;font:400 27px/1.4 Inter"><b>Barzakh · um estúdio Al Kántara</b><br><span style="color:#aaa">Estúdio de design</span><br>A passagem da sua marca.<br>Identidade visual e branding · São Luís · MA<br><span style="color:#E0F1FF">wa.me/5598985621808</span></div>
<div style="display:flex;gap:20px;padding:10px 30px 36px">{hl}</div>
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:3px">{grid}</div></div></body></html>'''
open(d+'/g.html','w').write(html)
subprocess.run(['node','-e',f'''const {{chromium}}=require('/opt/node-tools/node_modules/playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage({{viewport:{{width:1080,height:800}}}});await p.goto('file://{d}/g.html');await p.waitForTimeout(1500);await p.screenshot({{path:'{d}/g.png',fullPage:true}});await b.close()}})()'''],check=True)
from PIL import Image; Image.open(d+'/g.png').convert('RGB').save(d+'/grade.jpg',quality=90); os.remove(d+'/g.png'); os.remove(d+'/g.html')
