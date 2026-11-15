"""Textos v2 (empresa inteira) do deck, do plano e do one-pager. Conta Lindson, Maquiavel gerente, 15/11/2026.
Números: modelo.py. [preencher: ...] = dado que só o Lindson tem."""
FALTA = '<span style="background:#F5C518;color:#0A0A0A;font-weight:800;padding:0 6px">[preencher: {}]</span>'
def pf(x): return FALTA.format(x)
AVISO = ('Conversa privada com pessoa convidada, sem oferta pública de valores mobiliários. Projeções são estimativas com premissas '
         'explícitas, não promessa de resultado nem de retorno. A estrutura final passa por advogado e contador.')
UNID = [  # (nome, situação real, o que o dinheiro faz)
    ('1 · Agência para negócios locais', 'Receita hoje: R$ 4.800/mês (Jaci R$ 1.500, Leo Pinto R$ 2.500, WF R$ 800). Carteira de trabalhos: Tribuna 98, Real Time, Desentupidora SF, curso legislativo. Esteira de R$ 600 a R$ 3.500/mês.', 'Tráfego próprio para fechar clientes da esteira'),
    ('2 · Orégano Turbo (pizzarias)', 'Pronta para vender: marca, site com planos, kit social, contrato, preços aprovados (R$ 1.597 a 3.997/mês). 0 clientes ainda.', 'Tráfego, 5 fundadoras em 60 dias'),
    ('3 · Produtos digitais (Hubla)', 'Bio que Vende, Kit Mês Pronto, Kit WhatsApp, Kit Prospecção, Raio-X, Pack de capas, Manual de Campo; área de membros própria. Preços a definir.', 'Teste pequeno de tráfego; para se não se pagar'),
    ('4 · YouTube e marca pessoal', 'Passaporte da Bíblia e Raposa e Leão (longos prontos), @lindsonalmeida_. Sem receita hoje.', 'Nada do aporte: segue com a equipe de IA'),
    ('5 · Tecnologia própria', 'Central do Cliente e painéis, app e robô SDR do WhatsApp, Dublê (voz e imagem), VEKTOR (central de comando). Uso interno.', 'Nada do aporte: ativo e opção futura de SaaS'),
    ('6 · Equipe de IA', '4 contas de IA e agentes especialistas no mesmo repositório: produzem o que uma agência faria com 4 a 6 pessoas.', 'Vantagem de custo: contratação só depois de 15 clientes'),
]

def slides_deck(c):
    b, M, mes, F, foto = c['b'], c['M'], c['mes'], c['F'], c['foto']
    P = M.P; ap = P['aporte']; teto = ap*P['rs_teto']; q = {n: c['R60'][n]['quitado'] for n in M.CEN}
    S = []
    S.append(('Plano investidor · 2026', f'''<img class="fot" src="{foto(F['capa'])}"><div class="fade"></div>
<div style="position:absolute;top:200px;left:90px;width:880px"><span class="tag">Lindson Almeida · Alkantara · marketing e tecnologia</span>
<h1 style="font-size:124px;margin-top:26px">Uma empresa,<br><span class="am">seis frentes</span>,<br>um motor só.</h1>
<p style="font-size:26px;margin-top:26px;color:#cfcfcf;max-width:780px">Agência, pizzarias, produtos digitais, YouTube e tecnologia própria, tocados com uma equipe de IA. São Luís (MA).</p></div>
<div class="rod">{AVISO}</div>'''))
    S.append(('01 · O problema', '''<h2>O negócio local quer cliente,<br>e o marketing <span class="am">não entrega</span>.</h2>
<div class="g3" style="margin-top:30px">
<div class="box"><div class="big">1</div><p style="margin-top:12px"><b>Depende de indicação e de aplicativo.</b> O mês bom e o mês ruim não se controlam.</p></div>
<div class="box"><div class="big">2</div><p style="margin-top:12px"><b>Posta sem método.</b> Instagram parado ou bonito, sem anúncio que leve ao WhatsApp nem número para medir.</p></div>
<div class="box"><div class="big">3</div><p style="margin-top:12px"><b>Agência cara ou amadora.</b> Quem tem método cobra de R$ 3.000 a R$ 6.000/mês (régua da Alpha, 05/11/2026); o resto entrega post solto.</p></div></div>
<div class="box" style="margin-top:30px;border-top-color:#fff"><p><b class="am">Do outro lado, o meu problema:</b> tenho a fábrica montada e mais frentes prontas do que verba para colocar na frente do cliente. O que falta é tráfego, equipamento e a primeira contratação.</p></div>'''))
    S.append(('02 · A solução', f'''<img class="fot" src="{foto(F['solucao'])}"><div class="fade"></div>
<div style="width:840px"><h2>Marketing que <span class="am">vende</span>, com o número na mesa.</h2><ul>
<li><b>Gestão de redes, tráfego e vídeo</b> com pagamento antecipado e contrato com prazo.</li>
<li><b>Sites e mini sites</b> que levam o cliente ao WhatsApp.</li>
<li><b>Central do Cliente:</b> o dono aprova peças e vê o relatório num painel próprio.</li>
<li><b>Nicho de vitrine:</b> Orégano Turbo, só para pizzarias.</li>
<li><b>Garantia de entrega</b>, nunca de resultado.</li></ul></div>'''))
    S.append(('03 · As seis frentes', '<h2>Seis unidades, <span class="am">uma estrutura</span>.</h2><div class="g3" style="gap:18px">' + ''.join(
        f'<div class="box" style="padding:18px 22px"><p class="an am" style="font-size:30px">{n}</p><p style="font-size:20px;margin-top:6px">{s_}</p><p style="font-size:19px;margin-top:6px" class="cz">Aporte: {d}</p></div>' for n, s_, d in UNID) + '</div>'))
    S.append(('04 · Tração real', f'''<h2>O que é <span class="am">fato</span> hoje.</h2>
<div class="g4"><div class="box"><div class="big" style="font-size:64px">R$ 4.800</div><p>por mês de receita, de 3 clientes pagantes</p></div>
<div class="box"><div class="big">72</div><p>trabalhos no portfólio do site oficial</p></div>
<div class="box"><div class="big">4</div><p>sites de clientes no ar (pages.dev)</p></div>
<div class="box"><div class="big">7</div><p>produtos digitais prontos, com área de membros própria</p></div></div>
<table style="margin-top:26px"><tr><th>Cliente pagante</th><th>Serviço</th><th>Valor/mês</th></tr>
<tr><td>Clínica Dra. Jaci Cunha</td><td>Redes, conteúdo, tráfego, site</td><td><b>R$ 1.500</b></td></tr>
<tr><td>Vereador Leo Pinto</td><td>Comunicação do mandato no Instagram</td><td><b>R$ 2.500</b></td></tr>
<tr><td>WF Celulares</td><td>Rebranding, feed e stories</td><td><b>R$ 800</b></td></tr></table>
<p class="cz" style="margin-top:10px;font-size:20px">Tribuna 98, Real Time, Desentupidora SF e Rafael Imports: trabalhos entregues, sem pagamento recorrente hoje.</p>'''))
    S.append(('05 · O mercado', f'''<h2>Mercado grande, <span class="am">atendido mal</span>.</h2>
<div class="g3"><div class="box"><div class="big">40.332</div><p>pizzarias no Brasil</p></div><div class="box"><div class="big">98%</div><p>fazem delivery</p></div><div class="box"><div class="big">75%</div><p>usam aplicativo para pedido</p></div></div>
<p class="cz" style="margin-top:10px;font-size:20px">Fonte: Apubra/Galunion, citado no roteiro OT-04 do repositório [Conferir a fonte primária e o ano].</p>
<div class="box" style="margin-top:22px"><p><b>São Luís e Grande Ilha:</b> negócios locais ativos {pf('nº (Receita Federal/Sebrae)')} · pizzarias {pf('nº (CNAE 5611-2/01 ou Google Maps)')}.<br>
A projeção Base pede <b>{mes('Base',24)['cli']:.0f} clientes</b> no mês 24 somando todas as frentes: uma fração pequena do mercado local.</p></div>'''))
    S.append(('06 · Modelo de negócio', '''<h2>Recorrência <span class="am">paga antes</span>.</h2>
<div class="g2"><div><p class="an am" style="font-size:34px">Agência · esteira</p><table><tr><th>Degrau</th><th>Por mês</th></tr>
<tr><td>Vídeo</td><td>R$ 600</td></tr><tr><td>Tráfego</td><td>R$ 800</td></tr><tr><td>Alcance</td><td>R$ 1.200</td></tr><tr><td>Presença</td><td>R$ 2.200</td></tr><tr><td><b>Instagram que Vende</b></td><td><b>R$ 3.500</b></td></tr></table>
<p class="cz" style="font-size:19px;margin-top:6px">Mini site avulso R$ 497. Fonte: esteira-de-produtos.md.</p></div>
<div><p class="an am" style="font-size:34px">Orégano Turbo · pizzarias</p><table><tr><th>Plano</th><th>Por mês</th></tr>
<tr><td>Muralha</td><td>R$ 1.597 a 1.997</td></tr><tr><td><b>Fortaleza</b></td><td><b>R$ 2.197 a 2.997</b></td></tr><tr><td>Cidadela ▲</td><td>R$ 3.497 a 3.997</td></tr></table>
<p style="font-size:21px;margin-top:12px"><b>Produtos:</b> R$ 19 a 47 cada (sugestão; preço final do Lindson), venda na Hubla. <b>Verba de anúncio</b> do cliente paga direto à Meta.</p></div></div>'''))
    S.append(('07 · A máquina de vendas', '<h2>Como o dinheiro vira <span class="am">cliente</span>.</h2><div style="display:flex;gap:14px;margin-top:24px">' + ''.join(
        f'<div class="box" style="flex:1"><div class="an am" style="font-size:36px">{a}</div><p style="font-size:21px;margin-top:8px">{t}</p></div>' for a, t in [
        ('Atrair', 'Anúncio com formulário, Reels, YouTube, robô SDR com botão de WhatsApp'), ('Filtrar', 'Quem não pode pagar o plano recebe o produto digital'),
        ('Diagnóstico', '30 min mostrando o perfil por dentro'), ('Fechar', 'Proposta, contrato e cartão no mesmo dia'), ('Reter', 'Central, relatório, renovação 30 dias antes')]) +
        '''</div><div class="box" style="margin-top:26px;border-top-color:#fff"><p><b class="am">Uma frente alimenta a outra:</b> o YouTube e a marca pessoal trazem audiência; os produtos de R$ 19 a 47 filtram quem ainda não pode pagar; a agência e o Orégano fazem a receita recorrente; a tecnologia e a equipe de IA seguram o custo baixo.</p></div>'''))
    S.append(('08 · Uso do dinheiro', f'''<h2>{b(ap)}: para onde <span class="am">vai</span>.</h2><div class="tuso">{c['tabela_uso']()}</div>
<p class="cz" style="margin-top:8px;font-size:19px">Em 2 parcelas: {b(P['parcela1'])} na assinatura e {b(P['parcela2'])} quando a receita nova somar R$ 10 mil/mês por 2 meses seguidos (verificável na Central). [estimativa] = orçar antes de assinar.</p>'''))
    S.append(('09 · A ordem do dinheiro', f'''<h2>Primeiro onde <span class="am">já rende</span>.</h2>
<div class="g3"><div class="box"><div class="big">1º</div><p><b>Agência e base:</b> já vende e já recebe. Tráfego, equipamento, ferramentas, jurídico e reserva.</p></div>
<div class="box"><div class="big">2º</div><p><b>Orégano Turbo e o 1º criador:</b> pronta para vender; a 2ª parcela depende da tração.</p></div>
<div class="box"><div class="big">3º</div><p><b>Produtos:</b> teste de R$ 600/mês; para se o custo por venda não fechar.</p></div></div>
<div class="box" style="margin-top:26px;border-top-color:#fff"><p><b class="am">YouTube e tecnologia não levam dinheiro do investidor.</b> Já rodam com a equipe de IA e ficam como ativo da casa. Em paráfrase, o que escrevi no <i>Príncipe</i> XIII: quem depende de armas alheias vive da sorte de outro. O dinheiro de fora acelera, não sustenta.</p></div>'''))
    S.append(('10 · Projeção consolidada', f'''<h2>Receita mensal <span class="am">projetada</span>.</h2>
<div class="g2" style="grid-template-columns:1.25fr 1fr;gap:40px"><div>{c['barras']()}</div><div>''' + ''.join(
        f'<div class="box" style="margin-bottom:12px;padding:14px 20px"><p><b class="am">{n}</b></p><p style="font-size:21px">Mês 12: {mes(n,12)["cli"]:.0f} clientes · {b(mes(n,12)["rec"])}/mês<br>Mês 24: {mes(n,24)["cli"]:.0f} clientes · {b(mes(n,24)["rec"])}/mês<br><span class="cz">Lucro em 24 meses: {b(c["luc24"](n))}</span></p></div>' for n in M.CEN) +
        '''</div></div><p class="cz" style="margin-top:6px;font-size:18px">Projeção, não promessa. Parte dos R$ 4.800 reais; YouTube e tecnologia sem receita projetada. Premissas por unidade na planilha anexa.</p>'''))
    S.append(('11 · Unit economics', f'''<h2>Cada cliente <span class="am">se paga</span>?</h2>
<div class="g2" style="grid-template-columns:1.3fr 1fr;gap:40px"><div class="tuso">{c['tabela_unit']()}</div>
<div><ul><li>CAC ainda é <b>premissa</b>: o primeiro uso do dinheiro é medi-lo.</li><li>Olhe o LTV de 12 meses, não o teórico.</li><li>O que mais mexe no plano: <b>clientes novos por mês</b> e <b>churn</b>.</li><li>Produtos só seguem com retorno do tráfego acima de 1x.</li></ul></div></div>'''))
    S.append(('12 · Marcos', '<h2>O que você vai <span class="am">ver</span>, e quando.</h2><div class="g3">' + ''.join(
        f'<div class="box"><div class="big">{t}</div><ul style="margin-top:12px">{"".join(f"<li>{x}</li>" for x in xs)}<li>Base: ~{mes("Base",m)["cli"]:.0f} clientes, {b(mes("Base",m)["rec"])}/mês</li></ul></div>' for t, m, xs in [
        ('6 meses', 6, ['5 pizzarias fundadoras', 'CAC medido na agência e no Orégano', 'Veredito do teste de produtos']),
        ('12 meses', 12, ['Cases autorizados', 'Equipe a partir do 15º cliente', 'Revisão de preços']),
        ('18 meses', 18, ['Operação com equipe', 'Decidir SaaS da Central ou 2ª cidade'])]) +
        '</div><p class="cz" style="margin-top:14px;font-size:19px">Valores do cenário Base: projeção. Relatório mensal com os números reais da Central.</p>'))
    S.append(('13 · Estrutura do investimento', f'''<h2>Três formatos. <span class="am">Um</span> recomendado.</h2><div class="g3">
<div class="box"><p class="an" style="font-size:30px">1 · Mútuo conversível / anjo</p><p style="font-size:24px;margin-top:8px">LC 155/2016. <b>Você:</b> pode virar sócio da empresa toda com desconto. <b>Contra:</b> retorno só com venda ou recompra; o Lindson dilui.</p></div>
<div class="box" style="border-top:8px solid #F5C518;background:#262106"><p class="an am" style="font-size:30px">2 · Revenue share ★</p><p style="font-size:24px;margin-top:8px">{P['rs_pct']*100:.0f}% da <b>receita nova</b> (acima dos R$ 4.800 de hoje), do mês {P['rs_carencia']+1} até {P['rs_teto']:.1f}x ({b(teto)}), prazo máximo {P['rs_prazo']} meses. Sem cotas, sem voto.</p></div>
<div class="box"><p class="an" style="font-size:30px">3 · Sócio numa unidade</p><p style="font-size:24px;margin-top:8px">Ex.: Orégano Turbo como empresa separada. <b>Você:</b> cotas e dividendos dela. <b>Contra:</b> só uma frente; acordo de sócios.</p></div></div>
<p style="margin-top:18px;font-size:23px"><b class="am">Por que sobre a receita nova:</b> os R$ 4.800 já existiam antes do dinheiro; cobrar sobre eles tiraria do caixa o que o investidor não criou. Sobre a receita total, YouTube e tecnologia ficariam presos ao contrato. Teto (projeção): base mês {q['Base']}, otimista {q['Otimista']}, conservador {q['Conservador'] or 'depois de 60'}.</p>
<table style="margin-top:14px"><tr><th>Depois do acordo</th><th>1 · Conversível</th><th>2 · Revenue share</th><th>3 · Sócio na unidade</th></tr>
<tr><td>Cotas do Lindson</td><td>diluídas se converter</td><td><b class="am">100%</b></td><td>100% da empresa; maioria da unidade</td></tr>
<tr><td>Quando o investidor recebe</td><td>na venda ou recompra</td><td>todo mês, a partir do mês 4</td><td>se a unidade distribuir lucro</td></tr></table>'''))
    S.append(('14 · Riscos e como mitigamos', '''<h2>Os riscos, <span class="am">sem maquiagem</span>.</h2><table><tr><th>Risco</th><th>Como mitigamos</th></tr>
<tr><td>Vender menos que o previsto</td><td>2ª parcela só com receita nova de R$ 10 mil/mês; tráfego só sobe com custo medido</td></tr>
<tr><td>Concentração: 3 clientes pagam tudo hoje</td><td>Por isso o dinheiro vai para aquisição; nenhuma frente nova vive do aporte para sempre</td></tr>
<tr><td>Cliente cancelar (churn)</td><td>Contrato com prazo, pagamento antecipado, multa, relatório e Central</td></tr>
<tr><td>Dependência do Lindson</td><td>Processos escritos, equipe de IA, contratação com teste pago</td></tr>
<tr><td>Dispersão em muitas frentes</td><td>Ordem do dinheiro (1º, 2º, 3º); YouTube e tecnologia sem aporte</td></tr>
<tr><td>Meta, apps e plataformas</td><td>WhatsApp, lista e área de membros próprios; Google e YouTube</td></tr>
<tr><td>Jurídico e impostos</td><td>Contador (MEI não serve para agência), contratos por advogado, LGPD, INPI, sem promessa de resultado</td></tr></table>'''))
    S.append(('15 · O time', f'''<img class="fot" src="{foto(F['time'])}"><div class="fade"></div><div style="width:840px"><h2>Quem <span class="am">executa</span>.</h2>
<p><b class="am">Lindson Almeida</b> · estrategista digital de São Luís, dono da agência, criador dos canais Passaporte da Bíblia e Raposa e Leão. Clientes pagantes hoje: Jaci, Leo Pinto e WF Celulares.</p>
<p style="margin-top:14px"><b class="am">Equipe de IA</b> · 4 contas (Lindson, Zuleide, Pedro, Leandro) com gerente (Maquiavel) e especialistas: oferta e preço (Hormozi), copy, design, sistemas, pizzaria (Paollo e Rocco), YouTube (Peter).</p>
<p style="margin-top:14px"><b class="am">Contratações</b> · criador, gestor de tráfego e account a partir do 15º cliente, com teste pago.</p>
<p style="margin-top:14px"><b class="am">Apoio</b> · contador e advogado {pf('nomes')}.</p></div>'''))
    S.append(('16 · O pedido', f'''<img class="fot" src="{foto(F['pedido'])}"><div class="fade"></div><div style="width:860px"><h2 style="font-size:110px"><span class="am">{b(ap)}</span><br>para 12 meses.</h2>
<ul><li>Faixa: R$ 80 mil a R$ 120 mil · pode ser dividido entre 2 investidores.</li>
<li>Revenue share de {P['rs_pct']*100:.0f}% sobre a receita nova, até {P['rs_teto']:.1f}x ({b(teto)}), carência de {P['rs_carencia']} meses.</li>
<li>2 parcelas: {b(P['parcela1'])} + {b(P['parcela2'])} no marco de receita nova.</li><li>Relatório mensal da Central.</li></ul>
<p style="margin-top:18px;font-size:26px"><b>Próximo passo:</b> 30 minutos para ver a Central e a planilha por dentro.</p>
<p style="margin-top:8px;font-size:21px" class="cz">WhatsApp (98) 98562-1808 · @lindsonalmeida_ · lindsonalmeida.pages.dev</p></div><div class="rod">{AVISO}</div>'''))
    return S

def _sens(M):
    out = []
    for nm, kw in [('Base', {}), ('Metade dos clientes novos', dict(mult=0.5)), ('Ticket −20%', dict(ticket_mult=0.8)), ('Churn 8%', dict(ag_churn=0.08, ot_churn=0.08)), ('Clientes novos +50%', dict(mult=1.5))]:
        r = M.projetar('Base', **kw); out.append((nm, sum(l['lucro'] for l in r['linhas']), r['linhas'][-1]['rec'], M.projetar('Base', 60, **kw)['quitado']))
    return out

def paginas_plano(c):
    b, M, mes, F, foto = c['b'], c['M'], c['mes'], c['F'], c['foto']
    P = M.P; ap = P['aporte']; teto = ap*P['rs_teto']; q = {n: c['R60'][n]['quitado'] for n in M.CEN}
    G = []
    G.append(f'''<img src="{foto(F['plano_capa'])}" style="position:absolute;right:0;top:0;width:82mm;height:297mm;object-fit:cover;object-position:center 15%">
<div style="position:absolute;right:82mm;top:0;width:30mm;height:297mm;background:linear-gradient(90deg,#0A0A0A,transparent)"></div>
<div style="width:88mm;margin-top:50mm"><span class="tag">Plano de negócios v2</span><h1 style="font-size:54px;margin-top:14px">Lindson<br>Almeida<br><span class="am">plano</span><br>investidor</h1>
<p style="margin-top:14px">Agência de marketing e tecnologia de São Luís (MA): seis frentes de receita, uma estrutura e uma equipe de IA.</p>
<p class="nota" style="margin-top:40mm;width:80mm">{AVISO}</p></div>''')
    G.append(f'''<h2>Sumário <span class="am">executivo</span></h2>
<div class="g3" style="margin-bottom:12px"><div class="box"><div class="big">{b(ap)}</div><p class="nota">pedido (R$ 80 a 120 mil)</p></div><div class="box"><div class="big">{P['rs_pct']*100:.0f}% · {P['rs_teto']:.1f}x</div><p class="nota">sobre a receita nova</p></div><div class="box"><div class="big">R$ 4.800</div><p class="nota">receita real/mês hoje</p></div></div>
<p><b>O que é.</b> Uma agência de marketing e tecnologia com seis frentes: agência para negócios locais, Orégano Turbo (pizzarias), produtos digitais, YouTube e marca pessoal, tecnologia própria e uma equipe de IA que faz o trabalho de várias pessoas.</p>
<p><b>Onde está.</b> R$ 4.800/mês de 3 clientes pagantes (Jaci, Leo Pinto, WF Celulares), 72 trabalhos no portfólio, 4 sites de clientes no ar, Central do Cliente, 7 produtos prontos e a Orégano Turbo pronta para vender.</p>
<p><b>O pedido.</b> {b(ap)} em 2 parcelas ({b(P['parcela1'])} + {b(P['parcela2'])} quando a receita nova somar R$ 10 mil/mês por 2 meses), para 12 meses de tráfego, equipamento, 1º contratado, ferramentas, jurídico e reserva.</p>
<p><b>Contrapartida sugerida.</b> {P['rs_pct']*100:.0f}% da receita nova (acima dos R$ 4.800 de hoje), do mês {P['rs_carencia']+1} até {b(teto)} ({P['rs_teto']:.1f}x), prazo máximo de {P['rs_prazo']} meses. Sem cotas e sem voto.</p>
<h3>Projeção consolidada (não é promessa)</h3>{c['tabela_cen']()}''')
    G.append('<h2>As seis <span class="am">frentes</span></h2><table><tr><th>Unidade</th><th>Situação real (15/11/2026)</th><th>Papel do aporte</th></tr>' + ''.join(f'<tr><td><b>{n}</b></td><td>{s_}</td><td>{d}</td></tr>' for n, s_, d in UNID) +
             '''</table><h3>Como as frentes se somam</h3><p>YouTube e marca pessoal trazem audiência. Os produtos de R$ 19 a 47 filtram quem ainda não pode pagar um plano. A agência e o Orégano Turbo fazem a receita recorrente, paga antes. A tecnologia (Central, robô SDR, Dublê, VEKTOR) e a equipe de IA mantêm o custo de produção baixo até 15 clientes.</p>
<h3>Problema que resolvemos</h3><ul><li>O dono de negócio local depende de indicação e de aplicativo.</li><li>Posta sem método e sem número para medir.</li><li>Agência com método custa de R$ 3.000 a R$ 6.000/mês (régua da Alpha); o resto entrega post solto.</li></ul>''')
    G.append(f'''<h2>Tração e <span class="am">ativos</span></h2><table><tr><th>Cliente pagante</th><th>Serviço</th><th>Valor/mês</th></tr>
<tr><td>Clínica Dra. Jaci Cunha</td><td>Redes, conteúdo, tráfego, site</td><td>R$ 1.500</td></tr><tr><td>Vereador Leo Pinto</td><td>Comunicação do mandato no Instagram</td><td>R$ 2.500</td></tr><tr><td>WF Celulares</td><td>Rebranding, feed e stories</td><td>R$ 800</td></tr><tr><td colspan="2"><b>Total</b></td><td class="am"><b>R$ 4.800</b></td></tr></table>
<h3>Outros ativos</h3><table><tr><th>Ativo</th><th>Situação</th></tr>
<tr><td>Carteira de trabalhos</td><td>Tribuna 98, Real Time, Desentupidora SF, Rafael Imports, curso de processo legislativo (sem recorrência paga hoje)</td></tr>
<tr><td>Portfólio</td><td>72 trabalhos no site oficial (marca 19, Instagram 17, apps 8, sites 8, vídeo 7, produtos 6, estratégia 5, YouTube 2)</td></tr>
<tr><td>Orégano Turbo</td><td>Identidade v4.1, site com planos, kit social, 57 de 84 artes, Instagram criado em 09/11/2026</td></tr>
<tr><td>Produtos digitais</td><td>Bio que Vende, Kit Mês Pronto, Kit WhatsApp que Fecha, Kit Prospecção, Raio-X do Perfil, Pack de capas, Manual de Campo; área de membros própria com liberação pela Hubla</td></tr>
<tr><td>YouTube</td><td>Passaporte da Bíblia e Raposa e Leão, longos prontos para subir {pf('inscritos e status de monetização')}</td></tr>
<tr><td>Tecnologia</td><td>Central do Cliente, painéis, robô SDR, Dublê, VEKTOR</td></tr></table>''')
    G.append(f'''<h2>Mercado e <span class="am">clientes</span></h2>
<div class="g3"><div class="box"><div class="big">40.332</div><p class="nota">pizzarias no Brasil</p></div><div class="box"><div class="big">98%</div><p class="nota">fazem delivery</p></div><div class="box"><div class="big">75%</div><p class="nota">usam aplicativo</p></div></div>
<p class="nota" style="margin-top:6px">Fonte: Apubra/Galunion, citado no roteiro OT-04 [Conferir a fonte primária e o ano].</p>
<h3>São Luís e Grande Ilha</h3><ul><li>Negócios locais ativos: {pf('nº (Receita Federal/Sebrae)')}</li><li>Pizzarias: {pf('nº (CNAE 5611-2/01 ou Google Maps)')}</li><li>A projeção Base pede {mes('Base',24)['cli']:.0f} clientes no mês 24, somando agência e Orégano.</li></ul>
<h3>Quem compra</h3><ul><li><b>Agência:</b> dono de negócio local (saúde, comércio, serviços, político), 30 a 55 anos, que depende de indicação e quer cliente no WhatsApp.</li>
<li><b>Orégano:</b> dono de pizzaria com faturamento acima de R$ 30 mil/mês, noite fraca de segunda a quarta.</li><li><b>Produtos:</b> dono ou social media que ainda não pode pagar plano.</li></ul>
<h3>Concorrência</h3><p>Franquias de marketing (Alpha: R$ 2.100 a 6.000/mês), agências locais e freelancers. Nossa posição: método, preço abaixo da franquia, entrega local e sistema próprio.</p>''')
    G.append(f'''<h2>Modelo de <span class="am">negócio</span></h2><div class="g2"><div><h3 style="margin-top:0">Agência · esteira</h3><table><tr><th>Degrau</th><th>Por mês</th></tr>
<tr><td>Vídeo (4/mês)</td><td>R$ 600</td></tr><tr><td>Tráfego</td><td>R$ 800</td></tr><tr><td>Alcance</td><td>R$ 1.200</td></tr><tr><td>Presença</td><td>R$ 2.200</td></tr><tr><td>Instagram que Vende</td><td>R$ 3.500</td></tr></table></div>
<div><h3 style="margin-top:0">Orégano Turbo</h3><table><tr><th>Plano</th><th>Por mês</th></tr><tr><td>Muralha</td><td>R$ 1.597 a 1.997</td></tr><tr><td>Fortaleza</td><td>R$ 2.197 a 2.997</td></tr><tr><td>Cidadela ▲</td><td>R$ 3.497 a 3.997</td></tr></table></div></div>
<ul style="margin-top:10px"><li>Pagamento antecipado: contrato no cartão ou Pix com desconto; nada começa sem pagamento.</li><li>Contratos de 3 meses ou mais nos degraus 3 a 5 e nos planos do Orégano.</li><li>Mini site avulso R$ 497; vídeo extra R$ 150.</li><li>Produtos: R$ 19 a 47 (sugestão), Hubla, área de membros própria.</li><li>YouTube: AdSense e venda do Manual de Campo só depois de monetizar; não projetado.</li></ul>
<h3>Máquina de vendas</h3><p>Anúncio com formulário, Reels, YouTube e robô SDR com botão de WhatsApp → filtro (quem não pode pagar recebe o produto) → diagnóstico de 30 min → proposta e contrato no mesmo dia → Central, relatório e renovação 30 dias antes.</p>''')
    G.append(f'''<h2>Uso do <span class="am">dinheiro</span></h2>{c['tabela_uso']()}
<h3>A ordem (o conselho do Maquiavel)</h3><ol style="padding-left:18px"><li><b>Onde já rende:</b> agência (já vende e recebe), equipamento, ferramentas, jurídico e reserva.</li><li><b>O que está pronto:</b> Orégano Turbo e o 1º criador, com a 2ª parcela presa à tração.</li><li><b>O teste:</b> produtos, R$ 600/mês, para se o retorno do tráfego ficar abaixo de 1x.</li></ol>
<p>YouTube e tecnologia não recebem aporte: rodam com a equipe de IA. Quem depende de armas alheias vive da sorte de outro (<i>Príncipe</i> XIII, em paráfrase).</p>
<h3>Regras</h3><ul><li>Conta separada e extrato mensal ao investidor.</li><li>Reserva intocada até o mês 6.</li><li>Pró-labore de R$ 3.000/mês [confirmar].</li></ul>''')
    linhas = ''.join(f'<tr><td>{m}</td>' + ''.join(f'<td>{mes(n,m)["cli"]:.0f}</td><td>{b(mes(n,m)["rec"])}</td><td>{b(mes(n,m)["lucro"])}</td>' for n in M.CEN) + '</tr>' for m in (1, 3, 6, 9, 12, 15, 18, 21, 24))
    G.append(f'''<h2>Projeção <span class="am">24 meses</span></h2><p>Projeção, não promessa. Premissas editáveis na planilha (células amarelas); uma aba por unidade e o consolidado.</p>
<table><tr><th rowspan="2">Mês</th><th colspan="3">Conservador</th><th colspan="3">Base</th><th colspan="3">Otimista</th></tr><tr>{'<th>Clientes</th><th>Receita</th><th>Lucro</th>'*3}</tr>{linhas}</table>
<h3>Premissas por unidade</h3><ul><li><b>Agência:</b> base de R$ 4.800 mantida; novos 0,5 · 1 · 1,5 por mês; ticket R$ 1.200 · 2.200 · 2.800 (esteira); churn 6% · 5% · 4%.</li>
<li><b>Orégano:</b> novos 1 · 2 · 3 por mês com rampa; ticket R$ 2.000 · 2.400 · 2.700; churn 7% · 5% · 3%.</li><li><b>Produtos:</b> R$ 600/mês de tráfego nos meses 2 a 11; preço R$ 37; custo por venda R$ 45 · 30 · 22; taxa da plataforma 10% [Conferir].</li>
<li><b>Custos:</b> fixos R$ 1.500 + ferramentas R$ 500 + pró-labore R$ 3.000; R$ 150 por cliente; 6% de imposto [Conferir]; criador nos meses 4 a 9; equipe acima de 15 clientes.</li><li>YouTube e tecnologia: sem receita projetada.</li></ul>''')
    sens = _sens(M)
    G.append(f'''<h2>Unit economics e <span class="am">sensibilidade</span></h2>{c['tabela_unit']()}
<h3>Sensibilidade do cenário Base</h3><table><tr><th>Variação</th><th>Lucro em 24 meses</th><th>Receita no mês 24</th><th>Teto do revenue share</th></tr>''' + ''.join(f'<tr><td>{a}</td><td>{b(l)}</td><td>{b(r_)}</td><td>{("mês " + str(qq)) if qq else "depois de 60"}</td></tr>' for a, l, r_, qq in sens) + '''</table>
<h3>As 5 premissas mais sensíveis</h3><ol style="padding-left:18px"><li>Clientes novos por mês (agência e Orégano): ainda não medidos com tráfego.</li><li>Churn mensal: contratos novos, sem histórico.</li><li>Ticket médio dos novos (que degrau ou plano escolhem).</li><li>Manter os 3 contratos atuais (R$ 4.800, concentrados em 3 clientes).</li><li>Custo da equipe acima de 15 clientes.</li></ol>''')
    G.append(f'''<h2>Estrutura do <span class="am">investimento</span></h2><table><tr><th>Estrutura</th><th>Para o investidor</th><th>Para o Lindson</th></tr>
<tr><td><b>1 · Mútuo conversível / anjo</b> (LC 155/2016) sobre a empresa toda</td><td>+ pode virar sócio com desconto; não responde por dívidas. − retorno só com venda ou recompra.</td><td>+ sem pagamento mensal. − dilui a empresa toda; exige valuation.</td></tr>
<tr><td><b>2 · Revenue share sobre a receita nova</b> ★</td><td>+ recebe todo mês do mês {P['rs_carencia']+1}; teto claro; relatório. − sem garantia; se a receita nova não vier, recebe menos.</td><td>+ 100% das cotas e das decisões. − {P['rs_pct']*100:.0f}% da receita nova até o teto.</td></tr>
<tr><td><b>3 · Sócio numa unidade</b> (ex.: Orégano Turbo separada)</td><td>+ cotas da unidade. − só uma frente; depende de distribuição de lucro.</td><td>+ o resto da empresa fica fora. − CNPJ e acordo de sócios.</td></tr></table>
<h3>Recomendação: revenue share sobre a receita nova</h3><p>{P['rs_pct']*100:.0f}% de tudo o que a empresa faturar acima dos R$ 4.800/mês de hoje, a partir do mês {P['rs_carencia']+1}, até {b(teto)} ({P['rs_teto']:.1f}x), prazo máximo de {P['rs_prazo']} meses. Na projeção, o teto chega no mês {q['Base']} (base), {q['Otimista']} (otimista) e {q['Conservador'] or 'depois do 60'} (conservador).</p>
<p><b>Por que não sobre a receita total:</b> os R$ 4.800 existiam antes do dinheiro; cobrar sobre eles tiraria do caixa o que o investidor não criou. <b>Por que não só sobre as unidades financiadas:</b> a separação entre unidades exigiria contabilidade por frente e abriria discussão sobre cada real. A receita nova da empresa é simples de conferir na Central e no extrato.</p>
<p><b>O conselho do Maquiavel:</b> quem traz o dinheiro não deve levar a chave da casa. O revenue share paga o capital com o próprio resultado e devolve a casa inteira no teto.</p>
<h3>Cuidados legais</h3><ul><li>Conversa privada, sem oferta pública (CVM). [Conferir com advogado]</li><li>Contrato por advogado; tributação com contador. [Conferir]</li><li>Nenhuma promessa de retorno.</li></ul>''')
    G.append(f'''<h2>Riscos e <span class="am">mitigação</span></h2><table><tr><th>Risco</th><th>Prob.</th><th>Mitigação</th></tr>
<tr><td>Vender menos que o previsto</td><td>Média</td><td>2ª parcela só com receita nova de R$ 10 mil/mês; tráfego só sobe com custo medido</td></tr>
<tr><td>Concentração em 3 clientes</td><td>Alta</td><td>O dinheiro vai para aquisição; meta de diversificar a carteira até o mês 6</td></tr>
<tr><td>Churn</td><td>Média</td><td>Prazo mínimo, pagamento antecipado, multa, relatório, ouvidoria</td></tr>
<tr><td>Dependência do Lindson</td><td>Alta</td><td>Processos escritos, equipe de IA, contratação com teste pago; seguro {pf('avaliar')}</td></tr>
<tr><td>Dispersão em muitas frentes</td><td>Média</td><td>Ordem do dinheiro; YouTube e tecnologia sem aporte; produtos só se pagarem</td></tr>
<tr><td>Plataformas (Meta, Hubla, YouTube)</td><td>Média</td><td>WhatsApp, lista, área de membros e sites próprios</td></tr>
<tr><td>Jurídico (CDC, LGPD, eleitoral no cliente político)</td><td>Baixa a média</td><td>Sem promessa de resultado; dados só com autorização; regras eleitorais [Conferir]</td></tr>
<tr><td>Uso indevido do dinheiro</td><td>Baixa</td><td>Conta separada, extrato mensal, uso no contrato</td></tr></table>
<h3>Relatório mensal ao investidor</h3><ul><li>Receita por unidade e receita nova.</li><li>Clientes ativos, novos e cancelados.</li><li>Uso do dinheiro com extrato e valor do revenue share.</li><li>CAC e custo por diagnóstico.</li></ul>''')
    G.append(f'''<img src="{foto(F['plano_time'])}" style="float:right;width:62mm;height:90mm;object-fit:cover;object-position:center 15%;margin:0 0 8mm 8mm">
<h2>O <span class="am">time</span></h2><p><b>Lindson Almeida</b> · estrategista digital de São Luís (MA), dono da agência, criador dos canais Passaporte da Bíblia e Raposa e Leão. Faz venda, estratégia e gravação.</p>
<p><b>Equipe de IA</b> · 4 contas (Lindson, Zuleide, Pedro, Leandro) com gerente (Maquiavel) e especialistas: Hormozi, Copy, Design, Builder, Paollo e Rocco, Peter.</p>
<p><b>Contratações</b> · criador (R$ 2.080), gestor de tráfego (R$ 2.080) e account (R$ 3.000), a partir do 15º cliente, com teste pago de 1 semana.</p>
<p><b>Apoio</b> · contador {pf('nome')} e advogado {pf('nome')}.</p><div style="clear:both"></div>
<h3>Próximos passos</h3><ol style="padding-left:18px"><li>Reunião de 30 minutos: Central e planilha ao vivo.</li><li>Escolha da estrutura; advogado redige o contrato.</li><li>Conta separada, assinatura e 1ª parcela.</li><li>Relatório mensal a partir do mês 1.</li></ol>
<div class="box" style="margin-top:10mm"><p><b>Contato</b> · WhatsApp (98) 98562-1808 · @lindsonalmeida_ · lindsonalmeida.pages.dev</p></div><p class="nota" style="margin-top:8mm">{AVISO}</p>''')
    return G

def onepager(c):
    b, M, mes, F, foto = c['b'], c['M'], c['mes'], c['F'], c['foto']
    P = M.P; ap = P['aporte']; teto = ap*P['rs_teto']
    uso = ''.join(f'<tr><td style="font-size:11px;padding:3px 6px">{a}</td><td style="text-align:right;font-size:11px;padding:3px 6px"><b>{b(v)}</b></td></tr>' for un, a, d, v, qq, p in M.USO)
    cen = ''.join(f'<tr><td><b>{n}</b></td><td>{b(mes(n,12)["rec"])}</td><td>{b(mes(n,24)["rec"])}</td></tr>' for n in M.CEN)
    return f'''<div style="display:flex;gap:8mm;align-items:center"><div style="flex:1"><span class="tag">One-pager · investidor</span>
<h1 style="font-size:44px;margin-top:8px">Lindson Almeida:<br><span class="am">marketing e tecnologia</span></h1>
<p style="margin-top:6px">São Luís (MA) · R$ 4.800/mês de receita real (Jaci, Leo Pinto, WF) · 72 trabalhos no portfólio · seis frentes.</p></div>
<img src="{foto(F['one'])}" style="width:44mm;height:54mm;object-fit:cover;object-position:center 15%"></div>
<div class="g2" style="margin-top:3mm"><div>
<h3>As seis frentes</h3><ul><li><b>Agência</b> para negócios locais (esteira R$ 600 a 3.500/mês)</li><li><b>Orégano Turbo</b>, só pizzarias (R$ 1.597 a 3.997/mês), pronta</li><li><b>Produtos digitais</b> na Hubla, área de membros própria</li><li><b>YouTube</b> e marca pessoal</li><li><b>Tecnologia</b>: Central do Cliente, robô SDR, Dublê, VEKTOR</li><li><b>Equipe de IA</b>: 4 contas e agentes, custo baixo</li></ul>
<h3>Ordem do dinheiro</h3><p>1º onde já rende (agência), 2º o que está pronto (Orégano), 3º o teste (produtos). YouTube e tecnologia sem aporte.</p>
<h3>Marcos</h3><ul><li><b>6 meses:</b> 5 pizzarias fundadoras; CAC medido</li><li><b>12 meses:</b> cases; equipe a partir do 15º cliente</li></ul>
</div><div>
<h3>O pedido: {b(ap)}</h3><table>{uso}</table>
<p style="margin-top:3px">2 parcelas: {b(P['parcela1'])} + {b(P['parcela2'])} com receita nova de R$ 10 mil/mês.</p>
<h3>Estrutura sugerida</h3><p>{P['rs_pct']*100:.0f}% da receita nova (acima dos R$ 4.800) do mês {P['rs_carencia']+1} até {b(teto)} ({P['rs_teto']:.1f}x), máximo {P['rs_prazo']} meses. Sem cotas, sem voto.</p>
<h3>Projeção (receita/mês)</h3><table><tr><th>Cenário</th><th>Mês 12</th><th>Mês 24</th></tr>{cen}</table>
</div></div>
<div class="g2" style="margin-top:2mm"><div><h3>Clientes pagantes hoje</h3><p>Clínica Dra. Jaci Cunha R$ 1.500 · Vereador Leo Pinto R$ 2.500 · WF Celulares R$ 800 por mês.</p></div>
<div><h3>Riscos que tratamos</h3><ul><li>Concentração em 3 clientes: o dinheiro vai para aquisição</li><li>Vender menos: 2ª parcela só com tração</li><li>Pessoa-chave: processos e equipe de IA</li></ul></div></div>
<div class="box" style="margin-top:4mm;padding:8px 12px"><p><b>Próximo passo:</b> 30 minutos para ver a Central e a planilha ao vivo · WhatsApp (98) 98562-1808 · @lindsonalmeida_</p></div>
<p class="nota" style="margin-top:3mm;font-size:9px">{AVISO}</p>'''
