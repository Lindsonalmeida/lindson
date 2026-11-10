# WF Celulares · PAINEL FIXADO (3 posts que formam 1 imagem) · Designer gráfico · conta Pedro · 10/11/2026
# Pedido do Lindson: "eu quero algo assim" (referencias/00-referencia-lindson.webp) + "use a nossa identidade visual".
# Copia SÓ a COMPOSIÇÃO da referência: benefícios com ícones à esquerda, logo no centro, produtos em pedestal à direita,
# linha de categorias + parcelamento + 3 selos embaixo. Cores, letras e logo = identidade WF aprovada (caminho B,
# identidade/gerar3.py): preto, grafite, titânio, prata, branco e o azul #2F6BFF só como luz de recorte.
# Acabamento premium copiado de: apple.com/br/iphone-17-pro (palco preto, manchete fina), iStyle (UAE, faixa de
# benefícios), iShop Mixup (MX, pedestal de produto), panorama fixado anterior da WF (linha de luz atravessando).
# Imagens: Apple Newsroom 09/2025 (iPhone 17 Pro color lineup; AirPods Pro 3 recortado com recorte2.py). Ilustrativas.
# Margem segura: a grade 3:4 do Instagram corta ~34 px de cada lado de cada post; texto fica a >= 100 px das divisas.
import os, sys
D = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(D, '..', 'identidade'))
import gerar3 as g
PRATA, BRANCO, TITA, GRAF, AZUL, TG = g.PRATA, g.BRANCO, g.TITA, g.GRAF, g.AZUL, g.TIT_GRAD
GRAD = lambda t: f'<span style="background:{TG};-webkit-background-clip:text;color:transparent">{t}</span>'
VIDRO = 'background:linear-gradient(135deg,rgba(255,255,255,.09),rgba(255,255,255,.03));backdrop-filter:blur(18px);border:1px solid rgba(255,255,255,.14)'
LOGO = open(os.path.join(D, '..', 'identidade', 'logo-b', 'wf-logo-b-cor.svg')).read()
def ic(p): return f'<svg viewBox="0 0 100 100" width="54" height="54" fill="none" stroke="{PRATA}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round">{p}</svg>'
I_LAUDO = ic('<rect x="22" y="12" width="56" height="76" rx="8"/><path d="M34 34 H66 M34 48 H66 M34 62 L44 72 L64 54"/>')
I_TEC = ic('<path d="M62 14 a16 16 0 0 0 -18 22 L16 64 a8 8 0 0 0 12 12 L56 48 a16 16 0 0 0 22 -18 l-10 10 -10 -2 -2 -10 z"/>')
I_ENT = ic('<path d="M8 30 H58 V68 H8 Z M58 44 H76 L90 56 V68 H58"/><circle cx="24" cy="72" r="7"/><circle cx="74" cy="72" r="7"/>')
I_CART = ic('<rect x="10" y="24" width="80" height="54" rx="8"/><path d="M10 40 H90 M24 62 H44"/>')
I_ESC = ic('<path d="M50 10 L84 24 V50 C84 70 68 84 50 90 C32 84 16 70 16 50 V24 Z M36 50 L46 60 L66 40"/>')
I_PIN = ic('<path d="M50 90 C50 90 20 60 20 40 a30 30 0 0 1 60 0 C80 60 50 90 50 90 Z"/><circle cx="50" cy="40" r="10"/>')

def ben(y, icone, rot, forte, sub):
    return (f'<div style="position:absolute;left:130px;top:{y}px;width:800px;display:flex;gap:30px;align-items:center;{VIDRO};border-radius:28px;padding:30px 36px;box-sizing:border-box">'
            f'<div style="width:96px;height:96px;border-radius:50%;flex:none;display:flex;align-items:center;justify-content:center;background:radial-gradient(circle at 35% 30%,#2a2a2e,#0a0a0b);border:1px solid rgba(255,255,255,.18);box-shadow:0 0 30px rgba(47,107,255,.25)">{icone}</div>'
            f'<div><div style="font:300 24px Inter;color:{PRATA};letter-spacing:.14em;text-transform:uppercase">{rot}</div>'
            f'<div style="font:500 44px/1.1 Inter;letter-spacing:-.02em;margin:6px 0">{GRAD(forte)}</div>'
            f'<div style="font:300 26px Inter;color:{PRATA}">{sub}</div></div></div>')
def selo(x, icone, a, b):
    return (f'<div style="position:absolute;left:{x}px;top:1150px;width:420px;display:flex;gap:18px;align-items:center">'
            f'<div style="transform:scale(.8)">{icone}</div><div style="font:300 24px/1.25 Inter;color:{PRATA}">{a}<br><b style="font-weight:500;color:{BRANCO}">{b}</b></div></div>')

fundo = ('radial-gradient(ellipse 22% 60% at 50% 42%,rgba(47,107,255,.30),transparent 70%),'
         'radial-gradient(ellipse 30% 55% at 83% 62%,rgba(47,107,255,.22),transparent 70%),'
         'radial-gradient(ellipse 30% 60% at 14% 45%,rgba(142,138,132,.16),transparent 70%),'
         'linear-gradient(180deg,#050506 0%,#000 55%,#0b0b0d 100%)')
# feixes de luz de estúdio (diagonais finas que atravessam as 3 artes)
feixes = ''.join(f'<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;transform:rotate({r}deg);transform-origin:0 50%;'
                 f'background:linear-gradient(90deg,transparent,{c} 45%,transparent);filter:blur({bl}px);opacity:{o}"></div>'
                 for x, y, w, h, r, c, bl, o in [(-200, 240, 1500, 3, -9, '#cfd3da', 1, .55), (-200, 270, 1500, 40, -9, AZUL, 22, .35),
                                                (1500, 1290, 1300, 3, -6, '#cfd3da', 1, .6), (1500, 1305, 1300, 50, -6, AZUL, 26, .45),
                                                (2500, 120, 900, 2, 12, '#9db6ff', 1, .5)])
# anel de titânio atrás do logo (o "anel magnético" da v2 virou palco), com luz de recorte azul
anel = (f'<div style="position:absolute;left:1290px;top:150px;width:660px;height:660px;border-radius:50%;'
        f'background:radial-gradient(circle at 50% 40%,#1c1c20,#050506 70%);box-shadow:0 0 0 2px #2b2b30,0 0 0 14px #0b0b0d,0 0 0 16px rgba(199,201,204,.5),0 0 90px 10px rgba(47,107,255,.45),inset 0 0 60px rgba(0,0,0,.9)"></div>'
        f'<div style="position:absolute;left:1276px;top:136px;width:688px;height:688px;border-radius:50%;background:conic-gradient(from 200deg,transparent 0deg,#f4f2ee 30deg,transparent 70deg,transparent 180deg,{AZUL} 220deg,transparent 260deg);'
        f'-webkit-mask:radial-gradient(circle,transparent 336px,#000 338px,#000 344px,transparent 345px);filter:blur(.5px)"></div>'
        f'<div style="position:absolute;left:1430px;top:250px;width:380px">{LOGO}</div>')
centro = (anel +
          f'<div style="position:absolute;left:1080px;width:1080px;top:880px;text-align:center;font:200 60px/1 Inter;letter-spacing:-.03em;color:{BRANCO}">iPhone <span style="color:{TITA}">·</span> iPad <span style="color:{TITA}">·</span> Assistência</div>'
          f'<div style="position:absolute;left:1080px;width:1080px;top:975px;display:flex;justify-content:center"><div style="{VIDRO};border-radius:60px;padding:18px 44px;font:300 34px Inter;color:{PRATA};box-shadow:0 0 40px rgba(47,107,255,.25)">Parcelamos em até <b style="font:500 46px Inter;color:{BRANCO}">18x</b> no cartão</div></div>'
          + selo(1180, I_ESC, 'Lacrados e seminovos', 'com laudo') + selo(1520, I_CART, 'Pix ou cartão', 'em até 18x') + selo(1850, I_PIN, 'São Cristóvão', 'e Renascença')
          + f'<div style="position:absolute;left:1500px;top:1160px;width:1px;height:70px;background:rgba(255,255,255,.18)"></div><div style="position:absolute;left:1830px;top:1160px;width:1px;height:70px;background:rgba(255,255,255,.18)"></div>')
esq = (f'<div style="position:absolute;left:130px;top:150px;font:300 26px Inter;color:{PRATA};letter-spacing:.2em">WF CELULARES · SÃO LUÍS</div>'
       f'<div style="position:absolute;left:130px;top:200px;font:200 104px/1 Inter;letter-spacing:-.05em;color:{BRANCO}">iPhone com<br>{GRAD("procedência.")}</div>'
       + ben(500, I_LAUDO, 'Lacrados e seminovos', 'Laudo WF', 'testado, com garantia e nota')
       + ben(720, I_TEC, 'Assistência técnica', 'Especializada', 'orçamento antes de mexer')
       + ben(940, I_ENT, 'Compra segura', 'Entrega em São Luís', 'consulte o seu bairro')
       + f'<div style="position:absolute;left:130px;top:1190px;font:300 28px Inter;color:{PRATA}">WhatsApp <b style="font-weight:500;color:{BRANCO}">(98) 98827-1882</b></div>')
def pedestal(x, y, w):
    return (f'<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{w*.16}px;border-radius:50%;background:radial-gradient(ellipse at 50% 30%,#3a3a40,#0c0c0e 70%);'
            f'box-shadow:0 2px 0 rgba(199,201,204,.55) inset,0 0 60px rgba(47,107,255,.45),0 30px 50px rgba(0,0,0,.9)"></div>'
            f'<div style="position:absolute;left:{x}px;top:{y+w*.08}px;width:{w}px;height:{w*.12}px;background:linear-gradient(180deg,#151518,#050506);border-radius:0 0 {w/2}px {w/2}px / 0 0 {w*.08}px {w*.08}px;z-index:-1"></div>')
dir_ = (f'<div style="position:absolute;left:2190px;top:150px;width:950px;text-align:right;font:300 26px Inter;color:{PRATA};letter-spacing:.2em">LINHA 17 PRO · AIRPODS PRO 3</div>'
        + pedestal(2300, 1010, 820)
        + f'<img src="img/17pro-lineup.jpg" style="position:absolute;left:2270px;top:262px;width:880px;height:880px;object-fit:contain;mix-blend-mode:lighten">'
        + pedestal(2150, 1110, 340)
        + f'<img src="img/airpods-pro-3.png" style="position:absolute;left:2210px;top:735px;width:230px;filter:drop-shadow(0 20px 30px rgba(0,0,0,.8)) brightness(.92)">'
        + f'<div style="position:absolute;right:110px;top:1250px;font:300 18px Inter;color:#6e6e73">Imagens ilustrativas · Apple Newsroom</div>')
grao = ('<svg style="position:absolute;inset:0;opacity:.07;mix-blend-mode:overlay" width="3240" height="1350"><filter id="n"><feTurbulence baseFrequency=".9" numOctaves="2"/></filter>'
        '<rect width="100%" height="100%" filter="url(#n)"/></svg>')
html = ('<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Inter:wght@200;300;400;500&display=swap" rel="stylesheet">'
        '<style>body{margin:0;background:#222}img{display:block}</style></head><body>'
        f'<section class="f" id="pano" style="position:relative;overflow:hidden;width:3240px;height:1350px;background:{fundo};font-family:Inter;isolation:isolate">'
        f'{feixes}{esq}{centro}{dir_}{grao}</section></body></html>')
open(os.path.join(D, 'pecas.html'), 'w').write(html)
