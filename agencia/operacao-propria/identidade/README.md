# Orégano Turbo · identidade visual (conta Leandro, 05/11/2026)

**v2 premium (atual):** `gerar2.py` → `node render2.js` → `pecas-v2/`
- **Prancha da marca (5 páginas 4:5):** capa, sistema (selo, nome, personagem), cores e letras, personagem, aplicações.
- **Instagram:** `v2-avatar.png` (foto de perfil), 6 capas de destaque (`v2-destaque-*`) e 1 post de exemplo.

**O sistema:**
- **Selo:** nome em volta (DM Sans 700) e a folha de orégano com óculos de corrida no centro, em traço único.
- **Nome:** "orégano turbo" em Fraunces Black minúscula, eixos SOFT 100 e WONK 1.
- **Cores:** verde forno #13452B (45%) · amarelo turbo #F6C343 (35%) · creme massa #F4EBD9 (15%) · tomate #D9432B (5%).
- **Textos:** DM Sans.
- **Regra das cores:** sempre duas cores por peça, uma sobre a outra.

**v1 (substituída):** `mascote.py` + `gerar.py` → `pecas/`. Mascote cartum colorido; o Lindson pediu "algo premium".

**Também nesta pasta:** pesquisa em `TEMPLATE.md`, brief em `BRIEF.md`, prompt do Claude Design em `PROMPT-CLAUDE-DESIGN.md`.

**Entregue em 05/11:**
- `oregano-turbo-manual-de-marca.pdf` (8 páginas, de `manual.py` + `manual-pdf.js`). Fica no privado `CentralLindsonALmeida/dados/agencia/oregano-turbo/`, porque o GitHub deste repositório recusa arquivos grandes;
- `marca-v2/` com 12 vetores SVG de texto em curvas (de `vetores.py`, com as fontes do Google Fonts);
- `oregano-turbo-identidade-completa.zip` com tudo (montado na hora, fora do Git).

**Falta:**
- aprovação do Lindson;
- os 3 primeiros posts.

## v3 · direção séria (05/11/2026, conta Leandro), a versão atual
- **Pedido do Lindson:** "prefiro coisa mais séria, imagens reais, mockups" e "pense na persona".
- **Gerar:** `python3 gerar3.py && node render3.js` → `pecas-v3/` (11 pranchas).
- **Manual:** `python3 manual3.py && node manual-pdf.js manual3.html oregano-turbo-manual-v3.pdf`. O PDF fica no privado `dados/agencia/oregano-turbo/`.
- **Fotos e créditos:** `fotos-v3/`. **Símbolo em vetor:** `marca-v3/`. **Pesquisa (11 referências, 8 países):** `TEMPLATE.md`, seção v3; capturas em `referencias-v3/`.
- A v1 (mascote) e a v2 (selo lúdico) ficam só como histórico.

## v4 · impacto (06/11/2026, Paollo · conta Leandro, sessão paralela), a versão atual
- **Pedido do Lindson:** "identidade visual aprovada. apenas melhore para ter mais impacto, conexão, visual impactantes, imagens, menos espaços em branco" · "pode parecer uma pizzaria" · "nunca me dê coisas simplistas".
- **O que é:** a v3 aprovada (nome, símbolo, Inter Tight/Inter/IBM Plex Mono, carvão, verde, creme, brasa) **mais** Anton nas manchetes, tomate #D42A1F e açafrão #F2B33D, xadrez de cantina, padrão de 10 ícones em traço, selos redondos e comida recortada saindo da arte.
- **Gerar:** `python3 gerar4.py && node render4.js` → `pecas-v4/` (17 pranchas 1080×1350 + avatar 1080×1080). `SO=v4-08 python3 gerar4.py` gera só uma.
  - 01 capa · 02 logo e versões · 03 logo sobre foto · 04 cores · 05 letras · 06 padrões e selos · 07 fotografia · 08 caixa de pizza (3D em CSS) · 09 camiseta e avental · 10 copo, sacola e adesivo · 11 cartão e proposta · 12 celular (WhatsApp e relatório) · 13 Instagram (perfil e grade) · 14 post "Terça fraca?" · 15 post "PIZZA" · 16 avatar · 17 linguagem de campanha (grade de 4 cores).
- **Recortes:** `python3 recortar4.py fotos-v4/<foto>.jpg` (BiRefNet via rembg, um por processo) → `recortes-v4/*.png`.
- **Manual:** `python3 manual4.py && node manual-pdf.js manual4.html oregano-turbo-manual-v4.pdf` (18 páginas: capa, ficha técnica no estilo Colletivo, 16 pranchas, créditos). O HTML e o PDF ficam fora do Git (`.gitignore`); o PDF vai para o privado `dados/agencia/oregano-turbo/`.
- **Pesquisa e decisões:** `TEMPLATE.md`, seção v4; capturas novas em `referencias-v4/`.
- **Situação:** aguardando aprovação do Lindson.
