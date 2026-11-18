# Gera o HTML de cada camada (PNG transparente 1920x1080) de um vídeo longo do Pagode Fiado.
# Uso: python3 overlays.py <faixa> <pasta_saida>  -> escreve paginas.json para render.js
import json, sys, os, html
K = sys.argv[1]; OUT = sys.argv[2]; os.makedirs(OUT, exist_ok=True)
AQUI = os.path.dirname(os.path.abspath(__file__))
F = json.load(open(AQUI + '/faixas.json'))[K]
LOGO = open(AQUI + '/../../../processos/brand-book-premium/pagode-fiado/logo.svg').read()
LOGO = LOGO[LOGO.index('<svg'):]
Y, V, P, C, R = '#F2B705', '#1E6B52', '#111111', '#F3E9D2', '#C0392B'
CSS = """@import url('https://fonts.googleapis.com/css2?family=Shrikhand&family=Work+Sans:wght@500;700;800&family=Permanent+Marker&family=Caveat+Brush&display=block');
*{margin:0;box-sizing:border-box}html,body{width:1920px;height:1080px;background:transparent;overflow:hidden;font-family:'Work Sans'}
.sh{font-family:Shrikhand}.mk{font-family:'Permanent Marker'}.cv{font-family:'Caveat Brush'}
.logo svg{width:100%;height:auto;display:block}"""
e = html.escape
def pg(nome, corpo): return dict(nome=nome, html=f'<html><head><style>{CSS}</style></head><body>{corpo}</body></html>')
pags = []
num, tit = K, F['titulo']
# moldura fixa
pags.append(pg('moldura', f'''
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.72) 0,rgba(0,0,0,.35) 14%,transparent 26%,transparent 58%,rgba(0,0,0,.65) 100%)"></div>
<div class="logo" style="position:absolute;left:56px;top:44px;width:150px;filter:drop-shadow(0 8px 18px rgba(0,0,0,.5))">{LOGO}</div>
<div style="position:absolute;right:60px;top:56px;text-align:right">
 <div style="font:800 17px 'Work Sans';letter-spacing:.32em;color:{Y}">AO VIVO NO BAR DO SEU TIÃO</div>
 <div class="sh" style="font-size:40px;color:{C};margin-top:6px;text-shadow:0 4px 14px #000a">{e(tit)}</div>
 <div class="cv" style="font-size:28px;color:{C};opacity:.85">faixa {num} · álbum 01 · voz {e(F['voz'])}</div></div>
<div style="position:absolute;left:0;right:0;bottom:0;height:22px;background:repeating-conic-gradient({R} 0 25%,{C} 0 50%) 0 0/44px 44px"></div>'''))
# letra: tira de caderno pautado
for i, (a, b, t) in enumerate(F['letra']):
    rot = -1.2 if i % 2 else 0.8
    pags.append(pg(f'l{i:02d}', f'''
<div style="position:absolute;left:50%;bottom:74px;transform:translateX(-50%) rotate({rot}deg);max-width:1500px;padding:20px 54px 24px 70px;
background:{C};background-image:linear-gradient(90deg,transparent 46px,{R}88 46px,{R}88 49px,transparent 49px),repeating-linear-gradient({C} 0 52px,#9DB8D9 52px 54px);
box-shadow:0 18px 40px rgba(0,0,0,.55);border-radius:3px">
<div class="cv" style="font-size:64px;line-height:1.05;color:{P};white-space:nowrap">{e(t)}</div></div>'''))
# carimbos de parte
for i, (a, t) in enumerate(F['partes']):
    pags.append(pg(f'p{i}', f'''<div class="mk" style="position:absolute;left:120px;bottom:210px;transform:rotate(-8deg);border:5px solid {R};color:{R};
background:{C}e6;padding:4px 22px;font-size:40px;letter-spacing:.06em;text-transform:uppercase">{e(t)}</div>'''))
# abertura: quadro FIADO
pags.append(pg('abertura', f'''
<div style="position:absolute;inset:0;background:radial-gradient(ellipse at center,rgba(17,17,17,.35),rgba(17,17,17,.9))"></div>
<div style="position:absolute;left:50%;top:50%;transform:translate(-50%,-52%) rotate(-3deg);background:{P};border:22px solid #8B5A2B;
box-shadow:0 40px 90px #000c, inset 0 0 60px #0009;padding:50px 90px 56px;text-align:center;min-width:1040px">
 <div class="mk" style="font-size:118px;color:{C};line-height:1">FIADO</div>
 <div class="cv" style="font-size:44px;color:{Y};margin-top:6px">mesa 7 · sexta · pendura na conta</div>
 <div style="height:3px;background:{C}55;margin:26px 0"></div>
 <div class="sh" style="font-size:96px;color:{C};line-height:1"><span style="color:{Y}">{num}</span> · {e(tit)}</div>
 <div class="cv" style="font-size:40px;color:{C};opacity:.8;margin-top:18px">Pagode Fiado · ao vivo no Bar do Seu Tião · voz {e(F['voz'])}</div></div>'''))
# encerramento
pags.append(pg('fim', f'''
<div style="position:absolute;inset:0;background:{V};background-image:linear-gradient(#ffffff1c 2px,transparent 2px),linear-gradient(90deg,#ffffff1c 2px,transparent 2px);background-size:120px 120px"></div>
<div style="position:absolute;inset:0;background:radial-gradient(ellipse at center,transparent 40%,rgba(0,0,0,.55))"></div>
<div class="logo" style="position:absolute;left:50%;top:150px;transform:translateX(-50%) rotate(-3deg);width:500px;border-radius:26px;overflow:hidden;box-shadow:0 30px 70px #000a">{LOGO}</div>
<div class="cv" style="position:absolute;left:0;right:0;top:700px;text-align:center;font-size:96px;color:{C};text-shadow:0 6px 20px #0008">Pendura na conta.</div>
<div style="position:absolute;left:0;right:0;top:830px;text-align:center;font:700 26px 'Work Sans';letter-spacing:.24em;color:{Y}">ÁLBUM 01 · INSCREVA-SE E ATIVE O SININHO · @PAGODEFIADO</div>
<div style="position:absolute;left:0;right:0;bottom:0;height:60px;background:repeating-conic-gradient({R} 0 25%,{C} 0 50%) 0 0/60px 60px"></div>'''))
# luz vazando (VFX nos cortes)
pags.append(pg('luz', '''<div style="position:absolute;inset:0;background:radial-gradient(circle at 92% 18%,rgba(255,170,60,.85),rgba(255,120,30,.45) 30%,transparent 62%),radial-gradient(circle at 6% 90%,rgba(242,183,5,.5),transparent 45%)"></div>'''))
json.dump(pags, open(OUT + '/paginas.json', 'w'), ensure_ascii=False)
print(len(pags))
