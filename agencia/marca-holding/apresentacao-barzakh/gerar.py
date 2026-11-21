# Apresentação da identidade Barzakh · 17 slides 16:9 + carrossel 4:5 (conta Leandro, 21/11/2026)
# Processo: agencia/processos/briefing-branding-identidade-visual.md (4.2 estrutura, 8.7 receitas)
# Modelo de composição: case Cajuá (Behance) · capa, moodboard, conceito 5/7, paleta em colunas, variações 2x2.
# Uso: python3 gerar.py && python3 render.py
import json, os, math
D = os.path.dirname(os.path.abspath(__file__))
B = json.load(open(os.path.join(D, 'brand.json')))
OL, OB, MA, OU, LA = '#50422A', '#0E0F12', '#EEEAE2', '#CFAE74', '#2B3A8F'
OL2 = '#5A4A2C'; OL3 = '#3F3420'
FOIL = B['colors']['accent']['foil']
GRAIN = ("url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='300'%3E%3Cfilter id='n'%3E"
         "%3CfeTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3' stitchTiles='stitch'/%3E%3CfeColorMatrix values='0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 1 0'/%3E"
         "%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E\")")

def logo(f, w, h, fill=FOIL, extra=''):
    """logo vetorial (SVG como máscara) preenchido com ouro escovado ou cor chapada"""
    import base64
    u = 'data:image/svg+xml;base64,' + base64.b64encode(open(os.path.join(D, 'assets', f), 'rb').read()).decode()
    return (f'<div style="width:{w}px;height:{h}px;background:{fill};-webkit-mask:url({u}) center/contain no-repeat;'
            f'mask:url({u}) center/contain no-repeat;{extra}"></div>')

def grain(o=.06):
    return f'<div class="gr" style="opacity:{o}"></div>'

def lab(t, c=OU):
    return f'<div class="lab" style="color:{c}">{t}</div>'

def foot(n, c='rgba(238,234,226,.55)', txt='Barzakh · Identidade visual'):
    return (f'<div class="ft" style="color:{c}"><span>{txt}</span><span>{n:02d} / 17</span></div>')

def bgol():
    return f'background:radial-gradient(ellipse 80% 90% at 50% 40%,{OL2},{OL} 55%,{OL3});'

PHOTO = 'filter:grayscale(.55) sepia(.38) contrast(1.06) brightness(.82);'

CSS = f"""
@import url('https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,400;0,9..144,500;1,9..144,300;1,9..144,400&family=Inter+Tight:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap');
*{{margin:0;padding:0;box-sizing:border-box}}
body{{background:#222;font-family:'Inter Tight',sans-serif;color:{MA}}}
section{{position:relative;overflow:hidden;margin:0 0 40px}}
.s{{width:1920px;height:1080px}}
.c{{width:1080px;height:1350px}}
.gr{{position:absolute;inset:0;background-image:{GRAIN};mix-blend-mode:overlay;pointer-events:none;z-index:50}}
.lab{{font-family:'JetBrains Mono',monospace;font-size:16px;letter-spacing:.18em;text-transform:uppercase;font-weight:500}}
.ft{{position:absolute;left:120px;right:120px;bottom:56px;display:flex;justify-content:space-between;font-family:'JetBrains Mono',monospace;font-size:14px;letter-spacing:.16em;text-transform:uppercase;z-index:40}}
.disp{{font-family:'Fraunces',serif;font-weight:300;letter-spacing:-.025em;line-height:1}}
.body{{font-size:25px;line-height:1.5;max-width:60ch}}
.ph{{position:absolute;background-size:cover;background-position:center}}
.abs{{position:absolute}}
.card{{border-radius:24px;position:relative;overflow:hidden}}
b{{font-weight:600}}
"""

S = []  # slides

# 01 CAPA · fundo oliva + grão + símbolo gigante a 6% · rótulo à esquerda · logo vertical grande à direita
S.append(f'''<section class="s" style="{bgol()}">
<div class="abs" style="left:-260px;top:-180px;opacity:.06">{logo('barzakh-simbolo-bronze.svg',1440,1440,MA)}</div>
<div class="abs" style="left:120px;top:96px">{lab('Identidade visual · 2026')}</div>
<div class="abs" style="left:120px;top:440px;width:620px"><div class="disp" style="font-size:76px;color:{MA}">A passagem<br><i style="color:{OU}">da sua marca.</i></div></div>
<div class="abs" style="left:120px;bottom:96px">{lab('Barzakh · um estúdio Al Kántara','rgba(238,234,226,.6)')}</div>
<div class="abs" style="right:150px;top:150px;width:840px;height:780px;display:flex;align-items:center;justify-content:center">
<div style="position:absolute;width:620px;height:620px;border-radius:50%;background:radial-gradient(circle,rgba(43,58,143,.35),transparent 65%);filter:blur(30px)"></div>
<img src="assets/barzakh-vertical-ouro.png" style="position:relative;width:700px;filter:drop-shadow(0 30px 50px rgba(0,0,0,.35))"></div>
{grain(.07)}</section>''')

# 02 DESAFIO · split 5/7 texto | foto full-height
S.append(f'''<section class="s" style="background:{OB}">
<div class="abs" style="left:120px;top:96px">{lab('01 · O desafio')}</div>
<div class="abs" style="left:120px;top:300px;width:640px">
<div class="disp" style="font-size:61px;color:{MA}">Um estúdio de marca precisava de uma marca <i style="color:{OU}">à altura do que entrega.</i></div>
<p class="body" style="margin-top:48px;color:rgba(238,234,226,.72);max-width:30ch">A divisão de design do Al Kántara Group nasceu sem nome próprio. O desafio: um nome raro, que soe como estúdio sério, e uma identidade que fale de <b style="color:{MA}">transformação</b> sem cair no esotérico.</p></div>
<div class="ph" style="right:0;top:0;width:1040px;height:1080px;background-image:url(fotos/panteao2.jpg);{PHOTO}"></div>
<div class="abs" style="right:0;top:0;width:1040px;height:1080px;background:linear-gradient(90deg,{OB},transparent 30%)"></div>
<div class="abs" style="right:120px;bottom:96px;color:rgba(238,234,226,.6)" ><div class="lab" style="color:rgba(238,234,226,.6);font-size:14px">Panteão, Roma · a luz que entra pelo vão</div></div>
{grain()}</section>''')

# 03 ESTRATÉGIA
def col(t, h, b):
    return f'<div style="flex:1"><div class="lab" style="color:{OL}">{t}</div><div class="disp" style="font-size:39px;color:{OB};margin:24px 0 24px;line-height:1.15">{h}</div><p style="font-size:20px;line-height:1.5;color:rgba(14,15,18,.72)">{b}</p></div>'
S.append(f'''<section class="s" style="background:{MA}">
<div class="abs" style="left:120px;top:96px">{lab('02 · Estratégia', OL)}</div>
<div class="abs" style="left:120px;top:190px;width:1400px"><div class="disp" style="font-size:95px;color:{OB}">Para quem já é bom, <i style="color:{OL}">e ainda não parece.</i></div></div>
<div class="abs" style="left:120px;right:120px;top:560px;height:1px;background:rgba(14,15,18,.2)"></div>
<div class="abs" style="left:120px;right:120px;top:608px;display:flex;gap:64px">
{col('Público','Dono de negócio local, 28 a 50 anos','Vive do boca a boca, decide pelo celular à noite e sente que a marca ficou menor que o negócio.')}
{col('Posicionamento','Sistema de marca, não só um logo','Logo, cores, letras, voz e aplicações, apresentados aplicados antes do arquivo final, com o designer no WhatsApp.')}
{col('Arquétipo','O Mago sóbrio, com o Sábio ao lado','Transforma sem prometer milagre: mostra o antes e o depois, com calma e método.')}
{col('Palavras-chave','Arco · limiar · pedra · luz rasante · ouro','O místico da arquitetura e do museu. Nunca o da tenda de cartomante.')}
</div>{foot(3,'rgba(14,15,18,.5)')}{grain(.05)}</section>''')

# 04 MOODBOARD · grade de 9 fotos, gap 8, cores harmonizadas
mb = [('ando', 'Concreto · Tadao Ando'), ('siq', 'Passagem · Siq de Petra'), ('espiral', 'Forma · escada em espiral'),
      ('colunata', 'Sombra longa · colunata'), ('panteao2', 'Luz · óculo do Panteão'), ('mar', 'Dois mares · horizonte'),
      ('aqueduto2', 'Arco · aqueduto de Segóvia'), ('langen', 'Reflexo · Langen Foundation'), ('siq2', 'Pedra · desfiladeiro')]
cells = ''
for i, (f, t) in enumerate(mb):
    cells += (f'<div style="position:relative;overflow:hidden;background:{OB}"><div class="ph" style="inset:0;background-image:url(fotos/{f}.jpg);{PHOTO}"></div>'
              f'<div class="abs" style="inset:0;background:linear-gradient(0deg,rgba(14,15,18,.6),transparent 40%)"></div>'
              f'<div class="abs lab" style="left:24px;bottom:20px;font-size:13px;color:rgba(238,234,226,.85)">{t}</div></div>')
S.append(f'''<section class="s" style="background:{OB};display:grid;grid-template-columns:1.2fr 1fr 1fr;grid-template-rows:1fr 1fr 1fr;gap:8px">
{cells}<div class="abs" style="left:0;top:0;padding:28px 32px;background:{OL};z-index:5">{lab('03 · Moodboard')}</div>{grain()}</section>''')

# 05 CONCEITO · split 5/7
S.append(f'''<section class="s" style="{bgol()}">
<div class="abs" style="left:120px;top:96px">{lab('04 · O conceito')}</div>
<div class="abs" style="left:120px;top:220px;width:640px">
<div class="disp" style="font-size:95px;color:{MA}">Dois mares,<br><i style="color:{OU}">um limiar.</i></div>
<p class="body" style="margin-top:56px;color:rgba(238,234,226,.78)"><b style="color:{OU}">Barzakh</b> é a palavra árabe para a faixa entre duas águas que se encontram sem se misturar: o limiar.</p>
<p class="body" style="margin-top:24px;color:rgba(238,234,226,.78)">O <b style="color:{MA}">arco cheio</b> vem da ponte do Al Kántara. O <b style="color:{MA}">arco em linha</b>, embaixo, é o reflexo: a marca que ainda vai tomar forma.</p>
<p class="body" style="margin-top:24px;color:rgba(238,234,226,.78)">A <b style="color:{MA}">barra</b> no meio é a passagem. É ali que o estúdio trabalha.</p></div>
<div class="ph" style="right:0;top:0;width:1040px;height:1080px;background-image:url(fotos/mar.jpg);filter:sepia(.45) brightness(.85) contrast(1.05)"></div>
<div class="abs" style="right:0;top:0;width:1040px;height:1080px;background:linear-gradient(90deg,{OL},transparent 25%)"></div>
<div class="abs" style="right:300px;top:310px;opacity:.95">{logo('barzakh-simbolo-bronze.svg',440,440)}</div>
{grain()}</section>''')

# 06 CONSTRUÇÃO · símbolo em linha fina sobre grade, cotas
k = 3.4; cx, cy = 120, 120
def arc(r, top=True):
    y0 = 113.422 if top else 126.578
    dx = math.sqrt(max(r*r - (cy - y0)**2, 0))
    sweep = 1 if top else 0
    return f'M{cx-dx},{y0} A{r},{r} 0 0 {sweep} {cx+dx},{y0}'
geo = ''
for r in [92, 80.04, 60.72, 48.76, 29.44, 86.02, 54.74]:
    geo += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{MA}" stroke-opacity=".22" stroke-width=".3" stroke-dasharray="1.2 1.2"/>'
geo += f'<line x1="0" y1="{cy}" x2="240" y2="{cy}" stroke="{MA}" stroke-opacity=".3" stroke-width=".3"/><line x1="{cx}" y1="0" x2="{cx}" y2="240" stroke="{MA}" stroke-opacity=".3" stroke-width=".3"/>'
for d in [arc(92), arc(80.04), arc(60.72), arc(48.76), arc(29.44), arc(86.02, False), arc(54.74, False), arc(29.44, False)]:
    geo += f'<path d="{d}" fill="none" stroke="{OU}" stroke-width=".7"/>'
geo += f'<rect x="11.44" y="117.24" width="217.12" height="5.53" fill="none" stroke="{OU}" stroke-width=".7"/>'
u = 11.96
cot = ''
for r, y in [(92, 20), (60.72, 50), (29.44, 80)]:
    cot += (f'<line x1="{cx}" y1="{y+4}" x2="{cx+r}" y2="{y+4}" stroke="{OU}" stroke-width=".35"/><circle cx="{cx+r}" cy="{y+4}" r=".9" fill="{OU}"/>'
            f'<text x="{cx+r+3}" y="{y+5.5}" fill="{MA}" font-size="4.2" font-family="JetBrains Mono">r = {r/u:.1f}m</text>')
S.append(f'''<section class="s" style="background:{OB}">
<div class="abs" style="left:120px;top:96px">{lab('05 · Construção')}</div>
<div class="abs" style="left:120px;top:300px;width:520px">
<div class="disp" style="font-size:61px;color:{MA}">Geometria de <i style="color:{OU}">régua e compasso.</i></div>
<p class="body" style="margin-top:40px;color:rgba(238,234,226,.72)">Um só centro. Cinco raios. O módulo <b style="color:{OU}">m</b> é a espessura do arco: todas as medidas saem dele.</p>
<div class="lab" style="margin-top:48px;color:rgba(238,234,226,.55);font-size:14px;line-height:2">m = espessura do arco<br>arcos: 7,7m · 5,1m · 2,5m<br>vão do limiar = 1,1m</div></div>
<svg class="abs" style="right:120px;top:60px" width="{240*k}" height="{240*k}" viewBox="0 0 240 240">{geo}{cot}</svg>
{foot(6)}{grain()}</section>''')

# 07 LOGO HERO
S.append(f'''<section class="s" style="{bgol()}display:flex;align-items:center;justify-content:center">
<div style="position:absolute;width:900px;height:500px;border-radius:50%;background:radial-gradient(ellipse,rgba(43,58,143,.28),transparent 65%);filter:blur(40px)"></div>
<img src="assets/barzakh-horizontal-ouro.png" style="position:relative;width:1460px;filter:drop-shadow(0 24px 40px rgba(0,0,0,.3))">
{grain(.07)}</section>''')

# 08 VARIAÇÕES 2x2
def vc(bg, inner, t, tc):
    return f'<div class="card" style="background:{bg};display:flex;align-items:center;justify-content:center">{inner}<div class="abs lab" style="left:32px;top:28px;font-size:13px;color:{tc}">{t}</div></div>'
S.append(f'''<section class="s" style="background:{OB};padding:96px 120px">
<div style="display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:24px;height:100%">
{vc(OL, logo('barzakh-horizontal-bronze.svg',620,161), 'Principal · horizontal · ouro', 'rgba(238,234,226,.6)')}
{vc('#16181D', logo('barzakh-vertical-bronze.svg',420,300), 'Secundária · vertical · ouro', 'rgba(238,234,226,.6)')}
{vc(MA, logo('barzakh-horizontal-bronze.svg',620,161,OB), 'Positiva · mono obsidiana', 'rgba(14,15,18,.55)')}
{vc(LA, logo('barzakh-simbolo-bronze.svg',260,260,MA), 'Símbolo · negativo marfim', 'rgba(238,234,226,.7)')}
</div>{grain(.05)}</section>''')

# 09 PROTEÇÃO E MÍNIMO
X = 26.24 * (1000/833)  # raio do semicírculo central no horizontal, em px na escala 1000
S.append(f'''<section class="s" style="{bgol()}">
<div class="abs" style="left:120px;top:96px">{lab('06 · Área de proteção e tamanho mínimo')}</div>
<div class="abs" style="left:120px;top:300px;width:1000px;height:259px">
<div class="abs" style="left:{-X}px;top:{-X}px;right:{-X}px;bottom:{-X}px;border:2px dashed rgba(238,234,226,.5)"></div>
<div class="abs" style="left:{-X}px;top:{-X}px;width:{X}px;height:{X}px;background:rgba(207,174,116,.25);display:flex;align-items:center;justify-content:center;font-family:'JetBrains Mono';font-size:18px;color:{OU}">X</div>
<div class="abs" style="right:{-X}px;bottom:{-X}px;width:{X}px;height:{X}px;background:rgba(207,174,116,.25);display:flex;align-items:center;justify-content:center;font-family:'JetBrains Mono';font-size:18px;color:{OU}">X</div>
{logo('barzakh-horizontal-bronze.svg',1000,259)}</div>
<p class="abs body" style="left:120px;top:690px;width:900px;color:rgba(238,234,226,.75)"><b style="color:{OU}">X</b> = raio do semicírculo central do símbolo. Nada entra nessa margem: texto, borda ou outra marca.</p>
<div class="abs" style="left:1300px;top:300px;width:500px">
<div class="lab" style="color:rgba(238,234,226,.6)">Tamanho mínimo</div>
<div style="margin-top:40px;display:flex;align-items:flex-end;gap:48px">
<div>{logo('barzakh-simbolo-bronze.svg',32,32,OU)}<div class="lab" style="margin-top:16px;font-size:12px;color:{MA}">32 px</div></div>
<div>{logo('barzakh-simbolo-bronze.svg',24,24,OU)}<div class="lab" style="margin-top:16px;font-size:12px;color:{MA}">24 px</div></div>
<div>{logo('barzakh-simbolo-bronze.svg',16,16,OU)}<div class="lab" style="margin-top:16px;font-size:12px;color:{MA}">16 px</div></div></div>
<div style="margin-top:72px;font-size:20px;line-height:2;color:rgba(238,234,226,.8)">Símbolo · <b>24 px</b> · <b>8 mm</b><br>Horizontal · <b>140 px</b> · <b>35 mm</b><br>Vertical · <b>90 px</b> · <b>22 mm</b><br>Favicon · símbolo sem a barra fina abaixo de 16 px</div></div>
{foot(9)}{grain()}</section>''')

# 10 USOS INCORRETOS 3x2
def bad(inner, t, bg='#16181D'):
    return (f'<div class="card" style="background:{bg};display:flex;align-items:center;justify-content:center">{inner}'
            f'<div class="abs" style="left:28px;bottom:24px;display:flex;align-items:center;gap:12px"><span style="color:#D2553F;font-size:22px;font-weight:600">✕</span>'
            f'<span class="lab" style="font-size:13px;color:rgba(238,234,226,.7)">{t}</span></div></div>')
H = 'barzakh-horizontal-bronze.svg'
S.append(f'''<section class="s" style="background:{OB};padding:96px 120px">
<div class="abs" style="left:120px;top:40px">{lab('07 · Usos incorretos')}</div>
<div style="display:grid;grid-template-columns:repeat(3,1fr);grid-template-rows:1fr 1fr;gap:24px;height:100%">
{bad(logo(H,420,109,extra='transform:scaleX(1.45)'),'Esticar ou achatar')}
{bad(logo(H,420,109,extra='transform:rotate(-14deg)'),'Girar')}
{bad(logo(H,420,109,'#D23A8F'),'Trocar a cor')}
{bad(f'<div style="filter:drop-shadow(10px 12px 6px rgba(0,0,0,.9))">{logo(H,420,109)}</div>','Sombra ou brilho')}
{bad(f'<div class="ph" style="inset:0;background-image:url(fotos/aqueduto2.jpg)"></div><div style="position:relative">{logo(H,420,109)}</div>','Fundo poluído')}
{bad(f'<div style="filter:drop-shadow(2px 0 0 {MA}) drop-shadow(-2px 0 0 {MA}) drop-shadow(0 2px 0 {MA}) drop-shadow(0 -2px 0 {MA})">{logo(H,420,109)}</div>','Contorno')}
</div>{grain(.05)}</section>''')

# 11 PALETA · colunas de altura total
pal = [('Oliva Limiar', OL, '80 · 66 · 42', '0 · 18 · 48 · 69', '50%', MA),
       ('Obsidiana', OB, '14 · 15 · 18', '22 · 17 · 0 · 93', '25%', MA),
       ('Marfim', MA, '238 · 234 · 226', '0 · 2 · 5 · 7', '15%', OB),
       ('Ouro Escovado', FOIL, '207 · 174 · 116', '0 · 16 · 44 · 19', '7%', OB),
       ('Lápis', LA, '43 · 58 · 143', '70 · 59 · 0 · 44', '3%', MA)]
cols = ''
for n, c, rgb, cmyk, p, tc in pal:
    hx = OU if n == 'Ouro Escovado' else c
    cols += (f'<div style="flex:{float(p[:-1])+12};background:{c};position:relative">'
             f'<div class="abs" style="left:40px;top:96px;font-family:Fraunces;font-weight:300;font-size:76px;color:{tc};opacity:.9">{p}</div>'
             f'<div class="abs" style="left:40px;bottom:96px;color:{tc}"><div class="disp" style="font-size:39px;margin-bottom:24px">{n}</div>'
             f'<div class="lab" style="font-size:13px;line-height:2;color:{tc};opacity:.8">HEX {hx}<br>RGB {rgb}<br>CMYK {cmyk}</div></div></div>')
S.append(f'''<section class="s" style="display:flex">{cols}{grain(.06)}</section>''')

# 12 TIPOGRAFIA
def tc_(f, fam, w, t, sub, extra=''):
    return (f'<div class="card" style="background:#16181D;padding:48px;flex:1"><div class="lab" style="color:{OU};font-size:13px">{t}</div>'
            f'<div style="font-family:{fam};font-weight:{w};font-size:186px;line-height:1.1;margin:32px 0;color:{MA};{extra}">Aa</div>'
            f'<div style="font-size:31px;font-family:{fam};color:{MA}">{f}</div><div style="margin-top:12px;font-size:18px;color:rgba(238,234,226,.6)">{sub}</div></div>')
S.append(f'''<section class="s" style="background:{OB}">
<div class="abs" style="left:120px;top:96px">{lab('08 · Tipografia')}</div>
<div class="abs" style="left:120px;top:170px;width:1080px;height:600px;display:flex;gap:24px">
{tc_('Fraunces Light', 'Fraunces', 300, 'Principal · títulos', 'Serifa de calma. Itálico para a palavra que importa.', 'letter-spacing:-.03em')}
{tc_('Inter Tight', "'Inter Tight'", 500, 'Secundária · texto', 'Leitura limpa no celular e no papel.')}
</div>
<div class="abs" style="left:1260px;top:170px;width:540px">
<div class="lab" style="color:rgba(238,234,226,.5);font-size:13px">Hierarquia · escala 1,25</div>
<div class="disp" style="font-size:76px;margin-top:32px">Título 76</div>
<div class="disp" style="font-size:49px;margin-top:16px;color:{OU}"><i>Subtítulo 49</i></div>
<div style="font-size:25px;margin-top:24px;line-height:1.5;color:rgba(238,234,226,.8)">Corpo 25 · Inter Tight 400, entrelinha 1,5, até 60 caracteres por linha.</div>
<div style="font-size:20px;margin-top:16px;color:rgba(238,234,226,.6)">Legenda 20</div>
<div class="lab" style="margin-top:32px;color:{OU}">Rótulo 16 · JetBrains Mono</div></div>
<div class="abs" style="left:120px;top:810px;right:120px;font-family:Fraunces;font-weight:300;font-size:49px;letter-spacing:.02em;color:rgba(238,234,226,.35)">ABCDEFGHIJKLMNOPQRSTUVWXYZ &nbsp;abcdefghijklmnopqrstuvwxyz &nbsp;0123456789</div>
{foot(12)}{grain()}</section>''')

# 13 GRAFISMOS
def gcell(inner, t):
    return f'<div class="card" style="background:rgba(238,234,226,.04);border:1px solid rgba(207,174,116,.18);display:flex;align-items:center;justify-content:center">{inner}<div class="abs lab" style="left:28px;bottom:24px;font-size:12px;color:rgba(238,234,226,.6)">{t}</div></div>'
arcos = ''.join(f'<path d="M{x},60 A30,30 0 0 1 {x+60},60" fill="none" stroke="{OU}" stroke-width="2"/><path d="M{x+6},70 A24,24 0 0 0 {x+54},70" fill="none" stroke="{OU}" stroke-width="1" opacity=".6"/>' for x in range(0, 360, 60))
selo_txt = 'A PASSAGEM DA SUA MARCA · BARZAKH · '
S.append(f'''<section class="s" style="{bgol()}padding:170px 120px 120px">
<div class="abs" style="left:120px;top:96px">{lab('09 · Grafismos')}</div>
<div style="display:grid;grid-template-columns:repeat(3,1fr);grid-template-rows:1fr 1fr;gap:24px;height:100%">
{gcell(f'<svg width="360" height="100" viewBox="0 0 360 100">{arcos}</svg>','Friso de arcos')}
{gcell(f'<svg width="300" height="200" viewBox="0 0 300 200"><line x1="0" y1="100" x2="300" y2="100" stroke="{OU}" stroke-width="3"/><path d="M90,92 A60,60 0 0 1 210,92" fill="{OU}" opacity=".9"/><path d="M90,108 A60,60 0 0 0 210,108" fill="none" stroke="{OU}" stroke-width="2"/></svg>','O limiar · linha e reflexo')}
{gcell(f'<div style="width:220px;height:300px;border-radius:110px 110px 0 0;overflow:hidden;position:relative"><div class="ph" style="inset:0;background-image:url(fotos/siq.jpg);{PHOTO}"></div></div>','Moldura em arco para foto')}
{gcell(f'<svg width="240" height="240" viewBox="0 0 240 240"><defs><path id="cc" d="M120,120 m-90,0 a90,90 0 1,1 180,0 a90,90 0 1,1 -180,0"/></defs><text font-family="JetBrains Mono" font-size="13.4" letter-spacing="3.1" fill="{OU}"><textPath href="#cc">{selo_txt}{selo_txt[:0]}</textPath></text><circle cx="120" cy="120" r="70" fill="none" stroke="{OU}" stroke-width=".8"/></svg><div class="abs">{logo("barzakh-simbolo-bronze.svg",100,100)}</div>','Selo circular')}
{gcell(f'<div style="width:300px;height:200px;background:repeating-linear-gradient(90deg,transparent 0 22px,rgba(207,174,116,.5) 22px 23px),{OB};border-radius:12px;-webkit-mask:radial-gradient(circle at 50% 100%,transparent 60px,#000 61px)"></div>','Padrão de pautas com vão')}
{gcell(logo('barzakh-simbolo-bronze.svg',180,180,'none',f'border:0;background:{FOIL};opacity:.95'),'Símbolo · selo de acabamento')}
</div>{grain()}</section>''')

# 14 DIREÇÃO DE FOTOGRAFIA
def arch(f, w, h):
    return f'<div style="width:{w}px;height:{h}px;border-radius:{w//2}px {w//2}px 8px 8px;overflow:hidden;position:relative"><div class="ph" style="inset:0;background-image:url(fotos/{f}.jpg);{PHOTO}"></div></div>'
S.append(f'''<section class="s" style="background:{OB}">
<div class="abs" style="left:120px;top:96px">{lab('10 · Direção de fotografia')}</div>
<div class="abs" style="left:120px;top:200px;display:flex;gap:24px;align-items:flex-end">{arch('colunata',300,640)}{arch('espiral',300,560)}{arch('siq2',300,700)}</div>
<div class="abs" style="left:1200px;top:240px;width:600px">
<div class="disp" style="font-size:61px">Luz que entra <i style="color:{OU}">por um vão.</i></div>
<div style="margin-top:48px;font-size:20px;line-height:1.5;color:rgba(238,234,226,.8)">
<div class="lab" style="color:{OU};font-size:13px;margin-bottom:12px">Mostrar</div>Pedra, concreto, arco, luz rasante, sombra longa, horizonte. Tom quente, grão de filme, metade da imagem na sombra.
<div class="lab" style="color:#D2553F;font-size:13px;margin:32px 0 12px">Evitar</div>Lua, estrelas, mandala, deserto com camelo, símbolo religioso, rosto em close, foto de banco iluminada e colorida.</div></div>
{foot(14)}{grain()}</section>''')

# 15 APLICAÇÕES · papelaria do estúdio + assinatura de e-mail + capa do Behance (mockups em CSS)
SH = 'box-shadow:0 1px 2px rgba(0,0,0,.08),0 8px 24px rgba(0,0,0,.18),0 32px 64px rgba(0,0,0,.28)'
cartao_f = f'<div style="width:420px;height:240px;border-radius:10px;background:{OL};{SH};position:relative;overflow:hidden;display:flex;align-items:center;justify-content:center">{logo("barzakh-simbolo-bronze.svg",120,120)}<div class="gr" style="opacity:.08"></div></div>'
cartao_v = (f'<div style="width:420px;height:240px;border-radius:10px;background:{MA};{SH};position:relative;padding:32px">{logo("barzakh-horizontal-bronze.svg",190,49,OB)}'
            f'<div class="abs" style="left:32px;bottom:28px;font-size:13px;line-height:1.6;color:{OB}"><b>Lindson Almeida</b><br>Direção criativa<br><span style="font-family:JetBrains Mono;font-size:11px;letter-spacing:.08em">@barzakhstudio</span></div>'
            f'<div class="abs" style="right:32px;bottom:28px">{logo("barzakh-simbolo-bronze.svg",28,28,OL)}</div></div>')
timbrado = (f'<div style="width:420px;height:594px;background:{MA};{SH};position:relative;padding:40px">{logo("barzakh-horizontal-bronze.svg",160,42,OB)}'
            + ''.join(f'<div style="height:6px;background:rgba(14,15,18,.08);border-radius:3px;margin-top:{48 if i==0 else 14}px;width:{[100,92,96,70,100,88,94,60][i]}%"></div>' for i in range(8))
            + f'<div class="abs" style="left:40px;right:40px;bottom:32px;border-top:1px solid {OU};padding-top:12px;font-family:JetBrains Mono;font-size:9px;letter-spacing:.14em;color:{OL}">BARZAKH · UM ESTÚDIO AL KÁNTARA · SÃO LUÍS - MA</div></div>')
email = (f'<div style="width:620px;background:#fff;border-radius:16px;{SH};padding:32px;color:{OB}"><div style="font-size:14px;color:#888;border-bottom:1px solid #eee;padding-bottom:12px">Para: cliente · Assunto: sua proposta</div>'
         f'<div style="font-size:15px;line-height:1.6;margin:20px 0 28px;color:#333">Segue a apresentação do conceito aplicado. Qualquer dúvida, me chama no WhatsApp.</div>'
         f'<div style="display:flex;align-items:center;gap:20px;border-top:2px solid {OU};padding-top:20px"><div style="width:64px;height:64px;border-radius:50%;background:{OL};display:flex;align-items:center;justify-content:center">{logo("barzakh-simbolo-bronze.svg",40,40)}</div>'
         f'<div style="font-size:14px;line-height:1.5"><b style="font-family:Fraunces;font-weight:400;font-size:20px">Lindson Almeida</b><br>Direção criativa · Barzakh<br><span style="font-family:JetBrains Mono;font-size:11px;color:{OL};letter-spacing:.08em">BARZAKH · UM ESTÚDIO AL KÁNTARA</span></div></div></div>')
behance = (f'<div style="width:620px;border-radius:14px;overflow:hidden;{SH};background:#fff"><div style="height:34px;background:#ECECEC;display:flex;align-items:center;gap:8px;padding:0 14px"><i style="width:10px;height:10px;border-radius:50%;background:#ccc"></i><i style="width:10px;height:10px;border-radius:50%;background:#ccc"></i><i style="width:10px;height:10px;border-radius:50%;background:#ccc"></i><span style="margin-left:16px;font-size:11px;color:#777;font-family:JetBrains Mono">behance.net/barzakhstudio</span></div>'
           f'<div style="height:300px;background:radial-gradient(ellipse at 60% 40%,{OL2},{OL} 60%,{OL3});position:relative;display:flex;align-items:center;justify-content:space-between;padding:0 48px">'
           f'<div><div class="lab" style="font-size:10px;color:{OU}">Identidade visual</div><div class="disp" style="font-size:40px;margin-top:12px">Barzakh</div></div>{logo("barzakh-simbolo-bronze.svg",170,170)}<div class="gr" style="opacity:.08"></div></div></div>')
S.append(f'''<section class="s" style="background:#1A1712">
<div class="abs" style="left:120px;top:96px">{lab('11 · Aplicações do estúdio')}</div>
<div class="abs" style="left:120px;top:200px;transform:rotate(-3deg)">{timbrado}</div>
<div class="abs" style="left:430px;top:500px;transform:rotate(4deg)">{cartao_f}</div>
<div class="abs" style="left:520px;top:200px;transform:rotate(-1deg)">{cartao_v}</div>
<div class="abs" style="left:1180px;top:160px">{behance}</div>
<div class="abs" style="left:1180px;top:560px">{email}</div>
<div class="abs lab" style="left:120px;bottom:56px;font-size:12px;color:rgba(238,234,226,.45)">Papelaria · cartão · capa do Behance · assinatura de e-mail · mockups em CSS</div>
{grain(.05)}</section>''')

# 16 REDES SOCIAIS · perfil com a foto de perfil escolhida e os 3 fixados
def phone(inner, extra=''):
    return (f'<div style="width:420px;height:860px;border-radius:64px;background:#0A0A0A;padding:14px;{SH};{extra}"><div style="width:100%;height:100%;border-radius:52px;overflow:hidden;background:#000;position:relative">'
            f'<div class="abs" style="left:50%;top:12px;width:110px;height:30px;border-radius:20px;background:#000;transform:translateX(-50%);z-index:9"></div>{inner}</div></div>')
perfil = (f'<div style="padding:62px 20px 0;color:#fff;font-size:13px"><div style="font-weight:600;font-size:16px;text-align:center">barzakhstudio</div>'
          f'<div style="display:flex;align-items:center;gap:22px;margin-top:20px"><img src="assets/foto-de-perfil.jpg" style="width:86px;height:86px;border-radius:50%">'
          f'<div style="display:flex;gap:22px;text-align:center"><div><b>3</b><br>posts</div><div><b>·</b><br>seguidores</div><div><b>·</b><br>seguindo</div></div></div>'
          f'<div style="margin-top:12px;line-height:1.45"><b>Barzakh · Identidade Visual</b><br>A passagem da sua marca.<br>Identidade visual e branding · São Luís - MA<br>Um estúdio Al Kántara</div>'
          f'<div style="display:flex;gap:6px;margin-top:12px"><div style="flex:1;background:#262626;border-radius:8px;padding:7px;text-align:center;font-weight:600">Seguir</div><div style="flex:1;background:#262626;border-radius:8px;padding:7px;text-align:center;font-weight:600">Mensagem</div></div></div>'
          f'<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:2px;margin-top:18px">' + ''.join(f'<img src="assets/0{i}.jpg" style="width:100%;aspect-ratio:3/4;object-fit:cover">' for i in (1, 2, 3)) + '</div>')
post = (f'<div style="padding:60px 0 0;color:#fff"><div style="display:flex;align-items:center;gap:10px;padding:0 14px 10px;font-size:13px;font-weight:600"><img src="assets/foto-de-perfil.jpg" style="width:30px;height:30px;border-radius:50%">barzakhstudio</div>'
        f'<img src="assets/02.jpg" style="width:100%;aspect-ratio:3/4;object-fit:cover"><div style="padding:12px 14px;font-size:12px;line-height:1.5"><b>barzakhstudio</b> Barzakh quer dizer passagem. É isso que a gente faz com a sua marca.</div></div>')
S.append(f'''<section class="s" style="{bgol()}">
<div class="abs" style="left:120px;top:96px">{lab('12 · Redes sociais')}</div>
<div class="abs" style="left:120px;top:300px;width:420px"><div class="disp" style="font-size:61px">O perfil é a <i style="color:{OU}">primeira fachada.</i></div>
<p class="body" style="margin-top:32px;font-size:20px;color:rgba(238,234,226,.75)">Foto de perfil: o símbolo em ouro sobre oliva. Os 3 fixados formam uma só frase: a passagem da sua marca.</p></div>
<div class="abs" style="left:700px;top:110px;transform:perspective(1600px) rotateY(10deg) rotateX(2deg)">{phone(perfil)}</div>
<div class="abs" style="left:1240px;top:110px;transform:perspective(1600px) rotateY(-10deg) rotateX(2deg)">{phone(post)}</div>
{grain()}</section>''')

# 17 ENCERRAMENTO
S.append(f'''<section class="s" style="{bgol()}display:flex;flex-direction:column;align-items:center;justify-content:center">
<div class="abs" style="left:50%;top:50%;transform:translate(-50%,-50%);opacity:.06">{logo('barzakh-simbolo-bronze.svg',1300,1300,MA)}</div>
<img src="assets/barzakh-vertical-ouro.png" style="position:relative;width:560px">
<div class="disp" style="position:relative;font-size:39px;margin-top:48px;color:{MA}"><i>A passagem da sua marca.</i></div>
<div class="abs" style="left:120px;right:120px;bottom:96px;display:flex;justify-content:space-between">{lab('@barzakhstudio')}{lab('Direção criativa · Lindson Almeida','rgba(238,234,226,.6)')}{lab('Um estúdio Al Kántara')}</div>
{grain(.07)}</section>''')

# ---------- CARROSSEL 4:5 (8 telas) ----------
C = []
def cfoot(n):
    return f'<div class="abs" style="left:96px;right:96px;bottom:72px;display:flex;justify-content:space-between;z-index:40">{lab("Barzakh · identidade","rgba(238,234,226,.55)")}{lab(f"{n:02d}/08","rgba(238,234,226,.55)")}</div>'
C.append(f'''<section class="c" style="{bgol()}">
<div class="abs" style="left:-300px;top:400px;opacity:.06">{logo('barzakh-simbolo-bronze.svg',1300,1300,MA)}</div>
<div class="abs" style="left:96px;top:96px">{lab('Identidade visual · case')}</div>
<div class="abs" style="left:0;right:0;top:250px;display:flex;justify-content:center"><img src="assets/barzakh-vertical-ouro.png" style="width:760px"></div>
<div class="abs disp" style="left:96px;bottom:150px;font-size:76px">A passagem<br><i style="color:{OU}">da sua marca.</i></div>{cfoot(1)}{grain(.07)}</section>''')
C.append(f'''<section class="c" style="background:{OB}">
<div class="ph" style="left:0;top:0;right:0;height:640px;background-image:url(fotos/panteao2.jpg);{PHOTO}"></div><div class="abs" style="left:0;right:0;top:340px;height:300px;background:linear-gradient(transparent,{OB})"></div>
<div class="abs" style="left:96px;top:96px">{lab('O nome')}</div>
<div class="abs" style="left:96px;top:660px;width:880px"><div class="disp" style="font-size:149px;color:{OU}">Barzakh</div><div class="lab" style="margin-top:24px;color:rgba(238,234,226,.6)">bar · zak</div>
<p class="body" style="margin-top:40px;font-size:31px;color:rgba(238,234,226,.85)">Palavra árabe para o limiar: a faixa entre duas águas que se encontram sem se misturar.</p></div>{cfoot(2)}{grain()}</section>''')
C.append(f'''<section class="c" style="{bgol()}">
<div class="ph" style="left:0;right:0;top:0;height:700px;background-image:url(fotos/mar.jpg);filter:sepia(.45) brightness(.85)"></div><div class="abs" style="left:0;right:0;top:450px;height:250px;background:linear-gradient(transparent,{OL})"></div>
<div class="abs" style="left:96px;top:96px">{lab('O conceito')}</div>
<div class="abs" style="left:96px;top:740px;width:880px"><div class="disp" style="font-size:95px">Dois mares,<br><i style="color:{OU}">um limiar.</i></div>
<p class="body" style="margin-top:40px;font-size:31px;color:rgba(238,234,226,.85)">O arco é a ponte. O reflexo é a marca que vai tomar forma. A barra é a passagem.</p></div>{cfoot(3)}{grain()}</section>''')
C.append(f'''<section class="c" style="background:{OB}">
<div class="abs" style="left:96px;top:96px">{lab('Construção')}</div>
<svg class="abs" style="left:60px;top:170px" width="960" height="960" viewBox="0 0 240 240">{geo}{cot}</svg>
<div class="abs disp" style="left:96px;bottom:150px;font-size:61px">Régua e <i style="color:{OU}">compasso.</i></div>{cfoot(4)}{grain()}</section>''')
ccol = ''.join(f'<div style="flex:{float(p[:-1])+12};background:{c};position:relative"><div class="abs" style="left:96px;right:96px;bottom:28px;color:{tc};display:flex;justify-content:space-between;align-items:baseline"><div class="disp" style="font-size:39px">{n} <span style="font-size:25px;opacity:.7">{p}</span></div><div class="lab" style="font-size:14px;color:{tc};opacity:.8">{OU if n=="Ouro Escovado" else c}</div></div></div>' for n, c, rgb, cmyk, p, tc in pal)
C.append(f'''<section class="c" style="display:flex;flex-direction:column">{ccol}<div class="abs" style="left:96px;top:96px">{lab('Paleta','rgba(238,234,226,.8)')}</div>{grain()}</section>''')#{grain()}</section>''')
C.append(f'''<section class="c" style="background:{OB}">
<div class="abs" style="left:96px;top:96px">{lab('Tipografia')}</div>
<div class="abs" style="left:96px;top:220px;font-family:Fraunces;font-weight:300;font-size:400px;line-height:1;letter-spacing:-.04em">Aa</div>
<div class="abs" style="left:96px;top:700px"><div style="font-family:Fraunces;font-weight:300;font-size:61px">Fraunces <i style="color:{OU}">Light</i></div><div class="lab" style="margin-top:12px;color:rgba(238,234,226,.6)">Títulos</div>
<div style="margin-top:56px;font-size:49px;font-weight:500">Inter Tight</div><div class="lab" style="margin-top:12px;color:rgba(238,234,226,.6)">Texto</div>
<div style="margin-top:56px;font-family:JetBrains Mono;font-size:31px;color:{OU}">JetBrains Mono</div><div class="lab" style="margin-top:12px;color:rgba(238,234,226,.6)">Rótulos</div></div>{cfoot(6)}{grain()}</section>''')
C.append(f'''<section class="c" style="background:#1A1712">
<div class="abs" style="left:96px;top:96px">{lab('Aplicações do estúdio')}</div>
<div class="abs" style="left:96px;top:220px;transform:rotate(-3deg)">{timbrado}</div>
<div class="abs" style="left:520px;top:300px;transform:rotate(3deg)">{cartao_v}</div>
<div class="abs" style="left:440px;top:640px;transform:rotate(-2deg)">{cartao_f}</div>
<div class="abs disp" style="left:96px;bottom:150px;font-size:61px">Pronta para <i style="color:{OU}">se apresentar.</i></div>{cfoot(7)}{grain(.05)}</section>''')
C.append(f'''<section class="c" style="{bgol()}display:flex;flex-direction:column;align-items:center;justify-content:center">
<img src="assets/barzakh-simbolo-ouro.png" style="width:440px">
<div class="disp" style="font-size:61px;margin-top:56px;text-align:center">Barzakh quer dizer passagem.<br><i style="color:{OU}">É isso que a gente faz.</i></div>
<div style="margin-top:56px">{lab('@barzakhstudio')}</div>{cfoot(8)}{grain(.07)}</section>''')

html = lambda xs, cls: f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Barzakh · identidade</title><style>{CSS}</style></head><body>' + ''.join(x.replace(f'<section class="{cls}"', f'<section id="{cls}{i+1:02d}" class="{cls}"', 1) for i, x in enumerate(xs)) + '</body></html>'
open(os.path.join(D, 'apresentacao.html'), 'w').write(html(S, 's'))
open(os.path.join(D, 'carrossel.html'), 'w').write(html(C, 'c'))
print(len(S), 'slides,', len(C), 'telas')
