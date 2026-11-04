# Kit Mês Pronto · produto low ticket nº 1 do ranking (nota 88)

Conteúdo e template: conta Zuleide (03/11/2026). PDF montado: conta Pedro (04/11/2026), continuando de onde a Zuleide parou.

## O que o comprador recebe
| Arquivo | O que é | Onde está (repositório PRIVADO `CentralLindsonALmeida`) |
|---|---|---|
| `Kit-Mes-Pronto.pdf` | 52 páginas A4 deitado: capa, sumário + "como usar em 1 hora por semana", 30 roteiros (1 por página: gancho, texto na tela, falas, chamada, como gravar, exemplo), banco de 50 ganchos em 7 tipos, calendário de 30 dias (3 páginas), 10 modelos de legenda SEO com exemplo e contracapa com o convite para gravar com o Lindson | `produtos/kit-mes-pronto/entrega/` |
| `calendario-30-dias.xlsx` e `.csv` | o mesmo calendário em planilha, com colunas para data, gravado, postado e quantas pessoas chamaram no WhatsApp | `produtos/kit-mes-pronto/entrega/` |

Os colchetes `[SERVIÇO]`, `[BAIRRO]` etc. ficam destacados em amarelo no PDF para o comprador ver o que trocar.

## Como gerar de novo
No privado: `cd produtos/kit-mes-pronto/fonte` → `python3 kit.py` (monta `kit.html` com `roteiros.py`, `extras.py`, `calendario.py` e `kit.css`) → `node gerar-pdf.js` (gera o PDF em `../entrega/` e avisa se algum texto passou do rodapé). Planilha: `python3 calendario.py ../entrega`.

## Visual
Template **HUGE · Social Media Manager's Kit** (ArtisanaAura, Dribbble) na marca v2 preto e amarelo do Lindson: ver `TEMPLATE.md`. Páginas alternam off-white e preto, aberturas de seção em amarelo, 1ª letra do título em itálico de serifa, rodapé técnico em mono.

## Situação
- [x] Conteúdo (Zuleide) · [x] template (Zuleide) · [x] PDF e planilha (Pedro)
- [ ] O Lindson aprovar o PDF · [ ] definir o preço (faixa sugerida pelo Hormozi Squad: R$ 67 a 97, `../../hormozi.md`) · [ ] página de venda e checkout (texto em `OFERTA.md`)
