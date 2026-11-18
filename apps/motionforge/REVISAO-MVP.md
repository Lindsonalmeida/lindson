# Revisão do MVP (245 linhas, recebido em 18/11/2026) · bugs encontrados e correção

| # | Arquivo | Bug | Efeito | Correção |
|---|---|---|---|---|
| 1 | host.jsx | Usava `JSON.stringify`, que **não existe** no ExtendScript do AE | Painel quebrava na primeira chamada ("EvalScript error") | Serializador JSON próprio em ES3 |
| 2 | js/ | Faltava `CSInterface.js` | `new CSInterface()` falhava: painel em branco | Incluído o oficial (CEP-Resources, CEP_11.x, v11.0.0) |
| 3 | main.js | `JSON.parse` direto da resposta do AE | Erro do AE virava "Unexpected token" | `jsxJson()` com mensagem clara |
| 4 | host.jsx | `selectedLayers` lido **depois** de `layers.add` | Camada nova ia para o lugar errado | Índice da camada guardado no início do trabalho (a seleção pode mudar durante a geração) |
| 5 | host.jsx | Fundo removido entrava "ajustado à comp" | Recorte não ficava sobre a foto original (escala/posição/animação perdidas) | Duplica a camada e troca a fonte: mantém transformações, keyframes e efeitos |
| 6 | host.jsx | `saveFrameToPng` exporta a **comp inteira** | Recorte de texto/precomp vinha com as outras camadas | Opção "Exportar só a camada selecionada" (isola e restaura) |
| 7 | main.js | `waitFile` aceitava arquivo ainda sendo gravado | PNG cortado ao meio | Espera o tamanho estabilizar |
| 8 | main.js | Camada com PSD/AI era mandada direto ao rembg | Erro do Pillow | Só PNG/JPG/WebP/TIFF vão direto; o resto exporta o frame |
| 9 | main.js | Python padrão `python3` | No Windows não existe: remoção falhava | Detecta `py`, `python`, `python3` (ou caminho em Config) |
| 10 | fal.js | `fetch` do navegador do CEP | Sujeito a CORS e sem cancelamento | HTTP pelo Node com retry (3x, backoff), timeout e cancelamento |
| 11 | fal.js | Imagem ia como data URI em base64 | Frames 4K passam de vários MB: lento ou recusado | Upload para o storage do fal (`rest.fal.ai/storage/upload/initiate`) |
| 12 | main.js | `duration` e campos fixos para Kling 2.1 | Outros modelos recusavam (422) | Template de entrada por modelo, conferido no schema de cada endpoint |
| 13 | index.html | Modelo padrão `kling-video/v2.1/standard` | Versão antiga | Catálogo atualizado (Kling 3.0, Wan 2.6, Hailuo 2.3, Luma Ray 3.2…) |
| 14 | main.js | Gerar imagem sem comp aberta | Falha "sem comp" depois de pagar a geração | Sem comp, importa só no painel Projeto |
| 15 | main.js | `image_size` = tamanho da comp (ex.: 3840×2160) | Flux recusa ou cobra mais | Lado maior até 1440, múltiplo de 16, mesma proporção |
| 16 | fal.js | Sem cancelar e sem tratar 401/402/422 | Usuário preso esperando; erro técnico em inglês | Cancelar (PUT cancel_url), mensagens em português por tipo de erro |
| 17 | main.js | Sem logs | Impossível dar suporte | `~/MotionForge/logs/AAAA-MM-DD.log`, sem chaves |
| 18 | host.jsx | PNG com alpha podia ser interpretado errado | Borda escura no recorte | `alphaMode = STRAIGHT` |
| 19 | manifest | Sem tamanho mínimo/ícone | Painel espremido | MinSize/MaxSize e ícone |
| 20 | remove_bg.py | Ignorava rotação EXIF; sem modo lote | Foto de celular deitada; vídeo impossível | `exif_transpose`, modo `--batch`, `--check`, `--prep` |
