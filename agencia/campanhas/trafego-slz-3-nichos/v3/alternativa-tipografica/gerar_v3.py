"""v3 dos criativos (conta Leandro, 16/11/2026) após a reprovação da v2 ("péssimos"). python3 gerar_v3.py <insumos>
Insumos fora do Git: lin/cNN-rec.png (Lindson recortado, limpar_recorte.py), fonts/Anton.ttf. Paleta da marca: #0A0A0A, #F5F3EE, ação #F5C518."""
import asyncio,os,sys
from playwright.async_api import async_playwright
D=os.path.dirname(os.path.abspath(__file__)); I=sys.argv[1]
def L(c): return f"file://{I}/lin/{c}-rec.png"
CSS=f"""@font-face{{font-family:A;src:url('file://{I}/fonts/Anton.ttf')}}
*{{margin:0;padding:0;box-sizing:border-box}}body{{width:1080px;height:var(--H);overflow:hidden;position:relative;font-family:'Inter';font-weight:900}}
.A{{font-family:A;font-weight:400;text-transform:uppercase;line-height:.9;letter-spacing:-.005em}}
.y{{color:#F5C518}}.k{{color:#0A0A0A}}.w{{color:#F5F3EE}}.hl{{background:#F5C518;color:#0A0A0A;padding:0 .12em}}
.chip{{position:absolute;top:56px;left:60px;font:900 26px Inter;letter-spacing:.08em;text-transform:uppercase;padding:12px 22px;border-radius:99px}}
.cta{{position:absolute;left:60px;right:60px;bottom:60px;height:120px;border-radius:24px;display:flex;align-items:center;justify-content:space-between;padding:0 40px;font:900 40px Inter}}
.cta small{{font:700 24px Inter;opacity:.75;display:block}}.ar{{font-size:64px}}
.lin{{position:absolute;bottom:0;filter:drop-shadow(0 30px 50px rgba(0,0,0,.45))}}
.ph{{position:absolute;background:#111;border-radius:56px;padding:14px;box-shadow:0 50px 90px rgba(0,0,0,.45)}}.scr{{background:#fff;border-radius:44px;overflow:hidden;width:100%;height:100%}}
.nt{{background:rgba(245,243,238,.97);border-radius:30px;padding:22px 26px;display:flex;gap:20px;align-items:center;box-shadow:0 18px 40px rgba(0,0,0,.35);font:600 28px Inter;color:#111}}
.nt i{{width:62px;height:62px;border-radius:16px;background:#25D366;flex:none;display:flex;align-items:center;justify-content:center;color:#fff;font:900 34px Inter;font-style:normal}}.nt b{{display:block;font:900 26px Inter}}.nt span{{opacity:.7}}
.cell{{border-radius:10px}}
"""
def cta(cod,dark=True):
    bg,fg=("#0A0A0A","#F5C518") if dark else ("#F5C518","#0A0A0A")
    return f'<div class="cta" style="background:{bg};color:{fg}"><div><small style="color:{"#F5F3EE" if dark else "#0A0A0A"}">Raio-X grátis do seu Instagram</small>Manda {cod} no WhatsApp</div><div class="ar">→</div></div>'
def chip(t,dark=True): return f'<div class="chip" style="background:{"#0A0A0A" if dark else "#F5C518"};color:{"#F5C518" if dark else "#0A0A0A"}">{t} · São Luís</div>'
def grid(cores):
    return '<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:4px;padding:4px">'+''.join(f'<div class="cell" style="aspect-ratio:1;background:{c}"></div>' for c in cores)+'</div>'
def perfil(nome,cores,legenda,bom):
    return f'<div style="padding:46px 22px 12px;display:flex;gap:18px;align-items:center"><div style="width:96px;height:96px;border-radius:50%;background:{"#F5C518" if bom else "#ccc"};border:4px solid #fff;box-shadow:0 0 0 3px {"#0A0A0A" if bom else "#ddd"}"></div><div style="font:800 26px Inter;color:#111">{nome}<div style="font:500 19px Inter;color:#555;margin-top:6px">{legenda}</div></div></div>'+(f'<div style="margin:6px 22px 10px;background:#0A0A0A;color:#F5C518;border-radius:12px;text-align:center;font:800 22px Inter;padding:12px">Agendar pelo WhatsApp</div>' if bom else '<div style="height:20px"></div>')+grid(cores)
ARTS={}
def art(n,bg,body): ARTS[n]=(bg,body)
# 1 ADV · pergunta direta gigante + Lindson
art('ADV-1','#F5C518',lambda H: chip('Advogado')+f'<img class="lin" src="{L("c08")}" style="right:-120px;height:{H*.62:.0f}px">'+f'<div class="A k" style="position:absolute;left:60px;top:150px;width:900px;font-size:{H*.088:.0f}px">Quem procura<br>advogado em<br>São Luís<br><span class="hl" style="background:#0A0A0A;color:#F5C518">acha você?</span></div>'+cta('ADV'))
# 2 ADV · antes x depois do Instagram
art('ADV-2','#0A0A0A',lambda H: chip('Advogado',False)+f'<div class="A w" style="position:absolute;left:60px;top:140px;font-size:{H*.07:.0f}px">O mesmo escritório.<br><span class="y">Duas impressões.</span></div>'+f'<div class="ph" style="left:50px;top:{H*.33:.0f}px;width:470px;height:{H*.47:.0f}px;transform:rotate(-3deg);opacity:.85"><div class="scr">'+perfil('dr.escritorio',['#d9d9d9','#cfcfcf','#e5e5e5','#d0d0d0','#e0e0e0','#c8c8c8','#ddd','#d5d5d5','#cacaca'],'Bom dia! ☀',False)+'</div></div>'+f'<div class="ph" style="right:50px;top:{H*.31:.0f}px;width:470px;height:{H*.47:.0f}px;transform:rotate(3deg)"><div class="scr">'+perfil('dr.escritorio',['#0A0A0A','#F5C518','#1d2b44','#F5F3EE','#0A0A0A','#c9a55c','#1d2b44','#0A0A0A','#F5C518'],'Direito trabalhista · Renascença',True)+'</div></div>'+f'<div class="A" style="position:absolute;left:90px;top:{H*.29:.0f}px;font-size:44px;color:#999">ANTES</div><div class="A y" style="position:absolute;right:90px;top:{H*.27:.0f}px;font-size:44px">DEPOIS</div>'+cta('ADV',False))
# 3 ADV · busca no Google
art('ADV-3','#F5F3EE',lambda H: chip('Advogado')+f'<img class="lin" src="{L("c10")}" style="left:-110px;height:{H*.55:.0f}px">'+f'<div class="A k" style="position:absolute;left:60px;top:140px;font-size:{H*.075:.0f}px">Ser achado<br>no Google em<br><span class="hl">São Luís.</span></div>'+f'<div style="position:absolute;right:50px;top:{H*.42:.0f}px;width:600px;background:#fff;border-radius:28px;box-shadow:0 40px 80px rgba(0,0,0,.18);padding:28px;font-family:Arial">'+'<div style="border:2px solid #ddd;border-radius:99px;padding:16px 24px;font:500 26px Arial;color:#222">🔍 advogado trabalhista são luís</div>'+''.join(f'<div style="margin-top:22px;padding:18px;border-radius:16px;{st}"><div style="font:400 20px Arial;color:#555">{u}</div><div style="font:400 30px Arial;color:{c};margin-top:4px">{t}</div><div style="font:400 20px Arial;color:#666;margin-top:4px">★★★★★ · Renascença · Aberto agora</div></div>' for u,t,c,st in [('www.seuescritorio.com.br','Seu Escritório · Advocacia','#1a0dab','background:#FFF6CC;border:3px solid #F5C518'),('www.outro.com.br','Outro escritório','#1a0dab;opacity:.45','opacity:.45')])+'</div>'+cta('ADV'))
# 4 BARBA · notificações em cascata + Lindson
art('BARBA-1','#0A0A0A',lambda H: chip('Barbearia',False)+f'<img class="lin" src="{L("c12")}" style="right:-150px;height:{H*.6:.0f}px;opacity:.95">'+f'<div class="A w" style="position:absolute;left:60px;top:140px;font-size:{H*.085:.0f}px">Terça<br>também<br><span class="y">pode lotar.</span></div>'+''.join(f'<div class="nt" style="position:absolute;left:{60+j*14}px;width:640px;top:{H*(.45+j*.075):.0f}px;transform:rotate({(-2+j)*.8}deg)"><i>✓</i><div><b>{n} · WhatsApp</b><span>{m}</span></div></div>' for j,(n,m) in enumerate([('Rafael','Tem horário terça 10h?'),('Bruno','Corte + barba hoje?'),('Thiago','Vi o anúncio, quero agendar'),('Lucas','Sobrou vaga pra amanhã?')]))+cta('BARBA',False))
# 5 BARBA · print de agenda cheia
art('BARBA-2','#F5C518',lambda H: chip('Barbearia')+f'<div class="A k" style="position:absolute;left:60px;top:140px;font-size:{H*.09:.0f}px">Agenda cheia<br>até na terça.</div>'+f'<div style="position:absolute;left:60px;right:60px;top:{H*.36:.0f}px;background:#0A0A0A;border-radius:32px;padding:30px;box-shadow:0 40px 80px rgba(0,0,0,.3)"><div style="display:flex;justify-content:space-between;font:900 30px Inter;color:#F5C518;margin-bottom:18px"><span>TERÇA · AGENDA</span><span style="color:#F5F3EE;opacity:.6">exemplo</span></div>'+''.join(f'<div style="display:flex;gap:18px;align-items:center;margin-top:12px"><span style="font:800 26px Inter;color:#F5F3EE;width:90px;opacity:.7">{h}</span><div style="flex:1;background:{"#F5C518" if i%3 else "#F5F3EE"};border-radius:14px;padding:{H*.012:.0f}px 22px;font:800 26px Inter;color:#0A0A0A">{s}</div></div>' for i,(h,s) in enumerate([('09h','Corte + barba'),('10h','Degradê'),('11h','Corte + sobrancelha'),('14h','Barba'),('15h','Corte infantil'),('16h','Corte + barba'),('17h','Pigmentação')]))+'</div>'+cta('BARBA'))
# 6 BARBA · comparação
art('BARBA-3','#F5F3EE',lambda H: chip('Barbearia')+f'<div class="A k" style="position:absolute;left:60px;top:140px;font-size:{H*.07:.0f}px">Qual barbearia<br>o bairro <span class="hl">vê primeiro?</span></div>'+''.join(f'<div style="position:absolute;top:{H*.34:.0f}px;{side}:60px;width:465px;height:{H*.47:.0f}px;border-radius:32px;background:{bg};padding:36px;color:{fg}"><div class="A" style="font-size:52px;color:{tc}">{t}</div>'+''.join(f'<div style="display:flex;gap:16px;margin-top:{H*.024:.0f}px;font:800 30px Inter;line-height:1.15"><span style="color:{ic}">{ico}</span>{x}</div>' for x in itens)+'</div>' for side,bg,fg,tc,ic,ico,t,itens in [('left','#e4e1da','#555','#888','#c0392b','✕','Só posta',['Post de corte pronto','Impulsiona pro Brasil todo','Responde quando dá','Depende do sábado']),('right','#0A0A0A','#F5F3EE','#F5C518','#F5C518','✓','Anuncia no bairro',['Vídeo que chama pra agendar','Anúncio no raio da barbearia','Mensagem direto no WhatsApp','Movimento na semana toda'])])+cta('BARBA'))
# 7 SORRISO · selo/oferta + Lindson
art('SORRISO-1','#0A0A0A',lambda H: chip('Dentista',False)+f'<img class="lin" src="{L("c14")}" style="left:-80px;height:{H*.6:.0f}px">'+f'<div class="A w" style="position:absolute;left:60px;top:140px;font-size:{H*.08:.0f}px">Paciente novo<br><span class="y">toda semana</span><br>é rotina, não sorte.</div>'+f'<div style="position:absolute;right:60px;top:{H*.47:.0f}px;width:400px;height:400px;border-radius:50%;background:#F5C518;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;transform:rotate(-10deg);box-shadow:0 30px 60px rgba(0,0,0,.5);border:6px dashed #0A0A0A;outline:14px solid #F5C518"><div class="A k" style="font-size:118px">Grátis</div><div style="font:900 30px Inter;color:#0A0A0A;width:300px;line-height:1.1">Raio-X do Instagram da sua clínica</div></div>'+cta('SORRISO',False))
# 8 SORRISO · checklist
art('SORRISO-2','#F5F3EE',lambda H: chip('Dentista')+f'<div class="A k" style="position:absolute;left:60px;top:140px;font-size:{H*.075:.0f}px">Sua clínica<br>tem as <span class="hl">5?</span></div>'+''.join(f'<div style="position:absolute;left:60px;right:60px;top:{H*(.33+j*.092):.0f}px;display:flex;gap:28px;align-items:center;background:{"#0A0A0A" if j%2==0 else "#fff"};color:{"#F5F3EE" if j%2==0 else "#0A0A0A"};border-radius:24px;padding:{H*.018:.0f}px 32px;box-shadow:0 14px 30px rgba(0,0,0,.08)"><div style="width:64px;height:64px;border-radius:14px;border:4px solid #F5C518;flex:none;display:flex;align-items:center;justify-content:center;font:900 42px Inter;color:#F5C518">✓</div><div style="font:900 36px Inter;line-height:1.1">{t}</div></div>' for j,t in enumerate(['Bio que diz o que você faz e onde','Botão direto pro WhatsApp','Vídeo mostrando a clínica e a equipe','Anúncio no raio da clínica','Resposta rápida a quem chama']))+cta('SORRISO'))
# 9 SORRISO · pergunta direta + Lindson
art('SORRISO-3','#F5C518',lambda H: chip('Dentista')+f'<img class="lin" src="{L("c07")}" style="right:-140px;height:{H*.58:.0f}px">'+f'<div class="A k" style="position:absolute;left:60px;top:140px;width:960px;font-size:{H*.082:.0f}px">Orçamento<br>pedido.<br>Paciente<br><span class="hl" style="background:#0A0A0A;color:#F5C518">sumiu?</span></div><div style="position:absolute;left:60px;top:{H*.6:.0f}px;width:480px;font:800 34px Inter;color:#0A0A0A;line-height:1.2">Conteúdo que gera confiança antes da consulta.</div>'+cta('SORRISO'))
# capas dos Reels
CAP={'ADV':('#0A0A0A','c16','Dá pra anunciar<br><span class="y">sem ferir</span><br>a OAB?'),'BARBA':('#F5C518','c09','Sábado<br>lotado.<br><span class="hl" style="background:#0A0A0A;color:#F5C518">Terça vazia?</span>'),'SORRISO':('#F5F3EE','c11','Pediu<br>orçamento<br>e <span class="hl">sumiu?</span>')}
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        async def shot(bg,body,H,path):
            html=f'<html><head><style>:root{{--H:{H}px}}{CSS}</style></head><body style="background:{bg}">{body}</body></html>'
            t=f'{I}/_v3.html';open(t,'w').write(html);pg=await b.new_page(viewport={'width':1080,'height':H});await pg.goto('file://'+t);await pg.evaluate('document.fonts.ready');await pg.wait_for_timeout(300)
            await pg.screenshot(path=path,type='jpeg',quality=90);await pg.close()
        for n,(bg,f) in ARTS.items():
            await shot(bg,f(1920),1920,f'{D}/artes/{n}-9x16.jpg'); await shot(bg,f(1350),1350,f'{D}/artes/{n}-4x5.jpg')
        for k,(bg,c,t) in CAP.items():
            dark=bg=='#0A0A0A'; body=chip({'ADV':'Advogado','BARBA':'Barbearia','SORRISO':'Dentista'}[k],not dark)+f'<img class="lin" src="{L(c)}" style="right:-140px;height:1150px">'+f'<div class="A {"w" if dark else "k"}" style="position:absolute;left:60px;top:200px;font-size:170px">{t}</div><div style="position:absolute;left:60px;bottom:120px;font:900 34px Inter;color:{"#F5C518" if dark else "#0A0A0A"}">▶ REELS · 26 s</div>'
            await shot(bg,body,1920,f'{D}/capas-reels/{k}-capa.jpg')
        await b.close()
    from PIL import Image
    ims=[Image.open(f'{D}/artes/{n}-9x16.jpg') for n in ARTS]; w,h=360,640; S=Image.new('RGB',(3*w+80,3*h+80),'#222')
    for j,im in enumerate(ims): im.thumbnail((w,h)); S.paste(im,(20+(j%3)*(w+20),20+(j//3)*(h+20)))
    S.save(f'{D}/folha.jpg',quality=88)
    ims=[Image.open(f'{D}/capas-reels/{k}-capa.jpg') for k in CAP]; S=Image.new('RGB',(3*w+80,h+40),'#222')
    for j,im in enumerate(ims): im.thumbnail((w,h)); S.paste(im,(20+j*(w+20),20))
    S.save(f'{D}/folha-capas.jpg',quality=88)
asyncio.run(main())
