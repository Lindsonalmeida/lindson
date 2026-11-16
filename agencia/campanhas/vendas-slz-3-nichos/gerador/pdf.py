# Gera o PDF 4:5 da estratégia (conta Leandro, 16/11/2026). Uso: python3 gerador/pdf.py
import pathlib, asyncio, sys
from playwright.async_api import async_playwright
B=pathlib.Path(__file__).resolve().parents[1]; R=B.parents[2]
V=R/'agencia/marca-holding/v2'; F=V/'fontes'
REC=pathlib.Path(sys.argv[1]); NF=pathlib.Path(sys.argv[2])
IMG={'adv':['1505664194779-8beaceb93744','1589829545856-d10d557cf95f','1450101499163-c8848c66ca85','1521791055366-0d553872125f','1497366216548-37526070297c'],'barba':['1585747860715-2ba37e788b70','1599351431202-1e0f0137899a','1621605815971-fbc98d665033','1622286342621-4bd786c2447c','1503951914875-452162b0f3f1'],'dente':['1629909613654-28e377c37b09','1606811971618-4486d14f3f99','1588776814546-1ffcf47267a5','1598256989800-fe5f95da9787','1609840114035-3c981b782dfe']}
nf=lambda k,i:(NF/f'{IMG[k][i]}.jpg').as_uri()
eu=lambda c,h,css='right:-40px':f'<img src="{(REC/("c"+c+".png")).as_uri()}" style="position:absolute;bottom:0;{css};height:{h}px;filter:drop-shadow(-6px 0 0 rgba(184,149,90,.35)) drop-shadow(0 30px 40px rgba(0,0,0,.6));z-index:1">'
css=f"""
@font-face{{font-family:Fr;src:url('{(F/'Fraunces-Regular.ttf').as_uri()}')}}
@font-face{{font-family:FrS;src:url('{(F/'Fraunces-SemiBold.ttf').as_uri()}')}}
@font-face{{font-family:FrI;src:url('{(F/'Fraunces-Italic-latin.woff2').as_uri()}')}}
@font-face{{font-family:IT;src:url('{(F/'InterTight-Medium.ttf').as_uri()}')}}
@font-face{{font-family:ITS;src:url('{(F/'InterTight-SemiBold.ttf').as_uri()}')}}
@font-face{{font-family:JB;src:url('{(F/'JetBrainsMono-Medium.ttf').as_uri()}')}}
@page{{size:1080px 1350px;margin:0}}*{{box-sizing:border-box;margin:0}}
body{{font-family:IT;color:#EFEAE1}}
.gig{{position:absolute!important;left:-40px;right:-40px;top:520px;text-align:center;font-family:FrI;font-size:420px;line-height:1;color:rgba(239,220,190,.12);white-space:nowrap;z-index:1!important}}.lab{{position:absolute!important;top:44px;left:90px;right:90px;display:flex;justify-content:space-between;font-family:Fr;font-size:16px;letter-spacing:.3em;text-transform:uppercase;color:#8E8A82}}.bgf{{filter:sepia(.3) saturate(.9);position:absolute;inset:0;background-size:cover;background-position:center;z-index:0}}.p>*{{position:relative;z-index:2}}.p>.bgf,.p>img,.p>.ft{{position:absolute}}.p>.bgf{{z-index:0}}.strip{{position:absolute!important;left:90px;right:90px;bottom:100px;height:190px;background-size:cover;background-position:center;border-radius:200px 200px 0 0}}
.p{{width:1080px;height:1350px;padding:96px 90px;position:relative;overflow:hidden;background:#0B0C0E;page-break-after:always}}
.l{{background:#EFEAE1;color:#0B0C0E}}
.k{{font-family:JB;font-size:19px;letter-spacing:.18em;text-transform:uppercase;color:#B8955A}}
h1{{font-family:Fr;font-weight:400;font-size:112px;line-height:.98;letter-spacing:-.02em;margin:28px 0}}
h2{{font-family:Fr;font-weight:400;font-size:74px;line-height:1.02;letter-spacing:-.015em;margin:22px 0 34px}}
em{{font-family:FrI;font-style:normal;color:#B8955A}}
p,li{{font-size:26px;line-height:1.42}} li{{margin:0 0 12px 0}} ul{{padding-left:26px}}
.ft{{position:absolute;bottom:52px;left:90px;right:90px;display:flex;justify-content:space-between;font-family:JB;font-size:15px;letter-spacing:.14em;color:#8E8A82;text-transform:uppercase}}
table{{width:100%;border-collapse:collapse;font-size:23px}} td{{padding:13px 0;border-bottom:1px solid rgba(142,138,130,.35)}} td:last-child{{text-align:right;font-family:JB}}
tr.t td{{font-family:ITS;border:0;padding-top:22px;color:#B8955A;font-size:27px}}
.big{{font-family:Fr;font-size:200px;line-height:.9;color:#B8955A}}
.box{{border:1px solid #B8955A;padding:30px 34px;margin-top:26px}}
.msg{{background:#1A1C20;border-left:4px solid #B8955A;padding:30px 36px;font-size:27px;line-height:1.5;margin:20px 0}}
.l .msg{{background:#fff}}
.cols{{display:grid;grid-template-columns:1fr 1fr;gap:40px}}
.n{{font-family:JB;color:#B8955A;margin-right:12px}}
.nich{{}}.cover{{background:linear-gradient(180deg,rgba(11,12,14,.25),#0B0C0E 72%),url('{(V/'fotos-v2.1/slz-portugal.jpg').as_uri()}') center/cover}}
"""
def ft(n,t): return f'<div class="ft"><span>Al Kántara · Lindson Almeida</span><span>{t} · {n:02d}</span></div>'
P=[]
def pg(html,cls='',t='Vendas SLZ',img=None):
  if img and 'l' in cls: html+=f'<div class="strip" style="background-image:url({img})"></div>'
  elif img:
    g='rgba(11,12,14,.25),rgba(11,12,14,.55) 40%,#0B0C0E 85%' if cls=='nich' else 'rgba(11,12,14,.84),rgba(11,12,14,.92)'
    html=f'<div class="bgf" style="background-image:linear-gradient(180deg,{g}),url({img})"></div>'+html
  html+='<div class="lab"><span>Autoridade</span><span>Visibilidade</span><span>São Luís</span></div>'
  P.append((cls,html,t))
pg('<div class="k">Estratégia de vendas · São Luís · nov/2026</div><div style="position:absolute;bottom:170px;left:90px;right:90px"><h1>São Luís<br>precisa <em>te ver.</em></h1><p style="font-size:30px;max-width:560px">Oferta, copy, funil e fechamento para <b>advogados, barbeiros e dentistas</b>.</p></div>'+eu('13',1000,'right:-60px'),'cover')
pg('<div class="k">O princípio</div><h2>Persuasão máxima,<br><em>nenhuma mentira.</em></h2><ul><li>Desejo de faturar, visibilidade e medo de perder para o concorrente.</li><li>Escassez real: até 15 clientes; 1 por área ou bairro.</li><li>Sem resultado garantido, sem depoimento ou número inventado.</li><li>A conta do valor é sempre feita com o número <b>do cliente</b>.</li></ul><div class="box"><p>Agentes: Hormozi · Donald Miller · copy-squad · Pedro Sobral · Maquiavel</p></div>'+eu('09',760,'right:-30px'),img=nf('adv',4))
pg('<div class="k">Números com fonte</div><div class="cols" style="margin-top:50px"><div><div class="big">1,03<span style="font-size:80px">mi</span></div><p>habitantes em São Luís<br><span class="k">IBGE · Censo 2022</span></p></div><div><div class="big">1,3<span style="font-size:80px">mi</span></div><p>advogados no Brasil<br><span class="k">OAB Nacional · 2023</span></p></div></div><div style="margin-top:70px"><div class="big">400<span style="font-size:80px">mil+</span></div><p>cirurgiões-dentistas no Brasil<br><span class="k">CFO · 2024</span></p></div><p style="margin-top:50px;color:#8E8A82">Conferir a fonte no dia antes de pôr número numa peça.</p>',img=nf('dente',0))
pg('<div class="k">Funil</div><h2>Do anúncio<br>ao <em>contrato.</em></h2>'+''.join(f'<p style="margin:22px 0"><span class="n">0{i+1}</span>{s}</p>' for i,s in enumerate(['Tráfego Meta no raio de 3–8 km → isca Raio-X grátis do Instagram','WhatsApp: 3 perguntas (bairro, serviço, valor de 1 cliente)','Diagnóstico grátis de 20 min: a Conta do Cliente Perdido','Proposta no mesmo dia, na identidade do cliente','Fechamento: escassez real + Garantia de Entrega 30 dias','Quem não fechou: follow-up de 7 dias']))+'<div class="box"><p><b>Garantia de Entrega:</b> se no 1º mês não entregarmos todo o cronograma assinado, o mês seguinte é por nossa conta. Garante o trabalho, nunca o número de clientes.</p></div>','l',img=nf('barba',4))
N=[('Advogados','Autoridade Jurídica SLZ','Ser o nome lembrado<br>na sua <em>área.</em>',[('Perfil + Google Empresa reformados','R$ 1.500'),('12 conteúdos/mês no Provimento 205','R$ 2.400'),('Impulsionamento informativo local','R$ 1.200'),('Roteiro de WhatsApp ético','R$ 800'),('Relatório mensal','R$ 400'),('Bônus: checklist OAB por peça','R$ 500'),('Bônus: mini site bio','R$ 1.200'),('Bônus: dia de gravação trimestral','R$ 900')],'R$ 8.900','R$ 3.997','R$ 2.497','R$ 1.497','1 escritório por área do Direito','Se um contrato vale R$ 3.000 de honorários, 1 cliente novo paga o mês.',
'Oi, Dr. Marcos! Tudo bem? Sou o Lindson, aqui de São Luís.<br>Muito advogado bom vive só de indicação, e no mês fraco sente.<br>Eu ajudo escritórios a serem lembrados na sua área, dentro das regras da OAB.<br>Posso te mostrar como faria pro senhor?',
[('A OAB não deixa.','Deixa, desde 2021 (Prov. 205), se for informativo. O senhor aprova cada peça.'),('Está caro.','Um contrato da sua área paga o mês. Caro é a vaga ficar com o colega.'),('Vem por indicação.','Quem é indicado pesquisa seu nome. O que ele encontra hoje?'),('Não tenho tempo.','20 min de gravação por semana com roteiro. O resto é nosso.'),('Já tentei.','A diferença: cronograma assinado e garantia de entrega.'),('Vou pensar.','O que falta? A área fecha com o primeiro que confirmar.'),('Advocacia séria não posta.','Informativo e discreto. Seriedade também precisa ser vista.'),('Meu sobrinho faz.','Ele conhece o Provimento 205? O risco é do seu registro.')],
'Provimento 205/2021: conteúdo informativo, sem captação, sem preço, sem promessa de resultado e sem ostentação.'),
('Barbeiros','Cadeira Cheia','Terça cheia<br>como <em>sábado.</em>',[('Anúncio no raio de 3 km (dia fraco)','R$ 900'),('12 Reels/Stories por mês','R$ 1.200'),('Mensagem de retorno (30 dias)','R$ 500'),('Clube de Assinatura montado','R$ 800'),('Google Empresa do bairro','R$ 400'),('Bônus: agendamento no bio','R$ 300'),('Bônus: 3 roteiros de Reels','R$ 300')],'R$ 4.400','R$ 1.997','R$ 997','R$ 597','1 barbearia por bairro','Corte + barba de R$ 50: 20 clientes fixos pagam o mês. Ou 10 assinantes de R$ 100.',
'Fala, Ruan! Tudo certo? Aqui é o Lindson, de São Luís.<br>Sábado lotado e terça vazia: conheço bem essa agenda.<br>Eu ajudo barbearia a encher a cadeira no meio da semana, com anúncio no bairro e WhatsApp.<br>Quer que eu te mostre?',
[('Tá caro.','R$ 997 são 20 cortes. Quantas cadeiras vazias por semana?'),('Eu mesmo posto.','O anúncio leva quem ainda não te segue.'),('Impulsionei e nada.','Impulsionar post não é anúncio de raio com oferta do dia fraco.'),('Movimento é bom.','No sábado. E na terça?'),('Não sei se dá aqui.','Começa no plano de entrada; a garantia é de entrega.'),('Falar com o sócio.','Marca com ele junto, 15 min. A vaga do bairro não fica presa.'),('É tudo indicação.','E o cliente novo que chegou no bairro, quem indica?'),('Sem tempo de gravar.','3 vídeos de 15 s por semana, entre um corte e outro.')],
'Sem preço falso de “promoção relâmpago”: a oferta do dia fraco é real e fixa.'),
('Dentistas','Agenda de Avaliações','O orçamento parado<br><em>volta.</em>',[('Campanha de avaliação Meta + Google','R$ 1.800'),('12 conteúdos/mês por especialidade','R$ 2.400'),('Roteiro da recepção + follow-up 7 dias','R$ 1.200'),('Reativação da base (6 meses)','R$ 800'),('Relatório: avaliações e custo','R$ 400'),('Bônus: treino da recepcionista','R$ 600'),('Bônus: mini site da clínica','R$ 1.200'),('Bônus: checklist CFO por peça','R$ 400')],'R$ 8.800','R$ 4.497','R$ 2.497','R$ 1.497','1 clínica por especialidade por bairro','Implante particular de R$ 2.500–4.000: 1 fechado no mês paga o plano.',
'Oi, Dra. Paula! Tudo bem? Sou o Lindson, aqui de São Luís.<br>O paciente pede orçamento de implante, diz que vai pensar… e não volta mais.<br>Eu ajudo clínicas a ter paciente novo chegando toda semana, com anúncio e atendimento no WhatsApp.<br>Posso te mostrar como faria pra vocês?',
[('O CFO não deixa.','Deixa, com regras (Res. 196/2019). A senhora aprova cada peça.'),('Está caro.','Um implante paga o mês. Quantos orçamentos estão parados?'),('Já tenho agência.','Ela faz follow-up de orçamento e treina a recepção?'),('Só pedem preço.','A recepção tem roteiro que transforma preço em avaliação.'),('Agenda cheia.','De convênio ou particular? Troque hora barata por tratamento.'),('Vou pensar.','O que pesa mais: preço, tempo ou confiança?'),('Não gosto de aparecer.','Aparece o trabalho e a clínica. O rosto, só se quiser.'),('Já tentei tráfego.','O problema era o anúncio ou o WhatsApp depois? Cuidamos dos dois.')],
'Código de Ética Odontológica e Res. CFO 196/2019: sem antes e depois, sem promessa, sem preço como chamariz.')]
pers={'Advogados':'30–45 anos, escritório no Renascença, Calhau ou Centro. Audiência à tarde, WhatsApp à noite. Depende de indicação e vê colega aparecer mais. Valoriza seriedade e a ética da OAB. Está no Instagram, LinkedIn e Google.',
'Barbeiros':'24–38 anos, 2 a 4 cadeiras no Cohama, Turu, Cohab ou Vinhais. Corta o dia todo. Terça vazia, sábado lotado, cliente que some. Valoriza estilo e a rua. Vive no Instagram e WhatsApp.',
'Dentistas':'30–50 anos, clínica no Renascença, Ponta d\'Areia ou Calhau. Implante, lente, alinhador. Orçamento que “vai pensar”. Valoriza ética do CFO e imagem premium. Instagram e Google.'}
fu={'Advogados':['Exemplo de conteúdo da área','Manda 1 carrossel informativo','Indicação ou internet?','Dado OAB: 1,3 mi advogados','1 escritório por área: vaga aberta','Diagnóstico grátis de 20 min','Encerramento: “mande quero”'],
'Barbeiros':['Exemplo de anúncio de terça','Manda a arte (raio 3 km)','Quanto tá o corte + barba?','A conta da cadeira vazia','1 por bairro: ainda livre','Clube de Assinatura em 15 min','Encerramento: “manda bora”'],
'Dentistas':['Follow-up de orçamento de presente','Manda os 3 textos','Quantos orçamentos fecham?','Dado CFO: 400 mil+ dentistas','1 por especialidade no bairro','Diagnóstico de 20 min','Encerramento: “mande quero”']}
K={'Advogados':'adv','Barbeiros':'barba','Dentistas':'dente'};EU={'Advogados':'11','Barbeiros':'14','Dentistas':'15'}
for (nm,of,hd,st,tot,anc,pl,en,esc,conta,msg,obj,etica) in N:
  pg(f'<div class="gig">{of.split()[0]}</div>'+f'<div class="k">Nicho · {nm}</div><h1 style="margin-top:300px">{hd}</h1><p style="font-size:30px">Oferta <b style="color:#B8955A">“{of}”</b></p>'+eu(EU[nm],1000,'right:-230px'),'nich',nm,nf(K[nm],0))
  pg(f'<div class="k">Persona · {nm}</div><h2>Quem <em>compra.</em></h2><p style="font-size:30px">{pers[nm]}</p><div class="box"><p><b>Regra:</b> {etica}</p></div>','l',nm,nf(K[nm],1))
  pg(f'<div class="k">Stack de valor · {of}</div><h2>Tudo <em>isto.</em></h2><table>'+''.join(f'<tr><td>{a}</td><td>{b}</td></tr>' for a,b in st)+f'<tr class="t"><td>Valor percebido</td><td>{tot}/mês</td></tr></table>',t=nm,img=nf(K[nm],2))
  pg(f'<div class="k">Preço · {nm}</div><h2>Ancoragem<br>e <em>entrada.</em></h2><p style="color:#8E8A82;font-size:30px;text-decoration:line-through">Agência completa {anc}/mês</p><div class="big" style="font-size:150px;margin:20px 0">{pl}</div><p>por mês · contrato 6 meses</p><div class="box"><p>Plano de entrada: <b>{en}/mês</b></p><p>Escassez real: <b>{esc}</b> · fundador para os 3 primeiros até 15/12</p><p>Conta (hipótese): {conta}</p></div>',t=nm,img=nf(K[nm],3))
  pg(f'<div class="k">WhatsApp · Conexão → Dor → Desejo → Pergunta</div><h2>A primeira<br><em>mensagem.</em></h2><div class="msg">{msg}</div><div class="k" style="margin-top:44px">Follow-up 7 dias</div>'+''.join(f'<p style="margin:10px 0"><span class="n">D{i+1}</span>{s}</p>' for i,s in enumerate(fu[nm])),'l',nm,nf(K[nm],4))
  pg(f'<div class="k">8 objeções · {nm}</div><h2 style="font-size:60px">E quando<br>ele <em>disser…</em></h2>'+''.join(f'<p style="font-size:22px;margin:0 0 14px"><span class="n">{i+1:02d}</span><b>“{a}”</b> {b}</p>' for i,(a,b) in enumerate(obj)),t=nm,img=nf(K[nm],0))
pg('<div class="k">Reunião de 20 min</div><h2>O roteiro<br>do <em>sim.</em></h2>'+''.join(f'<p style="margin:16px 0"><span class="n">0{i+1}</span>{s}</p>' for i,s in enumerate(['Abertura: “hoje só quero entender seu negócio”','Situação: serviço, bairro, valor de 1 cliente','Dor: quanto custa um mês fraco?','Mostrar a busca no Google e no Instagram','Plano em 3 passos (StoryBrand)','A conta do valor com os números dele','Oferta + escassez + garantia','Fechar: “fechamos a vaga no seu nome?”'])),'l',img=nf('dente',1))
pg('<div class="k">Fechamento</div><h1 style="margin-top:260px;font-size:84px">Você é bom no que faz.<br>A cidade é que <em>não sabe.</em></h1><p style="font-size:30px">Eu faço São Luís te ver. Você atende.<br>Fechamos a vaga do seu bairro no seu nome?</p>'+eu('16',820,'right:-50px'),img=nf('barba',0))
html='<html><head><meta charset="utf-8"><style>'+css+'</style></head><body>'+''.join(f'<section class="p {c}">{h}{ft(i+1,t)}</section>' for i,(c,h,t) in enumerate(P))+'</body></html>'
(B/'gerador/pdf.html').write_text(html)
async def main():
  async with async_playwright() as p:
    b=await p.chromium.launch(); pgg=await b.new_page(viewport={'width':1080,'height':1350})
    await pgg.goto((B/'gerador/pdf.html').as_uri()); await pgg.wait_for_timeout(800)
    pass  # PDF final = páginas JPG (o PDF vetorial passava de 80 MB)
    (B/'paginas').mkdir(exist_ok=True)
    for i,el in enumerate(await pgg.query_selector_all('section')): await el.screenshot(path=str(B/f'paginas/{i+1:02d}.jpg'),quality=85,type='jpeg')
    await b.close()
asyncio.run(main())
from PIL import Image
ims=sorted((B/'paginas').glob('*.jpg')); c=6; w,h=360,450; r=-(-len(ims)//c)
f=Image.new('RGB',(c*w+(c+1)*20,r*h+(r+1)*20),'#1A1C20')
for i,p in enumerate(ims): f.paste(Image.open(p).resize((w,h)),(20+(i%c)*(w+20),20+(i//c)*(h+20)))
f.save(B/'folha.jpg',quality=88); print(len(ims),'paginas')
pp=[Image.open(x).convert('RGB') for x in ims]; pp[0].save(B/'estrategia-vendas-slz-3-nichos.pdf',save_all=True,append_images=pp[1:],resolution=144)
