# Barzakh BOOK v2 + MANUAL v2 (conta Leandro, 16/11/2026)
# Refeitos do zero no padrão da peça APROVADA pelo Lindson: marca/aprovado/placa-arco-monolito-ouro.png
# (placa em arco grafite fosco no concreto, monolito em ouro escovado, brilho Lápis difuso, BARZAKH em Fraunces dourada,
#  "UM ESTÚDIO AL KÁNTARA" em mono com o K da Al Kántara v2). Sem aqueduto, sem foto de turismo: só textura.
# Base: manual.py (textos) + ../../gerador/escuro.py (ouro, placa, concreto, cartão, timbrado).
# Referências (estudo, nunca cópia): ver ../TEMPLATE.md (Renovo 20 hot stamping, Studio Arch 02, Dahr 01 luz rasante).
# Uso: PYTHONPATH=<py> python3 manual_v2.py
import os, sys, glob, shutil
from PIL import Image
from playwright.sync_api import sync_playwright
sys.path.insert(0, '/home/user/lindson/agencia/marca-lindson/projeto-designer/v3/gerador')
import escuro as E
from escuro import OB, MA, GR, PE, BR, LA, GRAF, OURO, mask, mono, mono_inline, kv2, ENDOSSO

B = E.B; G = B + '/gerador'; T = G + '/trat'; OUT = B + '/entregas'; PNG = B + '/logos/png/ouro'
os.makedirs(PNG, exist_ok=True)
FONT = '/home/user/lindson/agencia/marca-holding/v2/fontes'
CONC = f'file://{T}/concreto-v2.jpg'; CONCD = f'file://{T}/concreto-escuro-v2.jpg'; PEDRA = f'file://{T}/pedra-v2.jpg'
SOMBRA = f'file://{T}/sombra-noite.jpg'; COLUNA = f'file://{T}/colunata-noite.jpg'

CSS = E.CSS + f"""
@font-face{{font-family:'Fraunces';src:url('file://{FONT}/Fraunces-Regular.ttf');font-weight:400}}
@font-face{{font-family:'Fraunces';src:url('file://{FONT}/Fraunces-SemiBold.ttf');font-weight:600}}
@font-face{{font-family:'Fraunces';font-style:italic;src:url('file://{FONT}/Fraunces-Italic%5BSOFT,WONK,opsz,wght%5D.ttf')}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:{OB}}}
.pg{{width:1920px;height:1080px;position:relative;overflow:hidden;page-break-after:always;font-family:'Inter Tight';color:{MA};background:{GRAF}}}
.pg:after{{content:'';position:absolute;inset:0;background-image:{E.NOISE};opacity:.10;mix-blend-mode:overlay;pointer-events:none;z-index:6}}
.mn{{font-family:'JetBrains Mono';font-size:17px;letter-spacing:.2em;text-transform:uppercase;color:{BR}}}
.t1{{font-family:'Fraunces';font-weight:400;font-size:110px;line-height:1.02;letter-spacing:.005em}}
.t2{{font-family:'Fraunces';font-weight:400;font-size:66px;line-height:1.1;letter-spacing:.005em}}
.cap{{font-family:'Fraunces';text-transform:uppercase;letter-spacing:.24em}}
.p{{font-size:24px;line-height:1.55;color:rgba(238,234,226,.9)}}
.p b{{color:#e3cb98;font-weight:500}}
.hd{{position:absolute;left:96px;right:96px;top:52px;display:flex;justify-content:space-between;align-items:center;z-index:7}}
.ft{{position:absolute;left:96px;right:96px;bottom:44px;display:flex;justify-content:space-between;align-items:center;z-index:7}}
.hl{{font-family:'JetBrains Mono';font-size:15px;letter-spacing:.2em;text-transform:uppercase;color:rgba(238,234,226,.6)}}
.felt{{background-color:{GRAF};background-image:{E.PAPER}}}
.arch{{position:absolute;overflow:hidden;box-shadow:inset 0 0 0 1px rgba(201,168,108,.35)}}
.lt{{background:#e9e4da;color:{OB}}}
"""

def glow(x, y, w, h, op=.7): return f'<div class="beam" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;opacity:{op}"></div>'
def logot(w, x=None, y=None, st=''):  # logotipo BARZAKH em ouro escovado
    pos = f'position:absolute;left:{x}px;top:{y}px;' if x is not None else 'position:relative;'
    return f'<div class="foil" style="{pos}width:{w}px;height:{w*130/577}px;-webkit-mask-image:{mask("logotipo-mono-branco")};{st}"></div>'
def wall(img=CONC, luz=.8, vin=.7):
    return (f'<div style="position:absolute;inset:0;background:url({img}) center/cover"></div><div class="win" style="opacity:{luz}"></div>'
            f'<div style="position:absolute;inset:0;background:linear-gradient(100deg,rgba(255,236,200,.10),transparent 40%),radial-gradient(ellipse at 55% 45%,transparent 25%,rgba(10,12,16,{vin}))"></div>')
def arch(x, y, w, h, img=None, inner='', bg=None):
    fill = f'background:url({img}) center/cover;' if img else f'background:{bg or "linear-gradient(160deg,#2a2c31,#141519)"};'
    return f'<div class="arch" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;border-radius:{w/2}px {w/2}px 0 0;{fill}">{inner}</div>'
def placa(s, x, y): return f'<div style="position:absolute;left:{x}px;top:{y}px">{E.placa(s)}</div>'
def swatch_ouro(w, h, label=True):
    return (f'<div style="position:relative;width:{w}px;height:{h}px;background:{OURO};box-shadow:inset 0 1px 0 rgba(255,240,200,.5),0 20px 40px rgba(0,0,0,.45)">'
            f'<div style="position:absolute;inset:0;background:repeating-linear-gradient(90deg,rgba(255,255,255,.05) 0 1px,transparent 1px 3px)"></div></div>')

class Doc:
    def __init__(s, nome): s.nome = nome; s.p = []
    def page(s, body, sec='', hf=True, cls=''):
        n = len(s.p) + 1
        hf_ = (f'<div class="hd"><div style="display:flex;gap:16px;align-items:center">{mono_inline(30)}<span class="hl">Barzakh · {s.nome}</span></div><span class="hl">{sec}</span></div>'
               f'<div class="ft"><span class="hl">{kv2(14, BR)}Um estúdio Al Kántara · v2 · 2026</span><span class="hl">{n:02d}</span></div>') if hf else ''
        s.p.append(f'<section class="pg {cls}">{body}{hf_}</section>')
    def capa(s, kicker, titulo):
        s.page(wall(CONC, .9, .75) + glow(820, 300, 900, 600, .35) + placa(1.3, 1000, 100) +
               f'<div style="position:absolute;inset:0;background:linear-gradient(90deg,rgba(10,12,16,.92) 0,rgba(10,12,16,.55) 38%,transparent 55%)"></div>'
               f'<div style="position:absolute;left:96px;top:96px;display:flex;gap:18px;align-items:center">{mono_inline(46)}<span class="mn">Barzakh · {kicker}</span></div>'
               f'<div style="position:absolute;left:96px;bottom:170px;width:820px"><div class="t1" style="font-size:132px">{titulo}</div></div>'
               f'<div class="mn" style="position:absolute;left:96px;bottom:90px">{ENDOSSO(16)} · São Luís, MA · v2 · 2026</div>', hf=False)
    def abertura(s, num, titulo, sub, img):
        s.page(f'<div class="felt" style="position:absolute;inset:0"></div>' + glow(1040, 380, 820, 560, .6) +
               arch(1060, 150, 700, 930, img, f'<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(10,12,16,.1),rgba(10,12,16,.65))"></div>'
                    f'<div class="beam" style="left:120px;top:330px;width:460px;height:340px;opacity:.8"></div>{mono(300, 200, 330)}') +
               f'<div style="position:absolute;left:96px;top:230px"><div class="mn">Capítulo {num}</div><div class="ser ouro" style="font-family:Fraunces;font-size:300px;line-height:.9;margin-top:10px">{num}</div>'
               f'<div class="t1" style="margin-top:30px">{titulo}</div><div class="p" style="margin-top:30px;max-width:760px">{sub}</div></div>', titulo)
    def html(s): return f'<html><head><meta charset="utf-8"><link rel="stylesheet" href="{E.FONTS}"><style>{CSS}</style></head><body>{"".join(s.p)}</body></html>'

def two(lbl, titulo, txt, right, wl=640, bg='felt'):
    return (f'<div class="{bg}" style="position:absolute;inset:0"></div>'
            f'<div style="position:absolute;left:96px;top:170px;width:{wl}px"><div class="mn">{lbl}</div><div class="t2" style="margin:26px 0 34px">{titulo}</div><div class="p">{txt}</div></div>'
            f'<div style="position:absolute;left:{96+wl+100}px;right:96px;top:150px;bottom:120px">{right}</div>')
def painel(inner, img=CONCD, luz=.6):  # área direita: parede de concreto com luz rasante
    return f'<div style="position:relative;width:100%;height:100%;overflow:hidden;box-shadow:0 0 0 1px rgba(201,168,108,.18)">{wall(img, luz, .55)}{inner}</div>'

# ======================================================================= BOOK v2
K = Doc('Branding book')
K.capa('Branding book', 'A passagem<br><i>da sua marca.</i>')
sk = [('01', 'O nome', 'Barzakh, pronúncia, significado'), ('02', 'Por que existimos', 'A ponte e a passagem, promessa'),
      ('03', 'Como soamos', 'Arquétipo e tom'), ('04', 'Para quem', 'Persona e o teste'), ('05', 'Onde estamos', 'Al Kántara Group e endosso')]
K.page('<div class="felt" style="position:absolute;inset:0"></div>' + arch(96, 170, 560, 820, PEDRA, glow(60, 330, 440, 340, .8) + mono(260, 150, 380)) +
       '<div style="position:absolute;left:780px;right:96px;top:150px"><div class="mn">Sumário</div>' +
       ''.join(f'<div style="display:flex;gap:44px;padding:26px 0;border-top:1px solid rgba(201,168,108,.3)"><span class="ouro" style="font:400 64px Fraunces;width:100px">{a}</span><div><div style="font:400 52px Fraunces">{b}</div><div class="p" style="font-size:22px;margin-top:4px">{c}</div></div></div>' for a, b, c in sk) + '</div>', 'Sumário')
K.page(f'<div class="felt" style="position:absolute;inset:0"></div>' + glow(500, 120, 1000, 460, .7) + logot(1400, 260, 170) +
       f'<div style="position:absolute;left:96px;right:96px;top:560px;height:1px;background:{BR};opacity:.6"></div>'
       f'<div style="position:absolute;left:96px;right:96px;top:610px;display:grid;grid-template-columns:1fr 1fr 1fr;gap:70px">'
       f'<div><div class="mn">Fala-se</div><div style="font:400 66px Fraunces;margin-top:12px">bar·zak</div><div class="p" style="margin-top:10px">Força no BAR. Escreve-se sempre Barzakh, com “kh” no fim, sem acento.</div></div>'
       f'<div><div class="mn">Quer dizer</div><div style="font:400 66px Fraunces;margin-top:12px">passagem</div><div class="p" style="margin-top:10px">Palavra árabe antiga: istmo, faixa entre duas coisas, o limiar entre dois lados.</div></div>'
       f'<div><div class="mn">Em uma frase</div><div style="font:400 italic 42px/1.2 Fraunces;margin-top:12px">“Barzakh quer dizer passagem. A gente faz a passagem da sua marca.”</div></div></div>', '01 · O nome')
K.abertura('02', 'Por que existimos', 'A holding é a ponte. O estúdio é a travessia.', SOMBRA)
K.page(two('02 · A ponte e a passagem', 'A holding é a ponte. O estúdio é a travessia.', '<b>Al Kántara</b> quer dizer “a ponte”: liga as duas margens. <b>Barzakh</b> é o ponto exato da travessia, onde uma coisa deixa de ser o que era e ainda está tomando forma.<br><br>Por isso o símbolo nasce do arco, a forma que segura a pedra-chave do grupo, e vira monolito: pedra cheia, gravada em ouro.',
       painel(placa(.92, 140, 90))), '02 · Por que existimos')
K.page(f'{wall(CONCD, .9, .8)}' + glow(300, 300, 1300, 500, .5) + mono(200, 860, 150) +
       f'<div style="position:absolute;left:200px;right:200px;top:430px;text-align:center"><div class="mn">02 · Promessa</div><div class="t1" style="margin-top:30px">“Sua marca vai sair pronta<br>para se apresentar.”</div>'
       f'<div class="p" style="margin:40px auto 0;max-width:1000px">Prometemos só o que depende de nós. Marca boa ajuda a passar confiança; venda depende de muita coisa que não controlamos, e a gente não finge que controla.</div></div>', '02 · Promessa')
K.abertura('03', 'Como soamos', 'Fala pouco, mostra muito.', COLUNA)
K.page(two('03 · Arquétipo', 'O Mago sóbrio, segurado pelo Sábio.', '<b>Mago</b> (principal): o que faz a coisa mudar de estado, do rascunho à forma. Não promete milagre; mostra o antes e o depois.<br><br><b>Sábio</b> (apoio): calma, método, explica com clareza. Cada frase bonita vem com um fato concreto do processo.',
       painel('<div style="position:absolute;inset:60px;display:grid;grid-template-columns:1fr 1fr;gap:40px">' +
              ''.join(f'<div class="felt" style="position:relative;padding:44px;box-shadow:0 30px 60px rgba(0,0,0,.5);border-radius:{"220px 220px 0 0" if i==0 else "220px 220px 0 0"};overflow:hidden">{glow(40,120,300,260,.6)}<div style="position:relative;margin-top:150px;text-align:center"><div class="ouro" style="font:400 70px Fraunces">{a}</div><div class="mn" style="margin-top:14px">{b}</div><div class="p" style="font-size:21px;margin-top:22px">{c}</div></div></div>'
                      for i, (a, b, c) in enumerate([('Mago', 'Principal', 'Muda o estado: do rascunho à forma.'), ('Sábio', 'Apoio', 'Calma, método, fato concreto.')])) + '</div>')), '03 · Arquétipo')
tom = [('Somos', 'Calmos · exatos · profundos · concretos'), ('Não somos', 'Esotéricos · gurus · apressados · vagos'), ('Dizemos', '“passagem”, “forma”, “pronta para se apresentar”'), ('Evitamos', '“viralizar”, “explodir”, “garantido”, promessa de venda')]
K.page(two('03 · Tom de voz', 'Frase curta, fato concreto.', 'Na prática: fala pouco, mostra muito. Toda frase bonita vem amarrada a uma etapa real do processo.',
       '<div style="display:grid;grid-template-columns:1fr 1fr;gap:30px;height:100%">' + ''.join(f'<div class="felt" style="padding:44px;box-shadow:inset 0 0 0 1px rgba(201,168,108,.3)"><div class="mn">{a}</div><div style="font:400 40px/1.3 Fraunces;margin-top:24px">{b}</div></div>' for a, b in tom) + '</div>'), '03 · Tom')
K.abertura('04', 'Para quem', 'Dono de negócio que quer parecer do tamanho que já é.', PEDRA)
K.page(two('04 · O teste', 'Essa pessoa compraria disso?', '<b>Sim,</b> se o místico aparecer como profundidade e cuidado: nome raro, visual sóbrio, frase curta, e logo em seguida o trabalho concreto.<br><br><b>Não,</b> se soar esotérico. Muitos clientes são cristãos praticantes: nada de símbolo religioso, nada que lembre tarô ou guru. O místico certo é o da arquitetura e do museu.',
       painel(arch(200, 80, 520, 720, SOMBRA, glow(60, 260, 400, 300, .7) + mono(220, 150, 300)), CONC)), '04 · Persona')
K.page(two('05 · Regras de endosso', '“Barzakh · um estúdio Al Kántara.”', '1. Para o cliente final: “Barzakh” grande, “um estúdio Al Kántara” pequeno, no máximo um terço da altura do nome.<br>2. Dentro da holding: Barzakh na grade das divisões, com o mesmo peso das irmãs.<br>3. Nunca “Al Kántara Barzakh”.<br>4. Direção criativa: Lindson Almeida.',
       painel(f'{glow(150,150,700,500,.6)}{mono(300, 330, 140)}{logot(560, 200, 480)}<div class="mn" style="position:absolute;left:0;right:0;top:640px;text-align:center;font-size:20px">{ENDOSSO(20)}</div>')), '05 · Endosso')
K.page(f'{wall(CONC, .95, .6)}' + placa(.62, 190, 230) +
       f'<div style="position:absolute;left:820px;top:300px">{E.cartao(560, 330)}</div><div style="position:absolute;left:1180px;top:520px;transform:rotate(-6deg)">{E.cartao(520, 306, True)}</div>'
       f'<div style="position:absolute;left:96px;bottom:120px" class="mn">05 · A marca no mundo · placa e cartão em hot stamping ouro</div>', '05 · Aplicação')
K.page(wall(CONCD, .8, .85) + glow(560, 260, 800, 500, .55) + mono(320, 800, 250) +
       f'<div style="position:absolute;left:0;right:0;top:640px;text-align:center"><div class="t2" style="font-style:italic">A passagem da sua marca.</div><div class="mn" style="margin-top:30px">@barzakhstudio · {ENDOSSO(16)}</div></div>', hf=False)

# ======================================================================= MANUAL v2
M = Doc('Manual de marca')
M.capa('Manual de marca', 'Manual<br><i>de marca.</i>')
M.page(two('Introdução', 'Dois mares que se encontram e não se misturam.', 'Este manual define como a Barzakh aparece no mundo, do avatar à fachada. A versão principal é o <b>monolito em ouro escovado</b>: o arco cheio, a pedra que segura a luz, sobre grafite fosco e concreto.<br><br>Em caso de dúvida, menos é mais, e o símbolo nunca é redesenhado.',
       painel(placa(.92, 140, 90))), 'Introdução')
M.abertura('01', 'Marca', 'O arco cheio, em ouro escovado, com a hora azul atrás.', PEDRA)
cons = (f'<svg viewBox="0 0 240 240" style="position:absolute;left:180px;top:60px;width:700px;height:700px" fill="none" stroke="#8E9BEA" stroke-width=".4" stroke-dasharray="2 2">'
        f'<circle cx="120" cy="120" r="92"/><circle cx="120" cy="120" r="60.7"/><circle cx="120" cy="120" r="29.4"/><path d="M0 120H240M120 0V240M11 0V240M229 0V240"/></svg>')
M.page(two('1.1 · Construção', 'A régua dos Dois mares.', 'Só círculos e uma linha. Arco externo de raio <b>R</b>; fenda interna em <b>0,66R</b>; disco de luz de <b>0,32R</b>. Abaixo da linha, o reflexo em contorno fino. A barra do horizonte mede <b>2,36R</b>.<br><br>Desenhado só com geometria: aguenta de 16 px a uma fachada.',
       painel(glow(200, 200, 600, 500, .6) + mono(700, 180, 60) + cons, CONCD, .3)), '1.1 · Construção')
M.page(two('1.2 · Significado', 'O que cada parte diz.', '<b>Arco cheio:</b> a marca pronta, de pé, pedra.<br><b>Reflexo de baixo:</b> de onde ela veio.<br><b>Linha do horizonte:</b> a passagem, o barzakh.<br><b>Ouro:</b> a luz, o fio do grupo.<br><b>Brilho Lápis atrás:</b> a hora azul, o minuto entre o dia e a noite.',
       painel(arch(160, 60, 640, 760, None, glow(80, 260, 480, 360, .9) + mono(400, 120, 200)))), '1.2 · Significado')
var = [('Símbolo', 'simbolo'), ('Horizontal', 'horizontal'), ('Vertical', 'vertical'), ('Avatar', 'avatar')]
def vimg(k): return f'file://{PNG}/barzakh-{k}-ouro.png'
M.page('<div class="felt" style="position:absolute;inset:0"></div><div style="position:absolute;left:96px;top:150px"><div class="mn">1.3 · Versões</div><div class="t2" style="margin-top:20px">Quatro versões, sempre em ouro.</div></div>'
       '<div style="position:absolute;left:96px;right:96px;top:380px;bottom:120px;display:grid;grid-template-columns:1fr 1.4fr 1fr 1fr;gap:28px">' +
       ''.join(f'<div style="position:relative;overflow:hidden;box-shadow:inset 0 0 0 1px rgba(201,168,108,.25)">{wall(CONCD,.4,.6)}{glow(40,120,300,260,.5)}<div style="position:absolute;inset:40px 30px 90px;background:url({vimg(k)}) center/contain no-repeat"></div><div class="mn" style="position:absolute;left:30px;bottom:30px">{a}</div></div>' for a, k in var) + '</div>', '1.3 · Versões')
fund = [('Grafite fosco', 'felt', ''), ('Concreto', '', CONC), ('Pedra', '', PEDRA), ('Campo Lápis', 'lap', '')]
M.page('<div class="felt" style="position:absolute;inset:0"></div><div style="position:absolute;left:96px;top:150px;width:1500px"><div class="mn">1.4 · Fundos permitidos</div><div class="t2" style="margin-top:20px">O ouro só sobre superfície escura e nobre.</div></div>'
       '<div style="position:absolute;left:96px;right:96px;top:400px;bottom:120px;display:grid;grid-template-columns:repeat(4,1fr);gap:28px">' +
       ''.join(f'<div class="{c if c=="felt" else ""}" style="position:relative;overflow:hidden;{f"background:url({img}) center/cover;" if img else ""}{"background:"+LA+";" if c=="lap" else ""}">{glow(40,80,300,300,.6) if c!="lap" else ""}{mono(220, 90, 90)}<div class="mn" style="position:absolute;left:28px;bottom:28px;color:{MA}">{a}</div></div>' for a, c, img in fund) + '</div>', '1.4 · Fundos')
M.page(two('1.5 · Proteção e mínimo', 'Espaço para respirar.', 'Em volta da assinatura, deixe livre <b>X</b> = metade da largura do arco. Nenhum texto, borda ou imagem entra nessa área.<br><br><b>Mínimos</b><br>Horizontal: 120 px · 30 mm<br>Símbolo: 24 px · 6 mm<br>Hot stamping: 8 mm',
       painel(f'<div style="position:absolute;left:150px;top:200px;width:700px;height:420px;border:1px dashed #8E9BEA"></div>'
              f'<div style="position:absolute;left:230px;top:280px;width:540px;height:260px;background:url({vimg("horizontal")}) center/contain no-repeat"></div>'
              f'<div class="mn" style="position:absolute;left:150px;top:640px;color:#8E9BEA">X ao redor</div>', CONCD, .3)), '1.5 · Proteção')
proib = [('Não esticar', 'transform:scaleX(1.5)'), ('Não girar', 'transform:rotate(25deg)'), ('Não recolorir', 'filter:hue-rotate(160deg) saturate(3)'), ('Não usar sobre foto clara', 'opacity:.5'), ('Não pôr contorno', 'outline:3px solid #fff;outline-offset:6px'), ('Não usar a versão de linha chapada', 'filter:grayscale(1) brightness(1.8)')]
M.page('<div class="felt" style="position:absolute;inset:0"></div><div style="position:absolute;left:96px;top:150px"><div class="mn">1.6 · Usos proibidos</div><div class="t2" style="margin-top:20px">Seis erros que quebram a pedra.</div></div>'
       '<div style="position:absolute;left:96px;right:96px;top:370px;bottom:120px;display:grid;grid-template-columns:repeat(6,1fr);gap:22px">' +
       ''.join(f'<div style="position:relative;overflow:hidden;box-shadow:inset 0 0 0 1px rgba(201,168,108,.25);{"background:#cfc8bb;" if i==3 else ""}"><div style="position:absolute;left:50%;top:38%;width:170px;height:170px;margin:-85px 0 0 -85px;{st}">{mono(170)}</div>'
               f'<svg style="position:absolute;inset:0;width:100%;height:100%" viewBox="0 0 100 100" preserveAspectRatio="none"><path d="M10 10L90 90" stroke="#c0453a" stroke-width=".8"/></svg>'
               f'<div style="position:absolute;left:20px;right:20px;bottom:24px;font-size:21px;line-height:1.3;color:{OB if i==3 else MA}">{a}</div></div>' for i, (a, st) in enumerate(proib)) + '</div>', '1.6 · Proibidos')
M.abertura('02', 'Cor', 'Muito escuro, pouca luz: grafite, concreto, ouro e a hora azul.', CONCD)
pal = [('Obsidiana', OB, 'Base'), ('Grafite', '#22262E', 'Placas, cartões'), ('Concreto', '#8A8F98', 'Parede, apoio'), ('Lápis da Hora Azul', LA, 'Brilho atrás do ouro'), ('Marfim', MA, 'Texto sobre escuro')]
M.page('<div class="felt" style="position:absolute;inset:0"></div><div style="position:absolute;left:96px;top:140px"><div class="mn">2.1 · Paleta</div><div class="t2" style="margin-top:18px">Ouro escovado e cinco chapadas.</div></div>'
       f'<div style="position:absolute;left:96px;top:340px;width:560px;height:600px">{swatch_ouro(560, 470)}<div style="margin-top:22px;font:400 38px Fraunces">Ouro escovado</div><div class="mn" style="margin-top:8px;font-size:15px">Hot stamping · Pantone 871 C · ref. #B4935A</div></div>'
       '<div style="position:absolute;left:720px;right:96px;top:340px;height:600px;display:grid;grid-template-columns:repeat(5,1fr);gap:20px">' +
       ''.join(f'<div><div style="height:470px;background:{h};box-shadow:inset 0 0 0 1px rgba(238,234,226,.15)"></div><div style="margin-top:22px;font:400 28px/1.15 Fraunces">{n}</div><div class="mn" style="font-size:15px;margin-top:8px">{h} · {u}</div></div>' for n, h, u in pal) + '</div>', '2.1 · Paleta')
M.page(two('2.2 · Proporção', 'Muito escuro, pouca luz.', 'Obsidiana e grafite 60 · concreto 20 · Lápis 10 · ouro 5 · marfim 5.<br><br>O ouro só em símbolo, nome e filete, nunca em área grande. O Lápis só como brilho difuso atrás do ouro ou campo de cor, nunca em texto pequeno. CMYK e Pantone aproximados: confirme com prova impressa.',
       '<div style="display:flex;height:100%;gap:6px">' + ''.join(f'<div style="flex:{f};position:relative;{"background:"+OURO if c=="o" else "background:"+c};box-shadow:inset 0 0 0 1px rgba(238,234,226,.12)"><div class="mn" style="position:absolute;left:18px;bottom:20px;color:{OB if c in ("o",MA) else MA};writing-mode:vertical-rl;transform:rotate(180deg)">{n} {f}%</div></div>' for c, f, n in [(OB, 60, 'Obsidiana'), ('#8A8F98', 20, 'Concreto'), (LA, 10, 'Lápis'), ('o', 5, 'Ouro'), (MA, 5, 'Marfim')]) + '</div>'), '2.2 · Proporção')
M.abertura('03', 'Tipografia', 'Uma serifada com respiro, uma sem serifa precisa e um mono para rótulos.', SOMBRA)
M.page(f'<div class="felt" style="position:absolute;inset:0"></div>{glow(1000,200,800,500,.5)}<div style="position:absolute;left:96px;top:150px"><div class="mn">3.1 · Títulos · Fraunces</div></div>'
       f'<div class="ouro" style="position:absolute;left:90px;top:220px;font:400 360px/1 Fraunces;letter-spacing:.01em">Aa</div>'
       f'<div style="position:absolute;left:820px;right:96px;top:250px"><div style="font:400 92px/1.08 Fraunces">A passagem<br><i>da sua marca.</i></div><div class="p" style="margin-top:40px">Fraunces Regular e Itálica nos títulos, com espaço normal entre letras. No nome BARZAKH, versal com espaçamento largo (+24) e em ouro escovado.</div>'
       f'<div style="font:400 30px/1.5 Fraunces;margin-top:40px;color:rgba(238,234,226,.75)">ABCDEFGHIJKLMNOPQRSTUVWXYZ<br>abcdefghijklmnopqrstuvwxyz 0123456789</div></div>', '3.1 · Fraunces')
M.page(two('3.2 · Texto e rótulos', 'Inter Tight e JetBrains Mono.', '<b>Inter Tight</b> no texto corrido (400, mínimo 20 px numa tela de 1920). <b>JetBrains Mono</b> em caixa alta e espaçada para rótulos, numeração e o endosso.<br><br>Nunca mais de três famílias numa peça.',
       '<div style="display:grid;gap:40px">'
       '<div class="felt" style="padding:50px;box-shadow:inset 0 0 0 1px rgba(201,168,108,.3)"><div class="mn">Inter Tight · texto</div><div style="font:500 64px Inter Tight;margin-top:16px">Marca pronta para se apresentar.</div><div class="p" style="margin-top:14px">Aa Bb Cc 0123456789 — leitura clara em tela e papel.</div></div>'
       f'<div class="felt" style="padding:50px;box-shadow:inset 0 0 0 1px rgba(201,168,108,.3)"><div class="mn">JetBrains Mono · rótulos</div><div class="mn" style="font-size:34px;margin-top:20px;color:{MA}">{ENDOSSO(30, BR)}</div><div class="mn" style="font-size:24px;margin-top:20px">Capítulo 01 · v2 · 2026</div></div></div>'), '3.2 · Texto')
M.page(two('3.3 · Grafismo do arco', 'O arco recorta a imagem.', 'O símbolo vira sistema: a moldura em <b>arco</b> recorta concreto, pedra ou sombra de janela. Dentro dela, o monolito em ouro e o brilho Lápis.<br><br>Use um arco por peça. Ele pode ser alto (porta), largo (janela) ou cortado pela borda.',
       painel('<div style="position:absolute;inset:0;display:flex;gap:30px;align-items:flex-end;padding:60px">' +
              ''.join(f'<div class="arch" style="position:relative;width:{w}px;height:{h}px;border-radius:{w/2}px {w/2}px 0 0;background:url({img}) center/cover;flex:none">{glow(w*.1,h*.35,w*.8,h*.4,.7)}{mono(w*.45, w*.275, h*.4)}</div>' for w, h, img in [(220, 560, SOMBRA), (330, 420, PEDRA), (260, 700, COLUNA)]) + '</div>', CONCD, .2)), '3.3 · Grafismo')
M.abertura('04', 'Imagem', 'Só textura: concreto, pedra, sombra de janela. Nunca turismo.', COLUNA)
tx = [(CONC, 'Concreto aparente'), (PEDRA, 'Pedra'), (SOMBRA, 'Sombra de janela'), (COLUNA, 'Luz rasante'), (CONCD, 'Concreto escuro'), ('felt', 'Grafite fosco')]
M.page('<div class="felt" style="position:absolute;inset:0"></div><div style="position:absolute;left:96px;top:150px;width:600px"><div class="mn">4.1 · Texturas</div><div class="t2" style="margin:20px 0 30px">Superfície, não paisagem.</div><div class="p">Escura, granulada, com luz rasante. Sem pessoas de banco, sem cartão-postal, sem monumento. A mesma curva escura e o mesmo grão em todas.</div></div>'
       '<div style="position:absolute;left:800px;right:96px;top:150px;bottom:120px;display:grid;grid-template-columns:repeat(3,1fr);gap:20px">' +
       ''.join(f'<div class="{"felt" if i=="felt" else ""}" style="position:relative;{"" if i=="felt" else f"background:url({i}) center/cover;"}"><div class="mn" style="position:absolute;left:20px;bottom:18px;color:{MA};background:rgba(10,12,16,.6);padding:6px 10px">{n}</div></div>' for i, n in tx) + '</div>', '4.1 · Texturas')
M.abertura('05', 'Aplicações', 'Do avatar à fachada, a mesma placa de pedra e ouro.', CONC)
M.page(two('5.1 · Cartão', 'Grafite com hot stamping ouro.', '<b>Cartão</b> 85 × 50 mm em papel preto texturizado de 350 g ou mais. Frente: monolito em hot stamping ouro. Verso: nome em Fraunces, cargo em mono e logotipo em ouro.',
       painel(f'<div style="position:absolute;left:80px;top:120px;transform:rotate(-4deg)">{E.cartao(520, 306)}</div><div style="position:absolute;left:300px;top:430px;transform:rotate(5deg)">{E.cartao(520, 306, True)}</div>', CONC, .9)), '5.1 · Cartão')
M.page(two('5.2 · Papelaria escura', 'Papel, envelope e lacre.', '<b>Papel timbrado</b> A4 grafite: assinatura em ouro no topo, filete no rodapé.<br><b>Envelope</b> azul Lápis com o monolito em ouro.<br><b>Lacre</b> em cera bronze com o monolito gravado, para propostas e entregas.',
       painel(f'<div style="position:absolute;left:60px;top:40px;transform:rotate(-3deg)">{E.timbrado(380)}</div><div style="position:absolute;left:440px;top:330px;transform:rotate(4deg)">{E.envelope(500)}</div>'
              f'<div style="position:absolute;left:760px;top:120px">{"%s"}</div>', CONC, .9)).replace('%s', ''), '5.2 · Papelaria')
def selo(d):
    return (f'<div style="position:relative;width:{d}px;height:{d}px;border-radius:47% 53% 50% 48%/52% 46% 54% 48%;background:radial-gradient(circle at 35% 30%,#d9a86a,#9a6a33 45%,#5e3b17 85%);box-shadow:0 14px 30px rgba(0,0,0,.6),inset 0 -6px 14px rgba(0,0,0,.45),inset 0 4px 8px rgba(255,220,170,.35)">'
            f'<div style="position:absolute;inset:{d*.12}px;border-radius:50%;background:radial-gradient(circle at 40% 35%,#c08a4c,#7a4f22);box-shadow:inset 0 3px 8px rgba(0,0,0,.55),inset 0 -2px 4px rgba(255,220,170,.3)"></div>'
            f'<div style="position:absolute;left:{d*.25}px;top:{d*.25}px;width:{d*.5}px;height:{d*.5}px;background:#5e3b17;-webkit-mask:{mask("monolito-mono-branco")} center/contain no-repeat;filter:drop-shadow(0 1px 0 rgba(255,220,170,.45))"></div></div>')
def ecobag(w):
    h = w * 1.15
    return (f'<div style="position:relative;width:{w}px;height:{h+w*.45}px">'
            f'<div style="position:absolute;left:{w*.25}px;top:0;width:{w*.5}px;height:{w*.6}px;border:{w*.04}px solid #1a1c20;border-bottom:none;border-radius:{w*.25}px {w*.25}px 0 0"></div>'
            f'<div class="paper" style="position:absolute;left:0;top:{w*.45}px;width:{w}px;height:{h}px;background-color:#1d1f24;box-shadow:0 40px 70px rgba(0,0,0,.6);overflow:hidden">'
            f'<div style="position:absolute;inset:0;background:repeating-linear-gradient(0deg,rgba(255,255,255,.025) 0 2px,transparent 2px 4px),repeating-linear-gradient(90deg,rgba(0,0,0,.08) 0 2px,transparent 2px 4px)"></div>'
            f'{mono(w*.5, w*.25, h*.2)}{logot(w*.5, w*.25, h*.68)}<div class="win" style="opacity:.6"></div></div></div>')
M.page(two('5.3 · Lacre e ecobag', 'Objetos que se guardam.', '<b>Selo de cera</b> bronze: fecha a pasta de entrega da marca.<br><b>Ecobag</b> em lona grafite com monolito e logotipo em silk ouro metálico. A sombra de janela é parte da foto, não da peça.',
       painel(f'<div style="position:absolute;left:70px;top:60px">{ecobag(420)}</div><div style="position:absolute;left:600px;top:180px">{selo(240)}</div><div style="position:absolute;left:640px;top:470px;transform:rotate(-12deg)">{selo(170)}</div>', CONC, .95)), '5.3 · Objetos')
M.page(wall(CONC, .95, .55) + glow(600, 200, 900, 600, .3) + placa(1.05, 600, 130) +
       f'<div style="position:absolute;left:96px;bottom:120px;width:460px"><div class="mn">5.4 · Placa na parede</div><div class="p" style="margin-top:18px">Placa em arco de grafite fosco, 60 × 60 cm, presa no concreto com afastadores ocultos. Monolito e nome em ouro escovado. Luz rasante de cima.</div></div>', '5.4 · Placa')
tiles = [CONC, 'f', PEDRA, SOMBRA, 'f', CONCD, 'f', COLUNA, PEDRA]
def phone(w=400):
    h = w * 2.05
    cel = ''.join(f'<div style="position:relative;aspect-ratio:4/5;{"background:"+GRAF if t=="f" else f"background:url({t}) center/cover"};overflow:hidden">{glow(10,30,100,80,.6) if t=="f" else ""}{mono(w*.12, w*.105, w*.13)}</div>' for t in tiles)
    return (f'<div style="position:relative;width:{w}px;height:{h}px;border-radius:{w*.13}px;background:#0b0c0f;padding:{w*.035}px;box-shadow:0 0 0 2px #2a2c31,0 50px 90px rgba(0,0,0,.7)">'
            f'<div style="width:100%;height:100%;border-radius:{w*.1}px;background:{OB};overflow:hidden;padding:{w*.12}px {w*.05}px 0">'
            f'<div style="display:flex;gap:{w*.05}px;align-items:center"><div style="width:{w*.22}px;height:{w*.22}px;border-radius:50%;background:url({vimg("avatar")}) center/cover;flex:none"></div>'
            f'<div style="font-size:{w*.04}px;line-height:1.4"><b style="font-size:{w*.047}px">@barzakhstudio</b><br>Barzakh · um estúdio Al Kántara<br><span style="color:#c9a86c">A passagem da sua marca.</span></div></div>'
            f'<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:3px;margin-top:{w*.08}px">{cel}</div></div></div>')
M.page(two('5.5 · Avatar e perfil', '@barzakhstudio', 'O avatar é sempre o monolito em ouro sobre grafite com o brilho Lápis, igual em Instagram, WhatsApp, YouTube e Google.<br><br>O feed alterna concreto, grafite e pedra, sempre com o símbolo em ouro.',
       painel(f'<div style="position:absolute;left:60px;top:150px;width:320px;height:320px;border-radius:50%;background:url({vimg("avatar")}) center/cover;box-shadow:0 30px 60px rgba(0,0,0,.6)"></div>'
              f'<div style="position:absolute;left:480px;top:-10px;transform:scale(.98);transform-origin:0 0">{phone(390)}</div>', CONCD)), '5.5 · Perfil')
def post45(w, titulo):
    h = w * 1.25
    return (f'<div style="position:relative;width:{w}px;height:{h}px;overflow:hidden;box-shadow:0 40px 80px rgba(0,0,0,.6)">{wall(CONC, .8, .6)}'
            f'{arch(w*.18, h*.12, w*.64, h*.62, None, glow(w*.1, h*.2, w*.44, h*.3, .8) + mono(w*.32, w*.16, h*.18))}'
            f'<div style="position:absolute;left:{w*.08}px;right:{w*.08}px;top:{h*.78}px;text-align:center;font:400 {w*.065}px/1.15 Fraunces;color:{MA}">{titulo}</div></div>')
def story(w):
    h = w * 16 / 9
    return (f'<div class="felt" style="position:relative;width:{w}px;height:{h}px;overflow:hidden;box-shadow:0 40px 80px rgba(0,0,0,.6)">'
            f'{arch(w*.1, h*.14, w*.8, h*.55, PEDRA, glow(w*.1, h*.15, w*.6, h*.25, .8) + mono(w*.4, w*.2, h*.16))}'
            f'{logot(w*.6, w*.2, h*.74)}<div style="position:absolute;left:0;right:0;top:{h*.85}px;text-align:center;font:500 {w*.035}px JetBrains Mono;letter-spacing:.2em;color:{BR}">{ENDOSSO(w*.035)}</div></div>')
M.page(two('5.6 · Post 4:5 e story', 'O arco em cada tela.', 'Post 1080 × 1350 e story 1080 × 1920: parede de concreto ou grafite, arco recortando a textura, monolito em ouro e frase curta em Fraunces.<br><br>Texto ilustrativo nos modelos.',
       painel(f'<div style="position:absolute;left:60px;top:90px">{post45(440, "Sua marca pronta para se apresentar.")}</div><div style="position:absolute;left:580px;top:20px">{story(400)}</div>', CONCD, .4)), '5.6 · Social')
M.page(two('5.7 · Assinatura de e-mail', 'Curta e sem imagem pesada.', 'Nome em serifada, cargo em mono, monolito e logotipo em ouro e o endosso. Sem frase motivacional, sem banner. O WhatsApp é sempre o oficial do site.',
       painel(f'<div class="felt" style="position:absolute;left:60px;right:60px;top:200px;padding:60px;box-shadow:0 30px 60px rgba(0,0,0,.6);display:flex;gap:50px;align-items:center">{mono_inline(170)}'
              f'<div style="border-left:1px solid {BR};padding-left:50px"><div style="font:400 50px Fraunces">Lindson Almeida</div><div class="mn" style="margin-top:10px">Direção criativa</div>{logot(300, None, None, "margin-top:28px")}<div class="mn" style="margin-top:20px;color:rgba(238,234,226,.7)">{ENDOSSO(17)} · @barzakhstudio</div></div></div>', CONC, .9)), '5.7 · E-mail')
M.page(wall(CONCD, .8, .85) + glow(560, 260, 800, 500, .55) + mono(320, 800, 250) +
       f'<div style="position:absolute;left:0;right:0;top:640px;text-align:center">{logot(560, None, None, "margin:0 auto")}<div class="mn" style="margin-top:34px">@barzakhstudio · {ENDOSSO(16)}</div></div>', hf=False)

CHECK = r"""() => { const out=[]; document.querySelectorAll('section.pg').forEach((s,i)=>{ const r=s.getBoundingClientRect();
 s.querySelectorAll('div,span').forEach(e=>{ if(!e.childNodes.length) return; const t=[...e.childNodes].filter(n=>n.nodeType==3&&n.textContent.trim()).length; if(!t) return;
  const b=e.getBoundingClientRect(); if(b.width==0) return;
  if(b.right>r.right+1||b.bottom>r.bottom+1||b.left<r.left-1) out.push((i+1)+': fora '+e.textContent.slice(0,40));
  if(e.scrollWidth>e.clientWidth+2 && getComputedStyle(e).overflow=='hidden') out.push((i+1)+': cortado '+e.textContent.slice(0,40));
  const fs=parseFloat(getComputedStyle(e).fontSize); if(fs<15) out.push((i+1)+': miudo '+fs+' '+e.textContent.slice(0,30)); }); }); return out; }"""

def logos_ouro(b):
    pg = b.new_page(viewport={'width': 1600, 'height': 1600})
    css = f'<style>{CSS}</style>'
    itens = {'simbolo': (1200, 1200, mono(1000, 100, 100)),
             'horizontal': (2400, 700, mono(560, 60, 70) + logot(1500, 760, 170) + f'<div class="mn" style="position:absolute;left:770px;top:540px;font-size:44px">{ENDOSSO(44)}</div>'),
             'vertical': (1400, 1500, mono(700, 350, 40) + logot(1200, 100, 830) + f'<div class="mn" style="position:absolute;left:0;right:0;top:1200px;text-align:center;font-size:44px">{ENDOSSO(44)}</div>'),
             'avatar': (1080, 1080, f'<div class="felt" style="position:absolute;inset:0;border-radius:50%;overflow:hidden">{glow(240,330,600,460,.9)}</div>' + mono(620, 230, 200))}
    for k, (w, h, inner) in itens.items():
        pg.set_viewport_size({'width': w, 'height': h})
        pg.set_content(f'<html><head><meta charset="utf-8"><link rel="stylesheet" href="{E.FONTS}">{css}</head><body style="margin:0;background:transparent"><div style="position:relative;width:{w}px;height:{h}px">{inner}</div></body></html>')
        pg.wait_for_timeout(2500); pg.evaluate('document.fonts.ready')
        pg.screenshot(path=f'{PNG}/barzakh-{k}-ouro.png', omit_background=True)
    pg.close()

def render():
    with sync_playwright() as p:
        b = p.chromium.launch(proxy={'server': os.environ['HTTPS_PROXY']} if os.environ.get('HTTPS_PROXY') else None, args=['--allow-file-access-from-files'], executable_path='/opt/pw-browsers/chromium-1243/chrome-linux64/chrome')
        logos_ouro(b)
        for doc, nome in [(K, 'barzakh-branding-book-v2'), (M, 'barzakh-manual-de-marca-v2')]:
            h = f'{G}/{nome}.html'; open(h, 'w').write(doc.html())
            pg = b.new_page(viewport={'width': 1920, 'height': 1080}); pg.goto('file://' + h); pg.wait_for_timeout(4000); pg.evaluate('document.fonts.ready')
            probs = pg.evaluate(CHECK); print(nome, len(doc.p), 'páginas ·', len(probs), 'alertas')
            for x in probs: print('  ', x)
            d = f'{OUT}/paginas-v2/{nome}'; shutil.rmtree(d, ignore_errors=True); os.makedirs(d)
            for i, el in enumerate(pg.query_selector_all('section.pg')): el.screenshot(path=f'{d}/{i+1:02d}.jpg', type='jpeg', quality=88)
            pg.close()
            ims = [Image.open(f).convert('RGB') for f in sorted(glob.glob(f'{d}/*.jpg'))]
            ims[0].save(f'{OUT}/{nome}.pdf', save_all=True, append_images=ims[1:], resolution=144, quality=88)
        b.close()

if __name__ == '__main__': render()
