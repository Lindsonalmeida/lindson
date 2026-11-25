# Auditoria SDR × prompts × PDFs

**Data da conferência:** 25/11/2026 15:13 (sessão autenticada do administrador)
**Fonte operacional:** Central do Cliente → Central do Administrador → aba SDR (`/painel/admin#sdr`)

## Retrato ao vivo do SDR

A aba SDR exibiu **393 leads no nicho Vereadores**, distribuídos entre 4 SDRs. Naquele momento, o painel indicava:

- 278 na lista;
- 115 enviados;
- 26 respostas;
- 1 reunião;
- 0 fechados;
- taxa de resposta exibida: 23%.

A lista ao vivo contém muito mais vereadores do que os prompts e materiais atualmente arquivados no GitHub. Portanto, a auditoria anterior baseada somente nos repositórios não representava todos os leads do SDR.

## Prompts encontrados sem PDF correspondente

| Lead no SDR | Status ao vivo | Prompt | Pesquisa/material | PDF final localizado |
|---|---|---|---|---|
| **Edir Sales** | Qualificado · SDR 2 | `PROMPT-DOSSIE-EDIR-SALES.md` | Não localizado | **Não** |
| **Felipe Andrade** | Enviado · SDR 3 | `PROMPT-DOSSIE-FELIPE-ANDRADE.md` | Não localizado | **Não** |
| **Fernandinho** | Respondeu · SDR 2 | `PROMPT-DOSSIE-FERNANDINHO.md` | Não localizado | **Não** |
| **Jardel Barroso** | Perdido · SDR 1 | `PROMPT-DOSSIE-JARDEL-BARROSO.md` | `jardel-barroso/material/dossie/` | **Não** |
| **Mesaac Cirqueira** | Qualificado · SDR 1 | `PROMPT-DOSSIE-MESAAC-CIRQUEIRA.md` | `mesaac-cirqueira/material/dossie/` | **Não** |
| **Francisco do Robertão** | Qualificado · SDR 1 | `PROMPT-DOSSIE-FRANCISCO-DO-ROBERTAO.md` | `francisco-do-robertao/material/` | **Não localizado fisicamente** |

### Observação sobre Francisco do Robertão

O README da pasta de Francisco do Robertão afirma que existiria um PDF v1, mas a conferência física da árvore do repositório não encontrou o arquivo PDF. O caso deve ser tratado como **PDF ausente ou perdido**, não como entrega confirmada.

## Prompts com PDF localizado

Alcemir Costa, Berson do Posto, Edidacio Lopes, Prof. Fabiano Fubá, Francisco Messias, Marcos Moura, Ozima Cury Rad, Rafael Campaner, Raimundo Penha, Ricardo Seidel e Thauana Padilha possuem PDF localizado no CentralLindsonALmeida. Thauana possui a v2 final reconstruída sobre o template técnico do Alcemir.

## Leads ao vivo que não possuem prompt individual no repositório

A aba SDR também mostra centenas de outros vereadores para os quais não foi localizado um `PROMPT-DOSSIE-<NOME>.md` individual. Eles não devem ser tratados como pesquisa pronta nem como dossiê pendente até que o prompt seja criado e a pesquisa seja executada.

## Conclusão operacional

A lista prioritária de dossiês com prompt criado e PDF ausente é:

1. Mesaac Cirqueira — pesquisa já disponível;
2. Jardel Barroso — pesquisa já disponível, embora o lead esteja marcado como perdido;
3. Francisco do Robertão — pesquisa já disponível; recuperar ou regenerar PDF;
4. Edir Sales — prompt criado, pesquisa ainda não localizada;
5. Felipe Andrade — prompt criado, pesquisa ainda não localizada;
6. Fernandinho — prompt criado, pesquisa ainda não localizada.

Não gerar PDF para os três últimos antes de confirmar que a extensão executou os prompts e produziu a pesquisa completa.
