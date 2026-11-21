# Fixados Barzakh · pesquisa premium e template (conta Leandro, 21/11/2026)

## Composição copiada
**Mova Street v5 (aprovado 19/11, "ótimo")**: painel único 3240×1440 cortado em 3 posts 1080×1440, frase contínua na base (mesmo tamanho e altura, centralizada em cada post, peso 600, sombra suave), assinatura pequena no alto do post 3.

## Referências (≥ 8, ≥ 3 países) · capturas NÃO salvas nesta rodada (sem navegação); conferir e salvar em `pesquisa/` na próxima
| # | Referência | País | Status | O que levamos |
|---|---|---|---|---|
| 1 | Mova Street v5 (nosso, aprovado) | BR | **escolhida** | painel contínuo + frase na base |
| 2 | ref-03 Lindson "café de luxo" preto e ouro | BR/Pinterest | **escolhida** | kit preto + ouro, mesma luz |
| 3 | Pentagram, aberturas de case (objeto herói centralizado sobre fundo neutro) | EUA/UK | **escolhida** | placa enorme no post do centro |
| 4 | Koto, grids de lançamento de identidade | UK | descartada | cor forte demais para a Barzakh |
| 5 | Studio Mucho, papelaria em luz rasante | Espanha | referência de luz | sombra de janela |
| 6 | Futura (MX), flat lays escuros | México | descartada | flat lay de cima perde a parede contínua |
| 7 | Anagrama, objetos em pedestal de pedra | México | referência | banco de concreto contínuo |
| 8 | Bureau Borsche, aberturas tipográficas | Alemanha | descartada | só texto (regra: nunca só texto) |
| 9 | Manual (SF), papelaria hot stamping | EUA | referência | logo como metal dentro do material |
| 10 | ref-01 MOYA (Lindson) família de objetos | Pinterest | parcial | família de objetos na mesma luz |

## As 3 para mostrar
1. Mova Street v5 (painel contínuo). 2. ref-03 preto e ouro. 3. Pentagram (objeto herói central).

## Técnica (trilho A)
Render 3D Three.js de uma cena só (`gerador/cena.js`): parede e banco de concreto contínuos, placa em arco aprovada, papelaria, caixa com selo Lápis e ecobag. Logo = PNG ouro oficial como textura com mapa de metal (hot stamping); nada colado em foto. Texto e assinatura planos por cima (`compor.py`).
Refazer: `python3 texturas.py && python3 render.py && python3 compor.py && python3 grade.py` (three@0.169 em node_modules do scratchpad; o caminho fica em `render.py`).
