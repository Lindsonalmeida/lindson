# Identidade visual Orégano Turbo · v2 PREMIUM (conta Leandro, 05/11/2026) · Brand Squad + Design Squad
# Lindson: "quero algo premium" → a v1 (mascote cartum colorido) fica de lado. Cópia da composição de:
#  1. Pentagram · Happy Face Pizza (selo redondo com o nome em volta de um rosto em traço, 2 cores verde+amarelo, letra 70s em minúsculas, carimbo em caixa/avental/broche)
#  2. Marka Collective · Paesano (personagem em traço único dentro do selo, fundo amarelo, aplicação em uniforme e caixa)
#  3. Gander · Graza (D&AD Graphite Pencil 2023): blocos de cor chapada, creme + verde profundo, tom brincalhão com acabamento caro
# Gera pecas2.html → node render2.js → pecas-v2/*.png
VERDE, AMARELO, CREME, TOMATE, TINTA = '#13452B', '#F6C343', '#F4EBD9', '#D9432B', '#0F1F17'
def folha(cor, traco=9, expressao='sorriso', w=None):
    """O personagem em traço único: folha de orégano com óculos de corrida."""
    bocas = {'sorriso': 'M84 128 Q100 142 116 128', 'uau': None, 'piscada': 'M84 130 Q100 140 116 130'}
    boca = f'<path d="{bocas[expressao]}"/>' if bocas.get(expressao) else '<ellipse cx="100" cy="134" rx="8" ry="10"/>'
    olho2 = '<path d="M112 100 Q120 94 128 100"/>' if expressao == 'piscada' else '<circle cx="120" cy="100" r="4" fill="' + cor + '" stroke="none"/>'
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" {f"width={w} height={w}" if w else ""} fill="none" stroke="{cor}" stroke-width="{traco}" stroke-linecap="round" stroke-linejoin="round">'
            f'<path d="M100 186 C 40 168, 34 82, 100 16 C 166 82, 160 168, 100 186 Z"/>'
            f'<path d="M100 186 L100 196"/>'
            f'<circle cx="80" cy="100" r="15"/><circle cx="120" cy="100" r="15"/><path d="M95 100 L105 100"/><path d="M65 98 L52 94"/><path d="M135 98 L148 94"/>'
            f'<circle cx="80" cy="100" r="4" fill="{cor}" stroke="none"/>{olho2}{boca}'
            f'<path d="M100 40 L100 58"/><path d="M100 152 L100 170"/></svg>')
def selo(tam, fundo=AMARELO, tinta=VERDE, texto='ORÉGANO TURBO · MKT PARA PIZZARIAS · ', expressao='sorriso', borda=True):
    """O selo (roundel): nome em volta, folha no centro. Peça principal da marca."""
    r = 100
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 240" width="{tam}" height="{tam}">'
            f'<circle cx="120" cy="120" r="118" fill="{fundo}"/>' + (f'<circle cx="120" cy="120" r="111" fill="none" stroke="{tinta}" stroke-width="2.4"/><circle cx="120" cy="120" r="72" fill="none" stroke="{tinta}" stroke-width="2.4"/>' if borda else '') +
            f'<defs><path id="c{tam}{expressao}" d="M120,120 m-{r - 9},0 a{r - 9},{r - 9} 0 1,1 {2 * (r - 9)},0 a{r - 9},{r - 9} 0 1,1 -{2 * (r - 9)},0"/></defs>'
            f'<text fill="{tinta}" style="font:700 17.2px \'DM Sans\'"><textPath href="#c{tam}{expressao}" textLength="{int(2 * 3.14159 * (r - 9)) - 6}" lengthAdjust="spacing">{texto}</textPath></text>'
            f'<g transform="translate(66 66) scale(.54)">{folha(tinta, 9, expressao).split(">", 1)[1].rsplit("</svg>", 1)[0].join(["<g fill=\'none\' stroke=\'" + tinta + "\' stroke-width=\'9\' stroke-linecap=\'round\' stroke-linejoin=\'round\'>", "</g>"])}</g></svg>')
WM = lambda tam, cor, extra='': f'<div class="wm" style="font-size:{tam}px;color:{cor};{extra}">orégano turbo</div>'
ROT = lambda t, cor: f'<div class="rot" style="color:{cor}">{t}</div>'
GRAO = ("url(\"data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='240' height='240'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3' stitchTiles='stitch'/>"
        "<feColorMatrix values='0 0 0 0 .5  0 0 0 0 .4  0 0 0 0 .3  0 0 0 .55 0'/></filter><rect width='100%25' height='100%25' filter='url(%23n)'/></svg>\")")
KRAFT = f'#C9A877'
P = []
# 1 · capa
P.append(('v2-01-capa', 1080, 1350, VERDE, f'''
<div class="a" style="left:80px;top:80px;width:920px;display:flex;justify-content:space-between">{ROT('Identidade visual', AMARELO)}{ROT('Nº 01 · 2026', AMARELO)}</div>
<div class="a" style="left:240px;top:250px">{selo(600)}</div>
<div class="a" style="left:0;width:1080px;top:930px;text-align:center">{WM(150, CREME)}</div>
<div class="a" style="left:0;width:1080px;top:1140px;text-align:center;font:500 30px/1.3 'DM Sans';color:{AMARELO}">o toque final que acelera a sua pizzaria</div>'''))
# 2 · sistema de logo
cartao = lambda x, y, w, h, bg, inner: f'<div class="a" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:{bg};border-radius:6px;display:grid;place-items:center">{inner}</div>'
P.append(('v2-02-logo', 1080, 1350, CREME, f'''
<div class="a" style="left:80px;top:80px">{ROT('O sistema · selo, nome e personagem', VERDE)}</div>
{cartao(80, 140, 450, 450, VERDE, selo(340))}
{cartao(550, 140, 450, 450, AMARELO, selo(340, VERDE, AMARELO, expressao='piscada'))}
{cartao(80, 610, 920, 260, '#fff', WM(132, VERDE))}
{cartao(80, 890, 290, 290, AMARELO, folha(VERDE, 9, w=200))}
{cartao(395, 890, 290, 290, VERDE, folha(AMARELO, 9, 'uau', w=200))}
{cartao(710, 890, 290, 290, TOMATE, selo(220, CREME, TOMATE, borda=False))}
<div class="a" style="left:80px;top:1210px;width:920px;font:400 21px/1.45 'DM Sans';color:{TINTA}">O <b>selo</b> é a assinatura principal (carimbo, avatar, caixa, avental). O <b>nome</b> em Fraunces minúscula entra quando há espaço horizontal. O <b>personagem</b> em traço único vive sozinho em posts e brindes. Sempre uma cor sobre a outra: nunca mais de duas no mesmo selo.</div>'''))
# 3 · cores e letras
P.append(('v2-03-cores-letras', 1080, 1350, '#fff', f'''
<div class="a" style="left:80px;top:80px">{ROT('Cores e letras', VERDE)}</div>
<div class="a" style="left:80px;top:140px;width:920px;height:440px;display:grid;grid-template-columns:1.6fr 1.2fr .7fr .5fr;gap:0;border-radius:6px;overflow:hidden">
 {''.join(f'<div style="background:{h};color:{t};padding:22px;display:flex;flex-direction:column;justify-content:flex-end;font:500 16px/1.4 DM Sans"><b style="font:900 30px/1 Fraunces;font-variation-settings:\'SOFT\' 100,\'WONK\' 1">{n}</b>{h}<br>{u}</div>' for n, h, t, u in [('verde forno', VERDE, CREME, 'base · 45%'), ('amarelo turbo', AMARELO, VERDE, 'par · 35%'), ('creme massa', CREME, VERDE, 'respiro · 15%'), ('tomate', TOMATE, CREME, 'ponto · 5%')])}</div>
<div class="a" style="left:80px;top:630px;width:920px">
 <div style="font:900 150px/.88 Fraunces;font-variation-settings:'SOFT' 100,'WONK' 1;color:{VERDE};letter-spacing:-.03em">pizza boa<br><span style="color:{TOMATE}">não basta.</span></div>
 <div style="font:500 20px 'DM Sans';color:#666;margin:16px 0 34px">Títulos · Fraunces Black, eixos SOFT 100 e WONK 1 (curvas macias de anos 70) · minúsculas · Google Fonts</div>
 <div style="font:700 40px/1.2 'DM Sans';color:{TINTA}">Pedido direto no seu WhatsApp, todo dia da semana.</div>
 <div style="font:400 26px/1.5 'DM Sans';color:#333;margin-top:12px">Textos · DM Sans 400, 500 e 700. Rótulos em caixa alta, espaçados, como etiqueta de caixa de pizza.</div></div>'''))
# 4 · personagem
P.append(('v2-04-personagem', 1080, 1350, AMARELO, f'''
<div class="a" style="left:80px;top:80px">{ROT('O personagem · traço único', VERDE)}</div>
<div class="a" style="left:80px;top:140px;font:900 96px/.9 Fraunces;font-variation-settings:'SOFT' 100,'WONK' 1;color:{VERDE}">o tempero<br>que acelera.</div>
{''.join(f'<div class="a" style="left:{80 + i * 310}px;top:420px;width:290px;text-align:center">{folha(VERDE, 9, e, w=260)}<div class="rot" style="color:{VERDE};margin-top:10px">{t}</div></div>' for i, (e, t) in enumerate([('sorriso', 'bora'), ('uau', 'uau'), ('piscada', 'se liga')]))}
<div class="a" style="left:80px;top:830px;width:920px;font:400 26px/1.55 'DM Sans';color:{VERDE}">
Desenhado com <b>um traço só, de espessura igual</b>, em uma cor por vez, como a Happy Face Pizza do Pentagram. Óculos de corrida: o "turbo". A folha de orégano: o detalhe que muda a pizza inteira, como o marketing faz com a pizzaria.<br><br>
<b>Regras:</b> nunca preenchido de cor, nunca com sombra ou degradê; sempre de frente; nunca triste, bravo ou segurando dinheiro. Novas poses (apontando, com o celular, comemorando) seguem o mesmo traço.</div>'''))
# 5 · aplicações (carimbo na caixa kraft, avental, broche, Instagram)
P.append(('v2-05-aplicacoes', 1080, 1350, CREME, f'''
<div class="a" style="left:80px;top:80px">{ROT('Aplicações', VERDE)}</div>
<div class="a" style="left:80px;top:140px;width:560px;height:560px;background:{KRAFT};background-image:{GRAO.replace(chr(34), '&quot;')};border-radius:6px;box-shadow:0 30px 60px -30px rgba(15,31,23,.6)">
 <div style="position:absolute;inset:26px;border:2px dashed rgba(15,31,23,.25);border-radius:4px"></div>
 <div style="position:absolute;left:120px;top:90px;opacity:.88;transform:rotate(-12deg)">{selo(320, 'transparent', TOMATE)}</div>
 <div style="position:absolute;left:40px;bottom:36px;font:700 16px 'DM Sans';letter-spacing:.3em;color:rgba(15,31,23,.6)">CARIMBO NA CAIXA DA PIZZARIA CLIENTE</div></div>
<div class="a" style="left:670px;top:140px;width:330px;height:560px;background:{VERDE};border-radius:6px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:26px">
 <div style="width:140px;height:140px;border-radius:50%;box-shadow:0 10px 20px rgba(0,0,0,.4)">{selo(140)}</div>
 <div style="width:110px;height:110px;border-radius:50%;box-shadow:0 10px 20px rgba(0,0,0,.4)">{selo(110, CREME, TOMATE, expressao='piscada')}</div>
 <div class="rot" style="color:{AMARELO}">broches da equipe</div></div>
<div class="a" style="left:80px;top:730px;width:920px;height:250px;background:#fff;border-radius:6px;display:flex;align-items:center;gap:30px;padding:0 34px">
 <div style="width:170px;height:170px;border-radius:50%;overflow:hidden;flex:none">{selo(170)}</div>
 <div style="font:400 23px/1.45 'DM Sans';color:{TINTA}"><b style="font:700 26px 'DM Sans'">oreganoturbo</b> · Orégano Turbo | Mkt Pizzarias<br>O toque final que acelera a sua pizzaria 🌿🏁<br>Pedido direto no WhatsApp, todo dia da semana</div></div>
<div class="a" style="left:80px;top:1010px;display:flex;gap:22px">{''.join(f'<div style="text-align:center"><div style="width:132px;height:132px;border-radius:50%;background:{bg};display:grid;place-items:center;font:900 {fs}px/1 Fraunces;font-variation-settings:\'SOFT\' 100,\'WONK\' 1;color:{c}">{t}</div><div style="font:500 17px DM Sans;color:{TINTA};margin-top:8px">{n}</div></div>' for t, n, bg, c, fs in [('raio-x', 'Raio-X', VERDE, AMARELO, 30), ('1·2·3', 'Como funciona', AMARELO, VERDE, 34), ('cases', 'Cases', VERDE, CREME, 34), ('r$', 'Planos', TOMATE, CREME, 48), ('rec', 'Bastidores', AMARELO, VERDE, 40), ('?!', 'Dúvidas', VERDE, AMARELO, 54)])}</div>'''))
# avatar, destaques, post
P.append(('v2-avatar', 1080, 1080, VERDE, f'<div class="a" style="left:90px;top:90px">{selo(900)}</div>'))
for i, (t, n, bg, c, fs) in enumerate([('raio-x', 'raio-x', VERDE, AMARELO, 220), ('1·2·3', 'como-funciona', AMARELO, VERDE, 220), ('cases', 'cases', VERDE, CREME, 230), ('r$', 'planos', TOMATE, CREME, 330), ('rec', 'bastidores', AMARELO, VERDE, 280), ('?!', 'duvidas', VERDE, AMARELO, 380)], 1):
    P.append((f'v2-destaque-{i}-{n}', 1080, 1920, bg, f'<div class="a" style="left:0;top:0;width:1080px;height:1920px;display:grid;place-items:center;font:900 {fs}px/1 Fraunces;font-variation-settings:\'SOFT\' 100,\'WONK\' 1;color:{c}">{t}</div>'))
P.append(('v2-post-exemplo', 1080, 1350, VERDE, f'''
<div class="a" style="left:80px;top:90px;width:920px;display:flex;justify-content:space-between">{ROT('Nº 01 · dia fraco', AMARELO)}{ROT('@oreganoturbo', AMARELO)}</div>
<div class="a" style="left:80px;top:190px;font:900 128px/.9 Fraunces;font-variation-settings:'SOFT' 100,'WONK' 1;color:{CREME};letter-spacing:-.03em">sua pizzaria<br>vende no sábado<br><span style="color:{AMARELO}">e para na terça?</span></div>
<div class="a" style="left:84px;top:640px;width:520px;font:500 34px/1.4 'DM Sans';color:{CREME}">Tem conserto. E começa por pedido direto no seu WhatsApp.</div>
<div class="a" style="left:640px;top:830px;transform:rotate(-10deg)">{selo(380)}</div>
<div class="a" style="left:84px;top:1200px;font:700 20px 'DM Sans';letter-spacing:.3em;color:{AMARELO}">ARRASTA PRO LADO →</div>'''))
CSS = f'''*{{margin:0;padding:0;box-sizing:border-box}}body{{background:#333}}.f{{position:relative;overflow:hidden;margin-bottom:20px}}.a{{position:absolute}}
.f::after{{content:"";position:absolute;inset:0;background-image:{GRAO};opacity:.18;mix-blend-mode:multiply;pointer-events:none}}
.wm{{font-family:Fraunces;font-weight:900;font-variation-settings:'SOFT' 100,'WONK' 1;letter-spacing:-.035em;line-height:1}}
.rot{{font:700 18px 'DM Sans';letter-spacing:.28em;text-transform:uppercase}}'''
html = ('<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght,SOFT,WONK@9..144,900,100,1&family=DM+Sans:wght@400;500;700&display=swap" rel="stylesheet">'
        f'<style>{CSS}</style></head><body>' + ''.join(f'<section class="f" id="{i}" style="width:{w}px;height:{h}px;background:{bg}">{c}</section>' for i, w, h, bg, c in P) + '</body></html>')
open('pecas2.html', 'w').write(html); print(len(P), 'peças v2')
