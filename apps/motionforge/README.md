# MotionForge · painel de IA para After Effects (conta Leandro, 18/11/2026)
Recebido do Lindson como zip (MVP). Extensão CEP 11 para AE 2022+: remover fundo (rembg local), animar imagem (image-to-video via fal.ai) e gerar imagem (Flux), importando o resultado na composição ativa.
- Código: `com.motionforge.panel/` · Especificação completa: `com.motionforge.panel/SPEC.md` · Instalação: `com.motionforge.panel/README.md`.
- Estado: MVP com 245 linhas (main.js, providers/fal.js, jsx/host.jsx, python/remove_bg.py). Faltam: CSInterface.js, settings.js, bgremove.js, providers Replicate e ComfyUI, aba Histórico, cancelar, custo, fundo em vídeo (fase 2) e empacotar .zxp.
- Chave do fal.ai: o usuário cola na aba Config (nunca no repositório).
- Sessão dedicada criada em 18/11/2026 para desenvolver só isso.
