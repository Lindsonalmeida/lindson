# WF Celulares · motion-02: criativos de alta retenção (gancho 0-3 s) · conta Leandro · 10/11/2026
# Pedido: "alta conversão, retenção, gatilho para 3 segundos no mínimo, prenda a atenção logo no início".
# Regras aplicadas (edit-ia-pro: nº 2 Gancho na tela, nº 10 Palavra de impacto, nº 1 Legenda palavra por palavra;
# reels-sem-gravar; motion #41, #163, #166, #169, #103 glitch só no "pare de rolar"):
#  - quadro 0 já é o impacto (sem logo, sem fade); voz desde o quadro 0; SFX de impacto no 0; corte a cada 0,8-1,2 s
#  - loop aberto ("o melhor vem no final"), micro-reveals, barra de progresso, final emenda com o começo
#  - zona segura do Reels: nada de texto nos 15% de cima (0-288 px) nem nos 15% de baixo (1632-1920 px)
import os, sys, json
D = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(D, '..', 'identidade'))
import gerar3 as g
TG = g.TIT_GRAD; IMG = '../motion-01/img/'
R = {r['n']: r for r in json.load(open(os.path.join(D, 'roteiros.json')))}
P = {p['n']: p for p in json.load(open(os.path.join(D, '..', 'motion-01', 'produtos.json')))}
NUM = '(98) 98827-1882'

def shots(n, T):
    p = P[n]; pr = 'R$ ' + p['preco'].split(',')[0]; cap = p['cap']
    base = {  # gancho diferente em cada vídeo (0 a ~3 s)
     1: [('preco', 0, {'txt': pr, 'sub': 'num iPhone 13 Pro Max?'}), ('prod', 1.0, {'z': 1.9, 'pan': -1}), ('texto', 2.0, {'l1': 'iPhone 13', 'l2': 'Pro Max'})],
     2: [('texto', 0, {'l1': 'POV:', 'l2': 'você com ' + pr + ' no bolso', 'tam': 96}), ('prod', 1.1, {'z': 2.2, 'pan': 1}), ('texto', 2.1, {'l1': 'entrando', 'l2': 'na WF'})],
     3: [('glitch', 0, {'txt': 'PARE DE<br>ROLAR'}), ('prod', 0.9, {'z': 2.0, 'pan': -1}), ('preco', 1.9, {'txt': pr, 'sub': 'iPhone 12 Pro Max'})],
     4: [('texto', 0, {'l1': 'Medo de', 'l2': 'seminovo bichado?', 'tam': 110}), ('prod', 1.0, {'z': 2.3, 'pan': 1, 'cinza': 1}), ('chip', 2.0, {'txt': '✓ Laudo WF'})],
     5: [('antes', 0, {'de': 'R$ 6.499', 'por': 'R$ 6.399'}), ('prod', 1.1, {'z': 1.8, 'pan': 1}), ('texto', 2.1, {'l1': 'iPhone 17', 'l2': 'Pro Max Silver'})],
    }[n]
    meio = [('loop', 3.0, {'txt': 'o melhor vem no final ↓'}), ('prod', 4.0, {'z': 1.2, 'pan': -1}), ('chip', 5.0, {'txt': cap}),
            ('prod', 6.0, {'z': 1.5, 'pan': 1}), ('chip', 7.0, {'txt': '✓ Testado · bateria conferida'}), ('chip', 8.0, {'txt': '✓ Garantia por escrito'}),
            ('preco', 9.0, {'txt': pr, 'sub': p['nome']}), ('chip', 10.1, {'txt': 'Até 18x' if n in (1, 3, 5) else 'Pix com desconto'})]
    fim = [('cta', T - 2.6, {})]
    return [s for s in base + meio if s[1] < T - 2.6] + fim

def legendas(n):
    """legenda palavra por palavra a partir do Whisper (tempo real da fala), juntando 'R $ 2 .699' em 'R$ 2.699'."""
    w = json.load(open(os.path.join(D, 'voz', f'{n}.json')))['palavras']; out = []; pend = None
    for p, t0, t1 in w:
        if p in ('R', '$', 'R$'):
            pend = t0 if pend is None else pend; continue
        if (p.startswith(',00') or p.startswith('.')) and out:
            out[-1] = (out[-1][0] + p.replace(',00', '').rstrip(','), out[-1][1]); continue
        if pend is not None and p[0].isdigit() and p.replace('.', '').replace(',', '').isdigit() and len(p) <= 2 and 'GB' not in p and False:
            pass
        if pend is not None:
            if p.isdigit() and len(p) <= 3 and t0 - pend < 1.5 and p not in ('256', '128'):
                out.append(('R$ ' + p, pend))
            else:
                out.append((p, t0))
            pend = None
        else:
            out.append((p, t0))
    return [({'Core': 'cor', 'GB': 'gigas', 'PIX': 'Pix', 'Mendo': 'Medo'}.get(p, p), t) for p, t in out]

CSS = f'''*{{margin:0;padding:0;box-sizing:border-box}}body{{width:1080px;height:1920px;background:#000;overflow:hidden;font-family:Inter}}
.s{{position:absolute;inset:0;display:none}}.grad{{background:{TG};-webkit-background-clip:text;color:transparent}}
.vidro{{background:rgba(255,255,255,.1);backdrop-filter:blur(20px);border:1px solid rgba(255,255,255,.2);border-radius:60px}}'''
def shot_html(i, k, a, p):
    img = f'{IMG}{p["img"]}'; bgp = f'radial-gradient(ellipse 80% 55% at 50% 45%,{p["tom"]},#000 72%)'
    prodbg = (f'<img class="pz" src="{img}" style="position:absolute;left:0;top:0;width:1080px;height:1920px;object-fit:contain;object-position:{p.get("pos","50% 50%")};'
              f'mix-blend-mode:lighten;{"filter:grayscale(1) brightness(.6);" if a.get("cinza") else ""}">')
    if k == 'prod':
        return f'<div class="s" id="s{i}" data-z="{a["z"]}" data-pan="{a["pan"]}" style="background:{bgp}">{prodbg}</div>'
    if k == 'preco':
        return (f'<div class="s" id="s{i}" style="background:{bgp}"><div class="pz" style="position:absolute;inset:0;opacity:.45">{prodbg}</div>'
                f'<div class="pop" style="position:absolute;left:0;right:0;top:640px;text-align:center;font:200 230px/1 Inter;letter-spacing:-.06em;color:#fff">{a["txt"]}</div>'
                f'<div style="position:absolute;left:0;right:0;top:920px;text-align:center;font:300 60px Inter" class="grad">{a["sub"]}</div></div>')
    if k == 'texto':
        return (f'<div class="s" id="s{i}" style="background:{bgp}"><div class="pop" style="position:absolute;left:70px;right:70px;top:560px;font:200 {a.get("tam",150)}px/1.02 Inter;letter-spacing:-.05em;color:#fff">'
                f'{a["l1"]}<br><span class="grad">{a["l2"]}</span></div></div>')
    if k == 'glitch':
        return (f'<div class="s" id="s{i}" style="background:#000">' + ''.join(f'<div class="gl" data-k="{c}" style="position:absolute;left:0;right:0;top:620px;text-align:center;font:400 200px/1 Inter;letter-spacing:-.04em;color:{col};mix-blend-mode:screen">{a["txt"]}</div>' for c, col in [(0, '#ff2a2a'), (1, '#2affd5'), (2, '#ffffff')]) + '</div>')
    if k == 'antes':
        return (f'<div class="s" id="s{i}" style="background:{bgp}"><div style="position:absolute;left:70px;top:520px;font:300 50px Inter;color:#8e8e93">antes</div>'
                f'<div style="position:absolute;left:70px;top:590px;font:200 150px Inter;color:#8e8e93;text-decoration:line-through;text-decoration-thickness:6px">{a["de"]}</div>'
                f'<div class="pop2" style="position:absolute;left:70px;top:820px;font:300 50px Inter" class="grad"><span class="grad">agora na WF</span></div>'
                f'<div class="pop2" style="position:absolute;left:70px;top:890px;font:200 210px/1 Inter;letter-spacing:-.05em;color:#fff">{a["por"]}</div>'
                f'<div style="position:absolute;left:70px;top:1130px;font:300 30px Inter;color:#8e8e93">preço anterior da própria loja · consulte disponibilidade</div></div>')
    if k == 'chip':
        return (f'<div class="s" id="s{i}" style="background:{bgp}"><div style="position:absolute;inset:0;filter:blur(18px);opacity:.6">{prodbg}</div>'
                f'<div class="pop vidro" style="position:absolute;left:90px;right:90px;top:760px;padding:60px 40px;text-align:center;font:300 76px/1.1 Inter;color:#fff">{a["txt"]}</div></div>')
    if k == 'loop':
        return (f'<div class="s" id="s{i}" style="background:#000"><div class="pop" style="position:absolute;left:70px;right:70px;top:700px;text-align:center;font:200 110px/1.05 Inter;letter-spacing:-.04em">'
                f'<span class="grad">e o melhor</span><br><span style="color:#fff">vem no final ↓</span></div></div>')
    if k == 'cta':
        return (f'<div class="s" id="s{i}" style="background:radial-gradient(ellipse 80% 55% at 50% 40%,#1e1e22,#000 72%)">'
                f'<div style="position:absolute;left:0;right:0;top:330px;display:flex;justify-content:center"><div style="width:230px">{g.logo_svg()}</div></div>'
                f'<div style="position:absolute;left:0;right:0;top:720px;text-align:center;font:300 64px Inter;color:#fff">Chama no WhatsApp agora</div>'
                f'<div class="pop" style="position:absolute;left:0;right:0;top:830px;text-align:center;font:300 118px Inter;letter-spacing:-.04em" class="grad"><span class="grad">{NUM}</span></div>'
                f'<div style="position:absolute;left:0;right:0;top:1010px;text-align:center;font:300 36px Inter;color:#a1a1a6">Consulte disponibilidade · São Luís</div>'
                f'<div style="position:absolute;left:0;right:0;top:1090px;display:flex;justify-content:center;gap:16px;font:300 30px Inter;color:#fff">'
                f'<span class="vidro" style="padding:14px 28px">Laudo WF</span><span class="vidro" style="padding:14px 28px">Garantia</span></div></div>')

for n in R:
    p = P[n]; dur = min(15.0, max(12.0, round(float(os.popen(f'ffprobe -v error -show_entries format=duration -of csv=p=0 {D}/voz/{n}.mp3').read()) + .3, 2)))
    S = shots(n, dur); L = legendas(n)
    corpo = ''.join(shot_html(i, k, a, p) for i, (k, t0, a) in enumerate(S))
    html = f'''<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Inter:wght@200;300;400&display=swap" rel="stylesheet"><style>{CSS}</style></head><body>
<div id="cena" style="position:absolute;inset:0">{corpo}</div>
<div id="leg" style="position:absolute;left:60px;right:60px;top:1400px;text-align:center;font:400 92px/1 Inter;letter-spacing:-.03em;color:#fff;text-shadow:0 6px 30px rgba(0,0,0,.9)"></div>
<div style="position:absolute;left:70px;right:70px;top:300px;height:8px;border-radius:4px;background:rgba(255,255,255,.15)"><div id="bar" style="height:100%;border-radius:4px;background:{TG}"></div></div>
<div id="leak" style="position:absolute;inset:-200px;background:radial-gradient(circle at 15% 10%,rgba(255,150,70,.45),transparent 40%),radial-gradient(circle at 90% 80%,rgba(80,130,255,.3),transparent 45%);mix-blend-mode:screen;pointer-events:none"></div>
<div style="position:absolute;right:70px;top:1560px;font:300 18px Inter;color:#6e6e73">Imagem ilustrativa · Apple Newsroom</div>
<div id="flash" style="position:absolute;inset:0;background:#fff;opacity:0"></div>
<script>
const S={json.dumps([[k, t0] for k, t0, a in S])},L={json.dumps(L, ensure_ascii=False)},T={dur};
const E=(a,b,t)=>Math.min(1,Math.max(0,(t-a)/(b-a))),ease=x=>1-Math.pow(1-x,3);
window.render=function(t){{
 let tt=t>T-.3?0:t; // últimos 0,3 s voltam ao 1º quadro: emenda em loop
 let a=0;for(let i=0;i<S.length;i++)if(tt>=S[i][1])a=i;
 S.forEach((s,i)=>document.getElementById('s'+i).style.display=i==a?'block':'none');
 const el=document.getElementById('s'+a),lt=tt-S[a][1],k=S[a][0];
 el.querySelectorAll('.pz').forEach(z=>{{const zz=+(el.dataset.z||1.15),pn=+(el.dataset.pan||0);z.style.transform=`scale(${{zz*(1+.06*lt)}}) translateX(${{pn*30*lt}}px)`}});
 el.querySelectorAll('.pop').forEach(p=>{{const q=ease(E(0,.18,lt));p.style.transform=`scale(${{1.15-.15*q}})`;p.style.opacity=1}});
 el.querySelectorAll('.pop2').forEach(p=>{{const q=ease(E(.45,.65,lt));p.style.transform=`scale(${{1.3-.3*q}})`;p.style.opacity=q}});
 el.querySelectorAll('.gl').forEach(g=>{{const kk=+g.dataset.k,j=(Math.sin(t*97+kk*13)*14)*(kk<2?1:0);g.style.transform=`translate(${{j}}px,${{(kk-1)*4*Math.sin(t*61)}}px)`}});
 const sh=Math.max(0,1-lt/.3)*(k=='preco'||k=='glitch'||a==0?1:.3);document.getElementById('cena').style.transform=`translate(${{12*sh*Math.sin(t*83)}}px,${{9*sh*Math.cos(t*71)}}px)`;
 document.getElementById('flash').style.opacity=Math.max(0,.55-lt/.12*.55)*(a>0?1:0);
 let w='';for(const [p,ts] of L)if(t>=ts)w=p;document.getElementById('leg').innerHTML=k=='cta'?'':w;
 document.getElementById('bar').style.width=(100*Math.min(1,t/T))+'%';
 document.getElementById('leak').style.opacity=.2+.15*Math.sin(t*1.3);
}};render(0);</script></body></html>'''
    open(os.path.join(D, f'v{n}.html'), 'w').write(html); json.dump({'dur': dur}, open(os.path.join(D, f'v{n}.json'), 'w'))
    print(n, dur, len(S), 'cortes')
