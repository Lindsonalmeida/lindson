# Tribuna 98 · site principal · persona e pesquisa (conta Leandro, 07/11/2026)

**Status: pesquisa premium INCOMPLETA. Site principal ainda NÃO construído. Nada entregue.**

## Persona (5 linhas)
- **Quem:** eleitor e cidadão do Maranhão (interior e São Luís) que acompanha política, prefeituras, licitações e eleições; também anunciantes locais e assessores de político.
- **Rotina:** celular no fim do dia e no WhatsApp; Instagram e Google para pesquisar um nome ou um caso.
- **Dor e desejo:** quer saber o que está acontecendo com o dinheiro público da sua cidade, sem ser enganado.
- **Confia em:** fonte citada, documento público, rosto e voz do Thiago, checagem de fatos, direito de resposta.
- **Afasta:** tom de panfleto, promessa de audiência, cara de blog genérico, número inventado.

## Pesquisa premium (estado real)
Meta: 8 referências confirmadas na própria página, de 3 países, 3 combinadas.

| Referência | Resultado |
|---|---|
| Exec Bio (Troy Miller, Framer), citada no TEMPLATE da bio | **Não confirmada**: a busca não encontrou o template com esse autor |
| Awwwards, news/media Site of the Day | **Não confirmada**: a busca só trouxe agências |
| Brand New / UnderConsideration (EUA), redesign de mídia | **Não confirmada**: não há caso de mídia; é a identidade da própria Brand New |
| Astral Media (Canadá) | **Descartada**: release de terceiros, não é trabalho premiado |

Faltou abrir as páginas (Awwwards, Behance, Framer bloqueados ou sem resultado nas rodadas anteriores). Próximo passo: o Lindson manda capturas ou o acesso é liberado, e a pesquisa é refeita com 8 páginas abertas.

## Decisões já tomadas pelo padrão (sem mudança)
- A bio JÁ EXISTE e está no ar em `tribuna98.pages.dev` (raiz, commit e0a6e01; `/bio` redireciona para a raiz). Recado do Lindson (07/11, via outra sessão): não refazer, não mover a bio, não mexer no link dela.
- O site principal é projeto novo, em rota própria (a definir com o Lindson), sem tocar a bio.
- O site novo fica AO LADO do WordPress (tribuna98.com.br). Premissa a confirmar.
- Cloudflare Pages, projeto `tribuna98`, branch `main`, framework None.

## Rodada de 07/11 (conta Leandro): site principal construído, aguardando aprovação
Rota (decisão do Lindson, 07/11): site principal na RAIZ `tribuna98.pages.dev/`, bio em `/bio/` (como a Real Time). Link do Instagram da bio precisa ser trocado pelo Lindson para `/bio/`. Branch `site-principal` do repo `Lindsonalmeida/tribuna98`, ainda sem publicar no `main`.

**Pesquisa confirmada (pela página da SND, `snd.org/snd-2026-worlds-best-designed/`, aberta e lida):**
| Referência | País | Reconhecimento | Página do site aberta? |
|---|---|---|---|
| The New York Times | EUA | World's Best-Designed Digital (SND47, 2026) | Não (403) |
| Weekendavisen | Dinamarca | World's Best-Designed Print (SND47) | Sim (aberta, com cookies) |
| De Volkskrant | Países Baixos | Finalista, "melhor tipografia" (SND47) | Sim |
| ProPublica | EUA | Finalista digital (SND47) | Sim |
| The Pudding | EUA | Finalista digital (SND47) | Sim (aberta, não usada) |
| The Washington Post | EUA | Finalista digital (SND47) | Não (tempo esgotado) |
| DIE ZEIT | Alemanha | Finalista impresso (SND47) | Não (bloqueio) |

**Faltou:** 8 referências (são 7 confirmadas). Awwwards e Behance não abriram nesta rodada.

**Combinadas (3):**
- **ProPublica** (EUA): manchete com foto ao lado e barra de temas no topo → hero e barra de editorias.
- **De Volkskrant** (Países Baixos): manchete em tipo forte, sóbria → títulos em Anton.
- **The New York Times** (EUA, só pelo texto da SND, página não aberta): mapas e dados de eleição → bloco de números e de "onde nos encontra". Esta é a menos conferida.

**Descartadas:** The Pudding (dados e gráficos interativos, não se encaixa no jornal de texto), Weekendavisen (impresso ilustrado, fora da fiscalização).

**Fotos:** nenhuma foto nova. A foto do Thiago já está usada na bio (03/11) e não se repete. Falta uma foto nova do Thiago, enviada uma por vez, para a capa do site.

## Publicado (07/11/2026, conta Leandro)
Versão 2 (camadas tecnológicas, três fotos do Thiago, nome corrigido para Tiago Azevedo) publicada no `main` do repositório `tribuna98` (commit 6ae31a9). Ajustes a pedido do Lindson.
