# Auditoria de fidelidade dos prompts de dossiê

**Data:** 25/11/2026
**Referência obrigatória:** `PROMPT-DOSSIE-MODELO.md`

## Padrão que deve ser seguido sem alteração

Todo prompt novo deve ser uma adaptação literal do `PROMPT-DOSSIE-MODELO.md`, trocando somente os dados entre colchetes e adaptando os blocos específicos à pessoa e à cidade. O prompt completo deve conter:

1. Regra de pesquisa completa, sem entrega parcial.
2. Bloco `JÁ TEMOS`, baseado na base do SDR e no TSE.
3. Treze blocos numerados de `0)` a `12)`.
4. LACUNAS e FONTES com link e data.
5. Pesquisa de Instagram real com os 12 posts, métricas e cálculo de engajamento.
6. Passivos em Escavador/JusBrasil, TJ, TRE, TCE e MP, com fonte, lado e situação.
7. Concorrência e contexto eleitoral local.
8. Foto oficial em alta resolução.
9. Regra de três caminhos antes de declarar algo não encontrado.
10. Navegador logado para Instagram/Facebook e DivulgaCandContas.
11. Arquivos obrigatórios no ZIP: Markdown 0–12, fotos, prints, CSV e checklist.
12. Releitura final item por item antes da resposta.

## Resultado da comparação

### Prompts conformes ao modelo completo

- `PROMPT-DOSSIE-BERSON-DO-POSTO.md`
- `PROMPT-DOSSIE-EDIDACIO-LOPES.md`
- `PROMPT-DOSSIE-EDIR-SALES.md`
- `PROMPT-DOSSIE-FELIPE-ANDRADE.md`
- `PROMPT-DOSSIE-FERNANDINHO.md`
- `PROMPT-DOSSIE-FRANCISCO-DO-ROBERTAO.md`
- `PROMPT-DOSSIE-MARCOS-MOURA.md`
- `PROMPT-DOSSIE-OZIMA-CURY-RAD.md`
- `PROMPT-DOSSIE-RAIMUNDO-PENHA.md`
- `PROMPT-DOSSIE-RICARDO-SEIDEL-v2.md`
- `PROMPT-DOSSIE-THAUANA-PADILHA.md`

Esses prompts seguem a estrutura completa de 0–12, têm regra de pesquisa completa, checklist e instrução de três caminhos.

### Prompts antigos ou parciais, que NÃO devem ser usados como modelo

- `PROMPT-DOSSIE-ALCEMIR-COSTA.md`
- `PROMPT-DOSSIE-FABIANO-FUBA.md`
- `PROMPT-DOSSIE-FRANCISCO-MESSIAS.md`
- `PROMPT-DOSSIE-JARDEL-BARROSO.md`
- `PROMPT-DOSSIE-MESAAC-CIRQUEIRA.md`
- `PROMPT-DOSSIE-RAFAEL-CAPANER.md`
- `PROMPT-DOSSIE-RICARDO-SEIDEL.md`

Eles têm formato anterior, normalmente com 9 blocos, sem a estrutura integral 0–12, sem checklist final e sem todas as exigências de pesquisa do modelo atual.

### Prompts de complemento

- `PROMPT-DOSSIE-EDIDACIO-LOPES-COMPLEMENTO.md`
- `PROMPT-DOSSIE-RAIMUNDO-PENHA-COMPLEMENTO.md`

São válidos somente como complementos de uma pesquisa parcial já existente. Não substituem o prompt completo 0–12 e não devem ser usados isoladamente para iniciar uma nova pesquisa.

## Regra operacional definitiva

A partir desta auditoria, nenhum novo prompt deve ser criado a partir dos prompts antigos de 9 blocos. Para Mesaac Cirqueira, Jardel Barroso e Francisco do Robertão, se a pesquisa for refeita ou complementada, deve-se usar uma nova versão fiel ao modelo oficial completo, preservando o prompt antigo apenas como histórico.

Para Edir Sales, Felipe Andrade e Fernandinho, os prompts individuais atuais estão no padrão completo; antes de gerar PDF, é obrigatório confirmar que a pesquisa/ZIP chegou com todos os arquivos exigidos e checklist preenchido.

A fidelidade deve ser verificada em duas camadas:

- **Prompt:** estrutura 0–12 + LACUNAS + FONTES + arquivos + checklist.
- **Entrega:** Markdown, fotos públicas creditadas, prints, CSV dos 12 posts, PDF de 26 páginas 16:9 e conferência visual antes da entrega.
