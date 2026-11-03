# Revisão geral do acervo Maquiavel (fase 2 da missão)

**Situação:** ciclo 1 concluído (02/11/2026); ciclo 2 concluído (03/11/2026; pendências 1–3 abaixo); agente v3 testado e correções dos testes v3 aplicadas no acervo (seção "Testes v3 — correções no acervo", conta Zuleide, 03/11/2026).

A pesquisa (fase 1) terminou com 11 arquivos (≈1,2 MB) feitos pelas contas Zuleide, Pedro e Lindson, mais o material paralelo em `frente-lindson/`. A revisão roda em ciclos até não sobrar nada a corrigir ou acrescentar ("sem erro, sem faltas, sem lacuna").

## Ciclo 1: três frentes
| Frente | O que faz | Relatório |
|---|---|---|
| Citações | Programa que extrai todas as citações em italiano dos arquivos e confere no texto original (Wikisource/Liber Liber); corrige as erradas | `revisao/citacoes.md` |
| Contradições | Datas, nomes, fatos e atribuições que divergem entre arquivos; decide pela fonte e corrige todos os arquivos | `revisao/contradicoes.md` |
| Cobertura e lacunas | Compara com a lista mestra de obras (`missoes-e-escritos-politicos.md`, seção A), capítulos, cartas, legações, pessoas e com `frente-lindson/`; fecha as lacunas listadas no fim de cada arquivo | `revisao/cobertura.md` |

## Como retomar
Cada relatório tem no topo "Situação: parcial — feito até X". Continuar dali. Regras: `REGRAS-DA-PESQUISA.md` e `COMO-SALVAR.md`.

## Resultado dos ciclos

### Ciclo 1 (conta Zuleide, 02/11/2026) — concluído
- **Citações** (`revisao/citacoes.md`): 2.060 citações em italiano conferidas por programa em 16 arquivos. 1.814 exatas, 77 iguais salvo grafia, 64 só por fonte secundária, 17 à mão, 85 fora do escopo, 3 não conferíveis (marcadas), 3 curtas demais. 37 correções de texto em 35 lugares + 9 notas. 709 citações conferidas também no capítulo indicado; 1 referência errada corrigida (*Discursos* III.41).
- **Contradições** (`revisao/contradicoes.md`): 46 divergências, todas resolvidas em 15 arquivos (34 decididas pela fonte, 12 com versões registradas igualmente em todos os arquivos). Agente atualizado.
- **Cobertura** (`revisao/cobertura.md`): todas as obras, capítulos (26 + 142 + 7 livros/27 regras + 8 livros) e pessoas cobertos. Lacunas fechadas: Vegécio × regras da *Arte da Guerra*, legações 1518 e 1525–27, escritos menores esquecidos (C.14), *La Sporta*, cartas (≈80 enviadas, ≈250 recebidas), traduções brasileiras comparadas, Montesquieu e Weber no original, Vettori †1540.

### Ciclo 2 — pendências que sobraram do ciclo 1
1. *Discursos*: 101 capítulos sem ficha detalhada + tabela *Príncipe* × *Discursos*. **[x] Feito (conta Lindson, 02/11):** fichas em `discursos-fichas-livro-1.md`, `-2.md` e `-3.md` (36 + 26 + 40, 300+ citações conferidas no italiano), tabela completa no livro-3 e 9 correções aplicadas em `discursos.md`.
2. Ensinamentos que faltam nos 248 (História de Florença, missões, cartas, literatura, Arte da Guerra além das regras) e conferência das aplicações de negócio nas fichas. **Feito (conta Zuleide, 03/11/2026):** `ensinamentos-complementares.md` (249–640), 11 correções de aplicação, `INDICE-POR-SITUACAO.md` — ver `revisao/cobertura.md`, "Ciclo 2 — ensinamentos".
3. Fatos e fontes: prisão de 1513 (12 × 19/2), sonho em Busini, colofões das primeiras edições, "dividir para reinar" × *Arte da Guerra* VI, casamento, bairro do nascimento, folhas do *Belfagor*, *Mandrágora* em Veneza, citações de terceiros (Croce, Guicciardini 18/07/1526, Giuliano de' Ricci), 64 citações só por fonte secundária, verbetes Treccani que faltaram, Diderot/Gentili/Pole/Bodin no original, idiomas polonês, coreano, hindi, turco. → **Feito (conta Zuleide, 03/11/2026):** ver `revisao/contradicoes.md`, seção "Ciclo 2" (C2.1–C2.8), com o que ficou aberto e por quê.


## Depois do ciclo 2 (pedido do Lindson, 03/11/2026)
"Quando terminar tudo, finalize o agente." Ao fechar o ciclo 2: agente v2 em `.claude/agents/maquiavel.md` (usando `INDICE-POR-SITUACAO.md`, `ensinamentos-complementares.md`, os relatórios da revisão e `dinheiro-online/`), rodar os 12 testes do `TESTES.md`, corrigir o que falhar, registrar no `REGISTRO-DAS-CONTAS.md` e tirar do quadro.

## Testes v3 — correções no acervo (conta Zuleide, 03/11/2026)

Correções achadas nos testes do agente v3 (as respostas dos testes ficam em `revisao/testes-v3/`; o agente em `.claude/agents/maquiavel.md` é outra frente e não foi mexido aqui). Cada item foi conferido no original.

| # | O que | Onde | Resultado |
|---|---|---|---|
| 1 | *Príncipe* XIII citado errado ("o e' ti cascano di dosso…", forma que não existe em edição nenhuma) | `dinheiro-online/plano-para-o-lindson.md` ("Uso pelo agente") e `dinheiro-online/servicos-e-agencia.md` | Trocado pelo texto de Inglese: "le arme di altri o le ti caggiono di dosso o le ti pesano o le ti stringono". **Conferência de citações rodada em toda a pasta `dinheiro-online/` e em `../maquiavel-todos-ensinamentos.md` e `../maquiavel-ensinamentos.md`**: 17 citações em italiano, 4 corrigidas (*Príncipe* III, VI, VII, XVIII), todas exatas agora. Registro: `revisao/citacoes.md`, "Testes v3"; tabela `revisao/citacoes-tabela-testes-v3.tsv` |
| 2 | *Príncipe* XVIII "conto di vivere" × "di vincere" | `recepcao-e-estudiosos.md` 5.1; `principe.md` 1.9 | Nota com as duas lições (vulgata "conto di vivere"; Inglese/Martelli "di vincere"; Villari "conto di vincere"); **o acervo usa "di vincere" (Inglese)** |
| 3 | Busenbaum, *Medulla theologiae moralis*, **1650** (contradições nº 37) | `recepcao-e-estudiosos.md` 5.1 (era "c. 1645/1650"), `contexto-e-personagens.md`, `maquiavel-nos-negocios.md`, `discursos.md`, `frente-lindson/contexto-e-personagens.md`, `frente-lindson/historias-e-curiosidades.md`, `../maquiavel-todos-ensinamentos.md` | Data e fórmula acrescentadas onde a frase "os fins justificam os meios" é tratada |
| 4 | Strauss, "a teacher of evil" | `principe.md` 4.2 e 7.4; `recepcao-e-estudiosos.md` 3.3 | Conferido na 1ª ed. (The Free Press, 1958, Internet Archive): **primeira frase da Introdução**, texto exato registrado; marca "citado de memória" retirada |
| 5 | Rousseau, *Contrato social* III.6 | `recepcao-e-estudiosos.md` 2.2; `principe.md` 4.1 e 7.1 | Francês conferido no fr.wikisource (ed. 1762: "En feignant de donner des leçons aux Rois il en a donné de grandes aux peuples. Le Prince de Machiavel est le livre des républicains.") e a nota de 1782 (via ed. Beaulavon 1903); os dois arquivos agora iguais |
| 6 | "senza danari" (teste 14) | `missoes-e-escritos-politicos.md` B.3; `TESTES.md` teste 14 | Não é máxima: é a queixa do enviado sem verba, conferida em Chiappelli I–II e Martelli — Lyon 30/7/1500 ("per essere homini sanza danari et sanza credito"), Blois 8/10/1500 ("non si va sanza danari"), Ímola 27/10/1502, Cesena 23/12/1502. Teste 14 passa a pedir a carta de Melun e a de Lyon |
| 7 | Prisão de 1513: "cerca de vinte nomes" × 12 suspeitos | `vida-e-cartas.md` (1513 e 6.7) | São duas listas: o papel de Boscoli ("18 o 20 nomi", Villari II cap. X; Ridolfi "una ventina", 7º lugar) × a lista de 12 suspeitos na carta de Giuliano ao Bibbiena de 19/2/1513 (Villari). O DBI não dá número |
| 8 | Carta de 16/4/1527 | `revisao/citacoes.md` (V3.6); `vida-e-cartas.md` 2.5 e 3.5 | "articolo" do Wikisource é erro do texto-fonte: Martelli e Lesca leem "i più difficili articuli". Destinatário (Francesco Vettori) dito em 2.5 |
| 9 | *História de Florença* III.7, "tanto quelli cittadini stimavano allora più la patria che l'anima" (Oito Santos) | `historia-de-florenca.md` 2.3 (cap. 7) e 3.7; `ensinamentos-complementares.md` **641** (novo) | Conferido em Martelli (BibIt), Liber Liber e Wikisource; ligado à carta a Vettori de 16/4/1527 |
| 10 | Carpi, maio de 1521 | `missoes-e-escritos-politicos.md` B.14; `ensinamentos-complementares.md` 542 | "il fumo ne è ito sino al cielo" datado: **18/5/1521**; acrescentado "perché la riputatione crescesse" (**17/5/1521**) com a lição (e o limite: nunca inventar fatos para o cliente) |
| 11 | *Príncipe* III "ruina" × "rovina" | `principe.md` 1.9 | Variante anotada (Inglese/Martelli "ruina"; vulgata "rovina"); o acervo usa "ruina" |
| 12 | Riscos legais | `dinheiro-online/riscos-legais-e-regras.md` 3.9 e 3.10 | Novas seções: **avaliações falsas** (política do Google lida na página oficial, restrições ao Perfil da Empresa, CDC arts. 36–37 e 67, Lei 9.279 art. 195, Súmula 227 STJ, casos próximos, FTC/UE/Reino Unido; [Conferir] no que não é oficial) e **marketing para candidato** (CNPJ e conta de campanha, prestação de contas, art. 57-C, Res. 23.610 alterada pela 23.755/2026, calendário de 2028; [Conferir]) |
| 13 | Linhas "Situação" | `historia-de-florenca.md`, `vida-e-cartas.md`, `principe.md`, `recepcao-e-estudiosos.md`, `missoes-e-escritos-politicos.md`, `contexto-e-personagens.md`, `literatura.md`, `arte-da-guerra.md`, `maquiavel-nos-negocios.md`, `discursos.md`, `ensinamentos-complementares.md`, `INDICE-POR-SITUACAO.md`, este `REVISAO.md` e os relatórios de `revisao/` | Atualizadas para os ciclos 1 e 2 e os testes v3 |
| 14 | Leão X (pedido do coordenador) | `vida-e-cartas.md` e `frente-lindson/vida-e-cartas.md` (1513), `contexto-e-personagens.md` (2 lugares), `principe.md` 1, `frente-lindson/historias-e-curiosidades.md`, `revisao/contradicoes.md` | Unificado: **eleito no escrutínio da manhã de 11/3/1513**, ordenado padre em 15/3, sagrado em 17/3, **coroado em 19/3/1513** (Villari II cap. X; DBI "Machiavelli"; relato do conclave de 4–11/3). A data 9/3 de algumas listas (Wikipédia italiana, Miranda) fica registrada e não é usada |

**Ficou aberto:** Ridolfi (número e posição dos nomes na lista de Boscoli) não aberto no livro; DBI "Leone X" não abriu na rede; texto oficial da Resolução TSE 23.607 com as mudanças de 2026, número 23.755 da alteração da 23.610 e resoluções de 2028 (só em 2028); decisão de Procon/TJ específica sobre avaliação falsa no Google; nota de 1782 de Rousseau conferida pela transcrição da ed. Beaulavon, não pelo fac-símile de 1782. O `CLAUDE.md` não foi mexido.
