# Pinterest Barzakh · peças da estratégia (conta Zuleide, 18/11/2026).
# Padrão aprovado: placa em arco, monolito em ouro escovado, concreto, brilho Lápis (escuro.py da v3) + "clean e rico".
# Pin de designer = mockup em tela cheia, quase sem texto, legenda pequena (regra 16/11). Sem preço, sem chamada de anúncio.
# Uso: python3 gerar.py   (playwright + chromium)
import os, importlib.util
from PIL import Image
H = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.abspath(os.path.join(H, '..'))
V3 = '/home/user/lindson/agencia/marca-lindson/projeto-designer/v3'
sp = importlib.util.spec_from_file_location('dk', V3 + '/gerador/escuro.py'); dk = importlib.util.module_from_spec(sp); sp.loader.exec_module(dk)
OB, MA, GR, PE, BR, LA = dk.OB, dk.MA, dk.GR, dk.PE, dk.BR, dk.LA
PINS = V3 + '/pinterest/pins'
CSS = dk.CSS + '*{box-sizing:border-box;margin:0}body{background:#0A0C10;font-family:Inter Tight}.m{position:relative;overflow:hidden}.lbl{font:500 14px "JetBrains Mono";letter-spacing:.2em;text-transform:uppercase}img{display:block}'
f = lambda p: 'file://' + p

def legenda(t, s):
    """Legenda pequena (não é chamada): título serifa 34 px + linha mono, monolito pequeno à direita."""
    return (f'<div style="position:absolute;left:0;right:0;bottom:0;height:150px;background:linear-gradient(transparent,rgba(10,12,16,.92) 45%);padding:0 56px 40px;display:flex;align-items:flex-end;justify-content:space-between">'
            f'<div><div style="font:400 34px/1.1 Fraunces;color:{MA}">{t}</div><div class="lbl" style="font-size:12px;margin-top:10px;color:{BR}">{s}</div></div>'
            f'<div style="text-align:center">{dk.mono_inline(46)}<div class="lbl" style="font-size:10px;margin-top:6px;color:{BR}">BARZAKH</div></div></div>')
def num(n, t, cor=None): return f'<div class="lbl" style="position:absolute;left:56px;top:56px;color:{cor or MA};opacity:.75">{n} · {t}</div>'

def livro(w, h, rot=''):
    return (f'<div class="paper" style="position:absolute;width:{w}px;height:{h}px;background-color:#15171c;border-radius:3px 8px 8px 3px;box-shadow:inset 10px 0 14px rgba(0,0,0,.6),0 50px 80px rgba(0,0,0,.65);overflow:hidden;{rot}">'
            f'<div class="beam" style="left:{w*.1}px;top:{h*.18}px;width:{w*.8}px;height:{h*.45}px;opacity:.6"></div>{dk.mono(w*.42, w*.29, h*.2)}'
            f'<div class="foil" style="position:absolute;left:{w*.24}px;top:{h*.6}px;width:{w*.52}px;height:{w*.1}px;-webkit-mask-image:{dk.mask("logotipo-mono-branco")};mask-image:{dk.mask("logotipo-mono-branco")}"></div>'
            f'<div style="position:absolute;left:0;right:0;bottom:{h*.08}px;text-align:center;font:500 {w*.028}px JetBrains Mono;letter-spacing:.3em;color:{BR}">BRAND BOOK · 2026</div></div>')

CORES = [('Obsidiana', OB, MA), ('Lápis da Hora Azul', LA, MA), ('Bronze', BR, OB), ('Grafite', GR, MA), ('Pedra', PE, OB), ('Marfim', MA, OB)]
def chip(nome, hx, tx, w=300, h=470):
    return (f'<div class="paper" style="width:{w}px;height:{h}px;background-color:{hx};box-shadow:0 30px 50px rgba(0,0,0,.45);position:relative;flex:none">'
            f'<div style="position:absolute;left:22px;bottom:22px;color:{tx}"><div style="font:400 26px Fraunces">{nome}</div><div class="lbl" style="font-size:11px;margin-top:6px;opacity:.75">{hx.upper()}</div></div></div>')

def pins():
    P = []
    # 1 · hot stamping em macro: o monolito em ouro sobre papel, luz rasante (ref. Pinterest busca "identidade visual luxo")
    P.append(('hot-stamping', 'Monolito em hot stamping', 'Detalhe · ouro escovado sobre papel', f'''
<div class="paper grain" style="position:absolute;inset:0;background-color:#101218;overflow:hidden"><div class="win" style="opacity:.8"></div>
<div class="beam" style="left:80px;top:380px;width:840px;height:760px;opacity:.85"></div></div>
{dk.mono(820, 90, 300, 'filter:drop-shadow(0 2px 0 rgba(255,240,200,.4)) drop-shadow(0 -2px 2px rgba(0,0,0,.8)) drop-shadow(0 30px 40px rgba(0,0,0,.5))')}
{num('05', 'Hot stamping', BR)}'''))
    # 2 · brand book: capa escura em pé + livro deitado, sobre concreto (ref. Pentagram/Collins: o livro como objeto)
    P.append(('brand-book', 'Brand book · Barzakh', 'Manual de marca impresso · capa em ouro', f'''
<div class="grain" style="position:absolute;inset:0;overflow:hidden">{dk.parede(1000, 1500, .8)}<div style="position:absolute;left:0;right:0;bottom:0;height:520px;background:linear-gradient(#1a1c21,#0c0d10)"></div></div>
{livro(520, 720, 'left:300px;top:250px;transform:rotate(-2deg)')}
{livro(360, 500, 'left:140px;top:880px;transform:perspective(1400px) rotateX(58deg) rotateZ(-62deg)')}
{num('06', 'Brand book')}'''))
    # 3 · paleta: chips de cor em leque sobre concreto claro (busca guiada: "identidade visual" -> "paleta de cores")
    leque = ''.join(f'<div style="position:absolute;left:{330}px;top:{300}px;transform-origin:50% 120%;transform:rotate({-30+i*12}deg)">{chip(*c)}</div>' for i, c in enumerate(CORES))
    P.append(('paleta-de-cores', 'Paleta de cores · Barzakh', 'Obsidiana, Lápis, Bronze, Grafite, Pedra, Marfim', f'''
<div class="grain" style="position:absolute;inset:0;overflow:hidden"><div class="conc" style="position:absolute;inset:0;filter:brightness(1.15) contrast(.9)"></div><div style="position:absolute;inset:0;background:radial-gradient(ellipse at 50% 45%,transparent 30%,rgba(10,12,16,.55))"></div></div>
{leque}{num('07', 'Paleta', MA)}'''))
    # 4 · tipografia: BARZAKH gigante em ouro + espécime (ref. Lundgren+Lindqvist / Mucho: letra como imagem)
    P.append(('tipografia', 'Tipografia · Barzakh', 'Fraunces e JetBrains Mono', f'''
<div class="paper grain" style="position:absolute;inset:0;background-color:{OB};overflow:hidden"><div class="beam" style="left:-100px;top:200px;width:1200px;height:700px;opacity:.6"></div></div>
<div class="ouro" style="position:absolute;left:40px;top:160px;font:300 520px/0.9 Fraunces;letter-spacing:-.02em">Bz</div>
<div style="position:absolute;left:60px;right:60px;top:760px;border-top:1px solid rgba(180,147,90,.5);padding-top:26px;display:flex;justify-content:space-between;color:{MA}">
<div style="font:400 64px/1.05 Fraunces">Aa Bb Cc<br><span style="font-style:italic;color:{BR}">Passagem</span></div>
<div class="lbl" style="text-align:right;color:{PE};line-height:2.2">Fraunces · títulos<br>JetBrains Mono · rótulos<br>Inter Tight · texto</div></div>
<div class="lbl" style="position:absolute;left:60px;top:1060px;color:{BR};font-size:16px">A B C D E F G H I J K L M N O P Q R S T U V W X Y Z</div>
{num('08', 'Letras', BR)}'''))
    # 5 · arco: porta em arco no concreto com luz Lápis atravessando (o conceito: a passagem)
    P.append(('arco-passagem', 'A passagem · Barzakh', 'Arquitetura da marca · arco e luz', f'''
<div class="grain" style="position:absolute;inset:0;overflow:hidden">{dk.parede(1000, 1500, .6)}</div>
<div style="position:absolute;left:230px;top:230px;width:540px;height:1100px;border-radius:270px 270px 0 0;background:radial-gradient(ellipse at 50% 70%,#4a5fd0,#2B3A8F 35%,#0e1330 80%);box-shadow:inset 0 0 0 14px #121419,inset 0 0 80px rgba(0,0,0,.8),0 0 160px rgba(43,58,143,.55)"></div>
<div style="position:absolute;left:230px;top:1330px;width:540px;height:170px;background:linear-gradient(rgba(70,96,230,.45),transparent);filter:blur(18px)"></div>
{dk.mono(300, 350, 520)}
{num('09', 'Conceito')}'''))
    # 6 · cases: mosaico de 6 marcas reais com calha fina (ref. Koto: grade de trabalhos dá cor e prova)
    cs = ['oregano-embalagem', 'wf-cartoes', 'realtime-celular', 'curso-poster', 'duble-celular', 'leo-papelaria']
    g = ''.join(f'<div style="overflow:hidden;background:#111"><img src="{f(PINS + "/" + c + ".jpg")}" style="width:100%;height:118%;object-fit:cover;object-position:top"></div>' for c in cs)
    P.append(('cases', 'Marcas reais · Barzakh', 'Identidade visual para pequenas empresas', f'''
<div style="position:absolute;inset:0;background:{OB}"></div>
<div style="position:absolute;left:24px;right:24px;top:24px;height:1250px;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr 1fr;gap:12px">{g}</div>'''))
    return [(n, t, s, f'<div class="m" style="width:1000px;height:1500px">{b}{legenda(t, s)}</div>') for n, t, s, b in P]

def capa_perfil():
    return f'''<div class="m grain" style="width:1600px;height:900px">{dk.parede(1600, 900, .8)}
<div style="position:absolute;left:520px;top:110px;filter:drop-shadow(0 50px 50px rgba(0,0,0,.6))">{dk.placa(560/680)}</div></div>'''

if __name__ == '__main__':
    from playwright.sync_api import sync_playwright
    with sync_playwright() as pw:
        b = pw.chromium.launch(proxy={'server': os.environ['HTTPS_PROXY']} if os.environ.get('HTTPS_PROXY') else None, args=['--allow-file-access-from-files'])
        p = b.new_page()
        def shot(body, w, h, out):
            hp = H + '/_tmp.html'; open(hp, 'w').write(f'<!doctype html><html><head><meta charset="utf-8"><link href="{dk.FONTS}" rel="stylesheet"><style>{CSS}</style></head><body>{body}</body></html>')
            p.set_viewport_size({'width': w, 'height': h}); p.goto('file://' + hp, wait_until='networkidle'); p.evaluate('document.fonts.ready'); p.wait_for_timeout(400)
            p.screenshot(path=out + '.png', clip={'x': 0, 'y': 0, 'width': w, 'height': h}); Image.open(out + '.png').convert('RGB').save(out + '.jpg', quality=88); os.remove(out + '.png')
        for n, t, s, body in pins(): shot(body, 1000, 1500, f'{OUT}/pins/barzakh-{n}'); print(n)
        shot(capa_perfil(), 1600, 900, f'{OUT}/capas/capa-do-perfil-1600x900')
        os.remove(H + '/_tmp.html')
