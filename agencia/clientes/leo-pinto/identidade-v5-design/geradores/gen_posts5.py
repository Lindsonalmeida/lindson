exec(open('gen_posts3.py').read().split("\nposts={}\n")[0])
RB='radial-gradient(circle at 60% 30%, #3A66FF 0%, #2350F5 45%, #05316E 100%)'
OB='radial-gradient(circle at 30% 30%, #FFC20E 0%, #FF9A2A 45%, #FF7A1A 100%)'
AT2='<div style="position: absolute; left: 0; right: 0; top: 52px; text-align: center; font-weight: 700; font-size: 20px; letter-spacing: 0.32em; color: {c}">@_LEONARDOPINTO</div>'
posts={}
posts['Post4Juntos']=('Post · Juntos somos mais fortes',(f'background: {RB}',f'''
  <img src="{u('linha')}" alt="" aria-hidden="true" style="position: absolute; left: -140px; top: 640px; width: 760px">
  {AT2.format(c='#FFFFFF')}
{disc(540,500,260,'i',540,pop=230)}
  <img src="{u('estrela')}" alt="" aria-hidden="true" style="position: absolute; left: 190px; top: 580px; width: 140px">
  <img src="{u('explosao')}" alt="" aria-hidden="true" style="position: absolute; left: 770px; top: 250px; width: 130px">
  <div style="position: absolute; left: 0; right: 0; top: 815px; text-align: center; font-family: 'Kaushan Script', cursive; font-size: 96px; line-height: 1; color: #FFC20E">juntos</div>
  <div style="position: absolute; left: 0; right: 0; top: 975px; text-align: center; font-family: Anton, sans-serif; font-size: 160px; line-height: 0.9; text-transform: uppercase">somos <span style="color: #FF7A1A">+</span> fortes</div>
{BAR}
'''))
posts['Post8ProjetoLei']=('Post · Projeto de lei',(f'background: {RB}',f'''
  <div style="position: absolute; left: -10px; top: 760px; font-family: Anton, sans-serif; font-size: 300px; line-height: 0.8; color: #FFFFFF; opacity: 0.07">LEI</div>
  <img src="{u('linha')}" alt="" aria-hidden="true" style="position: absolute; left: -160px; top: 1010px; width: 700px">
  <div style="position: absolute; left: 70px; top: 56px; font-weight: 700; font-size: 20px; letter-spacing: 0.3em">@_LEONARDOPINTO</div>
  <div style="position: absolute; left: 70px; top: 130px; display: flex; flex-direction: column; align-items: flex-start">
    <span style="font-family: Anton, sans-serif; font-size: 140px; line-height: 0.9; text-transform: uppercase">Projeto</span>
    <span style="font-family: 'Kaushan Script', cursive; font-size: 64px; color: #FFC20E; margin: -6px 0 -6px 8px">de</span>
    <span style="font-family: Anton, sans-serif; font-size: 180px; line-height: 0.9; color: #FFC20E">LEI</span>
    <span style="margin-top: 20px; background: #FF7A1A; padding: 8px 20px; font-weight: 900; font-size: 30px; text-transform: uppercase">» em andamento</span>
  </div>
  <div style="position: absolute; left: 70px; top: 720px; width: 380px; font-size: 26px; font-weight: 600; line-height: 1.4">[Nome do projeto: o que muda na vida das pessoas]</div>
{arch(770,480,560,'d',600)}
  <img src="{u('explosao')}" alt="" aria-hidden="true" style="position: absolute; left: 470px; top: 520px; width: 130px">
{BAR}
'''))
rows=''.join(f'<div style="display: flex; align-items: center; gap: 18px; padding: 14px 0; border-top: 2px solid rgba(5,49,110,0.15)"><span style="font-family: Anton, sans-serif; font-size: 44px; color: #FF7A1A">[{h}]</span><span style="font-weight: 800; font-size: 23px; line-height: 1.2">[Compromisso · local]</span></div>' for h in ['08h','10h','15h','19h'])
posts['Post9Agenda']=('Post · Agenda do dia',(f'background: {OB}',f'''
  <div style="position: absolute; right: -30px; top: 40px; font-family: Anton, sans-serif; font-size: 380px; line-height: 0.8; color: #FFFFFF; opacity: 0.16">HOJE</div>
  <img src="{u('linha')}" alt="" aria-hidden="true" style="position: absolute; left: -120px; top: 1040px; width: 640px; filter: brightness(0) invert(1)">
  <div style="position: absolute; left: 60px; top: 56px; font-weight: 700; font-size: 20px; letter-spacing: 0.3em; color: #05316E">@_LEONARDOPINTO</div>
  <div style="position: absolute; left: 56px; top: 110px; font-family: Anton, sans-serif; font-size: 180px; line-height: 0.85; color: #05316E">AGENDA</div>
  <div style="position: absolute; left: 66px; top: 270px; font-family: 'Kaushan Script', cursive; font-size: 72px; transform: rotate(-6deg)">do dia</div>
  <div style="position: absolute; left: 56px; top: 400px; width: 440px; background: #FFFFFF; border-radius: 22px; padding: 26px 28px 10px; box-sizing: border-box; color: #05316E; box-shadow: 0 30px 50px -20px rgba(5,49,110,0.5)">
    <div style="font-family: Anton, sans-serif; font-size: 58px; line-height: 1">[DD.MM]</div>
    <div style="font-size: 20px; font-weight: 600; margin: 4px 0 10px">[dia da semana]</div>
    {rows}
  </div>
{arch(800,440,560,'g',560,ring='#05316E')}
{BAR}
'''))
posts['Post10Pergunte']=('Post · Pergunte ao vereador',(f'background: {RB}',f'''
  <div style="position: absolute; left: 0; right: 0; top: 90px; text-align: center; font-family: Anton, sans-serif; font-size: 300px; line-height: 0.85; color: #FFFFFF; opacity: 0.07">FALA<br>COMIGO</div>
  <img src="{u('linha')}" alt="" aria-hidden="true" style="position: absolute; left: 480px; top: 700px; width: 720px">
  {AT2.format(c='#FFFFFF')}
{disc(540,460,250,'j',500,pop=280)}
  <img src="{u('estrela')}" alt="" aria-hidden="true" style="position: absolute; left: 200px; top: 560px; width: 140px">
  <div style="position: absolute; left: 50%; top: 780px; transform: translateX(-50%); width: 720px; background: #FFFFFF; border-radius: 30px; padding: 30px 40px; box-sizing: border-box; text-align: center; color: #05316E; box-shadow: 0 30px 60px -20px rgba(0,0,0,0.55)">
    <div style="font-family: Anton, sans-serif; font-size: 76px; line-height: 1; text-transform: uppercase">Pergunte ao <span style="color: #FF7A1A">vereador!</span></div>
    <div style="font-size: 26px; font-weight: 600; margin: 12px 0 20px">Tem alguma dúvida ou sugestão?</div>
    <div style="display: inline-block; background: #FFC20E; border-radius: 40px; padding: 14px 34px; font-weight: 800; font-size: 24px">Mande nos comentários</div>
  </div>
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
