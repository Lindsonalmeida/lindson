# Capa 12 (Paulo) · 3 opções (10/11/2026, conta Zuleide)

Retorno do Lindson sobre a v3: "as duas ficaram ótimas, só o perseguidor que não". **10 e 11 APROVADAS** (padrão de capa de longo do Passaporte, ver MEMORIA). A 12 "PERSEGUIDOR" foi reprovada (palavra longa, rosto macio, cena escura) e está em `v3-reprovada/`.

- Base nova: **Caravaggio, "Conversão de São Paulo"** (1600-01, Santa Maria del Popolo, Roma), domínio público, Wikimedia Commons, 1920 px (`fontes/caravaggio-conversao-de-sao-paulo-commons-1920.jpg`). Rosto grande, luz forte, manto vermelho.
- Recorte `fontes/recorte-saulo-caravaggio.png`: BiRefNet portrait + chave de luz no braço direito, ficando só o maior pedaço, com os restos do cavalo apagados.
- Gerador `motor/capa12_opcoes.py` → `capa-12a.jpg`, `capa-12b.jpg`, `capa-12c.jpg`. Prévia `motor/previa_capa12.py` → `previa-capa12-opcoes.jpg` (ao lado das 10 e 11 aprovadas, com teste a 160 px).

| Opção | Palavra | Copia | Como ficou |
|---|---|---|---|
| A | **CEGO?** | Epic History "MUTINY" | fundo azul vivo com nuvens e feixe de luz, Saulo caído com os braços erguidos na frente da palavra, selo do canal |
| B | **ELE CAIU** | Ciência Todo Dia "FLOW" | close no rosto de Saulo de olhos fechados, fundo laranja e vermelho saturado, palavra com brilho por cima |
| C | **MUDOU** | Johnny Harris | céu aberto de fim de tarde e horizonte limpo, Saulo à direita contra o sol, palavra à esquerda |

**Status: aguardando o Lindson escolher A, B ou C** (a escolhida vira `capa-12.jpg`).

---

# Capas dos longos 10 a 12 · v3 "jovem" (10/11/2026, conta Zuleide, designer gráfico)

Pedido do Lindson ao ver a v2: "na verdade eu gosto desse estilo (as 3 referências), copie para fazer as nossas assim, mais jovens".
A v3 copia de perto a linguagem das 3 referências escolhidas na v2: cor viva e saturada, contraste alto, 1 palavra gigante, cara de YouTube 2025.
A v2 (close sépia) ficou guardada em `v2/`.

- Gerador: `motor/capas_jovem.py` → `capa-10.jpg`, `capa-11.jpg`, `capa-12.jpg`. Prévia: `motor/previa_jovem.py` → `previa-v3.jpg` (cada capa ao lado da referência e o teste a 160 px).
- Recortes em `fontes/`: as gravuras foram ampliadas 2x (Real-ESRGAN, `ferramentas/melhorar_foto.py`), recortadas (BiRefNet portrait) e colorizadas com cor de cinema saturada.
- **Status: aguardando o OK do Lindson.**

| Capa | Referência copiada | Como ficou | Palavra |
|---|---|---|---|
| **10** Milagres | **Epic History "MUTINY"** (Reino Unido) | céu azul vivo com nuvens, palavra branca gigante de ponta a ponta no alto, Jesus (Doré 080) recortado e colorido (vermelho-terracota e creme) com o braço erguido na frente da palavra, selo do canal no canto (azul-noite) | **MILAGRE?** |
| **11** Êxodo | **Ciência Todo Dia "FLOW"** (Brasil) | close extremo no rosto de Moisés com os raios (Doré, Sinai, 1920 px), cor quente saturada, palavra branca gigante atravessando com brilho dourado e sombra | **VOLTAR?** |
| **12** Paulo | **Johnny Harris** (EUA) | fim de tarde, céu aberto e horizonte limpo à esquerda, sol baixo; Saulo (Doré 095) em meio corpo à direita, cobrindo os olhos contra a luz (a caminho de Damasco) | **PERSEGUIDOR** (a única em amarelo) |

Identidade mínima mantida: "PASSAPORTE DA BÍBLIA" pequeno (selo ou Special Elite) e a etiqueta ciano da série.

## Conferência
- A 160 px as 3 palavras leem (prévia).
- Limite: o rosto de Jesus (capa 10) e o de Saulo (capa 12) são pequenos na gravura original (cerca de 770 px); mesmo ampliados, ficam macios de perto. Se o Lindson quiser rosto mais nítido, o caminho é a gravura em alta do Wikimedia Commons (como o Moisés da capa 11).

---

# Capas dos longos 10 a 12 · v2 (09/11/2026, conta Zuleide, designer gráfico)

Refação pedida pelo Lindson: a v1 ("Pintura anotada", mais abaixo) foi **reprovada** por 4 falhas: capturas não salvas, imagem escura e cheia de detalhe com personagem pequeno, nenhum rosto ou gesto em close, pouco contraste entre assunto e fundo.

- Gerador: `motor/capas_v3.py` → `capa-10.jpg`, `capa-11.jpg`, `capa-12.jpg` (1280×720). Prévia: `motor/previa_v3.py` → `previa-v2.jpg` (as 3 capas, as 3 referências e a busca do YouTube a 320 px e a 160 px).
- Capturas reais em `referencias/` (16 arquivos + a folha `00-folha-50-miniaturas-coletadas.jpg` com as 50 miniaturas baixadas de `i.ytimg.com`; IDs em `ids-youtube.txt`). Behance e Dribbble capturados pelo Playwright em 09/11.
- **Status: aguardando aprovação do Lindson.**

## Persona (5 linhas)
1. Cristão brasileiro, católico ou evangélico, 25 a 60 anos, que quer entender a Bíblia e trava na leitura.
2. Vê YouTube no celular, à noite ou no intervalo, rolando a lista; decide em menos de 1 segundo, com a miniatura do tamanho de um polegar (160 px).
3. Dor: "leio e não entendo"; desconfia de capa sensacionalista, de "IA" ou de grito.
4. Para a rolagem quando vê um rosto ou gesto forte, uma luz dramática e uma pergunta curta que mexe com o que ele acha que já sabe.
5. Confia em arte clássica (Doré) e tom sério; clicaria numa cena bíblica grande e clara, com uma pergunta de 2 palavras.

## Pesquisa (16 capturas, 8 países)
Miniaturas oficiais baixadas de `i.ytimg.com/vi/<id>/maxresdefault.jpg` (vídeos recentes de cada canal, IDs em `referencias/ids-youtube.txt`). Número de visualizações não conferido.

| # | Arquivo | Canal / designer | País | O que tem | Situação |
|---|---|---|---|---|---|
| 1 | `02-epic-history-mutiny-UK.jpg` | Epic History | Reino Unido | 1 palavra gigante no alto; o personagem fica na frente da palavra | **ESCOLHIDA → capa 10** |
| 2 | `01-ciencia-todo-dia-flow-BR.jpg` | Ciência Todo Dia | Brasil | close extremo (olho), 1 ponto de foco, palavra gigante cruzando a imagem | **ESCOLHIDA → capa 11** |
| 3 | `03-johnny-harris-close-US.jpg` | Johnny Harris | EUA | rosto em close de um lado, luz quente, fundo sem detalhe, espaço livre para o texto | **ESCOLHIDA → capa 12** |
| 4 | `04-veritasium-luz-unica-AU.jpg` | Veritasium | Austrália/EUA | fundo preto, uma luz só | descartada: sem texto, depende de objeto aceso; ficou a ideia do fundo escuro |
| 5 | `05-epic-history-waterloo-UK.jpg` | Epic History | Reino Unido | retrato à direita + palavra gigante | descartada: o mapa no meio é poluído |
| 6 | `06-terra-x-zu-reich-DE.jpg` | Terra X History (ZDF) | Alemanha | ilustração com luz dourada, 2 palavras | descartada: ilustração digital, fora da gravura |
| 7 | `07-historia-meia-hora-BR.jpg` | História em Meia Hora | Brasil | rosto do apresentador + texto de 2 linhas | descartada: depende de apresentador (canal dark) e tem texto demais |
| 8 | `08-nota-bene-FR.jpg` | Nota Bene | França | apresentador em cena escura | descartada: depende de rosto do apresentador |
| 9 | `09-fall-of-civilizations-UK.jpg` | Fall of Civilizations | Reino Unido | paisagem + título fino | descartada: sem foco e ilegível a 160 px |
| 10 | `10-kings-and-generals.jpg` | Kings and Generals | EUA/Ucrânia (não conferido) | foto de guerra + título em faixa | descartada: muito detalhe |
| 11 | `11-academia-play-ES.jpg` | Academia Play | Espanha | cartum colorido com mão desenhando | descartada: estilo cartum |
| 12 | `12-bibleproject-US.jpg` | BibleProject | EUA | paisagem com título fino | descartada: pouco contraste |
| 13 | `13-oversimplified.jpg` | OverSimplified | Canadá (não conferido) | cartum | descartada: estilo cartum |
| 14 | `14-behance-busca-documentary.jpg` | Behance, busca "youtube thumbnail documentary" | vários | grades de capas de documentário | descartadas: colagens com muito texto |
| 15 | `15-behance-busca-bible-egor-goncharov.jpg` | Behance, Egor Goncharov e Maya Blizniuk | não conferido | rostos em close, teal e laranja de cinema | apoio: confirma o close com cor de cinema |
| 16 | `16-dribbble-busca-cinematic.jpg` | Dribbble, busca "youtube thumbnail cinematic" | vários | capas de cinema | descartadas: genéricas |

## O que cada capa copia
| Capa | Gravura e cena | Referência copiada | Texto |
|---|---|---|---|
| **10** Milagres | Doré 080, a ressurreição de Lázaro: Jesus de braço erguido em close (cerca de 55% da altura) | **Epic History "MUTINY":** palavra gigante no alto e a cabeça do personagem passando na frente dela (recorte pelo mapa de profundidade `dore/prof/080.png`; o braço não cobre a letra, para ler "SHOW?" a 160 px) | NÃO ERA **SHOW?** |
| **11** Êxodo | Doré, Moisés desce do Sinai com as tábuas (Bíblia inglesa de 1866, domínio público, Wikimedia Commons, 1920 px, em `fontes/`): rosto, raios e mão erguida em close | **Ciência Todo Dia "FLOW":** um só personagem em close, luz num ponto, frase gigante de lado a lado | QUIS **VOLTAR?** |
| **12** Paulo | Doré 095, a conversão: Saulo cobrindo o rosto diante da luz, em close à direita | **Johnny Harris:** personagem de um lado, luz quente nele, fundo afundado no escuro, texto empilhado no espaço livre | ELE **PERSEGUIA** |

Em todas: a cor de cinema do `capas2.py` (sombra petróleo, luz âmbar) com mais contraste, um único brilho atrás do foco, vinheta forte e fundo desfocado longe do foco. Mantidos da identidade: "PASSAPORTE DA BÍBLIA" em Special Elite, a etiqueta ciano da série e a palavra-chave em amarelo (Anton com contorno preto). Nada de vermelho.

## Conferência
- Persona: cena grande, gesto claro e pergunta de 2 a 3 palavras; tom sério, sem grito.
- A 160 px (prévia, lista do celular) as 3 frases leem; "SHOW?" só passou depois de tirar o braço da frente da letra W.
- Gravuras: 080 e 095 já são do canal; Moisés do Sinai é gravura nova (não usada antes).
- Teste sugerido no YouTube: v2 contra a A aprovada do `capas2.py`, por 2 semanas, ganhando a de maior tempo de exibição.

---

# v1 (reprovada em 09/11/2026)

# Capas dos longos 10 a 12 · pesquisa premium e composição copiada

Pedido do Lindson (09/11/2026, conta Zuleide, Peter): "as novas capas, faça no estilo novo também, das nossas pesquisas de designer".
Exceção à regra "só `capas2.py`", **só para os longos 10 a 12**. As capas aprovadas do `capas2.py` (A, B e C) continuam como alternativa no teste A/B/C do YouTube ("Testar e comparar").

- Gerador novo: `motor/capas_estudo.py` → `capas/v2/<id>-N.jpg` (fora do Git) e a prévia `capas-longos-10-12/previa-capas-10-12.jpg` (à esquerda a nova, à direita a A aprovada).
- Gerador aprovado: `python3 motor/capas2.py longo-10 longo-11 longo-12` → `capas/v2/<id>-A/B/C.jpg`.
- **Status: aguardando aprovação do Lindson.**

## Persona (5 linhas)
1. Cristão brasileiro, católico ou evangélico, de 25 a 60 anos, que quer ler a Bíblia e trava.
2. Vê YouTube no celular, à noite ou no intervalo; decide o clique em menos de 1 segundo.
3. Dor: "leio e não entendo"; desconfia de vídeo sensacionalista ou com cara de IA.
4. Confia em arte clássica, referência bíblica e tom sério e acolhedor.
5. Clicaria numa capa que mostra uma cena da Bíblia e aponta um detalhe que ele nunca reparou.

## Referências (10, de 7 países)
Os links são dos canais e estúdios. **Não conferido nesta sessão:** a busca da web não trouxe as páginas, e o YouTube não abre por robô aqui. Por isso não há capturas salvas e nenhum número de inscritos é citado.

| # | Referência | País | O que tem | Situação |
|---|---|---|---|---|
| 1 | **Johnny Harris** (youtube.com/@johnnyharris) | EUA | Foto ou mapa com **uma anotação à mão** (círculo, seta e nota) mostrando o detalhe da história | **ESCOLHIDA** |
| 2 | **Fall of Civilizations**, Paul Cooper (youtube.com/@FallofCivilizations) | Reino Unido | Pintura de ponta a ponta, sem moldura, com **título serifado em caixa alta**, curto e grave | **ESCOLHIDA** |
| 3 | **Veritasium** (youtube.com/@veritasium) | Austrália/EUA | **Um único foco**, até 3 palavras, imagem clara e limpa | **ESCOLHIDA** |
| 4 | BibleProject (youtube.com/@bibleproject) | EUA | Ilustração autoral, quase sem texto | descartada: exige ilustração própria e foge da gravura de Doré |
| 5 | Kurzgesagt (youtube.com/@kurzgesagt) | Alemanha | Vetor chapado e colorido | descartada: estilo vetorial, sem ligação com a pintura clássica |
| 6 | Epic History (youtube.com/@EpicHistoryTV) | Reino Unido | Pintura histórica com título bold e vermelho | descartada: vermelho (hipótese do Peter: confunde com "já assistido") |
| 7 | Nota Bene (youtube.com/@NotaBeneMovies) | França | Pintura histórica com o rosto do apresentador | descartada: depende de rosto, e o canal é dark |
| 8 | História em Meia Hora (youtube.com/@HistoriaEmMeiaHora) | Brasil | Imagem histórica com texto amarelo gigante | descartada como nova: é o que o `capas2.py` já faz (fica como B) |
| 9 | The AI Bible / Pray.com | EUA | Épico gerado por IA, azul-petróleo e laranja | descartada: estética "Marvel de videogame", criticada (ver `pesquisa/biblia-estilos-video.md`) |
| 10 | Academia Play (youtube.com/@AcademiaPlay) | Espanha | Pintura clássica com recortes e setas | descartada: recorte de figura em gravura P&B serrilha; ficou só a ideia da seta, pela ref. 1 |

## O que cada capa copia
- **Da ref. 1 (Johnny Harris):** um círculo amarelo feito à mão em volta do detalhe, uma seta e uma nota manuscrita (Caveat, a fonte de anotações do canal) com a pergunta do vídeo: "e ele dormia?", "livres… e quiseram voltar", "cadê o cavalo?". Isso conversa com o roteiro, porque cada vídeo ensina a "olhar o detalhe".
- **Da ref. 2 (Fall of Civilizations):** a gravura de ponta a ponta e o título em serifa clássica (Cinzel 900) em caixa alta, embaixo à esquerda, sobre um degradê escuro só na base.
- **Da ref. 3 (Veritasium):** um foco por capa, título de 2 ou 3 palavras e imagem clara (brilho +32% sobre a cor de cinema do `capas2`).
- **Mantido da identidade do Passaporte:** a gravura de Doré com a cor de cinema do `capas2.py` (função `grade`), "PASSAPORTE DA BÍBLIA" em Special Elite, a etiqueta ciano da série e a palavra-chave em amarelo. Nada de vermelho.

| Vídeo | Nova (N) | Aprovadas (capas2) |
|---|---|---|
| longo-10 Milagres | gravura 064 (tempestade), círculo no barco, "e ele dormia?", NÃO ERA **SHOW** | A NÃO ERA SHOW · B FICA CALADO · C MAR vs TÚMULO |
| longo-11 Êxodo | gravura 019 (o cesto no Nilo), círculo no cesto, "livres… e quiseram voltar", POR QUE **VOLTAR?** | A POR QUE VOLTAR? · B TIRADO DAS ÁGUAS · C EGITO vs DESERTO |
| longo-12 Paulo | gravura 095 (a luz no caminho), círculo em Saulo, "cadê o cavalo?", ELE **PERSEGUIA** | A ELE PERSEGUIA · B 3 NAUFRÁGIOS · C PERSEGUIDOR vs APÓSTOLO |

## Conferência
- Legível no celular: o título tem 112 px de altura de letra em 1280×720 e a nota tem 64 px.
- Só no círculo da longo-11 a nota passa perto das figuras. Se o Lindson achar poluído, a nota sai e ficam o círculo e o título.
- Teste sugerido no YouTube: N contra A (e C, se houver 3 slots), por 2 semanas, ganhando a de maior tempo de exibição.
