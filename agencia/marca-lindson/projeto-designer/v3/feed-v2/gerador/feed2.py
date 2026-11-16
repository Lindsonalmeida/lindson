# Barzakh · feed v2 "com vida" (conta Leandro, 16/11/2026). A v1 (../../feed/) foi REPROVADA: "feed morto, não é atraente".
# Mudanças: rosto do Lindson recortado (rec/, recortar.py) com rim light âmbar, cases na COR VIVA de cada cliente,
# xadrez de 3 tons (D escuro/ouro · C cor do case · L marfim claro), manchete Fraunces gigante legível na miniatura.
# Referências (../TEMPLATE.md):
#   R1 The Futur (EUA) ...... rosto do fundador grande + manchete gorda curta -> posts e capas com rosto
#   R2 &Walsh (EUA) ......... case em cor saturada chapada, produto enorme -> posts de case em cor viva
#   R3 Manual (EUA) ......... serifa editorial + quadro de cor quente, muito contraste -> posts marfim (L)
# Uso: PYTHONPATH=<scratchpad>/py python3 feed2.py
import os
from PIL import Image
from playwright.sync_api import sync_playwright
G = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.dirname(G)
V3 = '/home/user/lindson/agencia/marca-lindson/projeto-designer/v3'
MK = '/home/user/lindson/agencia/marca-lindson/projeto-designer/v2/mockups'
FONT = '/home/user/lindson/agencia/marca-holding/v2/fontes'
LOGO = V3 + '/marca/logos/png/ouro'
T = V3 + '/marca/gerador/trat'
u = lambda p: 'file://' + p
OB, MA, BR, LA = '#0A0C10', '#EEEAE2', '#B4935A', '#2B3A8F'
OURO = 'linear-gradient(115deg,#7a5e2f 0%,#d9bd84 22%,#8c6c38 40%,#e8d3a2 55%,#94733d 72%,#c9a86c 100%)'
NOISE = "url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='220' height='220'%3E%3Cfilter id='n'%3E%3CfeTurbulence baseFrequency='.85' numOctaves='3'/%3E%3C/filter%3E%3Crect width='220' height='220' filter='url(%23n)' opacity='.6'/%3E%3C/svg%3E\")"
CASE = {  # cor viva de cada cliente (dos mockups aprovados da v2)
    'oregano': ('#1E5B3B', '#F2C94C', 'Orégano Turbo', 'pizzaria'),
    'leo': ('#1F2F9E', '#F5C518', 'Leo Pinto', 'vereador'),
    'duble': ('#8B7CFF', '#0A0C10', 'Dublê', 'app de voz'),
    'realtime': ('#4FA8E8', '#0A0C10', 'Real Time', 'produtora'),
}
CSS = f"""
@font-face{{font-family:'Fraunces';src:url('file://{FONT}/Fraunces-Regular.ttf');font-weight:400}}
@font-face{{font-family:'Fraunces';src:url('file://{FONT}/Fraunces-SemiBold.ttf');font-weight:600}}
@font-face{{font-family:'Fraunces';font-style:italic;src:url('file://{FONT}/Fraunces-Italic%5BSOFT,WONK,opsz,wght%5D.ttf')}}
@font-face{{font-family:'Inter Tight';src:url('file://{FONT}/InterTight-SemiBold.ttf');font-weight:600}}
@font-face{{font-family:'Inter Tight';src:url('file://{FONT}/InterTight-Medium.ttf');font-weight:500}}
@font-face{{font-family:'JetBrains Mono';src:url('file://{FONT}/JetBrainsMono-Medium.ttf')}}
*{{box-sizing:border-box;margin:0;padding:0}} body{{background:#000}}
.pg{{width:1080px;position:relative;overflow:hidden;font-family:'Inter Tight';font-weight:500;color:{MA};margin-bottom:20px}}
.pg:after{{content:'';position:absolute;inset:0;background-image:{NOISE};opacity:.11;mix-blend-mode:overlay;pointer-events:none;z-index:20}}
.a{{position:absolute}}
.mn{{font-family:'JetBrains Mono';font-size:19px;letter-spacing:.18em;text-transform:uppercase}}
.fr{{font-family:'Fraunces';font-weight:600;letter-spacing:-.025em;line-height:.92}}
.it{{font-family:'Fraunces';font-style:italic;font-weight:400}}
.ouro{{background:{OURO};-webkit-background-clip:text;background-clip:text;color:transparent}}
.p{{font-size:30px;line-height:1.4}}
.face{{position:absolute;bottom:0;z-index:5;filter:saturate(1.12) contrast(1.06) drop-shadow(0 0 1.5px rgba(255,200,120,.85)) drop-shadow(-14px -6px 26px rgba(255,166,60,.38)) drop-shadow(0 30px 50px rgba(0,0,0,.5))}}
.esp{{transform:scaleX(-1)}}
.tag{{display:inline-block;padding:10px 18px;border-radius:40px;font-family:'JetBrains Mono';font-size:18px;letter-spacing:.14em;text-transform:uppercase}}
.mock{{position:absolute;background-size:cover;background-position:center;box-shadow:0 50px 90px rgba(0,0,0,.45);border-radius:6px}}
"""

def face(c, h=1000, x=None, right=None, esp=False, z=5):
    pos = f'left:{x}px' if x is not None else f'right:{right}px'
    return f'<img class="face{" esp" if esp else ""}" src="{u(G+"/rec/"+c+".png")}" style="height:{h}px;{pos};z-index:{z}">'

def fundo(t, cor=None):
    if t == 'D':
        return (f'<div class="a" style="inset:0;background:{OB}"></div><div class="a" style="inset:0;background:url({u(T+"/concreto-escuro-v2.jpg")}) center/cover;opacity:.45"></div>'
                f'<div class="a" style="inset:0;background:radial-gradient(circle at 62% 42%,rgba(214,150,60,.55),rgba(43,58,143,.35) 38%,transparent 70%)"></div>')
    if t == 'L':
        return (f'<div class="a" style="inset:0;background:{MA}"></div><div class="a" style="inset:0;background:url({u(T+"/concreto-v2.jpg")}) center/cover;opacity:.22;mix-blend-mode:multiply"></div>')
    return f'<div class="a" style="inset:0;background:{cor}"></div><div class="a" style="inset:0;background:radial-gradient(circle at 30% 20%,rgba(255,255,255,.22),transparent 55%),radial-gradient(circle at 90% 100%,rgba(0,0,0,.35),transparent 60%)"></div>'

def rod(t, n=None, dark=True):
    c = 'rgba(238,234,226,.85)' if dark else 'rgba(10,12,16,.75)'
    bgc = 'rgba(10,12,16,.55)' if dark else 'rgba(238,234,226,.85)'
    return (f'<div class="a mn" style="left:80px;right:80px;bottom:56px;display:flex;justify-content:space-between;color:{c};font-size:16px;z-index:12">'
            f'<span>@barzakhstudio</span><span style="background:{bgc};padding:6px 10px">{t}</span></div>')

def logo_av(x, y, s):
    return f'<img class="a" src="{u(LOGO+"/barzakh-simbolo-ouro.png")}" style="left:{x}px;top:{y}px;width:{s}px;z-index:12">'

def sec(i, body, h=1350):
    return f'<section class="pg" id="{i}" style="height:{h}px">{body}</section>'

S = []
# Ordem de postar (D escuro · C cor · L marfim; vizinho na grade e post seguido nunca iguais): 01 D Barzakh · 02 C mosaico · 03 L quanto custa · 04 C Dublê · 05 L rascunho · 06 D bastidor · 07 L caixa · 08 D anatomia · 09 C Real Time · 10 D menor · 11 C Leo · 12 L julga
# ============ 12 POSTS (número = ordem de postar; grade mostra 12 no topo-esquerda) ============
# 01 L · apresentação (R3 Manual): marfim, rosto c12 à direita, manchete à esquerda
S.append(('posts/03', fundo('L') + face('c12', 860, right=-230) +
  f'<div class="a mn" style="left:80px;top:80px;color:{LA}">Nº 03 · prazer</div>'
  f'<div class="a fr" style="left:80px;top:170px;width:560px;font-size:136px;color:{OB}">Quanto custa uma marca <span class="it" style="color:#9a7a3e">impro&shy;visada?</span></div>'
  f'<div class="a p" style="left:80px;top:900px;width:330px;color:#333">Cliente que não entende a sua marca vai embora sem dizer por quê.</div>' + rod('Barzakh · a passagem da sua marca', dark=False)))
# 02 C · mosaico de cases (R2 &Walsh)
mos = ''.join(f'<div class="mock" style="left:{80+(k%2)*470}px;top:{300+(k//2)*470}px;width:450px;height:450px;background-image:url({u(MK+"/"+m)})"></div>'
              for k, m in enumerate(['oregano-embalagem.jpg', 'curso-poster.jpg', 'duble-cartoes.jpg', 'realtime-celular.jpg']))
S.append(('posts/02', fundo('C', '#C8302B') + f'<div class="a fr" style="left:80px;top:90px;font-size:112px;color:{MA}">4 marcas, <span class="it">4 travessias.</span></div>' + mos + rod('Cases reais · arraste o perfil')))
# 03 D · rosto c10 + logo (apresentação do estúdio)
S.append(('posts/01', fundo('D') + f'<div class="a fr ouro" style="left:40px;top:130px;font-size:228px;z-index:3;letter-spacing:-.04em">BARZAKH</div>' + face('c10', 1000, x=150) +
  f'<div class="a" style="left:0;right:0;bottom:0;height:520px;background:linear-gradient(transparent,{OB} 75%);z-index:6"></div>'
  f'<div class="a fr" style="left:80px;bottom:150px;width:900px;font-size:92px;z-index:8">A passagem da <span class="it ouro">sua marca.</span></div>'
  f'<div class="a mn" style="left:80px;bottom:110px;color:{BR};z-index:8">Lindson Almeida · direção criativa</div>' + rod('um estúdio Al Kántara')))
# 04 C · case Dublê (roxo)
S.append(('posts/04', fundo('C', '#8B7CFF') + f'<div class="mock" style="left:80px;top:420px;width:920px;height:690px;background-image:url({u(MK+"/duble-celular.jpg")})"></div>'
  f'<div class="a tag" style="left:80px;top:90px;background:{OB};color:#c9c1ff">Case · Dublê · app de voz</div>'
  f'<div class="a fr" style="left:80px;top:170px;font-size:118px;color:{OB}">Só grava quem <span class="it">disse sim.</span></div>' + rod('Identidade + app', dark=False)))
# 05 D · bastidor com rosto c14 (o rascunho na mão)
S.append(('posts/06', fundo('D') + face('c14', 980, right=-60) +
  f'<div class="a mn" style="left:80px;top:90px;color:{BR}">Bastidor · Nº 06</div>'
  f'<div class="a fr" style="left:80px;top:160px;width:560px;font-size:128px;z-index:8">Toda marca começa <span class="it ouro">num rabisco.</span></div>'
  f'<div class="a" style="left:80px;top:760px;width:360px;height:360px;background:#f3eee2;transform:rotate(-6deg);box-shadow:0 40px 70px rgba(0,0,0,.6);z-index:7;padding:30px">'
  f'<img src="{u(LOGO+"/barzakh-simbolo-ouro.png")}" style="width:100%;filter:grayscale(1) contrast(2.2) brightness(.55) blur(.4px);opacity:.8"><div class="a mn" style="left:30px;bottom:18px;color:#555;font-size:14px">rascunho 03 · grafite</div></div>' + rod('Processo, não sorte')))
# 06 L · antes/depois de processo (rascunho -> marca aplicada), case Orégano
S.append(('posts/05', fundo('L') +
  f'<div class="a fr" style="left:80px;top:80px;font-size:120px;color:{OB}">Do rascunho <span class="it" style="color:#1E5B3B">à rua.</span></div>'
  f'<div class="a" style="left:80px;top:360px;width:450px;height:760px;background:#fbf8f1;box-shadow:0 30px 60px rgba(0,0,0,.18);display:flex;align-items:center;justify-content:center">'
  f'<svg width="380" height="380" viewBox="0 0 100 100"><g fill="none" stroke="#555" stroke-width=".8" stroke-dasharray="3 1.5"><circle cx="50" cy="50" r="38"/><path d="M30 62 Q50 15 72 40"/><path d="M28 60 Q52 22 70 44"/><line x1="10" y1="50" x2="90" y2="50" stroke="#c33"/><line x1="50" y1="10" x2="50" y2="90" stroke="#c33"/></g><text x="50" y="96" font-size="5" text-anchor="middle" fill="#777" font-family="monospace">ANTES · ESBOÇO</text></svg></div>'
  f'<div class="mock" style="left:550px;top:360px;width:450px;height:760px;background-image:url({u(MK+"/oregano-poster.jpg")})"></div>'
  f'<div class="a mn" style="left:550px;top:1135px;color:#1E5B3B">Depois · Orégano Turbo</div>' + rod('Antes e depois de processo', dark=False)))
# 07 C · case Real Time (azul)
S.append(('posts/09', fundo('C', '#4FA8E8') + f'<div class="mock" style="left:-40px;top:430px;width:1160px;height:870px;background-image:url({u(MK+"/realtime-papelaria.jpg")})"></div>'
  f'<div class="a tag" style="left:80px;top:90px;background:{OB};color:#9fd2f7">Case · Real Time · produtora</div>'
  f'<div class="a fr" style="left:80px;top:170px;font-size:150px;color:{OB}">No ar, <span class="it">agora.</span></div>' + rod('Identidade + papelaria', dark=False)))
# 08 L · rosto c08 + manchete
S.append(('posts/12', fundo('L') + f'<div class="a fr" style="left:60px;top:900px;font-size:330px;color:rgba(10,12,16,.08);z-index:2">JULGA</div>' + face('c08', 920, x=380) +
  f'<div class="a fr" style="left:80px;top:110px;width:520px;font-size:112px;color:{OB};z-index:8">Seu cliente <span class="it" style="color:#9a7a3e">julga antes</span> de ler.</div>'
  f'<div class="a p" style="left:80px;top:720px;width:340px;color:#333;z-index:8">Cor, letra e cuidado chegam primeiro. O texto chega depois.</div>' + rod('Limiar · Nº 12', dark=False)))
# 09 D · sistema de marca em ouro (monolito grande + grid de construção)
S.append(('posts/08', fundo('D') +
  f'<svg class="a" style="inset:0;z-index:3" width="1080" height="1350"><g stroke="rgba(201,168,108,.35)" fill="none"><circle cx="540" cy="700" r="380"/><circle cx="540" cy="700" r="260"/><line x1="0" y1="700" x2="1080" y2="700"/><line x1="540" y1="200" x2="540" y2="1200"/></g></svg>'
  + logo_av(240, 400, 600) +
  f'<div class="a fr" style="left:80px;top:90px;font-size:104px;z-index:8">Logo sozinho <span class="it ouro">não é marca.</span></div>'
  f'<div class="a mn" style="left:80px;bottom:110px;color:{BR};z-index:8">Símbolo · cores · letras · grafismos · aplicações</div>' + rod('Anatomia · Nº 08')))
# 10 C · case Leo (azul + amarelo), outdoor
# 11 C · case WF Celulares (preto premium sobre ouro escovado; sem maçã: só o WF em titânio, frase do brand book da WF). Leo saiu: vereador não entra com cara de campanha.
TI = 'linear-gradient(160deg,#f4f4f2 0%,#9a9da3 35%,#e9eaec 55%,#6f7278 80%,#cfd1d4 100%)'
S.append(('posts/11', f'<div class="a" style="inset:0;background:{OURO}"></div><div class="a" style="inset:0;background:radial-gradient(circle at 30% 20%,rgba(255,240,200,.35),transparent 55%),radial-gradient(circle at 85% 95%,rgba(40,25,5,.5),transparent 60%)"></div>'
  f'<div class="a tag" style="left:80px;top:90px;background:{OB};color:#d9dbe0">Case · WF Celulares · loja de iPhone</div>'
  f'<div class="a fr" style="left:80px;top:170px;width:920px;font-size:116px;color:{OB}">Procedência que <span class="it">dá para ver.</span></div>'
  f'<div class="a" style="left:150px;top:560px;width:780px;height:560px;background:linear-gradient(150deg,#1c1d20,#050506);border-radius:28px;transform:rotate(-4deg);box-shadow:0 60px 100px rgba(40,25,5,.6),inset 0 1px 0 rgba(255,255,255,.15);display:flex;flex-direction:column;align-items:center;justify-content:center">'
  f'<div style="font-family:Inter Tight;font-weight:600;font-size:250px;letter-spacing:-.06em;line-height:1;background:{TI};-webkit-background-clip:text;color:transparent">WF</div>'
  f'<div style="font-family:Inter Tight;font-weight:500;font-size:34px;letter-spacing:.55em;color:#c9cbd0;margin-top:10px">CELULARES</div></div>' + rod('Identidade + papelaria', dark=False)))
# 11 L · case Orégano em marfim (embalagem gigante)
S.append(('posts/07', fundo('L') + f'<div class="mock" style="left:80px;top:420px;width:920px;height:690px;background-image:url({u(MK+"/oregano-embalagem.jpg")})"></div>'
  f'<div class="a tag" style="left:80px;top:90px;background:#1E5B3B;color:#F3EEE6">Case · Orégano Turbo · pizzaria</div>'
  f'<div class="a fr" style="left:80px;top:170px;font-size:112px;color:{OB}">A caixa é a mídia <span class="it" style="color:#C8302B">mais vista.</span></div>' + rod('Embalagem · Nº 07', dark=False)))
# 12 D · rosto c13 + gancho principal (R1 The Futur)
S.append(('posts/10', fundo('D') + f'<div class="a fr" style="left:-10px;top:1000px;font-size:290px;color:rgba(201,168,108,.20);z-index:3;letter-spacing:-.05em">MENOR</div>' + face('c13', 980, right=-230) +
  f'<div class="a" style="left:0;top:0;width:640px;bottom:0;background:linear-gradient(90deg,rgba(10,12,16,.85),transparent);z-index:6"></div>'
  f'<div class="a fr" style="left:80px;top:110px;width:560px;font-size:116px;z-index:8">Sua marca parece <span class="it ouro">menor</span> que o seu negócio?</div>'
  f'<div class="a p" style="left:80px;top:870px;width:400px;z-index:8;color:#d8d2c6">3 sinais de marca improvisada. Arraste.</div>' + rod('Limiar · Nº 10')))

# ============ 3 CARROSSÉIS (5 telas, nenhuma repete layout) ============
def cta(cid, c, esp):
    return (cid, fundo('D') + face(c, 760, x=320, esp=esp) +
      f'<div class="a" style="left:0;right:0;bottom:0;height:560px;background:linear-gradient(transparent,{OB} 60%);z-index:6"></div>'
      f'<div class="a fr" style="left:80px;top:100px;width:920px;font-size:100px;z-index:8">Vamos atravessar <span class="it ouro">a sua?</span></div>'
      f'<div class="a tag" style="left:80px;bottom:200px;background:{OURO};color:{OB};z-index:8;font-size:22px">Orçamento no WhatsApp · link na bio</div>'
      f'<div class="a mn" style="left:80px;bottom:150px;color:{BR};z-index:8">Lindson Almeida · Barzakh</div>' + rod('Salve e compartilhe'))
# C1 Anatomia
S += [
 ('carrosseis/c1-anatomia/1', fundo('C', '#C8302B') + f'<div class="a fr" style="left:30px;top:140px;font-size:400px;color:{MA};z-index:3;letter-spacing:-.05em">LOGO</div>' + face('c15', 980, x=220) +
   f'<div class="a fr" style="left:80px;top:90px;font-size:64px;z-index:8;color:{OB}">Só ter um</div>'
   f'<div class="a" style="left:0;right:0;bottom:0;height:380px;background:linear-gradient(transparent,rgba(10,12,16,.92));z-index:6"></div>'
   f'<div class="a fr" style="left:80px;bottom:150px;font-size:96px;z-index:8">não é ter <span class="it" style="color:#F2B33D">marca.</span></div>' + rod('Arraste →')),
 ('carrosseis/c1-anatomia/2', fundo('L') + f'<div class="a fr" style="left:60px;top:40px;font-size:900px;color:#C8302B;line-height:.9">4</div>'
   f'<div class="a fr" style="left:560px;top:320px;width:440px;font-size:96px;color:{OB}">peças fazem uma <span class="it" style="color:#C8302B">família visual.</span></div>'
   f'<div class="a p" style="left:560px;top:820px;width:440px;color:#333">Letras, cores, grafismos e variações do logo. Faltou uma, a marca manca.</div>' + rod('01 de 04', dark=False)),
 ('carrosseis/c1-anatomia/3', ''.join(f'<div class="a" style="left:0;right:0;top:{y}px;height:{h}px;background:{c}"></div>' for y, h, c in [(0, 810, '#1E5B3B'), (810, 337, '#C8302B'), (1147, 203, '#F3EEE6')]) +
   f'<div class="a fr" style="left:80px;top:100px;font-size:120px">Cor com <span class="it" style="color:#F2B33D">proporção.</span></div>'
   f'<div class="a mn" style="left:80px;top:700px">60% · verde #1E5B3B</div><div class="a mn" style="left:80px;top:1060px">25% · tomate #C8302B</div>'
   f'<div class="a mn" style="left:80px;top:1190px;color:{OB}">15% · creme #F3EEE6 · case Orégano Turbo</div>'),
 ('carrosseis/c1-anatomia/4', fundo('D') + f'<div class="a fr ouro" style="left:80px;top:150px;font-size:520px;letter-spacing:-.04em">Aa</div>'
   f'<div class="a fr" style="left:80px;top:760px;width:900px;font-size:96px">1 letra de título. <span class="it ouro">1 de texto.</span></div>'
   f'<div class="a p" style="left:80px;top:1020px;width:820px;color:#cfc8bb">Uma família com pesos diferentes resolve a hierarquia. Cinco fontes viram ruído.</div>' + rod('03 de 04')),
 cta('carrosseis/c1-anatomia/5', 'c09', True),
]
# C2 Case Leo Pinto
S += [
 ('carrosseis/c2-case-leo/1', fundo('C', '#1F2F9E') + f'<div class="a fr" style="left:40px;top:160px;font-size:420px;color:#F5C518;z-index:3;letter-spacing:-.05em">CASE</div>' + face('c16', 940, x=170) +
   f'<div class="a" style="left:0;right:0;bottom:0;height:380px;background:linear-gradient(transparent,rgba(10,15,60,.95));z-index:6"></div>'
   f'<div class="a fr" style="left:80px;bottom:150px;width:920px;font-size:88px;z-index:8">Como nasceu a marca <span class="it" style="color:#F5C518">Leo Pinto.</span></div>'
   f'<div class="a mn" style="left:80px;top:90px;z-index:8">Bastidor de case · 5 telas</div>' + rod('Arraste →')),
 ('carrosseis/c2-case-leo/2', fundo('L') + f'<div class="mock" style="left:0;top:0;width:1080px;height:810px;border-radius:0;background-image:url({u(MK+"/leo-papelaria.jpg")})"></div>'
   f'<div class="a fr" style="left:80px;top:880px;width:920px;font-size:96px;color:{OB}">Só fonte, logo e cor. <span class="it" style="color:#1F2F9E">Nada de enfeite.</span></div>' + rod('Papelaria', dark=False)),
 ('carrosseis/c2-case-leo/3', fundo('C', '#F5C518') + f'<div class="mock" style="left:330px;top:120px;width:680px;height:1110px;background-image:url({u(MK+"/leo-celular.jpg")})"></div>'
   f'<div class="a fr" style="left:70px;top:140px;width:300px;font-size:84px;color:#1F2F9E">No celular, onde as pessoas estão.</div>' + rod('Redes', dark=False)),
 ('carrosseis/c2-case-leo/4', fundo('D') + ''.join(f'<div class="mock" style="left:{80+k*310}px;top:{360+(k%2)*80}px;width:290px;height:520px;background-image:url({u(MK+"/leo-"+m+".jpg")})"></div>' for k, m in enumerate(['cartoes', 'embalagem', 'poster']))
   + f'<div class="a fr" style="left:80px;top:110px;font-size:96px">A mesma marca <span class="it ouro">em tudo.</span></div>'
   f'<div class="a p" style="left:80px;top:1040px;width:900px;color:#cfc8bb">Cartão, copo, cartaz. Consistência nos detalhes é o que parece caro.</div>' + rod('Aplicações')),
 cta('carrosseis/c2-case-leo/5', 'c11', True),
]
# C3 Processo
S += [
 ('carrosseis/c3-processo/1', fundo('L') + f'<div class="a fr" style="left:30px;top:230px;font-size:240px;color:{OB};z-index:3;letter-spacing:-.05em;white-space:nowrap">6 ETAPAS</div>' + face('c08', 960, x=230, esp=True) +
   f'<div class="a fr" style="left:80px;top:90px;font-size:70px;color:{OB};z-index:8">Como uma marca <span class="it" style="color:#9a7a3e">atravessa</span></div>'
   f'<div class="a" style="left:0;right:0;bottom:0;height:300px;background:linear-gradient(transparent,{MA});z-index:6"></div>'
   f'<div class="a tag" style="left:80px;bottom:140px;background:{OB};color:{MA};z-index:8">Processo Barzakh · arraste</div>' + rod('Bastidor', dark=False)),
 ('carrosseis/c3-processo/2', fundo('D') + ''.join(
   f'<div class="a" style="left:80px;top:{230+k*170}px;width:920px;border-top:1px solid rgba(201,168,108,.4);padding-top:24px;display:flex;gap:40px;align-items:baseline"><span class="fr ouro" style="font-size:90px;width:120px">0{k+1}</span><span class="fr" style="font-size:62px">{e}</span></div>'
   for k, e in enumerate(['Briefing e persona', 'Pesquisa premium', 'Conceito', 'Sistema visual', 'Aplicações', 'Entrega + manual']))
   + f'<div class="a mn" style="left:80px;top:110px;color:{BR}">A travessia, etapa por etapa</div>' + rod('Prazo combinado no início')),
 ('carrosseis/c3-processo/3', fundo('L') + f'<div class="a" style="left:80px;top:300px;width:920px;height:820px;background:#fbf8f1;box-shadow:0 30px 60px rgba(0,0,0,.15);overflow:hidden">'
   f'<svg width="920" height="820"><g stroke="#c33" stroke-width="1" opacity=".5"><line x1="460" y1="0" x2="460" y2="820"/><line x1="0" y1="410" x2="920" y2="410"/></g><g fill="none" stroke="#999" stroke-dasharray="6 4"><circle cx="460" cy="410" r="300"/><circle cx="460" cy="410" r="200"/></g></svg>'
   f'<img class="a" src="{u(LOGO+"/barzakh-simbolo-ouro.png")}" style="left:260px;top:210px;width:400px"></div>'
   f'<div class="a fr" style="left:80px;top:90px;font-size:110px;color:{OB}">Grid antes <span class="it" style="color:#9a7a3e">de enfeite.</span></div>' + rod('03 · Conceito', dark=False)),
 ('carrosseis/c3-processo/4', fundo('C', '#8B7CFF') + f'<div class="mock" style="left:0;top:330px;width:1080px;height:810px;border-radius:0;background-image:url({u(MK+"/duble-outdoor.jpg")})"></div>'
   f'<div class="a fr" style="left:80px;top:90px;font-size:110px;color:{OB}">Teste na rua <span class="it">antes da rua.</span></div>'
   f'<div class="a mn" style="left:80px;top:1180px;color:{OB}">05 · Aplicação em mockup · case Dublê</div>'),
 cta('carrosseis/c3-processo/5', 'c15', True),
]
# ============ 3 CAPAS DE REEL (1080x1920; área segura central 1080x1350) ============
def reel(i, t, cor, c, esp, big, l1, l2, tom_txt=MA, acc='ouro', fx=90, ty=1240):
    accs = 'class="it ouro"' if acc == 'ouro' else f'class="it" style="color:{acc}"'
    return (f'reels/reel-r{i}-capa-1080x1920', fundo(t, cor) +
      f'<div class="a fr" style="left:-10px;top:520px;font-size:330px;color:rgba(255,255,255,.16);z-index:3;letter-spacing:-.05em;white-space:nowrap">{big}</div>' + face(c, 1250, x=fx, esp=esp) +
      f'<div class="a" style="left:0;right:0;bottom:0;height:900px;background:linear-gradient(transparent,rgba(10,12,16,.95) 60%);z-index:6"></div>'
      f'<div class="a tag" style="left:80px;top:330px;background:{OB};color:{BR};z-index:8">Reel · Barzakh</div>'
      f'<div class="a fr" style="left:80px;top:{ty}px;width:920px;font-size:118px;z-index:8;color:{tom_txt}">{l1} <span {accs}>{l2}</span></div>' + rod('Assista até o fim'), 1920)
R = [reel(1, 'D', None, 'c11', False, 'MENOR', 'Sua marca parece', 'menor?'),
     reel(2, 'C', '#1E5B3B', 'c14', True, 'CAIXA', 'A caixa que', 'fala por você.', acc='#F2B33D', fx=330, ty=1180),
     reel(3, 'C', '#8B7CFF', 'c12', True, '6 ETAPAS', 'Uma marca em', '6 etapas.', acc='#e7e2ff', fx=-150, ty=1300)]

html = f'<html><head><meta charset="utf-8"><style>{CSS}</style></head><body>' + ''.join(sec(k.replace('/', '_'), b) for k, b in S) + ''.join(sec(r[0].replace('/', '_'), r[1], r[2]) for r in R) + '</body></html>'
open(G + '/pecas.html', 'w').write(html)
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1080, 'height': 1350})
    pg.goto(u(G + '/pecas.html')); pg.wait_for_timeout(1500)
    for k in [s[0] for s in S] + [r[0] for r in R]:
        f = OUT + '/' + k + '.jpg'; os.makedirs(os.path.dirname(f), exist_ok=True)
        pg.locator('#' + k.replace('/', '_')).screenshot(path=f, type='jpeg', quality=90); print(k)
    b.close()
