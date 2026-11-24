exec(open('gen_posts3.py').read().split("\nposts={}\n")[0])
YB='radial-gradient(circle at 40% 30%, #FFE070 0%, #FFC20E 45%, #F5A800 100%)'
RB='radial-gradient(circle at 60% 30%, #3A66FF 0%, #2350F5 45%, #05316E 100%)'
AT2='<div style="position: absolute; left: 0; right: 0; top: 52px; text-align: center; font-weight: 700; font-size: 20px; letter-spacing: 0.32em; color: {c}">@_LEONARDOPINTO</div>'
posts={}
opts=''.join(f'<div style="display: flex; align-items: center; gap: 18px; border: 3px solid #2350F5; border-radius: 14px; padding: 16px 20px"><span style="width: 44px; height: 44px; border-radius: 50%; background: #2350F5; color: #FFFFFF; display: flex; align-items: center; justify-content: center; font-weight: 900; font-size: 22px">{l}</span><span style="font-weight: 700; font-size: 28px; color: #05316E">{t}</span></div>' for l,t in [('A','Festejo do padroeiro'),('B','São João'),('C','Bumba-meu-boi'),('D','Carnaval')])
posts['Post11Enquete']=('Post · Enquete',(f'background: {YB}',f'''
  <img src="{u('linha')}" alt="" aria-hidden="true" style="position: absolute; left: -160px; top: 120px; width: 900px; filter: brightness(0) saturate(100%) invert(26%) sepia(96%) saturate(4000%) hue-rotate(226deg); opacity: 0.9">
  <img src="{u('linha')}" alt="" aria-hidden="true" style="position: absolute; left: 400px; top: 880px; width: 820px; filter: brightness(0) invert(1); opacity: 0.85">
  {AT2.format(c='#05316E')}
  <div style="position: absolute; left: 110px; right: 110px; top: 230px; background: #FFFFFF; border-radius: 30px; padding: 0 0 36px; box-shadow: 0 40px 70px -30px rgba(5,49,110,0.55); overflow: hidden">
    <div style="background: #2350F5; padding: 34px 40px; text-align: center; font-weight: 800; font-size: 46px; line-height: 1.15">Qual festa do povoado<br>é a <span style="color: #FFC20E; font-family: 'Kaushan Script', cursive; font-weight: 400">sua preferida?</span></div>
    <div style="display: flex; flex-direction: column; gap: 18px; padding: 36px 50px 0">{opts}</div>
    <div style="text-align: center; margin-top: 26px; font-weight: 600; font-size: 22px; color: #2350F5">Responda nos comentários</div>
  </div>
  <img src="{u('explosao')}" alt="" aria-hidden="true" style="position: absolute; right: 70px; top: 160px; width: 150px">
{BAR}
'''))
items=''.join(f'<div style="display: flex; gap: 20px; align-items: baseline; padding: 14px 0"><span style="font-family: Anton, sans-serif; font-size: 62px; color: #FFC20E">0{i}</span><span style="font-weight: 700; font-size: 27px; color: #05316E">[Projeto aprovado {i}]</span></div>' for i in range(1,5))
dots=''.join('<span style="width: 22px; height: 22px; border-radius: 50%; background: #9AA4B5"></span>' for _ in range(12))
posts['Post12Projetos']=('Post · Projetos aprovados',(f'background: {RB}',f'''
  <img src="{u('estrela')}" alt="" aria-hidden="true" style="position: absolute; left: 50%; top: 120px; width: 1250px; transform: translateX(-50%); filter: brightness(0) saturate(100%) invert(79%) sepia(63%) saturate(1500%) hue-rotate(358deg)">
  {AT2.format(c='#FFFFFF')}
  <div style="position: absolute; left: 170px; top: 200px; width: 740px; height: 880px; background: #F7F6F1; border-radius: 10px; transform: rotate(-3deg); box-shadow: 0 40px 70px -30px rgba(0,0,0,0.6); box-sizing: border-box; padding: 70px 60px 40px">
    <div style="position: absolute; left: 40px; right: 40px; top: -12px; display: flex; justify-content: space-between">{dots}</div>
    <div style="font-weight: 600; font-size: 22px; color: #4A5568; letter-spacing: 0.08em">@_leonardopinto · mandato</div>
    <div style="font-family: Anton, sans-serif; font-size: 120px; line-height: 0.92; color: #2350F5; margin: 18px 0 10px">PROJETOS<br><span style="color: #05316E">APROVADOS</span></div>
    {items}
  </div>
{BAR}
'''))
posts['Post13Zap']=('Post · Chama no zap',(f'background: {YB}',f'''
  <div style="position: absolute; right: -180px; top: 300px; width: 760px; height: 1200px; border-radius: 380px; background: #2350F5; transform: rotate(24deg)"></div>
  <img src="{u('linha')}" alt="" aria-hidden="true" style="position: absolute; left: -140px; top: 960px; width: 760px; filter: brightness(0) invert(1)">
  {AT2.format(c='#05316E')}
  <div style="position: absolute; left: 70px; top: 130px; font-family: Anton, sans-serif; font-size: 190px; line-height: 0.88; text-transform: uppercase; color: #2350F5; transform: rotate(-4deg)">Chama<br><span style="color: #05316E">no zap</span></div>
  <div style="position: absolute; left: 80px; top: 560px; width: 360px; font-size: 30px; font-weight: 600; line-height: 1.4; color: #05316E">O gabinete do Leo responde você. [WhatsApp do gabinete]</div>
{arch(760,560,540,'e',520,ring='#FFFFFF')}
  <img src="{u('estrela')}" alt="" aria-hidden="true" style="position: absolute; left: 400px; top: 900px; width: 140px">
{BAR}
'''))
rep=''.join(f'<div style="font-family: Anton, sans-serif; font-size: 190px; line-height: 0.86; color: transparent; -webkit-text-stroke: 4px rgba(255,194,14,{o})">LIGADO</div>' for o in [0.9,0.6,0.4,0.25])
posts['Post14FiqueLigado']=('Post · Fique ligado',(f'background: {RB}',f'''
  <div style="position: absolute; left: 0; right: 0; top: 130px; text-align: center; font-weight: 700; font-size: 60px">Fique</div>
  <div style="position: absolute; left: 0; right: 0; top: 200px; text-align: center; font-family: Anton, sans-serif; font-size: 190px; line-height: 0.86; color: #FFC20E">LIGADO</div>
  <div style="position: absolute; left: 0; right: 0; top: 364px; text-align: center">{rep}</div>
  {AT2.format(c='#FFFFFF')}
{arch(540,600,600,'d',560)}
  <div style="position: absolute; left: 50%; bottom: 190px; transform: translateX(-50%) rotate(-3deg); background: #FFFFFF; border-radius: 20px; padding: 18px 34px; text-align: center; color: #05316E; box-shadow: 0 30px 50px -20px rgba(0,0,0,0.6)"><div style="font-family: Anton, sans-serif; font-size: 64px; line-height: 1">[DD.MM]</div><div style="font-weight: 700; font-size: 22px">[Evento · local]</div></div>
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
