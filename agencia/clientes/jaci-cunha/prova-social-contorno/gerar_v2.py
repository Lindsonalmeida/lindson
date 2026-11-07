# Prova social "Contorno facial masculino" da Dra. Jaci Cunha · VERSÃO 2 (Design Squad, conta Leandro, 07/11/2026).
# Pedido do Lindson (07/11): "não gostei, refaça no estilo da identidade dela". A v1 (gerar.py) foi REPROVADA:
# cara de template de clínica, arcos, fundo bege liso, sem a assinatura dela.
# Nada se cria, tudo se copia: cada peça copia uma composição REAL dos posts dela (../instagram-estilo/README.md)
# com o mesmo acabamento do feed aprovado (../conteudo-nov/gerar.py): Playfair Display itálica + Poppins, vinho #6E1A2A,
# ouro #B9A27A, café #5A4033, creme #F3EADD, assinatura fixa no topo (3 colunas) e no rodapé (2 colunas).
#   post-perfil  = modelo (b) premium: lado a lado em FUNDO PRETO com a logo oficial dourada (monograma JC 3D + DRA. JACI CUNHA)
#   carrossel-1  = capa "Entramos / na reta final do ano..." (sans bold + serifada itálica, faixas vinho, ARRASTE PARA O LADO)
#   carrossel-2  = modelo (a): antes em cima, depois embaixo, "Draª Jaci Cunha / Cro: 8514" no canto da foto de depois
#   carrossel-3  = "Preenchimento facial, (faixa translúcida) por que alguns ficam artificiais..." sobre o 3/4 lado a lado
#   carrossel-4  = modelo (c): tríptico "a tela: / a artista: / a obra de arte:" -> "o paciente: / a avaliação: / o contorno:"
#   carrossel-5  = tela informativa (véu branco sobre foto desfocada, título sans bold, checks verde-escuros, nota serifada)
#   carrossel-6  = "O que você precisa entender sobre / Bioestimulador de Colágeno (faixa dourada com fio e pontos) / QUANDO COMEÇAR?"
#   carrossel-7  = "Antes de qualquer procedimento, eu observo." (faixa café + sans itálico + pílula com seta)
#   story-1      = antes × depois + balão "Você faria?" (espaço livre para a figurinha de enquete do Instagram)
#   story-2      = "Entramos / na reta final..." em 9:16 com a chamada para a avaliação (espaço para a figurinha de link)
# Fotos do paciente SEM filtro de cor (regra CFO: foto sem edição). Só as fotos da Dra. levam o tratamento de cor do feed.
# Uso: python3 gerar_v2.py <pasta privada da entrega>   (fotos do paciente em <pasta>/fotos; fotos da Dra. na pasta privada fotos-novas
#      e em ../fotos; logo em ../identidade/v2/img) -> <pasta>/v2/*.jpg (1080×1350 e 1080×1920) + <pasta>/v2/previa.jpg
import sys, os, subprocess
import numpy as np
from PIL import Image, ImageDraw, ImageFont

AQUI = os.path.dirname(os.path.abspath(__file__))
D = os.path.abspath(sys.argv[1])
F = f'{D}/fotos'
OUT = f'{D}/v2'
NOVAS = os.path.abspath(f'{D}/../fotos-novas')
FOTOS = os.path.abspath(f'{AQUI}/../fotos')
IDV = os.path.abspath(f'{AQUI}/../identidade/v2/img')
os.makedirs(f'{OUT}/_tmp', exist_ok=True)
VINHO, OURO, CAFE, CREME = '#6E1A2A', '#B9A27A', '#5A4033', '#F3EADD'
VARIAM = 'Resultados variam de pessoa para pessoa.'

# ---------- logo oficial: monograma JC 3D dourado recortado do fundo bordô (identidade v2) ----------
def recorta_logo(nome, saida, sc=4):
    im = Image.open(f'{IDV}/{nome}').convert('RGB'); im = im.resize((im.width * sc, im.height * sc), Image.LANCZOS)
    a = np.asarray(im).astype(float); al = np.clip((a[..., 1] - 30) / 130, 0, 1)
    rgb = np.clip((a - np.array([104, 23, 32]) * (1 - al[..., None])) / np.maximum(al[..., None], .05), 0, 255)
    o = Image.fromarray(np.dstack([rgb, al * 255]).astype('uint8'), 'RGBA'); o.crop(o.getbbox()).save(saida)
recorta_logo('monograma.jpg', f'{OUT}/_tmp/monograma.png')

def tam(p): return Image.open(p).size
def ft(p, x, y, w, h, cx=.5, cy=.5, z=1.0, filtro=False, extra=''):
    """foto recortada pelo ponto focal (cx, cy em fração da foto), sem distorcer e sem borda da foto original aparecendo"""
    iw, ih = tam(p); s = max(w / iw, h / ih) * z; dw, dh = iw * s, ih * s
    l = min(0, max(w - dw, w / 2 - cx * dw)); t = min(0, max(h - dh, h / 2 - cy * dh))
    cl = ' class="jc"' if filtro else ''
    return (f'<div class="a" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;overflow:hidden;{extra}">'
            f'<img{cl} src="{p}" style="position:absolute;left:{l:.0f}px;top:{t:.0f}px;width:{dw:.0f}px;height:{dh:.0f}px"></div>')
P = lambda n: f'{F}/{n}.jpg'

def topo(cor='#fff', y=96):
    return (f'<div class="a topo" style="top:{y}px;color:{cor}"><span><b>CLINICA.</b>DRA<b>JACI</b>CUNHA<i class="ok">✓</i></span>'
            f'<span>CIRURGIÃ-DENTISTA</span><span>@clinica.dra<b>jaci</b>cunha</span></div>')
def rodape(cor='#fff', y=1210):
    return (f'<div class="a rod" style="top:{y}px;color:{cor}"><div>DRA JACI CUNHA<br><small>HARMONIZAÇÃO FACIAL<br>@clinica.drajacicunha</small></div>'
            f'<div style="text-align:right">CLÍNICA DRA. JACI CUNHA<br><small>AV. MILITAR, EM FRENTE À PRAÇA<br>DO VIVA - ZÉ DOCA/MA.</small></div></div>')
def cro(cor='#fff', x=None, y=None, right=None, al='right', tam_=24):  # "Draª Jaci Cunha / Cro: 8514" no canto da foto de depois
    pos = f'top:{y}px;' + (f'right:{right}px;' if right is not None else f'left:{x}px;')
    return (f'<div class="a S crs" style="{pos}color:{cor};text-align:{al};font-size:{tam_}px">Draª Jaci Cunha<br>'
            f'<span class="sans" style="font-style:normal;font-size:{tam_*.62:.0f}px;letter-spacing:.14em">CRO-MA 8514</span></div>')
def aviso(cor, y, tam_=15):
    return f'<div class="a avi" style="top:{y}px;color:{cor};font-size:{tam_}px">{VARIAM} · Draª Jaci Cunha · CRO-MA 8514</div>'
def rot(txt, x, y, cor='#fff', al='left', w=300):  # rótulo "antes"/"depois" em serifada itálica, como nos posts dela
    return f'<div class="a S rt" style="left:{x}px;top:{y}px;width:{w}px;text-align:{al};color:{cor}">{txt}</div>'
def gr(de, ate, a, cor='0,0,0'):
    return f'<div class="a" style="inset:0;background:linear-gradient(180deg,rgba({cor},0) {de}%,rgba({cor},{a}) {ate}%)"></div>'

pecas = []
# ---------- POST ÚNICO · modelo (b) premium: lado a lado de perfil, fundo preto, logo oficial dourada ----------
pecas.append(('post-perfil', 1350,
    '<div class="a" style="inset:0;background:radial-gradient(900px 700px at 50% 18%,#1B1512 0,#0A0807 70%)"></div>' + topo('rgba(214,192,150,.85)') +
    f'<img class="a" src="{OUT}/_tmp/monograma.png" style="left:50%;transform:translateX(-50%);top:146px;height:178px;filter:brightness(1.45) contrast(1.1)">'
    '<div class="a logo" style="top:330px">DRA. JACI CUNHA</div>'
    '<div class="a logo2" style="top:408px">HARMONIZAÇÃO OROFACIAL E ODONTOLOGIA</div>' +
    ft(P('perfil-antes'), 88, 452, 448, 648, .5, .5) + ft(P('perfil-depois'), 544, 452, 448, 648, .5, .5) +
    '<div class="a" style="left:88px;top:452px;width:904px;height:648px;box-shadow:0 0 0 1px rgba(198,160,106,.55)"></div>' +
    rot('antes', 88, 1108, OURO, 'center', 448) + rot('depois', 544, 1108, OURO, 'center', 448) +
    aviso('rgba(214,192,150,.75)', 1166, 14) + rodape('rgba(214,192,150,.8)', 1212)))

# ---------- CARROSSEL 1 · capa com gancho (cópia de "Entramos / na reta final do ano..." + faixas vinho + ARRASTE PARA O LADO) ----------
pecas.append(('carrossel-1', 1350,
    f'<div class="a" style="inset:0;background:{CREME}"></div>' + topo(CAFE) +
    f'<div class="a" style="left:88px;top:180px;width:900px"><div class="sans" style="font-size:54px;font-weight:700;color:{CAFE};line-height:1">Contorno facial</div>'
    f'<div class="S" style="font-size:112px;color:{VINHO};line-height:1.02;margin-top:2px">masculino...</div></div>'
    '<div class="a" style="right:88px;top:388px;text-align:right"><div><span class="fv">PAPADA, <b>MANDÍBULA</b></span></div><div><span class="fv">E <b>QUEIXO</b>:</span></div>'
    f'<div class="sans arr" style="margin-top:12px;color:{CAFE}"><b>ARRASTE</b> PARA O LADO</div></div>' +
    ft(P('perfil-antes'), 0, 580, 538, 770, .45, .5) + ft(P('perfil-depois'), 542, 580, 538, 770, .45, .5) +
    f'<div class="a" style="left:538px;top:580px;width:4px;height:770px;background:{CREME}"></div>' +
    gr(74, 100, .6) + rot('antes', 40, 596) + rot('depois', 582, 596) +
    aviso('rgba(255,255,255,.85)', 1176, 13) + rodape('rgba(255,255,255,.85)', 1212)))

# ---------- CARROSSEL 2 · modelo (a): frente empilhado, antes em cima / depois embaixo ----------
pecas.append(('carrossel-2', 1350,
    f'<div class="a" style="inset:0;background:{CREME}"></div>' + topo(CAFE, 60) +
    ft(P('frente-antes'), 88, 112, 904, 534, .48, .56) + ft(P('frente-depois'), 88, 654, 904, 534, .48, .56) +
    rot('antes', 112, 124, '#fff') + rot('depois', 112, 666, '#fff') +
    cro('#fff', y=1112, right=112) + rodape(CAFE, 1212)))
# (no modelo dela a tela de antes e depois não tem texto extra; o "resultados variam" vai na linha do rodapé abaixo)
pecas[-1] = (pecas[-1][0], 1350, pecas[-1][2].replace('<small>HARMONIZAÇÃO FACIAL<br>@clinica.drajacicunha</small>',
                                                     '<small>HARMONIZAÇÃO FACIAL<br>RESULTADOS VARIAM DE PESSOA PARA PESSOA</small>'))

# ---------- CARROSSEL 3 · 3/4 lado a lado com a faixa translúcida (cópia de "Preenchimento facial, por que...") ----------
pecas.append(('carrossel-3', 1350,
    ft(P('tres4-antes'), 0, 0, 538, 1350, .46, .42) + ft(P('tres4-depois'), 542, 0, 538, 1350, .46, .42) +
    '<div class="a" style="left:538px;top:0;width:4px;height:1350px;background:#fff"></div>' +
    gr(0, 14, 0, '0,0,0') + '<div class="a" style="inset:0;background:linear-gradient(180deg,rgba(0,0,0,.35) 0,rgba(0,0,0,0) 14%)"></div>' +
    gr(52, 92, .78) + topo('#fff') + rot('antes', 40, 160) + rot('depois', 582, 160) +
    '<div class="a" style="left:0;width:1080px;top:875px;text-align:center"><div class="sans" style="color:#fff;font-size:24px;letter-spacing:.24em;margin-bottom:16px">VISTA 3/4</div>'
    '<div style="padding:0 90px"><span class="faixa S" style="font-size:70px">a linha da mandíbula,</span></div>'
    '<div class="sans" style="color:#fff;font-size:34px;line-height:1.25;margin:16px auto 0;width:860px;font-weight:300">onde rosto e pescoço se <b>encontram</b> e o contorno fica mais <b>definido</b></div></div>' +
    aviso('rgba(255,255,255,.85)', 1176, 13) + rodape('rgba(255,255,255,.85)', 1212)))

# ---------- CARROSSEL 4 · tríptico narrativo (cópia de "a tela: / a artista: / a obra de arte:") ----------
def faixa_tri(y, foto, cx, cy, z, t1, t2, sub):
    return (ft(foto, 0, y, 1080, 448, cx, cy, z) +
            f'<div class="a" style="left:0;top:{y}px;width:1080px;height:448px;background:linear-gradient(90deg,rgba(0,0,0,.45) 0,rgba(0,0,0,0) 55%)"></div>'
            f'<div class="a" style="left:88px;top:{y+150}px"><div class="sans tri">{t1} <b>{t2}</b>:</div><div class="sans trs">{sub}</div></div>')
pecas.append(('carrossel-4', 1350,
    faixa_tri(0, P('perfil-antes'), .55, .63, 1.0, 'o', 'paciente', 'queria um contorno<br>mais definido') +
    faixa_tri(451, P('bastidor-cadeira'), .55, .42, 1.0, 'a', 'avaliação', 'rosto, pele e saúde<br>antes de qualquer indicação') +
    faixa_tri(902, P('perfil-depois'), .55, .63, 1.0, 'o', 'contorno', 'tratamento combinado,<br>expressão natural') +
    f'<div class="a" style="left:0;top:448px;width:1080px;height:3px;background:{CREME}"></div><div class="a" style="left:0;top:899px;width:1080px;height:3px;background:{CREME}"></div>' +
    topo('#fff', 60) + cro('#fff', y=1250, right=88, tam_=22) +
    '<div class="a avi" style="left:88px;right:auto;text-align:left;top:1290px;color:rgba(255,255,255,.85);font-size:13px">' + VARIAM + '</div>'))
# o tríptico dela não tem rodapé de 2 colunas (a foto vai até a borda); a assinatura do rodapé fica no canto da última faixa

# ---------- CARROSSEL 5 · tela informativa: "o que foi feito" (véu branco, sans bold caixa alta, checks verdes) ----------
itens = [('Lipo de papada', 'reduz a gordura embaixo do queixo'), ('Toxina botulínica', 'relaxa os músculos que puxam o contorno para baixo'),
         ('Preenchimento de mandíbula', 'desenha o ângulo do rosto'), ('Mento e pré-jowl', 'equilibram o queixo e suavizam a linha'),
         ('Bioestimulador de colágeno', 'ajuda a pele a ficar mais firme com o tempo')]
pecas.append(('carrossel-5', 1350,
    ft(f'{IDV}/consultorio.jpg', -60, -60, 1200, 1470, .5, .3, 1.0, extra='filter:blur(26px) saturate(.8)') +
    '<div class="a" style="inset:0;background:rgba(250,246,240,.74)"></div>' + topo(CAFE) +
    f'<div class="a" style="left:0;width:1080px;top:190px;text-align:center"><div class="sans" style="font-size:58px;font-weight:700;color:{CAFE};letter-spacing:.02em">O QUE FOI FEITO</div>'
    f'<div class="S" style="font-size:40px;color:{VINHO};margin-top:2px">um plano, cinco cuidados</div></div>'
    '<div class="a" style="left:150px;top:378px;width:800px">' +
    ''.join(f'<div class="ck"><i>✓</i><div><b>{a}</b><br><span>{b}</span></div></div>' for a, b in itens) + '</div>'
    f'<div class="a S" style="left:120px;width:840px;top:1052px;text-align:center;font-size:36px;color:{CAFE};line-height:1.2;font-stretch:condensed">'
    'Cada procedimento cuida de uma parte do contorno.<br><b>Juntos, no plano certo.</b></div>' +
    aviso(CAFE, 1170, 13) + rodape(CAFE, 1212)))

# ---------- CARROSSEL 6 · "o que esperar" (cópia de "Bioestimulador de Colágeno": faixa dourada com fio e pontos) ----------
pecas.append(('carrossel-6', 1350,
    ft(f'{NOVAS}/IMG_3018.jpg', 0, 0, 1080, 1350, .48, .30, 1.0, filtro=True) +
    '<div class="a" style="inset:0;background:linear-gradient(180deg,rgba(40,18,14,.25) 0,rgba(40,18,14,0) 18%,rgba(40,18,14,0) 44%,rgba(40,18,14,.82) 78%,rgba(40,18,14,.9) 100%)"></div>' +
    topo(CAFE) +
    '<div class="a" style="left:0;width:1080px;top:770px;text-align:center"><div class="sans" style="color:#fff;font-style:italic">O que você precisa <b>entender</b> sobre o</div>'
    '<div class="fio"><i></i><span class="S" style="font-size:66px">tempo do resultado</span><i></i></div>'
    '<div class="sans u" style="color:#fff">O QUE ESPERAR?</div>'
    '<div class="sans esp">Alguns efeitos aparecem nos <b>primeiros dias</b>.<br>'
    'Na lipo de papada, o resultado final aparece em <b>cerca de 6 meses</b>.<br>'
    'O bioestimulador forma colágeno <b>aos poucos</b>.<br>'
    'As fotos do depois são do <b>início do acompanhamento</b>.</div></div>' +
    aviso('rgba(255,255,255,.85)', 1176, 13) + rodape('rgba(255,255,255,.85)', 1212)))

# ---------- CARROSSEL 7 · fechamento com CTA (cópia de "Antes de qualquer procedimento, eu observo.") ----------
pecas.append(('carrossel-7', 1350,
    ft(f'{FOTOS}/jaci-off-white-sofa-sorrindo.jpg', 0, 0, 1080, 1350, .52, .40, 1.55, filtro=True) +
    '<div class="a" style="inset:0;background:rgba(58,32,24,.16);mix-blend-mode:multiply"></div>'
    '<div class="a" style="inset:0;background:linear-gradient(180deg,rgba(40,18,14,.18) 0,rgba(40,18,14,0) 20%,rgba(40,18,14,0) 46%,rgba(40,18,14,.78) 100%)"></div>' +
    topo('#fff') +
    '<div class="a" style="left:0;width:1080px;top:800px;text-align:center"><div class="sans" style="color:#fff;font-size:28px;margin-bottom:10px;font-style:italic">Antes de qualquer procedimento, <b>eu observo</b>.</div>'
    f'<div style="padding:0 80px"><span class="faixa S" style="font-size:70px;background:{CAFE}">Cada rosto tem um plano.</span></div>'
    '<div class="sans" style="color:#fff;font-size:33px;font-style:italic;font-weight:400;margin:16px auto 0;width:840px;line-height:1.3">'
    'Quer saber se esse tipo de tratamento combina com <b>você</b>? A resposta começa na <u>avaliação</u>.</div>'
    '<div class="pill">Agende sua avaliação no WhatsApp →</div></div>' +
    aviso('rgba(255,255,255,.85)', 1176, 13) + rodape('rgba(255,255,255,.85)', 1212)))

# ---------- STORY 1 · antes × depois + "Você faria?" (espaço para a enquete nativa do Instagram) ----------
pecas.append(('story-1', 1920,
    f'<div class="a" style="inset:0;background:radial-gradient(1000px 900px at 50% 30%,#86283B,{VINHO} 55%,#3E0C16)"></div>' + topo('#F3EADD', 210) +
    f'<div class="a" style="left:0;width:1080px;top:290px;text-align:center"><div class="sans" style="color:#F3EADD;font-size:26px;letter-spacing:.24em">CONTORNO FACIAL MASCULINO</div></div>' +
    ft(P('frente-antes'), 88, 350, 448, 620, .48, .48) + ft(P('frente-depois'), 544, 350, 448, 620, .48, .48) +
    f'<div class="a" style="left:88px;top:350px;width:904px;height:620px;box-shadow:0 0 0 2px {OURO}"></div>' +
    rot('antes', 88, 980, OURO, 'center', 448) + rot('depois', 544, 980, OURO, 'center', 448) +
    '<div class="a" style="left:0;width:1080px;top:1080px;text-align:center"><div class="balao" style="margin-left:420px">tratamento <b>combinado</b></div>'
    '<div class="S" style="color:#fff;font-size:150px;line-height:1">Você faria?</div>'
    '<div class="sans" style="color:#fff;margin-top:6px;font-size:28px;letter-spacing:.12em">RESPONDE <b>AQUI EMBAIXO</b> ↓</div></div>' +
    aviso('rgba(243,234,221,.8)', 1620, 15) + rodape('rgba(243,234,221,.85)', 1660)))

# ---------- STORY 2 · chamada para a avaliação (cópia de "Entramos / na reta final..." + faixas vinho) ----------
pecas.append(('story-2', 1920,
    ft(f'{FOTOS}/jaci-off-white-tablet.jpg', 0, 0, 1080, 1920, .5, .32, 1.0, filtro=True) +
    '<div class="a" style="inset:0;background:linear-gradient(180deg,rgba(0,0,0,.18) 0,rgba(0,0,0,0) 16%,rgba(0,0,0,0) 55%,rgba(0,0,0,.5) 100%)"></div>' +
    topo(CAFE, 210) +
    f'<div class="a" style="left:88px;top:300px;width:420px"><div class="sans" style="font-size:46px;font-weight:700;color:{CAFE};line-height:1.05">Cada rosto</div>'
    f'<div style="margin-top:6px"><span class="faixa S" style="font-size:84px;background:rgba(201,180,142,.85)">tem um plano.</span></div></div>'
    '<div class="a" style="right:88px;top:1190px;text-align:right"><div><span class="fv">AGENDE SUA</span></div><div><span class="fv"><b>AVALIAÇÃO</b></span></div>'
    '<div class="sans arr" style="margin-top:14px;text-shadow:0 1px 8px rgba(0,0,0,.6)">toque no <b>link</b> e fale com a clínica</div></div>' +
    aviso('rgba(255,255,255,.88)', 1620, 15) + rodape('rgba(255,255,255,.88)', 1660)))

CSS = f"""*{{margin:0;padding:0;box-sizing:border-box}} body{{background:#222}} .f{{position:relative;width:1080px;overflow:hidden;margin-bottom:20px;background:#ddd}} .a{{position:absolute}}
.S{{font-family:'Playfair Display';font-style:italic}} .sans{{font-family:Poppins;font-size:30px;letter-spacing:.01em}} .sans b{{font-weight:700}}
.topo{{left:88px;right:88px;display:flex;justify-content:space-between;font-family:Poppins;font-size:20px;letter-spacing:.02em;font-weight:400}} .topo b{{font-weight:700}}
.ok{{font-style:normal;display:inline-grid;place-items:center;width:15px;height:15px;border-radius:50%;background:#3897F0;color:#fff;font-size:9px;margin-left:6px;vertical-align:4px}}
.rod{{left:88px;right:88px;display:flex;justify-content:space-between;font-family:Poppins;font-size:17px;letter-spacing:.08em;line-height:1.25}} .rod small{{font-size:12.5px;opacity:.8;letter-spacing:.06em}}
.avi{{left:88px;right:88px;text-align:center;font-family:Poppins;letter-spacing:.04em}}
.rt{{font-size:40px;text-shadow:0 2px 10px rgba(0,0,0,.35)}} .crs{{line-height:1.05;text-shadow:0 2px 8px rgba(0,0,0,.4)}}
.logo{{left:0;width:1080px;text-align:center;font-family:'Cormorant Garamond';font-weight:500;font-size:62px;letter-spacing:.06em;
  background:linear-gradient(180deg,#F1DDB4,#C6A06A 55%,#9C7748);-webkit-background-clip:text;color:transparent}}
.logo2{{left:0;width:1080px;text-align:center;font-family:Montserrat;font-weight:600;font-size:15px;letter-spacing:.24em;color:#C6A06A}}
.fv{{display:inline-block;background:{VINHO};color:#fff;font-family:Poppins;font-size:44px;font-weight:400;padding:2px 16px;margin-top:6px;text-transform:uppercase}} .fv b{{font-weight:700}}
.arr{{color:#fff;font-size:22px;letter-spacing:.06em}}
.faixa{{display:inline;background:rgba(170,150,120,.78);color:#fff;padding:0 18px 4px;box-decoration-break:clone;-webkit-box-decoration-break:clone;line-height:1.28}}
.tri{{color:#fff;font-size:52px;font-weight:300;text-shadow:0 2px 12px rgba(0,0,0,.35)}} .tri b{{font-weight:700}}
.trs{{color:rgba(255,255,255,.78);font-size:24px;font-weight:300;letter-spacing:.04em;margin-top:6px;line-height:1.3}}
.ck{{display:flex;gap:22px;align-items:flex-start;margin-bottom:30px;font-family:Poppins;color:{CAFE}}} .ck i{{flex:none;font-style:normal;width:44px;height:44px;border-radius:50%;border:2.5px solid #2F4A3A;color:#2F4A3A;display:grid;place-items:center;font-size:24px;font-weight:700;margin-top:4px}}
.ck b{{font-size:30px;font-weight:700;text-transform:uppercase;letter-spacing:.02em}} .ck span{{font-size:25px;font-weight:300}}
.fio{{display:flex;align-items:center;justify-content:center;margin:14px auto}} .fio span{{background:linear-gradient(90deg,rgba(185,162,122,.94),rgba(185,162,122,.8));color:#fff;padding:2px 26px 8px;max-width:840px}}
.fio i{{flex:none;width:60px;height:2px;background:{OURO};position:relative}} .fio i:first-child:before,.fio i:last-child:after{{content:"";position:absolute;top:-4px;width:10px;height:10px;border-radius:50%;background:{OURO}}} .fio i:first-child:before{{left:-4px}} .fio i:last-child:after{{right:-4px}}
.u{{text-decoration:underline;text-underline-offset:6px}} .esp{{color:#fff;font-size:26px;font-weight:300;line-height:1.5;margin-top:22px}}
.balao{{display:inline-block;background:#fff;color:#222;font-family:Poppins;font-size:28px;line-height:1.15;padding:12px 24px;border-radius:18px;position:relative;margin-bottom:-6px}} .balao b{{font-weight:700}}
.balao:after{{content:"";position:absolute;left:30px;bottom:-12px;border:8px solid transparent;border-top-color:#fff;border-left-color:#fff}}
.pill{{display:inline-block;margin-top:30px;border:2px solid #fff;border-radius:999px;padding:12px 30px;font-family:Poppins;font-size:24px;color:#fff}}
.jc{{filter:saturate(.9) sepia(.07) contrast(1.03)}}
"""
html = (f'<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@1,400;1,500;1,600;1,700'
        f'&family=Poppins:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400;1,600&family=Cormorant+Garamond:wght@500;600&family=Montserrat:wght@600&display=swap" rel="stylesheet">'
        f'<style>{CSS}</style></head><body>' + ''.join(f'<section class="f" id="{i}" style="height:{h}px">{c}</section>' for i, h, c in pecas) + '</body></html>')
open(f'{OUT}/_tmp/artes.html', 'w').write(html)

JS = """const {chromium}=require('playwright');(async()=>{const [h,o]=process.argv.slice(1);const b=await chromium.launch();
const p=await b.newPage({viewport:{width:1100,height:2000},deviceScaleFactor:2});await p.goto('file://'+h,{waitUntil:'networkidle'});
await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(600);
for(const el of await p.$$('section.f'))await el.screenshot({path:o+'/'+(await el.getAttribute('id'))+'@2x.png'});await b.close()})();"""
subprocess.run(['node', '-e', JS, f'{OUT}/_tmp/artes.html', f'{OUT}/_tmp'], check=True, cwd=AQUI)
for i, h, _ in pecas:   # renderiza em 2x e reduz para 1080 de largura (texto e fio mais nítidos)
    Image.open(f'{OUT}/_tmp/{i}@2x.png').convert('RGB').resize((1080, h), Image.LANCZOS).save(f'{OUT}/{i}.jpg', quality=93)

# prévia: post + 7 telas do carrossel (2 linhas de 4) + 2 stories ao lado
w, hh, g = 432, 540, 16
fe = ['post-perfil'] + [f'carrossel-{k}' for k in range(1, 8)]
sh = Image.new('RGB', (4 * (w + g) + g + 2 * (432 + g), 2 * (hh + g) + g + 44), '#EFE7DC')
for k, n in enumerate(fe): sh.paste(Image.open(f'{OUT}/{n}.jpg').resize((w, hh), Image.LANCZOS), (g + (k % 4) * (w + g), g + (k // 4) * (hh + g)))
for k, n in enumerate(['story-1', 'story-2']):
    im = Image.open(f'{OUT}/{n}.jpg'); im = im.resize((432, 768), Image.LANCZOS); sh.paste(im, (g + 4 * (w + g) + k * (432 + g), g))
try: fnt = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 18)
except Exception: fnt = None
ImageDraw.Draw(sh).text((g, sh.height - 34), 'Dra. Jaci Cunha · Prova social "Contorno facial masculino" v2 (no estilo dela) · post + carrossel 7 telas + 2 stories · 07/11/2026', fill='#5A4033', font=fnt)
sh.save(f'{OUT}/previa.jpg', quality=88)
import shutil; shutil.rmtree(f'{OUT}/_tmp')   # temporários (2x, logo recortada, html com caminhos locais) não vão para o Git
print('ok', len(pecas), 'peças em', OUT)
