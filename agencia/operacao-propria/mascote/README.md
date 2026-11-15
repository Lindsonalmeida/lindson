# Seu Turbo · mascote da Orégano Turbo (conta Pedro, 15/11/2026, aguardando aprovação)

Pedido do Lindson (15/11): "crie um mascote para a Orégano Turbo, vamos usar ele animado em nossos vídeos".
Feito pelo Paollo com o Rocco, revisado pelo Designer gráfico e pelo Social media. Conceito e regras: `CONCEITO.md`. Pesquisa: `TEMPLATE.md`.

## O que tem aqui
| Arquivo | O que é |
|---|---|
| `seu-turbo.svg` | Vetor limpo, cada parte num `<g id="st-...">` (cabeça, olhos com pupila e pálpebra, sobrancelhas, 10 bocas, braços, 4 luvas por mão, corpo, pernas) |
| `rig/seu-turbo.js` | O rig: uma fonte só para SVG, peças, rig ao vivo e vídeo |
| `rig/index.html` | Rig ao vivo: parado (respira e pisca), aceno, aponta, joinha, fala com áudio ou microfone |
| `pecas/png/` | `principal.png` (transparente), `folha.png` (folha de modelo), `expressoes.png`, `poses.png` (transparentes), `reel.png` 1080x1920, `post.png` 1080x1350, `direcoes.png` |
| `demo/seu-turbo-demo.mp4` | Vídeo 9:16 de 12,5 s: voz Antonio +4%, trilha Mixkit, whoosh, impacto, pop, linhas de velocidade, luz vazando, tremor, grão |

## Como posar
```js
const t = SeuTurbo.criar(document.querySelector('svg'));
t.aplicar({ pose: 'aponta', expr: 'confiante', vira: .3, respira: Math.sin(tempo*2.2), piscar: SeuTurbo.piscada(tempo) });
```
- `pose`: neutro, aceno, aponta, joinha, pensando, confiante, apresenta. Ajuste fino: `R: {x, y, curva, mao, giro}` (o pulso vai para x,y e o braço de mangueira dobra sozinho).
- `expr`: neutro, feliz, surpreso, pensando, confiante, piscada. `boca`: repouso, A, E, O, MBP, F, sorriso, uau, hmm, debochado.
- Outros: `x, y, escala, rot, squash` (pouso), `inclina` (cabeça), `vira` (0 = frente, 1 = 3/4).

## Como fazer ele falar um áudio novo
`python3 demo/fazer.py "Seu texto aqui."` gera a voz (Antonio +4%, a aprovada nos Reels), mede volume e chiado quadro a quadro (lip-sync), renderiza os quadros pelo Playwright e mixa trilha + SFX.
Os gestos entram nas palavras de `marcas` (no `fazer.py`): troque as palavras-gatilho para o texto novo.
Com voz já gravada (Dublê, por exemplo): troque `voz.wav` e rode a partir do cálculo de `vol`/`zcr`.

## Exportar para sobrepor no motor de Reels (`../reels/motor/`)
- **Sequência PNG transparente:** `node demo/quadros.js demo/saida/tl.json saida/alfa --alfa` (só o boneco, fundo transparente).
- **WebM com alfa:** `ffmpeg -framerate 30 -i saida/alfa/%05d.png -c:v libvpx-vp9 -pix_fmt yuva420p -b:v 2M seu-turbo.webm`
- **MOV com alfa (ProRes 4444, para CapCut ou Premiere):** `ffmpeg -framerate 30 -i saida/alfa/%05d.png -c:v prores_ks -profile:v 4 -pix_fmt yuva444p10le seu-turbo.mov`
- No motor: o `palco.html` dos Reels é HTML renderizado pelo Playwright, então dá para pôr o `<svg>` e o `seu-turbo.js` direto na cena e chamar `aplicar()` no mesmo `render(t)`, sem vídeo intermediário. Uso sugerido: canto de baixo, 35 a 45% da largura, apontando para o título, e o joinha no CTA.

## Regras de uso
Sem promessa de resultado, sem tom infantil (ver `CONCEITO.md`). Número em peça só marcado "ilustrativo".
