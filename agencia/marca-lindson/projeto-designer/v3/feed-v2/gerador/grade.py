# Simulação do perfil @barzakhstudio com o feed v2 (conta Leandro, 16/11/2026). Grade: post 12 no topo-esquerda.
import os
from playwright.sync_api import sync_playwright
G=os.path.dirname(os.path.abspath(__file__)); O=os.path.dirname(G)
LOGO='/home/user/lindson/agencia/marca-lindson/projeto-designer/v3/marca/logos/png/ouro/barzakh-avatar-ouro.png'
u=lambda p:'file://'+p
cel=''.join(f'<div style="aspect-ratio:4/5;background:url({u(O+"/posts/%02d.jpg"%n)}) center/cover"></div>' for n in range(12,0,-1))
hl=''.join(f'<div style="text-align:center;font-size:24px"><div style="width:118px;height:118px;border-radius:50%;border:2px solid #333;background:#0A0C10 url({u(LOGO)}) center/80% no-repeat;margin:0 auto 10px"></div>{t}</div>' for t in ['Cases','Processo','Pacotes','Bastidor','Dúvidas'])
html=f'''<html><body style="margin:0;background:#15171c;font-family:-apple-system,Helvetica,Arial,sans-serif;color:#fff">
<div id="p" style="width:1180px;padding:40px 0;background:#15171c"><div style="margin:0 40px;border-radius:60px;background:#000;overflow:hidden;border:10px solid #2a2d33">
<div style="display:flex;justify-content:space-between;padding:30px 40px;font-size:30px;font-weight:600"><span>09:41</span><span>barzakhstudio ✓</span><span>☰</span></div>
<div style="display:flex;align-items:center;padding:10px 40px;gap:60px"><div style="width:190px;height:190px;border-radius:50%;background:#0A0C10 url({u(LOGO)}) center/85% no-repeat;border:3px solid #B4935A"></div>
<div style="display:flex;gap:70px;font-size:28px;text-align:center"><div><b style="font-size:34px">12</b><br>publicações</div><div><b>·</b><br>seguidores</div><div><b>·</b><br>seguindo</div></div></div>
<div style="padding:20px 40px;font-size:27px;line-height:1.45"><b>Barzakh | Identidade Visual</b><br>Identidade visual e branding · um estúdio Al Kántara<br>Direção criativa: Lindson Almeida · São Luís, MA<br>↓ Orçamento no WhatsApp<br><span style="color:#a9b8ff">lindsonalmeida.pages.dev/site/identidade</span></div>
<div style="display:flex;gap:14px;padding:0 40px 30px">{''.join(f'<div style="flex:1;background:#26282e;border-radius:14px;padding:18px;text-align:center;font-size:26px;font-weight:600">{t}</div>' for t in ['Seguir','Mensagem','WhatsApp'])}</div>
<div style="display:flex;justify-content:space-between;padding:0 40px 30px">{hl}</div>
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:4px">{cel}</div></div></div></body></html>'''
open(G+'/grade.html','w').write(html)
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':1180,'height':1000});pg.goto(u(G+'/grade.html'));pg.wait_for_timeout(800)
    pg.locator('#p').screenshot(path=O+'/grade.jpg',type='jpeg',quality=88);b.close()
