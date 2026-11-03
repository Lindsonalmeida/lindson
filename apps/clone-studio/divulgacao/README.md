# Divulgação do Dublê (conta Pedro, 03/11/2026)

Pedido do Lindson (03/11): "me envie 3 APNGs pra stories apresentando o Dublê, e faça um vídeo de 30 segundos com a minha voz, apresentando, e diga no vídeo que a voz é minha, clonada por você; se puder, minha imagem no cantinho falando, dizendo que sou um clone".

Composição copiada da tela v2 aprovada ("padrão premium", template Sermo, `../identidade/TEMPLATE.md`).

## Stories (`stories/`, 1080×1920)
| Story | Arquivo | O que mostra |
|---|---|---|
| 1 | `duble-story-1-apresentacao` | Halo de voz + "Sua voz, seu rosto. Só com o seu sim." |
| 2 | `duble-story-2-como-funciona` | Console digitando, onda tocando e aviso "Pronto: 9,4 s de voz" |
| 3 | `duble-story-3-so-com-autorizacao` | "Só entra quem autorizou." + termo, vídeo, fonte + selos Liberado/Bloqueado |

- `.png` = APNG animado (10 fps, loop infinito, cerca de 4 MB).
- `.mp4` = versão para postar (o Instagram não aceita APNG nos stories).
- Para refazer: `node grava.js <cena 1-3> <segundos> 30 <pasta>` (quadros de `story.html`) e depois o ffmpeg (APNG com `palettegen`, 128 cores).

## Vídeo de 30 s com a voz clonada do Lindson
- `video.html` + `grava_video.js`: legenda frase a frase, halo que reage à voz e foto dele no cantinho com o selo CLONE. Aviso "Feito com IA" o tempo todo.
- A voz (motor do Dublê, amostra de 4:52), a foto e o MP4 final **não vão para o GitHub**. O vídeo foi entregue ao Lindson na conversa da conta Pedro em 03/11.
- **Boca mexendo (lip-sync):** `lipsync.py` (MuseTalk 1.5 + MediaPipe, sem mmpose) está pronto, mas **não rodou na nuvem**: a segurança da sessão bloqueou a execução de código e modelos baixados de fora. No notebook do Lindson ele roda; ou uma sessão com permissão libera. Por isso o vídeo usa a foto com anel de voz animado.
