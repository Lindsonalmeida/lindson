# Kit de rede social v4 · @oreganoturbo (conta Zuleide, 08/11/2026)

**Pedido do Lindson (08/11):** "pegue a v3 e melhore com a pesquisa que o Claude fez no Google e no Pinterest".
- **Base:** kit v3 aprovado ("ESSE É O PADRÃO", `../v3/`).
- **Pesquisa:** `../../biblioteca-pizzaria/PESQUISA-08-11-IDENTIDADES-E-SOCIAL.md`.
- **Situação:** aguardando aprovação.

**Prévia:** `previa-feed.jpg`. **Peças:** `pecas/` (9 posts e 3 stories).

## O que mudou em relação à v3 (cada item vem da pesquisa)
| Lição da pesquisa | Aplicação na v4 |
|---|---|
| Campanha com um conceito só (Impasto) | Toda peça leva a **comanda "PEDIDO Nº01…12"**. O feed vira uma sequência de pedidos da Orégano Turbo. |
| 2 ou 3 cores e uma fonte, sempre | A paleta ficou fixa em tomate, verde, creme e carvão (açafrão só em detalhe). Saíram o céu azul, o amarelo-ouro e a grade de 4 cores. **Bagel Fat One** em todas as manchetes. |
| Padrão a evitar: fundo vermelho + pizza recortada + preço em selo | O Raio-X (p05 e story 2) virou um **cartaz escuro**, com o preço escrito na comanda e sem a explosão. |
| A foto vem primeiro; texto só em área livre | Nenhum texto cobre a pizza. A grade p03, que tinha texto por cima da pizza, saiu. |
| Pinterest nº1: PIZZA gigante atrás, mão por cima, fundo verde | p01 sobre verde, com "fome." passando por trás do rosto |
| Pinterest nº3: texto enorme, pizza cortada na borda | p02 (TERÇA) e p05 (pizza saindo pela borda) |
| Pinterest nº4: nome girando em volta da pizza, "PIZZA" vazado | p03 nova: anel "SÓ PIZZARIAS" em volta da pizza |
| Pinterest nº9: fundo preto, lettering amarelo e branco | p05, p08 e story 2 |

## Regras
- Mesmas fotos e recortes da v3 (`../v3/recortes`): a v4 **substitui** a v3, não é uso novo.
- Sem promessa de resultado.
- Preços só os aprovados: Raio-X R$ 297, abatido se fechar em 7 dias; 5 vagas de fundadora.
- "Imagem gerada por IA" em todas as peças; a conversa do story 3 é marcada como "exemplo ilustrativo".

## Como refazer
`python3 gerar.py && node render.js && python3 previa.py`
