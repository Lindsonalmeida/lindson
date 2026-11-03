# Carrosséis de novembro da Dra. Jaci Cunha · cópia das composições dos posts reais dela (instagram-estilo/README.md).
# Nada se cria, tudo se copia: cada capa copia um post dela (comentário em cada uma). Fotos: ../fotos (estúdio). Conta Lindson, 03/11/2026.
import sys, json, re
d, F = sys.argv[1], sys.argv[2]   # pasta de trabalho, pasta das fotos
T = json.load(open(f'{d}/textos.json'))
VINHO, OURO, CAFE, CREME = '#6E1A2A', '#B9A27A', '#5A4033', '#F3EADD'
def md(s):  # **bold** e _itálico serif_
    s = str(s).replace('\n', '<br>')
    s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s); return re.sub(r'_(.+?)_', r'<i class="S">\1</i>', s)
def foto(arq, pos='50% 30%', extra=''): return f'<img class="a bg" src="{F}/{arq}" style="object-position:{pos};{extra}">'
def topo(cor='#fff'):
    return (f'<div class="a topo" style="color:{cor}"><span><b>CLINICA.</b>DRA<b>JACI</b>CUNHA<i class="ok">✓</i></span><span>CIRURGIÃ-DENTISTA</span><span>@clinica.dra<b>jaci</b>cunha</span></div>')
def rodape(cor='#fff', centro=False):
    if centro: return f'<div class="a rod c" style="color:{cor}">CLÍNICA DRA. JACI CUNHA<br><small>AV. MILITAR, EM FRENTE À PRAÇA DO VIVA - ZÉ DOCA/MA.</small></div>'
    return (f'<div class="a rod" style="color:{cor}"><div>DRA JACI CUNHA<br><small>HARMONIZAÇÃO FACIAL<br>@clinica.drajacicunha</small></div>'
            f'<div style="text-align:right">CLÍNICA DRA. JACI CUNHA<br><small>AV. MILITAR, EM FRENTE À PRAÇA<br>DO VIVA - ZÉ DOCA/MA.</small></div></div>')
def pontos(i, n, cor='#fff'): return f'<div class="a dots">{"".join(f"<i style=\'background:{cor};opacity:{1 if k == i else .4}\'></i>" for k in range(n))}</div>'
ARR = '<div class="a arr" style="color:{c}"><b>ARRASTE</b> PARA O LADO</div>'
# capas: cada uma copia um post real dela
def capa(cid, t):
    t = dict(t, sans=t['sans'].split('\n')[0].strip())
    if cid == 'c1':   # cópia de "botox · As PERGUNTAS que você pensa mas não faz · O QUE NINGUÉM RESPONDE"
        return (foto('jaci-preto-mao-no-cabelo.jpg', '50% 20%') + '<div class="a" style="inset:0;background:linear-gradient(180deg,rgba(0,0,0,0) 45%,rgba(0,0,0,.45) 100%)"></div>' + topo() +
          f'<div class="a" style="left:0;width:1080px;top:770px;text-align:center"><div class="balao">{md(t.get("topo",""))}</div><div class="S big" style="color:#fff;font-size:{190 if len(t["serif"]) < 12 else 104}px;line-height:{.9 if len(t["serif"]) < 12 else 1.0};padding:0 70px">{t["serif"]}</div>'
          f'<div class="sans" style="color:#fff;margin-top:6px">{md(t["sans"])}</div></div>' + ARR.format(c='#fff'))
    if cid == 'c2':   # cópia de "O que você precisa entender sobre · Bioestimulador de Colágeno (faixa dourada com fio) · QUANDO COMEÇAR?"
        return (foto('jaci-off-white-frasco-botox.jpg', '50% 25%') + '<div class="a" style="inset:0;background:linear-gradient(180deg,rgba(0,0,0,0) 50%,rgba(0,0,0,.45) 100%)"></div>' + topo(OURO) +
          f'<div class="a" style="left:0;width:1080px;top:830px;text-align:center"><div class="sans" style="color:#fff;font-style:italic">{md(t.get("topo",""))}</div>'
          f'<div class="fio"><i></i><span class="S" style="font-size:66px">{t["serif"]}</span><i></i></div><div class="sans u" style="color:#fff">{md(t["sans"])}</div></div>' + rodape('#fff', True))
    if cid == 'c3':   # cópia de "Preenchimento facial, (faixa translúcida) por que alguns ficam artificiais e outros tão naturais? · ARRASTA PARA O LADO"
        return (foto('jaci-preto-sorriso-aberto.jpg', '50% 20%') + '<div class="a" style="inset:0;background:linear-gradient(180deg,rgba(0,0,0,0) 40%,rgba(0,0,0,.5) 100%)"></div>' + topo() +
          f'<div class="a" style="left:0;width:1080px;top:760px;text-align:center"><span class="faixa S" style="font-size:72px">{t["serif"]}</span>'
          f'<div class="sans" style="color:#fff;font-size:40px;line-height:1.2;margin-top:10px;font-weight:400">{md(t["sans"])}</div>'
          f'<div class="sans u" style="color:#fff;margin-top:60px;font-size:24px;font-style:italic">ARRASTA PARA O <b>LADO</b></div></div>' + rodape('#fff', True))
    if cid == 'c4':   # cópia de "Entramos na reta final do ano... · E EU SEMPRE AVISO (faixas vinho) · ARRASTE PARA O LADO"
        return (foto('jaci-off-white-sofa-sorrindo.jpg', '75% 20%') + '<div class="a" style="inset:0;background:linear-gradient(0deg,rgba(0,0,0,.35) 0,rgba(0,0,0,0) 35%)"></div>' + topo(CAFE) +
          f'<div class="a" style="left:96px;top:300px;width:400px;color:{CAFE}"><div class="sans" style="font-size:40px;font-weight:700">{md(t.get("topo",""))}</div><div class="S" style="font-size:78px;line-height:1">{t["serif"]}</div></div>'
          f'<div class="a" style="right:96px;top:1010px;text-align:right">' + ''.join(f'<div><span class="fv">{md(x)}</span></div>' for x in t["sans"].split(" / ")) +
          f'<div class="arr2"><b>ARRASTE</b> PARA O LADO</div></div>' + rodape())
BGS = {'c1': 'jaci-preto-rennova-sorrindo.jpg', 'c2': 'jaci-off-white-tablet.jpg', 'c3': 'jaci-nude-sofa-corpo-inteiro.jpg', 'c4': 'jaci-branco-cadeira-sorrindo.jpg'}
def interna(cid, t, i, n):  # cópia de "SEU BOTOX, DIA APÓS DIA" (foto desfocada com véu claro, título sans caps, checks, nota serif)
    base = foto(BGS[cid], '50% 30%', 'filter:blur(6px) saturate(.7);transform:scale(1.06)') + '<div class="a" style="inset:0;background:rgba(232,226,216,.72)"></div>' + topo(CAFE)
    if t['tipo'] == 'lista':
        corpo = f'<div class="tit">{md(t["titulo"])}</div>' + ''.join(f'<div class="li"><i>✓</i><span>{md(x)}</span></div>' for x in t['itens'])
    elif t['tipo'] == 'mito':
        corpo = (f'<div class="tit">{md(t.get("titulo","MITO OU VERDADE?"))}</div><div class="mv"><span class="fv">MITO</span><p>{md(t["mito"])}</p></div>'
                 f'<div class="mv"><span class="fv" style="background:{OURO}">VERDADE</span><p>{md(t["verdade"])}</p></div>')
    else:
        corpo = f'<div class="tit">{md(t["titulo"])}</div><p class="tx">{md(t.get("texto",""))}</p>'
    nota = f'<div class="S nota">{t["nota"]}</div>' if t.get('nota') else ''
    return base + f'<div class="a" style="left:130px;width:820px;top:200px;height:930px;display:flex;flex-direction:column;justify-content:center;color:{CAFE}"><div>{corpo}{nota}</div></div>' + pontos(i, n, CAFE) + rodape(CAFE)
def fim(cid, t, i, n):  # cópia de "Antes de qualquer procedimento, eu observo." (faixa café com serif itálica, sans itálico com bold, pílula com seta)
    return (foto('jaci-off-white-tablet.jpg' if cid in ('c1', 'c3') else 'jaci-preto-mao-no-cabelo.jpg', '50% 25%') + '<div class="a" style="inset:0;background:linear-gradient(180deg,rgba(0,0,0,0) 45%,rgba(0,0,0,.5) 100%)"></div>' + topo() +
      f'<div class="a" style="left:0;width:1080px;top:760px;text-align:center"><span class="faixa S" style="font-size:60px;background:{CAFE};opacity:.95">{t["serif"]}</span>'
      f'<div class="sans" style="color:#fff;font-size:34px;font-style:italic;font-weight:400;margin:16px auto 0;width:820px;line-height:1.3">{md(t["sans"])}</div>'
      f'<div class="pill">Chame no WhatsApp →</div></div>' + rodape('#fff', True))
secs = []
for cid in ['c1', 'c2', 'c3', 'c4']:
    telas = T[cid]['telas']; n = len(telas)
    for i, t in enumerate(telas):
        html = capa(cid, t) if t['tipo'] == 'capa' else fim(cid, t, i, n) if t['tipo'] == 'fim' else interna(cid, t, i, n)
        secs.append(f'<section class="f" id="{cid}-{i+1}">{html}</section>')
open(f'{d}/artes.html', 'w').write(f"""<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@1,400;1,500;1,600;1,700&family=Poppins:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400;1,600&display=swap" rel="stylesheet">
<style>*{{margin:0;padding:0;box-sizing:border-box}} body{{background:#222}} .f{{position:relative;width:1080px;height:1350px;overflow:hidden;margin-bottom:20px;background:#ddd}} .a{{position:absolute}}
.bg{{inset:0;width:1080px;height:1350px;object-fit:cover}} .S{{font-family:'Playfair Display';font-style:italic}} .sans{{font-family:Poppins;font-size:30px;letter-spacing:.01em}} .sans b{{font-weight:700}}
.topo{{left:88px;right:88px;top:96px;display:flex;justify-content:space-between;font-family:Poppins;font-size:20px;letter-spacing:.02em;font-weight:400}} .topo b{{font-weight:700}} .ok{{font-style:normal;display:inline-grid;place-items:center;width:15px;height:15px;border-radius:50%;background:#3897F0;color:#fff;font-size:9px;margin-left:6px;vertical-align:4px}}
.rod{{left:88px;right:88px;top:1210px;display:flex;justify-content:space-between;font-family:Poppins;font-size:17px;letter-spacing:.08em;line-height:1.25}} .rod small{{font-size:12.5px;opacity:.75;letter-spacing:.06em}} .rod.c{{display:block;text-align:center;top:1240px}}
.big{{font-size:190px;line-height:.9;font-weight:400}} .balao{{display:inline-block;background:#fff;color:#222;font-family:Poppins;font-size:24px;line-height:1.15;padding:12px 22px;border-radius:18px;position:relative;margin-left:340px;margin-bottom:-14px}} .balao b{{font-weight:700}}
.balao:after{{content:"";position:absolute;left:30px;bottom:-12px;border:8px solid transparent;border-top-color:#fff;border-left-color:#fff}}
.arr{{left:88px;top:1210px;font-family:Poppins;font-size:22px}} .arr b,.arr2 b{{font-weight:700}} .arr2{{font-family:Poppins;font-size:20px;color:#fff;margin-top:12px}} .u{{text-decoration:underline;text-underline-offset:6px}}
.fio{{display:flex;align-items:center;justify-content:center;gap:0;margin:12px auto}} .fio span{{background:linear-gradient(90deg,rgba(185,162,122,.9),rgba(185,162,122,.75));color:#fff;padding:2px 26px 8px}} .fio i{{width:60px;height:2px;background:{OURO};position:relative}} .fio i:first-child:before,.fio i:last-child:after{{content:"";position:absolute;top:-4px;width:10px;height:10px;border-radius:50%;background:{OURO}}} .fio i:first-child:before{{left:-4px}} .fio i:last-child:after{{right:-4px}}
.faixa{{display:inline;background:rgba(170,150,120,.72);color:#fff;padding:0 18px 4px;box-decoration-break:clone;-webkit-box-decoration-break:clone;line-height:1.25}}
.fv{{display:inline-block;background:{VINHO};color:#fff;font-family:Poppins;font-size:44px;font-weight:400;padding:2px 16px;margin-top:6px;letter-spacing:.01em;text-transform:uppercase}} .fv b{{font-weight:700}}
.tit{{font-family:Poppins;font-weight:700;font-size:56px;line-height:1.1;text-transform:uppercase;text-align:center;margin-bottom:40px}} .tit b{{font-weight:800}}
.li{{display:flex;gap:24px;align-items:flex-start;font-family:Poppins;font-size:37px;line-height:1.25;margin-bottom:34px}} .li i{{flex:none;display:grid;place-items:center;width:46px;height:46px;border:2.5px solid #2F5B3A;border-radius:50%;color:#2F5B3A;font-style:normal;font-size:24px;margin-top:-2px}} .li b{{font-weight:700}}
.tx{{font-family:Poppins;font-size:42px;line-height:1.35;text-align:center}} .tx b{{font-weight:700}} .nota{{font-size:30px;text-align:center;margin-top:40px;line-height:1.2}}
.mv{{margin-bottom:38px;text-align:center}} .mv .fv{{font-size:40px}} .mv p{{font-family:Poppins;font-size:36px;line-height:1.3;margin-top:14px}} .mv b{{font-weight:700}}
.pill{{display:inline-block;margin-top:34px;border:2px solid #fff;border-radius:999px;padding:12px 30px;font-family:Poppins;font-size:24px;color:#fff;letter-spacing:.02em}}
.dots{{right:88px;top:1170px;display:flex;gap:8px}} .dots i{{width:12px;height:12px;border-radius:50%;display:block}}
</style></head><body>{''.join(secs)}</body></html>""")
print(len(secs), 'telas')
