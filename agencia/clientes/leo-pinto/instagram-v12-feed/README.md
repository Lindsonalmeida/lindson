# Feed do Instagram · Vereador Leo Pinto (sistema aprovado, 31/10/2026)

Seis posts com **composições diferentes e a mesma assinatura**, para o feed ficar harmônico sem repetir arte (pedido do Lindson).
Prévia da grade: `previa-feed.jpg`. Decisões e histórico em `../identidade/BRIEF.md` (seção "Decisões de arte").

## Assinatura comum (não mudar)
- **Logo principal oficial** (`marca/logo_principal.png`), extraída em vetor do manual (PDF, página 5) por `marca/marca.svg` + `marca/logo.html`; o "• VEREADOR" é recomposto em Montserrat porque no PDF só parte dele está em vetor. Sempre com fumaça marinho atrás, para destacar.
- Faixa de padrão da marca na base (sem bandeirinhas: excluídas da identidade em definitivo).
- Paleta do book, raios atrás da cabeça, título condensado (Anton) + frase manuscrita (Kaushan Script) com traço laranja.
- Fotos reais do álbum, recortadas por IA e posicionadas pelo rosto detectado.

## Composições (uma por post)
1 dividido (amarelo) · 2 palavra gigante (azul) · 3 frase com sol sobre a maré (marinho) · 4 conversa de WhatsApp (azul) · 5 agenda (amarelo) · 6 close "Bom dia" (amarelo→laranja).

## Como gerar de novo
1. Fotos: álbum do Google Fotos do Leo (link com o Lindson). Baixe para uma pasta `album/` (fora do Git: são fotos do cliente) com nomes `f01.jpg`…`f30.jpg`.
2. Recorte e cor da camisa: `python3 recortar.py <album> recortes f23:original f28:amarelo ...` (rembg: `birefnet-portrait` + `u2net_cloth_seg`; cores: amarelo, azul, laranja, marinho, original). Rode uma foto por vez: o processo encerra depois de cada uma neste ambiente.
3. Rostos: o bloco de detecção (Haar `haarcascade_frontalface_default.xml`) grava `rostos.json` com a posição de cada rosto; a função `foto()` usa isso para centralizar e padronizar o tamanho.
4. Artes: `python3 gerar10.py && node render.js v12` (gera `artes.html` e `out/*.png`). Precisa de `recortes/`, `assets/sol.png` (= `marca/sol.png`) e `marca/logo_principal.png` ao lado do script.

Telefone, horários e locais nas artes 4 e 5 são exemplos: trocar pelos dados reais antes de postar.
