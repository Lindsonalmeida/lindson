// Vídeo 1 · "Quem conhece o seu bairro?" (textos revistos em 04/11: Leo é situação, nada critica a gestão) (ROTEIROS.md, conta Pedro, 04/11/2026)
// Fotos: f07 (close, polo laranja) · f11 (meio corpo, celular na mão) · f03 (close, mão no peito).
(() => {
const { pop, wipe, wipeOut, words, area, blk, inOut } = H_;
const sol = C.sol, lar = C.lar, mar = C.mar, roy = C.roy;
// whip pan para a direita (o conteúdo anda para a esquerda): saída e entrada com a mesma curva
const whipOut = (t, d = .42) => ({ x: [[t, 0], [t + d, -1080, 'ioE']], mbx: [[t, 0], [t + d * .5, 70, 'inQ'], [t + d, 0, 'outQ']] });
const whipIn = (d = .42) => ({ x: [[-d * .75, 1080], [d * .25, 0, 'ioE']], mbx: [[-d * .75, 0], [-d * .25, 70, 'inQ'], [d * .25, 0, 'outQ']] });
window.VIDEO = { id: 'v1', shots: [
// 1 · tipografia cinética
{ n: 1, t0: 0, t1: 3.5, post: .25,
  cam: { s: [[3.15, 1], [3.75, 1.35, 'inC']], o: [[3.3, 1], [3.75, 0, 'inQ']], blur: [[3.3, 0], [3.75, 14, 'inQ']] },
  layers: [ area([
    blk(['QUEM', 'CONHECE'], { max: 190, extra: { parts: words(['QUEM', 'CONHECE'], .15, .22) } }),
    blk(['O SEU', '*BAIRRO?*'], { max: 210, css: { marginTop: '22px' }, extra: { parts: words(['O SEU', 'BAIRRO?'], .75, .2, .4) } }),
  ], { css: { filter: 'drop-shadow(0 18px 30px rgba(2,12,50,.45))' } }) ] },
// 2 · paralaxe 2.5D: mapa atrás, VOCÊ. no meio, Leo na frente
{ n: 2, t0: 3.5, t1: 6.5, post: .7,
  layers: [
    { k: 'map', id: 'v1a', w: 1250, echo: true, stroke: '#BFD8FF', sw: 3, css: { left: '-85px', top: '520px' },
      tr: { o: [[0, 0], [.4, .85, 'outQ']], x: [[0, -50], [3.6, 40, 'lin']], s: [[0, 1.12], [3.6, 1.02, 'lin']] } },
    { cls: 'A', html: 'VOCÊ<span class="y">.</span>', css: { left: '0', width: '1080px', top: '640px', textAlign: 'center', fontSize: '470px', letterSpacing: '.01em' },
      tr: { s: [[.1, 1.6], [.6, 1, 'outE'], [3.6, .95, 'lin']], o: [[.1, 0], [.3, 1, 'lin']], blur: [[.1, 20], [.55, 0, 'outQ']], x: [[0, 30], [3.6, -25, 'lin']] } },
    { k: 'photo', src: 'f07', face: { cx: 640, cy: 1500, w: 430 },
      tr: { y: [[0, 380], [.75, 0, 'outE']], x: [[0, 30], [3.6, -10, 'lin']], s: [[0, 1], [3.6, 1.05, 'lin']], o: [[0, 0], [.2, 1, 'lin']] } },
  ] },
// 3 · tela dividida (azul em cima, laranja embaixo), cada metade num wipe em sentido oposto
{ n: 3, t0: 6.5, t1: 10.5, post: .1,
  layers: [
    { css: { left: 0, top: 0, width: '1080px', height: '960px', background: `linear-gradient(160deg,#1539BE,#0B2A8A 55%,${mar})` }, tr: { clip: wipe('l', 0, .55) } },
    { css: { left: 0, top: '960px', width: '1080px', height: '960px', background: `linear-gradient(200deg,#FF9A22,${lar} 55%,#F05A00)` }, tr: { clip: wipe('r', .2, .55) } },
    area([blk(['CADA RUA.', 'CADA *PRAÇA.*'], { max: 180, extra: { parts: words(['CADA RUA.', 'CADA PRAÇA.'], .45, .16) } })], { y0: 280, y1: 930, css: { filter: 'drop-shadow(0 16px 26px rgba(2,12,50,.4))' } }),
    area([blk(['CADA', '~POVOADO.~'], { max: 200, css: { color: mar }, extra: { parts: words(['CADA', 'POVOADO.'], 1.35, .2) } })], { y0: 990, y1: 1600 }),
  ] },
// 4 · máscara: o texto se revela por trás de um bloco marinho que desliza
{ n: 4, t0: 10.5, t1: 14, bg: BG, post: .3,
  cam: { clip: [[-.1, [0, 0, 0, 100]], [.35, [0, 0, 0, 0], 'ioE']], y: [[3.2, 0], [3.8, -260, 'inC']], o: [[3.4, 1], [3.8, 0, 'inQ']] },
  layers: [
    area([
      blk(['CADA CANTO', 'TEM SUA'], { max: 160, extra: { kids: [{ css: { inset: '-14px -10px', background: mar }, cls: 'box', tr: { x: [[.35, 0], [1.0, 1000, 'ioE']] } }] } }),
      blk(['*HISTÓRIA.*'], { max: 190, css: { marginTop: '26px' }, extra: { kids: [{ css: { inset: '-14px -10px', background: mar }, cls: 'box', tr: { x: [[1.1, 0], [1.75, 1000, 'ioE']] } }] } }),
    ], { css: { overflow: 'visible' } }),
  ] },
// 5 · morph de blocos: o bloco laranja se estica e vira um retângulo branco; o texto pousa em royal
{ n: 5, t0: 14, t1: 17.5, post: .2,
  cam: whipOut(3.3, .42),
  layers: [
    { cls: 'box', css: { left: '480px', top: '900px', width: '120px', height: '120px', background: lar },
      tr: { l: [[0, 480], [.45, 480], [.85, 70, 'ioE']], w: [[0, 120], [.45, 120], [.85, 940, 'ioE']],
            tp: [[0, 900], [.85, 900], [1.25, 610, 'ioE']], h: [[0, 120], [.85, 120], [1.25, 700, 'ioE']],
            s: [[0, 0], [.35, 1, 'outB']], r: [[0, -45], [.45, 0, 'outC']], rad: [[0, 60], [.45, 0, 'outQ']],
            bg: [[.85, lar], [1.25, '#FFFFFF', 'ioQ']] } },
    area([
      blk(['QUEM MORA LÁ'], { w: 800, max: 130, css: { color: roy }, extra: { parts: words(['QUEM MORA LÁ'], 1.15, .13) } }),
      blk(['SABE O QUE', '_IMPORTA._'], { w: 800, max: 140, css: { color: roy, marginTop: '18px' }, extra: { parts: words(['SABE O QUE', 'IMPORTA.'], 1.65, .13) } }),
    ], { y0: 640, y1: 1280 }),
  ] },
// 6 · whip pan até a foto (celular na mão); 1ª linha em Kaushan, 2ª em Montserrat Black
{ n: 6, t0: 17.5, t1: 21.5, pre: .32, post: .25,
  cam: Object.assign(whipIn(.42), { o: [[3.75, 1], [4.2, 0, 'inQ']], s: [[3.6, 1], [4.2, 1.25, 'inC']] }),
  layers: [
    { k: 'map', id: 'v1b', w: 1150, echo: true, stroke: '#BFD8FF', sw: 3, css: { left: '-20px', top: '860px' }, tr: { o: [[0, .6]], x: [[0, 40], [4, -40, 'lin']] } },
    { k: 'photo', src: 'f11', face: { cx: 800, cy: 1150, w: 340 }, tr: { x: [[0, 40], [4, -15, 'lin']], s: [[0, 1.0], [4, 1.05, 'lin']] } },
    { cls: 'K', html: 'Você me conta.', css: { left: '70px', top: '300px', width: '940px', textAlign: 'center', fontSize: '128px', color: sol, filter: 'drop-shadow(0 10px 22px rgba(2,12,50,.45))' },
      tr: { o: [[.15, 0], [.45, 1, 'outQ']], y: [[.15, 40], [.6, 0, 'outC']], x: [[0, 0], [4, 20, 'lin']] } },
    area([blk(['EU LEVO PRA', '*CÂMARA.*'], { w: 760, max: 150, extra: { parts: words(['EU LEVO PRA', 'CÂMARA.'], 1.0, .15) } })], { y0: 470, y1: 840, css: { left: '160px', width: '760px', filter: 'drop-shadow(0 14px 26px rgba(2,12,50,.5))' } }),
  ] },
// 7 · zoom-through: a câmera atravessa o "O" de SOMO e sai na frase seguinte
{ n: 7, t0: 21.5, t1: 25.5, post: .15,
  cam: { o: [[3.75, 1], [4.15, 0, 'inQ']], y: [[3.6, 0], [4.15, 200, 'inC']] },
  layers: [
    area([blk(['E S{O}MO', 'COM'], { w: 860, max: 300, extra: { zo: true, zoY: .52, parts: words(['E SOMO', 'COM'], .2, .16, .38),
      tr: { s: [[1.85, 1], [2.55, 46, 'inE']], zc: [[1.85, 0], [2.25, 1, 'ioC']], o: [[2.42, 1], [2.55, 0, 'lin']] } } })]),
    area([blk(['A'], { w: 900, max: 130 }), blk(['*PREFEITURA.*'], { w: 900, max: 180, css: { marginTop: '18px' } })],
      { tr: { s: [[2.3, .25], [2.85, 1, 'outE']], o: [[2.3, 0], [2.5, 1, 'lin']], blur: [[2.3, 18], [2.8, 0, 'outQ']] }, css: { filter: 'drop-shadow(0 16px 26px rgba(2,12,50,.45))' } }),
  ] },
// 8 · mapa desenhado: contorno amarelo em 2,5 s e depois o preenchimento azul claro
{ n: 8, t0: 25.5, t1: 30, pre: .1, post: .3,
  cam: { o: [[-.1, 0], [.15, 1, 'lin'], [4.25, 1], [4.75, 0, 'inQ']], s: [[4.2, 1], [4.8, 1.12, 'inC']] },
  layers: [
    { k: 'map', id: 'v1c', w: 980, sw: 7, stroke: sol, css: { left: '50px', top: '610px' },
      tr: { dash: [[.1, 0], [2.6, 1, 'ioQ']], fill: [[2.5, 0], [3.2, 1, 'outQ']], s: [[0, .96], [4.5, 1.03, 'lin']] } },
    { cls: 'A', html: 'SÃO JOÃO BATISTA', css: { left: '60px', width: '960px', top: '330px', textAlign: 'center', fontSize: '150px', filter: 'drop-shadow(0 14px 26px rgba(2,12,50,.4))' },
      tr: { clip: wipe('u', .3, .55), y: [[.3, 50], [.85, 0, 'outC']] } },
    area([blk(['INTEIRA, BAIRRO', 'POR *BAIRRO.*'], { w: 860, max: 120, extra: { parts: words(['INTEIRA, BAIRRO', 'POR BAIRRO.'], 1.5, .15) } })], { y0: 1310, y1: 1600, css: { filter: 'drop-shadow(0 12px 22px rgba(2,12,50,.5))' } }),
  ] },
// 9 · paralaxe leve com a foto à direita; etiqueta laranja "COMENTA AQUI" pisca uma vez
{ n: 9, t0: 30, t1: 35, post: .1,
  cam: { o: [[-.05, 0], [.25, 1, 'lin']] },
  layers: [
    { k: 'map', id: 'v1d', w: 1200, echo: true, stroke: '#BFD8FF', sw: 3, css: { left: '-60px', top: '820px' }, tr: { o: [[0, .7]], x: [[0, -40], [5, 30, 'lin']], s: [[0, 1.08], [5, 1, 'lin']] } },
    { k: 'photo', src: 'f03', face: { cx: 730, cy: 1000, w: 300 }, tr: { x: [[0, 70], [.7, 0, 'outC'], [5, -25, 'lin']], s: [[0, 1.0], [5, 1.06, 'lin']], o: [[0, 0], [.3, 1, 'lin']] } },
    area([blk(['COMENTA O NOME', 'DO SEU *BAIRRO*'], { w: 900, max: 120, extra: { parts: words(['COMENTA O NOME', 'DO SEU BAIRRO'], .3, .12) } }),
          blk(['E O QUE ELE', 'MERECE *GANHAR.*'], { w: 900, max: 120, css: { marginTop: '16px' }, extra: { parts: words(['E O QUE ELE', 'MERECE GANHAR.'], 1.25, .12) } })],
      { y0: 270, y1: 760, tr: { x: [[0, -15], [5, 15, 'lin']] }, css: { filter: 'drop-shadow(0 14px 26px rgba(2,12,50,.5))' } }),
    { cls: 'B box', html: 'Comenta aqui', css: { left: '60px', top: '1040px', padding: '20px 30px', fontSize: '44px', letterSpacing: '.02em', background: `linear-gradient(90deg,${lar},#FF9A22)` },
      tr: { x: [[2.2, -500], [2.7, 0, 'outE']], s: [[3.0, 1], [3.15, 1.12, 'outQ'], [3.35, 1, 'ioQ']], bg: [[3.0, lar], [3.12, '#FFC20E', 'lin'], [3.35, lar, 'lin']] } },
  ] },
// 10 · cartão final: blocos LEO e PINTO se montam, logo oficial sobe na base
{ n: 10, t0: 35, t1: 40, bg: BG,
  cam: { clip: [[0, [100, 0, 0, 0]], [.45, [0, 0, 0, 0], 'ioE']] },
  layers: [
    { k: 'map', id: 'v1e', w: 1100, echo: true, stroke: '#BFD8FF', sw: 3, css: { left: '-10px', top: '700px' }, tr: { o: [[.3, 0], [1, .55, 'lin']], s: [[0, 1.08], [5, 1, 'outQ']] } },
    area([blk(['DO POVO PARA', 'O ^POVO.^'], { w: 860, max: 150, extra: { parts: words(['DO POVO PARA', 'O POVO.'], .4, .12) } })], { y0: 290, y1: 640, css: { filter: 'drop-shadow(0 16px 28px rgba(2,12,50,.45))' } }),
    { cls: 'B box', html: 'LEO', css: { left: '170px', top: '700px', padding: '16px 30px 4px', fontSize: '190px', lineHeight: '.92', background: sol, color: mar },
      tr: { x: [[.9, -800], [1.35, 0, 'outE']], sx: [[.9, 1.6], [1.4, 1, 'outC']], mbx: [[.9, 50], [1.3, 0, 'outQ']] } },
    { cls: 'B box', html: 'PINTO', css: { left: '170px', top: '900px', padding: '16px 30px 4px', fontSize: '190px', lineHeight: '.92', background: '#fff', color: roy },
      tr: { x: [[1.05, 900], [1.5, 0, 'outE']], sx: [[1.05, 1.6], [1.55, 1, 'outC']], mbx: [[1.05, 50], [1.45, 0, 'outQ']] } },
    { cls: 'K', html: 'juntos podemos mais!', css: { left: '0', width: '1080px', top: '1115px', textAlign: 'center', fontSize: '84px', color: sol, filter: 'drop-shadow(0 8px 18px rgba(2,12,50,.4))' },
      tr: { clip: wipe('l', 2.1, .7, 'ioQ') } },
    { k: 'img', src: '@logo.png', css: { left: '405px', top: '1270px', width: '390px', filter: 'drop-shadow(0 14px 24px rgba(2,12,50,.45))' },
      tr: { y: [[1.6, 160], [2.2, 0, 'outE']], o: [[1.6, 0], [1.9, 1, 'lin']] } },
  ] },
] };
})();
