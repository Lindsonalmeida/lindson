# Real Time · feed v5, 30 artes (conta Leandro, 16/11/2026)
v3 reprovada (cartões de app) e v4 reprovada ("sem cores, feed morto"). **Modelo = instagram-v2** (luxo da RT): produto real recortado com luz de estúdio, fundos alternados (preto, gelo, foto colorida, azul vivo), manchete Geist com 2ª linha cinza, palavra gigante, callouts finos, botão azul.
- Fotos reais da RT (`../instagram-v3/fotos/`), recortadas por chroma key + rembg (`recortar.py` → `recortes/`), uma por post; fundos desfocados em `fundos/`.
- Composições K1–K6 copiadas da v2 (refs em `../instagram-v2/TEMPLATE.md` e `TEMPLATE.md`). Inventário e legendas iguais à v3.
- Gerar: `for i in $(seq 1 30); do node gerar.js $i; done` (um por processo) → `artes/rt-v5-post-NN.jpg`; `python3 grid.py` → `previa-grid.jpg`.
Situação: aguardando aprovação.
