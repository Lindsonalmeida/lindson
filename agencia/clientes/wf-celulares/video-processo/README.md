# Vídeo do processo · WF Celulares (~56 s, vertical) · conta Leandro, 10/11/2026 · aguardando aprovação
- **No Git:** `wf-processo-60s.mp4`, versão comprimida em 720×1280. **Versão cheia (1080×1920, 21 MB):** privado `dados/agencia/wf-celulares/wf-processo-60s.mp4`.
- **Folha de quadros:** `folha-quadros.jpg` (1 quadro a cada 2,5 s).
- **Estilo:** edit-ia-pro nº 5 (Motion explicativo) + nº 9 (Antes e depois). Do catálogo de motion: #163 zoom, #166 corte na batida, #169 flash branco no logo e no CTA, #152 light leak, #35 grão, motion blur (tmix), tremor no logo e no CTA, mockup de celular e a grade do feed montando.
- **Roteiro (7 blocos):** antes → engenharia reversa → logo → laudo → manual → 9 artes → CTA. O texto está em `voz.py`, com "WF" escrito como "dábliu éfe".
- **Voz: PROVISÓRIA.** É a voz masculina APROVADA Giuseppe Multilingual +4% (agencia/processos/vozes-ia.md), em `voz-edge/`. A voz 6 do Lindson (Chatterbox) não pôde rodar porque a rede baixava a 350 KB/s: torch e o modelo somam cerca de 4 GB, mais de 90 min. Para trocar, numa máquina com o Chatterbox: `python3 voz.py` gera `voz/` e depois `python3 montar.py voz`. A referência fica em `agencia/marca-lindson/voz/ref6.wav`, fora do Git.
- **Áudio:** trilha Mixkit #623 (licença Mixkit, sem crédito obrigatório; https://assets.mixkit.co/music/623/623.mp3) com ducking por sidechain. SFX Mixkit: whoosh #1489 nos cortes e impacto #1143 no logo e no CTA.
- **Gerar:** `python3 cenas.py` → `node render.js` (cenas/) → `python3 voz.py edge` → `python3 montar.py voz-edge`.

## Legenda do Reels (10/11, conta Leandro)
REBRANDING DE LOJA DE CELULAR EM SÃO LUÍS: DO LOGO GENÉRICO À MARCA COM PROCEDÊNCIA · O que estava travando · O que eu fiz (engenharia reversa, logo, Laudo WF, manual de 22 páginas, feed de 9 artes) · O resultado · CTA no direct · #rebranding #identidadevisual #lojadecelular #saoluisma #marketingdigital (o texto completo foi enviado ao Lindson na conversa)
