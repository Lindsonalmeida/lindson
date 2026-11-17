# Carrosseis "Economist 2027" (serie Previsoes e Premonicoes, Raposa e Leao). Designer grafico, 17/11/2026.
# Identidade: raposa-e-leao/IDENTIDADE.md (Noite, Ouro, Anton, Cinzel, 1 tarja Sangue). Tom sensacionalista
# pedido pelo Lindson, mas teoria sempre como pergunta/"a internet diz" e tela final "o que a revista diz".
# Composicoes copiadas (TEMPLATE.md): dossie de evidencia com circulo/seta (estilo explicador de mistério tipo
# Vox/"Unsolved"), numero gigante em contorno (Brut/Nexo listicle), split teoria x fato (checagem tipo Lupa/AFP).
import os, sys, json
from PIL import Image, ImageFilter, ImageEnhance
D = os.path.dirname(os.path.abspath(__file__)); CAP = sys.argv[1]  # pasta com q0..q5.png (recortes da capa)
R = os.path.join(D, '..', '..', 'raposa-e-leao', 'img'); os.makedirs(os.path.join(D, '_tmp'), exist_ok=True)
CROPS = {
 'espaco':('q0',(180,300,470,568)),'satelite':('q0',(190,330,345,535)),'astronauta':('q0',(320,320,430,410)),
 'iceberg':('q0',(430,300,610,440)),'lideres':('q0',(500,190,776,300)),'torre':('q0',(690,300,776,470)),
 'camelo':('q1',(190,290,500,450)),'aviao':('q1',(40,370,270,460)),'colunas':('q0',(480,450,740,568)),
 'china':('q2',(60,20,290,240)),'megafone':('q2',(270,20,410,180)),'agentes':('q2',(370,110,530,240)),
 'cybertruck':('q2',(550,130,740,215)),'robo':('q2',(270,200,480,335)),'incendio':('q2',(55,200,290,420)),
 'cofre':('q2',(495,205,615,305)),'seringa':('q2',(590,270,680,460)),'comprimidos':('q2',(495,290,610,430)),
 'chuva':('q2',(230,280,520,470)),'cerebro':('q2',(650,195,776,345)),'cientista':('q2',(640,380,776,530)),
 'indiagate':('q2',(385,320,505,475)),'grafico':('q3',(0,0,190,110)),'ampulheta':('q3',(245,20,335,140)),
 'cavaleiro':('q3',(330,30,490,165)),'kremlin':('q3',(440,0,665,210)),'pen':('q3',(0,110,230,235)),
 'marianne':('q3',(90,150,350,480)),'duto':('q3',(320,215,680,300)),'urna':('q3',(380,280,620,460)),
 'batom':('q3',(0,400,220,505)),'cacas':('q3',(330,480,660,568)),'guerra':('q4',(300,0,776,115)),
 'tanques':('q4',(540,30,776,110)),'lobos':('q4',(200,120,500,245)),'telescopio':('q4',(590,160,735,310)),
 'cristal':('q5',(0,130,250,335)),'peoes':('q5',(0,240,330,335)),'navio':('q5',(200,0,620,195)),
 'barril':('q5',(310,140,520,315)),'barracas':('q4',(440,275,745,415)),'misseis':('q2',(60,420,330,568)),
}
EX={'misseis','tanques','lideres'}
for k,(f,b) in CROPS.items():
    src = Image.open(os.path.join(CAP, f+'.png')).convert('RGB'); k2=0.5 if k in EX else 0.85; cx,cy=(b[0]+b[2])/2,(b[1]+b[3])/2; w,h=(b[2]-b[0])*k2+40,(b[3]-b[1])*k2+40
    im = src.crop((max(0,int(cx-w)),max(0,int(cy-h)),min(src.width,int(cx+w)),min(src.height,int(cy+h))))
    s = 900/max(im.size); im = im.resize((int(im.width*s), int(im.height*s)), Image.LANCZOS)
    im = im.filter(ImageFilter.UnsharpMask(3, 160, 2)); im = ImageEnhance.Contrast(im).enhance(1.15)
    im.save(os.path.join(D, '_tmp', k+'.jpg'), quality=88)
for p in ['maquiavel.jpg','cesar.jpg','borgia.jpg','lorenzo.jpg']:
    Image.open(os.path.join(R,p)).convert('L').resize((700, int(700*Image.open(os.path.join(R,p)).height/Image.open(os.path.join(R,p)).width))).save(os.path.join(D,'_tmp','r_'+p),quality=85)
C = json.load(open(os.path.join(D, 'roteiro.json'), encoding='utf-8'))
CR = '<div class="cr">Recorte: The Economist · The World Ahead 2027</div>'
def img(k): return f'_tmp/{k}.jpg'
def g(t):  # **palavra** em ouro, [[x]] tarja
    import re; t = re.sub(r'\*\*(.+?)\*\*', r'<b class="o">\1</b>', t); return re.sub(r'\[\[(.+?)\]\]', r'<span class="tj">\1</span>', t)
def topo(n, tot, et): return f'<div class="tp"><span>{et}</span><span>{n:02d}/{tot:02d}</span></div>'
SELO = '<div class="selo"><i>R</i> RAPOSA E LEÃO · PREVISÕES E PREMONIÇÕES</div>'
def cont(t): return f'<div class="cont">{t} <em>→</em></div>' if t else ''
def tela(cid, i, tot, s):
    L = s['l']; h = ''; e = s.get('et', 'THE ECONOMIST · 2027')
    if L == 'capa':
        h = f'''<img class="rt" src="_tmp/r_{s["retrato"]}"><div class="glow"></div>
        <div class="ev cap" style="transform:rotate(-4deg)"><img src="{img(s["img"])}"><div class="circ" style="{s.get("c","left:40%;top:30%")}"></div></div>
        <div class="alerta">⚠ {s["alerta"]}</div><h1 class="hcap">{g(s["t"])}</h1><p class="sub">{g(s["sub"])}</p>{CR}'''
    elif L == 'dossie':
        h = f'''<div class="ev big"><img src="{img(s["img"])}"><div class="circ" style="{s.get("c","left:35%;top:25%")}"></div><div class="seta" style="{s.get("a","left:62%;top:8%")}">↙</div></div>{CR}
        <div class="num">{s.get("n","")}</div><h2>{g(s["t"])}</h2><p class="tx">{g(s["tx"])}</p>'''
    elif L == 'split':
        h = f'''<div class="sp"><div class="ev tall"><img src="{img(s["img"])}"><div class="circ" style="{s.get("c","left:30%;top:30%")}"></div></div>
        <div class="spt"><div class="num s">{s.get("n","")}</div><h2>{g(s["t"])}</h2><p class="tx">{g(s["tx"])}</p></div></div>{CR}'''
    elif L == 'giga':
        h = f'''<div class="giga">{s["g"]}</div><div class="lupa"><img src="{img(s["img"])}"></div>{CR}
        <h2 class="gh">{g(s["t"])}</h2><p class="tx gtx">{g(s["tx"])}</p>'''
    elif L == 'versus':
        h = f'''<h2 class="vh">{g(s["t"])}</h2><div class="ev mid"><img src="{img(s["img"])}"><div class="circ" style="{s.get("c","left:40%;top:25%")}"></div></div>{CR}
        <div class="vs"><div class="vc r"><small>A INTERNET DIZ</small>{g(s["teoria"])}</div><div class="vc f"><small>O QUE SE SABE</small>{g(s["fato"])}</div></div>'''
    elif L == 'grade':
        cs = ''.join(f'<div class="gi"><img src="{img(k)}"><span>{lb}</span></div>' for k, lb in s['itens'])
        h = f'''<h2 class="vh">{g(s["t"])}</h2><div class="grd">{cs}</div>{CR}<p class="tx">{g(s["tx"])}</p>'''
    elif L == 'frase':
        h = f'''<img class="rt2" src="_tmp/r_{s["retrato"]}"><div class="glow g2"></div><div class="ev mini"><img src="{img(s["img"])}"></div>
        <blockquote>{g(s["q"])}</blockquote><cite>{s["fonte"]}</cite><p class="tx fx">{g(s["tx"])}</p>{CR}'''
    elif L == 'fim':
        ms = ''.join(f'<li><b>{a}</b> {b}</li>' for a, b in s['manchetes'])
        h = f'''<div class="fimtop">O QUE A REVISTA <b class="o">REALMENTE</b> DIZ</div><ul class="mn">{ms}</ul>
        <p class="tx fz">{g(s["tx"])}</p><div class="cta">{g(s["cta"])}</div>'''
    return f'<section class="f" id="{cid}-{i:02d}"><div class="gr"></div><div class="vg"></div>{topo(i, tot, e)}{h}{cont(s.get("prox",""))}{SELO}</section>'
CSS = open(os.path.join(D, 'estilo.css')).read()
out = ['<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Anton&family=Cinzel:wght@600;800&family=Cormorant+Garamond:ital,wght@1,600&family=Inter:wght@500;700;800&display=swap" rel="stylesheet"><style>'+CSS+'</style></head><body>']
for c in C:
    for i, s in enumerate(c['telas'], 1): out.append(tela(c['id'], i, len(c['telas']), s))
open(os.path.join(D, 'pecas.html'), 'w').write('\n'.join(out) + '</body></html>')
