# MotionForge: painel de IA para After Effects (MVP)

Remove fundos localmente, anima imagens (imagem para vídeo) e gera imagens via fal.ai. Os resultados são importados direto na composição ativa.

## Instalação (modo desenvolvedor)
1. **CSInterface.js**: baixe de https://github.com/Adobe-CEP/CEP-Resources/blob/master/CEP_11.x/CSInterface.js e coloque em `js/`.
2. **Ative o modo debug do CEP** (permite extensões sem assinatura):
   - Windows: `reg add HKCU\Software\Adobe\CSXS.11 /v PlayerDebugMode /t REG_SZ /d 1 /f`
   - macOS: `defaults write com.adobe.CSXS.11 PlayerDebugMode 1`
3. **Copie a pasta** `com.motionforge.panel` para:
   - Windows: `C:\Program Files (x86)\Common Files\Adobe\CEP\extensions\`
   - macOS: `~/Library/Application Support/Adobe/CEP/extensions/`
4. **Python + rembg**: `pip install "rembg[gpu]" pillow` (ou `rembg[cpu]`).
5. Reinicie o AE e abra **Janela > Extensões > MotionForge**.
6. Na aba **Config**: cole a chave do fal.ai (https://fal.ai/dashboard/keys) e o caminho do Python, depois clique em Salvar.

## Uso
- **Fundo**: selecione uma camada e clique em *Remover fundo*. O PNG com alpha é importado acima dela.
- **Animar**: selecione uma camada, escreva ou escolha um preset e clique em *Animar*. O MP4 é importado no tempo atual.
- **Gerar**: escreva um prompt e clique em *Gerar imagem*.
- Arquivos ficam em `~/MotionForge/outputs`. Ctrl+Z desfaz a importação.

## Trocar o modelo de vídeo
No campo "Modelo" use qualquer ID de image-to-video do fal.ai (Kling, Luma, Wan, MiniMax...). Os parâmetros variam por modelo. Confira a aba **API** de cada um em https://fal.ai/models e ajuste o objeto enviado em `btnAnim` (`main.js`).

## Distribuir (.zxp assinado)
Use o ZXPSignCmd (https://github.com/Adobe-CEP/CEP-Resources/tree/master/ZXPSignCMD):
```
ZXPSignCmd -selfSignedCert BR CE MinhaEmpresa MotionForge senha cert.p12
ZXPSignCmd -sign com.motionforge.panel MotionForge.zxp cert.p12 senha -tsa http://timestamp.digicert.com
```
Instale com o ZXP Installer (https://aescripts.com/learn/zxp-installer/).

## Referências
- CEP Cookbook: https://github.com/Adobe-CEP/CEP-Resources/blob/master/CEP_11.x/Documentation/CEP%2011.1%20HTML%20Extension%20Cookbook.md
- Exemplos CEP: https://github.com/Adobe-CEP/Samples
- AE Scripting Guide: https://ae-scripting.docsforadobe.dev/
- fal.ai Queue API: https://docs.fal.ai/model-endpoints/queue
- rembg: https://github.com/danielgatis/rembg
- ComfyUI (alternativa local, fase 2): https://github.com/comfyanonymous/ComfyUI
- Replicate HTTP API (alternativa, fase 2): https://replicate.com/docs/reference/http
- Bolt CEP (boilerplate moderno, se quiser migrar para React/TS): https://github.com/hyperbrew/bolt-cep

## Próximos passos (fase 2)
- Provedores Replicate e ComfyUI (`js/providers/`)
- Remoção de fundo em vídeo (ffmpeg extrai frames, rembg processa em lote, importação como sequência PNG)
- Aba de histórico, cancelamento e estimativa de custo
