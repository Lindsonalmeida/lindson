# Desentupidora SF · motion-sf-14-11: 5 criativos de anúncio em motion (9:16) · conta Zuleide · 14/11/2026
# Pedido do Lindson: "faça 5 criativos em motion para a SF desentupidora. vaso, ralo, caixa de gordura" + "crie os melhores motions que você puder".
# Motor: cenas em HTML com render(t) (base: wf-celulares/motion-02, conta Leandro), elevado com:
#  - tipografia cinética sincronizada à voz (cada palavra entra no tempo exato da fala, edge-tts WordBoundary)  #41
#  - câmera 2.5D: foto ao fundo, letra gigante no meio, técnico recortado na frente, cada camada numa velocidade  #25
#  - transição com motion blur (entrada com deslocamento + desfoque direcional + tmix no ffmpeg) e flash  #163 #169
#  - corte a cada 1 a 2 s, sincronizado à fala, com "punch-in" nas palavras fortes  #166
#  - VFX: anéis de água, redemoinho no ralo, onda de cheiro (feTurbulence), light leak, grão, vinheta, tremor  #152 #35
# Referências (TEMPLATE.md): A Sterling Plumbers/PMG (EUA) · B Drainpro/SBM (Austrália) · C Liquid-Plumr "Destroy annoying clogs" (EUA/NZ).
# Identidade SF: marinho #061a4a/#0a2a6e, royal #1d5fd0, céu #3fa9ff, laranja #ff8a00/#ff6a00, Montserrat 900 itálico caixa alta.
# Promessas: só as do site (orçamento grátis por foto/vídeo, sem quebra-quebra na maioria dos casos, cabo rotativo,
# técnico uniformizado, teste na hora, agendamento no mesmo dia conforme a agenda). Sem preço.
import os, json, html
D = os.path.dirname(os.path.abspath(__file__))
R = {r['n']: r for r in json.load(open(os.path.join(D, 'roteiros.json')))}
NUM = '(98) 98915-3929'; ARROBA = '@desentupidorasf_slz'
NAVY, NAVY2, ROYAL, CEU, LAR, LAR2 = '#061a4a', '#0a2a6e', '#1d5fd0', '#3fa9ff', '#ff8a00', '#ff6a00'
F = 'fotos/'

def W(n):  # tempos das palavras da voz
    return [p[1] for p in json.load(open(os.path.join(D, 'voz', f'{n}.json')))['palavras']]

# ---------- cenas ----------
# cada cena: dict(t=início, bg=cor|None, foto=arquivo, pos, z=(zoom ini, fim), pan=(x,y) px/s, spin=graus/s, escuro=0..1,
#   linhas=[(texto, palavra_índice|tempo, estilo)], rec=recorte, gigante=texto atrás do recorte, chips=[(txt, t)],
#   vfx=[...], cap=legenda palavra a palavra, punch=[tempos], nota=rodapé)
def cenas(n):
    w = W(n); T = lambda i: w[i]
    if n == 1:  # VASO · palavra gigante + 2.5D (ref. A Sterling: o objeto enorme, perto da câmera)
        return [
         dict(t=0, foto='7622581.jpg', pos='50% 40%', z=(1.25, 1.55), pan=(0, -14), escuro=.55, cap=0,
              linhas=[('DEU DESCARGA', 0, 'm'), ('E A ÁGUA', 2, 'm'), ('SUBIU?', 5, 'xg laranja')], punch=[T(5)], vfx=['agua']),
         dict(t=T(6) - .08, bg=ROYAL, linhas=[('CALMA.', 6, 'xg')], vfx=['aneis'], punch=[T(6) + .5]),
         dict(t=T(7) - .08, bg=NAVY, linhas=[('NÃO TENTA', 7, 'g'), ('RESOLVER', 9, 'g ceu'), ('NA FORÇA.', 11, 'g risco')]),
         dict(t=T(12) - .08, foto='32588556.jpg', pos='50% 30%', z=(1.6, 1.75), pan=(-10, 0), escuro=.7, desfoque=8,
              gigante='SF', rec='32588556-rec.png', recpos=(560, 520, 1180), chips=[('DESENTOPE VASO SANITÁRIO', T(14))]),
         dict(t=T(17) - .08, foto='4239015.jpg', pos='50% 60%', z=(1.25, 1.55), spin=40, escuro=.5, cap=1,
              linhas=[('CABO', 20, 'g'), ('ROTATIVO', 21, 'g laranja')], vfx=['redemoinho'], punch=[T(21)]),
         dict(t=T(22) - .08, bg=LAR2, linhas=[('SEM', 22, 'g escuro'), ('QUEBRA-', 23, 'xg branco'), ('QUEBRA', 23.5, 'xg branco')],
              nota=('na maioria dos casos', T(24)), vfx=['rachadura']),
         dict(t=T(28) - .1, cta='MANDA UMA FOTO', ctasub='e recebe o orçamento grátis'),
        ]
    if n == 2:  # VASO · lista de 3 sinais (ref. B Drainpro: tipo gigante no ritmo + C: problema numerado)
        return [
         dict(t=0, foto='7545637.jpg', pos='30% 50%', z=(1.35, 1.6), pan=(-18, 0), escuro=.35, cap=0,
              linhas=[('VASO', 0, 'xg'), ('ENTUPIDO', 1, 'g'), ('E VISITA CHEGANDO?', 3, 'm tarja')], punch=[T(3)]),
         dict(t=T(5) - .08, bg=ROYAL, numero='3', linhas=[('OLHA OS', 5, 'g'), ('3 SINAIS', 7, 'xg laranja')], punch=[T(7)]),
         dict(t=T(9) - .08, foto='7545637.jpg', pos='80% 60%', z=(2.2, 2.5), pan=(12, 8), escuro=.55, numero='01', tilt=1, cap=1,
              linhas=[('A ÁGUA', 9, 'g'), ('DEMORA', 11, 'g laranja'), ('PRA DESCER', 13, 'm')], vfx=['gotas']),
         dict(t=T(14) - .08, bg=NAVY, numero='02', linhas=[('FAZ', 14, 'g'), ('BARULHO', 15, 'xg ceu tremor')], vfx=['ondas']),
         dict(t=T(16) - .08, foto='9736334.jpg', pos='50% 60%', z=(1.3, 1.5), pan=(0, -12), escuro=.5, numero='03', cap=1,
              linhas=[('E VOLTA', 16, 'g'), ('COM CHEIRO', 19, 'g laranja cheiro')], vfx=['cheiro']),
         dict(t=T(20) - .08, bg=NAVY2, linhas=[('TÉCNICO', 20, 'g'), ('UNIFORMIZADO', 21, 'g ceu')], chips=[('✓ TESTE NA HORA', T(22))], vfx=['grade']),
         dict(t=T(25) - .08, bg=LAR2, linhas=[('AGENDAMENTO', 26, 'g branco'), ('NO MESMO DIA', 27, 'g escuro')],
              nota=('conforme a agenda', T(30)), vfx=['relogio']),
         dict(t=T(33) - .1, cta='CHAMA A SF', ctasub='orçamento grátis por foto ou vídeo'),
        ]
    if n == 3:  # RALO · tipo gigante sobre o ralo visto de cima (ref. B Drainpro)
        return [
         dict(t=0, foto='5768318.jpg', pos='50% 50%', z=(1.15, 1.7), spin=-6, escuro=.4, cap=0,
              linhas=[('ÁGUA', 0, 'xg'), ('PARADA', 1, 'xg'), ('NO BOX?', 3, 'g laranja')], vfx=['agua'], punch=[T(3)]),
         dict(t=T(4) - .08, bg=NAVY, linhas=[('CABELO', 4, 'g contorno'), ('SABÃO', 5, 'g ceu'), ('GORDURA', 7, 'g laranja')], vfx=['grade']),
         dict(t=T(8) - .08, foto='5768318.jpg', pos='50% 46%', z=(3.2, 3.8), spin=10, escuro=.55, cap=1,
              linhas=[('FECHAM', 8, 'g'), ('O RALO', 10, 'g laranja'), ('AOS POUCOS', 11, 'm')], vfx=['fechando']),
         dict(t=T(13) - .08, bg=LAR2, linhas=[('PRODUTO', 13, 'g branco'), ('DE MERCADO', 15, 'm branco'), ('SÓ EMPURRA', 17, 'g escuro empurra'), ('O PROBLEMA', 19, 'm branco')]),
         dict(t=T(20) - .08, foto='16509869.jpg', pos='45% 50%', z=(1.5, 1.75), pan=(16, 0), escuro=.45, cap=1,
              linhas=[('A SF LIMPA', 20, 'g'), ('O CANO', 24, 'g laranja'), ('COM MÁQUINA', 26, 'm')], punch=[T(26)]),
         dict(t=T(27) - .08, bg=ROYAL, linhas=[('SEM QUEBRAR', 27, 'g'), ('O PISO', 30, 'xg laranja')], nota=('na maioria dos casos', T(31)), vfx=['azulejo']),
         dict(t=T(35) - .1, cta='ORÇAMENTO GRÁTIS', ctasub='manda foto ou vídeo do ralo'),
        ]
    if n == 4:  # RALO/PIA · antes × depois em tela dividida (ref. C Liquid-Plumr)
        return [
         dict(t=0, foto='87299.jpg', pos='50% 50%', z=(1.4, 1.6), pan=(0, 0), escuro=.45, cinza=1, cap=0, etiqueta='ANTES',
              linhas=[('A PIA ENCHE', 1, 'g'), ('E NÃO', 4, 'g'), ('DESCE', 6, 'xg laranja')], vfx=['agua']),
         dict(t=T(7) - .08, split=('87299.jpg', '20661422.jpg'), linhas=[('A ÁGUA CORRE', 9, 'm'), ('DE NOVO', 11, 'g laranja')]),
         dict(t=T(13) - .08, bg=NAVY, linhas=[('RALO DA PIA', 13, 'g esq'), ('DO TANQUE', 17, 'g dir ceu'), ('OU DO BOX', 19, 'g esq laranja')], vfx=['grade']),
         dict(t=T(21) - .08, foto='20661422.jpg', pos='50% 40%', z=(1.5, 1.8), spin=-30, escuro=.4, cap=1,
              linhas=[('A SF RESOLVE', 21, 'm'), ('CABO', 25, 'xg'), ('ROTATIVO', 26, 'g laranja')], vfx=['redemoinho'], punch=[T(26)]),
         dict(t=T(27) - .08, bg=LAR2, linhas=[('TESTA', 28, 'xg branco'), ('NA HORA', 30, 'g escuro'), ('NA SUA FRENTE', 31, 'm branco')], vfx=['check']),
         dict(t=T(34) - .1, cta='MANDA UM VÍDEO', ctasub='e recebe o orçamento grátis'),
        ]
    if n == 5:  # CAIXA DE GORDURA · comércio, manchete + técnico com a máquina (ref. A + C)
        return [
         dict(t=0, foto='39618021.jpg', pos='50% 50%', z=(1.7, 2.0), spin=4, escuro=.4, cap=0,
              linhas=[('CHEIRO DE', 0, 'g'), ('ESGOTO', 2, 'xg laranja cheiro'), ('NA COZINHA?', 4, 'g')], vfx=['cheiro'], punch=[T(2)]),
         dict(t=T(7) - .08, foto='10949030.jpg', pos='40% 50%', z=(1.6, 1.85), pan=(-14, 0), escuro=.5, cap=1,
              linhas=[('PODE SER A', 7, 'm'), ('CAIXA DE', 10, 'g'), ('GORDURA CHEIA', 12, 'g tarja')], punch=[T(13)]),
         dict(t=T(14) - .08, foto='10949030.jpg', pos='90% 50%', z=(2.4, 2.6), pan=(10, 0), escuro=.72, desfoque=10,
              gigante='SF', rec='32588559-rec.png', recpos=(600, 760, 1150), chips=[('ATENDE COMÉRCIO', T(16))]),
         dict(t=T(18) - .08, bg=ROYAL, linhas=[('RESTAURANTES', 17, 'g'), ('CONDOMÍNIOS', 18, 'g ceu2'), ('EMPRESAS', 20, 'g laranja')], vfx=['grade']),
         dict(t=T(21) - .08, bg=NAVY, linhas=[('EM', 21, 'm'), ('SÃO LUÍS', 22, 'xg laranja')], vfx=['pin']),
         dict(t=T(24) - .08, bg=LAR2, linhas=[('LIMPEZA E', 24, 'g branco'), ('DESENTUPIMENTO', 26, 'g escuro'), ('COM MÁQUINA', 28, 'm branco')], punch=[T(28)]),
         dict(t=T(30) - .08, bg=NAVY2, linhas=[('AGENDAMENTO', 30, 'g'), ('CONFORME', 31, 'm ceu'), ('A AGENDA', 33, 'g laranja')], vfx=['relogio']),
         dict(t=T(34) - .1, cta='CHAMA NO WHATSAPP', ctasub='orçamento grátis por foto ou vídeo'),
        ]

def legenda(n):
    return [(p[0].upper().strip('.,?!:'), p[1]) for p in json.load(open(os.path.join(D, 'voz', f'{n}.json')))['palavras']]

CSS = f'''*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1920px;background:{NAVY};overflow:hidden;font-family:Montserrat}}
.s{{position:absolute;inset:0;display:none;overflow:hidden;perspective:1400px}}
.cam{{position:absolute;inset:0;transform-style:preserve-3d}}
.ft{{position:absolute;left:-10%;top:-10%;width:120%;height:120%;object-fit:cover}}
.ln{{position:absolute;left:70px;right:70px;font-style:italic;font-weight:900;text-transform:uppercase;color:#fff;line-height:.92;letter-spacing:-.02em;white-space:nowrap;text-shadow:0 10px 40px rgba(0,0,0,.45)}}
.ln .w{{display:inline-block;will-change:transform}}
.laranja{{color:{LAR}}}.ceu{{color:{CEU}}}.ceu2{{color:#bfe3ff}}.escuro{{color:{NAVY};text-shadow:none}}.branco{{color:#fff}}
.contorno{{color:transparent;-webkit-text-stroke:4px #fff;text-shadow:none}}
.tarja span.w{{background:{LAR2};padding:6px 26px 10px;color:#fff;text-shadow:none;box-shadow:0 18px 50px rgba(255,106,0,.45)}}

.chip{{position:absolute;left:70px;padding:22px 34px;border-radius:999px;background:{LAR2};color:#fff;font:italic 900 46px Montserrat;text-transform:uppercase;box-shadow:0 20px 60px rgba(0,0,0,.4)}}
.num{{position:absolute;right:-30px;top:330px;font:italic 900 820px/1 Montserrat;color:rgba(255,255,255,.08);letter-spacing:-.06em}}
.nota{{position:absolute;left:70px;font:600 34px Montserrat;color:#fff;opacity:.9}}
.et{{position:absolute;left:70px;top:420px;padding:12px 30px;border:3px solid #fff;border-radius:999px;font:italic 900 44px Montserrat;color:#fff}}
'''

def foto_layer(c):
    f = []
    filt = []
    if c.get('cinza'): filt.append('grayscale(.85)')
    if c.get('desfoque'): filt.append(f"blur({c['desfoque']}px)")
    f.append(f'<img class="ft zf" src="{F}{c["foto"]}" style="object-position:{c.get("pos","50% 50%")};filter:{" ".join(filt) or "none"}">')
    e = c.get('escuro', .4)
    f.append(f'<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(6,26,74,{e*.6}) 0%,rgba(6,26,74,{e}) 45%,rgba(6,26,74,{min(1,e+.35)}) 100%)"></div>')
    return ''.join(f)

def linhas_html(c, w, y0=None):
    L = c.get('linhas', []); out = []
    tam = {'xg': 270, 'g': 172, 'm': 100}
    hs = [tam[st.split()[0]] for _, _, st in L]
    tot = sum(h * .98 for h in hs) + 18 * (len(L) - 1)
    y = y0 if y0 is not None else max(450, 960 - tot / 2)
    if c.get('etiqueta'): y = max(y, 520)
    for (txt, idx, st), h in zip(L, hs):
        t0 = w[int(idx)] + (idx - int(idx)) * 0 if isinstance(idx, int) else (w[int(idx)] + .25)
        if c['t'] == 0 and idx in (0,): t0 = -1
        cls = ' '.join(st.split()[1:])
        al = 'right' if 'dir' in cls else 'left'
        palavras = ''.join(f'<span class="w" data-t="{t0 + k*0.07:.3f}">{html.escape(p)}</span>{"&nbsp;" if k < len(txt.split())-1 else ""}' for k, p in enumerate(txt.split()))
        out.append(f'<div class="ln {cls}" data-fit="1" style="top:{y:.0f}px;font-size:{h}px;text-align:{al}">{palavras}</div>')
        y += h * .98 + 18
    return ''.join(out), y

def vfx_html(v):
    if v == 'aneis' or v == 'agua':
        op = .35 if v == 'aneis' else .18
        return ''.join(f'<div class="anel" data-k="{k}" style="position:absolute;left:540px;top:{960 if v=="aneis" else 1150}px;width:10px;height:10px;border:6px solid rgba(255,255,255,{op});border-radius:50%;transform:translate(-50%,-50%)"></div>' for k in range(5))
    if v == 'redemoinho':
        return '<div class="giro" style="position:absolute;left:50%;top:50%;width:1600px;height:1600px;margin:-800px 0 0 -800px;background:repeating-conic-gradient(rgba(255,255,255,.07) 0 6deg,transparent 6deg 24deg);border-radius:50%;mix-blend-mode:screen"></div>'
    if v == 'grade':
        return f'<div class="grade" style="position:absolute;inset:-200px;background-image:linear-gradient(rgba(255,255,255,.06) 2px,transparent 2px),linear-gradient(90deg,rgba(255,255,255,.06) 2px,transparent 2px);background-size:120px 120px"></div>'
    if v == 'azulejo':
        return '<div class="grade" style="position:absolute;inset:-200px;background-image:linear-gradient(rgba(255,255,255,.18) 4px,transparent 4px),linear-gradient(90deg,rgba(255,255,255,.18) 4px,transparent 4px);background-size:180px 180px"></div>'
    if v == 'rachadura':
        return '<svg class="rach" viewBox="0 0 1080 1920" style="position:absolute;inset:0"><path d="M0 1240 L210 1200 L330 1290 L470 1180 L620 1260 L760 1170 L900 1240 L1080 1190" stroke="rgba(6,26,74,.55)" stroke-width="10" fill="none" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/></svg>'
    if v == 'check':
        return f'<svg class="chk" viewBox="0 0 1080 1920" style="position:absolute;inset:0"><circle cx="840" cy="560" r="120" fill="{NAVY}"/><path d="M780 560 L830 610 L910 515" stroke="#fff" stroke-width="26" stroke-linecap="round" stroke-linejoin="round" fill="none" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/></svg>'
    if v == 'ondas':
        return '<div style="position:absolute;left:70px;right:70px;top:1220px;height:180px;display:flex;gap:14px;align-items:center">' + ''.join(f'<div class="bar" data-k="{k}" style="flex:1;background:{CEU};border-radius:8px;height:20px"></div>' for k in range(26)) + '</div>'
    if v == 'cheiro':
        return '<div class="fumo" style="position:absolute;inset:0;background:radial-gradient(ellipse 60% 40% at 50% 70%,rgba(140,200,90,.22),transparent 70%);mix-blend-mode:screen"></div>'
    if v == 'gotas':
        return ''.join(f'<div class="gota" data-k="{k}" style="position:absolute;left:{120+k*190}px;top:0;width:14px;height:60px;border-radius:7px;background:linear-gradient(transparent,rgba(63,169,255,.8))"></div>' for k in range(5))
    if v == 'fechando':
        return f'<div class="anelf" style="position:absolute;left:540px;top:900px;width:900px;height:900px;margin:-450px 0 0 -450px;border-radius:50%;box-shadow:0 0 0 2000px rgba(6,26,74,.85);border:10px solid {LAR}"></div>'
    if v == 'relogio':
        return f'<div style="position:absolute;right:90px;top:1180px;width:220px;height:220px;border-radius:50%;border:12px solid rgba(255,255,255,.85)"><div class="ponteiro" style="position:absolute;left:50%;top:50%;width:10px;height:86px;margin-left:-5px;background:#fff;transform-origin:50% 0;border-radius:5px"></div></div>'
    if v == 'pin':
        return ''.join(f'<div class="anel" data-k="{k}" style="position:absolute;left:540px;top:1260px;width:10px;height:10px;border:6px solid rgba(255,138,0,.6);border-radius:50%;transform:translate(-50%,-50%)"></div>' for k in range(4)) + f'<div style="position:absolute;left:540px;top:1260px;width:44px;height:44px;margin:-22px;border-radius:50%;background:{LAR}"></div>'
    return ''

def cena_html(i, c, w, dur_cena):
    a = [f'<div class="s" id="s{i}" data-z0="{c.get("z",(1,1))[0]}" data-z1="{c.get("z",(1,1))[1]}" data-px="{c.get("pan",(0,0))[0]}" data-py="{c.get("pan",(0,0))[1]}" data-spin="{c.get("spin",0)}" data-tilt="{c.get("tilt",0)}" data-dur="{dur_cena:.3f}" data-punch="{",".join(f"{p:.3f}" for p in c.get("punch",[]))}">']
    a.append('<div class="cam">')
    if 'cta' in c:
        a.append(cta_html(c, w)); a.append('</div></div>'); return ''.join(a)
    if c.get('bg'):
        a.append(f'<div style="position:absolute;inset:0;background:radial-gradient(ellipse 90% 60% at 50% 40%,{c["bg"]},{NAVY if c["bg"]!=NAVY else "#020b24"} 95%)"></div>')
    if c.get('foto'):
        a.append(f'<div class="lf" data-d="1">{foto_layer(c)}</div>')
    if c.get('split'):
        f1, f2 = c['split']
        a.append(f'<div class="sp1" style="position:absolute;left:0;top:0;width:1080px;height:960px;overflow:hidden"><img class="ft zf" src="{F}{f1}" style="filter:grayscale(.85) brightness(.55)"><div class="et" style="top:440px">ANTES</div></div>')
        a.append(f'<div class="sp2" style="position:absolute;left:0;top:960px;width:1080px;height:960px;overflow:hidden"><img class="ft zf" src="{F}{f2}" style="object-position:50% 30%;filter:saturate(1.2) brightness(.8)"><div style="position:absolute;inset:0;background:linear-gradient(0deg,rgba(6,26,74,.75),transparent 60%)"></div><div class="et" style="top:60px;background:{LAR2};border-color:{LAR2}">DEPOIS</div></div>')
        a.append(f'<div class="spl" style="position:absolute;left:0;top:952px;height:16px;width:1080px;background:{LAR}"></div>')
    for v in c.get('vfx', []): a.append(f'<div class="vx" data-v="{v}">{vfx_html(v)}</div>')
    if c.get('numero'): a.append(f'<div class="num ld" data-d="2">{c["numero"]}</div>')
    if c.get('etiqueta'): a.append(f'<div class="et">{c["etiqueta"]}</div>')
    if c.get('gigante'):
        a.append(f'<div class="ld gig" data-d="2" style="position:absolute;left:0;right:0;top:380px;text-align:center;font:italic 900 1000px/1 Montserrat;letter-spacing:-.08em;color:{LAR};text-shadow:0 30px 80px rgba(0,0,0,.4)">{c["gigante"]}</div>')
    if c.get('rec'):
        x, y, h = c['recpos']
        a.append(f'<img class="ld rc" data-d="3" src="{F}{c["rec"]}" style="position:absolute;left:{x}px;top:{1920-h - 0}px;height:{h + 40}px;transform-origin:50% 100%;margin-left:-300px;filter:drop-shadow(0 30px 50px rgba(0,0,0,.6))">')
    if c.get('split'):
        hl, _ = linhas_html(c, w, y0=1300)
    else:
        hl, yfim = linhas_html(c, w)
    a.append(f'<div class="ld" data-d="2">{hl}</div>')
    for k, (txt, t0) in enumerate(c.get('chips', [])):
        a.append(f'<div class="chip w2" data-t="{t0:.3f}" style="top:{1290 + k*110}px">{html.escape(txt)}</div>')
    if c.get('nota'):
        txt, t0 = c['nota']; a.append(f'<div class="nota w2" data-t="{t0:.3f}" style="top:1400px">* {txt}</div>')
    a.append('</div></div>')
    return ''.join(a)

def cta_html(c, w):
    return (f'<div style="position:absolute;inset:0;background:radial-gradient(ellipse 80% 55% at 50% 38%,{ROYAL},{NAVY} 70%,#020b24)"></div>'
            + vfx_html('aneis').replace('top:960px', 'top:640px') +
            f'<div class="w2" data-t="{c["t"]:.3f}" style="position:absolute;left:390px;top:500px;width:300px;height:300px;border-radius:50%;overflow:hidden;border:8px solid #fff;box-shadow:0 30px 80px rgba(0,0,0,.5)"><img src="{F}logo.jpg" style="width:100%;height:100%;object-fit:cover;transform:scale(1.04)"></div>'
            f'<div class="ln w2" data-fit="1" data-t="{c["t"]+.15:.3f}" style="top:870px;font-size:96px;text-align:center">{c["cta"]}</div>'
            f'<div class="w2" data-t="{c["t"]+.35:.3f}" style="position:absolute;left:0;right:0;top:990px;text-align:center;font:600 42px Montserrat;color:#dce9ff">{c["ctasub"]}</div>'
            f'<div class="w2 pulso" data-t="{c["t"]+.55:.3f}" style="position:absolute;left:80px;right:80px;top:1080px;padding:34px 0 38px;border-radius:999px;background:linear-gradient(90deg,{LAR},{LAR2});text-align:center;box-shadow:0 24px 70px rgba(255,106,0,.55)">'
            f'<div style="font:600 34px Montserrat;color:#fff;opacity:.95">WhatsApp</div><div style="font:italic 900 88px/1.05 Montserrat;color:#fff;letter-spacing:-.02em">{NUM}</div></div>'
            f'<div class="w2" data-t="{c["t"]+.8:.3f}" style="position:absolute;left:0;right:0;top:1330px;text-align:center;font:700 38px Montserrat;color:#fff">{ARROBA} · São Luís e região</div>')

for n, r in R.items():
    w = W(n); voz_fim = json.load(open(os.path.join(D, 'voz', f'{n}.json')))['palavras'][-1][2]
    dur = round(voz_fim + 1.4, 2)
    C = cenas(n)
    starts = [max(0, c['t']) for c in C]; C[0]['t'] = 0
    corpo = ''.join(cena_html(i, c, w, (starts[i+1] if i+1 < len(C) else dur) - starts[i]) for i, c in enumerate(C))
    caps = [i for i, c in enumerate(C) if c.get('cap')]
    doc = f'''<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,600;0,700;0,900;1,900&display=swap" rel="stylesheet"><style>{CSS}</style></head><body>
<div id="cena" style="position:absolute;inset:0">{corpo}</div>
<div id="leg" style="position:absolute;left:60px;right:60px;top:1500px;text-align:center"><span id="legw" style="display:inline-block;font:italic 900 78px Montserrat;color:#fff;background:{LAR2};padding:6px 26px 12px;text-transform:uppercase;box-shadow:0 16px 40px rgba(0,0,0,.4)"></span></div>
<div style="position:absolute;left:70px;right:70px;top:300px;height:10px;border-radius:5px;background:rgba(255,255,255,.18)"><div id="bar" style="height:100%;width:0;border-radius:5px;background:{LAR}"></div></div>
<div style="position:absolute;left:70px;top:330px;display:flex;align-items:center;gap:16px"><img src="{F}logo.jpg" style="width:64px;height:64px;border-radius:50%;object-fit:cover;border:3px solid #fff"><div style="font:italic 900 30px Montserrat;color:#fff;letter-spacing:.02em">DESENTUPIDORA SF<div style="font:700 22px Montserrat;font-style:normal;color:#bcd3ff">São Luís · MA</div></div></div>
<div id="leak" style="position:absolute;inset:-300px;background:radial-gradient(circle at 12% 12%,rgba(255,138,0,.5),transparent 38%),radial-gradient(circle at 92% 82%,rgba(63,169,255,.4),transparent 42%);mix-blend-mode:screen;pointer-events:none"></div>
<div style="position:absolute;inset:0;background:radial-gradient(ellipse 75% 60% at 50% 50%,transparent 55%,rgba(0,0,0,.55));pointer-events:none"></div>
<div style="position:absolute;right:70px;top:1600px;font:600 18px Montserrat;color:rgba(255,255,255,.55)">Imagens ilustrativas · Pexels</div>
<div id="flash" style="position:absolute;inset:0;background:#fff;opacity:0;pointer-events:none"></div>
<svg width="0" height="0" style="position:absolute"><filter id="ond"><feTurbulence id="turb" type="fractalNoise" baseFrequency="0.012 0.03" numOctaves="2" seed="3"/><feDisplacementMap in="SourceGraphic" scale="26"/></filter></svg>
<script>
const ST={json.dumps(starts)},T={dur},L={json.dumps(legenda(n), ensure_ascii=False)},CAP={json.dumps(caps)};
const cl=(x)=>Math.min(1,Math.max(0,x)),E=(a,b,t)=>cl((t-a)/(b-a)),eo=x=>1-Math.pow(1-x,3),back=x=>{{const c=1.9;return 1+(c+1)*Math.pow(x-1,3)+c*Math.pow(x-1,2)}};
window.fit=()=>document.querySelectorAll('[data-fit]').forEach(el=>{{let fs=parseFloat(el.dataset.fs||(el.dataset.fs=el.style.fontSize));el.style.fontSize=fs+'px';el.style.right='auto';el.style.display='block';el.parentElement.closest('.s')&&(el.parentElement.closest('.s').style.display='block');
  while(el.scrollWidth>940&&fs>40){{fs-=4;el.style.fontSize=fs+'px'}}el.style.right='70px';const s=el.closest('.s');if(s)s.style.display='none'}});fit();
document.querySelectorAll('.risco').forEach(el=>{{const d=document.createElement('div');d.className='rl';d.style.cssText='position:absolute;left:0;top:52%;height:16px;background:#ff6a00;width:0';el.appendChild(d)}});
window.render=function(t){{
 let a=0;for(let i=0;i<ST.length;i++)if(t>=ST[i])a=i;
 for(let i=0;i<ST.length;i++)document.getElementById('s'+i).style.display=i==a?'block':'none';
 const el=document.getElementById('s'+a),lt=t-ST[a],d=+el.dataset.dur,u=cl(lt/d);
 // câmera: entrada com deslocamento + desfoque direcional (motion blur), saída com zoom
 const qin=eo(E(0,.22,lt)),qout=E(d-.12,d,lt),dir=(a%2?1:-1);
 let pz=1;(el.dataset.punch||'').split(',').filter(x=>x).forEach(p=>{{const k=t-(+p);if(k>=0&&k<.35)pz+=.07*(1-k/.35)}});
 const cam=el.querySelector('.cam');
 cam.style.transform=`translate3d(${{a?dir*(1-qin)*420:0}}px,${{a?(1-qin)*-120:0}}px,0) scale(${{(a?1.18-.18*qin:1)*pz*(1+.25*qout*qout)}}) rotateY(${{(+el.dataset.tilt)*(-6+12*u)}}deg) rotateX(${{(+el.dataset.tilt)*3}}deg)`;
 cam.style.filter=a&&qin<1?`blur(${{(1-qin)*16}}px)`:(qout>0?`blur(${{qout*12}}px)`:'none');
 // 2.5D: cada camada em velocidade diferente
 const z0=+el.dataset.z0,z1=+el.dataset.z1,px=+el.dataset.px,py=+el.dataset.py,sp=+el.dataset.spin;
 el.querySelectorAll('.zf').forEach(z=>{{z.style.transform=`scale(${{z0+(z1-z0)*eo(u)}}) translate(${{px*lt}}px,${{py*lt}}px) rotate(${{sp*lt}}deg)`}});
 el.querySelectorAll('.ld').forEach(z=>{{const k=+z.dataset.d;z.style.transform=`translate(${{-px*lt*k*.9}}px,${{k*-6*lt}}px) scale(${{1+.015*k*lt}})`}});
 // tipografia cinética: cada palavra entra no tempo da fala
 el.querySelectorAll('.w,.w2').forEach(s=>{{const ts=+s.dataset.t;const q=E(ts,ts+.2,t);
   if(t<ts){{s.style.opacity=0;return}}s.style.opacity=1;const b=back(q);
   s.style.transform=(s.classList.contains('w2')?'':'')+`translateY(${{(1-q)*70}}px) scale(${{1.6-.6*b}})`;s.style.filter=q<1?`blur(${{(1-q)*14}}px)`:'none'}});
 el.querySelectorAll('.tremor .w').forEach(s=>{{if(t>+s.dataset.t+.2)s.style.transform=`translate(${{Math.sin(t*90)*8}}px,${{Math.cos(t*77)*6}}px)`}});
 el.querySelectorAll('.empurra .w').forEach(s=>{{const ts=+s.dataset.t;if(t>ts+.2)s.style.transform=`translateX(${{eo(E(ts+.2,ts+.9,t))*60}}px) skewX(-8deg)`}});
 el.querySelectorAll('.esq').forEach(s=>s.style.transform=`translateX(${{-30+40*u}}px)`);el.querySelectorAll('.dir').forEach(s=>s.style.transform=`translateX(${{30-40*u}}px)`);
 el.querySelectorAll('.cheiro').forEach(s=>s.style.filter='url(#ond)');document.getElementById('turb').setAttribute('baseFrequency',`${{.012+.004*Math.sin(t*3)}} ${{.03+.01*Math.cos(t*2)}}`);
 el.querySelectorAll('.rl').forEach(r=>{{const ws=r.parentElement.querySelectorAll('.w'),ts=+ws[ws.length-1].dataset.t;r.style.width=(eo(E(ts+.25,ts+.55,t))*100)+'%'}});
 el.querySelectorAll('.pulso').forEach(p=>{{const ts=+p.dataset.t;if(t>ts+.2)p.style.transform=`scale(${{1+.035*Math.sin((t-ts)*7)}})`}});
 // VFX
 el.querySelectorAll('.anel').forEach(r=>{{const k=+r.dataset.k,ph=((lt*.9+k*.2)%1);r.style.width=r.style.height=(40+ph*1400)+'px';r.style.opacity=1-ph}});
 el.querySelectorAll('.giro').forEach(g=>g.style.transform=`rotate(${{lt*90}}deg)`);
 el.querySelectorAll('.grade').forEach(g=>g.style.transform=`translate(${{lt*40}}px,${{lt*-60}}px)`);
 el.querySelectorAll('.rach path').forEach(p=>p.style.strokeDashoffset=1-eo(E(.25,.6,lt)));
 el.querySelectorAll('.chk path').forEach(p=>p.style.strokeDashoffset=1-eo(E(.5,.9,lt)));
 el.querySelectorAll('.bar').forEach(b=>{{const k=+b.dataset.k;b.style.height=(20+150*Math.abs(Math.sin(t*9+k*.7))*Math.abs(Math.sin(t*3.1+k)))+'px'}});
 el.querySelectorAll('.fumo').forEach(f=>{{f.style.transform=`translateY(${{-lt*120}}px) scale(${{1+lt*.2}})`;f.style.opacity=.6+.4*Math.sin(t*4)}});
 el.querySelectorAll('.gota').forEach(g=>{{const k=+g.dataset.k,ph=((lt*.8+k*.37)%1);g.style.top=(-80+ph*2000)+'px'}});
 el.querySelectorAll('.anelf').forEach(f=>{{const q=eo(E(.2,d-.2,lt));f.style.width=f.style.height=(1000-640*q)+'px';f.style.margin=`${{-(500-320*q)}}px 0 0 ${{-(500-320*q)}}px`}});
 el.querySelectorAll('.ponteiro').forEach(p=>p.style.transform=`rotate(${{180+lt*360}}deg)`);
 el.querySelectorAll('.sp2').forEach(s=>s.style.clipPath=`inset(0 ${{100-eo(E(.05,.5,lt))*100}}% 0 0)`);
 el.querySelectorAll('.spl').forEach(s=>s.style.width=(eo(E(.05,.5,lt))*1080)+'px');
 el.querySelectorAll('.rc').forEach(r=>{{r.style.transform=`translate(${{-px*lt*3}}px,${{(1-eo(E(0,.35,lt)))*200}}px) scale(${{1+.03*lt}})`}});
 el.querySelectorAll('.gig').forEach(g=>{{g.style.opacity=eo(E(.05,.3,lt));g.style.transform=`scale(${{1.25-.25*eo(E(.05,.4,lt))+.02*lt}})`}});
 // tremor no impacto de cada corte
 const sh=Math.max(0,1-lt/.28)*(a==0?1.4:1);document.getElementById('cena').style.transform=`translate(${{14*sh*Math.sin(t*83)}}px,${{10*sh*Math.cos(t*71)}}px)`;
 document.getElementById('flash').style.opacity=a>0?Math.max(0,.6-lt/.1*.6):0;
 let lw='';if(CAP.includes(a))for(const [p,ts] of L)if(t>=ts-.02)lw=p;
 const lg=document.getElementById('legw');lg.textContent=lw;lg.style.display=lw?'inline-block':'none';
 document.getElementById('bar').style.width=(100*cl(t/T))+'%';
 document.getElementById('leak').style.opacity=.25+.2*Math.sin(t*1.7);document.getElementById('leak').style.transform=`rotate(${{t*6}}deg)`;
}};render(0);</script></body></html>'''
    open(os.path.join(D, f'v{n}.html'), 'w').write(doc)
    json.dump({'dur': dur, 'cortes': starts[1:], 'cta': starts[-1]}, open(os.path.join(D, f'v{n}.json'), 'w'))
    print(n, dur, len(C), 'cenas')
