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
def F(id, inner, bg, topo=False):
    frames.append(f'<section class="f" id="{id}" style="{bg}">{band(0) if topo else ""}{inner}{band(1254)}<div class="noise"></div></section>')

NAVY = f'background:radial-gradient(70% 60% at 85% 10%,#1D4FB8 0,transparent 60%),linear-gradient(180deg,{MAR} 0,#021440 100%)'
SOLLAR = f'background:radial-gradient(70% 55% at 55% 45%,#FFF1B0 0,transparent 60%),linear-gradient(180deg,#FFD23A 0,{SOL} 40%,{LAR} 100%)'
LOGO_Y = 1030
def coluna(left, top, linhas, script, escuro):
    sh = 'text-shadow:6px 6px 0 rgba(255,255,255,.75)' if not escuro else f'text-shadow:6px 6px 0 {DEEP}'
    h = ''.join(f'<div class="H2" style="color:{c};{sh}">{t}</div>' for t, c in linhas)
    sc = f'<div class="script2" style="color:{"#fff" if escuro else MAR}">{script}</div>{sublinha(380)}' if script else ''
    return f'<div class="a" style="left:{left}px;top:{top}px">{h}{sc}</div>'

def rays(cx, cy, cor, op, a=200, e=700):
    return (f'<div class="a" style="inset:0;opacity:{op};background:repeating-conic-gradient(from 4deg at {cx}px {cy}px,{cor} 0 3.2deg,transparent 3.2deg 12.86deg);'
            f'-webkit-mask:radial-gradient(circle at {cx}px {cy}px,transparent {a}px,#000 {a+40}px,#000 {e*.55:.0f}px,transparent {e}px)"></div>')

# 1 · DIVIDIDO (aprovado) · amarelo
F('v12-1-dividido', f"""{DOTS_SOL}{burst(300, 400, 'rgba(255,255,255,.55)')}
{foto('f23-original', 300, 290, 270)}
{coluna(590, 190, [('A GENTE', ROY), ('NÃO', MAR), ('PROMETE,', MAR)], 'volta pra mostrar', False)}
{logo(600, LOGO_Y, 260)}""", AMARELO, topo=True)

# 2 · PALAVRA GIGANTE · azul
F('v12-2-palavra', f"""{DOTS_AZUL}{rays(600, 560, SOL, .4)}
<div class="a Hg" style="left:0;right:0;top:120px">PRESENÇA</div>
{foto('f20-original', 270, 600, 400)}
<div class="a script2" style="right:80px;top:1110px;color:#fff;font-size:60px">todo dia, em todo canto</div>
{logo(86, LOGO_Y, 260)}""", AZUL)

# 3 · FRASE · sol nascendo sobre a maré · marinho
F('v12-3-frase', f"""
<div class="a" style="left:560px;top:-150px;width:820px;height:820px;border-radius:50%;background:radial-gradient(circle at 40% 38%,#FFF7DA 0,#FFE27A 22%,{SOL} 50%,{LAR} 100%)"></div>
<svg class="a" viewBox="0 0 1080 1350" style="left:0;top:0;width:1080px;height:1350px"><path d="M-20 560 Q540 400 1100 540 V1350 H-20Z" fill="{MARE}"/><path d="M-20 610 Q540 460 1100 600 V1350 H-20Z" fill="{ROY}"/><path d="M-20 660 Q540 530 1100 670 V1350 H-20Z" fill="{MAR}"/></svg>
{foto('f08-original', 300, 780, 600)}
<div class="a qm">“</div>
<div class="a" style="left:86px;top:250px"><div class="H2" style="color:#fff;font-size:96px;text-shadow:5px 5px 0 #021440">A GENTE NÃO</div><div class="H2" style="color:#fff;font-size:96px;text-shadow:5px 5px 0 #021440">PROMETE.</div>
<div class="script2" style="color:{SOL};font-size:58px">a gente volta pra mostrar</div></div>
{logo(86, LOGO_Y, 260)}""", NAVY)

# 4 · CONVERSA · WhatsApp · azul
F('v12-4-conversa', f"""{DOTS_AZUL}{rays(800, 460, SOL, .35)}
{foto('f10-original', 280, 810, 330)}
{coluna(80, 130, [('FALA COM', '#fff'), ('A GENTE!', SOL)], None, True)}
<div class="a chat" style="left:86px;top:390px">
 <div class="msg in">Oi! Manda sua demanda com foto e endereço 👋</div>
 <div class="msg out">A rua da escola tá sem luz.</div>
 <div class="msg in">Anotado. A gente leva pra Câmara e volta com resposta ✅</div>
 <div class="num">WhatsApp do gabinete · <b>(98) 9 0000-0000</b></div>
</div>
{logo(86, LOGO_Y, 260)}""", AZUL)

# 5 · AGENDA · amarelo
AG = [('SEG', 'Povoado Ilha Grande', 'Escuta com pescadores'), ('QUA', 'Câmara Municipal', 'Sessão ordinária'), ('SEX', 'Praça da Matriz', 'Gabinete na rua')]
F('v12-5-agenda', f"""{DOTS_SOL}{burst(780, 420, 'rgba(255,255,255,.55)')}
{foto('f12-original', 280, 790, 280)}
{coluna(80, 150, [('ONDE A', MAR), ('GENTE VAI.', ROY)], None, False)}
<div class="a" style="left:86px;top:430px;display:grid;gap:16px;width:470px">{''.join(f'<div class="ag"><em>{a}</em><p><b>{b}</b>{c}</p></div>' for a,b,c in AG)}</div>
{logo(86, LOGO_Y, 260)}""", AMARELO, topo=True)

# 6 · BOM DIA · close · sol→laranja
F('v12-6-bom-dia', f"""{rays(590, 560, '#FFFFFF', .5, 260, 900)}
<div class="a script2" style="left:0;right:0;top:24px;text-align:center;color:#fff;font-size:104px;transform:rotate(-5deg);text-shadow:0 5px 0 {MAR}">Bom dia,</div>
<div class="a H2" style="left:0;right:0;top:205px;text-align:center;color:{MAR};font-size:92px;text-shadow:5px 5px 0 rgba(255,255,255,.7)">SÃO JOÃO BATISTA!</div>
{foto('f24-original', 500, 600, 470)}
{logo(86, LOGO_Y, 260)}""", SOLLAR)
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
.Hg{{font-family:Anton;font-size:250px;line-height:1;text-align:center;color:{SOL};text-shadow:8px 8px 0 #021440;letter-spacing:.01em}}
.qm{{left:80px;top:40px;font-family:Anton;font-size:260px;line-height:1;color:{SOL}}}
.chat{{width:520px;display:flex;flex-direction:column;gap:14px}}.msg{{max-width:88%;padding:16px 20px;border-radius:22px;font-weight:700;font-size:24px;line-height:1.3;color:#132;box-shadow:0 6px 14px rgba(0,0,0,.18)}}.msg.in{{background:#fff;border-top-left-radius:6px}}.msg.out{{background:#DCF8C6;align-self:flex-end;border-top-right-radius:6px}}
.num{{white-space:nowrap;margin-top:6px;background:#25D366;color:#fff;border-radius:100px;padding:12px 22px;font-weight:700;font-size:22px;align-self:flex-start}}.num b{{font-weight:900}}
.ag{{display:flex;align-items:center;gap:18px;background:#fff;border-radius:22px;padding:14px;color:{MAR};box-shadow:0 8px 18px rgba(120,60,0,.15)}}.ag em{{font-style:normal;width:80px;height:80px;flex:none;border-radius:16px;background:{MAR};display:grid;place-items:center;font-family:Anton;font-size:30px;color:{SOL}}}.ag b{{display:block;font-size:28px;font-weight:900}}.ag p{{font-size:20px;font-weight:600;color:{ROY}}}
.zap{{background:#25D366;color:#fff;border-radius:20px;padding:14px 24px;font-weight:800;font-size:22px;letter-spacing:.04em;box-shadow:0 10px 24px rgba(0,0,0,.25)}}
.zap b{{display:block;font-size:40px;font-weight:900;letter-spacing:0;margin-top:2px}}
'''
open(os.path.join(d, 'artes.html'), 'w').write(f'<!doctype html><html><head><meta charset="utf-8"><title>v12</title><style>{CSS}</style></head><body>{"".join(frames)}</body></html>')
print(len(frames))
