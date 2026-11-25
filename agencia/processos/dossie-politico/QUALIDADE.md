# Dossiê político · exigências e padrão de qualidade (conta Zuleide, 25/11/2026)

Pedido do Lindson (25/11/2026): "salve no repositório todas as exigências e padrão de qualidade do dossiê". Este arquivo junta tudo. O estilo visual oficial está em `agencia/processos/dossie-politico.md` (conta Pedro) e o gerador em `agencia/processos/dossie-politico/README.md`. **Ler os três antes de qualquer dossiê.**

## 1. Para que serve
- É a peça de prospecção do vereador ou político. Mostra que a gente conhece a situação dele melhor do que ele, aponta os buracos de comunicação e termina na oferta (método em 4 fases até 2028).
- No SDR, o dossiê entra já na 1ª abordagem (msg v5 aprovada em 25/11: "Gostaria de te mostrar um dossiê completo sobre o seu mandato: como ele chega hoje ao eleitor, o que podemos fazer no restante do mandato e o aquecimento para 2028").
- Público: suplente e candidato também recebem dossiê, nunca chamados de "vereador".

## 2. Padrão único (nunca mudar o estilo)
- Lindson, 24/11: "Sempre vamos fazer todos no mesmo estilo." O modelo é o do Francisco Messias. Também são modelos oficiais: Alcemir Costa, Rafael Campaner e Fabiano Fubá (PDFs no privado em `dados/agencia/referencias/dossie-politico-modelos/`).
- **26 páginas 16:9**, na ordem fixa de `dossie-politico.md`.
- **Visual:** grafite (#1A1C1F) com papel creme em páginas alternadas e cor de destaque **do partido do político** (Podemos verde, PP azul-claro, PSD azul…), usada só como detalhe. Fontes: Anton/condensada, Archivo, IBM Plex Mono.
- **Títulos:** 2 linhas; a 2ª linha vai na cor do partido e termina com ponto.
- **Cabeçalho de toda página:** número + seção em mono.
- **Rodapé:** "DOSSIÊ · NOME · CIDADE/UF · DATA" + fontes da página + "NN/26".
- **Números:** gigantes, com legenda curta; barras com rótulo direto; só a barra do político na cor do partido.
- **Gerador:** copiar a pasta de um dossiê pronto (`dados/clientes-arquivos/fabiano-fuba/` ou `alcemir-costa/`), nunca criar do zero.
- **Dossiê de dentista ou clínica (lead de negócio):** mesmo gerador, adaptado em cerca de 18 páginas (ex.: Dra. Giseli Araújo, 25/11, acento teal).

## 3. Pesquisa (antes do PDF)
- A pesquisa é feita pela **extensão do Lindson** (navegador logado), com prompt no formato abaixo. A sessão sozinha não abre Instagram nem Facebook sem login.
- Fontes oficiais primeiro:
  - TSE: resultados.tse.jus.br, DivulgaCandContas e dados abertos;
  - site e SAPL da Câmara;
  - Diário Oficial;
  - imprensa, sempre com o lado de cada blog.
- Complemento do TSE (conta Pedro): votos, colocação, % dos válidos, eleitos e suplentes do partido, histórico de eleições.
- **Seções obrigatórias:**
  - identificação e homônimos;
  - situação atual;
  - linha do tempo eleitoral;
  - bens e doadores;
  - mandato (projetos, comissões, presença);
  - base por bairro e zona;
  - alianças;
  - contexto da cidade para 2028;
  - pesquisas;
  - Instagram (seguidores, frequência, últimos 12 posts, engajamento médio, melhores e piores);
  - outras redes e mídia;
  - passivos (TJ, TRE, TCE, MP);
  - concorrentes;
  - foto oficial em alta resolução;
  - lacunas e fontes.
- **Pesquisa parcial:** gerar um prompt de complemento só com o que falta. Modelo: o do Ricardo Seidel, em 25/11, com 10 itens: situação atual, Instagram, mídia, trabalho no cargo atual, mandato, base, política, bens, passivos e foto.

## 4. Regras de conteúdo (um erro = não entrega)
1. **Nenhum número inventado.** Todo número tem fonte, e toda conta mostra a fórmula no rodapé (ex.: "65% = 8.908 ÷ 13.690").
2. Notas por canal são **"avaliação da equipe"**, com o critério escrito na página (existe 2 · ativo 2 · formato 2 · alcance medido 2 · leva a ação 2).
3. Votos de 2028 são sempre **"simulação · não é previsão"**. Mapa é **"esquemático · sem escala"**.
4. **Passivos:**
   - com fonte, o lado da fonte e a situação;
   - quando couber, "sem condenação definitiva";
   - selo "CONDENAÇÕES: NENHUMA ENCONTRADA" só se houve consulta.
5. Sem promessa de voto ou de resultado, sem preço e sem nota interna da equipe.
6. **Dado que falta não é inventado:** a página sai como "dado a levantar" (modelo Laci v3) e entra na lista de lacunas.
7. Divergência entre fontes (ex.: 55,17% × 55,11%): mostrar as duas ou usar a oficial do TSE, e dizer qual.
8. **Situação atual sempre conferida.** Ex.: Seidel virou secretário em 2025 e uma suplente assumiu a vaga dele.
9. **Fotos:**
   - só de fonte pública oficial, com crédito;
   - ampliação no máximo 1,5× (a do TSE, 161×225, não serve para a capa);
   - recorte com rembg, e a borda da foto nunca aparece;
   - sem foto pública: capa com números do grupo, nunca uma foto inventada.
10. **CTA final** com WhatsApp (98) 98562-1808 (wa.me com mensagem pronta) e a assinatura "LINDSON ALMEIDA · ESTRATEGISTA DE COMUNICAÇÃO POLÍTICA · @LINDSONALMEIDA_".
11. **Tom:** diagnóstico respeitoso que abre conversa, nunca um ataque ao político.

## 5. Conferência antes de entregar (definição de pronto)
- Abrir com zoom a capa, o meio (págs. 6, 10, 13) e o fim: nada cortado, nada sobreposto, nenhum vazio sem sentido (págs. 10, 12 e 16 costumam sobrar).
- Conferir cada número grande contra a pesquisa: capa, resumo, votos, Instagram.
- Conferir a cor do partido, o nome e a cidade em todas as páginas, a data e a numeração "NN/26".
- Defeito conhecido: foto encostando no título (Alcemir v1, pág. 26). Conferir isso.
- Arquivo refeito ganha nome novo (-v2), e a versão antiga fica marcada na Biblioteca.
- Entregar com a lista honesta de lacunas e de defeitos que sobraram. Nunca dizer que agentes ou skills foram usados se não foram.

## 6. Nome dos arquivos e prompt da extensão (conta Pedro, 25/11)
- Nome de todo arquivo: **"Dossiê - Nome do vereador"** (ex.: `Dossiê - Ricardo Seidel.pdf`); versão nova `Dossiê - Nome v2.pdf`.
- Prompt oficial da extensão (itens 0–12, pesquisa completa obrigatória e checklist): `agencia/prospeccao/vereador/PROMPT-DOSSIE-MODELO.md`. Cada vereador ganha o seu `PROMPT-DOSSIE-<NOME>.md` na mesma pasta.

## 7. Onde salvar
- **Privado:**
  - `dados/clientes-arquivos/<politico>/`: material/ (pesquisa + prints), gerador, PDF -vN e previa.jpg;
  - commit com "Co-Authored-By" e "Claude-Session".
- **Repo lindson:**
  - linha no `MENTE-COLETIVA.md`;
  - aprovado ou reprovado na `MEMORIA-DO-LINDSON.md`;
  - lista "Dossiês já feitos" no README do gerador.

## 8. Dossiês feitos (situação em 25/11/2026)
- **Modelos oficiais:** Francisco Messias, Fabiano Fubá, Rafael Campaner, Alcemir Costa (v1; pág. 26 a corrigir se aprovado).
- **Aguardando avaliação:**
  - Laci Júnior v3;
  - Dra. Giseli Araújo v1 (dentista, 18 p.);
  - Ricardo Seidel v1 (pesquisa parcial, complemento pedido à extensão).
