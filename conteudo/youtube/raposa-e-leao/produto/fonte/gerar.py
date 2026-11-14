#!/usr/bin/env python3
# Gera o MANUAL DE CAMPO e a isca (7 frases) em HTML e PDF 4:5 (1080x1350). Conta Pedro, 14/11/2026.
# Uso: python3 gerar.py            (gera os dois, confere transbordo e salva as prévias em fonte/previa/)
# Referências copiadas (ver ../TEMPLATE.md): Stripe Press (página escura, linha técnica e rótulos pequenos),
# Daily Stoic Store (selo/medalha, seriedade clássica) e Antofágica/Adelphi (clássico editorial: capa com
# gravura e tipografia grande, cartão claro de citação).
import asyncio, html, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import conteudo as C
D = os.path.dirname(os.path.abspath(__file__)); P = os.path.dirname(D)
LINK_VENDA = ""   # quando a página de venda estiver no ar, pôr o link aqui e gerar de novo
e = html.escape

CSS = """
@font-face{font-family:Anton;src:url(../fonts/Anton-Regular.ttf)}
@font-face{font-family:Cinzel;src:url(../fonts/Cinzel.ttf);font-weight:400 900}
@font-face{font-family:Cormorant;src:url(../fonts/CormorantGaramond.ttf);font-weight:300 700}
@font-face{font-family:Cormorant;src:url(../fonts/CormorantGaramond-Italic.ttf);font-weight:300 700;font-style:italic}
@font-face{font-family:Inter;src:url(../fonts/Inter.ttf);font-weight:100 900}
:root{--noite:#0B0A08;--carvao:#17140F;--ouro:#C9A227;--ouro2:#E2BE4A;--brasa:#D9622B;--perg:#EFE6D2;--sangue:#8E1B1B;--cinza:#9c937f}
*{box-sizing:border-box;margin:0;padding:0}
@page{size:1080px 1350px;margin:0}
body{background:#000;font-family:Inter,sans-serif;color:var(--perg);-webkit-font-smoothing:antialiased}
.pg{width:1080px;height:1350px;position:relative;overflow:hidden;background:var(--noite);page-break-after:always;break-after:page;padding:64px 76px 0}
.pg:before{content:"";position:absolute;inset:0;background:radial-gradient(ellipse at 50% 30%,rgba(60,46,24,.35),transparent 62%);pointer-events:none}
.pg>*{position:relative}
.top{display:flex;justify-content:space-between;font:600 15px Cinzel;letter-spacing:.22em;color:var(--ouro);border-bottom:1px solid rgba(201,162,39,.35);padding-bottom:16px}
.top span:last-child{color:var(--cinza)}
.rod{position:absolute;left:76px;right:76px;bottom:38px;display:flex;justify-content:space-between;align-items:center;font:500 14px Inter;letter-spacing:.08em;color:#7d7462;border-top:1px solid rgba(239,230,210,.12);padding-top:14px}
.rod b{font:400 22px Anton;color:var(--ouro);letter-spacing:.04em}
h1,h2,.anton{font-family:Anton;font-weight:400;text-transform:uppercase;line-height:1.02;letter-spacing:.005em}
.rot{font:700 15px Cinzel;letter-spacing:.24em;color:var(--ouro);text-transform:uppercase}
p{font-size:24px;line-height:1.45}
em.o{font-style:normal;color:var(--ouro2)}
/* ---------- situação */
.cab{display:flex;gap:30px;align-items:flex-start;margin-top:34px}
.num{font:400 150px/0.86 Anton;color:transparent;-webkit-text-stroke:2px var(--ouro);min-width:170px}
.cab h2{font-size:55px;margin-top:14px;color:var(--perg)}
.modo{display:inline-block;font:700 14px Cinzel;letter-spacing:.24em;padding:7px 14px 6px;border:1px solid var(--ouro);color:var(--ouro2);border-radius:2px}
.modo.r{border-color:var(--brasa);color:#f08a52}
.modo.rl{border-image:linear-gradient(90deg,var(--brasa),var(--ouro)) 1;color:var(--perg)}
.cena{margin-top:26px;font-size:25px;color:#d9cfb9}
.cit{margin-top:26px;background:var(--carvao);border-left:5px solid var(--ouro);padding:26px 32px 24px}
.cit blockquote{font:italic 500 33px/1.22 Cormorant;color:var(--ouro2)}
.cit .trad{font-size:23px;line-height:1.4;margin-top:14px;color:var(--perg)}
.cit figcaption{font:700 14px Cinzel;letter-spacing:.22em;color:var(--cinza);margin-top:16px;text-transform:uppercase}
.vB .cab{flex-direction:row-reverse;justify-content:space-between}
.vB .num{text-align:right;color:var(--ouro);-webkit-text-stroke:0}
.vB .cit{background:var(--perg);border-left:0;border-top:5px solid var(--brasa)}
.vB .cit blockquote{color:#2a2012}.vB .cit .trad{color:#3b3222}.vB .cit figcaption{color:#7a5a1a}
.duas{display:grid;grid-template-columns:1fr 1.08fr;gap:36px;margin-top:28px}
.duas h3,.freio h3{font:700 15px Cinzel;letter-spacing:.24em;color:var(--ouro);margin-bottom:10px}
.duas p,.duas li{font-size:21.5px;line-height:1.42;color:#ded4bf}
.duas ol{list-style:none;counter-reset:n}
.duas li{counter-increment:n;position:relative;padding-left:40px;margin-bottom:10px}
.duas li:before{content:counter(n);position:absolute;left:0;top:-2px;font:400 27px Anton;color:var(--ouro)}
.freio{margin-top:22px;border:1px solid rgba(217,98,43,.55);padding:16px 22px 17px;display:grid;grid-template-columns:118px 1fr;gap:10px;align-items:start}
.freio h3{color:#f08a52;margin:4px 0 0}
.freio p{font-size:21px;line-height:1.4;color:#e6dcc8}
/* ---------- capa */
.capa{padding:0}
.capa .foto{position:absolute;right:-70px;top:150px;width:800px;height:1050px;background:center 12%/cover;filter:contrast(1.12) brightness(.92);-webkit-mask-image:linear-gradient(90deg,transparent 2%,#000 46%),linear-gradient(0deg,transparent 0,#000 30%);-webkit-mask-composite:source-in;mask-composite:intersect}
.brilho{position:absolute;border-radius:50%;background:radial-gradient(circle,rgba(217,98,43,.5),transparent 65%);mix-blend-mode:screen}
.capa .et{position:absolute;left:76px;top:70px;font:700 17px Cinzel;letter-spacing:.26em;color:var(--noite);background:var(--ouro);padding:11px 18px 9px}
.capa .canal{position:absolute;right:76px;top:76px;font:700 17px Cinzel;letter-spacing:.3em;color:var(--perg)}
.capa h1{position:absolute;left:70px;bottom:330px;font-size:236px;line-height:.86;color:var(--perg)}
.capa h1 em{font-style:normal;color:var(--ouro2);display:block}
.capa h1 small{display:block;font-size:92px;line-height:1;margin-bottom:14px;letter-spacing:.01em}
.capa .sub{position:absolute;left:76px;bottom:178px;width:700px;font:italic 500 37px/1.18 Cormorant;color:var(--perg)}
.capa .pe{position:absolute;left:76px;right:76px;bottom:56px;display:flex;align-items:center;gap:18px;border-top:1px solid rgba(201,162,39,.4);padding-top:22px;font:700 15px Cinzel;letter-spacing:.24em;color:var(--ouro)}
.capa .pe img{width:62px;height:62px;border-radius:50%}
.capa .pe span:last-child{margin-left:auto;color:var(--cinza)}
.tarja{background:var(--sangue);color:var(--perg);padding:0 14px}
/* ---------- abertura de parte */
.parte{padding:0}
.parte .foto{position:absolute;inset:0;background:center 15%/cover;filter:contrast(1.15) brightness(.62)}
.parte .veu{position:absolute;inset:0;background:linear-gradient(180deg,rgba(11,10,8,.55) 0,rgba(11,10,8,.1) 30%,rgba(11,10,8,.93) 62%,var(--noite) 100%)}
.parte .rom{position:absolute;left:70px;top:52px;font:400 250px/1 Anton;color:transparent;-webkit-text-stroke:2px var(--ouro2)}
.parte .cx{position:absolute;left:76px;right:76px;bottom:96px}
.parte h1{font-size:104px;color:var(--perg);margin:14px 0 14px}
.parte .lin{font:italic 500 36px/1.2 Cormorant;color:var(--ouro2);margin-bottom:30px}
.parte ol{list-style:none;border-top:1px solid rgba(201,162,39,.4)}
.parte li{display:flex;gap:22px;align-items:baseline;padding:13px 0;border-bottom:1px solid rgba(239,230,210,.14);font-size:25px}
.parte li b{font:400 27px Anton;color:var(--ouro);min-width:44px}
/* ---------- páginas de texto */
.txt h1{font-size:92px;margin:44px 0 26px}
.txt h1.m{font-size:76px}
.txt p{margin-bottom:20px;color:#e2d8c3}
.txt .gr{font:italic 500 40px/1.2 Cormorant;color:var(--ouro2);margin-bottom:26px}
.anat{margin-top:8px;border-top:1px solid rgba(201,162,39,.4)}
.anat div{display:grid;grid-template-columns:210px 1fr;gap:24px;padding:19px 0;border-bottom:1px solid rgba(239,230,210,.14)}
.anat b{font:700 16px Cinzel;letter-spacing:.22em;color:var(--ouro);padding-top:6px}
.anat span{font-size:23.5px;line-height:1.4}
.dois{display:grid;grid-template-columns:1fr 1fr;gap:26px;margin-top:26px}
.cartao{background:var(--carvao);padding:26px 28px;border-top:4px solid var(--ouro)}
.cartao.r{border-color:var(--brasa)}
.cartao h3{font:400 46px Anton;text-transform:uppercase;margin-bottom:10px}
.cartao p{font-size:22px;line-height:1.4;margin:0}
.lei{background:var(--perg);color:#241b0e;padding:36px 40px;margin:8px 0 28px;border-top:6px solid var(--brasa)}
.lei blockquote{font:italic 600 45px/1.15 Cormorant}
.lei p{font-size:25px;margin:16px 0 0;color:#3b3222}
.lei cite{display:block;font:700 15px Cinzel;font-style:normal;letter-spacing:.22em;color:#7a5a1a;margin-top:16px}
.sum{columns:2;column-gap:44px;margin-top:6px}
.sum section{break-inside:avoid;margin-bottom:22px}
.sum h3{font:700 15px Cinzel;letter-spacing:.2em;color:var(--ouro);border-bottom:1px solid rgba(201,162,39,.4);padding-bottom:8px;margin-bottom:8px}
.sum li{list-style:none;display:flex;gap:12px;font-size:19.5px;line-height:1.3;padding:3.5px 0;color:#e2d8c3}
.sum li b{font:400 20px Anton;color:var(--ouro);min-width:30px}
.perg{margin-top:4px;border-top:1px solid rgba(201,162,39,.4)}
.perg div{display:grid;grid-template-columns:74px 1fr;gap:10px;padding:13px 0 12px;border-bottom:1px solid rgba(239,230,210,.14)}
.perg i{font:400 52px/1 Anton;font-style:normal;color:var(--ouro)}
.perg h3{font:400 29px Anton;text-transform:uppercase;letter-spacing:.01em}
.perg p{font-size:22px;line-height:1.36;margin:4px 0 4px}
.perg small{font:700 12.5px Cinzel;letter-spacing:.2em;color:var(--cinza);text-transform:uppercase}
.folha{background:var(--perg);color:#241b0e}
.folha:before{display:none}
.folha .top{color:#7a5a1a;border-color:rgba(36,27,14,.3)}.folha .top span:last-child{color:#6b6252}
.folha h1{font-size:76px;margin:36px 0 8px}
.folha p{font-size:21px;color:#3b3222}
.folha .campo{margin-top:18px}
.folha .campo b{font:700 14px Cinzel;letter-spacing:.2em;color:#7a5a1a;display:block}
.folha .campo i{display:block;border-bottom:1px solid rgba(36,27,14,.45);height:42px}
.folha .g2{display:grid;grid-template-columns:1fr 1fr;gap:0 34px}
.folha .rod{color:#6b6252;border-color:rgba(36,27,14,.25)}.folha .rod b{color:#7a5a1a}
.l26{margin-top:2px;border-top:1px solid rgba(201,162,39,.4)}
.l26 div{display:grid;grid-template-columns:86px 250px 1fr;gap:14px;align-items:baseline;padding:13.5px 0;border-bottom:1px solid rgba(239,230,210,.14)}
.l26 i{font:400 30px Anton;font-style:normal;color:var(--ouro)}
.l26 b{font:700 14.5px Cinzel;letter-spacing:.12em;text-transform:uppercase;color:var(--perg);line-height:1.3}
.l26 span{font-size:21px;line-height:1.34;color:#ded4bf}
.ff{margin-top:2px;border-top:1px solid rgba(201,162,39,.4)}
.ff div{padding:12px 0 11px;border-bottom:1px solid rgba(239,230,210,.14);display:grid;grid-template-columns:1fr 220px;gap:6px 20px}
.ff h3{font:italic 600 31px/1.15 Cormorant;color:var(--perg)}
.ff .v{font:700 13px Cinzel;letter-spacing:.18em;text-align:right;color:#f08a52;padding-top:8px}
.ff p{grid-column:1/3;font-size:19.5px;line-height:1.36;color:#cfc5b0;margin:0}
.cred{columns:2;column-gap:40px;margin-top:8px}
.cred li{list-style:none;font-size:19px;line-height:1.35;padding:5px 0;color:#cfc5b0;break-inside:avoid}
.cred li b{color:var(--perg);font-weight:600}
.txt h3.sec{font:700 15px Cinzel;letter-spacing:.24em;color:var(--ouro);margin:26px 0 12px}
.passos div{display:grid;grid-template-columns:96px 1fr;gap:18px;padding:22px 0;border-bottom:1px solid rgba(239,230,210,.14)}
.passos i{font:400 84px/0.9 Anton;font-style:normal;color:transparent;-webkit-text-stroke:2px var(--ouro)}
.passos h3{font:400 36px Anton;text-transform:uppercase;margin-bottom:6px}
.passos p{font-size:23px;margin:0}
/* ---------- isca */
.fr .ver{display:inline-block;font:400 46px Anton;letter-spacing:.02em;padding:6px 20px 4px;margin-top:40px;background:var(--sangue);color:var(--perg)}
.fr .ver.ouro{background:var(--ouro);color:var(--noite)}
.fr .n{position:absolute;right:76px;top:120px;font:400 200px/1 Anton;color:transparent;-webkit-text-stroke:2px rgba(201,162,39,.7)}
.fr h1{font:italic 600 74px/1.04 Cormorant;text-transform:none;margin:24px 0 22px;max-width:800px;color:var(--perg)}
.fr h1:before{content:"“"}.fr h1:after{content:"”"}
.fr .pq{font-size:24px;color:#d9cfb9;max-width:900px}
.fr .cit{margin-top:26px}
.fr h3{font:700 15px Cinzel;letter-spacing:.24em;color:var(--ouro);margin:26px 0 8px}
.fr .certo{font-size:24px;color:#e6dcc8}
"""

def top(dir_="MANUAL DE CAMPO", esq="RAPOSA E LEÃO"):
    return f'<header class="top"><span>{esq} · MANUAL DE CAMPO</span><span>{e(dir_)}</span></header>'
def rod(n, txt="O texto é de Maquiavel. A aplicação é interpretação nossa."):
    return f'<footer class="rod"><span>{e(txt)}</span><b>{n:02d}</b></footer>'

def manual():
    pg = []; n = [0]
    def add(cls, inner, r=True, txt=None):
        n[0] += 1
        pg.append(f'<section class="pg {cls}">{inner}{rod(n[0], txt) if r and txt else rod(n[0]) if r else ""}</section>')
    # 1 capa (modelo de thumb A do canal: texto à esquerda, retrato P&B à direita, brilho de brasa)
    add("capa", '''<div class="brilho" style="right:60px;top:210px;width:760px;height:760px"></div>
<div class="foto" style="background-image:url(../img/maquiavel.jpg)"></div>
<div class="et">O PRÍNCIPE · DISCURSOS</div><div class="canal">RAPOSA E LEÃO</div>
<h1><small>MANUAL DE</small><em>CAMPO</em></h1>
<p class="sub">30 situações de poder no trabalho, nos negócios e na vida. O que Maquiavel escreveu, com obra e capítulo, e como jogar hoje.</p>
<div class="pe"><img src="../img/selo.jpg"><span>CADA FRASE COM A FONTE</span><span>EDIÇÃO 1 · 2026</span></div>''', r=False)
    # 2 aviso
    add("txt", top("ANTES DE COMEÇAR") + '''<h1>Leia isto <em class="o">primeiro</em></h1>
<p class="gr">Este não é um livro de frases. É um manual de consulta para a hora em que você precisa decidir.</p>
<p>Maquiavel passou catorze anos dentro do governo de Florença. Negociou com reis, com papas e com César Bórgia. Perdeu o cargo, foi preso e torturado. Só então escreveu o que tinha visto. Ele não escreveu sobre como o mundo deveria ser. Escreveu sobre como as pessoas agem quando há poder, dinheiro e medo em jogo.</p>
<p>Aqui você encontra <b>30 situações</b> que se repetem na vida de quem trabalha, negocia e lidera. Em cada uma, o texto dele vem primeiro, em italiano e em português, com obra e capítulo. Depois vem a aplicação.</p>
<h3 class="sec">TRÊS AVISOS HONESTOS</h3>
<p><b>1. O texto é dele. A aplicação é nossa.</b> Tudo o que está em "O lance" e em "O freio" é interpretação para a vida de hoje. Você pode discordar. A citação, não: ela foi conferida no original.</p>
<p><b>2. Este manual não promete resultado.</b> Ele ajuda a enxergar a situação e a escolher com mais calma. O resultado depende de você, dos outros e da sorte, que o próprio Maquiavel dizia mandar em metade.</p>
<p><b>3. Nada aqui ensina golpe.</b> Os exemplos dele têm crimes, e ele os conta para explicar o poder, não para recomendar. Cada situação termina com um freio.</p>''')
    # 3 como usar
    add("txt", top("COMO USAR") + '''<h1 class="m">Como ler <em class="o">cada página</em></h1>
<p>Não leia de uma vez. Procure no sumário a situação que você está vivendo e vá direto a ela. Toda página tem as mesmas cinco partes:</p>
<div class="anat">
<div><b>A CENA</b><span>A situação, do jeito que ela aparece na sua semana.</span></div>
<div><b>O TEXTO</b><span>O que Maquiavel escreveu, em italiano e em português, com obra e capítulo.</span></div>
<div><b>NO LIVRO</b><span>O caso ou o raciocínio que ele usa no mesmo trecho, como ele o conta.</span></div>
<div><b>O LANCE</b><span>Três passos para hoje. É interpretação nossa.</span></div>
<div><b>O FREIO</b><span>O limite. Onde a ideia vira distorção, abuso ou coisa ilegal.</span></div>
</div>
<div class="dois">
<div class="cartao r"><span class="modo r">RAPOSA</span><h3 style="margin-top:14px">Enxergar</h3><p>A situação pede leitura: separar fato de esperança, ver a armadilha, escolher a hora.</p></div>
<div class="cartao"><span class="modo">LEÃO</span><h3 style="margin-top:14px">Agir</h3><p>A situação pede firmeza: decidir, cortar, dizer não, sustentar a posição.</p></div>
</div>
<p style="margin-top:24px">No fim do manual há três ferramentas: <b>as 13 perguntas</b> para qualquer decisão, <b>a folha de decisão</b> para imprimir e <b>O Príncipe em 26 linhas</b>.</p>''')
    # 4 a lei
    add("txt", top("A LEI DO CANAL") + '''<h1>A raposa e <em class="o">o leão</em></h1>
<div class="lei"><blockquote lang="it">«bisogna adunque essere golpe a conoscere e' lacci, e lione a sbigottire e' lupi»</blockquote>
<p>"é preciso ser raposa para conhecer as armadilhas e leão para assustar os lobos"</p><cite>O PRÍNCIPE, CAP. XVIII</cite></div>
<p>A ideia inteira cabe nessa frase. No mesmo trecho ele explica: o leão não se defende das armadilhas, e a raposa não se defende dos lobos. Quem é só leão cai no laço. Quem é só raposa é devorado.</p>
<p>No capítulo XIX, ao falar do imperador Sétimo Severo, ele usa as duas palavras juntas: <i style="font-family:Cormorant;font-size:29px;color:var(--ouro2)">«uno ferocissimo lione e una astutissima golpe»</i>, um leão ferocíssimo e uma raposa astutíssima.</p>
<p>Quase todo erro que você vai ver nestas páginas é um erro de animal trocado. É a pessoa que bate de frente quando devia enxergar a armadilha. Ou a que fica calculando quando devia dizer não.</p>
<p><b>Por isso cada situação traz uma marca:</b> raposa, leão, ou os dois. Ela mostra o que aquele momento pede de você primeiro.</p>''')
    # 5 sumário
    s = top("SUMÁRIO") + '<h1 class="m">30 situações, <em class="o">6 terrenos</em></h1><div class="sum">'
    for i, (rom, nome, lin, img) in enumerate(C.PARTES):
        s += f'<section><h3>{rom} · {nome}</h3>' + ''.join(f'<li><b>{i*5+j+1:02d}</b>{e(C.S[i*5+j]["t"])}</li>' for j in range(5)) + '</section>'
    s += '<section><h3>FERRAMENTAS</h3><li><b>+</b>As 13 perguntas do Príncipe</li><li><b>+</b>Folha de decisão (para imprimir)</li><li><b>+</b>O Príncipe em 26 linhas</li><li><b>+</b>7 frases que ele nunca disse</li></section></div>'
    add("txt", s)
    # partes + situações
    k = 0
    for i, (rom, nome, lin, img) in enumerate(C.PARTES):
        lis = ''.join(f'<li><b>{i*5+j+1:02d}</b>{e(C.S[i*5+j]["t"])}</li>' for j in range(5))
        add("parte", f'<div class="foto" style="background-image:url(../img/{img}.jpg)"></div><div class="veu"></div><div class="brilho" style="right:-120px;top:120px;width:700px;height:700px;opacity:.55"></div><div class="rom">{rom}</div><div class="cx"><span class="rot">PARTE {rom}</span><h1>{nome}</h1><p class="lin">{e(lin)}</p><ol>{lis}</ol></div>', r=False)
        for j in range(5):
            x = C.S[k]; k += 1
            m = {"RAPOSA": "r", "LEÃO": "", "RAPOSA E LEÃO": "rl"}[x["modo"]]
            add(f"sit {'vA' if k % 2 else 'vB'}", top(f"PARTE {rom} · {nome}") + f'''<div class="cab"><div class="num">{k:02d}</div><div><span class="modo {m}">{x["modo"]}</span><h2>{e(x["t"])}</h2></div></div>
<p class="cena">{e(x["cena"])}</p>
<figure class="cit"><blockquote lang="it">«{e(x["it"])}»</blockquote><p class="trad">"{e(x["pt"])}"</p><figcaption>{e(x["ref"])}</figcaption></figure>
<div class="duas"><div><h3>NO LIVRO</h3><p>{e(x["caso"])}</p></div><div><h3>O LANCE</h3><ol>{''.join(f"<li>{e(l)}</li>" for l in x["lance"])}</ol></div></div>
<div class="freio"><h3>O FREIO</h3><p>{e(x["freio"])}</p></div>''')
    # 13 perguntas
    for a, b, tit in ((0, 6, 'As 13 perguntas <em class="o">do Príncipe</em>'), (6, 13, 'As 13 perguntas <em class="o">(continua)</em>')):
        s = top("FERRAMENTA 1") + f'<h1 class="m">{tit}</h1>' + ('<p>Antes de qualquer decisão que pese, passe por estas perguntas. Em geral, três ou quatro delas resolvem o caso.</p>' if a == 0 else '') + '<div class="perg">'
        for q in range(a, b):
            t, p_, r_ = C.PERGUNTAS[q]
            s += f'<div><i>{q+1}</i><span><h3>{e(t)}</h3><p>{e(p_)}</p><small>{e(r_)}</small></span></div>'
        add("txt", s + '</div>', txt="As perguntas são um método nosso, montado sobre os capítulos indicados.")
    # folha de decisão
    campos = ["A decisão, em uma frase", "Os fatos (só o que já aconteceu)", "O que é esperança minha"]
    c2 = ["Depende de mim", "Depende de outros", "Quem perde com isto", "Quem apoia de verdade", "O que é rio (não controlo)", "O dique que posso fazer"]
    c3 = ["O que pede este momento: raposa ou leão?", "O freio: o que eu não faço de jeito nenhum", "Decidi isto, nesta data"]
    s = top("FERRAMENTA 2 · PARA IMPRIMIR") + '<h1>Folha de <span style="color:#8E1B1B">decisão</span></h1><p>Imprima ou copie no caderno. Uma folha por decisão. Guarde: daqui a três meses, confira o que era fato e o que era esperança.</p>'
    s += ''.join(f'<div class="campo"><b>{e(c)}</b><i></i><i></i></div>' for c in campos)
    s += '<div class="g2">' + ''.join(f'<div class="campo"><b>{e(c)}</b><i></i><i></i></div>' for c in c2) + '</div>'
    s += ''.join(f'<div class="campo"><b>{e(c)}</b><i></i></div>' for c in c3)
    add("folha", s, txt="Raposa e Leão · Manual de Campo")
    # 26 linhas
    for a, b in ((0, 9), (9, 18), (18, 26)):
        s = top("FERRAMENTA 3") + f'<h1 class="m">O Príncipe em <em class="o">26 linhas</em></h1>' + ('<p>Um capítulo por linha, para você saber onde procurar no livro inteiro.</p>' if a == 0 else '') + '<div class="l26">'
        s += ''.join(f'<div><i>{r_}</i><b>{e(t)}</b><span>{e(l)}</span></div>' for r_, t, l in C.LINHAS26[a:b])
        add("txt", s + '</div>', txt="Resumo nosso. Para citar, vá ao capítulo.")
    # frases falsas
    s = top("BÔNUS") + '<h1 class="m">7 frases que ele <em class="o">nunca disse</em></h1><p>As frases mais famosas de Maquiavel não são dele, ou foram cortadas. Antes de repetir uma, confira aqui.</p><div class="ff">'
    for f in C.FALSAS:
        s += f'<div><h3>"{e(f["frase"])}"</h3><span class="v">{e(f["veredito"])}</span><p>{e(f["certo"])} <span style="color:var(--cinza)">({e(f["ref"])})</span></p></div>'
    add("txt", s + '</div>', txt="Fonte de cada veredito: o capítulo indicado.")
    # fontes e créditos
    add("txt", top("FONTES") + '''<h1 class="m">De onde vem <em class="o">cada frase</em></h1>
<p><b>O Príncipe:</b> as citações seguem o texto italiano da edição crítica de Giorgio Inglese (Einaudi, 1995). Uma delas, a do capítulo XIII, segue o texto tradicional impresso.</p>
<p><b>Discursos sobre a primeira década de Tito Lívio:</b> texto italiano de domínio público (edição Martelli e Wikisource italiano). A referência vem como livro e capítulo: "livro II, cap. 14".</p>
<p><b>Conferência:</b> cada trecho em italiano deste manual foi comparado, palavra por palavra, com o texto original. As traduções são livres e nossas, feitas para serem entendidas em uma leitura. Onde há "(…)", um pedaço do trecho foi pulado.</p>
<p><b>Casos históricos:</b> estão como Maquiavel os conta nos capítulos indicados. Ele escrevia para convencer, e historiadores discutem vários desses relatos.</p>
<h3 class="sec">IMAGENS · OBRAS EM DOMÍNIO PÚBLICO</h3><ul class="cred">''' + ''.join(f'<li><b>{e(a)}</b> · {e(b)}</li>' for a, b in C.CREDITOS[:6]) + '''</ul>
<h3 class="sec">USO</h3><p style="font-size:21px">Este material é de uso pessoal de quem comprou. Citar um trecho com a fonte é bem-vindo. Revender ou distribuir o arquivo, não.</p>''', txt="Raposa e Leão · Manual de Campo · Edição 1 · 2026")
    # próximo passo
    add("txt", top("O PRÓXIMO PASSO") + '''<h1>Agora, <em class="o">em campo</em></h1>
<p class="gr">Ler sobre poder não muda nada. O que muda é a próxima decisão.</p>
<div class="passos">
<div><i>1</i><span><h3>Uma situação por semana</h3><p>Escolha a que mais parece com a sua semana. Faça só o primeiro passo de "O lance". Anote o que aconteceu.</p></span></div>
<div><i>2</i><span><h3>Uma folha por decisão</h3><p>Para toda decisão que pese no bolso ou no nome, preencha a folha de decisão antes. Leva dez minutos.</p></span></div>
<div><i>3</i><span><h3>Os casos, em vídeo</h3><p>No canal Raposa e Leão, cada vídeo conta um desses casos por inteiro: Bórgia, Savonarola, Aníbal, Júlio II. Procure por @RaposaeLeao no YouTube.</p></span></div>
<div><i>4</i><span><h3>O livro inteiro</h3><p>Se este manual abriu o apetite, leia O Príncipe. São 26 capítulos curtos. Com as 26 linhas ao lado, você não se perde.</p></span></div>
</div>
<p style="margin-top:26px">Novos materiais do canal são avisados primeiro a quem tem este manual, pelo e-mail da compra.</p>''', txt="Raposa e Leão · Manual de Campo")
    return pg

def isca():
    pg = []; n = [0]
    def tp(d): return f'<header class="top"><span>RAPOSA E LEÃO</span><span>{e(d)}</span></header>'
    def add(cls, inner, r=True):
        n[0] += 1
        pg.append(f'<section class="pg {cls}">{inner}{rod(n[0], "Raposa e Leão · 7 frases que Maquiavel nunca disse") if r else ""}</section>')
    # capa (modelo de thumb B: retrato à esquerda, texto à direita, brilho de ouro)
    add("capa", '''<div class="brilho" style="left:-80px;top:120px;width:760px;height:760px;background:radial-gradient(circle,rgba(201,162,39,.42),transparent 65%)"></div>
<div class="foto" style="background-image:url(../img/maquiavel.jpg);right:auto;left:-150px;top:60px;transform:scaleX(-1)"></div>
<div class="et">CONFERIDO NO ORIGINAL</div><div class="canal">RAPOSA E LEÃO</div>
<h1 style="line-height:1.02;font-size:122px;bottom:300px;left:auto;right:70px;text-align:right"><small style="font-size:56px">7 FRASES QUE</small>MAQUIAVEL<em>NUNCA <span style="color:#fff;background:#8E1B1B;padding:0 12px;display:inline-block;line-height:.9;margin-top:10px">DISSE</span></em></h1>
<p class="sub" style="left:auto;right:76px;text-align:right;width:640px;bottom:170px">E o que ele escreveu de verdade, com obra e capítulo.</p>
<div class="pe"><img src="../img/selo.jpg"><span>GUIA GRATUITO DO CANAL</span><span>2026</span></div>''', r=False)
    add("txt", tp("POR QUE ISTO IMPORTA") + '''<h1 class="m">A frase mais famosa dele <em class="o">não é dele</em></h1>
<p class="gr">"Os fins justificam os meios." Você já leu, já ouviu, talvez já tenha repetido. Maquiavel nunca escreveu isso.</p>
<p>Ele é um dos autores mais citados do mundo, e um dos menos lidos. O resultado é que a maior parte do "Maquiavel" que circula em vídeo, em post e em palestra é de outra pessoa, de um filme, ou foi cortada no meio.</p>
<p>Isso tem custo. Quem aprende poder por frase falsa aprende errado: acha que ele mandou ser cruel, mentir e pisar nos outros. O texto diz coisa bem diferente, e bem mais útil.</p>
<p>Nas próximas páginas estão as sete mais repetidas. Em cada uma:</p>
<div class="anat">
<div><b>O VEREDITO</b><span>Falsa, cortada, de filme ou de outro autor.</span></div>
<div><b>O TEXTO</b><span>O que ele escreveu, em italiano e em português.</span></div>
<div><b>A FONTE</b><span>Obra e capítulo, para você conferir.</span></div>
<div><b>O USO CERTO</b><span>O que a ideia verdadeira ensina.</span></div>
</div>''')
    for i, f in enumerate(C.FALSAS):
        add("fr", tp(f"FRASE {i+1} DE 7") + f'''<div class="n">{i+1}</div><span class="ver {'ouro' if f['cor']=='ouro' else ''}">{e(f["veredito"])}</span>
<h1>{e(f["frase"])}</h1><p class="pq">{e(f["porque"])}</p>
<figure class="cit"><blockquote lang="it">«{e(f["it"])}»</blockquote><p class="trad">"{e(f["pt"])}"</p><figcaption>{e(f["ref"])}</figcaption></figure>
<h3>O USO CERTO</h3><p class="certo">{e(f["certo"])}</p>''')
    add("txt", tp("FERRAMENTA") + '''<h1 class="m">Como conferir uma frase em <em class="o">30 segundos</em></h1>
<p>Serve para Maquiavel e para qualquer autor antigo.</p>
<div class="passos">
<div><i>1</i><span><h3>Peça obra e capítulo</h3><p>Frase verdadeira tem endereço: "O Príncipe, capítulo XVII". Se a fonte é só o nome do autor, desconfie.</p></span></div>
<div><i>2</i><span><h3>Leia a linha de cima e a de baixo</h3><p>Quase toda distorção é um corte. O "temido ou amado" muda de sentido com a frase inteira.</p></span></div>
<div><i>3</i><span><h3>Veja quem está falando</h3><p>Às vezes o autor cita uma ideia para derrubá-la, como no provérbio da lama. E em peça de teatro, quem fala é o personagem.</p></span></div>
<div><i>4</i><span><h3>Desconfie da frase perfeita</h3><p>Texto de 1513 não soa como legenda de rede social. Se está redonda demais, alguém arredondou.</p></span></div>
</div>''')
    lk = f'<p style="margin-top:22px"><b>Para ver o manual:</b> {e(LINK_VENDA)}</p>' if LINK_VENDA else '<p style="margin-top:22px"><b>Para ver o manual:</b> o link está na descrição dos vídeos e no comentário fixado do canal Raposa e Leão.</p>'
    add("txt", tp("O PRÓXIMO PASSO") + '''<h1 class="m">Agora o que ele <em class="o">escreveu de fato</em></h1>
<p class="gr">Saber o que é falso é metade. A outra metade é usar o verdadeiro.</p>
<p>O <b>Manual de Campo</b> do canal pega 30 situações que se repetem no trabalho, nos negócios e na vida, e mostra em cada uma o que Maquiavel escreveu, com obra e capítulo, e como aplicar hoje.</p>
<div class="anat">
<div><b>30 SITUAÇÕES</b><span>Chefe, sócio, cliente, rival, dinheiro, crise e recomeço. Uma página para cada.</span></div>
<div><b>CADA FRASE COM A FONTE</b><span>Em italiano e em português, conferida no original.</span></div>
<div><b>3 PASSOS E 1 FREIO</b><span>O que fazer hoje, e onde a ideia vira distorção.</span></div>
<div><b>3 FERRAMENTAS</b><span>As 13 perguntas, a folha de decisão e O Príncipe em 26 linhas.</span></div>
</div>''' + lk + '<p style="margin-top:14px;color:var(--cinza);font-size:20px">As citações em italiano deste guia seguem a edição crítica de Giorgio Inglese (Einaudi, 1995). Traduções livres. Retrato da capa: Santi di Tito, séc. XVI, domínio público.</p>')
    return pg

async def render(nome, pgs, pdf):
    from playwright.async_api import async_playwright
    h = f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>{nome}</title><style>{CSS}</style></head><body>{"".join(pgs)}</body></html>'
    f = os.path.join(D, nome + ".html"); open(f, "w", encoding="utf-8").write(h)
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={"width": 1080, "height": 1350})
        await pg.goto("file://" + f); await pg.evaluate("document.fonts.ready"); await pg.wait_for_timeout(800)
        ruins = await pg.evaluate("""()=>[...document.querySelectorAll('.pg')].map((s,i)=>{const r=s.querySelector('.rod');if(!r)return null;const lim=r.getBoundingClientRect().top;let m=0;
          s.querySelectorAll(':scope > *:not(.rod):not(.n)').forEach(x=>{const b=x.getBoundingClientRect();if(b.bottom>m)m=b.bottom});
          const larg=[...s.querySelectorAll('*')].some(x=>x.scrollWidth>x.clientWidth+2&&getComputedStyle(x).overflow!=='hidden'&&x.clientWidth>0&&x.tagName!=='SECTION');
          return {pag:i+1,sobra:Math.round(lim-m),larg}}).filter(x=>x&&(x.sobra<10||x.larg))""")
        print(nome, len(pgs), "páginas", "| SEM ESPAÇO:" if ruins else "| ok", ruins or "")
        os.makedirs(os.path.join(P, "entrega"), exist_ok=True)
        await pg.pdf(path=os.path.join(P, "entrega", pdf), width="1080px", height="1350px", print_background=True, prefer_css_page_size=True)
        pv = os.path.join(D, "previa", nome); os.makedirs(pv, exist_ok=True)
        els = await pg.query_selector_all(".pg")
        for i, el in enumerate(els): await el.screenshot(path=os.path.join(pv, f"p{i+1:02d}.jpg"), type="jpeg", quality=78)
        await b.close()

if __name__ == "__main__":
    asyncio.run(render("manual", manual(), "Raposa-e-Leao-Manual-de-Campo.pdf"))
    asyncio.run(render("isca", isca(), "7-Frases-que-Maquiavel-Nunca-Disse.pdf"))
