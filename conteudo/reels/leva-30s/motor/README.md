# Motor v2 dos Reels de 30 s do Lindson (08/11/2026)

O motor lê um Reels do `../roteiros.json` (as cenas, a narração em blocos, o texto de tela, a CTA e a `capa_cor`) e a ficha de produção `producao/<id>.json`, e renderiza um vídeo de 1080×1920 a 30 fps, H.264 + AAC, normalizado em -14 LUFS. Gera também a capa no xadrez preto/amarelo e os quadros de conferência.

Ele é a evolução de `conteudo/reels/motor/` (Reels Tráfego v2/v3): mesmo esqueleto de HTML desenhado quadro a quadro pelo Playwright, com os SFX anotados pela própria cena.

## Comandos

```bash
cd conteudo/reels/leva-30s/motor
python3 render_leva.py                 # os 10 com voz provisória -> ../render/NN-slug-v1-voz-provisoria.mp4 + capa + conferência + previa-feed-reels.jpg
python3 render_leva.py L30-04          # só um
python3 reel.py L30-01 --step 15 --saida /tmp/p   # prévia rápida (só quadros), para ajustar a ficha
python3 reel.py L30-01 --capa amarelo,preto       # capas nas duas cores (comparação)
python3 gerar_voz_lindson.py           # gera ../voz/NN-bK.wav com a voz clonada do Lindson (ref.wav fora do Git; ~1,5-2 h na CPU)
python3 render_leva.py --voz lindson   # VERSÃO FINAL: usa ../voz/ -> ../render/NN-slug-v2-voz-lindson.mp4
python3 gerar_voz.py                   # alternativa: gera e renderiza direto pelo motor do Dublê (modo duble)
```

Dependências:
- Python: `pip install edge-tts soundfile scipy librosa pillow numpy`.
- Para os recortes: `rembg[cpu]`, `pymatting` e `opencv-contrib-python-headless`.
- Node com `playwright` global e Chromium em `/opt/pw-browsers/chromium`; outro caminho vai na variável `CHROMIUM=`.
- ffmpeg.

## Arquivos

| Arquivo | O que faz |
|---|---|
| `reel.py` | Faz um Reels inteiro: voz, tempo das cenas pela fala, capa, quadros, mixagem e mp4 |
| `voz.py` | Narração em blocos. Modo `lindson` (lê os blocos já gerados em `../voz/`), modo `provisoria` (edge-tts pt-BR-AntonioNeural, com o tempo de cada palavra e pausa ~0,24 s) ou modo `duble` (voz clonada pelo `apps/clone-studio/motor_voz.py`, Chatterbox) |
| `palco.html` | O palco. Tipos de cena: `banco`, `impacto`, `contador`, `perfil`, `frase`, `lista`, `split`, `chat`, `tier`, `foto`, `cta`. Cuida também de legenda, grão, light leak, flash, glitch, motion blur, zoom punch e shake |
| `capa.html` | Capa 1080×1920 com o miolo 4:5 seguro (y 285–1635). O amarelo segue o modelo aprovado c2y; o preto usa fundo escuro com a foto colorida e o amarelo só no acento |
| `producao/<id>.json` | Ficha de cada Reels: trilha, capa, e para cada cena o tipo, o clipe, a foto, as âncoras (palavra da fala que dispara cada coisa), os impactos, os VFX e os sons |
| `render_leva.py` | Roda a leva e organiza `../render/` (mp4, capa, conferência e prévia do feed) |
| `gerar_voz.py` | Um comando só para refazer tudo com a voz clonada |
| `lipsync_teste.py` | Teste de lip-sync Wav2Lip na CPU (foto + áudio). Ver `../INSUMOS.md` §6 |
| `fontes/` | Anton, Manrope e JetBrains Mono (Google Fonts, OFL), locais para o render não depender da rede |

## Como o tempo funciona

1. A voz sai em blocos (`blocos_voz` do roteiro), com o tempo de cada palavra.
2. As palavras da `narracao` de cada cena são casadas com as da voz (difflib). Cada cena começa 0,16 s antes da primeira palavra dela.
3. **#166 corte no beat:** cada corte é puxado para a batida mais próxima da trilha (librosa), numa janela de -0,15 s a +0,08 s.
4. Antes da cena seguinte à CTA, entra uma pausa de até 1,2 s, para a tela final respirar. O vídeo termina 1,3 s depois da última palavra, com no máximo 30,5 s.
5. Na ficha, tudo o que é "quando" pode ser uma palavra da fala: `hit`, `extraAt`, `badgeAt`, `riscoAt`, `carimboAt`, `cartaoAt`, `tempos_em` e `freeze`.

## Regras aplicadas

- A legenda vai palavra por palavra, com entrada em blur, em y 1395–1540. Fica fora do rosto e das margens do Instagram (topo 250 px, rodapé 380 px). Na cena com foto, a legenda some.
- O @lindsonalmeida_ fica no canto superior direito, em mono branco 60%.
- Os cards de impacto são amarelos #F5C518 com texto preto, e a palavra-chave vai em caixa preta.
- A foto do Lindson nunca aparece "falando": só na CTA, em parallax 2.5D, com palavra gigante atrás, etiquetas (#36) e faixa em loop (#48). Quando existir o lip-sync dele, basta pôr `"lipsync": "<vídeo em ../fotos/>"` na cena CTA da ficha.
- A trilha cai ~18 dB sob a voz (ataque 60 ms, soltura 350 ms). `drop: true` corta a batida antes do impacto.
- O 1º quadro do vídeo é a capa, para servir de miniatura. A capa também sai em jpg para o `cover_url`.

## Estilos (catálogo `agencia/biblioteca-motion/200-ESTILOS-MOTION-VFX.md`)

#41 #25 #28 #39 + #35 #152 #36 + #163 #166 #169 #173 #176 #48 #103 (glitch só no "erro"). Detalhes em `../INSUMOS.md` §7.
