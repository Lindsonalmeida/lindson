# Rebranding WF Celulares · FINAL caminho B "Assinatura" (aprovado pelo Lindson em 10/11/2026) · base v2 "universo Apple" (Designer gráfico · conta Leandro · 10/11/2026)
# v1 REPROVADA pelo Lindson: "precisa ter a ver com a Apple" (verde-limão/Back Market fugiu do universo do iPhone).
# v2: minimalismo premium no estilo de vitrine de tecnologia (muito respiro, titânio, prata, preto e branco),
# símbolo próprio com linguagem do aparelho (anel magnético, módulo de câmera, curva da borda) + WF.
# Uso da marca Apple: o Lindson informou em 10/11/2026 que o cliente tem permissão (maçã liberada, sem aviso legal).
# Logo = versão moderna do logo atual: maçã prata/titânio + WF + CELULARES, sem 3D cromado, legível em 110 px. Sem fonte San Francisco.
# Composição copiada de: vitrine de produto (fundo preto, produto centralizado, manchete fina em 2 linhas,
# 2ª linha em gradiente de titânio); iFixit (foto real de conserto, escuro); Nothing (rótulo técnico pequeno).
# Gera pecas2.html -> node render.js pecas2 -> pecas-v2/*.jpg -> python3 prancha2.py
import os
D = os.path.dirname(os.path.abspath(__file__))
PRETO, GRAF, TITA, PRATA, BRANCO, AZUL = '#000000', '#1D1D1F', '#8E8A84', '#C7C9CC', '#F5F5F7', '#2F6BFF'
TIT_GRAD = 'linear-gradient(135deg,#f4f2ee 0%,#b9b4ac 28%,#7d7871 52%,#d9d5ce 74%,#8b867f 100%)'
AVISO = 'Não somos revenda autorizada Apple. iPhone é marca da Apple Inc.'
B = 'banco/'
F_PROD, F_REPARO, F_PROVA = B+'1592750475338-74b7b21085ab.jpg', B+'r-1563770660941-20978e870e26.jpg', B+'1580910051074-3eb694886505.jpg'
DEFS = ('<defs><linearGradient id="ti" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#f6f4f0"/><stop offset=".3" stop-color="#bdb8b0"/>'
        '<stop offset=".55" stop-color="#7a756e"/><stop offset=".78" stop-color="#e2ded7"/><stop offset="1" stop-color="#8d887f"/></linearGradient></defs>')

def wf(cor, sw=7, esc=1, dx=0, dy=0):
    # monograma "WF ligado" (herdado da v1): última perna do W = haste do F; traço fino arredondado, geometria limpa
    return (f'<g transform="translate({dx} {dy}) scale({esc})"><path d="M24 36 L33 66 L42 44 L51 66 L51 36 L76 36 M51 51 L71 51" fill="none" '
            f'stroke="{cor}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"/></g>')

MACA = ('<path d="M50 34 C40 28 22 28 14 44 C6 60 12 86 26 102 C34 112 42 112 50 108 C58 112 66 112 74 102 C80 95 84 88 86 82 '
        'C76 77 72 68 72 60 C72 50 78 44 84 40 C78 31 66 28 58 31 C55 32 52 33 50 34 Z"/><path d="M52 26 C52 16 60 8 70 6 C70 16 62 24 52 26 Z"/>')
def maca(t, cor='url(#ti)'):
    return f'<svg viewBox="0 0 100 116" width="{t}" height="{t*1.16}" style="display:block">{DEFS}<g fill="{cor}">{MACA}</g></svg>'

def sim_a(t, fundo=PRETO, traco='url(#ti)'):
    """A · ANEL (recomendado): o círculo do logo atual vira o anel magnético fino; maçã titânio em cima, WF embaixo."""
    return (f'<svg viewBox="0 0 100 100" width="{t}" height="{t}" style="display:block">{DEFS}'
            f'<circle cx="50" cy="50" r="49" fill="{fundo}"/><circle cx="50" cy="50" r="44" fill="none" stroke="{traco}" stroke-width="2.6"/>'
            f'<g transform="translate(37 14) scale(.26)" fill="{traco}">{MACA}</g>{wf(BRANCO, 7, .78, 11, 22)}</svg>')

def sim_b(t, fundo=PRETO):
    """B · ASSINATURA: o logo atual refinado e empilhado: maçã, WF fino, CELULARES espaçado."""
    return (f'<div style="display:flex;flex-direction:column;align-items:center;gap:{t*.05}px">{maca(t*.36)}'
            f'<svg viewBox="20 30 62 42" width="{t*.5}" height="{t*.34}">{DEFS}{wf("url(#ti)", 6)}</svg>'
            f'<div style="font:500 {t*.075}px Inter;letter-spacing:.42em;color:{PRATA};margin-left:.42em">CELULARES</div></div>')

def sim_c(t, cor=BRANCO):
    """C · MÓDULO: quadrado de câmera de cantos contínuos com a maçã e o WF lado a lado (cara de ícone de app)."""
    return (f'<svg viewBox="0 0 100 100" width="{t}" height="{t}" style="display:block">{DEFS}'
            f'<rect x="4" y="4" width="92" height="92" rx="26" fill="#111" stroke="url(#ti)" stroke-width="2.5"/>'
            f'<g transform="translate(14 28) scale(.34)" fill="url(#ti)">{MACA}</g>{wf(cor, 7, .62, 34, 20)}</svg>')

def nome(t, cor=BRANCO, sub=True):
    s = f'<div style="font:600 {t}px/1 Inter;letter-spacing:-.035em;color:{cor};white-space:nowrap">WF Celulares</div>'
    if sub: s += f'<div style="font:500 {t*.26}px/1 Inter;letter-spacing:.02em;color:{TITA};margin-top:{t*.22}px">Especialista em iPhone · São Luís</div>'
    return f'<div>{s}</div>'

def aviso(*a, **k):
    return ''  # aviso retirado: cliente tem permissão (Lindson, 10/11)
    f'<div style="position:absolute;{pos};font:400 {t}px Inter;color:{cor};letter-spacing:.01em">{AVISO}</div>'

titulo = lambda a, b, t=104, cor=BRANCO: (f'<div style="font:600 {t}px/1.02 Inter;letter-spacing:-.045em;color:{cor}">{a}<br>'
    f'<span style="background:{TIT_GRAD};-webkit-background-clip:text;color:transparent">{b}</span></div>')

def sec(id, w, h, corpo, fundo=PRETO):
    return f'<section class="f" id="{id}" style="width:{w}px;height:{h}px;background:{fundo}">{corpo}</section>\n'


def logo_svg(cor_maca='url(#ti)', cor_wf='url(#ti)', cor_txt=PRATA):
    """Logo B vetorial: maçã + WF + CELULARES (viewBox 0 0 200 240)."""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 222">{DEFS}'
            f'<g transform="translate(67 4) scale(.72)" fill="{cor_maca}">{MACA}</g>'
            f'<g transform="translate(-10 18) scale(2.2)">{wf(cor_wf, 6)}</g>'
            f'<text x="104" y="212" text-anchor="middle" font-family="Inter" font-weight="500" font-size="20" letter-spacing="9" fill="{cor_txt}">CELULARES</text></svg>')
def sim_bm(t, fundo='transparent'):
    """Marca reduzida do B (avatar e assinatura de post): maçã + WF, sem a palavra (não lê pequeno)."""
    return (f'<svg viewBox="0 0 100 100" width="{t}" height="{t}" style="display:block;background:{fundo};border-radius:50%">{DEFS}'
            f'<g transform="translate(38 12) scale(.24)" fill="url(#ti)">{MACA}</g>{wf(BRANCO, 7, .82, 9, 16)}</svg>')
P = []
P.append(sec('03-avatar', 1080, 1080, f'<div style="position:absolute;inset:0;background:radial-gradient(circle at 50% 35%,#2a2a2d,#000 70%)"></div>'
    f'<div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center"><div style="width:640px">{logo_svg()}</div></div>'))

IC = {'Lacrados': '<rect x="26" y="22" width="48" height="56" rx="10"/><path d="M26 40 H74"/>',
 'Seminovos': '<rect x="32" y="12" width="36" height="76" rx="10"/><path d="M41 50 L48 57 L60 44"/>',
 'Assistência': '<path d="M62 14 a16 16 0 0 0 -18 22 L16 64 a8 8 0 0 0 12 12 L56 48 a16 16 0 0 0 22 -18 l-10 10 -10 -2 -2 -10 z"/>',
 'Avaliações': '<path d="M50 16 L59 38 L83 40 L65 55 L71 79 L50 66 L29 79 L35 55 L17 40 L41 38 Z"/>',
 'Entrega': '<rect x="18" y="30" width="64" height="48" rx="8"/><path d="M18 46 H82 M40 30 V46 M60 30 V46"/>',
 'Localização': '<path d="M50 88 C 32 64 24 50 24 38 a26 26 0 0 1 52 0 c0 12 -8 26 -26 50 z"/><circle cx="50" cy="38" r="9"/>'}
for i, (n, d) in enumerate(IC.items()):
    slug = n.lower().translate(str.maketrans('êçãõ', 'ecao'))
    P.append(sec(f'{4+i:02d}-destaque-{slug}', 1080, 1080,
        f'<div style="position:absolute;inset:0;background:radial-gradient(circle at 50% 30%,#2b2b2e,#000 72%)"></div>'
        f'<div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center">'
        f'<svg viewBox="0 0 100 100" width="520" height="520" fill="none" stroke="url(#ti)" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">{DEFS}'
        f'<circle cx="50" cy="50" r="47" stroke-width="1.2" opacity=".6"/><g transform="translate(18 14) scale(.64)">{d}</g></svg></div>'
        f'<div style="position:absolute;left:0;right:0;bottom:250px;text-align:center;font:500 46px Inter;letter-spacing:-.01em;color:{BRANCO}">{n}</div>'))

# post PRODUTO: vitrine (preto, manchete fina centralizada, produto grande embaixo)
P.append(sec('10-post-produto', 1080, 1350, f'''
<img src="{F_PROD}" style="position:absolute;left:0;right:0;bottom:0;width:1080px;height:900px;object-fit:cover;object-position:50% 40%">
<div style="position:absolute;inset:0;background:linear-gradient(180deg,#000 36%,rgba(0,0,0,0) 58%,rgba(0,0,0,.5) 92%)"></div>
<div style="position:absolute;top:110px;left:0;right:0;text-align:center"><div style="font:500 30px Inter;color:{TITA};margin-bottom:22px">iPhone seminovo</div>{titulo("Cara de novo.", "Laudo de verdade.", 92)}
<div style="font:400 30px/1.4 Inter;color:{PRATA};margin-top:26px">Testado, bateria medida, garantia e nota fiscal.</div></div>
<div style="position:absolute;left:60px;bottom:70px;display:flex;align-items:center;gap:18px">{sim_bm(78)}<span style="font:600 30px Inter;color:{BRANCO};letter-spacing:-.02em">WF Celulares</span></div>
<div style="position:absolute;right:40px;top:30px;font:400 14px Inter;color:{TITA}">Foto ilustrativa · Unsplash</div>{aviso()}'''))

# post ASSISTÊNCIA: foto real de conserto, escuro, manchete fina à esquerda
P.append(sec('11-post-assistencia', 1080, 1350, f'''
<img src="{F_REPARO}" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:62% 50%;filter:grayscale(.35) contrast(1.08)">
<div style="position:absolute;inset:0;background:linear-gradient(180deg,#000 0%,rgba(0,0,0,.82) 30%,rgba(0,0,0,0) 56%,rgba(0,0,0,.85) 100%)"></div>
<div style="position:absolute;left:70px;top:100px"><div style="font:500 30px Inter;color:{TITA};margin-bottom:22px">Assistência técnica iPhone</div>{titulo("Abre, testa,", "e só depois cobra.", 96)}</div>
<div style="position:absolute;left:70px;right:70px;bottom:80px;display:flex;justify-content:space-between;align-items:flex-end">
<div style="font:400 30px/1.45 Inter;color:{BRANCO}">Tela · Bateria · Conector · Placa<br><span style="color:{PRATA}">Orçamento antes de mexer.</span></div>{sim_bm(110)}</div>
<div style="position:absolute;right:30px;top:30px;font:400 14px Inter;color:{TITA}">Foto ilustrativa · Unsplash</div>{aviso(PRATA)}'''))

# post PROVA SOCIAL: claro (branco gelo), foto do aparelho + cartão de avaliação flutuante tipo notificação
P.append(sec('12-post-prova', 1080, 1350, f'''
<img src="{F_PROVA}" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:50% 50%">
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(245,245,247,.97) 0%,rgba(245,245,247,.85) 30%,rgba(245,245,247,0) 55%)"></div>
<div style="position:absolute;left:70px;top:100px">{titulo("Quem compra,", "volta.", 110, GRAF)}</div>
<div style="position:absolute;left:90px;right:90px;top:640px;background:rgba(255,255,255,.72);backdrop-filter:blur(24px);border-radius:40px;padding:44px 50px;box-shadow:0 30px 70px rgba(0,0,0,.18)">
<div style="display:flex;align-items:center;gap:20px">{sim_bm(70)}<div><div style="font:600 28px Inter;color:{GRAF}">Avaliação no Google</div><div style="font:500 30px Inter;color:#b8860b">★★★★★</div></div></div>
<div style="font:400 34px/1.4 Inter;color:{GRAF};margin-top:24px">"Troquei a tela no mesmo dia e me mostraram o teste antes de entregar."</div>
<div style="font:500 20px Inter;color:{TITA};margin-top:20px">EXEMPLO ILUSTRATIVO · trocar por print real autorizado</div></div>
<div style="position:absolute;right:30px;top:30px;font:400 14px Inter;color:{TITA}">Foto ilustrativa · Unsplash</div>{aviso(GRAF)}''', BRANCO))


# fachada (mockup): letreiro preto com a assinatura B em titânio, vitrine com produto
P.append(sec('13-fachada', 1920, 1080, f'''
<div style="position:absolute;inset:0;background:linear-gradient(#202024,#0a0a0b)"></div>
<div style="position:absolute;left:0;right:0;bottom:0;height:110px;background:#2a2a2c"></div>
<div style="position:absolute;left:180px;right:180px;top:90px;height:300px;background:#050505;display:flex;align-items:center;justify-content:center;gap:60px;box-shadow:0 30px 70px rgba(0,0,0,.7)">
<div style="width:150px">{logo_svg()}</div><div style="font:500 46px Inter;letter-spacing:.32em;color:{PRATA}">ESPECIALISTA EM IPHONE</div></div>
<div style="position:absolute;left:180px;right:180px;top:390px;bottom:110px;background:linear-gradient(120deg,#1b1b1e,#0c0c0d 55%,#2a2a2e);border:22px solid #141416;display:flex">
<div style="flex:1;border-right:14px solid #141416;position:relative;overflow:hidden"><img src="{F_PROD}" style="width:100%;height:100%;object-fit:cover;opacity:.85"></div>
<div style="flex:1;background:linear-gradient(90deg,rgba(255,255,255,.07),transparent)"></div>
<div style="flex:1;border-left:14px solid #141416;display:flex;align-items:center;justify-content:center;font:300 40px/1.4 Inter;color:{BRANCO};text-align:center">Lacrados<br>Seminovos<br>Assistência</div></div>
<div style="position:absolute;right:30px;bottom:24px;font:400 16px Inter;color:{TITA}">Mockup ilustrativo da fachada · foto Unsplash</div>'''))
# cartão + etiqueta de laudo
cart = lambda c: f'<div style="width:700px;height:400px;border-radius:24px;background:{c};box-shadow:0 40px 90px rgba(0,0,0,.6);position:relative;overflow:hidden">'
P.append(sec('14-cartao-etiqueta', 1920, 1080, f'''
<div style="position:absolute;inset:0;background:radial-gradient(circle at 40% 30%,#2a2a2e,#000 75%)"></div>
<div style="position:absolute;left:130px;top:120px;transform:rotate(-5deg)">{cart('#0b0b0c')}<div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center"><div style="width:200px">{logo_svg()}</div></div></div></div>
<div style="position:absolute;left:330px;top:520px;transform:rotate(3deg)">{cart(BRANCO)}
<div style="position:absolute;left:50px;top:46px;width:90px">{logo_svg('#1D1D1F','#1D1D1F','#1D1D1F')}</div>
<div style="position:absolute;left:50px;bottom:50px;font:400 24px/1.5 Inter;color:{GRAF}"><b style="font-weight:600">Especialista em iPhone</b><br>WhatsApp (98) 98827-1882<br>São Cristóvão · Renascença · São Luís</div>
<div style="position:absolute;right:0;top:0;bottom:0;width:22px;background:{TIT_GRAD}"></div></div></div>
<div style="position:absolute;right:170px;top:170px;width:440px;transform:rotate(6deg);background:{TIT_GRAD};border-radius:22px;padding:40px;color:#111;box-shadow:0 30px 70px rgba(0,0,0,.6)">
<div style="display:flex;align-items:center;gap:16px"><div style="width:56px">{logo_svg('#111','#111','#111')}</div><b style="font:600 28px Inter">Laudo WF</b></div>
<div style="font:400 28px/1.7 Inter;margin-top:20px">✓ Testado<br>✓ Bateria medida<br>✓ Com garantia<br>✓ Nota fiscal</div>
<div style="font:500 20px Inter;margin-top:16px;opacity:.7">Nº ____ · IMEI ______________</div></div>
<div style="position:absolute;right:150px;bottom:90px;font:500 20px Inter;color:{TITA};letter-spacing:.2em">ETIQUETA DE LAUDO · VAI NA CAIXA</div>'''))

html = ('<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">'
        '<style>body{margin:0;background:#333}section.f{position:relative;overflow:hidden;margin:0 0 40px}img{display:block}</style></head><body>' + ''.join(P) + '</body></html>')
open(os.path.join(D, 'pecas3.html'), 'w').write(html); print(len(P), 'peças')

# arquivos do logo B: SVG (cor, branca, preta)
os.makedirs(os.path.join(D,'logo-b'),exist_ok=True)
for n,a in {'cor':('url(#ti)','url(#ti)',PRATA),'branca':('#FFFFFF',)*3,'preta':('#000000',)*3}.items():
    open(os.path.join(D,'logo-b',f'wf-logo-b-{n}.svg'),'w').write(logo_svg(*a))
