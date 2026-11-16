# Reels 3D v2 · "Cinema 2.5D" (conta Leandro, 16/11/2026)
Substitui as miniaturas 3D (REPROVADAS 16/11: "horríveis"). Visual novo: Lindson recortado com relevo real e câmera de cinema em volta, tipografia 3D extrudada, luz volumétrica, grão e light leak, 3 animações diferentes (ÓRBITA, TÚNEL, CUBO). Pesquisa em `TEMPLATE.md`, roteiros e legendas em `ROTEIROS.md`, pronúncias em `PRONUNCIAS.md`.
- `motor/palco.html` (Three.js) + `motor/gerar.py` (voz 6 Chatterbox com tabela PRON → Whisper fala a fala ≥ 95% → Playwright 30 fps → ffmpeg com trilha Mixkit em ducking + SFX).
- Rodar: `cd motor && python3 gerar.py 01 02 03`. Saída `saida/` (MP4 ≤ 10 MB, cópia no privado `dados/agencia/reels-3d-v2/`), `capas/`, `folhas/`, `whisper/`.
- Trilhas: Mixkit (licença livre Mixkit), créditos na legenda: "Trilha: Mixkit".
