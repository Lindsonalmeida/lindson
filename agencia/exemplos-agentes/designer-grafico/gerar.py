# Pizzaria Brasa Viva (EXEMPLO DEMONSTRATIVO, marca fictícia) · Designer gráfico, conta Zuleide, 08/11/2026
# Gera logo/*.svg, prancha.html e aplicacoes.html. Depois: node render.js -> prancha.png e aplicacoes.png
# Referências copiadas (composição, nunca marca):
#  1) Decaf Girl · Misato Studio (favoritas/pin-962081539173882007): listras verticais na base da lata -> copo e caixa;
#     letra gorda curta em caixa alta; produto inteiro numa cor.
#  2) HOTWHIZ · Behance (favoritas/pin-1144969905302172033): cor chapada saturada + manchete gigante + ícone de chama
#     no rótulo -> post 4:5 e hero da prancha.
#  3) PizzaExpress · BrandOpus (PESQUISA-08-11 item 4) + Celentano (conceito): um ativo só, ampliado em tudo ->
#     os 3 anéis do arco viram faixas, padrão, moldura e recorte gigante.
import os, base64
D = os.path.dirname(os.path.abspath(__file__))
P = '../../operacao-propria/identidade/fotos-v4/'
FAV = '../../operacao-propria/biblioteca-pizzaria/favoritas/'
C = dict(farinha='#F3E7D3', brasa='#E2431D', carvao='#1A1411', chama='#FFB321', manj='#2E5B3B')

FL_OUT = 'M100 172C80 172 72 158 74 144C76 132 84 126 86 116C92 124 92 130 96 132C94 116 100 98 112 86C110 102 120 110 124 124C127 134 128 140 126 148C123 162 114 172 100 172Z'
FL_IN = 'M100 172C90 172 86 164 88 156C90 148 96 146 98 138C104 146 112 150 112 158C112 166 108 172 100 172Z'

def arcos(cor, w=14):
    s = ''
    for r in (84, 62, 40):
        s += f'<path d="M{100-r} 176V96A{r} {r} 0 0 1 {100+r} 96V176" fill="none" stroke="{cor}" stroke-width="{w}"/>'
    return s + f'<rect x="9" y="182" width="182" height="12" fill="{cor}"/>'

def simbolo(arc=C['brasa'], fo=C['chama'], fi=C['brasa'], extra=''):
    return (f'<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg" {extra}>' + arcos(arc) +
            f'<path d="{FL_OUT}" fill="{fo}"/><path d="{FL_IN}" fill="{fi}"/></svg>')

def carimbo(cor, fundo='none', txt='PIZZARIA BRASA VIVA · FORNO A LENHA · SÃO LUÍS - MA · ', extra=''):
    return (f'<svg viewBox="0 0 300 300" xmlns="http://www.w3.org/2000/svg" {extra}>'
            f'<circle cx="150" cy="150" r="146" fill="{fundo}" stroke="{cor}" stroke-width="6"/>'
            f'<circle cx="150" cy="150" r="104" fill="none" stroke="{cor}" stroke-width="3"/>'
            f'<defs><path id="cp" d="M150 150m-122 0a122 122 0 1 1 244 0a122 122 0 1 1-244 0"/></defs>'
            f'<text font-family="DM Sans" font-weight="700" font-size="19.5" letter-spacing="3.4" fill="{cor}">'
            f'<textPath href="#cp">{txt}</textPath></text>'
            f'<g transform="translate(88 82) scale(.62)">' + arcos(cor) +
            f'<path d="{FL_OUT}" fill="{cor}"/><path d="{FL_IN}" fill="{fundo if fundo!="none" else "#fff0"}"/></g></svg>')

# ---------- arquivos de logo ----------
os.makedirs(os.path.join(D, 'logo'), exist_ok=True)
FONT = "font-family=\"Bricolage Grotesque\" font-weight=\"800\" font-stretch=\"75%\""
open(os.path.join(D, 'logo/simbolo.svg'), 'w').write(simbolo())
open(os.path.join(D, 'logo/carimbo.svg'), 'w').write(carimbo(C['brasa']))
open(os.path.join(D, 'logo/horizontal.svg'), 'w').write(
    f'<svg viewBox="0 0 760 200" xmlns="http://www.w3.org/2000/svg"><g>{arcos(C["brasa"])}<path d="{FL_OUT}" fill="{C["chama"]}"/><path d="{FL_IN}" fill="{C["brasa"]}"/></g>'
    f'<text x="228" y="132" {FONT} font-size="128" fill="{C["carvao"]}">BRASA VIVA</text>'
    f'<text x="232" y="180" font-family="DM Sans" font-weight="700" font-size="26" letter-spacing="7" fill="{C["brasa"]}">PIZZARIA · SÃO LUÍS</text></svg>')
open(os.path.join(D, 'logo/vertical.svg'), 'w').write(
    f'<svg viewBox="0 0 400 520" xmlns="http://www.w3.org/2000/svg"><g transform="translate(110 0) scale(.9)">{arcos(C["brasa"])}<path d="{FL_OUT}" fill="{C["chama"]}"/><path d="{FL_IN}" fill="{C["brasa"]}"/></g>'
    f'<text x="200" y="320" text-anchor="middle" {FONT} font-size="140" fill="{C["carvao"]}">BRASA</text>'
    f'<text x="200" y="440" text-anchor="middle" {FONT} font-size="140" fill="{C["brasa"]}">VIVA</text>'
    f'<text x="200" y="500" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="24" letter-spacing="7" fill="{C["carvao"]}">PIZZARIA · SÃO LUÍS</text></svg>')

def uri(svg):
    return 'data:image/svg+xml;base64,' + base64.b64encode(svg.encode()).decode()

# padrão de arcos (grafismo 1)
PAD = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="120" height="120">'
       f'<rect width="200" height="200" fill="{C["brasa"]}"/>' + arcos(C['farinha']).replace('<rect', '<rect opacity="0"') + '</svg>')
PAD2 = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="90" height="90">'
        f'<rect width="200" height="200" fill="{C["carvao"]}"/>' + arcos('#3a2c24').replace('<rect', '<rect opacity="0"') + '</svg>')

HEAD = '''<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wdth,wght@12..96,75..100,200..800&family=DM+Sans:opsz,wght@9..40,400..700&display=swap" rel="stylesheet">
<style>
:root{--f:#F3E7D3;--b:#E2431D;--c:#1A1411;--ch:#FFB321;--m:#2E5B3B}
*{box-sizing:border-box;margin:0;padding:0}
body{width:1440px;background:var(--c);font-family:'DM Sans',sans-serif;color:var(--c)}
.t{font-family:'Bricolage Grotesque';font-weight:800;font-stretch:75%;text-transform:uppercase;line-height:.86;letter-spacing:-.01em}
.et{font-weight:700;font-size:13px;letter-spacing:.18em;text-transform:uppercase}
.faixas{background:repeating-linear-gradient(180deg,var(--b) 0 14px,transparent 14px 22px)}
.vfaixas{background:repeating-linear-gradient(90deg,var(--b) 0 14px,var(--f) 14px 26px)}
.arco{border-radius:999px 999px 0 0;overflow:hidden}
.arco img{width:100%;height:100%;object-fit:cover;display:block}
section{position:relative;overflow:hidden}
.num{font-family:'Bricolage Grotesque';font-weight:800;font-stretch:75%;font-size:15px;letter-spacing:.1em}
.demo{position:absolute;font-weight:700;font-size:11px;letter-spacing:.2em;text-transform:uppercase;padding:7px 12px;border:1.5px solid currentColor;border-radius:99px}
</style></head><body>'''

def sec_titulo(n, txt, cor='var(--c)', sub=''):
    return (f'<div style="display:flex;align-items:baseline;gap:22px;margin-bottom:34px;color:{cor}">'
            f'<span class="num" style="color:var(--b)">{n}</span><h2 class="t" style="font-size:66px">{txt}</h2>'
            f'<span style="margin-left:auto;font-size:15px;max-width:440px;opacity:.8;line-height:1.45">{sub}</span></div>')

S = simbolo
# ================= PRANCHA =================
h = HEAD
# --- A · HERO (HOTWHIZ: cor chapada + manchete gigante; foto na boca do forno)
h += f'''<section style="height:960px;background:var(--c);color:var(--f);padding:64px">
<span class="demo" style="top:40px;left:64px;color:var(--ch)">Exemplo demonstrativo · marca fictícia</span>
<span class="et" style="position:absolute;top:48px;right:64px;opacity:.7">Manual de identidade · v1 · 08/11/2026</span>
<div style="position:absolute;left:64px;top:130px;width:640px">
  <div style="width:150px;height:150px">{S()}</div>
  <h1 class="t" style="font-size:210px;margin-top:26px">Brasa<br><span style="color:var(--b)">Viva</span></h1>
  <div class="et" style="margin-top:22px;color:var(--ch)">Pizzaria · forno a lenha · São Luís - MA</div>
  <p style="margin-top:34px;font-size:22px;line-height:1.4;max-width:520px;opacity:.92">Conceito <b style="color:var(--ch)">“A boca do forno”</b>: tudo o que a marca mostra é visto de dentro do forno a lenha. O arco é logo, moldura, padrão e faixa.</p>
</div>
<div style="position:absolute;left:720px;top:212px;width:780px;height:686px">
  <svg viewBox="0 0 200 200" style="position:absolute;left:0;top:0;width:780px;height:780px">{''.join(f'<path d="M{100-r} 176V96A{r} {r} 0 0 1 {100+r} 96V176" fill="none" stroke="{C["brasa"]}" stroke-width="9"/>' for r in (84,62))}</svg>
  <div class="arco" style="position:absolute;left:166px;top:150px;width:448px;height:536px"><img src="{P}pepperoni-cima.jpg" style="object-position:50% 50%"></div>
  <div style="position:absolute;left:330px;top:470px;width:120px;height:120px;filter:drop-shadow(0 8px 18px rgba(0,0,0,.5))"><svg viewBox="70 80 60 96"><path d="{FL_OUT}" fill="{C["chama"]}"/><path d="{FL_IN}" fill="{C["brasa"]}"/></svg></div>
</div>
<div class="faixas" style="position:absolute;left:0;right:0;bottom:0;height:62px;opacity:1"></div>
<span style="position:absolute;left:64px;bottom:82px;font-size:11px;opacity:.55">Foto: Andy Li, CC0, Wikimedia Commons</span>
</section>'''

# --- B · PERSONA + CONCEITO
h += f'''<section style="background:var(--f);padding:80px 64px 72px">
{sec_titulo('01','Para quem é',sub='A marca serve a quem compra. Teste: essa pessoa pediria desta pizzaria? Sim: parece séria, quente e da cidade.')}
<div style="display:grid;grid-template-columns:1.15fr 1fr 1fr;gap:20px">
 <div style="background:var(--c);color:var(--f);border-radius:22px;padding:34px">
  <div class="et" style="color:var(--ch)">Persona · Camila, 34</div>
  <ol style="margin-top:18px;padding-left:20px;font-size:17px;line-height:1.5">
   <li>Analista no Renascença, casada, 1 filho; pede pizza 2 a 3 vezes por mês.</li>
   <li>Sexta à noite decide no celular, no Instagram e no iFood, em 5 minutos.</li>
   <li>Dor: pizza que chega fria, massa crua e marca que "parece todas iguais".</li>
   <li>Valoriza forno a lenha de verdade, borda bonita e entrega no horário.</li>
   <li>Confia em foto real, caixa caprichada e perfil bem cuidado.</li>
  </ol></div>
 <div style="background:var(--b);color:var(--f);border-radius:22px;padding:34px;position:relative;overflow:hidden">
  <div class="et">Conceito</div>
  <h3 class="t" style="font-size:74px;margin-top:16px">A boca<br><span style="color:var(--ch)">do forno</span></h3>
  <p style="font-size:16px;line-height:1.5;margin-top:18px;max-width:230px">Uma ideia só, ampliada em tudo (como as listras da PizzaExpress): 3 anéis de tijolo = ondas de calor.</p>
  <div style="position:absolute;right:-40px;bottom:-34px;width:190px;height:190px;opacity:.95">{S(C["f"] if False else C["farinha"],C["chama"],C["carvao"])}</div></div>
 <div style="background:#fff8ec;border:2px solid var(--c);border-radius:22px;padding:34px;display:flex;flex-direction:column">
  <div class="et" style="color:var(--b)">Posicionamento e tom</div>
  <p style="font-size:17px;line-height:1.5;margin-top:16px">Pizzaria de bairro com acabamento de marca grande. Fala direto, quente, sem gíria de delivery barato. Diferença para a esquina: <b>forno a lenha à vista</b> e a pizza que chega como saiu.</p>
  <div style="margin-top:auto;border-top:2px solid var(--c);padding-top:16px">
   <div class="et" style="opacity:.6">Assinatura</div>
   <div class="t" style="font-size:44px;margin-top:8px">Saiu do forno <span style="color:var(--b)">agora.</span></div></div></div>
</div></section>'''

# --- C · LOGO E VARIAÇÕES
h += f'''<section style="background:var(--f);padding:20px 64px 80px">
{sec_titulo('02','Logo e variações',sub='Símbolo: arco do forno com 3 anéis e chama viva. Proteção: 1 anel em volta. Mínimo: símbolo 24 px.')}
<div style="display:grid;grid-template-columns:1.35fr 1fr;grid-template-rows:330px 330px;gap:20px">
 <div style="background:#fff8ec;border-radius:22px;display:flex;align-items:center;justify-content:center;gap:30px;position:relative">
  <span class="et" style="position:absolute;top:24px;left:28px;opacity:.55">A · Horizontal</span>
  <div style="width:150px;height:150px">{S()}</div>
  <div><div class="t" style="font-size:132px;line-height:.82">Brasa Viva</div><div class="et" style="font-size:18px;color:var(--b);margin-top:14px;letter-spacing:.32em">Pizzaria · São Luís</div></div></div>
 <div style="grid-row:span 2;background:var(--b);border-radius:22px;display:flex;flex-direction:column;align-items:center;justify-content:center;color:var(--f);position:relative;overflow:hidden">
  <div style="position:absolute;inset:0;background:url({uri(PAD)});opacity:.13"></div>
  <span class="et" style="position:absolute;top:24px;left:28px;opacity:.75">B · Vertical</span>
  <div style="width:210px;height:210px;position:relative">{S(C["farinha"],C["chama"],C["carvao"])}</div>
  <div class="t" style="font-size:150px;text-align:center;margin-top:18px;position:relative">Brasa<br><span style="color:var(--c)">Viva</span></div>
  <div class="et" style="font-size:16px;margin-top:18px;letter-spacing:.32em;position:relative">Pizzaria · São Luís</div></div>
 <div style="display:grid;grid-template-columns:1fr 1fr;gap:20px">
  <div style="background:var(--c);border-radius:22px;display:flex;align-items:center;justify-content:center;position:relative">
   <span class="et" style="position:absolute;top:24px;left:28px;color:var(--f);opacity:.6">C · Carimbo (1 cor)</span>
   <div style="width:220px;height:220px;margin-top:22px">{carimbo(C["farinha"])}</div></div>
  <div style="background:var(--ch);border-radius:22px;position:relative;display:flex;align-items:center;justify-content:center;gap:18px">
   <span class="et" style="position:absolute;top:24px;left:28px;opacity:.7">D · Avatar</span>
   <div style="width:170px;height:170px;border-radius:50%;background:var(--b);padding:30px;margin-top:20px">{S(C["farinha"],C["chama"],C["carvao"])}</div>
   <div style="display:flex;flex-direction:column;gap:10px;align-items:center;margin-top:20px">
    <div style="width:64px;height:64px;border-radius:50%;background:var(--b);padding:11px">{S(C["farinha"],C["chama"],C["carvao"])}</div>
    <div style="width:36px;height:36px;border-radius:50%;background:var(--b);padding:6px">{S(C["farinha"],C["chama"],C["carvao"])}</div>
    <div style="width:24px;height:24px;border-radius:50%;background:var(--b);padding:4px">{S(C["farinha"],C["chama"],C["carvao"])}</div></div></div>
 </div></div></section>'''

# --- D · PALETA
sw = [('Farinha', C['farinha'], '243 231 211', 'Neutra · base', 45, 'var(--c)'),
      ('Brasa', C['brasa'], '226 67 29', 'Primária', 30, 'var(--f)'),
      ('Carvão', C['carvao'], '26 20 17', 'Secundária', 18, 'var(--f)'),
      ('Chama', C['chama'], '255 179 33', 'Destaque', 5, 'var(--c)'),
      ('Manjericão', C['manj'], '46 91 59', 'Detalhe', 2, 'var(--f)')]
bar = ''.join(f'<div style="flex:{p};background:{hx};color:{tc};padding:16px 18px;{"border:2px solid var(--c);" if n=="Farinha" else ""}" class="et">{p}%</div>' for n, hx, rgb, papel, p, tc in sw)
cards = ''.join(f'''<div style="background:{hx};color:{tc};border-radius:22px;padding:26px;height:250px;display:flex;flex-direction:column;{"border:2px solid var(--c);" if n=="Farinha" else ""}">
 <div class="et" style="opacity:.75">{papel}</div><div class="t" style="font-size:54px;margin-top:10px">{n}</div>
 <div style="margin-top:auto;font-size:15px;line-height:1.6"><b style="font-size:22px">{hx}</b><br>RGB {rgb}</div></div>''' for n, hx, rgb, papel, p, tc in sw)
h += f'''<section style="background:#fff8ec;padding:80px 64px">
{sec_titulo('03','Cores com proporção',sub='Farinha manda no fundo, Brasa grita, Carvão segura a foto. Chama só na chama e em 1 palavra por peça.')}
<div style="display:flex;height:64px;border-radius:14px;overflow:hidden;margin-bottom:20px">{bar}</div>
<div style="display:grid;grid-template-columns:repeat(5,1fr);gap:16px">{cards}</div></section>'''

# --- E · TIPOGRAFIA
h += f'''<section style="background:var(--c);color:var(--f);padding:80px 64px">
{sec_titulo('04','Duas letras',cor='var(--f)',sub='Bricolage Grotesque 800 condensada nos títulos (2ª linha em cor). DM Sans no texto. Google Fonts, grátis.')}
<div style="display:grid;grid-template-columns:1fr 1.2fr;gap:20px">
 <div style="background:var(--b);border-radius:22px;padding:34px;position:relative;overflow:hidden;height:470px">
  <div class="et">Título · Bricolage Grotesque 800 · largura 75</div>
  <div class="t" style="font-size:330px;line-height:.8;margin-top:20px;text-transform:none">Aa</div>
  <div class="t" style="font-size:40px;position:absolute;bottom:30px;left:34px;letter-spacing:.02em">ABCDEFGHIJKLMNOPQRSTUVWXYZ<br><span style="color:var(--ch)">0123456789 ÇÃÕÉ R$ & !?</span></div></div>
 <div style="display:grid;grid-template-rows:310px 140px;gap:20px;height:470px">
  <div style="background:var(--f);color:var(--c);border-radius:22px;padding:34px">
   <div class="et" style="color:var(--b)">Hierarquia na prática</div>
   <div class="t" style="font-size:86px;margin-top:14px">Borda alta,<br><span style="color:var(--b)">massa de 48 h.</span></div>
   <p style="font-size:17px;line-height:1.5;margin-top:16px;max-width:560px">Texto em DM Sans 400 a 17 px: claro no celular, sem competir com o título. Destaques em 700.</p></div>
  <div style="border:2px solid #3a2c24;border-radius:22px;padding:26px 30px;display:grid;grid-template-columns:repeat(3,1fr);gap:16px;align-items:center">
   <div><div style="font-size:46px;font-weight:400">Aa</div><div class="et" style="opacity:.6;margin-top:6px">DM Sans 400</div></div>
   <div><div style="font-size:46px;font-weight:500">Aa</div><div class="et" style="opacity:.6;margin-top:6px">DM Sans 500</div></div>
   <div><div style="font-size:46px;font-weight:700;color:var(--ch)">Aa</div><div class="et" style="opacity:.6;margin-top:6px">DM Sans 700</div></div></div>
 </div></div></section>'''

# --- F · GRAFISMOS
h += f'''<section style="background:var(--f);padding:80px 64px">
{sec_titulo('05','Grafismos do símbolo',sub='Nada de ícone solto: tudo nasce dos 3 anéis do arco. Assim a marca é reconhecida mesmo sem o logo.')}
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:16px;height:440px">
 <div style="border-radius:22px;background:url({uri(PAD)});background-size:120px;position:relative;overflow:hidden">
  <span class="et" style="position:absolute;left:0;right:0;bottom:0;background:var(--c);color:var(--f);padding:14px 18px">1 · Padrão de arcos</span></div>
 <div style="border-radius:22px;background:var(--c);position:relative;overflow:hidden">
  <div class="faixas" style="position:absolute;left:0;right:0;top:60px;height:132px"></div>
  <div class="t" style="position:absolute;left:24px;top:220px;font-size:64px;color:var(--f)">Quente<br><span style="color:var(--ch)">de verdade</span></div>
  <span class="et" style="position:absolute;left:0;right:0;bottom:0;background:var(--b);color:var(--f);padding:14px 18px">2 · Faixas de calor</span></div>
 <div style="border-radius:22px;background:var(--b);position:relative;overflow:hidden">
  <div class="arco" style="position:absolute;left:44px;right:44px;top:44px;bottom:72px;border:10px solid var(--f)"><img src="{P}calabresa.jpg"></div>
  <span class="et" style="position:absolute;left:0;right:0;bottom:0;background:var(--c);color:var(--f);padding:14px 18px">3 · Moldura-arco</span></div>
 <div style="border-radius:22px;background:var(--c);position:relative;overflow:hidden">
  <div style="position:absolute;left:-150px;top:30px;width:620px;height:620px">{S(C["brasa"],C["chama"],C["carvao"])}</div>
  <span class="et" style="position:absolute;left:0;right:0;bottom:0;background:var(--ch);color:var(--c);padding:14px 18px">4 · Arco gigante na borda</span></div>
</div>
<p style="font-size:11px;opacity:.55;margin-top:12px">Foto da moldura: Horacio Cambeiro, CC BY 4.0, Wikimedia Commons</p></section>'''

# --- G · USOS PROIBIDOS
def proib(conteudo, txt, bg='#fff8ec'):
    return (f'<div style="background:{bg};border-radius:18px;height:230px;position:relative;overflow:hidden;border:2px solid var(--c)">'
            f'<div style="position:absolute;inset:0 0 54px;display:flex;align-items:center;justify-content:center">{conteudo}</div>'
            f'<div style="position:absolute;top:12px;right:12px;width:38px;height:38px;border-radius:50%;background:var(--b);color:var(--f);display:flex;align-items:center;justify-content:center;font-weight:700;font-size:22px">✕</div>'
            f'<div style="position:absolute;left:0;right:0;bottom:0;background:var(--c);color:var(--f);padding:13px 16px;font-size:14px;font-weight:500">{txt}</div></div>')
pr = ''.join([
    proib(f'<div style="width:220px;height:110px">{S(extra="preserveAspectRatio=none style=width:100%;height:100%")}</div>', 'Esticar ou achatar o símbolo'),
    proib(f'<div style="width:130px;height:130px">{S("#2a6cd6","#7be05a","#c03ad6")}</div>', 'Trocar as cores ou a chama'),
    proib(f'<div style="width:130px;height:130px;filter:drop-shadow(6px 6px 0 #000) drop-shadow(0 0 2px #000)">{S()}</div>', 'Sombra, contorno ou efeito'),
    proib(f'<img src="{P}calabresa-porcoes.jpg" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover"><div style="width:120px;height:120px;position:relative">{S()}</div>', 'Logo sobre foto sem área limpa'),
    proib('<div style="font-family:Bricolage Grotesque;font-weight:200;font-size:42px">Brasa Viva</div>', 'Título em peso fino ou outra letra'),
    proib('<div style="font-size:84px;line-height:1">👨‍🍳🍕</div>', 'Chef de bigode, pizza cartum, xadrez'),
])
h += f'''<section style="background:var(--f);padding:0 64px 80px">
{sec_titulo('06','Usos proibidos',sub='Se a peça cair num destes, refaz antes de postar.')}
<div style="display:grid;grid-template-columns:repeat(6,1fr);gap:14px">{pr}</div></section>'''

# --- H · REFERÊNCIAS
refs = [('pin-962081539173882007.jpg', 'Decaf Girl · Misato Studio', 'Listras verticais na base da lata viram a base do copo e da caixa; letra gorda curta.'),
        ('pin-1144969905302172033.jpg', 'HOTWHIZ · Behance', 'Cor chapada saturada + manchete gigante + chama no rótulo: hero e post.'),
        (None, 'PizzaExpress · BrandOpus (Reino Unido)', 'Um ativo só ampliado em tudo: os 3 anéis viram faixa, padrão, moldura e recorte.')]
rc = ''.join(f'''<div style="display:grid;grid-template-columns:150px 1fr;gap:20px;align-items:center;background:#2a201b;border-radius:18px;padding:16px">
 {f'<div style="height:150px;border-radius:12px;overflow:hidden"><img src="{FAV}{f}" style="width:100%;height:100%;object-fit:cover"></div>' if f else '<div style="height:150px;border-radius:12px;background:repeating-linear-gradient(90deg,#1d3f8f 0 12px,#f3e7d3 12px 24px);display:flex;align-items:flex-end;padding:10px"><span class="et" style="background:var(--c);color:var(--f);padding:6px 8px;font-size:10px">Pesquisa 08/11 · nº 4</span></div>'}
 <div><div class="et" style="color:var(--ch)">Copiado de</div><div class="t" style="font-size:34px;margin-top:6px">{n}</div><p style="font-size:14px;line-height:1.45;margin-top:8px;opacity:.85">{d}</p></div></div>''' for f, n, d in refs)
h += f'''<section style="background:var(--c);color:var(--f);padding:80px 64px 56px">
{sec_titulo('07','3 referências combinadas',cor='var(--f)',sub='Composição copiada, nunca marca, desenho ou texto. Base: biblioteca de pizzaria e pesquisa de 08/11.')}
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:16px">{rc}</div>
<div style="display:flex;justify-content:space-between;align-items:center;margin-top:40px;padding-top:24px;border-top:1px solid #3a2c24;font-size:12px;opacity:.6">
 <span>Pizzaria Brasa Viva é uma marca fictícia, criada como exemplo demonstrativo pelo Designer gráfico da agência Lindson Almeida.</span>
 <span>Fotos: Wikimedia Commons (créditos em cada peça)</span></div></section>'''
h += '</body></html>'
open(os.path.join(D, 'prancha.html'), 'w').write(h)

# ================= APLICAÇÕES =================
a = HEAD
# tamanho fixo dos tiles para não sobrar espaço
caixa = f'''<div style="position:relative;width:640px;height:640px;background:var(--f);border-radius:10px;box-shadow:0 40px 60px rgba(0,0,0,.55),0 0 0 1px rgba(0,0,0,.25), inset 0 0 0 14px #eadbc2;overflow:hidden">
 <div style="position:absolute;inset:14px;border:2px dashed rgba(26,20,17,.18);border-radius:4px"></div>
 <div class="vfaixas" style="position:absolute;left:0;right:0;bottom:0;height:170px"></div>
 <div style="position:absolute;left:0;right:0;bottom:170px;height:14px;background:var(--b)"></div>
 <div style="position:absolute;left:50%;top:70px;transform:translateX(-50%);width:300px;height:300px">{carimbo(C["brasa"])}</div>
 <div class="t" style="position:absolute;left:0;right:0;top:396px;text-align:center;font-size:48px">Saiu do forno <span style="color:var(--b)">agora.</span></div>
 <div class="et" style="position:absolute;left:28px;top:30px;color:var(--b);font-size:11px">Cuidado · quente de verdade</div>
 <div class="et" style="position:absolute;right:28px;top:30px;font-size:11px">@pizzariabrasaviva</div>
 <div style="position:absolute;inset:0;background:linear-gradient(135deg,rgba(255,255,255,.18),transparent 40%,rgba(0,0,0,.08))"></div></div>'''

post = f'''<div style="position:relative;width:480px;height:600px;background:var(--b);overflow:hidden;border-radius:6px;box-shadow:0 30px 50px rgba(0,0,0,.35)">
 <div class="t" style="position:absolute;left:28px;top:30px;font-size:88px;color:var(--f)">Saiu do<br><span style="color:var(--ch)">forno</span><br>agora.</div>
 <div style="position:absolute;right:-110px;top:240px;width:420px;height:420px;opacity:.95">{S(C["carvao"],C["brasa"],C["brasa"]).replace(FL_OUT,"M0 0").replace(FL_IN,"M0 0")}</div>
 <div class="arco" style="position:absolute;right:20px;top:290px;width:236px;height:262px;border:8px solid var(--f)"><img src="{P}queijo-puxando.jpg" style="object-position:40% 50%"></div>
 <div style="position:absolute;left:28px;bottom:78px;width:170px;background:var(--c);color:var(--f);border-radius:12px;padding:12px 14px;font-size:12px;line-height:1.35"><b style="color:var(--ch)">Forno a lenha</b><br>Peça pelo link da bio ou no iFood.</div>
 <div class="faixas" style="position:absolute;left:0;right:0;bottom:0;height:44px;background:repeating-linear-gradient(180deg,var(--c) 0 8px,transparent 8px 13px),var(--b)"></div>
 <div style="position:absolute;left:28px;top:330px;display:flex;align-items:center;gap:8px;color:var(--f)"><div style="width:34px;height:34px">{S(C["farinha"],C["chama"],C["carvao"])}</div><div class="t" style="font-size:24px">Brasa Viva</div></div>
 <span style="position:absolute;right:28px;top:548px;color:var(--f);font-size:8px;opacity:.75">Foto: Foodie Moodie, CC0</span></div>'''

sacola = f'''<div style="position:relative;width:300px;height:400px;margin-top:60px">
 <div style="position:absolute;left:80px;top:-56px;width:140px;height:90px;border:10px solid #8b6a48;border-bottom:none;border-radius:70px 70px 0 0"></div>
 <div style="position:absolute;inset:0;background:linear-gradient(90deg,#c39a6c,#d4ac7d 22%,#caa073 60%,#b88e60);border-radius:4px;box-shadow:0 30px 40px rgba(0,0,0,.35)"></div>
 <div style="position:absolute;left:0;right:0;top:0;height:30px;background:rgba(0,0,0,.1)"></div>
 <div style="position:absolute;left:50%;top:60px;transform:translateX(-50%);width:110px;height:110px">{S(C["carvao"],C["brasa"],C["carvao"])}</div>
 <div class="t" style="position:absolute;left:0;right:0;top:186px;text-align:center;font-size:78px;color:var(--c)">Brasa<br><span style="color:var(--b)">Viva</span></div>
 <div class="et" style="position:absolute;left:0;right:0;bottom:24px;text-align:center;font-size:10px;color:var(--c)">Pizzaria · São Luís</div></div>'''

copo = f'''<div style="position:relative;width:240px;height:380px;margin-top:40px">
 <div style="position:absolute;left:-8px;right:-8px;top:0;height:30px;background:#2a201b;border-radius:10px 10px 4px 4px"></div>
 <div style="position:absolute;inset:26px 0 0;clip-path:polygon(0 0,100% 0,88% 100%,12% 100%);background:var(--b);overflow:hidden">
  <div class="vfaixas" style="position:absolute;left:0;right:0;bottom:0;height:130px;background:repeating-linear-gradient(90deg,var(--f) 0 12px,var(--b) 12px 22px)"></div>
  <div style="position:absolute;left:50%;top:40px;transform:translateX(-50%);width:90px;height:90px">{S(C["farinha"],C["chama"],C["carvao"])}</div>
  <div class="t" style="position:absolute;left:0;right:0;top:146px;text-align:center;font-size:46px;color:var(--f)">Brasa<br>Viva</div>
  <div style="position:absolute;inset:0;background:linear-gradient(90deg,rgba(0,0,0,.25),transparent 30%,rgba(255,255,255,.18) 55%,rgba(0,0,0,.2))"></div></div>
 <div style="position:absolute;left:20px;right:20px;bottom:-24px;height:24px;background:radial-gradient(rgba(0,0,0,.4),transparent 70%)"></div></div>'''

grid_fotos = ['pepperoni-inteira.jpg', None, 'fatia-puxando.jpg', None, 'caixa-viagem.jpg', 'calabresa-porcoes.jpg', 'queijo-borda.jpg', None, 'pepperoni-fatia.jpg']
alt = [f'<div style="background:var(--b);display:flex;align-items:center;justify-content:center"><div class="t" style="font-size:20px;color:var(--f);text-align:center">Saiu<br><span style="color:var(--ch)">agora</span></div></div>',
       f'<div style="background:url({uri(PAD)});background-size:40px"></div>',
       f'<div style="background:var(--c);display:flex;align-items:center;justify-content:center"><div style="width:56px;height:56px">{S()}</div></div>']
gi, k = '', 0
for f in grid_fotos:
    if f: gi += f'<div style="background:url({P}{f}) center/cover"></div>'
    else: gi += alt[k]; k += 1
perfil = f'''<div style="width:380px;background:#fff;border-radius:30px;padding:22px 18px;box-shadow:0 30px 50px rgba(0,0,0,.35);font-size:13px;color:#111">
 <div style="display:flex;align-items:center;gap:18px">
  <div style="width:92px;height:92px;border-radius:50%;padding:4px;background:conic-gradient(var(--ch),var(--b),var(--ch))"><div style="width:100%;height:100%;border-radius:50%;background:var(--b);border:3px solid #fff;padding:14px">{S(C["farinha"],C["chama"],C["carvao"])}</div></div>
  <div style="display:flex;gap:18px;text-align:center"><div><b style="font-size:16px">128</b><br>posts</div><div><b style="font-size:16px">—</b><br>seguidores</div><div><b style="font-size:16px">—</b><br>seguindo</div></div></div>
 <div style="margin-top:12px;line-height:1.45"><b>Pizzaria Brasa Viva</b><br>Forno a lenha à vista · São Luís - MA<br>Saiu do forno agora. Peça pelo link 👇</div>
 <div style="display:flex;gap:12px;margin:14px 0">{''.join(f'<div style="text-align:center;font-size:11px"><div style="width:52px;height:52px;border-radius:50%;border:2px solid #ddd;padding:3px"><div style="width:100%;height:100%;border-radius:50%;background:{b};padding:8px">{S(C["farinha"],C["chama"],C["carvao"]) if i%2==0 else S()}</div></div>{t}</div>' for i,(b,t) in enumerate([("var(--b)","Cardápio"),("var(--f)","Forno"),("var(--c)","Pedidos"),("var(--ch)","Bairros"),("var(--b)","Avaliações")]))}</div>
 <div style="display:grid;grid-template-columns:repeat(3,1fr);grid-auto-rows:112px;gap:2px;border-radius:6px;overflow:hidden">{gi}</div></div>'''

a += f'''<section style="background:var(--c);color:var(--f);padding:56px 64px 0;height:150px">
 <span class="demo" style="right:64px;top:56px;color:var(--ch)">Exemplo demonstrativo · marca fictícia</span>
 <div style="display:flex;align-items:center;gap:20px"><div style="width:64px;height:64px">{S()}</div>
 <h1 class="t" style="font-size:76px">Aplicações <span style="color:var(--b)">reais</span></h1></div></section>
<section style="display:grid;grid-template-columns:860px 1fr;height:840px">
 <div style="background:var(--c);position:relative;display:flex;align-items:center;justify-content:center;overflow:hidden">
  <div style="position:absolute;inset:0;background:url({uri(PAD2)});background-size:90px;opacity:.9"></div>
  <span class="et" style="position:absolute;left:40px;top:28px;color:var(--ch)">Caixa de pizza · vista de cima · a mídia mais vista</span>
  <div style="position:relative">{caixa}</div>
  <span style="position:absolute;left:40px;bottom:24px;font-size:12px;opacity:.6;max-width:720px">Carimbo no centro, faixa de 14 px (a mesma espessura dos anéis) e listras na base copiadas da lata Decaf Girl.</span></div>
 <div style="background:var(--ch);position:relative;display:flex;align-items:center;justify-content:center">
  <span class="et" style="position:absolute;left:36px;top:28px;color:var(--c)">Post 4:5 · feed</span>
  <div style="zoom:1.1">{post}</div>
  <span style="position:absolute;left:36px;bottom:24px;font-size:12px;color:var(--c);opacity:.75">Cor chapada + manchete gigante (HOTWHIZ) e foto na boca do forno.</span></div>
</section>
<section style="display:grid;grid-template-columns:1fr 1fr 1.25fr;height:700px">
 <div style="background:var(--b);position:relative;display:flex;align-items:center;justify-content:center;overflow:hidden">
  <div style="position:absolute;left:-120px;bottom:-140px;width:480px;height:480px;opacity:.18">{S(C["carvao"],C["carvao"],C["b"] if False else C["brasa"])}</div>
  <span class="et" style="position:absolute;left:32px;top:28px;color:var(--f)">Sacola kraft · 1 cor + Brasa</span>{sacola}</div>
 <div style="background:var(--f);position:relative;display:flex;align-items:center;justify-content:center;overflow:hidden">
  <div class="faixas" style="position:absolute;left:0;right:0;top:110px;height:66px;opacity:.95"></div>
  <span class="et" style="position:absolute;left:32px;top:28px;color:var(--b)">Copo · listras de calor</span>{copo}</div>
 <div style="background:#2a201b;position:relative;display:flex;align-items:center;justify-content:center;overflow:hidden">
  <span class="et" style="position:absolute;left:32px;top:28px;color:var(--ch)">Avatar e perfil do Instagram</span>
  <div style="margin-top:30px">{perfil}</div></div>
</section>
<section style="background:var(--c);color:var(--f);padding:22px 64px;display:flex;justify-content:space-between;font-size:11px;opacity:.75">
 <span>Marca fictícia (exemplo demonstrativo). Números do perfil omitidos de propósito.</span>
 <span>Fotos Wikimedia Commons: Andy Li CC0 · Foodie Moodie CC0 · BullDawg2021 CC BY 4.0 · PattayaPatrol CC BY-SA 4.0 · Snowjam CC BY-SA 4.0 · H. Cambeiro CC BY 4.0 · jeffreyw CC BY 2.0 · MVS9966 CC BY 3.0</span></section>
</body></html>'''
open(os.path.join(D, 'aplicacoes.html'), 'w').write(a)
print('ok')
