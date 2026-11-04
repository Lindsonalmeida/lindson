# Leo Pinto · Motion v1 · 4 vídeos de 40 s (conta Pedro, 04/11/2026)

Quatro Reels em motion graphics (1080×1920, 30 fps, 40,0 s, H.264 + AAC 192k 48 kHz com música e efeitos sonoros) feitos tela a tela a partir de `ROTEIROS.md`, na identidade v13 versão 3 (`../instagram-v13-apresentacao/README.md`). Os roteiros ainda **não foram aprovados pelo Lindson**, e "mais bem votado" (vídeo 2, tela 4) ainda precisa ser conferido no TSE 2024.

| Vídeo | Gancho | Fotos do álbum |
|---|---|---|
| V1 | Quem sabe o que falta no seu bairro? | f07 · f11 · f03 |
| V2 | Prazer, eu sou o Leo | f16 · f02 · f30 |
| V3 | A gente não promete. A gente volta pra mostrar. | f04 · f15 (na rua) · f18 |
| V4 | Se você pudesse mudar uma coisa amanhã… | f05 · f19 · f27 (na rua) |

Registro das fotos: `../FOTOS-USADAS.md`. Nenhuma foto se repete entre os 4 vídeos, nem com o feed v12/v13.

## Onde fica cada coisa
- **No Git (aqui):** `engine.html` + `engine.js` (motor), `v1.js` a `v4.js` (lista de telas de cada vídeo), `mapa.js` (contorno oficial de SJB, gerado de `../instagram-v13-apresentacao/mapa-sjb.json`), `render.js` (renderizador), `audio.py` (trilha e efeitos sonoros), `CREDITOS.md` (créditos das músicas), `recortar.py` (recorte de uma foto), `meta.py` (acha o rosto em cada recorte).
- **Fora do Git** (fotos do cliente e vídeos): `CentralLindsonALmeida/dados/clientes-arquivos/leo/motion-v1/`
  - `leo-motion-v1.mp4` … `leo-motion-v4.mp4` e `leo-motion-vN-folha.jpg` (folha de contato: 1 quadro por tela).
  - `assets/recortes/fNN.png` (recortes BiRefNet), `assets/meta.js` (rosto de cada recorte), `assets/logo.png` (logo oficial, `../instagram-v12-feed/marca/logo_principal.png`), `assets/rua.jpg` (rua desfocada, sem bandeirinhas), `assets/fonts/` (Anton, Kaushan Script, Montserrat 600/700/900 do Google Fonts, licença OFL), `assets/modelos/haar_face.xml`.

## Som e VFX (pedido do Lindson, 04/11/2026)
- **Música:** Kevin MacLeod (incompetech.com), CC BY 4.0: V1 Inspired, V2 Wholesome, V3 Feelin Good e V4 Carefree. A linha de crédito de cada vídeo, que vai na legenda, está em `CREDITOS.md`.
- **Efeitos sonoros** sintetizados no `audio.py` (numpy, nada baixado):
  - whoosh em cada whip pan, wipe, zoom-through e mapa;
  - pop em cada palavra e bloco que salta;
  - clique de tecla na máquina de escrever;
  - impacto (boom) em VOCÊ., 2024, TÁ FEITO., nos números 1 a 4 e nas letras A a D;
  - riser antes do cartão final e sino na logo.
- **Deixas geradas dos dados:** `cueList()` no `engine.js` lê o `vN.js` e grava `cues-vN.json`. Nada é marcado à mão.
- **Mixagem:** efeitos de -12 a -18 dB abaixo do pico da música, ducking sob impactos e riser, `loudnorm` a -14 LUFS e pico real de até -1,5 dBTP.
- **VFX** (no `engine.js`, também tirado das deixas):
  - tremor de câmera de 3 quadros em cada impacto;
  - luz quente que vaza em amarelo/laranja, num degradê suave que atravessa a tela nas transições (sem raio nem sol);
  - aberração cromática leve nos whip pans: vermelho e azul se deslocam no eixo do movimento, junto com o desfoque direcional;
  - granulação de 10%.

## Como o motor funciona
- Tudo é **determinístico**: `render(t)` calcula o estado de cada camada a partir do tempo `t` (nenhuma transição CSS, timer ou requestAnimationFrame na animação). O `render.js` chama `render(f/30)` para os 1200 quadros, tira o print do palco e manda os JPEG para o ffmpeg.
- Cada tela (`shots`) tem `t0`/`t1` em segundos, `pre`/`post` (sobreposição nas transições), `cam` (o quadro inteiro: whip pan, zoom, máscara) e `layers`. Cada camada tem trilhas de keyframes `[[t, valor, easing]]`: `x y s sx sy r sk o blur mbx mby clip poly w h l tp rad bg col ls dash fill echoDash zc`.
- Easing real: cúbico, expo, back (estouro 0 → 110 → 100%), bounce. Whip pan com **desfoque direcional** (filtro SVG `feGaussianBlur` só no eixo do movimento). Paralaxe 2.5D com mapa, texto e recorte em camadas que andam em velocidades e escalas diferentes.
- Técnicas: tipografia cinética palavra por palavra, máscara/wipe (`clip-path` inset e polígono diagonal), tela dividida, zoom-through (a câmera atravessa a letra marcada `{O}` e centraliza nela), contador (só 2000 → 2024 e os passos 1 a 4), mapa desenhado (`stroke-dashoffset` e depois o preenchimento), morph de blocos (largura, altura, raio, posição, cor por wipe), máquina de escrever com cursor, logo montando no cartão final.
- Marcação dos textos: `*amarelo*`, `^degradê amarelo→laranja^`, `_laranja_`, `~branco~`, `[royal]`, `§marinho§`. Linhas empilhadas (`blk`) são ajustadas uma a uma à mesma largura, como a frase empilhada da v13.
- Recorte posicionado **pelo rosto** (`face: {cx, cy, w}` em px do palco). A base da foto some num degradê e, se o recorte encosta na lateral da foto original (ombro cortado), essa lateral também some, então a borda cortada nunca aparece. Texto fica na área segura (y 250 a 1600) e nunca em cima do rosto.

## Como gerar de novo
```bash
A=/home/user/centrallindsonalmeida/dados/clientes-arquivos/leo/motion-v1/assets
VENV=<venv com rembg, opencv e imageio_ffmpeg>
# 1. recortes (1 foto por processo, 1 a 2 min cada): BiRefNet portrait, foto reduzida a 2600 px, realce leve de cor
for f in 07 11 03 16 02 30 04 15 18 05 19 27; do $VENV/bin/python recortar.py <album>/f$f.jpg $A/recortes/f$f.png; done
# 2. rostos
$VENV/bin/python meta.py $A
# 3. vídeos (precisa do playwright no node)
export FFMPEG=$($VENV/bin/python -c "import imageio_ffmpeg;print(imageio_ffmpeg.get_ffmpeg_exe())")
node render.js v1 v2 v3 v4 --a $A --out $A/..
# 4. som (músicas em $A/musica; troca o áudio dos MP4 na pasta de saída)
FFMPEG=$FFMPEG python3 audio.py $A/.. v1 v2 v3 v4
# conferir quadros soltos sem gerar o vídeo:
node render.js v2 --a $A --out /tmp/previa --previa 1.5,12.3,38
```
Para abrir no navegador: `engine.html?v=v1&a=<pasta assets>&t=12.5`.

## Créditos das referências (Dribbble, pesquisa da conta Pedro em `REFERENCIAS.md`)
- "Vertical animation built for Reels", Daria Yanovich, dribbble.com/shots/26444363: tipografia cinética vertical, palavra pulando.
- "Debt-Free Justice: Animating political empowerment", Luis Andrey Ramirez Chavarria, dribbble.com/shots/27007672: mapa desenhado com título condensado (Anton) sobre o mapa.
- "FinTech SaaS Kinetic Promo Animation", Moxel Motion, dribbble.com/shots/27724873: frase palavra por palavra com respiro e transições limpas (whip pan, blocos).
- "Kinetic Typography Stories Animation", Serhii Nikonov, dribbble.com/shots/27676379: texto formando forma, ritmo de stories (blocos de letras, máquina de escrever).
