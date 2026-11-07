# Curso de processo legislativo · identidade v2 "Sinal" (pesquisa premium nova)
Conta Leandro, 07/11/2026 · pedido do Lindson: **"quero uma identidade mais impactante e atual. não pode parecer amador e antigo."** · status: **aguardando aprovação do Lindson**

**Direção A "Ata" (serifa, papel marfim) foi reprovada** pelo Lindson e não volta. Não usar serifa de documento antigo nem fundo bege no curso.

Persona: a mesma de `TEMPLATE.md` (vereador, assessor e servidor de câmara do Maranhão). Ela lê no celular, e um visual antigo lhe passa a ideia de "instituição velha", de que o curso também é antigo. Por isso o visual precisa de cara de agora.

## Referências desta rodada (país e ano confirmados na própria página)
| # | Referência | País e ano (na página) | Captura | Situação | O que se copia |
|---|---|---|---|---|---|
| 1 | **Public School 9 Brand Identity** (K-Design Award) | EUA · 2025 · WINNER | `referencias/13-public-school-9-us.png` | **Escolhida 1** | Sans bold como voz principal, com um deslocamento de cor e um efeito de "erro de impressão" usado com moderação. Copiado: sombra deslocada da capa 05 |
| 2 | **Soapbox · "A bold relaunch for a leading progressive magazine"** | estúdio em Sydney (página: sydney) · 2025 e 2026 | `referencias/15-progress-soapbox-au.png` | **Escolhida 2** | Hero escuro com grotesca grande, de frase em bloco, sem decoração. Copiado nas capas 01 e 04. **Atenção:** a página mostra o estúdio em Sydney, não o país da revista |
| 3 | **The Nation redesenhado por Athletics** (GDUSA) | EUA (página: "USA") · 2025 e 2026 | `referencias/14-the-nation-us.png` | **Escolhida 3** | Cabeçalho grande com uma cor de marca forte, usada como reconhecimento. Copiado: o dourado como cor de marca. **Atenção:** a página é de notícia, lida pela captura |
| 4 | Fiasco Design · identidade da Bayswater (educação) | Reino Unido (página: london) · 2024 a 2026 | `referencias/12-fiasco-bayswater-uk.png` | Descartada | Visual não analisado nesta rodada; fica para uma próxima pesquisa |
| 5 | Pentagram · identidade do Camden Art Centre | Reino Unido (página: london) · 2025 | `referencias/16-pentagram-camden-uk.png` | Descartada | Identidade cultural, mais serifa e patrimônio. Pouco impacto para Reels |
| 6 | Obama Foundation · fonte nova | Não confirmado na página | (sem captura) | Descartada | O país não aparece na página |
| 7 | Pentagram · Galvan, MIT Technology Review, Renaissance | Só a lista de escritórios aparece | `referencias/05-galvan-pentagram.png` | Descartadas | A página mostra os escritórios, não o país do projeto |

Referências da v1 (GOV.UK, Montague, D&AD, CQUniversity, Rheinische, JKR e outras) ficam em `TEMPLATE.md`. Não entram na v2: a v1 foi reprovada.

**Países confirmados nesta rodada: EUA, Reino Unido e Austrália (estúdio). Três referências atuais escolhidas.**

## Escolhida final (combinação)
- Sans bold em caixa alta, com entrelinha curta (PS9 + Soapbox).
- Cor única de destaque, dourado `#C8B078` (tom medido no cartaz do curso), sobre verde-garrafa `#00241C`. A cor de marca do Nation virou o dourado do curso.
- Rótulo em mono (JetBrains Mono) e moldura de série "Nº 01/09".

## Descartadas, com motivo
- Serifa e papel bege: parecem documento antigo (reprovado).
- Azul royal com amarelo: é a identidade do Tribuna 98, proibida para o curso.
- Ícones de linha e ilustração de Congresso: cara de cartilha.

## Como ficou nas peças (`capas-v2/`)
| Capa | Composição | Referência |
|---|---|---|
| 01 urgência | cor cheia, título em sinal | Soapbox |
| 02 pode votar | "?" gigante (número de fundo) | The Nation |
| 03 tramitar | problema × solução | PS9 |
| 04 devido processo | palavra gigante | Soapbox |
| 05 sessão secreta | cartão com sombra deslocada | PS9 |
| 06 princípio | faixas | Soapbox |
| 07 medida provisória | anel com "MP" | The Nation |
| 08 quórum | frase de impacto | Soapbox |
| 09 quem propõe | "PL" gigante | The Nation |

Títulos continuam propostas: confirmar com a estrutura do curso antes de publicar.

## Board de referência do Lindson (Pinterest · "CURSOS", pedido de 07/11)
Link: https://br.pinterest.com/lindsonalmeidaa/cursos/ · 34 pins no total; 12 carregaram para análise (o restante exige login, e o board pede conta).
**Veredito:** o board é de templates de mercado (artes de matrícula e de cursos com preço), **não é pesquisa premium**. Os pins não trazem estúdio, país nem prêmio confirmados, então **não contam** nas 8 referências.
**O que ensina e entra na v3:** quase todos os pins põem uma **pessoa real recortada** ocupando boa parte do quadro, com **título gigante e pesado** sobre uma **faixa de cor**, mais um **selo (pill)** com a informação principal e ícones em lista.
**Por que ficou fraco na v2:** as capas v2 são só tipografia, sem nenhuma pessoa. O Lindson sentiu falta disso, e a crítica está certa.
**Consequência:** a v3 precisa da foto do instrutor (recorte). Sem a foto, não há como chegar nesse padrão sem ilustração no lugar de pessoa real, o que é proibido.
**Modelo:** `capas-v2/modelo-v3-com-foto.png` (gerador `gerar-v3-modelo.js`). O quadro tracejado é o espaço reservado para o recorte do instrutor.
Pendência: as fotos dos dois instrutores, uma por mensagem, e o recorte com fundo transparente.

**Atualização (07/11):** o Lindson mandou capturas do board completo, já logado (cerca de 40 peças). Mesmo veredito: são templates de mercado, com preço e matrícula, sem autoria, país ou prêmio confirmados, então não contam como pesquisa premium. O padrão se repete: pessoa real recortada, título gigante e faixa de cor. Mais limpas e úteis como composição: "inglês" (letras empilhadas com recorte) e "Digital marketing" (pessoas recortadas sobre fundo verde). Próximo passo para a pesquisa premium: referências de estúdios com autoria e país na própria página, como o Behance e o Dribbble, com recorte de pessoa em educação ou serviço público.
