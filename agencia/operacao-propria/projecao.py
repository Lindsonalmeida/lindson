# Gera PROJECAO-PROPRIA.xlsx (conta Leandro, 05/11/2026): operação própria do Lindson, mesmo formato da planilha da Alpha,
# sem taxa de franquia e sem royalties, com a equipe entrando por gatilho de número de clientes. Tudo com fórmula (aba Premissas editável).
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter as L
wb = openpyxl.Workbook(); P = wb.active; P.title = 'Premissas'
AM, PR, CZ = PatternFill('solid', fgColor='F5C518'), PatternFill('solid', fgColor='111111'), PatternFill('solid', fgColor='FFF6CC')
B = Font(bold=True); BW = Font(bold=True, color='F5C518')
prem = [  # (rótulo, valor, formato, nota)
 ('Ticket médio por cliente (R$/mês)', 2400, 'R$ #,##0', 'Mistura dos 3 planos para pizzarias (PRECOS-PIZZARIAS.md). DECISÃO DO LINDSON'),
 ('Taxa de saída de clientes por mês', 0.05, '0%', 'Suposição: trocar pelo número real depois de 6 meses'),
 ('Imposto sobre o faturamento', 0.06, '0%', 'Simples Nacional, faixa inicial. Confirmar com o contador'),
 ('Custo por contato (lead) no anúncio (R$)', 100, 'R$ #,##0', 'SUPOSIÇÃO. A Alpha usa R$ 350. Trocar pelo real medido'),
 ('Contatos que viram cliente', 0.27, '0%', 'Da planilha da Alpha (4 de 15). Medir o seu'),
 ('Custos fixos (ferramentas, contador, sistema) R$/mês', 1500, 'R$ #,##0', 'Da planilha da Alpha'),
 ('Custo variável por cliente (deslocamento, edição extra) R$/mês', 150, 'R$ #,##0', 'Suposição'),
 ('Criador de conteúdo, grava e edita (R$/mês por pessoa)', 2080, 'R$ #,##0', 'Salário do "criador" da planilha da Alpha'),
 ('   … 1 criador a cada N clientes acima de 15 (o Lindson atende 15 sozinho, com a equipe Claude)', 5, '0', 'Decisão do Lindson 05/11: 15 clientes sozinho'),
 ('Gestor de tráfego (R$/mês por pessoa)', 2080, 'R$ #,##0', 'Salário da planilha da Alpha'),
 ('   … 1 gestor a cada N clientes acima de 15', 15, '0', 'Até 15 clientes o Lindson faz o tráfego'),
 ('Closer/SDR (R$/mês) · entra acima de 15 clientes, se os novos do mês forem pelo menos', 2080, 'R$ #,##0', 'SUPOSIÇÃO (a Alpha não informa)'),
 ('   … novos no mês', 3, '0', ''),
 ('Account / atendimento (R$/mês por pessoa)', 3000, 'R$ #,##0', 'Salário da planilha da Alpha'),
 ('   … 1 account a cada N clientes acima de 15', 15, '0', 'Suposição'),
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
     10: f'=ROUNDUP(MAX(0,{col}6-15)/{ref["ed_n"]},0)*{ref["ed"]}',
     11: f'=ROUNDUP(MAX(0,{col}6-15)/{ref["ge_n"]},0)*{ref["ge"]}',
     12: f'=IF(AND({col}6>15,{col}4>={ref["cl_n"]}),{ref["cl"]},0)',
     13: f'=ROUNDUP(MAX(0,{col}6-15)/{ref["ac_n"]},0)*{ref["ac"]}',
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

# ---- Aba "Pagamentos" (05/11, pedido do Lindson: "pagamento é sempre antecipado... modelos totais ou mensais, igual à Alpha, MRR, TCV")
T = wb.create_sheet('Pagamentos')
T['A1'] = 'PAGAMENTO SEMPRE ANTECIPADO · MRR (mensal antecipado) ou TCV (contrato inteiro na frente)'; T['A1'].font = BW; T['A1'].fill = PR
T['A3'] = 'Desconto no Pix à vista do TCV'; T['B3'] = 0.05; T['B3'].number_format = '0%'; T['B3'].fill = CZ; T['B3'].font = B; T['C3'] = 'DECISÃO DO LINDSON'
T['A4'] = 'Taxa do cartão parcelado (se você absorver)'; T['B4'] = 0; T['B4'].number_format = '0.0%'; T['B4'].fill = CZ; T['B4'].font = B; T['C4'] = 'Conferir na plataforma (Hubla ou outra) e decidir se repassa ao cliente'
cab = ['Plano', 'Prazo', 'Meses', 'MRR: mensalidade antecipada', 'TCV: valor total', 'TCV no Pix à vista', 'TCV no cartão: até', 'Parcela no cartão', 'Você recebe no cartão (líquido)']
for c, t in enumerate(cab, 1): x = T.cell(6, c, t); x.font = BW; x.fill = PR; x.alignment = Alignment(wrap_text=True)
precos = [('Muralha', [1997, 1797, 1597]), ('Fortaleza', [2997, 2597, 2197]), ('Cidadela ▲', [3997, 3697, 3497])]
prazos = [('Trimestral', 3, 3), ('Semestral', 6, 6), ('Anual', 12, 12)]
r = 7
for nome, vals in precos:
    for (pz, meses, parc), v in zip(prazos, vals):
        T.cell(r, 1, nome).font = B; T.cell(r, 2, pz); T.cell(r, 3, meses)
        m = T.cell(r, 4, v); m.fill = CZ; m.font = B
        T.cell(r, 5, f'=D{r}*C{r}'); T.cell(r, 6, f'=E{r}*(1-$B$3)'); T.cell(r, 7, parc)
        T.cell(r, 8, f'=E{r}/G{r}'); T.cell(r, 9, f'=E{r}*(1-$B$4)')
        for c in (4, 5, 6, 8, 9): T.cell(r, c).number_format = 'R$ #,##0.00'
        T.cell(r, 7).number_format = '0"x"'
        r += 1
for c, w in zip('ABCDEFGHI', (16, 12, 7, 18, 16, 16, 12, 16, 20)): T.column_dimensions[c].width = w
T.row_dimensions[6].height = 45
T.cell(r + 1, 1, 'Regras: nada começa sem pagamento. MRR = paga o mês antes de ele começar (cartão recorrente ou Pix até o dia combinado). TCV = paga o contrato inteiro antes de começar (Pix à vista com desconto, ou cartão parcelado: o limite do cartão garante o contrato).')
T.cell(r + 2, 1, 'Receita reconhecida: o TCV recebido na frente é serviço de vários meses. Guarde e conte como receita 1/N por mês (MRR equivalente = TCV ÷ meses).')
wb.save('PROJECAO-PROPRIA.xlsx'); print('pagamentos ok')
