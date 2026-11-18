# Quadros semanais do Leo Pinto: capas-modelo feed 1080x1350 e Reels 1080x1920 no padrao v13 v3 (social media, conta Zuleide, 18/11/2026)
# Uso: python3 gerar.py <pasta com fontes, fotos, logos e mapa-sjb.json> && node render.js <pasta>
import json, sys
D = sys.argv[1] if len(sys.argv) > 1 else '.'
MAR, ROY, SOL, LAR = '#05316E', '#2350F5', '#FFC20E', '#FF7A1A'
M = json.load(open(f'{D}/mapa-sjb.json'))
BG = {'A': f"radial-gradient(1100px 1000px at 70% 38%,#4A78FF 0,#2E5BFA 26%,{ROY} 46%,#1539BE 70%,#0B2A8A 88%,#082063 100%)",
      'L': "radial-gradient(1100px 1000px at 70% 38%,#FFB347 0,#FF9A22 24%,#FF7A1A 46%,#F2600C 70%,#D9480A 88%,#B23A06 100%)"}
# id, cor, linha1, linha2, dia, hora, formato, frase, foto, (largura, x) feed, (largura, x) reels
Q = [
 ('q1-leo-no-povoado', 'L', 'LEO NO', 'POVOADO', 'SEGUNDA', '20h45', 'REELS', 'o seu povoado no Instagram', 'i-maos-abertas-branca', (700, 430), (860, 300)),
 ('q2-pediu-ta-feito', 'A', 'PEDIU?', 'TÁ FEITO.', 'TERÇA', '12h45', 'CARROSSEL', 'a gente volta pra mostrar', 'b-punho', (1000, 260), (1250, 120)),
 ('q3-olho-de-engenheiro', 'L', 'OLHO DE', 'ENGENHEIRO', 'QUINTA', '20h45', 'REELS', 'a obra explicada em 30 segundos', 'd-bracos-cruzados-branca', (860, 330), (1060, 220)),
 ('q4-gente-da-baixada', 'A', 'GENTE DA', 'BAIXADA', 'SEXTA', '12h45', 'REELS', 'quem faz a nossa terra', 'g-maos-juntas-amarela', (900, 300), (1150, 170)),
]
GRAO = ("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='3' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 .5  0 0 0 0 .5  0 0 0 0 .5  0 0 0 .9 0'/></filter><rect width='100%25' height='100%25' filter='url(%23n)'/></svg>")
CSS = """@font-face{font-family:'Kaushan Script';src:url(Kaushan.ttf)}
@font-face{font-family:Montserrat;font-weight:700;src:url(M700.ttf)}@font-face{font-family:Montserrat;font-weight:900;src:url(M900.ttf)}
*{margin:0;padding:0;box-sizing:border-box}body{background:#222}section.f{position:relative;overflow:hidden;margin:0 0 20px}
.a{position:absolute}.K{font-family:'Kaushan Script';line-height:1.05}
.B{font-family:Montserrat;font-weight:900;text-transform:uppercase;line-height:.92;letter-spacing:-.02em;white-space:nowrap}
.L{font-family:Montserrat;font-weight:700;text-transform:uppercase;letter-spacing:.3em;white-space:nowrap}
.caixa{display:inline-block;padding:16px 26px 6px;box-shadow:0 24px 40px -22px rgba(2,12,50,.7)}"""

def arte(q, W, H, reels):
    id_, cor, l1, l2, dia, hora, fmt, frase, foto, pf, pr = q
    w, x = pr if reels else pf
    top = 250 if reels else 130
    fs = 150 if reels else 128
    b1 = SOL if cor == 'A' else MAR
    t1 = MAR if cor == 'A' else '#fff'
    t2 = ROY if cor == 'A' else LAR
    dest = SOL if cor == 'A' else MAR
    logo = 'logo.png' if cor == 'A' else 'logo-marinho.png'
    fy = 150 if reels else 70
    by = H - (380 if reels else 120)
    ky = top + fs * 2.2 + 40
    return f"""<section class="f" id="{id_}{'-reels' if reels else '-feed'}" style="width:{W}px;height:{H}px;background:{BG[cor]}">
<div class="a" style="inset:0;background:linear-gradient(115deg,rgba(255,255,255,0) 55%,rgba(255,255,255,.06) 70%,rgba(3,18,70,.30) 100%)"></div>
<svg class="a" style="left:0;top:0" width="{W}" height="{H}"><g transform="translate({380 if not reels else 300},{top + 300}) scale({1.25 if not reels else 1.5})"><polygon points="{M['pts']}" fill="rgba(255,255,255,.13)" stroke="rgba(255,255,255,.4)" stroke-width="1.6" stroke-linejoin="round"/></g></svg>
<img class="a" src="{foto}.png" style="left:{x}px;bottom:-4px;width:{w}px;filter:drop-shadow(0 30px 50px rgba(2,12,50,.45))">
<div class="a L" style="left:64px;top:{fy}px;font-size:{24 if reels else 21}px;color:#fff">Quadro semanal <span style="color:{dest}">•</span> {fmt}</div>
<div class="a" style="left:58px;top:{top}px" data-fit="{W - 130}">
 <div class="caixa B" style="background:{b1};color:{t1};font-size:{fs}px">{l1}</div><br>
 <div class="caixa B" style="background:#fff;color:{t2};font-size:{fs}px;margin-top:10px">{l2}</div></div>
<div class="a K" style="left:66px;top:{ky}px;font-size:{64 if reels else 52}px;color:{SOL if cor == 'A' else '#fff'};text-shadow:0 4px 18px rgba(2,12,50,.35);width:{620 if reels else 470}px">{frase}</div>
<div class="a B" style="left:64px;top:{ky + (190 if reels else 150)}px;padding:16px 24px;font-size:{36 if reels else 30}px;letter-spacing:.04em;color:#fff;background:{LAR if cor == 'A' else MAR};box-shadow:0 20px 34px -20px rgba(2,12,50,.7)">Toda {dia} · {hora}</div>
<img class="a" src="{logo}" style="left:52px;top:{by - 200}px;width:270px;filter:drop-shadow(0 14px 24px rgba(2,12,50,.35))">
<div class="a L" style="left:64px;top:{by + 10}px;font-size:19px;letter-spacing:.16em;color:#fff">@_leonardopinto</div>
<div class="a" style="inset:0;background-image:url(&quot;{GRAO}&quot;);opacity:.10;mix-blend-mode:overlay"></div>
</section>"""

FIT = """<script>document.fonts.ready.then(()=>{document.querySelectorAll('[data-fit]').forEach(d=>{const m=+d.dataset.fit;d.querySelectorAll('.caixa').forEach(c=>{let s=parseFloat(c.style.fontSize);while(c.offsetWidth>m&&s>40){s-=2;c.style.fontSize=s+'px'}})})})</script>"""
html = f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>" + ''.join(arte(q, 1080, 1350, False) + arte(q, 1080, 1920, True) for q in Q) + FIT + "</body></html>"
open(f'{D}/artes.html', 'w').write(html)
