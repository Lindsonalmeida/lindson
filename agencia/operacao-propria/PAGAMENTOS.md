# Modelos de pagamento: sempre antecipado (MRR ou TCV)

Conta Leandro (Hormozi Squad · Pricing), 05/11/2026.

Pedido do Lindson: "pagamento é sempre antecipado, crie os modelos de pagamentos totais ou mensais, igual à Alpha, modelo MRR, TCV, algo assim".

Calculadora com fórmulas: aba **Pagamentos** de `PROJECAO-PROPRIA.xlsx`. Os preços amarelos e o desconto do Pix são editáveis. Preços: `PRECOS-PIZZARIAS.md` (sugestão, aguardando aprovação).

## 1. Os dois modelos
| | **MRR · mensal antecipado** | **TCV · contrato inteiro na frente** |
|---|---|---|
| O que é | *Monthly Recurring Revenue*: a pizzaria paga **cada mês antes de ele começar** | *Total Contract Value*: a pizzaria paga **o valor total do prazo antes de começar** |
| Como paga | Cartão recorrente (cobra sozinho todo mês) ou Pix até o dia combinado | **Pix à vista com 5% de desconto** ou **cartão em até 3x, 6x ou 12x** (conforme o prazo) |
| Para você | Caixa entra todo mês; risco de atraso e de saída no meio | Caixa entra todo na frente; o limite do cartão garante o contrato |
| Igual à Alpha? | A Alpha mostra o "por mês" | É o "Valor total: R$ X, em até 12x no cartão" da Alpha |

**Regra de ouro:** nada começa sem o pagamento confirmado. Isso vale para o 1º mês, para cada mês do MRR e para o TCV.

## 2. A tabela (preços sugeridos)
| Plano | Prazo | MRR (por mês, antecipado) | TCV (total) | TCV no Pix à vista (−5%) | TCV no cartão |
|---|---|---|---|---|---|
| Muralha | Trimestral | R$ 1.997 | R$ 5.991 | R$ 5.691,45 | 3x de R$ 1.997 |
| Muralha | Semestral | R$ 1.797 | R$ 10.782 | R$ 10.242,90 | 6x de R$ 1.797 |
| Muralha | Anual | R$ 1.597 | R$ 19.164 | R$ 18.205,80 | 12x de R$ 1.597 |
| Fortaleza | Trimestral | R$ 2.997 | R$ 8.991 | R$ 8.541,45 | 3x de R$ 2.997 |
| Fortaleza | Semestral | R$ 2.597 | R$ 15.582 | R$ 14.802,90 | 6x de R$ 2.597 |
| Fortaleza | Anual | R$ 2.197 | R$ 26.364 | R$ 25.045,80 | 12x de R$ 2.197 |
| Cidadela ▲ | Trimestral | R$ 3.997 | R$ 11.991 | R$ 11.391,45 | 3x de R$ 3.997 |
| Cidadela ▲ | Semestral | R$ 3.697 | R$ 22.182 | R$ 21.072,90 | 6x de R$ 3.697 |
| Cidadela ▲ | Anual | R$ 3.497 | R$ 41.964 | R$ 39.865,80 | 12x de R$ 3.497 |

**Como ler:**
- **A parcela do cartão é igual ao MRR.** Para a pizzaria, o valor mensal é o mesmo; a diferença é que o contrato inteiro fica garantido no limite do cartão. Por isso o TCV no cartão é o modelo que você mais quer vender.
- **O Pix à vista ganha 5%**, porque o dinheiro entra todo e sem taxa. O percentual é decisão sua.
- **Taxa do cartão parcelado:** confira na plataforma de cobrança. Decida se você **absorve** (o cliente vê a tabela acima) ou **repassa** (o cliente paga os juros do parcelamento). A Alpha não mostra juros na página.
- **Condição de fundador:** vale nos dois modelos. Exemplo: Fortaleza a R$ 2.197 em 6 meses dá TCV de R$ 13.182, ou 6x de R$ 2.197.

## 3. O que vender primeiro (ordem na conversa)
1. **TCV no cartão, prazo semestral ou anual.** Fale do valor da parcela, que é o mesmo do mensal.
2. Se a pizzaria não tem limite no cartão: **TCV no Pix**, com os 5%.
3. Se não tem o total: **MRR** no mesmo prazo, com cartão recorrente. Se não tiver cartão, Pix antecipado.
4. Se nada cabe: **Raio-X da Pizzaria** (downsell, `PRECOS-PIZZARIAS.md`).

**Frase pronta:** "O valor é o mesmo por mês. A diferença é só se você prefere deixar o contrato todo garantido no cartão ou pagar mês a mês antes de cada mês começar. Qual fica melhor pra você?"

## 4. Regras do contrato (para o `modelo-contrato/`)
| Tema | Regra sugerida | Situação |
|---|---|---|
| Início | O serviço começa depois do pagamento confirmado (TCV) ou do 1º mês pago (MRR) | — |
| MRR em atraso | Serviço pausado no dia seguinte ao vencimento; retoma ao pagar. Após [N] dias, o contrato pode ser encerrado com a multa do prazo | [N]: **decisão do Lindson** |
| Arrependimento | 7 dias com devolução total, se a contratação foi feita fora do estabelecimento ou online (CDC, art. 49) | [Conferir com advogado] |
| Saída antes do fim (TCV) | Devolve os meses não usados, menos uma multa de [X]% sobre eles | [X]: **decisão do Lindson** · [Conferir com advogado] |
| Saída antes do fim (MRR) | Multa de [X]% sobre as mensalidades que faltam | Mesma decisão |
| Renovação | Proposta 30 dias antes do fim, com os números do período; sem renovação automática no TCV | — |
| Verba de anúncio | Paga pela pizzaria direto à Meta, fora do contrato | — |

## 5. Os números para acompanhar (painel do dono, toda segunda)
| Número | O que é | Conta |
|---|---|---|
| **MRR** | Quanto entra por mês de serviço | soma das mensalidades ativas + (TCV ÷ meses) de cada contrato pago na frente |
| **TCV vendido no mês** | Quanto foi contratado no mês | soma dos valores totais fechados |
| **Caixa antecipado** | Dinheiro recebido por serviço ainda não prestado | TCV recebido − meses já entregues |
| **Receita reconhecida** | O que você já "ganhou" de fato | 1/N do TCV a cada mês entregue + MRR pago |
| **Contratos que vencem em 30 dias** | Renovação | lista |

**Verdade efetiva (Maquiavel):** o TCV anual cai todo de uma vez no caixa, mas é dinheiro de 12 meses de trabalho. Quem gasta o anual no 1º mês fica sem caixa no 6º. Guarde o caixa antecipado numa conta separada e transfira 1/N por mês para a conta da operação.

## 6. Como cobrar (ferramenta)
- **A plataforma precisa ter:**
  - cartão parcelado em até 12x;
  - cartão recorrente (assinatura);
  - Pix;
  - link de pagamento para mandar no WhatsApp.
- **A Hubla** já está prevista para os produtos do Estado Próprio. Use a mesma, se ela fizer assinatura e parcelado de serviço, ou outra que faça.
- **Taxas:** confira as da plataforma escolhida antes de fechar o desconto do Pix.

## 7. O que decidir
1. Desconto do Pix à vista (sugestão: 5%).
2. Juros do parcelamento: você absorve ou o cliente paga?
3. Dias de atraso antes de encerrar o MRR.
4. Multa de saída antecipada (% sobre os meses que faltam).
5. Plataforma de cobrança.
