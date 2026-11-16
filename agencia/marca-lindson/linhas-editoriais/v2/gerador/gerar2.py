# Linhas editoriais v2 da marca Lindson (conta Leandro, 16/11/2026). Mesmas pautas da v1 (conteudo.py), visual refeito.
# Referências (v2/TEMPLATE.md): R1 "Solaris Runway" (0xOVERFLOWX, Dribbble) = retrato em cena + manchete condensada gigante
# cruzando a foto; R2 "A4 Trends Poster" (Matthieu Martigny, França) = palavra gigante vertical na cor de destaque colada ao retrato;
# R3 "No Limits" (Ahmed Elshaer, Dribbble) = palavra gigante ATRÁS da pessoa recortada. + aprovadas 16/11: Denis Bugatti (luz de
# cinema, 1 palavra neon) e Gomes & Moura (serifa itálica editorial, rótulos pequenos). Sem celular desenhado, sem ícones, sem cartões.
import os, sys, re, html
from conteudo import POSTS, ORDEM
from playwright.sync_api import sync_playwright
from PIL import Image
B = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.dirname(B)
REC = os.environ.get('REC', '/tmp/claude-0/-home-user/b9464785-a028-5189-b9f0-a7ed9d7dd59e/scratchpad/rec')
ORIG = '/home/user/centrallindsonalmeida/painel/fotos-lindson/escolhidas-2026-11-16'
AG = '/home/user/lindson/agencia'
F = {'01': .8, '02': .7, '03': .85, '04': .5, '05': .5, '06': .62, '07': .6, '08': 1.0, '09': .75, '10': .8,
     '11': .38, '12': .42, '13': .45, '14': .36, '15': .5, '16': .55}
DIM = {}
Y, K = '#F5C518', '#0A0A0B'
# pautas que ficam fora da v2 por falta de foto boa (sem foto do Lindson nem trabalho real de cliente): travadas até chegar lote novo
FORA = ['e4', 'r4', 'a4', 'f4', 'p3', 'p4', 'd2', 'd4']
ORD2 = [p for p in ORDEM if p not in FORA]

def e(s): return html.escape(s or '', quote=False)
def ne(t): return re.sub(r'\*(.+?)\*', r'<b class="ne">\1</b>', e(t))
def plain(t): return re.sub(r'\*', '', t or '')
def src(p): return 'file://' + (p if p.startswith('/') else AG + '/' + p)

CSS = f"""*{{margin:0;padding:0;box-sizing:border-box}}body{{width:1080px;height:1350px;overflow:hidden;background:{K};font-family:Manrope;-webkit-font-smoothing:antialiased;color:#fff}}
.a{{position:relative;width:1080px;height:1350px;overflow:hidden;background:{K}}}.abs{{position:absolute}}
.an{{font-family:Anton;text-transform:uppercase;line-height:.86;letter-spacing:-.005em}}
.mo{{font-family:'JetBrains Mono';font-weight:500;letter-spacing:.22em;text-transform:uppercase;font-size:17px}}
.se{{font-family:Fraunces;font-style:italic;font-weight:300}}
.ne{{color:{Y};font-weight:inherit;text-shadow:0 0 40px rgba(245,197,24,.45)}}
.bd{{font-size:30px;line-height:1.42;font-weight:500;color:rgba(255,255,255,.82)}}
.grao{{position:absolute;inset:0;pointer-events:none;opacity:.16;mix-blend-mode:overlay;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='220' height='220'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E")}}
.vin{{position:absolute;inset:0;pointer-events:none;background:radial-gradient(ellipse at 55% 40%,transparent 45%,rgba(0,0,0,.55) 100%)}}
.top,.bot{{position:absolute;left:60px;right:60px;display:flex;justify-content:space-between;align-items:center}}.top{{top:52px}}.bot{{bottom:46px}}
.rule{{height:1px;background:currentColor;opacity:.35;flex:1;margin:0 24px}}
"""
def grade(n, pos='50% 30%', scale=1.0, bri=.55, sat=1.15, bw=False, blur=0):
    f = f'brightness({bri}) contrast(1.12) saturate({0 if bw else sat}) sepia({0 if bw else .18})' + (f' blur({blur}px)' if blur else '')
    return f'<img class="abs" src="file://{ORIG}/lindson-{n}.jpg" style="inset:0;width:100%;height:100%;object-fit:cover;object-position:{pos};transform:scale({scale});filter:{f}">'
def corte(n, x, top, H, flip=False, sh=True):
    w, h = DIM[n]; th = H / F[n]; tw = th * w / h
    return (f'<img class="abs" src="file://{REC}/lindson-{n}.png" style="left:{x}px;top:{top}px;width:{tw:.0f}px;{"transform:scaleX(-1);" if flip else ""}'
            f'filter:contrast(1.08) saturate(1.08) {"drop-shadow(-30px 0 60px rgba(0,0,0,.6))" if sh else ""}">')
def luz(x, y, r=900, a=.35):
    return f'<div class="abs" style="left:{x-r//2}px;top:{y-r//2}px;width:{r}px;height:{r}px;border-radius:50%;background:radial-gradient(circle,rgba(245,170,40,{a}),transparent 65%)"></div>'
def moldura(L, R, pag, ia):
    return (f'<div class="top"><span class="mo">{e(L)}</span><span class="rule"></span><span class="mo">{e(R)}</span></div>'
            f'<div class="bot"><span class="mo">@lindsonalmeida_</span><span class="mo" style="opacity:.55">{"imagem gerada por IA" if ia else ""}</span><span class="mo">{pag}</span></div>')
def tit(s):
    if s.get('titulo'): return s['titulo']
    return [s.get('t', '')]

# ---- composições ----
def C_capa(s, n, v):  # R3 + R1: palavra gigante atrás do recorte, manchete embaixo
    linhas = tit(s); big = max((plain(w).strip('.,?!') for l in linhas for w in l.split()), key=len)
    bfs = min(520, int(1900 / max(4, len(big))))
    x = s.get('x', 300)
    return (grade(n, bri=.42, blur=6, scale=1.1) + luz(x + 330, 420) +
            f'<div class="abs an" style="left:0;right:0;top:170px;text-align:center;font-size:{bfs}px;color:{Y};opacity:.92;white-space:nowrap">{e(big)}</div>' +
            corte(n, x, s.get('top', 210), s.get('H', 1150)) +
            '<div class="abs" style="inset:0;background:linear-gradient(0deg,rgba(10,10,11,.96) 6%,rgba(10,10,11,0) 46%)"></div>' +
            f'<div class="abs an" style="left:60px;right:60px;bottom:116px;font-size:{min(118, s.get("fs",130)*0.8):.0f}px">' + '<br>'.join(ne(l) for l in linhas) + '</div>' +
            (f'<div class="abs bd" style="left:60px;right:300px;bottom:118px;display:none"></div>'))
def C_vert(s, n, v):  # R2: palavra vertical gigante amarela colada ao retrato
    linhas = tit(s); word = max((plain(w) for l in linhas for w in l.split()), key=len).strip('.,?!')
    return (grade(n, bri=.3, blur=10, scale=1.15) +
            f'<div class="abs an" style="left:-40px;top:1350px;transform-origin:0 0;transform:rotate(-90deg);font-size:{min(400, int(2600/max(5,len(word))))}px;color:{Y};white-space:nowrap;line-height:.8">{e(word)}</div>' +
            corte(n, 360, 190, 1160) + '<div class="abs" style="left:0;right:0;bottom:0;height:520px;background:linear-gradient(0deg,rgba(10,10,11,.97) 30%,transparent)"></div>' +
            f'<div class="abs an" style="left:400px;right:60px;bottom:120px;font-size:84px">' + '<br>'.join(ne(l) for l in linhas) + '</div>')
def C_close(s, n, v):  # R1: close da cena (rosto) + manchete cruzando
    pos = ['70% 20%', '30% 25%', '60% 35%'][v % 3]
    return (grade(n, pos=pos, scale=1.6, bri=.5) + '<div class="abs" style="inset:0;background:linear-gradient(90deg,rgba(10,10,11,.92) 30%,rgba(10,10,11,.1) 80%)"></div>' +
            f'<div class="abs" style="left:60px;width:640px;top:250px"><div class="mo" style="color:{Y}">{e(s.get("k",""))}</div>'
            f'<div class="an" style="font-size:112px;margin-top:30px">{ne(s.get("t",""))}</div>'
            f'<div style="width:80px;height:2px;background:{Y};margin:44px 0 34px"></div><div class="bd">{e(s.get("b",""))}</div></div>')
def C_num(s, n, v):  # número gigante em contorno atrás do recorte (R3)
    return (grade(n, bri=.3, blur=12, scale=1.2) + luz(760, 500, 1000, .3) +
            f'<div class="abs an" style="right:40px;top:120px;font-size:900px;color:transparent;-webkit-text-stroke:3px {Y};line-height:.8">{e(s["n"])}</div>' +
            corte(n, 470, 300, 1050, flip=True) + '<div class="abs" style="inset:0;background:linear-gradient(90deg,rgba(10,10,11,.95) 25%,transparent 65%)"></div>' +
            f'<div class="abs" style="left:60px;width:560px;bottom:150px"><div class="an" style="font-size:96px">{ne(s["t"])}</div><div class="bd" style="margin-top:32px">{e(s["b"])}</div></div>')
def C_xy(s, n, v):  # foto dividida: P&B (como está) x cor (como fica)
    return (f'<div class="abs" style="left:0;top:0;width:540px;height:1350px;overflow:hidden">{grade(n, pos="40% 30%", scale=1.3, bw=True, bri=.38)}</div>'
            f'<div class="abs" style="left:540px;top:0;width:540px;height:1350px;overflow:hidden">{grade(n, pos="60% 30%", scale=1.3, bri=.6)}</div>'
            f'<div class="abs" style="left:539px;top:0;width:2px;height:1350px;background:{Y}"></div>'
            '<div class="abs" style="inset:0;background:linear-gradient(0deg,rgba(10,10,11,.95) 10%,transparent 60%)"></div>'
            f'<div class="abs" style="left:60px;width:440px;bottom:140px"><div class="mo" style="opacity:.6">{e(s.get("kx",""))}</div><div class="an" style="font-size:66px;margin-top:20px;opacity:.55;text-decoration:line-through;text-decoration-thickness:4px">{e(s["x"])}</div><div class="bd" style="font-size:24px;margin-top:20px">{e(s.get("bx",""))}</div></div>'
            f'<div class="abs" style="left:600px;width:420px;bottom:140px"><div class="mo" style="color:{Y}">{e(s.get("ky",""))}</div><div class="an" style="font-size:66px;margin-top:20px;color:{Y}">{e(s["y"])}</div><div class="bd" style="font-size:24px;margin-top:20px">{e(s.get("by",""))}</div></div>')
def C_lista(s, n, v):  # editorial (Gomes & Moura): foto à direita, lista numerada com fios finos
    it = ''.join(f'<div style="display:flex;gap:28px;align-items:baseline;padding:26px 0;border-top:1px solid rgba(255,255,255,.22)"><span class="mo" style="color:{Y}">{i+1:02d}</span><span style="font-size:34px;font-weight:700;line-height:1.2">{e(x)}</span></div>' for i, x in enumerate(s['itens']))
    return (f'<div class="abs" style="left:540px;top:0;width:540px;height:1350px;overflow:hidden">{grade(n, pos="55% 25%", scale=1.25, bri=.62)}</div>'
            '<div class="abs" style="left:420px;top:0;width:300px;height:1350px;background:linear-gradient(90deg,#0A0A0B,transparent)"></div>'
            f'<div class="abs" style="left:60px;width:560px;top:200px"><div class="mo" style="color:{Y}">{e(s.get("k",""))}</div><div class="an" style="font-size:104px;margin:28px 0 50px">{ne(s["t"])}</div>{it}</div>')
def C_img(s, n, v):  # trabalho real de cliente, grande, sobre a cena desfocada
    ims = s['imgs']; k = len(ims); w = {1: 640, 2: 430, 3: 300}[k]; h = int(w * (16/9 if s.get('vert') else 1.25)); h = min(h, 760)
    gap = 30; x0 = (1080 - (k*w + (k-1)*gap)) // 2
    fr = ''.join(f'<img class="abs" src="{src(im)}" style="left:{x0+i*(w+gap)}px;top:{170 + (0 if i%2==0 else 40)}px;width:{w}px;height:{h}px;object-fit:cover;object-position:top;box-shadow:0 40px 80px rgba(0,0,0,.7)">' for i, im in enumerate(ims))
    bg = grade(n, bri=.28, blur=16, scale=1.2) if n else f'<img class="abs" src="{src(ims[0])}" style="inset:0;width:100%;height:100%;object-fit:cover;filter:blur(30px) brightness(.3);transform:scale(1.2)">'
    return (bg + fr + '<div class="abs" style="left:0;right:0;bottom:0;height:520px;background:linear-gradient(0deg,#0A0A0B 45%,transparent)"></div>'
            f'<div class="abs" style="left:60px;right:60px;bottom:130px"><div class="mo" style="color:{Y}">{e(s.get("k",""))}</div><div class="an" style="font-size:{s.get("fs",88)}px;margin-top:22px">{ne(s["t"])}</div><div class="bd" style="margin-top:22px;font-size:27px">{e(s.get("b",""))}</div></div>')
def tarja(t): return re.sub(r'\*(.+?)\*', lambda m: '<span style="background:#0A0A0B;color:#F5C518;padding:0 .1em">' + m.group(1) + '</span>', e(t))
def C_cta(s, n, v):  # fechamento amarelo com recorte (Bugatti) e botão de contorno fino
    return (f'<div class="abs" style="inset:0;background:{Y}"></div>' +
            f'<div class="abs an" style="left:-10px;top:120px;font-size:430px;color:rgba(10,10,11,.08);white-space:nowrap">{e(plain(s["t"]).split()[-1])}</div>' +
            corte(n, 420, 240, 1100) +
            f'<div class="abs" style="left:60px;width:520px;top:330px;color:{K}"><div class="an" style="font-size:124px">{tarja(s["t"])}</div>'
            f'<div style="font-size:31px;line-height:1.4;font-weight:600;margin-top:36px">{e(s.get("b",""))}</div>'
            f'<div class="mo" style="display:inline-block;margin-top:44px;border:2px solid {K};padding:18px 30px;font-size:18px">{e(s.get("bt","comenta aqui embaixo"))} →</div></div>')
def C_manchete(s, n, v):  # R3: palavra gigante atrás + manchete
    return (grade(n, bri=.4, blur=6, scale=1.1) + luz(560, 520) +
            f'<div class="abs an" style="left:0;right:0;top:150px;text-align:center;font-size:{int(1900/max(4,len(s["fundo"])))}px;color:{Y};white-space:nowrap">{e(s["fundo"])}</div>' +
            corte(n, s.get('x', 270), 230, 1080) + '<div class="abs" style="inset:0;background:linear-gradient(0deg,rgba(10,10,11,.97) 8%,transparent 42%)"></div>' +
            f'<div class="abs an" style="left:60px;right:60px;bottom:120px;font-size:112px">' + '<br>'.join(ne(l) for l in s['titulo']) + '</div>')
def C_frase(s, n, v):  # Gomes & Moura: cena inteira com luz dourada, serifa itálica
    return (grade(n, pos='50% 30%', bri=.62, sat=1.05) + '<div class="abs" style="inset:0;background:linear-gradient(0deg,rgba(10,10,11,.97) 30%,transparent 70%)"></div>' +
            f'<div class="abs an" style="left:-10px;top:110px;font-size:300px;color:rgba(255,255,255,.1);white-space:nowrap">{e(s["fundo"])}</div>' +
            f'<div class="abs" style="left:60px;right:60px;bottom:130px"><div class="mo" style="color:{Y}">Papo de dono · {e(s["n"])}</div>'
            f'<div class="se" style="font-size:76px;line-height:1.08;margin-top:30px">“{ne(s["q"])}”</div><div style="width:80px;height:2px;background:{Y};margin:36px 0 22px"></div><div class="mo" style="opacity:.75">{e(s["autor"])}</div></div>')
def C_dividida(s, n, v):
    a, b = s['antes'], s['depois']
    side = lambda x, d, lab, c: f'<div class="abs" style="left:{x}px;top:0;width:540px;height:1000px;overflow:hidden;background:#151517"><img src="{src(d["img"])}" style="width:100%;height:100%;object-fit:cover;object-position:top;{"filter:grayscale(1) brightness(.7)" if lab=="ANTES" else ""}"><div class="abs mo" style="left:30px;top:120px;color:{c}">{lab}</div></div>'
    return (side(0, a, 'ANTES', '#fff') + side(540, b, 'DEPOIS', Y) + f'<div class="abs" style="left:539px;top:0;width:2px;height:1000px;background:{Y}"></div>'
            '<div class="abs" style="left:0;right:0;top:760px;height:240px;background:linear-gradient(0deg,#0A0A0B,transparent)"></div>'
            f'<div class="abs" style="left:60px;right:60px;top:1010px"><div class="an" style="font-size:86px">{ne(s["t"])}</div><div class="bd" style="font-size:26px;margin-top:18px">{e(s.get("b",""))}</div></div>')

def escolher(s, j, v):
    l = s['l']
    if j == 0 and l == 'capa': return C_vert if v % 3 == 2 else C_capa
    return {'capa': C_capa, 'manchete': C_manchete, 'num': C_num, 'card': C_close, 'chat': C_close, 'xy': C_xy, 'lista': C_lista,
            'img': C_img, 'cta': C_cta, 'frase': C_frase, 'dividida': C_dividida}[l]

def pagina(inner, L, R, pag, ia):
    return (f'<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Anton&family=Fraunces:ital,wght@1,300;1,400&family=JetBrains+Mono:wght@500&family=Manrope:wght@500;600;700&display=swap" rel="stylesheet"><style>{CSS}</style></head>'
            f'<body><div class="a">{inner}<div class="vin"></div>{moldura(L, R, pag, ia)}<div class="grao"></div></div></body></html>')

def main(sel):
    for f in os.listdir(REC):
        if f.endswith('.png'): DIM[f[8:10]] = Image.open(os.path.join(REC, f)).size
    tmp = os.path.join(REC, '_v2.html')
    with sync_playwright() as pw:
        br = pw.chromium.launch(); pg = br.new_page(viewport={'width': 1080, 'height': 1350})
        for v, pid in enumerate(ORD2):
            if sel and pid not in sel: continue
            P = POSTS[pid]; fotos = [s['foto'] for s in P['telas'] if s.get('foto')]; n = fotos[0] if fotos else None
            d = os.path.join(OUT, P['linha'], P['nn']); os.makedirs(d, exist_ok=True)
            for j, s in enumerate(P['telas']):
                fn = escolher(s, j, v)
                if n is None and fn not in (C_img, C_dividida): raise SystemExit(f'{pid}: tela sem foto')
                pag = f'{j+1:02d}/{len(P["telas"]):02d}' if len(P['telas']) > 1 else ''
                open(tmp, 'w').write(pagina(fn(s, n, v + j), P['rotulo'], 'São Luís · MA', pag, n is not None))
                pg.goto('file://' + tmp); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(300)
                pg.screenshot(path=os.path.join(d, f'v2-{j+1:02d}.jpg'), type='jpeg', quality=88)
            print('ok', pid)
        br.close()

if __name__ == '__main__':
    main(sys.argv[1:])
