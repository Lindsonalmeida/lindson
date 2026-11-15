# Leo Pinto · v17 · 10 posts 1080x1350 (conta Leandro, 15/11/2026) · kit v13 v3 + v14 (gerar9): Anton, Montserrat Black, Kaushan, logo, cores.
# Sem foto livre do Leo (todas já usadas, ver ../FOTOS-USADAS.md): posts tipográficos / só logo. Sem raios, faixas, ícones, fumaça ou sol.
# Uso: python3 gerar.py <pasta com assets/ e mapa-sjb.json> && node ../instagram-v14-datas/render.js <pasta>
import sys, json
d = sys.argv[1]; M = json.load(open(f'{d}/mapa-sjb.json'))
MAR, ROY, SOL, LAR, CRE = '#05316E', '#2350F5', '#FFC20E', '#FF7A1A', '#FFF6E8'
GRAO = ("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'>"
        "<filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='3' stitchTiles='stitch'/>"
        "<feColorMatrix values='0 0 0 0 .5  0 0 0 0 .5  0 0 0 0 .5  0 0 0 .9 0'/></filter><rect width='100%25' height='100%25' filter='url(%23n)'/></svg>")
LARANJA = f'radial-gradient(1000px 900px at 30% 22%,#FFC84A 0,#FFA526 28%,#FF8A1F 52%,{LAR} 74%,#E8590C 100%)'
AZUL = f'radial-gradient(1100px 1000px at 40% 30%,#4A78FF 0,#2E5BFA 26%,{ROY} 46%,#1539BE 72%,#082063 100%)'
MARINHO = f'radial-gradient(1100px 900px at 70% 20%,#123E8C 0,#082063 55%,#041640 100%)'
CREME = f'radial-gradient(1000px 900px at 30% 20%,#FFFFFF 0,{CRE} 60%,#FBE6C8 100%)'
AMAR = f'radial-gradient(1000px 900px at 30% 20%,#FFE066 0,{SOL} 55%,#F5A800 100%)'
SPLIT = f'linear-gradient(180deg,{LAR} 0,#FF8A1F 50%,{MAR} 50%,#082063 100%)'
CLAROS = (LARANJA, CREME, AMAR)
def mapa(x, y, w, cor='#BFD8FF', op=.30):
    s = w/1000
    return (f'<svg class="a" style="left:0;top:0" width="1080" height="1350"><g transform="translate({x},{y}) scale({s})">'
            f'<polygon points="{M["pts"]}" fill="{cor}" fill-opacity="{op*.5}" stroke="{cor}" stroke-opacity="{op*1.4}" stroke-width="{2/s}" stroke-linejoin="round"/></g></svg>')
H = lambda t, fs, cor='#fff', ex='': f'<div class="H" style="font-size:{fs}px;color:{cor};{ex}">{t}</div>'
def cx(t, fundo, cor, fs, ex=''): return f'<div class="box" style="background:{fundo};color:{cor};font-size:{fs}px;{ex}">{t}</div>'
GRAD = f'background:linear-gradient(180deg,#FFE066,{SOL} 45%,{LAR});-webkit-background-clip:text;background-clip:text;color:transparent'
def ASSINA(bg, logo=True, pos='left:80px;top:1150px;width:236px'):
    lg = 'logo-marinho.png' if bg in CLAROS else 'logo.png'
    return ('<div class="a pill"><img src="assets/avatar.jpg">@_leonardopinto</div>' +
            (f'<img class="a" src="assets/{lg}" style="{pos};filter:drop-shadow(0 8px 16px rgba(2,12,50,.28))">' if logo else ''))
P = []

# 1 · 19/11 Dia da Bandeira · LARANJA · data em blocos empilhados (letreiro, Kittl "campaign poster" + Dribbble "Joelle Reimer")
P.append(('v17-01-bandeira', LARANJA, f"""{mapa(420, 360, 760, '#fff', .22)}
<div class="a" style="left:80px;top:230px"><div class="L" style="font-size:24px;color:{MAR}">19 de novembro</div>
 <div style="margin-top:26px">{cx('Dia da', MAR, '#fff', 120, 'font-family:Anton;letter-spacing:.01em')}</div>
 <div style="margin-top:14px">{cx('Bandeira', '#fff', ROY, 190, 'font-family:Anton;letter-spacing:.01em')}</div></div>
<div class="a K" style="left:86px;top:760px;font-size:70px;color:#fff;width:900px;text-shadow:0 6px 20px rgba(120,40,0,.35)">orgulho de ser brasileiro<br>e são-joanense</div>
<div class="a M" style="left:86px;top:1010px;font-size:24px;color:{MAR};width:880px;line-height:1.5">Ordem e Progresso desde 1889</div>
{ASSINA(LARANJA, True, 'right:80px;top:1130px;width:250px')}"""))

# 2 · Fé · MARINHO · citação gigante centralizada (D&AD / It's Nice That: tipografia editorial em fundo escuro)
P.append(('v17-02-fe', MARINHO, f"""
<div class="a H" style="left:60px;top:150px;font-size:420px;line-height:1;{GRAD}">“</div>
<div class="a" style="left:90px;top:420px;width:900px">
 {H('Entrega o teu', 110, '#fff')}{H('caminho', 170, '#fff', GRAD + ';margin-top:6px')}{H('ao Senhor', 110, '#fff', 'margin-top:6px')}</div>
<div class="a M" style="left:94px;top:880px;font-size:26px;color:#BFD8FF;letter-spacing:.3em">Salmos 37:5</div>
<div class="a K" style="left:90px;top:960px;font-size:58px;color:{SOL}">boa semana, São João Batista</div>
{ASSINA(MARINHO, True, 'right:80px;top:1150px;width:220px')}"""))

# 3 · Cidade · AZUL · mapa oficial gigante + nome da cidade (Koto: marca de lugar com forma real)
P.append(('v17-03-cidade', AZUL, f"""{mapa(60, 120, 1100, '#BFD8FF', .34)}{mapa(90, 150, 1100, '#BFD8FF', .12)}
<div class="a" style="left:80px;top:250px"><div class="L" style="font-size:24px;color:{SOL}">Baixada Maranhense</div></div>
<div class="a" style="left:76px;top:720px">{H('São João', 170, '#fff')}{H('Batista', 230, '#fff', GRAD + ';margin-top:4px')}</div>
<div class="a K" style="left:84px;top:1150px;font-size:56px;color:#fff">a terra que eu amo</div>
{ASSINA(AZUL, True, 'right:80px;top:1150px;width:220px')}"""))

# 4 · 26/11 Ação de Graças · CREME · palavra repetida em contorno + uma cheia (GDJ "brutalist typography posters")
rep = ''.join(f'<div class="H" style="font-size:250px;line-height:.86;color:transparent;-webkit-text-stroke:3px rgba(35,80,245,.28)">Obrigado</div>' for _ in range(2))
P.append(('v17-04-acao-de-gracas', CREME, f"""
<div class="a" style="left:70px;top:150px">{rep}{H('Obrigado', 250, ROY, 'line-height:.86')}{rep[:len(rep)//2]}</div>
<div class="a" style="left:80px;top:1010px">{cx('26/11 · Dia de Ação de Graças', LAR, '#fff', 44)}</div>
<div class="a K" style="left:84px;top:1110px;font-size:52px;color:{MAR}">por cada povoado,<br>por cada família</div>
{ASSINA(CREME, True, 'right:80px;top:1160px;width:210px')}"""))

# 5 · Cultura · AMARELO · palavra gigante sangrando nas bordas (Designi "vereador" + GDUSA tipografia de campanha)
P.append(('v17-05-cultura', AMAR, f"""
<div class="a H" style="left:-40px;top:300px;font-size:360px;color:{MAR};letter-spacing:-.01em">Baixada</div>
<div class="a" style="left:80px;top:210px"><div class="L" style="font-size:24px;color:{MAR}">nossa cultura</div></div>
<div class="a" style="left:80px;top:690px;display:flex;flex-direction:column;gap:14px;align-items:flex-start">
 {cx('é fé', ROY, '#fff', 70)}{cx('é festa', '#fff', ROY, 70)}{cx('é a nossa gente', LAR, '#fff', 70)}</div>
<div class="a K" style="left:84px;top:1015px;font-size:56px;color:{MAR}">orgulho de ser do Maranhão</div>
{ASSINA(AMAR, True, 'right:80px;top:1150px;width:220px')}"""))

# 6 · 03/12 Pessoas com Deficiência · AZUL · cartão branco central (Dribbble "political social media", cartões de interface)
P.append(('v17-06-inclusao', AZUL, f"""{mapa(500, 700, 700, '#BFD8FF', .2)}
<div class="a" style="left:0;width:1080px;top:190px;text-align:center"><div class="L" style="font-size:24px;color:{SOL}">3 de dezembro</div>
 {H('Inclusão', 170, '#fff', 'margin-top:34px')}<div style="margin-top:8px">{cx('se faz junto', SOL, MAR, 74, 'font-family:Anton;letter-spacing:.01em')}</div></div>
<div class="a card" style="left:150px;top:640px;width:780px">
 <div class="M" style="font-size:22px;color:{LAR};letter-spacing:.24em">Dia Internacional das Pessoas com Deficiência</div>
 <div class="lista"><div class="li"><b>01</b>Respeite a vaga e a rampa</div><div class="li"><b>02</b>Pergunte antes de ajudar</div><div class="li"><b>03</b>Respeite o tempo do outro</div></div></div>
<div class="a K" style="left:0;width:1080px;top:1060px;text-align:center;font-size:54px;color:#fff">ninguém fica para trás</div>
{ASSINA(AZUL, True, 'left:422px;top:1170px;width:236px')}"""))

# 7 · Saudação da semana · SPLIT laranja/marinho · tela dividida (Kittl "campaign poster" duas cores)
P.append(('v17-07-boa-semana', SPLIT, f"""
<div class="a" style="left:80px;top:250px">{H('Bora', 200, '#fff')}{H('trabalhar', 200, MAR, 'margin-top:4px')}</div>
<div class="a" style="left:80px;top:720px">{H('com fé', 160, SOL)}{H('e alegria', 160, '#fff', 'margin-top:4px')}</div>
<div class="a K" style="left:86px;top:1090px;font-size:54px;color:#fff">uma ótima semana pra você!</div>
{ASSINA(MARINHO, True, 'right:80px;top:1160px;width:200px')}"""))

# 8 · 08/12 Dia da Família · MARINHO · palavra gigante vertical + data em bloco (It's Nice That, cartaz editorial)
P.append(('v17-08-familia', MARINHO, f"""
<div class="a H vert" style="left:40px;top:1300px;font-size:300px;{GRAD}">Família</div>
<div class="a" style="left:420px;top:250px;width:600px"><div class="L" style="font-size:24px;color:{SOL}">8 de dezembro</div>
 {H('Dia da', 110, '#fff', 'margin-top:18px')}{H('Família', 150, '#fff', 'margin-top:4px')}</div>
<div class="a K" style="left:420px;top:620px;font-size:64px;color:{SOL};width:600px">é a nossa maior riqueza</div>
<div class="a" style="left:420px;top:830px;width:560px;font:600 32px/1.4 Montserrat;color:#DCE6FF">Dia de Nossa Senhora da Conceição. Que Deus abençoe cada lar de São João Batista.</div>
{ASSINA(MARINHO, True, 'left:420px;top:1130px;width:236px')}"""))

# 9 · Conte sempre comigo · BRANCO (CREME) · nome em blocos de cor do v13 v3 + frase (padrão aprovado)
P.append(('v17-09-conte-comigo', 'linear-gradient(180deg,#FFFFFF,#EEF3FF)', f"""{mapa(380, 420, 800, ROY, .14)}
<div class="a" style="left:80px;top:230px"><div class="L" style="font-size:24px;color:{ROY}">vereador de São João Batista</div>
 <div style="margin-top:26px;display:flex;gap:16px">{cx('Leo', SOL, MAR, 150)}{cx('Pinto', ROY, '#fff', 150)}</div></div>
<div class="a" style="left:80px;top:620px">{H('Conte', 190, MAR)}{H('sempre', 190, LAR)}{H('comigo', 190, MAR)}</div>
<div class="a K" style="left:86px;top:1170px;font-size:50px;color:{ROY}">do povo para o povo</div>
{ASSINA(CREME, True, 'right:80px;top:1150px;width:210px')}"""))

# 10 · Orgulho são-joanense · LARANJA · enquete de gostos (cartão branco com opções, padrão v14/v15)
P.append(('v17-10-orgulho', LARANJA, f"""
<div class="a" style="left:0;width:1080px;top:170px;text-align:center"><div class="L" style="font-size:24px;color:{MAR}">enquete</div>
 {H('O que mais', 110, '#fff', 'margin-top:14px')}<div style="margin-top:8px">{cx('te dá orgulho', MAR, '#fff', 84, 'font-family:Anton;letter-spacing:.01em')}</div>
 {H('na nossa terra?', 92, '#fff', 'margin-top:10px')}</div>
<div class="a" style="left:150px;top:610px;width:780px;background:#fff;border-radius:36px;overflow:hidden;box-shadow:0 40px 70px -30px rgba(120,40,0,.6)">
 <div style="padding:30px 34px;display:flex;flex-direction:column;gap:16px"><div class="op"><b>1</b>A festa do povoado</div><div class="op"><b>2</b>O peixe do lago</div><div class="op"><b>3</b>O futebol de domingo</div><div class="op"><b>4</b>A fé da nossa gente</div></div></div>
<div class="a K" style="left:0;width:1080px;top:1060px;text-align:center;font-size:50px;color:#fff">comenta o número aqui embaixo</div>
{ASSINA(LARANJA, True, 'left:422px;top:1160px;width:236px')}"""))

secs = ''.join(f'<section class="f" id="{i}" style="background:{bg}">{c}<div class="a" style="inset:0;background-image:url(&quot;{GRAO}&quot;);opacity:.10;mix-blend-mode:overlay;pointer-events:none"></div></section>' for i, bg, c in P)
html = f"""<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Anton&family=Kaushan+Script&family=Montserrat:wght@600;700;800;900&display=swap" rel="stylesheet">
<style>*{{margin:0;padding:0;box-sizing:border-box}} body{{background:#222}}
.f{{position:relative;width:1080px;height:1350px;overflow:hidden;margin-bottom:20px}} .a{{position:absolute}}
.K{{font-family:'Kaushan Script';line-height:1.08}} .box{{font-family:Montserrat;font-weight:900;text-transform:uppercase;letter-spacing:-.02em;display:inline-block;white-space:nowrap;padding:10px 22px 4px;line-height:1;box-shadow:0 20px 34px -20px rgba(2,12,50,.7)}}
.L,.M{{font-family:Montserrat;font-weight:700;text-transform:uppercase;letter-spacing:.3em}} .M{{letter-spacing:.08em}}
.H{{font-family:Anton;text-transform:uppercase;line-height:.9;white-space:nowrap;letter-spacing:.005em}}
.vert{{transform:rotate(-90deg);transform-origin:left top;line-height:1}}
.card{{background:#fff;border-radius:30px;padding:40px 38px 36px;box-shadow:0 40px 70px -30px rgba(2,12,50,.55)}}
.lista{{margin-top:26px;display:flex;flex-direction:column;gap:20px}} .li{{display:flex;align-items:center;gap:18px;font-family:Montserrat;font-weight:800;font-size:28px;white-space:nowrap;color:{MAR};text-transform:uppercase}}
.li b{{font-weight:900;font-size:58px;color:{ROY};letter-spacing:-.04em;min-width:86px}}
.op{{display:flex;align-items:center;gap:16px;border:2.5px solid {ROY};border-radius:16px;padding:12px 16px;font-family:Montserrat;font-weight:800;font-size:30px;color:{MAR};text-transform:uppercase}}
.op b{{display:grid;place-items:center;width:46px;height:46px;border-radius:50%;background:{ROY};color:#fff;font-size:24px}}
.pill{{left:76px;top:62px;display:flex;align-items:center;gap:12px;background:rgba(255,255,255,.92);border-radius:999px;padding:6px 20px 6px 6px;font-family:Montserrat;font-weight:700;font-size:21px;color:{MAR};box-shadow:0 10px 20px -12px rgba(2,12,50,.5)}}
.pill img{{width:46px;height:46px;border-radius:50%;object-fit:cover}}
</style></head><body>{secs}</body></html>"""
open(f'{d}/artes.html', 'w').write(html)
print(len(P), 'artes')
