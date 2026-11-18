# Pagode Fiado · Vídeos longos v2 (sessão GOMINHO, conta Pedro, 18/11/2026)

Pedido do Lindson: "gere todos os vídeos longos que faltam do Pagode Fiado". A v1 foi reprovada ("os áudios estão com falha, essas não são as aprovadas"); esta v2 segue os documentos dele no Drive *Pagode Fiado*.

## O que é
- **11 vídeos, um por faixa aprovada** (00 a 10), 16:9 1080p, no formato aprovado "Ao vivo no Bar do Seu Tião", com o título do roteiro do clipe: "Pagode Fiado - <Faixa> (Ao Vivo no Bar do Seu Tião)".
- **Álbum completo** (~38 min, as 11 em sequência, com capítulos): o "vídeo longo de 35 a 40 minutos" da semana +3 do plano.
- O áudio é o mp3 aprovado, **copiado sem recodificar**: nada é somado por cima da música (a falha da v1 era o ruído e as músicas geradas de novo).

## Como é feito (motor próprio)
1. `letras.py` → `letras.json`: letras oficiais (album-01-historia e PROMPT-SUNO-V4-7 do Drive).
2. `transcrever.py`: tempos das palavras de cada faixa (faster-whisper small, com a letra como dica).
3. `alinhar.py`: casa a letra oficial com os tempos (karaokê palavra a palavra; refrões repetidos e linhas que faltaram).
4. `camadas.py` + `render.js`: camadas na identidade (quadro-negro do FIADO na abertura, tira do caderno do fiado com a letra em lápis e caneta azul, polaroide dos personagens, nomes, selo oficial, fecho "Próximo capítulo").
5. `motor.py <faixa> <pasta>`: fotos de referência do Drive (pasta Imagens) com profundidade 3D (Depth Anything V2), câmera lenta, retratos em polaroide (sozinho, dupla e trio da roda), cortes no tempo da música, luz quente vazando, grão e vinheta. Rosto sempre inteiro; marca de cerveja da cadeira apagada.
6. `capas.py`: thumbnail de cada faixa. `publicar.py` → `publicar.json` (título, descrição com a letra, tags). `montar-album.py`: álbum + `album-capitulos.txt`. `painel.sh`: versão 720p do painel.

## Onde estão
- Painel: /painel/canais → Pagode Fiado → Materiais (720p) · originais 1080p e álbum: Drive *Pagode Fiado/Vídeos longos v2*.
- Insumos: privado `dados/agencia/pagode-fiado/` (músicas aprovadas e imagens).

## Limites
- Não há animação de boca nem vídeo gerado (Kling/Runway sem crédito): o movimento vem das fotos em 3D. O clipe animado de "Copo Americano" continua no plano.
