# Capas de Reels do curso v6 (10/11/2026, conta Zuleide, designer grafico).
# Regra do Lindson: "a identidade sim, mas as composicoes nao podem ser iguais, senao cansa visualmente".
# Mantem da v5: verde/dourado/creme, Instrument Serif + Inter Tight, o paragrafo, grao, vinheta, cantos com numeracao, vidro fosco, rim light, as mesmas fotos recortadas.
# Patamar Rafael x Tiago: cada um tem 1 capa com rosto 460, 1 com 260 e 2 com 330 (nenhum maior que o outro na serie).
# Composicao de cada capa e a referencia copiada:
#  01 Koto "Where London Meets" (UK): pessoa a direita, palavra gigante empilhada na vertical a esquerda
#  02 R1 Behance 222952139 Key Visual Experts (BR): close de rosto cortado pela borda, tema embaixo em faixa
#  03 R3 Behance 166179777 Social Media Advocacia (BR): meio corpo com documento juridico em primeiro plano
#  04 Studio Dumbar (NL): tela dividida em diagonal, bloco de cor dourado com palavra
#  05 Harvard Law Review (US) / The Guardian Law (UK): moldura de jornal, cabecalho, colunas, foto em caixa
#  06 R2 Behance 144495005 Dieggo Bruno Advogados (BR): selo/carimbo gigante, professor menor ao lado
#  07 Pentagram (US/UK) cartazes tipograficos: artigo de lei gigante ao fundo
#  08 R1 Key Visual Experts (BR): composicao centrada com aura de luz e feixes
import json,cv2,numpy as np
from PIL import Image
V,O,CR,OE='#123528','#C8A96B','#F3EEE3','#8A6A30'
G='linear-gradient(180deg,#FFF4D2 0%,#E9CF8E 30%,#C8A96B 55%,#7A5A26 100%)'
GE='linear-gradient(180deg,#B8924F,#8A6A30 50%,#3E2E12)'
HC=cv2.CascadeClassifier('/root/.modelos/haar.xml')
def rosto(path):
  im=Image.open(path);b=Image.new('RGBA',im.size,(150,150,150,255));b.alpha_composite(im.convert('RGBA'));g=cv2.cvtColor(np.asarray(b.convert('RGB')),cv2.COLOR_RGB2GRAY)
  r=sorted(HC.detectMultiScale(g,1.1,6,minSize=(100,100)).tolist(),key=lambda x:-x[2])[0];return im.size,r
def cut(f,face,cx,top,extra=''):
  (w,h),(x,y,fw,fh)=rosto(f);s=face/fw
  return f'<img class="pes" src="{f}" style="width:{w*s:.0f}px;left:{cx-(x+fw/2)*s:.0f}px;top:{top-y*s:.0f}px;{extra}">'
NOME={'rafael':'Prof. Rafael Araújo Veras','tiago':'Prof. Tiago Azevedo'}
def selo(i,x,y,w,rot,txt='PROCESSO LEGISLATIVO ✦ REGIMENTO EM 1 MINUTO ✦',mid='§',cls=''):
  return f'<svg class="selo {cls}" style="left:{x}px;top:{y}px;width:{w}px;transform:rotate({rot}deg)" viewBox="0 0 200 200"><defs><path id="cc{i}{x}" d="M100,100 m-76,0 a76,76 0 1,1 152,0 a76,76 0 1,1 -152,0"/></defs><circle cx="100" cy="100" r="96"/><circle cx="100" cy="100" r="58"/><text><textPath href="#cc{i}{x}">{txt}</textPath></text><text x="100" y="124" text-anchor="middle" class="sg">{mid}</text></svg>'
def H(t,h,cls='',st=''): return f'<h1 class="ha {cls}" style="{st}">{t.replace(h,f"<em>{h}</em>")}</h1>'
def vidro(i,tema,st): return f'<div class="vidro" style="{st}"><small>AULA {i:02d} · TEMA</small>{tema}</div>'
def scene(c,op=None): return f'<div class="scene" style="background-image:url(banco/{c});{f"opacity:{op}" if op else ""}"></div>' if c else '<div class="hemi"></div>'
SW='<div class="sw" style="{}"><span></span>assista ao Reels ↓</div>'.format
def L(i,p,f,t,h,back,tema,cena):
  if i==1:  # Koto: palavra vertical a esquerda, professor a direita
    return scene(cena)+f'''<div class="tint"></div><div class="halo" style="left:390px;top:300px"></div>
    <div class="vert">{back}</div><div class="vert v2">{back}</div>
    {cut(f,330,690,520)}<div class="flare" style="top:1060px;left:300px"></div>
    {selo(i,820,1030,170,14)}<div class="fade"></div>
    {vidro(i,tema,'left:300px;top:1010px')}{H(t,h,'',"bottom:400px;left:250px;font-size:80px")}{SW('bottom:330px;left:250px')}'''
  if i==2:  # close de rosto, tema embaixo
    return scene(cena,.25)+f'''<div class="tint"></div><div class="halo" style="left:90px;top:120px;width:900px;height:900px"></div>
    {cut(f,460,540,330)}<div class="fade" style="top:960px"></div>
    <div class="faixa"><span>§ AULA 02</span>{back}<span>REGIMENTO</span></div>
    {H(t,h,'cen',"bottom:360px;text-align:center;font-size:100px")}{SW('bottom:290px;left:0;right:0;justify-content:center')}'''
  if i==3:  # meio corpo + documento em primeiro plano
    return scene(cena)+f'''<div class="tint"></div><div class="feixe"></div><div class="halo" style="left:240px;top:300px"></div>
    <div class="back" style="top:300px">{back}</div>
    {cut(f,330,600,470)}
    <div class="docg"><b>§ Questão de Ordem</b><p>Art. 151 · Regimento Interno</p><i></i><i></i><i style="width:70%"></i><i></i><i style="width:55%"></i>
    {selo(i,330,190,190,-14,'DEFERIDA ✦ PLENÁRIO ✦ DEFERIDA ✦ PLENÁRIO ✦','✓','sepia')}</div>
    {H(t,h,'',"bottom:430px;right:380px;font-size:84px")}{SW('bottom:350px')}'''
  if i==4:  # diagonal dividida
    return f'''<div class="diag"></div><div class="diag2"></div>{scene(cena)}
    <div class="dword">{back}</div>
    {cut(f,330,750,520)}<div class="fade" style="top:1250px;background:none"></div>
    {vidro(i,tema,'left:84px;top:1000px')}
    <div class="hbox">{H(t,h,'',"position:static;font-size:86px")}</div>{SW('bottom:320px;left:auto;right:84px')}'''
  if i==5:  # jornal
    return scene(cena,.3)+f'''<div class="jornal"><div class="mast">O Diário do Plenário</div><div class="linha"><span>Edição 05</span><span>São Luís · Maranhão</span><span>§ Processo Legislativo</span></div>
    <div class="caixa">{cut(f,260,250,150)}<div class="cap">{NOME[p]} explica no Reels</div></div>
    <div class="cols"><b>MOÇÃO</b><i></i><i></i><i style="width:80%"></i><i></i><i></i><i style="width:60%"></i><i></i><i></i><i style="width:85%"></i><i></i><i style="width:40%"></i></div>
    {H(t,h,'jn',"")}<div class="lead">Manifesta a posição da Câmara. Não vira lei.</div></div>
    {selo(i,770,1300,200,-10,'EXTRA ✦ EXTRA ✦ EXTRA ✦ EXTRA ✦ EXTRA ✦','05')}'''
  if i==6:  # carimbo gigante + professor menor
    return scene(cena)+f'''<div class="tint"></div>
    {selo(i,-120,380,900,-12,'PROCEDIMENTO ✦ ABREVIADO ✦ CONCLUSIVO ✦ RITO ✦','rito','gig')}
    <div class="halo" style="left:520px;top:620px;width:560px;height:560px"></div>
    {cut(f,260,790,760)}<div class="fade" style="top:1180px"></div>
    {vidro(i,tema,'left:84px;top:1110px')}{H(t,h,'',"bottom:430px;font-size:88px")}{SW('bottom:350px')}'''
  if i==7:  # artigo de lei gigante
    return scene(cena)+f'''<div class="tint"></div><div class="feixe"></div>
    <div class="art">Art.<br>59</div><div class="art a2">Art.<br>59</div>
    <div class="halo" style="left:140px;top:280px;width:820px;height:820px"></div>
    {cut(f,460,650,470)}<div class="flare" style="top:1150px"></div><div class="fade" style="top:1130px"></div>
    <div class="cf">Constituição Federal · Art. 59: <b>sete espécies normativas</b></div>
    {H(t,h,'',"bottom:430px;font-size:90px")}{SW('bottom:350px')}'''
  if i==8:  # centrada com aura
    return scene(cena,.2)+f'''<div class="tint"></div><div class="raios"></div><div class="feixe" style="left:180px"></div>
    <div class="aura"></div><div class="anel"></div><div class="anel a2"></div>
    {cut(f,330,540,560)}<div class="flare" style="top:1080px"></div><div class="fade" style="top:1110px"></div>
    <div class="ttop">{back}</div>
    {H(t,h,'cen',"bottom:430px;text-align:center;font-size:94px")}{SW('bottom:350px;left:0;right:0;justify-content:center')}'''
def capa(i,p,f,t,h,back,tema,cena,claro):
  bg=CR if claro else V
  return f'''<div class="c {'claro' if claro else 'escuro'} L{i}" style="background:{bg}">{L(i,p,f,t,h,back,tema,cena)}
  <div class="tag"><b>§</b> PROCESSO LEGISLATIVO <span>·</span> {NOME[p]}</div><div class="num">{i:02d}<small>/08</small></div>
  <div class="k k1"></div><div class="k k2"></div><div class="k k3"></div><div class="k k4"></div>
  <div class="vig"></div><div class="grao"></div></div>'''
capas=[
 ('01-rafael-emenda','rafael','rafael-recorte.png','Vereador pode aumentar despesa por emenda?','despesa','emenda','Emenda','p7054510.jpg',0),
 ('02-tiago-portaria','tiago','tiago-recorte.png','Portaria serve para quê?','para quê?','portaria','Portaria','p34066105.jpg',1),
 ('03-rafael-questao-de-ordem','rafael','rafael-mw6s8tkztximaf.png','O que é questão de ordem?','questão de ordem?','ordem','Questão de ordem','p32266781.jpg',0),
 ('04-tiago-sancionar','tiago','tiago-mw6rwc95u97ywi.png','Prefeito pode sancionar sem falar nada?','sem falar nada?','sanção','Sanção tácita',None,1),
 ('05-rafael-mocao','rafael','rafael-mw6s8xu06d52o9.png','Moção não é projeto de lei','não é','moção','Moção','p36207471.jpg',0),
 ('06-tiago-procedimento','tiago','tiago-mw6rwf9inhnxgb.png','O que é procedimento abreviado ou conclusivo?','abreviado ou conclusivo?','rito','Rito abreviado',None,1),
 ('07-rafael-fases','rafael','rafael-mw6s8vb8cmafyz.png','Quais são as fases do processo legislativo?','fases','fases','Fases','p35013248.jpg',0),
 ('08-tiago-urgencia','tiago','tiago-mw6rwhdqij2dph.png','O prefeito pode pedir urgência em qualquer projeto?','urgência','urgência','Urgência','p7224866.jpg',1),
]
css=open('estilo.css').read().replace('$G',G).replace('$GE',GE).replace('$V',V).replace('$O',O).replace('$CR',CR).replace('$OE',OE)
out=[(n,capa(k+1,*a)) for k,(n,*a) in enumerate(capas)]
open('pecas.html','w').write('<html><head><meta charset=utf-8><style>'+css+'</style></head><body>'+''.join(f'<div id="{n}">{h}</div>' for n,h in out)+'</body></html>')
json.dump([n for n,_ in out],open('nomes.json','w'))
