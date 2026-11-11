# Desentupidora SF · feed v1 (4 artes 1080x1350) · conta Zuleide, 03/11/2026.
# Fluxo aprovado do Leo (instagram-v14-datas): HTML -> Playwright (render.js) -> JPG, depois feed.py monta a prévia.
# Regra do Lindson: nada se cria, tudo se copia. Cada arte copia a composição de um modelo existente (citado em cada bloco
# e em textos.json; capturas em referencias/). Identidade do cliente = site desentupidorasf.pages.dev + flyer do cliente:
# azul royal/marinho, laranja de destaque, branco, Montserrat 800/900 com itálico 900 nos títulos, logo circular oficial.
# Sem emojis, adesivos ou ícones 3D. Assinatura fixa em todas: logo + @ + WhatsApp no rodapé esquerdo.
# Uso: python3 gerar.py . && node render.js $PWD && python3 feed.py .
import sys
d = sys.argv[1] if len(sys.argv) > 1 else '.'
NAVY, BLUE, ROY, SKY, LAR, LAR2, BG = '#061a4a', '#0a2a6e', '#1d5fd0', '#3fa9ff', '#ff6a00', '#ff8a00', '#f4f8ff'
ARROBA, ZAP = '@desentupidorasf_slz', '(98) 92010-5710'
GRAO = ("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'>"
        "<filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='3' stitchTiles='stitch'/>"
        "<feColorMatrix values='0 0 0 0 .5  0 0 0 0 .5  0 0 0 0 .5  0 0 0 .9 0'/></filter><rect width='100%25' height='100%25' filter='url(%23n)'/></svg>")


def assina(claro=True, top=1170):
    """Assinatura fixa: logo circular oficial + @ + WhatsApp, sempre no rodapé esquerdo."""
    c1, c2 = ('#fff', 'rgba(255,255,255,.85)') if claro else (BLUE, '#3d4f73')
    return (f'<div class="a sig" style="left:64px;top:{top}px"><img src="assets/logo.jpg">'
            f'<div><b style="color:{c1}">{ARROBA}</b><span style="color:{c2}">WhatsApp {ZAP}</span></div></div>')


P = []
# 1 · SOCORRO RÁPIDO · FOTO (Pexels 6419128, mãos de profissional no encanamento embaixo da pia) · fundo AZUL ROYAL
#   Cópia do Designi "Desentupidora Precisa de Ajuda Urgente" (designi.com.br/58a306c92cd5fca2): foto grande ocupando a arte,
#   cartão de cor com cantos arredondados à direita com a pergunta em caixa alta, pílula branca de chamada com seta e
#   segunda pílula branca embaixo (no modelo: bandeiras de cartão; aqui: os serviços). O selo 3D do modelo foi tirado (proibido).
P.append(('p1', f"""
<img class="a" src="assets/pexels-6419128.jpg" style="inset:0;width:1080px;height:1350px;object-fit:cover;object-position:38% 50%;filter:saturate(.8) contrast(1.08) brightness(1.12)">
<div class="a" style="inset:0;background:{ROY};mix-blend-mode:multiply;opacity:.30"></div>
<div class="a" style="inset:0;background:linear-gradient(90deg,rgba(6,26,74,.10) 0,rgba(6,26,74,.20) 40%,rgba(10,42,110,.80) 70%,rgba(10,42,110,.95) 100%)"></div>
<div class="a" style="inset:0;background:linear-gradient(180deg,rgba(6,26,74,.55) 0,rgba(6,26,74,0) 22%,rgba(6,26,74,0) 70%,rgba(6,26,74,.85) 100%)"></div>
<div class="a kick" style="left:64px;top:70px;color:#fff">Desentupidora em São Luís</div>
<div class="a" style="left:500px;top:300px;width:520px;padding:48px 44px 92px;background:linear-gradient(160deg,{LAR2},{LAR});border-radius:44px 120px 44px 44px;box-shadow:0 40px 70px -30px rgba(0,0,0,.55)">
 <div class="T" style="font-size:70px;color:{NAVY}">Água<br>voltando<br>pelo ralo?</div>
 <div class="t" style="font-size:28px;color:#fff;margin-top:22px;line-height:1.3">Não espere o banheiro alagar. A SF resolve sem quebrar piso.</div></div>
<div class="a pil" style="left:530px;top:820px;width:460px"><i>›</i><div>Mande foto no WhatsApp<br><b>orçamento grátis</b></div></div>
<div class="a pil2" style="left:530px;top:960px;width:460px">Pia · Ralo · Vaso · Esgoto</div>
{assina(True)}"""))

# 2 · EVITE O PREJUÍZO · SÓ LOGO (cenário: ralo de inox Pexels 220612, quase transparente com véu laranja) · fundo LARANJA
#   Cópia do Designi "Lembrete Não Espere o Entupimento Acontecer" (designi.com.br/29d59e4074114199): a mesma frase repetida
#   4 vezes em letras gigantes, cartão branco no centro com faixa de cor no topo, título e texto, botão arredondado saindo
#   da base do cartão e onda escura no rodapé com os contatos.
REP = ''.join(f'<div class="T" style="font-size:150px;line-height:.98;color:{c}">Óleo na pia</div>' for c in (BLUE, 'rgba(10,42,110,.55)', 'rgba(10,42,110,.55)', BLUE))
P.append(('p2', f"""
<img class="a" src="assets/pexels-220612.jpg" style="inset:0;width:1080px;height:1350px;object-fit:cover;opacity:.30;filter:grayscale(1) contrast(1.2);mix-blend-mode:multiply">
<div class="a" style="inset:0;background:radial-gradient(700px 600px at 70% 30%,rgba(255,176,32,.55),transparent 70%)"></div>
<div class="a" style="left:0;width:1080px;top:150px;text-align:center">{REP}</div>
<div class="a" style="left:200px;top:400px;width:680px;background:#fffaf2;border-radius:40px;overflow:hidden;box-shadow:0 40px 70px -24px rgba(90,30,0,.55)">
 <div style="background:{BLUE};height:64px;display:flex;align-items:center;justify-content:center"><span class="kick" style="color:#fff;font-size:22px">Lembrete</span></div>
 <div style="padding:34px 50px 70px;text-align:center"><div class="T" style="font-size:52px;color:{BLUE};line-height:1.02">A gordura endurece<br><span style="color:{LAR}">e entope o cano</span></div>
 <div class="t" style="font-size:29px;color:#2a3655;margin-top:22px;line-height:1.35">Óleo de fritura não vai na pia. Guarde numa garrafa e leve ao ponto de coleta.</div></div></div>
<div class="a pil" style="left:290px;top:820px;width:500px;background:{BLUE};color:#fff;justify-content:center"><i style="background:{LAR2}">›</i><div>Pia já entupiu?<br><b style="color:{LAR2}">orçamento grátis</b></div></div>
<svg class="a" style="left:0;top:1060px" width="1080" height="290"><path d="M0 70 C 220 0 420 10 600 60 C 800 115 960 90 1080 30 L1080 290 L0 290 Z" fill="{BLUE}"/></svg>
{assina(True, 1175)}"""))

# 3 · BASTIDORES DO SERVIÇO · FOTO (técnico da SF, material do cliente no site, + foto real de serviço: caixa de esgoto aberta)
#   fundo MARINHO ESCURO · Cópia do Designi "Desentupidora Pia da Cozinha Entupida" (designi.com.br/273594c76412bf7e):
#   cartão laranja com o profissional no alto à esquerda, traço laranja + título em duas cores à direita, pílula laranja do
#   telefone saindo por cima da 2ª foto (cartão claro embaixo à direita) e logo + @ embaixo. O escudo 3D do modelo foi tirado.
P.append(('p3', f"""
<div class="a" style="inset:0;background:radial-gradient(900px 800px at 80% 20%,#123a8a 0,transparent 60%),radial-gradient(700px 700px at 0% 100%,#0a2a6e 0,transparent 60%)"></div>
<div class="a" style="left:64px;top:150px;width:430px;height:470px;border-radius:40px;background:linear-gradient(160deg,{LAR2},{LAR});overflow:hidden;box-shadow:0 40px 70px -30px rgba(0,0,0,.7)">
 <img src="assets/tecnico.jpg" style="position:absolute;left:30px;top:24px;width:380px;height:446px;object-fit:cover;object-position:50% 0;border-radius:28px 28px 0 0"></div>
<div class="a kick" style="left:64px;top:84px;color:{SKY}">Desentupidora SF · São Luís</div>
<div class="a" style="left:545px;top:200px;width:180px;height:9px;background:{LAR2};border-radius:9px"></div>
<div class="a" style="left:545px;top:236px;width:480px"><div class="T" style="font-size:58px;color:#fff;line-height:1.02">Caixa de<br>esgoto</div>
 <div class="T" style="font-size:58px;color:{LAR2};line-height:1.02">cheia assim?</div>
 <div class="t" style="font-size:26px;color:rgba(255,255,255,.85);margin-top:22px;line-height:1.35">Quando ela enche, o mau cheiro sobe e o esgoto volta pelo ralo.</div></div>
<div class="a" style="left:500px;top:610px;width:520px;height:440px;border-radius:40px;overflow:hidden;box-shadow:0 40px 70px -30px rgba(0,0,0,.7);border:6px solid #fff">
 <img src="assets/caixa-esgoto.jpg" style="width:100%;height:100%;object-fit:cover;object-position:0 70%;transform:scale(1.12);transform-origin:20% 80%">
 <div class="kick" style="position:absolute;left:18px;bottom:18px;background:rgba(6,26,74,.88);color:#fff;font-size:16px;letter-spacing:.14em;padding:10px 16px;border-radius:999px">Foto real de um serviço da SF</div></div>
<div class="a" style="left:64px;top:700px;width:520px;height:118px;border-radius:60px;background:linear-gradient(90deg,{LAR2},{LAR});display:flex;align-items:center;gap:20px;padding:0 30px 0 16px;box-shadow:0 30px 50px -24px rgba(0,0,0,.7)">
 <div style="width:88px;height:88px;border-radius:50%;background:#fff3e4;display:grid;place-items:center;font:900 italic 17px Montserrat;color:{LAR};text-transform:uppercase;letter-spacing:-.01em;line-height:1;text-align:center">Whats<br>App</div>
 <div class="T" style="font-size:44px;color:{NAVY};white-space:nowrap"><span style="font-size:28px">(98)</span> 92010-5710</div></div>
<div class="a kick" style="left:64px;top:870px;color:#fff;font-size:20px;line-height:1.7">Orçamento grátis<br><span style="color:{LAR2}">Sem quebra-quebra</span></div>
{assina(True)}"""))

# 4 · FALA COM A GENTE · SÓ LOGO · fundo CLARO (branco azulado do site) · Cópia do cartão de enquete "Conta pra gente!"
#   do Leo (31/12, aprovado pelo Lindson em 03/11; ele copiou o Designi "Qual a marca da sua primeira bike?"):
#   pergunta no topo com a 2ª linha numa caixa de cor, cartão branco com faixa de cor e 4 opções numeradas, palavra gigante
#   quase transparente atrás e "comenta o número" embaixo.
OPS = ['Pia da cozinha', 'Ralo do banheiro', 'Vaso sanitário', 'Caixa de gordura']
P.append(('p4', f"""
<div class="a" style="inset:0;background:radial-gradient(900px 700px at 20% 10%,#ffffff 0,{BG} 50%,#dbe7fb 100%)"></div>
<div class="a" style="left:-20px;top:760px;width:1140px;text-align:right"><div class="T" style="font-size:330px;line-height:.82;color:rgba(29,95,208,.10)">Entu<br>piu?</div></div>
<div class="a" style="left:0;width:1080px;top:120px;text-align:center"><div class="kick" style="color:{ROY}">Desentupidora SF pergunta</div>
 <div class="T" style="font-size:86px;color:{BLUE};margin-top:18px">O que já entupiu</div>
 <div style="margin-top:12px"><span class="T box" style="font-size:66px;background:{LAR};color:#fff">aí na sua casa?</span></div></div>
<div class="a" style="left:150px;top:470px;width:780px;background:#fff;border-radius:36px;overflow:hidden;box-shadow:0 40px 70px -30px rgba(6,26,74,.45)">
 <div class="T" style="background:{ROY};color:#fff;text-align:center;font-size:54px;padding:22px 0 18px">Conta pra gente!</div>
 <div style="padding:28px 34px 32px;display:flex;flex-direction:column;gap:16px">{''.join(f'<div class="op"><b>{n}</b>{t}</div>' for n, t in zip('1234', OPS))}</div></div>
<div class="a" style="left:0;width:1080px;top:1035px;text-align:center"><span class="T" style="font-size:46px;color:{LAR}">comenta o número aqui embaixo</span></div>
{assina(False)}"""))

secs = ''.join(f'<section class="f" id="{i}" style="background:{bg}">{c}<div class="a" style="inset:0;background-image:url(&quot;{GRAO}&quot;);opacity:.08;mix-blend-mode:overlay;pointer-events:none"></div></section>'
               for (i, c), bg in zip(P, [ROY, LAR2, NAVY, BG]))
html = f"""<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,600;0,700;0,800;0,900;1,800;1,900&display=swap" rel="stylesheet">
<style>*{{margin:0;padding:0;box-sizing:border-box}} body{{background:#222}}
.f{{position:relative;width:1080px;height:1350px;overflow:hidden;margin-bottom:20px;font-family:Montserrat}} .a{{position:absolute}}
.T{{font-family:Montserrat;font-weight:900;font-style:italic;text-transform:uppercase;letter-spacing:-.02em;line-height:.95}}
.t{{font-family:Montserrat;font-weight:600}}
.kick{{font-family:Montserrat;font-weight:800;text-transform:uppercase;letter-spacing:.22em;font-size:21px}}
.box{{display:inline-block;padding:8px 26px 10px;box-shadow:0 20px 34px -20px rgba(6,26,74,.7);transform:rotate(-2deg)}}
.pil{{display:flex;align-items:center;gap:18px;background:#fff;border-radius:28px;padding:18px 26px 18px 18px;font-weight:700;font-size:26px;line-height:1.2;color:{BLUE};box-shadow:0 26px 44px -22px rgba(0,0,0,.6)}}
.pil b{{font-weight:900;font-style:italic;text-transform:uppercase;font-size:28px;color:{LAR}}}
.pil i{{flex:none;display:grid;place-items:center;width:64px;height:64px;border-radius:50%;background:{BLUE};color:#fff;font:900 46px/1 Montserrat;padding-bottom:6px}}
.pil2{{background:#fff;border-radius:22px;padding:20px 22px;font-weight:800;font-size:22px;letter-spacing:.04em;text-transform:uppercase;color:{BLUE};text-align:center;box-shadow:0 26px 44px -22px rgba(0,0,0,.6)}}
.op{{display:flex;align-items:center;gap:18px;border:2.5px solid {ROY};border-radius:18px;padding:14px 18px;font-weight:800;font-size:30px;color:{BLUE};text-transform:uppercase}}
.op b{{display:grid;place-items:center;width:50px;height:50px;border-radius:50%;background:{LAR};color:#fff;font-size:26px;font-weight:900}}
.sig{{display:flex;align-items:center;gap:20px}} .sig img{{width:118px;height:118px;border-radius:50%;object-fit:cover;clip-path:circle(48.5%);box-shadow:0 14px 26px -12px rgba(0,0,0,.6)}}
.sig div{{display:flex;flex-direction:column;gap:4px}} .sig b{{font-weight:800;font-size:27px}} .sig span{{font-weight:700;font-size:23px}}
</style></head><body>{secs}</body></html>"""
open(f'{d}/artes.html', 'w').write(html)
print('artes.html ok')
