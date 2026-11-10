# Capas de Reels · Rafael e Tiago (10/11/2026, conta Zuleide, designer gráfico)
Status: **aguardando aprovação do Lindson.** Imagens no privado: `CentralLindsonALmeida/dados/clientes-arquivos/curso/capas-reels/` e no painel do curso, aba **Para aprovar**.

## Persona (5 linhas)
Vereador, assessor ou servidor de câmara municipal no Maranhão, 28 a 55 anos. Rotina de sessões, pareceres e prazos do regimento. Dor: errar no plenário por não saber o rito. Valoriza seriedade, clareza e autoridade de quem ensina. Confia em professor com credencial e linguagem de manual, não em post "fofo". Está no Instagram entre uma sessão e outra.
Teste: compraria? Sim, se a capa parece material de estudo sério e o professor aparece com autoridade.

## Pesquisa premium (capturas em `referencias/`, 9 válidas, 5 países)
| # | Referência | País | Situação |
|---|---|---|---|
| 01 | Pentagram, Work | EUA/Reino Unido | descartada (portfólio geral) |
| 02 | Studio Dumbar, Work | Países Baixos | **escolhida (C)**: bloco de cor com glifo gigante |
| 04 | Collins, Work | EUA | descartada (cartões de case, pouco texto) |
| 05 | Koto, Work (Norton, Where London Meets) | Reino Unido | **escolhida (A e D)**: palavra gigante atrás da imagem; caixa alta empilhada |
| 06 | Harvard Law Review | EUA | **escolhida (B)**: rótulo editorial + título serifado |
| 07 | Der Spiegel | Alemanha | descartada (pop-up cobre a página) |
| 08 | Yale Law Journal | EUA | descartada (parecida com a 06) |
| 09 | The Guardian, Law | Reino Unido | descartada (foto de notícia) |
| 10 | Monocle | Suíça | descartada (revista, pouco contraste) |
Bloqueadas: Mucho (ES), The Economist, Die Zeit, Le Monde.

## Composições
A foto + palavra gigante atrás (Koto) · B editorial (Harvard Law Review) · C dourado com § gigante (Dumbar) · D caixa alta empilhada (Koto).
Ordem de postar: 01 Rafael A, 02 Tiago A (creme), 03 Rafael B, 04 Tiago C, 05 Rafael D, 06 Tiago B, 07 Rafael C, 08 Tiago D. Rosto dos dois com a mesma largura (360 px) e mesma altura.

## Fotos
Só existe **1 foto real de cada professor** no painel/privado. Usadas: Rafael na capa 01, Tiago na capa 02. Capas 03 a 08 saíram tipográficas: **faltam 3 fotos de cada** (6 no total).

## v2 (10/11, retorno do Lindson): 01 e 02 APROVADAS; 03 a 08 refeitas com imagem de banco
Fotos novas do painel: não deu para ler (ficam no KV `CONTAS`, chave `foto:curso:<id>`; o conector da Cloudflare só lista namespaces e a rota `/api/fotos` exige login). Usei banco Pexels (licença Pexels, uso livre, crédito opcional):
| Capa | Pexels ID | Foto · autor |
|---|---|---|
| 03 questão de ordem | 32266781 | Plenário vazio com microfones · Héctor Berganza |
| 04 sancionar | 34066105 | Mão assinando documento formal |
| 05 moção | 36207471 | Plenário do Parlamento suíço, Berna · Christian Wasserfallen |
| 06 procedimento | 7054510 | Pessoa escrevendo no papel |
| 07 fases | 35013248 | Câmara dos Comuns do Canadá · Daniel Miller |
| 08 urgência | 7224866 | Ampulheta · Dhia Eddine |
Ordem das cores no grid: verde, creme, verde, creme, dourado, creme, dourado, verde (sem cor igual lado a lado nem em cima).

## v4 (10/11): 03 a 08 copiam o sistema APROVADO da 01/02
Mesmo código (`A2` = função `A` da 01/02 com outra foto): recorte BiRefNet (`recorte2.py`), rosto ~360 px na mesma altura, palavra gigante em Instrument Serif itálico atrás da cabeça, manchete Inter Tight 900 com 1 destaque em itálico dourado, tag "§ PROCESSO LEGISLATIVO · Prof." no topo, "assista ao Reels ↓". Xadrez: Rafael verde, Tiago creme (grid sem cor repetida ao lado nem em cima).
Coleta aplicada (em todas): social-media-advocacia estilo **E Black & Gold Autoridade** (retrato recortado + palavra gigante no fundo) e **F Assinatura gráfica** (§ fixo); tabela premium (hierarquia de 3 níveis, 1 palavra em itálico serifado, rodapé fixo, mesmo tratamento de foto); designer-grafico "letra passando por trás da pessoa"; motion #35 grão.
Palavra de fundo: 03 ordem · 04 sanção · 05 moção · 06 rito · 07 fases · 08 urgência.

## v5 (10/11): v4 REPROVADA ("muito simples, sem camadas, sem glamour"); v5 em camadas
Capturas reais do Behance em `v5/referencias/` (prévias; capturas inteiras no scratch da sessão):
| # | Referência (BR) | O que foi copiado |
|---|---|---|
| R1 | Behance 222952139 · Key Visual Experts (A Manada) | aura de luz atrás do expert, rim light no contorno, feixes de luz de cima |
| R2 | Behance 144495005 · Dieggo Bruno Advogados (Isaque dsgn) | preto/verde + dourado, cena real ao fundo, selo do escritório, linha dourada na chamada |
| R3 | Behance 166179777 · Social Media Advocacia (Igor Vinicius) | palavra serifada gigante cortada atrás da pessoa, objeto jurídico (§ em bronze, documento) |
Descartadas: as outras 97 do `lancamento-infoprodutor-expert` (neon/laranja fora da paleta) e Dark Luxo cobre (paleta).
Camadas (12): cena de banco desfocada (Pexels da v2, uma por capa; 04 e 06 com bancadas do plenário desenhadas) · vinheta de cor · feixe · halo · palavra gigante em degradê com sombra projetada + contorno deslocado · § gigante em relevo · documento "§ Nº" · professor recortado com rim light e sombra · brilho anamórfico · carimbo circular · vidro fosco com o tema · cantos de corte e numeração 01/08 · grão. Rosto 330 px, mesma linha para Rafael e Tiago.
