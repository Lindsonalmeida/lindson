"""Site bio Al Kántara Group (fase 3, conta Leandro/Webdesigner, 16/11/2026). Modelo: bio do Lindson (lindsonalmeida.pages.dev/bio/).
Gera ../bio/index.html. OG 1200x630 em ../bio/og.jpg (feito pelo shots.js).  python3 gerador/bio.py"""
import os
from urllib.parse import quote
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'bio')
SITE = 'https://lindsonalmeida.pages.dev/alkantara/'
WA = 'https://wa.me/5598985621808?text='
P = ['M0,0 L100,480 L164,480 L164,0 Z', 'M196,0 L196,199.19 L380.54,0 Z', 'M480,0 L424.16,0 L201.32,240.53 L384.39,458.93 Z', 'M360.3,480 L196,283.99 L196,480 Z']
def simb(cores): return '<svg viewBox="0 0 480 480" aria-hidden="true">' + ''.join(f'<path fill="{c}" d="{p}"/>' for c, p in zip(cores, P)) + '</svg>'
DIVS = [('labs', 'Labs', 'IA e software', '#2E4BFF', 0), ('barzakh', 'Barzakh', 'Marca, design e vendas', '#C9A35A', 1), ('media', 'Media', 'Canais e audiência', '#F0A202', 2), ('ventures', 'Ventures', 'Negócios próprios', '#0E8C66', 3)]
def bt(k, n, a, c, i):
    ico = '<img src="m/barzakh-avatar.png" alt="">' if k == 'barzakh' else simb(tuple(c if j == i else 'rgba(239,234,225,.14)' for j in range(4)))
    sub = 'um estúdio Al Kántara' if k == 'barzakh' else 'Al Kántara ' + n
    return f'<a class="div{" ouro" if k == "barzakh" else ""}" href="{SITE}{k}.html" style="--c:{c}"><span class="ic">{ico}</span><span><b>{n}</b><small>{sub} · {a}</small></span><i>→</i></a>'
CASES = [('barzakh-capa', 'Barzakh', 'Identidade · estúdio'), ('duble', 'Dublê', 'App · IA'), ('realtime', 'Real Time', 'Identidade'), ('wf', 'WF Celulares', 'Identidade')]
html = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Al Kántara Group · links</title><meta name="description" content="Grupo de tecnologia de São Luís (MA): Labs, Barzakh, Media e Ventures. Estrutura para o que vem.">
<meta property="og:title" content="Al Kántara Group"><meta property="og:description" content="Estrutura para o que vem. Labs, Barzakh, Media e Ventures.">
<meta property="og:image" content="{SITE}bio/og.jpg"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0B0C0E"><link rel="icon" href="simbolo-latao.svg">
<style>
@font-face{{font-family:F;src:url(f/fraunces.ttf);font-display:swap}}@font-face{{font-family:F;src:url(f/fraunces-it.ttf);font-style:italic;font-display:swap}}
@font-face{{font-family:I;src:url(f/inter.ttf);font-weight:500;font-display:swap}}@font-face{{font-family:I;src:url(f/inter-sb.ttf);font-weight:600;font-display:swap}}
:root{{--tinta:#0B0C0E;--graf:#16181C;--calc:#EFEAE1;--pedra:#8E8A82;--latao:#B8955A;--ouro:#C9A35A;--lin:rgba(239,234,225,.12)}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--tinta);color:var(--calc);font:500 15px/1.5 I,system-ui,sans-serif;overflow-x:hidden}}a{{color:inherit;text-decoration:none}}img,svg{{display:block;max-width:100%}}
.grao{{position:fixed;inset:0;pointer-events:none;z-index:9;opacity:.06;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='160' height='160'%3E%3Cfilter id='n'%3E%3CfeTurbulence baseFrequency='.9' numOctaves='2'/%3E%3C/filter%3E%3Crect width='160' height='160' filter='url(%23n)'/%3E%3C/svg%3E")}}
.halo{{position:fixed;left:50%;top:-180px;width:640px;height:520px;transform:translateX(-50%);background:radial-gradient(closest-side,rgba(184,149,90,.22),transparent);pointer-events:none}}
main{{position:relative;max-width:520px;margin:0 auto;padding:44px 16px 40px}}
.mono{{font:600 10.5px/1.4 I,sans-serif;letter-spacing:.22em;text-transform:uppercase;color:var(--pedra);margin:0}}
.av{{width:96px;height:96px;border-radius:28px;background:var(--graf);border:1px solid rgba(184,149,90,.45);display:grid;place-items:center;margin:0 auto 18px;animation:sobe .9s both}}.av svg{{width:52px}}
h1{{font:400 44px/1 F,serif;letter-spacing:-.02em;text-align:center;margin:6px 0 10px;animation:sobe .9s .08s both}}h1 em{{color:var(--latao)}}
.frase{{text-align:center;color:rgba(239,234,225,.74);margin:0 auto 26px;max-width:340px;animation:sobe .9s .16s both}}
.cta{{display:flex;gap:10px;margin-bottom:30px;animation:sobe .9s .24s both}}.cta a{{flex:1;text-align:center;padding:15px 10px;border-radius:99px;font-weight:600}}
.wa{{background:var(--latao);color:var(--tinta)}}.st{{border:1px solid var(--lin)}}
.sec{{margin:0 0 12px;display:flex;justify-content:space-between;align-items:baseline}}
.div{{display:flex;align-items:center;gap:14px;padding:14px;border-radius:20px;background:var(--graf);border:1px solid var(--lin);margin-bottom:10px;transition:transform .3s,border-color .3s}}
.div:hover{{transform:translateY(-2px);border-color:var(--c)}}.div .ic{{width:44px;height:44px;border-radius:12px;background:#0f1013;display:grid;place-items:center;flex:none;padding:9px}}
.div b{{display:block;font:400 22px/1.1 F,serif}}.div small{{color:var(--pedra);font-size:12.5px}}.div i{{margin-left:auto;font-style:normal;color:var(--c)}}
.div.ouro{{background:linear-gradient(135deg,#221b0f,#121214 70%);border-color:rgba(201,163,90,.55)}}.div.ouro b{{color:var(--ouro)}}.div.ouro .ic{{padding:4px;background:#0B0C0E}}
.ig{{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin:26px 0 30px}}.ig a{{padding:12px 14px;border-radius:14px;border:1px solid var(--lin);font-size:13px}}.ig a span{{display:block;color:var(--pedra);font-size:11px}}
.cases{{display:grid;grid-template-columns:1fr 1fr;gap:10px}}.case{{position:relative;border-radius:18px;overflow:hidden;aspect-ratio:4/5;background:var(--graf)}}
.case img{{width:100%;height:100%;object-fit:cover}}.case div{{position:absolute;inset:auto 0 0;padding:28px 12px 12px;background:linear-gradient(transparent,rgba(11,12,14,.9))}}.case b{{display:block;font:400 18px/1.1 F,serif}}.case span{{font-size:11px;color:var(--pedra)}}
.mais{{display:block;text-align:center;margin:14px 0 34px;color:var(--latao);font-weight:600}}
.ap{{border-radius:22px;overflow:hidden;position:relative}}.ap img{{width:100%;aspect-ratio:16/11;object-fit:cover}}.ap p{{position:absolute;left:14px;bottom:12px;margin:0;font:400 22px/1.1 F,serif}}.ap p em{{color:var(--latao)}}
footer{{text-align:center;margin-top:30px}}footer .k{{width:22px;margin:0 auto 10px;opacity:.7}}
.rv{{opacity:0;transform:translateY(18px);transition:opacity .8s,transform .8s}}.rv.in{{opacity:1;transform:none}}
@keyframes sobe{{from{{opacity:0;transform:translateY(16px)}}}}@media (prefers-reduced-motion:reduce){{*{{animation:none!important;transition:none!important}}.rv{{opacity:1;transform:none}}}}
</style></head><body><div class="grao" aria-hidden="true"></div><div class="halo" aria-hidden="true"></div>
<main><div class="av">{simb(('#EFEAE1', '#EFEAE1', '#B8955A', '#EFEAE1'))}</div>
<p class="mono" style="text-align:center">GRUPO DE TECNOLOGIA · SÃO LUÍS, MA</p>
<h1>Al Kántara <em>Group</em></h1><p class="frase">Estrutura para o que vem. Tecnologia, marca e audiência para negócios que querem ir longe.</p>
<div class="cta"><a class="wa" href="{WA}{quote('Olá! Vim pelo Instagram da Al Kántara.')}" target="_blank" rel="noopener">WhatsApp</a><a class="st" href="{SITE}">Site do grupo</a></div>
<div class="sec"><p class="mono">AS QUATRO DIVISÕES</p></div>
{''.join(bt(*d) for d in DIVS)}
<div class="ig"><a href="https://instagram.com/barzakhstudio" target="_blank" rel="noopener"><span>Instagram</span>@barzakhstudio</a><a href="https://instagram.com/lindsonalmeida_" target="_blank" rel="noopener"><span>Fundador</span>@lindsonalmeida_</a></div>
<div class="sec"><p class="mono">ÚLTIMOS CASES</p></div>
<div class="cases">{''.join(f'<a class="case rv" href="{SITE}cases.html"><img src="m/{i}.webp" alt="{n}" loading="lazy"><div><b>{n}</b><span>{t}</span></div></a>' for i, n, t in CASES)}</div>
<a class="mais" href="{SITE}cases.html">Ver todos os cases →</a>
<div class="ap rv"><img src="m/fachada.webp" alt="Placa Al Kántara em fachada de São Luís" loading="lazy"><p>Quatro pedras,<br><em>uma chave.</em></p></div>
<footer><svg class="k" viewBox="0 0 480 480">{''.join(f'<path fill="#8E8A82" d="{p}"/>' for p in P)}</svg><p class="mono">© 2026 AL KÁNTARA GROUP</p></footer></main>
<script>const io=new IntersectionObserver(es=>es.forEach(e=>{{if(e.isIntersecting){{e.target.classList.add('in');io.unobserve(e.target)}}}}));document.querySelectorAll('.rv').forEach(e=>io.observe(e))</script>
</body></html>'''
open(os.path.join(D, 'index.html'), 'w').write(html); print('bio ok')
