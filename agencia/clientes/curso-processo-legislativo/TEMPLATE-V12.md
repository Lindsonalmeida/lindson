# Template v12 · pesquisa premium para capas de Reels (curso de processo legislativo)
07/11/2026 · status: pesquisa concluída, aguardando aprovação do Lindson
Público e persona: ver `TEMPLATE.md` (vereadores, assessores e servidores de câmara). Capturas em `referencias-v12/`.

## Método e critérios
- Cada página foi aberta no Chrome (Playwright), lida em texto e capturada em `referencias-v12/`.
- **País:** lido no texto da página institucional do estúdio (contato ou sobre), porque a página de cada peça não traz o país. Quando o estúdio tem escritórios em vários países (Koto), o país aparece como "estúdio com escritórios em ...", e não como país de origem da peça.
- **Ano:** só conta o ano do projeto escrito na página (rótulo "ÁREA · ANO", título ou "©ANO"). Ano de prêmio, de lançamento de marca ou de outro evento não conta.
- Bloqueio: página que não abriu (403, conexão recusada, 404 ou "navegador não suportado") não entra na contagem.

## Candidatas com país e ano confirmados (11)

| # | Peça | Autor / estúdio | País (onde está na página) | Ano (onde está) | URL | Captura | Situação |
|---|---|---|---|---|---|---|---|
| 1 | The Norton Museum of Art, "Where Art Meets Life" (identidade) | Koto | Reino Unido, Alemanha e EUA (contato: London, Berlin, Culver City) | 2026 ("CULTURE · 2026") | https://koto.com/projects/the-norton-museum-of-art | `referencias-v12/koto-norton.png` | **Escolhida 1** |
| 2 | Scout Motors (case) | Locomotive | Canadá (rodapé: "Montréal (QC), Canada") | 2024 ("©2024") | https://locomotive.ca/en/work/scout-motors | `referencias-v12/loc-scout-motors.png` | **Escolhida 2** |
| 3 | "O ano esportivo 2023" (Strava, Year in Sport) | Hello Monday | Países Baixos (sobre: "Amsterdam Netherlands") | 2023 (título e texto) | https://hellomonday.com/work/strava-year-in-sport-2023 | `referencias-v12/hm-strava-2023.png` | **Escolhida 3** |
| 4 | Amazon, global brand transformation | Koto | Reino Unido, Alemanha e EUA (contato) | 2025 ("MARKETPLACES · 2025") | https://koto.com/projects/amazon | `referencias-v12/koto-amazon.png` | **Escolhida 4** |
| 5 | MTV VMAs 2022, campanha de movimento imersiva | Studio Dumbar | Países Baixos (contato: "Rotterdam ... The Netherlands") | 2022 (título) | https://www.studiodumbar.com/work/mtv-vmas-2022 | `referencias-v12/sd-mtv-vmas-2022.png` | **Escolhida 5** |
| 6 | Nubank, "Effortless banking, everywhere" | Koto | Reino Unido, Alemanha e EUA (contato) | 2026 ("BANKING · 2026") | https://koto.com/projects/nubank | `referencias-v12/koto-nubank.png` | Não escolhida (captura não revisada visualmente nesta rodada) |
| 7 | Adobe, "An Ethnographic Study of the Entrepreneurial Creator" | Koto | Reino Unido, Alemanha e EUA (contato) | 2026 ("SOFTWARE · 2026") | https://koto.com/projects/adobe | `referencias-v12/koto-adobe.png` | Não escolhida (captura não revisada visualmente nesta rodada) |
| 8 | Lyft, "Your Lyft is arriving" | Koto | Reino Unido, Alemanha e EUA (contato) | 2025 ("TRAVEL · 2025") | https://koto.com/projects/lyft | `referencias-v12/koto-lyft.png` | Não escolhida (captura não revisada visualmente nesta rodada) |
| 9 | Microsoft Copilot+PC | Koto | Reino Unido, Alemanha e EUA (contato) | 2024 ("TECH · 2024") | https://koto.com/projects/microsoft-copilot-pc | `referencias-v12/koto-copilot-pc.png` | Descartada (ver abaixo) |
| 10 | Tripadvisor, "Every type of traveler, every type of trip" | Koto | Reino Unido, Alemanha e EUA (contato) | 2025 ("TRAVEL · 2025") | https://koto.com/projects/tripadvisor | `referencias-v12/koto-tripadvisor.png` | Descartada (ver abaixo) |
| 11 | DEMO 2025 (Studio Dumbar) | Studio Dumbar | Países Baixos (contato) | 2025 (título) | https://www.studiodumbar.com/work/demo-2025 | `referencias-v12/sd-demo-2025.png` (a captura mostra o topo da página, não a peça) | Descartada (ver abaixo) |

Países confirmados nas candidatas: Países Baixos (3 estúdios de peça: Dumbar e Hello Monday), Canadá (Locomotive) e Reino Unido, Alemanha e EUA (Koto, estúdio com escritórios nesses três países). O critério de três países é cumprido, mas o da Koto é de estúdio com escritórios, não de origem única da peça.

## As 5 escolhidas e o que se extrai de cada uma

**1. Norton Museum of Art (Koto, 2026, UK/DE/EUA)**
- Grade: o nome ocupa a largura inteira no alto; o resto é foto de fundo e um rótulo pequeno.
- Hierarquia: marca gigante > imagem > linha de rótulo (categoria · ano).
- Foto: pintura real em tela cheia, escurecida para o texto ler.
- Cor: amarelo-dourado sobre marrom quase preto. Esta é a base do dourado e preto pedido.
- Tipografia: serifa de caixa alta, grande no topo, e linha de apoio em caixa alta espaçada.
- Para a capa do curso: nome do curso em serifa caixa alta gigante, subtítulo espaçado, fundo escuro com foto real. Não copiar a pintura nem o selo da marca.

**2. Scout Motors (Locomotive, 2024, Canadá)**
- Grade: título grande no terço de baixo à esquerda; foto numa caixa no canto inferior direito; metadados nos cantos.
- Hierarquia: título > foto > metadados.
- Foto: caixa de foto recortada com margem branca, sem sangria.
- Cor: branco e preto, sem acento colorido.
- Tipografia: serifa de alto contraste no título, sans pequena nos metadados.
- Para a capa do curso: serifa para o nome do curso, branco com preto, ano e tema em rodapé sans. É a peça mais "instituição séria" da lista.

**3. Strava, O ano esportivo 2023 (Hello Monday, 2023, Países Baixos)**
- Grade: título centralizado em duas linhas sobre foto em tela cheia.
- Hierarquia: palavra-chave > etiqueta com o ano > foto.
- Foto: P&B com trama de meio-tom (efeito impresso), que dá seriedade.
- Cor: preto, cinza e um acento laranja, só na etiqueta.
- Tipografia: sans em caixa alta no título; o ano dentro de faixa inclinada.
- Para a capa do curso: a faixa com o ano (ex.: "2026") como acento único, foto em P&B. Cuidado com a inclinação: usar só se o Lindson aprovar movimento na capa.

**4. Amazon, global brand transformation (Koto, 2025, UK/DE/EUA)**
- Grade: menu lateral numerado como trilho; área principal grande.
- Hierarquia: título > subtítulo > rótulo em caixa alta "MARKETPLACES · 2025".
- Foto: frame de vídeo real (caminhão), em área grande com legenda curta.
- Cor: fundo quase preto, texto branco e acento amarelo.
- Tipografia: sans condensada, com rótulo pequeno em caixa alta.
- Para a capa do curso: linha "rótulo · ano" logo abaixo do título, fundo preto e um só acento de cor.

**5. MTV VMAs 2022 (Studio Dumbar, 2022, Países Baixos)**
- Grade: planos em volume (prismas) que giram, cada um com um fragmento de foto recortado.
- Hierarquia: o movimento vem primeiro; o texto é mínimo.
- Foto: fragmentos de foto recortados em planos 3D.
- Cor: a original é amarelo chapado e fica de fora (muito alta para o público). Aproveitar só o recurso do recorte em volume, em preto e branco ou com dourado.
- Para a capa do curso: um recorte de foto em prisma, para dar profundidade a um Reels de movimento. Versão estática só se o Lindson aprovar.

## Descartadas e motivo
- **Microsoft Copilot+PC (Koto):** gradiente laranja desfocado, sem hierarquia de texto legível.
- **Tripadvisor (Koto):** verde chapado com logo no centro. Cor de marca forte demais, nenhum texto para hierarquia.
- **DEMO 2025 (Studio Dumbar):** a captura não mostra a peça (é o topo da página com a fachada), e a cor é amarela chapada. Não dá para avaliar a peça com a captura.
- **Nubank, Adobe e Lyft (Koto):** boas, mas não revisadas visualmente nesta rodada. Ficam de reserva.

## Fora por regra (não contadas)
- **Sem país na página do estúdio:** Made Thought (só "London" e "New York" como cidades), Pentagram (página Sobre lista Londres, Nova York, Austin e Berlim sem país), Collins, Bruce Mau (Toronto aparece só como cliente), Sagmeister & Walsh (país só em eventos), Nosigner (sem país no texto lido).
- **Estúdio errado:** Build Creative (Atlanta, estúdio de vídeo). Não é o Build de Londres.
- **Sem ano na página:** Bendy 10, Wongle, Bang & Olufsen, Dream With AI, Netflix Kids & Family (Hello Monday).
- **Ano que não é do projeto:** Residente (2018 é o ano do Grammy citado no texto); Driver (2017 é o ano do lançamento público da marca).
- **Texto ilegível na página:** Locomotive Lightship, Wolverine Worldwide e Dulcedo (capturas salvas; anos não contados).

## Bloqueadas (6 fontes, nenhuma candidata contada a partir delas)
- **Awwwards** (awwwards.com): conexão recusada pelo servidor.
- **Behance** (behance.net): 403/400 ao abrir.
- **Fiasco** (fiasco.co.uk): 403, verificação anti-bot da Cloudflare ("Just a moment").
- **Active Theory** (activetheory.net): página informa "Your browser is not supported".
- **Koto, koto.co.uk/work:** 404 nesta rodada (versão anterior do domínio).
- **Koto, koto.studio/work e home:** conexão recusada (o site atual está em koto.com, que abriu normalmente).

Não abertos nesta rodada: Dribbble, o site da D&AD e as páginas individuais de projeto da Pentagram.

## Próximo passo
Aprovar as 5 escolhidas (Norton, Scout Motors, Strava 2023, Amazon, MTV VMAs 2022) ou pedir mais uma rodada com Nubank, Adobe e Lyft revisadas visualmente.
