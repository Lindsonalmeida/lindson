"""Modelo do plano investidor (conta Lindson/Maquiavel, 15/11/2026).
Fonte única dos números do deck, do plano e do one-pager. A planilha (planilha.py)
reproduz a mesma lógica em fórmulas. TUDO aqui é PROJEÇÃO com premissas, não promessa.
Premissas de origem: agencia/operacao-propria/DECISOES-APROVADAS.md, PRECOS-PIZZARIAS.md,
README.md (custos da equipe) e projecao.py."""
import math

# ---------- premissas comuns (origem entre parênteses) ----------
P = dict(
    aporte=70000,          # pedido sugerido (faixa R$ 50 a 80 mil) - proposta deste plano
    fixo=1500,             # custos fixos/mês (PRECOS-PIZZARIAS.md item 2)
    var_cliente=150,       # deslocamento e captação por cliente (idem)
    imposto=0.06,          # 6% (idem) [Conferir com contador]
    prolabore=3000,        # a partir do 3º cliente (DECISOES-APROVADAS 20)
    trafego_ini=900,       # R$ 30/dia nos 2 primeiros meses (DECISOES-APROVADAS 19)
    trafego=1500,          # depois do 2º mês, com o aporte (proposta)
    custo_func=2080,       # criador / gestor (README operação própria, planilha Alpha)
    custo_account=3000,
    limite_solo=15,        # até 15 clientes sozinho (decisão 05/11)
    receita_agencia=4800,  # Jaci 1.500 + Leo 2.500 + WF 800 (Lindson, 15/11/2026)
    ferramentas=500,       # ferramentas/mês [estimativa: preencher com o real]
    rs_pct=0.10, rs_teto=1.5, rs_carencia=3, rs_prazo=60,  # revenue share sugerido
)
CEN = {  # conservador, base, otimista
    'Conservador': dict(novos=[0,1,1,1], novos_d=1, ticket=2000, churn=0.07),
    'Base':        dict(novos=[1,1,2,2], novos_d=2, ticket=2400, churn=0.05),
    'Otimista':    dict(novos=[1,2,2,3], novos_d=3, ticket=2700, churn=0.03),
}
# uso do dinheiro (proposta; valores marcados [estimativa] precisam de orçamento real)
USO = [
    ('Tráfego para atrair pizzarias', 'R$ 1.500/mês por 12 meses (hoje: R$ 30/dia)', 18000, 'Meses 1 a 12'),
    ('1º contratado: criador (grava e edita)', 'R$ 2.080/mês por 6 meses, até a receita pagar', 12480, 'Meses 4 a 9'),
    ('Equipamento de gravação', 'câmera/celular, luz, microfone, tripé [estimativa: orçar]', 8000, 'Mês 1'),
    ('Ferramentas e software', 'edição, IA, Hubla, Meta, domínio [estimativa: R$ 500/mês x 12]', 6000, 'Meses 1 a 12'),
    ('Formalização e proteção', 'contador, advogado (contrato do investidor e dos clientes), INPI classe 35 [estimativa]', 4500, 'Meses 1 a 2'),
    ('Reserva de caixa', '3 meses de fixos + pró-labore (R$ 4.500 x 3) + folga', 21020, 'Intocada até o mês 6'),
]
assert sum(u[2] for u in USO) == P['aporte']

def novos_mes(c, m):
    return c['novos'][m-1] if m <= len(c['novos']) else c['novos_d']

def projetar(nome, meses=24, ticket=None, churn=None, novos_mult=1.0, aporte=None):
    c = dict(CEN[nome]); P2 = dict(P)
    if ticket: c['ticket'] = ticket
    if churn is not None: c['churn'] = churn
    if aporte: P2['aporte'] = aporte
    cli = 0.0; caixa = P2['aporte']; acum_rs = 0; linhas = []
    teto = P2['aporte']*P2['rs_teto']; quitado = None
    for m in range(1, meses+1):
        n = novos_mes(c, m)*novos_mult
        cli = cli*(1-c['churn']) + n
        rec_piz = cli*c['ticket']
        rec = rec_piz + P2['receita_agencia']
        trafego = P2['trafego_ini'] if m <= 2 else P2['trafego']
        equipe = 0
        if cli > P2['limite_solo']:
            extra = math.ceil((cli-P2['limite_solo'])/5)
            equipe = extra*P2['custo_func'] + P2['custo_func'] + P2['custo_account']
        elif 4 <= m <= 9:
            equipe = P2['custo_func']  # 1º criador financiado pelo aporte
        pl = P2['prolabore'] if cli >= 3 else 0
        custos = P2['fixo'] + P2['ferramentas'] + cli*P2['var_cliente'] + rec*P2['imposto'] + trafego + equipe + pl
        lucro = rec - custos
        rs = 0
        if m > P2['rs_carencia'] and acum_rs < teto:
            rs = min(rec_piz*P2['rs_pct'], teto-acum_rs)
        acum_rs += rs
        if quitado is None and acum_rs >= teto-0.5: quitado = m
        caixa += lucro - rs - (8000+4500 if m == 1 else 0)
        linhas.append(dict(m=m, novos=n, cli=cli, rec=rec, rec_piz=rec_piz, custos=custos, lucro=lucro, rs=rs, acum_rs=acum_rs, caixa=caixa))
    return dict(linhas=linhas, quitado=quitado, teto=teto, c=c)

def unit(nome):
    c = CEN[nome]
    margem = c['ticket']*(1-P['imposto']) - P['var_cliente']
    vida = 1/c['churn']
    cac = P['trafego']/c['novos_d']
    return dict(ticket=c['ticket'], margem=margem, vida=vida, ltv=margem*vida, ltv12=margem*min(vida,12), cac=cac, payback=cac/margem, ratio=margem*vida/cac)

def brl(v, dec=0):
    s = f"{v:,.{dec}f}".replace(',', 'X').replace('.', ',').replace('X', '.')
    return 'R$ ' + s

if __name__ == '__main__':
    for n in CEN:
        r = projetar(n); L = r['linhas']
        print(n, [(l['m'], round(l['cli'],1), round(l['rec']), round(l['lucro'])) for l in L if l['m'] in (6,12,18,24)], 'quitado', r['quitado'], 'caixa min', round(min(l['caixa'] for l in L)))
        print('  unit', {k: round(v,1) for k,v in unit(n).items()})
