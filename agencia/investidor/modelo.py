"""Modelo do plano investidor v2: EMPRESA INTEIRA do Lindson (conta Lindson/Maquiavel, 15/11/2026).
Unidades: Agência (negócios locais), Orégano Turbo (pizzarias), Produtos digitais (Hubla),
YouTube + marca pessoal, Tecnologia própria, Equipe de IA. Fonte única dos números dos PDFs;
planilha.py reproduz em fórmulas. Tudo é PROJEÇÃO com premissas, não promessa.
Origem: receita real (Lindson 15/11: Jaci 1.500 + Leo 2.500 + WF 800), esteira-de-produtos.md,
DECISOES-APROVADAS.md, PRECOS-PIZZARIAS.md, README da operação própria, low-ticket/maquiavel.md."""
import math

P = dict(
    aporte=100000,           # pedido sugerido (faixa R$ 80 a 120 mil)
    parcela1=60000, parcela2=40000,
    base_agencia=4800,       # receita real hoje (Lindson, 15/11/2026)
    clientes_base=3,         # Jaci, Leo Pinto, WF Celulares
    fixo=1500, ferramentas=500, var_cliente=150, imposto=0.06,
    prolabore=3000,          # a partir do mês 1 [decisão do Lindson]
    traf_ag=1000,            # tráfego da agência/mês (proposta)
    traf_ot0=900, traf_ot=1500,  # Orégano: R$ 30/dia nos meses 1-2 (aprovado), depois 1.500
    traf_pd=600, pd_ini=2,   # tráfego dos produtos a partir do mês 2 (teste)
    pd_ticket=37, pd_taxa=0.10,  # preço sugerido (Manual de Campo R$ 37; low ticket R$ 19 a 47) e taxa Hubla [Conferir]
    custo_func=2080, custo_account=3000, limite_solo=15,
    cri_ini=4, cri_fim=9,    # 1º criador financiado pelo aporte
    gasto_ini=8000+6000,     # equipamento + jurídico/contábil no mês 1
    rs_pct=0.10, rs_teto=1.5, rs_carencia=3, rs_prazo=60,
)
CEN = {
    'Conservador': dict(ag_novos=0.5, ag_ticket=1200, ag_churn=0.06,
                        ot_novos=[0,1,1,1], ot_d=1, ot_ticket=2000, ot_churn=0.07, pd_cpa=45),
    'Base':        dict(ag_novos=1.0, ag_ticket=2200, ag_churn=0.05,
                        ot_novos=[1,1,2,2], ot_d=2, ot_ticket=2400, ot_churn=0.05, pd_cpa=30),
    'Otimista':    dict(ag_novos=1.5, ag_ticket=2800, ag_churn=0.04,
                        ot_novos=[1,2,2,3], ot_d=3, ot_ticket=2700, ot_churn=0.03, pd_cpa=22),
}
USO = [  # (unidade, item, detalhe, valor, quando, prioridade)
    ('Agência', 'Tráfego para atrair clientes locais', 'R$ 1.000/mês por 12 meses', 12000, 'Meses 1 a 12', 1),
    ('Orégano Turbo', 'Tráfego para atrair pizzarias', 'R$ 30/dia nos meses 1-2, R$ 1.500/mês depois', 18000, 'Meses 1 a 12', 2),
    ('Agência + Orégano', '1º contratado: criador (grava e edita)', 'R$ 2.080/mês por 6 meses', 12480, 'Meses 4 a 9', 2),
    ('Todas', 'Equipamento de gravação', 'câmera/celular, luz, microfone, tripé [estimativa: orçar]', 8000, 'Mês 1', 1),
    ('Produtos', 'Tráfego dos produtos digitais (teste)', 'R$ 600/mês por 10 meses; só continua se o custo por venda fechar', 6000, 'Meses 2 a 11', 3),
    ('Todas', 'Ferramentas e software', 'edição, IA, Hubla, Meta, hospedagem [estimativa: R$ 500/mês]', 6000, 'Meses 1 a 12', 1),
    ('Todas', 'Formalização e proteção', 'contador, advogado (investidor e clientes), INPI das marcas [estimativa]', 6000, 'Meses 1 a 2', 1),
    ('Todas', 'Reserva de caixa', 'cerca de 4 meses de fixos + pró-labore; intocada até o mês 6', 31520, 'Até o mês 6', 1),
]
assert sum(u[3] for u in USO) == P['aporte']

def projetar(nome, meses=24, mult=1.0, ag_churn=None, ot_churn=None, ticket_mult=1.0):
    c = dict(CEN[nome])
    if ag_churn is not None: c['ag_churn'] = ag_churn
    if ot_churn is not None: c['ot_churn'] = ot_churn
    ag = 0.0; ot = 0.0; acum = 0.0; caixa = P['aporte']; teto = P['aporte']*P['rs_teto']; quit = None; L = []
    for m in range(1, meses+1):
        ag = ag*(1-c['ag_churn']) + c['ag_novos']*mult
        n_ot = (c['ot_novos'][m-1] if m <= 4 else c['ot_d'])*mult
        ot = ot*(1-c['ot_churn']) + n_ot
        base = P['base_agencia']  # premissa: os 3 contratos atuais se mantêm
        r_ag = base + ag*c['ag_ticket']*ticket_mult
        r_ot = ot*c['ot_ticket']*ticket_mult
        traf_pd = P['traf_pd'] if P['pd_ini'] <= m <= 11 else 0
        vendas = traf_pd/c['pd_cpa']
        r_pd = vendas*P['pd_ticket']*(1-P['pd_taxa'])
        rec = r_ag + r_ot + r_pd
        cli = P['clientes_base'] + ag + ot
        traf = P['traf_ag'] + (P['traf_ot0'] if m <= 2 else P['traf_ot']) + traf_pd
        if cli > P['limite_solo']:
            equipe = math.ceil((cli-P['limite_solo'])/5)*P['custo_func'] + P['custo_func'] + P['custo_account']
        elif P['cri_ini'] <= m <= P['cri_fim']:
            equipe = P['custo_func']
        else: equipe = 0
        custos = P['fixo'] + P['ferramentas'] + P['prolabore'] + cli*P['var_cliente'] + rec*P['imposto'] + traf + equipe
        lucro = rec - custos
        incr = rec - P['base_agencia']   # receita nova das unidades financiadas
        rs = min(max(incr, 0)*P['rs_pct'], teto-acum) if (m > P['rs_carencia'] and acum < teto) else 0
        acum += rs
        if quit is None and acum >= teto-0.5: quit = m
        caixa += lucro - rs - (P['gasto_ini'] if m == 1 else 0)
        L.append(dict(m=m, ag=P['clientes_base']+ag, ot=ot, vendas=vendas, r_ag=r_ag, r_ot=r_ot, r_pd=r_pd, rec=rec, cli=cli,
                      custos=custos, lucro=lucro, rs=rs, acum=acum, caixa=caixa))
    return dict(linhas=L, quitado=quit, teto=teto)

def unit(nome):
    c = CEN[nome]; out = {}
    for k, tk, ch, cac in (('Agência', c['ag_ticket'], c['ag_churn'], P['traf_ag']/c['ag_novos']),
                           ('Orégano', c['ot_ticket'], c['ot_churn'], P['traf_ot']/c['ot_d'])):
        mg = tk*(1-P['imposto']) - P['var_cliente']
        out[k] = dict(ticket=tk, margem=mg, vida=1/ch, ltv12=mg*min(1/ch, 12), cac=cac, cac_cheio=cac+500, payback=(cac+500)/mg)
    out['Produtos'] = dict(ticket=P['pd_ticket'], liquido=P['pd_ticket']*(1-P['pd_taxa']), cpa=c['pd_cpa'], roas=P['pd_ticket']*(1-P['pd_taxa'])/c['pd_cpa'])
    return out

def brl(v, dec=0):
    s = f"{v:,.{dec}f}".replace(',', 'X').replace('.', ',').replace('X', '.')
    return 'R$ ' + s

if __name__ == '__main__':
    for n in CEN:
        r = projetar(n); L = r['linhas']
        print(n, [(l['m'], round(l['cli'],1), round(l['r_ag']), round(l['r_ot']), round(l['r_pd']), round(l['rec']), round(l['lucro'])) for l in L if l['m'] in (1,6,12,24)],
              'q60', projetar(n, 60)['quitado'], 'cxmin', round(min(l['caixa'] for l in L)))
