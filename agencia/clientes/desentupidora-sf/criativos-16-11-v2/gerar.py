# Criativos SF v2 (conta Pedro, 16/11/2026). Gera artes.html (feed 1080x1350 + story 1080x1920).
# Refs: A "Every drop. Handled." (EUA, Pinterest) = foto heroica escura + manchete condensada;
# B "Premium Plumbing" (Bangladesh, Dribbble) = ferramenta/técnico heroico com luz de borda;
# C Officina Poligonale (Itália, Dribbble CGI) = produto/água isolado em fundo escuro com luz dramática.
F='fotos/'
CSS='''
:root{--n0:#020a1f;--n1:#061a4a;--n2:#0a2a6e;--r:#1d5fd0;--c:#3fa9ff;--o:#ff8a00;--o2:#ff6a00;--w:#f4f8ff}
*{margin:0;box-sizing:border-box}body{background:#111;font-family:Montserrat;color:#fff}
section{position:relative;overflow:hidden;width:1080px;margin:20px;background:var(--n0);isolation:isolate}
.f{height:1350px}.s{height:1920px}
.L{position:absolute;inset:0}
.studio{background:radial-gradient(60% 45% at 60% 42%,#1d4fae 0%,#0a2a6e 38%,#041038 70%,#020a1f 100%)}
.grain{background:url(fotos/grao.png);mix-blend-mode:overlay;opacity:.22;z-index:50}
.vig{background:radial-gradient(120% 90% at 50% 45%,transparent 55%,rgba(0,4,16,.75) 100%);z-index:40}
.leak{background:radial-gradient(40% 30% at 100% 0%,rgba(255,138,0,.45),transparent 70%),radial-gradient(35% 25% at 0% 100%,rgba(63,169,255,.25),transparent 70%);mix-blend-mode:screen;z-index:41}
.mono{font-family:'IBM Plex Mono';font-weight:500;letter-spacing:.18em;text-transform:uppercase}
.h{font-weight:900;text-transform:uppercase;letter-spacing:-.035em;line-height:.84}
.o{color:var(--o);background:linear-gradient(180deg,#ffb347,#ff6a00);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;filter:drop-shadow(0 10px 30px rgba(255,106,0,.35))}
.brand{position:absolute;z-index:60;display:flex;align-items:center;gap:16px;font-weight:800;font-size:26px;letter-spacing:.02em}
.brand img{width:76px;height:76px;border-radius:50%;box-shadow:0 0 0 3px rgba(255,255,255,.9),0 10px 30px rgba(0,0,0,.5)}
.brand small{display:block;font:500 17px 'IBM Plex Mono';letter-spacing:.16em;opacity:.7;text-transform:uppercase}
.cta{position:absolute;z-index:60;display:flex;align-items:center;justify-content:space-between;gap:20px;
 background:linear-gradient(180deg,#ffa53a,#ff6a00);color:#1b0a00;border-radius:22px;padding:26px 34px;font-weight:900;font-size:36px;text-transform:uppercase;letter-spacing:-.01em;
 box-shadow:inset 0 2px 0 rgba(255,255,255,.55),inset 0 -6px 14px rgba(150,40,0,.35),0 24px 50px -10px rgba(255,106,0,.55),0 6px 14px rgba(0,0,0,.4)}
.cta b{font:600 26px 'IBM Plex Mono';letter-spacing:.04em;background:rgba(27,10,0,.12);padding:10px 16px;border-radius:12px}
.glass{background:linear-gradient(160deg,rgba(255,255,255,.16),rgba(255,255,255,.04));backdrop-filter:blur(18px) saturate(140%);border:1px solid rgba(255,255,255,.22);box-shadow:inset 0 1px 0 rgba(255,255,255,.3),0 30px 60px -20px rgba(0,0,0,.7)}
.tick{position:absolute;z-index:60;width:34px;height:34px;border-color:rgba(255,255,255,.55);border-style:solid;border-width:0}
.idx{position:absolute;z-index:60;font:500 18px 'IBM Plex Mono';letter-spacing:.2em;opacity:.65}
.legal{position:absolute;z-index:60;font:500 15px 'IBM Plex Mono';letter-spacing:.1em;opacity:.5;text-transform:uppercase}
'''
def frame(H):
    return f'''<div class="tick" style="left:36px;top:36px;border-left-width:2px;border-top-width:2px"></div>
<div class="tick" style="right:36px;top:36px;border-right-width:2px;border-top-width:2px"></div>
<div class="tick" style="left:36px;bottom:36px;border-left-width:2px;border-bottom-width:2px"></div>
<div class="tick" style="right:36px;bottom:36px;border-right-width:2px;border-bottom-width:2px"></div>
<div class="L leak"></div><div class="L vig"></div><div class="L grain"></div>'''
BR='<img src="fotos/logo.jpg"><div>Desentupidora SF<small>São Luís · MA</small></div>'
TEL='(98) 92010-5710'
def c1(s):  # Ref B: técnico heroico + manchete atrás dele (letra passando por trás) + sombra de contato
    H=1920 if s else 1350; top=330 if s else 190
    return f'''<section id="c1-{'story' if s else 'feed'}" class="{'s' if s else 'f'}">
<div class="L studio"></div>
<div class="L" style="background:repeating-linear-gradient(90deg,rgba(255,255,255,.025) 0 1px,transparent 1px 120px),repeating-linear-gradient(0deg,rgba(255,255,255,.025) 0 1px,transparent 1px 120px)"></div>
<div class="idx" style="right:80px;top:{150 if s else 98}px">01 / VASO SANITÁRIO</div>
<div class="h" style="position:absolute;left:62px;top:{top}px;font-size:{150 if s else 128}px;z-index:2">VASO</div>
<div class="h o" style="position:absolute;left:50px;top:{top+(130 if s else 110)}px;font-size:{176 if s else 168}px;z-index:2">ENTUPIU?</div>
<div style="position:absolute;left:50%;bottom:{560 if s else 300}px;width:760px;height:90px;transform:translateX(-30%);background:radial-gradient(closest-side,rgba(0,0,0,.85),transparent);filter:blur(8px);z-index:3"></div>
<img src="fotos/t1-final.png" style="position:absolute;right:-230px;bottom:{520 if s else 260}px;height:{1060 if s else 900}px;z-index:4;filter:drop-shadow(-30px 30px 40px rgba(0,0,0,.55))">
<div class="L" style="z-index:5;background:linear-gradient(180deg,transparent {62 if s else 58}%,rgba(2,10,31,.92) {78 if s else 80}%,#020a1f)"></div>
<div class="glass" style="position:absolute;z-index:60;left:70px;right:70px;bottom:{330 if s else 170}px;border-radius:26px;padding:30px 36px;font-size:30px;font-weight:600;line-height:1.3">
Desentupimento <span style="color:var(--o);font-weight:800">sem quebrar e sem tirar a louça</span>, na maioria dos casos. Técnico uniformizado na sua casa.</div>
<div class="cta" style="left:70px;right:70px;bottom:{200 if s else 60}px">Chamar no WhatsApp<b>{TEL}</b></div>
<div class="brand" style="left:70px;top:{120 if s else 70}px">{BR}</div>
{frame(H)}</section>'''
def c2(s):  # Ref A: foto heroica escura full bleed + manchete condensada com hierarquia
    H=1920 if s else 1350
    return f'''<section id="c2-{'story' if s else 'feed'}" class="{'s' if s else 'f'}">
<div class="L" style="background:url(fotos/t2-final.jpg) center {'40%' if s else '30%'}/cover;transform:scale(1.04)"></div>
<div class="L" style="background:linear-gradient(180deg,rgba(2,10,31,.85) 0%,rgba(2,10,31,.1) 30%,rgba(2,10,31,.0) 50%,rgba(2,10,31,.9) 75%,#020a1f 100%)"></div>
<div class="L" style="background:radial-gradient(30% 22% at 50% {'46%' if s else '42%'},rgba(63,169,255,.35),transparent 70%);mix-blend-mode:screen"></div>
<div class="brand" style="left:70px;top:{120 if s else 70}px">{BR}</div>
<div class="idx" style="right:80px;top:{150 if s else 98}px">02 / RALO · BOX</div>
<div style="position:absolute;left:70px;right:70px;bottom:{560 if s else 330}px;z-index:60">
 <div class="mono" style="font-size:22px;color:var(--c);margin-bottom:22px">— Água subindo pelo ralo?</div>
 <div class="h" style="font-size:{150 if s else 150}px;text-shadow:0 20px 60px rgba(0,0,0,.6)">RALO</div>
 <div class="h o" style="font-size:{150 if s else 150}px">VOLTANDO?</div>
</div>
<div style="position:absolute;left:70px;right:70px;bottom:{350 if s else 170}px;z-index:60;display:grid;grid-template-columns:repeat(3,1fr);gap:14px">
 {''.join(f'<div class="glass" style="border-radius:18px;padding:20px 22px;font-size:23px;font-weight:700;line-height:1.2"><span class="mono" style="display:block;font-size:15px;color:var(--o);margin-bottom:8px">0{i+1}</span>{t}</div>' for i,t in enumerate(['Sem quebrar o piso*','Orçamento grátis pela foto','Máquina de cabo rotativo']))}
</div>
<div class="cta" style="left:70px;right:70px;bottom:{200 if s else 60}px">Mandar foto do ralo<b>{TEL}</b></div>
<div class="legal" style="left:70px;bottom:{160 if s else 30}px;opacity:0">.</div>
{frame(H)}</section>'''
def c3(s):  # Ref C: corte do cano isolado, luz dramática, objeto heroico
    H=1920 if s else 1350; top=300 if s else 180
    return f'''<section id="c3-{'story' if s else 'feed'}" class="{'s' if s else 'f'}">
<div class="L studio" style="background:radial-gradient(55% 40% at 50% 62%,#1a4bb0 0%,#08245e 45%,#020a1f 100%)"></div>
<div class="brand" style="left:70px;top:{120 if s else 70}px">{BR}</div>
<div class="idx" style="right:80px;top:{150 if s else 98}px">03 / RESTAURANTES</div>
<div style="position:absolute;left:70px;top:{top}px;z-index:60">
 <div class="mono" style="font-size:22px;color:var(--c);margin-bottom:20px">— Restaurantes e condomínios</div>
 <div class="h" style="font-size:{124 if s else 112}px">CAIXA DE</div>
 <div class="h o" style="font-size:{124 if s else 112}px">GORDURA</div>
 <div class="h" style="font-size:{124 if s else 112}px">CHEIA?</div>
</div>
<div style="position:absolute;left:-40px;right:-40px;top:{820 if s else 600}px;height:{620 if s else 520}px;z-index:5;background:url(fotos/t3-final.jpg) center/cover;-webkit-mask:radial-gradient(60% 60% at 50% 50%,#000 55%,transparent 100%);mask:radial-gradient(60% 60% at 50% 50%,#000 55%,transparent 100%)"></div>
<div class="glass" style="position:absolute;z-index:60;right:70px;top:{top+40}px;width:300px;border-radius:22px;padding:24px 26px;font-size:22px;font-weight:600;line-height:1.3">
<span class="mono" style="font-size:15px;color:var(--o);display:block;margin-bottom:10px">● Limpeza</span>Gordura retirada e destino correto do resíduo.</div>
<div style="position:absolute;left:70px;right:70px;bottom:{330 if s else 165}px;z-index:60;font-size:28px;font-weight:600;line-height:1.35;opacity:.92">Desentupimento e limpeza com técnicos uniformizados. <span style="color:var(--o)">Agendamento conforme a agenda.</span></div>
<div class="cta" style="left:70px;right:70px;bottom:{200 if s else 60}px">Pedir orçamento grátis<b>{TEL}</b></div>
{frame(H)}</section>'''
def c4(s):  # Ref A+C: celular 3D com conversa real, luz de borda e sombra projetada
    H=1920 if s else 1350; ph=900 if s else 860
    msgs=[('in','Oi! A pia da cozinha não desce 😩 Segue a foto'),('img',''),('out','Recebemos! Já te passo o orçamento grátis e o horário disponível 👍'),('in','Perfeito, obrigada!')]
    chat=''.join(
      '<div style="align-self:flex-start;width:62%%;height:%dpx;border-radius:16px;background:url(fotos/t5.webp) center/cover;box-shadow:0 4px 10px rgba(0,0,0,.2)"></div>'%(260 if s else 190) if k=='img' else
      f'<div style="align-self:{"flex-end" if k=="in" else "flex-start"};max-width:80%;background:{"#d9fdd3" if k=="in" else "#fff"};color:#111;border-radius:16px;padding:14px 18px;font:500 {24 if s else 21}px Inter,sans-serif;line-height:1.3;box-shadow:0 2px 4px rgba(0,0,0,.12)">{t}</div>' for k,t in msgs)
    return f'''<section id="c4-{'story' if s else 'feed'}" class="{'s' if s else 'f'}">
<div class="L studio" style="background:radial-gradient(50% 40% at 68% 55%,#2a66d8 0%,#0a2a6e 40%,#020a1f 100%)"></div>
<div class="L" style="background:radial-gradient(22% 18% at 70% 60%,rgba(255,138,0,.35),transparent 70%);mix-blend-mode:screen"></div>
<div class="brand" style="left:70px;top:{120 if s else 70}px">{BR}</div>
<div class="idx" style="left:80px;top:{290 if s else 200}px">04 / ORÇAMENTO</div>
<div style="position:absolute;left:70px;top:{340 if s else 245}px;z-index:60">
 <div class="h" style="font-size:{150 if s else 120}px">MANDA</div><div class="h" style="font-size:{150 if s else 120}px">A <span class="o">FOTO.</span></div>
 <div style="margin-top:28px;font-size:{32 if s else 27}px;font-weight:600;line-height:1.3;width:{900 if s else 430}px;opacity:.92">A gente responde com o <span style="color:var(--o)">orçamento grátis</span> no WhatsApp.</div>
</div>
<div style="position:absolute;right:{110 if s else 60}px;top:{690 if s else 400}px;perspective:2200px;z-index:10">
 <div style="position:absolute;left:40px;right:-40px;bottom:-70px;height:80px;background:radial-gradient(closest-side,rgba(0,0,0,.8),transparent);filter:blur(10px)"></div>
 <div style="width:{ph*0.49:.0f}px;height:{ph}px;border-radius:64px;padding:16px;background:linear-gradient(135deg,#3a3f4a,#0d0f14 40%,#2b2f38);transform:rotateY(-18deg) rotateX(6deg) rotateZ(-3deg);box-shadow:inset 0 0 0 2px rgba(255,255,255,.18),-10px 0 0 -4px rgba(255,138,0,.55),40px 60px 90px -20px rgba(0,0,0,.85),0 0 120px rgba(63,169,255,.25)">
  <div style="width:100%;height:100%;border-radius:50px;overflow:hidden;background:#efe7dd;display:flex;flex-direction:column;position:relative">
   <div style="background:#075e54;padding:{60 if s else 46}px 20px 18px;display:flex;align-items:center;gap:12px;font:600 {24 if s else 20}px Inter,sans-serif"><img src="fotos/logo.jpg" style="width:46px;height:46px;border-radius:50%">Desentupidora SF</div>
   <div style="flex:1;padding:18px 16px;display:flex;flex-direction:column;gap:12px;background:linear-gradient(#efe7dd,#e6dccf)">{chat}</div>
   <div class="L" style="background:linear-gradient(115deg,rgba(255,255,255,.28) 0%,transparent 28%);pointer-events:none"></div>
  </div></div></div>
<div class="cta" style="left:70px;right:70px;bottom:{200 if s else 60}px">Mandar no WhatsApp<b>{TEL}</b></div>
<div class="legal" style="left:70px;bottom:{160 if s else 24}px;opacity:.45">Imagens geradas por IA · ilustrativo</div>
{frame(H)}</section>'''
html=f'''<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@600;700;800;900&family=IBM+Plex+Mono:wght@500;600&family=Inter:wght@500;600&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>{''.join(f(s) for f in (c1,c2,c3,c4) for s in (0,1))}</body></html>'''
open('artes.html','w').write(html)
