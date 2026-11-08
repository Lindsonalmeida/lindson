# Leva de Reels de 30 s: insumos de produção (08/11/2026)

Este arquivo cobre a produção. A estratégia e os roteiros estão em `ESTRATEGIA.md` e `roteiros.json`; o motor está em `motor/README.md`.

## 1. Fotos do Lindson

**Onde estão:** as originais de estúdio (c00 a c16, subidas pela aba Minhas fotos) ficam no KV da Central e não estão no Git. Neste ambiente só existem as cópias do repositório privado `CentralLindsonALmeida`:
- `membros/img/c07` a `c16`: retratos de estúdio coloridos (720×1290; a c16 tem 1143×2048);
- `membros/img/vc-*` e `vf-c12`: closes;
- `site/img/lindson-*`, `bio/lindson-bio.jpg`;
- os recortes das landing pages (`produtos/landing/*/img/hero.png` e `sobre.png`).

Todas são coloridas, com luz âmbar de estúdio e terno escuro. Nenhuma é P&B. A folha de prévia está em `fotos/folha-fotos.jpg`; a pasta `fotos/` fica fora do Git.

**Recortes sem fundo:** foram feitos com BiRefNet portrait, filtro guiado e descontaminação de cor (`agencia/marca-lindson/ferramentas/recorte2.py`). Depois passaram por Real-ESRGAN x2 (`ferramentas/melhorar_foto.py`) no RGB, e o alfa foi ampliado com Lanczos. O recorte da c16 foi conferido a 200% no preto e no amarelo: cabelo e orelhas sem halo.
- `c07-rec2` a `c16-rec2`, `lindson-bio-rec2`, `lindson-contato-rec2`, `bio-que-vende-sobre-rec2`;
- os recortes que já existiam: `c13-rec-site` (herói do site), `kit-whatsapp-hero`, `raio-x-hero`, `kit-mes-pronto-sobre`, `kit-prospeccao-sobre`.

**Regra "foto usada uma vez":** todas essas fotos já foram usadas, nas artes v2, nos pôsteres da área de membros, no site ou nas landing pages. Nesta v1 elas entram **só como rascunho de conferência**. Na versão final, cada Reels usa foto nova ou variação por IA aprovada pelo Lindson. Na v1, a foto aparece na capa e em no máximo uma cena do vídeo (a CTA, em parallax 2.5D). Ela entra com movimento forte, palavra gigante atrás e etiquetas, e nunca como "ele falando" (regra de 03/11).

| Reels | Capa (cor) | Cena com foto no vídeo |
|---|---|---|
| 01 POV perfil | c16-rec2 (amarelo) | c13-rec-site (CTA) |
| 02 Bio que espanta | c07-rec2 (preto) | kit-whatsapp-hero (CTA) |
| 03 Legenda | c08-rec2 (amarelo) | raio-x-hero (CTA) |
| 04 Cliente sumiu | c09-rec2 (preto) | kit-mes-pronto-sobre (CTA) |
| 05 Mito do site | c10-rec2 (amarelo) | kit-prospeccao-sobre (CTA) |
| 06 Tier list | c11-rec2 (preto) | lindson-bio-rec2 (CTA) |
| 07 Link do zap | c12-rec2 (amarelo) | lindson-contato-rec2 (CTA) |
| 08 Semana do cliente | c14-rec2 (preto) | c13-rec2 (CTA) |
| 09 Gancho | c15-rec2 (amarelo) | bio-que-vende-sobre-rec2 (CTA) |
| 10 Desafio 7 dias | c16-rec2 **espelhada** (preto) | c08-rec2 **espelhada** (CTA) |

Repetições dentro da leva: a c16 aparece nas capas 01 e 10 (na 10, espelhada) e a c08 aparece na capa 03 e na CTA da 10 (espelhada). Na versão final, nenhuma foto se repete.

## 2. Motor existente (reaproveitado)

`conteudo/reels/motor/` (`build.py`, `core.js` e os palcos stage, tv, pov, tier, motion, zine, cctv, game e mapa-mental) foi usado nos Reels Tráfego v2 e v3. O processo é este: um JSON de cenas (`say`/`cap`), a voz Kokoro `pm_alex`, um HTML desenhado quadro a quadro pelo Playwright (`render(t)`), os SFX anotados pela cena (`window.SFX`), SFX e música sintetizados em numpy e o resultado juntado no ffmpeg.

O motor v2 (`motor/`) mantém esse esqueleto e troca quatro coisas:
- a voz sai em blocos, com o tempo real de cada palavra;
- entram vídeos de banco e fotos recortadas;
- SFX e trilhas são reais e licenciados, com ducking;
- a capa é gerada no xadrez.

## 3. Vídeos de banco

Estão em `banco/video/`: 15 cortes Mixkit de 5 s, verticais 1080×1920, mudos, com menos de 1,6 MB cada. Os créditos estão em `banco/CREDITOS.md`. Temas: celular na mão (noite, cama, digitando, WhatsApp, página de venda), notificação, negócio local (barbearia, lojista, café), escritório entediado, empresário, empreendedora no notebook e cidade à noite.

Coverr abre nesta rede, mas nada foi baixado de lá. Pexels e Pixabay bloqueiam robô e não foram contornados.

## 4. SFX e trilha

Estão em `banco/sfx/`: 19 sons Mixkit (whoosh, sweep, pop, impacto, riser, swell, click, digitação, glitch, notificação, obturador). O `kit.json` guarda o pico de cada som para o alinhamento.

As trilhas estão em `banco/trilha/`:
- Trap Electro Vibes, 112 BPM;
- Midnight Funk, 117 BPM;
- Pop Track 03, 108 BPM.

Licença Mixkit (sem Content ID).

## 5. Narração

- **Voz clonada (Dublê):** o Chatterbox Multilingual **roda aqui na CPU**. Instalado num venv separado (torch CPU + chatterbox-tts), o `apps/clone-studio/motor_voz.py` gerou 5 s de fala em 69 s, contando ~35 s de carga. Uma narração de 25 s leva ~4 a 5 min. O teste usou uma referência sintética, nunca a voz de outra pessoa. O script já está pronto: `motor/gerar_voz.py`. Ele lê `agencia/marca-lindson/voz/ref.wav` (pasta no `.gitignore`) e renderiza a leva inteira com a voz dele, em blocos de até ~220 caracteres.
- **v1 (esta leva):** voz provisória pt-BR-AntonioNeural (edge-tts), também em blocos, com tempo de cada palavra e pausas encurtadas para ~0,24 s. Os vídeos saem com a etiqueta "RASCUNHO · VOZ PROVISÓRIA" e o nome `-v1-voz-provisoria`.
- **Falta:** o áudio de referência do Lindson. Os 2 áudios de WhatsApp de 02/11 e 19/10 ficaram só na sessão da conta Pedro.

## 6. Lip-sync na CPU (teste)

`motor/lipsync_teste.py` usa o Wav2Lip GAN 96 (ONNX do FaceFusion), com uma foto e um áudio. Gerou 3,7 s em 17 s na CPU, então é **viável em tempo**. A boca abre e fecha no ritmo, mas a qualidade ainda é de rascunho: a boca fica mais mole que o resto do rosto (saída de 96 px) e a cabeça fica parada.

Para virar entrega faltam três coisas:
- restaurar o rosto (GFPGAN/CodeFormer em ONNX);
- dar movimento de cabeça (LivePortrait);
- a voz real dele.

O teste está em `fotos/lipsync-teste-wav2lip-3s.mp4`, fora do Git. Até lá, a regra de 03/11 vale: nada de foto parada "falando".

## 7. Estilos (catálogo `agencia/biblioteca-motion/200-ESTILOS-MOTION-VFX.md`)

- **Base:** #41 tipografia cinética (manchete e legenda palavra por palavra com blur), #25 2.5D/parallax (recorte + palavra gigante + câmera), #28 UI motion (perfil do Instagram, bio riscada, WhatsApp, tier list), #39 neubrutalism (contorno preto, sombra dura, #F5C518).
- **Acabamento:** #35 grão, #152 light leak âmbar, #36 collage (etiquetas no recorte).
- **Transições:** #163 zoom punch, #166 corte no beat (corte puxado para a batida mais próxima), #169 flash nos impactos, #173 split screen (antes × depois, erro × acerto), #176 freeze frame no fecho, #48 faixa de texto em loop na CTA, #103 glitch só no "erro".
