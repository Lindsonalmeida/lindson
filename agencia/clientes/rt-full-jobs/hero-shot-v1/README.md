# Hero shot v1 · Real Time (conta Zuleide, 16/11/2026)
Teste de "hero shot" estilo Advantage+ da Meta, feito por código (sem IA de fundo): produto recortado fiel, sobre mesa de set escura,
luz de produto, contra-luz azul da marca (#2E9BFF), sombra de contato, reflexo, vinheta e grão. Layout = Inventário (instagram-v2/serie.html, layout B) em versão escura.
- `cena.py` monta a cena (cenas: mesa, concreto, azul). `peca.html` aplica a identidade. `gerar.js` faz 4:5 e 9:16.
- Outras peças do Inventário: acrescente em `pecas.json` (dados iguais ao array de serie.html + `recorte` e `cena`) e rode `node gerar.js pecas.json`.
- Saída em `saida/`; `folha.jpg` = prévia. Situação: aguardando aprovação.
- **Vídeo (16/11, conta Zuleide):** `video/` — imagem para vídeo por código (Plano B, sem IA: produto 100% fiel). `cena_fundo.py` gera a cena sem produto; `video.html` anima (dolly 1.00→1.08 com parallax, varredura de luz, rim azul pulsando, poeira, grão, textos em fade/slide, REC e timecode, CTA no fim); `node video/render.js 9x16 <pasta>` faz os quadros; ffmpeg junta com trilha Midnight Funk (Mixkit) + SFX. MP4 fora do Git, no painel /painel/rt.
