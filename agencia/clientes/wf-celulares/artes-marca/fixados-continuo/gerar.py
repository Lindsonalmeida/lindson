# WF Celulares · 3 posts fixados em PANORAMA (3240x1350 cortado em 3) · conta Zuleide · 10/11/2026
# Mesmo conteúdo do ../gerar.py (caminho B, Apple, escuro). Composição copiada de: carrossel/panorama de grade do
# Instagram (Apple @apple "split grid" de lançamento) + keynote Apple (linha de luz e reflexo atravessando o palco).
# Fundo: degradê contínuo preto -> bronze -> azul. Elementos que atravessam as divisas: linha de luz horizontal,
# reflexo do lineup (divisa 1|2) e o iPhone dourado (divisa 1|2) + iPhone dark mode (divisa 2|3).
import os, sys, re
D = os.path.dirname(os.path.abspath(__file__)); A = os.path.dirname(D)
sys.path.insert(0, os.path.join(A, '..', 'identidade')); import gerar3 as g
src = open(os.path.join(A, 'gerar.py')).read()
P = []
ns = {'__file__': os.path.join(A, 'gerar.py')}
exec(src.split("html = (")[0].replace("img/", "../img/"), ns)  # monta ns['P'] com as 3 seções
def miolo(s):  # tira a section e o fundo próprio, fica só o conteúdo
    s = re.sub(r'^<section[^>]*>', '', s); s = s[:-len('</section>')]
    return re.sub(r'^<div style="position:absolute;inset:0;background:[^"]*"></div>', '', s)
secs = {re.search(r'id="([^"]+)"', s).group(1): miolo(s) for s in ns['P']}
ordem = ['01-nova-wf', '02-procedencia', '03-onde-estamos']
fundo = ('linear-gradient(90deg,#000 0%,#0b0a09 18%,#2a2520 42%,#3a3228 52%,#1d2a40 68%,#0f2350 82%,#040a18 100%)')
brilho = ('radial-gradient(ellipse 30% 45% at 17% 55%,rgba(255,255,255,.06),transparent 70%),'
          'radial-gradient(ellipse 30% 50% at 50% 45%,rgba(212,180,140,.14),transparent 70%),'
          'radial-gradient(ellipse 30% 50% at 84% 45%,rgba(60,110,220,.18),transparent 70%)')
paineis = ''.join(f'<div style="position:absolute;left:{i*1080}px;top:0;width:1080px;height:1350px">{secs[k]}</div>' for i, k in enumerate(ordem))
luz = ('<div style="position:absolute;left:0;width:3240px;top:452px;height:2px;background:linear-gradient(90deg,transparent,rgba(255,255,255,.5) 15%,#d8c3a5 50%,#7fa6ff 85%,transparent);box-shadow:0 0 24px 4px rgba(220,200,170,.35)"></div>'
       '<div style="position:absolute;left:0;width:3240px;top:398px;height:110px;background:radial-gradient(ellipse 50% 50% at 50% 50%,rgba(255,240,220,.10),transparent 70%)"></div>')
# reflexo do lineup que se estende até o painel 2 + iPhone grande atravessando a divisa 2|3
cruz = ('<img src="../img/16-lineup.jpg" style="position:absolute;left:760px;top:1180px;width:900px;height:420px;object-fit:contain;transform:scaleY(-1) rotate(0);opacity:.14;mix-blend-mode:lighten;-webkit-mask-image:linear-gradient(to top,#000,transparent 35%)">'
        '<img src="../img/12-darkmode.png" style="position:absolute;left:1900px;top:820px;width:380px;height:740px;object-fit:contain;transform:rotate(-8deg);opacity:.55;mix-blend-mode:lighten;filter:blur(1px)">')
html = ('<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Inter:wght@200;300;400&display=swap" rel="stylesheet">'
        '<style>body{margin:0;background:#333}img{display:block;mix-blend-mode:lighten}</style></head><body>'
        f'<section id="pano" style="position:relative;overflow:hidden;width:3240px;height:1350px;background:{fundo}">'
        f'<div style="position:absolute;inset:0;background:{brilho}"></div>{luz}{cruz}{paineis}</section></body></html>')
open(os.path.join(D, 'pecas.html'), 'w').write(html)
