# Canal do YouTube "Lindson Almeida": peças do kit (Designer gráfico, conta Zuleide, 17/11/2026)
# Identidade = marca pessoal aprovada (artes v2: preto + amarelo #F5C518 c2y, Anton + Manrope, palavra-chave em caixa amarela, rótulo mono).
# Composições copiadas de: The Futur (rosto grande + palavra condensada gigante), Dan Koe (banner preto minimalista de uma palavra),
# O Primo Rico / Joel Jota (série com assinatura fixa, rosto à direita e 2-3 palavras gigantes). Ver TEMPLATE.md.
# Uso: REC=<pasta dos recortes> python3 gerar.py && NODE_PATH=$(npm root -g) node render.js && python3 previa.py
import os
B = os.path.dirname(os.path.abspath(__file__))
R = os.environ.get('REC', '/tmp/ytrec')
def im(n): return 'file://' + os.path.join(R, n)

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Anton&family=Manrope:wght@500;700;800&family=JetBrains+Mono:wght@500;700&display=swap');
:root{--y:#F5C518;--k:#0A0A0A;--w:#F4F1EA}
*{margin:0;padding:0;box-sizing:border-box}body{background:#222}
section.f{position:relative;overflow:hidden;background:var(--k);color:var(--w);font-family:Manrope}
.A{font-family:Anton;text-transform:uppercase;line-height:.88;letter-spacing:.5px}
.M{font-family:'JetBrains Mono';text-transform:uppercase;letter-spacing:3px;font-weight:700}
.cx{background:var(--y);color:var(--k);padding:0 .12em;display:inline-block}
.grain:after{content:'';position:absolute;inset:0;pointer-events:none;opacity:.10;mix-blend-mode:overlay;
 background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='220' height='220'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E")}
.glow{position:absolute;border-radius:50%;filter:blur(90px);background:radial-gradient(circle,rgba(245,197,24,.55),rgba(245,197,24,0) 70%)}
.p{position:absolute;bottom:0;filter:drop-shadow(-14px 0 26px rgba(245,197,24,.28)) drop-shadow(0 30px 40px rgba(0,0,0,.6))}
.out{color:transparent;-webkit-text-stroke:3px rgba(245,197,24,.35)}
.tag{position:absolute;font-family:'JetBrains Mono';font-weight:700;letter-spacing:3px;text-transform:uppercase}
.vin{position:absolute;inset:0;background:radial-gradient(ellipse at 50% 45%,transparent 55%,rgba(0,0,0,.65))}
"""

def thumb(id_, corpo):
    return f'<section class="f grain" id="{id_}" style="width:1280px;height:720px">{corpo}</section>'

P = []
# 1. Banner 2560x1440 (área segura central 1546x423 = x 507..2053, y 508..931). Copia Dan Koe (preto, 1 palavra) + The Futur (rosto).
P.append(f'''<section class="f grain" id="banner" style="width:2560px;height:1440px">
<div class="A out" style="position:absolute;left:-40px;top:250px;font-size:900px;white-space:nowrap;-webkit-text-stroke:4px rgba(245,197,24,.16)">AUTORIDADE</div>
<div class="glow" style="width:1100px;height:1100px;left:1250px;top:250px"></div>
<div style="position:absolute;left:507px;top:508px;width:1546px;height:423px">
  <div class="M" style="color:var(--y);font-size:22px;margin-top:40px">● Canal oficial · São Luís (MA) para o Brasil</div>
  <div class="A" style="font-size:150px;margin-top:22px">LINDSON <span class="cx">ALMEIDA</span></div>
  <div style="font-size:34px;font-weight:700;margin-top:28px;max-width:900px;line-height:1.25">Marketing, design e vendas para negócio local.<br><span style="color:#9a9a9a;font-weight:500">Sem enrolação. Toda terça e sexta, 19h.</span></div>
</div>
<img class="p" src="{im('l03.png')}" style="height:880px;left:1520px;bottom:509px;transform:translateY(400px)">
<div style="position:absolute;left:0;right:0;bottom:0;height:509px;background:linear-gradient(transparent,var(--k) 22%)"></div>
<div class="tag" style="left:507px;top:960px;color:#777;font-size:18px">PAPO RETO · RAIO-X · BASTIDORES · VENDAS · IA NA PRÁTICA · NEGÓCIO LOCAL</div>
<div class="vin"></div></section>''')

# 2. Foto de perfil 800x800 = o MESMO avatar do Instagram/mini site/LinkedIn (c10 sobre amarelo). Regra 15/11.
P.append(f'''<section class="f" id="perfil" style="width:800px;height:800px;background:var(--y)">
<div style="position:absolute;inset:0;background:radial-gradient(circle at 50% 35%,#ffe27a,transparent 60%)"></div>
<img src="{im('c10.png')}" style="position:absolute;width:1000px;left:-100px;top:-40px"></section>''')

# 3. Marca-d'água 150x150 (PNG transparente): monograma LA em caixa amarela.
P.append('''<section class="f" id="marca-dagua" style="width:150px;height:150px;background:transparent">
<div style="position:absolute;inset:10px;background:var(--y);border-radius:22px;display:flex;align-items:center;justify-content:center;box-shadow:0 4px 14px rgba(0,0,0,.4)">
<span class="A" style="color:var(--k);font-size:76px;line-height:1">LA</span></div></section>''')

# 4. Thumbs-modelo (1 por quadro; composições diferentes; rosto sempre livre)
# T1 Papo Reto — copia The Futur "THEY DON'T CARE": rosto à direita, 2 linhas condensadas, 2ª em caixa amarela; aspas gigantes (artes v2 "Papo reto").
P.append(thumb('thumb-1-papo-reto', f'''<div class="glow" style="width:700px;height:700px;left:640px;top:0"></div>
<div style="position:absolute;left:44px;top:-80px;font-family:Georgia,serif;font-weight:700;font-size:440px;color:var(--y)">&ldquo;</div>
<img class="p" src="{im('l01.png')}" style="height:760px;right:-10px;bottom:-130px">
<div class="A" style="position:absolute;left:60px;top:250px;font-size:132px">POST NÃO<br><span class="cx">VENDE</span></div>
<div class="tag" style="left:64px;bottom:44px;font-size:20px;color:var(--y)">PAPO RETO · 01</div><div class="vin"></div>'''))

# T2 Raio-X — copia Joel Jota (split antes × depois com seta): fundo dividido preto/amarelo, ele no meio.
P.append(thumb('thumb-2-raio-x', f'''<div style="position:absolute;right:0;top:0;width:52%;height:100%;background:var(--y)"></div>
<div class="A" style="position:absolute;left:40px;top:60px;font-size:68px;color:#8a8a8a">ANTES</div>
<div class="A" style="position:absolute;right:40px;top:60px;font-size:68px;color:var(--k)">DEPOIS</div>
<img class="p" src="{im('l07.png')}" style="height:700px;left:430px;bottom:-110px">
<div class="A" style="position:absolute;left:40px;bottom:60px;font-size:118px;width:470px">PERFIL<br>QUE <span class="cx">AFASTA</span></div>
<div class="A" style="position:absolute;right:40px;bottom:60px;font-size:118px;color:var(--k);text-align:right">PERFIL<br>QUE VENDE</div>
<div class="tag" style="left:40px;top:150px;font-size:18px;color:var(--y)">RAIO-X</div>'''))

# T3 Bastidores do Estúdio — copia Satori "layout": palavra gigante ATRÁS da pessoa, fundo amarelo cheio.
P.append(thumb('thumb-3-bastidores', f'''<section style="position:absolute;inset:0;background:var(--y)"></section>
<div class="A" style="position:absolute;left:0;right:0;top:70px;text-align:center;font-size:330px;color:var(--k)">MARCA</div>
<img class="p" src="{im('l02.png')}" style="height:720px;left:430px;bottom:-150px;filter:drop-shadow(0 30px 40px rgba(0,0,0,.45))">
<div class="A" style="position:absolute;left:44px;bottom:50px;font-size:64px;color:var(--k);background:var(--w);padding:6px 16px">DO ZERO</div>
<div class="tag" style="right:44px;bottom:60px;font-size:20px;color:var(--k)">BASTIDORES DO ESTÚDIO</div>'''))

# T4 Vendas na Real — copia Hormozi "IDIOT PROOF": rosto à esquerda, pergunta curta enorme à direita, número em contorno.
P.append(thumb('thumb-4-vendas', f'''<div class="glow" style="width:640px;height:640px;left:-120px;top:40px"></div>
<div class="A out" style="position:absolute;right:30px;top:-60px;font-size:520px">?</div>
<img class="p" src="{im('l06.png')}" style="height:800px;left:-40px;bottom:-200px">
<div class="A" style="position:absolute;right:56px;top:190px;font-size:128px;text-align:right">O CLIENTE<br><span class="cx">SUMIU</span></div>
<div style="position:absolute;right:56px;top:470px;font-size:28px;font-weight:700;color:#bdbdbd">o que dizer no WhatsApp</div>
<div class="tag" style="right:56px;bottom:44px;font-size:20px;color:var(--y)">VENDAS NA REAL</div><div class="vin"></div>'''))

# T5 IA na Prática — copia Flux Academy "AI Website": tarja amarela no topo + rosto central grande + rótulo mono de terminal.
P.append(thumb('thumb-5-ia', f'''<div style="position:absolute;inset:0;background:linear-gradient(180deg,#151515,#050505)"></div>
<div class="M" style="position:absolute;left:44px;top:200px;font-size:22px;color:#6f6f6f;line-height:1.7">&gt; claude code<br>&gt; criar site<br>&gt; publicar_</div>
<div class="glow" style="width:620px;height:620px;left:330px;top:60px"></div>
<img class="p" src="{im('l14.png')}" style="height:1400px;left:430px;bottom:-830px">
<div class="A" style="position:absolute;left:0;top:0;right:0;background:var(--y);color:var(--k);font-size:120px;padding:18px 44px 8px">A IA FEZ MEU SITE</div>
<div class="tag" style="right:44px;bottom:44px;font-size:20px;color:var(--y)">IA NA PRÁTICA</div><div class="vin"></div>'''))

# T6 Negócio Local — copia O Primo Rico (cena real ao fundo, desfocada, + manchete gigante à esquerda).
P.append(thumb('thumb-6-negocio-local', f'''<img src="{im('bg09.jpg')}" style="position:absolute;width:100%;height:100%;object-fit:cover;filter:saturate(1.1)">
<div style="position:absolute;inset:0;background:linear-gradient(90deg,rgba(0,0,0,.92) 35%,rgba(0,0,0,.15))"></div>
<img class="p" src="{im('l09.png')}" style="height:820px;right:-60px;bottom:-200px">
<div class="A" style="position:absolute;left:56px;top:160px;font-size:124px">SÃO LUÍS<br>COMPRA<br><span class="cx">ASSIM</span></div>
<div class="tag" style="left:60px;bottom:44px;font-size:20px;color:var(--y)">NEGÓCIO LOCAL</div><div class="vin"></div>'''))

# 5. Capa de Short 1080x1920 (rosto no terço de cima, texto na faixa segura do meio-baixo)
P.append(f'''<section class="f grain" id="capa-short" style="width:1080px;height:1920px">
<div class="A out" style="position:absolute;left:-30px;top:120px;font-size:560px;line-height:.8">REAL</div>
<div class="glow" style="width:900px;height:900px;left:90px;top:200px"></div>
<img class="p" src="{im('l08.png')}" style="width:1180px;left:-50px;bottom:620px">
<div style="position:absolute;left:0;right:0;bottom:0;height:820px;background:linear-gradient(transparent,var(--k) 18%)"></div>
<div class="A" style="position:absolute;left:70px;bottom:330px;font-size:150px">PREÇO NÃO<br>É O <span class="cx">PROBLEMA</span></div>
<div class="tag" style="left:74px;bottom:250px;font-size:26px;color:var(--y)">LINDSON ALMEIDA · PAPO RETO</div><div class="vin"></div></section>''')

# 6. Bumper/intro estático 1920x1080
P.append(f'''<section class="f grain" id="bumper" style="width:1920px;height:1080px">
<div class="A out" style="position:absolute;left:-30px;top:130px;font-size:760px;white-space:nowrap;-webkit-text-stroke:4px rgba(245,197,24,.18)">AUTORIDADE</div>
<div class="glow" style="width:900px;height:900px;left:1000px;top:120px"></div>
<img class="p" src="{im('l16.png')}" style="height:980px;right:110px;bottom:-60px">
<div style="position:absolute;left:120px;top:380px">
<div class="M" style="color:var(--y);font-size:24px">● NO AR</div>
<div class="A" style="font-size:190px;margin-top:20px">LINDSON<br><span class="cx">ALMEIDA</span></div></div>
<div class="tag" style="left:124px;bottom:80px;font-size:22px;color:#8a8a8a">MARKETING · DESIGN · VENDAS</div><div class="vin"></div></section>''')

open(os.path.join(B, 'pecas.html'), 'w').write('<!doctype html><meta charset="utf-8"><style>' + CSS + '</style>' + '\n'.join(P))
print('ok', len(P))
