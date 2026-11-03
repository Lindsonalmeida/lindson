# HeyGen por dentro: engenharia reversa por fontes públicas (conta Pedro, 03/11/2026)

> Pedido do Lindson (03/11): "engenharia reversa completa do HeyGen e do Eleven Labs", para criar o nosso app de clone de imagem e voz.
> Feita só com informação pública (documentação, API, relatório técnico, preços e análises). Nenhum código fechado foi acessado.
> As páginas `heygen.com`, `developers.heygen.com` e `creatify.ai` não abriram por causa da rede desta sessão, então os dados vieram dos resumos de busca, com o link de cada fonte. Preços e endpoints mudam: confira na página oficial antes de decidir.
> **[INFERÊNCIA]** marca conclusão nossa. **[FABRICANTE]** marca algo divulgado só pelo HeyGen ou por concorrente, sem teste independente.

## 1. O que o produto faz

| Recurso | O que é | Fonte |
|---|---|---|
| Photo Avatar / Avatar IV | Faz 1 foto falar a partir de texto ou áudio: lábios, cabeça, microexpressões e gestos. | [Creatify](https://creatify.ai/blog/aurora-vs-heygen-avatar) |
| Instant Avatar (gêmeo digital) | Clone feito com vídeo do celular. Antes pedia 2 a 5 min; o Avatar V pede cerca de 15 s. | [Help](https://help.heygen.com/en/articles/8389138-instant-avatar-instruction), [MindStudio](https://www.mindstudio.ai/blog/heygen-avatar-5-clone-appearance-15-seconds) |
| Studio Avatar | Clone de alta qualidade gravado em estúdio. | [Guia de gravação](https://help.heygen.com/en/articles/8300578-guidelines-for-video-shooting-high-quality-studio-avatars) |
| Avatar V (abr/2026) | Modelo mais novo: aprende como a pessoa se mexe com um vídeo curto. Em maio/2026 ganhou "Custom Motion". | [Pesquisa](https://www.heygen.com/research/avatar-v-model), [Relatório técnico](https://dynamic.heygen.ai/www/Paper%20Links/avatarv_tech_report.pdf) |
| LiveAvatar | Avatar que conversa ao vivo (WebRTC/LiveKit), produto separado desde 06/11/2025. | [Blog](https://www.heygen.com/blog/liveavatar-by-heygen), [Docs LiveKit](https://docs.heygen.com/docs/streaming-api-integration-with-livekit-v2) |
| Video Translate | Traduz vídeo com a voz clonada e lábios ajustados (diz "175+ línguas e dialetos"). | [Translate](https://www.heygen.com/en-us/translate) |
| Voz | Clonagem própria, ou ElevenLabs/LMNT pela chave de API do usuário. | [Help](https://help.heygen.com/en/articles/8310663-how-to-integrate-elevenlabs-other-third-party-voices) |
| Templates, editor, roteiro com IA | Modelos de cena, também pela API. | [Guia da API](https://www.heygen.com/blog/heygen-api-guide) |
| API, MCP e integrações | API REST, servidor MCP; Canva, Zapier, Make, n8n, HubSpot, Claude etc. | [developers.heygen.com](https://developers.heygen.com), [Integrações](https://www.heygen.com/integrations) |

## 2. Como funciona por dentro

**Caminho do vídeo:**
1. **Texto → voz.** TTS próprio ou de parceiro (ElevenLabs pela chave do usuário). Não há anúncio oficial de que a voz padrão seja da ElevenLabs.
2. **Áudio → movimento e imagem.**
   - **Avatar IV** **[FABRICANTE, via Creatify]**: motor "áudio para expressão inspirado em difusão". Gera primeiro em baixa resolução, depois refina rosto e boca, e um decodificador entrega os quadros em fluxo. Vídeos longos são feitos em pedaços emendados por interpolação.
   - **Avatar V**: Diffusion Transformer com *flow matching*. Lê o vídeo de referência inteiro como tokens, com atenção esparsa. O áudio entra por *cross-attention* e o movimento por "motion injection". Foi ajustado com GRPO e DPO a partir de preferência humana ([pesquisa](https://www.heygen.com/research/avatar-v-model)).
3. **Render.** O Avatar V sai em 1080p a 25 fps e usa **8 GPUs por pedido**. Guarda em cache os tokens da referência e usa uma "âncora de aparência" do primeiro pedaço para o rosto não mudar ([inferência em escala](https://www.heygen.com/en-gb/research/avatar-inference-at-scale)).

**Tipo de modelo:** difusão de vídeo, não NeRF nem Gaussian Splatting. **[INFERÊNCIA]** Os avatares antigos, feitos de gravação, trocavam só a região da boca no vídeo original.

**Material de treino:** Avatar V cerca de 15 s; Instant antigo 2 a 5 min (olhando para a câmera, boa luz, fundo liso); Avatar IV 1 foto. Sempre com vídeo de consentimento.

**Limites:** não publica tempo por minuto (há relato de 23 min do envio à exportação, 18 deles na fila). Creator até 1080p, 4K só no Pro; duração máxima Free 1 min, Creator/Pro 30 min, Business 60 min.

## 3. API (v3 é a atual; v2 ainda serve para templates e Studio)

- `POST /v2/video/generate`: cria o vídeo e devolve o `video_id`.
- `POST /v2/template/{id}/generate`, `GET /v2/templates`, `GET /v2/avatars`, `GET /v2/voices`.
- Tradução: `POST /v3/video-translations`.
- Avatar de foto `POST /v1/avatar/photo`; consentimento em [avatar-consent](https://developers.heygen.com/docs/avatar-consent.md).
- Status: `GET /v3/videos/{video_id}`. Webhooks v3 assinados com HMAC-SHA256.
- **Fluxo:** gerar → `video_id` → webhook (ou consulta de status) → baixar o MP4.
- **Preço:** carteira pré-paga a partir de US$ 5, cobrança por segundo. Avatar IV com foto ≈ US$ 3/min; com gêmeo digital ≈ US$ 4/min; Cinematic US$ 7 por vídeo; criar avatar US$ 1 ([preços](https://developers.heygen.com/docs/pricing.md)).

## 4. Planos (2026; as fontes divergem)

Free US$ 0 (até 1 min, com marca d'água) · Creator US$ 29/mês (1080p, até 30 min) · Pro US$ 49 ou 99/mês (4K) · Business US$ 149/mês + US$ 20 por usuário · Enterprise sob consulta. Os créditos acabam rápido ([preços](https://www.heygen.com/en-gb/pricing), [Creatify](https://creatify.ai/blog/heygen-pricing-(2026)-plans-and-what-you-ll-actually-pay)).

## 5. Consentimento (regra que vamos copiar no nosso app)

- Avatar de outra pessoa sem consentimento explícito é proibido, inclusive de famosos ([moderação](https://www.heygen.com/moderation-policy)).
- **Vídeo de consentimento obrigatório:** a mesma pessoa, com menos de 30 s, lendo "Eu, [nome], autorizo o uso das minhas imagens para criar um avatar". Não vale gravar uma tela tocando o texto.
- Verificação de pessoa viva. Conteúdo político é categoria moderada.

## 6. Fortes, fracos e o que denuncia "cara de IA"

- **Fortes:** realismo, clone com 15 s, tradução com voz clonada, API madura.
- **Fracos:** créditos confusos, fila, moderação, suporte, línguas asiáticas piores.
- **Cara de IA:** lábios fora de sincronia em palavras difíceis, gestos repetidos, "vale da estranheza" em vídeos longos, corpo inventado em avatar de 1 foto, voz certinha demais. **[INFERÊNCIA]** Também denunciam o olhar fixo sem variação, dentes e língua borrados, fundo parado e emendas entre pedaços.

## 7. Equivalentes de código aberto (para o nosso app)

| Parte | Projeto | Uso comercial | Qualidade | Máquina |
|---|---|---|---|---|
| Lábios em vídeo real | **LatentSync 1.5/1.6** (ByteDance) | Apache 2.0, sim | Muito boa; 1.6 em 512 px | GPU 8 GB (1.5) / 18 GB (1.6) |
| Lábios em tempo real | **MuseTalk** (Tencent) | Código MIT; pesos OpenRAIL-M, confirmar | Boa, rosto 256 px | GPU ~6 a 8 GB, ~tempo real |
| Foto + áudio → meio corpo | **EchoMimic V2/V3** | Apache 2.0, sim | Boa | GPU 12 a 16 GB |
| Foto + áudio → vídeo (mais perto do Avatar IV/V) | **InfiniteTalk / MultiTalk / FantasyTalking** (base Wan2.1) | Confirmar | Alta | GPU 24 GB ou mais; com pouca memória fica bem mais lento |
| Foto + áudio (difusão) | **Hallo 2/3** | Hallo3 MIT, mas depende do CogVideoX | Alta, muito lenta | GPU grande |
| Retrato animado por vídeo-guia | **LivePortrait** | MIT, mas o detector InsightFace não é comercial (trocar) | Muito boa | GPU; em CPU é lento |
| Cabeça falante simples | **SadTalker** | Apache 2.0 | Média | GPU 6 a 8 GB |
| Lábios (antigo) | **Wav2Lip** | **Não comercial** | Boca borrada | — |
| Referência fechada | OmniHuman 1.5 | Sem código; só API paga | Topo | — |

**[INFERÊNCIA] Montagem de um "HeyGen nosso":** LatentSync 1.5 sobre um vídeo real gravado da pessoa (fica mais real e mais barato); EchoMimic V3 ou InfiniteTalk para foto falante; MuseTalk para tempo real. Tudo de vídeo precisa de GPU de 8 a 24 GB. **Só com CPU, nenhuma opção de vídeo com boa qualidade é viável.**
