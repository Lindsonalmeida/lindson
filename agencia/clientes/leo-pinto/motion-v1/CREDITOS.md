# Motion v1 do Leo · créditos das músicas (conta Pedro, 04/11/2026)

As músicas são do Kevin MacLeod (incompetech.com), com licença CC BY 4.0. O crédito é obrigatório: cole a linha do vídeo no fim da legenda do Instagram.

| Vídeo | Linha para a legenda |
|---|---|
| V1 · "Quem sabe o que falta no seu bairro?" | Música: Inspired – Kevin MacLeod (incompetech.com), licença CC BY 4.0 (creativecommons.org/licenses/by/4.0/) |
| V2 · "Prazer, eu sou o Leo" | Música: Wholesome – Kevin MacLeod (incompetech.com), licença CC BY 4.0 (creativecommons.org/licenses/by/4.0/) |
| V3 · "A gente não promete. A gente volta pra mostrar." | Música: Feelin Good – Kevin MacLeod (incompetech.com), licença CC BY 4.0 (creativecommons.org/licenses/by/4.0/) |
| V4 · "Se você pudesse mudar uma coisa amanhã…" | Música: Carefree – Kevin MacLeod (incompetech.com), licença CC BY 4.0 (creativecommons.org/licenses/by/4.0/) |

- **Arquivos das músicas:** ficam fora do Git, em `CentralLindsonALmeida/dados/clientes-arquivos/leo/motion-v1/assets/musica/`. Foram baixados de `https://incompetech.com/music/royalty-free/mp3-royaltyfree/<Título>.mp3`.
- **Mixagem:** os primeiros 40 s de cada música, com fade-in de 0,5 s e fade-out de 1,5 s. A música abaixa sob os impactos (ducking) e o áudio final fica em -14 LUFS, com pico real de até -1,5 dBTP. O script é o `audio.py`.
- **Efeitos sonoros:** whoosh, pop, tecla, impacto, riser e sino. Foram sintetizados no próprio `audio.py` com numpy, então não têm crédito a dar. Eles tocam nas deixas geradas dos dados de cada vídeo (`cues-vN.json`).
