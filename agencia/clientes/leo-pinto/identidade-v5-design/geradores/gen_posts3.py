exec(open('gen_posts.py').read().split("posts={}")[0])
SZ={'b':(1399,1255),'d':(1285,1401),'g':(1372,1401),'e':(1118,1403),'i':(1031,1402),'j':(1373,1402)}
def disc(cx,cy,r,ph,pw,dx=0,alt='Leo Pinto',pop=360,disc_bg='radial-gradient(circle at 50% 40%, #3A66FF 0%, #2350F5 45%, #05316E 100%)',ring1='#FFC20E',ring2='#E8650C'):
  W,H=SZ[ph]; h=pw*H/W
  L=cx-r; T=cy-r-pop
  import json as _j; dx=(0.5-_j.load(open('facex.json'))[ph])*pw
  return f'''  <div style="position: absolute; left: {cx-r-70}px; top: {cy-r-70}px; width: {2*r+140}px; height: {2*r+140}px; border-radius: 50%; border: 34px solid {ring1}; box-sizing: border-box"></div>
  <div style="position: absolute; left: {cx-r-22}px; top: {cy-r-22}px; width: {2*r+44}px; height: {2*r+44}px; border-radius: 50%; border: 22px solid {ring2}; box-sizing: border-box"></div>
  <div style="position: absolute; left: {L}px; top: {cy-r}px; width: {2*r}px; height: {2*r}px; border-radius: 50%; background: {disc_bg}"></div>
  <div style="position: absolute; left: {L}px; top: {T}px; width: {2*r}px; height: {2*r+pop}px; overflow: hidden; border-radius: 0 0 {r}px {r}px">
    <img src="{u(ph)}" alt="{alt}" style="position: absolute; left: {r-pw/2+dx:.0f}px; bottom: -{h*0.06:.0f}px; width: {pw}px">
  </div>'''

def arch(cx,w,top,ph,pw,ring='#FFC20E',bg='radial-gradient(circle at 50% 35%, #3A66FF 0%, #2350F5 50%, #05316E 100%)'):
  import json as _j; fx=_j.load(open('facex.json'))[ph]
  return f'''  <div style="position: absolute; left: {cx-w/2-18:.0f}px; top: {top-18}px; width: {w+36}px; bottom: 150px; border-radius: {w/2+18:.0f}px {w/2+18:.0f}px 0 0; border: 14px solid {ring}; border-bottom: none; box-sizing: border-box"></div>
  <div style="position: absolute; left: {cx-w/2:.0f}px; top: {top}px; width: {w}px; bottom: 150px; border-radius: {w/2:.0f}px {w/2:.0f}px 0 0; overflow: hidden; background: {bg}">
    <img src="{u(ph)}" alt="Leo Pinto" style="position: absolute; left: {w/2-fx*pw:.0f}px; bottom: 0; width: {pw}px">
  </div>'''
def flush(ph,h,cx_hint=None):
  import json as _j; fx=_j.load(open('facex.json'))[ph]
  return fx
BAR=f'''
  <div style="position: absolute; left: 0; right: 0; bottom: 0; height: 150px; background: #05316E"></div>
  <div style="position: absolute; left: 60px; right: 60px; bottom: 0; height: 150px; display: flex; align-items: center; justify-content: space-between">
    <div style="display: flex; align-items: center; gap: 14px"><span style="font-weight: 800; font-size: 26px; letter-spacing: 0.24em">JUNTOS</span><svg width="62" height="28" viewBox="0 0 96 44" aria-hidden="true"><path d="M0 0l20 22L0 44h14l20-22L14 0zM30 0l20 22-20 22h14l20-22L44 0zM60 0l20 22-20 22h14l20-22L74 0z" fill="#FFC20E"/></svg><span style="font-weight: 900; font-size: 34px; text-transform: uppercase; color: #FFC20E">podemos mais!</span></div>
    <img src="{u('branco')}" alt="Logo Leo Pinto" style="width: 130px">
  </div>'''
posts={}
posts['Post1TamoJunto']=('Post · Tamo junto',('background: radial-gradient(circle at 50% 30%, #3A66FF 0%, #2350F5 45%, #05316E 100%)',f'''
  <div style="position: absolute; left: -40px; top: -160px; font-family: Anton, sans-serif; font-size: 1400px; line-height: 1; color: #1A44D8; opacity: 0.7">#</div>
  <img src="{u('linha')}" alt="" aria-hidden="true" style="position: absolute; left: -120px; top: 760px; width: 760px">
  {AT.format(c='#FFFFFF')}
{disc(540,520,300,'e',600)}
  <img src="{u('estrela')}" alt="" aria-hidden="true" style="position: absolute; left: 150px; top: 600px; width: 170px">
  <img src="{u('explosao')}" alt="" aria-hidden="true" style="position: absolute; left: 790px; top: 200px; width: 160px">
  <div style="position: absolute; left: 0; right: 0; top: 905px; text-align: center; font-family: Anton, sans-serif; font-size: 190px; line-height: 0.9; text-transform: uppercase"><span style="color: #FFC20E">#</span>TAMO JUNTO</div>
  <div style="position: absolute; left: 0; right: 0; top: 1090px; display: flex; justify-content: center"><span style="background: #FF7A1A; padding: 6px 26px; font-weight: 900; font-size: 40px; text-transform: uppercase">com o Leo</span></div>
{BAR}
'''))
posts['Post2TocomLeo']=('Post · #tôcom Leo',('background: radial-gradient(circle at 70% 60%, #3A66FF 0%, #2350F5 50%, #05316E 100%)',f'''
  <img src="{u('linha')}" alt="" aria-hidden="true" style="position: absolute; left: -100px; top: 980px; width: 700px">
  <div style="position: absolute; right: 64px; top: 56px; font-weight: 700; font-size: 20px; letter-spacing: 0.3em">@_LEONARDOPINTO</div>
  <div style="position: absolute; left: 64px; top: 110px; display: flex; align-items: center; gap: 16px">
    <span style="font-family: Anton, sans-serif; font-size: 210px; line-height: 0.8; color: #FFC20E">#</span>
    <div style="display: flex; flex-direction: column"><span style="font-weight: 400; font-size: 74px; line-height: 1">tôcom</span><span style="font-weight: 900; font-size: 84px; line-height: 0.95">LEO PINTO</span></div>
  </div>
  <div style="position: absolute; left: 64px; top: 380px; width: 400px; font-size: 28px; font-weight: 500; line-height: 1.45; color: rgba(255,255,255,0.9)">Vereador de São João Batista. Perto de você, todo mandato.</div>
  <div style="position: absolute; left: 590px; top: 470px; width: 660px; height: 660px; border-radius: 50%; border: 40px solid #FFC20E; box-sizing: border-box"></div>
  <div style="position: absolute; left: 670px; top: 550px; width: 500px; height: 500px; border-radius: 50%; background: radial-gradient(circle at 50% 40%, #3A66FF, #05316E 80%)"></div>
  <img src="{u('b')}" alt="Leo Pinto com o punho erguido" style="position: absolute; right: 0; bottom: 150px; height: 760px">
  <img src="{u('explosao')}" alt="" aria-hidden="true" style="position: absolute; left: 580px; top: 330px; width: 120px">
  <div style="position: absolute; left: 50px; top: 520px; transform: rotate(-6deg); display: flex; flex-direction: column; align-items: flex-start">
    <span style="font-family: 'Kaushan Script', cursive; font-size: 50px; margin-left: 16px">voz do povo</span>
    <span style="background: #FFC20E; padding: 8px 22px 2px; font-family: Anton, sans-serif; font-size: 64px; line-height: 1; color: #05316E">SEMPRE PERTO</span>
  </div>
{BAR}
'''))
posts['Post3Presente']=('Post · Presente nos povoados',('background: radial-gradient(circle at 30% 40%, #FFA040 0%, #FF7A1A 50%, #E8650C 100%)',f'''
  <img src="{u('mapa')}" alt="" aria-hidden="true" style="position: absolute; left: 420px; top: 120px; width: 700px; opacity: 0.16">
  <img src="{u('linha')}" alt="" aria-hidden="true" style="position: absolute; left: 520px; top: 1010px; width: 640px">
  <div style="position: absolute; left: 64px; top: 56px; font-weight: 700; font-size: 20px; letter-spacing: 0.3em">@_LEONARDOPINTO</div>
  <div style="position: absolute; right: 64px; top: 130px; display: flex; flex-direction: column; align-items: flex-end; font-family: Anton, sans-serif; line-height: 0.88; text-transform: uppercase">
    <span style="font-size: 120px">Presente</span><span style="font-size: 120px">nos</span>
    <span style="font-size: 120px; background: #05316E; color: #FFC20E; padding: 8px 18px 0">povoados!</span>
  </div>
{disc(330,850,270,'d',660)}
  <img src="{u('estrela')}" alt="" aria-hidden="true" style="position: absolute; left: 30px; top: 960px; width: 150px">
  <div style="position: absolute; right: 64px; top: 600px; width: 400px; background: #FFFFFF; border-radius: 22px; padding: 26px 30px; box-sizing: border-box; color: #05316E; font-size: 25px; font-weight: 600; line-height: 1.4; box-shadow: 0 30px 50px -20px rgba(5,49,110,0.5)">Cada canto de São João Batista merece atenção. Perto pra ouvir, junto pra fazer.</div>
  <img src="{u('explosao')}" alt="" aria-hidden="true" style="position: absolute; right: 40px; top: 840px; width: 130px">
{BAR}
'''))
A=os.path.abspath('lindson/agencia/clientes/leo-pinto/identidade-v2/assets');F=os.path.abspath('fotos-v5');FA=os.path.abspath('fotos-limpas');K=os.path.abspath('kit')
loc={'a':FA+'/a-close-laranja.png','e':F+'/e-celular.png','b':F+'/b-punho.png','d':F+'/d-bracos-cruzados-branca.png','g':F+'/g-maos-juntas-amarela.png','j':F+'/j-close-sorrindo.png','i':F+'/i-maos-abertas-branca.png','logo':A+'/logo.png','marinho':A+'/logo-marinho.png','branco':A+'/logo-mono-branco.png','linha':K+'/mapa-linha.svg','explosao':K+'/explosao-mapa.svg','estrela':K+'/estrela-ciano.svg','grao':K+'/grao.png','mapa':K+'/mapa-camada.svg'}
inv={'/_blob/'+v:'file://'+loc[k] for k,v in B.items()}
for name,(title,body) in posts.items():
  s=page(title,body)
  open(f'leo-id/project/{name}.dc.html','w').write(s)
  r=s.replace('<script src="./support.js"></script>','')
  for a,b in inv.items(): r=r.replace(a,b)
  open(f'render/{name}.html','w').write(r)
