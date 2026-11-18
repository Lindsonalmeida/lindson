# Brand book + manual (um PDF só, 1920x1080, texto selecionável) · Leo Pinto identidade v2 (conta Pedro, 18/11/2026)
# Processo e profundidade copiados do Al Kántara v2 (agencia/marca-holding/v2/): plataforma -> sistema -> aplicações -> resumo.
from base import CSS, COR, logo, foto, c
T = '../entregas/templates'
R = '../referencias'
pgs = []

def pg(inner, bg='var(--pr)', n=True):
    k = len(pgs) + 1
    num = f'<div class="lab box" style="right:70px;bottom:44px;font-size:16px;color:rgba(244,242,238,.55)">Leo Pinto · Identidade v2 · {k:02d}</div>' if n else ''
    pgs.append(f'<section class="pg" style="background:{bg}">{inner}{num}<div class="grao"></div></section>')

def tit(cap, t1, t2='', cor='var(--br)', x=110, y=110, w=900, s=104):
    return f'''<div class="box" style="left:{x}px;top:{y}px;width:{w}px">
<div class="lab" style="color:var(--ou)">{cap}</div>
<div class="ci" style="font-size:{s}px;margin-top:26px;color:{cor};font-weight:900">{t1}{'<br><span style="color:var(--la)">'+t2+'</span>' if t2 else ''}</div>
<div class="hz" style="position:relative;width:160px;margin-top:40px"></div></div>'''

def txt(t, x, y, w, s=24, cor='#cfcac2'):
    return f'<div class="box" style="left:{x}px;top:{y}px;width:{w}px;font:400 {s}px/1.55 Mont;color:{cor}">{t}</div>'

def img(src, x, y, w, extra=''):
    return f'<img class="box" src="{src}" style="left:{x}px;top:{y}px;width:{w}px;{extra}">'

def tela(src, x, y, w, rot=0):  # celular
    h = int(w * 2.05)
    return f'''<div class="box" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;border-radius:{w*.14}px;background:#111;padding:{w*.035}px;
transform:rotate({rot}deg);box-shadow:0 60px 90px rgba(0,0,0,.7),inset 0 0 0 2px #333,0 0 0 1px #000">
<div style="width:100%;height:100%;border-radius:{w*.11}px;overflow:hidden;background:#000;display:flex;flex-direction:column">
<div style="height:{w*.16}px;background:#000;display:flex;align-items:center;padding:0 {w*.06}px;font:600 {w*.045}px Mont;color:#fff">leopinto</div>
<img src="{src}" style="width:100%;display:block"></div></div>'''

# 01 CAPA
pg(f'''<div class="box" style="inset:0;background:radial-gradient(circle at 70% 40%,rgba(255,122,26,.5),transparent 50%)"></div>
<div class="ci box" style="left:110px;top:120px;font-size:30px;letter-spacing:.5em;color:var(--ou);font-weight:500">Identidade de marca · v2</div>
<div class="bc box" style="left:90px;top:230px;font-size:330px;color:rgba(255,255,255,.06)">MANDATO</div>
<img class="foto" src="{foto('d-bracos-cruzados-branca')}" style="right:60px;bottom:0;width:960px">
{img(logo('branco'), 110, 420, 640)}
<div class="lab box" style="left:110px;top:920px;font-size:22px">Brand book e manual · Vereador de São João Batista · MA · novembro de 2026</div>
<div class="vin"></div>''', n=False)

# 02 SUMÁRIO
items = ['Por que uma v2', 'Persona e públicos', 'Plataforma e posicionamento', 'Tom de voz', 'Manifesto', 'Conceito: o horizonte',
         'Logo mantido · área de proteção', 'Versões e usos proibidos', 'Cores do partido', 'Tipografia', 'Grid editorial',
         'Direção de foto', 'Redes: posts, carrossel, story, Reels', 'Os 4 quadros semanais', 'Feed em xadrez', 'Bio e página',
         'Assinatura em movimento', 'Campanha e papelaria', 'Outdoor e evento', 'Quem construiu', 'Referências', 'Resumo de 1 página']
lis = ''.join(f'<div style="display:flex;gap:28px;border-top:1px solid rgba(255,255,255,.14);padding:13px 0"><span class="bc" style="color:var(--la);font-size:30px;width:56px">{i+1:02d}</span><span class="ci" style="font-size:24px;font-weight:700">{t}</span></div>' for i, t in enumerate(items))
pg(tit('Sumário', 'O que', 'tem aqui') + f'<div class="box" style="left:820px;top:110px;width:1000px;columns:2;column-gap:60px">{lis}</div>')

# 03 POR QUE V2
pg(f'''{tit('01 · Diagnóstico', 'De amador', 'a autoridade.')}
{txt('A identidade anterior nasceu rápida, para dar conta do dia a dia: Montserrat Black com Kaushan Script, degradês, etiquetas e muita cor ao mesmo tempo. Funcionou, mas não tinha o peso de quem representa a cidade.<br><br><b style="color:#fff">O que fica:</b> o logo LEO PINTO com o sol nascendo sobre as águas da Baixada e as cores do partido, nos códigos exatos.<br><b style="color:#fff">O que muda:</b> preto como base, tipografia romana de autoridade, retas, uma linha de horizonte e foto com luz de cinema.', 110, 560, 760, 25)}
<div class="box" style="left:1000px;top:110px;width:820px;height:860px;display:grid;grid-template-columns:1fr 1fr;gap:24px">
 <div style="position:relative;background:url(../../instagram-v13-apresentacao/leo-v13-1-esquerda.jpg) center/cover;filter:grayscale(.2) brightness(.8)"><div class="lab" style="position:absolute;left:18px;bottom:18px;background:#000;padding:8px 12px">Antes · v13</div></div>
 <div style="position:relative;background:url({T}/post-manchete.jpg) center/cover"><div class="lab" style="position:absolute;left:18px;bottom:18px;background:var(--la);color:#000;padding:8px 12px">Agora · v2</div></div>
</div>''')

# 04 PERSONA
pers = [('O morador da sede', '35 a 60 anos · comerciante, servidor, pai de família', 'Quer ver quem resolve. Confia em rosto conhecido e em fato com data.'),
        ('O povo dos povoados', 'pescador, lavrador, mãe de família', 'Vê o celular no almoço e à noite. Compartilha no grupo da família o que reconhece.'),
        ('O jovem', '16 a 29 anos · estudante, atleta, primeiro emprego', 'Quer um vereador que fale direto, sem enrolação, e que esteja no campo e na rua.'),
        ('Lideranças e Prefeitura', 'presidentes de associação, igreja, secretarias', 'Precisam de um aliado firme, que some forças e assina junto.')]
cards = ''.join(f'<div style="background:#111418;border-top:4px solid var(--la);padding:34px"><div class="ci" style="font-size:32px;font-weight:900">{a}</div><div class="lab" style="color:var(--ou);font-size:16px;margin:14px 0">{b}</div><div style="font:400 21px/1.5 Mont;color:#cfcac2">{d}</div></div>' for a, b, d in pers)
pg(f'''{tit('02 · Persona', 'Quem precisa', 'confiar nele', s=88)}
{txt('Persona principal (5 linhas): morador de São João Batista, 25 a 65 anos; vê o Instagram e os grupos de WhatsApp no almoço e à noite; dor: "político só aparece na eleição"; confia em rosto conhecido, povoado escrito, fé e prova com data; teste: ele compartilharia no grupo da família?', 110, 520, 700, 23)}
<div class="box" style="left:880px;top:110px;width:930px;display:grid;grid-template-columns:1fr 1fr;gap:22px">{cards}</div>''')

# 05 PLATAFORMA
blk = [('Propósito', 'Estar presente o mandato inteiro, perto de cada povoado, e mostrar o que foi feito.'),
       ('Posicionamento', 'Para o morador de São João Batista que cansou de político que some, Leo Pinto é o vereador engenheiro que está na rua o ano todo e mostra cada entrega, em parceria com a Prefeitura.'),
       ('Diferença', 'Olho de engenheiro: vê a obra, entende o problema técnico e acompanha até ficar pronto.'),
       ('Arquétipo', 'Governante (ordem, responsabilidade, palavra cumprida) com o pé no Cara Comum (é do povo, fala como o povo).'),
       ('Assinatura', 'PRESENÇA QUE RESOLVE.')]
pg(f'''{tit('03 · Plataforma', 'A decisão', 'antes do desenho', s=88)}
<div class="box" style="left:880px;top:110px;width:930px">{''.join(f'<div style="display:grid;grid-template-columns:260px 1fr;gap:30px;border-top:1px solid rgba(255,255,255,.18);padding:20px 0"><div class="lab" style="color:var(--la)">{a}</div><div class="ci" style="font-size:{27 if a!="Assinatura" else 50}px;line-height:1.2;font-weight:{700 if a!="Assinatura" else 900};text-transform:none">{b}</div></div>' for a, b in blk)}</div>
<img class="foto" src="{foto('b-punho')}" style="left:60px;bottom:0;width:640px">''')

# 06 TOM DE VOZ
pares = [('Firme', 'Agressivo'), ('Direto', 'Seco'), ('Do povo', 'Popularesco'), ('Prestador de contas', 'Prometedor'), ('Aliado da gestão', 'Crítico da gestão'), ('Sério', 'Distante')]
pg(f'''{tit('04 · Tom de voz', 'Fala de', 'quem resolve', s=74)}<img class="foto" src="{foto('i-maos-abertas-branca')}" style="left:60px;bottom:0;width:470px">
<div class="box" style="left:880px;top:110px;width:930px">
<div style="display:grid;grid-template-columns:1fr 1fr;gap:0 40px"><div class="lab" style="color:var(--la);padding-bottom:16px">Ele é</div><div class="lab" style="color:#777;padding-bottom:16px">Ele não é</div>
{''.join(f'<div class="ci" style="font-size:40px;border-top:1px solid rgba(255,255,255,.2);padding:16px 0;font-weight:900">{a}</div><div class="ci" style="font-size:40px;border-top:1px solid rgba(255,255,255,.1);padding:16px 0;color:#555;text-decoration:line-through">{b}</div>' for a, b in pares)}</div>
<div style="margin-top:40px;font:400 22px/1.6 Mont;color:#cfcac2">Escreva assim: <b style="color:#fff">"Fui ao povoado, vi, registrei e voltei para mostrar."</b> Nunca assim: "vamos lutar para conquistar". Frase curta, verbo de ação, fato com data e lugar. Sem promessa, sem número que o Leo não confirmou, sem pedir voto.</div></div>''')

# 07 MANIFESTO
pg(f'''<div class="box" style="inset:0;background:radial-gradient(circle at 75% 45%,rgba(255,122,26,.45),transparent 50%)"></div>
<img class="foto" src="{foto('f-punhos')}" style="right:-40px;bottom:0;width:820px">
<div class="box" style="left:110px;top:100px;width:1050px"><div class="lab" style="color:var(--ou)">05 · Manifesto</div>
<div class="ci" style="font-size:46px;line-height:1.32;margin-top:34px;text-transform:none;font-weight:700">Eleição dura um dia.<br>O mandato dura quatro anos.<br>E é nos quatro anos que a gente mostra quem é.<br><span style="color:var(--la)">Presença não é aparecer. É voltar.</span><br>Voltar ao povoado, à obra, à conversa.<br>Ouvir, registrar, somar com a Prefeitura<br>e mostrar o que ficou pronto.<br><span style="color:var(--ou)">Palavra dada, obra feita.</span></div>
<div class="bc" style="font-size:72px;margin-top:40px">Presença que <span style="color:var(--la)">resolve.</span></div></div><div class="vin"></div>''')

# 08 CONCEITO
pg(f'''{tit('06 · Conceito', 'O horizonte', 'da Baixada', s=88)}
{txt('O símbolo do logo já contava a história: o sol nascendo sobre as águas da Baixada. A v2 não inventa grafismo novo. Ela pega a única linha reta que existe nesse símbolo, o horizonte, e faz dela a régua do sistema: um fio em Amarelo-Sol que separa foto e texto, sustenta títulos e alinha todas as peças.<br><br>Reta, firme, sempre na horizontal. Não é raio, não é faixa, não é ícone: é a linha onde o trabalho aparece todo dia.', 110, 540, 700, 24)}
<div class="box" style="left:900px;top:110px;width:910px;height:860px;background:#0d0f13;overflow:hidden">
 <img src="../assets/simbolo-sol.png" style="position:absolute;left:255px;top:120px;width:400px">
 <div class="hz" style="left:0;right:0;top:342px;height:3px"></div>
 <div class="lab" style="position:absolute;left:40px;top:540px;color:var(--ou)">linha do horizonte = régua do sistema</div>
 <div style="position:absolute;left:40px;right:40px;bottom:40px;display:grid;grid-template-columns:repeat(3,1fr);gap:20px">
 {''.join(f'<div style="height:250px;background:url({T}/{t}.jpg) center/cover"></div>' for t in ['post-frase', 'quadro-q2', 'santinho'])}</div>
</div>''')

# 09 LOGO + ÁREA DE PROTEÇÃO
pg(f'''{tit('07 · Logo', 'Mantido.', 'Protegido.', s=96)}
{txt('O logo atual continua: LEO PINTO, com o sol sobre as águas no lugar do O. Ele ganha regras de luxo: respiro mínimo, tamanho mínimo e um só jeito de aparecer, direto no fundo, sem balão nem placa.<br><br><b style="color:#fff">Área de proteção:</b> a altura do O (x) em volta de todo o logo.<br><b style="color:#fff">Tamanho mínimo:</b> 120 px de largura na tela; 25 mm impresso.', 110, 560, 700, 24)}
<div class="box" style="left:900px;top:110px;width:910px;height:860px;background:#0d0f13">
 <div style="position:absolute;left:150px;top:180px;width:610px;height:500px;outline:2px dashed rgba(255,194,14,.7);outline-offset:0"></div>
 <img src="{logo('branco')}" style="position:absolute;left:235px;top:250px;width:440px">
 {''.join(f'<div class="bc" style="position:absolute;{p};font-size:40px;color:var(--ou)">x</div>' for p in ['left:180px;top:200px', 'left:700px;top:200px', 'left:180px;top:620px', 'left:700px;top:620px'])}
 <div class="lab" style="position:absolute;left:40px;bottom:40px;color:var(--ou)">x = altura do sol · área livre em volta</div>
 <div style="position:absolute;right:40px;bottom:40px;display:flex;align-items:flex-end;gap:30px"><img src="{logo('branco')}" style="width:120px"><span class="lab" style="font-size:14px">mín. 120 px</span></div>
</div>''')

# 10 VERSÕES + PROIBIDOS
vers = [(logo('branco'), 'var(--pr)', 'Principal · sobre preto'), (logo('marinho'), 'var(--la)', 'Sobre laranja · marinho'),
        (logo('preto'), '#F4F2EE', 'Monocromática · carimbo'), (logo('ouro'), 'var(--ma2)', 'Metálica · Amarelo-Sol'),
        ('../assets/simbolo-sol.png', 'var(--pr)', 'Símbolo isolado · avatar')]
proib = ['Balão, placa ou cápsula atrás', 'Esticar ou inclinar', 'Trocar as cores do sol', 'Logo vertical com "LE PINTO"', 'Sombra 3D, raios ou fumaça']
pg(f'''<div class="box" style="left:110px;top:100px"><div class="lab" style="color:var(--ou)">08 · Versões e usos proibidos</div></div>
<div class="box" style="left:110px;top:160px;width:1700px;display:grid;grid-template-columns:repeat(5,1fr);gap:20px">
{''.join(f'<div><div style="height:330px;background:{b};display:flex;align-items:center;justify-content:center"><img src="{s}" style="width:{70 if "simbolo" in s else 82}%"></div><div class="lab" style="font-size:15px;margin-top:14px">{t}</div></div>' for s, b, t in vers)}</div>
<div class="box" style="left:110px;top:600px;width:1700px;display:grid;grid-template-columns:repeat(5,1fr);gap:20px">
{''.join(f'<div><div style="height:250px;background:#15181d;position:relative;display:flex;align-items:center;justify-content:center;overflow:hidden"><img src="{logo("branco")}" style="width:70%;{st}"><div style="position:absolute;inset:0;background:linear-gradient(to top right,transparent 49%,#e33 49.5%,#e33 50.5%,transparent 51%)"></div></div><div class="lab" style="font-size:15px;margin-top:14px;color:#e88">Não · {t}</div></div>' for t, st in zip(proib, ['background:#2350F5;border-radius:60px;padding:20px', 'transform:scaleX(1.5)', 'filter:hue-rotate(160deg)', 'transform:rotate(90deg)', 'filter:drop-shadow(12px 12px 0 #FF7A1A)']))}</div>''')

# 11 CORES
sw = [('laranja', 25), ('preto', 45), ('marinho', 12), ('ouro', 8), ('royal', 5), ('branco', 5)]
def rgb(h): return ', '.join(str(int(h[i:i+2], 16)) for i in (1, 3, 5))
pg(f'''{tit('09 · Cores', 'As cores', 'do partido', s=88)}
{txt('Os códigos são exatamente os do logo e da identidade aprovada: o laranja do Solidariedade é a cor principal, o azul é apoio, o amarelo do sol vira o acento metálico. O luxo vem do preto como base e dos tons profundos das mesmas cores (Laranja Profundo #B4500C e Marinho Noite #021A3D), nunca de cor nova.', 110, 520, 700, 23)}
<div class="box" style="left:880px;top:110px;width:930px;height:120px;display:flex">{''.join(f'<div style="flex:{p};background:{c(k)}"></div>' for k, p in sw)}</div>
<div class="lab box" style="left:880px;top:245px;font-size:15px">Proporção: preto 45 · laranja 25 · marinho 12 · amarelo-sol 8 · royal 5 · branco 5</div>
<div class="box" style="left:880px;top:300px;width:930px;display:grid;grid-template-columns:repeat(4,1fr);gap:18px">
{''.join(f'<div style="background:#111418"><div style="height:150px;background:{COR[k][0]};{"outline:1px solid #333" if k=="preto" else ""}"></div><div style="padding:16px"><div class="ci" style="font-size:20px;font-weight:900">{COR[k][1]}</div><div style="font:600 15px/1.6 Mont;color:#cfcac2;margin-top:6px">{COR[k][0]}<br>RGB {rgb(COR[k][0])}<br><span style="color:var(--ou)">{COR[k][2]}</span></div></div></div>' for k in COR)}</div>''')

# 12 TIPOGRAFIA
pg(f'''{tit('10 · Tipografia', 'Romana de', 'autoridade', s=88)}
<div class="box" style="left:880px;top:110px;width:930px">
 <div style="border-top:1px solid rgba(255,255,255,.2);padding:24px 0"><div class="lab" style="color:var(--la)">Títulos · Cinzel 700/900</div><div class="ci" style="font-size:96px;font-weight:900;margin-top:14px">Palavra dada</div><div style="font:400 19px Mont;color:#999;margin-top:8px">Capitulares romanas, de inscrição em pedra: peso institucional, sem delicadeza.</div></div>
 <div style="border-top:1px solid rgba(255,255,255,.2);padding:24px 0"><div class="lab" style="color:var(--la)">Manchetes e rótulos · Barlow Condensed 600/800</div><div class="bc" style="font-size:120px;margin-top:14px">Presença que resolve</div></div>
 <div style="border-top:1px solid rgba(255,255,255,.2);padding:24px 0"><div class="lab" style="color:var(--la)">Texto · Montserrat 400/600 (a família do logo)</div><div style="font:400 26px/1.5 Mont;margin-top:14px">Fui ao povoado, vi, registrei e voltei para mostrar o que ficou pronto.</div></div>
 <div style="font:400 18px/1.6 Mont;color:#999">Fora: Kaushan Script, caligrafia, itálico decorativo e serifas finas. Todas gratuitas (Google Fonts, OFL).</div>
</div>''')

# 13 GRID
pg(f'''{tit('11 · Grid', 'Retas,', 'peso, margem', s=88)}
{txt('Grid de 6 colunas com margem de 60 px no 4:5 (1080×1350) e 70 px no 9:16. Foto ocupa de 50 a 70% da peça e nunca fica sob o texto. O fio do horizonte sempre alinhado às colunas. Duas regras de composição: <b style="color:#fff">lateral</b> (texto numa metade, Leo na outra) e <b style="color:#fff">eixo</b> (simetria central, para frase e evento).', 110, 540, 700, 23)}
<div class="box" style="left:950px;top:90px;width:720px;height:900px;background:url({T}/post-manchete.jpg) center/cover">
 <div style="position:absolute;inset:40px;display:grid;grid-template-columns:repeat(6,1fr);gap:16px">{''.join('<div style="background:rgba(255,122,26,.16);border-left:1px solid rgba(255,122,26,.6);border-right:1px solid rgba(255,122,26,.6)"></div>' for _ in range(6))}</div>
 <div style="position:absolute;inset:40px;outline:2px solid var(--ou)"></div></div>''')

# 14 FOTO
pg(f'''<img class="foto" src="{foto('a-close-laranja')}" style="left:-120px;bottom:0;width:1100px">
<div class="box" style="left:0;top:0;bottom:0;width:900px;background:linear-gradient(90deg,transparent 60%,var(--pr))"></div>
{tit('12 · Direção de foto', 'Retrato de', 'liderança', x=980, s=88)}
{txt('<b style="color:#fff">Luz:</b> contraluz duro e lateral, fundo escuro, um brilho laranja atrás (o sol do logo).<br><b style="color:#fff">Pose:</b> olhar firme na câmera, braços cruzados, punho, mão que aponta o caminho; nada de pose fofa.<br><b style="color:#fff">Roupa:</b> camisa social escura ou terno sem gravata em eventos; polo do partido na rua.<br><b style="color:#fff">Cena:</b> o Leo no meio do povo, como líder: na obra, no povoado, no campo.<br><b style="color:#fff">Tratamento:</b> contraste +14%, saturação −8%, grão leve; sempre recortado, nunca a foto inteira.<br><br><span style="color:var(--ou)">Próxima sessão (pedido ao Leo): retrato de estúdio com camisa escura e contraluz, e fotos reais de rua com moradores. As fotos deste manual são do acervo e servem só para demonstrar o sistema.</span>', 980, 520, 840, 22)}''')

# 15 REDES
pg(f'''<div class="box" style="left:110px;top:100px"><div class="lab" style="color:var(--ou)">13 · Redes · templates</div><div class="ci" style="font-size:54px;font-weight:900;margin-top:20px">Post, carrossel,<br><span style="color:var(--la)">story e Reels</span></div></div>
{tela(T+'/post-manchete.jpg', 110, 420, 270, -4)}{tela(T+'/post-laranja.jpg', 420, 380, 270, 0)}
<div class="box" style="left:840px;top:150px;width:1000px;display:grid;grid-template-columns:repeat(3,1fr);gap:14px">{''.join(f'<img src="{T}/carrossel-{i}.jpg" style="width:100%">' for i in (1, 2, 3))}</div>
<div class="lab box" style="left:840px;top:590px;font-size:15px">Carrossel: capa · número em contorno · chamada (cada tela muda a composição)</div>
<div class="box" style="left:840px;top:650px;display:flex;gap:14px">{''.join(f'<img src="{T}/{t}.jpg" style="height:330px">' for t in ('story', 'reels', 'post-frase'))}</div>''')

# 16 QUADROS
pg(f'''<div class="box" style="left:110px;top:100px"><div class="lab" style="color:var(--ou)">14 · Os 4 quadros semanais</div><div class="ci" style="font-size:66px;font-weight:900;margin-top:20px">Uma semana, <span style="color:var(--la)">quatro encontros</span></div></div>
<div class="box" style="left:110px;top:330px;width:1700px;display:grid;grid-template-columns:repeat(4,1fr);gap:22px">
{''.join(f'<div><img src="{T}/quadro-{q}.jpg" style="width:100%;box-shadow:0 30px 60px rgba(0,0,0,.6)"><div class="lab" style="font-size:16px;margin-top:16px">{d}</div></div>' for q, d in [('q1', 'Seg · Leo no Povoado'), ('q2', 'Ter · Pediu? Tá Feito.'), ('q3', 'Qui · Olho de Engenheiro'), ('q4', 'Sex · Gente da Baixada')])}</div>''')

# 17 FEED XADREZ
ordem = ['quadro-q1', 'post-manchete', 'post-laranja', 'quadro-q2', 'carrossel-3', 'post-frase', 'quadro-q3', 'carrossel-1', 'quadro-q4']
pg(f'''{tit('15 · Feed', 'Xadrez de', 'laranja e preto', s=80)}
{txt('Laranja e escuro alternam em toda a grade; nunca dois posts seguidos na mesma composição. Foto real em todas, logo sempre aplicado direto, fio do horizonte como assinatura.', 110, 540, 640, 23)}
<div class="box" style="left:900px;top:70px;width:760px;background:#000;padding:26px;box-shadow:0 40px 90px rgba(0,0,0,.7)">
 <div style="display:flex;align-items:center;gap:24px;margin-bottom:22px"><img src="{T}/avatar.jpg" style="width:110px;border-radius:50%"><div><div style="font:800 26px Mont">Leo Pinto</div><div style="font:400 18px/1.5 Mont;color:#aaa">Vereador · São João Batista/MA<br>Presença que resolve.</div></div></div>
 <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:4px">{''.join(f'<div style="aspect-ratio:4/5;background:url({T}/{o}.jpg) center/cover"></div>' for o in ordem)}</div></div>''')

# 18 BIO / PÁGINA
pg(f'''{tit('16 · Bio e página', 'Link da bio', 'no padrão premium', s=80)}
{txt('Página de bio (arquivo bio.html no pacote): primeira dobra com retrato, nome e assinatura; depois os 4 quadros, prestação de contas e contato do gabinete. Mesmo preto, mesmo laranja e o mesmo avatar do Instagram, como manda a regra de todos os canais.', 110, 540, 680, 23)}
{tela('../entregas/bio-celular.jpg', 980, 90, 380, 0)}{tela(T+'/story.jpg', 1420, 180, 330, 3)}''')

# 19 MOTION
pg(f'''{tit('17 · Assinatura em movimento', 'Vinheta', 'do logo', s=80)}
{txt('6 segundos, com som: escuro total → o fio do horizonte se abre (whoosh) → o sol nasce atrás da linha (grave) → LEO PINTO entra firme → "Presença que resolve" (impacto). Usar no início e no fim de todo Reels. Arquivo: leo-vinheta.mp4.', 110, 540, 680, 23)}
<div class="box" style="left:900px;top:110px;width:910px;display:grid;grid-template-columns:1fr 1fr;gap:16px">{''.join(f'<div style="position:relative"><img src="../entregas/motion/q{i}.jpg" style="width:100%"><div class="lab" style="position:absolute;left:12px;top:12px;font-size:14px">{t}</div></div>' for i, t in enumerate(['0,5 s', '1,5 s', '3 s', '5 s']))}</div>''')

# 20 CAMPANHA E PAPELARIA (mockups)
pg(f'''<div class="box" style="inset:0;background:radial-gradient(circle at 50% 40%,#2a2d33,#08090c 70%)"></div>
<div class="box" style="left:110px;top:90px"><div class="lab" style="color:var(--ou)">18 · Campanha e papelaria</div></div>
<div class="box" style="left:140px;top:250px;transform:perspective(1600px) rotateX(38deg) rotateZ(-18deg);box-shadow:30px 50px 60px rgba(0,0,0,.7)"><img src="{T}/timbrado.jpg" style="width:520px;display:block"></div>
<div class="box" style="left:760px;top:430px;transform:perspective(1600px) rotateX(38deg) rotateZ(12deg);box-shadow:20px 40px 50px rgba(0,0,0,.7)"><img src="{T}/cartao-frente.jpg" style="width:440px;display:block"></div>
<div class="box" style="left:820px;top:200px;transform:perspective(1600px) rotateX(38deg) rotateZ(-6deg);box-shadow:20px 40px 50px rgba(0,0,0,.7)"><img src="{T}/cartao-verso.jpg" style="width:440px;display:block"></div>
<div class="box" style="left:1330px;top:180px;transform:perspective(1600px) rotateX(30deg) rotateZ(8deg);box-shadow:20px 40px 50px rgba(0,0,0,.7)"><img src="{T}/santinho.jpg" style="width:300px;display:block"></div>
<div class="box" style="left:1420px;top:560px;transform:rotate(-8deg)"><div style="width:20px;height:120px;margin:0 auto;background:linear-gradient(#FF7A1A,#B4500C)"></div><img src="{T}/cracha.jpg" style="width:260px;display:block;border-radius:14px;box-shadow:20px 40px 50px rgba(0,0,0,.7)"></div>
<div class="lab box" style="left:110px;bottom:90px;font-size:16px">Papel timbrado · cartão (frente e verso) · cartão de mandato · crachá da equipe · renders digitais, nomes ilustrativos</div>''')

# 21 CAMISETA
pg(f'''<div class="box" style="inset:0;background:radial-gradient(circle at 50% 40%,#2a2d33,#08090c 70%)"></div>
{tit('18 · Fardamento', 'Equipe', 'na rua', s=80)}
{txt('Camiseta preta com o logo branco no peito e o fio do horizonte; equipe de rua com polo laranja do partido e o logo marinho. Bordado no peito esquerdo em peças sociais.', 110, 540, 600, 23)}
<div class="box" style="left:900px;top:120px;width:820px;height:840px">
<svg viewBox="0 0 820 840" style="position:absolute;inset:0;filter:drop-shadow(0 50px 60px rgba(0,0,0,.8))"><defs><linearGradient id="g" x1="0" x2="1"><stop offset="0" stop-color="#1b1d22"/><stop offset=".5" stop-color="#0c0d10"/><stop offset="1" stop-color="#18191d"/></linearGradient></defs>
<path d="M260 40 Q410 110 560 40 L800 160 L720 360 L640 320 L640 820 L180 820 L180 320 L100 360 L20 160 Z" fill="url(#g)"/><path d="M260 40 Q410 110 560 40 Q410 150 260 40Z" fill="#000"/></svg>
<img src="{T}/camiseta.png" style="position:absolute;left:260px;top:220px;width:300px"></div>''')

# 22 OUTDOOR E EVENTO
pg(f'''<div class="box" style="inset:0;background:linear-gradient(#0c1a33,#3b2412 70%,#120c08)"></div>
<div class="box" style="left:0;right:0;bottom:0;height:260px;background:linear-gradient(#1a120c,#050505)"></div>
<div class="box" style="left:180px;top:120px;width:1080px;height:360px;padding:10px;background:#111;box-shadow:0 40px 80px rgba(0,0,0,.8)"><img src="{T}/outdoor.jpg" style="width:100%;height:100%;display:block"></div>
<div class="box" style="left:420px;top:490px;width:16px;height:340px;background:#1a1a1a"></div><div class="box" style="left:1000px;top:490px;width:16px;height:340px;background:#1a1a1a"></div>
<div class="box" style="left:1330px;top:300px;width:500px;transform:perspective(1200px) rotateY(-24deg);box-shadow:0 40px 80px rgba(0,0,0,.8)"><img src="{T}/banner.jpg" style="width:100%;display:block"></div>
<div class="box" style="left:110px;top:60px"><div class="lab" style="color:var(--ou)">19 · Outdoor e banner de evento</div></div>
<div class="lab box" style="left:110px;bottom:90px;font-size:16px">Outdoor 9×3 m · painel de palco "Prestação de contas" · renders digitais</div>''')

# 23 QUEM CONSTRUIU
ag = [('Marty Neumeier', 'brand-squad', 'Onliness: "o único vereador engenheiro que volta para mostrar a obra" virou o posicionamento.'),
      ('Alina Wheeler', 'brand-squad', 'Processo em 5 fases e o manual: logo mantido, área de proteção, versões, usos proibidos.'),
      ('David Aaker', 'brand-squad', 'Identidade essencial (presença) e estendida (engenheiro, Baixada, parceria).'),
      ('Archetype Consultant', 'brand-squad', 'Governante + Cara Comum: autoridade sem distância.'),
      ('Brand Chief', 'brand-squad', 'Ordem: estratégia antes do desenho; manter o logo e as cores do partido.'),
      ('Design Chief · Brad Frost', 'design-squad', 'Sistema em átomos: fio do horizonte, 2 composições, 4 quadros como componentes.'),
      ('Donald Miller', 'marketing-squad', 'O povo é o herói, o Leo é o guia; assinatura de 3 palavras.'),
      ('Copy Chief', 'copy-squad', 'Frases curtas com verbo de ação; "Palavra dada, obra feita."'),
      ('Marshall Ganz · Story Chief', 'storytelling', 'Narrativa pública: eu (engenheiro), nós (a Baixada), agora (o mandato).'),
      ('Manifestador', 'movement', 'Manifesto curto: "Presença não é aparecer. É voltar."'),
      ('Hormozi Content', 'hormozi-squad', 'Prova antes de promessa: cada post é uma entrega com data.'),
      ('Vision Chief', 'c-level-squad', 'Marca de mandato de 4 anos, não de eleição de 1 dia.'),
      ('Maquiavel', 'agente', 'Imagem pública (Príncipe XVIII e XXI): parecer firme e cumprir; aliado da gestão, nunca crítico.'),
      ('Designer gráfico', 'agente', 'Pesquisa premium, composição copiada e conferência a 360 px.'),
      ('Social media', 'agente', 'Feed em xadrez, horários dos quadros e legenda SEO.'),
      ('Webdesigner + /landing-page', 'agente e skill', 'Bio com primeira dobra premium e ordem das seções.'),
      ('/reels-viral e /repurposing', 'skills', 'Vinheta de 6 s no início, gancho em 2 s; 1 quadro vira Reels, carrossel e Stories.')]
pg(f'''<div class="box" style="left:110px;top:90px"><div class="lab" style="color:var(--ou)">20 · Quem construiu</div><div class="ci" style="font-size:60px;font-weight:900;margin-top:16px">Todos os agentes, <span style="color:var(--la)">uma marca</span></div></div>
<div class="box" style="left:110px;top:290px;width:1700px;columns:2;column-gap:60px">{''.join(f'<div style="break-inside:avoid;border-top:1px solid rgba(255,255,255,.15);padding:11px 0;display:grid;grid-template-columns:300px 1fr;gap:20px"><div><div class="ci" style="font-size:19px;font-weight:900;text-transform:none">{a}</div><div class="lab" style="font-size:12px;color:var(--la);margin-top:4px">{s}</div></div><div style="font:400 17px/1.45 Mont;color:#cfcac2">{t}</div></div>' for a, s, t in ag)}</div>''')

# 24 REFERÊNCIAS
refs = [('01-obama-hope-us', 'Obama "Hope" · EUA', 'retrato de liderança + 1 palavra'), ('15-rolex-ch', 'Rolex · Suíça', 'cor de marca absoluta e serifa de autoridade'),
        ('17-astonmartin-uk', 'Aston Martin · Reino Unido', 'preto profundo, retas, foto dramática')]
pg(f'''<div class="box" style="left:110px;top:90px"><div class="lab" style="color:var(--ou)">21 · Referências · as 3 combinadas</div><div class="ci" style="font-size:60px;font-weight:900;margin-top:16px">Copiar a composição, <span style="color:var(--la)">nunca o layout</span></div></div>
<div class="box" style="left:110px;top:300px;width:1700px;display:grid;grid-template-columns:repeat(3,1fr);gap:26px">{''.join(f'<div><div style="height:360px;background:url({R}/{f}.jpg) top/cover;outline:1px solid #333"></div><div class="ci" style="font-size:26px;font-weight:900;margin-top:18px;text-transform:none">{t}</div><div style="font:400 19px Mont;color:#cfcac2;margin-top:6px">{d}</div></div>' for f, t, d in refs)}</div>
{txt('Pesquisa completa (16 capturas, 8 países: EUA, França, Portugal, Brasil, Reino Unido, Suíça, Alemanha, Itália) em TEMPLATE.md: Obama 2008 (Sol Sender), Ocasio-Cortez 2018 (Tandem), Macron 2017, Mayor of London, Porto. (White Studio), Pentagram, Collins, Tom Ford, Ralph Lauren, Behance de campanha política.', 110, 860, 1700, 19)}''')

# 25 RESUMO
pg(f'''<div class="box" style="left:110px;top:90px"><div class="lab" style="color:var(--ou)">22 · Resumo de 1 página</div></div>
<div class="box" style="left:110px;top:160px;width:1700px;display:grid;grid-template-columns:1.1fr 1fr 1fr;gap:50px">
<div><img src="{logo('branco')}" style="width:420px"><div class="bc" style="font-size:60px;margin-top:30px">Presença que <span style="color:var(--la)">resolve.</span></div>
<div style="display:flex;margin-top:40px;height:70px">{''.join(f'<div style="flex:{p};background:{c(k)};{"outline:1px solid #333" if k=="preto" else ""}"></div>' for k, p in sw)}</div>
<div style="font:600 15px/1.8 Mont;color:#cfcac2;margin-top:12px">#08090C preto · #FF7A1A laranja · #05316E marinho · #FFC20E amarelo-sol · #2350F5 royal · #F4F2EE branco</div></div>
<div><div class="lab" style="color:var(--la)">Sempre</div><div style="font:400 20px/1.8 Mont;color:#eee;margin-top:12px">Cinzel nos títulos, Barlow Condensed nas manchetes, Montserrat no texto · fio do horizonte em amarelo-sol · preto de base e xadrez com laranja · foto real recortada, luz de cinema · logo direto no fundo · fato com data e lugar · parceria com a Prefeitura</div></div>
<div><div class="lab" style="color:#e88">Nunca</div><div style="font:400 20px/1.8 Mont;color:#eee;margin-top:12px">balão atrás do logo · raios, faixas, ícones, fumaça, sol desenhado · script ou caligrafia · cor fora do partido · promessa ou número sem fonte · pedir voto, número de urna ou 2028 · crítica à gestão · "bairro" (é povoado) · foto repetida</div></div></div>''')

# 26 CONTRACAPA
pg(f'''<div class="box" style="inset:0;background:radial-gradient(circle at 50% 50%,rgba(255,122,26,.35),transparent 50%)"></div>
<img src="{logo('branco')}" class="box" style="left:50%;top:44%;transform:translate(-50%,-50%);width:620px">
<div class="lab box" style="left:0;right:0;bottom:120px;text-align:center;font-size:18px">Identidade v2 · novembro de 2026 · Agência Lindson Almeida · São Luís · MA</div><div class="vin"></div>''', n=False)

html = f'<!doctype html><html lang="pt-BR"><meta charset="utf-8"><title>Leo Pinto · Identidade v2</title><style>{CSS}.pg{{position:relative;width:1920px;height:1080px;overflow:hidden;page-break-after:always}}</style>' + '\n'.join(pgs)
open('book.html', 'w').write(html)
print(len(pgs), 'paginas')
