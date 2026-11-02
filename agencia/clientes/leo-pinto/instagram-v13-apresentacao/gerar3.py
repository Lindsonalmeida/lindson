# v13.3 · apresentação do Leo Pinto aplicando as referências do Lindson (Marcelo Tavares e Erick Monteiro, 02/11/2026):
# retrato grande de perto, nome em blocos de cor, nome empilhado em Montserrat Black, slogan em etiqueta,
# mapa oficial de São João Batista (IBGE, via geodata-br) em camada translúcida, degradê azul e granulação.
# Textos do Lindson: vereador mais bem votado · do povo para o povo · jovem, engenheiro, compromisso com São João Batista.
# Arte-mestra pensada na grade 3:4 (3 × 1012 + 34 px de sangria). Conta Lindson.
import sys, json
MAR, ROY, SOL, LAR = '#05316E', '#2350F5', '#FFC20E', '#FF7A1A'
B = 34; W, H = 3036 + 2*B, 1350
X = lambda x: x + B
M = json.load(open(f'{sys.argv[1]}/mapa-sjb.json'))
# leo-14 (polo amarela, retrato de perto): recorte 1675×1270, cabeça x 511–1187 (centro 850)
E = .92; LW = int(1675*E); LH = int(1270*E); LX = X(520) - int(850*E); LY = H - LH + 6
GRAO = ("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'>"
        "<filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='3' stitchTiles='stitch'/>"
        "<feColorMatrix values='0 0 0 0 .5  0 0 0 0 .5  0 0 0 0 .5  0 0 0 .9 0'/></filter><rect width='100%25' height='100%25' filter='url(%23n)'/></svg>")
MW = 1560; MS = MW/1000; MX, MY = X(560), 300
html = f"""<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Kaushan+Script&family=Montserrat:ital,wght@0,600;0,700;0,800;0,900;1,900&display=swap" rel="stylesheet">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
#p{{position:relative;width:{W}px;height:{H}px;overflow:hidden;
 background:radial-gradient(1300px 1000px at {X(620)}px 520px,#4A78FF 0,#2E5BFA 26%,{ROY} 46%,#1539BE 70%,#0B2A8A 88%,#082063 100%)}}
.a{{position:absolute}} .K{{font-family:'Kaushan Script';line-height:1.08}}
.B{{font-family:Montserrat;font-weight:900;text-transform:uppercase;line-height:.92;letter-spacing:-.02em;white-space:nowrap}}
.L{{font-family:Montserrat;font-weight:700;text-transform:uppercase;letter-spacing:.38em;white-space:nowrap}}
.caixa{{display:inline-block;padding:14px 26px 6px;box-shadow:0 24px 40px -22px rgba(2,12,50,.7)}}
</style></head><body style="margin:0"><div id="p">
<!-- luz diagonal suave do lado direito (profundidade) -->
<div class="a" style="inset:0;background:linear-gradient(115deg,rgba(255,255,255,0) 55%,rgba(255,255,255,.06) 70%,rgba(3,18,70,.35) 100%)"></div>
<!-- CAMADA · mapa de São João Batista (contorno oficial) em azul claro, com eco em linha -->
<svg class="a" style="left:0;top:0" width="{W}" height="{H}">
 <defs><linearGradient id="mg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#8CC0FF" stop-opacity=".46"/><stop offset="1" stop-color="#5A86FF" stop-opacity=".20"/></linearGradient></defs>
 <g transform="translate({MX+46},{MY+40}) scale({MS})"><polygon points="{M['pts']}" fill="none" stroke="#9CC4FF" stroke-opacity=".35" stroke-width="{2.2/MS*1.6}" stroke-linejoin="round"/></g>
 <g transform="translate({MX},{MY}) scale({MS})"><polygon points="{M['pts']}" fill="url(#mg)" stroke="#BFD8FF" stroke-opacity=".5" stroke-width="{1.6/MS*1.6}" stroke-linejoin="round"/></g>
</svg>
<!-- 1 · ESQUERDA: retrato grande -->
<div class="a K" style="left:{X(0)}px;width:1012px;top:96px;text-align:center;font-size:74px;color:#fff;text-shadow:0 4px 20px rgba(2,12,50,.4)">Prazer, eu sou o <span style="color:{SOL}">Leo</span></div>
<img class="a" src="assets/leo-14-original.png" style="left:{LX}px;top:{LY}px;width:{LW}px;filter:drop-shadow(0 30px 50px rgba(2,12,50,.45))">
<!-- 2 · MEIO: nome em blocos -->
<div class="a L" style="left:{X(1150)}px;top:236px;font-size:24px;color:rgba(255,255,255,.9)">São João Batista <span style="color:{SOL}">•</span> MA</div>
<div class="a" style="left:{X(1146)}px;top:290px">
 <div class="caixa B" style="background:{SOL};color:{MAR};font-size:200px">LEO</div><br>
 <div class="caixa B" style="background:#fff;color:{ROY};font-size:200px;margin-top:10px">PINTO</div></div>
<div class="a B" style="left:{X(1146)}px;top:782px;padding:18px 26px;font-size:38px;letter-spacing:.02em;color:#fff;background:linear-gradient(90deg,{LAR},#FF9A22);box-shadow:0 20px 34px -20px rgba(120,40,0,.7)">Vereador mais bem votado</div>
<div class="a L" style="left:{X(1150)}px;top:898px;font-size:28px;letter-spacing:.2em;color:#fff">Jovem <span style="color:{SOL}">•</span> Engenheiro</div>
<div class="a K" style="left:{X(1148)}px;top:946px;font-size:66px;color:{SOL};text-shadow:0 4px 18px rgba(2,12,50,.35)">compromisso com<br>São João Batista</div>
<!-- 3 · DIREITA: promessa + chamada + assinatura -->
<div class="a B" style="left:{X(2154)}px;top:132px;font-size:136px;color:#fff;filter:drop-shadow(0 16px 28px rgba(2,12,50,.4))">Do povo<br>para o<br><span style="background:linear-gradient(180deg,#FFE066,{SOL} 50%,{LAR});-webkit-background-clip:text;background-clip:text;color:transparent">povo</span></div>
<div class="a K" style="left:{X(2158)}px;top:540px;font-size:70px;color:#fff">juntos podemos mais!</div>
<div class="a B" style="left:{X(2154)}px;top:668px;padding:18px 26px;font-size:36px;letter-spacing:.02em;color:{ROY};background:#fff;box-shadow:0 20px 34px -20px rgba(2,12,50,.7)">Me conta sua demanda</div>
<div class="a L" style="left:{X(2158)}px;top:772px;font-size:22px;letter-spacing:.16em;line-height:1.6;color:rgba(255,255,255,.85)">Siga e acompanhe<br>o mandato de perto</div>
<img class="a" src="assets/logo.png" style="left:{X(2154)}px;top:{1230-262}px;width:352px;filter:drop-shadow(0 14px 24px rgba(2,12,50,.4))">
<div class="a L" style="left:{X(2560)}px;top:1180px;font-size:20px;letter-spacing:.16em;color:rgba(255,255,255,.85)">@_leonardopinto</div>
<!-- granulação fina -->
<div class="a" style="inset:0;background-image:url(&quot;{GRAO}&quot;);opacity:.10;mix-blend-mode:overlay"></div>
</div></body></html>"""
open(f'{sys.argv[1]}/artes.html', 'w').write(html)
