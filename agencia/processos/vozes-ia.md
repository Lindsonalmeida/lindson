# Vozes de IA (edge-tts) · ranking e ajustes

Teste de 10/11/2026 (conta Pedro). Mesmo texto para todas, em 3 velocidades (+0%, +4%, +8%):

> "Sabe aquele paciente que chega na clínica e já sai encantado? Na Doutora Jáci Cunha, em Zé Doca, cada detalhe é pensado pra você. E tem novidade: agora a gente atende em Real Taime pelo WhatsApp, inclusive pela bê efe vinte e seis. Me chama agora e garanta o seu horário."

Métricas objetivas (Whisper small em português + silencedetect do ffmpeg): **sim** = semelhança da transcrição com o texto (1 = perfeito); **pausas** = silêncios acima de 0,45 s; **desvio** = irregularidade dos intervalos entre palavras (menor = mais fluido); **ppm** = palavras por minuto. Dados brutos: `CentralLindsonALmeida/dados/agencia/vozes-ia/metricas-teste-2026-11-10.json`. Amostras mp3 (top 5 + Francisca) na mesma pasta.

Observação: o edge-tts hoje só oferece **um** homem nativo do Brasil (Antonio). Donato, Fabio, Humberto, Julio, Nicolau, Valerio e Thiago Multilingual **não existem mais** no serviço. As demais vozes masculinas que falam português são as Multilingual (sotaque ainda estrangeiro de leve, ouvir antes de usar em cliente).

## Referência (aprovada)

| # | Voz | Ajuste | sim | pausas | desvio | ppm | Observação |
|---|---|---|---|---|---|---|---|
| ★ | pt-BR-FranciscaNeural (feminina) | rate +4%, pitch +0Hz | 0,946 | 1 (pontuação) | 0,116 | 167 | APROVADA ("perfeita"). Gerador: `agencia/clientes/jaci-cunha/black-friday/video.py` |

## Masculinas, ranking

| # | Voz | Ajuste | sim | pausas | desvio | ppm | Prós e contras |
|---|---|---|---|---|---|---|---|
| 1 | pt-BR-AntonioNeural | rate +4%, pitch +0Hz | 0,936 | 4 (pontuação, até 0,9 s) | 0,216 | 154 | Único homem com sotaque brasileiro nativo, mesma família da Francisca. Pausa um pouco mais nas vírgulas: usar menos vírgulas no texto. |
| 2 | en-US-AndrewMultilingualNeural | rate +8% | 0,947 | 0 | 0,142 | 151 | Muito fluido e caloroso, acertou "Zé Doca". Leve sotaque estrangeiro; em +4% às vezes falha a conexão (repetir). |
| 3 | en-AU-WilliamMultilingualNeural | rate +4% | 0,946 | 0 | 0,145 | 161 | Fluido, sem pausas longas. Sotaque leve. |
| 4 | it-IT-GiuseppeMultilingualNeural | rate +4% | 0,946 | 0 | 0,144 | 160 | Fluido; timbre mais grave. Sotaque leve. |
| 5 | en-US-BrianMultilingualNeural | rate +8% | 0,946 | 1 | 0,168 | 151 | Conversacional, casual. Em +0% pausa demais. |
| 6 | de-DE-FlorianMultilingualNeural | rate +8% | 0,935 | 0 | 0,151 | 174 | Ok; em +0/+4% leu "real o time". |
| 7 | fr-FR-RemyMultilingualNeural | rate +8% | 0,946 | 0 | 0,143 | 172 | Em +0/+4% errou "Real Taime"; confiança mais baixa. |
| 8 | pt-PT-DuarteNeural | rate +4% | 0,936 | 4 (até 1 s) | 0,231 | 175 | Sotaque de Portugal ("atenda", "para"): não usar para cliente do Brasil. |

## Dicas fonéticas (texto da voz)

- **Jaci:** "Jáci" sai como "já se" no Antonio e no Andrew; para homens, testar "Jássi Cunha".
- **Zé Doca:** escrever "Zé Doca" (separado). Se emendar, "Zé, Dóca".
- **Real time:** escrever "Real Taime" (Florian e Remy só acertam a +8%).
- **BF26:** "bê efe vinte e seis"; **CRO-MA:** "cê erre ó, Maranhão".
- Gerar em blocos de até ~220 caracteres; Multilingual às vezes devolve erro de conexão: repetir a chamada.

## Comando

```bash
SSL_CERT_FILE=/root/.ccr/ca-bundle.crt python -m edge_tts --proxy "$HTTPS_PROXY" \
  -v pt-BR-AntonioNeural --rate=+4% --pitch=+0Hz -f texto.txt --write-media voz.mp3
```

## Aprovadas pelo Lindson (10/11/2026)
- Feminina: Francisca (+4%).
- Masculinas: **04 Giuseppe Multilingual (+4%)**, sempre com pronúncia corrigida no texto, e **01 Antonio (+4%)**.

## Atualização 10/11/2026 (conta Leandro) · Giuseppe REPROVADO, usar voz nativa pt-BR
- **Giuseppe Multilingual reprovado** pelo Lindson em 10/11 ("as pronúncias estão erradas"). O padrão masculino passa a ser o **pt-BR-AntonioNeural +4%**, sem pitch e sem eco.
- **Teste de vozes masculinas grátis** (mesma frase, Whisper small pt; amostras em `agencia/clientes/wf-celulares/motion-02/vozes-teste/`):

| Voz | sim | pausas | Observação |
|---|---|---|---|
| **pt-BR-AntonioNeural +4% (edge-tts)** | **0,976** | 5 (pontuação) | ESCOLHIDA: nativo, acerta modelo, número e preço |
| Piper pt_BR faber medium (local, CPU) | 0,894 | 0 | fluido, mas soa robótico e tropeça em "seminovo" |
| Piper pt_BR edresson low (local, CPU) | 0,847 | 0 | errou "laudo" ("quando audo") |
| gTTS pt-BR (referência) | 0,930 | 3 | voz feminina do Google, só como referência |
| Coqui XTTS v2 / Kokoro (pm_alex) | não testados | | exigem torch e GB de download (rede ~350 KB/s) |

- **Grafia que funcionou no Antonio** (conferida no Whisper, sim ≥ 0,93):

| Termo | Escrever | Observação |
|---|---|---|
| WF | "dábliu éfe" | o Whisper devolve "WF" |
| iPhone | "iPhone" | normal |
| Pro Max | "Pro Max" | no 17 sai "Pro Mac": usar "Pro Max, cor silver" |
| GB | "gigas" | |
| preços | por extenso ("dois mil seiscentos e noventa e nove reais") | |
| laudo | "E com laudo." (frase curta) | "com laudo" e "com o laudo" no meio da frase saem "com o Aldo" / "um áudio" |
| seminovo | "seminovo" | "semi-novo" sai "ser um novo" |
| loja | "Uma loja de iPhone," | depois de "a", sai "moja" |
| premium | evitar ("prêmio"); usar "de luxo" | |
| titânio | "cor de titânio" | "em titânio" sai "entitrâneo" |
- **Conferência automática:** `agencia/clientes/wf-celulares/motion-02/voz.py` (gera, transcreve, compara e tenta alternativas).
