# Pagode Fiado · 15 artes de frase 1080x1350 (conta Zuleide, 16/11/2026)
import json,os,sys,base64,html
import subprocess
D=os.path.dirname(os.path.abspath(__file__))
FOT=sys.argv[1]; OUT=sys.argv[2]; os.makedirs(OUT,exist_ok=True)
F=json.load(open(D+'/frases.json')); P=json.load(open(FOT+'/fotos.json'))
LOGO=open(D+'/../../../processos/brand-book-premium/pagode-fiado/logo.svg').read()
def b64(p): return 'data:image/jpeg;base64,'+base64.b64encode(open(p,'rb').read()).decode()
CSS="""@import url('https://fonts.googleapis.com/css2?family=Shrikhand&family=Work+Sans:wght@400;600;800&family=Permanent+Marker&family=Caveat+Brush&display=block');
*{margin:0;box-sizing:border-box}body{width:1080px;height:1350px;overflow:hidden;font-family:'Work Sans'}
.a{position:relative;width:1080px;height:1350px;overflow:hidden}
.ph{position:absolute;inset:0;background-size:cover;background-position:center}
.sh{font-family:Shrikhand;line-height:.95}.mk{font-family:'Permanent Marker'}.cv{font-family:'Caveat Brush'}
.logo{position:absolute;width:210px}.logo svg{width:100%;height:auto}
.tag{position:absolute;font:800 22px 'Work Sans';letter-spacing:.25em;text-transform:uppercase}
.cred{font:600 26px 'Work Sans';letter-spacing:.04em}
.grao:after{content:'';position:absolute;inset:0;background:radial-gradient(ellipse at center,transparent 55%,rgba(0,0,0,.45));pointer-events:none}"""
Y,V,K,C,R='#F2B705','#1E6B52','#111111','#F3E9D2','#C0392B'
def logo(pos,w=210): return f'<div class="logo" style="{pos};width:{w}px">{LOGO}</div>'
def art(f,ph,i):
  t=f['tipo'];l1=html.escape(f['l1']);l2=html.escape(f['l2']);sub=html.escape(f['sub']);cr=html.escape(f['cred'])
  num=f'<div class="tag" style="top:56px;right:60px;color:{{c}}">Nº {i:02d} · Caderno do fiado</div>'
  if t=='A': return f'''<div class="a grao"><div class="ph" style="background-image:url({ph});filter:saturate(1.1) contrast(1.05)"></div>
  <div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.15) 30%,rgba(17,17,17,.95) 78%)"></div>
  {num.format(c=C)}{logo('top:40px;left:56px')}
  <div style="position:absolute;left:60px;right:60px;bottom:110px"><div class="sh" style="font-size:118px;color:{Y}">{l1}</div>
  <div class="sh" style="font-size:96px;color:{C};margin-top:8px">{l2}</div>
  <div class="cv" style="font-size:54px;color:{C};margin-top:26px;opacity:.9">{sub}</div></div>
  <div style="position:absolute;bottom:0;left:0;right:0;height:22px;background:repeating-linear-gradient(90deg,{R} 0 60px,{C} 60px 120px)"></div></div>'''
  if t=='B': return f'''<div class="a" style="background:{C};background-image:repeating-linear-gradient(180deg,transparent 0 63px,rgba(30,107,82,.28) 63px 65px)">
  <div style="position:absolute;left:110px;top:0;bottom:0;width:3px;background:{R};opacity:.7"></div>
  {num.format(c=V)}
  <div style="position:absolute;top:150px;right:80px;width:520px;height:620px;background:#fff;padding:22px 22px 90px;transform:rotate(4deg);box-shadow:0 30px 60px rgba(0,0,0,.25)">
  <div style="width:100%;height:100%;background:url({ph}) center/cover"></div><div class="cv" style="position:absolute;bottom:20px;left:30px;font-size:44px;color:{K}">sexta, mesa 7</div></div>
  <div style="position:absolute;top:70px;left:150px;width:160px;height:46px;background:rgba(242,183,5,.75);transform:rotate(-6deg)"></div>
  <div style="position:absolute;left:150px;right:80px;bottom:90px"><div class="mk" style="font-size:96px;color:{R};line-height:1">{l1}</div>
  <div class="cv" style="font-size:88px;color:{K};line-height:1;margin-top:20px">{l2}</div></div>
  {logo('top:130px;left:150px',190)}</div>'''
  if t=='C': return f'''<div class="a grao" style="background:{K}"><div class="ph" style="background-image:url({ph});filter:grayscale(1) contrast(1.15) brightness(.6)"></div>
  <div class="sh" style="position:absolute;left:30px;top:200px;font-size:{280 if len(l1)>4 else 330}px;color:{Y};mix-blend-mode:normal;letter-spacing:-.02em;white-space:nowrap">{l1}</div>
  {num.format(c=Y)}{logo('top:40px;left:56px')}
  <div style="position:absolute;left:60px;right:60px;bottom:140px;font:800 78px/1.05 'Work Sans';color:{C}">{l2}</div>
  <div style="position:absolute;left:60px;bottom:100px;width:180px;height:10px;background:{R}"></div></div>'''
  if t=='D': return f'''<div class="a" style="background:{V}"><div class="ph" style="bottom:auto;height:760px;background-image:url({ph})"></div>
  <div style="position:absolute;top:720px;left:0;right:0;height:80px;background:repeating-linear-gradient(90deg,{V} 0 80px,#F3E9D2 80px 82px),{V};border-top:8px solid {Y}"></div>
  {num.format(c=C)}
  <div style="position:absolute;left:60px;right:60px;top:830px"><div class="sh" style="font-size:96px;color:{Y}">{l1}</div>
  <div class="sh" style="font-size:80px;color:{C};margin-top:14px">{l2}</div></div>
  {logo('bottom:46px;right:56px',190)}</div>'''
  if t=='E': return f'''<div class="a grao"><div class="ph" style="background-image:url({ph});filter:saturate(.9) brightness(.75)"></div>
  {num.format(c=C)}{logo('top:40px;left:56px')}
  <div style="position:absolute;left:110px;right:110px;top:420px;background:#FFF8E1;padding:80px 70px 70px;transform:rotate(-2.5deg);box-shadow:0 30px 70px rgba(0,0,0,.45)">
  <div style="position:absolute;top:-34px;left:50%;margin-left:-60px;width:120px;height:120px;border-radius:50%;background:{R};box-shadow:0 10px 20px rgba(0,0,0,.35)"></div>
  <div class="cv" style="font-size:80px;color:{K};line-height:1.05">{l1}</div>
  <div class="mk" style="font-size:92px;color:{R};line-height:1.05;margin-top:24px">{l2}</div>
  <div class="cv" style="font-size:44px;color:{V};margin-top:30px;text-align:right">— Pagode Fiado</div></div></div>'''
  if t=='F': return f'''<div class="a" style="background:{K}"><div class="ph" style="left:540px;background-image:url({ph});filter:grayscale(.2)"></div>
  <div style="position:absolute;left:540px;top:0;bottom:0;width:240px;background:linear-gradient(90deg,{K},transparent)"></div>
  {num.format(c=C)}{logo('top:40px;left:56px',190)}
  <div class="sh" style="position:absolute;left:40px;top:180px;font-size:420px;color:{R};line-height:.8">“</div>
  <div style="position:absolute;left:60px;width:620px;top:520px"><div class="sh" style="font-size:84px;color:{C}">{l1}</div>
  <div class="sh" style="font-size:96px;color:{Y};margin-top:10px">{l2}</div>
  <div class="cred" style="color:{C};margin-top:46px;opacity:.85">{cr}</div></div></div>'''
  if t=='G': return f'''<div class="a" style="background:{Y}"><div style="position:absolute;top:150px;left:50%;margin-left:-330px;width:660px;height:660px;border-radius:50%;background:url({ph}) center/cover;border:18px solid {K}"></div>
  <div style="position:absolute;top:120px;left:50%;margin-left:-370px;width:740px;height:740px;border-radius:50%;border:4px dashed {R}"></div>
  {num.format(c=K)}{logo('top:40px;left:56px',190)}
  <div style="position:absolute;left:40px;right:40px;top:900px;text-align:center"><div class="sh" style="font-size:120px;color:{K}">{l1}</div>
  <div class="sh" style="font-size:130px;color:{R};margin-top:-6px">{l2}</div>
  <div class="cv" style="font-size:52px;color:{V};margin-top:20px">{sub}</div></div></div>'''
  if t=='H': return f'''<div class="a grao" style="background:{K}"><div class="ph" style="background-image:url({ph});filter:grayscale(1) contrast(1.2) brightness(.7)"></div>
  {num.format(c=C)}{logo('top:40px;left:56px')}
  <div style="position:absolute;left:0;right:60px;top:640px"><div class="sh" style="display:inline-block;background:{R};color:{C};font-size:84px;padding:20px 40px 26px 60px">{l1}</div><br>
  <div class="sh" style="display:inline-block;background:{Y};color:{K};font-size:96px;padding:20px 40px 30px 60px;margin-top:16px">{l2}</div>
  <div class="cred" style="color:{C};margin:36px 0 0 60px">{cr}</div></div></div>'''
for i,f in enumerate(F,1):
  ph=b64(os.path.join(FOT,P[f.get('foto',i-1)]['f']))
  h=f'{OUT}/f{i:02d}.html'; open(h,'w').write(f'<html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{art(f,ph,i)}</body></html>')
  px=os.environ.get('HTTPS_PROXY','')
  subprocess.run(['google-chrome','--headless=new','--no-sandbox','--hide-scrollbars','--disable-gpu',f'--proxy-server={px}' if px else '--no-proxy-server','--virtual-time-budget=8000','--window-size=1080,1350',f'--screenshot={OUT}/frase-{i:02d}.png','file://'+h],capture_output=True,timeout=90)
  os.remove(h)
print('ok')
