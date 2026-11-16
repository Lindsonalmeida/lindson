# Barzakh · feed v3 "com energia da Provedor v2" (conta Leandro, 16/11/2026).
# v1 (../../feed/) "feed morto"; v2 (../../feed-v2/) "ainda sem vida". Régua: linha-frases/artes-provedor-v2 (aprovada 14/11).
# O que muda: Anton gigante na palavra-chave + Fraunces itálica na nuance, blocos de OURO chapado e quente (o "amarelo" da Barzakh),
# fitas de texto atravessando, números gigantes em contorno, selo circular, mockups grandes e inclinados em camada,
# rosto recortado com rim light âmbar. 3 a 4 camadas por post, sem respiro vazio.
# Referências (../TEMPLATE.md):
#   R1 Provedor v2 (BR, aprovada) ... palavra gigante atrás do rosto, fita, número em contorno, palavra em caixa
#   R2 &Walsh (EUA) ................. case em cor chapada saturada, produto enorme e inclinado
#   R3 Dribbble "bold typography poster" (vários países) ... tipografia condensada ocupando a arte, contorno
# Uso: python3 feed3.py
import os
from playwright.sync_api import sync_playwright
G = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.dirname(G)
V3 = '/home/user/lindson/agencia/marca-lindson/projeto-designer/v3'
REC = V3 + '/feed-v2/gerador/rec'
MK = '/home/user/lindson/agencia/marca-lindson/projeto-designer/v2/mockups'
FONT = '/home/user/lindson/agencia/marca-holding/v2/fontes'
ANTON = '/home/user/lindson/conteudo/youtube/raposa-e-leao/produto/fonts/Anton-Regular.ttf'
LOGO = V3 + '/marca/logos/png/ouro'
T = V3 + '/marca/gerador/trat'
CHROME = '/opt/pw-browsers/chromium_headless_shell-1243/chrome-headless-shell-linux64/chrome-headless-shell'
u = lambda p: 'file://' + p
OB, MA, AU = '#0A0C10', '#F3EEE4', '#EDB13F'   # carvão, marfim, OURO quente saturado
AUG = 'linear-gradient(135deg,#F6C453 0%,#E9A92F 55%,#D8922028 100%),#E9A92F'
NOISE = "url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='220' height='220'%3E%3Cfilter id='n'%3E%3CfeTurbulence baseFrequency='.85' numOctaves='3'/%3E%3C/filter%3E%3Crect width='220' height='220' filter='url(%23n)' opacity='.6'/%3E%3C/svg%3E\")"
CSS = f"""
@font-face{{font-family:'Anton';src:url('file://{ANTON}')}}
@font-face{{font-family:'Fraunces';src:url('file://{FONT}/Fraunces-SemiBold.ttf');font-weight:600}}
@font-face{{font-family:'Fraunces';font-style:italic;src:url('file://{FONT}/Fraunces-Italic%5BSOFT,WONK,opsz,wght%5D.ttf')}}
@font-face{{font-family:'Inter Tight';src:url('file://{FONT}/InterTight-SemiBold.ttf');font-weight:600}}
@font-face{{font-family:'JetBrains Mono';src:url('file://{FONT}/JetBrainsMono-Medium.ttf')}}
*{{box-sizing:border-box;margin:0;padding:0}} body{{background:#000}}
.pg{{width:1080px;position:relative;overflow:hidden;font-family:'Inter Tight';font-weight:600;color:{MA};margin-bottom:20px}}
.pg:after{{content:'';position:absolute;inset:0;background-image:{NOISE};opacity:.13;mix-blend-mode:overlay;pointer-events:none;z-index:30}}
.a{{position:absolute}}
.an{{font-family:'Anton';text-transform:uppercase;line-height:.86;letter-spacing:-.005em}}
.it{{font-family:'Fraunces';font-style:italic;font-weight:400;letter-spacing:-.02em;text-transform:none}}
.mn{{font-family:'JetBrains Mono';font-size:18px;letter-spacing:.18em;text-transform:uppercase}}
.cx{{background:{AU};color:{OB};padding:0 .12em;box-decoration-break:clone;-webkit-box-decoration-break:clone}}
.cxd{{background:{OB};color:{AU};padding:0 .12em}}
.ol{{font-family:'Anton';color:transparent;-webkit-text-stroke:3px {AU};line-height:.8}}
.old{{font-family:'Anton';color:transparent;-webkit-text-stroke:3px {OB};line-height:.8}}
.p{{font-size:28px;line-height:1.35;font-weight:600}}
.face{{position:absolute;bottom:0;z-index:6;filter:saturate(1.18) contrast(1.1) sepia(.12) drop-shadow(0 0 2px rgba(255,190,90,.95)) drop-shadow(-18px -8px 30px rgba(255,160,40,.55)) drop-shadow(0 30px 50px rgba(0,0,0,.55))}}
.mock{{position:absolute;background-size:cover;background-position:center;box-shadow:0 60px 110px rgba(0,0,0,.6),0 0 0 1px rgba(255,255,255,.08);border-radius:10px}}
.fita{{position:absolute;left:-200px;width:1500px;height:74px;display:flex;align-items:center;white-space:nowrap;overflow:hidden;font-family:'Anton';font-size:40px;letter-spacing:.06em;z-index:9;box-shadow:0 14px 30px rgba(0,0,0,.45)}}
"""

def face(c, h, x=None, right=None, esp=False, z=6):
    pos = f'left:{x}px' if x is not None else f'right:{right}px'
    tr = 'transform:scaleX(-1);' if esp else ''
    return f'<img class="face" src="{u(REC+"/"+c+".png")}" style="height:{h}px;{pos};z-index:{z};{tr}">'

def fundo(t, cor=None):
    if t == 'D':
        return (f'<div class="a" style="inset:0;background:{OB}"></div><div class="a" style="inset:0;background:url({u(T+"/concreto-escuro-v2.jpg")}) center/cover;opacity:.5"></div>'
                f'<div class="a" style="inset:0;background:radial-gradient(circle at 60% 45%,rgba(237,170,60,.55),rgba(120,60,10,.25) 40%,transparent 72%)"></div>')
    if t == 'O':
        return (f'<div class="a" style="inset:0;background:{AUG}"></div><div class="a" style="inset:0;background:radial-gradient(circle at 25% 15%,rgba(255,240,190,.55),transparent 50%),radial-gradient(circle at 90% 100%,rgba(120,50,0,.35),transparent 60%)"></div>')
    return (f'<div class="a" style="inset:0;background:{cor}"></div><div class="a" style="inset:0;background:radial-gradient(circle at 30% 20%,rgba(255,255,255,.25),transparent 55%),radial-gradient(circle at 90% 100%,rgba(0,0,0,.4),transparent 60%)"></div>')

def fita(top, rot, txt='IDENTIDADE ✦ MARCA ✦ TRAVESSIA ✦ ', bg=AU, fg=OB, z=9, cls=''):
    return f'<div class="fita {cls}" style="top:{top}px;transform:rotate({rot}deg);background:{bg};color:{fg};z-index:{z}"><span class="run">{txt*6}</span></div>'

def selo(x, y, s=210, bg=OB, fg=AU, z=12, cls=''):
    return (f'<div class="a {cls}" style="left:{x}px;top:{y}px;width:{s}px;height:{s}px;border-radius:50%;background:{bg};z-index:{z};box-shadow:0 20px 40px rgba(0,0,0,.45)">'
            f'<svg class="giro" viewBox="0 0 200 200" width="{s}" height="{s}" style="position:absolute;inset:0"><defs><path id="cc" d="M100,100 m-74,0 a74,74 0 1,1 148,0 a74,74 0 1,1 -148,0"/></defs>'
            f'<text font-family="JetBrains Mono" font-size="14.2" letter-spacing="3.2" fill="{fg}"><textPath href="#cc">BARZAKH ✦ UM ESTÚDIO AL KÁNTARA ✦ </textPath></text></svg>'
            f'<img src="{u(LOGO+"/barzakh-simbolo-ouro.png")}" style="position:absolute;left:30%;top:30%;width:40%;{"filter:brightness(0)" if bg != OB else ""}"></div>')

def topo(dark=True, tag=''):
    c = MA if dark else OB
    return (f'<div class="a" style="left:70px;right:70px;top:56px;display:flex;justify-content:space-between;align-items:center;z-index:20">'
            f'<img src="{u(LOGO+"/barzakh-horizontal-ouro.png")}" style="height:40px;{"" if dark else "filter:brightness(0)"}">'
            f'<span class="mn" style="color:{c};border:1.5px solid {c};padding:8px 14px;border-radius:30px;font-size:15px">{tag}</span></div>')

def rod(t, dark=True):
    c = MA if dark else OB
    return (f'<div class="a mn" style="left:70px;right:70px;bottom:44px;display:flex;justify-content:space-between;color:{c};font-size:15px;z-index:20">'
            f'<span>@barzakhstudio</span><span>{t}</span></div>')

def mock(img, x, y, w, h, r=0, z=5):
    return f'<div class="mock" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;transform:rotate({r}deg);background-image:url({u(MK+"/"+img)});z-index:{z}"></div>'

def sec(i, body, h=1350):
    return f'<section class="pg" id="{i}" style="height:{h}px">{body}</section>'

S = []
# ===== 12 POSTS · ordem de postar · ritmo D(escuro) O(ouro) C(cor do case), nunca dois iguais seguidos =====
# 01 D · apresentação (R1): BARZAKH gigante atrás do rosto c10, selo, fita, número 01
S.append(('posts/01', fundo('D') + topo(True, 'Nº 01 · prazer') +
  f'<div class="a an" style="left:0;right:0;top:160px;text-align:center;font-size:280px;color:{AU};z-index:3">BARZAKH</div>' +
  f'<div class="a ol" style="right:40px;top:470px;font-size:300px;z-index:2">01</div>' + face('c10', 1060, x=140) + selo(820, 560) +
  f'<div class="a" style="left:0;right:0;bottom:0;height:480px;background:linear-gradient(transparent,{OB} 70%);z-index:7"></div>' +
  fita(905, -4) +
  f'<div class="a an" style="left:70px;bottom:120px;font-size:120px;z-index:10">A PASSAGEM DA <span class="it" style="color:{AU};font-size:118px">sua marca.</span></div>' + rod('Lindson Almeida · direção criativa')))
# 02 O · case Orégano (R2): bloco ouro chapado, MARCA gigante, embalagem inclinada, fita escura
S.append(('posts/02', fundo('O') + topo(False, 'Case · Orégano Turbo') +
  f'<div class="a an" style="left:50px;top:130px;font-size:300px;color:{OB};z-index:2">A CAIXA</div>'
  f'<div class="a old" style="right:50px;top:400px;font-size:330px;z-index:2">02</div>' +
  mock('oregano-embalagem.jpg', 110, 470, 860, 640, -6) + fita(1060, 5, 'A CAIXA É A MÍDIA MAIS VISTA ✦ ', OB, AU) +
  f'<div class="a" style="left:70px;top:1170px;z-index:10;font-size:62px;color:{OB}" ><span class="it">é a mídia mais vista.</span></div>' + rod('Embalagem · pizzaria', False)))
# 03 D · gancho (R1): MENOR gigante atrás do rosto c13, palavra em caixa ouro
S.append(('posts/03', fundo('D') + topo(True, 'Limiar') +
  f'<div class="a an" style="left:-10px;top:140px;font-size:420px;color:{AU};z-index:3">MENOR</div>' + face('c13', 1050, right=-120) +
  f'<div class="a" style="left:0;top:0;width:620px;bottom:0;background:linear-gradient(90deg,rgba(10,12,16,.9),transparent);z-index:7"></div>'
  f'<div class="a an" style="left:70px;top:560px;width:600px;font-size:104px;line-height:1.02;z-index:10">SUA MARCA PARECE <span class="cx">MENOR</span> <span class="it" style="color:{AU}">que o seu negócio?</span></div>' +
  fita(1150, 3, '3 SINAIS ✦ ARRASTE ✦ ') + rod('Nº 03')))
# 04 C · case Dublê roxo (R2): celular gigante inclinado + cartões, selo, número 04
S.append(('posts/04', fundo('C', '#7B6BF5') + topo(True, 'Case · Dublê') +
  f'<div class="a ol" style="left:40px;top:120px;font-size:420px;-webkit-text-stroke-color:{MA};z-index:2;opacity:.6">04</div>' +
  mock('duble-cartoes.jpg', 520, 330, 520, 420, 9, 4) + mock('duble-celular.jpg', 60, 420, 700, 620, -7, 5) + selo(820, 760, 200) +
  f'<div class="a an" style="left:70px;top:1060px;font-size:130px;color:{OB};z-index:10">SÓ GRAVA QUEM <span class="it" style="color:{MA}">disse sim.</span></div>' + rod('Identidade + app')))
# 05 O · bastidor (R1): rosto c16 sobre ouro, RABISCO escuro gigante atrás
S.append(('posts/05', fundo('O') + topo(False, 'Bastidor') +
  f'<div class="a an" style="left:-10px;top:150px;font-size:290px;color:{OB};z-index:3">RABISCO</div>' + face('c16', 1040, x=330) +
  f'<div class="a" style="left:60px;top:560px;width:340px;height:420px;background:#f6f1e6;transform:rotate(-7deg);z-index:8;box-shadow:0 30px 60px rgba(60,30,0,.45);padding:26px">'
  f'<svg viewBox="0 0 100 110" width="288" height="320"><g fill="none" stroke="#222" stroke-width=".9"><circle cx="50" cy="50" r="36" stroke-dasharray="3 2"/><path d="M22 58 Q50 12 78 40"/><path d="M20 62 Q52 20 80 46"/><line x1="8" y1="50" x2="92" y2="50" stroke="#c33"/><line x1="50" y1="8" x2="50" y2="92" stroke="#c33"/></g><text x="50" y="106" font-size="6" text-anchor="middle" font-family="monospace" fill="#555">RASCUNHO 03 · GRAFITE</text></svg></div>'
  f'<div class="a" style="left:0;right:0;bottom:0;height:300px;background:{OB};z-index:9"></div>'
  f'<div class="a an" style="left:70px;bottom:110px;font-size:104px;z-index:10">TODA MARCA COMEÇA <span class="it" style="color:{AU}">num rabisco.</span></div>' + rod('Processo, não sorte')))
# 06 D · anatomia: LOGO ≠ MARCA, 3 mockups em leque, número 4 contorno
S.append(('posts/06', fundo('D') + topo(True, 'Anatomia') +
  f'<div class="a an" style="left:70px;top:130px;font-size:170px;z-index:10">LOGO <span style="color:{AU}">NÃO É</span><br>MARCA</div>' +
  f'<div class="a ol" style="right:30px;top:290px;font-size:520px;z-index:2">4</div>' +
  mock('realtime-cartoes.jpg', 40, 480, 470, 560, -10, 5) + mock('oregano-cartoes.jpg', 330, 440, 470, 600, 2, 6) + mock('duble-papelaria.jpg', 600, 500, 440, 540, 11, 7) +
  fita(1100, -3, 'LETRAS ✦ CORES ✦ GRAFISMOS ✦ VARIAÇÕES ✦ ') + rod('4 peças fazem a família visual')))
# 07 C · case Real Time azul: NO AR gigante, outdoor inclinado, selo
S.append(('posts/07', fundo('C', '#2F8FE0') + topo(True, 'Case · Real Time') +
  f'<div class="a an" style="left:50px;top:110px;font-size:420px;color:{OB};z-index:2">NO AR</div>' +
  mock('realtime-outdoor.jpg', 70, 560, 940, 600, -4, 5) + selo(60, 470, 190) +
  fita(1135, 4, 'PRODUTORA ✦ NO AR, AGORA ✦ ', OB, '#7cc4ff') +
  f'<div class="a" style="left:640px;top:450px;z-index:10;font-size:76px;color:{MA}"><span class="it">agora.</span></div>' + rod('Identidade + rua')))
# 08 D · rosto c07 + JULGA gigante, frase em caixa
S.append(('posts/08', fundo('D') + topo(True, 'Limiar') +
  f'<div class="a an" style="left:0;right:0;top:130px;text-align:center;font-size:400px;color:{AU};z-index:3">JULGA</div>' +
  f'<div class="a ol" style="left:30px;top:640px;font-size:280px;z-index:2">08</div>' + face('c07', 1020, x=300) +
  f'<div class="a" style="left:0;right:0;bottom:0;height:470px;background:linear-gradient(transparent,{OB} 65%);z-index:7"></div>'
  f'<div class="a an" style="left:70px;bottom:150px;font-size:112px;z-index:10">SEU CLIENTE <span class="cx">JULGA</span> <span class="it" style="color:{AU}">antes de ler.</span></div>' + selo(830, 520, 180) + rod('Cor e letra chegam primeiro')))
# 09 O · quanto custa (R3): tipografia ocupando tudo + cartões Leo como identidade
S.append(('posts/09', fundo('O') + topo(False, 'Pergunta honesta') +
  f'<div class="a an" style="left:60px;top:130px;font-size:250px;color:{OB};z-index:3">QUANTO<br>CUSTA</div>' +
  mock('leo-cartoes.jpg', 520, 600, 520, 480, 8, 5) +
  f'<div class="a" style="left:60px;top:700px;width:460px;z-index:10;font-size:86px;line-height:1;color:{OB}"><span class="it">uma marca impro&shy;visada?</span></div>' +
  fita(1130, -4, 'CLIENTE VAI EMBORA SEM DIZER POR QUÊ ✦ ', OB, AU) + rod('Leia a legenda', False)))
# 10 C · verde Orégano: pôster gigante inclinado + cartões, número 10
S.append(('posts/10', fundo('C', '#1E5B3B') + topo(True, 'Case · Orégano Turbo') +
  f'<div class="a ol" style="right:30px;top:100px;font-size:420px;z-index:2;-webkit-text-stroke-color:#F2B33D">10</div>' +
  mock('oregano-poster.jpg', 540, 300, 470, 700, 6, 5) + mock('oregano-cartoes.jpg', 60, 560, 520, 470, -8, 6) +
  f'<div class="a an" style="left:70px;top:140px;width:520px;font-size:150px;color:{MA};z-index:10">DO RASCUNHO</div>' +
  fita(1080, -3, 'PEDIDO Nº ✦ DO RASCUNHO À RUA ✦ ', '#F2B33D', OB) +
  f'<div class="a" style="left:70px;top:1180px;font-size:70px;z-index:10;color:{MA}"><span class="it">à rua.</span></div>' + rod('Pizzaria')))
# 11 D · rosto c09 + TRAVESSIA, duas fitas cruzadas
S.append(('posts/11', fundo('D') + topo(True, 'Manifesto') +
  f'<div class="a an" style="left:-20px;top:170px;font-size:250px;color:{AU};z-index:3;white-space:nowrap">TRAVESSIA</div>' + face('c09', 1040, x=180) +
  fita(790, -7) + fita(870, 5, 'PROCESSO ✦ CONCEITO ✦ SISTEMA ✦ ', OB, AU, 8) +
  f'<div class="a" style="left:0;right:0;bottom:0;height:360px;background:linear-gradient(transparent,{OB} 30%);z-index:10"></div>'
  f'<div class="a an" style="left:70px;bottom:100px;font-size:92px;line-height:1.1;z-index:11">MARCA NÃO É ENFEITE.<br><span class="it" style="color:{AU}">é passagem.</span></div>' + rod('Nº 11')))
# 12 O · CTA: rosto c11 sobre ouro, SUA VEZ gigante, selo
S.append(('posts/12', fundo('O') + topo(False, 'Agenda aberta') +
  f'<div class="a an" style="left:0;right:0;top:150px;text-align:center;font-size:300px;white-space:nowrap;color:{OB};z-index:3">SUA VEZ</div>' + face('c11', 1030, x=250, esp=True) + selo(810, 560, 200) +
  f'<div class="a" style="left:0;right:0;bottom:0;height:290px;background:{OB};z-index:9"></div>' +
  f'<div class="a an" style="left:70px;bottom:120px;font-size:96px;z-index:10">VAMOS ATRAVESSAR <span class="it" style="color:{AU}">a sua?</span></div>' + rod('Orçamento no WhatsApp · link na bio')))

# ===== 2 CARROSSÉIS · 5 telas, nenhuma repete layout =====
S += [
 ('carrosseis/c1-anatomia/1', fundo('O') + topo(False, 'Carrossel · arraste') +
   f'<div class="a an" style="left:0;right:0;top:130px;text-align:center;font-size:470px;color:{OB};z-index:3">LOGO</div>' + face('c12', 1040, x=220) +
   fita(930, -5, 'NÃO É MARCA ✦ ', OB, AU) +
   f'<div class="a" style="left:0;right:0;bottom:0;height:250px;background:{OB};z-index:9"></div>'
   f'<div class="a an" style="left:70px;bottom:100px;font-size:96px;z-index:10">SÓ TER UM <span class="it" style="color:{AU}">não basta.</span></div>' + rod('Arraste →')),
 ('carrosseis/c1-anatomia/2', fundo('D') + topo(True, '01 de 04') +
   f'<div class="a ol" style="left:20px;top:110px;font-size:1150px;z-index:2">4</div>'
   f'<div class="a an" style="left:520px;top:170px;width:520px;font-size:100px;line-height:1.18;z-index:10">PEÇAS FAZEM UMA <span class="cx">FAMÍLIA</span></div>' +
   ''.join(f'<div class="a an" style="left:520px;top:{700+k*120}px;font-size:70px;z-index:10"><span style="color:{AU}">0{k+1}</span> {t}</div>' for k, t in enumerate(['LETRAS', 'CORES', 'GRAFISMOS', 'VARIAÇÕES'])) + rod('Faltou uma, a marca manca')),
 ('carrosseis/c1-anatomia/3', ''.join(f'<div class="a" style="left:0;right:0;top:{y}px;height:{h}px;background:{c}"></div>' for y, h, c in [(0, 810, '#1E5B3B'), (810, 337, '#C8302B'), (1147, 203, '#F3EEE6')]) +
   f'<div class="a an" style="left:60px;top:90px;font-size:300px;color:#F2B33D">60%</div>'
   f'<div class="a an" style="left:60px;top:420px;font-size:120px;color:{MA}">COR COM<br><span class="it">proporção.</span></div>' +
   mock('oregano-celular.jpg', 690, 90, 330, 500, 7, 5) +
   f'<div class="a an" style="left:60px;top:880px;font-size:160px;color:{MA}">25%</div><div class="a mn" style="left:440px;top:960px">tomate #C8302B</div>'
   f'<div class="a an" style="left:60px;top:1180px;font-size:120px;color:{OB}">15%</div><div class="a mn" style="left:300px;top:1235px;color:{OB}">creme #F3EEE6 · case Orégano Turbo</div>'),
 ('carrosseis/c1-anatomia/4', fundo('C', '#7B6BF5') + topo(True, '03 de 04') +
   f'<div class="a an" style="left:60px;top:130px;font-size:230px;color:{OB};z-index:3">EM TUDO.</div>' +
   mock('duble-poster.jpg', 40, 470, 420, 620, -9, 5) + mock('duble-embalagem.jpg', 330, 520, 420, 560, 3, 6) + mock('duble-cartoes.jpg', 640, 450, 400, 600, 12, 7) +
   fita(1140, 3, 'CONSISTÊNCIA NOS DETALHES PARECE CARO ✦ ', OB, '#c9c1ff') + rod('Case Dublê')),
 ('carrosseis/c1-anatomia/5', fundo('D') + topo(True, 'Salve') +
   f'<div class="a an" style="left:0;right:0;top:150px;text-align:center;font-size:250px;white-space:nowrap;color:{AU};z-index:3">SUA MARCA</div>' + face('c14', 1000, x=200, esp=True) + selo(820, 560, 200) +
   f'<div class="a" style="left:0;right:0;bottom:0;height:420px;background:linear-gradient(transparent,{OB} 55%);z-index:7"></div>'
   f'<div class="a an" style="left:70px;bottom:200px;font-size:100px;z-index:10">VAMOS ATRAVESSAR <span class="it" style="color:{AU}">a sua?</span></div>'
   f'<div class="a mn" style="left:70px;bottom:130px;z-index:10;background:{AU};color:{OB};padding:12px 18px">Orçamento no WhatsApp · link na bio</div>' + rod('Compartilhe')),
]
S += [
 ('carrosseis/c2-processo/1', fundo('D') + topo(True, 'Carrossel · arraste') +
   f'<div class="a ol" style="left:-20px;top:100px;font-size:900px;z-index:2">6</div>'
   f'<div class="a an" style="left:430px;top:150px;font-size:250px;color:{AU};z-index:3">ETAPAS</div>' + face('c15', 1030, x=260) +
   f'<div class="a" style="left:0;right:0;bottom:0;height:420px;background:linear-gradient(transparent,{OB} 60%);z-index:7"></div>' + fita(990, 4) +
   f'<div class="a an" style="left:70px;bottom:110px;font-size:96px;z-index:10">COMO UMA MARCA <span class="it" style="color:{AU}">atravessa.</span></div>' + rod('Arraste →')),
 ('carrosseis/c2-processo/2', fundo('O') + topo(False, 'A travessia') +
   ''.join(f'<div class="a" style="left:60px;right:60px;top:{170+k*190}px;height:170px;border-top:3px solid {OB};display:flex;align-items:center;gap:36px;z-index:5"><span class="an old" style="font-size:150px">0{k+1}</span><span class="an" style="font-size:86px;color:{OB}">{e}</span></div>'
   for k, e in enumerate(['BRIEFING E PERSONA', 'PESQUISA PREMIUM', 'CONCEITO', 'SISTEMA VISUAL', 'APLICAÇÕES', 'MANUAL'])) + rod('Prazo combinado no início', False)),
 ('carrosseis/c2-processo/3', fundo('C', '#C8302B') + topo(True, '03 · Conceito') +
   f'<div class="a an" style="left:60px;top:130px;font-size:200px;color:{MA};z-index:3">GRID ANTES</div>' +
   f'<div class="a" style="left:110px;top:420px;width:860px;height:760px;background:#f6f1e6;transform:rotate(-3deg);z-index:5;box-shadow:0 50px 90px rgba(0,0,0,.5)">'
   f'<svg width="860" height="760" style="position:absolute;inset:0"><g stroke="#c33" opacity=".55"><line x1="430" y1="0" x2="430" y2="760"/><line x1="0" y1="380" x2="860" y2="380"/></g><g fill="none" stroke="#888" stroke-dasharray="7 5"><circle cx="430" cy="380" r="300"/><circle cx="430" cy="380" r="200"/></g></svg>'
   f'<img src="{u(LOGO+"/barzakh-simbolo-ouro.png")}" style="position:absolute;left:230px;top:180px;width:400px"></div>' +
   fita(1170, 3, 'DE ENFEITE ✦ ', OB, AU) + rod('Construção do símbolo')),
 ('carrosseis/c2-processo/4', fundo('D') + topo(True, '05 · Aplicação') +
   mock('realtime-fachada.jpg', 0, 160, 1080, 760, 0, 3) +
   f'<div class="a" style="left:0;right:0;top:600px;height:320px;background:linear-gradient(transparent,{OB});z-index:4"></div>'
   f'<div class="a an" style="left:60px;top:720px;font-size:180px;line-height:1.02;z-index:10">TESTE NA <span class="cx">RUA</span></div>'
   f'<div class="a" style="left:60px;top:960px;font-size:80px;z-index:10;color:{AU}"><span class="it">antes da rua.</span></div>' + rod('Mockup · case Real Time')),
 ('carrosseis/c2-processo/5', fundo('O') + topo(False, 'Salve') +
   f'<div class="a an" style="left:0;right:0;top:140px;text-align:center;font-size:360px;color:{OB};z-index:3">AGENDA</div>' + face('c08', 1010, x=240) +
   fita(900, -4, 'AGENDA ABERTA ✦ UM ESTÚDIO AL KÁNTARA ✦ ', OB, AU) +
   f'<div class="a" style="left:0;right:0;bottom:0;height:270px;background:{OB};z-index:9"></div>'
   f'<div class="a an" style="left:70px;bottom:110px;font-size:96px;z-index:10">A PRÓXIMA PODE SER <span class="it" style="color:{AU}">a sua.</span></div>' + rod('Link na bio')),
]
# ===== 3 CAPAS DE REEL 1080x1920 (centro seguro 1080x1350) — sem rosto: mockups grandes, para não repetir foto =====
def reel(i, t, cor, big, l1, l2, mk, ftxt):
    dark = t != 'O'
    c = MA if dark else OB
    return (f'reels/reel-r{i}-capa-1080x1920', fundo(t, cor) +
      f'<div class="a an" style="left:0;right:0;top:300px;text-align:center;font-size:{360 if len(big)<8 else 250}px;white-space:nowrap;color:{AU if t=="D" else OB};z-index:3">{big}</div>' +
      mock(mk[0], 60, 700, 560, 640, -8, 5) + mock(mk[1], 470, 640, 560, 700, 7, 6) + selo(820, 1240, 200) +
      fita(1420, -4, ftxt, OB if t != 'D' else AU, AU if t != 'D' else OB) +
      f'<div class="a an" style="left:70px;top:1540px;width:940px;font-size:100px;color:{c};z-index:10">{l1} <span class="it" style="color:{AU if t!="O" else OB}">{l2}</span></div>' +
      f'<div class="a mn" style="left:70px;top:240px;color:{c};z-index:10">Reel · Barzakh</div>', 1920)
R = [reel(1, 'D', None, 'MENOR?', 'SUA MARCA PARECE', 'menor?', ('realtime-poster.jpg', 'realtime-celular.jpg'), 'ASSISTA ATÉ O FIM ✦ '),
     reel(2, 'O', None, 'A CAIXA', 'A CAIXA QUE', 'fala por você.', ('oregano-embalagem.jpg', 'oregano-poster.jpg'), 'PIZZARIA ✦ EMBALAGEM ✦ '),
     reel(3, 'C', '#7B6BF5', '6 ETAPAS', 'UMA MARCA EM', '6 etapas.', ('duble-papelaria.jpg', 'duble-outdoor.jpg'), 'PROCESSO BARZAKH ✦ ')]

if __name__ == '__main__':
    html = f'<html><head><meta charset="utf-8"><style>{CSS}</style></head><body>' + ''.join(sec(k.replace('/', '_'), b) for k, b in S) + ''.join(sec(r[0].replace('/', '_'), r[1], r[2]) for r in R) + '</body></html>'
    open(G + '/pecas.html', 'w').write(html)
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=CHROME); pg = b.new_page(viewport={'width': 1080, 'height': 1350})
        pg.goto(u(G + '/pecas.html')); pg.wait_for_timeout(2000)
        for k in [s[0] for s in S] + [r[0] for r in R]:
            f = OUT + '/' + k + '.jpg'; os.makedirs(os.path.dirname(f), exist_ok=True)
            pg.locator('#' + k.replace('/', '_')).screenshot(path=f, type='jpeg', quality=90); print(k)
        b.close()
