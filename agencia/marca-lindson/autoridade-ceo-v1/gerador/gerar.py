# Plano de Comunicação de Autoridade · Lindson Almeida CEO · v1 (conta Leandro, 25/11/2026)
# Visual: Al Kántara Group v2.1 (Fraunces + Inter Tight + JetBrains Mono, Tinta/Calcário/Grafite, Latão só detalhe).
# Composição copiada de: CT Group (UK, política como UMA prática de uma consultoria), Marcelo Vitorino (BR, retrato
# editorial + cargo claro) e Debbie Millman / Marty Neumeier (US, nome gigante + frase-tese assinada). Ver TEMPLATE.md.
import os, sys, json
H = os.path.abspath(os.path.dirname(__file__))
B = os.path.abspath(H + '/..')
AK = os.path.abspath(B + '/../../marca-holding/v2')
sys.path.insert(0, AK + '/gerador')
from simbolo import pecas, path
sys.path.insert(0, H)
from conteudo import *

INK, LIME, STONE, BRASS, GRAPH = '#0B0C0E', '#EFEAE1', '#8E8A82', '#B8955A', '#1A1C20'
DIVC = {'Labs': '#2E4BFF', 'Barzakh': '#E8461E', 'Media': '#F0A202', 'Ventures': '#0E8C66'}
F = 'file://' + AK

def K(s, cor=INK, idx=None, dc=None):
    ps = ''.join(f'<path fill="{dc if (idx is not None and i == idx) else cor}" d="{path(p, s, 0, 0)}"/>' for i, p in enumerate(pecas()))
    return f'<svg viewBox="0 0 {24*s} {24*s}" width="{24*s}" height="{24*s}">{ps}</svg>'
def corte(s, x, y, cor, op=1, idx=None, dc=None):
    return f'<div class="col" style="left:{x}px;top:{y}px;opacity:{op}">{K(s, cor, idx, dc)}</div>'
def logo(kind='horizontal', var='negativo', h=44):
    return f'<img src="{F}/logos/svg/alkantara-{kind}-{var}.svg" style="height:{h}px">'

CSS = f'''
@font-face{{font-family:F;src:url({F}/fontes/Fraunces-Regular.ttf);font-weight:400}}
@font-face{{font-family:F;src:url({F}/fontes/Fraunces-SemiBold.ttf);font-weight:600}}
@font-face{{font-family:F;font-style:italic;src:url("{F}/fontes/Fraunces-Italic%5BSOFT,WONK,opsz,wght%5D.ttf")}}
@font-face{{font-family:I;src:url({F}/fontes/InterTight-Medium.ttf);font-weight:500}}
@font-face{{font-family:I;src:url({F}/fontes/InterTight-SemiBold.ttf);font-weight:600}}
@font-face{{font-family:M;src:url({F}/fontes/JetBrainsMono-Medium.ttf);font-weight:500}}
@page{{size:1920px 1080px;margin:0}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:#222;font-family:I;-webkit-font-smoothing:antialiased}}
.pg{{width:1920px;height:1080px;position:relative;overflow:hidden;page-break-after:always;background:{INK};color:{LIME}}}
.pg.l{{background:{LIME};color:{INK}}}
.pg.s{{background:{GRAPH}}}
.pg.b{{background:{BRASS};color:{INK}}}
.grain:after{{content:"";position:absolute;inset:0;pointer-events:none;opacity:.05;background-image:url(file://{H}/grao.png)}}
.hd{{position:absolute;left:120px;right:120px;top:52px;display:flex;justify-content:space-between;font:500 15px M;letter-spacing:.14em;text-transform:uppercase;opacity:.62}}
.ft{{position:absolute;left:120px;right:120px;bottom:44px;display:flex;justify-content:space-between;font:500 15px M;letter-spacing:.14em;text-transform:uppercase;opacity:.5}}
.ey{{font:500 18px M;letter-spacing:.18em;text-transform:uppercase;color:{BRASS}}}
.l .ey,.b .ey{{color:#7a5f30}}
.h1{{font:400 156px/0.94 F;letter-spacing:-.015em}}
.h2{{font:400 84px/1.02 F;letter-spacing:-.012em}}
.h3{{font:400 46px/1.1 F;letter-spacing:-.005em}}
.h4{{font:600 30px/1.2 F}}
.it{{font-style:italic;color:{BRASS}}}
.l .it{{color:#8a6a35}}
.b .it{{color:{INK}}}
.p{{font:500 24px/1.5 I;opacity:.88}}
.ps{{font:500 20px/1.45 I;opacity:.84}}
.pm{{font:500 17px/1.45 I;opacity:.84}}
.mono{{font:500 15px M;letter-spacing:.14em;text-transform:uppercase}}
.rule{{height:1px;background:currentColor;opacity:.22}}
.col{{position:absolute}}
.num{{font:400 230px/0.82 F;letter-spacing:-.02em}}
.tb{{width:100%;border-collapse:collapse}}
.tb td,.tb th{{text-align:left;vertical-align:top;padding:14px 18px 14px 0;border-top:1px solid rgba(127,127,127,.28);font:500 19px/1.4 I}}
.tb th{{font:500 14px M;letter-spacing:.14em;text-transform:uppercase;color:{BRASS};border-top:0;padding-bottom:10px}}
.l .tb th{{color:#7a5f30}}
.tag{{display:inline-block;padding:6px 12px;border:1px solid currentColor;font:500 13px M;letter-spacing:.14em;text-transform:uppercase}}
.box{{border:1px solid rgba(184,149,90,.55);padding:28px 30px;position:relative}}
.fill{{background:{GRAPH};padding:30px}}
.l .fill{{background:#E3DDD1}}
.q{{font:400 34px/1.25 F;font-style:italic}}
'''
pages = []
def P(body, cls='', sec=''):
    n = len(pages) + 1
    hd = (f'<div class="hd"><span>Lindson Almeida · Plano de Autoridade</span><span>{sec}</span></div>'
          f'<div class="ft"><span>v1 · 25.11.2026 · confidencial</span><span>{n:02d}</span></div>') if sec != 'none' else ''
    pages.append(f'<section class="pg grain {cls}">{body}{hd}</section>')

FOTO_CAPA = 'file://' + H + '/capa-lindson-03.jpg'
exec(open(H + '/paginas.py').read())

html = f'<!doctype html><meta charset=utf-8><style>{CSS}</style>' + ''.join(pages)
open(B + '/plano-autoridade-ceo-v1.html', 'w').write(html)
print('paginas', len(pages))
