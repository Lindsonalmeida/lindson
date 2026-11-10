# Capas de Reels do curso (Rafael e Tiago), 10/11/2026, conta Zuleide, designer grafico.
# Referencias copiadas: A = Koto/Norton (UK, manchete gigante atras da pessoa); B = Harvard Law Review (EUA, rotulo editorial + serif);
# C = Studio Dumbar (NL, bloco de cor com glifo gigante); D = Koto/Where London Meets (UK, caixa alta empilhada ocupando a largura).
import json
V,O,CR,CA='#123528','#C8A96B','#F3EEE3','#0B2219'
P={'rafael':dict(f='rafael-recorte.png',w=797,fx=477.5,fy=74,fw=343,nome='Prof. Rafael Araújo Veras'),
   'tiago':dict(f='tiago-recorte.png',w=1098,fx=535.5,fy=97,fw=411,nome='Prof. Tiago Azevedo')}
FACE=360
def foto(p,cx,top):
  d=P[p];s=FACE/d['fw'];w=d['w']*s
  return f'<img class="pes" src="{d["f"]}" style="width:{w:.0f}px;left:{cx-d["fx"]*s:.0f}px;top:{top-d["fy"]*s:.0f}px">'
def tag(p,cor):return f'<div class="tag" style="color:{cor}"><b>§</b> PROCESSO LEGISLATIVO <span>·</span> {P[p]["nome"]}</div>'
def A(p,t,h,back,bg,fg,ac):
  return f'''<div class="c" style="background:{bg}">{tag(p,ac)}<div class="back" style="color:{ac}">{back}</div>{foto(p,540,430)}
  <div class="fade" style="background:linear-gradient(transparent,{bg} 55%)"></div>
  <h1 class="ha" style="color:{fg}">{t.replace(h,f'<em style="color:{ac}">{h}</em>')}</h1><div class="sw" style="color:{ac}">assista ao Reels ↓</div></div>'''
def B(p,n,t,h,sub):
  return f'''<div class="c" style="background:{CR}">{tag(p,V)}<div class="hr"></div><div class="vol">Nº {n} &nbsp;·&nbsp; REGIMENTO EM 1 MINUTO</div>
  <h1 class="hb">{t.replace(h,f'<em>{h}</em>')}</h1><div class="hr2"></div><p class="sub">{sub}</p><div class="sec">§</div></div>'''
def C(p,t,h):
  return f'''<div class="c" style="background:{O}">{tag(p,V)}<div class="glifo">§</div><h1 class="hc">{t.replace(h,f'<span>{h}</span>')}</h1></div>'''
def D(p,linhas,dest):
  ls=''.join(f'<div class="{"dd" if i==dest else ""}">{l}</div>' for i,l in enumerate(linhas))
  return f'''<div class="c" style="background:{CA}">{tag(p,O)}<div class="hd">{ls}</div><div class="rod">§ curso de processo legislativo</div></div>'''
capas=[
 ('01-rafael-emenda',A('rafael','Vereador pode aumentar despesa por emenda?','despesa','emenda',V,CR,O)),
 ('02-tiago-portaria',A('tiago','Portaria serve para quê?','para quê?','portaria',CR,V,'#9C7B3E')),
 ('03-rafael-questao-de-ordem',B('rafael','02','O que é questão de ordem?','questão de ordem?','Quando usar, quem pode levantar e o que o presidente faz.')),
 ('04-tiago-sancionar',C('tiago','Prefeito pode sancionar sem falar nada?','sem falar nada?')),
 ('05-rafael-mocao',D('rafael',['MOÇÃO','NÃO É','PROJETO','DE LEI'],1)),
 ('06-tiago-procedimento',B('tiago','06','O que é procedimento abreviado ou conclusivo?','abreviado ou conclusivo?','Quando o projeto não precisa ir ao plenário.')),
 ('07-rafael-fases',C('rafael','Quais são as fases do processo legislativo?','fases')),
 ('08-tiago-urgencia',D('tiago',['O PREFEITO','PODE PEDIR','URGÊNCIA','EM QUALQUER','PROJETO?'],2)),
]
css=f'''@import url('https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Inter+Tight:wght@400;600;800;900&display=swap');
body{{margin:0}}.c{{width:1080px;height:1920px;position:relative;overflow:hidden;font-family:'Inter Tight'}}
.c:after{{content:'';position:absolute;inset:0;background:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='200' height='200'%3E%3Cfilter id='n'%3E%3CfeTurbulence baseFrequency='.9'/%3E%3C/filter%3E%3Crect width='200' height='200' filter='url(%23n)' opacity='.07'/%3E%3C/svg%3E");pointer-events:none}}
.tag{{position:absolute;top:300px;left:84px;right:84px;font:600 26px 'Inter Tight';letter-spacing:.14em;z-index:5}}.tag b{{font:italic 40px 'Instrument Serif';margin-right:6px}}.tag span{{opacity:.5}}
.back{{position:absolute;top:340px;left:-20px;right:-20px;text-align:center;font:italic 330px/1 'Instrument Serif';letter-spacing:-.03em;z-index:1}}
.pes{{position:absolute;z-index:2;-webkit-mask-image:linear-gradient(#000 70%,transparent 96%)}}
.fade{{position:absolute;left:0;right:0;top:1000px;height:500px;z-index:3}}
.ha{{position:absolute;left:84px;right:84px;bottom:390px;margin:0;font:900 96px/1 'Inter Tight';letter-spacing:-.03em;z-index:4}}.ha em{{font:italic 400 112px/1 'Instrument Serif'}}
.sw{{position:absolute;left:84px;bottom:310px;font:600 26px 'Inter Tight';letter-spacing:.14em;text-transform:uppercase;z-index:4}}
.hr{{position:absolute;top:360px;left:84px;right:84px;border-top:3px solid {V}}}.vol{{position:absolute;top:395px;left:84px;font:800 28px 'Inter Tight';color:#9C7B3E;letter-spacing:.16em}}
.hb{{position:absolute;top:520px;left:84px;right:84px;margin:0;font:400 178px/.93 'Instrument Serif';color:{V};letter-spacing:-.02em}}.hb em{{color:#9C7B3E}}
.hr2{{position:absolute;bottom:470px;left:84px;width:200px;border-top:8px solid {O}}}.sub{{position:absolute;bottom:330px;left:84px;right:240px;margin:0;font:500 38px/1.3 'Inter Tight';color:{V}}}
.sec{{position:absolute;right:-60px;bottom:180px;font:italic 820px/1 'Instrument Serif';color:{O};opacity:.35}}
.glifo{{position:absolute;right:-180px;top:180px;font:italic 1500px/1 'Instrument Serif';color:{V};opacity:.95}}
.hc{{position:absolute;left:84px;right:84px;bottom:340px;margin:0;font:900 118px/.98 'Inter Tight';color:{CA};letter-spacing:-.035em;z-index:2}}.hc span{{background:{V};color:{O};padding:0 14px;box-decoration-break:clone;-webkit-box-decoration-break:clone;font:italic 400 128px/1.12 'Instrument Serif'}}
.hd{{position:absolute;top:420px;left:70px;right:70px;font:900 168px/.9 'Inter Tight';color:{CR};letter-spacing:-.045em}}.hd .dd{{color:{CA};background:{O};display:inline-block;padding:0 16px;font:italic 400 190px/1 'Instrument Serif'}}
.rod{{position:absolute;bottom:310px;left:84px;font:italic 46px 'Instrument Serif';color:{O}}}'''
html='<html><head><meta charset=utf-8><style>'+css+'</style></head><body>'+''.join(f'<div id="{n}">{h}</div>' for n,h in capas)+'</body></html>'
open('pecas.html','w').write(html);json.dump([n for n,_ in capas],open('nomes.json','w'))
