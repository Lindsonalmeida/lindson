# Cenas IA1 a IA5 no Hugging Face · Orégano Turbo (conta Leandro, 24/11/2026)
Para os 3 Reels virais (`../ROTEIROS-VIRAIS-v1.md`, seção "Prompts de vídeo").

## Situação: TRAVADO, 0 de 5 cenas geradas
1. **Conector HF:** `dynamic_space` com `invoke` desligado ("gradio=none" no cabeçalho). Resolver em huggingface.co/settings/mcp: tirar `gradio=none` ou pôr os Spaces liberados.
2. **`evalstate/FLUX.1-Krea-dev`:** o Space está em erro (503, "Your space is in error").
3. **Alternativa testada:** o Space oficial `black-forest-labs/FLUX.1-Krea-dev` (rodando, mesmo modelo) chamado direto pelo `gradio_client`. Recusou: "You have exceeded your ZeroGPU runs limit. Authenticate with a Hugging Face token".
4. **Wan 2.2** (`zerogpu-aoti/wan2-2-fp8da-aoti-faster`) está no ar (parâmetros: input_image por URL, prompt, duration_seconds 3,5 a 5, steps 6). Depende da imagem e da mesma cota.

Para destravar: liberar o invoke no MCP do HF **ou** salvar um token do HF no ambiente (rede/segredo) e rodar `python3 gerar_imagens.py IA1 a` … `IA5 a`.

## Prompts de imagem (FLUX Krea, 720×1280, guidance 4,5, 28 passos), já revisados pelos 8 critérios
Os prompts estão em `gerar_imagens.py`. O que mudou em relação ao roteiro: IA4 virou "cardápio de papel em branco" (o critério 6 proíbe letra falsa), na IA3 a faca fica parada na linha do meio (o vídeo faz o corte) e todos levam "no text, no letters".

## Prompts de movimento (Wan 2.2, 4 s, sutil e cinematográfico)
- IA1: slow push-in, steam rising, flames flickering, peel slides out steadily
- IA2: hands fold the box lid closed, slight handheld sway
- IA3: knife slowly cuts down the middle line, cheese stretches, camera static top-down
- IA4: finger slides slowly down the blank menu, fire flickers in bokeh
- IA5: slice lifts slowly, cheese pull stretches, steam, embers drift

## Conferência (8 critérios)
Nenhuma imagem foi gerada, então não há nada para conferir. Cada imagem deve ser conferida ampliada (mãos, queijo, fogo, letra falsa) antes de ser animada.
