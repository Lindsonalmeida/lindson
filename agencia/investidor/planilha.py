"""Gera PLANO-INVESTIDOR.xlsx com fórmulas reais (premissas em amarelo).
Uso: python3 planilha.py <saida.xlsx>"""
import sys
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter as L
import modelo as M

out = sys.argv[1] if len(sys.argv) > 1 else 'PLANO-INVESTIDOR.xlsx'
wb = Workbook()
AM = PatternFill('solid', fgColor='F5C518'); PR = PatternFill('solid', fgColor='0A0A0A')
CZ = PatternFill('solid', fgColor='EFEFEF')
B = Font(bold=True); BW = Font(bold=True, color='FFFFFF'); T = Font(bold=True, size=14)
fin = Side(style='thin', color='BBBBBB'); BOX = Border(top=fin, bottom=fin, left=fin, right=fin)
R = '"R$" #,##0'; PC = '0.0%'; N1 = '0.0'

def head(ws, r, vals, c0=1):
    for i, v in enumerate(vals):
        x = ws.cell(r, c0+i, v); x.fill = PR; x.font = BW; x.alignment = Alignment(wrap_text=True, vertical='center')

# ---------------- Premissas ----------------
ws = wb.active; ws.title = 'Premissas'
ws['A1'] = 'PLANO INVESTIDOR · PREMISSAS (células amarelas são editáveis)'; ws['A1'].font = T
ws['A2'] = 'Projeção, não promessa. Origem de cada número na coluna D. Conversa privada, sem oferta pública; estrutura final com advogado e contador.'
head(ws, 4, ['Premissa comum', 'Valor', '', 'Origem'])
comuns = [
    ('aporte', 'Aporte do investidor', M.P['aporte'], R, 'Proposta deste plano (faixa R$ 50 a 80 mil)'),
    ('fixo', 'Custos fixos por mês', M.P['fixo'], R, 'PRECOS-PIZZARIAS.md, item 2'),
    ('ferr', 'Ferramentas por mês', M.P['ferramentas'], R, '[estimativa: preencher com o real]'),
    ('var', 'Custo variável por cliente/mês', M.P['var_cliente'], R, 'PRECOS-PIZZARIAS.md, item 2'),
    ('imp', 'Imposto sobre a receita', M.P['imposto'], PC, '6% [Conferir com contador]'),
    ('pl', 'Pró-labore (a partir do 3º cliente)', M.P['prolabore'], R, 'DECISOES-APROVADAS.md, item 20'),
    ('traf0', 'Tráfego meses 1 e 2', M.P['trafego_ini'], R, 'DECISOES-APROVADAS.md, item 19 (R$ 30/dia)'),
    ('traf', 'Tráfego a partir do mês 3', M.P['trafego'], R, 'Proposta com o aporte'),
    ('func', 'Custo de criador ou gestor/mês', M.P['custo_func'], R, 'README operação própria, item 5'),
    ('acc', 'Custo de account/mês', M.P['custo_account'], R, 'README operação própria, item 5'),
    ('lim', 'Clientes que o Lindson atende sozinho', M.P['limite_solo'], '0', 'Decisão 05/11/2026'),
    ('cri_ini', '1º criador financiado: mês inicial', 4, '0', 'Proposta (uso do dinheiro)'),
    ('cri_fim', '1º criador financiado: mês final', 9, '0', 'Proposta (uso do dinheiro)'),
    ('ini', 'Gasto único no mês 1 (equipamento + formalização)', 12500, R, 'Uso do dinheiro'),
    ('rs_pct', 'Revenue share: % da receita', M.P['rs_pct'], PC, 'Estrutura 2 (sugestão)'),
    ('rs_teto', 'Revenue share: teto (múltiplo do aporte)', M.P['rs_teto'], '0.00"x"', 'Estrutura 2 (sugestão)'),
    ('rs_car', 'Revenue share: carência (meses)', M.P['rs_carencia'], '0', 'Estrutura 2 (sugestão)'),
    ('mult', 'Multiplicador de clientes novos (sensibilidade)', 1, '0.00', 'Use 0,5 para testar metade da meta'),
    ('fat_atual', 'Faturamento atual da agência/mês (base)', 4800, R, 'Lindson, 15/11/2026: Jaci R$ 1.500 + Leo Pinto R$ 2.500 + WF R$ 800'),
]
NM = {}
r = 5
for k, rot, v, fmt, org in comuns:
    ws.cell(r, 1, rot); c = ws.cell(r, 2, v); c.fill = AM; c.number_format = fmt; ws.cell(r, 4, org)
    NM[k] = f"Premissas!$B${r}"; r += 1
r += 1
head(ws, r, ['Premissa por cenário', 'Conservador', 'Base', 'Otimista', 'Origem']); r += 1
SC = {}
cen = list(M.CEN.keys())
rows = [('n1', 'Clientes novos no mês 1', lambda c: c['novos'][0], '0.0'),
        ('n2', 'Clientes novos no mês 2', lambda c: c['novos'][1], '0.0'),
        ('n3', 'Clientes novos no mês 3', lambda c: c['novos'][2], '0.0'),
        ('n4', 'Clientes novos no mês 4', lambda c: c['novos'][3], '0.0'),
        ('nd', 'Clientes novos/mês depois do 4º', lambda c: c['novos_d'], '0.0'),
        ('tk', 'Ticket médio/mês', lambda c: c['ticket'], R),
        ('ch', 'Saída de clientes por mês (churn)', lambda c: c['churn'], PC)]
orig = {'nd': 'Meta aprovada: 2/mês (DECISOES 18)', 'tk': 'Tabela aprovada R$ 1.597 a 3.997; base R$ 2.400 (projecao.py)', 'ch': 'projecao.py usa 5%'}
for k, rot, f, fmt in rows:
    ws.cell(r, 1, rot)
    for j, n in enumerate(cen):
        c = ws.cell(r, 2+j, f(M.CEN[n])); c.fill = AM; c.number_format = fmt
    ws.cell(r, 5, orig.get(k, 'Proposta (rampa de entrada)'))
    SC[k] = r; r += 1
ws.column_dimensions['A'].width = 48; ws.column_dimensions['B'].width = 16; ws.column_dimensions['C'].width = 16
ws.column_dimensions['D'].width = 16; ws.column_dimensions['E'].width = 50
ws.freeze_panes = 'A5'

def sc(k, j):  # referência absoluta da premissa do cenário j (0..2)
    return f"Premissas!${L(2+j)}${SC[k]}"

# ---------------- Uso do dinheiro ----------------
u = wb.create_sheet('Uso do dinheiro')
u['A1'] = 'USO DO DINHEIRO (proposta; [estimativa] = pedir orçamento)'; u['A1'].font = T
head(u, 3, ['Item', 'Detalhe', 'Valor', '% do aporte', 'Quando'])
for i, (a, b, v, q) in enumerate(M.USO):
    rr = 4+i; u.cell(rr, 1, a); u.cell(rr, 2, b); c = u.cell(rr, 3, v); c.fill = AM; c.number_format = R
    u.cell(rr, 4, f"=C{rr}/$C${4+len(M.USO)}").number_format = PC; u.cell(rr, 5, q)
tr = 4+len(M.USO)
u.cell(tr, 1, 'TOTAL').font = B; u.cell(tr, 3, f"=SUM(C4:C{tr-1})").number_format = R; u.cell(tr, 3).font = B
u.cell(tr+1, 1, 'Confere com o aporte da aba Premissas?'); u.cell(tr+1, 3, f'=IF(C{tr}={NM["aporte"]},"OK","AJUSTAR")')
for col, w in zip('ABCDE', (40, 70, 14, 12, 22)): u.column_dimensions[col].width = w

# ---------------- Projeção ----------------
p = wb.create_sheet('Projeção 24 meses')
p['A1'] = 'PROJEÇÃO 24 MESES POR CENÁRIO (projeção, não promessa)'; p['A1'].font = T
cols = ['Mês', 'Novos', 'Clientes', 'Receita (agência + pizzarias)', 'Tráfego', 'Equipe', 'Pró-labore', 'Variável', 'Imposto', 'Fixos + ferr.', 'Custos', 'Lucro', 'Revenue share', 'RS acumulado', 'Caixa']
BLK = {}
start = 3
for j, n in enumerate(cen):
    p.cell(start, 1, f'Cenário {n}').font = T
    head(p, start+1, cols)
    f0 = start+2; BLK[n] = (f0, f0+23)
    for m in range(1, 25):
        rr = f0+m-1; pv = rr-1
        p.cell(rr, 1, m)
        p.cell(rr, 2, f"=IF(A{rr}<=4,INDEX({sc('n1',j)}:{sc('n4',j)},A{rr}),{sc('nd',j)})*{NM['mult']}")
        prev = f"C{pv}" if m > 1 else "0"
        p.cell(rr, 3, f"={prev}*(1-{sc('ch',j)})+B{rr}")
        p.cell(rr, 4, f"=C{rr}*{sc('tk',j)}+{NM['fat_atual']}")
        p.cell(rr, 5, f"=IF(A{rr}<=2,{NM['traf0']},{NM['traf']})")
        p.cell(rr, 6, f"=IF(C{rr}>{NM['lim']},CEILING((C{rr}-{NM['lim']})/5,1)*{NM['func']}+{NM['func']}+{NM['acc']},IF(AND(A{rr}>={NM['cri_ini']},A{rr}<={NM['cri_fim']}),{NM['func']},0))")
        p.cell(rr, 7, f"=IF(C{rr}>=3,{NM['pl']},0)")
        p.cell(rr, 8, f"=C{rr}*{NM['var']}")
        p.cell(rr, 9, f"=D{rr}*{NM['imp']}")
        p.cell(rr, 10, f"={NM['fixo']}+{NM['ferr']}")
        p.cell(rr, 11, f"=SUM(E{rr}:J{rr})")
        p.cell(rr, 12, f"=D{rr}-K{rr}")
        acp = f"N{pv}" if m > 1 else "0"
        p.cell(rr, 13, f"=IF(AND(A{rr}>{NM['rs_car']},{acp}<{NM['aporte']}*{NM['rs_teto']}),MIN((D{rr}-{NM['fat_atual']})*{NM['rs_pct']},{NM['aporte']}*{NM['rs_teto']}-{acp}),0)")
        p.cell(rr, 14, f"={acp}+M{rr}")
        cxp = f"O{pv}" if m > 1 else NM['aporte']
        p.cell(rr, 15, f"={cxp}+L{rr}-M{rr}-IF(A{rr}=1,{NM['ini']},0)")
        p.cell(rr, 2).number_format = N1; p.cell(rr, 3).number_format = N1
        for cc in range(4, 16): p.cell(rr, cc).number_format = R
    tot = f0+24
    p.cell(tot, 1, 'Total 24m').font = B
    for cc in (4, 11, 12, 13):
        p.cell(tot, cc, f"=SUM({L(cc)}{f0}:{L(cc)}{f0+23})").number_format = R; p.cell(tot, cc).font = B
    start = tot+3
for i in range(1, 16): p.column_dimensions[L(i)].width = 13
p.column_dimensions['A'].width = 18

# ---------------- Unit economics ----------------
ue = wb.create_sheet('Unit economics')
ue['A1'] = 'UNIT ECONOMICS POR CENÁRIO (premissas, a medir com os primeiros clientes)'; ue['A1'].font = T
head(ue, 3, ['Métrica', 'Conservador', 'Base', 'Otimista', 'Como se calcula'])
mets = [
    ('Ticket médio/mês', lambda j: f"={sc('tk',j)}", R, 'Premissa'),
    ('Margem de contribuição/cliente/mês', lambda j: f"={sc('tk',j)}*(1-{NM['imp']})-{NM['var']}", R, 'Ticket - imposto - variável'),
    ('Vida média do cliente (meses)', lambda j: f"=1/{sc('ch',j)}", N1, '1 / churn'),
    ('LTV (margem x vida)', lambda j: f"={L(2+j)}5*{L(2+j)}6", R, 'Sem desconto financeiro'),
    ('LTV limitado a 12 meses (visão prudente)', lambda j: f"={L(2+j)}5*MIN({L(2+j)}6,12)", R, 'Como o investidor deve olhar'),
    ('CAC só de tráfego', lambda j: f"={NM['traf']}/{sc('nd',j)}", R, 'Tráfego/mês ÷ novos/mês'),
    ('CAC cheio (+ R$ 500 de tempo comercial e Raio-X)', lambda j: f"={L(2+j)}9+500", R, '[premissa: medir]'),
    ('Payback do CAC cheio (meses)', lambda j: f"={L(2+j)}10/{L(2+j)}5", '0.00', 'CAC cheio ÷ margem'),
    ('LTV(12m) ÷ CAC cheio', lambda j: f"={L(2+j)}8/{L(2+j)}10", '0.0"x"', 'Acima de 3x é saudável'),
    ('Clientes no equilíbrio (novos ÷ churn)', lambda j: f"={sc('nd',j)}/{sc('ch',j)}", N1, 'Teto natural da carteira'),
]
for i, (rot, f, fmt, como) in enumerate(mets):
    rr = 4+i; ue.cell(rr, 1, rot)
    for j in range(3): c = ue.cell(rr, 2+j, f(j)); c.number_format = fmt
    ue.cell(rr, 5, como)
ue.column_dimensions['A'].width = 50; ue.column_dimensions['E'].width = 34
for c in 'BCD': ue.column_dimensions[c].width = 15

# ---------------- Retorno do investidor ----------------
ri = wb.create_sheet('Retorno do investidor')
ri['A1'] = 'RETORNO DO INVESTIDOR POR ESTRUTURA (simulação; nada garantido)'; ri['A1'].font = T
ri['A2'] = 'Conversa privada, sem oferta pública. Estrutura e números finais passam por advogado e contador.'
head(ri, 4, ['Estrutura 1 · Mútuo conversível / contrato de participação (LC 155/2016)', 'Valor', 'Nota'])
e1 = [('Valuation pré-money combinado', 600000, R, '[negociar: premissa, não é avaliação]'),
      ('Desconto na conversão', 0.20, PC, 'Prática comum de mercado [Conferir]'),
      ('Valuation de conversão', '=B5*(1-B6)', R, ''),
      ('Participação do investidor se converter', f"={NM['aporte']}/(B7+{NM['aporte']})", PC, 'O Lindson mantém o controle'),
      ('Lucro anual no mês 24 (cenário Base)', f"=SUM('Projeção 24 meses'!L{BLK['Base'][1]-11}:L{BLK['Base'][1]})", R, 'Da aba Projeção'),
      ('Múltiplo de lucro para avaliar a empresa', 4, '0.0"x"', '[premissa de saída: negociar]'),
      ('Valor estimado da participação no mês 24', '=B8*B9*B10', R, 'Só se houver venda/recompra'),
      ('Múltiplo sobre o aporte', f"=B11/{NM['aporte']}", '0.00"x"', 'Ilustrativo')]
for i, (a, v, fmt, nota) in enumerate(e1):
    rr = 5+i; ri.cell(rr, 1, a); c = ri.cell(rr, 2, v); c.number_format = fmt
    if not str(v).startswith('='): c.fill = AM
    ri.cell(rr, 3, nota)
head(ri, 14, ['Estrutura 2 · Revenue share com teto (recomendada)', 'Conservador', 'Base', 'Otimista'])
for j, n in enumerate(cen):
    a, b = BLK[n]
    ri.cell(15, 2+j, f"='Projeção 24 meses'!N{b}").number_format = R
    ri.cell(16, 2+j, f"={L(2+j)}15/{NM['aporte']}").number_format = '0.00"x"'
    ri.cell(17, 2+j, f"=IFERROR(INDEX('Projeção 24 meses'!A{a}:A{b},MATCH(TRUE,INDEX('Projeção 24 meses'!N{a}:N{b}>={NM['aporte']}*{NM['rs_teto']}-1,0),0)),\"depois do mês 24\")")
    ri.cell(18, 2+j, f"=MIN('Projeção 24 meses'!O{a}:O{b})").number_format = R
ri.cell(15, 1, 'Recebido pelo investidor em 24 meses'); ri.cell(16, 1, 'Múltiplo recebido em 24 meses')
ri.cell(17, 1, 'Mês em que o teto é atingido'); ri.cell(18, 1, 'Menor caixa da empresa em 24 meses (com o aporte)')
ri.cell(19, 1, f'Teto total: aporte x teto (aba Premissas). Prazo máximo sugerido: {M.P["rs_prazo"]} meses; se não atingir, o saldo vence sem garantia [decidir com advogado].')
head(ri, 21, ['Estrutura 3 · Sócio-investidor na unidade Orégano Turbo (empresa separada)', 'Valor', 'Nota'])
e3 = [('Valuation pré-money da unidade', 300000, R, '[negociar]'),
      ('Participação do investidor', f"={NM['aporte']}/(B22+{NM['aporte']})", PC, 'Minoritária: Lindson mantém a maioria'),
      ('Lucro do ano 2 (cenário Base)', f"=SUM('Projeção 24 meses'!L{BLK['Base'][1]-11}:L{BLK['Base'][1]})", R, ''),
      ('% do lucro distribuído', 0.5, PC, '[decidir no acordo de sócios]'),
      ('Dividendos do investidor no ano 2', '=B23*B24*B25', R, 'Ilustrativo'),
      ('Anos para recuperar o aporte nesse ritmo', f"={NM['aporte']}/B26", '0.0', '')]
for i, (a, v, fmt, nota) in enumerate(e3):
    rr = 22+i; ri.cell(rr, 1, a); c = ri.cell(rr, 2, v); c.number_format = fmt
    if not str(v).startswith('='): c.fill = AM
    ri.cell(rr, 3, nota)
ri.column_dimensions['A'].width = 66; ri.column_dimensions['C'].width = 40
for c in 'BD': ri.column_dimensions[c].width = 18

# ---------------- Sensibilidade ----------------
s = wb.create_sheet('Sensibilidade')
s['A1'] = 'SENSIBILIDADE · lucro mensal no equilíbrio da carteira (clientes = novos/mês ÷ churn)'; s['A1'].font = T
s['A2'] = 'Fórmula fechada: muda o ticket (linhas) e o churn (colunas), com 2 clientes novos/mês e custos da aba Premissas.'
s['A3'] = 'Clientes novos/mês:'; s['B3'] = 2; s['B3'].fill = AM
tks = [1800, 2000, 2200, 2400, 2600, 2800, 3000]; chs = [0.03, 0.04, 0.05, 0.07, 0.10]
s.cell(5, 1, 'Ticket \\ Churn').font = B
for j, ch in enumerate(chs):
    c = s.cell(5, 2+j, ch); c.number_format = PC; c.fill = AM
for i, tk in enumerate(tks):
    rr = 6+i; c = s.cell(rr, 1, tk); c.number_format = R; c.fill = AM
    for j in range(len(chs)):
        col = L(2+j); cli = f"($B$3/{col}$5)"
        equipe = f"IF({cli}>{NM['lim']},CEILING(({cli}-{NM['lim']})/5,1)*{NM['func']}+{NM['func']}+{NM['acc']},0)"
        f = f"={cli}*$A{rr}*(1-{NM['imp']})-{cli}*{NM['var']}-{NM['fixo']}-{NM['ferr']}-{NM['traf']}-{NM['pl']}-{equipe}"
        s.cell(rr, 2+j, f).number_format = R
s.cell(14, 1, 'Leitura: o churn pesa mais que o ticket. Cada ponto de churn a menos aumenta a carteira de equilíbrio.')
s.cell(16, 1, 'Sensibilidade do cenário Base, lucro acumulado em 24 meses (calculado pelo modelo.py, valores):').font = B
head(s, 17, ['Variação', 'Lucro acumulado 24m', 'Clientes no mês 24'])
base = M.projetar('Base')
var = [('Base', {}), ('Ticket -20%', dict(ticket=2400*0.8)), ('Ticket +20%', dict(ticket=2400*1.2)),
       ('Churn 8%', dict(churn=0.08)), ('Churn 3%', dict(churn=0.03)), ('Metade dos clientes novos', dict(novos_mult=0.5)),
       ('Clientes novos +50%', dict(novos_mult=1.5))]
for i, (nome, kw) in enumerate(var):
    r_ = M.projetar('Base', **kw); rr = 18+i
    s.cell(rr, 1, nome); s.cell(rr, 2, round(sum(l['lucro'] for l in r_['linhas']))).number_format = R
    s.cell(rr, 3, round(r_['linhas'][-1]['cli'], 1))
s.column_dimensions['A'].width = 34
for c in 'BCDEF': s.column_dimensions[c].width = 18
wb.save(out); print('ok', out)
