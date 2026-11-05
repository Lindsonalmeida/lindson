# v15.1 (05/11): o Lindson gostou das que têm imagem (s01, s04, s08, s09) → as outras 6 ganharam paisagem real da Baixada com véu da cor, mantendo a composição.
# v15 · Leo Pinto · 10 artes de saudação + correções de "situação" (conta Leandro, 05/11/2026)
# Pedidos do Lindson (05/11): "crie só 10 artes de saudação" e, depois da Bruna (equipe do Leo) vetar o 31/12
# ("vai dar margem para baterem no prefeito"): "refaça todos os conteúdos, visando que ele é situação".
# Regras: padrão aprovado v13 v3 + kit das datas v14 (gerar9.py): Anton/Montserrat/Kaushan, laranja e azul em xadrez,
# assinatura fixa (@ no topo, logo na base), sem raios, faixas, ícones, fumaça ou sol desenhado; foto de banco só com véu da cor.
# Fotos: as 7 fotos livres do álbum do Leo não estão nesta máquina, então as saudações usam só tipografia e paisagens reais
# da Baixada Maranhense (Wikimedia Commons, CC BY-SA, crédito na arte e na legenda: assets/banco/creditos.json).
# Situação: nada de "demanda", "o que falta", "o que precisa", "cobrar", "fiscalizar": só celebrar, agradecer, convidar e somar.
# Uso: python3 gerar.py <pasta com assets/ e originais/>  →  artes.html ;  node ../instagram-v14-datas/render.js <pasta>
import sys, json, re, os
d = sys.argv[1]
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../instagram-v14-datas/gerar9.py')).read()
kit = src[:src.index('P = []')]
_argv = sys.argv; sys.argv = ['gerar9', d]
exec(kit)  # MAR, ROY, SOL, LAR, GRAO, AMARELO, AZUL, mapa(), ASSINA(), cx(), H, GRAD
import ast as _ast  # GLASS, CHIP, MESH_AZUL e MESH_LAR ficam no meio dos posts do gerar9: pega só essas atribuições
for _n in _ast.parse(src).body:
    if isinstance(_n, _ast.Assign) and getattr(_n.targets[0], 'id', '') in ('GLASS', 'CHIP', 'MESH_AZUL', 'MESH_LAR', 'H', 'GRAD'):
        exec(_ast.get_source_segment(src, _n))
sys.argv = _argv
head = src[src.index('html = f"""') + 11:src.index('</style>')] + '</style>'
head = eval('f"""' + head + '"""')
CRED = json.load(open(f'{d}/assets/banco/creditos.json'))
def credito(arq, cor='rgba(255,255,255,.75)'):
    c = CRED[arq]; return f'<div class="a" style="right:40px;bottom:26px;font:600 13px Montserrat;color:{cor};letter-spacing:.04em">Foto: {c["autor"]} · Wikimedia Commons · {c["licenca"]}</div>'
def fundo_foto(arq, pos='50% 50%', veu=ROY, op=.55, extra=''):
    return (f'<img class="a" src="assets/banco/{arq}" style="inset:0;width:1080px;height:1350px;object-fit:cover;object-position:{pos};{extra}">'
            f'<div class="a" style="inset:0;background:{veu};mix-blend-mode:multiply;opacity:{op}"></div>')
def op(n, t): return f'<div class="op"><b>{n}</b>{t}</div>'
P = []

# 1 · BOM DIA (segunda) · AZUL · paisagem real com véu + título condensado gigante (Engenharia reversa Designi/Behance itens 1 e 4; Designi "vereador social media", captura referencias/v1.jpg)
P.append(('s01-bom-dia-segunda', AZUL, f"""{fundo_foto('barcos-baixada-maranhense5-jpg.jpg', '50% 60%', '#0B2A8A', .50)}
<div class="a" style="inset:0;background:linear-gradient(180deg,rgba(7,26,85,0) 30%,rgba(7,26,85,.85) 78%)"></div>
<div class="a" style="left:80px;top:180px">{CHIP('Segunda-feira', MAR, '#FFC20E')}</div>
<div class="a" style="left:72px;top:690px">{H('Bom dia,', 190, '#fff', 'text-shadow:0 10px 30px rgba(0,0,0,.35)')}</div>
<div class="a" style="left:76px;top:860px">{H('São João Batista!', 104, '#fff', GRAD + ';padding-top:.2em;margin-top:-.2em')}</div>
<div class="a K" style="left:80px;top:985px;font-size:52px;color:#fff">que a semana comece com fé e trabalho</div>
{credito('barcos-baixada-maranhense5-jpg.jpg')}"""))

# 2 · BOA SEMANA · LARANJA · enquete leve: cópia do Designi "Bom início de semana · Como foi seu fim de semana?" (captura referencias/d31.jpg), emojis trocados por letras
P.append(('s02-boa-semana-enquete', AZUL, f"""{fundo_foto('barcos-baixada-maranhense4-jpg.jpg', '50% 50%', '#E8590C', 0.62, '')}<div class="a" style="inset:0;background:linear-gradient(180deg,rgba(150,50,0,.55),rgba(150,50,0,.2) 45%,rgba(150,50,0,.6))"></div>{mapa(560, 160, 620, '#FFFFFF', .22)}
<div class="a" style="left:80px;top:190px;width:900px">{H('Bom início', 150, '#fff', 'text-shadow:0 8px 24px rgba(120,40,0,.3)')}
 <div class="K" style="font-size:96px;color:#FFE066;margin:-6px 0 0 6px">de semana!</div>
 <div class="B" style="font-size:44px;color:#fff;margin-top:26px;line-height:1.1;text-transform:none;letter-spacing:-.01em">Como foi o seu<br>fim de semana?</div></div>
<div class="a" style="left:80px;top:720px;width:640px;display:flex;flex-direction:column;gap:16px">
 {''.join(f'<div class="op" style="background:#fff;border-color:#fff;box-shadow:0 20px 34px -22px rgba(120,40,0,.7)"><b>{n}</b>{t}</div>' for n, t in zip('ABC', ['Descansei com a família', 'Trabalhei bastante', 'Fui à missa ou ao culto']))}</div>
<div class="a K" style="right:80px;top:1060px;font-size:46px;color:#fff;text-align:right">comenta a letra<br>aqui embaixo</div>{credito('barcos-baixada-maranhense4-jpg.jpg')}"""))

# 3 · BOM DIA · AZUL · enquete do café: cópia do Designi "Enquete · Você prefere o seu café" (cartão branco com cabeçalho e opções, referencias/d31.jpg)
P.append(('s03-bom-dia-cafe', AZUL, f"""{fundo_foto('matinha-maranh-o-jpg.jpg', '50% 40%', '#0B2A8A', 0.62, '')}<div class="a" style="inset:0;background:linear-gradient(180deg,rgba(7,26,85,.7),rgba(7,26,85,.25) 40%,rgba(7,26,85,.75))"></div>{mapa(-200, 700, 760, '#BFD8FF', .25)}
<div class="a" style="left:0;width:1080px;top:180px;text-align:center"><div class="L" style="font-size:22px;color:#FFC20E">bom dia, Baixada</div>
 {H('No café da manhã', 104, '#fff', 'margin-top:14px')}<div style="margin-top:8px">{cx('você prefere?', '#FFC20E', MAR, 66, 'font-family:Anton;letter-spacing:.01em')}</div></div>
<div class="a" style="left:170px;top:560px;width:740px;background:#fff;border-radius:36px;overflow:hidden;box-shadow:0 40px 70px -30px rgba(2,12,50,.7)">
 <div class="H" style="background:{LAR};color:#fff;text-align:center;font-size:50px;padding:18px 0 14px">Enquete do dia</div>
 <div style="padding:26px 34px 30px;display:flex;flex-direction:column;gap:14px">{op(1, 'Cuscuz com ovo')}{op(2, 'Tapioca')}{op(3, 'Pão com manteiga')}{op(4, 'Mingau')}</div></div>
<div class="a" style="left:0;width:1080px;top:1095px;text-align:center"><span class="K" style="font-size:48px;color:#fff">comenta o número do seu favorito</span></div>{credito('matinha-maranh-o-jpg.jpg')}"""))

# 4 · BOA TARDE · LARANJA · dois postais inclinados: cópia do Designi "Praia ou montanha?" (fotos em moldura branca inclinadas + pergunta, referencias/d31.jpg)
def postal(arq, x, y, rot, pos='50% 50%'):
    return (f'<div class="a" style="left:{x}px;top:{y}px;width:430px;background:#fff;padding:16px 16px 60px;transform:rotate({rot}deg);box-shadow:0 30px 50px -24px rgba(90,30,0,.6)">'
            f'<img src="assets/banco/{arq}" style="display:block;width:398px;height:430px;object-fit:cover;object-position:{pos}"></div>')
P.append(('s04-boa-tarde-postais', AMARELO, f"""
<div class="a" style="left:0;width:1080px;top:150px;text-align:center">{H('Boa tarde!', 170, '#fff', 'text-shadow:0 8px 24px rgba(120,40,0,.3)')}
 <div class="K" style="font-size:56px;color:{MAR};margin-top:6px">um pedacinho da nossa Baixada</div></div>
{postal('barcos-baixada-maranhense-jpg.jpg', 90, 470, -6, '45% 60%')}{postal('lago-de-viana-1-jpg.jpg', 560, 500, 5, '50% 55%')}
<div class="a" style="left:0;width:1080px;top:1010px;text-align:center">{cx('qual é a sua paisagem favorita?', MAR, '#fff', 40)}</div>
<div class="a" style="right:40px;bottom:26px;font:600 12px Montserrat;color:rgba(5,49,110,.8);text-align:right;line-height:1.5">Fotos: {CRED['barcos-baixada-maranhense-jpg.jpg']['autor']} e {CRED['lago-de-viana-1-jpg.jpg']['autor']}<br>Wikimedia Commons · CC BY-SA 4.0</div>"""))

# 5 · BOA NOITE · MARINHO · minimalismo premium (linguagem v14.4 aprovada) + mapa oficial do padrão v13 v3
MARINHO = f'radial-gradient(900px 800px at 70% 20%,#1C3FA8 0,#0B2470 45%,#04123F 100%)'
P.append(('s05-boa-noite', MARINHO, f"""{fundo_foto('apa-baixada-maranhense-jpg.jpg', '40% 50%', '#04123F', 0.55, '')}<div class="a" style="inset:0;background:linear-gradient(90deg,rgba(4,18,63,.85),rgba(4,18,63,.2) 75%)"></div>{mapa(300, 360, 900, '#9DB8FF', .30)}
<div class="a" style="left:80px;top:300px">{H('Boa', 230, '#fff')}</div>
<div class="a K" style="left:96px;top:520px;font-size:200px;color:#FFC20E;line-height:1">noite</div>
<div class="a" style="left:86px;top:830px;width:560px;font:600 34px/1.35 Montserrat;color:#DCE6FF">Descansa, que amanhã tem mais trabalho, mais encontro e mais São João Batista.</div>{credito('apa-baixada-maranhense-jpg.jpg')}"""))

# 6 · BOM FIM DE SEMANA · AZUL · cópia do Designi "Qual a marca da sua primeira bike? · Conta pra gente!" (palavra gigante atrás + cartão com lista numerada, referencias/d31.jpg)
P.append(('s06-fim-de-semana', AZUL, f"""{fundo_foto('barcos-baixada-maranhense2-jpg.jpg', '50% 50%', '#0B2A8A', 0.6, '')}<div class="a" style="inset:0;background:linear-gradient(180deg,rgba(7,26,85,.75),rgba(7,26,85,.2) 40%,rgba(7,26,85,.8))"></div>
<div class="a" style="left:-40px;top:900px;width:1160px;text-align:center">{H('Sábado', 380, 'rgba(255,255,255,.14)', 'line-height:.8')}</div>
<div class="a" style="left:0;width:1080px;top:160px;text-align:center"><div class="L" style="font-size:22px;color:#FFC20E">bom fim de semana!</div>
 {H('O que não pode faltar', 88, '#fff', 'margin-top:12px')}<div style="margin-top:6px">{cx('no seu fim de semana?', '#FFC20E', MAR, 58, 'font-family:Anton;letter-spacing:.01em')}</div></div>
<div class="a" style="left:150px;top:500px;width:780px;background:#fff;border-radius:36px;overflow:hidden;box-shadow:0 40px 70px -30px rgba(2,12,50,.7)">
 <div class="H" style="background:{LAR};color:#fff;text-align:center;font-size:52px;padding:18px 0 14px">Conta pra gente!</div>
 <div style="padding:26px 34px 30px;display:flex;flex-direction:column;gap:14px">{op(1, 'Família reunida')}{op(2, 'Futebol com os amigos')}{op(3, 'Banho de rio')}{op(4, 'Almoço de domingo')}</div></div>
<div class="a" style="left:0;width:1080px;top:1085px;text-align:center"><span class="K" style="font-size:48px;color:#fff">comenta o número</span></div>{credito('barcos-baixada-maranhense2-jpg.jpg')}"""))

# 7 · BOM DIA · LARANJA · palavra repetida empilhada: cópia do modelo "SOU PEDRO" enviado pelo Lindson (referencias/modelo-natal-sou-pedro.png), sem a pessoa
contorno = '-webkit-text-stroke:3px rgba(255,255,255,.85);color:transparent'
P.append(('s07-bom-dia-repetido', AZUL, f"""{fundo_foto('cria-o-de-b-falos-rio-pericum-panoramio-.jpg', '38% 50%', '#E8590C', 0.5, 'transform:scale(1.08);transform-origin:30% 40%')}<div class="a" style="inset:0;background:linear-gradient(180deg,rgba(150,50,0,.7),rgba(150,50,0,.1) 55%,rgba(150,50,0,.75))"></div>
<div class="a" style="left:60px;top:150px;line-height:.86">
 {H('Bom dia', 250, '#fff', 'text-shadow:0 10px 30px rgba(120,40,0,.3)')}
 {H('Bom dia', 250, '', contorno)}
 {H('Bom dia', 250, '', contorno + ';opacity:.55')}</div>
<div class="a" style="left:70px;top:850px">{cx('São João Batista', MAR, '#fff', 64, 'font-family:Anton;letter-spacing:.01em')}</div>
<div class="a K" style="left:80px;top:960px;font-size:56px;color:#FFE066">acordou com coragem? bora!</div>{credito('cria-o-de-b-falos-rio-pericum-panoramio-.jpg')}"""))

# 8 · BOM DIA · LARANJA→paisagem · frase de impacto sobre foto real com véu da cor: cópia da composição do Designi "Consciência Negra" (texto empilhado sobre retrato/paisagem duotone, referencias/d20.jpg)
P.append(('s08-bom-dia-pescadores', AZUL, f"""{fundo_foto('pescadores-rio-pericum-panoramio-jpg.jpg', '40% 50%', LAR, .55, 'transform:scale(1.06);transform-origin:30% 40%')}
<div class="a" style="inset:0;background:linear-gradient(90deg,rgba(120,40,0,.75),rgba(120,40,0,0) 70%)"></div>
<div class="a" style="left:80px;top:230px;width:760px">
 <div class="K" style="font-size:70px;color:#FFE066">bom dia para quem</div>
 {H('acorda cedo', 140, '#fff', 'margin-top:10px')}{H('e faz a nossa', 140, '#fff')}{H('Baixada', 160, '#fff', GRAD + ';padding-top:.2em;margin-top:-.2em')}
 <div style="margin-top:26px">{CHIP('pescador · lavrador · comerciante · professor', '#fff', 'rgba(5,49,110,.85)')}</div></div>
{credito('pescadores-rio-pericum-panoramio-jpg.jpg')}"""))

# 9 · BOA TARDE · AZUL · bento grid (linguagem v14.4 aprovada: "bento grid"): 4 blocos, uma foto real, saudação, lugar e frase
P.append(('s09-boa-tarde-bento', MESH_AZUL, f"""
<div class="bento" style="left:70px;top:150px;width:520px;height:600px;border-radius:30px"><img src="assets/banco/igarap-do-engenho-jpg.jpg" style="width:100%;height:100%;object-fit:cover;object-position:40% 50%"></div>
<div class="bento" style="left:610px;top:150px;width:400px;height:290px;border-radius:30px;background:#FFC20E;display:grid;place-items:center">{H('Boa', 150, MAR)}</div>
<div class="bento" style="left:610px;top:460px;width:400px;height:290px;border-radius:30px;background:#fff;display:grid;place-items:center">{H('tarde!', 140, ROY)}</div>
<div class="bento" style="left:70px;top:770px;width:940px;height:240px;border-radius:30px;{GLASS};padding:34px 40px">
 <div class="L" style="font-size:20px;color:#FFC20E">São João Batista • Maranhão</div>
 <div class="K" style="font-size:62px;color:#fff;margin-top:14px">um café, uma boa conversa e bora que a tarde é nossa</div></div>
<div class="a" style="right:40px;bottom:26px;font:600 13px Montserrat;color:rgba(255,255,255,.75)">Foto: {CRED['igarap-do-engenho-jpg.jpg']['autor']} · Wikimedia Commons · {CRED['igarap-do-engenho-jpg.jpg']['licenca']}</div>"""))

# 10 · BOA SEMANA (domingo à noite) · LARANJA · o padrão aprovado v13 v3: nome em blocos de cor, rótulo espaçado, frase empilhada, Kaushan e mapa
P.append(('s10-boa-semana-blocos', AZUL, f"""{fundo_foto('barcos-baixada-maranhense3-jpg.jpg', '50% 50%', '#E8590C', 0.6, '')}<div class="a" style="inset:0;background:linear-gradient(90deg,rgba(150,50,0,.8),rgba(150,50,0,.15) 80%)"></div>{mapa(420, 300, 760, '#FFFFFF', .24)}
<div class="a L" style="left:80px;top:200px;font-size:22px;color:#fff">domingo à noite • São João Batista</div>
<div class="a" style="left:76px;top:260px;display:flex;flex-direction:column;align-items:flex-start;gap:14px">
 {cx('Boa', '#FFC20E', MAR, 170, 'font-family:Anton;padding:14px 30px 6px')}{cx('semana!', '#fff', ROY, 170, 'font-family:Anton;padding:14px 30px 6px')}</div>
<div class="a" style="left:80px;top:740px;width:820px">{H('Fé, trabalho', 96, '#fff')}{H('e união', 96, '#FFE066')}</div>
<div class="a K" style="left:84px;top:960px;font-size:62px;color:#fff">juntos podemos mais!</div>{credito('barcos-baixada-maranhense3-jpg.jpg')}"""))

# ---- CORREÇÕES DE SITUAÇÃO (por cima das artes já aprovadas; as fotos recortadas do Leo não estão nesta máquina)
# 15/11: o cartão é recriado igual ao do gerar9 (mesma posição, giro e tamanho), só com a lista nova. Antes: "Fiscaliza a prefeitura · ... · Leva a demanda do seu bairro".
P.append(('p1-15-11-situacao', 'url(originais/p1-15-11.jpg) center/cover', f"""
<div class="a card" style="left:96px;top:690px;width:800px;transform:rotate(-2deg);padding:28px 36px 30px">
 <div style="display:flex;align-items:baseline;gap:18px"><span class="K" style="font-size:46px;color:{LAR};white-space:nowrap">se liga!</span>{H('O que faz um vereador?', 62, ROY)}</div>
 <div class="lista" style="margin-top:18px;gap:14px">{''.join(f'<div class="li"><b>0{i+1}</b><span>{t}</span></div>' for i, t in enumerate(['Vota as leis da cidade', 'Aprova projetos pro povo', 'Trabalha junto pela cidade']))}</div></div>"""))
# 31/12: refeito. Antes "O que o seu bairro precisa em 2027?" (vetado pela Bruna). Agora: conquista pessoal de 2026 (positivo, sem margem para crítica). Mesma composição aprovada (Designi "primeira bike").
P.append(('p5-31-12-situacao', AMARELO, f"""
<div class="a" style="left:-30px;top:880px;width:1140px;text-align:center">{H('2026', 620, 'rgba(255,255,255,.18)', 'line-height:.8')}</div>
<div class="a" style="left:0;width:1080px;top:150px;text-align:center"><div class="L" style="font-size:22px;color:{MAR}">31 de dezembro</div>
 {H('Qual foi a sua', 96, '#fff', 'margin-top:12px;text-shadow:0 8px 24px rgba(120,40,0,.35)')}<div style="margin-top:6px">{cx('conquista em 2026?', MAR, '#fff', 64, 'font-family:Anton;letter-spacing:.01em')}</div></div>
<div class="a" style="left:150px;top:520px;width:780px;background:#fff;border-radius:36px;overflow:hidden;box-shadow:0 40px 70px -30px rgba(120,40,0,.6)">
 <div class="H" style="background:{ROY};color:#fff;text-align:center;font-size:52px;padding:18px 0 14px">Conta pra gente!</div>
 <div style="padding:26px 34px 30px;display:flex;flex-direction:column;gap:14px">{op(1, 'Saúde da família')}{op(2, 'Um trabalho novo')}{op(3, 'Os estudos')}{op(4, 'A casa e a família')}</div></div>
<div class="a" style="left:0;width:1080px;top:985px;text-align:center"><span class="K" style="font-size:50px;color:#fff;text-shadow:0 4px 16px rgba(120,40,0,.4)">obrigado por 2026, São João Batista!</span></div>"""))
# Apresentação v13 · arte 3: "ME CONTA SUA DEMANDA" → "CONTE SEMPRE COMIGO" (mesma caixa branca, mesma fonte)
P.append(('leo-v13-3-direita-situacao', 'url(originais/leo-v13-3-direita.jpg) center/cover', f"""
<div class="a B" style="left:166px;top:668px;width:576px;height:68px;padding:0 26px;display:flex;align-items:center;font-size:36px;letter-spacing:.02em;color:{ROY};background:#fff">Conte sempre comigo</div>"""))

SEM_ASS = ('p1-15-11-situacao', 'leo-v13-3-direita-situacao')
GRAO_DIV = '<div class="a" style="inset:0;background-image:url(&quot;' + GRAO + '&quot;);opacity:.10;mix-blend-mode:overlay;pointer-events:none"></div>'
secs = ''.join('<section class="f" id="' + i + '" style="background:' + bg + '">' + c + ('' if i in SEM_ASS else ASSINA(bg, i) + GRAO_DIV) + '</section>' for i, bg, c in P)
open(f'{d}/artes.html', 'w').write(f'<!doctype html><html><head><meta charset="utf-8">{head}</head><body>{secs}</body></html>')
print(len(P), 'artes')
