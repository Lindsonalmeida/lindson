# Capas dos Reels (1080x1920) e posts das datas (1080x1350) da Dra. Jaci, novembro/2026 (conta Leandro, 04/11/2026).
# Nada se cria, tudo se copia: cada composição copia um post real dela (../instagram-estilo/README.md), as mesmas dos carrosséis de ../instagram-nov/.
# Reels: a arte inteira fica dentro da faixa central 4:5 (y 285–1635), que é o que aparece na grade do perfil.
# Uso: python3 gerar.py <pasta das fotos hd> && node render.js
import sys, json, re, os
from PIL import Image, ImageStat
F = sys.argv[1]; T = json.load(open('textos.json'))
VINHO, OURO, CAFE, CREME = '#6E1A2A', '#B9A27A', '#5A4033', '#F3EADD'
def md(s):
    s = str(s).replace('\n', '<br>'); s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s); return re.sub(r'_(.+?)_', r'<i class="S">\1</i>', s)
FEED = bool(os.environ.get('FEED'))
SOBE = {'IMG_3013.jpg', 'IMG_3051.jpg', 'IMG_3010.jpg', 'IMG_3026.jpg', 'IMG_3009.jpg', 'IMG_3035.jpg', 'IMG_3023.jpg', 'IMG_3052.jpg', 'IMG_3014.jpg'}  # close: no 4:5 a foto sobe para o texto ficar no peito
def foto(arq, pos='50% 22%', extra=''):
    if FEED and arq in SOBE and pos == '50% 22%': pos = '50% 78%'
    return f'<img class="a bg" src="{F}/{arq}" style="object-position:{pos};{extra}">'
def topo_base(z, cor='#fff'):
    return f'<div class="a topo" style="top:{z+96}px;color:{cor}"><span><b>CLINICA.</b>DRA<b>JACI</b>CUNHA<i class="ok">✓</i></span><span>CIRURGIÃ-DENTISTA</span><span>@clinica.dra<b>jaci</b>cunha</span></div>'
def rodape(z, cor='#fff', centro=True):
    if centro: return f'<div class="a rod c" style="top:{z+1232}px;color:{cor}">CLÍNICA DRA. JACI CUNHA · CRO-MA 8514<br><small>AV. MILITAR, EM FRENTE À PRAÇA DO VIVA - ZÉ DOCA/MA.</small></div>'
    return (f'<div class="a rod" style="top:{z+1210}px;color:{cor}"><div>DRA JACI CUNHA<br><small>HARMONIZAÇÃO FACIAL<br>CRO-MA 8514</small></div>'
            f'<div style="text-align:right">CLÍNICA DRA. JACI CUNHA<br><small>AV. MILITAR, EM FRENTE À PRAÇA<br>DO VIVA - ZÉ DOCA/MA.</small></div></div>')
def veu_base(de=40, ate=.55): return f'<div class="a" style="inset:0;background:linear-gradient(180deg,rgba(0,0,0,0) {de}%,rgba(0,0,0,{ate}) 100%)"></div>'
def selo(c, cor='#fff'):  # "REELS" ou data, pequeno, para a pessoa saber o que é
    return ''
def luz(arq, y0, y1):  # brilho médio (0-255) de uma faixa da foto, para escolher a cor da assinatura e a força do véu
    im = Image.open(f'{F}/{arq}').convert('L'); w, h = im.size; return ImageStat.Stat(im.crop((0, int(h*y0), w, int(h*y1)))).mean[0]
def arte(c, H):
    z = (H - 1350) // 2; f = c['foto'] + '.jpg'; k = c['comp']; t = c
    zt = z + (110 if H == 1350 else 0)  # no feed 4:5 o texto desce para não cobrir o rosto
    # feed harmônico (pedido do Lindson 04/11): xadrez claro/escuro na grade, mesma correção de cor em todas as fotos
    global topo, veu
    def topo(z, cor='#fff', _t=topo_base): return _t(z, cor)
    if c.get('tom') == 'claro':
        def veu(de=40, ate=.55): return f'<div class="a" style="inset:0;background:linear-gradient(180deg,rgba(243,234,221,0) {de-5}%,rgba(243,234,221,{min(ate+.3,.88)}) 92%)"></div>'
    else:
        def veu(de=40, ate=.55): return (f'<div class="a" style="inset:0;background:rgba(58,32,24,.2);mix-blend-mode:multiply"></div>'
                                          f'<div class="a" style="inset:0;background:linear-gradient(180deg,rgba(40,18,14,.15) 0,rgba(40,18,14,0) 25%,rgba(40,18,14,0) {de}%,rgba(40,18,14,{ate+.2}) 100%)"></div>')
    if k == 'balao':   # cópia de "botox · As PERGUNTAS que você pensa mas não faz · O QUE NINGUÉM RESPONDE"
        big = len(t['serif']) < 12
        return (foto(f) + veu(45, .55) + topo(z) +
          f'<div class="a" style="left:0;width:1080px;top:{zt+760}px;text-align:center"><div class="balao">{md(t["topo"])}</div>'
          f'<div class="S" style="color:#fff;font-size:{(200 if len(t['serif'])<7 else 160) if big else 120}px;line-height:{.9 if big else 1};padding:0 70px">{t["serif"]}</div>'
          f'<div class="sans" style="color:#fff;margin-top:8px;font-size:34px">{md(t["sans"])}</div></div>' + rodape(z))
    if k == 'fio':     # cópia de "O que você precisa entender sobre · Bioestimulador de Colágeno (faixa dourada com fio) · QUANDO COMEÇAR?"
        return (foto(f) + veu(48, .55) + topo(z, OURO) +
          f'<div class="a" style="left:0;width:1080px;top:{zt+840}px;text-align:center"><div class="sans" style="color:#fff;font-style:italic">{md(t["topo"])}</div>'
          f'<div class="fio"><i></i><span class="S" style="font-size:{66 if len(t["serif"]) < 24 else 54}px">{md(t["serif"]).replace('<i class="S">','<u style="text-decoration:none;font-weight:700">').replace('</i>','</u>')}</span><i></i></div><div class="sans u" style="color:#fff">{md(t["sans"])}</div></div>' + rodape(z))
    if k == 'faixa':   # cópia de "Preenchimento facial, (faixa translúcida) por que alguns ficam artificiais e outros tão naturais?"
        return (foto(f) + veu(38, .55) + topo(z) +
          f'<div class="a" style="left:0;width:1080px;top:{zt+740}px;text-align:center"><div class="sans" style="color:#fff;font-size:26px;letter-spacing:.2em;margin-bottom:18px">{md(t["topo"])}</div>'
          f'<div style="padding:0 90px"><span class="faixa S" style="font-size:70px">{t["serif"]}</span></div>'
          f'<div class="sans" style="color:#fff;font-size:38px;line-height:1.25;margin:18px auto 0;width:860px;font-weight:300">{md(t["sans"])}</div></div>' + rodape(z))
    if k == 'faixas':  # cópia de "Entramos na reta final do ano... · E EU SEMPRE AVISO (faixas vinho)"
        return (foto(f, '62% 22%') + '<div class="a" style="inset:0;background:linear-gradient(0deg,rgba(0,0,0,.38) 0,rgba(0,0,0,0) 38%)"></div>' + topo(z, CAFE) +
          f'<div class="a" style="left:96px;top:{z+250}px;width:560px"><span class="fv" style="font-weight:700;text-transform:none;font-size:40px">{md(t["topo"])}</span><div style="margin-top:8px"><span class="faixa S" style="font-size:80px;background:rgba(201,180,142,.85)">{md(t["serif"]).replace("<i class=\"S\">","").replace("</i>","")}</span></div></div>'
          f'<div class="a" style="right:96px;top:{z+990}px;text-align:right">' + ''.join(f'<div><span class="fv">{md(x)}</span></div>' for x in t["sans"].split(" / ")) + '</div>' + rodape(z, '#fff', False))
    if k == 'tablet':  # cópia de "checklist do pós botox": palavra gigante fina + faixa vinho
        return (foto(f) + veu(50, .5) + topo(z) +
          f'<div class="a" style="left:0;width:1080px;top:{zt+700}px;text-align:center"><div class="sans" style="color:#fff;font-size:26px;letter-spacing:.24em">{md(t["topo"])}</div>'
          f'<div class="S" style="color:#fff;font-size:{230 if len(t['serif'])<7 else 175}px;line-height:.95;font-weight:400">{t["serif"]}</div>'
          f'<span class="fv" style="font-size:46px;text-transform:none">{md(t["sans"])}</span></div>' + rodape(z))
    if k == 'frases':  # cópia de "frases que eu amo ouvir!": depoimentos em volta + título com faixa caramelo
        # sem depoimento inventado: frases são da própria Dra. ou dúvidas comuns (depoimento real só com TCLE)
        fr = {'r04': ['gente **daqui**', 'orgulho de **Zé Doca**', 'feito com **carinho**'],
              'r07': ['"vai ficar **natural**?"', '"dói?"', '"e se eu não **gostar**?"'],
              'r16': ['obrigada pela **confiança**', 'cada **sorriso** conta', 'dezembro **chegando**']}.get(c['id'], [])
        pos = [(70, 520, 'left'), (640, 600, 'right'), (70, 1050, 'left')]
        return (foto(f) + veu(55, .5) + topo(z) +
          ''.join(f'<div class="a S dep" style="left:{x}px;top:{z+y}px;text-align:{al}">{md(s)}</div>' for s, (x, y, al) in zip(fr, pos)) +
          f'<div class="a" style="left:0;width:1080px;top:{zt+700}px;text-align:center"><div class="sans" style="color:#fff;font-size:30px;margin-bottom:6px">{md(t["topo"])}</div>'
          f'<span class="faixa S" style="font-size:96px;background:rgba(201,180,142,.82)">{md(t["serif"]).replace("<i class=\"S\">","").replace("</i>","")}</span>'
          f'<div class="sans" style="color:#fff;font-size:32px;margin-top:16px">{md(t["sans"])}</div></div>' + rodape(z))
    if k == 'cafe':    # cópia de "Antes de qualquer procedimento, eu observo." (faixa café + sans itálico + pílula com seta)
        return (foto(f) + veu(42, .55) + topo(z) +
          f'<div class="a" style="left:0;width:1080px;top:{zt+760}px;text-align:center"><div class="sans" style="color:#fff;font-size:28px;margin-bottom:10px;font-style:italic">{md(t["topo"])}</div>'
          f'<div style="padding:0 80px"><span class="faixa S" style="font-size:66px;background:{CAFE};opacity:.95">{t["serif"]}</span></div>'
          f'<div class="sans" style="color:#fff;font-size:34px;font-style:italic;font-weight:400;margin:16px auto 0;width:820px;line-height:1.3">{md(t["sans"])}</div>'
          f'<div class="pill">Chame no WhatsApp →</div></div>' + rodape(z))
    if k == 'invertido':  # cópia do tríptico "a artista:" (foto nítida dividida) em cor invertida vinho (faixas vinho de "E EU SEMPRE AVISO")
        return (f'<div class="a" style="inset:0;background:radial-gradient(900px 900px at 25% 40%,#86283B,{VINHO} 60%,#4A0F1B)"></div>'
          f'<img class="a" src="{F}/{f}" style="right:0;top:0;width:520px;height:{H}px;object-fit:cover;object-position:50% 22%">' + topo(z, '#F3EADD') +
          f'<div class="a" style="left:96px;width:470px;top:{z+250}px;height:900px;display:flex;flex-direction:column;justify-content:center;color:#F7EFE6">'
          f'<div class="sans" style="font-size:24px;letter-spacing:.24em;color:{OURO};margin-bottom:24px">{md(t["topo"])}</div>'
          f'<div class="S" style="font-size:{78 if len(t["serif"]) < 26 else 58}px;line-height:1.05;border-left:4px solid {OURO};padding-left:26px">{md(t["serif"]).replace("<i class=\"S\">","<span style=\"color:"+OURO+"\">").replace("</i>","</span>")}</div>'
          f'<div class="sans" style="font-size:32px;margin-top:30px;line-height:1.3">{md(t["sans"])}</div></div>' + rodape(z, '#F3EADD', False))
    raise SystemExit('composição? ' + k)
secs = []
for c in T:
    H = 1350 if os.environ.get('FEED') or c['tipo'] != 'reels' else 1920
    h = arte(c, H)
    if c.get('tom') == 'claro': h = h.replace('color:#fff', 'color:#5A4033').replace('color:#F3EADD', 'color:#5A4033')
    secs.append(f'<section class="f {c.get("tom", "")}" id="{c["id"]}" style="height:{H}px">{h}</section>')
open('artes.html', 'w').write(f"""<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@1,400;1,500;1,600;1,700&family=Poppins:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400;1,600&display=swap" rel="stylesheet">
<style>*{{margin:0;padding:0;box-sizing:border-box}} body{{background:#222}} .f{{position:relative;width:1080px;overflow:hidden;margin-bottom:20px;background:#ddd}} .a{{position:absolute}}
.bg{{inset:0;width:100%;height:100%;object-fit:cover}} .S{{font-family:'Playfair Display';font-style:italic}} .sans{{font-family:Poppins;font-size:30px;letter-spacing:.01em}} .sans b{{font-weight:700}}
.topo{{left:88px;right:88px;display:flex;justify-content:space-between;font-family:Poppins;font-size:20px;letter-spacing:.02em;font-weight:400}} .topo b{{font-weight:700}} .ok{{font-style:normal;display:inline-grid;place-items:center;width:15px;height:15px;border-radius:50%;background:#3897F0;color:#fff;font-size:9px;margin-left:6px;vertical-align:4px}}
.rod{{left:88px;right:88px;display:flex;justify-content:space-between;font-family:Poppins;font-size:17px;letter-spacing:.08em;line-height:1.25}} .rod small{{font-size:12.5px;opacity:.8;letter-spacing:.06em}} .rod.c{{display:block;text-align:center}}
.balao{{display:inline-block;background:#fff;color:#222;font-family:Poppins;font-size:26px;line-height:1.15;padding:12px 22px;border-radius:18px;position:relative;margin-left:300px;margin-bottom:-10px}} .balao b{{font-weight:700}}
.balao:after{{content:"";position:absolute;left:30px;bottom:-12px;border:8px solid transparent;border-top-color:#fff;border-left-color:#fff}} .u{{text-decoration:underline;text-underline-offset:6px}}
.fio{{display:flex;align-items:center;justify-content:center;margin:14px auto}} .fio span{{background:linear-gradient(90deg,rgba(185,162,122,.92),rgba(185,162,122,.78));color:#fff;padding:2px 26px 8px;max-width:840px}} .fio i{{flex:none;width:60px;height:2px;background:{OURO};position:relative}} .fio i:first-child:before,.fio i:last-child:after{{content:"";position:absolute;top:-4px;width:10px;height:10px;border-radius:50%;background:{OURO}}} .fio i:first-child:before{{left:-4px}} .fio i:last-child:after{{right:-4px}}
.faixa{{display:inline;background:rgba(170,150,120,.75);color:#fff;padding:0 18px 4px;box-decoration-break:clone;-webkit-box-decoration-break:clone;line-height:1.28}}
.fv{{display:inline-block;background:{VINHO};color:#fff;font-family:Poppins;font-size:44px;font-weight:400;padding:2px 16px;margin-top:6px;text-transform:uppercase}} .fv b{{font-weight:700}}
.dep{{color:#fff;font-size:40px;width:380px;line-height:1.15;text-shadow:0 2px 6px rgba(0,0,0,.55),0 0 26px rgba(0,0,0,.45)}} .dep b{{font-weight:700}}
.claro .pill{{color:#5A4033;border-color:#5A4033}} .claro .dep{{text-shadow:none;color:#6E1A2A!important}} .bg{{filter:saturate(.9) sepia(.07) contrast(1.03)}} .pill{{display:inline-block;margin-top:34px;border:2px solid #fff;border-radius:999px;padding:12px 30px;font-family:Poppins;font-size:24px;color:#fff}}
</style></head><body>{''.join(secs)}</body></html>""")
print(len(secs), 'artes')
