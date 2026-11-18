# Leo Pinto · identidade v2 · pesquisa premium (conta Pedro, 18/11/2026)

Pedido do Lindson (18/11): "essa identidade dele foi feita quando eu era muito amador... mantenha o que foi feito como logo, mas refaça pra algo premium, marca de luxo". Direções no meio do trabalho: luxo masculino (relógio, alfaiataria, carro), sem nada feminino; e **as mesmas cores do partido** (hex exatos do logo).
Nível de referência: Al Kántara Group v2 (`agencia/marca-holding/v2/`).

## Capturas (16, 8 países) · `referencias/`
| # | Referência | País | Uso |
|---|---|---|---|
| 01 | Obama "Hope" (Shepard Fairey) | EUA | **ESCOLHIDA** · retrato de liderança + 1 palavra (post manchete, outdoor) |
| 02 | Obama 2008 (Sol Sender) | EUA | sol nascendo no horizonte = mesmo símbolo do Leo; reforçou o conceito |
| 03 | Ocasio-Cortez 2018 (Tandem) | EUA | descartada: estética de oposição/insurgência, não serve a quem é situação |
| 04 | Renaissance / En Marche (Macron) | França | monograma sóbrio; usada na capa de Reels (simetria) |
| 05 | Porto. (White Studio) · Behance | Portugal | descartada: sistema de ícones (proibido no Leo) |
| 06 | Pentagram | EUA/UK | grid editorial do manual |
| 07 | Behance · campanha política BR | Brasil | descartada: o "padrão de santinho" (fundo saturado + selo) que queremos superar |
| 08 | Behance · political branding | vários | descartada: degradês e neon |
| 11 | Mayor of London | Reino Unido | tipografia institucional e retas |
| 12 | Lula 2022 | Brasil | descartada: cor de partido em degradê, sem luxo |
| 14 | Collins | EUA | página de sistema e motion |
| 15 | Rolex | Suíça | **ESCOLHIDA** · cor de marca absoluta + serifa romana de autoridade |
| 16 | Tom Ford | EUA | preto + branco, alfaiataria; tom de voz seco e firme |
| 17 | Aston Martin | Reino Unido | **ESCOLHIDA** · preto profundo, linha reta, foto dramática, vinheta |
| 18 | Ralph Lauren (Purple Label) | EUA | retrato em close centralizado (post frase) |
| 19 | Behance · luxury menswear | vários | acabamento de papelaria |

As 3 combinadas: **Obama Hope + Rolex + Aston Martin**. Nossas referências usadas: processo e profundidade do Al Kántara v2; quadros semanais de 18/11 (Zuleide); regras do Leo na MEMORIA (situação, sem grafismo, logo sem balão, povoado, laranja principal).

## Redes v3 (18/11/2026, conta Pedro) · as artes de redes da v2 foram reprovadas ("péssimas")
Diagnóstico da v2: recorte com halo laranja (drop-shadow) e matte borrado; texto pequeno sem hierarquia; Cinzel pequena perdida; grandes áreas de laranja vazio; foto pequena; mesma composição em quase tudo; "VEREADOR" do logo encavalado no texto.
Capturas novas em `referencias/redes-v3/` (8, de 5 países) + as 16 da v2: Labour UK, GQ US, Esquire US, Élysée FR, Casa Rosada AR (Milei), Mayor of London UK, Renaissance FR (Macron), GQ Brasil.
**Escolhidas:** (1) **Labour "Hope Again/Budget in full"** → manchete condensada gigante + bloco de cor + pessoa recortada (post bloco, carrossel 1, Reels); (2) **GQ Men of the Year (US/BR)** → capa de revista, retrato dominante, palavra gigante atrás (post capa, story, quadros); (3) **Renaissance (Macron)** → foto inteira tratada em duotom + legenda grande (post frase, carrossel 3).
Descartadas: Esquire (portal, sem peça social), Élysée e Casa Rosada (institucional frio), London (sem retrato).
Técnica: recortes refeitos com BiRefNet portrait (`assets/fotos-v3/`), sem halo; Barlow Condensed 800 gigante; Cinzel só na frase. Gerador `gerador/redes3.py` → `render_r3.js`; PDF `book3.py` → `render_b3.js` → `entregas/leo-pinto-identidade-v3-redes.pdf`.
