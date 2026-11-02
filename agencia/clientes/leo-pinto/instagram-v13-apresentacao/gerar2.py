# v13.2 · 3 artes de apresentação do Leo Pinto, versão sofisticada (pedido do Lindson: camadas, degradês, capricho).
# Mesma arte-mestra pensada na grade 3:4 (3 × 1012 + 34 px de sangria). Só fontes, logo e cores. Conta Lindson, 02/11/2026.
import sys
MAR, ROY, SOL, LAR = '#05316E', '#2350F5', '#FFC20E', '#FF7A1A'
B = 34; W, H = 3036 + 2*B, 1350
X = lambda x: x + B
E = .9; LW = int(1224*E); LX = X(1518) - int(630*E); LY = 400 - int(290*E)
GRAO = ("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'>"
        "<filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='3' stitchTiles='stitch'/>"
        "<feColorMatrix values='0 0 0 0 .5  0 0 0 0 .5  0 0 0 0 .5  0 0 0 .9 0'/></filter><rect width='100%25' height='100%25' filter='url(%23n)'/></svg>")
html = f"""<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Anton&family=Kaushan+Script&family=Montserrat:wght@600;700;800;900&display=swap" rel="stylesheet">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
#p{{position:relative;width:{W}px;height:{H}px;overflow:hidden;
 background:radial-gradient(1100px 900px at {X(1900)}px 420px,#3D6CFF 0,{ROY} 34%,#1236B8 62%,#0A2577 82%,{MAR} 100%)}}
.a{{position:absolute}} .H{{font-family:Anton;line-height:.86;text-transform:uppercase;white-space:nowrap}}
.K{{font-family:'Kaushan Script';line-height:1.08}} .M{{font-family:Montserrat;font-weight:800;letter-spacing:.1em;text-transform:uppercase}}
.vidro{{border-radius:34px;background:linear-gradient(135deg,rgba(255,255,255,.20),rgba(255,255,255,.05));border:1.5px solid rgba(255,255,255,.32);
 backdrop-filter:blur(18px);-webkit-backdrop-filter:blur(18px);box-shadow:0 30px 60px -30px rgba(2,16,60,.55),inset 0 1px 0 rgba(255,255,255,.35)}}
.grad-sol{{background:linear-gradient(180deg,#FFE066 0,{SOL} 45%,{LAR} 100%);-webkit-background-clip:text;background-clip:text;color:transparent}}
</style></head><body style="margin:0"><div id="p">
<!-- CAMADA 1 · campo quente (amarelo → laranja) com corte diagonal que passa atrás do Leo -->
<div class="a" style="inset:0;clip-path:polygon(0 0,{X(1330)}px 0,{X(960)}px 100%,0 100%);
 background:radial-gradient(1000px 820px at {X(260)}px 160px,#FFE270 0,#FFD23A 30%,{SOL} 55%,#FF9A22 82%,{LAR} 100%)"></div>
<!-- fio de luz na borda do corte (dá acabamento à diagonal) -->
<svg class="a" style="left:0;top:0" width="{W}" height="{H}"><defs><linearGradient id="fio" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".0"/><stop offset=".35" stop-color="#fff" stop-opacity=".55"/><stop offset="1" stop-color="#fff" stop-opacity=".0"/></linearGradient></defs>
 <line x1="{X(1330)}" y1="0" x2="{X(960)}" y2="{H}" stroke="url(#fio)" stroke-width="3"/></svg>
<!-- CAMADA 2 · tipografia fantasma atrás do Leo -->
<div class="a H" style="left:{X(1320)}px;top:150px;font-size:1010px;color:#fff;opacity:.07;letter-spacing:-.01em">BAIXADA</div>
<!-- CAMADA 3 · luz suave nas costas -->
<div class="a" style="left:{X(1518)-620}px;top:-260px;width:1240px;height:1240px;border-radius:50%;background:radial-gradient(circle,rgba(255,255,255,.30) 0,rgba(255,255,255,.10) 38%,rgba(255,255,255,0) 68%)"></div>

<!-- 1 · ESQUERDA -->
<div class="a M" style="left:{X(136)}px;top:136px;font-size:30px;color:{MAR};letter-spacing:.42em;opacity:.85">Prazer,</div>
<div class="a H" style="left:{X(130)}px;top:186px;font-size:196px;color:{MAR}">SOU O</div>
<div class="a H" style="left:{X(150)}px;top:392px;font-size:660px;color:transparent;-webkit-text-stroke:3px rgba(5,49,110,.28)">LEO</div>
<div class="a H" style="left:{X(124)}px;top:366px;font-size:660px;background:linear-gradient(180deg,#0B47B8 0,{MAR} 70%);-webkit-background-clip:text;background-clip:text;color:transparent;filter:drop-shadow(0 22px 26px rgba(150,60,0,.22))">LEO</div>
<div class="a K" style="left:{X(136)}px;top:952px;font-size:80px;color:{MAR}">vereador de<br><span style="color:#fff;text-shadow:0 3px 14px rgba(170,70,0,.35)">São João Batista</span></div>
<div class="a vidro M" style="left:{X(132)}px;top:1166px;padding:20px 34px;font-size:28px;color:{MAR};background:linear-gradient(135deg,rgba(255,255,255,.55),rgba(255,255,255,.22));border-color:rgba(255,255,255,.7)">Eleito em 2024 <span style="color:{LAR}">●</span> Maranhão</div>

<!-- 2 · MEIO: retrato -->
<div class="a" style="left:{X(1518)-430}px;top:{H-120}px;width:860px;height:200px;border-radius:50%;background:radial-gradient(closest-side,rgba(2,16,60,.45),rgba(2,16,60,0))"></div>
<img class="a" src="assets/leo-01-cor.png" style="left:{LX}px;top:{LY}px;width:{LW}px;filter:drop-shadow(0 34px 44px rgba(2,16,60,.38))">
<div class="a" style="left:{X(1012)-B}px;width:{1012+2*B}px;top:{H-470}px;height:470px;background:linear-gradient(180deg,rgba(5,30,90,0) 0,rgba(5,30,90,.55) 55%,rgba(3,22,70,.92) 100%)"></div>
<div class="a" style="left:{X(1012)}px;width:1012px;top:1012px;text-align:center">
 <div class="K" style="font-size:76px;color:{SOL}">engenheiro e na rua</div>
 <div class="H" style="font-size:206px;margin-top:4px;background:linear-gradient(180deg,#fff 0,#fff 55%,#FFE7A8 100%);-webkit-background-clip:text;background-clip:text;color:transparent;filter:drop-shadow(0 6px 24px rgba(0,10,40,.45))">DA BAIXADA</div></div>

<!-- 3 · DIREITA -->
<div class="a H" style="left:{X(2154)}px;top:118px;font-size:178px;color:#fff;filter:drop-shadow(0 18px 30px rgba(2,16,60,.35))">JUNTOS<br>PODEMOS<br><span class="grad-sol">MAIS!</span></div>
<div class="a vidro" style="left:{X(2150)}px;top:640px;width:740px;padding:38px 44px 40px">
 <div class="K" style="font-size:72px;color:{SOL}">me conta sua demanda</div>
 <div class="M" style="margin-top:18px;font-size:27px;line-height:1.55;color:#fff">Siga e acompanhe<br>o mandato de perto</div></div>
<img class="a" src="assets/logo.png" style="left:{X(2154)}px;top:{1230-262}px;width:352px;filter:drop-shadow(0 14px 24px rgba(2,16,60,.4))">
<div class="a M" style="left:{X(2560)}px;top:1176px;font-size:24px;color:rgba(255,255,255,.85);letter-spacing:.18em">@_leonardopinto</div>

<!-- CAMADA FINAL · granulação fina -->
<div class="a" style="inset:0;background-image:url(&quot;{GRAO}&quot;);opacity:.10;mix-blend-mode:overlay"></div>
</div></body></html>"""
open(f'{sys.argv[1]}/artes.html', 'w').write(html)
