# Conferência das imagens de IA · carrosséis virais v1 (24/11/2026, conta Zuleide)
Situação: **0 aprovadas, 0 descartadas: nada foi gerado.**
- Conector Hugging Face: `dynamic_space` invoke bloqueado ("invoke operation is disabled because gradio=none is set"); FLUX.1-schnell/dev oficiais = HTTP 404.
- API Gradio direta (mcp-tools/FLUX.1-Krea-dev e evalstate/flux1_schnell, Spaces RUNNING em ZeroGPU): fila aceita, resultado `event: error / data: null`. huggingface.co responde "Invalid username or password" = o proxy não injeta credencial HF; ZeroGPU anônimo sem cota.
- Próximo passo: liberar token HF no ambiente ou Lindson gerar no Gemini com `imagens/PROMPTS.md`; depois conferir os 8 critérios aqui.
