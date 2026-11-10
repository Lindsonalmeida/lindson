# WF Celulares · artes-02: 9 artes do feed, versão Pro escura (Designer gráfico · conta Leandro · 10/11/2026)
# v1 (artes-01) REPROVADA: "quero algo mais premium, esse branco parece pobre".
# Base: preto profundo, grafite, titânio escuro e azul profundo; produto grande, luz de estúdio, reflexo em vidro preto,
# tipografia fina de keynote, preço elegante, selos em vidro fosco. Imagens: Apple Newsroom (press images) -
# uso autorizado pelo Lindson em 10/11 ("pode pegar as imagens na internet"); fontes no README.
# Composição copiada de (TEMPLATE.md, seção artes-02): apple.com/iphone-17-pro (produto central + título fino),
# keynote (número gigante), Bang & Olufsen (produto lateral + texto em coluna), Nothing (ficha numerada),
# Samsung Unpacked (lineup em perspectiva com reflexo), Apple Newsroom (close de câmera sangrado).
import os, sys
D = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(D, '..', 'identidade'))
import gerar3 as g
PRATA, BRANCO, TITA, TG = g.PRATA, g.BRANCO, g.TITA, g.TIT_GRAD
F = {'preto': 'radial-gradient(ellipse 80% 60% at 50% 55%,#1c1c1f,#000 70%)',
     'titanio': 'radial-gradient(ellipse 90% 70% at 50% 40%,#3a3632,#14120f 75%)',
     'azul': 'radial-gradient(ellipse 90% 70% at 50% 45%,#0f2350,#030812 75%)'}
GRAD = lambda t: f'<span style="background:{TG};-webkit-background-clip:text;color:transparent">{t}</span>'
VIDRO = 'background:rgba(255,255,255,.08);backdrop-filter:blur(18px);-webkit-backdrop-filter:blur(18px);border:1px solid rgba(255,255,255,.16)'
selo = lambda t: f'<span style="display:inline-block;{VIDRO};border-radius:40px;padding:14px 28px;font:400 24px Inter;color:{BRANCO};margin:0 10px 12px 0">{t}</span>'
MARCA = f'<div style="display:flex;align-items:center;gap:14px">{g.sim_bm(64)}<span style="font:500 24px Inter;color:{BRANCO};letter-spacing:-.01em">WF Celulares</span></div>'
ZAP = f'<div style="font:300 24px Inter;color:{PRATA};letter-spacing:.02em">WhatsApp (98) 98827-1882</div>'
ILU = lambda pos='right:30px;top:28px': f'<div style="position:absolute;{pos};font:300 14px Inter;color:#6e6e73">Imagem ilustrativa · Apple Newsroom</div>'
def preco(v, t=120, al='left'):
    r, c = v.split(',')
    return (f'<div style="text-align:{al};font:200 {t}px/1 Inter;letter-spacing:-.04em;color:{BRANCO}"><span style="font-size:{t*.28}px;font-weight:300;vertical-align:top;margin-right:10px;color:{PRATA}">R$</span>'
            f'{r}<span style="font-size:{t*.34}px">,{c}</span></div>')
def chao(img, x, y, w, h, pos='50% 50%'):
    """produto + reflexo no vidro preto (copia o piso espelhado das keynotes)."""
    return (f'<img src="img/{img}" style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;object-fit:cover;object-position:{pos}">'
            f'<img src="img/{img}" style="position:absolute;left:{x}px;top:{y+h}px;width:{w}px;height:{h}px;object-fit:cover;object-position:{pos};transform:scaleY(-1);opacity:.22;'
            f'-webkit-mask-image:linear-gradient(to top,#000,transparent 35%)">')
P = []
def sec(id, tom, corpo):
    P.append(f'<section class="f" id="{id}" style="width:1080px;height:1350px;background:#000"><div style="position:absolute;inset:0;background:{F[tom]}"></div>{corpo}</section>')

# 01 · 30 dias de Black (keynote: número gigante fino + produto atrás) · preto
sec('01-black-30-dias', 'preto', f'''
<div style="position:absolute;left:0;right:0;top:200px;text-align:center;font:300 600px/.8 Inter;letter-spacing:-.06em;opacity:.9">{GRAD("30")}</div>
<img src="img/16-hero.jpg" style="position:absolute;left:240px;top:330px;width:600px;height:740px;object-fit:cover;object-position:50% 50%">
<div style="position:absolute;left:0;right:0;top:70px;display:flex;justify-content:center">{MARCA}</div>
<div style="position:absolute;left:0;right:0;top:1130px;text-align:center;font:200 84px/1 Inter;letter-spacing:-.04em;color:{BRANCO}">dias de Black.</div>
<div style="position:absolute;left:0;right:0;top:1235px;text-align:center;font:300 26px Inter;color:{PRATA}">iPhone lacrado e seminovo com preço de Black Friday, todo dia.</div>{ILU()}''')

# 02 · iPhone 12 Pro Max R$ 2.299 (B&O: produto sangrando à direita, texto em coluna) · azul profundo
sec('02-oferta-12-pro-max', 'azul', f'''
<img src="img/12-announce.jpg" style="position:absolute;left:300px;top:330px;width:1000px;height:760px;object-fit:cover;object-position:30% 50%;mix-blend-mode:lighten">
<div style="position:absolute;left:70px;top:80px">{MARCA}</div>
<div style="position:absolute;left:70px;top:220px;font:300 28px Inter;color:{PRATA}">Seminovo · garantia e procedência WF</div>
<div style="position:absolute;left:70px;top:270px;font:200 112px/1 Inter;letter-spacing:-.05em;color:{BRANCO}">iPhone 12<br>{GRAD("Pro Max")}</div>
<div style="position:absolute;left:70px;top:1030px">{preco("2.299,00")}</div>
<div style="position:absolute;left:70px;bottom:70px;display:flex;gap:0">{selo("128 GB")}{selo("Pix ou cartão")}</div>
<div style="position:absolute;right:70px;bottom:84px">{ZAP}</div>{ILU()}''')

# 03 · Assistência (Newsroom: close sangrado da câmera + título fino) · titânio
sec('03-assistencia', 'titanio', f'''
<img src="img/16-camsys.jpg" style="position:absolute;left:-60px;top:380px;width:1200px;height:900px;object-fit:cover;object-position:45% 50%">
<div style="position:absolute;inset:0;background:linear-gradient(180deg,#14120f 0%,rgba(20,18,15,.6) 32%,transparent 50%,transparent 70%,#000 100%)"></div>
<div style="position:absolute;left:70px;top:90px"><div style="font:300 28px Inter;color:{PRATA};margin-bottom:20px">Assistência técnica iPhone</div>
<div style="font:200 104px/1.02 Inter;letter-spacing:-.05em;color:{BRANCO}">Quebrou?<br>{GRAD("A gente resolve.")}</div></div>
<div style="position:absolute;left:70px;right:70px;bottom:80px;display:flex;justify-content:space-between;align-items:flex-end">
<div>{selo("Tela")}{selo("Bateria")}{selo("Câmera")}{selo("Placa")}<div style="font:300 28px Inter;color:{BRANCO};margin-top:10px">Orçamento antes de mexer.</div></div>{g.sim_bm(100)}</div>{ILU()}''')

# 04 · iPhone 17 Pro Max Silver R$ 6.499 (apple.com Pro: lineup central com reflexo) · preto
sec('04-oferta-17-pro-max-silver', 'preto', f'''
<div style="position:absolute;left:0;right:0;top:90px;text-align:center"><div style="font:300 28px Inter;color:{PRATA};margin-bottom:16px">Black Friday WF · seminovo · garantia Apple</div>
<div style="font:200 104px/1 Inter;letter-spacing:-.05em;color:{BRANCO}">iPhone 17 Pro Max</div><div style="font:200 56px Inter;letter-spacing:-.03em;margin-top:10px">{GRAD("Silver · 256 GB")}</div></div>
{chao("17-lineup.jpg", 140, 420, 800, 520, "50% 50%")}
<div style="position:absolute;left:0;right:0;top:1060px;display:flex;justify-content:center">{preco("6.499,00", 120, "center")}</div>
<div style="position:absolute;left:0;right:0;bottom:60px;display:flex;justify-content:center">{ZAP}</div>{ILU()}''')

# 05 · Laudo WF (Nothing: ficha numerada + aparelho de perfil) · azul profundo
it = lambda n, t, s: (f'<div style="display:flex;gap:28px;padding:24px 0;border-top:1px solid rgba(255,255,255,.14)"><span style="font:300 24px Inter;color:{TITA};width:44px">{n}</span>'
    f'<div><div style="font:300 40px Inter;color:{BRANCO};letter-spacing:-.02em">{t}</div><div style="font:300 22px Inter;color:#8e8e93;margin-top:4px">{s}</div></div></div>')
sec('05-laudo-wf', 'azul', f'''
<img src="img/12-blue.jpg" style="position:absolute;left:-200px;top:300px;width:1480px;height:420px;object-fit:cover;object-position:50% 50%;mix-blend-mode:lighten">
<div style="position:absolute;left:70px;top:90px;font:300 28px Inter;color:{PRATA}">Procedência WF</div>
<div style="position:absolute;left:70px;top:140px;font:200 100px/1 Inter;letter-spacing:-.05em;color:{BRANCO}">Todo iPhone sai {GRAD("com laudo.")}</div>
<div style="position:absolute;left:70px;right:70px;top:740px">{it("01","Testado","tela, câmera, Face ID, som e sinal")}{it("02","Bateria medida","a saúde da bateria vai escrita")}{it("03","Com garantia","por escrito")}{it("04","Nota fiscal","para comprar sem medo")}</div>
<div style="position:absolute;left:70px;bottom:60px">{MARCA}</div>{ILU()}''')

# 06 · iPhone 11 R$ 1.399 (Samsung Unpacked: lineup de cores em leque com reflexo) · titânio
sec('06-oferta-iphone-11', 'titanio', f'''
<div style="position:absolute;left:70px;top:90px;font:300 28px Inter;color:{PRATA}">O queridinho chegou</div>
<div style="position:absolute;left:70px;top:140px;font:200 140px/1 Inter;letter-spacing:-.06em;color:{BRANCO}">iPhone {GRAD("11")}</div>
{chao("11-lineup.png", 120, 380, 840, 560, "50% 50%").replace("object-fit:cover", "object-fit:contain")}
<div style="position:absolute;left:70px;top:1010px;width:520px">{selo("128 GB")}{selo("Bateria 100%")}{selo("Garantia da loja")}</div>
<div style="position:absolute;right:70px;top:1010px">{preco("1.399,00", 110, "right")}<div style="text-align:right;font:300 22px Inter;color:{PRATA};margin-top:8px">no Pix · ou 12x no cartão</div></div>
<div style="position:absolute;left:70px;right:70px;bottom:60px;display:flex;justify-content:space-between;align-items:center">{MARCA}{ZAP}</div>{ILU()}''')

# 07 · prova social (tela de bloqueio + notificações de vidro) · preto
nt = lambda y, t, r: (f'<div style="position:absolute;left:150px;right:150px;top:{y}px;transform:rotate({r}deg);{VIDRO};background:rgba(40,40,44,.6);border-radius:34px;padding:28px 34px">'
    f'<div style="display:flex;justify-content:space-between;font:400 20px Inter;color:#a1a1a6"><span>WhatsApp · Cliente WF</span><span>agora</span></div>'
    f'<div style="font:300 30px/1.35 Inter;color:{BRANCO};margin-top:10px">{t}</div></div>')
sec('07-prova-social', 'preto', f'''
<img src="img/17-lock.jpg" style="position:absolute;left:290px;top:300px;width:500px;height:1000px;object-fit:cover;object-position:50% 40%;opacity:.85">
<div style="position:absolute;left:0;right:0;top:90px;text-align:center;font:200 104px/1 Inter;letter-spacing:-.05em;color:{BRANCO}">Quem compra, {GRAD("volta.")}</div>
{nt(560, '"Chegou certinho, bateria em 100% como falaram. Obrigado, WF!"', -2)}{nt(800, '"Troquei a tela no mesmo dia e me mostraram o teste antes de entregar."', 1.5)}
<div style="position:absolute;left:0;right:0;bottom:60px;text-align:center"><span style="{VIDRO};border-radius:30px;padding:12px 22px;font:300 20px Inter;color:{PRATA}">Exemplo ilustrativo · trocar por print real autorizado</span></div>{ILU()}''')

# 08 · iPhone 17 Pro Max 256 GB R$ 6.950 (apple.com Pro: produto central frente e verso, preço embaixo) · titânio
sec('08-oferta-17-pro-max-256', 'titanio', f'''
<div style="position:absolute;left:0;right:0;top:80px;text-align:center"><div style="font:300 28px Inter;color:{PRATA};margin-bottom:16px">Disponível na loja</div>
<div style="font:200 104px/1 Inter;letter-spacing:-.05em;color:{BRANCO}">iPhone 17 Pro Max</div><div style="font:300 30px Inter;color:{PRATA};margin-top:14px">256 GB · garantia Apple até 08/27</div></div>
{chao("17-orange.jpg", 190, 360, 700, 600, "50% 50%")}
<div style="position:absolute;left:0;right:0;top:1040px;display:flex;justify-content:center">{preco("6.950,00", 116, "center")}</div>
<div style="position:absolute;left:0;right:0;top:1190px;display:flex;justify-content:center">{selo("Brindes inclusos")}{selo("Entrega grátis em São Luís")}{selo("Até 18x")}</div>
<div style="position:absolute;left:0;right:0;bottom:30px;display:flex;justify-content:center">{ZAP}</div>{ILU()}''')

# 09 · pagamento e entrega (close de câmera à direita + lista em vidro) · azul profundo
ic = lambda d, t, s: (f'<div style="display:flex;align-items:center;gap:26px;{VIDRO};border-radius:28px;padding:24px 28px;margin-bottom:18px">'
    f'<svg viewBox="0 0 100 100" width="60" height="60" fill="none" stroke="url(#ti)" stroke-width="4" stroke-linecap="round" stroke-linejoin="round">{g.DEFS}{d}</svg>'
    f'<div><div style="font:300 34px Inter;color:{BRANCO}">{t}</div><div style="font:300 22px Inter;color:#8e8e93">{s}</div></div></div>')
sec('09-pagamento-entrega', 'azul', f'''
<img src="img/17-camera.jpg" style="position:absolute;left:560px;top:0;width:700px;height:1350px;object-fit:cover;object-position:30% 50%;-webkit-mask-image:linear-gradient(90deg,transparent,#000 35%)">
<div style="position:absolute;left:70px;top:90px;font:200 96px/1.02 Inter;letter-spacing:-.05em;color:{BRANCO}">Do seu<br>{GRAD("jeito.")}</div>
<div style="position:absolute;left:70px;top:420px;width:600px">
{ic('<path d="M50 12 L88 50 L50 88 L12 50 Z"/><path d="M36 50 L50 36 L64 50 L50 64 Z"/>', 'Pix com desconto', 'pagou, separou')}
{ic('<rect x="10" y="24" width="80" height="54" rx="8"/><path d="M10 40 H90 M24 62 H44"/>', 'Até 12x ou 18x', 'no cartão')}
{ic('<path d="M8 30 H58 V68 H8 Z M58 44 H76 L90 56 V68 H58"/><circle cx="24" cy="72" r="7"/><circle cx="74" cy="72" r="7"/>', 'Entrega em São Luís', 'consulte o seu bairro')}
{ic('<path d="M50 88 C 32 64 24 50 24 38 a26 26 0 0 1 52 0 c0 12 -8 26 -26 50 z"/><circle cx="50" cy="38" r="9"/>', 'Retire na loja', 'São Cristóvão · Renascença')}</div>
<div style="position:absolute;left:70px;bottom:70px">{MARCA}<div style="margin-top:14px">{ZAP}</div></div>{ILU()}''')

html = ('<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;600&display=swap" rel="stylesheet">'
        '<style>body{margin:0;background:#333}section.f{position:relative;overflow:hidden;margin:0 0 40px}img{display:block;mix-blend-mode:lighten}</style></head><body>' + ''.join(P) + '</body></html>')
open(os.path.join(D, 'pecas.html'), 'w').write(html); print(len(P), 'artes')
