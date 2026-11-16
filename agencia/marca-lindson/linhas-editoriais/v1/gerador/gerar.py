# Linhas editoriais v1 da marca Lindson (conta Leandro, 16/11/2026)
# 28 conteúdos (7 linhas x 4). Identidade: preto + amarelo #F5C518, Anton + Manrope + JetBrains Mono, grão (capas-1611 aprovado)
# + linguagem dos criativos aprovados em 16/11 (Denis Bugatti: pessoa recortada 50-70%, luz de cinema, palavra gigante com 1 palavra neon;
# Gomes & Moura: serifa itálica no editorial das frases, palavra gigante translúcida ao fundo, rótulos pequenos no topo).
# Uso: python3 gerar.py [id ...]   (recortes em $REC, gerados com ferramentas/recorte2.py das fotos escolhidas-2026-11-16)
import os, sys, json, html
from conteudo import POSTS, ORDEM
from playwright.sync_api import sync_playwright

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(BASE)
REC = os.environ.get('REC', '/tmp/claude-0/-home-user/b9464785-a028-5189-b9f0-a7ed9d7dd59e/scratchpad/rec')
ORIG = '/home/user/centrallindsonalmeida/painel/fotos-lindson/escolhidas-2026-11-16'
AG = '/home/user/lindson/agencia'
F = {'01': .8, '02': .7, '03': .85, '04': .5, '05': .5, '06': .62, '07': .6, '08': 1.0, '09': .75, '10': .8,
     '11': .38, '12': .42, '13': .45, '14': .36, '15': .5, '16': .55}
DIM = {}
Y, K, CR = '#F5C518', '#0B0B0C', '#F1EBDF'

def e(s): return html.escape(s, quote=False)
def neon(t):  # *palavra* = destaque
    import re
    return re.sub(r'\*(.+?)\*', r'<b class="ne">\1</b>', e(t))
def src(p): return 'file://' + (p if p.startswith('/') else AG + '/' + p)

CSS = f"""*{{margin:0;padding:0;box-sizing:border-box}}body{{width:1080px;height:1350px;overflow:hidden;font-family:Manrope;-webkit-font-smoothing:antialiased}}
.a{{position:relative;width:1080px;height:1350px;overflow:hidden}}.abs{{position:absolute}}
.an{{font-family:Anton;text-transform:uppercase;line-height:.9;letter-spacing:.005em}}
.mo{{font-family:'JetBrains Mono';font-weight:700;letter-spacing:.16em;text-transform:uppercase;font-size:22px}}
.se{{font-family:Fraunces;font-style:italic;font-weight:400}}
.ne{{color:{Y};font-weight:inherit;text-shadow:0 0 38px rgba(245,197,24,.55)}}
.yel .ne,.cre .ne{{text-shadow:none;background:{K};color:{Y};padding:.06em .12em 0;display:inline-block;line-height:.92;margin:.03em 0}}
.grao{{position:absolute;inset:0;pointer-events:none;opacity:.14;mix-blend-mode:overlay;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='220' height='220'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E")}}
.dk{{background:{K};color:#fff}}.yel{{background:{Y};color:{K}}}.cre{{background:{CR};color:{K}}}
.top{{position:absolute;left:64px;right:64px;top:56px;display:flex;justify-content:space-between;align-items:center}}
.bot{{position:absolute;left:64px;right:64px;bottom:48px;display:flex;justify-content:space-between;align-items:center;font-size:20px}}
.bot .mo{{font-size:18px}}.ia{{opacity:.6}}
.ln{{height:2px;background:currentColor;opacity:.5;flex:1;margin:0 22px}}
.phone{{position:absolute;width:430px;height:880px;border-radius:64px;background:#111;border:14px solid #1d1d1f;box-shadow:0 40px 90px rgba(0,0,0,.55),0 0 0 2px #333 inset;overflow:hidden}}
.phone .scr{{position:absolute;inset:0;background:#0f1416;padding:70px 26px 26px;display:flex;flex-direction:column;gap:16px}}
.bub{{max-width:86%;padding:16px 20px;border-radius:22px;font-size:21px;line-height:1.3;color:#fff;font-weight:600}}
.bub.me{{align-self:flex-end;background:#065e50}}.bub.ele{{align-self:flex-start;background:#202c33}}
.bub small{{display:block;font-size:14px;opacity:.6;text-align:right;margin-top:6px}}
.body{{font-size:34px;line-height:1.35;font-weight:600}}
.fr{{position:absolute;box-shadow:0 30px 70px rgba(0,0,0,.5);border-radius:18px;overflow:hidden;background:#222}}.fr img{{width:100%;height:100%;object-fit:cover;display:block}}
.chk i::after{{content:'✓';color:{Y}}}.yel .chk i::after{{color:{Y}}}.dk .chk i::after{{color:{K}}}.chk{{display:flex;gap:26px;align-items:flex-start;font-size:42px;font-weight:800;line-height:1.2}}.chk i{{flex:none;width:52px;height:52px;border:5px solid currentColor;border-radius:10px;display:flex;align-items:center;justify-content:center;font-style:normal;font-size:34px;background:currentColor}}
.pill{{display:inline-block;padding:10px 22px;border-radius:999px;border:2px solid currentColor}}
"""

def foto(n, x, top, H, glow=True, flip=False):
    """pessoa recortada, do busto para cima: H = altura do busto visível (topo da cabeça até a base do quadro)."""
    w, h = DIM[n]; th = H / F[n]; tw = th * w / h
    g = f'<div class="abs" style="left:{x+tw*.5-420}px;top:{top-40}px;width:840px;height:840px;border-radius:50%;background:radial-gradient(circle,rgba(245,197,24,.55),rgba(245,197,24,.12) 45%,transparent 70%);filter:blur(10px)"></div>' if glow else ''
    return g + f'<img class="abs" src="file://{REC}/lindson-{n}.png" style="left:{x}px;top:{top}px;width:{tw:.0f}px;{"transform:scaleX(-1);" if flip else ""}filter:drop-shadow(0 0 2px rgba(245,197,24,.0)) contrast(1.05) saturate(1.05)">'

def cena(n, cor):
    if cor != 'dk': return ''
    return f'<img class="abs" src="file://{ORIG}/lindson-{n}.jpg" style="inset:0;width:100%;height:100%;object-fit:cover;filter:blur(18px) brightness(.38) saturate(1.2);transform:scale(1.1)"><div class="abs" style="inset:0;background:linear-gradient(180deg,rgba(11,11,12,.2),rgba(11,11,12,.85) 78%)"></div>'

def moldura(top_l, top_r, pag, cor, ia):
    c = K if cor in ('yel', 'cre') else '#fff'
    t = f'<div class="top" style="color:{c}"><span class="mo">{e(top_l)}</span><span class="ln"></span><span class="mo">{e(top_r)}</span></div>'
    b = f'<div class="bot" style="color:{c}"><span class="mo">@lindsonalmeida_</span><span class="mo ia">{"imagem gerada por IA" if ia else ""}</span><span class="mo">{pag}</span></div>'
    return t + b

# ---------- layouts ----------
def L_capa(s, cor):  # pessoa à direita, manchete gigante embaixo à esquerda (Bugatti)
    n = s['foto']; x = s.get('x', 330)
    t = ''.join(f'<div>{neon(l)}</div>' for l in s['titulo'])
    fs = s.get('fs', 150)
    sub = f'<div class="body" style="font-size:32px;max-width:640px;margin-top:26px;opacity:.9">{e(s["sub"])}</div>' if s.get('sub') else ''
    fade = 'linear-gradient(0deg,rgba(11,11,12,.95) 8%,rgba(11,11,12,0) 52%)' if cor == 'dk' else 'linear-gradient(0deg,rgba(245,197,24,.98) 10%,rgba(245,197,24,0) 50%)'
    return cena(n, cor) + foto(n, x, s.get('top', 150), s.get('H', 1200), glow=(cor == 'dk')) + f'<div class="abs" style="inset:0;background:{fade}"></div><div class="abs an" style="left:64px;right:64px;bottom:120px;font-size:{fs}px">{t}{sub}</div>', True

def L_manchete(s, cor):  # palavra gigante translúcida atrás, pessoa no centro, manchete na faixa
    n = s['foto']
    bg = f'<div class="abs an" style="left:-30px;right:-30px;top:120px;font-size:{s.get("bfs",420)}px;text-align:center;opacity:{.16 if cor=="dk" else .2};color:{"#fff" if cor=="dk" else K};line-height:.82">{e(s["fundo"])}</div>'
    faixa = K if cor == 'yel' else Y; tc = Y if cor == 'yel' else K
    t = '<br>'.join(e(l) for l in s['titulo'])
    return (cena(n, cor) + bg + foto(n, s.get('x', 250), s.get('top', 190), s.get('H', 1000), glow=(cor == 'dk')) +
            f'<div class="abs an" style="left:0;right:0;bottom:110px;background:{faixa};color:{tc};padding:34px 64px 30px;font-size:{s.get("fs",104)}px;transform:rotate(-2deg) scale(1.04)">{t}</div>'), True

def L_num(s, cor):
    return (f'<div class="abs an" style="left:40px;top:130px;font-size:520px;color:transparent;-webkit-text-stroke:4px {Y if cor=="dk" else K};opacity:.9;line-height:.85">{e(s["n"])}</div>'
            f'<div class="abs" style="left:64px;right:64px;top:640px"><div class="an" style="font-size:96px">{neon(s["t"])}</div><div class="body" style="margin-top:34px;opacity:.88">{e(s["b"])}</div></div>'), False

def L_card(s, cor):  # cartão claro com mono + imagem/mockup ao lado
    img = s.get('img'); mock = s.get('mock')
    vis = f'<div class="fr" style="right:64px;top:200px;width:420px;height:{s.get("ih",525)}px;transform:rotate(3deg)"><img src="{src(img)}"></div>' if img else ''
    if mock: vis = phone(mock, 600, 190, .86)
    return (vis + f'<div class="abs" style="left:64px;top:200px;width:{460 if (img or mock) else 950}px"><div class="mo" style="opacity:.6">{e(s.get("k",""))}</div><div class="an" style="font-size:88px;margin-top:22px">{neon(s["t"])}</div></div>'
            f'<div class="abs" style="left:64px;right:64px;bottom:130px;background:#fff;color:{K};border-radius:28px;padding:44px 48px;box-shadow:0 20px 60px rgba(0,0,0,.15)"><div class="body">{e(s["b"])}</div></div>'), False

def phone(m, x, y, sc=1.0, rot=-4):
    bs = ''.join(f'<div class="bub {w}">{e(t)}<small>{h}</small></div>' for w, t, h in m.get('chat', []))
    head = f'<div style="color:#fff;font-weight:800;font-size:22px;padding-bottom:14px;border-bottom:1px solid #2a3439">{e(m.get("nome",""))}</div>'
    extra = m.get('html', '')
    return f'<div class="phone" style="left:{x}px;top:{y}px;transform:rotate({rot}deg) scale({sc});transform-origin:top left"><div class="scr">{head}{bs}{extra}</div></div>'

def L_chat(s, cor):
    return (phone(s['mock'], 560, 210, .95, 4) + f'<div class="abs" style="left:64px;top:210px;width:470px"><div class="mo" style="opacity:.6">{e(s.get("k",""))}</div><div class="an" style="font-size:92px;margin-top:22px">{neon(s["t"])}</div><div class="body" style="margin-top:34px;font-size:30px;opacity:.88">{e(s["b"])}</div></div>'), False

def L_xy(s, cor):
    a, b = s['x'], s['y']
    return (f'<div class="abs" style="left:0;right:0;top:150px;height:560px;background:#1b1b1d;color:#bbb;padding:70px 64px"><div class="mo" style="color:#ff5a4f">{e(s.get("kx","ERRADO"))}</div><div class="an" style="font-size:84px;margin-top:24px;text-decoration:line-through;text-decoration-thickness:6px;text-decoration-color:#ff5a4f;color:#fff">{e(a)}</div><div class="body" style="margin-top:22px;font-size:30px">{e(s.get("bx",""))}</div></div>'
            f'<div class="abs" style="left:0;right:0;top:710px;height:520px;background:{Y};color:{K};padding:70px 64px"><div class="mo">{e(s.get("ky","CERTO"))}</div><div class="an" style="font-size:84px;margin-top:24px">{e(b)}</div><div class="body" style="margin-top:22px;font-size:30px">{e(s.get("by",""))}</div></div>'), False

def L_lista(s, cor):
    it = ''.join(f'<div class="chk"><i></i><span>{e(x)}</span></div>' for x in s['itens'])
    return (f'<div class="abs" style="left:64px;right:64px;top:180px"><div class="mo">{e(s.get("k",""))}</div><div class="an" style="font-size:100px;margin-top:22px">{neon(s["t"])}</div></div>'
            f'<div class="abs" style="left:64px;right:64px;top:{s.get("ly",520)}px;display:flex;flex-direction:column;gap:34px">{it}</div>'), False

def L_img(s, cor):  # imagens reais de cliente em molduras inclinadas
    ims = s['imgs']; out = ''
    pos = {1: [(250, 170, 580, 725, -3)], 2: [(90, 190, 440, 550, -5), (550, 250, 440, 550, 4)],
           3: [(60, 230, 330, 586, -6), (375, 180, 330, 586, 0), (690, 230, 330, 586, 6)]}[len(ims)]
    if s.get('vert'): pos = {3: [(70, 170, 300, 533, -5), (390, 140, 300, 533, 0), (710, 170, 300, 533, 5)], 2: [(130, 160, 360, 640, -4), (590, 190, 360, 640, 4)]}[len(ims)]
    for (x, y, w, h, r), im in zip(pos, ims):
        out += f'<div class="fr" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;transform:rotate({r}deg)"><img src="{src(im)}"></div>'
    return out + f'<div class="abs" style="left:64px;right:64px;bottom:120px"><div class="mo" style="opacity:.7">{e(s.get("k",""))}</div><div class="an" style="font-size:{s.get("fs",92)}px;margin-top:18px">{neon(s["t"])}</div><div class="body" style="margin-top:20px;font-size:30px;opacity:.88">{e(s.get("b",""))}</div></div>', False

def L_cta(s, cor):
    return (phone(s['mock'], 610, 300, .82, 6) + f'<div class="abs" style="left:64px;top:220px;width:560px"><div class="mo">{e(s.get("k","SUA VEZ"))}</div><div class="an" style="font-size:132px;margin-top:22px">{neon(s["t"])}</div><div class="body" style="margin-top:34px;font-size:32px">{e(s["b"])}</div><div class="pill mo" style="margin-top:40px;font-size:20px">{e(s.get("bt","comenta aqui embaixo"))}</div></div>'), False

def L_dividida(s, cor):
    a, b = s['antes'], s['depois']
    def lado(x, d, lab, cc):
        im = f'<img src="{src(d["img"])}" style="width:100%;height:100%;object-fit:{d.get("fit","cover")};object-position:top;display:block;background:#1b1b1d">' if d.get('img') else phone(d['mock'], 40, 30, .62, 0)
        return f'<div class="abs" style="left:{x}px;top:150px;width:540px;height:860px;overflow:hidden;background:#1b1b1d">{im}<div class="abs mo" style="left:24px;top:24px;background:{cc};color:{K if cc==Y else "#fff"};padding:10px 18px;font-size:22px">{lab}</div></div>'
    return (lado(0, a, 'ANTES', '#ff5a4f') + lado(540, b, 'DEPOIS', Y) + f'<div class="abs" style="left:532px;top:150px;width:16px;height:860px;background:{K}"></div>'
            f'<div class="abs" style="left:64px;right:64px;top:1040px"><div class="an" style="font-size:{s.get("fs",76)}px">{neon(s["t"])}</div><div class="body" style="font-size:28px;margin-top:14px;opacity:.88">{e(s.get("b",""))}</div></div>'), False

def L_frase(s, cor):  # editorial (Gomes & Moura): serifa itálica, palavra translúcida, rótulo pequeno
    n = s.get('foto'); fc = '#fff' if cor == 'dk' else K; ac = Y if cor == 'dk' else K
    fundo = f'<div class="abs an" style="left:-20px;top:110px;font-size:330px;opacity:.1;color:{fc};white-space:nowrap">{e(s["fundo"])}</div>'
    if n:
        grad = "rgba(11,11,12,.97)" if cor == "dk" else "rgba(245,197,24,.98)"
        return (cena(n, cor) + fundo + foto(n, s.get('x', 470), s.get('top', 300), s.get('H', 1050), glow=(cor == 'dk')) +
                f'<div class="abs" style="left:0;right:0;bottom:0;height:640px;background:linear-gradient(0deg,{grad} 50%,transparent)"></div>'
                f'<div class="abs" style="left:64px;right:64px;bottom:130px"><div class="mo" style="opacity:.7;font-size:18px">PAPO DE DONO · {e(s["n"])}</div>'
                f'<div class="se" style="font-size:{s.get("fs",64)}px;line-height:1.12;margin-top:24px">“{neon(s["q"])}”</div>'
                f'<div class="mo" style="margin-top:26px;font-size:18px;color:{ac}">{e(s["autor"])}</div></div>'), True
    nota = {'nome': 'Notas', 'html': f'<div class="se" style="color:#fff;font-size:40px;line-height:1.2;margin-top:30px">“{e(s["q"])}”</div><div class="mo" style="color:{Y};font-size:15px;margin-top:30px;letter-spacing:.1em">{e(s["autor"])}</div>'}
    return (fundo + phone(nota, 620, 260, .88, 5) +
            f'<div class="abs" style="left:64px;width:520px;top:300px"><div class="mo" style="opacity:.7;font-size:18px">PAPO DE DONO · {e(s["n"])}</div>'
            f'<div class="an" style="font-size:96px;margin-top:24px">{neon(s["t"])}</div>'
            f'<div class="body" style="margin-top:30px;font-size:30px">{e(s["na"])}</div></div>'), False

LAY = dict(capa=L_capa, manchete=L_manchete, num=L_num, card=L_card, chat=L_chat, xy=L_xy, lista=L_lista, img=L_img, cta=L_cta, dividida=L_dividida, frase=L_frase)

def pagina(s, cor, pag, top_l, top_r):
    inner, ia = LAY[s['l']](s, cor)
    ia = ia or s.get('ia', False)
    return f'''<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Anton&family=Fraunces:ital,wght@1,400;1,600&family=JetBrains+Mono:wght@500;700&family=Manrope:wght@600;800&display=swap" rel="stylesheet"><style>{CSS}</style></head>
<body><div class="a {cor}">{inner}{moldura(top_l, top_r, pag, cor, ia)}<div class="grao"></div></div></body></html>'''

def main(sel):
    from PIL import Image
    for f in os.listdir(REC):
        if f.endswith('.png'): DIM[f[8:10]] = Image.open(os.path.join(REC, f)).size
    tmp = os.path.join(REC, '_p.html')
    with sync_playwright() as pw:
        br = pw.chromium.launch(); pg = br.new_page(viewport={'width': 1080, 'height': 1350})
        for i, pid in enumerate(ORDEM):
            P = POSTS[pid]
            if sel and pid not in sel: continue
            cor0 = 'dk' if i % 2 == 0 else 'yel'
            d = os.path.join(OUT, P['linha'], P['nn']); os.makedirs(d, exist_ok=True)
            prev = None
            for j, s in enumerate(P['telas']):
                nxt = None
                opp = 'yel' if cor0 == 'dk' else 'dk'
                cor = cor0 if j == 0 else (s.get('cor') or (opp if j % 2 else cor0))
                if j and cor == prev: cor = [c for c in ('dk', 'yel', 'cre') if c != prev and c != (nxt or '')][0]
                prev = cor
                pag = f'{j+1:02d}/{len(P["telas"]):02d}' if len(P['telas']) > 1 else ''
                open(tmp, 'w').write(pagina(s, cor, pag, P['rotulo'], P.get('rotr', 'SÃO LUÍS · MA')))
                pg.goto('file://' + tmp); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(250)
                pg.screenshot(path=os.path.join(d, f'{j+1:02d}.png'))
            print('ok', pid)
        br.close()

if __name__ == '__main__':
    main(sys.argv[1:])
