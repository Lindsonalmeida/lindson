# Reels "miniaturas 3D" · nicho do Lindson (conta Leandro, 14/11/2026)

Pedido do Lindson (14/11): "crie 3 roteiros assim pro meu nicho, e vamos criar 3 vídeos nesse mesmo estilo, sempre focando em viralizar".
Base: análise privada `dados/agencia/referencias/explicando-direito-3d/` (fórmula: tema de bolso + data → gancho de pegadinha → 1 objeto por ideia → fonte na tela → conclusão prática → enquete → CTA "comenta PALAVRA").
Visual **próprio** (não copia o deles): mesa preta com aro amarelo e grade fina, bonecos de manequim low-poly, objetos gigantes (celular, relógio, balcão, caixa registradora, moedas, pizza, coração, avião de papel), poeira amarela, HUD série · tema · capítulo, selo de fonte circular girando, número gigante em cartão, legenda palavra por palavra (palavra-chave em caixa amarela), carimbo X / ✓.

- `roteiros.json`: as falas, os objetos, o selo e o CTA de cada Reels (fonte do gerador).
- `ROTEIROS.md`: roteiros, legendas SEO, enquetes e hashtags.
- `motor/palco.html` (Three.js 0.160) + `motor/gerar.py` (edge-tts → Whisper → Playwright quadro a quadro 30 fps → ffmpeg com trilha Mixkit em ducking e SFX).
- `capas/`, `folhas/`, `whisper/` (texto conferido), `saida/` (MP4 ≤ 10 MB).
- Rodar: `cd motor && python3 gerar.py 01 02 03` (≈ 1 Reels por 20 a 30 min em CPU).
- **Voz provisória:** pt-BR-AntonioNeural +4%. A voz 6 (Chatterbox, `leva-30s/motor/gerar_voz_lindson.py`) precisa de torch, que não existe nesta máquina; para trocar, gere os WAV das falas com ela e ponha em `/tmp/mini3d/NN/fK.mp3`.
