# Pagode Fiado · Notícias do pagode · modelo semanal (conta Zuleide, 16/11/2026)
# Uso: python3 gerar.py [noticias.json] [pasta_saida]  -> noticia-NN.jpg (+ -2,-3 se carrossel) e grade.jpg
import json,os,sys,html,subprocess
from PIL import Image
D=os.path.dirname(os.path.abspath(__file__))
J=sys.argv[1] if len(sys.argv)>1 else D+'/noticias.json'; OUT=sys.argv[2] if len(sys.argv)>2 else D+'/artes'
os.makedirs(OUT,exist_ok=True); N=json.load(open(J))
LOGO=open(D+'/../../../processos/brand-book-premium/pagode-fiado/logo.svg').read()
Y,V,K,C,R='#F2B705','#1E6B52','#111111','#F3E9D2','#C0392B'
CSS="""@import url('https://fonts.googleapis.com/css2?family=Shrikhand&family=Work+Sans:wght@400;600;800&family=Permanent+Marker&family=Caveat+Brush&display=block');
*{margin:0;box-sizing:border-box}body{width:1080px;height:1350px;overflow:hidden;font-family:'Work Sans'}
.a{position:relative;width:1080px;height:1350px;overflow:hidden}.sh{font-family:Shrikhand;line-height:.98}.mk{font-family:'Permanent Marker'}.cv{font-family:'Caveat Brush'}
.logo{position:absolute}.logo svg{width:100%;height:auto}
.ch{display:inline-block;font:800 26px 'Work Sans';letter-spacing:.22em;padding:12px 22px}
.tx{font:600 44px/1.25 'Work Sans'}.fo{position:absolute;left:70px;bottom:60px;font:600 24px 'Work Sans';letter-spacing:.06em;opacity:.85}
.sel{position:absolute;top:60px;right:60px;font:800 22px 'Work Sans';letter-spacing:.25em}
.xd{position:absolute;bottom:0;left:0;right:0;height:22px;background:repeating-linear-gradient(90deg,#C0392B 0 60px,#F3E9D2 60px 120px)}"""
def lg(pos,w=200): return f'<div class="logo" style="{pos};width:{w}px">{LOGO}</div>'
def fs(t,base,k=9): n=max(len(w) for w in t.split()); return min(base,int(base*k/max(n,k)))
def capa(n,i):
  t=n['tipo'];b=html.escape(n['big']);c=html.escape(n['chapeu']);x=html.escape(n['l2']);f=html.escape('Fonte: '+n['fonte'])
  sel=lambda col:f'<div class="sel" style="color:{col}">NOTÍCIAS DO PAGODE · Nº {i:02d}</div>'
  if t=='A': return f'''<div class="a" style="background:{Y}">{sel(K)}{lg('top:40px;left:60px')}
  <div style="position:absolute;left:70px;right:70px;top:300px"><span class="ch" style="background:{K};color:{Y}">{c}</span>
  <div class="sh" style="font-size:{fs(n['big'],200)}px;color:{K};margin-top:40px">{b}</div>
  <div class="tx" style="color:{K};margin-top:50px;border-left:12px solid {R};padding-left:30px">{x}</div></div>
  <div class="fo" style="color:{K}">{f}</div><div class="xd"></div></div>'''
  if t=='B': return f'''<div class="a" style="background:{K}">{sel(C)}{lg('top:40px;left:60px')}
  <div class="sh" style="position:absolute;right:-40px;top:170px;font-size:700px;color:{R};opacity:.9;line-height:.9">40</div>
  <div style="position:absolute;left:70px;right:70px;bottom:150px"><span class="ch" style="background:{Y};color:{K}">{c}</span>
  <div class="sh" style="font-size:{fs(n['big'],150)}px;color:{C};margin-top:30px">{b}</div>
  <div class="tx" style="color:{C};margin-top:30px">{x}</div></div><div class="fo" style="color:{C}">{f}</div></div>'''
  if t=='C': return f'''<div class="a" style="background:{C};background-image:repeating-linear-gradient(180deg,transparent 0 63px,rgba(30,107,82,.25) 63px 65px)">
  <div style="position:absolute;left:110px;top:0;bottom:0;width:3px;background:{R}"></div>{sel(V)}{lg('top:40px;left:140px',190)}
  <div style="position:absolute;left:150px;right:70px;top:280px"><span class="ch" style="background:{V};color:{C}">{c}</span>
  <div class="mk" style="font-size:{fs(n['big'],130)}px;line-height:1.02;color:{R};margin-top:40px">{b}</div>
  <div class="cv" style="font-size:60px;line-height:1.1;color:{K};margin-top:40px">{x}</div></div><div class="fo" style="left:150px;color:{K}">{f}</div></div>'''
  if t=='D': return f'''<div class="a" style="background:{V}">{sel(C)}{lg('top:40px;left:60px')}
  <div style="position:absolute;left:70px;right:70px;top:260px;border:6px solid {Y};padding:60px 50px">
  <span class="ch" style="background:{Y};color:{K}">{c}</span>
  <div class="sh" style="font-size:{fs(n['big'],150,7)}px;color:{Y};margin-top:40px">{b}</div>
  <div class="tx" style="color:{C};margin-top:40px">{x}</div></div><div class="fo" style="color:{C}">{f}</div><div class="xd"></div></div>'''
  if t=='E': return f'''<div class="a" style="background:{R}">{sel(C)}{lg('top:40px;left:60px')}
  <div style="position:absolute;left:90px;right:90px;top:330px;background:#FFF8E1;padding:80px 60px 70px;transform:rotate(-2deg);box-shadow:0 30px 70px rgba(0,0,0,.4)">
  <div style="position:absolute;top:-30px;left:50%;margin-left:-110px;width:220px;height:56px;background:rgba(242,183,5,.85);transform:rotate(3deg)"></div>
  <div class="cv" style="font-size:44px;color:{V}">{c}</div>
  <div class="sh" style="font-size:{fs(n['big'],150)}px;color:{K};margin-top:16px">{b}</div>
  <div class="tx" style="font-size:40px;color:{K};margin-top:30px">{x}</div></div><div class="fo" style="color:{C}">{f}</div></div>'''
  if t=='F': return f'''<div class="a" style="background:{K}">{sel(Y)}{lg('top:40px;left:60px')}
  <div style="position:absolute;left:0;right:0;top:260px">{''.join(f'<div class="sh" style="font-size:{112 if k!=1 else 90}px;white-space:nowrap;color:{Y if k==1 else "transparent"};-webkit-text-stroke:3px {Y};margin-left:{50-260*(k!=1)}px">{b}</div>' for k in range(3))}</div>
  <div style="position:absolute;left:70px;right:70px;bottom:140px"><span class="ch" style="background:{R};color:{C}">{c}</span>
  <div class="tx" style="color:{C};margin-top:30px">{x}</div></div><div class="fo" style="color:{C}">{f}</div></div>'''
  if t=='G': return f'''<div class="a" style="background:{Y}">{sel(K)}{lg('top:40px;left:60px')}
  <div style="position:absolute;top:220px;left:50%;margin-left:-300px;width:600px;height:600px;border-radius:50%;background:{V};border:16px solid {K}"></div>
  <div style="position:absolute;top:190px;left:50%;margin-left:-330px;width:660px;height:660px;border-radius:50%;border:4px dashed {R}"></div>
  <div class="sh" style="position:absolute;top:380px;left:290px;right:290px;text-align:center;font-size:{fs(n['big'],96,6)}px;color:{Y}">{b}</div>
  <div style="position:absolute;left:70px;right:70px;top:900px;text-align:center"><span class="ch" style="background:{K};color:{Y}">{c}</span>
  <div class="tx" style="color:{K};margin-top:30px">{x}</div></div><div class="fo" style="color:{K}">{f}</div></div>'''
  if t=='H': return f'''<div class="a" style="background:{K}">{sel(C)}{lg('top:40px;left:60px')}
  <div style="position:absolute;left:0;right:60px;top:330px"><span class="ch" style="margin-left:70px;background:{C};color:{K}">{c}</span><br>
  {''.join(f'<div class="sh" style="display:inline-block;background:{bg};color:{co};font-size:{fs(n["big"],120)}px;padding:16px 40px 26px 70px;margin-top:22px">{html.escape(p)}</div><br>' for p,bg,co in zip(n['big'].split(' + '),[R,Y],[C,K]))}
  <div class="tx" style="color:{C};margin:40px 0 0 70px">{x}</div></div><div class="fo" style="color:{C}">{f}</div><div class="xd"></div></div>'''
def tela(n,i,s,k,tot):
  bg,co,ac=[(C,K,R),(V,C,Y)][k%2]
  return f'''<div class="a" style="background:{bg}"><div class="sel" style="color:{co}">{k+2}/{tot}</div>{lg('top:40px;left:60px',170)}
  <div style="position:absolute;left:70px;right:70px;top:380px"><div class="sh" style="font-size:{fs(s['t'],170)}px;color:{ac}">{html.escape(s['t'])}</div>
  <div class="tx" style="font-size:54px;color:{co};margin-top:50px">{html.escape(s['x'])}</div></div>
  <div class="cv" style="position:absolute;left:70px;bottom:120px;font-size:50px;color:{co}">Pendura na conta. Segue o @pagodefiado</div>
  <div class="fo" style="color:{co}">{html.escape('Fonte: '+n['fonte'])}</div></div>'''
px=os.environ.get('HTTPS_PROXY','')
def shot(body,name):
  h=f'{OUT}/_t.html'; open(h,'w').write(f'<html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{body}</body></html>')
  p=f'{OUT}/{name}.png'
  subprocess.run(['google-chrome','--headless=new','--no-sandbox','--hide-scrollbars','--disable-gpu',f'--proxy-server={px}' if px else '--no-proxy-server','--virtual-time-budget=8000','--window-size=1080,1350',f'--screenshot={p}','file://'+h],capture_output=True,timeout=90)
  Image.open(p).convert('RGB').save(p[:-4]+'.jpg',quality=88); os.remove(p); os.remove(h); return p[:-4]+'.jpg'
capas=[]
for i,n in enumerate(N,1):
  capas.append(shot(capa(n,i),f'noticia-{i:02d}'))
  cs=n.get('carrossel',[])
  for k,s in enumerate(cs): shot(tela(n,i,s,k,len(cs)+1),f'noticia-{i:02d}-{k+2}')
g=Image.new('RGB',(3*360,((len(capas)+2)//3)*450),'#111')
for j,p in enumerate(capas): g.paste(Image.open(p).resize((360,450)),((j%3)*360,(j//3)*450))
g.save(OUT+'/../grade.jpg',quality=85); print('ok',len(capas))
