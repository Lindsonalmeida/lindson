# Rebranding WF Celulares · v1 (Designer gráfico · conta Leandro · 10/11/2026)
# Pedido do Lindson (10/11): "faça uma engenharia reversa e faça o rebranding dessa marca".
# Conceito: PROCEDÊNCIA. Todo aparelho que sai da WF tem laudo: testado, com garantia, com nota.
# Composição copiada de (ver ../TEMPLATE.md):
#   1. iFixit (EUA): fundo escuro + mão real no conserto + manchete curta e firme (post Assistência, destaques).
#   2. Back Market (França): bloco de cor chapada gritante + produto grande sangrando (post Produto, fachada).
#   3. Nothing (Reino Unido): tipografia de matriz de pontos (Doto) como rótulo técnico, ficha/laudo (etiquetas, cartão).
# Herança mantida do logo antigo: o azul e o círculo (no caminho B). Removido: maçã da Apple, efeito 3D, couro.
# Gera pecas.html -> node render.js -> pecas/*.jpg -> python3 prancha.py
import os
D = os.path.dirname(os.path.abspath(__file__))
CARVAO, GRAFITE, AZUL, SINAL, PRATA, BRANCO = '#0A0C10', '#171B23', '#2F6BFF', '#C8FF2E', '#D5DAE2', '#F5F7FA'
B = 'banco/'
F_PROD, F_REPARO, F_PROVA, F_TELA = B+'1592750475338-74b7b21085ab.jpg', B+'r-1563770660941-20978e870e26.jpg', B+'1605236453806-6ff36851218e.jpg', B+'r-1585060544812-6b45742d762f.jpg'

# ------------------------------------------------ marca
def mono(t, cor=BRANCO, caixa=AZUL, fundo=True, sw=11):
    """Caminho A · 'WF ligado': a última perna do W é a haste do F, dentro da silhueta de um celular."""
    r = f'<rect x="4" y="2" width="92" height="96" rx="20" fill="{caixa}"/>' if fundo else f'<rect x="6" y="4" width="88" height="92" rx="19" fill="none" stroke="{caixa}" stroke-width="6"/>'
    return (f'<svg viewBox="0 0 100 100" width="{t}" height="{t}" style="display:block">{r}'
            f'<path d="M16 28 L28 74 L40 44 L52 74 L52 28 L82 28 M52 51 L76 51" fill="none" stroke="{cor}" stroke-width="{sw}" stroke-linecap="square" stroke-linejoin="miter"/>'
            f'<circle cx="80" cy="74" r="6" fill="{SINAL}"/></svg>')

def assinatura(t, cor=BRANCO, sub=True, caixa=AZUL):
    s = f'<div style="display:flex;align-items:center;gap:{t*.32}px">{mono(t*1.25, caixa=caixa)}<div>'
    s += f'<div style="font:700 {t}px/.86 \'Space Grotesk\';letter-spacing:-.04em;color:{cor};white-space:nowrap">WF Celulares</div>'
    if sub: s += f'<div style="font:600 {t*.24}px/1 \'Doto\';letter-spacing:.14em;color:{cor};opacity:.8;margin-top:{t*.22}px;white-space:nowrap">LACRADOS · SEMINOVOS · ASSISTÊNCIA</div>'
    return s + '</div></div>'

def selo(t):
    """Caminho B · selo de procedência: mantém o círculo azul do logo antigo, sem maçã e sem 3D."""
    return (f'<svg viewBox="0 0 200 200" width="{t}" height="{t}" style="display:block"><defs><path id="aro" d="M100 100 m-74 0 a74 74 0 1 1 148 0 a74 74 0 1 1 -148 0"/></defs>'
            f'<circle cx="100" cy="100" r="98" fill="{AZUL}"/><circle cx="100" cy="100" r="62" fill="{CARVAO}"/>'
            f'<text font-family="Space Grotesk" font-weight="700" font-size="15" letter-spacing="3.2" fill="{BRANCO}"><textPath href="#aro">CELULARES · ASSISTÊNCIA · SÃO LUÍS · MA · </textPath></text>'
            f'<text x="100" y="118" text-anchor="middle" font-family="Space Grotesk" font-weight="700" font-size="54" letter-spacing="-3" fill="{BRANCO}">WF</text>'
            f'<circle cx="100" cy="140" r="4" fill="{SINAL}"/></svg>')

def palavra(t, cor=BRANCO):
    """Caminho C · 'wf.' minúsculo, o ponto é a cabeça de um parafuso (o reparo)."""
    return (f'<div style="display:flex;align-items:baseline;font:700 {t}px/1 \'Space Grotesk\';letter-spacing:-.07em;color:{cor}">wf'
            f'<svg viewBox="0 0 40 40" width="{t*.3}" height="{t*.3}" style="margin-left:{t*.04}px"><circle cx="20" cy="20" r="19" fill="{CARVAO}"/>'
            f'<path d="M20 9 V31 M9 20 H31" stroke="{SINAL}" stroke-width="5"/></svg></div>')

def rotulo(txt, cor=SINAL, fundo='transparent', t=26):
    return f'<span style="display:inline-block;font:700 {t}px/1 \'Doto\';letter-spacing:.12em;color:{cor};background:{fundo};padding:{t*.35}px {t*.5}px;border:2px solid {cor}">{txt}</span>'

def laudo(t=1):
    """Grafismo da marca: a etiqueta de laudo (ficha técnica com picote e código)."""
    return (f'<div style="background:{SINAL};color:{CARVAO};padding:{22*t}px {26*t}px;font:700 {22*t}px/1.25 \'Doto\';letter-spacing:.06em;'
            f'clip-path:polygon(0 0,100% 0,100% 100%,{14*t}px 100%,0 calc(100% - {14*t}px));box-shadow:0 0 0 0">'
            f'<div style="font:700 {13*t}px/1 \'Inter\';letter-spacing:.2em;margin-bottom:{10*t}px">LAUDO WF</div>'
            f'✓ TESTADO<br>✓ BATERIA MEDIDA<br>✓ COM GARANTIA<br>✓ NOTA FISCAL</div>')

GRAO = "background-image:url(\"data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='200' height='200'><filter id='n'><feTurbulence baseFrequency='.9' numOctaves='2'/></filter><rect width='200' height='200' filter='url(%23n)' opacity='.09'/></svg>\")"
GRADE = f"background-image:linear-gradient({GRAFITE} 1px,transparent 1px),linear-gradient(90deg,{GRAFITE} 1px,transparent 1px);background-size:54px 54px"

def sec(id, w, h, corpo, fundo=CARVAO):
    return f'<section class="f" id="{id}" style="width:{w}px;height:{h}px;background:{fundo}">{corpo}<div class="g" style="{GRAO}"></div></section>\n'

P = []
# ---------- 01 · caminhos de logo (prancha de apresentação, composição Nothing: 3 colunas, rótulo de matriz)
col = lambda n, nome, obj, txt, fundo: (f'<div style="flex:1;background:{fundo};padding:56px;display:flex;flex-direction:column;justify-content:space-between;position:relative">'
    f'<div style="display:flex;justify-content:space-between">{rotulo(n, SINAL if fundo!=SINAL else CARVAO)}<span style="font:600 20px Inter;color:{BRANCO if fundo!=SINAL else CARVAO};opacity:.7">{nome}</span></div>'
    f'<div style="display:flex;justify-content:center;align-items:center;flex:1">{obj}</div>'
    f'<div style="font:500 22px/1.4 Inter;color:{BRANCO if fundo!=SINAL else CARVAO}">{txt}</div></div>')
P.append(sec('01-caminhos', 1920, 1080, '<div style="display:flex;height:100%;gap:6px;background:#000">' +
    col('A · RECOMENDADO', 'WF ligado', f'<div>{mono(300)}<div style="margin-top:40px">{assinatura(64, sub=False)}</div></div>', 'A última perna do W vira a haste do F, dentro do contorno de um celular. O ponto verde é o "aparelho aprovado". Lê bem a 24 px.', CARVAO) +
    col('B', 'Selo de procedência', selo(420), 'Mantém o círculo e o azul que o cliente já reconhece, sem a maçã. Funciona como carimbo na caixa e no laudo.', GRAFITE) +
    col('C', 'wf. parafuso', palavra(260, CARVAO), 'Minúsculo e direto. O ponto final é a cabeça do parafuso: a assistência dentro do nome.', SINAL) + '</div>'))

# ---------- 02 · sistema (paleta com proporção + letras + grafismo)
cores = [(CARVAO, 'Carvão', '60%', BRANCO), (AZUL, 'Azul WF', '20%', BRANCO), (PRATA, 'Prata', '10%', CARVAO), (SINAL, 'Sinal', '10%', CARVAO)]
barra = ''.join(f'<div style="flex:{p[:-1]};background:{c};padding:28px;display:flex;flex-direction:column;justify-content:flex-end;color:{tc}"><b style="font:700 34px \'Space Grotesk\'">{n}</b><span style="font:600 20px Doto;letter-spacing:.1em">{c} · {p}</span></div>' for c, n, p, tc in cores)
P.append(sec('02-sistema', 1920, 1080, f'''<div style="position:absolute;inset:0;{GRADE};opacity:.9"></div>
<div style="position:absolute;left:80px;top:70px">{rotulo('02 · SISTEMA')}</div>
<div style="position:absolute;left:80px;top:150px;font:700 150px/.86 'Space Grotesk';letter-spacing:-.05em;color:{BRANCO}">Aa<span style="color:{AZUL}">Gg</span></div>
<div style="position:absolute;left:80px;top:300px;font:500 26px/1.5 Inter;color:{PRATA};width:640px"><b style="color:{BRANCO}">Space Grotesk</b> 700 · títulos<br><b style="color:{BRANCO}">Inter</b> 400–600 · textos, preços, legendas<br><b style="color:{SINAL};font-family:Doto">DOTO</b> · só rótulos técnicos (laudo, código, selo)</div>
<div style="position:absolute;right:80px;top:120px;width:300px;transform:rotate(4deg)">{laudo(1.4)}</div>
<div style="position:absolute;right:460px;top:150px">{mono(220)}</div>
<div style="position:absolute;left:0;right:0;bottom:0;height:430px;display:flex">{barra}</div>'''))

# ---------- 03 · avatar 1080 (conferido em 110 px)
P.append(sec('03-avatar', 1080, 1080, f'<div style="position:absolute;inset:0;background:radial-gradient(circle at 50% 40%,#3d78ff,{AZUL} 55%,#1d4fd6)"></div><div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center">{mono(700, caixa="transparent", sw=12)}</div>', AZUL))

# ---------- 04-09 · capas de destaque (ícone em traço, grade, cor alternada)
ICS = {
 'Lacrados': '<rect x="22" y="30" width="56" height="44" rx="4"/><path d="M22 44 H78 M50 30 V74"/><path d="M40 30 C 40 18, 50 16, 50 30 C 50 16, 60 18, 60 30"/>',
 'Seminovos': '<rect x="32" y="12" width="36" height="76" rx="8"/><path d="M40 52 L48 60 L62 44"/><path d="M44 80 H56"/>',
 'Assistência': '<path d="M62 14 a16 16 0 0 0 -18 22 L16 64 a8 8 0 0 0 12 12 L56 48 a16 16 0 0 0 22 -18 l-10 10 -10 -2 -2 -10 z"/>',
 'Avaliações': '<path d="M50 14 L60 38 L86 40 L66 56 L72 82 L50 68 L28 82 L34 56 L14 40 L40 38 Z"/>',
 'Entrega': '<path d="M10 30 H60 V68 H10 Z M60 44 H78 L90 56 V68 H60"/><circle cx="26" cy="72" r="7"/><circle cx="76" cy="72" r="7"/>',
 'Localização': '<path d="M50 90 C 30 64 22 50 22 38 a28 28 0 0 1 56 0 c0 12 -8 26 -28 52 z"/><circle cx="50" cy="38" r="10"/>',
}
for i, (n, d) in enumerate(ICS.items()):
    fundo, tr, tx = [(CARVAO, SINAL, BRANCO), (AZUL, BRANCO, BRANCO)][i % 2]
    P.append(sec(f'{4+i:02d}-destaque-{n.lower().replace("ê","e").replace("ç","c").replace("ã","a").replace("õ","o")}', 1080, 1080,
        f'<div style="position:absolute;inset:0;{GRADE};opacity:{.6 if fundo==CARVAO else .25}"></div>'
        f'<div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:40px">'
        f'<svg viewBox="0 0 100 100" width="440" height="440" fill="none" stroke="{tr}" stroke-width="6" stroke-linejoin="round" stroke-linecap="round">{d}</svg>'
        f'<div style="font:700 60px Doto;letter-spacing:.12em;color:{tx}">{n.upper()}</div></div>', fundo))

# ---------- 10 · post PRODUTO (Back Market: bloco chapado gritante + produto grande sangrando)
P.append(sec('10-post-produto', 1080, 1350, f'''
<div style="position:absolute;inset:0;background:{SINAL}"></div>
<div style="position:absolute;left:-40px;top:40px;font:700 330px/.8 'Space Grotesk';letter-spacing:-.07em;color:{CARVAO}">SEMI<br>NOVO</div>
<img src="{F_PROD}" style="position:absolute;right:-40px;bottom:150px;width:700px;height:700px;object-fit:cover;object-position:52% 50%;clip-path:polygon(18% 0,100% 0,100% 100%,0 100%);filter:contrast(1.1)">
<div style="position:absolute;left:60px;top:720px;width:380px">{laudo(1.25)}</div>
<div style="position:absolute;left:0;right:0;bottom:0;height:150px;background:{CARVAO};display:flex;align-items:center;justify-content:space-between;padding:0 60px">
 <div style="font:600 34px/1.15 Inter;color:{BRANCO}">Com cara de novo.<br><span style="color:{SINAL}">Com laudo de verdade.</span></div>{mono(96)}</div>
<div style="position:absolute;right:20px;bottom:160px;font:500 14px Inter;color:{BRANCO};opacity:.8">Foto ilustrativa · Unsplash</div>'''))

# ---------- 11 · post ASSISTÊNCIA (iFixit: escuro, mão real no conserto, manchete firme, texto fora da mão)
P.append(sec('11-post-assistencia', 1080, 1350, f'''
<img src="{F_REPARO}" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:60% 50%;filter:saturate(1.15) contrast(1.1)">
<div style="position:absolute;inset:0;background:linear-gradient(180deg,{CARVAO} 0%,rgba(10,12,16,.75) 34%,rgba(10,12,16,0) 58%,rgba(10,12,16,.2) 80%,{CARVAO} 100%)"></div>
<div style="position:absolute;left:60px;top:60px">{rotulo('ASSISTÊNCIA TÉCNICA')}</div>
<div style="position:absolute;left:60px;top:140px;font:700 120px/1.08 'Space Grotesk';letter-spacing:-.05em;color:{BRANCO}">Quebrou?<br><span style="background:{AZUL};padding:0 18px">A gente abre.</span></div>
<div style="position:absolute;left:60px;right:60px;bottom:60px;display:flex;justify-content:space-between;align-items:flex-end">
 <div style="font:500 30px/1.35 Inter;color:{BRANCO}">Tela, bateria, conector e placa.<br><b style="color:{SINAL}">Orçamento antes de mexer.</b></div>{mono(110)}</div>
<div style="position:absolute;right:24px;top:24px;font:500 14px Inter;color:{BRANCO};opacity:.7">Foto ilustrativa · Unsplash</div>'''))

# ---------- 12 · post PROVA SOCIAL (Nothing: matriz de pontos + aparelho como tela de depoimento)
P.append(sec('12-post-prova', 1080, 1350, f'''
<div style="position:absolute;inset:0;background:{AZUL}"></div>
<div style="position:absolute;inset:0;background-image:radial-gradient(rgba(255,255,255,.18) 2px,transparent 2.5px);background-size:26px 26px"></div>

<div style="position:absolute;left:60px;top:230px;font:700 96px/.9 'Space Grotesk';letter-spacing:-.05em;color:{BRANCO};width:600px">Quem compra,<br><span style="color:{SINAL}">volta.</span></div>
<div style="position:absolute;right:-70px;top:150px;width:560px;height:1060px;border-radius:70px;background:{CARVAO};border:14px solid #1b2030;box-shadow:40px 40px 0 rgba(0,0,0,.35);padding:110px 50px 50px;transform:rotate(-6deg)">
 <div style="font:700 22px Doto;color:{SINAL};letter-spacing:.12em">AVALIAÇÃO · GOOGLE</div>
 <div style="font:600 46px Inter;color:{SINAL};margin:18px 0">★★★★★</div>
 <div style="font:500 34px/1.35 Inter;color:{BRANCO}">"Troquei a tela no mesmo dia e me mostraram o teste antes de entregar."</div>
 <div style="margin-top:40px;font:600 24px Inter;color:{PRATA}">Cliente WF · São Luís</div>
 <div style="margin-top:60px">{rotulo('EXEMPLO ILUSTRATIVO', PRATA, t=18)}</div></div>
<div style="position:absolute;left:60px;bottom:70px;font:500 28px/1.4 Inter;color:{BRANCO};width:470px">Print real de cliente entra aqui, com autorização.</div>
<div style="position:absolute;left:60px;bottom:200px">{mono(100, caixa=CARVAO)}</div>'''))

# ---------- 13 · fachada (mockup em CSS, Back Market: faixa chapada + nome grande)
P.append(sec('13-fachada', 1920, 1080, f'''
<div style="position:absolute;inset:0;background:linear-gradient(#1a2233,#0b0e14)"></div>
<div style="position:absolute;left:0;right:0;bottom:0;height:120px;background:#2a2d33"></div>
<div style="position:absolute;left:160px;right:160px;top:120px;height:230px;background:{CARVAO};display:flex;align-items:center;padding:0 70px;gap:50px;box-shadow:0 30px 60px rgba(0,0,0,.6)">
 {mono(160)}<div style="font:700 150px/.9 'Space Grotesk';letter-spacing:-.05em;color:{BRANCO}">WF Celulares</div></div>
<div style="position:absolute;left:160px;right:160px;top:350px;height:56px;background:{SINAL};display:flex;align-items:center;justify-content:space-around;font:700 26px Doto;letter-spacing:.14em;color:{CARVAO}"><span>LACRADOS</span><span>SEMINOVOS</span><span>ASSISTÊNCIA</span><span>ACESSÓRIOS</span></div>
<div style="position:absolute;left:160px;right:160px;top:406px;bottom:120px;background:linear-gradient(120deg,#1d2a44,#0e1320 60%,#25365a);border-left:24px solid {GRAFITE};border-right:24px solid {GRAFITE};display:flex">
 <div style="flex:1;border-right:16px solid {GRAFITE};display:flex;align-items:center;justify-content:center"><div style="width:360px;height:360px;opacity:.95">{selo(360)}</div></div>
 <div style="flex:1;border-right:16px solid {GRAFITE};background:linear-gradient(90deg,rgba(255,255,255,.08),transparent)"></div>
 <div style="flex:1;display:flex;align-items:center;justify-content:center"><div style="width:300px;transform:rotate(-3deg)">{laudo(1.3)}</div></div></div>
<div style="position:absolute;right:40px;bottom:30px;font:500 16px Inter;color:{PRATA};opacity:.7">Mockup ilustrativo da fachada</div>'''))

# ---------- 14 · cartão + etiqueta de laudo
cart = lambda lado: f'<div style="width:700px;height:400px;border-radius:22px;box-shadow:0 40px 80px rgba(0,0,0,.55);position:relative;overflow:hidden;{lado}">'
P.append(sec('14-cartao-etiqueta', 1920, 1080, f'''
<div style="position:absolute;inset:0;{GRADE}"></div>
<div style="position:absolute;left:120px;top:140px;transform:rotate(-5deg)">{cart(f"background:{AZUL}")}<div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center">{mono(240, caixa=CARVAO)}</div></div></div>
<div style="position:absolute;left:300px;top:520px;transform:rotate(3deg)">{cart(f"background:{BRANCO}")}
 <div style="position:absolute;left:50px;top:50px">{assinatura(44, cor=CARVAO, sub=False)}</div>
 <div style="position:absolute;left:50px;bottom:50px;font:500 24px/1.5 Inter;color:{CARVAO}">WhatsApp (98) 98827-1882<br>São Cristóvão · Renascença · São Luís</div>
 <div style="position:absolute;right:0;top:0;bottom:0;width:26px;background:{SINAL}"></div></div></div>
<div style="position:absolute;right:160px;top:170px;width:420px;transform:rotate(6deg)">{laudo(1.8)}<div style="background:{BRANCO};padding:20px 36px;font:700 22px Doto;letter-spacing:.1em;color:{CARVAO}">Nº WF-0000 · IMEI ____</div></div>
<div style="position:absolute;right:120px;bottom:80px">{rotulo('ETIQUETA DE LAUDO · VAI NA CAIXA')}</div>'''))

html = ('<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;700&family=Inter:wght@400;500;600;700&family=Doto:wght@600;700&display=swap" rel="stylesheet">'
        '<style>body{margin:0;background:#333}section.f{position:relative;overflow:hidden;margin:0 0 40px}.g{position:absolute;inset:0;pointer-events:none;mix-blend-mode:overlay}img{display:block}</style></head><body>' + ''.join(P) + '</body></html>')
open(os.path.join(D, 'pecas.html'), 'w').write(html)
print(len(P), 'peças')
