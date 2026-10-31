# v11 · estilo aprovado (teste B): faixas de padrão topo/base, foto grande de um lado, título condensado
# empilhado do outro, frase manuscrita com traço laranja, raios atrás da cabeça.
# Ajustes: logo PRINCIPAL oficial (extraída do manual) com fumaça marinho atrás, fotos reais do álbum
# posicionadas pelo rosto, sem bandeirinhas, variação amarelo/azul e lado da foto.
import os, json
d = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(d, 'icons.py')).read())
ROY, MAR, SOL, LAR, MARE, DEEP = '#2350F5', '#05316E', '#FFC20E', '#FF7A1A', '#08BDFF', '#0A1F7A'
R = json.load(open(os.path.join(d, 'rostos.json')))
NOISE = ("url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='240' height='240'%3E%3Cfilter id='n'%3E"
         "%3CfeTurbulence type='fractalNoise' baseFrequency='.95' numOctaves='2' stitchTiles='stitch'/%3E%3C/filter%3E"
         "%3Crect width='240' height='240' filter='url(%23n)'/%3E%3C/svg%3E\")")

def icon(name, color, size):
    return (f'<svg viewBox="0 0 100 100" width="{size}" height="{size}" fill="none" stroke="{color}" stroke-width="8" '
            f'stroke-linecap="round" stroke-linejoin="round">{ICONS[name]}</svg>')

def band(top):
    # faixa de padrão da marca — sem bandeirinhas
    tiles = [(MAR, icon('Lagos', SOL, 54)), (SOL, f'<b style="color:{MAR}">DO POVO,<br>PRO POVO!</b>'),
             (ROY, '<img src="assets/sol.png" style="height:62px">'), ('#FFF4D6', icon('Pesca', MAR, 56)),
             (LAR, '<b style="color:#fff">SÃO JOÃO<br>BATISTA</b>'), (MAR, icon('Obras', SOL, 54)),
             ('#FFF4D6', f'<b style="color:{ROY}">A GENTE<br>VOLTA!</b>'), (ROY, icon('Povo', '#fff', 58))]
    return f'<div class="band" style="top:{top}px">' + ''.join(f'<div style="background:{b}">{c}</div>' for b, c in tiles) + '</div>'

def foto(nome, fw, cx, ftop):
    r = R[nome]; s = fw / r['fw']
    return (f'<img class="a pp" src="recortes/{nome}.png" style="left:{cx-(r["fx"]+r["fw"]/2)*s:.0f}px;'
            f'top:{ftop-r["fy"]*s:.0f}px;width:{r["W"]*s:.0f}px">')

def burst(cx, cy, cor):
    return (f'<div class="a" style="left:{cx-450}px;top:{cy-450}px;width:900px;height:900px;background:repeating-conic-gradient(from 0deg at 50% 50%,{cor} 0 1.4deg,transparent 1.4deg 9deg);'
            f'-webkit-mask:radial-gradient(circle,transparent 0 190px,#000 210px,transparent 70%)"></div>')

def fumaca(cx, cy, w, h, op=.92):
    return (f'<svg class="a" viewBox="0 0 {w} {h}" style="left:{cx-w/2}px;top:{cy-h/2}px;width:{w}px;height:{h}px;overflow:visible">'
            f'<defs><filter id="fm{cx}{cy}" x="-50%" y="-80%" width="200%" height="260%"><feTurbulence type="fractalNoise" baseFrequency=".012 .024" numOctaves="3" seed="5"/>'
            f'<feDisplacementMap in="SourceGraphic" scale="100"/><feGaussianBlur stdDeviation="30"/></filter></defs>'
            f'<g filter="url(#fm{cx}{cy})"><ellipse cx="{w*.5}" cy="{h*.52}" rx="{w*.38}" ry="{h*.32}" fill="{DEEP}" opacity="{op}"/>'
            f'<ellipse cx="{w*.42}" cy="{h*.46}" rx="{w*.24}" ry="{h*.2}" fill="{MAR}" opacity="{op}"/></g></svg>')

def logo(left, top, w=300):
    h = w * 1460 / 1966
    return fumaca(left + w / 2, top + h / 2, w * 1.9, h * 1.9) + f'<img class="a" src="marca/logo_principal.png" style="left:{left}px;top:{top}px;width:{w}px">'

def sublinha(w=440):
    return f'<svg viewBox="0 0 500 40" width="{w}" style="display:block;margin:-4px 0 0 6px"><path d="M6 28 C150 8 330 6 494 16" stroke="{LAR}" stroke-width="12" fill="none" stroke-linecap="round"/></svg>'

AMARELO = f'background:{SOL}'
AZUL = f'background:radial-gradient(75% 60% at 50% 40%,#3A68FF 0,{ROY} 38%,#1838C4 70%,{DEEP} 100%)'
DOTS_SOL = '<div class="a dots" style="background:radial-gradient(circle,rgba(180,90,0,.13) 1.6px,transparent 2px) 0 0/14px 14px"></div>'
DOTS_AZUL = '<div class="a dots" style="background:radial-gradient(circle,rgba(255,255,255,.08) 1.6px,transparent 2px) 0 0/14px 14px"></div>'

frames = []
def F(id, inner, bg):
    frames.append(f'<section class="f" id="{id}" style="{bg}">{inner}<div class="noise"></div></section>')

def coluna(left, top, linhas, script, escuro):
    sh = 'text-shadow:6px 6px 0 rgba(255,255,255,.75)' if not escuro else f'text-shadow:6px 6px 0 {DEEP}'
    h = ''.join(f'<div class="H2" style="color:{c};{sh}">{t}</div>' for t, c in linhas)
    sc = f'<div class="script2" style="color:{"#fff" if escuro else MAR}">{script}</div>{sublinha(380)}' if script else ''
    return f'<div class="a" style="left:{left}px;top:{top}px">{h}{sc}</div>'

# 1 · amarelo · foto à esquerda (layout aprovado) · logo principal sob o texto
F('v11-1-volta-pra-mostrar', f'''{band(0)}{DOTS_SOL}{burst(300, 380, 'rgba(255,255,255,.55)')}
{foto('f23-original', 300, 290, 250)}
{coluna(590, 180, [('A GENTE', ROY), ('NÃO', MAR), ('PROMETE,', MAR)], 'volta pra mostrar', False)}
{logo(600, 850)}
{band(1254)}''', AMARELO)

# 2 · azul · foto à direita · texto à esquerda
F('v11-2-do-povo', f'''{band(0)}{DOTS_AZUL}{burst(760, 400, 'rgba(255,194,14,.45)')}
{foto('f08-original', 300, 770, 270)}
{coluna(80, 180, [('DO POVO,', '#fff'), ('PRO POVO.', SOL)], 'um mandato de presença', True)}
{logo(86, 880)}
{band(1254)}''', AZUL)

# 3 · amarelo · foto à esquerda acenando · texto à direita
F('v11-3-chega-cedo', f'''{band(0)}{DOTS_SOL}{burst(330, 360, 'rgba(255,255,255,.55)')}
{foto('f28-amarelo', 280, 330, 230)}
<div class="a script2" style="left:600px;top:170px;color:{MAR};font-size:60px">Quem caminha junto</div>
{coluna(600, 260, [('CHEGA', ROY), ('CEDO.', MAR)], None, False)}
{logo(610, 860)}
{band(1254)}''', AMARELO)

# 4 · azul · foto à direita com celular · WhatsApp
F('v11-4-whatsapp', f'''{band(0)}{DOTS_AZUL}{burst(770, 420, 'rgba(255,194,14,.45)')}
{foto('f10-original', 290, 790, 300)}
{coluna(80, 180, [('FALA COM', '#fff'), ('A GENTE!', SOL)], None, True)}
<div class="a zap" style="left:86px;top:470px">WhatsApp do gabinete<b>(98) 9 0000-0000</b></div>
{logo(86, 900)}
{band(1254)}''', AZUL)

CSS = f'''
@import url('https://fonts.googleapis.com/css2?family=Anton&family=Montserrat:wght@700;800;900&family=Kaushan+Script&display=swap');
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:#111;display:flex;flex-wrap:wrap;gap:40px;padding:40px;font-family:Montserrat}}
.f{{position:relative;width:1080px;height:1350px;overflow:hidden;color:#fff;flex:none}}
.a{{position:absolute}}
.noise{{position:absolute;inset:0;background:{NOISE};opacity:.07;mix-blend-mode:overlay;pointer-events:none}}
.pp{{filter:drop-shadow(0 24px 30px rgba(0,0,0,.28))}}
.band{{position:absolute;left:0;right:0;height:96px;display:grid;grid-template-columns:repeat(8,1fr);z-index:3}}
.band div{{display:grid;place-items:center;text-align:center;font-family:Anton;font-size:24px;line-height:.95}}
.band b{{font-weight:400}}
.dots{{left:0;right:0;top:96px;bottom:96px}}
.H2{{font-family:Anton;font-size:118px;line-height:1.0;white-space:nowrap}}
.script2{{font-family:'Kaushan Script';font-size:64px;margin-top:14px;transform:rotate(-4deg);white-space:nowrap}}
.zap{{background:#25D366;color:#fff;border-radius:20px;padding:14px 24px;font-weight:800;font-size:22px;letter-spacing:.04em;box-shadow:0 10px 24px rgba(0,0,0,.25)}}
.zap b{{display:block;font-size:40px;font-weight:900;letter-spacing:0;margin-top:2px}}
'''
open(os.path.join(d, 'artes.html'), 'w').write(f'<!doctype html><html><head><meta charset="utf-8"><title>v11</title><style>{CSS}</style></head><body>{"".join(frames)}</body></html>')
print(len(frames))
