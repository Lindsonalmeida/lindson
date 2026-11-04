# Kit WhatsApp que Fecha · produto low ticket (nota 83)

Conteúdo e template: conta Zuleide (03/11/2026). PDF, atalhos e acabamento premium: conta Pedro (04/11/2026), continuando de onde a Zuleide parou.

## O que o comprador recebe (repositório PRIVADO `CentralLindsonALmeida/produtos/kit-whatsapp-que-fecha/entrega/`)
| Arquivo | O que é |
|---|---|
| `Kit-WhatsApp-que-Fecha.pdf` | 24 páginas 4:5 (leitura no celular): capa com o kit em pé, "para quem é", o script de 6 passos (1 página por passo: porquê, mensagem pronta, o que nunca mandar, a regra), 20 respostas para "quanto custa?" em 5 tipos de negócio, mensagens de recuperação (sumiu, vou pensar, tá caro, pós-venda, avaliação), etiquetas do WhatsApp Business e como cadastrar os atalhos |
| `atalhos.txt` e `atalhos.csv` | as 43 mensagens com o código do atalho (ex.: `/valor`) para colar nas respostas rápidas do WhatsApp Business |

## Como gerar de novo
`cd produtos/kit-whatsapp-que-fecha/fonte` → `python3 gerar.py` (lê `conteudo.py`, monta `kit.html` e os atalhos) → `node gerar-pdf.js` (PDF em `../entrega/` e aviso se algum texto passar do rodapé).

## Visual
Template **Freelancer Client-Winning AI Prompt Kit** (Fused4Design, Dribbble), ver `TEMPLATE.md`, na marca v2 preto e amarelo. Acabamento premium aprovado nas artes do Lindson: grão de filme, cantos de corte, pílula de vidro e palavra em itálico com luz dourada.

## Situação
- [x] Conteúdo e template (Zuleide) · [x] PDF e atalhos (Pedro)
- [ ] O Lindson aprovar · [ ] preço (o Lindson define) · [ ] página de venda (texto em `OFERTA.md`)
