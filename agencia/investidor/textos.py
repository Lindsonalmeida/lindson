"""Textos do deck, do plano e do one-pager (conta Lindson, Maquiavel gerente, 15/11/2026).
Tudo o que é número vem de modelo.py. Campos [preencher: ...] são dados que só o Lindson tem."""

FALTA = '<span style="background:#F5C518;color:#0A0A0A;font-weight:800;padding:0 6px">[preencher: {}]</span>'
def pf(x): return FALTA.format(x)

AVISO = ('Conversa privada com pessoa convidada, sem oferta pública de valores mobiliários. Projeções são estimativas com premissas '
         'explícitas, não promessa de resultado nem de retorno. A estrutura final passa por advogado e contador.')

def funil():
    itens = [('15', 'contatos/mês', '#1C1C1C', '#fff'), ('13', 'marcam diagnóstico', '#2a2a2a', '#fff'), ('9', 'comparecem', '#3a3a3a', '#fff'), ('4', 'fecham', '#F5C518', '#0A0A0A')]
    return '<div style="display:flex;margin-top:26px">' + ''.join(f'<div style="flex:1;background:{bg};color:{cor};padding:16px 20px"><div class="an" style="font-size:56px">{n}</div><p style="font-size:21px;color:{cor}">{t}</p></div>' for n, t, bg, cor in itens) + '</div><p class="cz" style="font-size:19px;margin-top:6px">Metas do funil na fase de equipe (README da operação própria): premissa a medir.</p>'

def cards_cen(c):
    b, M, mes = c['b'], c['M'], c['mes']
    return ''.join(f'<div class="box" style="margin-bottom:14px;padding:16px 22px"><p><b class="am">{n}</b> <span class="cz" style="font-size:19px">{M.CEN[n]["novos_d"]} novos/mês · ticket {b(M.CEN[n]["ticket"])} · churn {M.CEN[n]["churn"]*100:.0f}%</span></p><p style="font-size:22px">Mês 12: {mes(n,12)["cli"]:.0f} clientes · {b(mes(n,12)["rec"])}/mês<br>Mês 24: {mes(n,24)["cli"]:.0f} clientes · {b(mes(n,24)["rec"])}/mês<br><span class="cz">Lucro em 24 meses: {b(c["luc24"](n))}</span></p></div>' for n in M.CEN)

def slides_deck(c):
    b, M, mes, F, foto = c['b'], c['M'], c['mes'], c['F'], c['foto']
    ap = M.P['aporte']; teto = ap*M.P['rs_teto']
    q = {n: c['R60'][n]['quitado'] for n in M.CEN}
    S = []
    S.append(('Plano investidor · 2026', f'''
<img class="fot" src="{foto(F['capa'])}"><div class="fade"></div>
<div style="position:absolute;top:220px;left:90px;width:900px">
<span class="tag">Operação Orégano Turbo · marketing para pizzarias</span>
<h1 style="font-size:132px;margin-top:26px">Capital para<br><span class="am">acelerar</span> o que<br>já funciona.</h1>
<p style="font-size:24px;margin-top:26px;color:#cfcfcf;max-width:760px">Lindson Almeida · estrategista digital · São Luís (MA)</p></div>
<div class="rod">{AVISO}</div>'''))
    S.append(('01 · O problema', '''
<h2>O dono de pizzaria<br>anuncia no <span class="am">escuro</span>.</h2>
<div class="g3" style="margin-top:40px">
<div class="box"><div class="big">1</div><p style="margin-top:12px"><b>Depende de app e de indicação.</b> O pedido vem do aplicativo, que fica com uma parte, ou do boca a boca, que não se controla.</p></div>
<div class="box"><div class="big">2</div><p style="margin-top:12px"><b>Posta sem método.</b> Instagram parado ou bonito, mas sem anúncio que leve ao WhatsApp nem número para medir.</p></div>
<div class="box"><div class="big">3</div><p style="margin-top:12px"><b>Agência cara ou amadora.</b> Quem tem método cobra de R$ 3.000 a R$ 6.000/mês (régua da Alpha, prints de 05/11/2026); o resto entrega post solto.</p></div>
</div>
<div class="box" style="margin-top:34px;border-top-color:#fff"><p><b class="am">Quem é o cliente:</b> dono ou sócio de pizzaria, 30 a 55 anos, na loja à noite e nas compras de dia. Sofre com a noite fraca de segunda a quarta, já pagou "social media" que não trouxe pedido e confia em quem aparece na loja e mostra número simples toda semana.</p></div>'''))
    S.append(('02 · A solução', f'''
<img class="fot" src="{foto(F['solucao'])}"><div class="fade"></div>
<div style="width:840px"><h2>Anúncio, Instagram<br>e WhatsApp, com o<br><span class="am">número na mesa</span>.</h2>
<ul style="margin-top:10px">
<li><b>Assessoria só para pizzarias</b> (nicho único: método, vitrine e cases no mesmo setor).</li>
<li><b>Criativos gravados na pizzaria</b>, tráfego para pedido no WhatsApp ou cardápio digital, iFood organizado.</li>
<li><b>Relatório toda segunda</b> na Central do Cliente: investimento, conversas, custo por conversa.</li>
<li><b>Contrato com prazo e pagamento antecipado</b> (mensal ou contrato inteiro no cartão).</li>
<li><b>Garantia de entrega</b>, nunca de resultado: se não entregarmos o combinado, o mês não é cobrado.</li></ul></div>'''))
    S.append(('03 · O que já existe (sem o seu dinheiro)', '''
<h2>A fábrica já está <span class="am">montada</span>.</h2>
<div class="g4" style="margin-top:30px">
<div class="box"><div class="big">R$ 4.800</div><p><b>por mês de receita atual</b>, de 3 clientes pagantes: Dra. Jaci, Leo Pinto e WF Celulares.</p></div>
<div class="box"><div class="big">72</div><p><b>trabalhos no portfólio</b> do site oficial: marca, Instagram, sites, apps, vídeo, estratégia.</p></div>
<div class="box"><div class="big">4</div><p><b>sites de clientes no ar</b> (pages.dev): Jaci, Tribuna 98, Desentupidora SF e Rafael Imports.</p></div>
<div class="box"><div class="big">1</div><p><b>Central do Cliente</b>: painel por cliente com aprovações, entregas, pagamentos e relatório.</p></div>
</div>
<div class="g2" style="margin-top:28px">
<div><p><b class="am">Orégano Turbo pronta para vender:</b> identidade v4.1 e manual, site com planos e formulário, kit social, linhas editoriais, 57 de 84 artes do calendário, Instagram criado em 09/11/2026, agentes de pizzaria (Paollo e Rocco).</p></div>
<div><p><b class="am">Operação com equipe Claude:</b> 4 contas de IA e agentes especialistas (gerência, oferta, copy, design, sistemas, YouTube) trabalhando no mesmo repositório, com processos escritos.</p></div></div>'''))
    S.append(('04 · Tração real', f'''
<h2>Tração: o que é <span class="am">fato</span> hoje.</h2>
<table style="margin-top:14px"><tr><th>Indicador</th><th>Situação real (repositório, 15/11/2026)</th></tr>
<tr><td>Clientes pagantes</td><td>3: Dra. Jaci R$ 1.500, Leo Pinto R$ 2.500, WF Celulares R$ 800 (por mês)</td></tr>
<tr><td>Outros trabalhos entregues</td><td>Tribuna 98 e Real Time (sites e conteúdo, sem pagamento hoje), Desentupidora SF, Rafael Imports</td></tr>
<tr><td>Faturamento mensal da agência</td><td><b>R$ 4.800/mês</b> (base atual; entra na projeção somada às pizzarias)</td></tr>
<tr><td>Clientes pizzaria (Orégano Turbo)</td><td>0 · operação pronta para a primeira venda; meta aprovada: 5 fundadoras em 60 dias</td></tr>
</table>
<div class="g3" style="margin-top:24px"><div class="box"><p><b class="am">Confira ao vivo</b><br>Central do Cliente, sites no ar e portfólio em lindsonalmeida.pages.dev</p></div>
<div class="box"><p><b class="am">Próximo marco</b><br>5 pizzarias fundadoras em 60 dias (meta aprovada)</p></div>
<div class="box"><p><b class="am">Sem exagero</b><br>Resultado de cliente só com autorização escrita (LGPD)</p></div></div>'''))
    S.append(('05 · O mercado', f'''
<h2>Um nicho grande,<br>atendido <span class="am">mal</span>.</h2>
<div class="g3" style="margin-top:20px">
<div class="box"><div class="big">40.332</div><p>pizzarias no Brasil</p></div>
<div class="box"><div class="big">98%</div><p>fazem delivery</p></div>
<div class="box"><div class="big">75%</div><p>usam aplicativo para receber pedido</p></div></div>
<p class="cz" style="margin-top:12px;font-size:20px">Fonte: Apubra/Galunion, como citado no roteiro OT-04 do repositório [Conferir a fonte primária e o ano antes da reunião].</p>
<div class="box" style="margin-top:24px"><p><b>São Luís e Grande Ilha:</b> {pf('nº de pizzarias ativas (Receita Federal, CNAE 5611-2/01, ou Google Maps)')} · com faturamento acima de R$ 30 mil/mês (o corte do nosso formulário): {pf('estimativa')}.<br>
A capacidade do plano é pequena perto disso: <b>15 pizzarias</b> com o Lindson sozinho; a projeção Base chega a <b>{mes('Base',24)['cli']:.0f}</b> no mês 24.</p></div>'''))
    S.append(('06 · Modelo de negócio', '''
<h2>Preços <span class="am">aprovados</span> e<br>pagamento antecipado.</h2>
<table><tr><th>Plano (por mês)</th><th>Trimestral</th><th>Semestral</th><th>Anual</th><th>Para quem</th></tr>
<tr><td><b>Muralha</b></td><td>R$ 1.997</td><td>R$ 1.797</td><td>R$ 1.597</td><td>4 criativos, tráfego, cardápio digital</td></tr>
<tr><td><b>Fortaleza</b> (principal)</td><td>R$ 2.997</td><td>R$ 2.597</td><td>R$ 2.197</td><td>+ Instagram, iFood, 8 criativos, diária mensal</td></tr>
<tr><td><b>Cidadela ▲</b></td><td>R$ 3.997</td><td>R$ 3.697</td><td>R$ 3.497</td><td>+ relatório semanal, reunião, exclusividade no bairro</td></tr></table>
<div class="g3" style="margin-top:26px">
<div class="box"><p><b>Antecipado sempre</b><br>Contrato inteiro no cartão (até 12x) ou Pix com 5%; nada começa sem pagamento.</p></div>
<div class="box"><p><b>Entrada barata</b><br>Raio-X da Pizzaria por R$ 297, abatido se fechar em 7 dias.</p></div>
<div class="box"><p><b>Verba de anúncio</b><br>Paga pela pizzaria direto à Meta, mínimo R$ 1.000/mês. Não passa pelo nosso caixa.</p></div></div>
<p class="cz" style="margin-top:14px;font-size:20px">Fonte: DECISOES-APROVADAS.md (05/11/2026). Também seguem ativos os planos da agência (esteira de R$ 600 a R$ 3.500/mês).</p>'''))
    S.append(('07 · A máquina de vendas', '''
<h2>Como o dinheiro<br>vira <span class="am">cliente</span>.</h2>
<div style="display:flex;gap:14px;margin-top:30px">''' + ''.join(f'<div class="box" style="flex:1"><div class="an am" style="font-size:38px">{a}</div><p style="font-size:23px;margin-top:8px">{t}</p></div>' for a, t in [
        ('Atrair', 'Anúncio com formulário, Reels, YouTube, app SDR com botão de WhatsApp'),
        ('Filtrar', 'Faturamento ≥ R$ 30 mil e R$ 1.000 de verba; quem não passa recebe o Raio-X'),
        ('Diagnóstico', '30 min mostrando o perfil por dentro'),
        ('Fechar', 'Proposta com 3 planos, contrato e cartão no mesmo dia'),
        ('Reter', 'Relatório de segunda, ouvidoria, renovação 30 dias antes')]) + '''</div>
''' + funil() + '''<p style="margin-top:18px"><b>Regra de verba:</b> R$ 30/dia nos 2 primeiros meses; só sobe se o custo por diagnóstico ficar abaixo de R$ 150 (decisão aprovada). <b>O aporte acelera esse passo</b>, e só depois de medido.</p>'''))
    S.append(('08 · Uso do dinheiro', f'''
<h2>{b(ap)}: para onde <span class="am">vai</span>.</h2>
<div class="tuso">{c['tabela_uso']()}</div>
<p style="margin-top:14px;font-size:23px" class="cz">Aporte em 2 parcelas: {b(40000)} na assinatura e {b(30000)} quando a operação tiver 5 pizzarias pagantes (marco verificável na Central). Itens marcados [estimativa] terão orçamento antes da assinatura.</p>'''))
    S.append(('09 · Projeção em 3 cenários', f'''
<h2>Receita mensal <span class="am">projetada</span>.</h2>
<div class="g2" style="grid-template-columns:1.15fr 1fr;gap:50px"><div>{c['barras']('rec')}</div><div>{cards_cen(c)}</div></div>
<p class="cz" style="margin-top:14px;font-size:25px">Projeção, não promessa. Premissas: clientes novos por mês, ticket e churn por cenário; custos de PRECOS-PIZZARIAS.md; equipe a partir do 16º cliente; pró-labore R$ 3.000 a partir do 3º. Receita inclui os R$ 4.800/mês atuais da agência. Planilha anexa.</p>'''))
    S.append(('10 · Unit economics', f'''
<h2>Cada cliente <span class="am">se paga</span> rápido?</h2>
<div class="g2" style="grid-template-columns:1.25fr 1fr;gap:50px"><div>{c['tabela_unit']()}</div>
<div><p><b class="am">Como ler</b></p><ul><li>O CAC ainda é <b>premissa</b>: o primeiro uso do dinheiro é medi-lo de verdade.</li>
<li>Olhe o LTV limitado a 12 meses, não o teórico.</li><li>O número que mais move o plano é o <b>churn</b> (veja a sensibilidade na planilha).</li>
<li>Pagamento antecipado faz o caixa entrar antes do custo.</li></ul></div></div>'''))
    S.append(('11 · Marcos', f'''
<h2>O que você vai <span class="am">ver</span>, e quando.</h2>
<div class="g3" style="margin-top:20px">
<div class="box"><div class="big">6 meses</div><ul style="margin-top:12px"><li>5 fundadoras fechadas (meta: 60 dias)</li><li>Funil medido: custo por diagnóstico e CAC reais</li><li>Base: ~{mes('Base',6)['cli']:.0f} pizzarias, {b(mes('Base',6)['rec'])}/mês</li><li>1º criador em teste pago</li></ul></div>
<div class="box"><div class="big">12 meses</div><ul style="margin-top:12px"><li>Primeiros cases com autorização</li><li>Revisão de preços com números reais</li><li>Base: ~{mes('Base',12)['cli']:.0f} pizzarias, {b(mes('Base',12)['rec'])}/mês</li><li>Equipe a partir do 16º cliente</li></ul></div>
<div class="box"><div class="big">18 meses</div><ul style="margin-top:12px"><li>Operação rodando com equipe</li><li>Base: ~{mes('Base',18)['cli']:.0f} pizzarias, {b(mes('Base',18)['rec'])}/mês</li><li>Avaliar segunda cidade ou nicho vizinho</li></ul></div></div>
<p class="cz" style="margin-top:18px;font-size:20px">Valores do cenário Base: projeção. Relatório mensal ao investidor com os números reais da Central.</p>'''))
    S.append(('12 · Estrutura do investimento', f'''
<h2>Três formatos. <span class="am">Um</span> recomendado.</h2>
<div class="g3">
<div class="box"><p class="an" style="font-size:32px">1 · Mútuo conversível / anjo (LC 155/2016)</p><p style="font-size:23px;margin-top:8px"><b>Você:</b> pode virar sócio no futuro com desconto. <b>Contra:</b> retorno só se houver venda ou recompra; o Lindson dilui.</p></div>
<div class="box" style="border-top:8px solid #F5C518;background:#262106"><p class="an am" style="font-size:32px">2 · Revenue share com teto ★</p><p style="font-size:23px;margin-top:8px">{M.P['rs_pct']*100:.0f}% da receita da operação de pizzarias, a partir do mês {M.P['rs_carencia']+1}, até {M.P['rs_teto']:.1f}x o aporte ({b(teto)}), prazo máximo {M.P['rs_prazo']} meses. <b>Você:</b> recebe todo mês, sem esperar venda. <b>Contra:</b> sem garantia; se a receita não vier, recebe menos.</p></div>
<div class="box"><p class="an" style="font-size:32px">3 · Sócio na unidade Orégano Turbo</p><p style="font-size:23px;margin-top:8px"><b>Você:</b> cotas minoritárias e dividendos de uma empresa separada. <b>Contra:</b> acordo de sócios, contabilidade própria, retorno só se distribuir lucro.</p></div></div>
<p style="margin-top:22px;font-size:25px"><b class="am">Por que a 2:</b> o investidor vê dinheiro voltando todo mês e o Lindson mantém 100% das cotas e das decisões. Teto atingido (projeção, 60 meses): conservador mês {q['Conservador'] or '>60'}, base mês {q['Base']}, otimista mês {q['Otimista']}.</p>
<table style="margin-top:16px"><tr><th>Quem manda depois</th><th>1 · Conversível</th><th>2 · Revenue share</th><th>3 · Sócio na unidade</th></tr>
<tr><td>Cotas do Lindson</td><td>diluídas se converter</td><td><b class="am">100%</b></td><td>100% da agência; maioria da unidade</td></tr></table>'''))
    S.append(('13 · Riscos e como mitigamos', '''
<h2>Os riscos, <span class="am">sem maquiagem</span>.</h2>
<table><tr><th>Risco</th><th>Como mitigamos</th></tr>
<tr><td>Vender menos que o previsto</td><td>Aporte em 2 parcelas (a 2ª só com 5 pizzarias pagantes); verba de tráfego só sobe com custo medido</td></tr>
<tr><td>Cliente cancelar cedo (churn)</td><td>Contrato com prazo, pagamento antecipado, multa de 20%, relatório de segunda, ouvidoria</td></tr>
<tr><td>Dependência do Lindson</td><td>Processos escritos, equipe Claude, contratação com teste pago de 1 semana</td></tr>
<tr><td>Dependência da Meta e do app</td><td>WhatsApp e lista próprios, Google e YouTube, cardápio digital do cliente</td></tr>
<tr><td>Jurídico e impostos</td><td>Contador (MEI não serve para agência), contratos por advogado, LGPD, INPI da marca, sem promessa de resultado</td></tr>
<tr><td>Concorrência (Alpha e agências locais)</td><td>Nicho único, preço 16% a 36% abaixo da Alpha, Central do Cliente e entrega local</td></tr>
<tr><td>Uso indevido do dinheiro</td><td>Conta separada, extrato mensal ao investidor, uso definido em contrato</td></tr></table>'''))
    S.append(('14 · O time', f'''
<img class="fot" src="{foto(F['time'])}"><div class="fade"></div>
<div style="width:840px"><h2>Quem <span class="am">executa</span>.</h2>
<p><b class="am">Lindson Almeida</b> · estrategista digital de São Luís, dono de agência de gestão de redes sociais, criador dos canais Passaporte da Bíblia e Raposa e Leão. Clientes pagantes hoje: Jaci, Leo Pinto e WF Celulares.</p>
<p style="margin-top:16px"><b class="am">Equipe Claude</b> · 4 contas de IA trabalhando no mesmo repositório, com gerente (Maquiavel) e especialistas de oferta e preço (Hormozi), copy, design, sistemas (Builder), pizzaria (Paollo e Rocco) e YouTube (Peter).</p>
<p style="margin-top:16px"><b class="am">Próximas contratações</b> · criador (grava e edita), gestor de tráfego e account, a partir do 16º cliente, cada um com teste pago antes.</p>
<p style="margin-top:16px"><b class="am">Apoio</b> · contador e advogado {pf('nomes')}.</p></div>'''))
    S.append(('15 · O pedido', f'''
<img class="fot" src="{foto(F['pedido'])}"><div class="fade"></div>
<div style="width:860px"><h2 style="font-size:110px"><span class="am">{b(ap)}</span><br>para 12 meses.</h2>
<ul><li>Faixa aceita: R$ 50 mil a R$ 80 mil · pode ser dividido entre 2 investidores.</li>
<li>Formato sugerido: revenue share de {M.P['rs_pct']*100:.0f}% até {M.P['rs_teto']:.1f}x ({b(teto)}), carência de {M.P['rs_carencia']} meses.</li>
<li>Em 2 parcelas: {b(40000)} + {b(30000)} no marco de 5 pizzarias.</li>
<li>Relatório mensal com os números reais da Central.</li></ul>
<p style="margin-top:22px;font-size:24px"><b>Próximo passo:</b> 30 minutos para você ver a Central e a planilha por dentro.</p>
<p style="margin-top:10px;font-size:23px" class="cz">WhatsApp (98) 98562-1808 · @lindsonalmeida_ · lindsonalmeida.pages.dev</p></div>
<div class="rod">{AVISO}</div>'''))
    return S

def paginas_plano(c):
    b, M, mes, F, foto = c['b'], c['M'], c['mes'], c['F'], c['foto']
    ap = M.P['aporte']; teto = ap*M.P['rs_teto']; q = {n: c['R60'][n]['quitado'] for n in M.CEN}
    P = []
    P.append(f'''<img src="{foto(F['plano_capa'])}" style="position:absolute;right:0;top:0;width:82mm;height:297mm;object-fit:cover;object-position:center 15%">
<div style="position:absolute;right:82mm;top:0;width:30mm;height:297mm;background:linear-gradient(90deg,#0A0A0A,transparent)"></div>
<div style="width:88mm;margin-top:50mm"><span class="tag">Plano de negócios · 15/11/2026</span>
<h1 style="font-size:58px;margin-top:14px">Orégano<br>Turbo<br><span class="am">plano</span><br>investidor</h1>
<p style="margin-top:14px;font-size:14px">Marketing para pizzarias de São Luís (MA), com o método e a estrutura da agência de Lindson Almeida.</p>
<p class="nota" style="margin-top:40mm;width:80mm">{AVISO}</p></div>''')
    P.append(f'''<h2>Sumário <span class="am">executivo</span></h2>
<div class="g3" style="margin:10px 0 14px"><div class="box"><div class="big">{b(ap)}</div><p class="nota">pedido (faixa R$ 50 a 80 mil)</p></div>
<div class="box"><div class="big">{M.P['rs_pct']*100:.0f}% · {M.P['rs_teto']:.1f}x</div><p class="nota">revenue share com teto (recomendado)</p></div>
<div class="box"><div class="big">R$ 4.800</div><p class="nota">receita atual/mês (3 pagantes)</p></div></div>
<p><b>O que é.</b> Uma assessoria de marketing só para pizzarias (Orégano Turbo), com três planos com prazo (Muralha, Fortaleza e Cidadela), pagamento antecipado, relatório de segunda e a Central do Cliente. Nasce dentro de uma agência que já fatura R$ 4.800/mês com 3 clientes pagantes e tem 72 trabalhos publicados no portfólio.</p>
<p><b>Por que agora.</b> A operação está pronta para vender (identidade, site com planos, kit social, contrato, preços aprovados). Falta dinheiro para acelerar a aquisição de clientes (tráfego), gravar com qualidade (equipamento) e contratar o primeiro criador antes que o Lindson chegue ao limite de 15 clientes sozinho.</p>
<p><b>O pedido.</b> {b(ap)} em 2 parcelas ({b(40000)} na assinatura e {b(30000)} com 5 pizzarias pagantes), para 12 meses de uso.</p>
<p><b>A contrapartida sugerida.</b> {M.P['rs_pct']*100:.0f}% da receita bruta da operação de pizzarias, a partir do mês {M.P['rs_carencia']+1}, até atingir {M.P['rs_teto']:.1f}x o aporte ({b(teto)}), com prazo máximo de {M.P['rs_prazo']} meses. Sem cotas, sem voto, com relatório mensal.</p>
<h3>Projeção resumida (não é promessa)</h3>{c['tabela_cen']((12,24))}
<p class="nota" style="margin-top:8px">Teto do revenue share atingido no mês {q['Base']} (base), {q['Otimista']} (otimista) e {q['Conservador'] or 'depois do mês 60'} (conservador).</p>''')
    P.append(f'''<h2>Problema e <span class="am">solução</span></h2>
<h3>O problema do dono de pizzaria</h3><ul>
<li>Pedido concentrado no aplicativo (que fica com parte da venda) e no boca a boca.</li>
<li>Instagram sem método: posta, mas não há anúncio que leve ao WhatsApp nem número para medir.</li>
<li>Agência com método custa de R$ 3.000 a R$ 6.000/mês (régua da Alpha, prints de 05/11/2026); o resto entrega post solto.</li></ul>
<h3>A solução</h3><ul>
<li><b>Nicho único:</b> só pizzaria. Os roteiros, a biblioteca de cenas e os cases se somam.</li>
<li><b>Criativos gravados na pizzaria</b> (diária mensal ou bimestral), editados e narrados.</li>
<li><b>Tráfego (Meta)</b> para pedido no WhatsApp ou cardápio digital, com código por anúncio.</li>
<li><b>iFood organizado:</b> fotos, descrições, cardápio, combos e destaques (promoções e taxas ficam com a pizzaria).</li>
<li><b>Relatório de segunda</b> e ouvidoria na Central do Cliente.</li>
<li><b>Garantia de entrega</b> (não de resultado): se não entregarmos criativos, campanha e relatório, o mês não é cobrado, desde que a pizzaria aprove em 48 h, libere a gravação e pague em dia.</li></ul>
<h3>Por que nós</h3>
<p>Preço 16% a 36% abaixo da referência do mercado, operação enxuta com equipe de IA, sistema próprio de acompanhamento e presença local em São Luís. A falta de autoridade no nicho é compensada com risco menor para o cliente: prazo mínimo de 3 meses, garantia de entrega e 5 vagas de fundadora.</p>''')
    P.append(f'''<h2>O que já <span class="am">existe</span></h2>
<table><tr><th>Ativo</th><th>Situação (repositório, 15/11/2026)</th></tr>
<tr><td>Clientes pagantes</td><td>Dra. Jaci Cunha R$ 1.500/mês, Vereador Leo Pinto R$ 2.500/mês, WF Celulares R$ 800/mês = R$ 4.800/mês</td></tr>
<tr><td>Outros trabalhos</td><td>Tribuna 98 e Real Time (sem pagamento hoje), Desentupidora SF, Rafael Imports, curso de processo legislativo</td></tr>
<tr><td>Portfólio</td><td>72 trabalhos no site oficial (marca 19, Instagram 17, apps 8, sites 8, vídeo 7, produtos 6, estratégia 5, YouTube 2)</td></tr>
<tr><td>Sites de clientes no ar</td><td>drajacicunha, tribuna98, desentupidorasf e rafaelimports (.pages.dev)</td></tr>
<tr><td>Central do Cliente</td><td>Painel por cliente: aprovações, entregas, pagamentos, relatórios, fotos usadas</td></tr>
<tr><td>Orégano Turbo</td><td>Identidade v4.1 e manual, site com planos e formulário, kit social, calendário de 4 semanas, 57 de 84 artes, Instagram criado em 09/11/2026</td></tr>
<tr><td>Produtos de entrada</td><td>Bio que Vende, Kit Mês Pronto, Kit Prospecção, Kit WhatsApp que Fecha, Raio-X do Perfil (Estado Próprio)</td></tr>
<tr><td>Ferramentas internas</td><td>App SDR com botão de WhatsApp, Dublê (clone de voz e imagem), geradores de artes e vídeos</td></tr>
<tr><td>Canais próprios</td><td>Passaporte da Bíblia e Raposa e Leão (YouTube)</td></tr></table>
<h3>O que ainda é campo em branco</h3><ul>
<li>Custos fixos reais do mês: {pf('valor; o plano usa R$ 1.500 + R$ 500 de ferramentas')}</li></ul>''')
    P.append(f'''<h2>Mercado e <span class="am">cliente</span></h2>
<div class="g3"><div class="box"><div class="big">40.332</div><p class="nota">pizzarias no Brasil</p></div><div class="box"><div class="big">98%</div><p class="nota">fazem delivery</p></div><div class="box"><div class="big">75%</div><p class="nota">usam aplicativo</p></div></div>
<p class="nota" style="margin-top:6px">Fonte: Apubra/Galunion, citado no roteiro OT-04 do repositório. [Conferir a fonte primária e o ano antes de apresentar.]</p>
<h3>São Luís e Grande Ilha</h3><ul>
<li>Pizzarias ativas: {pf('nº (Receita Federal, CNAE 5611-2/01, ou contagem no Google Maps)')}</li>
<li>Pizzarias com faturamento acima de R$ 30 mil/mês (nosso corte): {pf('estimativa')}</li>
<li>A projeção Base pede {mes('Base',24)['cli']:.0f} clientes no mês 24. A conta "clientes ÷ pizzarias elegíveis" mostra quanto do mercado precisamos ganhar.</li></ul>
<h3>Persona do cliente (dono de pizzaria)</h3><ul>
<li>Dono ou sócio, 30 a 55 anos, trabalha na loja à noite e cuida de compra e equipe de dia.</li>
<li>Dor: noite fraca de segunda a quarta, dependência do app, já pagou "social media" que não trouxe pedido.</li>
<li>Valoriza: pedido no WhatsApp, foto que dá fome, número simples toda semana.</li>
<li>Confia: em quem aparece na loja, mostra outras pizzarias e não promete milagre.</li>
<li>Onde está: Instagram, WhatsApp, grupos de fornecedores, iFood.</li></ul>
<h3>Concorrência</h3><p>Franquias de marketing para restaurantes (Alpha: R$ 2.100 a R$ 6.000/mês + anúncio), agências locais generalistas e freelancers. Nossa posição: método de franquia, preço abaixo e entrega local, com sistema próprio.</p>''')
    P.append(f'''<h2>Modelo de negócio e <span class="am">vendas</span></h2>
<table><tr><th>Plano (por mês)</th><th>Trimestral</th><th>Semestral</th><th>Anual</th><th>Entrega</th></tr>
<tr><td><b>Muralha</b></td><td>R$ 1.997</td><td>R$ 1.797</td><td>R$ 1.597</td><td>4 criativos/mês, tráfego, cardápio digital, gravação bimestral, relatório mensal</td></tr>
<tr><td><b>Fortaleza</b></td><td>R$ 2.997</td><td>R$ 2.597</td><td>R$ 2.197</td><td>8 criativos, tráfego, Instagram, iFood, diária mensal</td></tr>
<tr><td><b>Cidadela ▲</b></td><td>R$ 3.997</td><td>R$ 3.697</td><td>R$ 3.497</td><td>Fortaleza + relatório semanal, reunião mensal, grupo com o Lindson, exclusividade no bairro</td></tr></table>
<ul style="margin-top:8px"><li>Pagamento sempre antecipado: contrato inteiro no cartão (Hubla, até 12x) ou Pix com 5%; ou mensal antecipado.</li>
<li>Atraso: pausa no dia seguinte; encerramento em 15 dias. Multa de saída: 20% dos meses que faltam.</li>
<li>Fundadoras: 5 vagas com o preço anual no prazo semestral, em troca de case autorizado por escrito.</li>
<li>Raio-X da Pizzaria (R$ 297) para quem não passa no filtro ou não fecha.</li></ul>
<h3>Funil e metas</h3>
<table><tr><th>Etapa</th><th>Como</th><th>Meta (premissa a medir)</th></tr>
<tr><td>Atrair</td><td>Anúncio com formulário, Reels, YouTube, prospecção ativa pelo app SDR</td><td>15 contatos/mês</td></tr>
<tr><td>Filtrar</td><td>Faturamento ≥ R$ 30 mil/mês e R$ 1.000 de verba</td><td>—</td></tr>
<tr><td>Diagnóstico</td><td>30 min, perfil ao vivo</td><td>9 comparecem; custo por diagnóstico &lt; R$ 150</td></tr>
<tr><td>Fechar</td><td>3 planos, contrato e cartão no mesmo dia</td><td>2 por mês (meta aprovada)</td></tr></table>
<p class="nota" style="margin-top:6px">Fontes: DECISOES-APROVADAS.md, PAGAMENTOS.md e README da operação própria (05/11/2026).</p>''')
    P.append(f'''<h2>Uso do <span class="am">dinheiro</span></h2>{c['tabela_uso']()}
<h3>Regras de uso</h3><ul>
<li><b>Parcelas:</b> {b(40000)} na assinatura; {b(30000)} quando houver 5 pizzarias pagantes (verificável na Central).</li>
<li><b>Tráfego:</b> R$ 30/dia nos 2 primeiros meses; sobe para R$ 1.500/mês só com custo por diagnóstico abaixo de R$ 150.</li>
<li><b>Contratação:</b> o 1º criador entra no mês 4 com teste pago de 1 semana; o aporte cobre 6 meses até a receita pagar sozinha.</li>
<li><b>Reserva:</b> intocada até o mês 6, para atraso de cliente ou mês fraco. <b>Prestação de contas</b> mensal com extrato.</li>
<li><b>Pró-labore:</b> R$ 3.000/mês só a partir do 3º cliente pizzaria (decisão aprovada).</li>
</ul>
<h3>Marcos</h3><table><tr><th>Quando</th><th>O que se verifica</th><th>Cenário Base (projeção)</th></tr>
<tr><td>Mês 6</td><td>CAC e custo por diagnóstico reais; 1º criador efetivado ou trocado</td><td>{mes('Base',6)['cli']:.0f} clientes · {b(mes('Base',6)['rec'])}/mês</td></tr>
<tr><td>Mês 12</td><td>Cases autorizados; revisão de preços; equipe a partir do 16º</td><td>{mes('Base',12)['cli']:.0f} clientes · {b(mes('Base',12)['rec'])}/mês</td></tr>
<tr><td>Mês 18</td><td>Operação com equipe; decidir 2ª cidade ou nicho vizinho</td><td>{mes('Base',18)['cli']:.0f} clientes · {b(mes('Base',18)['rec'])}/mês</td></tr></table>''')
    linhas = ''.join(f'<tr><td>{l["m"]}</td>' + ''.join(f'<td>{c["R"][n]["linhas"][l["m"]-1]["cli"]:.1f}</td><td>{b(c["R"][n]["linhas"][l["m"]-1]["rec"])}</td><td>{b(c["R"][n]["linhas"][l["m"]-1]["lucro"])}</td>' for n in M.CEN) + '</tr>' for l in c['R']['Base']['linhas'] if l['m'] % 3 == 0 or l['m'] == 1)
    P.append(f'''<h2>Projeção <span class="am">24 meses</span></h2>
<p>Projeção, não promessa. As premissas estão na aba Premissas da planilha (células amarelas) e podem ser trocadas na frente do investidor.</p>
<table><tr><th rowspan="2">Mês</th><th colspan="3">Conservador</th><th colspan="3">Base</th><th colspan="3">Otimista</th></tr>
<tr>{'<th>Clientes</th><th>Receita</th><th>Lucro</th>'*3}</tr>{linhas}</table>
<h3>Premissas</h3><ul>
<li>Novos clientes: conservador 1/mês, base 2/mês (meta aprovada), otimista 3/mês, com rampa nos 4 primeiros meses.</li>
<li>Ticket médio: R$ 2.000 · R$ 2.400 (o da projeção já aprovada) · R$ 2.700. Churn: 7% · 5% · 3% ao mês.</li>
<li>Custos: fixos R$ 1.500 + ferramentas R$ 500 [estimativa], R$ 150 por cliente, 6% de imposto [Conferir com contador], tráfego R$ 900 nos meses 1 e 2 e R$ 1.500 depois, criador de R$ 2.080 nos meses 4 a 9, equipe completa acima de 15 clientes, pró-labore R$ 3.000 a partir do 3º cliente.</li>
<li>Receita = R$ 4.800/mês atuais da agência + pizzarias (começa de zero). O revenue share incide só sobre a receita das pizzarias. Lucro antes do revenue share.</li></ul>''')
    P.append(f'''<h2>Unit <span class="am">economics</span></h2>{c['tabela_unit']()}
<ul style="margin-top:8px"><li><b>Margem de contribuição</b> = ticket − 6% de imposto − R$ 150 de custo variável.</li>
<li><b>LTV limitado a 12 meses:</b> a visão prudente. O LTV teórico (margem ÷ churn) é maior, mas depende de um churn que ainda não foi medido.</li>
<li><b>CAC cheio</b> soma ao tráfego R$ 500 de tempo comercial e Raio-X por cliente [premissa].</li></ul>
<h3>Sensibilidade: o que mais mexe no resultado</h3>
<p>No equilíbrio da carteira (clientes = novos por mês ÷ churn), com 2 clientes novos por mês:</p>
<table><tr><th>Ticket \\ churn</th><th>3%</th><th>5%</th><th>7%</th><th>10%</th></tr>''' + ''.join(
        '<tr><td>' + b(tk) + '</td>' + ''.join(f'<td>{b(_eq(M, tk, ch))}</td>' for ch in (0.03, 0.05, 0.07, 0.10)) + '</tr>' for tk in (1800, 2400, 3000)) + '''</table>
<p class="nota" style="margin-top:4px">Lucro mensal no equilíbrio, antes do revenue share. Tabela completa na aba Sensibilidade.</p>
<h3>As 5 premissas mais sensíveis</h3><ol style="padding-left:18px">
<li><b>Churn mensal</b>: de 5% para 8% derruba a carteira de equilíbrio de 40 para 25 clientes.</li>
<li><b>Clientes novos por mês</b>: a meta de 2/mês ainda não foi testada.</li>
<li><b>Ticket médio</b>: depende de quantas pizzarias escolhem o Fortaleza.</li>
<li><b>CAC real</b>: tráfego, diagnóstico e taxa de fechamento ainda são premissas.</li>
<li><b>Custo da equipe</b> acima de 15 clientes (salários da referência da Alpha).</li></ol>''')
    P.append(f'''<h2>Estrutura do <span class="am">investimento</span></h2>
<table><tr><th>Estrutura</th><th>Para o investidor</th><th>Para o Lindson</th></tr>
<tr><td><b>1 · Mútuo conversível / contrato de participação</b> (investidor-anjo, LC 155/2016)</td><td>+ pode virar sócio com desconto; não responde por dívidas da empresa. − retorno só com conversão e venda/recompra; prazo longo.</td><td>+ não paga nada todo mês. − dilui cotas; precisa de valuation; mais custo jurídico.</td></tr>
<tr><td><b>2 · Revenue share com teto</b> ★</td><td>+ recebe todo mês a partir do mês {M.P['rs_carencia']+1}; teto claro ({M.P['rs_teto']:.1f}x); relatório mensal. − sem garantia; se a receita cair, recebe menos e mais devagar.</td><td>+ mantém 100% das cotas e das decisões; o pagamento acompanha a receita. − tira {M.P['rs_pct']*100:.0f}% do caixa por alguns anos.</td></tr>
<tr><td><b>3 · Sócio-investidor na unidade Orégano Turbo</b> (empresa separada)</td><td>+ participa do crescimento da unidade. − depende de distribuição de lucro; acordo de sócios.</td><td>+ a agência fica fora do negócio. − divide uma empresa; contabilidade e CNPJ próprios.</td></tr></table>
<h3>Recomendação: revenue share com teto</h3>
<p>{M.P['rs_pct']*100:.0f}% da receita bruta da operação de pizzarias, a partir do mês {M.P['rs_carencia']+1}, até {b(teto)} ({M.P['rs_teto']:.1f}x), prazo máximo de {M.P['rs_prazo']} meses. Na projeção, o teto é atingido no mês {q['Base']} (base) e {q['Otimista']} (otimista); no conservador, {('no mês ' + str(q['Conservador'])) if q['Conservador'] else 'não é atingido em 60 meses'}. O que acontece com o saldo no fim do prazo é cláusula a decidir com advogado.</p>
<p><b>Por quê (o conselho do Maquiavel).</b> Quem traz dinheiro para dentro de casa não deve trazer também a chave da casa. Escrevi que as armas alheias, em paráfrase, ou te abandonam, ou te pesam, ou te apertam (<i>Príncipe</i> XIII). O revenue share paga o capital com o próprio resultado e devolve a casa inteira quando o teto é atingido. Se o investidor fizer questão de ser sócio, a estrutura 3 limita a sociedade à unidade de pizzarias e deixa a agência fora.</p>
<h3>Cuidados legais</h3><ul><li>Conversa privada com pessoas convidadas, sem oferta pública (regras da CVM). [Conferir com advogado]</li>
<li>Contrato escrito por advogado; tratamento contábil e tributário com contador (MEI não serve para agência). [Conferir]</li>
<li>Nenhuma promessa de retorno: o investidor recebe uma parte da receita que existir.</li></ul>''')
    P.append(f'''<h2>Riscos e <span class="am">mitigação</span></h2>
<table><tr><th>Risco</th><th>Probabilidade</th><th>Mitigação</th></tr>
<tr><td>Vender menos que o previsto</td><td>Média</td><td>2ª parcela só com 5 pagantes; verba de tráfego só sobe com custo medido; Raio-X como entrada</td></tr>
<tr><td>Churn alto</td><td>Média</td><td>Prazo mínimo, pagamento antecipado, multa de 20%, relatório de segunda, ouvidoria, downsell antes de cancelar</td></tr>
<tr><td>Dependência do Lindson (pessoa-chave)</td><td>Alta</td><td>Processos escritos, equipe Claude, contratação com teste pago; seguro de vida {pf('avaliar')}</td></tr>
<tr><td>Dependência da Meta e de apps</td><td>Média</td><td>WhatsApp e lista próprios, Google, YouTube, cardápio digital do cliente</td></tr>
<tr><td>Atraso de pagamento do cliente</td><td>Média</td><td>Pausa no dia seguinte, encerramento em 15 dias, cartão recorrente</td></tr>
<tr><td>Jurídico (CDC, LGPD, publicidade)</td><td>Baixa a média</td><td>Sem promessa de resultado; dados de cliente só com autorização escrita; contratos revisados</td></tr>
<tr><td>Concorrência</td><td>Média</td><td>Nicho, preço, entrega local, Central; registro da marca no INPI (classe 35)</td></tr>
<tr><td>Uso indevido do dinheiro</td><td>Baixa</td><td>Conta separada, extrato mensal, uso definido em contrato</td></tr></table>
<h3>O que o investidor recebe todo mês</h3><ul><li>Clientes ativos, novos e cancelados.</li><li>Receita do mês e valor do revenue share.</li><li>Uso do dinheiro com extrato.</li><li>Custo por diagnóstico e CAC.</li></ul>''')
    P.append(f'''<img src="{foto(F['plano_time'])}" style="float:right;width:62mm;height:90mm;object-fit:cover;object-position:center 15%;margin:0 0 8mm 8mm">
<h2>O <span class="am">time</span></h2>
<p><b>Lindson Almeida</b> · estrategista digital de São Luís (MA), dono de agência de gestão de redes sociais e criador dos canais Passaporte da Bíblia e Raposa e Leão. Faz venda, estratégia e gravação, e atende sozinho até 15 pizzarias com a equipe Claude.</p>
<p><b>Equipe Claude</b> · 4 contas de IA (Lindson, Zuleide, Pedro e Leandro) no mesmo repositório, com um gerente (Maquiavel) e especialistas: Hormozi (oferta e preço), Copy, Design, Builder (sistemas), Paollo e Rocco (pizzaria e campanha de comida) e Peter (YouTube).</p>
<p><b>Contratações previstas</b> · criador (R$ 2.080), gestor de tráfego (R$ 2.080) e account (R$ 3.000), a partir do 16º cliente, sempre com teste pago de 1 semana.</p>
<p><b>Apoio</b> · contador {pf('nome')} e advogado {pf('nome')}.</p>
<div style="clear:both"></div>
<h3>Próximos passos</h3><ol style="padding-left:18px"><li>Reunião de 30 minutos: Central do Cliente e planilha ao vivo.</li><li>Investidor escolhe a estrutura; advogado redige o contrato.</li><li>Conta separada e assinatura; 1ª parcela.</li><li>Relatório mensal a partir do mês 1.</li></ol>
<div class="box" style="margin-top:12mm"><p><b>Contato</b> · WhatsApp (98) 98562-1808 · @lindsonalmeida_ · lindsonalmeida.pages.dev</p></div>
<p class="nota" style="margin-top:8mm">{AVISO}</p>''')
    return P

def _eq(M, tk, ch, novos=2):
    import math
    cli = novos/ch
    eq = (math.ceil((cli-M.P['limite_solo'])/5)*M.P['custo_func'] + M.P['custo_func'] + M.P['custo_account']) if cli > M.P['limite_solo'] else 0
    return cli*tk*(1-M.P['imposto']) - cli*M.P['var_cliente'] - M.P['fixo'] - M.P['ferramentas'] - M.P['trafego'] - M.P['prolabore'] - eq

def onepager(c):
    b, M, mes, F, foto = c['b'], c['M'], c['mes'], c['F'], c['foto']
    ap = M.P['aporte']; teto = ap*M.P['rs_teto']
    uso = ''.join(f'<tr><td>{a}</td><td style="text-align:right"><b>{b(v)}</b></td></tr>' for a, d, v, q in M.USO)
    cen = ''.join(f'<tr><td><b>{n}</b></td><td>{mes(n,12)["cli"]:.0f} · {b(mes(n,12)["rec"])}</td><td>{mes(n,24)["cli"]:.0f} · {b(mes(n,24)["rec"])}</td></tr>' for n in M.CEN)
    return f'''<div style="display:flex;gap:10mm;align-items:center">
<div style="flex:1"><span class="tag">One-pager · investidor</span><h1 style="font-size:50px;margin-top:8px">Orégano Turbo:<br><span class="am">marketing para pizzarias</span></h1>
<p style="margin-top:6px">Lindson Almeida · São Luís (MA) · agência com R$ 4.800/mês de 3 clientes pagantes e 72 trabalhos no portfólio.</p></div>
<img src="{foto(F['one'])}" style="width:50mm;height:62mm;object-fit:cover;object-position:center 15%"></div>
<div class="g2" style="margin-top:4mm"><div>
<h3>Problema</h3><p>O dono de pizzaria depende do aplicativo e do boca a boca, posta sem método e não mede o que o anúncio traz.</p>
<h3>Solução</h3><p>Assessoria só para pizzarias: criativos gravados na loja, tráfego para pedido no WhatsApp, iFood organizado e relatório toda segunda na Central do Cliente. Pagamento antecipado e garantia de entrega (não de resultado).</p>
<h3>Preços aprovados (por mês)</h3><p>Muralha R$ 1.597 a 1.997 · Fortaleza R$ 2.197 a 2.997 · Cidadela R$ 3.497 a 3.997. Verba de anúncio paga pela pizzaria.</p>
<h3>Já existe</h3><ul><li>Pagantes: Jaci, Leo Pinto e WF (R$ 4.800/mês)</li><li>Central do Cliente, app SDR, sites no ar</li><li>Orégano Turbo: identidade, site com planos, kit social, Instagram</li></ul>
<h3>Mercado</h3><p>40.332 pizzarias no Brasil, 98% com delivery (Apubra/Galunion, a conferir). São Luís: [preencher].</p>
</div><div>
<h3>O pedido: {b(ap)}</h3><table>{uso}</table>
<p style="margin-top:4px">Em 2 parcelas: {b(40000)} + {b(30000)} com 5 pizzarias pagantes.</p>
<h3>Estrutura sugerida</h3><p>Revenue share: {M.P['rs_pct']*100:.0f}% da receita das pizzarias a partir do mês {M.P['rs_carencia']+1}, até {b(teto)} ({M.P['rs_teto']:.1f}x), prazo máximo {M.P['rs_prazo']} meses. Sem cotas, sem voto, relatório mensal.</p>
<h3>Projeção (clientes · receita/mês)</h3><table><tr><th>Cenário</th><th>Mês 12</th><th>Mês 24</th></tr>{cen}</table>
<p class="nota" style="font-size:11px">Projeção com premissas na planilha anexa, não promessa.</p>
</div></div>
<div class="g2" style="margin-top:2mm"><div><h3>Marcos</h3><ul><li><b>2 meses:</b> 5 pizzarias fundadoras</li><li><b>6 meses:</b> CAC e funil medidos; 1º criador</li><li><b>12 meses:</b> cases autorizados; equipe a partir do 16º cliente</li></ul></div>
<div><h3>Riscos que tratamos</h3><ul><li>Vender menos: 2ª parcela só com 5 pagantes</li><li>Churn: prazo, pagamento antecipado, relatório de segunda</li><li>Pessoa-chave: processos escritos e equipe Claude</li></ul></div></div>
<div class="box" style="margin-top:5mm;padding:8px 12px"><p><b>Próximo passo:</b> 30 minutos para ver a Central e a planilha ao vivo · WhatsApp (98) 98562-1808 · @lindsonalmeida_</p></div>
<p class="nota" style="margin-top:3mm;font-size:9px">{AVISO}</p>'''
