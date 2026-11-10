# WF Celulares · 3 primeiros posts da marca nova (fecham a 1ª linha do feed) · conta Leandro · 10/11/2026
# Linha escura premium das artes-02. Imagens: Apple Newsroom (press images, uso autorizado pelo Lindson em 10/11).
# Composição copiada de: keynote Apple (logo central + lineup com reflexo) -> 1; apple.com Pro (cartão de vidro sobre
# produto) -> 2; Bang & Olufsen (coluna de texto + produto lateral) -> 3.
import os, sys
D = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(D, '..', 'identidade'))
import gerar3 as g
PRATA, BRANCO, TITA, TG = g.PRATA, g.BRANCO, g.TITA, g.TIT_GRAD
GRAD = lambda t: f'<span style="background:{TG};-webkit-background-clip:text;color:transparent">{t}</span>'
VIDRO = 'background:rgba(255,255,255,.08);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);border:1px solid rgba(255,255,255,.16)'
ILU = '<div style="position:absolute;right:30px;top:28px;font:300 14px Inter;color:#6e6e73">Imagem ilustrativa · Apple Newsroom</div>'
F = {'preto': 'radial-gradient(ellipse 80% 60% at 50% 50%,#1c1c1f,#000 70%)', 'titanio': 'radial-gradient(ellipse 90% 70% at 50% 40%,#3a3632,#14120f 75%)',
     'azul': 'radial-gradient(ellipse 90% 70% at 50% 45%,#0f2350,#030812 75%)'}
P = []
sec = lambda id, t, c: P.append(f'<section class="f" id="{id}" style="width:1080px;height:1350px;background:#000"><div style="position:absolute;inset:0;background:{F[t]}"></div>{c}{ILU}</section>')

sec('01-nova-wf', 'preto', f'''
<div style="position:absolute;left:0;right:0;top:110px;display:flex;justify-content:center"><div style="width:300px">{g.logo_svg()}</div></div>
<div style="position:absolute;left:0;right:0;top:500px;text-align:center;font:200 92px/1.05 Inter;letter-spacing:-.05em;color:{BRANCO}">Nova WF.<br>{GRAD("Mesma confiança.")}</div>
<div style="position:absolute;left:0;right:0;top:730px;text-align:center;font:300 34px Inter;color:{PRATA}">Agora com procedência.</div>
<img src="img/16-lineup.jpg" style="position:absolute;left:90px;top:830px;width:900px;height:420px;object-fit:contain">
<img src="img/16-lineup.jpg" style="position:absolute;left:90px;top:1250px;width:900px;height:420px;object-fit:contain;transform:scaleY(-1);opacity:.2;-webkit-mask-image:linear-gradient(to top,#000,transparent 30%)">''')

it = lambda t, s: f'<div style="display:flex;gap:22px;align-items:baseline;padding:20px 0;border-top:1px solid rgba(255,255,255,.14)"><span style="font:300 34px Inter;color:{BRANCO}">✓ {t}</span><span style="font:300 22px Inter;color:#a1a1a6">{s}</span></div>'
sec('02-procedencia', 'titanio', f'''
<img src="img/12-gold.jpg" style="position:absolute;left:470px;top:330px;width:680px;height:980px;object-fit:cover;object-position:20% 50%">
<div style="position:absolute;left:70px;top:90px;font:300 28px Inter;color:{PRATA}">O que é procedência</div>
<div style="position:absolute;left:70px;top:140px;font:200 100px/1.02 Inter;letter-spacing:-.05em;color:{BRANCO}">Todo iPhone<br>{GRAD("sai com laudo.")}</div>
<div style="position:absolute;left:70px;top:640px;width:620px;{VIDRO};background:rgba(30,28,26,.55);border-radius:36px;padding:40px 44px">
<div style="display:flex;align-items:center;gap:16px;margin-bottom:14px">{g.sim_bm(56)}<span style="font:400 30px Inter;color:{BRANCO}">Laudo WF</span></div>
{it("Testado","tela, câmera, som e sinal")}{it("Com garantia","por escrito")}{it("Com nota","fiscal, sempre")}</div>
<div style="position:absolute;left:70px;bottom:70px;font:300 26px Inter;color:{PRATA}">É assim que se compra seminovo sem medo.</div>''')

srv = lambda n, t, s: f'<div style="padding:26px 0;border-top:1px solid rgba(255,255,255,.14)"><span style="font:300 22px Inter;color:{TITA}">{n}</span><div style="font:200 58px/1.1 Inter;letter-spacing:-.03em;color:{BRANCO}">{t}</div><div style="font:300 24px Inter;color:#a1a1a6">{s}</div></div>'
sec('03-onde-estamos', 'azul', f'''
<img src="img/12-darkmode.png" style="position:absolute;left:640px;top:300px;width:420px;height:820px;object-fit:contain;transform:rotate(6deg)">
<div style="position:absolute;left:70px;top:90px;font:200 96px/1.02 Inter;letter-spacing:-.05em;color:{BRANCO}">O que a<br>{GRAD("gente faz.")}</div>
<div style="position:absolute;left:70px;top:390px;width:580px">{srv("01","Lacrados","iPhone, iPad e Xiaomi")}{srv("02","Seminovos","com laudo, garantia e nota")}{srv("03","Assistência","orçamento antes de mexer")}</div>
<div style="position:absolute;left:70px;right:70px;bottom:70px;{VIDRO};border-radius:36px;padding:30px 40px;display:flex;justify-content:space-between;align-items:center">
<div><div style="font:300 30px Inter;color:{BRANCO}">📍 São Cristóvão · Renascença</div><div style="font:300 24px Inter;color:{PRATA};margin-top:6px">São Luís · MA</div></div>
<div style="text-align:right"><div style="font:300 22px Inter;color:{PRATA}">WhatsApp</div><div style="font:400 34px Inter;color:{BRANCO}">(98) 98827-1882</div></div></div>''')

html = ('<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Inter:wght@200;300;400&display=swap" rel="stylesheet">'
        '<style>body{margin:0;background:#333}section.f{position:relative;overflow:hidden;margin:0 0 40px}img{display:block;mix-blend-mode:lighten}</style></head><body>' + ''.join(P) + '</body></html>')
open(os.path.join(D, 'pecas.html'), 'w').write(html); print(len(P), 'posts')
