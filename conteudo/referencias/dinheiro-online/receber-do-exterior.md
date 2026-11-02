# Receber do exterior (Google, YouTube, EUA, Stripe, PayPal, Wise, Payoneer)

**Situação:** completo (rodada 1, 02/11/2026). Taxas mudam: confira a página oficial antes de decidir.

Regras deste arquivo: cada número tem fonte e data. "Lido no oficial" = página da própria empresa ou do governo lida em 02/11/2026. "Blog" = fonte de terceiros. "Não conferido" = não deu para confirmar.

**Isto não substitui contador.** Tributação depende do caso. No fim há a lista do que levar ao contador.

---

## 1. O mapa: de onde vem o dinheiro e por onde ele passa

| Fonte do dinheiro | Como paga | Onde cai | Imposto no Brasil (PF) |
|---|---|---|---|
| YouTube (AdSense) | Transferência internacional em dólar | Banco brasileiro com câmbio, ou conta global | Carnê-leão mensal |
| AdSense de site | Igual ao YouTube | Igual | Carnê-leão |
| Cliente estrangeiro de serviço | Wire, ACH, cartão (Stripe), PayPal, Payoneer | Conta global ou banco | Carnê-leão (PF) ou nota de exportação (PJ) |
| Plataformas dos EUA (Gumroad, Etsy, Amazon KDP, ClickBank, Upwork, Fiverr) | Direto no banco, Payoneer ou PayPal (varia por plataforma) | Varia | Carnê-leão (PF) ou receita da empresa |
| Hotmart/Kiwify vendendo para fora | A plataforma recebe e paga em reais | Conta brasileira | Como venda nacional da plataforma (confirmar com contador) |

---

## 2. Google AdSense e YouTube

### 2.1 Como o pagamento chega
- **Limite mínimo para pagar: US$ 100.** Fonte: blogs de câmbio (Remessa Online, Nomad, MonetizeMore), consultados em 02/11/2026. Não conferido na Central de Ajuda do AdSense nesta rodada.
- **Forma:** transferência eletrônica internacional, em dólar, para um banco escolhido. Mesmas fontes. O Google processa por volta do dia 21 do mês seguinte (blogs; não conferido no oficial).
- **Tarifa do banco que recebe:** varia muito. Um blog cita bancos tradicionais cobrando de R$ 115 a R$ 440 por recebimento (exiap.com.br, guia 2026); outro cita Bradesco a US$ 100 (blog, não conferido). Bancos digitais com câmbio (Inter, Nomad, Wise e outros) costumam ser mais baratos: **compare antes**.

### 2.2 O imposto dos EUA que o YouTube retém (importante)
- **Desde 2021, o Google retém imposto americano sobre o que o canal ganha com espectadores dos EUA.** Fontes: Tecnoblog (2021), air.io (guia em português) e Unclik, consultados em 02/11/2026.
- **O Brasil não tem tratado contra bitributação com os EUA.** Por isso, mesmo com o formulário fiscal (W-8BEN) preenchido no AdSense, a retenção sobre a receita de espectadores americanos é de **30%**. Fontes: air.io/pt/monetization/youtube-tax-info-w-8ben e Unclik.
- **Sem o formulário,** o Google pode reter **até 24% de toda a receita**, de todos os países. Fonte: Unclik. **Conclusão prática: preencha as informações fiscais no AdSense.**
- O formulário vence em 3 anos. O que já foi retido não volta. Fontes: air.io, Unclik.
- **O imposto retido nos EUA pode ser abatido no carnê-leão**, até o limite do imposto brasileiro sobre aquela renda (air.io; Tactus). Guarde o relatório de retenção do AdSense (e o formulário 1042-S, quando houver).
- **Para os canais do Lindson:** como Passaporte da Bíblia e Raposa e Leão falam português, a maior parte do público deve ser do Brasil. Então a retenção dos EUA pesa pouco. Confira em YouTube Studio > Analytics > Público > Países.

### 2.3 Regras do YPP que mudam em 2027 (complementa o Peter)
- **Hoje:** 1.000 inscritos + 4.000 horas de vídeos longos públicos em 12 meses **ou** 10 milhões de views de Shorts em 90 dias. Lido no oficial (support.google.com/youtube/answer/72851), 02/11/2026.
- **A partir de 01/02/2027, para quem ainda não entrou:** 1.000 inscritos + **8.000 horas** em 12 meses **ou** **20 milhões** de views de Shorts em 90 dias. Fonte: Shacknews, 10/08/2026. A página oficial confirma que o programa muda em 01/02/2027 e que é preciso **aceitar os novos termos no YouTube Studio até 31/01/2027** para continuar monetizando.
- Blogs (vidIQ, AIR) falam de regra de manutenção para quem já é parceiro (1.000 horas por ano ou 1 milhão de views de Shorts). **Não conferido no oficial.**
- **Consequência:** se algum canal do Lindson estiver perto das 4.000 horas, **vale acelerar para entrar antes de 01/02/2027**. Interpretação.

---

## 3. Contas e serviços para receber

| Serviço | Para que serve | Taxas principais | Fonte e data |
|---|---|---|---|
| **Stripe (conta Brasil)** | Cobrar cartão de cliente, inclusive estrangeiro, num site próprio | 3,99% + R$ 0,39 (cartão nacional); **+2%** cartão internacional; boleto R$ 3,45; Pix 1,19% (só por convite); contestação R$ 55 | Lido no oficial, stripe.com/br/pricing, 02/11/2026 |
| **PayPal (conta Brasil)** | Receber de cliente que só paga por PayPal | 4,79% + tarifa fixa (doméstico); **+1,61%** internacional; **conversão 3,5% acima do câmbio base** ao receber em outra moeda; Pix 0,99% | Lido no oficial, paypal.com/br/webapps/mpp/merchant-fees, 02/11/2026 |
| **Payoneer** | Receber de plataformas e clientes dos EUA/Europa com dados bancários locais | Receber em conta da moeda local: grátis; em moeda não local: 1% (mín. US$ 1); saque com conversão para outra moeda: **1,2% a 4%** | Lido no oficial, payoneer.com/pricing, 02/11/2026 |
| **Wise** | Conta com dados bancários dos EUA (ACH) e outros países | Receber USD doméstico (sem Swift): grátis; **wire/Swift em USD: 6,11 USD por pagamento**; conversão: ver simulador | Lido no oficial, wise.com/br/pricing/receive, 02/11/2026 |
| **Banco brasileiro com câmbio** | Receber AdSense e transferências | Tarifa por recebimento + spread do câmbio | Variável; consultar o banco |

**Como escolher (interpretação):**
- **Cliente americano pagando serviço:** mande dados ACH da Wise (sem custo de recebimento) ou cobre por Stripe (custo maior, mas o cliente paga com cartão).
- **Evite receber em dólar pelo PayPal e converter lá dentro:** 1,61% + 3,5% de conversão.
- **YouTube:** banco com câmbio barato, ou conta global que aceite o AdSense (há relatos de que funciona com Wise em USD; **não conferido**).

---

## 4. Câmbio e IOF
- **IOF na entrada de dinheiro do exterior para pessoa física:** fontes indicam **0,38%** (texto consolidado do Decreto 6.306/2007 citado no Decreto 12.466/2025; Remessa Online). Em 2025 houve vaivém: decretos de maio e junho de 2025, sustação pelo Congresso (Decreto Legislativo 176/2025, 27/06/2025) e julgamento no STF. **Não conferi o texto vigente**: confirmar no momento da operação, o banco mostra o IOF no contrato de câmbio.
- **Spread:** a diferença entre o câmbio comercial e o que o banco paga. Costuma ser o custo maior. Compare o valor final em reais, não a "tarifa zero".

---

## 5. Impostos no Brasil

### 5.1 Pessoa física: carnê-leão
- **Quem recebe do exterior sem retenção no Brasil paga o IR todo mês pelo carnê-leão** (programa no e-CAC/Meu Imposto de Renda). Fontes: Fast Company Brasil e Contabilidade Zen (2026); regra geral da Receita.
- **Tabela mensal 2026** (lido no oficial, gov.br/receitafederal, tabelas/2026, 02/11/2026):

| Base mensal | Alíquota | Parcela a deduzir |
|---|---|---|
| Até R$ 2.428,80 | isento | – |
| R$ 2.428,81 a 2.826,65 | 7,5% | R$ 182,16 |
| R$ 2.826,66 a 3.751,05 | 15% | R$ 394,16 |
| R$ 3.751,06 a 4.664,68 | 22,5% | R$ 675,49 |
| Acima de R$ 4.664,68 | 27,5% | R$ 908,73 |

- **Redução nova (Lei 15.270/2025), mesma página oficial:** quem tem rendimento tributável mensal **até R$ 5.000** tem redução de até R$ 312,89 (o imposto pode zerar). De R$ 5.000,01 a R$ 7.350, a redução é R$ 978,62 − 0,133145 × rendimento. Acima de R$ 7.350, não há redução.
- **Exemplo (interpretação, conta simples):** canal que rende US$ 300 no mês a R$ 5,50 = R$ 1.650 → isento. Rende US$ 2.000 = R$ 11.000 → 27,5% − 908,73 = **R$ 2.116,27** de imposto (antes de abater o que os EUA reteram). Nessa faixa, abrir empresa costuma compensar: ver 5.2.
- **Vencimento:** último dia útil do mês seguinte ao recebimento (regra geral do carnê-leão; confirmar no programa).

### 5.2 Empresa (MEI, ME no Simples)
- **MEI pode exportar serviço**, mas **dentro do teto de R$ 81 mil por ano** (contando a exportação) e só se a atividade estiver na lista do MEI. Fontes: Contabilizei, Contabilidade Zen, Contmatic (2026). Há o PLP 187/2025, que mudaria isso; **situação não conferida**.
- **YouTuber em geral não cabe no MEI:** a produção de vídeo (CNAE 5911-1/99) não está na lista do MEI na interpretação mais comum. Fontes: Contabilidade Zen e Tactus (2026). A Alkantara (marketing) também precisa conferir se o CNAE dela está na lista.
- **ME no Simples Nacional:** as fontes divergem se o criador cai no Anexo III (a partir de 6%) ou no Anexo V (a partir de 15,5%), o que depende do CNAE e do **Fator R** (folha/pró-labore ≥ 28% da receita leva ao Anexo III). Fontes: contabilidade.com, Tactus, Contabilidade Zen (2026). **Decisão do contador.**
- **Exportação de serviço tem vantagens:** PIS e Cofins não incidem quando o dinheiro entra no Brasil (Leis 10.637/2002 e 10.833/2003), e o ISS não incide sobre exportação de serviço (LC 116/2003, art. 2º), **salvo quando o resultado do serviço acontece no Brasil**. Fontes: guias de contabilidade (2026) que citam as leis. No Simples, a receita de exportação é informada separada no PGDAS para tirar esses tributos.
- **Atenção à reforma tributária (IBS/CBS):** entra em transição a partir de 2026–2027. As regras da exportação de serviço tendem a manter a desoneração, mas **não conferi o texto final**. Perguntar ao contador.

### 5.3 O que levar ao contador (checklist)
1. Quanto entra por mês de fora (YouTube, clientes, plataformas) e de onde.
2. Relatórios de retenção do AdSense (imposto dos EUA) e o 1042-S.
3. Se compensa tirar o YouTube do CPF e pôr numa ME (Simples, Anexo III com Fator R).
4. Se a Alkantara pode faturar serviço para cliente do exterior como exportação (nota com campo de exportação, sem ISS/PIS/Cofins).
5. Qual banco/conta usar para o contrato de câmbio sair com a natureza certa (serviço, direito autoral, publicidade).
6. Como a reforma tributária (CBS/IBS) muda isso em 2027.

---

## 6. Riscos ao receber do exterior
- **Conta bloqueada por verificação** (PayPal, Payoneer, Wise pedem comprovantes). Tenha contrato, invoice e site da empresa à mão.
- **Estorno (chargeback) em cartão internacional:** Stripe cobra R$ 55 por contestação (lido no oficial). Contrato e prova de entrega evitam perda.
- **Golpe do "cliente estrangeiro" que paga a mais e pede devolução:** ver `golpes-e-riscos.md`.
- **Esquecer o carnê-leão:** multa e juros. Pagar todo mês, mesmo em valor baixo.

---

## Uso pelo agente
- **Lição 1:** dinheiro de fora só vale o que sobra em reais. Some taxa da plataforma + conversão + IOF + IR antes de comemorar. *(Interpretação)*
- **Lição 2:** preencha o W-8BEN no AdSense. Sem ele, perde até 24% de tudo; com ele, só os 30% sobre a parte dos EUA.
- **Lição 3:** canal no CPF acima de uns R$ 5 mil/mês paga 27,5% na margem. Leve ao contador a ideia de ME no Simples.
- **Lição 4:** antes de 01/02/2027, aceitar os novos termos do YPP no Studio e, se der, bater as 4.000 horas antes da regra nova.
- Maquiavel diria que o príncipe prudente "fa come gli arcieri prudenti" (faz como os arqueiros prudentes), mirando mais alto para acertar onde quer (*Príncipe* VI): calcule a sobra líquida, não o bruto.

## Lacunas (próxima rodada)
- Limite e data exata de pagamento do AdSense na Central de Ajuda oficial (só blogs).
- Percentual de receita dos longos (55%) e dos Shorts (45%): só reportagens de 2022–2023; não achei página oficial atual.
- IOF vigente na entrada de recursos (texto atual do Decreto 6.306 após o STF).
- Taxa de conversão da Wise para BRL (depende do dia; usar o simulador).
- Se o AdSense paga para Wise/Nomad em USD sem problema (relatos, não conferido).
- Regras de exportação de serviço sob a reforma tributária (LC 214/2025).
- Situação do PLP 187/2025 (MEI exportador).
