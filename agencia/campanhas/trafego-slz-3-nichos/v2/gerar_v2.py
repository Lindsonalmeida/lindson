"""v2 da campanha de tráfego SLZ 3 nichos (conta Leandro, 16/11/2026). Uso: python3 gerar_v2.py <pasta-insumos>
Insumos (fora do Git): fr/*.jpg (frames Mixkit), lin/cNN-rec.png (recortes do Lindson), fonts/*.ttf, qr/*.png."""
import asyncio, os, sys, base64
from playwright.async_api import async_playwright
D=os.path.dirname(os.path.abspath(__file__)); I=sys.argv[1]; A=f'{D}/artes'
def u(p): return 'file://'+os.path.join(I,p)
FONT=f"""@font-face{{font-family:F;src:url('{u("fonts/Fraunces.ttf")}')}}@font-face{{font-family:F;font-style:italic;src:url('{u("fonts/Fraunces-Italic.ttf")}')}}@font-face{{font-family:I;src:url('{u("fonts/Inter.ttf")}')}}"""
GRAIN="data:image/svg+xml;base64,"+base64.b64encode(b"<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 .5 0 0 0 0 .5 0 0 0 0 .5 0 0 0 .55 0'/></filter><rect width='100%' height='100%' filter='url(#n)'/></svg>").decode()
N={'ADV':dict(nome='Advogado',ac='#D4B06A',sh='8,14,28',cod='ADV'),
   'BARBA':dict(nome='Barbearia',ac='#E0823F',sh='18,12,8',cod='BARBA'),
   'SORRISO':dict(nome='Dentista',ac='#5FD3C4',sh='6,26,28',cod='SORRISO')}
CSS=FONT+"""*{margin:0;box-sizing:border-box}body{width:%(w)dpx;height:%(h)dpx;overflow:hidden;position:relative;background:#000;color:#F4EFE6;font-family:I}
.bg{position:absolute;inset:0;background-size:cover;background-position:%(pos)s;filter:saturate(.75) contrast(1.08)}
.tone{position:absolute;inset:0;background:linear-gradient(180deg,rgba(var(--sh),.15) 0%%,rgba(var(--sh),.35) 40%%,rgba(var(--sh),.94) 78%%,rgba(var(--sh),1));mix-blend-mode:normal}
.leak{position:absolute;width:900px;height:900px;border-radius:50%%;background:radial-gradient(circle,var(--ac) 0,transparent 65%%);opacity:.35;mix-blend-mode:screen;top:-300px;right:-300px;filter:blur(30px)}
.grain{position:absolute;inset:0;background-image:url(%(g)s);opacity:.22;mix-blend-mode:overlay}
.vig{position:absolute;inset:0;box-shadow:inset 0 0 260px rgba(0,0,0,.75)}
.k{font:700 24px I;letter-spacing:.24em;text-transform:uppercase;color:var(--ac);display:flex;gap:14px;align-items:center}.k:before{content:'';width:46px;height:2px;background:var(--ac)}
h1{font-family:F;font-weight:400;line-height:.92;letter-spacing:-.01em;word-spacing:.06em;font-variation-settings:'opsz' 144,'SOFT' 50}h1 em{font-style:italic;color:var(--ac)}
.txt{position:absolute;left:72px;right:72px;bottom:190px}.s{font-size:30px;line-height:1.35;opacity:.85;margin-top:26px;max-width:820px}
.cta{position:absolute;left:72px;right:72px;bottom:70px;display:flex;justify-content:space-between;align-items:center;font:600 26px I;border-top:1px solid rgba(255,255,255,.25);padding-top:26px}
.pill{background:var(--ac);color:#111;padding:16px 30px;border-radius:99px;font-weight:800;box-shadow:0 10px 40px rgba(0,0,0,.4)}
.tag{position:absolute;top:60px;left:72px;right:72px;display:flex;justify-content:space-between;font:500 20px I;opacity:.8}
.ph{position:absolute;width:430px;height:880px;border-radius:64px;background:#0b0b0c;padding:16px;box-shadow:0 60px 120px rgba(0,0,0,.7),0 0 0 2px rgba(255,255,255,.15);transform:rotate(-6deg)}
.sc{width:100%%;height:100%%;border-radius:50px;background:#E9E2D8 url(%(g)s);overflow:hidden;font-size:22px;color:#111;display:flex;flex-direction:column}
.wh{background:#075E54;color:#fff;padding:60px 24px 20px;font-weight:700;font-size:24px}.wh small{display:block;font-weight:400;opacity:.8;font-size:17px}
.ms{padding:20px;display:flex;flex-direction:column;gap:14px}.b{padding:14px 18px;border-radius:16px;max-width:85%%;line-height:1.3;box-shadow:0 1px 1px rgba(0,0,0,.15)}.me{align-self:flex-end;background:#DCF8C6}.ot{background:#fff}
.lin{position:absolute;filter:drop-shadow(0 40px 60px rgba(0,0,0,.6)) drop-shadow(-12px 0 30px rgba(var(--rim),.35))}
.cred{position:absolute;bottom:22px;right:72px;font-size:14px;opacity:.45}
.card{position:absolute;background:rgba(10,10,12,.55);backdrop-filter:blur(18px);border:1px solid rgba(255,255,255,.18);border-radius:28px;padding:30px 34px;font-size:26px;line-height:1.35}
.num{font-family:F;font-style:italic;color:var(--ac);font-size:120px;line-height:.8;display:block;margin-bottom:10px}
"""
def chat(cod,ot):
    return f'<div class="wh">Lindson Almeida<small>online</small></div><div class="ms"><div class="b me">Oi, Lindson! Vim do anúncio. Quero o raio-x grátis do meu Instagram. Código {cod}</div><div class="b ot">{ot}</div><div class="b me">@meuperfil · bairro Renascença</div></div>'
def page(k,w,h,bg,pos,body,rim='255,200,120'):
    c=N[k]
    return f"""<html><head><style>{CSS%dict(w=w,h=h,pos=pos,g=GRAIN)}:root{{--ac:{c['ac']};--sh:{c['sh']};--rim:{rim}}}</style></head><body>
<div class="bg" style="background-image:url('{u('fr/'+bg)}')"></div><div class="tone"></div><div class="leak"></div>{body}<div class="vig"></div><div class="grain"></div>
<div class="cred">Imagem ilustrativa · Mixkit</div></body></html>"""
def cta(c,txt='Raio-X grátis do seu Instagram'): return f'<div class="cta"><span>{txt}</span><span class="pill">Manda {c} no WhatsApp</span></div>'
def tag(k,n): return f'<div class="tag"><span>LINDSON ALMEIDA · São Luís</span><span>{k}-{n}</span></div>'
ARTS={
'ADV-1':('ADV',1080,1920,'adv-16108.jpg','60% 30%',lambda:tag('ADV',1)+'<div class="ph" style="right:70px;top:300px">'+'<div class="sc">'+chat('ADV','Oi! Me manda o @ e o bairro do escritório. Em até 24 h te devolvo o raio-x.')+'</div></div><div class="txt"><div class="k">Advogado · São Luís</div><h1 style="font-size:132px;margin-top:26px">Dá pra anunciar <em>sem ferir</em> a OAB?</h1><div class="s">Provimento 205: conteúdo informativo, sem promessa e sem preço.</div></div>'+cta('ADV')),
'ADV-2':('ADV',1080,1350,'adv-12315.jpg','30% 30%',lambda:tag('ADV',2)+f'<img class="lin" src="{u("lin/c08-rec.png")}" style="height:1020px;right:-60px;bottom:0">'+'<div class="txt" style="right:420px;bottom:200px"><div class="k">Advogado</div><h1 style="font-size:104px;margin-top:22px">Indicação não pode ser o seu <em>único</em> plano.</h1><div class="s">Instagram sério, dentro das regras da OAB.</div></div>'+cta('ADV'),'212,176,106'),
'ADV-3':('ADV',1080,1350,'adv-16105.jpg','40% 35%',lambda:tag('ADV',3)+'<div class="card" style="right:72px;top:150px;width:420px"><b style="color:var(--ac)">PODE</b><br>informar, explicar direitos, áreas de atuação</div><div class="card" style="right:72px;top:390px;width:420px"><b style="color:#ff8a7a">NÃO PODE</b><br>preço, promessa, captação</div><div class="txt"><div class="k">Carrossel · 4 telas</div><h1 style="font-size:112px;margin-top:22px">O que a OAB <em>permite</em> no seu Instagram</h1></div>'+cta('ADV')),
'BARBA-1':('BARBA',1080,1920,'barba-40127.jpg','50% 40%',lambda:tag('BARBA',1)+'<div class="ph" style="right:60px;top:280px;transform:rotate(5deg)"><div class="sc">'+chat('BARBA','Fechou! Me manda o @ da barbearia e o bairro que eu te mostro.')+'</div></div><div class="txt"><div class="k">Barbearia · São Luís</div><h1 style="font-size:150px;margin-top:26px">Sábado lotado. Terça <em>vazia?</em></h1><div class="s">Anúncio pro pessoal do seu bairro chamar no seu WhatsApp.</div></div>'+cta('BARBA')),
'BARBA-2':('BARBA',1080,1350,'barba-43233.jpg','65% 30%',lambda:tag('BARBA',2)+'<div class="card" style="left:72px;top:150px;display:flex;gap:10px">'+''.join(f'<div style="width:78px;height:96px;border-radius:14px;{"border:2px dashed var(--ac)" if d in("TER","QUA") else "background:var(--ac);color:#111"};display:flex;align-items:flex-end;padding:8px;font:800 17px I">{d}</div>' for d in ['SEG','TER','QUA','QUI','SEX','SÁB'])+'</div><div class="txt"><div class="k">Barbearia</div><h1 style="font-size:150px;margin-top:22px">Cadeira vazia <em>não volta.</em></h1><div class="s">Anúncio no raio da sua barbearia, mensagem no seu WhatsApp.</div></div>'+cta('BARBA')),
'BARBA-3':('BARBA',1080,1350,'barba-271.jpg','50% 50%',lambda:tag('BARBA',3)+'<div class="txt" style="bottom:330px"><div class="k">Carrossel · 4 telas</div><h1 style="font-size:150px;margin-top:22px"><span class="num" style="font-size:300px">3</span>erros que deixam sua cadeira <em>vazia</em></h1></div>'+cta('BARBA')),
'SORRISO-1':('SORRISO',1080,1920,'sorriso-12140.jpg','35% 40%',lambda:tag('SORRISO',1)+'<div class="ph" style="right:60px;top:300px"><div class="sc">'+chat('SORRISO','Oi! Me manda o @ da clínica e o bairro. Raio-x em até 24 h.')+'</div></div><div class="txt"><div class="k">Dentista · São Luís</div><h1 style="font-size:150px;margin-top:26px">Pediu orçamento e <em>sumiu?</em></h1><div class="s">Conteúdo e anúncio dentro das regras do CFO.</div></div>'+cta('SORRISO')),
'SORRISO-2':('SORRISO',1080,1350,'sorriso-6609.jpg','60% 40%',lambda:tag('SORRISO',2)+f'<img class="lin" src="{u("lin/c15-rec.png")}" style="height:980px;right:-70px;bottom:0">'+'<div class="txt" style="right:430px"><div class="k">Dentista</div><h1 style="font-size:116px;margin-top:22px">Cadeira vazia na <em>quarta?</em></h1><div class="s">Anúncio no raio da clínica e atendimento no WhatsApp, dentro do CFO.</div></div>'+cta('SORRISO'),'95,211,196'),
'SORRISO-3':('SORRISO',1080,1350,'sorriso-12145.jpg','50% 35%',lambda:tag('SORRISO',3)+'<div class="card" style="left:72px;top:150px;width:440px"><b style="color:var(--ac)">PODE</b><br>nome, CRO, especialidade, conteúdo educativo</div><div class="card" style="left:540px;top:150px;width:470px"><b style="color:#ff8a7a">NÃO PODE</b><br>antes e depois, preço, desconto, promessa</div><div class="txt"><div class="k">Carrossel · 4 telas</div><h1 style="font-size:118px;margin-top:22px">Anúncio de dentista: o que o <em>CFO</em> deixa fazer</h1></div>'+cta('SORRISO')),
}
# telas de texto dos Reels (PNG transparente sobre o vídeo)
CENAS=__import__('json').load(open(f'{D}/reels/cenas.json'))
def cena_html(k,i,t,final):
    c=N[k]
    return f"""<html><head><style>{FONT}*{{margin:0}}body{{width:1080px;height:1920px;background:transparent;font-family:I;color:#F4EFE6;position:relative}}
.g{{position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,0) 35%,rgba({c['sh']},.9) 80%)}}
.t{{position:absolute;left:70px;right:70px;bottom:330px}}.k{{font:700 26px I;letter-spacing:.24em;color:{c['ac']};text-transform:uppercase}}
h1{{font-family:F;font-weight:400;font-size:{110 if len(t)<60 else 88}px;line-height:.98;margin-top:22px;text-shadow:0 6px 30px rgba(0,0,0,.5)}}h1 em{{font-style:italic;color:{c['ac']}}}
.p{{position:absolute;bottom:200px;left:70px;background:{c['ac']};color:#111;font:800 34px I;padding:20px 36px;border-radius:99px}}</style></head><body><div class="g"></div>
<div class="t"><div class="k">{c['nome']} · São Luís</div><h1>{t}</h1></div>{f'<div class="p">Manda {c["cod"]} no WhatsApp</div>' if final else ''}</body></html>"""
PDF=[('capa',None),('Leitura','A agência capta clientes','O anúncio é do Lindson para donos de escritório, barbearia e clínica em São Luís. Sem preço no anúncio, sem promessa de resultado. Valor só na conversa, depois do raio-x.','adv-21261.jpg'),
('Objetivo','Mensagens no WhatsApp','Evento: conversas iniciadas. Dono local responde no WhatsApp, não em formulário. Formulário só como teste na fase 3.','barba-40130.jpg'),
('Oferta · Hormozi','Raio-X grátis + plano de 30 dias','Entregue em até 24 h no WhatsApp. Valor alto, risco zero para o dono. Códigos: ADV, BARBA, SORRISO.','sorriso-33328.jpg'),
('Persona · Advogado','Sério, discreto, com medo da OAB','26 a 55 anos · Renascença, Cohama, Calhau, Centro. Depende de indicação. Confia em quem conhece o Provimento 205.','adv-16105.jpg'),
('Persona · Barbeiro','Sábado lotado, terça vazia','21 a 45 anos · Cohatrac, Turu, Cidade Operária, Anil. Vive no Reels. Quer simples e no WhatsApp.','barba-43233.jpg'),
('Persona · Dentista','Orçamento que não volta','26 a 58 anos · Renascença, Calhau, Cohama, Ponta d’Areia. Valoriza a ética do CFO e agenda previsível.','sorriso-12140.jpg'),
('Estrutura · Pedro Sobral','1 campanha · 3 conjuntos','ABO no teste (verba igual por nicho), CBO a partir do dia 14. Público aberto (Advantage+) com sugestões; o criativo chama o nicho pelo nome.','adv-16108.jpg'),
('Orçamento','Hipótese a testar','Fase 1 (dias 1–7): R$ 20/dia por conjunto. Fase 2 (8–14): CBO R$ 60/dia. Fase 3 (15–30): +20% a cada 3 dias no que estiver abaixo da média. Nenhum resultado prometido.','barba-271.jpg'),
('criativos',None),('reels',None),
('WhatsApp','Saudação e cadência','Pede o @ e o bairro. Raio-x no D1, exemplo de post no D3, lembrete no D7, encerramento no D14.','sorriso-6609.jpg'),
('Otimização','Dia 3 · 7 · 14','D3: só corta criativo sem conversa e gasto acima de 2× a média. D7: corta o pior de cada conjunto. D14: CBO e escala gradual.','adv-8878.jpg'),
('Subida','Checklist de 10 passos','Portfólio, WhatsApp ligado, Engajamento → Mensagens, conjuntos, mensagem pronta, nomes, prévia, revisões no D3/D7/D14. Completo em ESTRATEGIA.md.','sorriso-12145.jpg')]
PCSS=FONT+"""@page{size:1080px 1350px;margin:0}*{margin:0;box-sizing:border-box}body{font-family:I;color:#F1ECE3}
.pg{width:1080px;height:1350px;position:relative;overflow:hidden;page-break-after:always;background:#0d0e10}
.bg{position:absolute;inset:0;background-size:cover;background-position:center;filter:saturate(.7) contrast(1.1)}
.tn{position:absolute;inset:0;background:linear-gradient(180deg,rgba(13,14,16,.2),rgba(13,14,16,.55) 45%,#0d0e10 80%)}
.lk{position:absolute;width:900px;height:900px;border-radius:50%;background:radial-gradient(circle,#D4B06A,transparent 65%);opacity:.28;mix-blend-mode:screen;top:-320px;right:-320px;filter:blur(30px)}
.gr{position:absolute;inset:0;background-image:url(GRAIN);opacity:.2;mix-blend-mode:overlay}
.c{position:absolute;left:90px;right:90px;bottom:120px}.k{color:#D4B06A;letter-spacing:.22em;text-transform:uppercase;font:700 22px I}
h1{font-family:F;font-weight:400;font-size:100px;line-height:.95;margin:28px 0;letter-spacing:-.02em}h1 em{font-style:italic;color:#D4B06A}p{font-size:32px;line-height:1.45;opacity:.85;max-width:880px}
.n{position:absolute;top:70px;right:90px;font-family:F;font-style:italic;font-size:64px;color:#D4B06A}.f{position:absolute;top:84px;left:90px;font-size:18px;opacity:.6;letter-spacing:.12em}
.gd{position:absolute;inset:200px 90px 120px;display:grid;gap:14px}.gd img{width:100%;height:100%;object-fit:cover;border-radius:10px;box-shadow:0 20px 40px rgba(0,0,0,.5)}
.rl{display:flex;gap:26px;position:absolute;top:330px;left:90px;right:90px}.rl div{flex:1;text-align:center;font-size:22px}.rl img.cv{width:100%;border-radius:16px;box-shadow:0 30px 60px rgba(0,0,0,.6)}.rl img.qr{width:150px;margin-top:18px;border-radius:8px;background:#fff;padding:8px}"""
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        async def shot(html,w,h,path,transparent=False):
            pg=await b.new_page(viewport={'width':w,'height':h}); tmp=f'{I}/_t.html'; open(tmp,'w').write(html); await pg.goto('file://'+tmp); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(500)
            await pg.screenshot(path=path,type='png' if transparent else 'jpeg',quality=None if transparent else 92,omit_background=transparent); await pg.close()
        for n,(k,w,h,bg,pos,f,*r) in ARTS.items(): await shot(page(k,w,h,bg,pos,f(),*r),w,h,f'{A}/{n}.jpg')
        os.makedirs(f'{I}/cenas',exist_ok=True)
        for k,lst in CENAS.items():
            for i,c in enumerate(lst): await shot(cena_html(k,i,c['tela'],i==len(lst)-1),1080,1920,f'{I}/cenas/{k}-{i}.png',True)
        from PIL import Image
        ims=[Image.open(f'{A}/{n}.jpg') for n in ARTS]; cw,ch=360,640; S=Image.new('RGB',(cw*3+80,ch*3+80),'#0d0e10')
        for j,im in enumerate(ims): im=im.copy(); im.thumbnail((cw,ch)); S.paste(im,(20+(j%3)*(cw+20)+(cw-im.width)//2,20+(j//3)*(ch+20)+(ch-im.height)//2))
        S.save(f'{A}/folha.jpg',quality=90)
        if os.environ.get('SO_ARTES'): return await b.close()
        html=f'<html><head><style>{PCSS.replace("GRAIN",GRAIN)}</style></head><body>'
        for i,it in enumerate(PDF):
            if it[0]=='capa':
                html+=f'<div class="pg"><div class="bg" style="background-image:url({u("fr/adv-16108.jpg")});opacity:.35"></div><div class="tn"></div><div class="lk"></div><img src="{u("lin/c11-rec.png")}" style="position:absolute;right:-80px;bottom:0;height:1100px;filter:drop-shadow(-14px 0 40px rgba(212,176,106,.35))"><div class="f">LINDSON ALMEIDA · TRÁFEGO PAGO</div><div class="c" style="right:440px"><div class="k">São Luís · 3 nichos</div><h1 style="font-size:118px">Uma campanha, <em>três</em> conjuntos.</h1><p>Advogado, barbeiro e dentista no clique para WhatsApp. Conta Leandro, 16/11/2026.</p></div><div class="gr"></div></div>'
            elif it[0]=='criativos':
                html+='<div class="pg"><div class="f">CRIATIVOS · 9 PEÇAS</div><div class="n">'+f'{i:02d}'+'</div><div class="gd" style="grid-template-columns:repeat(3,1fr);grid-template-rows:repeat(3,1fr)">'+''.join(f'<img src="file://{A}/{n}.jpg">' for n in ARTS)+'</div><div class="gr"></div></div>'
            elif it[0]=='reels':
                html+='<div class="pg"><div class="lk"></div><div class="f">REELS · NARRAÇÃO, SFX, VFX E TRILHA</div><div class="n">'+f'{i:02d}'+'</div><div class="c" style="top:150px;bottom:auto"><h1 style="font-size:84px">Assista aos <em>3 Reels</em></h1></div><div class="rl">'+''.join(f'<div><img class="cv" src="file://{D}/reels/{k}-capa.jpg"><br><img class="qr" src="{u("qr/"+k+".png")}"><br>{k} · aponte a câmera</div>' for k in N)+'</div><div class="c"><p style="font-size:24px">Trilha e imagens: Mixkit (licença livre). Narração gerada por IA. Links dos vídeos no painel do admin.</p></div><div class="gr"></div></div>'
            else:
                a,t,tx,bg=it; html+=f'<div class="pg"><div class="bg" style="background-image:url({u("fr/"+bg)})"></div><div class="tn"></div><div class="lk"></div><div class="f">LINDSON ALMEIDA · TRÁFEGO SÃO LUÍS</div><div class="n">{i:02d}</div><div class="c"><div class="k">{a}</div><h1>{t}</h1><p>{tx}</p></div><div class="gr"></div></div>'
        open(f'{I}/_pdf.html','w').write(html+'</body></html>')
        pg=await b.new_page(); await pg.goto(f'file://{I}/_pdf.html'); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(1500)
        await pg.pdf(path=f'{D}/ESTRATEGIA-v2.pdf',width='1080px',height='1350px',print_background=True); await b.close()
asyncio.run(main())
