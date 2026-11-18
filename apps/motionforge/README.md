# MotionForge · painel de IA para After Effects (conta Leandro)

Extensão CEP 11 para After Effects 2022+ (Windows e macOS). Três funções, e o resultado entra direto na composição ativa:

1. **Remover fundo** de foto, frame ou **vídeo** (rembg local e grátis, ou nuvem: fal.ai / Replicate).
2. **Animar imagem** (imagem → vídeo) via fal.ai, Replicate ou ComfyUI local.
3. **Gerar imagem** (Flux, SDXL…) e encadear com "Animar esta".

Mais: aba **Histórico**, barra de progresso, **cancelar** (cancela também no provedor), **custo estimado** com o preço da conta do fal.ai, lista de modelos configurável, logs diários, retry com backoff.

- **Instalar no Windows:** [`INSTALAR-WINDOWS.md`](INSTALAR-WINDOWS.md) (duplo clique em `tools/INSTALAR.bat`).
- **Especificação:** `com.motionforge.panel/SPEC.md` · **Bugs do MVP corrigidos:** [`REVISAO-MVP.md`](REVISAO-MVP.md) · **Visual:** [`TEMPLATE.md`](TEMPLATE.md).
- Chaves de API: o usuário cola na aba Config; ficam em `~/MotionForge/config.json` (fora do repositório).

## Estrutura
```
com.motionforge.panel/          ← a extensão (é isto que vai para o .zxp)
  CSXS/manifest.xml             CEP 11, AEFT [22.0,99.9], Node + mixed-context
  index.html · css/style.css    UI (fonte Inter embutida, tema segue o do AE)
  js/CSInterface.js             oficial da Adobe (CEP-Resources, CEP_11.x)
  js/main.js                    só DOM; chama o núcleo
  js/core.js                    fluxos: removeBg, animate, generate, estimate, histórico
  js/settings.js                config/chaves em ~/MotionForge
  js/models.js                  catálogo de modelos + templates de entrada
  js/bgremove.js                rembg (Python) e ffmpeg (vídeo → frames → lote → sequência PNG)
  js/history.js                 ~/MotionForge/history.json
  js/lib/http.js|errors.js|logger.js   HTTP com retry/cancelar, mensagens claras, logs sem chaves
  js/providers/fal.js|replicate.js|comfy.js
  jsx/host.jsx                  ExtendScript (ES3, JSON próprio): info, isolar camada, exportar frame, importar/posicionar
  python/remove_bg.py           imagem, lote (vídeo), diagnóstico, redução para upload
  comfy/*.json                  workflows ComfyUI formato API (Wan 2.1 I2V, SDXL)
  tests/                        testes (não vão para o .zxp)
tools/INSTALAR.bat · instalar-windows.ps1 · empacotar-zxp.ps1 · empacotar-zxp.sh · preview.js
```

## Modelos (conferidos em 18/11/2026)
IDs e parâmetros tirados do catálogo `https://api.fal.ai/v1/models` e do schema de cada endpoint
(`https://fal.ai/api/openapi/queue/openapi.json?endpoint_id=<id>`); Replicate pela aba API de cada modelo.

| Provedor | Imagem → vídeo | Gerar imagem | Fundo |
|---|---|---|---|
| fal.ai | Kling 3.0 Standard, Kling 2.5 Turbo Pro, Kling 4.0, Wan 2.6 Flash, Hailuo 2.3 Fast, Luma Ray 3.2, LTX 2.3 Fast, Seedance 2.0 Fast | FLUX.1 schnell/dev, FLUX 1.1 pro, FLUX 2 pro, SDXL | BiRefNet v2, Bria RMBG 2.0, BiRefNet v2 vídeo (ProRes 4444 com alpha) |
| Replicate | Kling 2.5 Turbo Pro, Hailuo 02, Wan 2.2 I2V Fast | FLUX.1 schnell/dev | Bria Remove Background |
| ComfyUI | Wan 2.1 I2V 480p (workflow incluso) | SDXL (workflow incluso) | — (use o local) |

**Trocar ou acrescentar modelo sem mexer no código:** Config › Modelos extras (JSON). Exemplo:
```json
[{"provider":"fal","kind":"i2v","id":"fal-ai/kling-video/v3/pro/image-to-video","label":"Kling 3.0 Pro","durations":[5,10],
  "input":{"start_image_url":"{{image}}","prompt":"{{prompt}}","duration":"{{duration:str}}","generate_audio":"{{audio}}"}}]
```
Marcadores: `{{image}} {{video}} {{prompt}} {{negative}} {{seed}} {{aspect}} {{size}} {{audio}} {{duration}}` (número), `{{duration:str}}` (texto). Campo vazio é omitido.
`kind`: `i2v`, `t2i`, `bg` (imagem) ou `bgv` (vídeo). Mesmo `id` de um modelo embutido = substitui.

ComfyUI: no ComfyUI, **Workflow › Exportar (API)**, troque os valores por marcadores (`{{image}}`, `{{prompt}}`, `{{seed}}`, `{{width}}`, `{{height}}`, `{{frames}}`) e aponte o arquivo em Config. Saída com vários PNG vira sequência no AE.

## Desenvolvimento
```bash
cd apps/motionforge
npm install          # eslint (só para desenvolvimento)
npm run lint         # JS (ES2020, Node 15/Chromium 88 do CEP 11) e JSX (ES3)
npm test             # 21 testes: providers com servidor simulado, host.jsx num AE simulado, rembg e ffmpeg reais
node tools/preview.js /tmp/ui   # capturas da UI fora do AE (Playwright)
```
Depuração no AE: arquivo `.debug` (porta 8088) → `http://localhost:8088` no Chrome.

## Estado (18/11/2026, conta Leandro)
- Pronto: todas as etapas do SPEC (fases 1 e 2), instalador Windows, empacotador .zxp, testes.
- Testado aqui: rembg real (imagem e lote), ffmpeg real (vídeo → sequência), fluxos fal/Replicate/ComfyUI com servidor simulado, host.jsx num AE simulado, lint.
- **Falta testar no AE de verdade** (não há After Effects neste ambiente): abrir no PC do Lindson e validar os critérios de aceite do SPEC §12.
- Fase 3 (backend com login e créditos para revender) não foi feita, como previsto no SPEC.
