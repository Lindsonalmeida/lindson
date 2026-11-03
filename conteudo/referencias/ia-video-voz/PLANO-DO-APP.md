# Plano do nosso app de clone de imagem e voz (conta Pedro, 03/11/2026)

Junta as três pesquisas desta pasta: `HEYGEN.md`, `ELEVENLABS.md` e `OUTRAS-FERRAMENTAS.md`.

## Decisões do Lindson (03/11)
- **Uso interno** (não é para vender agora).
- **Roda no computador do Lindson.** Este ambiente na nuvem não tem placa de vídeo; o vídeo de avatar precisa de GPU NVIDIA.
- **De quem:** o próprio Lindson; clientes **com termo de autorização** (Leo Pinto, Dra. Jaci e outros); personagens dos canais dark (narradores e figuras em domínio público).
- **PC do Lindson (03/11):** notebook Acer Nitro 5 com **NVIDIA GeForce RTX 3050 Laptop GPU** (normalmente 4 GB de memória de vídeo; confirmar no dxdiag se é 4 ou 6 GB) e Intel UHD integrada. **Nível do app: 4 GB.**
  - Local: voz clonada (Qwen3-TTS 0,6B ou Chatterbox pt-br), Applio/RVC, faster-whisper, MuseTalk 1.5 (devagar) e LivePortrait.
  - Nuvem só quando precisar: LatentSync, EchoMimic, InfiniteTalk (corpo e gestos). Duix/HeyGem não cabe (pede RTX 4070).

## O que o app faz (copiado dos melhores)
1. **Biblioteca:** cada rosto e cada voz com dono, etiqueta (Lindson / cliente / personagem), termo assinado, vídeo de consentimento e data de vencimento. Sem termo e consentimento, não gera.
2. **Clonar voz:** grava ou envia 1 a 2 min de áudio limpo → voz pronta. Opção "criar voz por descrição" para narradores.
3. **Clonar rosto:** guia de gravação de 2 min de vídeo base (luz, fundo, olhar, boca fechada nas pausas).
4. **Gerar vídeo:** roteiro → voz (com o nosso `conteudo/youtube/comum/voz_humana.py` aplicado por cima: pausas, respiração, variação) → boca sincronizada no vídeo base → vídeo final com legenda.
5. **Gravuras vivas** (canais dark): o Lindson atua num vídeo do celular e a gravura copia a expressão (estilo Runway Act-Two). Encaixa no motor Pintura Viva.
6. **Editor de roteiro** com marcas de emoção e pausa e um dicionário de pronúncia.
7. **Fila** com tempo estimado e aviso de pronto.
8. **Proteções:** marca d'água inaudível; selo "feito com IA"; modo político com o bloqueio eleitoral do TSE.

## Pilha por nível de computador (só licenças MIT ou Apache)

| Peça | Placa de 8 GB | Placa de 12 a 16 GB | Placa de 24 GB |
|---|---|---|---|
| Voz clonada PT-BR | VoxCPM2 ou Chatterbox pt-br | + Qwen3-TTS 1.7B | idem |
| Ajuste fino do timbre | Applio (RVC) | idem | idem |
| Transcrição e legenda | faster-whisper | idem | idem |
| Pessoa real falando | vídeo base + MuseTalk 1.5 (rápido) ou LatentSync 1.5 (bonito) | + Duix/HeyGem como base pronta (com outro TTS) | + LatentSync 1.6 |
| Foto falando (meio corpo) | nuvem, só quando precisar | EchoMimic V3 | InfiniteTalk 720p, LongCat Avatar |
| Gravuras vivas | LivePortrait (trocar o detector InsightFace) | idem | idem |
| Corpo e gestos estilo HeyGen | nuvem (Sync ~US$ 0,08/s, Kling ~US$ 0,04 a 0,09/s) | InfiniteTalk 480p à noite | InfiniteTalk / Wan 2.2 S2V |

**Não usar** (licença não comercial ou proibida): Wav2Lip, Sonic, XTTS-v2, F5-TTS pt-br, Fish S1 aberto, IndexTTS e os pesos do InsightFace. Como o uso é interno, podem servir só para comparação de qualidade.

## Etapas
1. Receber do Lindson o modelo da placa de vídeo e a RAM.
2. Montar o protótipo de voz (VoxCPM2 ou Chatterbox + `voz_humana.py`) e testar com 2 min da voz dele, comparando com o edge-tts atual.
3. Montar o protótipo de vídeo (vídeo base + MuseTalk) com 2 min de vídeo dele.
4. Fazer a interface (biblioteca, consentimento, fila), passando pelo Builder Squad, como manda o `CLAUDE.md`.
5. Instalador para Windows (`.bat`), testado no PC dele.
