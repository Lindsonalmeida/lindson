# ElevenLabs por dentro: engenharia reversa por fontes públicas (conta Pedro, 03/11/2026)

> Pedido do Lindson (03/11): engenharia reversa da ElevenLabs para criar o nosso app de clone de voz.
> Só informação pública. O site elevenlabs.io não abriu na rede desta sessão, então os dados oficiais vieram de trechos de busca das páginas da empresa e de análises de terceiros.
> **[oficial]** = página da ElevenLabs · **[terceiro]** = outra fonte · **[INFERÊNCIA]** = dedução nossa. Preços mudam: confira em elevenlabs.io/pricing.

## 1. Produtos

| Produto | O que faz | Fonte |
|---|---|---|
| **Eleven v4 / v4 Turbo** (28/09/2026) | Modelo mais novo: tags de emoção, diálogo com várias vozes, clone com cerca de 10 s, 90+ idiomas; Turbo com cerca de 100 a 150 ms | [blog v4](https://elevenlabs.io/blog/eleven-v4), [Unite.AI](https://www.unite.ai/elevenlabs-launches-eleven-v4-with-low-latency-turbo-variant/) |
| Eleven v3 | Expressivo, com tags de áudio; 70+ idiomas, 5.000 caracteres por pedido | [modelos](https://elevenlabs.io/docs/overview/models) |
| Multilingual v2 | Locução e audiolivro, estável; 29 idiomas | [ajuda](https://elevenlabs.io/docs/help-center/technical/what-models-do-you-offer-and-what-is-the-difference-between-them) |
| Flash v2.5 | Menos de 75 ms, metade do preço | [modelos](https://elevenlabs.io/docs/overview/models) |
| Voice Design | Cria voz a partir de uma descrição (20 a 1.000 caracteres) e gera 3 prévias | [vozes](https://elevenlabs.io/docs/capabilities/voices) |
| Clone instantâneo (IVC) | 1 a 2 min de áudio limpo (v4: cerca de 10 s); a partir do Starter | [IVC](https://elevenlabs.io/docs/eleven-creative/voices/voice-cloning/instant-voice-cloning) |
| Clone profissional (PVC) | Mínimo 30 min, ideal 2 a 3 h; treino de 2 a 6 h; verificação ao vivo da voz | [PVC](https://elevenlabs.io/docs/eleven-creative/voices/voice-cloning/professional-voice-cloning) |
| Voice Library | O dono do clone PVC ganha quando usuários pagantes usam a voz | [payouts](https://elevenlabs.io/docs/eleven-creative/voices/payouts) |
| Speech-to-Speech | Troca a voz de uma gravação mantendo ritmo e emoção | [modelos](https://elevenlabs.io/docs/overview/models) |
| Dubbing | 90+ idiomas; editor manual só no V1 (29 idiomas); cerca de US$ 0,33/min | [dubbing](https://elevenlabs.io/docs/eleven-creative/products/dubbing.md) |
| Scribe v2 | Fala para texto, cerca de US$ 0,22 a 0,39 por hora; tempo real com cerca de 150 ms | [realtime](https://elevenlabs.io/realtime-speech-to-text) |
| Sound Effects v2 | Efeitos de 0,5 a 30 s, com loop | [API](https://elevenlabs.io/docs/api-reference/text-to-sound-effects/convert.md) |
| Eleven Music | Música licenciada (Merlin, Kobalt) | [Business Wire](https://www.businesswire.com/news/home/20250805333301/en) |
| ElevenAgents | Agente de voz (STT + LLM + voz), cerca de US$ 0,08/min mais o LLM | [getmacha](https://www.getmacha.com/blog/elevenlabs-agents-pricing-explained) |
| Studio | Editor de áudio longo e audiolivro | [ElevenReader](https://elevenreader.io/blog/authors-guide-ai-audiobooks) |
| Voice Isolator | Tira ruído e música; cerca de US$ 0,12/min | [preços API](https://elevenlabs.io/pricing/api) |

## 2. Como funciona por dentro

- A empresa **não publica artigos** nem tamanho dos modelos. Do v4 diz só: "arquitetura totalmente nova", entende o contexto da cena e tem "novo método de capturar a identidade do falante".
- **[INFERÊNCIA] Arquitetura provável** (padrão dos sistemas abertos):
  1. um codec neural transforma áudio em tokens ([SoundStream](https://arxiv.org/abs/2107.03312), [EnCodec](https://arxiv.org/abs/2210.13438));
  2. um transformer lê o texto e prevê os tokens, em sequência (como o [VALL-E](https://arxiv.org/abs/2301.02111)) ou de uma vez por flow matching (como o [F5-TTS](https://arxiv.org/abs/2410.06885));
  3. um vetor de identidade do falante, tirado do áudio de referência, permite clonar com poucos segundos.
  Indícios: as tags de emoção funcionam como texto; o v3 "alucina" no modo Creative; Flash e Turbo são versões menores.
- **Tags (v3/v4):** `[whispers]`, `[laughs]`, `[sighs]`, `[excited]` etc. A estabilidade tem 3 posições: Creative (expressivo, pode alucinar), Natural, Robust ([guia de prompting](https://elevenlabs.io/docs/best-practices/prompting)).
- **Controles:** `stability`, `similarity_boost`, `style`, `use_speaker_boost`, `speed` (0,8 a 1,2).
- **Pausas e pronúncia:** `<break time="1.5s"/>` (até 3 s; não funciona no v3/v4); fonemas só no Flash; dicionário de pronúncia .PLS; `apply_text_normalization` escreve números por extenso.
- **PT-BR:** o que mais pesa é usar voz **nativa pt-BR** (clonada ou da biblioteca); voz inglesa falando português sai com sotaque. Escreva números, siglas e datas por extenso.

## 3. API

| Função | Endpoint |
|---|---|
| Texto para fala | `POST /v1/text-to-speech/{voice_id}` |
| Streaming | `POST /v1/text-to-speech/{voice_id}/stream` |
| WebSocket | `wss://api.elevenlabs.io/v1/text-to-speech/{voice_id}/stream-input` |
| Vozes | `/v1/voices`, `/v1/voices/{id}/settings` |
| Dublagem | `/v1/dubbing` |
| Efeitos | `/v1/sound-generation` |

Saída em MP3, PCM (16, 24 e 44,1 kHz) ou μ-law. Preço: v3/v4 cerca de US$ 0,08 por mil caracteres; Flash/Turbo US$ 0,04.

## 4. Planos (2026)

Free US$ 0 (10 mil créditos, **sem uso comercial**) · Starter US$ 6 (30 mil, clone instantâneo) · Creator US$ 22 (121 mil, clone profissional) · Pro US$ 99 · Scale US$ 299 · Business US$ 990. Para YouTube monetizado: plano pago ativo **no momento em que o áudio é gerado** ([ajuda](https://elevenlabs.io/docs/help-center/legal/can-i-publish-the-content-i-generate-on-the-platform.md)).

## 5. Consentimento e segurança (regras que vamos copiar)

- Clonar voz de outra pessoa sem permissão é proibido (suspensão e denúncia).
- Clone profissional exige verificação ao vivo de que a voz é de quem envia.
- "No-go voices": bloqueio de vozes parecidas com as de figuras públicas, sobretudo políticos ([ajuda](https://elevenlabs.io/docs/help-center/legal/what-are-no-go-voices.md)).
- Marca d'água invisível SynthID desde jun/2026 e Audio Detector ([SynthID](https://elevenlabs.io/blog/synthid)).
- **[INFERÊNCIA] Canais:** usar voz de IA com transparência e marcar "conteúdo alterado ou sintético" no YouTube quando for realista.

## 6. Como soar humano (e não cair em "conteúdo inautêntico")

- **Sinais de IA:** ritmo igual, mesma entonação no fim das frases, ênfase errada, número lido errado, emoção constante, voz popular da biblioteca, pausas iguais, emendas de blocos picados.
- **Boas práticas:**
  1. Escrever para falar: frases curtas e médias alternadas, perguntas no meio.
  2. Pontuar com moderação (vírgula = pausa; travessão = corte; reticências = hesitação).
  3. Usar poucas tags de emoção.
  4. Escrever números por extenso e manter um dicionário de pronúncia.
  5. Gerar 2 ou 3 versões e escolher, em blocos de parágrafo.
  6. Usar voz própria ou pouco usada.
  7. Na edição: respiração, música baixa e cortes.
- A regra do YouTube (15/07/2025) mira vídeos em massa de um mesmo modelo, não a voz de IA em si ([SEJ](https://searchenginejournal.com/youtube-targets-mass-produced-content-in-monetization-update/550337/)). Nosso `voz_humana.py` já aplica parte disso (variação por frase, pausas e respiração).

## 7. Equivalentes de código aberto (foco em PT-BR)

| Projeto | Uso comercial | PT-BR | Clona | Máquina |
|---|---|---|---|---|
| **Chatterbox Multilingual** (Resemble) | **MIT, sim** (com marca d'água) | Sim (23 idiomas) | Sim, poucos segundos | GPU; CPU lento (Nano para CPU) |
| **Qwen3-TTS** (Alibaba) | **Apache 2.0, sim** | Sim | Sim, sem treino | GPU (0,6B e 1,7B) |
| **Kokoro-82M** | **Apache 2.0, sim** | Sim (pf_dora, pm_alex, pm_santa), um pouco robótico | Não | Roda bem em CPU |
| **OpenVoice V2** | **MIT, sim** | Timbre em qualquer idioma | Sim (transfere timbre) | Leve, CPU |
| **RVC** | MIT | Independe do idioma | Voz para voz (treino com 10 min ou mais) | GPU para treinar; converter em CPU |
| **faster-whisper** (fala para texto) | MIT | Muito bom | — | CPU com int8 |
| **Demucs** (isolar voz) | MIT | — | — | CPU (1,5 a 4 vezes a duração) |
| Stable Audio Open / 3.0 (efeitos e música) | Liberado até US$ 1 mi/ano | — | — | GPU |
| XTTS-v2 | **Não comercial** | Bom | Sim (6 s) | GPU |
| F5-TTS / F5-TTS-pt-br | **Não comercial** | Bom (ajuste pt-BR) | Sim | GPU |
| Fish Speech / OpenAudio S1 | **Não comercial** | Médio | Sim | GPU |
| Spark-TTS, Voxtral, AudioCraft | **Não comercial** | — | — | GPU |
| Orpheus, Dia, Sesame CSM | Abertos, mas **sem PT** | Não | Sim | GPU |

**[INFERÊNCIA] Montagem de uma "ElevenLabs nossa" com uso comercial liberado:**
- Clone com texto: Chatterbox ou Qwen3-TTS.
- Voz pronta em CPU: Kokoro.
- Voz para voz: RVC.
- Transcrição: faster-whisper.
- Isolar voz: Demucs.
- Efeitos e música: Stable Audio Open.

Para uso **interno** (decisão do Lindson em 03/11), os modelos não comerciais com melhor PT-BR (F5-pt-br, XTTS-v2) podem servir de teste. Para entregar a cliente ou monetizar, ficar nos de licença comercial.
