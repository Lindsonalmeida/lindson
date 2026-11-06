# Prova social "Contorno facial masculino" da Dra. Jaci Cunha (conta Leandro, 06/11/2026).
# Mesma identidade e acabamento dos carrosséis aprovados de novembro (instagram-nov/gerar.py): Playfair Display itálica + Poppins,
# vinho #6E1A2A, ouro #B9A27A, café #5A4033, creme #F3EADD, assinatura fixa no topo e no rodapé.
# Referências (TEMPLATE.md): A = RxPhoto/PatientNow (padrão clínico: mesmo ângulo, mesmo tamanho, rótulos ANTES/DEPOIS),
# B = Biles Hendry · Story Aesthetics (UK: editorial sóbrio, serif + sans, muito respiro), C = Seon Clinic/LAIN (KR: fotos em moldura, numeração).
# Uso: python3 gerar.py <pasta privada da entrega> <pasta identidade/v2/img>   (fotos em <pasta>/fotos, gera <pasta>/artes.html)
import sys
D, LOGO = sys.argv[1], sys.argv[2]
F = f'{D}/fotos'
VINHO, OURO, CAFE, CREME, NUDE = '#6E1A2A', '#B9A27A', '#5A4033', '#F3EADD', '#E9DCCF'
OBRIG = 'Resultados variam de pessoa para pessoa. Imagens autorizadas pelo paciente.'
ASSIN = 'Dra. Jaci Cunha · CRO-MA 8514'

def topo(cor='#fff'):
    return (f'<div class="a topo" style="color:{cor}"><span><b>CLINICA.</b>DRA<b>JACI</b>CUNHA<i class="ok">✓</i></span>'
            f'<span>CIRURGIÃ-DENTISTA</span><span>@clinica.dra<b>jaci</b>cunha</span></div>')
def aviso(cor, top=1236, h=1350):  # as 3 frases obrigatórias, em toda peça com foto
    return f'<div class="a aviso" style="color:{cor};top:{top}px">{OBRIG}<br><b>{ASSIN}</b></div>'
def rodape(cor):
    return (f'<div class="a rod" style="color:{cor}"><div>DRA JACI CUNHA<br><small>HARMONIZAÇÃO OROFACIAL<br>CRO-MA 8514</small></div>'
            f'<div style="text-align:right">CLÍNICA DRA. JACI CUNHA<br><small>AV. MILITAR, EM FRENTE À PRAÇA<br>DO VIVA - ZÉ DOCA/MA.</small></div></div>')
def pontos(i, n, cor):
    return f'<div class="a dots">{"".join(f"<i style=\'background:{cor};opacity:{1 if k == i else .35}\'></i>" for k in range(n))}</div>'
def img(arq, x, y, w, h, pos='50% 40%', extra=''):
    return f'<img class="a" src="{F}/{arq}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;object-fit:cover;object-position:{pos};{extra}">'
def rot(txt, x, y, cor, fundo):  # rótulo ANTES / DEPOIS
    return f'<div class="a rot" style="left:{x}px;top:{y}px;color:{cor};background:{fundo}">{txt}</div>'
def par(ang, x, y, w, h, gap, pos, lab_y=None, lab_c=('#fff', CAFE), borda=''):
    """antes x depois do MESMO ângulo, mesmo tamanho e o mesmo recorte (object-position igual nos dois)."""
    w2 = (w - gap) // 2; ly = y + h - 70 if lab_y is None else lab_y
    return (img(f'{ang}-antes.jpg', x, y, w2, h, pos, borda) + img(f'{ang}-depois.jpg', x + w2 + gap, y, w2, h, pos, borda) +
            rot('ANTES', x + 24, ly, *lab_c) + rot('DEPOIS', x + w2 + gap + 24, ly, *lab_c))
N = 7
# ---------- carrossel ----------
def t1():  # CAPA · faixa escura com o título no topo (referência B) + perfil x perfil sangrando embaixo, rótulos clínicos (referência A)
    return (f'<div class="a" style="inset:0;background:linear-gradient(180deg,#2A0A10,{VINHO})"></div>' +
            par('perfil', 0, 380, 1080, 970, 6, '74% 0%', lab_y=414, lab_c=(CAFE, 'rgba(243,234,221,.92)')) +
            '<div class="a" style="left:537px;top:380px;width:6px;height:970px;background:#F3EADD"></div>'
            '<div class="a" style="left:0;top:1080px;width:1080px;height:270px;background:linear-gradient(180deg,rgba(42,10,16,0),rgba(42,10,16,.85))"></div>' + topo('#F3EADD') +
            f'<div class="a" style="left:0;width:1080px;top:168px;text-align:center"><span class="faixa S" style="font-size:80px">Contorno facial masculino</span>'
            '<div class="sans" style="color:#F7EFE6;font-size:30px;line-height:1.25;margin-top:16px;font-weight:400">papada, mandíbula e queixo: <b>tratamento combinado</b></div></div>'
            '<div class="a sans u" style="right:88px;top:1176px;color:#fff;font-size:20px;font-style:italic">ARRASTA PARA O <b>LADO</b></div>' + aviso('#fff', 1236))
def t2():  # FRENTE · creme, duas fotos em moldura (referência C) + número dourado e fio (cópia de "Bioestimulador")
    return (f'<div class="a" style="inset:0;background:{CREME}"></div>' + topo(CAFE) +
            f'<div class="a" style="left:0;width:1080px;top:168px;text-align:center"><div class="fio"><i></i><span class="S" style="font-size:54px">De frente</span><i></i></div></div>' +
            par('frente', 88, 290, 904, 640, 24, '50% 30%', borda='border-radius:4px') +
            f'<div class="a" style="left:120px;width:840px;top:972px;text-align:center;color:{CAFE}"><p class="tx" style="font-size:34px">O rosto ganha um <b>contorno mais definido</b>, '
            f'do queixo até o ângulo da mandíbula, sem perder a <b>expressão natural</b>.</p></div>' + pontos(1, N, CAFE) + aviso(CAFE, 1236))
def t3():  # 3/4 · cor invertida vinho, fotos encostadas no topo e texto com fio dourado à esquerda (cópia das faixas vinho de "E EU SEMPRE AVISO")
    return (f'<div class="a" style="inset:0;background:radial-gradient(900px 800px at 30% 80%,#86283B,{VINHO} 60%,#4A0F1B)"></div>' +
            par('tres4', 0, 0, 1080, 760, 6, '46% 34%', lab_c=(VINHO, 'rgba(243,234,221,.92)')) +
            '<div class="a" style="left:537px;top:0;width:6px;height:760px;background:#6E1A2A"></div>' +
            '<div class="a" style="left:0;top:0;width:1080px;height:230px;background:linear-gradient(180deg,rgba(0,0,0,.38),rgba(0,0,0,0))"></div>' + topo() +
            f'<div class="a sans" style="left:0;width:1080px;top:150px;text-align:center;color:#fff;font-size:20px;letter-spacing:.3em;font-weight:600">VISTA 3/4</div>' +
            f'<div class="a" style="left:110px;width:860px;top:830px;color:#F7EFE6"><div class="S" style="font-size:66px;line-height:1.05;border-left:4px solid {OURO};padding-left:26px;margin-bottom:26px">A linha da mandíbula</div>'
            f'<p class="tx" style="text-align:left;font-size:34px">No ângulo de três quartos aparece a <b>transição entre rosto e pescoço</b>, onde a papada e o pré-jowl mais pesam.</p></div>'
            + pontos(2, N, '#F3EADD') + aviso('#F3EADD', 1236))
PROC = [('Lipo de papada', 'reduz a gordura <b>embaixo do queixo</b>'),
        ('Toxina botulínica', 'relaxa músculos que <b>puxam o contorno</b> para baixo'),
        ('Preenchimento de mandíbula', 'desenha o <b>ângulo do rosto</b>'),
        ('Mento e pré-jowl', 'equilibra o <b>queixo</b> e suaviza a "quebra" da linha'),
        ('Bioestimulador de colágeno', 'ajuda a pele a ficar <b>mais firme</b> com o tempo')]
def t4():  # O QUE FOI FEITO · creme tipográfico com números dourados em lista (referência B, editorial)
    li = ''.join(f'<div class="pr"><span class="S n">{k + 1:02d}</span><div><div class="pt">{a}</div><div class="pd">{b}</div></div></div>' for k, (a, b) in enumerate(PROC))
    return (f'<div class="a" style="inset:0;background:{CREME}"></div>' + topo(CAFE) +
            f'<div class="a" style="left:110px;width:860px;top:200px;color:{CAFE}"><div class="sans" style="font-size:24px;letter-spacing:.25em;color:{OURO};font-weight:600">O QUE FOI FEITO</div>'
            f'<div class="S" style="font-size:70px;line-height:1.05;margin:10px 0 34px">5 cuidados, um plano só</div>{li}</div>' + pontos(3, N, CAFE) + rodape(CAFE))
def t5():  # BASTIDOR · foto real na cadeira, faixa café (cópia de "Antes de qualquer procedimento, eu observo")
    return (img('bastidor-cadeira.jpg', 0, 0, 1080, 1350, '60% 40%') +
            '<div class="a" style="inset:0;background:linear-gradient(180deg,rgba(0,0,0,.3) 0,rgba(0,0,0,0) 18%,rgba(0,0,0,0) 48%,rgba(0,0,0,.72) 100%)"></div>' + topo() +
            f'<div class="a" style="left:88px;width:900px;top:840px;color:#fff"><div class="sans" style="font-size:22px;letter-spacing:.25em;font-weight:600">BASTIDOR</div>'
            f'<span class="faixa S" style="font-size:62px;background:{CAFE};opacity:.95">Tudo começa na avaliação</span>'
            f'<div class="sans" style="font-size:31px;font-style:italic;font-weight:400;margin-top:18px;line-height:1.35">A Dra. Jaci analisa o rosto, a pele e a <b>saúde</b> antes de indicar qualquer procedimento.</div></div>'
            + pontos(4, N, '#fff') + aviso('#fff', 1236))
ESPERA = ['O <b>resultado varia</b> de pessoa para pessoa.',
          'Na lipo de papada, o resultado final aparece em <b>cerca de 6 meses</b>.',
          'Bioestimulador age aos poucos: o colágeno <b>leva semanas</b> para se formar.',
          'Nas fotos, o "depois" é do <b>acompanhamento inicial</b> do tratamento combinado.',
          '<b>Avaliação antes de tudo</b>: só ela diz o que faz sentido para você.']
def t6():  # O QUE ESPERAR · nude com cartão branco e checks (cópia de "Seu botox, dia após dia")
    li = ''.join(f'<div class="li"><i>✓</i><span>{x}</span></div>' for x in ESPERA)
    return (f'<div class="a" style="inset:0;background:{NUDE}"></div>' + topo(CAFE) +
            f'<div class="a" style="left:88px;width:904px;top:190px;height:960px;background:#FBF7F2;border-radius:6px;box-shadow:0 30px 60px rgba(90,64,51,.12)"></div>'
            f'<div class="a" style="left:150px;width:780px;top:250px;color:{CAFE}"><div class="tit" style="text-align:left;font-size:52px;margin-bottom:12px">O que esperar</div>'
            f'<div class="S" style="font-size:40px;color:{VINHO};margin-bottom:44px">com calma e com verdade</div>{li}</div>' + pontos(5, N, CAFE) + rodape(CAFE))
def t7():  # CHAMADA · vinho com o monograma oficial (cópia da faixa vinho + pílula do fechamento aprovado)
    return (f'<div class="a" style="inset:0;background:radial-gradient(800px 700px at 50% 30%,#86283B,{VINHO} 55%,#4A0F1B)"></div>' +
            f'<img class="a" src="{LOGO}/monograma.jpg" style="left:390px;top:170px;width:300px;height:410px;object-fit:cover;-webkit-mask-image:radial-gradient(closest-side,#000 70%,transparent);mix-blend-mode:lighten">' + topo('#F3EADD') +
            f'<div class="a" style="left:0;width:1080px;top:620px;text-align:center;color:#F7EFE6"><div class="S" style="font-size:84px;line-height:1.02">Quer entender o<br>seu contorno?</div>'
            f'<div class="sans" style="font-size:32px;margin:26px auto 0;width:820px;line-height:1.35;font-weight:400">Agende sua <b>avaliação</b> com a Dra. Jaci Cunha, aqui em Zé Doca.</div>'
            f'<div class="pill" style="border-color:{OURO};color:#fff;background:rgba(185,162,122,.18)">Chame no WhatsApp →</div></div>' + rodape('#F3EADD'))
# ---------- post único (feed) · perfil x perfil em arcos, manchete no creme (referência C + B) ----------
def post():
    return (f'<div class="a" style="inset:0;background:{CREME}"></div>' + topo(CAFE) +
            f'<div class="a" style="left:0;width:1080px;top:160px;text-align:center;color:{CAFE}"><div class="sans" style="font-size:22px;letter-spacing:.3em;color:{OURO};font-weight:600">PERFIL · ANTES × DEPOIS</div>'
            f'<div class="S" style="font-size:76px;line-height:1.02;margin-top:10px">Papada, mandíbula e queixo</div></div>' +
            img('perfil-antes.jpg', 88, 330, 440, 700, '38% 36%', 'border-radius:220px 220px 6px 6px') +
            img('perfil-depois.jpg', 552, 330, 440, 700, '38% 36%', 'border-radius:220px 220px 6px 6px') +
            rot('ANTES', 110, 966, '#fff', VINHO) + rot('DEPOIS', 574, 966, '#fff', VINHO) +
            f'<div class="a" style="left:0;width:1080px;top:1060px;text-align:center;color:{CAFE}"><div class="sans" style="font-size:30px">Contorno facial masculino · <b>tratamento combinado</b></div>'
            f'<div class="sans" style="font-size:24px;margin-top:10px;font-style:italic">Agende sua avaliação no WhatsApp</div></div>' + aviso(CAFE, 1236))
# ---------- stories 1080x1920 ----------
def story1():  # 3/4 x 3/4 empilhado + espaço livre para a figurinha de enquete "Você faria?"
    return (f'<div class="a" style="inset:0;background:radial-gradient(900px 900px at 50% 60%,#86283B,{VINHO} 55%,#4A0F1B)"></div>' +
            topo('#F3EADD').replace('top:96px', 'top:150px') +
            f'<div class="a" style="left:0;width:1080px;top:230px;text-align:center;color:#F7EFE6"><div class="S" style="font-size:72px;line-height:1">Contorno facial masculino</div>'
            f'<div class="sans" style="font-size:26px;margin-top:10px;letter-spacing:.2em">VISTA 3/4 · TRATAMENTO COMBINADO</div></div>' +
            img('tres4-antes.jpg', 80, 400, 452, 720, '46% 32%', 'border-radius:6px') + img('tres4-depois.jpg', 548, 400, 452, 720, '46% 32%', 'border-radius:6px') +
            rot('ANTES', 100, 1050, VINHO, 'rgba(243,234,221,.92)') + rot('DEPOIS', 568, 1050, VINHO, 'rgba(243,234,221,.92)') +
            f'<div class="a" style="left:0;width:1080px;top:1190px;text-align:center"><div class="S" style="font-size:96px;color:#fff">Você faria?</div>'
            f'<div class="a" style="left:240px;top:150px;width:600px;height:190px;border:2px dashed rgba(243,234,221,.35);border-radius:22px"></div>'
            f'<div class="sans" style="position:absolute;left:0;width:1080px;top:232px;font-size:20px;color:rgba(243,234,221,.45);letter-spacing:.15em">ENQUETE: SIM · QUERO SABER MAIS</div></div>' +
            aviso('#F3EADD', 1640) + f'<div class="a sans" style="left:0;width:1080px;top:1720px;text-align:center;color:{OURO};font-size:24px">Agende sua avaliação · @clinica.drajacicunha</div>')
def story2():  # frente x frente em creme + chamada com espaço para a figurinha de link
    return (f'<div class="a" style="inset:0;background:{CREME}"></div>' + topo(CAFE).replace('top:96px', 'top:150px') +
            par('frente', 80, 260, 920, 1000, 16, '50% 32%', lab_c=('#fff', VINHO), borda='border-radius:6px') +
            f'<div class="a" style="left:0;width:1080px;top:1300px;text-align:center;color:{CAFE}"><div class="fio"><i></i><span class="S" style="font-size:58px">Seu rosto merece um plano</span><i></i></div>'
            f'<div class="sans" style="font-size:32px;margin:22px auto 0;width:860px;line-height:1.35">Lipo de papada, toxina, preenchimento e bioestimulador: <b>cada caso pede uma avaliação</b>.</div>'
            f'<div class="pill" style="border-color:{VINHO};color:#fff;background:{VINHO};font-size:30px;padding:16px 40px;margin-top:40px">Agende sua avaliação →</div></div>' +
            aviso(CAFE, 1660))
PECAS = [('carrossel-1', t1), ('carrossel-2', t2), ('carrossel-3', t3), ('carrossel-4', t4), ('carrossel-5', t5), ('carrossel-6', t6), ('carrossel-7', t7),
         ('post-perfil', post), ('story-1', story1), ('story-2', story2)]
secs = ''.join(f'<section class="f{" st" if n.startswith("story") else ""}" id="{n}">{fn()}</section>' for n, fn in PECAS)
open(f'{D}/artes.html', 'w').write(f"""<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@1,400;1,500;1,600;1,700&family=Poppins:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400;1,600&display=swap" rel="stylesheet">
<style>*{{margin:0;padding:0;box-sizing:border-box}} body{{background:#222}} .f{{position:relative;width:1080px;height:1350px;overflow:hidden;margin-bottom:20px;background:#ddd}} .f.st{{height:1920px}} .a{{position:absolute}}
.S{{font-family:'Playfair Display';font-style:italic}} .sans{{font-family:Poppins;font-size:30px;letter-spacing:.01em}} .sans b{{font-weight:700}}
.topo{{left:88px;right:88px;top:96px;display:flex;justify-content:space-between;font-family:Poppins;font-size:20px;letter-spacing:.02em;font-weight:400}} .topo b{{font-weight:700}} .ok{{font-style:normal;display:inline-grid;place-items:center;width:15px;height:15px;border-radius:50%;background:#3897F0;color:#fff;font-size:9px;margin-left:6px;vertical-align:4px}}
.rod{{left:88px;right:88px;top:1210px;display:flex;justify-content:space-between;font-family:Poppins;font-size:17px;letter-spacing:.08em;line-height:1.25}} .rod small{{font-size:12.5px;opacity:.75;letter-spacing:.06em}}
.aviso{{left:0;width:1080px;text-align:center;font-family:Poppins;font-size:17px;letter-spacing:.04em;line-height:1.5}} .aviso b{{font-weight:600;letter-spacing:.12em;text-transform:uppercase;font-size:15px}}
.rot{{font-family:Poppins;font-size:20px;font-weight:600;letter-spacing:.25em;padding:8px 18px 7px;border-radius:999px}}
.u{{text-decoration:underline;text-underline-offset:6px}} .u b{{font-weight:700}}
.fio{{display:flex;align-items:center;justify-content:center;margin:12px auto}} .fio span{{background:linear-gradient(90deg,rgba(185,162,122,.9),rgba(185,162,122,.75));color:#fff;padding:2px 26px 8px}} .fio i{{width:60px;height:2px;background:{OURO};position:relative}} .fio i:first-child:before,.fio i:last-child:after{{content:"";position:absolute;top:-4px;width:10px;height:10px;border-radius:50%;background:{OURO}}} .fio i:first-child:before{{left:-4px}} .fio i:last-child:after{{right:-4px}}
.faixa{{display:inline;background:rgba(170,150,120,.78);color:#fff;padding:0 18px 4px;box-decoration-break:clone;-webkit-box-decoration-break:clone;line-height:1.25}}
.tit{{font-family:Poppins;font-weight:700;font-size:56px;line-height:1.1;text-transform:uppercase;text-align:center;margin-bottom:40px}}
.tx{{font-family:Poppins;font-size:42px;line-height:1.35;text-align:center}} .tx b{{font-weight:700}}
.pr{{display:flex;gap:30px;align-items:baseline;padding:20px 0;border-top:1px solid rgba(185,162,122,.55)}} .pr:last-child{{border-bottom:1px solid rgba(185,162,122,.55)}} .pr .n{{font-size:54px;color:{OURO};width:70px;flex:none}}
.pt{{font-family:Poppins;font-weight:700;font-size:34px;text-transform:uppercase;letter-spacing:.02em}} .pd{{font-family:Poppins;font-size:28px;margin-top:2px}} .pd b{{font-weight:700}}
.li{{display:flex;gap:24px;align-items:flex-start;font-family:Poppins;font-size:32px;line-height:1.3;margin-bottom:34px}} .li i{{flex:none;display:grid;place-items:center;width:46px;height:46px;border:2.5px solid #2F5B3A;border-radius:50%;color:#2F5B3A;font-style:normal;font-size:24px;margin-top:-2px}} .li b{{font-weight:700}}
.pill{{display:inline-block;margin-top:40px;border:2px solid #fff;border-radius:999px;padding:14px 34px;font-family:Poppins;font-size:26px;color:#fff;letter-spacing:.02em}}
.dots{{right:88px;top:1180px;display:flex;gap:8px}} .dots i{{width:12px;height:12px;border-radius:50%;display:block}}
</style></head><body>{secs}</body></html>""")
print(len(PECAS), 'peças')
