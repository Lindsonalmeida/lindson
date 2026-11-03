# Outras ferramentas de clone de rosto e voz (conta Pedro, 03/11/2026)

> Pedido do Lindson (03/11): "pesquise outras ferramentas de clone que possam contribuir com o melhor desenvolvimento da nossa".
> Só fontes públicas. As páginas oficiais de sync.so, huggingface.co, synthesia.io, d-id.com e hedra.com não abriram na rede desta sessão; os dados vieram de buscas e de terceiros. Preços variam entre as fontes. **[INFERÊNCIA]** = dedução nossa.

## A) Avatar e vídeo comerciais

| Ferramenta | O que faz / ideia para copiar | Preço aprox. | API | Consentimento |
|---|---|---|---|---|
| Synthesia | Avatar pessoal por vídeo ou foto | Creator ~US$ 89/mês; Studio Avatar US$ 1.000/ano ([creatify](https://creatify.ai/blog/synthesia-pricing-(2026)-plans-credits-and-what-you-ll-actually-pay)) | Sim | **Vídeo de consentimento gravado ao vivo, sem upload, mesma pessoa** ([docs](https://docs.synthesia.io/docs/personal-avatars)) |
| D-ID | Foto falante, agentes ao vivo | US$ 29 a 196/mês | Sim, por minuto | Consentimento, marca d'água, moderação |
| Hedra Character-3 | Foto + áudio + texto: **o áudio comanda o rosto, o texto orienta gestos** ([hedra](https://www.hedra.com/models/video/hedra/character-3)) | US$ 20/50/100; API ~US$ 0,011/s | Sim | — |
| Tavus | Réplica com ~2 min de vídeo; treino de 4 a 5 h avisado por callback ([docs](https://docs.tavus.io/sections/replica/overview)) | US$ 39 a 397/mês | Sim | **Frase de consentimento falada dentro do vídeo de treino** |
| Captions / Mirage | Gêmeo de IA e atores para anúncio | US$ 399/mês (Mirage Studio) | Sim | — |
| Argil | Clone com ~2 min + vídeo de consentimento separado | US$ 39/149/499 | Sim | Prova de vida |
| Akool | Avatar, troca de rosto, tradução, ao vivo | US$ 21 a 119 | Sim | Responsabilidade do usuário |
| Colossyan / Vidnoz | Avatar com foto ou 20 s de vídeo; tradução com português | US$ 13 a 88 | Zapier | — |
| Kling Avatar 2.0 | Foto + voz → até 5 min | ~US$ 0,04 a 0,09/s | Sim (revendedores) | — |
| Veo 3.1 | Vídeo com áudio nativo; PT fraco | US$ 0,05 a 0,25/s | Sim | — |
| Runway Act-Two | **Transferência de atuação**: um vídeo de alguém atuando move outro personagem | ~US$ 0,05/s | Sim | — |
| OmniHuman 1.5 | Foto + áudio → corpo inteiro com gestos | ~US$ 0,12 a 0,16/s | Sim | — |
| Sync Labs (lipsync-2-pro, sync-3, react-1) | Lip-sync em vídeo existente, até 4K; react-1 muda a emoção depois de gravado; dublagem em 29 idiomas; `estimateCost` antes de gerar ([sync](https://sync.so/blog/sync-3-most-intelligent-lipsync-model)) | ~US$ 0,07 a 0,08/s | Sim | — |

## B) Voz comerciais

| Ferramenta | Destaque | PT-BR |
|---|---|---|
| Resemble AI | Marca d'água inaudível PerTh que resiste a MP3; consentimento verificável | Via Chatterbox (aberto) |
| **PlayHT** | **Fechou em 2025** (equipe foi para a Meta). Não usar | — |
| Cartesia Sonic-3 | Latência baixíssima, clone com 3 a 10 s | Sim, vozes prontas |
| Fish Audio | Clone com 10 a 30 s; US$ 15 por milhão de bytes | Sim |
| MiniMax Speech 2.6/2.8 | Clone e criar voz por descrição (US$ 3 por voz) | Sim |
| Hume Octave 2 | Fala que "atua" por instrução de emoção; clone com 15 s | Sim |
| Murf Falcon 2 | TTS barato | Não confirmado |

Para narração longa expressiva em PT-BR, os mais promissores são Hume e MiniMax **[INFERÊNCIA]**.

## C) Abertos e locais (base do nosso app)

Tempos por minuto são estimativas **[INFERÊNCIA]**.

### Vídeo e avatar

| Projeto | O que faz | Licença | VRAM | RTX 3060 12 GB / 4090 por 1 min |
|---|---|---|---|---|
| **Duix / HeyGem** ("HeyGen local") | Clona aparência e voz a partir de vídeo, lip-sync, offline, com API ([github](https://github.com/duixcom/Duix.Heygem)) | Comercial grátis até 100 mil usuários ou US$ 10 mi | Recomenda RTX 4070, 32 GB RAM, Docker, mais de 100 GB de disco | 3 a 6 min / 1 a 2 min. **A voz dele não tem português** |
| **MuseTalk 1.5** | Lip-sync em tempo real sobre vídeo | **MIT, inclusive pesos** | 4 GB funciona (lento) | 1 a 3 min / ~1 min |
| **LatentSync 1.5/1.6** | Melhor lip-sync aberto em vídeo existente | Apache-2.0 | 8 GB / 18 GB | 10 a 20 min / 3 a 6 min |
| **LivePortrait** | Foto segue um vídeo de atuação; instalador Windows | MIT, **trocar o detector InsightFace** (não comercial) | ~4 a 6 GB | 2 a 4 min / menos de 1 min. Ótimo para **gravuras** dos canais |
| **EchoMimic V3** | Foto + áudio → meio corpo | Apache-2.0 | 12 a 16 GB | 30 a 60 min / 8 a 15 min |
| **InfiniteTalk / MultiTalk** (Wan2.1-14B) | Dublagem vídeo→vídeo longa ou foto→vídeo, corpo e gestos | Apache-2.0 | Alta (fp8, offload) | 1 a 3 h (480p) / 15 a 30 min |
| Wan 2.2 S2V-14B | Áudio → corpo inteiro | Apache-2.0 | 80 GB oficial; menos com offload | impraticável / 30 a 60 min |
| Hunyuan Video Avatar | Retrato a corpo inteiro com emoção | Licença Tencent (conferir) | 10 GB via Wan2GP | horas / 1 a 2 h |
| LongCat-Video-Avatar 1.5 (mai/2026) | Várias pessoas, vídeo longo | MIT | int8 | — / 20 a 40 min |
| LiveTalking | Avatar ao vivo (WebRTC) | Apache-2.0 | — | tempo real |
| Linly-Talker | Conversa completa (LLM + fala + avatar): inspiração de arquitetura | MIT (componentes variam) | — | — |
| Sonic (Tencent), Wav2Lip | — | **Não comercial: não usar** | — | — |

### Voz

| Projeto | O que faz | Licença | PT-BR | Máquina |
|---|---|---|---|---|
| **VoxCPM2** (abr/2026) | Clone, criar voz por texto, 48 kHz ([github](https://github.com/OpenBMB/VoxCPM)) | **Apache-2.0** | **Sim** (erro de 1,48% em PT) | ~8 GB; 1 min de áudio em 8 a 18 s na 4090 |
| **Qwen3-TTS** | Clone com 3 s, criar voz por descrição | **Apache-2.0** | Sim | 0,6B/1,7B, cabe em 8 GB |
| **Chatterbox Multilingual** | Clone sem treino, com marca d'água PerTh | **MIT** | **Sim, modelo próprio pt-br** | Baixa |
| **Applio (RVC)** | Voz para voz, treino de timbre; instalador `.bat` | MIT | Independe do idioma | Baixa |
| GPT-SoVITS | Fine-tune com 1 min | MIT | **Não** | — |
| OpenVoice V2 | Conversor de timbre | MIT | Não nativo; parado desde 2024 | — |
| AllTalk v2 | Servidor que junta vários motores, com API estilo OpenAI | AGPL-3.0 | Depende do motor | — |
| F5-TTS pt-br, XTTS-v2, IndexTTS | — | **Não comerciais** | — | — |

### Juntadores
- **ComfyUI** com os nós de InfiniteTalk/Wan e o **TTS Audio Suite** (19 motores, RVC, legendas, vozes de personagens) ([github](https://github.com/diodiogod/TTS-Audio-Suite)).
- **Wan2GP**: perfis para pouca VRAM, instaladores `.bat`, TTS embutido ([github](https://github.com/deepbeepmeep/Wan2GP)).
- **Pinokio**: instalador de 1 clique (FaceFusion, LivePortrait).

## D) O que copiar dos comerciais (telas e recursos)

1. Vídeo de consentimento **ao vivo** dentro do app (Synthesia, Tavus, Argil), guardado com o termo assinado. Sem os dois, o app não gera.
2. **Modo político** (vereador): rótulo "conteúdo feito com IA" e bloqueio de conteúdo novo 72 h antes e 24 h depois de cada turno, pela resolução do TSE de 2026 ([barbieri](https://www.barbieriadvogados.com/inteligencia-artificial-nas-eleicoes-2026/)) **[confirmar com advogado]**.
3. Marca d'água inaudível e selo visível (PerTh, já no Chatterbox).
4. Biblioteca de vozes e rostos com etiqueta (Lindson / cliente / personagem), vencimento do termo e quem pode usar.
5. Editor de roteiro com emoção e ritmo, e dicionário de pronúncia (São Luís, nomes de clientes).
6. "Criar voz por descrição" para os narradores dos canais (VoxCPM2, Qwen3).
7. Estimativa de tempo antes de gerar e fila com aviso de pronto.
8. Guia de gravação do vídeo base (2 min, luz, fundo, boca fechada nas pausas).
9. Tradução com lábios num passo só.
10. Ajuste de emoção depois de gravado (react-1) e transferência de atuação (Act-Two) para "interpretar" uma gravura.

Na LGPD, rosto e voz são dado biométrico, ou seja, dado sensível, e pedem consentimento específico (art. 5º II e art. 11) **[confirmar com advogado]**. Ver também `conteudo/referencias/dinheiro-online/riscos-legais-e-regras.md`.
