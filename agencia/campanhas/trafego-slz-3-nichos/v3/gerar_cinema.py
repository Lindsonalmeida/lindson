"""v3 cinema (conta Leandro, 16/11/2026), no padrão da referência aprovada (Behance "Criativos Denis Bugatti 2026", referencias-lindson/22-26.webp):
Lindson protagonista grande em cena dramática, frase curta: linha fina + palavras gigantes condensadas, 1 palavra neon com brilho, assinatura no rodapé.
Geração de cena por IA ficou bloqueada (Gemini free tier = 0, HeyGen sem créditos): cena montada com foto real do Lindson recortada + fundo cinematográfico (Mixkit).
python3 gerar_cinema.py <insumos>  (bg3/*.jpg, lin/cNN-rec.png, fonts/Anton.ttf)"""
import asyncio,os,sys
from playwright.async_api import async_playwright
D=os.path.dirname(os.path.abspath(__file__)); I=sys.argv[1]
RED,LIME='#FF2E3B','#C8FF2E'
#  nome: fundo, pos fundo, blur, lindson, espelhar, tint, linha fina, gigante (com <n>palavra</n>), cor neon, linha final
P={'ADV-1':('fogo','50% 50%',0,'c08',0,'255,90,20','seu concorrente','JÁ ESTÁ<br><n>NO GOOGLE</n>',RED,'e você?'),
 'ADV-2':('fumaca','20% 50%',0,'c10',1,'120,150,255','quando a indicação para,','QUEM TE<br><n>ACHA?</n>',RED,''),
 'ADV-3':('dinheiro','70% 40%',2,'c16',0,'90,200,90','advogado em São Luís','SEJA<br><n>ENCONTRADO</n>',LIME,'sem ferir a OAB'),
 'BARBA-1':('barbearia','40% 40%',14,'c12',0,'255,170,80','sábado lotado,','TERÇA<br><n>VAZIA?</n>',RED,''),
 'BARBA-2':('luzes','0% 50%',6,'c09',1,'200,80,255','o bairro inteiro rolando o Reels','AGENDA<br><n>LOTADA</n>',LIME,'começa no anúncio certo'),
 'BARBA-3':('fogos','50% 50%',0,'c07',0,'255,140,40','movimento','A SEMANA<br><n>TODA</n>',LIME,'não só no sábado'),
 'SORRISO-1':('clinica','50% 40%',16,'c14',0,'120,200,255','dentista,','CADEIRA VAZIA<br><n>CUSTA CARO</n>',RED,''),
 'SORRISO-2':('fumaca2','50% 50%',0,'c15',1,'200,200,220','pediu orçamento e','<n>SUMIU</n>',RED,'faltou confiança, não preço'),
 'SORRISO-3':('lava','50% 50%',0,'c11',0,'255,60,40','paciente novo','TODA<br><n>SEMANA</n>',LIME,'com anúncio e conteúdo no CFO')}
CAPAS={'ADV':('fumaca','30% 50%',0,'c13',0,'255,200,120','advogado de São Luís','DÁ PRA ANUNCIAR<br><n>SEM FERIR</n> A OAB?',RED,'▶ reels'),
 'BARBA':('luzes','0% 50%',8,'c12',1,'200,80,255','dono de barbearia','SÁBADO LOTADO.<br>TERÇA <n>VAZIA?</n>',LIME,'▶ reels'),
 'SORRISO':('fogo','50% 50%',4,'c10',0,'255,90,20','dentista','PEDIU ORÇAMENTO<br>E <n>SUMIU?</n>',RED,'▶ reels')}
def html(H,bg,pos,blur,lin,esp,tint,fina,giga,cor,fim):
    gs=int(H*.12)
    return f"""<html><head><style>@font-face{{font-family:A;src:url('file://{I}/fonts/Anton.ttf')}}*{{margin:0;box-sizing:border-box}}
body{{width:1080px;height:{H}px;overflow:hidden;position:relative;background:#050505;font-family:Inter}}
.bg{{position:absolute;inset:-40px;background:url('file://{I}/bg3/{bg}.jpg') {pos}/cover;filter:blur({blur}px) brightness(.75) saturate(1.35) contrast(1.15)}}
.tn{{position:absolute;inset:0;background:radial-gradient(ellipse at 50% 30%,rgba({tint},.18),transparent 60%),linear-gradient(180deg,rgba(0,0,0,.35),rgba(0,0,0,0) 25%,rgba(0,0,0,.15) 50%,rgba(0,0,0,.92) 82%,#000)}}
.p{{position:absolute;left:50%;bottom:0;height:{H*.86:.0f}px;transform:translateX(-50%) {'scaleX(-1)' if esp else ''};filter:contrast(1.12) saturate(1.05) drop-shadow({'-' if esp else ''}16px 0 26px rgba({tint},.55)) drop-shadow(0 0 60px rgba({tint},.25))}}
.sh{{position:absolute;inset:0;background:linear-gradient(180deg,transparent 52%,rgba(0,0,0,.55) 66%,rgba(0,0,0,.95) 86%)}}
.t{{position:absolute;left:50px;right:50px;bottom:{H*.085:.0f}px;text-align:center;color:#fff}}
.f{{font:300 {H*.03:.0f}px Inter;letter-spacing:.01em;text-transform:uppercase;opacity:.95;margin-bottom:10px}}
.g{{white-space:nowrap;font-family:A;font-size:{gs}px;line-height:.9;text-transform:uppercase;letter-spacing:-.005em;text-shadow:0 8px 30px rgba(0,0,0,.6)}}
n{{color:{cor};text-shadow:0 0 18px {cor}aa,0 0 50px {cor}66}}
.e{{font:400 {H*.022:.0f}px Inter;text-transform:uppercase;letter-spacing:.06em;opacity:.85;margin-top:14px}}
.s{{position:absolute;bottom:{H*.025:.0f}px;left:0;right:0;text-align:center;font:800 18px Inter;letter-spacing:.32em;color:#fff;opacity:.75}}
.gr{{position:absolute;inset:0;opacity:.13;mix-blend-mode:overlay;background:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='200' height='200'><filter id='n'><feTurbulence baseFrequency='.9' numOctaves='2'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>")}}
</style></head><body><div class="bg"></div><div class="tn"></div><img class="p" src="file://{I}/lin/{lin}-rec.png"><div class="sh"></div><div class="gr"></div>
<div class="t"><div class="f">{fina}</div><div class="g">{giga}</div>{f'<div class="e">{fim}</div>' if fim else ''}</div><div class="s">LINDSON ALMEIDA</div><script>const g=document.querySelector('.g');let z=parseFloat(getComputedStyle(g).fontSize);while(g.scrollWidth>980&&z>40){{z-=4;g.style.fontSize=z+'px'}}</script></body></html>"""
# editorial de luxo (referência aprovada "Gomes & Moura"): nome: fundo, pos, blur, lindson, espelhar, palavra de fundo, título caixa alta, itálico dourado, apoio, botão, lado do texto
E={'ADV-2':('adv-16108','60% 40%',10,'c10',1,'Direito','QUEM PROCURA','te encontra?','Conteúdo sério, dentro do Provimento 205, para quem pesquisa advogado em São Luís.','QUERO O RAIO-X GRÁTIS','left'),
 'ADV-3':('adv-8878','40% 40%',12,'c16',0,'Google','O CLIENTE','pesquisa antes.','Ser achado no Google e no Instagram é o novo cartão de visita do escritório.','MANDA ADV NO WHATSAPP','right'),
 'SORRISO-2':('sorriso-12145','50% 40%',12,'c15',1,'Sorriso','CONFIANÇA','antes da consulta.','O paciente escolhe quem ele já conhece. Conteúdo e anúncio dentro das regras do CFO.','MANDA SORRISO','left'),
 'SORRISO-3':('sorriso-33328','30% 40%',14,'c11',0,'Agenda','UM','ritual de agenda cheia.','Anúncio no raio da clínica, atendimento no WhatsApp, rotina que se repete toda semana.','QUERO O RAIO-X GRÁTIS','right')}
def edit(H,bg,pos,blur,lin,esp,fundo,tit,it,apoio,bot,lado):
    al='left' if lado=='left' else 'right'; px='left:70px' if lado=='left' else 'right:70px'; pp='right:-90px' if lado=='left' else 'left:-90px'
    return f"""<html><head><style>@font-face{{font-family:F;src:url('file://{I}/fonts/Fraunces.ttf')}}@font-face{{font-family:F;font-style:italic;src:url('file://{I}/fonts/Fraunces-Italic.ttf')}}*{{margin:0;box-sizing:border-box}}
body{{width:1080px;height:{H}px;overflow:hidden;position:relative;background:#1a120b;font-family:Inter;color:#F3E9DA}}
.bg{{position:absolute;inset:-40px;background:url('file://{I}/bg3/{bg}.jpg') {pos}/cover;filter:blur({blur}px) sepia(.55) saturate(1.3) brightness(.62) contrast(1.05)}}
.lt{{position:absolute;inset:0;background:radial-gradient(ellipse at {'85%' if lado=='left' else '15%'} 15%,rgba(255,190,110,.45),transparent 55%),linear-gradient(180deg,rgba(26,18,11,.1),rgba(26,18,11,.25) 60%,rgba(20,13,8,.9))}}
.big{{position:absolute;bottom:{H*.06:.0f}px;left:-20px;right:-20px;text-align:center;font:italic 400 {H*.2:.0f}px F;color:rgba(255,220,170,.13);white-space:nowrap}}
.p{{position:absolute;{pp};bottom:0;height:{H*.8:.0f}px;{'transform:scaleX(-1);' if esp else ''}filter:sepia(.18) saturate(1.05) contrast(1.06) drop-shadow({'-' if (lado=='left')!=bool(esp) else ''}18px -6px 30px rgba(255,180,90,.45))}}
.top{{position:absolute;top:48px;left:70px;right:70px;display:flex;justify-content:space-between;font:500 18px Inter;letter-spacing:.32em;opacity:.7}}
.t{{position:absolute;{px};top:{H*.11:.0f}px;width:560px;text-align:{al}}}
h1{{font:400 {H*.052:.0f}px F;line-height:1;text-transform:uppercase;letter-spacing:.01em}}h1 i{{display:block;text-transform:none;font-style:italic;color:#E2B26A;font-size:1.12em;margin-top:6px}}
.a{{font:400 {H*.017:.0f}px Inter;line-height:1.45;opacity:.88;margin-top:26px}}
.b{{display:inline-block;margin-top:30px;border:1.5px solid #E2B26A;color:#F3E9DA;padding:16px 30px;font:600 {H*.0125:.0f}px Inter;letter-spacing:.24em}}
.s{{position:absolute;bottom:{H*.025:.0f}px;left:0;right:0;text-align:center;font:700 16px Inter;letter-spacing:.4em;opacity:.7}}
</style></head><body><div class="bg"></div><div class="lt"></div><div class="big">{fundo}</div><img class="p" src="file://{I}/lin/{lin}-rec.png">
<div class="top"><span>TRÁFEGO</span><span>GOOGLE</span><span>WHATSAPP</span></div><div class="t"><h1>{tit}<i>{it}</i></h1><div class="a">{apoio}</div><div class="b">{bot}</div></div><div class="s">LINDSON ALMEIDA · SÃO LUÍS</div></body></html>"""
for k in E: P.pop(k,None)
G=f'{D}/cenas-gemini'
def encaixe(h,nome):
    g=f'{G}/{nome}.jpg'
    if os.path.exists(g):
        h=h.replace('<div class="bg"></div>',f'<div class="bg" style="inset:0;background:url(file://{g}) center/cover;filter:none"></div>',1)
        return __import__('re').sub(r'<img class="p"[^>]*>','',h,1)
    return h.replace('</body>','<div style="position:absolute;top:110px;left:0;right:0;text-align:center"><span style="background:#ff2e3b;color:#fff;font:900 22px Inter;letter-spacing:.2em;padding:8px 18px">PROVISÓRIA</span></div></body>')
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        async def shot(h,H,out):
            t=f'{I}/_c.html';open(t,'w').write(h);pg=await b.new_page(viewport={'width':1080,'height':H});await pg.goto('file://'+t);await pg.evaluate('document.fonts.ready');await pg.wait_for_timeout(300);await pg.screenshot(path=out,type='jpeg',quality=90);await pg.close()
        for n,a in P.items():
            await shot(encaixe(html(1920,*a),n),1920,f'{D}/artes/{n}-9x16.jpg'); await shot(encaixe(html(1350,*a),n),1350,f'{D}/artes/{n}-4x5.jpg')
        for n,a in E.items():
            await shot(encaixe(edit(1920,*a),n),1920,f'{D}/artes/{n}-9x16.jpg'); await shot(encaixe(edit(1350,*a),n),1350,f'{D}/artes/{n}-4x5.jpg')
        for k,a in CAPAS.items(): await shot(encaixe(html(1920,*a),'CAPA-'+k),1920,f'{D}/capas-reels/{k}-capa.jpg')
        await b.close()
    from PIL import Image
    w,h=360,640;S=Image.new('RGB',(3*w+80,3*h+80),'#111')
    for j,n in enumerate(['ADV-1','ADV-2','ADV-3','BARBA-1','BARBA-2','BARBA-3','SORRISO-1','SORRISO-2','SORRISO-3']):
        im=Image.open(f'{D}/artes/{n}-9x16.jpg');im.thumbnail((w,h));S.paste(im,(20+(j%3)*(w+20),20+(j//3)*(h+20)))
    S.save(f'{D}/folha.jpg',quality=88);S=Image.new('RGB',(3*w+80,h+40),'#111')
    for j,k in enumerate(CAPAS):
        im=Image.open(f'{D}/capas-reels/{k}-capa.jpg');im.thumbnail((w,h));S.paste(im,(20+j*(w+20),20))
    S.save(f'{D}/folha-capas.jpg',quality=88)
asyncio.run(main())
