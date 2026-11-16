# Hero shot v1 · Real Time (conta Zuleide, 16/11/2026)
Teste de "hero shot" estilo Advantage+ da Meta, feito por código (sem IA de fundo): produto recortado fiel, sobre mesa de set escura,
luz de produto, contra-luz azul da marca (#2E9BFF), sombra de contato, reflexo, vinheta e grão. Layout = Inventário (instagram-v2/serie.html, layout B) em versão escura.
- `cena.py` monta a cena (cenas: mesa, concreto, azul). `peca.html` aplica a identidade. `gerar.js` faz 4:5 e 9:16.
- Outras peças do Inventário: acrescente em `pecas.json` (dados iguais ao array de serie.html + `recorte` e `cena`) e rode `node gerar.js pecas.json`.
- Saída em `saida/`; `folha.jpg` = prévia. Situação: aguardando aprovação.
