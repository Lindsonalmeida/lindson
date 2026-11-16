# 30 Stories 1080x1920 v2 (conta Leandro, 16/11/2026), no padrão aprovado "Criativos Denis Bugatti 2026" (Behance 247742319):
# Lindson protagonista em cena cinematográfica com metáfora, luz de cinema, tipografia condensada gigante com 1 palavra neon, assinatura pequena.
# Gemini Imagem sem cota (429) em 16/11: cena = foto real (Unsplash) + recorte real do Lindson (recorte2.py) em camadas.
# Uso: python3 gerador/stories.py <pasta_recortes> <pasta_cenas> <pasta_fotos_nicho>
import sys, pathlib, asyncio
from PIL import Image, ImageOps
from playwright.async_api import async_playwright
B=pathlib.Path(__file__).resolve().parents[1]; R=B.parents[2]
ANTON=R/'agencia/marca-lindson/projeto-designer/pinterest/Anton-Regular.ttf'; F=R/'agencia/marca-holding/v2/fontes'
REC,CEN,NF=[pathlib.Path(a) for a in sys.argv[1:4]]; TMP=B/'gerador/_tmp'; TMP.mkdir(exist_ok=True)
U=lambda p: pathlib.Path(p).as_uri()
POKER='1511193311914-0346f16efe90'; PALCO='1503095396549-807759245b35'; XADREZ='1529699211952-734e80c4d42b'; CAVALOS='1586165368502-1bad197a6461'
LUVAS='1549719386-74dfcbf7dbed'; DINHEIRO='1580519542036-c47de6196ba5'; QUEDA='1611974789855-9c2a0a7236a3'; PROJETOR='1535016120720-40c646be5580'; NEON='1470225620780-dba8ba36b745'
NEONC={'adv':'#FFC94D','barba':'#FF3B3B','dente':'#36F1E0'}; COD={'adv':'ADV','barba':'BARBA','dente':'SORRISO'}
ORD={'adv':['07','08','09','10','11','12','13','14','15','16'],'barba':['16','15','14','13','12','11','10','09','08','07'],'dente':['11','12','13','14','15','16','07','08','09','10']}
# (cena, é_foto_do_nicho, kicker, linha1, PALAVRA NEON, linha3, apoio, layout)
S={'adv':[
 (PALCO,0,'Advogados · São Luís','Quem sobe','no palco','é lembrado','A cidade lembra de quem ela vê.','c'),
 ('1505664194779-8beaceb93744',1,'Indicação não basta','Ele pesquisa','seu nome','antes de ligar','O que ele encontra hoje?','l'),
 (CAVALOS,0,'1,3 milhão de advogados no Brasil (OAB, 2023)','No tabuleiro,','ninguém','espera você','Quem não aparece, não é lembrado.','r'),
 ('1589829545856-d10d557cf95f',1,'Provimento 205/2021','Aparecer','com ética','é permitido','Conteúdo informativo, sem captação. Você aprova cada peça.','c'),
 (PROJETOR,0,'Autoridade Jurídica SLZ','Sua área','em foco','toda semana','Perfil, Google, 12 conteúdos e impulsionamento informativo.','l'),
 (XADREZ,0,'Escassez real','1 escritório','por área','em São Luís','A vaga fica com o primeiro que confirmar.','r'),
 ('1450101499163-c8848c66ca85',1,'Seu tempo vale mais','Você grava','20 min','a gente faz o resto','Roteiro pronto, toda semana.','c'),
 ('1521791055366-0d553872125f',1,'Garantia de entrega','Não entregou?','o mês','é nosso','Se no 1º mês o cronograma assinado não for cumprido.','l'),
 (DINHEIRO,0,'Faça a conta com o seu número','Um contrato','paga','o mês','Exemplo: contrato de R$ 3.000 x plano de R$ 2.497. Hipótese, não promessa.','r'),
 ('1497366216548-37526070297c',1,'Raio-X grátis do seu Instagram','Mande','ADV','no WhatsApp','E receba o plano de 30 dias para o seu escritório.','c')],
'barba':[
 (LUVAS,0,'Barbearias · São Luís','Sábado lotado.','Terça','vazia?','Isso tem conserto.','c'),
 ('1622286342621-4bd786c2447c',1,'O cliente que some','Cortou uma vez','e sumiu','pra sempre?','A mensagem de retorno chama ele de volta.','l'),
 (CAVALOS,0,'Concorrência no bairro','Barbearia nova','abriu','na sua rua','Quem aparece mais, leva o cliente.','r'),
 ('1503951914875-452162b0f3f1',1,'Anúncio de raio','Só quem mora','a 3 km','vê você','Oferta do dia fraco para o bairro certo.','c'),
 (NEON,0,'Cadeira Cheia','Seu nome','aceso','no bairro','Anúncio, 12 Reels e Stories, Google e retorno de clientes.','l'),
 ('1585747860715-2ba37e788b70',1,'Escassez real','1 barbearia','por bairro','e só','Duas no mesmo bairro, uma rouba cliente da outra.','r'),
 (DINHEIRO,0,'Clube de assinatura','Renda','todo mês','chova ou faça sol','A gente monta preço, regra e arte.','c'),
 (PALCO,0,'Garantia de entrega','Não entregou?','o mês','é nosso','Se no 1º mês o cronograma não for cumprido.','l'),
 ('1621605815971-fbc98d665033',1,'Faça a conta com o seu preço','R$ 997 =','20 cortes','de R$ 50','Exemplo. Use o preço da sua barbearia.','r'),
 ('1599351431202-1e0f0137899a',1,'Fale comigo','Mande','BARBA','no WhatsApp','Raio-X grátis do seu Instagram + plano de 30 dias.','c')],
'dente':[
 (QUEDA,0,'Clínicas · São Luís','“Vou pensar.”','E sumiu','O orçamento parou aí?','Dá para trazer esse paciente de volta.','c'),
 ('1598256989800-fe5f95da9787',1,'Cadeira vazia','Terça vazia','não volta','nunca mais','Anúncio de avaliação no raio da clínica.','l'),
 (CAVALOS,0,'Mais de 400 mil dentistas no Brasil (CFO, 2024)','O paciente','escolhe','quem encontra','E em quem confia.','r'),
 ('1588776814546-1ffcf47267a5',1,'Follow-up de orçamento','7 dias','depois','ainda dá','Recepção com roteiro: preço vira avaliação.','c'),
 (PROJETOR,0,'Agenda de Avaliações','Sua clínica','em foco','no bairro','Campanha, 12 conteúdos, roteiro da recepção e reativação.','l'),
 (XADREZ,0,'Escassez real','1 clínica','por bairro','por especialidade','Não anuncio dois implantodontistas no mesmo bairro.','r'),
 ('1629909613654-28e377c37b09',1,'Regras do CFO','Sem antes e depois','sem promessa','sem preço chamariz','Cada peça passa no checklist e você aprova.','c'),
 (PALCO,0,'Garantia de entrega','Não entregou?','o mês','é nosso','Se no 1º mês o cronograma não for cumprido.','l'),
 (DINHEIRO,0,'Faça a conta com o seu preço','1 implante','paga','o mês','Exemplo: implante de R$ 2.500 x plano de R$ 2.497. Hipótese.','r'),
 ('1606811971618-4486d14f3f99',1,'Fale comigo','Mande','SORRISO','no WhatsApp','Raio-X grátis do seu Instagram + plano de 30 dias.','c')]}
css=f"""@font-face{{font-family:Fr;src:url('{U(F/'Fraunces-Regular.ttf')}')}}@font-face{{font-family:FrI;src:url('{U(F/'Fraunces-Italic-latin.woff2')}')}}@font-face{{font-family:A;src:url('{U(ANTON)}')}}@font-face{{font-family:IT;src:url('{U(F/'InterTight-Medium.ttf')}')}}@font-face{{font-family:ITS;src:url('{U(F/'InterTight-SemiBold.ttf')}')}}@font-face{{font-family:JB;src:url('{U(F/'JetBrainsMono-Medium.ttf')}')}}
*{{margin:0;box-sizing:border-box}}body{{width:1080px;height:1920px;overflow:hidden;background:#07080A;color:#fff;font-family:IT;position:relative}}
.L{{position:absolute}}.bg{{inset:-30px;background-size:cover;background-position:center;filter:saturate(.8) contrast(1.15) brightness(.62)}}
.vig{{inset:0;background:radial-gradient(120% 80% at 50% 40%,transparent 35%,rgba(0,0,0,.85))}}
.base{{left:0;right:0;bottom:0;height:1100px;background:linear-gradient(180deg,transparent,rgba(7,8,10,.82) 45%,#07080A 80%)}}
.topo{{left:0;right:0;top:0;height:420px;background:linear-gradient(rgba(7,8,10,.85),transparent)}}
.fog{{left:-200px;right:-200px;bottom:520px;height:500px;background:radial-gradient(50% 50% at 50% 50%,rgba(255,255,255,.10),transparent);filter:blur(30px)}}
.grao{{inset:0;opacity:.16;mix-blend-mode:overlay;background:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='3'/></filter><rect width='300' height='300' filter='url(%23n)'/></svg>")}}
.som{{bottom:-20px;height:160px;border-radius:50%;background:rgba(0,0,0,.85);filter:blur(40px)}}
.eu{{bottom:0}}
.t{{left:60px;right:60px;text-align:center;font-family:A;text-transform:uppercase;line-height:.9;letter-spacing:-.005em;text-shadow:0 6px 30px rgba(0,0,0,.7)}}
.k{{font-family:JB;font-size:24px;letter-spacing:.18em;text-transform:uppercase;color:rgba(255,255,255,.8)}}
.ass{{left:0;right:0;bottom:150px;text-align:center;font-family:JB;font-size:20px;letter-spacing:.3em;color:rgba(255,255,255,.55)}}
.cta{{left:50%;transform:translateX(-50%);bottom:215px;padding:20px 34px;border-radius:50px;font-family:ITS;font-size:30px;color:#07080A;white-space:nowrap}}
"""
def eu(n,i,lay):
  im=Image.open(REC/f'c{ORD[n][i]}.png')
  if n!='adv': im=ImageOps.mirror(im)
  out=TMP/f'eu-{n}-{i}.png'; im.save(out); ar=im.width/im.height
  h={'c':1180,'l':1120,'r':1120}[lay]; w=int(h*ar); x={'c':540-w//2,'l':-60,'r':1140-w}[lay]
  cor=NEONC[n]
  return f'<div class="L som" style="left:{x+40}px;width:{w-80}px"></div><img class="L eu" src="{U(out)}" style="left:{x}px;height:{h}px;filter:drop-shadow(0 0 2px {cor}55) drop-shadow({"-" if lay!="l" else ""}10px 0 18px {cor}33) drop-shadow(0 40px 50px rgba(0,0,0,.7))">'
GEM=B/'stories/cenas-gemini'  # imagens geradas pelo Lindson no Gemini: cenas-gemini/<nicho>/NN.jpg (9:16, sem texto)
def fundo(n,i,src,lay,warm=False):
  g=GEM/n/f'{i+1:02d}.jpg'
  if g.exists(): return f'<div class="L" style="inset:0;background:url({U(g)}) center/cover"></div>', True
  f='sepia(.35) saturate(.9) brightness(.62) contrast(1.1)' if warm else ''
  return f'<div class="L bg" style="background-image:url({U(src)});{("filter:"+f) if f else ""}"></div>', False
def editorial(n,i):
  cena,nicho,k,l1,neon,l3,apoio,lay=S[n][i]; src=(NF if nicho else CEN)/f'{cena}.jpg'
  bg,gem=fundo(n,i,src,lay,True); ouro='#D9B26A'
  labels=''.join(f'<span>{x}</span>' for x in ['Autoridade','Visibilidade','São Luís'])
  giant=neon.split()[0]
  body=(bg+'<div class="L" style="inset:0;background:radial-gradient(700px 900px at 75% 30%,rgba(255,170,80,.28),transparent 70%);mix-blend-mode:screen"></div><div class="L vig"></div><div class="L topo" style="height:900px;background:linear-gradient(rgba(12,9,6,.9),rgba(12,9,6,.4) 60%,transparent)"></div>'
   +f'<div class="L" style="left:-40px;right:-40px;top:900px;text-align:center;font-family:FrI;font-size:{min(460,int(1400/max(3,len(giant))))}px;line-height:1;color:rgba(239,220,190,.13);white-space:nowrap">{giant}</div>'
   +('' if gem else eu(n,i,lay))+'<div class="L base" style="height:700px;background:linear-gradient(180deg,transparent,rgba(12,9,6,.75) 55%,#0c0906)"></div>'
   +f'<div class="L" style="top:150px;left:90px;right:90px;display:flex;justify-content:space-between;font-family:Fr;font-size:22px;letter-spacing:.25em;text-transform:uppercase;color:rgba(239,234,225,.6)">{labels}</div>'
   +f'<div class="L" style="top:290px;left:80px;right:80px;text-align:center;font-family:Fr;text-transform:uppercase;font-size:84px;line-height:1.02;color:#F3EBDD;text-shadow:0 4px 30px rgba(0,0,0,.6)">{l1}<br><span style="font-family:FrI;text-transform:none;color:{ouro};font-size:104px">{neon}</span><br>{l3}</div>'
   +f'<div class="L" style="top:690px;left:150px;right:150px;text-align:center;font-size:30px;line-height:1.4;color:rgba(243,235,221,.85)">{apoio}</div>'
   +f'<div class="L" style="left:50%;transform:translateX(-50%);bottom:230px;border:1.5px solid {ouro};color:#F3EBDD;padding:20px 40px;font-family:Fr;font-size:26px;letter-spacing:.18em;text-transform:uppercase;white-space:nowrap;background:rgba(12,9,6,.45)">Mande {COD[n]} no WhatsApp</div>'
   +f'<div class="L ass">{k}</div><div class="L grao"></div>')
  return f'<html><head><meta charset="utf-8"><style>{css}</style></head><body>{body}</body></html>'
def story(n,i):
  if i%2==1: return editorial(n,i)
  cena,nicho,k,l1,neon,l3,apoio,lay=S[n][i]; cor=NEONC[n]
  src=(NF if nicho else CEN)/f'{cena}.jpg'
  luz=f'<div class="L" style="inset:0;background:radial-gradient(600px 900px at {"80%" if lay!="r" else "20%"} 25%,{cor}30,transparent 70%);mix-blend-mode:screen"></div>'
  top=1060
  txt=(f'<div class="L t" style="top:{top}px"><div class="k" style="margin-bottom:22px">{k}</div>'
       f'<div style="font-size:{118 if len(l1)<13 else 96}px">{l1}</div>'
       f'<div style="font-size:{200 if len(neon)<9 else 150}px;color:{cor};text-shadow:0 0 18px {cor},0 0 60px {cor}aa,0 0 120px {cor}66">{neon}</div>'
       f'<div style="font-size:{104 if len(l3)<14 else 76}px">{l3}</div></div>'
       f'<div class="L" style="left:90px;right:90px;bottom:320px;text-align:center;font-size:28px;line-height:1.35;color:rgba(255,255,255,.85)">{apoio}</div>')
  cta=f'<div class="L cta" style="background:{cor};box-shadow:0 0 30px {cor}88">Mande {COD[n]} no WhatsApp →</div>' if i!=0 else f'<div class="L cta" style="background:#fff">Responda este story →</div>'
  bg,gem=fundo(n,i,src,lay)
  body=(bg+f'{luz}<div class="L vig"></div><div class="L topo"></div><div class="L fog"></div>'
        +('' if gem else eu(n,i,lay))+'<div class="L base" style="height:900px"></div>'+txt+cta+
        '<div class="L ass">LINDSON ALMEIDA · AL KÁNTARA</div><div class="L grao"></div>')
  return f'<html><head><meta charset="utf-8"><style>{css}</style></head><body>{body}</body></html>'
async def main():
  async with async_playwright() as p:
    b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':1080,'height':1920})
    for n in S:
      d=B/'stories'/n; d.mkdir(parents=True,exist_ok=True)
      for i in range(10):
        h=TMP/f'{n}{i}.html'; h.write_text(story(n,i)); await pg.goto(h.as_uri()); await pg.wait_for_timeout(250)
        await pg.screenshot(path=str(d/f'{i+1:02d}.png'))
      ims=[Image.open(d/f'{i+1:02d}.png').convert('RGB').resize((324,576)) for i in range(10)]
      f=Image.new('RGB',(5*324+6*20,2*576+3*20),'#111')
      for k,im in enumerate(ims): f.paste(im,(20+(k%5)*344,20+(k//5)*596))
      f.save(d/'folha.jpg',quality=88)
    await b.close()
asyncio.run(main())
