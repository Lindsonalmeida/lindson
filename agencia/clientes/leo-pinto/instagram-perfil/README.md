# Foto de perfil do Instagram · Vereador Leo Pinto (conta Lindson, 02/11/2026)

Foto escolhida: **leo-23** do álbum (de frente, sorriso aberto, braços cruzados, camisa amarela). Rosto ocupa 25% da largura para ler bem no círculo pequeno.
Identidade: paleta do book v3 (azul royal #2350F5, marinho #05316E, amarelo #FFC20E, laranja #FF7A1A) e raios atrás da cabeça, como no feed v12.

Três versões: **A azul** (recomendada: camisa amarela contrasta com o azul da marca), B marinho com sol atrás da cabeça, C amarela (o amarelo da camisa se mistura com o fundo).
As imagens finais (1080×1080) não vão para o GitHub (foto do cliente): foram entregues ao Lindson na conversa.

## Como gerar de novo
1. Recorte: `python3 ../instagram-v12-feed/recortar.py <album> <pasta> leo-23:original` (precisa de `opencv-python-headless` e `rembg`).
2. Montagem: `python3 montar.py <pasta>` → `perfil-A-azul.jpg`, `perfil-B-marinho.jpg`, `perfil-C-sol.jpg` e `previa-perfil.jpg` (como aparece no Instagram).
