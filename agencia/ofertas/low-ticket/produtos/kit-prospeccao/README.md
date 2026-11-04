# Kit Prospecção pelo WhatsApp · produto low ticket (nota 80)

Conteúdo, planilha e template: conta Zuleide (03/11/2026). PDF: conta Leandro (04/11/2026), na fila de PDFs que a conta Pedro continuava (Pedro parou no limite de uso).

## O que o comprador recebe (repositório PRIVADO `CentralLindsonALmeida/produtos/kit-prospeccao/entrega/`, cópia em `membros-arquivos/kit-prospeccao/`)
| Arquivo | O que é |
|---|---|
| `Kit-Prospeccao-pelo-WhatsApp.pdf` | 33 páginas 4:5 (leitura no celular): capa, sumário, o kit em números, o método Conexão → Dor → Desejo → Pergunta (com a anatomia de uma mensagem), os 2 filtros (WhatsApp de celular + Instagram ativo), a cadência de 4 toques em 5 dias, a rotina de 1 hora (manhã busca, tarde chama), como usar a planilha, os 10 nichos (2 páginas cada: buscas prontas + as 10 mensagens; aviso nos nichos de saúde), as 10 objeções e os cuidados |
| `Planilha-Cadencia-Kit-Prospeccao.xlsx` | planilha da Zuleide (Como usar, Cadência, Painel, Config, Mensagens, Nichos, Objeções) com link wa.me por fórmula |
| `100-Mensagens-Kit-Prospeccao.txt` | as 100 mensagens em texto, para copiar |

## Como gerar de novo
`cd produtos/kit-prospeccao/fonte` → `python3 dados.py` (confere as 100 mensagens: até 280 caracteres, sem "vi que", link ou preço) → `python3 gerar.py` (monta `kit.html` e copia a planilha e o .txt para `entrega/`) → `node gerar-pdf.js` (PDF em `../entrega/` e aviso se algum texto passar do rodapé). Depois copie o PDF para `membros-arquivos/kit-prospeccao/`.

## Visual
Template **The Product-Led Sales Playbook** (Pocus, mekkie, Dribbble), escolhido pela Zuleide (`TEMPLATE.md`), na marca v2 preto e amarelo: capa com "WHATSAPP" gigante e "100 MENSAGENS" vazado na base, sumário tipográfico pesado, página de números gigantes com "RESUMO" vazado, cartões de fase com seta (filtros e rotina), linha tracejada com círculos que crescem (cadência). Base de CSS e acabamento (grão, cantos de corte) dos kits da conta Pedro.

## Situação
- [x] Conteúdo, planilha e template (Zuleide) · [x] PDF (Leandro) · [x] arquivo na área de membros (`functions/_membros.js`)
- [ ] O Lindson aprovar · [ ] preço (o Lindson define) · [ ] página de venda (texto em `OFERTA.md`; a landing está com a conta Pedro)
