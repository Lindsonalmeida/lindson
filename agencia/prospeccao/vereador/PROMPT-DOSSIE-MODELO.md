# Prompt OFICIAL da extensão para dossiê político (Lindson, 25/11/2026: "esse é o tipo de prompt")
Use SEMPRE este formato (13 blocos numerados 0–12 + LACUNAS + FONTES + /prints). Ele alimenta as 26 páginas do padrão oficial (`agencia/processos/dossie-politico/README.md`). ANTES de escrever: pesquise quem é o político na base de leads do SDR (`CentralLindsonALmeida/functions/_sdr.js`: cidade, @, WhatsApp, fonte) e no TSE (resultados.tse.jus.br: partido, nº, votos 2024 e 2026) e ponha um bloco "JÁ TEMOS" no prompt (regra do Lindson, 25/11: "sempre pesquise quem eles são, da base de leads do SDR"). Troque só os dados entre [colchetes] e adapte os blocos 1, 2, 6 e 7 à pessoa e à cidade.

```
REGRA Nº 1 · ESTA PESQUISA SÓ ACABA QUANDO ESTIVER COMPLETA. É PROIBIDO ENTREGAR VERSÃO PARCIAL.
Antes de me responder, confira o CHECKLIST do fim. Se qualquer item estiver ❌ e você ainda não tentou 3 caminhos diferentes para ele, NÃO entregue: volte e continue pesquisando. Só entregue quando todos os itens estiverem ✅ ou ❌ com os 3 caminhos tentados escritos. Não resuma, não pule bloco, não troque dado por "a verificar".

Faça um DOSSIÊ POLÍTICO completo do(a) [VEREADOR(A) NOME COMPLETO] (urna provável "[URNA]"), [PARTIDO], Câmara Municipal de [CIDADE/UF], mandato [2025–2028] ([mandatos anteriores]). Instagram: @[insta]. Perfil oficial: [link da Câmara]
Use só fontes públicas, com link e data em cada informação. Não invente número. O que não achar vai em LACUNAS. Ao falar da imprensa, diga o lado de cada veículo (favorável, crítico, neutro).

Entregue em Markdown, nesta ordem:
0) IDENTIFICAÇÃO: nome completo e de urna, número, partido, nascimento, homônimos descartados.
1) SITUAÇÃO ATUAL (mês/ano): cargo hoje, Mesa Diretora ou comissões, se disputou 2026 (cargo, votos, resultado).
2) QUEM É: formação, profissão, família política, trajetória social/religiosa, pautas.
3) VIDA ELEITORAL (TSE: resultados.tse.jus.br e DivulgaCandContas): todas as eleições (ano, cargo, partido, votos, % dos válidos, colocação, eleito/suplente). Em 2024: votos do partido na cidade, eleitos, suplentes, quociente. Votos por seção/bairro, se conseguir.
4) BENS E CONTAS (DivulgaCandContas): bens declarados por eleição; receitas, doadores e despesas das campanhas.
5) MANDATO NA CÂMARA: projetos, indicações, requerimentos (número, tema, situação), comissões, presença.
6) ALIANÇAS E POLÍTICA: relação com o prefeito e o grupo local; partido estadual, deputados que apoia; relação com o governador eleito Eduardo Braide (PSD) e com o ex-governador Carlos Brandão; nomes para prefeito em 2028; temas que desgastam a gestão.
7) CONTEXTO DA CIDADE: população e eleitorado, prefeito e vice, resultado de 2024, nº de vereadores e bancadas, cidades vizinhas de influência.
8) INSTAGRAM @[insta]: seguidores, seguindo, posts, bio, link da bio, destaques; posts nos últimos 30 dias; últimos 12 posts (data, formato, tema, curtidas, comentários); engajamento médio (interações ÷ seguidores); 3 que mais e 3 que menos funcionaram; leitura do que funciona.
9) OUTRAS REDES E MÍDIA: Facebook, TikTok, YouTube, WhatsApp/canal; entrevistas, rádios, blogs da região; o que a imprensa fala.
10) PASSIVOS: Escavador/JusBrasil, TJ, TRE, TCE, MP — cada item com fonte, lado e situação ("sem condenação definitiva" quando for o caso).
11) CONCORRÊNCIA: vereadores com perfil parecido e possíveis rivais em 2028, com votos e presença digital.
12) FOTO: 1 foto oficial em alta (site da Câmara ou TSE), com link.
Ao final: LACUNAS e FONTES (link + data). Salve o documento e o zip com o nome "Dossiê - [Nome do vereador]". Salve prints em /prints: perfil do Instagram, os 3 melhores posts, página oficial da Câmara, foto oficial e 2 matérias principais.
PESQUISA COMPLETA É OBRIGATÓRIA (não entregue versão parcial):
- Trabalhe sozinho até o fim; não pare para perguntar. Só pare se pedirem senha, código ou pagamento.
- Use o navegador logado: abra o Instagram e o Facebook de verdade (não só a busca do Google) e role o perfil até ter os 12 posts.
- Se um site não abrir, tente de novo e use alternativas antes de desistir: outra URL do mesmo órgão, cache do Google, web.archive.org, Diário Oficial do município, portal da transparência, SAPL da Câmara, notícias da Câmara. TSE: use resultados.tse.jus.br (votos) e divulgacandcontas.tse.jus.br aberto no navegador (bens, contas, foto). Só escreva "não encontrado" depois de tentar 3 caminhos, e diga quais tentou.
- Cada número precisa de link + data. Calcule e mostre as contas (% dos válidos, engajamento).

ARQUIVOS OBRIGATÓRIOS NO ZIP "Dossiê - [Nome do vereador]" (são usados nas 26 páginas do PDF):
1. Dossiê - [Nome do vereador].md (a pesquisa, nesta ordem 0–12 + LACUNAS + FONTES)
2. /fotos/foto-oficial (a maior resolução disponível, mínimo 1000 px de altura; anote a fonte)
3. /fotos/ 3 a 5 fotos públicas dele em ação (plenário, sessão, bairro, evento), com fonte de cada uma
4. /prints/ perfil do Instagram (tela inteira), os 3 melhores posts, a página oficial na Câmara, a ficha do TSE/DivulgaCand, 2 a 4 matérias principais (com título e data visíveis)
5. instagram-12-posts.csv (data, formato, tema, curtidas, comentários, link)
6. CHECKLIST no fim do .md: tabela com cada bloco 0–12 e cada arquivo acima marcado ✅ feito ou ❌ faltou + motivo e os 3 caminhos tentados
ÚLTIMO PASSO OBRIGATÓRIO: releia este prompt do início ao fim e confira item por item contra o que você entregou. Faltou algo que ainda dá para buscar? Volte e busque antes de responder.
```

Modelo real: Ozima Cury Rad (MDB, Senador La Rocque/MA), 25/11/2026.
Lição (Ricardo Seidel, 25/11): o prompt antigo (9 itens) voltou parcial; TSE resultados.tse.jus.br funciona daqui (a equipe completa votos), DivulgaCand dá 403 fora do navegador.
