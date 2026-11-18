# MotionForge (extensão CEP 11 para After Effects 2022+)

- Instalar no Windows: `../INSTALAR-WINDOWS.md` (duplo clique em `../tools/INSTALAR.bat`).
- Visão geral, modelos e desenvolvimento: `../README.md`.
- Especificação original: `SPEC.md`.

Instalação manual rápida: ative `PlayerDebugMode=1` em `HKCU\Software\Adobe\CSXS.11` (Windows) ou
`defaults write com.adobe.CSXS.11 PlayerDebugMode 1` (macOS), copie esta pasta para
`%APPDATA%\Adobe\CEP\extensions\` (Windows) ou `~/Library/Application Support/Adobe/CEP/extensions/` (macOS),
instale `pip install "rembg[cpu]" pillow` e reinicie o AE. Abra em Janela › Extensões › MotionForge.
