# Teste 01 de clonagem de voz (conta Pedro, 03/11/2026)

- **Motor:** Chatterbox Multilingual (Resemble AI, licença MIT, com marca d'água inaudível PerTh), `language_id="pt"`.
- **Amostra de voz:** 10 s gerados com a voz sintética pt-BR-AntonioNeural (`fazref.py`). Nenhuma voz de pessoa real foi usada; a do Lindson entra quando ele gravar os 2 min com consentimento.
- **Resultado:** `clone-voz-teste-01.mp3` (9,4 s).
- **Tempo:** 31 s para carregar e 618 s para gerar, **só com CPU** (4 núcleos, sem placa de vídeo, nesta nuvem). Na RTX 3050 do Lindson a expectativa é de segundos **[INFERÊNCIA, testar]**.
- **Como repetir:** `python -m venv venv && pip install torch torchaudio chatterbox-tts edge-tts`, depois `python fazref.py` e `python teste_voz.py`.
- **Próximo:** passar a saída pelo `conteudo/youtube/comum/voz_humana.py` (pausas, respiração, tratamento de estúdio), comparar com o Qwen3-TTS 0,6B e montar a interface do app.
