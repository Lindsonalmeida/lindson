import asyncio, os
from playwright.async_api import async_playwright
D=os.path.dirname(os.path.abspath(__file__)); A=os.path.join(D,'artes'); os.makedirs(A,exist_ok=True)
N={'ADV':dict(nome='Advogado',bg='#0E1626',ac='#C9A55C',tx='#F3EEE4',cod='ADV'),
   'BARBA':dict(nome='Barbeiro',bg='#141110',ac='#D2763C',tx='#F2ECE6',cod='BARBA'),
   'SORRISO':dict(nome='Dentista',bg='#F2F5F4',ac='#0F7C74',tx='#0D1B1A',cod='SORRISO')}
ART={'ADV':[('reel','Advogado de São Luís:','dá pra anunciar <em>sem ferir</em> a OAB?','Provimento 205 · conteúdo informativo'),
            ('est','Indicação','não pode ser o seu <em>único</em> plano.','Instagram sério, dentro das regras da OAB'),
            ('car','O que a OAB','<em>permite</em> no seu Instagram','Carrossel · 4 telas')],
     'BARBA':[('reel','Sábado lotado.','Terça <em>vazia?</em>','Anúncio pro pessoal do seu bairro'),
            ('est','Cadeira vazia','<em>não volta.</em>','grade'),
            ('car','3 erros','que deixam sua cadeira <em>vazia</em> na semana','Carrossel · 4 telas')],
     'SORRISO':[('reel','Pediu orçamento','e <em>sumiu?</em>','Conteúdo e anúncio dentro do CFO'),
            ('est','Cadeira vazia','na <em>quarta?</em>','grade'),
            ('car','Anúncio de dentista:','o que o <em>CFO</em> deixa fazer','Carrossel · 4 telas')]}
CSS="""@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,700&family=Inter:wght@400;600;800&display=swap');
*{margin:0;box-sizing:border-box}body{width:%dpx;height:%dpx;background:var(--bg);color:var(--tx);font-family:Inter;overflow:hidden;position:relative}
.p{position:absolute;inset:72px;display:flex;flex-direction:column}.k{font-size:26px;letter-spacing:.18em;text-transform:uppercase;color:var(--ac);font-weight:800}
h1{font-family:Fraunces;font-weight:500;line-height:.95;letter-spacing:-.02em}h1 em{font-style:italic;color:var(--ac)}
.s{font-size:30px;opacity:.75;margin-top:28px}.cta{margin-top:auto;display:flex;justify-content:space-between;align-items:center;border-top:2px solid var(--ac);padding-top:28px;font-size:28px;font-weight:600}
.pill{background:var(--ac);color:var(--bg);padding:16px 28px;border-radius:99px;font-weight:800}
.big{position:absolute;right:-40px;bottom:120px;font-family:Fraunces;font-size:520px;opacity:.06;line-height:1}
.chat{margin-top:60px;background:rgba(127,127,127,.12);border-radius:36px;padding:36px;display:flex;flex-direction:column;gap:18px;font-size:30px}
.b{padding:20px 26px;border-radius:24px;max-width:80%%}.me{align-self:flex-end;background:var(--ac);color:var(--bg)}.ot{background:rgba(127,127,127,.22)}
.g{display:grid;grid-template-columns:repeat(6,1fr);gap:12px;margin-top:48px}.g div{height:120px;border-radius:14px;background:var(--ac);display:flex;align-items:flex-end;padding:12px;font-size:22px;font-weight:800;color:var(--bg)}.g .v{background:transparent;border:3px dashed var(--ac);color:var(--ac)}
.n{position:absolute;top:72px;right:72px;font-size:22px;opacity:.6}"""
def art(k,i,t):
    c=N[k];tipo,a,b,s=t;w,h=(1080,1920) if tipo=='reel' else (1080,1350)
    extra=''
    if tipo=='reel': extra=f'<div class="chat"><div class="b me">Oi, Lindson! Vim do anúncio. Quero o raio-x grátis. Código {c["cod"]}</div><div class="b ot">Oi! Me manda o @ do seu Instagram e o bairro. Em até 24 h te devolvo o raio-x.</div></div>'
    if s=='grade':
        dias=['SEG','TER','QUA','QUI','SEX','SÁB'];vaz={'BARBA':[1,2],'SORRISO':[2]}[k]
        extra='<div class="g">'+''.join(f'<div class="{"v" if j in vaz else ""}">{d}</div>' for j,d in enumerate(dias))+'</div>'; s='Anúncio no raio do seu negócio, mensagem no seu WhatsApp'
    fs=150 if tipo=='reel' else 120
    return f"""<html><head><style>:root{{--bg:{c['bg']};--ac:{c['ac']};--tx:{c['tx']}}}{CSS%(w,h)}</style></head><body>
<div class="big">{c['cod'][0]}</div><div class="n">{k}-{i+1}</div><div class="p"><div class="k">{c['nome']} · São Luís</div>
<h1 style="font-size:{fs*0.55:.0f}px;margin-top:80px">{a}</h1><h1 style="font-size:{fs}px;margin-top:10px">{b}</h1><div class="s">{s}</div>{extra}
<div class="cta"><span>Raio-X grátis do seu Instagram</span><span class="pill">Manda {c['cod']}</span></div></div></body></html>""",w,h
PAGES=[('Campanha de tráfego','São Luís · 3 nichos','Advogado, barbeiro e dentista em uma campanha, três conjuntos. Clique para WhatsApp, isca de raio-x grátis. Conta Leandro, 16/11/2026.'),
('Leitura','Agência capta clientes','O anúncio é do Lindson para donos de escritório, barbearia e clínica. Sem preço no anúncio, sem promessa de resultado. Valor só na conversa, depois do raio-x.'),
('Objetivo','Mensagens no WhatsApp','Evento: conversas iniciadas. Dono local responde no WhatsApp, não em formulário. Formulário só como teste na fase 3, se vierem muitos curiosos.'),
('Oferta · Hormozi','Raio-X grátis + plano de 30 dias','Entregue em até 24 h no WhatsApp. Valor alto percebido, risco zero. Códigos: ADV, BARBA, SORRISO.'),
('Persona · Advogado','Sério, discreto, com medo da OAB','26 a 55 anos, Renascença, Cohama, Calhau, Centro. Depende de indicação. Confia em quem conhece o Provimento 205.'),
('Persona · Barbeiro','Sábado lotado, terça vazia','21 a 45 anos, Cohatrac, Turu, Cidade Operária, Anil. Vive no Reels. Quer simples e no WhatsApp.'),
('Persona · Dentista','Orçamento que não volta','26 a 58 anos, Renascença, Calhau, Cohama, Ponta d’Areia. Valoriza ética do CFO e agenda previsível.'),
('Estrutura · Pedro Sobral','1 campanha · 3 conjuntos','ABO no teste (verba igual por nicho), CBO a partir do dia 14. Público aberto (Advantage+) com sugestões; o criativo chama o nicho pelo nome.'),
('Orçamento','Hipótese a testar','Fase 1 (dias 1–7): R$ 20/dia por conjunto. Fase 2 (8–14): CBO R$ 60/dia. Fase 3 (15–30): +20% a cada 3 dias no que estiver abaixo da média. Nenhum resultado prometido.'),
('Criativos','3 por conjunto','Reel com narração, SFX e VFX · estático 4:5 · carrossel 4 telas. Sem foto de cliente inventado.'),
('WhatsApp','Saudação e cadência','Pede o @ e o bairro. Raio-x no D1, exemplo de post no D3, lembrete no D7, encerramento no D14.'),
('Otimização','Dia 3 · 7 · 14','D3: só corta criativo sem conversa e gasto acima de 2× a média. D7: corta o pior de cada conjunto. D14: CBO e escala gradual.'),
('Nomenclatura','LA_MSG_SLZ_3NICHOS','Conjuntos ADV_, BARBA_, SORRISO_. UTMs dinâmicas do Meta. No WhatsApp, o código faz o papel de UTM.'),
('Subida','Checklist de 10 passos','Portfólio, WhatsApp ligado, Engajamento → Mensagens, conjuntos, mensagem pronta, nomes, prévia, revisões no D3/D7/D14. Completo em ESTRATEGIA.md.')]
def pg(i,a,b,c,img=''):
    return f"""<html><head><style>@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500&family=Inter:wght@400;700&display=swap');
@page{{size:1080px 1350px;margin:0}}*{{margin:0;box-sizing:border-box}}body{{font-family:Inter}}.pg{{width:1080px;height:1350px;background:#0F1012;color:#EFEBE3;padding:90px;position:relative;page-break-after:always;overflow:hidden}}
.k{{color:#C9A55C;letter-spacing:.2em;text-transform:uppercase;font-weight:700;font-size:22px}}h1{{font-family:Fraunces;font-weight:500;font-size:96px;line-height:1;margin:40px 0}}p{{font-size:34px;line-height:1.45;opacity:.82;max-width:860px}}
.n{{position:absolute;bottom:70px;right:90px;font-family:Fraunces;font-size:200px;opacity:.07}}.f{{position:absolute;bottom:80px;left:90px;font-size:20px;opacity:.5}}img{{width:100%;border-radius:18px;margin-top:40px}}</style></head><body>"""
async def main():
    async with async_playwright() as p:
        br=await p.chromium.launch(); out=[]
        for k in N:
            for i,t in enumerate(ART[k]):
                h,w,hh=art(k,i,t); pgx=await br.new_page(viewport={'width':w,'height':hh}); await pgx.set_content(h); await pgx.wait_for_timeout(700)
                f=f'{A}/{k}-{i+1}.jpg'; await pgx.screenshot(path=f,type='jpeg',quality=90); out.append(f); await pgx.close()
        from PIL import Image
        ims=[Image.open(f).convert('RGB') for f in out]; cw,ch=360,640; sheet=Image.new('RGB',(cw*3+80,ch*3+80),'#0F1012')
        for j,im in enumerate(ims):
            im.thumbnail((cw,ch)); sheet.paste(im,(20+(j%3)*(cw+20)+(cw-im.width)//2,20+(j//3)*(ch+20)+(ch-im.height)//2))
        sheet.save(f'{A}/folha.jpg',quality=90)
        html=pg(0,'','','')
        for i,(a,b,c) in enumerate(PAGES):
            extra=f'<img src="file://{A}/folha.jpg" style="width:70%">' if a=='Criativos' else ''
            html+=f'<div class="pg"><div class="k">{a}</div><h1>{b}</h1><p>{c}</p>{extra}<div class="n">{i+1:02d}</div><div class="f">Lindson Almeida · tráfego São Luís · hipóteses a testar</div></div>'
        pgx=await br.new_page(); await pgx.goto('about:blank'); open(f'{D}/_pdf.html','w').write(html+'</body></html>')
        await pgx.goto(f'file://{D}/_pdf.html'); await pgx.wait_for_timeout(1000)
        await pgx.pdf(path=f'{D}/ESTRATEGIA.pdf',width='1080px',height='1350px',print_background=True); os.remove(f'{D}/_pdf.html'); await br.close()
asyncio.run(main())
