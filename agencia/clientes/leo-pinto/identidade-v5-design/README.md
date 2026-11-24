# Leo Pinto · identidade v5 (Claude Design) · conta Pedro, 21 a 24/11/2026

Canvas no Claude Design (fonte viva): https://claude.ai/artifact/NiEPRvj7uESL6jzaMzMHRN (privado da conta passaportedabiblia; compartilhar pelo menu Share).

Pedido do Lindson (21/11): "vamos recriar a identidade visual dele… use o Claude Design… visualmente atraente, nada amador, premium, identidade de político. Preserve as cores e a logo e remonte o restante."

## O que foi mantido
- **Logo oficial** (sol sobre as águas): `../identidade-v2/assets/logo.png`, `logo-marinho.png`, `logo-mono-branco.png`. Sempre "LEO PINTO" por extenso, sem placa nem balão.
- **Cores** (hex medidos no próprio logo): laranja `#FF7A1A` (principal), marinho `#05316E`, royal `#2350F5`, sol `#FFC20E`. Apoio: marinho noite `#021A3D`, laranja queimado `#E8650C`/`#B4500C`, ciano da água `#3FB8E8`, papel `#F5F3EE`.
  - Atenção: a MEMORIA registrava marinho `#082063`; o logo usa `#05316E`. Vale `#05316E`.
- **Fontes oficiais do Leo:** Anton (títulos e palavras gigantes), Montserrat 400–900 (nome, frases, texto), Kaushan Script (toque manuscrito).

## O sistema aprovado (o que fazer)
1. **Disco com arcos** (anel amarelo + anel laranja + disco royal→marinho). A cabeça sai por cima do disco e o corpo termina na curva: nenhuma borda reta de camisa aparece.
2. **Foto encostada na borda da arte** (só o recorte do punho, `b-punho`, encostado na direita), com os arcos atrás.
3. **Peça sem foto com um elemento forte:** cartão de enquete, bloco de anotações sobre estrela, frase gigante com foto dentro das letras.
4. **Rosto sempre centralizado** no disco (centro da cabeça calculado em `geradores/facex.json`).
5. **Camadas sempre, nunca fundo chapado:** degradê radial + formas arredondadas tom sobre tom + mapa de São João Batista em camada (6–16%) + palavra gigante clara + textura granulada (`assets/kit/grao.png`).
6. **Traços liberados pelo Lindson (21/11), sempre organizados, um por zona:** linha amarela do contorno do município (horizonte), explosão laranja com o mapa, estrela ciano atrás do ombro, chevrons `›››` na faixa.
7. **Faixa marinho fixa na base** dos posts: "JUNTOS ››› PODEMOS MAIS!" + logo branco; @_LEONARDOPINTO no topo.
8. **Situação:** textos de parceria com a Prefeitura, nada de cobrança nem problema; opções de enquete só positivas. Sem número de urna, sem "pré-candidato".

## Aprovados (entregas/)
| # | Peça | Arquivo |
|---|---|---|
| 08 | Banner laranja "Do povo, pro povo." ("super aprovado") | `entregas/BannerLaranja.jpg` |
| 09 | Banner azul (logo central) | `entregas/BannerAzul.jpg` |
| 10 | Avatar e capas de destaque | `entregas/Destaques.jpg` |
| 11 | Mockup de 3 posts inclinados | `entregas/PostFeed.jpg` |
| 13 | Post #tôcom Leo Pinto (foto na borda) | `entregas/Post2TocomLeo.jpg` |
| 14 | Post Presente nos povoados (disco) | `entregas/Post3Presente.jpg` |
| 15 | Post Juntos somos + fortes (disco) | `entregas/Post4Juntos.jpg` |
| 17 | Post "Fazer política é cuidar de gente." | `entregas/Post6Frase.jpg` |
| 21 | Post Pergunte ao vereador (disco + cartão) | `entregas/Post10Pergunte.jpg` |
| 22 | Post Enquete (festas do povoado) | `entregas/Post11Enquete.jpg` |
| 23 | Post Projetos aprovados (bloco de anotações) | `entregas/Post12Projetos.jpg` |
| 27 | Figurinha de aniversário para story (Valmissandro), PNG sem fundo | `entregas/27-figurinha-aniversario-valmissandro.png` |
| 28 | Faixa de aniversário para story, PNG sem fundo | `entregas/28-faixa-aniversario-valmissandro.png` |

Pranchas do manual (01 capa, 02 logo, 03 cores, 04 tipografia, 05 fotografia, 06 redes, 07 gabinete) estão em `entregas/` e ainda **não foram avaliadas**.

Campos entre colchetes nos posts (projetos, datas) são de propósito: preencher só com dado real do mandato.

## Reprovados (não repetir)
- **Foto solta com corte lateral aparecendo** e base branca esfumada (posts 12, 15 v1, 19 v1, 20 v1, 21 v1).
- **Foto dentro de arco/moldura alta** (posts 19, 20, 24 Chama no zap, 25 Fique ligado): o arco caiu todas as vezes.
- **"#" gigante repetido como fundo** (12 #Tamo junto) e cartões com muitos campos vazios (16 Mandato, 18 Requerimento, 20 Agenda).
- **Aniversário em post feed** com espaço vazio para a foto do aniversariante (26). Para aniversário de story vale a figurinha/faixa (27/28).
- Primeira versão do canvas: tudo desorganizado e fundos só com cor ("não gosto de fundo duro, só com a cor").

## Fotos
`assets/fotos-v5/`: recortes refinados (borda do cabelo sem franja clara, base cortada reta) a partir de `../identidade-v2/assets/fotos-v4/`. Usar sempre estes.

## Como gerar de novo
Os `.dc.html` em `fonte/` são as pranchas do Claude Design (abrem no canvas). Os geradores em `geradores/` (Python) escrevem os `.dc.html` e uma versão local para render com Playwright; as imagens apontam para os assets do canvas (`/_blob/<id>`), e o mapa id → arquivo local está dentro de cada gerador. Mockups de boné, bandeira e camiseta: prompts em `PROMPTS-MOCKUPS-GEMINI.md` (regra 18/11: cena inteira no Gemini, por cima só o logo vetorial). Pendente.
