"""Base visual das redes Al Kántara (conta Pedro, 16/11/2026). HTML -> PNG via render.js."""
import os, re, html as H
V2 = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
F = 'file://' + V2 + '/fase2/site-bio/f/'
COR = dict(grupo='#B8955A', labs='#2E4BFF', barzakh='#E8461E', media='#F0A202', ventures='#0E8C66')
IDX = dict(labs=0, barzakh=1, media=2, ventures=3, grupo=2)
NOME = dict(grupo='Al Kántara Group', labs='Al Kántara Labs', barzakh='Barzakh · um estúdio Al Kántara', media='Al Kántara Media', ventures='Al Kántara Ventures')
P = ['M0,0 L100,480 L164,480 L164,0 Z', 'M196,0 L196,199.19 L380.54,0 Z', 'M480,0 L424.16,0 L201.32,240.53 L384.39,458.93 Z', 'M360.3,480 L196,283.99 L196,480 Z']
LOGO_N = 'file://' + V2 + '/logos/svg/alkantara-horizontal-negativo.svg'
LOGO_P = 'file://' + V2 + '/logos/svg/alkantara-horizontal-positivo.svg'
def simb(acesa=2, cor='#B8955A', base='#17191d', st=''):
    return f'<svg viewBox="0 0 480 480" style="{st}">' + ''.join(f'<path fill="{cor if i==acesa else base}" d="{p}"/>' for i, p in enumerate(P)) + '</svg>'
def it(t):  # *palavra* -> itálico latão
    t = H.escape(t); return re.sub(r'\*(.+?)\*', r'<em>\1</em>', t)
CSS = f'''@font-face{{font-family:F;src:url({F}fraunces.ttf)}}@font-face{{font-family:F;font-style:italic;src:url({F}fraunces-it.woff2)}}
@font-face{{font-family:I;src:url({F}inter.ttf);font-weight:500}}@font-face{{font-family:I;src:url({F}inter-sb.ttf);font-weight:600}}@font-face{{font-family:M;src:url({F}mono.ttf)}}
*{{margin:0;padding:0;box-sizing:border-box}}body{{font:500 30px/1.4 I;-webkit-font-smoothing:antialiased;overflow:hidden}}
.pg{{position:relative;overflow:hidden}}
.esc{{background:#0B0C0E;color:#EFEAE1}}.cla{{background:#EFEAE1;color:#0B0C0E}}
.mono{{font:500 22px/1.3 M;letter-spacing:.16em;text-transform:uppercase}}
h1,h2{{font-family:F;font-weight:400;letter-spacing:-.02em}}h1 em,h2 em{{font-style:italic}}
.grao{{position:absolute;inset:0;opacity:.07;pointer-events:none;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='220' height='220'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.8' numOctaves='3'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E")}}
.faixa{{display:flex;height:6px}}.faixa i{{flex:1}}
'''
FAIXA = '<div class="faixa"><i style="background:#2E4BFF"></i><i style="background:#E8461E"></i><i style="background:#F0A202"></i><i style="background:#0E8C66"></i></div>'
def doc(w, h, corpo, extra=''):
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}{extra}</style></head><body style="width:{w}px;height:{h}px">{corpo}</body></html>'
