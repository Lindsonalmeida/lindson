# Culto de Gratidão · aniversário do Prefeito Mecinho (10/11/2026, designer gráfico).
# Composição copiada: cobertura editorial de evento (ref 1 Contra "Election coverage" Mauritânia: foto real sangrando no topo
# + manchete pesada embaixo; ref 2 Behance "político" BR: foto em cartão com etiqueta; ref 3 "Díky, že můžem" CZ: frase gigante empilhada).
# Identidade v13 v3: degradê royal→marinho, Montserrat Black, Kaushan, etiquetas chapadas, logo oficial. Sem grafismos.
import sys
D=sys.argv[1]; MAR,ROY,SOL,LAR='#05316E','#2350F5','#FFC20E','#FF7A1A'
GRAO=("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='3' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 .5  0 0 0 0 .5  0 0 0 0 .5  0 0 0 .9 0'/></filter><rect width='100%25' height='100%25' filter='url(%23n)'/></svg>")
FUNDO=f"radial-gradient(1100px 900px at 30% 30%,#3E6CFF 0,{ROY} 40%,#1539BE 68%,#082063 100%)"
G=f"background:linear-gradient(180deg,#FFE066,{SOL} 50%,{LAR});-webkit-background-clip:text;background-clip:text;color:transparent"
def foto(src,x,y,w,h,pos,tilt=0,extra=''):
  return f'<div class="a" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:url(assets/{src}) {pos}/cover;transform:rotate({tilt}deg);box-shadow:0 40px 60px -30px rgba(2,12,50,.8);outline:10px solid #fff;{extra}"></div>'
def tela(id,w,h,body):
  return f'<div class="t" id="{id}" style="width:{w}px;height:{h}px">{body}<img class="a" src="assets/logo.png" style="right:56px;bottom:46px;width:200px;filter:drop-shadow(0 10px 20px rgba(2,12,50,.5))"><div class="a" style="inset:0;background-image:url(&quot;{GRAO}&quot;);opacity:.10;mix-blend-mode:overlay"></div></div>'
L=lambda t,x,y,s=24,c='rgba(255,255,255,.92)':f'<div class="a L" style="left:{x}px;top:{y}px;font-size:{s}px;color:{c}">{t}</div>'
def tag(t,x,y,bg,c,s=34): return f'<div class="a B" style="left:{x}px;top:{y}px;padding:16px 24px 12px;font-size:{s}px;letter-spacing:.01em;background:{bg};color:{c};box-shadow:0 20px 34px -20px rgba(2,12,50,.7)">{t}</div>'
T=[]
# C1 capa · foto real do grupo sangrando no topo (Leo à direita, no mesmo patamar do grupo)
T.append(tela('c1',1080,1350,
 '<div class="a" style="left:0;top:0;width:1080px;height:860px;background:url(assets/f24-grupo.jpg) 100% 30%/auto 1000px no-repeat"></div>'
 f'<div class="a" style="left:0;top:560px;width:1080px;height:320px;background:linear-gradient(180deg,rgba(8,32,99,0),#0B2A8A 85%)"></div>'
 + L('Culto de Ação de Graças <span style="color:#FFC20E">•</span> São João Batista',64,860,22)
 + f'<div class="a B" style="left:60px;top:906px;font-size:118px;color:#fff">Uma noite de<br><span style="{G}">gratidão</span></div>'
 + f'<div class="a K" style="left:64px;top:1150px;font-size:50px;color:#fff;line-height:1.1">pelo aniversário do<br><span style="color:{SOL}">Prefeito Mecinho</span></div>'))
# C2 · frase gigante empilhada + foto do momento da palavra em cartão inclinado
T.append(tela('c2',1080,1350,
 L('Celebração de Gratidão',70,96)
 + f'<div class="a B" style="left:64px;top:150px;font-size:112px;color:#fff">Gratidão<br>é a nossa<br><span style="{G}">oração</span></div>'
 + foto('f22-palavra.jpg',300,600,700,520,'40% 30%',3)
 + tag('Fé • família • São João Batista',64,1180,SOL,MAR,30)))
# C3 · parabéns ao prefeito, foto do palco em cartão grande, etiqueta laranja
T.append(tela('c3',1080,1350,
 foto('f25-palco.jpg',70,90,940,640,'50% 35%',-2)
 + tag('Feliz aniversário',70,790,LAR,'#fff',40)
 + f'<div class="a B" style="left:64px;top:880px;font-size:96px;color:#fff">Prefeito<br><span style="{G}">Mecinho</span></div>'
 + f'<div class="a K" style="left:66px;top:1100px;font-size:46px;color:#fff;line-height:1.15">que Deus abençoe sua vida<br>com saúde e sabedoria</div>'))
# C4 · última tela, foto real da plateia sangrando
T.append(tela('c4',1080,1350,
 '<div class="a" style="left:0;top:0;width:1080px;height:820px;background:url(assets/f23-plateia.jpg) 64% 70%/auto 1180px no-repeat"></div>'
 f'<div class="a" style="left:0;top:520px;width:1080px;height:320px;background:linear-gradient(180deg,rgba(8,32,99,0),#0B2A8A 85%)"></div>'
 + f'<div class="a B" style="left:60px;top:830px;font-size:92px;color:#fff">Foi uma honra<br><span style="{G}">estar presente</span></div>'
 + f'<div class="a K" style="left:64px;top:1050px;font-size:48px;color:#fff;line-height:1.15">seguimos juntos, com fé,<br>por <span style="color:{SOL}">São João Batista</span></div>'
 + L('Leo Pinto <span style="color:#FFC20E">•</span> Vereador',64,1240,22)))
# Stories
T.append(tela('s1',1080,1920,
 '<div class="a" style="left:0;top:0;width:1080px;height:1240px;background:url(assets/f24-grupo.jpg) 100% 30%/auto 1300px no-repeat"></div>'
 f'<div class="a" style="left:0;top:900px;width:1080px;height:360px;background:linear-gradient(180deg,rgba(8,32,99,0),#0B2A8A 85%)"></div>'
 + L('Ontem à noite <span style="color:#FFC20E">•</span> Culto de Ação de Graças',64,1250,24)
 + f'<div class="a B" style="left:60px;top:1300px;font-size:120px;color:#fff">Celebração<br>de <span style="{G}">gratidão</span></div>'
 + f'<div class="a K" style="left:64px;top:1560px;font-size:56px;color:#fff;line-height:1.1">pelo aniversário do<br><span style="color:{SOL}">Prefeito Mecinho</span></div>'))
T.append(tela('s2',1080,1920,
 tag('Feliz aniversário',70,170,LAR,'#fff',44)
 + f'<div class="a B" style="left:64px;top:280px;font-size:140px;color:#fff">Prefeito<br><span style="{G}">Mecinho</span></div>'
 + foto('f25-palco.jpg',90,680,900,900,'52% 40%',-2)
 + f'<div class="a K" style="left:70px;top:1640px;font-size:52px;color:#fff;line-height:1.1">muita saúde, paz e bênçãos!</div>'))
T.append(tela('s3',1080,1920,
 '<div class="a" style="left:0;top:0;width:1080px;height:1920px;background:url(assets/f23-plateia.jpg) 64% 60%/auto 1920px no-repeat"></div>'
 f'<div class="a" style="left:0;top:900px;width:1080px;height:1020px;background:linear-gradient(180deg,rgba(8,32,99,0),rgba(11,42,138,.92) 55%,#082063)"></div>'
 + f'<div class="a B" style="left:60px;top:1340px;font-size:90px;color:#fff">Gratidão a Deus<br><span style="{G}">por esta noite</span></div>'
 + f'<div class="a K" style="left:64px;top:1570px;font-size:54px;color:#fff;line-height:1.1">seguimos juntos,<br>com fé</div>'))
html=f"""<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Kaushan+Script&family=Montserrat:wght@700;900&display=swap" rel="stylesheet">
<style>*{{margin:0;padding:0;box-sizing:border-box}}body{{background:#000}}.t{{position:relative;overflow:hidden;background:{FUNDO};margin-bottom:20px}}.a{{position:absolute}}
.K{{font-family:'Kaushan Script'}}.B{{font-family:Montserrat;font-weight:900;text-transform:uppercase;line-height:.92;letter-spacing:-.02em;white-space:nowrap;filter:drop-shadow(0 12px 24px rgba(2,12,50,.4))}}
.L{{font-family:Montserrat;font-weight:700;text-transform:uppercase;letter-spacing:.3em;white-space:nowrap}}</style></head><body>{''.join(T)}</body></html>"""
open(f'{D}/pecas.html','w').write(html)
