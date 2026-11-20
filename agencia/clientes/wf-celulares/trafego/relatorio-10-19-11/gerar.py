# WF Celulares · relatório da campanha Meta Ads 10–19/11/2026 (conta Pedro, 20/11/2026)
# Identidade aprovada B "Assinatura" (preto, grafite, titânio, prata, branco gelo; Inter fina; logo B branca).
# Composição copiada do manual da marca WF (identidade/manual-pags, 16:9: rótulo espaçado + título curto + 1 ideia por página)
# e do keynote Apple (número gigante sozinho, legenda fina embaixo).
# Números: só os confirmados (PLANO-OTIMIZACAO-19-11.md, conta Leandro). Faturamento = estimativa pelos preços anunciados.
# python3 gerar.py && node render.js
import os
D = os.path.dirname(os.path.abspath(__file__))

INV, CONV, VEND = 158.97, 95, 5
CPC = INV / CONV            # 1,67
CPV = INV / VEND            # 31,79
TAXA = VEND / CONV * 100    # 5,26 %
DIAS = 9                    # 10 a 18/11
PRECOS = [('17 Pro Max seminovo', 5850), ('14 Plus azul', 2499), ('12 Pro Max', 2199)]
EST = sum(p for _, p in PRECOS)   # 10.548
ROAS = EST / INV                  # 66,4
br = lambda v, c=2: f'{v:,.{c}f}'.replace(',', 'X').replace('.', ',').replace('X', '.')

CSS = """
@font-face{font-family:I;src:local('Inter')}
*{box-sizing:border-box;margin:0;padding:0}
html,body{background:#000}
body{font-family:'Inter',sans-serif;color:#F5F5F7;-webkit-font-smoothing:antialiased}
section.p{width:1920px;height:1080px;position:relative;overflow:hidden;page-break-after:always;
 background:radial-gradient(1200px 700px at 78% 18%,#1D1D1F 0%,#0A0A0B 55%,#000 100%);padding:110px 130px}
.rot{font:500 17px 'Inter';letter-spacing:.32em;text-transform:uppercase;color:#8E8A84}
h1{font:300 92px/1.02 'Inter Display','Inter';letter-spacing:-.035em;margin-top:26px}
h2{font:300 64px/1.06 'Inter Display','Inter';letter-spacing:-.03em;margin-top:22px;max-width:1500px}
.ti{background:linear-gradient(100deg,#F5F5F7 0%,#C7C9CC 40%,#8E8A84 75%,#C7C9CC 100%);-webkit-background-clip:text;color:transparent}
p,li{font:300 27px/1.5 'Inter';color:#D2D2D7}
.mut{color:#8E8A84}
b{font-weight:500;color:#F5F5F7}
.rod{position:absolute;left:130px;right:130px;bottom:56px;display:flex;justify-content:space-between;align-items:center;
 font:400 15px 'Inter';letter-spacing:.14em;text-transform:uppercase;color:#6E6C68}
.rod img{height:34px;opacity:.9}
.lin{height:1px;background:linear-gradient(90deg,#8E8A84,transparent);margin:34px 0}
.num{font:200 150px/1 'Inter Display','Inter';letter-spacing:-.05em;white-space:nowrap}
.leg{font:400 19px 'Inter';letter-spacing:.18em;text-transform:uppercase;color:#8E8A84;margin-top:14px}
.est{font:500 15px 'Inter';letter-spacing:.2em;text-transform:uppercase;color:#C7C9CC;border-bottom:1px solid #8E8A84;padding-bottom:3px}
.g{display:grid;gap:60px}
table{border-collapse:collapse;width:100%}
td,th{font:300 21px/1.35 'Inter';color:#D2D2D7;text-align:left;padding:13px 16px;border-bottom:1px solid #2E2E31;vertical-align:top}
th{font:500 14px 'Inter';letter-spacing:.2em;text-transform:uppercase;color:#8E8A84}
.ok{color:#C7C9CC}.er{color:#F5F5F7;font-weight:500}
.th img{width:100%;border-radius:14px;display:block}
.cap{font:400 16px/1.4 'Inter';color:#8E8A84;margin-top:12px;letter-spacing:.04em}
ol.n{list-style:none;counter-reset:k}ol.n li{counter-increment:k;position:relative;padding-left:64px;margin:0 0 20px}
ol.n li:before{content:counter(k,decimal-leading-zero);position:absolute;left:0;top:4px;font:400 17px 'Inter';letter-spacing:.2em;color:#8E8A84}
"""

def pag(n, rot, corpo, total):
    return (f'<section class="p"><div class="rot">{n:02d} · {rot}</div>{corpo}'
            f'<div class="rod"><img src="img/logo.png" alt="WF Celulares"><span>Relatório Meta Ads · 10 a 19/11/2026</span><span>{n:02d} / {total:02d}</span></div></section>')

def dots():
    # 95 conversas, 5 vendas (gráfico de unidades: 1 ponto = 1 conversa)
    s = ''
    for i in range(CONV):
        v = i < VEND
        s += f'<span style="width:30px;height:30px;border-radius:50%;display:inline-block;margin:0 9px 9px 0;{"background:linear-gradient(135deg,#F5F5F7,#8E8A84)" if v else "border:1.5px solid #3A3936"}"></span>'
    return f'<div style="width:780px;line-height:0">{s}</div>'

def barras_fat():
    mx = 6000; h = 420; out = ''
    itens = [(n, v) for n, v in PRECOS] + [('13 rosa', None), ('13 Pro Max', None)]
    for nome, v in itens:
        if v:
            hh = int(h * v / mx)
            b = f'<div style="height:{hh}px;width:120px;border-radius:4px 4px 0 0;background:linear-gradient(180deg,#C7C9CC,#8E8A84)"></div>'
            t = f'R$ {br(v,0)}'
        else:
            b = f'<div style="height:{int(h*0.36)}px;width:120px;border:1.5px dashed #6E6C68;border-bottom:none;border-radius:4px 4px 0 0"></div>'
            t = 'a informar'
        out += (f'<div style="display:flex;flex-direction:column;align-items:center;justify-content:flex-end;width:170px">'
                f'<div style="font:400 22px Inter;color:{"#F5F5F7" if v else "#8E8A84"};margin-bottom:12px">{t}</div>{b}'
                f'<div style="font:400 16px Inter;letter-spacing:.06em;color:#8E8A84;margin-top:14px;text-align:center;height:44px">{nome}</div></div>')
    return f'<div style="display:flex;align-items:flex-end;gap:14px;border-bottom:1px solid #3A3936;padding-bottom:0">{out}</div>'

def relatorio():
    P = []
    # 1 capa
    P.append(('CAPA', f'''<div style="position:absolute;right:150px;top:250px;text-align:center"><img src="img/logo.png" style="width:440px"></div>
<div style="position:absolute;left:130px;bottom:230px"><div class="rot">Relatório de tráfego pago · Meta Ads</div>
<h1 style="font-size:120px">Campanha de<br><span class="ti">mensagens.</span></h1>
<p style="margin-top:30px" class="mut">10 a 18/11/2026 (dados) · otimização de 19/11 · São Luís</p></div>'''))
    # 2 resumo
    P.append(('RESUMO', f'''<h2>O que o dinheiro gerou, <span class="ti">em 5 linhas.</span></h2><div class="lin"></div>
<ol class="n" style="max-width:1500px">
<li><b>R$ {br(INV)}</b> investidos de 10 a 18/11 viraram <b>{CONV} conversas</b> no WhatsApp e <b>{VEND} vendas</b> informadas.</li>
<li>Cada conversa custou <b>R$ {br(CPC)}</b>; cada venda, <b>R$ {br(CPV)}</b>. Uma venda a cada {CONV//VEND} conversas.</li>
<li>Quem vende é o vídeo real <b>"aparelho na mão + preço"</b>: os modelos vendidos são os desses Reels.</li>
<li>Os 5 vídeos ilustrativos (V01 a V05) ficaram atrás; 3 saem, a assistência (V02) fica, o V05 fica em teste.</li>
<li>Agora: saldo com cartão automático, raio de 8 km fixo, R$ 30 + R$ 8 por dia e 6 Reels reais novos.</li></ol>'''))
    # 3 estrutura
    P.append(('PERÍODO E ESTRUTURA', '''<h2>Uma campanha, um raio, <span class="ti">um destino.</span></h2><div class="lin"></div>
<div class="g" style="grid-template-columns:1fr 1fr">
<div><p><b>Período dos dados:</b> 10 a 18/11/2026 (9 dias, relatório da extensão).</p>
<p style="margin-top:18px"><b>15/11:</b> o Lindson criou a campanha <b>"WF Celulares | Mensagens WhatsApp | Nov26"</b>, subiu os criativos novos (V01 a V05) e reajustou a estratégia.</p>
<p style="margin-top:18px"><b>19/11:</b> plano de otimização e comando da extensão (conta Leandro).</p>
<p style="margin-top:18px"><b>Objetivo:</b> conversas no WhatsApp. Cobrança pré-paga (saldo).</p></div>
<div><div class="rot" style="margin-bottom:26px">Regras fixas · conferir em toda edição</div>
<table><tr><td class="er">Local</td><td>Só São Luís · raio de 8 km da Av. Daniel de La Touche</td></tr>
<tr><td class="er">Expansão</td><td>"Alcançar mais pessoas" desligado (a duplicação de conjunto costuma religar)</td></tr>
<tr><td class="er">Destino</td><td>Só WhatsApp (sem Messenger, sem Direct)</td></tr>
<tr><td class="er">IA da Meta</td><td>Retoques automáticos do criativo desligados</td></tr>
<tr><td class="er">Edição</td><td>Nada de recomendação da Meta que mude local, público ou criativo</td></tr></table></div></div>'''))
    # 4 números
    P.append(('NÚMEROS', f'''<h2>Os números <span class="ti">confirmados.</span></h2>
<div class="g" style="grid-template-columns:repeat(3,1fr);margin-top:90px">
<div><div class="num" style="font-size:118px;margin-top:22px">R$ {br(INV)}</div><div class="leg">investidos · 10 a 18/11</div></div>
<div><div class="num ti">{CONV}</div><div class="leg">conversas no WhatsApp</div></div>
<div><div class="num ti">{VEND}</div><div class="leg">vendas informadas</div></div></div>
<div class="g" style="grid-template-columns:repeat(3,1fr);margin-top:110px">
<div><div class="num" style="font-size:96px">R$ {br(CPC)}</div><div class="leg">por conversa</div></div>
<div><div class="num" style="font-size:96px">R$ {br(CPV)}</div><div class="leg">por venda</div></div>
<div><div class="num" style="font-size:96px">{br(TAXA,1)}%</div><div class="leg">das conversas viraram venda</div></div></div>
<p class="mut" style="position:absolute;left:130px;bottom:120px;font-size:19px">Média do período: R$ {br(INV/DIAS)} por dia e {br(CONV/DIAS,1)} conversas por dia. Fonte: relatório da extensão (10–18/11) e vendas informadas ao Lindson.</p>'''))
    # 5 funil
    P.append(('FUNIL', f'''<div class="g" style="grid-template-columns:1fr 820px;align-items:center;height:760px">
<div><h2>Uma venda a cada <span class="ti">{CONV//VEND} conversas.</span></h2><div class="lin"></div>
<p>Cada ponto é uma conversa. Os <b>{VEND} claros</b> viraram venda: 17 Pro Max seminovo, 14 Plus azul, 13 rosa, 13 Pro Max e 12 Pro Max.</p>
<p style="margin-top:20px">O gargalo não é o anúncio (a conversa sai barata): é <b>a conversa virar venda</b>. Resposta rápida, foto e vídeo do aparelho e o parcelamento claro sobem essa taxa sem gastar mais.</p></div>
<div>{dots()}</div></div>'''))
    # 6 faturamento
    P.append(('FATURAMENTO', f'''<div class="g" style="grid-template-columns:1fr 900px;align-items:end;height:770px">
<div><div class="est">Estimativa pelos preços anunciados · a confirmar com o dono</div>
<h2 style="margin-top:30px">Pelo menos <span class="ti">R$ {br(EST,0)}</span><br>em 3 das 5 vendas.</h2><div class="lin"></div>
<p>Preços dos Reels postados no Instagram da loja. O 13 rosa e o 13 Pro Max não têm preço anunciado: <b>valor a informar</b>.</p>
<p style="margin-top:20px">ROAS estimado (parcial): <b>{br(ROAS,0)}×</b> o investido. É receita, não lucro: o retorno real depende da margem de cada aparelho, que só o dono sabe.</p></div>
<div>{barras_fat()}</div></div>'''))
    # 7 criativos
    th = ''.join(f'<div class="th"><img src="img/quadro{n}.jpg"><div class="cap">{t}</div></div>' for n, t in [(44, '17 Pro Max seminovo · vendeu'), (42, '14 Plus · vendeu'), (43, '12 Pro Max · vendeu')])
    tv = ''.join(f'<div class="th"><img src="img/v0{n}.jpg"><div class="cap">{t}</div></div>' for n, t in [(1, 'V01 Laudo · pausar'), (2, 'V02 Assistência · manter'), (3, 'V03 Black · pausar'), (4, 'V04 Como comprar · pausar'), (5, 'V05 Duas lojas · em teste')])
    P.append(('CRIATIVOS', f'''<h2>O real vende. <span class="ti">O ilustrativo explica.</span></h2>
<div style="display:grid;grid-template-columns:560px 1fr;gap:70px;margin-top:46px">
<div><div class="rot" style="margin-bottom:18px">Vencedor · aparelho na mão + preço</div><div style="display:grid;grid-template-columns:repeat(3,1fr);gap:14px">{th}</div>
<p style="margin-top:24px;font-size:22px">Vídeo da própria loja, modelo e cor na tela, preço grande. Os modelos que venderam são desses Reels.</p></div>
<div><div class="rot" style="margin-bottom:18px">V01 a V05 · foto ilustrativa, sem preço</div><div style="display:grid;grid-template-columns:repeat(5,1fr);gap:14px">{tv}</div>
<p style="margin-top:24px;font-size:22px"><b>V02 fica</b>: é outro conceito (assistência), o que a Meta precisa para variar. <b>V05</b> sai se passar de R$ 8 por conversa em 3 dias. V01, V03 e V04 saem: sem preço e sem aparelho real, falam com quem ainda não quer comprar.</p></div></div>
<p class="mut" style="position:absolute;left:130px;bottom:118px;font-size:18px">Gasto e conversas por anúncio estão no relatório bruto da extensão, que não foi salvo no repositório (ver pendências).</p>'''))
    # 8 problemas
    P.append(('PROBLEMAS ENCONTRADOS', '''<h2>Quatro problemas, <span class="ti">quatro correções.</span></h2><div class="lin"></div>
<table><tr><th style="width:24%">Problema</th><th style="width:40%">O que aconteceu</th><th>Correção</th></tr>
<tr><td class="er">Público vazando</td><td>Até 15/11, parte das conversas do anúncio #1 veio de fora de São Luís (vendas que a loja não atende).</td><td>Raio de 8 km da Daniel de La Touche e expansão desligada; conferir em toda edição.</td></tr>
<tr><td class="er">Saldo zerado</td><td>Conta pré-paga: com saldo R$ 0 os anúncios param de rodar.</td><td>Recarregar e cadastrar cartão como pagamento automático (só o Lindson ou o dono).</td></tr>
<tr><td class="er">Retoques de IA da Meta</td><td>A Meta pode cortar, expandir ou reescrever o criativo sem conferência (preço e texto em risco).</td><td>Desligados; item fixo do checklist de edição.</td></tr>
<tr><td class="er">Número de WhatsApp duplo</td><td>Os V01 a V05 mostram (98) 98827-1882 (o da bio); o anúncio leva para +55 98 9120-8085.</td><td>O dono confirma qual é o de vendas; a contagem de vendas soma os dois.</td></tr></table>'''))
    # 9 auditoria V
    P.append(('AUDITORIA · V01 A V05', '''<h2>Padrão de exigência <span class="ti">aplicado para trás.</span></h2>
<p class="mut" style="margin-top:14px;font-size:21px">8 critérios de imagem (conferencia-imagem-ia.md) com zoom. As fotos não são de IA (imprensa Apple e Unsplash), mas passam pela mesma régua. Um erro = não usa.</p>
<table style="margin-top:26px"><tr><th style="width:23%">Critério</th><th style="width:41%">Achado</th><th>Peças</th></tr>
<tr><td class="er">Resolução (máx. 1,5×)</td><td>Foto horizontal esticada para 9:16: 16-camsys 2,2×, 11-water 2,1×, 17-camera, 12-back e 12-announce 1,7× (mais 10% de zoom)</td><td>V01, V02, V05 · V03 no limite (1,47× + zoom)</td></tr>
<tr><td class="er">Texto falso / outra língua</td><td>Tela de bloqueio em inglês: "Thursday, November 12", "Tue Apr 1", "Tuesday, October 13", app "Spin"</td><td>V02, V04</td></tr>
<tr><td class="er">Foto repetida</td><td>16-camsys, 17-camera, 17-orange, 17-lineup, 17-lock e 12-announce já estão no feed artes-02; cada vídeo repete a mesma foto em 2 a 3 cenas</td><td>V01, V03, V04, V05</td></tr>
<tr><td class="er">Mensagem em 1 s</td><td>Sem aparelho real e sem preço: não diz "tem esse iPhone por esse valor"</td><td>V01, V03, V04, V05</td></tr>
<tr><td class="er">Identidade (18/11)</td><td>Pílula no rótulo e manchete Black: a marca pede Inter fina e nada de pílula</td><td>V01 a V05</td></tr>
<tr><td class="er">Promessa a confirmar</td><td>"Cartão em até 18x" para tudo (o próprio perfil mostra 18x num post e 12x noutro); "Laudo WF com 5 testes"</td><td>V04, V01</td></tr>
<tr><td class="ok">Cena, olhar, mãos, geometria</td><td>Sem pessoas montadas nem objetos impossíveis; aparelhos inteiros</td><td>ok</td></tr></table>'''))
    # 10 auditoria reels
    tc = ''.join(f'<div class="th"><img src="img/capa{n}.jpg"><div class="cap">capa {n}</div></div>' for n in range(41, 46))
    P.append(('AUDITORIA · REELS 41 A 45', f'''<div style="display:grid;grid-template-columns:1fr 820px;gap:70px">
<div><h2>O vídeo é bom. <span class="ti">A capa, não.</span></h2>
<table style="margin-top:34px"><tr><th style="width:34%">Critério</th><th>Achado</th></tr>
<tr><td class="ok">Cena, mãos, escala</td><td>Vídeo real da loja, aparelho na mão: ok (é o vencedor)</td></tr>
<tr><td class="er">Resolução</td><td>Capas feitas de print do Reel, ampliado 2,5× a 2,7× (limite 1,5×)</td></tr>
<tr><td class="er">Fundo claro</td><td>Capas 42 e 44 claras: repetem o branco reprovado em 10/11 ("parece pobre")</td></tr>
<tr><td class="er">Preço em tarja</td><td>Preço em bloco azul e rótulos em pílula: a WF pede preço elegante, sem tarja</td></tr>
<tr><td class="er">Quadro</td><td>42 tremido; 43 mostra tapete infantil no chão</td></tr></table>
<p style="margin-top:26px;font-size:22px"><b>Trocar:</b> refazer as 5 capas escuras, do arquivo original do vídeo (1080p), preço em Inter fina sem bloco. Os vídeos seguem no ar.</p></div>
<div style="display:grid;grid-template-columns:repeat(5,1fr);gap:12px;align-content:start;margin-top:150px">{tc}</div></div>'''))
    # 11 feito 19/11
    P.append(('O QUE FOI FEITO EM 19/11', '''<div class="g" style="grid-template-columns:1fr 1fr">
<div><h2>Estrutura <span class="ti">enxuta.</span></h2><div class="lin"></div>
<ol class="n"><li><b>Conjunto principal</b> · 8 km, só WhatsApp, Advantage+ público · <b>R$ 30/dia</b></li>
<li><b>Remarketing</b> · assistiu Reels 90 dias, engajou no Instagram e mandou mensagem em 365 dias · <b>R$ 8/dia</b></li>
<li><b>Anúncios</b> · pausar V01, V03 e V04; manter "Celular parcelado", V02 e V05</li>
<li><b>Texto curto</b> · 2 a 3 linhas, sem bloco de hashtags (anúncio antigo não se edita: perde o aprendizado)</li></ol>
<p class="mut" style="font-size:19px">Plano e comando da extensão prontos (conta Leandro). A execução no Gerenciador se confirma com os prints da extensão.</p></div>
<div><div class="rot" style="margin-top:30px">Regras de decisão · depois de 3 a 4 dias, sem mexer no aprendizado</div>
<div style="margin-top:40px;display:grid;gap:44px">
<div><div class="num" style="font-size:84px">&gt; R$ 8</div><div class="leg">por conversa, ou sem entrega → pausa</div></div>
<div><div class="num" style="font-size:84px">&lt; R$ 60</div><div class="leg">por venda, com estoque → +20% a cada 3 dias</div></div>
<div><div class="num" style="font-size:84px">&gt; 3</div><div class="leg">de frequência → trocar criativos</div></div></div></div></div>'''))
    # 12 próximos
    P.append(('PRÓXIMOS 7 E 14 DIAS', '''<h2>Mais vídeo real, <span class="ti">mesma disciplina.</span></h2><div class="lin"></div>
<div class="g" style="grid-template-columns:1fr 1fr">
<div><div class="rot" style="margin-bottom:24px">Até 26/11 · 7 dias</div><ol class="n">
<li>Saldo com cartão automático; conferir as regras fixas nos 2 conjuntos.</li>
<li>6 Reels novos no formato vencedor (8 a 12 s): 17 Pro Max, 14 Plus, 13 Pro Max, 13 cores, 12 Pro Max e "chegou hoje" com 3 aparelhos, gravados na loja.</li>
<li>Preço "a partir de" e parcelamento de cada aparelho confirmado pelo dono.</li>
<li>Etiquetas no WhatsApp e planilha diária (página 13).</li>
<li>Dia 3: só olhar. Dia 7: aplicar as regras de decisão.</li></ol></div>
<div><div class="rot" style="margin-bottom:24px">Até 03/12 · 14 dias · Black Friday</div><ol class="n">
<li>Entrar os 6 Reels de uma vez (lote), não um por dia.</li>
<li>Black Friday (28/11) só com <b>oferta real</b> que o dono confirmar: aparelho, preço, prazo e quantidade. Sem oferta, sem anúncio de Black.</li>
<li>Remarketing de Black no conjunto de R$ 8, com o mesmo vídeo real.</li>
<li>Primeiro relatório semanal com custo por venda e ROAS reais.</li>
<li>Assistência em conjunto próprio só com R$ 50/dia ou mais.</li></ol></div></div>'''))
    # 13 medição
    P.append(('MEDIÇÃO DE VENDA', '''<div class="g" style="grid-template-columns:1fr 1fr">
<div><h2>Sem anotar, <span class="ti">não há ROAS.</span></h2><div class="lin"></div>
<p>A Meta conta conversas; venda só a loja conta. Duas rotinas de 1 minuto resolvem.</p>
<div class="rot" style="margin:44px 0 22px">Etiquetas no WhatsApp Business</div>
<table><tr><td class="er" style="width:200px">Anúncio</td><td>toda conversa que chega pelo anúncio</td></tr>
<tr><td class="er">Vendeu</td><td>quando fecha</td></tr><tr><td class="er">Valor</td><td>valor da venda na própria etiqueta ou nota</td></tr></table></div>
<div><div class="rot" style="margin:30px 0 22px">Planilha diária · uma linha por dia</div>
<table><tr><th>Coluna</th><th>Exemplo de preenchimento</th></tr>
<tr><td>Data</td><td>20/11</td></tr><tr><td>Conversas do anúncio</td><td>contagem da etiqueta</td></tr>
<tr><td>Vendas e aparelhos</td><td>modelo e cor</td></tr><tr><td>Valor de cada venda</td><td>R$ do caixa</td></tr>
<tr><td>Número que recebeu</td><td>9120-8085 ou 98827-1882</td></tr>
<tr><td>Gasto do dia</td><td>Gerenciador de Anúncios</td></tr></table>
<p style="margin-top:26px;font-size:22px">Toda segunda: custo por venda = gasto ÷ vendas; ROAS = vendas em R$ ÷ gasto.</p></div></div>'''))
    # 14 pendências
    P.append(('PENDÊNCIAS', '''<h2>O que falta <span class="ti">para fechar o número.</span></h2><div class="lin"></div>
<div class="g" style="grid-template-columns:1fr 1fr">
<div><div class="rot" style="margin-bottom:24px">Lindson</div><ol class="n">
<li>Recarregar o saldo e cadastrar o cartão automático.</li>
<li>Colar o comando de 19/11 na extensão e salvar o relatório dela no repositório.</li>
<li>Salvar o relatório bruto de 10 a 18/11 (por anúncio, posicionamento, idade e gênero).</li>
<li>Aprovar a troca das capas 41 a 45 e a saída de V01, V03 e V04.</li></ol></div>
<div><div class="rot" style="margin-bottom:24px">Dono da WF</div><ol class="n">
<li>Valor de cada uma das 5 vendas (13 rosa e 13 Pro Max sem preço anunciado).</li>
<li>Qual WhatsApp é o de vendas: 98827-1882 ou 9120-8085.</li>
<li>Parcelamento por aparelho (12x ou 18x) e se o Laudo WF sai por escrito.</li>
<li>Oferta real de Black Friday e os 6 Reels gravados na loja.</li>
<li>IDs do conjunto A e dos anúncios V02 a V04 (vêm da extensão).</li></ol></div></div>'''))
    # 15 fecho
    P.append(('PARA O CLIENTE', '''<div style="position:absolute;left:130px;top:300px;max-width:1500px">
<h1 style="font-size:104px">Cada R$ 31,79 em anúncio<br><span class="ti">trouxe uma venda de iPhone.</span></h1>
<p style="margin-top:40px;max-width:1250px">A mensagem para o dono: a venda saiu barata perto do valor de um iPhone; agora o ganho está em gravar mais vídeos reais, responder rápido e anotar cada venda. Sem promessa de número: o próximo relatório mostra o resultado real.</p></div>'''))
    tot = len(P)
    return ''.join(pag(i + 1, r, c, tot) for i, (r, c) in enumerate(P))

def cliente():
    a = f'''<section class="p"><div class="rot">WF Celulares · anúncios no Instagram e Facebook · 10 a 18/11/2026</div>
<h2>O que o seu investimento <span class="ti">gerou.</span></h2>
<div class="g" style="grid-template-columns:repeat(3,1fr);margin-top:90px">
<div><div class="num" style="font-size:118px;margin-top:22px">R$ {br(INV)}</div><div class="leg">investidos em 9 dias</div></div>
<div><div class="num ti">{CONV}</div><div class="leg">conversas no WhatsApp</div></div>
<div><div class="num ti">{VEND}</div><div class="leg">iPhones vendidos</div></div></div>
<div class="lin" style="margin-top:80px"></div>
<p style="max-width:1500px">Cada conversa custou <b>R$ {br(CPC)}</b> e cada venda, <b>R$ {br(CPV)}</b>. Venderam 17 Pro Max seminovo, 14 Plus azul, 13 rosa, 13 Pro Max e 12 Pro Max.
Só nos 3 com preço anunciado, foram cerca de <b>R$ {br(EST,0)}</b> <span class="mut">(estimativa pelos preços dos posts; confirme os valores com a gente)</span>.</p>
<div class="rod"><img src="img/logo.png" alt="WF Celulares"><span>Resumo para o cliente</span><span>01 / 02</span></div></section>'''
    b = f'''<section class="p"><div class="rot">O que vem agora</div>
<h2>Mais vídeo da loja, <span class="ti">mais venda anotada.</span></h2><div class="lin"></div>
<div class="g" style="grid-template-columns:1fr 1fr">
<ol class="n"><li>O que mais vendeu foi o <b>vídeo do aparelho na mão com o preço</b>. Vamos fazer mais 6 assim, gravados na loja.</li>
<li>Os anúncios ficam <b>só para São Luís</b> (8 km da Daniel de La Touche) e só para o WhatsApp.</li>
<li>Orçamento: <b>R$ 30 por dia</b> para quem ainda não conhece a loja e <b>R$ 8 por dia</b> para quem já viu os vídeos.</li></ol>
<div><div class="rot" style="margin-bottom:24px">Precisamos de você</div><ol class="n">
<li>Cartão cadastrado como pagamento automático (o saldo zerou e o anúncio para).</li>
<li>Marcar no WhatsApp as conversas do anúncio e as vendas, com o valor.</li>
<li>O valor das 5 vendas, o parcelamento de cada aparelho e qual número atende as vendas.</li>
<li>A oferta de Black Friday, se tiver. Sem oferta real, não anunciamos Black.</li></ol></div></div>
<div class="rod"><img src="img/logo.png" alt="WF Celulares"><span>Resumo para o cliente</span><span>02 / 02</span></div></section>'''
    return a + b

for nome, corpo, tit in [('relatorio.html', relatorio(), 'WF · Relatório Meta Ads 10–19/11'), ('cliente.html', cliente(), 'WF · Resumo da campanha')]:
    open(os.path.join(D, nome), 'w').write(f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>{tit}</title><style>{CSS}</style></head><body>{corpo}</body></html>')
print('ok', br(CPC), br(CPV), br(TAXA, 1), br(EST, 0), br(ROAS, 1))
