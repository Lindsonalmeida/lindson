# Bio que Vende em 15 Minutos · produto low ticket (nota 85 · bump dos outros kits)

Template: conta Zuleide (03/11/2026). Conteúdo: Copy Squad (Copy Chief → Joe Sugarman e David Ogilvy, tom de Eugene Schwartz), PDF: conta Leandro (04/11/2026), na fila de PDFs que a conta Pedro continuava.

## O que o comprador recebe (PRIVADO `CentralLindsonALmeida/produtos/bio-que-vende/entrega/`, cópia em `membros-arquivos/bio-que-vende/`)
| Arquivo | O que é |
|---|---|
| `Pack-Capas-de-Destaque.zip` (o **bump**) | 36 capas de destaque 2160×3840 (12 temas × preto, amarelo e branco), só tipográficas, nas 4 composições do Almeria Haus (palavra + itálico, texto em arco, pílula, anel fino), com `EDITAR-capas.html` para trocar a palavra e um LEIA-ME. Fonte: `produtos/bio-que-vende/bump/` (`capas.html`, `gerar.js`) |
| `Bio-que-Vende-em-15-Minutos.pdf` | 30 páginas 4:5: capa, abertura, 6 capítulos (aberturas em página cheia amarela/preta), a fórmula em 5 partes, o caminho perfil → bio → link → WhatsApp, os 15 minutos em 5 etapas de 3 (etiqueta MIN, caixas "Lembre" e "Faça agora" com linha para preencher, exemplo), 8 antes × depois com o perfil desenhado no celular (negócios fictícios), o Teste dos 5 Segundos (10 itens), os 7 destaques, os 3 fixados, os 6 erros e 10 modelos para copiar |

## Como gerar de novo
`cd produtos/bio-que-vende/fonte` → `python3 conteudo.py` (confere: bios até 150 caracteres, palavras proibidas) → `python3 gerar.py` → `node gerar-pdf.js` (PDF em `../entrega/` e aviso se algum texto passar do rodapé). Depois copie o PDF para `membros-arquivos/bio-que-vende/`.

## Visual
**COURAGE · Modern Editorial Book Design** (NIVORA, Dribbble) + **book interior layout** (NIVORA) para as páginas de exercício, escolhidos pela Zuleide (`TEMPLATE.md`), na marca v2 preto e amarelo: manchete Anton em 4 linhas, aspas grandes, régua curta, capitular serifada, faixa amarela na lombada nas listas, círculo amarelo atrás do celular no antes × depois.

## Situação
- [x] Template (Zuleide) · [x] conteúdo (Copy Squad) · [x] PDF (Leandro) · [x] arquivo na área de membros (`functions/_membros.js`, testes 45/45)
- [ ] O Lindson aprovar · [ ] preço (faixa sugerida R$ 17 a 27, decisão dele) · [x] Pack de capas de destaque (bump, conta Leandro) · [ ] o Lindson criar o produto do bump na Hubla (preço abaixo da Bio) · [ ] página de venda (com a conta Pedro)
