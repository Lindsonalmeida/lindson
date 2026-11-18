# Especificação: Plugin "MotionForge" para After Effects

> Documento para entregar a um dev ou agente de código (ex.: Claude Code). Projeto original, sem nenhum código ou recurso de terceiros.

## 1. Objetivo
Um painel dentro do Adobe After Effects (2022+, Windows e macOS) que:
1. **Remove o fundo** da camada selecionada (imagem ou frame atual).
2. **Anima uma imagem** (pessoa ou produto) via IA de imagem para vídeo.
3. **Gera imagens** a partir de um prompt de texto.
4. **Importa o resultado** automaticamente no projeto e na composição ativa.

## 2. Arquitetura
```
[Painel CEP (HTML/JS)] ──CSInterface──> [ExtendScript (.jsx) no AE]
        │
        └── fetch/HTTP ──> [Provedor de IA]
                            ├─ Opção A: fal.ai / Replicate (nuvem, paga por uso)
                            └─ Opção B: ComfyUI local (http://127.0.0.1:8188)
        └── child_process ──> [rembg local (Python)] (remoção de fundo grátis)
```
- Tecnologia do painel: **Adobe CEP 11** (Node.js habilitado). Usar CEP e não UXP, porque o UXP ainda é limitado no AE.
- Comunicação com o AE: `CSInterface.evalScript()` chamando funções do ExtendScript.

## 3. Estrutura de pastas
```
com.motionforge.panel/
├── CSXS/manifest.xml
├── index.html
├── css/style.css
├── js/
│   ├── CSInterface.js        (biblioteca oficial da Adobe, repositório Adobe-CEP/CEP-Resources)
│   ├── main.js               (lógica da UI)
│   ├── providers/
│   │   ├── fal.js            (cliente fal.ai)
│   │   ├── replicate.js      (cliente Replicate)
│   │   └── comfy.js          (cliente ComfyUI local)
│   ├── bgremove.js           (chama rembg via child_process)
│   └── settings.js           (salva chaves de API e preferências em JSON no userData)
├── jsx/host.jsx              (funções ExtendScript)
└── python/remove_bg.py       (script rembg)
```

## 4. manifest.xml (pontos-chave)
- `ExtensionBundleId`: `com.motionforge.panel`
- Host: `<Host Name="AEFT" Version="[22.0,99.9]"/>`
- `CSXSVersion` 11.0
- `<CEFCommandLine>`: `--enable-nodejs`, `--mixed-context`
- Tipo: `Panel`, tamanho 360x600, menu "MotionForge"
- Em desenvolvimento: ativar `PlayerDebugMode=1` (chave `HKCU\Software\Adobe\CSXS.11` no Windows, `defaults write com.adobe.CSXS.11 PlayerDebugMode 1` no Mac) para rodar sem assinatura.

## 5. Funções ExtendScript (jsx/host.jsx)
| Função | O que faz | Retorno |
|---|---|---|
| `getSelectedLayerInfo()` | Verifica se a comp está ativa e há uma camada selecionada; devolve nome, tipo, caminho do arquivo de origem se for footage | JSON string |
| `exportCurrentFrame(outPath)` | `comp.saveFrameToPng(comp.time, File(outPath))`; aguarda o arquivo existir | `"ok"` ou erro |
| `importToComp(filePath, asNewLayer)` | `app.project.importFile(new ImportOptions(File(path)))`, adiciona à comp ativa acima da camada selecionada, ajusta in-point para `comp.time` | nome da nova camada |
| `replaceLayerSource(filePath)` | Opcional: substitui a source da camada selecionada | `"ok"` |
| `getCompSettings()` | largura, altura, fps, duração | JSON |

Usar `app.beginUndoGroup("MotionForge")` / `endUndoGroup()` em toda alteração.

## 6. Fluxos

### 6.1 Remover fundo
1. UI chama `getSelectedLayerInfo()`.
2. Se a camada for imagem com arquivo, usa o arquivo; senão chama `exportCurrentFrame(tmp/in.png)`.
3. Node roda `python remove_bg.py in.png out.png` (modelo `birefnet-general` ou `u2net`).
4. `importToComp(out.png)`.
- Alternativa na nuvem: endpoint de background removal no fal.ai/Replicate.
- Para vídeo: extrair frames com ffmpeg, rodar rembg em lote, reimportar como sequência PNG com alpha (fase 2).

`remove_bg.py`:
```python
import sys
from rembg import remove, new_session
from PIL import Image
s = new_session(sys.argv[3] if len(sys.argv) > 3 else "birefnet-general")
remove(Image.open(sys.argv[1]), session=s).save(sys.argv[2])
```
Instalação: `pip install rembg[gpu] pillow` (ou `rembg` sem GPU).

### 6.2 Animar imagem (imagem → vídeo)
1. Obter a imagem (igual ao 6.1).
2. Usuário preenche: **prompt de movimento**, duração (5s/10s), proporção (pegar da comp), modelo.
3. Enviar ao provedor:
   - fal.ai: upload da imagem (`fal.storage.upload`), depois `fal.queue.submit(modelId, {image_url, prompt, duration})`, consultar status a cada 3s e baixar o `video.url`.
   - Replicate: `POST /v1/predictions` com `version` e `input`, consultar `GET /v1/predictions/{id}`.
   - ComfyUI: `POST /prompt` com workflow JSON (Wan 2.x I2V), acompanhar via WebSocket `/ws`, baixar de `/view`.
4. Salvar MP4 em `~/MotionForge/outputs/`, depois `importToComp()`.
5. UI mostra barra de progresso, botão cancelar e custo estimado.

Modelos sugeridos (configuráveis numa lista, confirmar IDs atuais na documentação do provedor):
- Kling (image-to-video), Luma Ray, Runway Gen, Wan 2.x I2V (open-source, roda local).

### 6.3 Gerar imagem
- Prompt, negativo, proporção e seed. Modelo Flux (schnell/dev/pro) ou SDXL.
- Resultado PNG é importado. Botão "Animar esta" encadeia com 6.2.

## 7. UI do painel
Abas: **Remover Fundo | Animar | Gerar | Histórico | Config**
- Topo: preview da camada selecionada (thumbnail do frame exportado).
- Animar: textarea de prompt, presets de movimento ("zoom lento", "câmera orbita", "pessoa sorri e acena", "produto gira 360°"), select de duração e modelo, botão **Gerar**.
- Histórico: grid dos arquivos gerados; clique reimporta.
- Config: provedor (fal / Replicate / ComfyUI), chave de API (salva localmente, nunca no código), URL do ComfyUI, caminho do Python, pasta de saída.
- Tema escuro combinando com o AE: ler `CSInterface.getHostEnvironment().appSkinInfo`.

## 8. Tratamento de erros
- Sem comp ou camada selecionada: mensagem clara.
- Chave inválida (401), falta de saldo (402), timeout acima de 10 min: mensagens específicas.
- Retry com backoff em erros de rede (3 tentativas).
- Logs em `~/MotionForge/logs/AAAA-MM-DD.log`.

## 9. Segurança
- Chaves de API salvas em arquivo de config do usuário (fase 2: keychain do SO via `keytar`).
- Não enviar nada além da imagem e do prompt.
- Se um dia vender o plugin: as chaves devem ficar num **backend próprio** (proxy) com login e sistema de créditos, nunca dentro do plugin.

## 10. Empacotamento e distribuição
- Assinar com `ZXPSignCmd` (certificado autoassinado serve para uso interno) e gerar `.zxp`.
- Instalar com ZXP Installer (aescripts) ou Anastasiy's Extension Manager.
- Instalação manual: copiar a pasta para
  - Win: `C:\Program Files (x86)\Common Files\Adobe\CEP\extensions\`
  - Mac: `/Library/Application Support/Adobe/CEP/extensions/`

## 11. Fases
| Fase | Entrega |
|---|---|
| 1 (MVP) | Painel, remoção de fundo local, imagem→vídeo via fal.ai, importação automática |
| 2 | Replicate e ComfyUI, histórico, presets, remoção de fundo em vídeo |
| 3 | Backend com login e créditos (Node/Supabase + Stripe/Mercado Pago), caso vá revender |

## 12. Critérios de aceite do MVP
- [ ] Painel abre em Janela > Extensões > MotionForge no AE 2022+.
- [ ] Selecionar uma camada e clicar em "Remover Fundo" adiciona um PNG com alpha acima dela em menos de 15s (GPU) ou 60s (CPU).
- [ ] "Animar" com prompt gera um MP4 que é importado na comp no tempo atual.
- [ ] Desfazer (Ctrl+Z) remove a camada importada.
- [ ] Erros aparecem na UI sem travar o AE.

## 13. Custos estimados (conferir preços atuais)
- Remoção de fundo local: grátis.
- Imagem→vídeo na nuvem: algo entre centavos e cerca de US$1 por clipe de 5s, dependendo do modelo.
- Local (Wan no ComfyUI): grátis, mas exige GPU com 12 a 24 GB de VRAM.
