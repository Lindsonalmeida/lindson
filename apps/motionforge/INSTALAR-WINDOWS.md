# Instalar o MotionForge no Windows (passo a passo)

Tempo: uns 10 minutos (e mais o download do modelo de recorte, cerca de 1 GB, que acontece só uma vez).
Requisitos: Windows 10 ou 11 e After Effects 2022 ou mais novo.

---

## Caminho rápido (recomendado)

1. **Baixe a pasta `apps/motionforge`** deste repositório.
   No GitHub: botão verde **Code › Download ZIP**. Extraia e abra `apps\motionforge`.
2. **Feche o After Effects.**
3. Abra a pasta `tools` e dê **dois cliques em `INSTALAR.bat`**.
   O instalador faz tudo sozinho, sem pedir senha de administrador:
   - libera extensões sem assinatura (PlayerDebugMode do CEP);
   - copia o painel para `C:\Users\<você>\AppData\Roaming\Adobe\CEP\extensions\com.motionforge.panel`;
   - instala o Python, se faltar, e o `rembg` (remover fundo, grátis);
   - instala o `ffmpeg`, se faltar (necessário para remover fundo de **vídeo**).

   Se o Windows mostrar "O Windows protegeu o computador", clique em **Mais informações › Executar assim mesmo**.

   Tem placa NVIDIA e quer o recorte mais rápido? Rode no PowerShell, dentro de `tools`:
   ```powershell
   powershell -ExecutionPolicy Bypass -File .\instalar-windows.ps1 -Gpu -BaixarModelo
   ```
   (`-BaixarModelo` já baixa o modelo agora, em vez de no primeiro uso.)
4. **Abra o After Effects** › menu **Janela › Extensões › MotionForge**.
5. No painel, vá à aba **Config**:
   - **Provedor:** fal.ai (padrão).
   - **Chave do fal.ai:** crie em https://fal.ai/dashboard/keys, cole no campo e clique em **Testar chave**.
     A chave fica só no seu computador, em `C:\Users\<você>\MotionForge\config.json`. Nunca vai para o repositório.
   - Clique em **Detectar e testar rembg** e **Testar ffmpeg**: os dois devem ficar verdes.

Pronto. A aba **Fundo** já funciona sem chave (é local e grátis). **Animar** e **Gerar** usam a chave do fal.ai e cobram por uso na sua conta de lá. O custo estimado aparece em cima do botão, antes de gerar.

---

## Como usar

| Aba | O que fazer | O que volta para o AE |
|---|---|---|
| **Fundo** | Selecione a camada (foto, vídeo, texto, precomp) e clique em **Remover fundo**. | Foto: nova camada acima, com as mesmas animações e efeitos, sem fundo. Vídeo: sequência PNG com alpha, alinhada ao trecho usado na comp. |
| **Animar** | Selecione a camada, escreva o movimento (ou toque num preset), escolha duração e modelo, clique em **Animar camada**. | MP4 importado no tempo atual da comp, ajustado ao tamanho dela. |
| **Gerar** | Descreva a imagem, escolha a proporção (Comp = a da composição) e clique em **Gerar imagem**. Depois, **Animar esta** manda a imagem para a aba Animar. | PNG/JPG importado no tempo atual. |
| **Histórico** | Tudo o que foi gerado. Clique para importar de novo. | — |

- **Ctrl+Enter** dispara o botão principal. **Esc** cancela o trabalho em andamento (o pedido no provedor também é cancelado).
- **Ctrl+Z** no AE desfaz a importação de uma vez.
- Arquivos gerados: `C:\Users\<você>\MotionForge\outputs`. Logs (para suporte): `C:\Users\<você>\MotionForge\logs`.

---

## Instalação manual (se preferir não rodar o script)

1. No PowerShell:
   ```powershell
   reg add HKCU\Software\Adobe\CSXS.11 /v PlayerDebugMode /t REG_SZ /d 1 /f
   ```
2. Copie a pasta `com.motionforge.panel` para `%APPDATA%\Adobe\CEP\extensions\` (crie as pastas se não existirem).
3. Instale o Python 3.10+ em https://www.python.org/downloads/ (marque **Add python.exe to PATH**) e rode:
   ```powershell
   py -m pip install "rembg[cpu]" pillow
   ```
4. Para vídeo: `winget install -e --id Gyan.FFmpeg`.
5. Reinicie o After Effects.

---

## Versão assinada (.zxp), para instalar em outros PCs

No Windows, dentro de `apps\motionforge`:
```powershell
powershell -ExecutionPolicy Bypass -File tools\empacotar-zxp.ps1 -Senha "uma-senha-sua"
```
Gera `dist\MotionForge-1.0.0.zxp` (baixa o ZXPSignCmd oficial da Adobe e cria um certificado próprio na primeira vez).
Instale o .zxp com o **ZXP Installer** (https://aescripts.com/learn/zxp-installer/). Guarde o `dist\motionforge-cert.p12` e a senha: as próximas versões precisam do mesmo certificado.

---

## Se algo não funcionar

| Sintoma | Solução |
|---|---|
| O menu **Extensões › MotionForge** não aparece | Rode o `INSTALAR.bat` de novo com o AE fechado. Confira se a pasta está em `%APPDATA%\Adobe\CEP\extensions\com.motionforge.panel`. Em AE 2025/2026, o instalador já liberou CSXS.11 e CSXS.12. |
| Painel abre em branco | Feche e abra o AE. Para ver o erro: com o painel aberto, acesse `http://localhost:8088` no Chrome (depuração do CEP). |
| "Python 3 não encontrado" | Em Config › Python, cole o caminho completo, ex.: `C:\Users\<você>\AppData\Local\Programs\Python\Python312\python.exe`. |
| "O rembg não está instalado" | `py -m pip install "rembg[cpu]" pillow` |
| Primeira remoção demora | Normal: o modelo (cerca de 1 GB) é baixado uma vez. Depois leva segundos (GPU) ou até um minuto (CPU). |
| "ffmpeg não encontrado" | Feche e abra o AE depois de instalar. Ou, em Config › ffmpeg, cole o caminho do `ffmpeg.exe`. |
| "Chave de API inválida" / "Sem saldo" | Confira a chave em fal.ai/dashboard/keys e o saldo em fal.ai/dashboard/billing. |
| "O modelo recusou os parâmetros" | O provedor mudou o modelo. Escolha outro na lista ou ajuste em Config › Modelos extras (ver README). |
