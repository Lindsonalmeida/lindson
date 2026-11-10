# WF Celulares · 9 artes para o feed (Designer gráfico · conta Leandro · 10/11/2026) · identidade final caminho B
# Preços e ofertas = os que o próprio cliente publicou (prints em ../referencias-cliente/posts-10-11/). Sem "iPhone 18".
# Fotos: Unsplash (licença livre), todas marcadas "Foto ilustrativa"; créditos no README. Trocar pela foto real quando chegar.
# Composição copiada de (ver ../TEMPLATE.md, seção artes-01):
#   vitrine de produto (fundo preto, produto central, título fino 2 linhas com gradiente) -> 01, 08
#   Back Market (preço grande em bloco + produto na mão) -> 02, 06
#   iFixit (foto de conserto sangrada, escura) -> 03
#   Nothing (ficha técnica / laudo em lista) -> 05, 09
#   notificação de vidro fosco (apple-like UI) -> 07 ; banner editorial de titânio -> 04
import os, sys
D = os.path.dirname(os.path.abspath(__file__)); I = os.path.join(D, '..', 'identidade'); sys.path.insert(0, I)
import gerar3 as g
PRETO, GRAF, TITA, PRATA, BRANCO, TG = g.PRETO, g.GRAF, g.TITA, g.PRATA, g.BRANCO, g.TIT_GRAD
B = '../identidade/banco/'
LOGO = lambda w=150, *a: f'<div style="width:{w}px">{g.logo_svg(*a)}</div>'
MARCA = lambda c=BRANCO: f'<div style="display:flex;align-items:center;gap:14px">{g.sim_bm(64)}<span style="font:600 26px Inter;color:{c};letter-spacing:-.02em">WF Celulares</span></div>'
ILU = lambda c=TITA, pos='right:30px;top:28px': f'<div style="position:absolute;{pos};font:400 15px Inter;color:{c}">Foto ilustrativa</div>'
ZAP = lambda c=BRANCO: f'<div style="font:500 24px Inter;color:{c}">WhatsApp (98) 98827-1882</div>'
GRAD = lambda t: f'<span style="background:{TG};-webkit-background-clip:text;color:transparent">{t}</span>'
P = []
sec = lambda id, corpo, f=PRETO: P.append(f'<section class="f" id="{id}" style="width:1080px;height:1350px;background:{f}">{corpo}</section>')
def preco(v, cor=BRANCO, t=150):
    r, c = v.split(',')
    return f'<div style="font:600 {t}px/1 Inter;letter-spacing:-.05em;color:{cor}"><span style="font-size:{t*.3}px;vertical-align:top;margin-right:8px">R$</span>{r}<span style="font-size:{t*.35}px">,{c}</span></div>'

# 01 · abertura Black Friday "30 dias" (número gigante + produto)
sec('01-black-30-dias', f'''
<div style="position:absolute;inset:0;background:radial-gradient(circle at 50% 62%,#2a2a2e,#000 62%)"></div>
<div style="position:absolute;left:0;right:0;top:70px;display:flex;justify-content:center">{LOGO(140)}</div>
<div style="position:absolute;left:0;right:0;top:300px;text-align:center;font:700 560px/.8 Inter;letter-spacing:-.07em">{GRAD("30")}</div>
<img src="{B}n-1695048133142-1a20484d2569.jpg" style="position:absolute;left:90px;top:560px;width:900px;height:520px;object-fit:cover;-webkit-mask-image:radial-gradient(ellipse 60% 60% at 50% 50%,#000 45%,transparent 75%)">
<div style="position:absolute;left:0;right:0;top:1090px;text-align:center;font:600 76px/1 Inter;letter-spacing:-.04em;color:{BRANCO}">dias de Black.</div>
<div style="position:absolute;left:0;right:0;top:1190px;text-align:center;font:400 28px Inter;color:{PRATA}">iPhone lacrado e seminovo com preço de Black Friday, todo dia.</div>
{ILU()}''')

# 02 · oferta iPhone 12 Pro Max (claro, produto na mão + preço em bloco)
sec('02-oferta-12-pro-max', f'''
<img src="{B}n-1632661674596-df8be070a5c5.jpg" style="position:absolute;right:0;top:0;width:620px;height:1350px;object-fit:cover;object-position:40% 50%">
<div style="position:absolute;left:70px;top:80px">{MARCA(GRAF)}</div>
<div style="position:absolute;left:70px;top:240px;width:380px;font:500 28px/1.3 Inter;color:{TITA}">Seminovo · garantia e procedência WF</div>
<div style="position:absolute;left:70px;top:320px;font:600 96px/1 Inter;letter-spacing:-.045em;color:{GRAF}">iPhone 12<br>Pro Max</div>
<div style="position:absolute;left:70px;top:560px;font:500 30px Inter;color:{GRAF}">128 GB</div>
<div style="position:absolute;left:40px;top:760px;background:{GRAF};padding:40px 44px;border-radius:28px;box-shadow:0 30px 60px rgba(0,0,0,.25)"><div style="font:500 24px Inter;color:{PRATA};margin-bottom:10px">por apenas</div>{preco("2.299,00", BRANCO, 120)}</div>
<div style="position:absolute;left:70px;bottom:90px">{ZAP(GRAF)}<div style="font:400 22px Inter;color:{TITA};margin-top:8px">Pix ou cartão</div></div>
{ILU(BRANCO)}''', BRANCO)

# 03 · assistência técnica (foto sangrada escura)
sec('03-assistencia', f'''
<img src="{B}r-1563770660941-20978e870e26.jpg" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:62% 50%;filter:grayscale(.3) contrast(1.1)">
<div style="position:absolute;inset:0;background:linear-gradient(180deg,#000 0%,rgba(0,0,0,.8) 30%,rgba(0,0,0,0) 55%,rgba(0,0,0,.9) 100%)"></div>
<div style="position:absolute;left:70px;top:90px"><div style="font:500 28px Inter;color:{TITA};margin-bottom:22px">Assistência técnica iPhone</div>
<div style="font:600 100px/1.02 Inter;letter-spacing:-.045em;color:{BRANCO}">Quebrou?<br>{GRAD("A gente resolve.")}</div></div>
<div style="position:absolute;left:70px;right:70px;bottom:80px;display:flex;justify-content:space-between;align-items:flex-end">
<div style="font:400 30px/1.5 Inter;color:{BRANCO}">Tela · Bateria · Conector · Placa<br><span style="color:{PRATA}">Orçamento antes de mexer.</span></div>{g.sim_bm(110)}</div>{ILU(PRATA)}''')

# 04 · oferta iPhone 17 Pro Max Silver (banner de titânio)
sec('04-oferta-17-pro-max-silver', f'''
<div style="position:absolute;inset:0;background:{TG}"></div>
<img src="{B}n-1727093493864-0bcbd16c7e6d.jpg" style="position:absolute;left:-40px;top:430px;width:600px;height:640px;object-fit:cover;object-position:35% 50%;border-radius:0 40px 40px 0;box-shadow:30px 30px 80px rgba(0,0,0,.35)">
<div style="position:absolute;left:70px;top:80px;font:500 28px Inter;color:#1d1d1f">Black Friday WF</div>
<div style="position:absolute;left:70px;top:130px;font:600 110px/1 Inter;letter-spacing:-.05em;color:#111">iPhone 17<br>Pro Max Silver</div>
<div style="position:absolute;right:60px;top:520px;width:300px;font:500 26px/1.5 Inter;color:#111;text-align:right">256 GB<br>Seminovo<br><b>Garantia Apple</b></div>
<div style="position:absolute;right:60px;bottom:200px;text-align:right">{preco("6.499,00", "#111", 110)}</div>
<div style="position:absolute;right:60px;bottom:90px">{ZAP("#111")}</div>{ILU("#111")}''', '#bbb')

# 05 · Laudo WF / procedência (claro, ficha técnica)
item = lambda n, t, s: f'<div style="display:flex;gap:26px;padding:26px 0;border-top:1px solid #d5d5da"><span style="font:600 26px Inter;color:{TITA};width:50px">{n}</span><div><div style="font:600 38px Inter;color:{GRAF};letter-spacing:-.02em">{t}</div><div style="font:400 24px Inter;color:#6e6e73;margin-top:4px">{s}</div></div></div>'
sec('05-laudo-wf', f'''
<img src="{B}n-1603891128711-11b4b03bb138.jpg" style="position:absolute;right:-80px;top:120px;width:470px;height:640px;object-fit:cover;border-radius:40px;transform:rotate(8deg);box-shadow:0 40px 80px rgba(0,0,0,.25)">
<div style="position:absolute;left:70px;top:90px;font:500 28px Inter;color:{TITA}">Procedência WF</div>
<div style="position:absolute;left:70px;top:140px;font:600 104px/1.02 Inter;letter-spacing:-.05em;color:{GRAF}">Todo iPhone<br>sai com<br><span style="background:linear-gradient(135deg,#6b665f,#b9b4ac,#57534d);-webkit-background-clip:text;color:transparent">laudo.</span></div>
<div style="position:absolute;left:70px;right:70px;top:620px">{item("01","Testado","tela, câmera, Face ID, som e sinal")}{item("02","Bateria medida","a saúde da bateria vai escrita")}{item("03","Com garantia","por escrito, com prazo no laudo")}{item("04","Nota fiscal","para comprar sem medo")}</div>
<div style="position:absolute;left:70px;bottom:70px">{MARCA(GRAF)}</div>{ILU(TITA, "right:30px;bottom:30px")}''', BRANCO)

# 06 · oferta iPhone 11 (grafite, aparelho inclinado + chips de ficha)
chip = lambda t: f'<span style="display:inline-block;border:1px solid #48484a;border-radius:40px;padding:12px 24px;font:500 24px Inter;color:{BRANCO};margin:0 10px 12px 0">{t}</span>'
sec('06-oferta-iphone-11', f'''
<img src="{B}n-1591337676887-a217a6970a8a.jpg" style="position:absolute;left:0;top:0;width:1080px;height:700px;object-fit:cover">
<div style="position:absolute;left:0;right:0;top:560px;height:140px;background:linear-gradient(transparent,{GRAF})"></div>
<div style="position:absolute;left:70px;top:740px;font:500 28px Inter;color:{TITA}">O queridinho chegou</div>
<div style="position:absolute;left:70px;top:790px;font:600 110px/1 Inter;letter-spacing:-.05em;color:{BRANCO}">iPhone 11</div>
<div style="position:absolute;left:70px;top:930px;width:560px">{chip("128 GB")}{chip("Bateria 100%")}{chip("Garantia da loja")}{chip("12x no cartão")}</div>
<div style="position:absolute;right:70px;top:930px;text-align:right">{preco("1.399,00", BRANCO, 104)}<div style="font:400 22px Inter;color:{PRATA};margin-top:10px">no Pix</div></div>
<div style="position:absolute;left:70px;right:70px;bottom:70px;display:flex;justify-content:space-between;align-items:center">{MARCA()}{ZAP(PRATA)}</div>{ILU("#111")}''', GRAF)

# 07 · prova social (notificação de vidro fosco, ilustrativo)
card = lambda y, txt, rot: (f'<div style="position:absolute;left:80px;right:80px;top:{y}px;transform:rotate({rot}deg);background:rgba(255,255,255,.75);backdrop-filter:blur(24px);border-radius:36px;padding:34px 40px;box-shadow:0 30px 60px rgba(0,0,0,.18)">'
    f'<div style="display:flex;justify-content:space-between;font:500 22px Inter;color:#6e6e73"><span>WhatsApp · Cliente WF</span><span>agora</span></div>'
    f'<div style="font:400 34px/1.35 Inter;color:{GRAF};margin-top:12px">{txt}</div></div>')
sec('07-prova-social', f'''
<img src="{B}1580910051074-3eb694886505.jpg" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;filter:brightness(1.05)">
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(245,245,247,.97) 0%,rgba(245,245,247,.6) 40%,rgba(245,245,247,.2) 100%)"></div>
<div style="position:absolute;left:70px;top:90px;font:600 104px/1.02 Inter;letter-spacing:-.05em;color:{GRAF}">Quem compra,<br><span style="background:linear-gradient(135deg,#6b665f,#b9b4ac,#57534d);-webkit-background-clip:text;color:transparent">volta.</span></div>
{card(440, '"Chegou certinho, bateria em 100% como falaram. Obrigado, WF!"', -2)}
{card(720, '"Troquei a tela no mesmo dia e me mostraram o teste antes de entregar."', 2)}
<div style="position:absolute;left:70px;bottom:80px;font:500 22px Inter;color:{GRAF};background:rgba(255,255,255,.8);padding:12px 20px;border-radius:30px">EXEMPLO ILUSTRATIVO · trocar por print real autorizado</div>
<div style="position:absolute;right:70px;bottom:70px">{g.sim_bm(90, "#000")}</div>{ILU(TITA)}''', BRANCO)

# 08 · oferta iPhone 17 Pro Max 256 GB com brindes (vitrine preta, produto central)
sec('08-oferta-17-pro-max-256', f'''
<div style="position:absolute;inset:0;background:radial-gradient(circle at 50% 55%,#26262a,#000 60%)"></div>
<div style="position:absolute;left:0;right:0;top:90px;text-align:center"><div style="font:500 28px Inter;color:{TITA};margin-bottom:18px">Disponível na loja</div>
<div style="font:600 100px/1 Inter;letter-spacing:-.05em;color:{BRANCO}">iPhone 17 Pro Max</div><div style="font:400 34px Inter;color:{PRATA};margin-top:16px">256 GB · garantia Apple até 08/27</div></div>
<img src="{B}n-1616348436168-de43ad0db179.jpg" style="position:absolute;left:190px;top:400px;width:700px;height:560px;object-fit:cover;border-radius:36px">
<div style="position:absolute;left:0;right:0;top:1000px;display:flex;justify-content:center">{preco("6.950,00", BRANCO, 120)}</div>
<div style="position:absolute;left:0;right:0;top:1160px;display:flex;justify-content:center;gap:16px;font:500 24px Inter;color:#111">
<span style="background:{TG};padding:12px 26px;border-radius:40px">Brindes inclusos</span><span style="background:{TG};padding:12px 26px;border-radius:40px">Entrega grátis em São Luís</span><span style="background:{TG};padding:12px 26px;border-radius:40px">até 18x</span></div>
<div style="position:absolute;left:0;right:0;bottom:50px;display:flex;justify-content:center">{ZAP(PRATA)}</div>{ILU()}''')

# 09 · pagamento e entrega (titânio, lista de ícones + mão com celular)
ic = lambda d, t, s: (f'<div style="display:flex;align-items:center;gap:28px;padding:24px 0;border-top:1px solid rgba(0,0,0,.18)">'
    f'<svg viewBox="0 0 100 100" width="70" height="70" fill="none" stroke="#111" stroke-width="5" stroke-linecap="round" stroke-linejoin="round">{d}</svg>'
    f'<div><div style="font:600 38px Inter;color:#111;letter-spacing:-.02em">{t}</div><div style="font:400 24px Inter;color:#333">{s}</div></div></div>')
sec('09-pagamento-entrega', f'''
<div style="position:absolute;inset:0;background:{TG}"></div>
<img src="{B}n-1510557880182-3d4d3cba35a5.jpg" style="position:absolute;right:0;top:0;width:430px;height:1350px;object-fit:cover;object-position:38% 50%">
<div style="position:absolute;left:70px;top:90px;font:600 96px/1.02 Inter;letter-spacing:-.05em;color:#111">Do jeito que<br>fica bom<br>pra você.</div>
<div style="position:absolute;left:70px;top:520px;width:540px">
{ic('<path d="M50 12 L88 50 L50 88 L12 50 Z"/><path d="M36 50 L50 36 L64 50 L50 64 Z"/>', 'Pix com desconto', 'pagou, separou')}
{ic('<rect x="10" y="24" width="80" height="54" rx="8"/><path d="M10 40 H90 M24 62 H44"/>', 'Até 12x ou 18x', 'no cartão')}
{ic('<path d="M8 30 H58 V68 H8 Z M58 44 H76 L90 56 V68 H58"/><circle cx="24" cy="72" r="7"/><circle cx="74" cy="72" r="7"/>', 'Entrega em São Luís', 'consulte o seu bairro')}
{ic('<path d="M50 88 C 32 64 24 50 24 38 a26 26 0 0 1 52 0 c0 12 -8 26 -26 50 z"/><circle cx="50" cy="38" r="9"/>', 'Ou retire na loja', 'São Cristóvão · Renascença')}</div>
<div style="position:absolute;left:70px;bottom:70px">{ZAP("#111")}</div>{ILU(BRANCO)}''', '#bbb')

html = ('<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">'
        '<style>body{margin:0;background:#333}section.f{position:relative;overflow:hidden;margin:0 0 40px}img{display:block}</style></head><body>' + ''.join(P) + '</body></html>')
open(os.path.join(D, 'pecas.html'), 'w').write(html); print(len(P), 'artes')
