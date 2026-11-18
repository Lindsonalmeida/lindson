# Kit YouTube Barzakh (conta Zuleide, 18/11/2026). Padrão aprovado: placa monolito ouro escovado, concreto, brilho Lápis
# + direção "clean e rico": foto grande do Lindson (rosto livre), Oswald caixa alta (masculina), Fraunces só na assinatura.
# Composições copiadas de: The Futur (rosto grande + palavras condensadas), Satori Graphics (objeto gigante + palavra),
# Visualize Value (fundo limpo, equação tipográfica). Ver ../TEMPLATE.md.
# Uso: python3 gerar.py && NODE_PATH=$(npm root -g) node render.js && python3 previa.py
import os, re
B = os.path.dirname(os.path.abspath(__file__))
F = '/home/user/centrallindsonalmeida/painel/fotos-lindson/escolhidas-2026-11-16/'
SV = open('/home/user/lindson/agencia/marca-lindson/projeto-designer/v3/marca/logos/svg/barzakh-monolito-bronze.svg').read()

def mono(w, gid):
    s = SV.replace('#B4935A', 'url(#%s)' % gid)
    s = s.replace('<svg ', '<svg style="width:%dpx;height:%dpx;display:block" ' % (w, w), 1)
    d = ('<defs><linearGradient id="%s" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#F3DDA0"/>'
         '<stop offset=".35" stop-color="#C9A45E"/><stop offset=".6" stop-color="#8A6A33"/>'
         '<stop offset=".8" stop-color="#E6C77F"/><stop offset="1" stop-color="#9C7A3E"/></linearGradient></defs>') % gid
    i = s.index('>') + 1
    return s[:i] + d + s[i:]

def im(n): return 'file://' + F + 'lindson-%s.jpg' % n

CSS = open(os.path.join(B, 'estilo.css')).read()
P = []
# BANNER 2560x1440 · área segura 1546x423 (x507-2053, y508-931)
P.append(f'''<section class="f conc grain" id="banner" style="width:2560px;height:1440px">
<div class="ph" style="right:-120px;top:0;width:1250px;height:1440px;background-image:url({im('05')});background-position:50% 18%;-webkit-mask-image:linear-gradient(90deg,transparent,#000 38%)"></div>
<div style="position:absolute;inset:0;background:linear-gradient(90deg,rgba(30,29,28,.75),rgba(30,29,28,.55) 45%,transparent 70%)"></div>
<div class="arch" style="left:507px;top:380px;width:560px;height:700px"></div>
<div class="lap" style="left:560px;top:520px;width:460px;height:380px"></div>
<div style="position:absolute;left:607px;top:470px">{mono(360,'g1')}</div>
<div class="F gold" style="position:absolute;left:507px;width:560px;top:850px;text-align:center;font-size:58px;font-weight:600">BARZAKH</div>
<div class="M" style="position:absolute;left:507px;width:560px;top:930px;text-align:center;color:#b9b2a3;font-size:17px">um estúdio Al Kántara</div>
<div style="position:absolute;left:1120px;top:520px;width:600px">
 <div class="M" style="color:#e9d9b0;font-size:20px">Canal oficial · Marca e design</div>
 <div class="O" style="color:#fff;font-size:100px;margin-top:20px;white-space:nowrap;text-shadow:0 6px 30px rgba(0,0,0,.35)">A PASSAGEM<br><span class="gold">DA SUA MARCA</span></div>
 <div style="color:#f1ece2;font-size:28px;margin-top:22px;font-weight:500">Identidade visual e branding por dentro, com o fundador Lindson Almeida.</div></div>
</section>''')
# AVATAR 800x800: monolito ouro na placa grafite com Lápis
P.append(f'''<section class="f grain" id="avatar" style="width:800px;height:800px;background:radial-gradient(circle at 50% 45%,#2a2c33,#121316)">
<div class="lap" style="left:170px;top:200px;width:460px;height:400px"></div>
<div style="position:absolute;left:130px;top:90px">{mono(540,'g2')}</div>
<div class="F gold" style="position:absolute;width:800px;top:600px;text-align:center;font-size:56px;font-weight:600;padding-left:.35em">BARZAKH</div></section>''')

def T(i, b): return f'<section class="f grain" id="thumb-0{i}" style="width:1280px;height:720px">{b}</section>'
# T1 Raio-X de marca · The Futur
P.append(T(1, f'''<div class="conc" style="position:absolute;inset:0;filter:brightness(1.6) sepia(.25)"></div>
<div class="ph" style="right:-40px;top:0;width:700px;height:720px;background-image:url({im('04')});background-position:50% 14%;background-size:118%;-webkit-mask-image:linear-gradient(90deg,transparent,#000 22%)"></div>
<div class="M" style="position:absolute;left:60px;top:70px;color:#2B3A8F;font-size:22px">Raio-X de marca</div>
<div class="O" style="position:absolute;left:56px;top:120px;font-size:150px;color:#17181b">SUA MARCA<br>PARECE</div>
<div class="O" style="position:absolute;left:56px;top:400px;font-size:190px;background:#17181b;padding:0 18px"><span class="gold">BARATA?</span></div>
<div style="position:absolute;left:62px;bottom:26px;opacity:.9">{mono(70,'g3')}</div>'''))
# T2 Caso aberto · Satori
P.append(T(2, f'''<div style="position:absolute;inset:0;background:radial-gradient(circle at 30% 50%,#34478f,#1b1f33 55%,#121316)"></div>
<div class="ph" style="right:0;top:0;width:560px;height:720px;background-image:url({im('11')});background-position:50% 12%;-webkit-mask-image:linear-gradient(90deg,transparent,#000 30%)"></div>
<div style="position:absolute;left:0;right:0;bottom:0;height:300px;background:linear-gradient(transparent,rgba(12,13,20,.85))"></div>
<div style="position:absolute;left:40px;top:20px;filter:drop-shadow(0 20px 40px rgba(0,0,0,.6))">{mono(440,'g4')}</div>
<div class="M" style="position:absolute;left:70px;top:470px;color:#d9c79b;font-size:22px">Caso aberto · nº 01</div>
<div class="O" style="position:absolute;left:66px;top:520px;font-size:104px;color:#fff;text-shadow:0 4px 20px rgba(0,0,0,.6)">DO NOME AO <span class="gold">SÍMBOLO</span></div>'''))
# T3 Fundamentos · Visualize Value
P.append(T(3, f'''<div style="position:absolute;inset:0;background:#EEEAE2"></div>
<div class="ph" style="left:70px;top:70px;width:470px;height:650px;border-radius:300px 300px 0 0;background-image:url({im('10')});background-position:48% 30%;background-size:170%;box-shadow:0 30px 60px rgba(0,0,0,.25)"></div>
<div class="M" style="position:absolute;left:610px;top:110px;color:#2B3A8F;font-size:22px">Fundamentos de marca</div>
<div class="O" style="position:absolute;left:604px;top:160px;font-size:200px;color:#17181b">LOGO</div>
<div class="O" style="position:absolute;left:604px;top:345px;font-size:120px;color:#a59c86">NÃO É</div>
<div class="O" style="position:absolute;left:604px;top:470px;font-size:190px;background:#17181b;padding:0 16px"><span class="gold">MARCA</span></div>'''))
open(os.path.join(B, 'pecas.html'), 'w').write('<!doctype html><html><head><meta charset="utf-8"><style>' + CSS + '</style></head><body>' + ''.join(P) + '</body></html>')
