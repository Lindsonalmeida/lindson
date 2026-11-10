# Apresentação em 5 stories para vender o rebranding da WF Celulares (Designer gráfico · conta Leandro · 10/11/2026)
# É o Lindson mostrando o trabalho. Linha escura e premium das artes-02. Copy: PADRAO-COPY (simples, uma leitura).
# Composição copiada de: keynote Apple (antes × depois em tela dividida, título fino), cases do Behance (mockups em leque),
# Bang & Olufsen (produto + coluna de texto). Gera pecas.html -> node render.js -> 0*.jpg
import os, sys
D = os.path.dirname(os.path.abspath(__file__)); W = os.path.join(D, '..'); sys.path.insert(0, os.path.join(W, 'identidade'))
import gerar3 as g
PRATA, BRANCO, TITA, TG = g.PRATA, g.BRANCO, g.TITA, g.TIT_GRAD
GRAD = lambda t: f'<span style="background:{TG};-webkit-background-clip:text;color:transparent">{t}</span>'
VIDRO = 'background:rgba(255,255,255,.08);backdrop-filter:blur(18px);border:1px solid rgba(255,255,255,.16)'
FUNDO = 'radial-gradient(ellipse 90% 60% at 50% 45%,#1c1c1f,#000 70%)'
TOPO = f'<div style="position:absolute;left:70px;top:90px;font:400 26px Inter;color:{PRATA};letter-spacing:.02em">@lindsonalmeida_ · case WF Celulares</div>'
num = lambda n: f'<div style="position:absolute;right:70px;top:90px;font:300 26px Inter;color:{TITA}">{n}/5</div>'
P = []
sec = lambda id, n, c, f=FUNDO: P.append(f'<section class="f" id="{id}" style="width:1080px;height:1920px;background:#000"><div style="position:absolute;inset:0;background:{f}"></div>{TOPO}{num(n)}{c}</section>')

# 1 · gancho: antes × depois
sec('01-antes-depois', 1, f'''
<div style="position:absolute;left:70px;top:200px;font:200 120px/1 Inter;letter-spacing:-.05em;color:{BRANCO}">Mesma loja.<br>{GRAD("Outra marca.")}</div>
<div style="position:absolute;left:70px;right:70px;top:540px;height:1060px;display:flex;gap:20px">
<div style="flex:1;border-radius:36px;overflow:hidden;position:relative;background:#111"><img src="../referencias-cliente/logo-atual.jpg" style="width:100%;height:100%;object-fit:contain;filter:saturate(.8) brightness(.9)">
<span style="position:absolute;left:24px;top:24px;{VIDRO};border-radius:30px;padding:10px 22px;font:400 24px Inter;color:{BRANCO}">Antes</span></div>
<div style="flex:1;border-radius:36px;overflow:hidden;position:relative;background:radial-gradient(circle at 50% 40%,#2a2a2e,#000 70%);display:flex;align-items:center;justify-content:center"><div style="width:330px">{g.logo_svg()}</div>
<span style="position:absolute;left:24px;top:24px;{VIDRO};border-radius:30px;padding:10px 22px;font:400 24px Inter;color:{BRANCO}">Depois</span></div></div>
<div style="position:absolute;left:70px;right:70px;top:1650px;font:300 34px/1.4 Inter;color:{PRATA}">Rebranding da WF Celulares, loja de iPhone em São Luís. Toca pra ver como foi →</div>''')

# 2 · o que travava (sem humilhar)
it = lambda n, t, s: (f'<div style="{VIDRO};border-radius:32px;padding:36px 40px;margin-bottom:24px"><div style="font:300 24px Inter;color:{TITA}">{n}</div>'
    f'<div style="font:300 46px/1.2 Inter;color:{BRANCO};margin-top:8px;letter-spacing:-.02em">{t}</div><div style="font:300 28px/1.4 Inter;color:#a1a1a6;margin-top:10px">{s}</div></div>')
sec('02-o-que-travava', 2, f'''
<div style="position:absolute;left:70px;top:200px;font:200 104px/1.02 Inter;letter-spacing:-.05em;color:{BRANCO}">O produto era bom.<br>{GRAD("A marca não contava isso.")}</div>
<div style="position:absolute;left:70px;right:70px;top:620px">
{it("01","Logo com efeito 3D","bonito de perto, mas some no tamanho do celular")}
{it("02","Foto de perfil com promoção","o cliente via o preço, não a loja")}
{it("03","@ difícil de digitar","quem ouvia o nome não achava o perfil")}
{it("04","Nada mostrava a garantia","e quem compra seminovo quer ter certeza")}</div>''')

# 3 · nova marca
sec('03-nova-marca', 3, f'''
<div style="position:absolute;left:0;right:0;top:300px;display:flex;justify-content:center"><div style="width:520px">{g.logo_svg()}</div></div>
<div style="position:absolute;left:70px;right:70px;top:1040px;text-align:center;font:200 96px/1.05 Inter;letter-spacing:-.05em;color:{BRANCO}">Celular com<br>{GRAD("procedência.")}</div>
<div style="position:absolute;left:110px;right:110px;top:1340px;text-align:center;font:300 34px/1.45 Inter;color:{PRATA}">A marca de sempre, mais limpa e moderna. E uma ideia que vende: todo iPhone sai com laudo, garantia e nota.</div>
<div style="position:absolute;left:0;right:0;top:1600px;display:flex;justify-content:center;gap:16px;font:300 26px Inter;color:{BRANCO}">
<span style="{VIDRO};border-radius:40px;padding:14px 28px">Testado</span><span style="{VIDRO};border-radius:40px;padding:14px 28px">Bateria medida</span><span style="{VIDRO};border-radius:40px;padding:14px 28px">Garantia</span></div>''')

# 4 · aplicações (leque de mockups: perfil, feed, fachada, manual)
cel = lambda img, x, y, r, s=1: (f'<div style="position:absolute;left:{x}px;top:{y}px;width:{380*s}px;height:{780*s}px;border-radius:{56*s}px;border:{10*s}px solid #2a2a2e;overflow:hidden;'
    f'transform:rotate({r}deg);box-shadow:0 40px 80px rgba(0,0,0,.7);background:#000"><img src="{img}" style="width:100%;height:100%;object-fit:cover"></div>')
sec('04-aplicacoes', 4, f'''
<div style="position:absolute;left:70px;top:200px;font:200 104px/1.02 Inter;letter-spacing:-.05em;color:{BRANCO}">Do perfil<br>{GRAD("à fachada.")}</div>
{cel("../artes-02/previa-grade.jpg", 60, 520, -8)}{cel("../artes-02/04-oferta-17-pro-max-silver.jpg", 640, 520, 8)}{cel("../identidade/pecas-final/03-avatar.jpg", 350, 470, 0)}
<img src="../identidade/pecas-final/13-fachada.jpg" style="position:absolute;left:70px;top:1340px;width:560px;height:315px;object-fit:cover;border-radius:24px;box-shadow:0 30px 60px #000">
<img src="../identidade/manual-pags/09.jpg" style="position:absolute;left:660px;top:1340px;width:350px;height:197px;object-fit:cover;border-radius:18px">
<img src="../identidade/manual-pags/11.jpg" style="position:absolute;left:660px;top:1558px;width:350px;height:197px;object-fit:cover;border-radius:18px">
<div style="position:absolute;left:70px;top:1790px;font:300 30px Inter;color:{PRATA}">Logo, manual de 22 páginas, 9 artes, destaques e fachada.</div>''')

# 5 · CTA (padrão copy: conexão, dor, desejo, pergunta)
sec('05-cta', 5, f'''
<div style="position:absolute;left:70px;top:260px;font:200 110px/1.02 Inter;letter-spacing:-.05em;color:{BRANCO}">Sua loja vende bem,<br>mas a marca<br>{GRAD("não mostra isso?")}</div>
<div style="position:absolute;left:70px;right:70px;top:760px;font:300 40px/1.45 Inter;color:{PRATA}">Eu monto a marca, o perfil e as artes da sua loja, do jeito que eu fiz pra WF.</div>
<div style="position:absolute;left:70px;right:70px;top:1160px;{VIDRO};border-radius:44px;padding:50px;text-align:center">
<div style="font:300 48px Inter;color:{BRANCO}">Quer isso na sua loja?</div><div style="font:500 44px Inter;margin-top:16px">{GRAD("Me chama no direct")}</div></div>
<div style="position:absolute;left:0;right:0;top:1500px;text-align:center;font:300 64px Inter;letter-spacing:-.02em;color:{BRANCO}">@lindsonalmeida_</div>
<div style="position:absolute;left:0;right:0;top:1600px;text-align:center;font:300 26px Inter;color:{TITA}">Lindson Almeida · São Luís</div>''')

html = ('<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Inter:wght@200;300;400;500&display=swap" rel="stylesheet">'
        '<style>body{margin:0;background:#333}section.f{position:relative;overflow:hidden;margin:0 0 40px}img{display:block}</style></head><body>' + ''.join(P) + '</body></html>')
open(os.path.join(D, 'pecas.html'), 'w').write(html); print(len(P), 'stories')
