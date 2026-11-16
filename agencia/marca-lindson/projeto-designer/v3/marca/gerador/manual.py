# Barzakh · um estúdio Al Kántara · branding book + manual de marca (conta Leandro, 16/11/2026)
# Modelo copiado: agencia/marca-holding/gerador/gerar.py (mesma família, HTML -> PDF 16:9 por Playwright).
# Referências aplicadas (ver ../TEMPLATE.md, seção "Referências do Lindson"):
#   capas/aberturas = Dahr 01 + Haykalh 03 (luz rasante, feixe azul) + Eclipse serif 12 (disco com halo)
#   símbolo monolito = Studio Arch 02 + Arch Stone Houses 17 · editorial = Oskaya 11
#   mockups = Renovo 20 (hot stamping), Clio 19 (veludo), Arch Studio 06 (ecobag com sombra de janela)
#   grafismo do horizonte = Portal editorial 13 + Lundgren+Lindqvist 08 · foto = MGA 26 + Arcavea 15
# Uso: python3 manual.py    (precisa de ../logos/svg, gerado por logos.py; fotos em ./fotos, Wikimedia Commons)
import os, json, glob, zipfile, shutil, base64
from PIL import Image, ImageEnhance, ImageOps, ImageFilter
import numpy as np
from playwright.sync_api import sync_playwright

B = '/home/user/lindson/agencia/marca-lindson/projeto-designer/v3/marca'
G = B + '/gerador'; S = B + '/logos/svg'; OUT = B + '/entregas'; F = G + '/fotos'; T = G + '/trat'
os.makedirs(OUT, exist_ok=True); os.makedirs(T, exist_ok=True)
OB, MA, GR, PE, BR, LA = '#0A0C10', '#EEEAE2', '#22262E', '#8A8F98', '#B4935A', '#2B3A8F'

# ------------------------------------------------------------ fotos: tratamento único (escura, granulada, fria)
def tratar(nome, modo='noite', crop=None):
    out = f'{T}/{nome}-{modo}.jpg'
    if os.path.exists(out): return out
    im = Image.open(f'{F}/{nome}.jpg').convert('RGB')
    if crop: w, h = im.size; im = im.crop((int(crop[0]*w), int(crop[1]*h), int(crop[2]*w), int(crop[3]*h)))
    if modo in ('noite', 'pedra'):
        g = ImageOps.grayscale(im)
        g = ImageEnhance.Contrast(g).enhance(1.35)
        a = np.asarray(g).astype(np.float32) / 255
        a = a ** (1.55 if modo == 'noite' else 1.2)
        sh = np.array([10, 12, 18], np.float32); hi = np.array([238, 230, 214], np.float32)
        rgb = sh + (hi - sh) * a[..., None]
    else:  # 'cor': mantém a hora azul, escurece
        a = np.asarray(ImageEnhance.Color(im).enhance(.75)).astype(np.float32) / 255
        rgb = (a ** 1.45) * 255
    rng = np.random.default_rng(7); rgb += rng.normal(0, 9, rgb.shape[:2])[..., None]
    Image.fromarray(np.clip(rgb, 0, 255).astype(np.uint8)).save(out, quality=88)
    return out

FT = {k: tratar(*v) for k, v in {
    'aqueduto': ('aqueduto2', 'noite'), 'aquedutoN': ('aqueduto', 'noite'), 'colunata': ('colunata', 'noite'),
    'sombra': ('sombra', 'noite'), 'espiral': ('espiral', 'pedra'), 'mar': ('mar', 'noite'),
    'langen': ('langen', 'cor'), 'slz': ('slz', 'cor'), 'concreto': ('ando', 'pedra', (0, .3, .3, 1)),
    'aqueduto_cor': ('aqueduto2', 'cor')}.items()}
def U(k): return 'file://' + FT[k]

# ------------------------------------------------------------ logos
KV2 = open('/home/user/lindson/agencia/marca-holding/v2/logos/svg/alkantara-simbolo-mono-branco.svg').read()
def kv2(px, cor='currentColor'):  # o K (pedra-chave) da Al Kántara v2, ao lado do endosso
    return KV2.replace('#FFFFFF', cor).replace('<svg ', f'<svg style="width:{px}px;height:{px}px;display:inline-block;vertical-align:-.12em;margin-right:.6em" ', 1)
def svgtxt(n): return open(f'{S}/barzakh-{n}.svg').read()
def L(n, st=''): return svgtxt(n).replace('<svg ', f'<svg style="width:100%;height:100%;display:block;{st}" ', 1)

def monolito(cor, luz, mar, reflexo, bg=None, R=92, cx=120, base=120):
    """Variação monolito: régua dos Dois mares com o mundo de cima em arco CHEIO; reflexo segue em linha."""
    w = R * .13; g = w * .55; rk = R * .32; o = []
    ri = R * .66; h = w * .16; rh = rk + w * .45
    # arco cheio (o portal): domo sólido, com a fenda do anel interno (0,66R) e o vão do disco recortados (evenodd)
    o.append(f'<path fill="{cor}" fill-rule="evenodd" d="M{cx-R},{base-g} A{R},{R} 0 0 1 {cx+R},{base-g} Z '
             f'M{cx-ri-h},{base-g} A{ri+h},{ri+h} 0 0 1 {cx+ri+h},{base-g} L{cx+ri-h},{base-g} A{ri-h},{ri-h} 0 0 0 {cx-ri+h},{base-g} Z '
             f'M{cx-rh},{base-g} A{rh},{rh} 0 0 1 {cx+rh},{base-g} Z"/>')
    o.append(f'<path fill="{luz}" d="M{cx-rk},{base-g} A{rk},{rk} 0 0 1 {cx+rk},{base-g} Z"/>')
    for r in (R, R * .66):
        rm = r - w / 2
        o.append(f'<path fill="none" stroke="{reflexo}" stroke-width="{w*.35}" d="M{cx-rm},{base+g} A{rm},{rm} 0 0 0 {cx+rm},{base+g}"/>')
    o.append(f'<path fill="{mar}" d="M{cx-rk},{base+g} A{rk},{rk} 0 0 0 {cx+rk},{base+g} Z"/>')
    o.append(f'<rect fill="{cor}" x="{cx-R*1.18}" y="{base-g*.42}" width="{R*2.36}" height="{g*.84}"/>')
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 240" width="240" height="240">{"".join(o)}</svg>'

MONO = {'monolito-negativo': (MA, BR, LA, MA, OB), 'monolito-positivo': (OB, BR, LA, OB, MA),
        'monolito-lapis': (MA, BR, OB, MA, LA), 'monolito-bronze': (BR, BR, BR, BR, None),
        'monolito-mono-preto': (OB, OB, OB, OB, None), 'monolito-mono-branco': (MA, MA, MA, MA, None)}
for n, (c, l, m, r, bg) in MONO.items():
    open(f'{S}/barzakh-{n}.svg', 'w').write(monolito(c, l, m, r, bg))
def M_(n, st=''): return L(n, st)

def mask(n):  # SVG -> data URI para máscara (hot stamping, gravação)
    return "url('data:image/svg+xml;base64," + base64.b64encode(svgtxt(n).encode()).decode() + "')"

# ------------------------------------------------------------ CSS
NOISE = "url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='220' height='220'%3E%3Cfilter id='n'%3E%3CfeTurbulence baseFrequency='.85' numOctaves='3'/%3E%3C/filter%3E%3Crect width='220' height='220' filter='url(%23n)' opacity='.6'/%3E%3C/svg%3E\")"
PAPER = "url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='300'%3E%3Cfilter id='p'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.55' numOctaves='4'/%3E%3CfeColorMatrix values='0 0 0 0 .5 0 0 0 0 .45 0 0 0 0 .4 0 0 0 .55 0'/%3E%3C/filter%3E%3Crect width='300' height='300' filter='url(%23p)'/%3E%3C/svg%3E\")"
CSS = f"""
@import url('https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300..600;1,9..144,300..600&family=Inter+Tight:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&display=swap');
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:{OB}}}
.pg{{width:1920px;height:1080px;position:relative;overflow:hidden;page-break-after:always;font-family:'Inter Tight';color:{MA};background:{OB}}}
.lt{{background:{MA};color:{OB}}}
.mono{{font-family:'JetBrains Mono';font-size:15px;letter-spacing:.14em;text-transform:uppercase}}
.ser{{font-family:'Fraunces';font-weight:400;font-variation-settings:'opsz' 144;letter-spacing:-.01em}}
.cap{{font-family:'Fraunces';text-transform:uppercase;letter-spacing:.32em}}
.hd{{position:absolute;left:96px;right:96px;top:56px;display:flex;justify-content:space-between;opacity:.6;z-index:5}}
.ft{{position:absolute;left:96px;right:96px;bottom:48px;display:flex;justify-content:space-between;opacity:.55;z-index:5}}
.t1{{font-family:'Fraunces';font-weight:400;font-variation-settings:'opsz' 144;font-size:104px;line-height:1;letter-spacing:-.01em}}
.t2{{font-family:'Fraunces';font-weight:400;font-variation-settings:'opsz' 144;font-size:64px;line-height:1.06;letter-spacing:-.005em}}
.p{{font-size:24px;line-height:1.5;font-weight:400;opacity:.9}}
.br{{color:{BR}}} .la{{color:#8E9BEA}}
.card{{border:1px solid rgba(238,234,226,.14);border-radius:3px}}
.lt .card{{border-color:rgba(10,12,16,.14)}}
.ph{{background-size:cover;background-position:center}}
.grain:after,.pg:after{{content:'';position:absolute;inset:0;background-image:{NOISE};opacity:.08;mix-blend-mode:overlay;pointer-events:none;z-index:6}}
.paper{{background-image:{PAPER}}}
.win{{position:absolute;inset:-20%;background:repeating-linear-gradient(100deg,transparent 0 130px,rgba(0,0,0,.55) 130px 170px,transparent 170px 300px);filter:blur(10px);transform:skewY(-8deg);mix-blend-mode:multiply;pointer-events:none}}
.beam{{position:absolute;background:radial-gradient(ellipse at center,rgba(70,96,230,.55),rgba(43,58,143,.22) 40%,transparent 70%);filter:blur(30px);pointer-events:none}}
.foil{{background:linear-gradient(115deg,#7a5e2f 0%,#d9bd84 22%,#8c6c38 40%,#e8d3a2 55%,#94733d 72%,#c9a86c 100%);-webkit-mask-size:contain;-webkit-mask-repeat:no-repeat;-webkit-mask-position:center;filter:drop-shadow(0 1px 0 rgba(255,240,200,.35)) drop-shadow(0 -1px 1px rgba(0,0,0,.6))}}
.deb{{-webkit-mask-size:contain;-webkit-mask-repeat:no-repeat;-webkit-mask-position:center}}
.lbl{{position:absolute;font-family:'JetBrains Mono';font-size:14px;letter-spacing:.14em;text-transform:uppercase}}
"""

class Doc:
    def __init__(s, nome): s.nome = nome; s.p = []
    def page(s, body, sec='', lt=False, hf=True):
        n = len(s.p) + 1
        hdr = f'<div class="hd mono"><span>Barzakh · {s.nome}</span><span>{sec}</span></div><div class="ft mono"><span>{kv2(13)}Um estúdio Al Kántara · v1.1 · 2026</span><span>{n:02d}</span></div>' if hf else ''
        s.p.append(f'<section class="pg {"lt" if lt else ""}">{body}{hdr}</section>')
    def divider(s, num, titulo, sub, foto):
        s.page(horizonte(foto, 0, 0, 1920, 1080, linha=.62, veu=.55) +
               f'<div class="beam" style="left:1080px;top:380px;width:900px;height:420px"></div>'
               f'<div style="position:absolute;right:150px;top:470px;width:420px;height:420px;opacity:.95">{M_("monolito-negativo")}</div>'
               f'<div style="position:absolute;left:96px;top:250px"><div class="mono br">Seção {num}</div><div class="ser" style="font-size:250px;line-height:.85;margin-top:20px">{titulo}</div></div>'
               f'<div class="p" style="position:absolute;left:96px;top:740px;max-width:720px">{sub}</div>', titulo)
    def html(s): return f'<html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{"".join(s.p)}</body></html>'

def horizonte(foto, x, y, w, h, linha=.5, veu=.35, disco=False, pos='center'):
    """Grafismo do horizonte: a linha corta a foto; em cima nítido, embaixo desfocado e granulado."""
    yl = int(h * linha)
    d = (f'<div style="position:absolute;left:{w/2-h*.09}px;top:{yl-h*.09}px;width:{h*.18}px;height:{h*.18}px;border-radius:50%;'
         f'background:linear-gradient(180deg,{BR} 50%,{LA} 50%);box-shadow:0 0 {h*.12}px rgba(180,147,90,.35)"></div>') if disco else ''
    return (f'<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;overflow:hidden">'
            f'<div class="ph" style="position:absolute;inset:0;background-image:url({U(foto)});background-position:{pos}"></div>'
            f'<div style="position:absolute;left:0;right:0;top:{yl}px;bottom:0;overflow:hidden"><div class="ph" style="position:absolute;left:-30px;right:-30px;top:{-yl-30}px;height:{h+60}px;background-image:url({U(foto)});background-position:{pos};filter:blur(9px) brightness(.7)"></div>'
            f'<div style="position:absolute;inset:0;background-image:{NOISE};opacity:.35;mix-blend-mode:overlay"></div><div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(43,58,143,.28),rgba(10,12,16,.6))"></div></div>'
            f'<div style="position:absolute;inset:0;background:linear-gradient(90deg,rgba(10,12,16,{veu}),rgba(10,12,16,{veu*.2}))"></div>'
            f'<div style="position:absolute;left:0;right:0;top:{yl}px;height:1px;background:{MA};opacity:.75"></div>{d}</div>')

def two(lbl, titulo, txt, right, wl=560):
    return (f'<div style="position:absolute;left:96px;top:150px;width:{wl}px"><div class="mono br">{lbl}</div><div class="t2" style="margin:24px 0 32px">{titulo}</div><div class="p">{txt}</div></div>'
            f'<div style="position:absolute;left:{96+wl+104}px;right:96px;top:150px;bottom:130px">{right}</div>')

def box(content, bg=OB, pad=60, extra=''):
    pb = pad + 30 if 'padding-bottom' in extra else pad
    return f'<div style="background:{bg};width:100%;height:100%;position:relative"><div style="position:absolute;left:{pad}px;right:{pad}px;top:{pad}px;bottom:{pb}px">{content}</div></div>'

def rgbc(h): h = h.lstrip('#'); return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
def cmyk(h):
    r, g, b = [v / 255 for v in rgbc(h)]; k = 1 - max(r, g, b)
    return tuple(round(v * 100) for v in ((1-r-k)/(1-k), (1-g-k)/(1-k), (1-b-k)/(1-k), k))

# ------------------------------------------------------------ ícones de linha (mesmo traço do reflexo: fino, ponta reta)
IC = {'escuta': '<path d="M8 12h32v20H22l-8 7v-7H8z"/>', 'busca': '<circle cx="21" cy="21" r="11"/><path d="M29 29l11 11"/>',
      'forma': '<path d="M8 38V24a16 16 0 0 1 32 0v14"/><path d="M16 38V24a8 8 0 0 1 16 0v14"/>', 'sistema': '<rect x="8" y="8" width="13" height="13"/><rect x="27" y="8" width="13" height="13"/><rect x="8" y="27" width="13" height="13"/><path d="M27 33h13M33 27v13"/>',
      'luz': '<path d="M4 26h40"/><path d="M15 26a9 9 0 0 1 18 0"/><path d="M15 30a9 9 0 0 0 18 0" stroke-dasharray="2 3"/>', 'entrega': '<path d="M8 16l16-8 16 8v18l-16 8-16-8z"/><path d="M8 16l16 8 16-8M24 24v18"/>',
      'conversa': '<path d="M10 10h28v20H26l-8 8v-8h-8z"/><path d="M17 20h14"/>', 'prazo': '<rect x="8" y="10" width="32" height="30"/><path d="M8 18h32M16 6v8M32 6v8M16 27h6"/>',
      'local': '<path d="M24 42s-13-12-13-22a13 13 0 0 1 26 0c0 10-13 22-13 22z"/><circle cx="24" cy="20" r="4"/>', 'arquivo': '<path d="M12 6h17l9 9v27H12z"/><path d="M29 6v9h9M18 26h14M18 33h10"/>',
      'mockup': '<rect x="14" y="5" width="20" height="38" rx="3"/><path d="M21 37h6"/>', 'pasta': '<path d="M6 14h14l4 4h18v22H6z"/>'}
def icon(k, c=MA, s=64): return f'<svg viewBox="0 0 48 48" width="{s}" height="{s}" fill="none" stroke="{c}" stroke-width="1.6" stroke-linecap="square">{IC[k]}</svg>'

# ------------------------------------------------------------ peças (posts, story, pin, behance)
def post(i):  # 1080x1350 desenhado em 432x540 (escala .4)
    W, H = 432, 540
    if i == 0:
        return (horizonte('colunata', 0, 0, W, H, .58, .25) + f'<div class="beam" style="left:120px;top:250px;width:260px;height:120px"></div>'
                f'<div class="ser" style="position:absolute;left:28px;top:40px;font-size:46px;line-height:1">Sua marca já existe<br><i class="br">no seu atendimento.</i></div>'
                f'<div class="mono" style="position:absolute;left:28px;bottom:26px;font-size:9px">01 · Barzakh</div><div style="position:absolute;right:24px;bottom:18px;width:44px;height:44px">{M_("monolito-negativo")}</div>')
    if i == 1:
        return (f'<div class="paper" style="position:absolute;inset:0;background-color:{MA}"></div><div class="win" style="opacity:.35"></div>'
                f'<div class="mono" style="position:absolute;left:28px;top:30px;font-size:9px;color:{OB}">A escuta · etapa 01</div>'
                f'<div class="ser" style="position:absolute;left:28px;top:110px;right:28px;font-size:52px;line-height:1;color:{OB}">Antes de desenhar, a gente conversa sobre <i style="color:{LA}">quem compra de você.</i></div>'
                f'<div style="position:absolute;left:28px;bottom:30px;width:150px;height:44px">{L("horizontal-positivo")}</div>')
    if i == 2:
        return (f'<div style="position:absolute;inset:0;background:{LA}"></div><div class="beam" style="left:-40px;top:120px;width:520px;height:320px;background:radial-gradient(ellipse,rgba(160,180,255,.55),transparent 65%)"></div>'
                f'<div style="position:absolute;left:96px;top:110px;width:240px;height:240px">{M_("monolito-lapis")}</div>'
                f'<div class="ser" style="position:absolute;left:0;right:0;top:380px;text-align:center;font-size:40px">Barzakh quer dizer<br><i>passagem.</i></div><div class="mono" style="position:absolute;left:0;right:0;bottom:24px;text-align:center;font-size:9px">bar·zak · @barzakhstudio</div>')
    return (f'<div class="ph" style="position:absolute;inset:0;background-image:url({U("espiral")})"></div><div style="position:absolute;inset:0;background:linear-gradient(0deg,{OB} 30%,rgba(10,12,16,.1))"></div>'
            f'<div class="mono br" style="position:absolute;left:28px;top:30px;font-size:9px">Case · antes e depois</div>'
            f'<div style="position:absolute;left:28px;right:28px;bottom:80px;display:grid;grid-template-columns:1fr 1fr;gap:10px">'
            f'<div style="height:110px;background:#ddd;display:grid;place-items:center;color:#c33;font:700 22px Arial">logo antigo</div><div style="height:110px;background:{GR};display:grid;place-items:center" class="ser"><span style="font-size:24px;letter-spacing:.2em">MARCA</span></div></div>'
            f'<div class="mono" style="position:absolute;left:28px;bottom:30px;font-size:9px;opacity:.7">Exemplo ilustrativo</div>')

def story():  # 1080x1920 em 304x540
    W, H = 304, 540
    return (horizonte('aqueduto', 0, 0, W, H, .55, .3, disco=True) +
            f'<div style="position:absolute;left:22px;top:30px;width:120px;height:40px">{L("horizontal-negativo")}</div>'
            f'<div class="ser" style="position:absolute;left:22px;right:22px;top:340px;font-size:34px;line-height:1">Do improviso<br><i class="br">à forma.</i></div>'
            f'<div style="position:absolute;left:22px;right:22px;bottom:30px;border:1px solid rgba(238,234,226,.5);padding:10px;text-align:center" class="mono"><span style="font-size:9px">Me chama no WhatsApp</span></div>')

def pin():  # 1000x1500 em 360x540
    return (f'<div class="ph" style="position:absolute;left:0;top:0;width:360px;height:330px;background-image:url({U("sombra")})"></div>'
            + horizonte('mar', 0, 330, 360, 210, .3, .2) +
            f'<div style="position:absolute;left:0;right:0;top:300px;height:70px;background:linear-gradient(transparent,{OB} 45%,{OB})"></div>'
            f'<div class="ser" style="position:absolute;left:24px;right:24px;top:320px;font-size:30px;line-height:1.02">Identidade visual para clínica: 6 aplicações</div>'
            f'<div class="mono" style="position:absolute;left:24px;bottom:22px;font-size:8px">barzakhstudio · Identidade visual</div>')

def behance():  # 808x632 em 404x316
    return (horizonte('langen', 0, 0, 404, 316, .66, .4) +
            f'<div class="mono br" style="position:absolute;left:22px;top:20px;font-size:8px">Case 001 · Identidade visual</div>'
            f'<div class="ser" style="position:absolute;left:22px;top:120px;font-size:44px;line-height:.95">Nome do<br><i>cliente</i></div>'
            f'<div style="position:absolute;right:20px;bottom:16px;width:96px;height:30px">{L("horizontal-negativo")}</div>')

def frame(inner, w, h, r=0):
    return f'<div class="grain" style="position:relative;width:{w}px;height:{h}px;overflow:hidden;border-radius:{r}px;box-shadow:0 30px 60px rgba(0,0,0,.55);background:{OB}">{inner}</div>'

def phone(inner, w=360, h=740):
    return (f'<div style="width:{w}px;height:{h}px;border-radius:52px;background:#050608;padding:12px;box-shadow:0 0 0 2px #2c3038,0 50px 90px rgba(0,0,0,.7),inset 0 0 0 1px #444">'
            f'<div style="position:relative;width:100%;height:100%;border-radius:42px;overflow:hidden;background:{OB}">{inner}'
            f'<div style="position:absolute;top:10px;left:50%;transform:translateX(-50%);width:96px;height:26px;border-radius:14px;background:#000"></div></div></div>')

def perfil():
    tiles = [('ph', 'colunata'), ('lap', ''), ('ph', 'aqueduto'), ('txt', 'Do improviso à forma.'), ('ph', 'espiral'), ('mono', ''), ('ph', 'mar'), ('lt', 'A escuta'), ('ph', 'langen')]
    def tile(t, v):
        if t == 'ph': return f'<div class="ph" style="background-image:url({U(v)})"></div>'
        if t == 'lap': return f'<div style="background:{LA};padding:16px">{M_("monolito-lapis")}</div>'
        if t == 'mono': return f'<div style="background:{OB};padding:18px">{M_("monolito-negativo")}</div>'
        if t == 'lt': return f'<div class="paper ser" style="background-color:{MA};color:{OB};display:grid;place-items:center;font-size:17px">{v}</div>'
        return f'<div class="ser" style="background:{GR};display:grid;place-items:center;text-align:center;font-size:15px;padding:8px">{v}</div>'
    return (f'<div style="padding:52px 16px 0;font-size:12px">'
            f'<div style="display:flex;justify-content:space-between" class="mono"><span style="font-size:11px">barzakhstudio</span><span style="font-size:11px">···</span></div>'
            f'<div style="display:flex;align-items:center;gap:18px;margin-top:16px"><div style="width:78px;height:78px;border-radius:50%;overflow:hidden;background:{OB};border:1px solid #333;flex:none;padding:10px">{M_("monolito-negativo")}</div>'
            f'<div style="display:flex;gap:16px;text-align:center;font-size:11px"><div><b>Posts</b></div><div><b>Seguidores</b></div><div><b>Seguindo</b></div></div></div>'
            f'<div style="margin-top:12px;font-weight:600">Barzakh · Identidade Visual</div>'
            f'<div style="opacity:.8;line-height:1.4;margin-top:4px">A passagem da sua marca.<br>Identidade visual e branding em São Luís, MA.<br>Direção criativa: Lindson Almeida · um estúdio Al Kántara</div>'
            f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:6px;margin-top:12px"><div style="background:{GR};padding:7px;text-align:center;border-radius:6px">Mensagem</div><div style="background:{BR};color:{OB};padding:7px;text-align:center;border-radius:6px">WhatsApp</div></div>'
            f'<div style="display:flex;gap:14px;margin:14px 0">' + ''.join(f'<div style="text-align:center;font-size:9px"><div style="width:48px;height:48px;border-radius:50%;border:1px solid {BR};display:grid;place-items:center;margin-bottom:4px">{icon(k, MA, 24)}</div>{t}</div>' for k, t in [('escuta', 'Processo'), ('forma', 'Cases'), ('luz', 'Antes/depois'), ('conversa', 'Orçamento')]) +
            f'</div></div><div style="display:grid;grid-template-columns:repeat(3,1fr);grid-auto-rows:112px;gap:2px">' + ''.join(tile(*t) for t in tiles) + '</div>')

def cartao_frente(w=340, h=200):
    return (f'<div class="paper" style="position:relative;width:{w}px;height:{h}px;background-color:#101218;border-radius:3px;overflow:hidden;box-shadow:0 2px 2px rgba(0,0,0,.4),0 26px 40px rgba(0,0,0,.55)">'
            f'<div class="foil" style="position:absolute;left:{w/2-h*.32}px;top:{h*.18}px;width:{h*.64}px;height:{h*.64}px;-webkit-mask-image:{mask("monolito-mono-branco")}"></div></div>')
def cartao_verso(w=340, h=200):
    return (f'<div class="paper" style="position:relative;width:{w}px;height:{h}px;background-color:{MA};color:{OB};border-radius:3px;overflow:hidden;box-shadow:0 2px 2px rgba(0,0,0,.25),0 26px 40px rgba(0,0,0,.45);padding:{h*.12}px">'
            f'<div class="ser" style="font-size:{h*.13}px">Lindson Almeida</div><div class="mono" style="font-size:{h*.042}px;margin-top:4px;color:{BR}">Direção criativa</div>'
            f'<div style="position:absolute;left:{h*.12}px;bottom:{h*.12}px;font-size:{h*.055}px;line-height:1.5">@barzakhstudio<br>São Luís · Maranhão</div>'
            f'<div class="foil" style="position:absolute;right:{h*.12}px;bottom:{h*.1}px;width:{h*.32}px;height:{h*.12}px;-webkit-mask-image:{mask("logotipo-mono-preto")}"></div></div>')

def timbrado(w=300):
    h = w * 1.414
    return (f'<div class="paper" style="position:relative;width:{w}px;height:{h}px;background-color:#F2EFE8;color:{OB};box-shadow:0 30px 50px rgba(0,0,0,.45);padding:{w*.09}px;overflow:hidden">'
            f'<div style="width:{w*.38}px;height:{w*.1}px">{L("horizontal-positivo")}</div>'
            f'<div style="margin-top:{w*.12}px">' + ''.join(f'<div style="height:3px;background:rgba(10,12,16,.12);margin:{w*.03}px 0;width:{v}%"></div>' for v in [92, 88, 95, 70, 90, 85, 60, 93, 80, 50]) + '</div>'
            f'<div style="position:absolute;left:{w*.09}px;right:{w*.09}px;bottom:{w*.06}px;border-top:1px solid {BR};padding-top:6px;display:flex;justify-content:space-between;font-family:JetBrains Mono;font-size:{w*.022}px;letter-spacing:.1em"><span>BARZAKH · UM ESTÚDIO AL KÁNTARA</span><span>@BARZAKHSTUDIO</span></div></div>')

def envelope(w=420):
    h = w * .5
    return (f'<div class="paper" style="position:relative;width:{w}px;height:{h}px;background-color:{LA};box-shadow:0 26px 50px rgba(0,0,0,.5);overflow:hidden">'
            f'<div style="position:absolute;inset:0;background:linear-gradient(160deg,transparent 49.5%,rgba(0,0,0,.25) 50%,transparent 51%),linear-gradient(20deg,transparent 49.5%,rgba(0,0,0,.25) 50%,transparent 51%)"></div>'
            f'<div style="position:absolute;left:{w*.06}px;top:{h*.12}px;width:{w*.28}px;height:{h*.18}px">{L("horizontal-mono-branco")}</div>'
            f'<div class="foil" style="position:absolute;right:{w*.07}px;bottom:{h*.12}px;width:{h*.3}px;height:{h*.3}px;-webkit-mask-image:{mask("monolito-mono-branco")}"></div></div>')

# ======================================================================= BRANDING BOOK
K = Doc('Branding book')
K.page(f'<div class="ph" style="position:absolute;inset:0;background-image:url({U("aquedutoN")})"></div>'
       f'<div style="position:absolute;inset:0;background:linear-gradient(90deg,{OB} 18%,rgba(10,12,16,.35) 70%,rgba(10,12,16,.7))"></div>'
       f'<div class="beam" style="left:1050px;top:250px;width:900px;height:600px"></div>'
       f'<div style="position:absolute;left:1230px;top:260px;width:540px;height:540px">{M_("monolito-negativo")}</div>'
       f'<div style="position:absolute;left:96px;top:80px;width:430px;height:130px">{L("horizontal-negativo")}</div>'
       f'<div style="position:absolute;left:96px;bottom:130px"><div class="mono br">Branding book · v1.0 · 2026</div><div class="ser" style="font-size:170px;line-height:.9;margin-top:24px">A passagem<br><i>da sua marca.</i></div></div>'
       f'<div class="mono" style="position:absolute;right:96px;bottom:60px;opacity:.6">Um estúdio Al Kántara · São Luís, MA</div>', hf=False)
sk = [('01', 'O nome', 'Barzakh, pronúncia, significado'), ('02', 'Por que existimos', 'Propósito, posicionamento, promessa'), ('03', 'Como soamos', 'Manifesto, arquétipo, tom, vocabulário'),
      ('04', 'Para quem', 'Persona e o teste'), ('05', 'Onde estamos', 'Al Kántara Group, endosso, perfis')]
K.page(f'<div class="ph" style="position:absolute;left:0;top:0;width:700px;height:1080px;background-image:url({U("colunata")})"></div><div style="position:absolute;left:0;top:0;width:700px;height:1080px;background:linear-gradient(90deg,rgba(10,12,16,.2),{OB})"></div>'
       '<div style="position:absolute;left:96px;bottom:150px"><div class="mono br">Sumário</div><div class="t1" style="margin-top:24px">Conteúdo</div></div>'
       '<div style="position:absolute;left:860px;right:96px;top:170px">' + ''.join(f'<div style="display:flex;gap:40px;padding:30px 0;border-top:1px solid rgba(238,234,226,.18)"><span class="ser br" style="font-size:60px;width:90px">{a}</span><div><div class="ser" style="font-size:54px">{b}</div><div class="p" style="font-size:20px">{c}</div></div></div>' for a, b, c in sk) + '</div>', 'Sumário')
K.page(f'<div style="position:absolute;inset:0;background:radial-gradient(ellipse at 70% 55%,rgba(43,58,143,.45),transparent 55%)"></div>'
       f'<div style="position:absolute;left:96px;top:150px"><div class="mono br">01 · O nome</div></div>'
       f'<div class="cap" style="position:absolute;left:90px;right:96px;top:250px;font-size:290px;line-height:1;letter-spacing:.12em">Barzakh</div>'
       f'<div style="position:absolute;left:96px;right:96px;top:600px;height:1px;background:{MA};opacity:.5"></div>'
       f'<div style="position:absolute;left:96px;top:640px;display:grid;grid-template-columns:1fr 1fr 1fr;gap:64px;right:96px">'
       f'<div><div class="mono br">Fala-se</div><div class="ser" style="font-size:64px;margin-top:10px">bar·zak</div><div class="p" style="font-size:20px">Força no BAR. Escreve-se sempre Barzakh, com “kh” no fim, sem acento.</div></div>'
       f'<div><div class="mono br">Quer dizer</div><div class="ser" style="font-size:64px;margin-top:10px">passagem</div><div class="p" style="font-size:20px">Palavra árabe antiga: istmo, faixa entre duas coisas, o limiar entre dois lados.</div></div>'
       f'<div><div class="mono br">Em uma frase</div><div class="ser" style="font-size:40px;margin-top:10px;line-height:1.1">“Barzakh quer dizer passagem. A gente faz a passagem da sua marca.”</div></div></div>', '01 · O nome')
K.page(two('01 · A ponte e a passagem', 'A holding é a ponte. O estúdio é a travessia.', '<b>Al Kántara</b> quer dizer “a ponte”: liga as duas margens. <b>Barzakh</b> é o ponto exato da travessia, onde uma coisa deixa de ser o que era e ainda está tomando forma.<br><br>Por isso o símbolo nasce do arco, a forma que segura a pedra-chave do grupo, e ganha o que só ele tem: o reflexo abaixo da linha, os dois mares que se encontram e não se misturam.',
       f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:24px;height:100%"><div style="position:relative">{horizonte("aqueduto_cor", 0, 0, 500, 800, .7, .5)}<div style="position:absolute;left:30px;top:30px;width:300px;height:90px"><img src="file:///home/user/lindson/agencia/marca-holding/v2/logos/svg/alkantara-horizontal-negativo.svg" style="width:100%;height:100%;object-fit:contain;object-position:left"></div><div class="mono" style="position:absolute;left:30px;bottom:30px">A ponte · o grupo</div></div>'
       f'<div style="position:relative;background:{GR}"><div class="beam" style="left:20px;top:250px;width:460px;height:300px"></div><div style="position:absolute;left:60px;right:60px;top:200px;height:380px">{L("simbolo-negativo")}</div><div class="mono br" style="position:absolute;left:30px;bottom:30px">A passagem · o estúdio</div></div></div>'), '01 · O nome')
K.page(f'<div class="ph" style="position:absolute;inset:0;background-image:url({U("sombra")});background-position:center 30%"></div><div style="position:absolute;inset:0;background:linear-gradient(90deg,{OB} 35%,rgba(10,12,16,.25))"></div>'
       f'<div style="position:absolute;left:96px;top:200px;width:1100px"><div class="mono br">02 · Propósito</div><div class="ser" style="font-size:118px;line-height:1;margin-top:30px">Fazer o negócio que já é bom <i class="br">parecer o que ele é.</i></div>'
       f'<div class="p" style="max-width:820px;margin-top:40px">Muito negócio de São Luís atende bem, tem cliente fiel e se apresenta com uma marca feita às pressas. A Barzakh existe para fechar essa distância.</div></div>', '02 · Por que existimos')
pos = [('Para', 'donos de negócio local que já vendem pelo boca a boca e sentem que a marca ficou menor do que o negócio,'), ('a Barzakh é', 'um estúdio de identidade visual e branding'),
       ('que faz a passagem', 'da marca improvisada para a marca que se apresenta: logo, cores, letras, voz e aplicações, com processo claro e o designer no WhatsApp.'),
       ('Diferente de', 'quem entrega “só um logo” ou um arquivo de Canva: a Barzakh entrega um sistema que dá para usar todo dia, mostrado em mockup antes do arquivo final.')]
K.page('<div style="position:absolute;left:96px;top:150px;width:520px"><div class="mono br">02 · Posicionamento</div><div class="t2" style="margin-top:24px">Uma frase para saber onde estamos.</div></div>'
       f'<div style="position:absolute;left:96px;bottom:130px;width:520px;height:380px">{horizonte("espiral", 0, 0, 520, 380, .55, .2)}</div>'
       '<div style="position:absolute;left:720px;right:96px;top:150px">' + ''.join(f'<div style="display:grid;grid-template-columns:300px 1fr;gap:30px;padding:32px 0;border-top:1px solid rgba(238,234,226,.18)"><span class="mono br" style="padding-top:12px">{a}</span><span class="ser" style="font-size:40px;line-height:1.12">{b}</span></div>' for a, b in pos) + '</div>', '02 · Por que existimos')
K.page(two('02 · Promessa', '“Sua marca vai sair pronta para se apresentar.”', 'Prometemos só o que depende de nós. Marca boa ajuda a passar confiança; venda depende de muita coisa que não controlamos, e a gente não finge que controla.',
       f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:24px;height:100%"><div class="card" style="padding:40px;background:{GR}"><div class="mono br">Podemos prometer</div>' + ''.join(f'<div style="display:flex;gap:18px;align-items:center;padding:16px 0;border-bottom:1px solid rgba(238,234,226,.1)">{icon(k, BR, 40)}<span style="font-size:22px">{t}</span></div>' for k, t in [('escuta', 'Processo em etapas'), ('prazo', 'Prazo combinado por escrito'), ('mockup', 'Marca aplicada em mockup'), ('arquivo', 'Arquivos completos e guia'), ('conversa', 'Conversa direta com o designer')]) +
       '</div><div class="card" style="padding:40px"><div class="mono" style="color:#d9776b">Nunca escrevemos</div>' + ''.join(f'<div style="padding:16px 0;border-bottom:1px solid rgba(238,234,226,.1);font-size:22px;text-decoration:line-through;opacity:.6">{t}</div>' for t in ['“Venda mais”', '“Garantido”', '“Resultado em X dias”', '“X% mais clientes”', '“A marca que vai mudar sua vida”']) + '</div></div>'), '02 · Por que existimos')
man = ['Todo negócio bom passa por um limiar.', 'De um lado, a marca feita às pressas: o logo do sobrinho, o post de cada jeito, o perfil que você tem receio de mandar.', 'Do outro, a marca que se apresenta sem pedir desculpa.', 'Entre os dois, existe uma passagem.', 'Nós chamamos essa passagem de Barzakh.',
       'Ali, nada se inventa do nada: a gente escuta quem você é e quem compra de você.', 'Procura no mundo inteiro o que há de melhor, e traz para a sua rua.', 'Dá forma, cor, letra e voz ao que você já é.', 'E só entrega quando a marca está de pé, aplicada, pronta para a luz.']
K.page(horizonte('mar', 0, 0, 1920, 1080, .5, .55) +
       f'<div style="position:absolute;left:96px;top:130px;width:1300px"><div class="mono br">03 · Manifesto</div><div class="ser" style="font-size:38px;line-height:1.28;margin-top:26px">' + '<br>'.join(man[:5]) + '</div></div>'
       f'<div style="position:absolute;left:96px;top:600px;width:1300px" class="ser"><div style="font-size:38px;line-height:1.28;opacity:.8">' + '<br>'.join(man[5:]) + '</div><div style="font-size:52px;margin-top:22px"><i class="br">Não prometemos milagre. Prometemos a travessia bem feita.</i></div></div>', '03 · Como soamos')
K.page(two('03 · Arquétipo', 'O Mago sóbrio, segurado pelo Sábio.', '<b>Mago</b> (principal): o que faz a coisa mudar de estado, do rascunho à forma. Não promete milagre; mostra o antes e o depois.<br><br><b>Sábio</b> (apoio): calma, método, explica com clareza. Cada frase bonita vem com um fato concreto do processo.<br><br>Na prática: fala pouco, mostra muito.',
       f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:24px;height:100%">' + ''.join(f'<div style="position:relative;overflow:hidden"><div class="ph" style="position:absolute;inset:0;background-image:url({U(f)})"></div><div style="position:absolute;inset:0;background:linear-gradient(0deg,{OB} 20%,rgba(10,12,16,.1))"></div><div style="position:absolute;left:36px;right:36px;bottom:40px"><div class="mono br">{a}</div><div class="ser" style="font-size:80px;margin-top:8px">{b}</div><div class="p" style="font-size:20px">{c}</div></div></div>' for f, a, b, c in [('concreto', 'Principal', 'Mago', 'Transforma: do improviso à forma.'), ('colunata', 'Apoio', 'Sábio', 'Explica: método, etapas, prazo.')]) + '</div>'), '03 · Como soamos')
voz = [('Sua marca já existe no seu atendimento. A gente dá forma a ela.', 'Vamos despertar a alma da sua marca.'), ('Em 10 dias úteis você vê o conceito aplicado no cartão, no Instagram e na fachada.', 'Resultados incríveis garantidos em tempo recorde!'),
       ('Antes de desenhar, a gente conversa sobre quem compra de você.', 'Fazemos um mergulho profundo no DNA do seu branding.'), ('Esse é o seu logo hoje. Esse é ele depois da passagem.', 'Transformamos sua marca e suas vendas vão explodir.'), ('Barzakh quer dizer passagem. É isso que a gente faz.', 'Barzakh é um portal energético entre dimensões.')]
K.page('<div style="position:absolute;left:96px;top:150px;width:520px"><div class="mono br">03 · Tom de voz</div><div class="t2" style="margin:24px 0 30px">Calmo, preciso, caloroso.</div><div class="p">Frases curtas. Uma ideia por frase. No máximo uma frase poética por peça; o resto é concreto. “Você” e “a gente”. Sem exclamação em excesso, sem emoji, sem jargão.</div></div>'
       '<div style="position:absolute;left:720px;right:96px;top:150px;bottom:130px;display:grid;grid-template-columns:1fr 1fr;gap:24px">'
       f'<div class="card" style="padding:34px;background:{GR}"><div class="mono br">Falamos assim</div>' + ''.join(f'<div class="ser" style="font-size:27px;line-height:1.2;padding:17px 0;border-bottom:1px solid rgba(238,234,226,.1)">“{a}”</div>' for a, b in voz) + '</div>'
       '<div class="card" style="padding:34px"><div class="mono" style="color:#d9776b">Não falamos assim</div>' + ''.join(f'<div class="ser" style="font-size:27px;line-height:1.2;padding:17px 0;border-bottom:1px solid rgba(238,234,226,.1);opacity:.5;text-decoration:line-through">“{b}”</div>' for a, b in voz) + '</div></div>', '03 · Como soamos')
et = [('escuta', 'Briefing', 'a escuta'), ('busca', 'Persona e pesquisa', 'a busca'), ('forma', 'Conceito', 'a forma'), ('sistema', 'Sistema', 'cores, letras, voz'), ('luz', 'Aplicações', 'a luz'), ('entrega', 'Entrega', 'arquivos e guia')]
K.page('<div style="position:absolute;left:96px;top:150px;width:700px"><div class="mono br">03 · Vocabulário e etapas</div><div class="t2" style="margin-top:24px">Palavras nossas.</div></div>'
       '<div style="position:absolute;left:96px;top:330px;width:740px"><div class="ser" style="font-size:40px;line-height:1.35">limiar · passagem · travessia · forma · luz · margem · ponte · arco · pedra · contorno · assinatura · presença · de pé · pronta</div>'
       '<div class="mono" style="color:#d9776b;margin-top:40px">Proibidas</div><div class="p" style="margin-top:10px;font-size:21px">energia, vibração, alma, sagrado, ritual, despertar, manifestar, garantido, explodir, faturar mais.</div></div>'
       '<div style="position:absolute;left:940px;right:96px;top:150px;bottom:130px;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:repeat(3,1fr);gap:16px">' +
       ''.join(f'<div class="card" style="padding:26px;position:relative;background:{GR if i % 3 == 0 else "transparent"}">{icon(k, BR, 46)}<div class="mono" style="position:absolute;right:24px;top:26px;opacity:.6">0{i+1}</div><div class="ser" style="font-size:38px;margin-top:20px">{a}</div><div class="mono" style="font-size:14px;opacity:.6;margin-top:6px">{b}</div></div>' for i, (k, a, b) in enumerate(et)) + '</div>', '03 · Como soamos')
pers = [('Quem', 'Dono ou dona de negócio local de São Luís e interior (clínica, loja, restaurante, escritório, profissional liberal), de 28 a 50 anos, que vive do boca a boca e já tem Instagram.'),
        ('Rotina', 'Atende o dia inteiro, posta quando sobra tempo, faz arte no Canva ou com alguém da família. Decide pelo celular, à noite, no WhatsApp.'),
        ('Dor', 'A marca parece amadora perto do concorrente; cada post sai de um jeito; tem receio de mandar o perfil para um cliente maior.'),
        ('Valoriza', 'Trabalho real de gente da região, processo claro, prazo cumprido, alguém que entende de negócio.'),
        ('Confia quando', 'Vê o case completo (antes e depois, marca aplicada), fala com o próprio designer e recebe uma proposta organizada.')]
K.page(f'<div class="ph" style="position:absolute;left:0;top:0;width:640px;height:1080px;background-image:url({U("slz")})"></div><div style="position:absolute;left:0;top:0;width:640px;height:1080px;background:linear-gradient(0deg,{OB},rgba(10,12,16,.15) 60%)"></div>'
       '<div style="position:absolute;left:96px;bottom:130px;width:480px"><div class="mono br">04 · Persona</div><div class="t2" style="margin-top:20px">Quem compra da Barzakh.</div></div>'
       '<div style="position:absolute;left:760px;right:96px;top:150px">' + ''.join(f'<div style="display:grid;grid-template-columns:220px 1fr;gap:30px;padding:24px 0;border-top:1px solid rgba(238,234,226,.18)"><span class="mono br" style="padding-top:6px">{a}</span><span style="font-size:25px;line-height:1.45;font-weight:300">{b}</span></div>' for a, b in pers) + '</div>', '04 · Para quem')
K.page(two('04 · O teste', 'Essa pessoa compraria disso?', '<b>Sim,</b> se o místico aparecer como profundidade e cuidado: nome raro, visual sóbrio, frase curta, e logo em seguida o trabalho concreto.<br><br><b>Não,</b> se soar esotérico. Muitos clientes são cristãos praticantes: nada de símbolo religioso, nada que lembre tarô ou guru.<br><br>O místico certo é o da arquitetura e do museu: luz que entra por um arco, pedra, sombra longa, silêncio.',
       f'<div style="display:grid;grid-template-columns:1.3fr 1fr;gap:24px;height:100%"><div style="position:relative">{horizonte("aqueduto", 0, 0, 640, 800, .6, .15)}<div class="mono br" style="position:absolute;left:24px;top:24px">✓ O místico da arquitetura</div></div>'
       f'<div class="card" style="padding:36px"><div class="mono" style="color:#d9776b">✕ Fica de fora</div>' + ''.join(f'<div style="padding:14px 0;border-bottom:1px solid rgba(238,234,226,.1);font-size:21px;opacity:.75">{t}</div>' for t in ['Lua, estrela, constelação', 'Olho, mandala, chakra, cristal', 'Tarô, incenso, fumaça mística', 'Caligrafia árabe, crescente', 'Roxo neon, degradê galáxia', 'Dourado de bijuteria, glitter', 'Deserto, camelo, lanterna oriental']) + '</div></div>'), '04 · Para quem')
K.page('<div style="position:absolute;left:96px;top:150px;width:560px"><div class="mono br">05 · Arquitetura</div><div class="t2" style="margin:24px 0 30px">Marca endossada.</div><div class="p">A Barzakh tem nome e personalidade próprios. O Al Kántara Group aparece como selo de confiança, nunca na frente. É a única divisão sem “Al Kántara” no nome, de propósito: é a que vende direto ao dono de negócio e precisa soar como estúdio.</div></div>'
       '<div style="position:absolute;left:760px;right:96px;top:170px">'
       f'<div style="width:330px;height:90px;margin:0 auto"><img src="file:///home/user/lindson/agencia/marca-holding/v2/logos/svg/alkantara-horizontal-negativo.svg" style="width:100%;height:100%;object-fit:contain"></div>'
       f'<div style="margin:30px 60px 0;height:40px;border:1px solid {BR};border-bottom:none;opacity:.6"></div>'
       '<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:16px">' +
       ''.join(f'<div class="card" style="height:300px;padding:26px;position:relative;{st}"><div class="mono" style="font-size:11px;opacity:.6">{d}</div><div class="ser" style="font-size:{fs}px;margin-top:16px;line-height:1">{n}</div><div class="mono" style="position:absolute;left:26px;bottom:22px;font-size:11px;opacity:.6">{r}</div>{x}</div>'
               for n, d, r, st, fs, x in [('Al Kántara Labs', 'Divisão', 'Tecnologia, apps', 'opacity:.5', 40, ''), ('Barzakh', 'Divisão', 'Design e branding', f'border-color:{BR};background:{LA}', 54, f'<div style="position:absolute;right:20px;top:110px;width:110px;height:110px">{M_("monolito-lapis")}</div>'),
                                         ('Al Kántara Media', 'Divisão', 'Conteúdo e canais', 'opacity:.5', 40, ''), ('Al Kántara Ventures', 'Divisão', 'Negócios próprios', 'opacity:.5', 40, '')]) + '</div></div>', '05 · Onde estamos')
K.page(two('05 · Regras de endosso', '“Barzakh · um estúdio Al Kántara.”', '1. Para o cliente final: “Barzakh” grande, “um estúdio Al Kántara” pequeno, no máximo um terço da altura do nome.<br>2. Dentro da holding: Barzakh na grade das divisões, com o mesmo peso das irmãs.<br>3. Nunca “Al Kántara Barzakh”.<br>4. O Lindson continua o rosto: “direção criativa: Lindson Almeida”.',
       f'<div style="display:grid;grid-template-rows:1.25fr 1fr;gap:24px;height:100%"><div style="position:relative">{horizonte("langen", 0, 0, 960, 440, .62, .45)}<div style="position:absolute;left:50px;top:60px;width:560px;height:250px">{L("vertical-negativo") if False else L("assinatura-negativo")}</div></div>'
       '<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:16px">' + ''.join(f'<div class="card" style="padding:26px"><div class="mono br" style="font-size:14px">{r}</div><div style="font-size:23px;margin-top:14px;font-weight:500">{h}</div><div class="p" style="font-size:16px;margin-top:6px">{n}</div></div>' for r, h, n in [('Instagram', '@barzakhstudio', 'Barzakh · Identidade Visual'), ('Behance', 'barzakhstudio', 'Barzakh Studio'), ('Pinterest', 'barzakhstudio', 'Barzakh | Identidade Visual e Branding')]) + '</div></div>'), '05 · Onde estamos')
K.page(f'<div class="ph" style="position:absolute;inset:0;background-image:url({U("concreto")})"></div><div class="win" style="opacity:.8"></div><div style="position:absolute;inset:0;background:linear-gradient(90deg,{OB} 30%,rgba(10,12,16,.4))"></div>'
       f'<div class="beam" style="left:1100px;top:300px;width:800px;height:500px"></div><div style="position:absolute;left:1250px;top:300px;width:480px;height:480px">{M_("monolito-negativo")}</div>'
       f'<div style="position:absolute;left:96px;top:300px"><div class="mono br">Assinatura</div><div class="ser" style="font-size:160px;line-height:.92;margin-top:24px">A passagem<br><i class="br">da sua marca.</i></div><div class="mono" style="margin-top:40px;opacity:.7">Barzakh · um estúdio Al Kántara · @barzakhstudio</div></div>', 'Assinatura')

# ======================================================================= MANUAL DE MARCA
M = Doc('Manual de marca')
M.page(horizonte('aquedutoN', 0, 0, 1920, 1080, .64, .45) +
       f'<div class="beam" style="left:900px;top:420px;width:1000px;height:520px"></div>'
       f'<div style="position:absolute;left:1220px;top:200px;width:560px;height:560px">{M_("monolito-negativo")}</div>'
       f'<div style="position:absolute;left:96px;top:80px;width:430px;height:130px">{L("horizontal-negativo")}</div>'
       f'<div style="position:absolute;left:96px;top:420px"><div class="mono br">Manual de identidade visual · v1.0 · 2026</div><div class="ser" style="font-size:150px;line-height:.92;margin-top:24px">Onde a marca<br><i>toma forma.</i></div></div>'
       f'<div class="mono" style="position:absolute;right:96px;bottom:60px;text-align:right;opacity:.6">Um estúdio Al Kántara · São Luís, MA</div>', hf=False)
idx = [('01', 'Marca', 'Símbolo, régua, monolito, versões, proteção, usos'), ('02', 'Cor', 'Paleta, códigos, proporção'), ('03', 'Tipografia e grafismo', 'Famílias, hierarquia, horizonte, ícones'),
       ('04', 'Imagem', 'Direção de foto'), ('05', 'Aplicações', 'Instagram, Pinterest, Behance, papelaria, e-mail, mockups')]
M.page(f'<div class="ph" style="position:absolute;right:0;top:0;width:640px;height:1080px;background-image:url({U("sombra")})"></div><div style="position:absolute;right:0;top:0;width:640px;height:1080px;background:linear-gradient(270deg,rgba(10,12,16,.1),{OB})"></div>'
       '<div style="position:absolute;left:96px;top:150px"><div class="mono br">Sumário</div><div class="t1" style="margin-top:24px">Conteúdo</div></div>'
       '<div style="position:absolute;left:96px;width:1060px;top:330px">' + ''.join(f'<div style="display:flex;gap:40px;padding:18px 0;border-top:1px solid rgba(238,234,226,.18)"><span class="ser br" style="font-size:50px;width:80px">{a}</span><div><div class="ser" style="font-size:46px">{b}</div><div class="p" style="font-size:18px">{c}</div></div></div>' for a, b, c in idx) + '</div>', 'Sumário')
M.page(two('Introdução', 'Dois mares que se encontram e não se misturam.', 'Este manual define como a Barzakh aparece no mundo, do avatar à fachada. O símbolo nasce do arco que segura a pedra-chave do Al Kántara Group e ganha o que só ele tem: o reflexo abaixo da linha.<br><br>Em cima, o mundo nítido: a marca pronta. Embaixo, o reflexo: de onde ela veio. No meio, a linha do horizonte, a passagem. Em caso de dúvida, menos é mais, e o símbolo nunca é redesenhado.',
       f'<div style="position:relative;height:100%">{horizonte("mar", 0, 0, 1000, 800, .48, .2, disco=True)}</div>'), 'Introdução')
M.divider('01', 'Marca', 'O arco da ponte, espelhado no rio. A luz partida na linha: Bronze em cima, Lápis embaixo.', 'colunata')
reg = open(f'{S}/barzakh-simbolo-positivo.svg').read().split('>', 1)[1].replace('</svg>', '')
M.page(two('1.1 · Construção', 'A régua dos Dois mares.', 'Só círculos e uma linha. Arco externo de raio <b>R</b>; interno, <b>0,66R</b>; espessura <b>0,13R</b>. Abaixo da linha, o reflexo: os mesmos arcos em contorno de 0,35 da espessura. No centro, o disco de luz de <b>0,32R</b>, partido na linha. A barra do horizonte mede <b>2,36R</b>.<br><br>Desenhado só com geometria: aguenta de 16 px a uma fachada.',
       f'<div class="paper" style="width:100%;height:100%;position:relative;background-color:{MA}">'
       '<svg viewBox="0 0 240 240" style="position:absolute;inset:30px;width:calc(100% - 60px);height:calc(100% - 60px)"><g stroke="#B4935A" stroke-width=".3" fill="none">'
       + ''.join(f'<line x1="{x}" y1="0" x2="{x}" y2="240"/>' for x in range(0, 241, 10)) + ''.join(f'<line x1="0" y1="{y}" x2="240" y2="{y}"/>' for y in range(0, 241, 10)) +
       '<circle cx="120" cy="120" r="92" stroke-dasharray="2 2"/><circle cx="120" cy="120" r="60.7" stroke-dasharray="2 2"/><circle cx="120" cy="120" r="29.4" stroke-dasharray="2 2"/><line x1="0" y1="120" x2="240" y2="120" stroke-dasharray="3 2"/></g>'
       + reg.replace('fill="#0A0C10"', 'fill="#0A0C10" fill-opacity=".9"') +
       '<g font-family="JetBrains Mono" font-size="5" fill="#B4935A"><text x="200" y="40">R</text><text x="168" y="62">0,66R</text><text x="138" y="98">0,32R</text><text x="14" y="114">2,36R</text><text x="196" y="210">reflexo · 0,35w</text></g></svg></div>'), '01 · Marca')
M.page(two('1.2 · Significado', 'O que cada parte diz.', '<b>Arcos de cima:</b> a marca pronta, de pé.<br><b>Reflexo de baixo:</b> de onde ela veio, o improviso que fica para trás.<br><b>Linha do horizonte:</b> a passagem, o barzakh.<br><b>Disco partido:</b> a luz (Bronze, o fio do grupo) e a hora azul (Lápis, a cor do estúdio): o minuto entre o dia e a noite.',
       f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:24px;height:100%"><div style="position:relative;background:{OB};border:1px solid #222">{horizonte("aqueduto", 0, 0, 476, 800, .5, .3)}<div class="mono" style="position:absolute;left:24px;bottom:24px">A foto · o arco e o rio</div></div>'
       f'<div style="position:relative;background:{GR};padding:110px 60px">{L("simbolo-negativo")}<div class="mono br" style="position:absolute;left:24px;bottom:24px">O símbolo · Dois mares</div></div></div>'), '01 · Marca')
M.page(two('1.3 · Variação monolito', 'O arco cheio, para gravar.', 'Mesma régua, com o mundo de cima em <b>arco cheio</b> (pedra monolítica) e o anel interno como fenda. O reflexo continua em linha.<br><br><b>Use em:</b> avatar, hot stamping, gravação em pedra, metal e couro, placa, selo de envelope.<br><b>Não use:</b> no lugar da assinatura principal em site e proposta.',
       f'<div style="display:grid;grid-template-columns:1.3fr 1fr;grid-template-rows:1fr 1fr;gap:20px;height:100%">'
       f'<div style="grid-row:span 2;position:relative;overflow:hidden;background:{OB}"><div class="ph" style="position:absolute;inset:0;background-image:url({U("concreto")});opacity:.5"></div><div class="win" style="opacity:.7"></div><div class="beam" style="left:40px;top:180px;width:520px;height:380px"></div><div style="position:absolute;left:80px;right:80px;top:120px;bottom:120px">{M_("monolito-negativo")}</div><div class="mono br" style="position:absolute;left:24px;bottom:24px">Monolito · negativo</div></div>'
       f'<div style="position:relative">{box(M_("monolito-lapis"), LA, 40)}<div class="mono" style="position:absolute;left:18px;bottom:14px;font-size:14px">Lápis · avatar</div></div>'
       f'<div style="position:relative;background:#141217" class="paper"><div class="foil" style="position:absolute;inset:50px;-webkit-mask-image:{mask("monolito-mono-branco")}"></div><div class="mono br" style="position:absolute;left:18px;bottom:14px;font-size:14px">Hot stamping bronze</div></div></div>'), '01 · Marca')
vs = [('Horizontal · principal', 'horizontal-negativo', OB, 50), ('Vertical', 'vertical-positivo', MA, 30), ('Símbolo', 'simbolo-negativo', GR, 40),
      ('Logotipo', 'logotipo-positivo', MA, 60), ('Assinatura com tagline', 'assinatura-negativo', OB, 40), ('Avatar', 'avatar-lapis', LA, 0)]
M.page('<div style="position:absolute;left:96px;top:140px"><div class="mono br">1.4 · Versões</div><div class="t2" style="margin-top:20px">Seis formas, um sistema.</div></div><div style="position:absolute;left:96px;right:96px;top:320px;bottom:120px;display:grid;grid-template-columns:repeat(3,1fr);grid-template-rows:1fr 1fr;gap:20px">' +
       ''.join(f'<div style="position:relative;min-height:0;overflow:hidden">{box(L(f), bg, pd, "padding-bottom:" + str(pd + 30) + "px")}<div class="mono" style="position:absolute;left:18px;bottom:14px;font-size:14px;color:{OB if bg == MA else MA}">{t}</div></div>' for t, f, bg, pd in vs) + '</div>', '01 · Marca')
cv = [('Positivo', 'horizontal-positivo', MA), ('Negativo', 'horizontal-negativo', OB), ('Lápis', 'horizontal-lapis', LA), ('Bronze', 'horizontal-bronze', OB), ('Mono preto', 'horizontal-mono-preto', '#FFFFFF'), ('Mono branco', 'horizontal-mono-branco', GR)]
M.page(two('1.5 · Cores da assinatura', 'Cor, negativo e uma cor.', 'Use a <b>negativa</b> sobre Obsidiana e foto escura (é a mais usada), a <b>positiva</b> sobre Marfim e a <b>Lápis</b> sobre o campo azul. Mono preto e mono branco para carimbo, gravação, fax e jornal. Bronze só em superfícies escuras e nobres.',
       '<div style="display:grid;grid-template-columns:1fr 1fr;grid-template-rows:repeat(3,1fr);gap:16px;height:100%">' + ''.join(f'<div style="position:relative;min-height:0;overflow:hidden">{box(L(f), bg, 34, "padding-bottom:50px")}<div class="mono" style="position:absolute;left:16px;bottom:12px;font-size:11px;color:{OB if bg in (MA, "#FFFFFF") else MA}">{t}</div></div>' for t, f, bg in cv) + '</div>'), '01 · Marca')
M.page(two('1.6 · Proteção e tamanho mínimo', 'Espaço para respirar.', 'Em volta da assinatura, deixe livre <b>X</b> = metade da largura do arco externo. Nenhum texto, borda ou imagem entra nessa área.<br><br><b>Mínimos</b><br>Horizontal: 120 px · 30 mm<br>Vertical: 80 px · 20 mm<br>Símbolo: 16 px · 5 mm<br>Monolito: 24 px · 6 mm (hot stamping: 8 mm)',
       f'<div style="display:grid;grid-template-rows:1.4fr 1fr;gap:20px;height:100%"><div style="background:{MA};display:grid;place-items:center"><div style="position:relative;padding:60px;outline:2px dashed {BR};background:repeating-linear-gradient(45deg,rgba(180,147,90,.14) 0 8px,transparent 8px 16px)"><div style="background:{MA};width:640px;height:193px">{L("horizontal-positivo")}</div>' +
       ''.join(f'<span class="mono br" style="position:absolute;{p}">X</span>' for p in ['left:22px;top:46%', 'right:22px;top:46%', 'top:18px;left:50%', 'bottom:18px;left:50%']) + '</div></div>'
       f'<div style="background:{GR};display:flex;align-items:flex-end;justify-content:space-around;padding:40px 30px 30px">' + ''.join(f'<div style="text-align:center"><div style="width:{w}px;height:{h}px;margin:0 auto 14px">{L(f) if not f.startswith("monolito") else M_(f)}</div><div class="mono" style="font-size:11px">{t}</div></div>' for f, w, h, t in [('horizontal-negativo', 300, 90, '300 px'), ('horizontal-negativo', 120, 36, '120 px · mín.'), ('vertical-negativo', 80, 70, '80 px · mín.'), ('simbolo-negativo', 16, 16, '16 px'), ('monolito-negativo', 24, 24, '24 px')]) + '</div></div>'), '01 · Marca')
bad = [('Não distorcer', 'transform:scaleX(1.45)'), ('Não girar', 'transform:rotate(-12deg)'), ('Não trocar cores', 'filter:hue-rotate(150deg) saturate(3)'), ('Sem brilho ou degradê', 'filter:drop-shadow(0 0 12px #a855f7) drop-shadow(0 0 22px #22d3ee)'),
       ('Sem lua ou estrela', 'X'), ('Não pôr sobre foto agitada', 'Y')]
def bad_cell(t, st):
    if st == 'X': inner = f'<div style="position:relative;width:100%;height:120px">{L("horizontal-positivo")}<span style="position:absolute;left:22px;top:-26px;font-size:40px;color:{BR}">☾ ✦</span></div>'
    elif st == 'Y': inner = f'<div class="ph" style="position:absolute;inset:0;background-image:url({U("slz")});filter:saturate(1.6) brightness(1.5)"></div><div style="position:relative;width:100%;height:120px">{L("horizontal-mono-preto")}</div>'
    else: inner = f'<div style="width:100%;height:120px;{st}">{L("horizontal-positivo")}</div>'
    return f'<div style="position:relative;background:{MA};display:grid;place-items:center;padding:56px;overflow:hidden">{inner}<div style="position:absolute;inset:0;background:linear-gradient(to top right,transparent 49.6%,#C0392B 49.6% 50.4%,transparent 50.4%)"></div><div class="mono" style="position:absolute;left:18px;bottom:14px;font-size:14px;color:#C0392B;background:{MA};padding:2px 6px">✕ {t}</div></div>'
M.page('<div style="position:absolute;left:96px;top:140px"><div class="mono br">1.7 · Usos incorretos</div><div class="t2" style="margin-top:20px">O que nunca fazer.</div></div><div style="position:absolute;left:96px;right:96px;top:320px;bottom:120px;display:grid;grid-template-columns:repeat(3,1fr);gap:20px">' + ''.join(bad_cell(*b) for b in bad) + '</div>', '01 · Marca')
M.divider('02', 'Cor', 'A noite, o marfim da pedra, o bronze da luz e o azul da hora entre o dia e a noite.', 'mar')
pal = [('Obsidiana', OB, '55%', 'Base. Fundos e textos sobre marfim.'), ('Marfim', MA, '25%', 'Respiro, papel, texto sobre escuro.'), ('Lápis da Hora Azul', LA, '12%', 'Cor do estúdio. Campos de cor, metade de baixo do disco.'),
       ('Bronze', BR, '5%', 'A luz. Disco, filetes, numeração, hot stamping.'), ('Grafite', GR, '3%', 'Superfícies e cartões.'), ('Pedra', PE, '—', 'Legendas, linhas, texto de apoio.')]
M.page('<div style="position:absolute;left:96px;top:140px"><div class="mono br">2.1 · Paleta</div><div class="t2" style="margin-top:20px">Seis cores, códigos exatos.</div></div><div style="position:absolute;left:96px;right:96px;top:320px;bottom:120px;display:grid;grid-template-columns:repeat(6,1fr);gap:14px">' +
       ''.join(f'<div style="background:{h};color:{OB if h in (MA, BR, PE) else MA};padding:26px 22px;display:flex;flex-direction:column;justify-content:flex-end;position:relative;border:1px solid rgba(238,234,226,.1)"><div class="mono" style="position:absolute;top:22px;left:22px;font-size:14px;opacity:.8">{pc}</div><div class="ser" style="font-size:34px;line-height:1">{n}</div><div class="mono" style="font-size:14px;line-height:1.9;margin-top:16px">HEX {h}<br>RGB {" ".join(map(str, rgbc(h)))}<br>CMYK {" ".join(map(str, cmyk(h)))}</div><div style="font-size:14px;line-height:1.4;margin-top:14px;opacity:.85">{d}</div></div>' for n, h, pc, d in pal) + '</div>', '02 · Cor')
M.page(two('2.2 · Proporção e regras', 'Muito escuro, pouca luz.', 'Obsidiana 55 · Marfim 25 · Lápis 12 · Bronze 5 · Grafite e Pedra 3.<br><br>Lápis só em campo de cor e no disco, nunca em texto pequeno sobre Obsidiana. Bronze nunca em área grande ao lado do Lápis. O Índigo noturno da holding não entra nas peças da Barzakh. CMYK aproximado: confirme com prova impressa.',
       '<div style="display:grid;grid-template-rows:200px 1fr;gap:24px;height:100%"><div style="display:flex;height:100%">' + ''.join(f'<div style="flex:{v};background:{c};position:relative;border:1px solid rgba(238,234,226,.08)"><span class="mono" style="position:absolute;left:12px;bottom:10px;font-size:11px;color:{OB if c in (MA, BR) else MA}">{v}</span></div>' for c, v in [(OB, 55), (MA, 25), (LA, 12), (BR, 5), (GR, 3)]) + '</div>'
       f'<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:16px">'
       f'<div style="position:relative;background:{OB};border:1px solid #222;padding:30px"><div class="ser" style="font-size:44px">Texto Marfim sobre Obsidiana</div><div class="mono br" style="position:absolute;left:20px;bottom:16px;font-size:11px">✓ 16:1</div></div>'
       f'<div style="position:relative;background:{LA};padding:30px"><div class="ser" style="font-size:44px">Marfim sobre Lápis</div><div class="mono" style="position:absolute;left:20px;bottom:16px;font-size:11px">✓ 8:1</div></div>'
       f'<div style="position:relative;background:{OB};border:1px solid #222;padding:30px"><div style="font-size:20px;color:{LA}">Lápis em texto pequeno sobre Obsidiana some.</div><div class="mono" style="position:absolute;left:20px;bottom:16px;font-size:11px;color:#d9776b">✕ Evitar</div></div></div></div>'), '02 · Cor')
M.divider('03', 'Tipografia', 'Serifada fina com muito respiro, uma sem serifa precisa e um mono para rótulos.', 'espiral')
M.page('<div style="position:absolute;left:96px;top:140px"><div class="mono br">3.1 · Famílias</div><div class="t2" style="margin-top:20px">Três vozes, a mesma família do grupo.</div></div>'
       '<div style="position:absolute;left:96px;right:96px;top:330px;bottom:120px;display:grid;grid-template-columns:1.3fr 1fr 1fr;gap:20px">'
       f'<div class="card" style="padding:40px;position:relative;background:{GR}"><div class="mono br">Títulos · Fraunces</div><div class="ser" style="font-size:180px;line-height:1;margin-top:20px">Aa</div><div class="ser" style="font-size:36px;margin-top:10px">A passagem <i>da sua marca.</i></div><div class="mono" style="position:absolute;left:40px;bottom:30px;font-size:14px;opacity:.6">Regular e Itálica · versal espaçada 0,32em no logotipo</div></div>'
       '<div class="card" style="padding:40px;position:relative"><div class="mono br">Texto · Inter Tight</div><div style="font-size:150px;line-height:1;margin-top:20px;font-weight:300">Aa</div><div style="font-size:20px;line-height:1.5;margin-top:16px;font-weight:300">Light 300 para texto, Medium 500 para destaque, SemiBold 600 só em botão.</div></div>'
       '<div class="card" style="padding:40px;position:relative"><div class="mono br">Rótulos · JetBrains Mono</div><div style="font-family:JetBrains Mono;font-size:130px;line-height:1;margin-top:30px">01</div><div class="mono" style="font-size:16px;margin-top:20px;line-height:1.8">ETAPA 01 · A ESCUTA<br>CASE 004 · CLÍNICA</div></div></div>', '03 · Tipografia')
hier = [('Display · Serif 140/0,92', 'ser', 'Onde a marca toma forma.', 120), ('Título · Serif 76/1', 'ser', 'Antes de desenhar, a gente escuta.', 64), ('Subtítulo · Inter Tight 300 · 34', 'sub', 'Identidade visual e branding em São Luís, MA.', 32),
        ('Texto · Inter Tight 300 · 22/1,5', 'txt', 'A Barzakh entrega um sistema que você consegue usar todo dia: logo, cores, letras, voz e aplicações, mostrados em mockup antes do arquivo final.', 22), ('Rótulo · Mono 15 · +14', 'mono', 'Etapa 03 · A forma · 2026', 15)]
M.page('<div style="position:absolute;left:96px;top:140px"><div class="mono br">3.2 · Hierarquia</div></div><div style="position:absolute;left:96px;right:96px;top:200px">' +
       ''.join(f'<div style="display:grid;grid-template-columns:300px 1fr;gap:30px;align-items:center;padding:22px 0;border-bottom:1px solid rgba(238,234,226,.12)"><span class="mono" style="font-size:14px;opacity:.6">{a}</span><span class="{"ser" if c == "ser" else ("mono br" if c == "mono" else "")}" style="font-size:{s}px;line-height:1.1;font-weight:300">{t}</span></div>' for a, c, t, s in hier) + '</div>', '03 · Tipografia')
M.page(two('3.3 · Grafismo do horizonte', 'A linha que corta a foto.', 'O símbolo vira sistema: uma linha fina de Marfim atravessa a foto. <b>Em cima, nítido</b>: a marca pronta. <b>Embaixo, desfocado e granulado</b>, com véu azul: o reflexo, o que ficou para trás.<br><br>A linha fica entre 45% e 65% da altura. Pode levar o disco partido em cima dela, só uma vez por peça.',
       '<div style="display:grid;grid-template-columns:1.4fr 1fr;grid-template-rows:1fr 1fr;gap:20px;height:100%">'
       f'<div style="grid-row:span 2;position:relative">{horizonte("aqueduto", 0, 0, 590, 800, .55, .15, disco=True)}<div class="mono" style="position:absolute;left:20px;top:20px">Com disco · capa</div></div>'
       f'<div style="position:relative">{horizonte("colunata", 0, 0, 410, 390, .5, .1)}<div class="mono" style="position:absolute;left:16px;top:16px;font-size:14px">Sem disco · post</div></div>'
       f'<div style="position:relative">{horizonte("langen", 0, 0, 410, 390, .62, .1)}<div class="mono" style="position:absolute;left:16px;top:16px;font-size:14px">Foto colorida · hora azul</div></div></div>'), '03 · Grafismo')
M.page(two('3.4 · Ícones de linha', 'O traço do reflexo.', 'Ícones em linha de 1,6 px numa grade de 48, ponta reta, sem preenchimento: o mesmo traço do reflexo do símbolo. Um estilo só; nunca misturar com ícone cheio ou colorido.<br><br>Cor: Marfim ou Bronze sobre escuro, Obsidiana sobre claro.',
       '<div style="display:grid;grid-template-columns:repeat(4,1fr);grid-template-rows:repeat(3,1fr);gap:14px;height:100%">' +
       ''.join(f'<div class="card" style="position:relative;display:grid;place-items:center;background:{GR if i in (0, 5, 10) else "transparent"}">{icon(k, BR if i % 3 == 1 else MA, 76)}<div class="mono" style="position:absolute;left:14px;bottom:10px;font-size:11px;opacity:.6">{k}</div></div>' for i, k in enumerate(IC)) + '</div>'), '03 · Grafismo')
M.divider('04', 'Imagem', 'Escura, granulada, arquitetura e luz rasante. O místico do museu, nunca o da feira.', 'sombra')
M.page('<div style="position:absolute;left:96px;top:140px;width:600px"><div class="mono br">4.1 · Direção de foto</div><div class="t2" style="margin:20px 0 26px">Pedra, sombra, silêncio.</div><div class="p" style="font-size:21px">Arquitetura (arcos, vãos, escadas, colunas), horizonte de mar, concreto e pedra crua, sombra de janela e luz rasante dura. Tratamento único: preto e branco quente, sombras em Obsidiana, grão de 6% a 9%. Foto colorida só na hora azul.</div>'
       '<div class="mono" style="color:#d9776b;margin-top:34px">Nunca</div><div class="p" style="font-size:21px;margin-top:8px">Tarô, lua, estrela, olho, mandala, cristal, incenso, deserto com camelo, foto de banco sorrindo para a câmera.</div></div>'
       '<div style="position:absolute;left:760px;right:96px;top:140px;bottom:120px;display:grid;grid-template-columns:repeat(3,1fr);grid-template-rows:1fr 1fr;gap:14px">' +
       ''.join(f'<div class="ph grain" style="position:relative;background-image:url({U(k)});{"grid-row:span 2" if i == 0 else ""}"><div class="mono" style="position:absolute;left:12px;bottom:10px;font-size:11px;background:rgba(10,12,16,.6);padding:3px 6px">{t}</div></div>' for i, (k, t) in enumerate([('colunata', 'Sombra longa'), ('espiral', 'Forma'), ('aqueduto', 'Arco'), ('mar', 'Horizonte'), ('concreto', 'Concreto cru')])) + '</div>', '04 · Imagem')
M.page(two('4.2 · Antes e depois do tratamento', 'Toda foto passa pelo mesmo filtro.', 'Mesma receita em todas: tirar a cor (ou baixar para 75% na hora azul), contraste +35%, curva escura, sombras em Obsidiana, luzes em Marfim quente e grão. Assim o feed parece uma série, mesmo com fotos de origens diferentes.<br><br>Fotos deste manual: Wikimedia Commons (licenças livres, créditos no README).',
       f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;height:100%"><div class="ph" style="position:relative;background-image:url(file://{F}/aqueduto2.jpg)"><div class="mono" style="position:absolute;left:16px;top:16px;background:rgba(10,12,16,.7);padding:4px 8px;color:#d9776b">✕ Original</div></div>'
       f'<div class="ph" style="position:relative;background-image:url({U("aqueduto")})"><div class="mono br" style="position:absolute;left:16px;top:16px;background:rgba(10,12,16,.7);padding:4px 8px">✓ Tratada Barzakh</div></div></div>'), '04 · Imagem')
M.divider('05', 'Aplicações', 'Do avatar à fachada: a mesma passagem em cada ponto de contato.', 'langen')
M.page('<div style="position:absolute;left:96px;top:140px;width:520px"><div class="mono br">5.1 · Instagram 4:5</div><div class="t2" style="margin:20px 0 26px">Quatro composições que se alternam.</div><div class="p" style="font-size:21px">1080 × 1350. Nunca duas seguidas iguais: foto com horizonte, papel Marfim com frase, campo Lápis com o monolito, case com antes e depois. Exemplos de case marcados como ilustrativos.</div></div>'
       '<div style="position:absolute;left:720px;right:96px;top:150px;bottom:110px;display:grid;grid-template-columns:1fr 1fr;gap:18px;justify-items:center;align-items:center">' +
       ''.join(f'<div style="zoom:.72">{frame(post(i), 432, 540)}</div>' for i in range(4)) + '</div>', '05 · Digital')
M.page(f'<div class="ph" style="position:absolute;inset:0;background-image:url({U("concreto")});opacity:.35"></div><div class="win" style="opacity:.6"></div>'
       '<div style="position:absolute;left:96px;top:140px;width:520px"><div class="mono br">5.2 · Story e avatar</div><div class="t2" style="margin:20px 0 26px">Vertical com o horizonte no meio.</div><div class="p" style="font-size:21px">Story 1080 × 1920: linha do horizonte entre 50% e 60%, texto na parte nítida, botão em contorno embaixo. Avatar: monolito no Obsidiana, legível a 40 px.</div></div>'
       f'<div style="position:absolute;left:760px;top:150px"><div style="zoom:1.5">{frame(story(), 304, 540, 10)}</div></div>'
       f'<div style="position:absolute;left:1300px;top:240px;display:flex;flex-direction:column;gap:40px;align-items:center">' +
       ''.join(f'<div style="text-align:center"><div style="width:{s}px;height:{s}px;border-radius:50%;overflow:hidden;background:{bg};padding:{s*.12}px;box-shadow:0 10px 30px rgba(0,0,0,.5);margin:0 auto">{M_(n)}</div><div class="mono" style="font-size:11px;margin-top:10px">{s} px</div></div>' for n, bg, s in [('monolito-negativo', OB, 280), ('monolito-lapis', LA, 120), ('monolito-negativo', OB, 40)]) + '</div>', '05 · Digital')
M.page('<div style="position:absolute;left:96px;top:140px;width:520px"><div class="mono br">5.3 · Pinterest e Behance</div><div class="t2" style="margin:20px 0 26px">Pin vertical e capa de case.</div><div class="p" style="font-size:21px">Pin 1000 × 1500: foto em cima, horizonte embaixo, título que responde a uma busca (“identidade visual para clínica”). Capa Behance 808 × 632: foto da hora azul com linha, número do case em mono e assinatura no canto.</div></div>'
       f'<div style="position:absolute;left:740px;top:150px">{frame(pin(), 360, 540)}<div class="mono" style="margin-top:14px;font-size:14px;opacity:.6">Pin · 1000 × 1500</div></div>'
       f'<div style="position:absolute;left:1160px;top:150px;transform:scale(1.6);transform-origin:top left">{frame(behance(), 404, 316)}</div><div class="mono" style="position:absolute;left:1160px;top:680px;font-size:14px;opacity:.6">Capa de case Behance · 808 × 632</div>'
       f'<div style="position:absolute;left:1160px;top:730px;right:96px;display:grid;grid-template-columns:repeat(3,1fr);gap:10px">' + ''.join(f'<div class="ph" style="height:180px;background-image:url({U(k)})"></div>' for k in ['colunata', 'espiral', 'mar']) + '</div>', '05 · Digital')
M.page(two('5.4 · Papelaria', 'Cartão, papel e envelope.', '<b>Cartão</b> 85 × 50 mm: frente Obsidiana com monolito em hot stamping bronze; verso Marfim com nome em serifada e logotipo em bronze. Papel texturizado de 350 g ou mais.<br><b>Papel timbrado</b> A4: assinatura no topo, filete bronze no rodapé.<br><b>Envelope</b> DL em Lápis, selo monolito em bronze.',
       f'<div class="paper" style="position:relative;width:100%;height:100%;background-color:#1a1c22;overflow:hidden"><div class="win" style="opacity:.5"></div>'
       f'<div style="position:absolute;left:60px;top:60px;transform:rotate(-4deg)">{timbrado(330)}</div>'
       f'<div style="position:absolute;left:470px;top:80px;transform:rotate(3deg)">{envelope(470)}</div>'
       f'<div style="position:absolute;left:470px;top:420px;transform:rotate(-6deg)">{cartao_frente(320, 188)}</div>'
       f'<div style="position:absolute;left:720px;top:520px;transform:rotate(5deg)">{cartao_verso(320, 188)}</div></div>'), '05 · Papelaria')
M.page(two('5.5 · Assinatura de e-mail', 'Curta e sem imagem pesada.', 'Nome em serifada, cargo em mono bronze, assinatura da Barzakh e o endosso. Sem frase motivacional, sem banner. O número de WhatsApp é sempre o oficial do site.',
       f'<div style="position:relative;height:100%;background:#E9E6E0;border-radius:8px;overflow:hidden;color:{OB};box-shadow:0 40px 80px rgba(0,0,0,.5)">'
       f'<div style="height:52px;background:#d8d4cc;display:flex;align-items:center;gap:10px;padding:0 20px"><i style="width:12px;height:12px;border-radius:50%;background:#c9c4ba"></i><i style="width:12px;height:12px;border-radius:50%;background:#c9c4ba"></i><i style="width:12px;height:12px;border-radius:50%;background:#c9c4ba"></i><span class="mono" style="margin-left:20px;font-size:14px;opacity:.6">Nova mensagem</span></div>'
       f'<div style="padding:40px 60px;font-size:20px;line-height:1.6"><div style="opacity:.5;border-bottom:1px solid #ccc;padding-bottom:10px">Para: cliente · Assunto: Proposta de identidade visual</div><div style="margin-top:26px">Oi, tudo bem? Segue a proposta organizada, com as etapas e o prazo de cada uma. Qualquer dúvida, me chama no WhatsApp.</div>'
       f'<div style="margin-top:46px;display:flex;gap:34px;align-items:center;border-top:1px solid {BR};padding-top:30px"><div style="width:120px;height:120px;background:{OB};padding:14px;flex:none">{M_("monolito-negativo")}</div>'
       f'<div><div class="ser" style="font-size:40px;line-height:1">Lindson Almeida</div><div class="mono br" style="font-size:14px;margin:8px 0 12px">Direção criativa</div><div style="font-size:17px;line-height:1.5">Barzakh · um estúdio Al Kántara<br>@barzakhstudio · São Luís, MA<br><span style="opacity:.6">WhatsApp: número oficial do site</span></div></div></div></div></div>'), '05 · Digital')
# mockups
M.page(f'<div class="paper" style="position:absolute;inset:0;background-color:#16171b"></div><div class="ph" style="position:absolute;inset:0;background-image:url({U("concreto")});opacity:.45;mix-blend-mode:screen"></div>'
       f'<div class="win" style="opacity:.85"></div><div class="beam" style="left:700px;top:200px;width:900px;height:600px;opacity:.6"></div>'
       f'<div style="position:absolute;left:820px;top:230px;transform:perspective(1600px) rotateX(38deg) rotateZ(-14deg)">{cartao_frente(560, 330)}</div>'
       f'<div style="position:absolute;left:1180px;top:540px;transform:perspective(1600px) rotateX(38deg) rotateZ(10deg)">{cartao_verso(560, 330)}</div>'
       '<div style="position:absolute;left:96px;top:150px;width:520px"><div class="mono br">5.6 · Mockup · cartão</div><div class="t2" style="margin:20px 0 26px">Hot stamping e sombra de janela.</div><div class="p" style="font-size:21px">O monolito em bronze sobre papel escuro texturizado, com luz rasante. É o primeiro objeto que o cliente segura: vale o acabamento.</div></div>', '05 · Mockups')
M.page(f'<div style="position:absolute;inset:0;background:radial-gradient(ellipse at 65% 40%,#2a2d36,{OB} 70%)"></div><div class="win" style="opacity:.6"></div>'
       f'<div style="position:absolute;left:840px;top:110px;transform:perspective(2000px) rotateY(-14deg) rotateX(6deg)">{phone(perfil(), 400, 820)}</div>'
       f'<div style="position:absolute;left:1340px;top:260px;transform:perspective(2000px) rotateY(-20deg)">{phone(story(), 300, 610)}</div>'
       '<div style="position:absolute;left:96px;top:150px;width:560px"><div class="mono br">5.7 · Mockup · celular</div><div class="t2" style="margin:20px 0 26px">O perfil como vitrine.</div><div class="p" style="font-size:21px">Avatar monolito, nome de exibição com a palavra-chave “Identidade Visual”, bio em três linhas com o rosto do estúdio e destaques em ícone de linha. Grade alternando foto, papel e campo Lápis.</div></div>', '05 · Mockups')
M.page(f'<div class="ph" style="position:absolute;inset:0;background-image:url({U("concreto")})"></div><div class="win" style="opacity:.9"></div><div style="position:absolute;inset:0;background:linear-gradient(90deg,{OB} 30%,rgba(10,12,16,.15) 70%,rgba(10,12,16,.4))"></div>'
       f'<div style="position:absolute;left:980px;top:170px;width:680px;height:680px;border-radius:340px 340px 0 0;background:linear-gradient(160deg,#2a2c31,#141519);box-shadow:inset 0 0 0 1px rgba(255,255,255,.06),0 50px 90px rgba(0,0,0,.7);overflow:hidden">'
       f'<div class="paper" style="position:absolute;inset:0;opacity:.6"></div><div class="beam" style="left:120px;top:250px;width:440px;height:300px;opacity:.7"></div>'
       f'<div class="foil" style="position:absolute;left:170px;top:120px;width:340px;height:340px;-webkit-mask-image:{mask("monolito-mono-branco")}"></div>'
       f'<div class="foil" style="position:absolute;left:150px;top:500px;width:380px;height:80px;-webkit-mask-image:{mask("logotipo-mono-branco")}"></div>'
       f'<div class="mono" style="position:absolute;left:0;right:0;top:600px;text-align:center;font-size:13px;color:{BR}">{kv2(12, BR)}um estúdio Al Kántara</div></div>'
       '<div style="position:absolute;left:96px;top:150px;width:560px"><div class="mono br">5.8 · Mockup · placa do estúdio</div><div class="t2" style="margin:20px 0 26px">Um arco na parede.</div><div class="p" style="font-size:21px">Placa em arco de metal escovado escuro, com o monolito e o logotipo em bronze, presa no concreto. Iluminação rasante de cima. Proposta de aplicação; sem fachada definida ainda.</div></div>', '05 · Mockups')
M.page(f'<div class="ph" style="position:absolute;inset:0;background-image:url({U("concreto")});filter:brightness(1.6)"></div><div class="win" style="opacity:.9;mix-blend-mode:multiply"></div>'
       f'<div style="position:absolute;inset:0;background:linear-gradient(90deg,{OB} 30%,rgba(10,12,16,0) 60%)"></div>'
       f'<div class="paper" style="position:absolute;left:880px;top:150px;width:520px;height:640px;background-color:#d9d2c3;transform:rotate(-7deg);box-shadow:0 40px 70px rgba(0,0,0,.6);clip-path:polygon(4% 0,96% 0,100% 100%,0 100%)">'
       f'<div style="position:absolute;left:150px;top:-40px;width:220px;height:160px;border:16px solid #c4bba8;border-bottom:none;border-radius:110px 110px 0 0"></div>'
       f'<div style="position:absolute;left:110px;top:200px;width:300px;height:300px">{M_("monolito-positivo").replace("#EEEAE2", "transparent", 1) if False else M_("monolito-mono-preto")}</div>'
       f'<div style="position:absolute;left:90px;top:520px;width:340px;height:70px">{L("logotipo-mono-preto")}</div><div class="win" style="opacity:.5"></div></div>'
       f'<div style="position:absolute;left:1340px;top:330px;width:360px;height:500px;background:{LA};transform:rotate(9deg);box-shadow:0 40px 70px rgba(0,0,0,.6);border-radius:4px 12px 12px 4px;overflow:hidden" class="paper">'
       f'<div style="position:absolute;left:0;top:0;bottom:0;width:18px;background:rgba(0,0,0,.25)"></div><div class="foil" style="position:absolute;left:90px;top:120px;width:180px;height:180px;-webkit-mask-image:{mask("monolito-mono-branco")}"></div>'
       f'<div class="mono" style="position:absolute;left:0;right:0;bottom:40px;text-align:center;font-size:14px;color:{MA}">Caderno de processo</div><div class="win" style="opacity:.4"></div></div>'
       '<div style="position:absolute;left:96px;top:150px;width:560px"><div class="mono br">5.9 · Mockup · ecobag e caderno</div><div class="t2" style="margin:20px 0 26px">O que o cliente leva para casa.</div><div class="p" style="font-size:21px">Ecobag de algodão cru com o monolito em serigrafia preta; caderno de processo em capa Lápis com hot stamping bronze. Entregue junto com o guia de marca.</div></div>', '05 · Mockups')
M.page(f'<div class="ph" style="position:absolute;inset:0;background-image:url({U("aqueduto")})"></div><div style="position:absolute;inset:0;background:linear-gradient(90deg,{OB} 40%,rgba(10,12,16,.3))"></div>'
       f'<div class="beam" style="left:1100px;top:300px;width:800px;height:500px"></div><div style="position:absolute;left:1260px;top:300px;width:460px;height:460px">{M_("monolito-negativo")}</div>'
       f'<div style="position:absolute;left:96px;top:280px;width:1000px"><div class="mono br">Contato e arquivos</div><div class="ser" style="font-size:120px;line-height:.95;margin-top:24px">Pronta para<br><i class="br">se apresentar.</i></div>'
       f'<div class="p" style="margin-top:36px;font-size:20px">Arquivos em <span class="mono" style="font-size:15px">entregas/elementos.zip</span>: logos em SVG e PNG, paleta em JSON, fontes. Dúvidas sobre uso: direção criativa, Lindson Almeida · @barzakhstudio.</div>'
       f'<div class="mono" style="margin-top:40px;font-size:14px;opacity:.6;line-height:1.8">Fotos: Wikimedia Commons (CC0, CC BY, CC BY-SA), tratadas. Aqueduto de Segóvia, colunata, Hyogo Prefectural Museum of Art,<br>Langen Foundation, Vitra Conference Pavilion, centro histórico de São Luís, “Between shadow & light”, “Monochrome ships on horizon”.</div></div>', 'Fim')

# ======================================================================= render + conferência
CHECK = r"""() => {
  const out = [];
  document.querySelectorAll('section.pg').forEach((sec, i) => {
    const sr = sec.getBoundingClientRect();
    sec.querySelectorAll('*').forEach(el => {
      if (el.closest('svg') && el.tagName !== 'svg') return;
      const own = [...el.childNodes].some(n => n.nodeType === 3 && n.textContent.trim().length > 1);
      if (!own) return;
      const r = el.getBoundingClientRect(); if (r.width === 0) return;
      let hidden = false, p = el.parentElement;
      while (p && p !== sec) { const st = getComputedStyle(p); if (st.transform !== 'none') { hidden = true; break; } p = p.parentElement; }
      const txt = el.textContent.trim().slice(0, 40);
      if (el.scrollWidth > el.clientWidth + 2 && getComputedStyle(el).display !== 'inline') out.push([i + 1, 'scrollW', txt, el.scrollWidth, el.clientWidth]);
      const rg = document.createRange(); rg.selectNodeContents(el); const tr = rg.getBoundingClientRect();
      let q = el.parentElement;
      while (q && q !== sec) { const st = getComputedStyle(q); if (st.overflow === 'hidden' && st.transform === 'none') { const qr = q.getBoundingClientRect();
        if (tr.right > qr.right + 2 || tr.bottom > qr.bottom + 2 || tr.left < qr.left - 2 || tr.top < qr.top - 2) { out.push([i + 1, 'cortado', txt, Math.round(tr.right - qr.right), Math.round(tr.bottom - qr.bottom)]); break; } } q = q.parentElement; }
      if (!hidden && (tr.right > sr.right - 40 || tr.bottom > sr.bottom - 30)) out.push([i + 1, 'pagina', txt]);
    });
  });
  // sobreposição de blocos de texto com o rodapé/cabeçalho
  return out;
}"""

def render():
    with sync_playwright() as p:
        b = p.chromium.launch(proxy={'server': os.environ['HTTPS_PROXY']} if os.environ.get('HTTPS_PROXY') else None, args=['--allow-file-access-from-files'], executable_path='/opt/pw-browsers/chromium-1243/chrome-linux64/chrome')
        for doc, nome in [(K, 'barzakh-branding-book'), (M, 'barzakh-manual-de-marca')]:
            h = f'{G}/{nome}.html'; open(h, 'w').write(doc.html())
            pg = b.new_page(viewport={'width': 1920, 'height': 1080}); pg.goto('file://' + h); pg.wait_for_timeout(3500)
            pg.evaluate('document.fonts.ready')
            probs = pg.evaluate(CHECK)
            print(nome, len(doc.p), 'páginas ·', len(probs), 'alertas')
            for x in probs: print('  ', x)
            d = f'{OUT}/paginas/{nome}'; shutil.rmtree(d, ignore_errors=True); os.makedirs(d)
            for i, el in enumerate(pg.query_selector_all('section.pg')):
                el.screenshot(path=f'{d}/{i+1:02d}.jpg', type='jpeg', quality=86)
            pg.close()
            ims = [Image.open(f) .convert('RGB') for f in sorted(glob.glob(f'{d}/*.jpg'))]  # PDF a partir das páginas (o PDF vetorial estoura memória com os desfoques)
            ims[0].save(f'{OUT}/{nome}.pdf', save_all=True, append_images=ims[1:], resolution=144, quality=88)
        # PNG das variações monolito
        pg = b.new_page(viewport={'width': 720, 'height': 720})
        for n in MONO:
            pg.set_content(f'<html><body style="margin:0;background:transparent">{svgtxt(n).replace("<svg ", "<svg style=\"width:720px;height:720px;display:block\" ", 1)}</body></html>')
            pg.screenshot(path=f'{B}/logos/png/barzakh-{n}.png', omit_background=True)
        b.close()

def elementos():
    pal = {n: {'hex': h, 'rgb': rgbc(h), 'cmyk_aprox': cmyk(h), 'proporcao': pc, 'uso': d} for n, h, pc, d in pal_all}
    json.dump(pal, open(f'{G}/paleta.json', 'w'), ensure_ascii=False, indent=2)
    fontes = ('Barzakh · fontes (Google Fonts, licença OFL)\n'
              'Títulos: Fraunces (Regular e Itálica, eixo óptico 144 nos títulos) — logotipo em versal com kerning à mão (mesma família da holding Al Kántara v2)\n'
              'Texto: Inter Tight (300 texto, 500 destaque, 600 botão)\n'
              'Rótulos e numeração: JetBrains Mono (400, caixa alta, +14)\n'
              'https://fonts.google.com/specimen/Fraunces · https://fonts.google.com/specimen/Inter+Tight · https://fonts.google.com/specimen/JetBrains+Mono\n')
    with zipfile.ZipFile(f'{OUT}/elementos.zip', 'w', zipfile.ZIP_DEFLATED) as z:
        for f in sorted(glob.glob(f'{B}/logos/svg/*.svg') + glob.glob(f'{B}/logos/png/*.png')):
            z.write(f, 'logos/' + f.split('/logos/')[1])
        z.write(f'{G}/paleta.json', 'paleta.json'); z.writestr('fontes.txt', fontes)

pal_all = pal
render(); elementos()
