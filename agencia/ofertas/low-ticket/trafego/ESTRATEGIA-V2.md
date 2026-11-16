# Tráfego dos low ticket (Hubla) · Bio que Vende em 15 Minutos · estratégia v2
(conta Pedro, 16/11/2026. Base: `../produtos/bio-que-vende/OFERTA.md`, `../venda/ESCADA.md`, `../venda/ESTRUTURA.md`, `../hormozi.md`, `../maquiavel.md`, `../RANKING.md` · Meta Andromeda: privado `dados/agencia/referencias/meta-andromeda/README.md`)

## 0. O que sabemos e o que falta
- Não há prompt v1 de extensão para os low ticket no repositório (só os da Real Time). Esta v2 parte de um **diagnóstico de premissas**: a extensão primeiro lê o que existe e compara.
- **Preço:** "o Lindson define" (OFERTA.md). Não há valor gravado. **Link Hubla:** ainda `PREENCHER` em `agencia/sistema-clientes/site/functions/_membros.js`. **Pixel/CAPI na Hubla:** não registrado.
- Sem número inventado e sem promessa de resultado: as contas abaixo são fórmulas para preencher com o preço real.

## 1. O que os agentes disseram (arquivos lidos em `/root/.claude/commands/`)
| Agente | Contribuição aplicada |
|---|---|
| Traffic Chief | Diagnosticar antes de mexer: problema é oferta, rastreio, criativo ou estrutura? A v2 começa lendo o estado e checando o pixel. |
| Pixel Specialist | Navegador + servidor sempre: Pixel da Hubla + API de Conversões; evento **Purchase** com valor e moeda; sem isso, otimizar para compra é às cegas. |
| Pedro Sobral | Mercado BR: estrutura simples, campanha de Vendas, executar e ler o número, sem lenda de "público quente mágico". |
| Molly Pittman | Mínimo de 2 ganchos por avatar; cada gancho vira criativo visualmente diferente. |
| Depesh Mandalia | CBO com poucos conjuntos; testar por "graduação": conceito que vence volta em lote; avatares (5W). |
| Media Buyer | CBO, nomenclatura padrão, 1 criativo por anúncio, checar gasto × orçamento. |
| Fiscal | ROAS de equilíbrio pelo valor real do pedido (produto + bump + upsell − taxa Hubla); verba só sobe com o número no verde. |
| Creative Analyst | Julgar por conceito/padrão (gancho, formato), detectar cansaço (frequência↑, CTR↓). |
| Hormozi Ads | Anúncio é o 4º canal; oferta boa paga o anúncio. Low ticket existe para **liquidar o CPA** com bump/upsell. Mata perdedor rápido, escala vencedor. |
| Hormozi Offers | Equação de valor: "15 minutos, com o celular na mão" reduz tempo e esforço; garantia de 7 dias aumenta a chance percebida. |
| Donald Miller | Cliente é o herói: anúncio fala da dor (perfil não faz chamar) e do plano simples (5 partes, 15 min), Lindson é o guia. |

## 2. Premissas típicas que a v1 pode ter errado (a extensão confere)
1. Objetivo Tráfego/Engajamento em vez de **Vendas** → corrigir para Vendas, otimizando **Compra** (Purchase).
2. Pixel sem API de Conversões ou evento errado (InitiateCheckout como meta) → Purchase com valor.
3. Vários conjuntos com interesses empilhados, cada um com verba pequena → **1 campanha, 1 conjunto amplo** (Andromeda).
4. Poucos criativos ou todos variações da mesma peça → **8 a 15 conceitos diferentes**.
5. Edições diárias (verba, criativo) que reiniciam o aprendizado → mudanças em lote, no máximo a cada 3–4 dias.
6. Bio vendida sozinha sem bump/upsell → ligar o funil da ESCADA (bump Pack de capas; upsell Raio-X; downsell Kit/Pack).
7. Página do anúncio ≠ página de venda/checkout com a mesma promessa.

## 3. Conta do equilíbrio (Fiscal + Hormozi)
- **Valor médio do pedido (VMP)** = preço Bio + (preço Pack × % que leva o bump) + (preço Raio-X × % upsell).
- **Margem por pedido** = VMP − taxa Hubla.
- **CPA máximo** = margem por pedido. **ROAS de equilíbrio** = VMP ÷ margem.
- Regra: se o CPA real passar do máximo por 7 dias com ≥ 1.000 impressões por criativo vencedor, o problema é oferta/página, não verba.

## 4. Estrutura v2 (Andromeda)
- **1 campanha** `LT · Vendas · Bio que Vende` · objetivo Vendas · meta Compra · CBO · Advantage+ (campanha de vendas Advantage+ se a conta permitir).
- **1 conjunto** `Brasil · Amplo · 22-55` · Advantage+ público, sem interesses empilhados (sugestão opcional: empreendedorismo, pequenos negócios, Instagram para negócios) · posicionamentos Advantage+ · Brasil.
- **Verba:** a que o Lindson aprovar. Referência para sair do aprendizado: ~50 compras/semana; com low ticket e verba baixa isso não acontece. Por isso: não fragmentar; se em 7 dias tiver < 10 compras, trocar a otimização para **Início de finalização** (InitiateCheckout) temporariamente, sem criar outro conjunto, e voltar a Compra quando tiver volume.
- **Remarketing:** não separado; o Advantage+ já entrega para quem visitou. Abandono de carrinho é tratado pela Hubla (ESCADA: 1 h e 24 h).

## 5. Criativos: 8 a 15 conceitos realmente diferentes
Reels com áudio (voz do Lindson ou Reels dele já publicados), sem preço no criativo, sem promessa de resultado.
| # | Ângulo | Formato | Gancho (3 s) |
|---|---|---|---|
| 1 | Dor | Lindson falando | "Sua bio está espantando cliente." |
| 2 | Teste dos 5 segundos | Tela do celular | "Abre seu perfil. Conta 5 segundos." |
| 3 | Antes × depois | Tela dividida | Bio ruim × bio refeita |
| 4 | Objeção tempo | Texto na tela + cronômetro | "15 minutos. Com o celular na mão." |
| 5 | Persona salão/estética | Reels com cena de negócio | "Quem faz unha não pode ter bio assim." |
| 6 | Persona prestador de serviço | Cena de trabalho | "Você é bom no que faz. A bio não mostra." |
| 7 | Persona loja/varejo | Produto + perfil | "O cliente olha a bio antes de chamar." |
| 8 | Prova do método | Carrossel das 5 partes | "A bio que vende tem 5 partes." |
| 9 | Erro comum | Estático manchete | "3 erros na bio que fazem ninguém chamar." |
| 10 | Destaques e fixados | Tela do celular | "Seus destaques dizem o que você vende?" |
| 11 | Garantia | Lindson falando | "Se não servir, devolvo. 7 dias." |
| 12 | Curiosidade | Texto na tela | "Por que perfil bonito não vende." |
Copy: estrutura do PADRAO-COPY (Conexão → Dor → Desejo → Pergunta), chamada "Quero minha bio nova".

## 6. Rotina de otimização
- **Dia 3:** só checar se gasta e se o pixel registra Purchase. Não mexer. Desligar criativo com erro/reprovado.
- **Dia 7:** desligar conceitos com gasto ≥ 2× CPA máximo e 0 compra, ou CTR de link muito abaixo da média da conta. Manter os que geram compra. Anotar padrões vencedores (ângulo/formato).
- **Dia 14:** lote de 3–5 conceitos novos inspirados nos vencedores (de uma vez). Verba só sobe (até 20% a cada 3–4 dias) se CPA ≤ máximo por 7 dias — decisão do Lindson.
- Sempre: desligar, nunca excluir; não editar no mesmo dia vários itens.

## 7. O Lindson precisa informar
Preço da Bio (e do Pack/Raio-X), link do checkout Hubla, se o Pixel + API de Conversões estão ligados na Hubla, verba diária atual e qual conta de anúncios a extensão usa.
