# WF Celulares · motion-01: 5 criativos em motion graphics 1080×1920, ~14 s (Designer gráfico · conta Leandro · 10/11/2026)
# Estilos lidos em dados/agencia/referencias/edit-ia-pro (nº 5 Motion explicativo, nº 2 Gancho na tela) e motion-animacao-vfx:
# #41 tipografia cinética · #25 2.5D/parallax (giro em Y do aparelho + reflexo no chão) · #163 zoom · #166 corte na batida ·
# #169 flash de luz · #152 light leak · #35 grão · shake no impacto do preço · motion blur (tmix no ffmpeg).
# Composição copiada de: apple.com/iphone Pro (produto central com rim light e reflexo), keynote (preço entrando grande e fino),
# vidro fosco das telas do iOS (selos). Imagens: Apple Newsroom, modelo CERTO de cada vídeo (fontes no README).
# Gera v<N>.html; render.js captura os quadros; montar.py junta vídeo, voz D, SFX e trilha.
import os, sys, json
D = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(D, '..', 'identidade'))
import gerar3 as g
TG = g.TIT_GRAD
V = json.load(open(os.path.join(D, 'produtos.json')))
CSS = f'''*{{margin:0;padding:0;box-sizing:border-box}}body{{width:1080px;height:1920px;background:#000;overflow:hidden;font-family:Inter}}
#cena{{position:absolute;inset:0;transform-origin:50% 50%}}
.grad{{background:{TG};-webkit-background-clip:text;color:transparent}}
.vidro{{position:absolute;background:rgba(255,255,255,.09);backdrop-filter:blur(18px);border:1px solid rgba(255,255,255,.18);border-radius:44px;padding:20px 34px;font:300 34px Inter;color:#f5f5f7;white-space:nowrap}}
.pal{{display:inline-block;margin-right:22px}}'''
for p in V:
    fit = 'contain'
    selos = ''.join(f'<div class="vidro sl" style="left:{70 + i*0}px;top:{820 + i*110}px">{s}</div>' for i, s in enumerate(p['selos']))
    nome = ''.join(f'<span class="pal w">{w}</span>' for w in p['nome'].split())
    html = f'''<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Inter:wght@200;300;400&display=swap" rel="stylesheet"><style>{CSS}</style></head><body>
<div id="cena">
 <div id="bg" style="position:absolute;inset:0;background:radial-gradient(ellipse 70% 45% at 50% 42%,{p['tom']},#000 72%)"></div>
 <div id="rim" style="position:absolute;left:50%;top:40%;width:900px;height:1300px;margin:-650px 0 0 -450px;border-radius:50%;background:radial-gradient(closest-side,rgba(255,255,255,.22),transparent);filter:blur(30px)"></div>
 <div id="prod" style="position:absolute;left:{p['x']}px;top:{p['y']}px;width:{p['w']}px;height:{p['h']}px;perspective:1600px">
  <img id="ph" src="img/{p['img']}" style="width:100%;height:100%;object-fit:{fit};object-position:{p.get('pos','50% 50%')};mix-blend-mode:lighten;transform-style:preserve-3d">
  <img id="rf" src="img/{p['img']}" style="position:absolute;left:0;top:100%;width:100%;height:100%;object-fit:{fit};object-position:{p.get('pos','50% 50%')};transform:scaleY(-1);opacity:.18;-webkit-mask-image:linear-gradient(to top,#000,transparent 28%);mix-blend-mode:lighten"></div>
 <div id="sheen" style="position:absolute;top:0;bottom:0;width:260px;background:linear-gradient(90deg,transparent,rgba(255,255,255,.16),transparent);filter:blur(20px);transform:skewX(-14deg)"></div>
 <div id="eyebrow" style="position:absolute;left:70px;top:150px;font:300 34px Inter;color:#a1a1a6;letter-spacing:.02em">{p['eyebrow']}</div>
 <div id="nome" style="position:absolute;left:70px;right:40px;top:200px;font:200 128px/1.02 Inter;letter-spacing:-.05em;color:#f5f5f7">{nome}</div>
 <div id="cap" style="position:absolute;left:70px;top:{200 + 135*p['linhas']}px;font:300 54px Inter;letter-spacing:-.02em" class="grad">{p['cap']}</div>
 <div id="preco" style="position:absolute;left:0;right:0;top:1470px;text-align:right;padding-right:70px;font:200 168px/1 Inter;letter-spacing:-.05em;color:#f5f5f7"><span style="font-size:52px;font-weight:300;vertical-align:top;color:#c7c9cc;margin-right:12px">R$</span>{p['preco'].split(',')[0]}<span style="font-size:60px">,{p['preco'].split(',')[1]}</span></div>
 <div id="era" style="position:absolute;right:70px;top:1660px;font:300 30px Inter;color:#8e8e93">{p.get('era','')}</div>
 {selos}
 <div id="fim" style="position:absolute;inset:0;background:radial-gradient(ellipse 80% 55% at 50% 40%,#1e1e22,#000 72%);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:60px">
  <div style="width:420px">{g.logo_svg()}</div>
  <div style="text-align:center;font:200 64px/1.15 Inter;letter-spacing:-.03em;color:#f5f5f7">Chama no WhatsApp<br><span class="grad">(98) 98827-1882</span></div>
  <div style="font:300 34px Inter;color:#a1a1a6;letter-spacing:.08em">SÃO LUÍS · MA</div></div>
 <div id="leak" style="position:absolute;inset:-200px;background:radial-gradient(circle at 15% 10%,rgba(255,150,70,.5),transparent 40%),radial-gradient(circle at 90% 80%,rgba(80,130,255,.35),transparent 45%);mix-blend-mode:screen"></div>
 <div style="position:absolute;right:30px;bottom:28px;font:300 18px Inter;color:#6e6e73">Imagem ilustrativa · Apple Newsroom</div>
</div><div id="flash" style="position:absolute;inset:0;background:#fff;opacity:0"></div>
<script>
const E=(a,b,t)=>Math.min(1,Math.max(0,(t-a)/(b-a)));const ease=x=>1-Math.pow(1-x,3);const $=id=>document.getElementById(id);
window.render=function(t){{
 const r=ease(E(.4,3.2,t));$('prod').style.opacity=r;
 const giro=-26*(1-r)+4*Math.sin(t*.6);$('ph').style.transform=`rotateY(${{giro}}deg) scale(${{1.18-.18*r+.03*E(3,10.5,t)}})`;
 $('rf').style.transform=`scaleY(-1) rotateY(${{-giro}}deg)`;
 $('rim').style.opacity=.3+.7*r;$('sheen').style.left=(-300+1700*E(1.2,3.4,t))+'px';
 $('eyebrow').style.opacity=E(1.2,1.8,t);
 document.querySelectorAll('.w').forEach((w,i)=>{{const k=ease(E(1.6+i*.28,2.2+i*.28,t));w.style.opacity=k;w.style.transform=`translateY(${{60*(1-k)}}px)`;w.style.filter=`blur(${{12*(1-k)}}px)`}});
 const c=ease(E(3.6,4.3,t));$('cap').style.opacity=c;$('cap').style.transform=`translateX(${{-80*(1-c)}}px)`;
 const pr=ease(E(5.6,6.1,t));$('preco').style.opacity=pr;$('preco').style.transform=`scale(${{1.35-.35*pr}})`;$('preco').style.filter=`blur(${{18*(1-pr)}}px)`;$('era').style.opacity=E(6.4,7,t);
 const sh=t>6.05&&t<6.45?(1-(t-6.05)/.4):0;$('cena').style.transform=`translate(${{14*sh*Math.sin(t*90)}}px,${{10*sh*Math.cos(t*70)}}px) scale(${{1+.02*E(0,11,t)}})`;
 document.querySelectorAll('.sl').forEach((s,i)=>{{const k=ease(E(7.4+i*.45,7.9+i*.45,t));s.style.opacity=k;s.style.transform=`translateX(${{-120*(1-k)}}px)`}});
 const f=ease(E(10.6,11.1,t));$('fim').style.opacity=f;$('fim').style.transform=`scale(${{1.1-.1*f}})`;
 $('leak').style.opacity=.25+.2*Math.sin(t*.9);$('leak').style.transform=`translate(${{40*Math.sin(t*.4)}}px,${{30*Math.cos(t*.5)}}px)`;
 const fl=Math.max(t>.3&&t<.7?1-Math.abs(t-.45)/.25:0,t>10.45&&t<10.95?1-Math.abs(t-10.6)/.35:0,t>5.95&&t<6.25?.5*(1-Math.abs(t-6.05)/.2):0);$('flash').style.opacity=Math.max(0,fl);
}};render(0);</script></body></html>'''
    open(os.path.join(D, f"v{p['n']}.html"), 'w').write(html)
print(len(V), 'vídeos')
