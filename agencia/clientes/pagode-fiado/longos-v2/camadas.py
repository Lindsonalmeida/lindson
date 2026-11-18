# Camadas gráficas (PNG transparente) de um vídeo longo do Pagode Fiado v2, na identidade do canal.
# Uso: python3 camadas.py <faixa> <pasta_trabalho>  ->  <pasta>/cam<faixa>/paginas.json (depois: node render.js <pasta>/cam<faixa>)
import json, sys, os, html, base64
K, W = sys.argv[1], sys.argv[2]; AQUI = os.path.dirname(os.path.abspath(__file__))
L = json.load(open(AQUI + '/letras.json')); F = L[K]
OUT = f'{W}/cam{K}'; os.makedirs(OUT, exist_ok=True)
Y, V, P, C, R, AZ = '#F2B705', '#1E6B52', '#111111', '#F3E9D2', '#C0392B', '#1C3A86'
FONTES = "@import url('https://fonts.googleapis.com/css2?family=Shrikhand&family=Caveat+Brush&family=Permanent+Marker&family=Work+Sans:wght@500;600;700;800&display=block');"
BASE = FONTES + "*{margin:0;box-sizing:border-box}html,body{width:1920px;height:1080px;background:transparent;overflow:hidden}"
e = html.escape
def b64(p): return 'data:image/png;base64,' + base64.b64encode(open(p, 'rb').read()).decode()
LOGO = b64(f'{W}/img/marca-dagua-150.png')
def pg(nome, corpo, css='', sel=None): return dict(nome=nome, sel=sel, html=f'<html><head><style>{BASE}{css}</style></head><body>{corpo}</body></html>')
pags = []
ORDEM = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10']
prox = ORDEM[ORDEM.index(K) + 1] if K != '10' else None
num = 'Prólogo' if K == '00' else f'Faixa {K}'
# 1) HUD fixo: selo do canal (marca d'água oficial) e a faixa no canto
pags.append(pg('hud', f'''<img src="{LOGO}" style="position:absolute;left:54px;top:42px;width:118px;filter:drop-shadow(0 6px 14px rgba(0,0,0,.45))">
<div style="position:absolute;right:58px;top:52px;text-align:right;text-shadow:0 2px 12px rgba(0,0,0,.75)">
<div style="font:800 15px 'Work Sans';letter-spacing:.34em;color:{Y}">AO VIVO NO BAR DO SEU TIÃO</div>
<div style="font:400 34px Shrikhand;color:{C};margin-top:4px">{e(F["titulo"])}</div>
<div style="font:400 24px 'Caveat Brush';color:{C};opacity:.85">{e(num)} · Álbum 01 · Copo Americano</div></div>'''))
# 2) tira de caderno com a letra: base (lápis) e caneta (palavras já cantadas)
CSS_TIRA = f""".t{{display:inline-block;position:absolute;left:0;top:0;max-width:1640px;padding:16px 52px 22px 74px;background:{C};
background-image:linear-gradient(90deg,transparent 50px,{R}99 50px,{R}99 53px,transparent 53px),repeating-linear-gradient({C} 0 54px,#A9C1DE 54px 56px);
border-radius:4px;box-shadow:0 16px 36px rgba(0,0,0,.55)}}
.t .q{{font:800 19px 'Work Sans';letter-spacing:.2em;color:{R};text-transform:uppercase;margin-bottom:2px}}
.t .x{{font:400 62px/1.06 'Caveat Brush';white-space:nowrap}} .w{{display:inline-block}}"""
vistos = {}
for li, (parte, quem, txt) in enumerate(F['linhas']):
    chave = (quem if parte == 'Fala' or K == '04' else '') + '|' + txt
    if chave in vistos: continue
    vistos[chave] = li
    q = ''
    if parte == 'Fala': q = f'<div class="q">{e(quem)} fala</div>'
    elif K == '04' and quem in ('Davi', 'Lívia (Bia)'): q = f'<div class="q">{e(quem.replace(" (Bia)", ""))}</div>'
    elif K == '10' and quem in ('Davi', 'Bia', 'Juninho', 'Neguinho'): q = f'<div class="q">{e(quem)}</div>'
    pal = ' '.join(f'<span class="w">{e(w)}</span>' for w in txt.split())
    for cor, suf in (('#8E887C', 'a'), (AZ, 'b')):
        pags.append(pg(f'l{li:02d}{suf}', f'<div class="t">{q}<div class="x" style="color:{cor}">{pal}</div></div>', CSS_TIRA, '.t'))
json.dump({k: v for k, v in vistos.items()}, open(f'{OUT}/tiras.json', 'w'), ensure_ascii=False)
# 3) etiquetas de nome (personagens)
GENTE = {'davi': ('Davi Lua', 'vocal · Madureira'), 'neguinho': ('Neguinho do Cavaco', 'cavaquinho · Osasco'), 'rafa': ('Rafa Tantã', 'tantã · Salvador'),
         'juninho': ('Juninho Banjo', 'banjo e segunda voz · BH'), 'ze': ('Mestre Zé Pandeiro', 'pandeiro · Vila Isabel'), 'bia': ('Bia Rebolo', 'rebolo e vocal · Recife'),
         'tiao': ('Seu Tião', 'dono do bar e da conta')}
for k, (n, f) in GENTE.items():
    pags.append(pg(f'n_{k}', f'''<div class="n" style="display:inline-block;position:absolute;left:0;top:0;padding:6px 4px 10px">
<div style="font:400 50px/1 Shrikhand;color:{C};text-shadow:0 4px 16px rgba(0,0,0,.8)">{e(n)}</div>
<div style="height:6px;width:120px;background:{Y};margin:12px 0 10px;border-radius:3px"></div>
<div style="font:700 19px 'Work Sans';letter-spacing:.22em;color:{Y};text-transform:uppercase;text-shadow:0 2px 10px rgba(0,0,0,.9)">{e(f)}</div></div>''', '', '.n'))
# 3b) moldura de foto (polaroide com fita) para o layout "retrato": janela transparente do tamanho da foto
JANELA = {'davi': (512, 760)}
for k, (n, f) in GENTE.items():
    fw, fh = JANELA.get(k, (618, 760)); b, bb = 18, 78
    pags.append(pg(f'm_{k}', f'''<div class="m" style="position:absolute;left:0;top:0;width:{fw + 2 * b}px;height:{fh + b + bb}px">
<div style="position:absolute;left:0;top:0;right:0;height:{b}px;background:#F6F1E4"></div>
<div style="position:absolute;left:0;top:{b}px;width:{b}px;height:{fh}px;background:#F6F1E4"></div>
<div style="position:absolute;right:0;top:{b}px;width:{b}px;height:{fh}px;background:#F6F1E4"></div>
<div style="position:absolute;left:0;right:0;bottom:0;height:{bb}px;background:#F6F1E4;display:flex;align-items:center;padding-left:26px">
<span style="font:400 44px 'Caveat Brush';color:{AZ}">{e(n)}</span><span style="font:400 30px 'Caveat Brush';color:{R};margin-left:16px">{e(f.split(' · ')[0])}</span></div>
<div style="position:absolute;left:50%;top:2px;width:170px;height:40px;margin-left:-85px;background:rgba(236,226,196,.82);transform:rotate(-3deg);box-shadow:0 2px 6px rgba(0,0,0,.18)"></div></div>''', '', '.m'))
# 4) abertura: quadro-negro do Seu Tião com a faixa escrita a giz
GIZ = "filter:url(#giz)"
SVG = '<svg width="0" height="0" style="position:absolute"><filter id="giz"><feTurbulence type="fractalNoise" baseFrequency="1.1" numOctaves="2" result="n"/><feColorMatrix in="n" type="matrix" values="0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 -2.1 1.35" result="m"/><feComposite in="SourceGraphic" in2="m" operator="in"/></filter></svg>'
tit = F['titulo']
pags.append(pg('abre_q', f'''{SVG}<div style="position:absolute;inset:0;background:radial-gradient(ellipse at 50% 46%,rgba(17,17,17,.15),rgba(17,17,17,.78) 70%)"></div>
<div style="position:absolute;left:50%;top:50%;width:1180px;transform:translate(-50%,-50%) rotate(-1.6deg);background:#1d2420;
background-image:radial-gradient(ellipse at 30% 20%,rgba(255,255,255,.07),transparent 60%),radial-gradient(ellipse at 80% 85%,rgba(255,255,255,.05),transparent 55%);
border:26px solid #7A4E2A;border-radius:6px;box-shadow:0 50px 110px rgba(0,0,0,.85),inset 0 0 70px rgba(0,0,0,.65);padding:46px 70px 54px;text-align:center">
<div style="{GIZ};font:400 112px/1 'Permanent Marker';color:#F4F1E6;letter-spacing:.04em">FIADO</div>
<div style="{GIZ};height:5px;width:420px;margin:14px auto 24px;background:#F4F1E6;border-radius:3px;transform:rotate(-1deg)"></div>
<div style="{GIZ};font:400 44px 'Caveat Brush';color:{Y}">{e(num)} · Álbum 01 · Copo Americano</div>
<div style="{GIZ};font:400 118px/1.02 'Caveat Brush';color:#F4F1E6;margin-top:10px">{e(tit)}</div>
<div style="{GIZ};font:400 40px/1.25 'Caveat Brush';color:#F4F1E6;opacity:.92;margin:22px auto 0;max-width:900px">{e(F["historia"])}</div>
<div style="{GIZ};font:400 30px 'Caveat Brush';color:{Y};margin-top:26px;opacity:.95">Pagode Fiado · ao vivo no Bar do Seu Tião</div></div>'''))
# 5) fecho: próximo capítulo (sobre a capa do canal, sem cobrir o logo do centro)
if prox:
    nf = L[prox]; nt = f'Faixa {prox} · {nf["titulo"]}'; lb = 'Próximo capítulo'
else:
    nt = 'Fim do Álbum 01 · Copo Americano'; lb = 'Obrigado por ouvir'
pags.append(pg('fim', f'''<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,0) 55%,rgba(0,0,0,.7) 100%)"></div>
<div style="position:absolute;left:50%;top:812px;transform:translateX(-50%) rotate(-1deg);background:{C};padding:16px 48px 20px 72px;border-radius:4px;
background-image:linear-gradient(90deg,transparent 50px,{R}99 50px,{R}99 53px,transparent 53px),repeating-linear-gradient({C} 0 52px,#A9C1DE 52px 54px);box-shadow:0 18px 40px rgba(0,0,0,.6);white-space:nowrap;text-align:center">
<div style="font:800 18px 'Work Sans';letter-spacing:.24em;color:{R};text-transform:uppercase">{e(lb)}</div>
<div style="font:400 64px/1.05 'Caveat Brush';color:{AZ}">{e(nt)}</div></div>
<div style="position:absolute;left:0;right:0;top:996px;text-align:center;font:800 20px 'Work Sans';letter-spacing:.28em;color:{Y};text-shadow:0 2px 10px #000">PENDURA NA CONTA · INSCREVA-SE · @PAGODEFIADO</div>'''))
# 6) luz quente vazando (VFX dos cortes)
pags.append(pg('luz', '<div style="position:absolute;inset:0;background:radial-gradient(circle at 88% 16%,rgba(255,176,64,.95),rgba(255,120,30,.5) 28%,transparent 60%),radial-gradient(circle at 8% 92%,rgba(242,183,5,.55),transparent 42%)"></div>'))
json.dump(pags, open(f'{OUT}/paginas.json', 'w'), ensure_ascii=False)
print(K, len(pags))
