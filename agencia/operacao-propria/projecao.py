# Gera PROJECAO-PROPRIA.xlsx (conta Leandro, 05/11/2026): operação própria do Lindson, mesmo formato da planilha da Alpha,
# sem taxa de franquia e sem royalties, com a equipe entrando por gatilho de número de clientes. Tudo com fórmula (aba Premissas editável).
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter as L
wb = openpyxl.Workbook(); P = wb.active; P.title = 'Premissas'
AM, PR, CZ = PatternFill('solid', fgColor='F5C518'), PatternFill('solid', fgColor='111111'), PatternFill('solid', fgColor='FFF6CC')
B = Font(bold=True); BW = Font(bold=True, color='F5C518')
prem = [  # (rótulo, valor, formato, nota)
 ('Ticket médio por cliente (R$/mês)', 3000, 'R$ #,##0', 'Mistura Muralha R$ 2.200 e Fortaleza R$ 3.500. DECISÃO DO LINDSON'),
 ('Taxa de saída de clientes por mês', 0.05, '0%', 'Suposição: trocar pelo número real depois de 6 meses'),
 ('Imposto sobre o faturamento', 0.06, '0%', 'Simples Nacional, faixa inicial. Confirmar com o contador'),
 ('Custo por contato (lead) no anúncio (R$)', 100, 'R$ #,##0', 'SUPOSIÇÃO. A Alpha usa R$ 350. Trocar pelo real medido'),
 ('Contatos que viram cliente', 0.27, '0%', 'Da planilha da Alpha (4 de 15). Medir o seu'),
 ('Custos fixos (ferramentas, contador, sistema) R$/mês', 1500, 'R$ #,##0', 'Da planilha da Alpha'),
 ('Custo variável por cliente (deslocamento, edição extra) R$/mês', 150, 'R$ #,##0', 'Suposição'),
 ('Criador de conteúdo, grava e edita (R$/mês por pessoa)', 2080, 'R$ #,##0', 'Salário do "criador" da planilha da Alpha'),
 ('   … 1 criador a cada N clientes acima de 4 (o Lindson atende 4 sozinho)', 5, '0', 'Suposição; os 4 primeiros são do Lindson (esteira-de-produtos.md)'),
 ('Gestor de tráfego (R$/mês por pessoa)', 2080, 'R$ #,##0', 'Salário da planilha da Alpha'),
 ('   … 1 gestor a cada N clientes (entra acima de 8)', 15, '0', 'Suposição; até 8 clientes o Lindson faz o tráfego'),
 ('Closer/SDR (R$/mês) · entra quando os novos do mês forem pelo menos', 2080, 'R$ #,##0', 'SUPOSIÇÃO (a Alpha não informa)'),
 ('   … novos no mês', 3, '0', ''),
 ('Account / atendimento (R$/mês por pessoa)', 3000, 'R$ #,##0', 'Salário da planilha da Alpha'),
 ('   … 1 account a cada N clientes (entra acima de 12)', 15, '0', 'Suposição'),
 ('Pró-labore do Lindson (R$/mês)', 0, 'R$ #,##0', 'DECISÃO DO LINDSON (0 = tudo vira lucro da empresa)'),
 ('Clientes que já pagam hoje (entram no mês 1)', 0, '0', 'LINDSON PREENCHE (Leo, Jaci, Rafael, SF, Real Time, Tribuna: quantos pagam plano mensal)'),
]
P['A1'] = 'PREMISSAS · troque os valores amarelos'; P['A1'].font = BW; P['A1'].fill = PR
for i, (r, v, f, n) in enumerate(prem, 3):
    P.cell(i, 1, r); c = P.cell(i, 2, v); c.number_format = f; c.fill = CZ; c.font = B; P.cell(i, 3, n).font = Font(italic=True, color='777777')
P['A21'] = 'Clientes novos por mês (meta de vendas · DECISÃO DO LINDSON)'; P['A21'].font = B
novos = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4, 4]
for m in range(12):
    P.cell(22, m + 2, f'Mês {m+1}').font = B; c = P.cell(23, m + 2, novos[m]); c.fill = CZ; c.font = B
P.cell(23, 1, 'Novos'); P.column_dimensions['A'].width = 62; P.column_dimensions['C'].width = 70
ref = {k: f'Premissas!$B${i}' for i, k in enumerate(['ticket', 'churn', 'imp', 'cpl', 'conv', 'fixo', 'var', 'ed', 'ed_n', 'ge', 'ge_n', 'cl', 'cl_n', 'ac', 'ac_n', 'pl', 'base'], 3)}

S = wb.create_sheet('Projeção')
S['A1'] = 'PROJEÇÃO · OPERAÇÃO PRÓPRIA (sem franquia, sem royalties)'; S['A1'].font = BW; S['A1'].fill = PR
linhas = ['Clientes no início', 'Novos clientes', 'Saídas', 'Clientes no fim', 'FATURAMENTO', 'Imposto', 'Anúncio para atrair clientes',
          'Criadores (grava e edita)', 'Gestores de tráfego', 'Closer/SDR', 'Account', 'Custos fixos', 'Custo variável', 'Pró-labore', 'LUCRO DO MÊS', 'LUCRO ACUMULADO', 'Contatos (leads) necessários']
for j, t in enumerate(linhas, 3): S.cell(j, 1, t).font = B
for m in range(12):
    c = m + 2; col = L(c); prev = L(c - 1)
    S.cell(2, c, f'Mês {m+1}').font = B
    f = {
     3: f'={ref["base"]}' if m == 0 else f'={prev}6',
     4: f'=Premissas!{L(m+2)}23',
     5: f'=ROUND({col}3*{ref["churn"]},0)',
     6: f'={col}3+{col}4-{col}5',
     7: f'={col}3*{ref["ticket"]}',  # quem fecha no mês começa a pagar no mês seguinte (igual à planilha da Alpha)
     8: f'={col}7*{ref["imp"]}',
     19: f'=ROUNDUP({col}4/{ref["conv"]},0)',
     9: f'={col}19*{ref["cpl"]}',
     10: f'=ROUNDUP(MAX(0,{col}6-4)/{ref["ed_n"]},0)*{ref["ed"]}',
     11: f'=IF({col}6>8,ROUNDUP({col}6/{ref["ge_n"]},0),0)*{ref["ge"]}',
     12: f'=IF({col}4>={ref["cl_n"]},{ref["cl"]},0)',
     13: f'=IF({col}6>12,ROUNDUP({col}6/{ref["ac_n"]},0),0)*{ref["ac"]}',
     14: f'={ref["fixo"]}',
     15: f'={col}6*{ref["var"]}',
     16: f'={ref["pl"]}',
     17: f'={col}7-SUM({col}8:{col}16)',
     18: f'={col}17' if m == 0 else f'={prev}18+{col}17',
    }
    for r, v in f.items():
        x = S.cell(r, c, v); x.number_format = '0' if r in (3, 4, 5, 6, 19) else 'R$ #,##0'
        if r in (7, 17, 18): x.font = B
for r in (7, 17, 18):
    for c in range(1, 14): S.cell(r, c).fill = CZ
S.column_dimensions['A'].width = 30
for c in range(2, 14): S.column_dimensions[L(c)].width = 12
S['A21'] = 'Comparação: no mesmo período, a franquia Alpha custaria a taxa de R$ 30.000 + 20% do faturamento (royalties 18% + marketing 2%).'
S['A22'] = 'Royalties que você deixa de pagar (12 meses):'; S['B22'] = '=SUM(B7:M7)*20%'; S['B22'].number_format = 'R$ #,##0'; S['B22'].font = B
S['A23'] = 'Economia total sem a franquia (12 meses):'; S['B23'] = '=B22+30000'; S['B23'].number_format = 'R$ #,##0'; S['B23'].font = B
wb.save('PROJECAO-PROPRIA.xlsx'); print('ok')
