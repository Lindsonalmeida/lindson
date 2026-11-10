# Leo Pinto · v16 · 10 conteúdos (4 saudações + 6 estratégicos) · conta Zuleide, 09-10/11/2026

**Pedido do Lindson (09/11):** "quero 10 conteúdos dele, com foto, no novo padrão de qualidade, variando entre saudação e conteúdos estratégicos sobre o que ele já fez como vereador".

## Situação: PARADO, falta material do cliente
As artes não foram desenhadas porque faltam duas coisas que não podem ser inventadas:
1. **Fotos do Leo que ainda não foram usadas.** Do álbum de estúdio só sobram 7 livres (f06, f09, f17, f21, f22, f26, f29; ver `../FOTOS-USADAS.md`), e elas **não estão nesta máquina** (ficam na aba Fotos da Central, que exige login, e no rascunho de outra conta). Mesmo com elas, faltam **pelo menos 3 fotos** para 10 peças sem repetir. Ideal para os estratégicos: fotos dele nos povoados, na Câmara e nas entregas.
2. **O que ele fez como vereador, com fonte.** Nada no repositório, no privado (`dados/leo.json` não tem entregas do mandato) nem em busca pública (10/11). A estratégia já pedia a "lista de entregas e indicações do mandato" (`../estrategia/ESTRATEGIA.md`, seção 10).

**Pronto:** persona, pesquisa premium (`TEMPLATE.md`, 10 capturas em `referencias/`, 5 países), plano das 10 peças (abaixo) e as legendas das 4 saudações (`TEXTOS.md`).

**Como retomar:** com as fotos em `<scratchpad>/leo-album/` e os fatos em `TEXTOS.md`, montar `gerar.py` a partir do kit do `../instagram-v14-datas/gerar9.py` (mesmo jeito da v15), rodar `node ../instagram-v14-datas/render.js <pasta>`, conferir a borda do recorte (checagem do `gerar6.py`), gerar `previa-feed.jpg`, subir na aba "Para aprovar" do painel do Leo como a v15 fez (`../instagram-v15-saudacoes/legendas_painel.py`; **não rodar o `montar-leo.py`**) e acrescentar as fotos no `FOTOS-USADAS.md`.

## Persona (o eleitor de São João Batista)
1. **Quem:** morador da sede e dos povoados de São João Batista (MA), 25 a 65 anos: pescador, lavrador, comerciante, servidor, mãe de família, jovem que estuda.
2. **Rotina:** acorda cedo (campo, lago, comércio); vê o celular à noite e no almoço, pelos stories e pelos grupos de WhatsApp da família, da igreja e do futebol.
3. **Dor:** político que só aparece em eleição; não sabe o que o vereador faz de verdade.
4. **Valoriza e confia:** rosto conhecido, foto real no lugar dele, o nome do povoado escrito, fé, festa, gratidão e prova (data, número da indicação, o morador junto). Gosta da parceria com a prefeitura, não de briga.
5. **Onde está:** Instagram @_leonardopinto (3.161 seguidores em 01/11) e WhatsApp.

**Teste "ele compraria disso?":** só se a peça mostrar uma coisa que ele reconhece (o povoado dele, o Leo lá, uma entrega real). Peça com fato genérico ou foto repetida não passa. Por isso o v16 espera o material.

## Plano das 10 peças (ordem do feed, cor e composição nunca repetidas em seguida)
| # | Tipo | Data / tema | Composição copiada | Cor |
|---|---|---|---|---|
| 1 | Saudação | 19/11 Dia da Bandeira | AOC 2018 (Tandem): retrato grande + blocos inclinados | Laranja |
| 2 | Estratégico E1 | "NA CÂMARA." | Labour 2024 "Change": uma palavra gigante + retrato | Azul |
| 3 | Estratégico E2 | nome do povoado | Mamdani 2025 (Forge): letreiro do lugar em amarelo sobre azul | Marinho |
| 4 | Saudação | 26/11 Ação de Graças | AOC: "OBRIGADO" em bloco + retrato | Laranja |
| 5 | Estratégico E3 | "PEDIU? TÁ FEITO." | AOC + v13 v3 (nome em blocos) | Azul |
| 6 | Saudação | 03/12 Pessoas com Deficiência | Labour: "INCLUSÃO" + retrato | Laranja |
| 7 | Estratégico E4 | "OLHO DE ENGENHEIRO" | Labour: uma palavra | Marinho |
| 8 | Saudação | 08/12 Dia da Família | AOC: "FAMÍLIA" gigante atrás do Leo | Laranja |
| 9 | Estratégico E5 | 2º povoado | Mamdani | Azul |
| 10 | Estratégico E6 | "2026 DO MANDATO" | AOC + Labour | Laranja |

Datas já feitas e fora daqui: 15/11, 20/11, 11/12, 25/12, 31/12, 01/01 (v14) e as saudações genéricas da v15. Aniversário da cidade: sem fonte confiável, pedir ao Leo.

## Correção "bairro" → "povoado" (09-10/11)
São João Batista não tem bairros, só povoados. Trocado nos textos já feitos: `../instagram-v13-apresentacao/TEXTOS.md`, `../instagram-v14-datas/TEXTOS.md` e `textos.json`, `../instagram-v15-saudacoes/TEXTOS.md` e `legendas_painel.py`, `../whatsapp-figurinhas/README.md`, `../estrategia/` (3 arquivos), `../identidade/BRIEF.md`, `agencia/sistema-clientes/leo-pinto/gabinete.js` e `painel-leo.html` (rótulos e legendas, sem mexer nos nomes internos do código) e, no privado, `dados/leo.json` e `painel/leo.html`. A `BIO.md` já estava certa e as 10 figurinhas não têm a palavra. **Ficou:** os vídeos do Motion v1 já postados ("Comenta o nome do seu bairro", "Manda no direct a demanda do seu bairro") e os geradores antigos da v14; a categoria de fotos "Bairros e povoados" da Central não mudou porque as fotos já enviadas estão guardadas com esse nome.
