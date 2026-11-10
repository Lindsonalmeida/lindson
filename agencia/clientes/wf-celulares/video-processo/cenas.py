# Cenas do vídeo "processo WF Celulares" (1080×1920) · conta Leandro · 10/11/2026
# Estilo (dados/agencia/referencias/edit-ia-pro, 13 estilos): nº 5 "Motion explicativo" + nº 9 "Antes e depois";
# catálogo motion-animacao-vfx: #41 tipografia cinética, #25 2.5D/parallax, #28 UI motion (mockup de celular),
# #163 zoom, #166 corte na batida, #169 flash de luz, #152 light leak, #35 grão.
# Gera cenas.html -> node render.js -> cenas/*.png (fundo + camada de frente separadas para o parallax)
import os, sys
D = os.path.dirname(os.path.abspath(__file__)); W = os.path.join(D, '..'); sys.path.insert(0, os.path.join(W, 'identidade'))
import gerar3 as g
PRATA, BRANCO, TITA, TG = g.PRATA, g.BRANCO, g.TITA, g.TIT_GRAD
GRAD = lambda t: f'<span style="background:{TG};-webkit-background-clip:text;color:transparent">{t}</span>'
FUNDO = 'radial-gradient(ellipse 90% 60% at 50% 45%,#1c1c1f,#000 70%)'
AVISO = '<div style="position:absolute;left:0;right:0;bottom:40px;text-align:center;font:300 22px Inter;color:#6e6e73">voz do Lindson gerada por IA · @lindsonalmeida_</div>'
tit = lambda a, b, y=220: f'<div style="position:absolute;left:70px;right:70px;top:{y}px;font:200 112px/1.02 Inter;letter-spacing:-.05em;color:{BRANCO}">{a}<br>{GRAD(b)}</div>'
etq = lambda t: f'<div style="position:absolute;left:70px;top:120px;font:400 28px Inter;letter-spacing:.24em;color:{TITA}">{t}</div>'
cel = lambda img, x, y, w=560, r=0, fit='cover': (f'<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{w*2.05}px;border-radius:{w*.14}px;border:{w*.025}px solid #2c2c30;'
    f'overflow:hidden;transform:rotate({r}deg);box-shadow:0 50px 100px rgba(0,0,0,.8);background:#000"><img src="{img}" style="width:100%;height:100%;object-fit:{fit}"></div>')
S = []
def cena(id, corpo):
    S.append(f'<section class="f" id="{id}" style="width:1080px;height:1920px;background:#000"><div style="position:absolute;inset:0;background:{FUNDO}"></div>{corpo}{AVISO}</section>')

R = '../referencias-cliente/'; I = '../identidade/'; A = '../artes-02/'
cena('01-antes', etq('ANTES') + tit('Uma loja boa,', 'uma marca confusa.') + cel(R + 'logo-atual.jpg', 260, 640, 560, -4, 'contain'))
cena('02-engenharia', etq('ENGENHARIA REVERSA') + tit('Primeiro,', 'entender tudo.') +
     f'<img src="{R}perfil-instagram-10-11.png" style="position:absolute;left:40px;top:700px;width:1000px;border-radius:24px;box-shadow:0 40px 80px #000">' +
     ''.join(f'<div style="position:absolute;left:{x}px;top:{y}px;background:rgba(255,255,255,.1);backdrop-filter:blur(16px);border:1px solid rgba(255,255,255,.2);border-radius:30px;padding:16px 28px;font:300 32px Inter;color:#fff">{t}</div>'
             for x, y, t in [(70, 1260, 'logo some no celular'), (420, 1380, 'perfil com promoção'), (120, 1500, '@ difícil de achar'), (460, 1620, 'garantia escondida')]))
cena('03-logo', etq('A NOVA MARCA') + f'<div style="position:absolute;left:0;right:0;top:480px;display:flex;justify-content:center"><div style="width:600px">{g.logo_svg()}</div></div>'
     + f'<div style="position:absolute;left:0;right:0;top:1300px;text-align:center;font:200 100px/1.05 Inter;letter-spacing:-.05em;color:#fff">Celular com<br>{GRAD("procedência.")}</div>')
cena('04-laudo', etq('O CONCEITO') + tit('Todo iPhone', 'sai com laudo.') + f'<img src="{I}pecas-final/14-cartao-etiqueta.jpg" style="position:absolute;left:-420px;top:700px;width:1900px">')
cena('05-manual', etq('MANUAL DA MARCA · 22 PÁGINAS') + tit('Cada detalhe', 'no papel.') +
     ''.join(f'<img src="{I}manual-pags/{p}.jpg" style="position:absolute;left:{x}px;top:{y}px;width:760px;border-radius:18px;transform:rotate({r}deg);box-shadow:0 40px 80px #000">'
             for p, x, y, r in [('11', 60, 760, -7), ('09', 260, 1000, 4), ('06', 120, 1250, -2), ('01', 220, 1490, 3)]))
grade = [f'{A}{f}' for f in sorted(os.listdir(os.path.join(W, 'artes-02'))) if f[:2].isdigit() and f.endswith('.jpg')]
for k in range(1, 10):
    cel_grade = ''.join(f'<img src="{grade[i]}" style="position:absolute;left:{60 + (i % 3) * 324}px;top:{620 + (i // 3) * 405}px;width:316px;height:395px;object-fit:cover;opacity:{1 if i < k else 0}">' for i in range(9))
    cena(f'06-feed-{k}', etq('9 ARTES PARA O FEED') + tit('Cara de', 'vitrine premium.') + cel_grade)
cena('07-cta', tit('Quer isso', 'na sua loja?', 520) + f'<div style="position:absolute;left:70px;top:860px;font:300 56px Inter;color:#fff">Me chama no direct.</div>'
     + f'<div style="position:absolute;left:0;right:0;top:1200px;text-align:center;font:300 84px Inter;letter-spacing:-.02em;color:#fff">@lindsonalmeida_</div>'
     + f'<div style="position:absolute;left:0;right:0;top:1330px;display:flex;justify-content:center"><div style="width:200px">{g.logo_svg()}</div></div>')
html = ('<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Inter:wght@200;300;400&display=swap" rel="stylesheet">'
        '<style>body{margin:0;background:#333}section.f{position:relative;overflow:hidden;margin:0 0 40px}img{display:block}</style></head><body>' + ''.join(S) + '</body></html>')
open(os.path.join(D, 'pecas.html'), 'w').write(html); print(len(S), 'cenas')
