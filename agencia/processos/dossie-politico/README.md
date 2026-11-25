# Dossiê político (padrão Francisco Messias) · conta Leandro, 24/11/2026

> **Exigências e padrão de qualidade completos: `agencia/processos/dossie-politico/QUALIDADE.md` (ler antes de todo dossiê).**
Lindson, 24/11/2026: "Sempre vamos fazer todos no mesmo estilo." Todo dossiê de vereador/político segue o do Francisco Messias:
PDF 26 p. 16:9 (1600×900), grafite + 1 acento (cor do partido), Anton + Archivo + IBM Plex Mono, grid, números enormes, mapa esquemático, rede de alianças, gráficos de barra com rótulo direto.

## Onde está o modelo (repo privado CentralLindsonALmeida)
- Gerador parametrizado: `dados/clientes-arquivos/fabiano-fuba/` (`gerar.py` + `dados.json` + `estilo.css` + `render.js` + `mont.py`).
- Original: `dados/clientes-arquivos/francisco-messias/` (gerar.py com o texto embutido).

## Como gerar um dossiê novo
1. `cp -r dados/clientes-arquivos/fabiano-fuba dados/clientes-arquivos/<novo>` e apague PDF, prévia, fotos e material antigos.
2. Ponha a pesquisa da extensão em `<novo>/material/` e as fotos públicas em `<novo>/fotos/` (Câmara/SAPL, notícias, prints; fonte no README; ampliação ≤ 1,5×; recorte com rembg).
3. Edite `dados.json`: `titulo`, `pdf`, `rodape`, `acento` (+ `acento_escuro`, `acento_rgb`), `whatsapp`, `barras` e as 26 `paginas` (mesma ordem e seções). No html: `[[bar:CHAVE]]` = gráfico; `{{A}}` = cor de acento.
4. `python3 gerar.py && NODE_PATH=/opt/node-tools/node_modules node render.js` · prints: `node render.js 1,13 <pasta>` · prévia: `python3 mont.py <pasta> 1,6,10,12,13,22 previa.jpg`.
5. Conferir capa, meio e fim com zoom e cada número contra a pesquisa (conta no rodapé).

## As 26 seções
capa · resumo · quem é · trajetória e bens · linha do tempo eleitoral · votos em números · mapa da base (esquemático) · mandato · produção/pautas · alianças · contexto 2028 · pesquisa ou caso-chave · diagnóstico (% canais) · nota por canal · raio-X Instagram · concorrentes · lacunas · passivos ("o que os adversários vão usar") · SWOT · cenários · simulação 2028 · 4 fases da assessoria · metas e calendário · por que agora · provas e fontes · contato (WhatsApp (98) 98562-1808, "estrategista de comunicação política").

## Regras
Só dados da pesquisa, com fonte; notas = "avaliação da equipe" com critério; votos 2028 = "simulação"; mapa = "esquemático"; sem promessa de voto, sem preço, sem nota interna; passivos com fonte e lado e "sem condenação definitiva"; fotos só de fonte pública, sem login.
- 24/11/2026 · Rafael Campaner (Leandro): dossiê v1 no gerador do Fubá, acento ciano PP #0096D6, pasta privado dados/clientes-arquivos/rafael-campaner/.

## O que os 3 PDFs modelo mostram (Messias, Fubá, Campaner · análise conta Zuleide, 24/11/2026)
Modelos em `dados/agencia/referencias/dossie-politico-modelos/` (privado). Os três são o mesmo template: só mudam nome, acento e dados.

**Partes fixas (iguais nos 3):**
- Cabeçalho de página: quadradinho com nº (fundo acento; preto nas páginas vermelhas) + fio + título em Plex Mono espaçado.
- Rodapé: fio cinza; "DOSSIÊ · NOME · CIDADE/UF · DD.MM.AAAA" + fonte/conta da página; nº "NN/26" em Anton.
- Alternância de fundo: grafite (maioria) · creme #F0EFEC (p.3, 5, 8, 11, 15, 17, 20, 23) · acento cheio (p.13 e 24).
- Título de 2 linhas em Anton caixa alta: 1ª afirmação em branco/preto, 2ª a virada na cor de acento, terminando em ponto.
- Textos fixos: tag da capa "DOSSIÊ DE INTELIGÊNCIA POLÍTICA E COMUNICAÇÃO · CONFIDENCIAL"; meta "CIDADE · ESTADO / DATA / PREPARADO POR LINDSON ALMEIDA"; p.13 "dos canais de um político ele ocupa hoje"; p.14 critério de nota (existe 2 · ativo 2 · formato 2 · alcance medido 2 · leva a ação 2); p.17 "Sete buracos. Todos têm conserto." + 8º card escuro "0"; p.18 selo "CONDENAÇÕES: NENHUMA ENCONTRADA…"; p.22 "Um método, quatro fases, até a urna de 2028." (DEZ/26–FEV/27 · MAR–JUN/27 · JUL/27–MAR/28 · ABR–OUT/28); p.23 calendário legal com as 7 datas e o texto da lei; p.24 três números (22 meses · 16 meses · 1 número do político); p.26 CTA.

**Estrutura por página (layout):** 1 capa (nome 2 linhas, sobrenome no acento; subtítulo; fio acento; 3 KPIs; "2028" gigante a 4% no fundo; político recortado à direita com brilho do acento; crédito da foto no canto) · 2 título + lead + 3 chips FORÇA/FRAQUEZA/RISCO | 4 KPIs em grade 2×2 · 3 foto/print oficial à esquerda + tabela rótulo-mono/valor · 4 linha do tempo 7 marcos (derrota em cinza, ano atual no acento, 2028 com bolinha vazada) + barras de bens + "Leitura" com o "ativo de narrativa" entre aspas · 5 tabela de eleições (linha da última no acento) | barras votos/receita + selo de custo por voto · 6 faixa de 4 números gigantes + barras da chapa + callout com número enorme no acento e fio vertical · 7 mapa esquemático SVG (grade, círculos no acento, legenda "MAPA ESQUEMÁTICO · SEM ESCALA") + lista 3 bases · 8 tabela do mandato + 1–2 fotos com legenda mono · 9 título "N matérias/indicações. Cada uma é um conteúdo não feito." + selo com pautas | barras · 10 rede de alianças SVG (centro no acento, 7 caixas, legenda cheia/tracejada/acento=tensão) · 11 4 números + barras de bancadas + foto/lista "O que muda o jogo" · 12 caso-chave (pesquisa × urna ou investigação) · 13 página toda no acento: % gigante + 7 cards de canal (ativo em preto) · 14 barras de nota + média em selo + tabela "por que a nota" · 15 4 números do Instagram + print do perfil + "O que funciona" / "O que custa alcance" · 16 barras % dos válidos + título + selo "presença digital dos concorrentes: não levantada" · 17 grade 4×2 numerada · 18 tabela tema/o que existe/fonte·lado/situação · 19 SWOT 2×2 (Forças no acento) · 20 3 cenários (o mais provável em card escuro com fio acento; rótulo de probabilidade em mono acento) · 21 barras "SIMULAÇÃO · NÃO É PREVISÃO" + caixa com conta passo a passo 1-4 · 22 4 colunas de fase (1ª com fio acento) · 23 4 metas gigantes + linha do tempo com eleição no acento · 24 fundo acento, título branco + 3 números com fios pretos · 25 grade 3×2 de capturas das fontes + lista de fontes com o lado de cada blog · 26 foto de base/plenário escurecida com degradê para o acento, título 2 linhas, botão WhatsApp no acento, assinatura em mono.

**Componentes:** barras horizontais com rótulo à esquerda, valor em Anton à direita, só a barra do político no acento (resto cinza); selo = caixa com borda acento e texto mono caixa alta; chips com borda branca; números gigantes em Anton com legenda Archivo pequena; toda conta escrita no rodapé ("14% = 1 ÷ 7").
**Acento:** só no sobrenome da capa, 2ª linha dos títulos, quadradinho do nº, barra do político, ano atual da linha do tempo, selos, centro da rede, página 13 e 24 inteiras e botão. Nunca em texto corrido.
**Fotos:** capa = foto oficial recortada (perfil da Câmara/SAPL) com crédito; p.3 = foto ou print oficial; p.8/11 = fotos de notícias da Câmara com legenda e fonte; p.25 = prints das fontes; p.26 = foto de base/plenário. Sem foto pública: não inventar (ver Laci v3: capa com números do grupo e bloco "SEM FOTO · dado a levantar").
**CTA final:** "PRÓXIMO PASSO", frase de 2 linhas que devolve a tese (ex.: "A base já está na rua."), "Uma conversa de 30 minutos para apresentar o plano completo, fase por fase", botão WHATSAPP (98) 98562-1808 com link wa.me e mensagem pronta, "LINDSON ALMEIDA · ESTRATEGISTA/COMUNICAÇÃO E ESTRATÉGIA POLÍTICA · @LINDSONALMEIDA_".

## Dossiês já feitos neste padrão
- Francisco Messias (PDT, vermelho) · Prof. Fabiano Fubá (PSD, azul) · Rafael Campaner (PP, azul claro) · **Laci Júnior v3 (PSB, vermelho, 24/11/2026, conta Zuleide)**: `dados/clientes-arquivos/laci-junior/dossie-laci-junior-v3.pdf`. A v2 (tinta/marfim Economist) foi SUBSTITUÍDA: estilo fora do padrão.

## Nome dos arquivos (Lindson, 25/11/2026)
Todo documento do dossiê (PDF final, Markdown da pesquisa, zip) é salvo como **"Dossiê - Nome do vereador"** (ex.: `Dossiê - Ricardo Seidel.pdf`). Versão nova: `Dossiê - Nome v2.pdf`.
