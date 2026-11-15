"""Gera PLANO-INVESTIDOR.xlsx v2 (empresa inteira) com fórmulas reais. Premissas em amarelo.
Uso: python3 planilha.py <saida.xlsx>"""
import sys
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter as L
import modelo as M

out = sys.argv[1] if len(sys.argv) > 1 else 'PLANO-INVESTIDOR.xlsx'
wb = Workbook()
AM = PatternFill('solid', fgColor='F5C518'); PR = PatternFill('solid', fgColor='0A0A0A')
B = Font(bold=True); BW = Font(bold=True, color='FFFFFF'); T = Font(bold=True, size=14)
R = '"R$" #,##0'; PC = '0.0%'; N1 = '0.0'
cen = list(M.CEN)
def head(ws, r, vals, c0=1):
    for i, v in enumerate(vals):
        x = ws.cell(r, c0+i, v); x.fill = PR; x.font = BW; x.alignment = Alignment(wrap_text=True, vertical='center')

ws = wb.active; ws.title = 'Premissas'
ws['A1'] = 'PLANO INVESTIDOR v2 · EMPRESA INTEIRA · PREMISSAS (amarelo = editável)'; ws['A1'].font = T
ws['A2'] = 'Projeção, não promessa. Conversa privada, sem oferta pública; estrutura final com advogado e contador.'
head(ws, 4, ['Premissa comum', 'Valor', '', 'Origem'])
P = M.P
comuns = [
    ('aporte', 'Aporte do investidor', P['aporte'], R, 'Proposta (faixa R$ 80 a 120 mil)'),
    ('base', 'Receita atual da agência/mês (base)', P['base_agencia'], R, 'Lindson 15/11: Jaci 1.500 + Leo 2.500 + WF 800'),
    ('cbase', 'Clientes pagantes hoje', P['clientes_base'], '0', 'Jaci, Leo Pinto, WF Celulares'),
    ('fixo', 'Custos fixos/mês', P['fixo'], R, 'PRECOS-PIZZARIAS.md [preencher com o real]'),
    ('ferr', 'Ferramentas/mês', P['ferramentas'], R, '[estimativa]'),
    ('pl', 'Pró-labore/mês', P['prolabore'], R, 'DECISOES-APROVADAS 20 (R$ 3.000) [confirmar]'),
    ('var', 'Custo variável por cliente/mês', P['var_cliente'], R, 'PRECOS-PIZZARIAS.md'),
    ('imp', 'Imposto sobre a receita', P['imposto'], PC, '[Conferir com contador]'),
    ('tag', 'Tráfego agência/mês', P['traf_ag'], R, 'Proposta'),
    ('tot0', 'Tráfego Orégano meses 1-2', P['traf_ot0'], R, 'DECISOES-APROVADAS 19'),
    ('tot', 'Tráfego Orégano depois', P['traf_ot'], R, 'Proposta'),
    ('tpd', 'Tráfego produtos/mês (meses 2 a 11)', P['traf_pd'], R, 'Proposta (teste)'),
    ('pdtk', 'Preço médio do produto digital', P['pd_ticket'], R, 'Sugestão (R$ 19 a 47); preço final do Lindson'),
    ('pdtx', 'Taxa da plataforma (Hubla)', P['pd_taxa'], PC, '[Conferir]'),
    ('func', 'Custo criador/gestor/mês', P['custo_func'], R, 'README operação própria'),
    ('acc', 'Custo account/mês', P['custo_account'], R, 'README operação própria'),
    ('lim', 'Clientes que o Lindson atende sozinho', P['limite_solo'], '0', 'Decisão 05/11'),
    ('cri0', '1º criador financiado: mês inicial', P['cri_ini'], '0', 'Uso do dinheiro'),
    ('cri1', '1º criador financiado: mês final', P['cri_fim'], '0', 'Uso do dinheiro'),
    ('ini', 'Gasto único mês 1 (equipamento + jurídico)', P['gasto_ini'], R, 'Uso do dinheiro'),
    ('rsp', 'Revenue share: % da receita NOVA', P['rs_pct'], PC, 'Estrutura recomendada'),
    ('rst', 'Revenue share: teto (x aporte)', P['rs_teto'], '0.00"x"', 'Estrutura recomendada'),
    ('rsc', 'Revenue share: carência (meses)', P['rs_carencia'], '0', 'Estrutura recomendada'),
    ('mult', 'Multiplicador de clientes novos', 1, '0.00', 'Sensibilidade (0,5 = metade)'),
]
NM = {}; r = 5
for k, rot, v, fmt, org in comuns:
    ws.cell(r, 1, rot); c = ws.cell(r, 2, v); c.fill = AM; c.number_format = fmt; ws.cell(r, 4, org); NM[k] = f"Premissas!$B${r}"; r += 1
r += 1; head(ws, r, ['Premissa por cenário', 'Conservador', 'Base', 'Otimista', 'Origem']); r += 1
SC = {}
rows = [('agn', 'Agência: clientes novos/mês', 'ag_novos', N1, 'Proposta'), ('agt', 'Agência: ticket médio dos novos', 'ag_ticket', R, 'Esteira R$ 600 a 3.500 (esteira-de-produtos.md)'),
        ('agc', 'Agência: churn/mês dos novos', 'ag_churn', PC, 'Premissa'),
        ('o1', 'Orégano: novos mês 1', 0, N1, 'Rampa'), ('o2', 'Orégano: novos mês 2', 1, N1, 'Rampa'), ('o3', 'Orégano: novos mês 3', 2, N1, 'Rampa'), ('o4', 'Orégano: novos mês 4', 3, N1, 'Rampa'),
        ('od', 'Orégano: novos/mês depois', 'ot_d', N1, 'Meta aprovada: 2/mês'), ('ott', 'Orégano: ticket médio', 'ot_ticket', R, 'Tabela aprovada R$ 1.597 a 3.997'),
        ('otc', 'Orégano: churn/mês', 'ot_churn', PC, 'projecao.py usa 5%'), ('cpa', 'Produtos: custo por venda (CPA)', 'pd_cpa', R, 'Premissa a medir')]
for k, rot, key, fmt, org in rows:
    ws.cell(r, 1, rot)
    for j, n in enumerate(cen):
        v = M.CEN[n]['ot_novos'][key] if isinstance(key, int) else M.CEN[n][key]
        c = ws.cell(r, 2+j, v); c.fill = AM; c.number_format = fmt
    ws.cell(r, 5, org); SC[k] = r; r += 1
for col, w in zip('ABCDE', (46, 16, 16, 16, 48)): ws.column_dimensions[col].width = w
def sc(k, j): return f"Premissas!${L(2+j)}${SC[k]}"

u = wb.create_sheet('Uso do dinheiro')
u['A1'] = 'USO DO DINHEIRO POR UNIDADE (prioridade 1 = rende primeiro)'; u['A1'].font = T
head(u, 3, ['Unidade', 'Item', 'Detalhe', 'Valor', '%', 'Quando', 'Prioridade'])
for i, (un, a, d, v, q, p) in enumerate(M.USO):
    rr = 4+i; u.cell(rr, 1, un); u.cell(rr, 2, a); u.cell(rr, 3, d); c = u.cell(rr, 4, v); c.fill = AM; c.number_format = R
    u.cell(rr, 5, f"=D{rr}/$D${4+len(M.USO)}").number_format = PC; u.cell(rr, 6, q); u.cell(rr, 7, p)
tr = 4+len(M.USO); u.cell(tr, 2, 'TOTAL').font = B; u.cell(tr, 4, f"=SUM(D4:D{tr-1})").number_format = R
u.cell(tr+1, 2, 'Confere com o aporte?'); u.cell(tr+1, 4, f'=IF(D{tr}={NM["aporte"]},"OK","AJUSTAR")')
for col, w in zip('ABCDEFG', (18, 38, 60, 13, 8, 16, 10)): u.column_dimensions[col].width = w

def bloco_rows(j): s = 4 + j*29; return s, s+2   # título em s, cabeçalho s+1, dados s+2..s+25
def unidade(nome, cols, fn):
    sh = wb.create_sheet(nome); sh['A1'] = f'{nome.upper()} · 24 meses por cenário (projeção)'; sh['A1'].font = T
    for j, n in enumerate(cen):
        s, f0 = bloco_rows(j); sh.cell(s, 1, f'Cenário {n}').font = B; head(sh, s+1, cols)
        for m in range(1, 25):
            rr = f0+m-1; pv = rr-1; sh.cell(rr, 1, m)
            for ci, (f, fmt) in enumerate(fn(j, m, rr, pv), start=2):
                c = sh.cell(rr, ci, f); c.number_format = fmt
    for i in range(1, len(cols)+1): sh.column_dimensions[L(i)].width = 15
    return sh
# Agência: B novos, C clientes novos acumulados, D receita (base + novos), E clientes totais
unidade('Agência', ['Mês', 'Novos', 'Carteira nova', 'Receita', 'Clientes totais'], lambda j, m, rr, pv: [
    (f"={sc('agn',j)}*{NM['mult']}", N1), (f"={('C'+str(pv)) if m>1 else '0'}*(1-{sc('agc',j)})+B{rr}", N1),
    (f"={NM['base']}+C{rr}*{sc('agt',j)}", R), (f"={NM['cbase']}+C{rr}", N1)])
unidade('Orégano Turbo', ['Mês', 'Novos', 'Pizzarias', 'Receita'], lambda j, m, rr, pv: [
    (f"=IF(A{rr}<=4,INDEX({sc('o1',j)}:{sc('o4',j)},A{rr}),{sc('od',j)})*{NM['mult']}", N1),
    (f"={('C'+str(pv)) if m>1 else '0'}*(1-{sc('otc',j)})+B{rr}", N1), (f"=C{rr}*{sc('ott',j)}", R)])
unidade('Produtos digitais', ['Mês', 'Tráfego', 'Vendas', 'Receita líquida'], lambda j, m, rr, pv: [
    (f"=IF(AND(A{rr}>=2,A{rr}<=11),{NM['tpd']},0)", R), (f"=B{rr}/{sc('cpa',j)}", N1), (f"=C{rr}*{NM['pdtk']}*(1-{NM['pdtx']})", R)])
yt = wb.create_sheet('YouTube e Tecnologia')
yt['A1'] = 'YOUTUBE, MARCA PESSOAL, TECNOLOGIA E EQUIPE DE IA'; yt['A1'].font = T
for i, (a, b_) in enumerate([
    ('Canais dark (Passaporte da Bíblia, Raposa e Leão)', 'Receita não projetada até monetizar. [preencher: inscritos, horas, status do YPP]'),
    ('Manual de Campo (Raposa e Leão, PDF 50 p.)', 'Entra na aba Produtos digitais (preço sugerido R$ 37, a decidir)'),
    ('Marca pessoal @lindsonalmeida_', 'Canal de aquisição da agência; sem receita própria projetada'),
    ('Tecnologia: Central do Cliente, painéis, app SDR, robô do WhatsApp, Dublê, VEKTOR', 'Ativo interno; SaaS é opção futura, sem receita projetada'),
    ('Equipe de IA (4 contas + agentes)', 'Custo dentro de Ferramentas; substitui contratação até 15 clientes')]):
    yt.cell(3+i, 1, a); yt.cell(3+i, 2, b_)
yt.column_dimensions['A'].width = 70; yt.column_dimensions['B'].width = 80

co = wb.create_sheet('Consolidado')
co['A1'] = 'CONSOLIDADO DA EMPRESA · 24 meses por cenário (projeção, não promessa)'; co['A1'].font = T
cols = ['Mês', 'Rec. agência', 'Rec. Orégano', 'Rec. produtos', 'Receita total', 'Clientes', 'Tráfego', 'Equipe', 'Fixos+ferr+PL', 'Variável', 'Imposto', 'Custos', 'Lucro', 'Rec. nova', 'Revenue share', 'RS acumulado', 'Caixa']
BLK = {}
for j, n in enumerate(cen):
    s, f0 = bloco_rows(j); co.cell(s, 1, f'Cenário {n}').font = B; head(co, s+1, cols); BLK[n] = (f0, f0+23)
    for m in range(1, 25):
        rr = f0+m-1; pv = rr-1; co.cell(rr, 1, m)
        F = [f"='Agência'!D{rr}", f"='Orégano Turbo'!D{rr}", f"='Produtos digitais'!D{rr}", f"=SUM(B{rr}:D{rr})",
             f"='Agência'!E{rr}+'Orégano Turbo'!C{rr}",
             f"={NM['tag']}+IF(A{rr}<=2,{NM['tot0']},{NM['tot']})+'Produtos digitais'!B{rr}",
             f"=IF(F{rr}>{NM['lim']},CEILING((F{rr}-{NM['lim']})/5,1)*{NM['func']}+{NM['func']}+{NM['acc']},IF(AND(A{rr}>={NM['cri0']},A{rr}<={NM['cri1']}),{NM['func']},0))",
             f"={NM['fixo']}+{NM['ferr']}+{NM['pl']}", f"=F{rr}*{NM['var']}", f"=E{rr}*{NM['imp']}", f"=SUM(G{rr}:K{rr})", f"=E{rr}-L{rr}",
             f"=MAX(E{rr}-{NM['base']},0)"]
        acp = f"P{pv}" if m > 1 else "0"
        F += [f"=IF(AND(A{rr}>{NM['rsc']},{acp}<{NM['aporte']}*{NM['rst']}),MIN(N{rr}*{NM['rsp']},{NM['aporte']}*{NM['rst']}-{acp}),0)",
              f"={acp}+O{rr}", f"={('Q'+str(pv)) if m>1 else NM['aporte']}+M{rr}-O{rr}-IF(A{rr}=1,{NM['ini']},0)"]
        for ci, f in enumerate(F, start=2):
            c = co.cell(rr, ci, f); c.number_format = N1 if ci == 6 else R
    t = f0+24; co.cell(t, 1, 'Total 24m').font = B
    for ci in (5, 12, 13, 15):
        co.cell(t, ci, f"=SUM({L(ci)}{f0}:{L(ci)}{f0+23})").number_format = R
for i in range(1, 18): co.column_dimensions[L(i)].width = 13

ue = wb.create_sheet('Unit economics')
ue['A1'] = 'UNIT ECONOMICS (premissas a medir)'; ue['A1'].font = T
head(ue, 3, ['Métrica', 'Conservador', 'Base', 'Otimista', 'Como'])
mets = []
for un, tk, ch, nv, tr in (('Agência', 'agt', 'agc', 'agn', NM['tag']), ('Orégano', 'ott', 'otc', 'od', NM['tot'])):
    mets += [(f'{un}: margem/cliente/mês', lambda j, tk=tk: f"={sc(tk,j)}*(1-{NM['imp']})-{NM['var']}", R, 'Ticket - imposto - variável'),
             (f'{un}: LTV 12 meses', lambda j, tk=tk, ch=ch: f"=({sc(tk,j)}*(1-{NM['imp']})-{NM['var']})*MIN(1/{sc(ch,j)},12)", R, 'Visão prudente'),
             (f'{un}: CAC cheio (tráfego/novos + R$ 500)', lambda j, nv=nv, tr=tr: f"={tr}/{sc(nv,j)}+500", R, '[premissa]'),
             (f'{un}: payback (meses)', lambda j, tk=tk, nv=nv, tr=tr: f"=({tr}/{sc(nv,j)}+500)/({sc(tk,j)}*(1-{NM['imp']})-{NM['var']})", '0.0', 'CAC ÷ margem')]
mets += [('Produtos: receita líquida por venda ÷ CPA (ROAS)', lambda j: f"={NM['pdtk']}*(1-{NM['pdtx']})/{sc('cpa',j)}", '0.00"x"', 'Abaixo de 1 = para o tráfego')]
for i, (rot, f, fmt, como) in enumerate(mets):
    rr = 4+i; ue.cell(rr, 1, rot)
    for j in range(3): ue.cell(rr, 2+j, f(j)).number_format = fmt
    ue.cell(rr, 5, como)
ue.column_dimensions['A'].width = 48; ue.column_dimensions['E'].width = 30
for c_ in 'BCD': ue.column_dimensions[c_].width = 15

ri = wb.create_sheet('Retorno do investidor')
ri['A1'] = 'RETORNO DO INVESTIDOR POR ESTRUTURA (simulação; nada garantido)'; ri['A1'].font = T
ri['A2'] = 'Conversa privada, sem oferta pública. Valores finais com advogado e contador.'
head(ri, 4, ['Estrutura 2 · Revenue share sobre a receita NOVA (recomendada)', 'Conservador', 'Base', 'Otimista'])
for j, n in enumerate(cen):
    a, b_ = BLK[n]
    ri.cell(5, 2+j, f"=Consolidado!P{b_}").number_format = R
    ri.cell(6, 2+j, f"={L(2+j)}5/{NM['aporte']}").number_format = '0.00"x"'
    ri.cell(7, 2+j, f"=IFERROR(INDEX(Consolidado!A{a}:A{b_},MATCH(TRUE,INDEX(Consolidado!P{a}:P{b_}>={NM['aporte']}*{NM['rst']}-1,0),0)),\"depois do mês 24\")")
    ri.cell(8, 2+j, f"=MIN(Consolidado!Q{a}:Q{b_})").number_format = R
for i, t in enumerate(['Recebido em 24 meses', 'Múltiplo em 24 meses', 'Mês do teto', 'Menor caixa da empresa em 24 meses']): ri.cell(5+i, 1, t)
head(ri, 10, ['Estrutura 1 · Mútuo conversível / anjo (LC 155/2016)', 'Valor', 'Nota'])
e1 = [('Valuation pré-money combinado', 800000, R, '[negociar]'), ('Desconto na conversão', 0.2, PC, '[Conferir]'),
      ('Participação se converter', f"={NM['aporte']}/(B11*(1-B12)+{NM['aporte']})", PC, 'Lindson mantém o controle'),
      ('Lucro do ano 2 (Base)', f"=SUM(Consolidado!M{BLK['Base'][1]-11}:M{BLK['Base'][1]})", R, ''),
      ('Múltiplo de lucro (saída)', 4, '0.0"x"', '[premissa]'), ('Valor ilustrativo da participação', '=B13*B14*B15', R, 'Só com venda/recompra')]
for i, (a, v, fmt, nt) in enumerate(e1):
    rr = 11+i; ri.cell(rr, 1, a); c = ri.cell(rr, 2, v); c.number_format = fmt; ri.cell(rr, 3, nt)
    if not str(v).startswith('='): c.fill = AM
head(ri, 18, ['Estrutura 3 · Sócio-investidor numa unidade (ex.: Orégano Turbo separada)', 'Valor', 'Nota'])
e3 = [('Valuation pré-money da unidade', 300000, R, '[negociar]'), ('Participação', f"={NM['aporte']}/(B19+{NM['aporte']})", PC, 'Minoritária'),
      ('Lucro do ano 2 da unidade (aprox.: receita Orégano x 40%)', f"=SUM('Orégano Turbo'!D{BLK['Base'][1]-11}:D{BLK['Base'][1]})*0.4", R, '[premissa de margem]'),
      ('% distribuído', 0.5, PC, '[acordo de sócios]'), ('Dividendos no ano 2', '=B20*B21*B22', R, 'Ilustrativo')]
for i, (a, v, fmt, nt) in enumerate(e3):
    rr = 19+i; ri.cell(rr, 1, a); c = ri.cell(rr, 2, v); c.number_format = fmt; ri.cell(rr, 3, nt)
    if not str(v).startswith('='): c.fill = AM
ri.column_dimensions['A'].width = 66; ri.column_dimensions['C'].width = 30
for c_ in 'BD': ri.column_dimensions[c_].width = 18

s = wb.create_sheet('Sensibilidade')
s['A1'] = 'SENSIBILIDADE DO CENÁRIO BASE (valores calculados pelo modelo.py)'; s['A1'].font = T
head(s, 3, ['Variação', 'Lucro 24m', 'Receita mês 24', 'Mês do teto do RS'])
var = [('Base', {}), ('Metade dos clientes novos', dict(mult=0.5)), ('Clientes novos +50%', dict(mult=1.5)), ('Ticket -20%', dict(ticket_mult=0.8)),
       ('Ticket +20%', dict(ticket_mult=1.2)), ('Churn 8% (agência e Orégano)', dict(ag_churn=0.08, ot_churn=0.08)), ('Churn 3%', dict(ag_churn=0.03, ot_churn=0.03))]
for i, (nm, kw) in enumerate(var):
    r_ = M.projetar('Base', **kw); r6 = M.projetar('Base', 60, **kw)
    s.cell(4+i, 1, nm); s.cell(4+i, 2, round(sum(l['lucro'] for l in r_['linhas']))).number_format = R
    s.cell(4+i, 3, round(r_['linhas'][-1]['rec'])).number_format = R; s.cell(4+i, 4, r6['quitado'] or '>60')
s.column_dimensions['A'].width = 34
for c_ in 'BCD': s.column_dimensions[c_].width = 18
wb.move_sheet('Consolidado', offset=-6)
wb.save(out); print('ok', out)
