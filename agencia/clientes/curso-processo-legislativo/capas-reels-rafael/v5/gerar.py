# Capas de Reels do curso v5 (10/11/2026, conta Zuleide, designer grafico): camadas e glamour.
# Copia: R1 Behance 222952139 "Key Visual Experts" (Alex Paimel/A Manada, BR): aura de luz atras do expert, rim light, feixes e particulas;
#        R2 Behance 144495005 "Dieggo Bruno Advogados" (Isaque dsgn, BR): preto+dourado, cena real quente ao fundo, manchete com tarja dourada, selo do escritorio no rodape;
#        R3 Behance 166179777 "Social Media Advocacia" (Igor Vinicius, BR): palavra serifada gigante cortada atras da pessoa, objeto juridico em bronze, textura.
# + acabamento aprovado da marca do Lindson: vidro fosco, cantos de corte com numeracao, vinheta, grao, letra gigante com luz em degrade e sombra projetada, brilho anamorfico.
import json,cv2,numpy as np
from PIL import Image
V,O,CR,CA,OE='#123528','#C8A96B','#F3EEE3','#0B2219','#8A6A30'
HC=cv2.CascadeClassifier('/root/.modelos/haar.xml')
def rosto(path):
  im=Image.open(path);b=Image.new('RGBA',im.size,(150,150,150,255));b.alpha_composite(im.convert('RGBA'));g=cv2.cvtColor(np.asarray(b.convert('RGB')),cv2.COLOR_RGB2GRAY)
  r=sorted(HC.detectMultiScale(g,1.1,6,minSize=(100,100)).tolist(),key=lambda x:-x[2])[0];return im.size,r
FACE,TOP=330,470   # mesmo patamar: rosto 330 px, topo da cabeca na mesma linha para Rafael e Tiago
def cut(f,cx=540):
  (w,h),(x,y,fw,fh)=rosto(f);s=FACE/fw
  return f'<img class="pes" src="{f}" style="width:{w*s:.0f}px;left:{cx-(x+fw/2)*s:.0f}px;top:{TOP-y*s:.0f}px">'
NOME={'rafael':'Prof. Rafael Araújo Veras','tiago':'Prof. Tiago Azevedo'}
def hemi():  # cena desenhada: bancadas do plenario em arco (sem foto de banco)
  return '<div class="hemi"></div>'
def capa(i,p,f,t,h,back,tema,cena,claro):
  bg=CR if claro else V; fg=V if claro else CR; ac=OE if claro else O
  sc=f'<div class="scene" style="background-image:url(banco/{cena})"></div>' if cena else hemi()
  return f'''<div class="c {'claro' if claro else 'escuro'}" style="background:{bg}">
  {sc}<div class="tint"></div>
  <div class="feixe"></div><div class="halo"></div>
  <div class="back">{back}</div><div class="back2">{back}</div>
  <div class="doc"><b>§ {i:02d}</b><i></i><i></i><i style="width:60%"></i><i></i><i style="width:75%"></i><i></i><i style="width:40%"></i></div>
  <div class="secg">§</div>
  {cut(f)}
  <div class="flare"></div>
  <svg class="selo" viewBox="0 0 200 200"><defs><path id="cc{i}" d="M100,100 m-76,0 a76,76 0 1,1 152,0 a76,76 0 1,1 -152,0"/></defs><circle cx="100" cy="100" r="96" /><circle cx="100" cy="100" r="58"/><text><textPath href="#cc{i}">PROCESSO LEGISLATIVO ✦ REGIMENTO EM 1 MINUTO ✦</textPath></text><text x="100" y="122" text-anchor="middle" class="sg">§</text></svg>
  <div class="tag"><b>§</b> PROCESSO LEGISLATIVO <span>·</span> {NOME[p]}</div>
  <div class="num">{i:02d}<small>/08</small></div>
  <div class="k k1"></div><div class="k k2"></div><div class="k k3"></div><div class="k k4"></div>
  <div class="fade"></div>
  <div class="vidro"><small>AULA {i:02d} · TEMA</small>{tema}</div>
  <h1 class="ha">{t.replace(h,f'<em>{h}</em>')}</h1>
  <div class="sw"><span></span>assista ao Reels ↓</div>
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
G='linear-gradient(180deg,#FFF4D2 0%,#E9CF8E 30%,#C8A96B 55%,#7A5A26 100%)'
css=f'''@import url('https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Inter+Tight:wght@400;600;800;900&display=swap');
body{{margin:0}}.c{{width:1080px;height:1920px;position:relative;overflow:hidden;font-family:'Inter Tight'}}
.scene{{position:absolute;inset:0;background-size:cover;background-position:center;filter:grayscale(1) contrast(1.2);opacity:.55;mix-blend-mode:luminosity}}
.escuro .scene{{mix-blend-mode:soft-light;opacity:.9}}.claro .scene{{mix-blend-mode:multiply;opacity:.35;filter:grayscale(1) sepia(.5) contrast(1.1)}}
.hemi{{position:absolute;left:-300px;right:-300px;top:900px;height:1400px;border-radius:50%;background:repeating-radial-gradient(circle at 50% 50%,transparent 0 46px,rgba(200,169,107,.22) 46px 50px,transparent 50px 92px);opacity:.9}}
.tint{{position:absolute;inset:0;background:radial-gradient(ellipse 70% 45% at 50% 38%,transparent,rgba(11,34,25,.75))}}.claro .tint{{background:radial-gradient(ellipse 70% 45% at 50% 38%,transparent,rgba(170,140,90,.35))}}
.feixe{{position:absolute;left:180px;top:-200px;width:720px;height:1500px;background:conic-gradient(from 160deg at 50% 0%,transparent 0deg,rgba(255,230,170,.22) 12deg,transparent 26deg,rgba(255,230,170,.14) 34deg,transparent 46deg);filter:blur(8px)}}
.halo{{position:absolute;left:190px;top:330px;width:700px;height:700px;border-radius:50%;background:radial-gradient(circle,rgba(240,205,130,.75) 0%,rgba(200,169,107,.35) 35%,transparent 68%);filter:blur(10px)}}
.claro .halo{{background:radial-gradient(circle,rgba(255,255,255,.95) 0%,rgba(200,169,107,.45) 40%,transparent 70%)}}
.back,.back2{{position:absolute;top:330px;left:-40px;right:-40px;text-align:center;font:italic 340px/1 'Instrument Serif';letter-spacing:-.03em;white-space:nowrap}}
.back{{background:{G};-webkit-background-clip:text;color:transparent;filter:drop-shadow(0 28px 26px rgba(0,0,0,.55))}}
.claro .back{{background:linear-gradient(180deg,#B8924F,#8A6A30 50%,#3E2E12);-webkit-background-clip:text;filter:drop-shadow(0 26px 20px rgba(60,40,10,.35))}}
.back2{{color:transparent;-webkit-text-stroke:2px rgba(232,205,142,.45);transform:translate(14px,-10px)}}
.doc{{position:absolute;right:46px;top:640px;width:250px;height:330px;background:linear-gradient(160deg,#FBF6EA,#E8DCC0);transform:rotate(9deg);box-shadow:-20px 30px 50px rgba(0,0,0,.45);padding:26px 24px;box-sizing:border-box}}
.doc b{{display:block;font:italic 44px 'Instrument Serif';color:{OE};margin-bottom:14px;border-bottom:2px solid {O};padding-bottom:8px}}.doc i{{display:block;height:9px;background:#CDBF9F;margin:14px 0;width:100%}}
.secg{{position:absolute;left:30px;top:700px;font:italic 420px/1 'Instrument Serif';background:{G};-webkit-background-clip:text;color:transparent;opacity:.85;filter:drop-shadow(-6px 10px 0 rgba(0,0,0,.35)) drop-shadow(2px -2px 0 rgba(255,244,210,.5))}}
.pes{{position:absolute;z-index:5;-webkit-mask-image:linear-gradient(#000 72%,transparent 95%);filter:drop-shadow(0 0 2px rgba(255,236,190,.95)) drop-shadow(0 0 22px rgba(224,190,120,.55)) drop-shadow(-34px 40px 50px rgba(0,0,0,.6))}}
.flare{{position:absolute;z-index:6;left:-100px;right:-100px;top:1000px;height:6px;background:linear-gradient(90deg,transparent,rgba(255,236,190,.0) 20%,rgba(255,240,200,.95) 50%,rgba(255,236,190,0) 80%,transparent);filter:blur(1.5px);box-shadow:0 0 30px 8px rgba(240,205,130,.35)}}
.selo{{position:absolute;z-index:7;left:70px;top:1000px;width:190px;transform:rotate(-12deg);filter:drop-shadow(0 12px 18px rgba(0,0,0,.45))}}
.selo circle{{fill:rgba(18,53,40,.55);stroke:{O};stroke-width:3}}.selo circle+circle{{fill:none;stroke-dasharray:4 5}}.selo text{{font:700 13.5px 'Inter Tight';letter-spacing:.17em;fill:#EBD59E}}.selo .sg{{font:italic 70px 'Instrument Serif';fill:#EBD59E;letter-spacing:0}}
.tag{{position:absolute;z-index:8;top:296px;left:84px;right:84px;font:600 24px 'Inter Tight';letter-spacing:.14em;color:#EBD59E}}.tag b{{font:italic 38px 'Instrument Serif';margin-right:6px}}.tag span{{opacity:.5}}.claro .tag{{color:{OE}}}
.num{{position:absolute;z-index:8;top:282px;right:84px;font:italic 64px/1 'Instrument Serif';color:#EBD59E}}.num small{{font:600 20px 'Inter Tight';letter-spacing:.1em;opacity:.6}}.claro .num{{color:{OE}}}
.k{{position:absolute;z-index:8;width:44px;height:44px;border:0 solid {O}}}.k1{{top:250px;left:40px;border-top-width:3px;border-left-width:3px}}.k2{{top:250px;right:40px;border-top-width:3px;border-right-width:3px}}.k3{{bottom:250px;left:40px;border-bottom-width:3px;border-left-width:3px}}.k4{{bottom:250px;right:40px;border-bottom-width:3px;border-right-width:3px}}
.fade{{position:absolute;z-index:6;left:0;right:0;top:1080px;bottom:0;background:linear-gradient(rgba(18,53,40,0),{V} 42%)}}.claro .fade{{background:linear-gradient(rgba(243,238,227,0),{CR} 42%)}}
.vidro{{position:absolute;z-index:9;right:84px;top:1040px;padding:18px 26px;border-radius:18px;background:rgba(255,255,255,.12);backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);border:1.5px solid rgba(235,213,158,.6);box-shadow:inset 0 1px 0 rgba(255,255,255,.4),0 18px 40px rgba(0,0,0,.35);font:italic 50px/1 'Instrument Serif';color:#FFF4D2}}
.vidro small{{display:block;font:700 16px 'Inter Tight';letter-spacing:.2em;color:#EBD59E;margin-bottom:8px}}.claro .vidro{{background:rgba(18,53,40,.55);}}
.ha{{position:absolute;z-index:9;left:84px;right:84px;bottom:400px;margin:0;font:900 92px/1 'Inter Tight';letter-spacing:-.03em;color:{CR};text-shadow:0 6px 24px rgba(0,0,0,.35)}}.claro .ha{{color:{V};text-shadow:none}}
.ha em{{font:italic 400 110px/1 'Instrument Serif';background:{G};-webkit-background-clip:text;color:transparent;padding-right:6px}}.claro .ha em{{background:linear-gradient(180deg,#B8924F,#7A5A26);-webkit-background-clip:text}}
.sw{{position:absolute;z-index:9;left:84px;bottom:318px;font:700 24px 'Inter Tight';letter-spacing:.16em;text-transform:uppercase;color:#EBD59E;display:flex;align-items:center;gap:16px}}.sw span{{width:90px;height:3px;background:{G}}}.claro .sw{{color:{OE}}}
.vig{{position:absolute;inset:0;z-index:10;background:radial-gradient(ellipse at 50% 45%,transparent 55%,rgba(0,0,0,.45));pointer-events:none}}.claro .vig{{background:radial-gradient(ellipse at 50% 45%,transparent 60%,rgba(90,60,20,.25))}}
.grao{{position:absolute;inset:0;z-index:11;opacity:.09;mix-blend-mode:overlay;background:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='220' height='220'%3E%3Cfilter id='n'%3E%3CfeTurbulence baseFrequency='.85' numOctaves='2'/%3E%3C/filter%3E%3Crect width='220' height='220' filter='url(%23n)'/%3E%3C/svg%3E")}}'''
out=[(n,capa(k+1,*a)) for k,(n,*a) in enumerate(capas)]
open('pecas.html','w').write('<html><head><meta charset=utf-8><style>'+css+'</style></head><body>'+''.join(f'<div id="{n}">{h}</div>' for n,h in out)+'</body></html>')
json.dump([n for n,_ in out],open('nomes.json','w'))
