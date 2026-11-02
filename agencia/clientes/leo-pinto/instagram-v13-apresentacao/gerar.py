# v13 · 3 artes de apresentação do Leo Pinto (Direção B da pesquisa: cores chapadas + retrato central).
# Arte-mestra pensada na grade 3:4: 3 × 1012 visíveis + 34 px de sangria nas pontas (3104 × 1350).
# Post N = mestra x (N−1)·1012−34 … N·1012+34. Identidade 02/11/2026: só fontes, logo e cores. Conta Lindson.
import sys
MAR, ROY, SOL, LAR = '#05316E', '#2350F5', '#FFC20E', '#FF7A1A'
B = 34; W, H = 3036 + 2*B, 1350
X = lambda x: x + B                     # coordenada da grade → coordenada do arquivo
TROCA = 1400                            # amarelo → azul, atrás do corpo do Leo
# leo-01 (polo laranja, braços cruzados): recorte 1224×1745, cabeça x 406–854 (centro 630), olhos y≈290
E = .9; LW = int(1224*E); LX = X(1518) - int(630*E); LY = 400 - int(290*E)
html = f"""<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Anton&family=Kaushan+Script&family=Montserrat:wght@600;700;800;900&display=swap" rel="stylesheet">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
#p{{position:relative;width:{W}px;height:{H}px;overflow:hidden;background:linear-gradient(90deg,{SOL} 0 {X(TROCA)}px,{ROY} {X(TROCA)}px 100%)}}
.a{{position:absolute}} .H{{font-family:Anton;line-height:.86;text-transform:uppercase;white-space:nowrap}}
.K{{font-family:'Kaushan Script';line-height:1.08}} .M{{font-family:Montserrat;font-weight:800;letter-spacing:.08em;text-transform:uppercase}}
</style></head><body style="margin:0"><div id="p">
<!-- 1 · esquerda (amarelo): quem -->
<div class="a H" style="left:{X(128)}px;top:120px;font-size:200px;color:{MAR}">SOU O</div>
<div class="a H" style="left:{X(118)}px;top:300px;font-size:660px;color:{MAR}">LEO</div>
<div class="a K" style="left:{X(132)}px;top:900px;font-size:84px;color:{ROY}">vereador de<br>São João Batista</div>
<div class="a M" style="left:{X(134)}px;top:1192px;font-size:34px;color:{MAR}">Eleito em 2024 · Maranhão</div>
<!-- 2 · meio: retrato que costura as duas cores -->
<img class="a" src="assets/leo-01-cor.png" style="left:{LX}px;top:{LY}px;width:{LW}px">
<div class="a" style="left:{X(1012)}px;width:1012px;top:1000px;text-align:center">
 <div class="K" style="font-size:78px;color:#fff;text-shadow:0 2px 18px rgba(5,49,110,.35)">engenheiro e na rua</div>
 <div class="H" style="font-size:200px;color:#fff;margin-top:6px;text-shadow:0 4px 30px rgba(5,49,110,.35)">DA BAIXADA</div></div>
<!-- 3 · direita (azul): chamada + assinatura -->
<div class="a H" style="left:{X(2154)}px;top:120px;font-size:178px;color:#fff">JUNTOS<br>PODEMOS<br><span style="color:{SOL}">MAIS!</span></div>
<div class="a K" style="left:{X(2158)}px;top:612px;font-size:80px;color:{SOL}">me conta sua demanda</div>
<div class="a M" style="left:{X(2160)}px;top:730px;font-size:30px;line-height:1.5;color:#fff">Siga e acompanhe<br>o mandato de perto</div>
<img class="a" src="assets/logo.png" style="left:{X(2154)}px;top:{1230-300}px;width:404px">
</div></body></html>"""
open(f'{sys.argv[1]}/artes.html', 'w').write(html)
