# Al Kántara Group v2 · brand book + manual de marca (conta Pedro, 16/11/2026)
# Referências copiadas (composição): Lippincott (serifada editorial gigante em títulos e manifesto),
# Wolff Olins / Blank Street (aplicação física como protagonista: fachada, placas, mockups) e
# Landor (marca gigante cortada na borda da página = símbolo recortado nas capas). Detalhes no TEMPLATE.md.
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from simbolo import pecas, path, KEY
from conteudo import *
B = os.path.abspath(os.path.dirname(__file__) + '/..')
INK, LIME, STONE, BRASS, GRAPH = '#0B0C0E', '#EFEAE1', '#8E8A82', '#B8955A', '#1A1C20'
DIV = [('Labs', '#2E4BFF', 'IA e software', 'Dublê · Central de Comando · VEKTOR'),
       ('Studio', '#E8461E', 'Marca, design e vendas', 'Lindson Almeida Studio · Apps SDR'),
       ('Media', '#F0A202', 'Canais e audiência', 'Passaporte da Bíblia · Raposa e Leão'),
       ('Ventures', '#0E8C66', 'Negócios próprios', 'Orégano Turbo · Estado Próprio')]

def K(s, cor=INK, idx=None, dc=None, ox=0, oy=0, extra=''):
    ps = ''.join(f'<path fill="{dc if (idx is not None and i == idx) else cor}" d="{path(p, s, 0, 0)}"/>' for i, p in enumerate(pecas()))
    return f'<svg viewBox="0 0 {24*s} {24*s}" width="{24*s}" height="{24*s}" style="{extra}">{ps}</svg>'
def logo(kind='horizontal', var='negativo', h=60, extra=''):
    return f'<img src="../logos/svg/alkantara-{kind}-{var}.svg" style="height:{h}px;{extra}">'
def divlogo(d, var='negativo', h=60):
    return f'<img src="../logos/svg/alkantara-div-{d.lower()}-horizontal-{var}.svg" style="height:{h}px">'

CSS = f'''
@font-face{{font-family:F;src:url(../fontes/Fraunces-Regular.ttf);font-weight:400}}
@font-face{{font-family:F;src:url(../fontes/Fraunces-SemiBold.ttf);font-weight:600}}
@font-face{{font-family:I;src:url(../fontes/InterTight-Medium.ttf);font-weight:500}}
@font-face{{font-family:I;src:url(../fontes/InterTight-SemiBold.ttf);font-weight:600}}
@page{{size:1920px 1080px;margin:0}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:#222;font-family:I;-webkit-font-smoothing:antialiased}}
.pg{{width:1920px;height:1080px;position:relative;overflow:hidden;page-break-after:always;background:{INK};color:{LIME}}}
.pg.l{{background:{LIME};color:{INK}}}
.pg.s{{background:{GRAPH}}}
.grain:after{{content:"";position:absolute;inset:0;pointer-events:none;opacity:.10;mix-blend-mode:overlay;
 background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='300'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='3'/%3E%3C/filter%3E%3Crect width='300' height='300' filter='url(%23n)'/%3E%3C/svg%3E")}}
.hd{{position:absolute;left:120px;right:120px;top:56px;display:flex;justify-content:space-between;font:500 13px 'JetBrains Mono';letter-spacing:.14em;text-transform:uppercase;opacity:.62}}
.ft{{position:absolute;left:120px;right:120px;bottom:48px;display:flex;justify-content:space-between;font:500 13px 'JetBrains Mono';letter-spacing:.14em;text-transform:uppercase;opacity:.5}}
.mono{{font:500 14px 'JetBrains Mono';letter-spacing:.14em;text-transform:uppercase}}
.ey{{font:500 15px 'JetBrains Mono';letter-spacing:.18em;text-transform:uppercase;color:{BRASS}}}
.h1{{font:400 168px/0.92 F;letter-spacing:-.035em}}
.h2{{font:400 92px/1 F;letter-spacing:-.03em}}
.h3{{font:400 50px/1.05 F;letter-spacing:-.02em}}
.it{{font-style:italic}}
.p{{font:500 21px/1.5 I;opacity:.78;max-width:620px}}
.ps{{font:500 17px/1.5 I;opacity:.72}}
.big{{font:600 22px/1.3 I}}
.rule{{height:1px;background:currentColor;opacity:.22}}
.col{{position:absolute}}
.chip{{display:inline-block;padding:7px 12px;border:1px solid currentColor;border-radius:99px;font:500 12px 'JetBrains Mono';letter-spacing:.12em;text-transform:uppercase;opacity:.8}}
.card{{border-radius:4px;overflow:hidden;position:relative}}
.num{{font:400 260px/0.8 F;letter-spacing:-.05em}}
'''
pages = {'book': [], 'manual': []}
cur = ['book']
def P(body, cls='', sec='', n=None):
    lst = pages[cur[0]]; n = len(lst) + 1
    doc = 'Brand Book' if cur[0] == 'book' else 'Manual de Identidade'
    hd = f'<div class="hd"><span>Al Kántara Group · {doc}</span><span>{sec}</span></div><div class="ft"><span>v2 · 2026</span><span>{n:02d}</span></div>' if sec != 'none' else ''
    lst.append(f'<section class="pg grain {cls}">{body}{hd}</section>')

# ---------- elementos de cena ----------
def juntas(cor=LIME, op=.12, sc=1):
    # as 3 juntas do K estendidas como linhas de construção pela página
    return f'''<svg class="col" style="left:0;top:0" width="1920" height="1080"><g stroke="{cor}" stroke-opacity="{op}" stroke-width="1" fill="none">
<line x1="760" y1="0" x2="760" y2="1080"/><line x1="760" y1="540" x2="1400" y2="-150"/><line x1="760" y1="540" x2="1330" y2="1230"/></g></svg>'''
def corte(s, x, y, cor, op=1, idx=None, dc=None, rot=0):
    return f'<div class="col" style="left:{x}px;top:{y}px;opacity:{op};transform:rotate({rot}deg)">{K(s, cor, idx, dc)}</div>'
def chapa(w, h, fundo, conteudo, rx=0, ry=0, rz=0, sh=.55, extra=''):
    return f'''<div style="width:{w}px;height:{h}px;background:{fundo};transform:perspective(2400px) rotateX({rx}deg) rotateY({ry}deg) rotateZ({rz}deg);
box-shadow:0 2px 2px rgba(0,0,0,.25),0 30px 60px -10px rgba(0,0,0,{sh}),0 80px 120px -40px rgba(0,0,0,{sh});position:relative;overflow:hidden;{extra}">{conteudo}
<div style="position:absolute;inset:0;background:linear-gradient(115deg,rgba(255,255,255,.10),rgba(255,255,255,0) 40%,rgba(0,0,0,.10));pointer-events:none"></div></div>'''
MESA = f'background:radial-gradient(1200px 700px at 30% 20%,#2b2d31,#121315 60%,#0a0a0b);'
MESA_CLARA = 'background:radial-gradient(1300px 800px at 35% 25%,#e9e4da,#cfc8bb 65%,#b9b2a4);'

exec(open(os.path.dirname(__file__) + '/paginas_book.py').read())
cur[0] = 'manual'
exec(open(os.path.dirname(__file__) + '/paginas_manual.py').read())

os.makedirs(B + '/paginas', exist_ok=True)
for k, lst in pages.items():
    open(f'{B}/paginas/{k}.html', 'w').write(f'<!doctype html><meta charset=utf-8><style>{CSS}</style>' + ''.join(lst))
    print(k, len(lst))
