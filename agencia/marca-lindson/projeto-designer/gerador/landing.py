import sys,html,os
sys.path.insert(0,'.'); from conteudo import *
e=html.escape
cards="".join(f'<a class=case href="{SITE}"><img src="../img/id/{c["id"]}.jpg" alt="{e(c["titulo"])}" loading=lazy><b>{e(c["titulo"].split(" · ")[0])}</b><span>{e(c["conceito"].split(".")[0])}.</span></a>' for c in CASES)
pk="".join(f'<div class=pk><h3>{e(p["nome"])}</h3><p class=para>{e(p["para"])}</p><ul>'+"".join(f"<li>{e(i)}</li>" for i in p["itens"])+f'</ul><p class=prazo>Prazo: {e(p["prazo"])}</p><a class=btn href="{WA}%20Pacote%20{p["nome"]}.">Pedir orçamento</a></div>' for p in PACOTES)
et="".join(f'<li><b>{i+1:02d} · {e(a)}</b><span>{e(b)}</span></li>' for i,(a,b) in enumerate(ETAPAS))
H=f'''<!doctype html><html lang=pt-BR><head><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1">
<title>Identidade Visual · {e(STUDIO)}</title><meta name=description content="Identidade visual, brand book e site para negócios. Designer em São Luís (MA). Orçamento pelo WhatsApp.">
<meta property=og:image content="https://lindsonalmeida.pages.dev/site/img/id/real-time.jpg">
<link href="https://fonts.googleapis.com/css2?family=Anton&family=Manrope:wght@400;600;800&display=swap" rel=stylesheet>
<style>:root{{--k:#0A0A0A;--y:#F5C518}}*{{margin:0;padding:0;box-sizing:border-box}}body{{background:var(--k);color:#fff;font:400 17px/1.6 Manrope,sans-serif}}
.w{{max-width:1180px;margin:auto;padding:0 20px}}h1,h2,h3{{font-family:Anton;text-transform:uppercase;line-height:.95;font-weight:400}}
nav{{display:flex;justify-content:space-between;align-items:center;padding:22px 0;font-weight:800;letter-spacing:2px;font-size:13px;text-transform:uppercase}}
.btn{{display:inline-block;background:var(--y);color:var(--k);font-weight:800;padding:15px 26px;border-radius:999px;text-decoration:none}}
.hero{{padding:70px 0 90px}}.hero h1{{font-size:clamp(54px,10vw,132px)}}.hero h1 em{{color:var(--y);font-style:normal}}.hero p{{max-width:620px;font-size:20px;opacity:.85;margin:26px 0 34px}}
.tag{{color:var(--y);font-weight:800;letter-spacing:3px;font-size:13px;text-transform:uppercase;margin-bottom:14px}}section{{padding:80px 0;border-top:1px solid #222}}h2{{font-size:clamp(40px,6vw,76px);margin-bottom:36px}}
.cases{{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:22px}}.case{{color:#fff;text-decoration:none}}.case img{{width:100%;aspect-ratio:808/632;object-fit:cover;border-radius:10px;display:block;transition:.3s}}.case:hover img{{transform:translateY(-4px)}}.case b{{display:block;margin-top:12px;font-size:19px}}.case span{{opacity:.7;font-size:15px}}
.dor{{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:22px}}.dor div{{border-left:3px solid var(--y);padding-left:18px}}
ol.et{{list-style:none;display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:26px}}ol.et b{{display:block;font-size:19px;color:var(--y)}}
.pks{{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:22px}}.pk{{background:#141414;border:1px solid #262626;border-radius:14px;padding:30px;display:flex;flex-direction:column}}.pk:nth-child(3){{border-color:var(--y)}}.pk h3{{font-size:46px;color:var(--y)}}.pk ul{{margin:16px 0 18px 18px;flex:1}}.pk .para{{opacity:.8}}.pk .prazo{{font-weight:800;margin-bottom:18px}}
.fim{{background:var(--y);color:var(--k);text-align:center}}.fim .btn{{background:var(--k);color:#fff}}footer{{padding:30px 0;opacity:.6;font-size:14px}}</style></head><body>
<div class=w><nav><span>{e(STUDIO)}</span><a class=btn href="{WA}">Orçamento</a></nav>
<header class=hero><div class=tag>Identidade visual · brand book · site</div><h1>Sua marca do<br><em>tamanho do seu</em><br>negócio.</h1>
<p>Eu crio a identidade visual completa do seu negócio: logo, cores, letras, brand book e a marca aplicada no Instagram e no site. Designer em São Luís (MA), atendo todo o Brasil.</p><a class=btn href="{WA}">Pedir orçamento no WhatsApp</a></header></div>
<section><div class=w><div class=tag>Você se reconhece?</div><h2>O cliente julga<br>na primeira olhada</h2><div class=dor>
<div><b>Cada post sai de um jeito</b><br>e ninguém lembra da sua marca.</div><div><b>O logo foi feito às pressas</b><br>e hoje parece menor que o negócio.</div><div><b>Você quer cobrar mais</b><br>mas a marca não passa esse valor.</div></div></div></section>
<section><div class=w><div class=tag>Cases do estúdio</div><h2>Marcas que já<br>saíram daqui</h2><div class=cases>{cards}</div></div></section>
<section><div class=w><div class=tag>Como funciona</div><h2>6 etapas, prazo certo</h2><ol class=et>{et}</ol></div></section>
<section id=pacotes><div class=w><div class=tag>Pacotes</div><h2>Escolha o caminho</h2><div class=pks>{pk}</div>
<p style="margin-top:26px;opacity:.7">O investimento é passado no WhatsApp, depois de entender o seu negócio. <a href="briefing.html" style="color:var(--y)">Adiantar o briefing →</a></p></div></section>
<section class=fim><div class=w><h2>Vamos criar a sua marca?</h2><a class=btn href="{WA}">Chamar no WhatsApp</a></div></section>
<div class=w><footer>{e(STUDIO)} · São Luís, MA · <a href="{SITE}" style="color:inherit">portfólio</a></footer></div></body></html>'''
open(sys.argv[1]+'/index.html','w').write(H)
fs="".join(f'<fieldset><legend>{e(t)}</legend>'+"".join(f'<label>{e(q)}<textarea name="{e(q)}" rows=2></textarea></label>' for q in qs)+'</fieldset>' for t,qs in BRIEFING)
B=f'''<!doctype html><html lang=pt-BR><head><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1"><title>Briefing · {e(STUDIO)}</title>
<link href="https://fonts.googleapis.com/css2?family=Anton&family=Manrope:wght@400;600;800&display=swap" rel=stylesheet>
<style>*{{box-sizing:border-box}}body{{margin:0;background:#0A0A0A;color:#fff;font:400 16px/1.5 Manrope,sans-serif}}.w{{max-width:760px;margin:auto;padding:40px 16px}}h1{{font:400 clamp(44px,9vw,80px)/.95 Anton;text-transform:uppercase}}h1 em{{color:#F5C518;font-style:normal}}
fieldset{{border:1px solid #2a2a2a;border-radius:12px;margin:22px 0;padding:20px}}legend{{color:#F5C518;font-weight:800;letter-spacing:2px;text-transform:uppercase;font-size:13px;padding:0 8px}}label{{display:block;font-weight:600;margin:12px 0}}textarea{{width:100%;margin-top:6px;background:#151515;color:#fff;border:1px solid #333;border-radius:8px;padding:10px;font:inherit}}
button{{background:#F5C518;color:#0A0A0A;border:0;border-radius:999px;padding:16px 28px;font:800 17px Manrope;cursor:pointer;width:100%}}</style></head><body><div class=w>
<p style="color:#F5C518;font-weight:800;letter-spacing:3px;font-size:13px">{e(STUDIO.upper())}</p><h1>Briefing de<br><em>identidade visual</em></h1><p style="opacity:.8">Responda o que souber. No fim, o botão abre o WhatsApp com tudo escrito.</p>
<form id=f>{fs}<button type=submit>Enviar pelo WhatsApp</button></form></div>
<script>document.getElementById('f').onsubmit=function(ev){{ev.preventDefault();var t='Briefing de identidade visual\\n';document.querySelectorAll('textarea').forEach(function(a){{if(a.value.trim())t+='\\n*'+a.name+'*\\n'+a.value.trim()+'\\n'}});location.href='https://wa.me/5598985621808?text='+encodeURIComponent(t)}}</script></body></html>'''
open(sys.argv[1]+'/briefing.html','w').write(B)
