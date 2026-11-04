// Vídeo 2 · "Prazer, eu sou o Leo" (ROTEIROS.md, conta Pedro, 04/11/2026)
// Fotos: f16 (close, polo amarela) · f02 (meio corpo, braços cruzados) · f30 (busto, polo branca).
(() => {
const { pop, wipe, wipeOut, words, area, blk } = H_;
const sol = C.sol, lar = C.lar, mar = C.mar, roy = C.roy;
const SH = 'drop-shadow(0 16px 28px rgba(2,12,50,.45))';
// caixas de palavra (tela 2) e blocos (tela 7)
const caixa = (txt, bg, col, fs, t, r) => ({ cls: 'B box', html: txt, css: { position: 'relative', padding: '18px 34px 8px', margin: '12px 0', fontSize: fs + 'px', lineHeight: '.95', background: bg, color: col },
  tr: { y: [[t, -1500], [t + .75, 0, 'outBo']], r: [[t, r * 3], [t + .75, r, 'outQ']], o: [[t, 0], [t + .05, 1, 'lin']] } });
const bloco = (i, word, bg, col) => {
  const T = 395 + i * 205, L0 = 440, T0 = 860;
  return [
    { cls: 'box', css: { left: L0 + 'px', top: T0 + 'px', width: '200px', height: '200px', background: bg },
      tr: { s: [[0, 0], [.35, 1, 'outB']], r: [[0, -30], [.35, 0, 'outC']],
        l: [[.45, L0], [.95 + i * .08, 120, 'ioE'], [3.2, 120], [3.65, L0, 'ioE']], w: [[.45, 200], [.95 + i * .08, 840, 'ioE'], [3.2, 840], [3.65, 200, 'ioE']],
        tp: [[.45, T0], [.95 + i * .08, T, 'ioE'], [3.2, T], [3.65, T0, 'ioE']], h: [[.45, 200], [.95 + i * .08, 170, 'ioE'], [3.2, 170], [3.65, 200, 'ioE']],
        bg: [[3.2, bg], [3.6, lar, 'lin']], o: [[3.75, 1], [3.95, 0, 'lin']] } },
    { cls: 'B', html: word, css: { left: '120px', top: T + 'px', width: '840px', height: '170px', display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: '112px', color: col, paddingTop: '10px' },
      tr: Object.assign(pop(.95 + i * .08 + .12, .32), { o: [[1.07 + i * .08, 0], [1.12 + i * .08, 1, 'lin'], [3.05, 1], [3.2, 0, 'lin']] }) },
  ];
};
window.VIDEO = { id: 'v2', shots: [
// 1 · paralaxe 2.5D: rosto se aproxima, fundo recua, "Prazer," em Kaushan atrás da cabeça
{ n: 1, t0: 0, t1: 3.5, post: .3,
  cam: { o: [[3.4, 1], [3.8, 0, 'inQ']], s: [[3.3, 1], [3.8, 1.18, 'inC']] },
  layers: [
    { k: 'map', id: 'v2a', w: 1300, echo: true, stroke: '#BFD8FF', sw: 3, css: { left: '-110px', top: '620px' }, tr: { o: [[0, 0], [.5, .8, 'lin']], s: [[0, 1.18], [3.8, 1.0, 'outQ']] } },
    { cls: 'K', html: 'Prazer,', css: { left: 0, width: '1080px', top: '850px', textAlign: 'center', fontSize: '230px', color: sol, filter: SH },
      tr: { o: [[.15, 0], [.5, 1, 'lin']], s: [[.15, .85], [3.8, 1.02, 'outQ']], y: [[0, 20], [3.8, -10, 'lin']] } },
    { k: 'photo', src: 'f16', face: { cx: 570, cy: 1470, w: 420 }, tr: { y: [[0, 140], [.8, 0, 'outE']], s: [[0, .98], [3.8, 1.09, 'ioQ']], o: [[0, 0], [.25, 1, 'lin']] } },
    area([blk(['EU SOU', 'O *LEO.*'], { w: 760, max: 200, extra: { parts: words(['EU SOU', 'O LEO.'], .7, .16) } })], { y0: 290, y1: 820, css: { filter: SH } }),
  ] },
// 2 · tipografia cinética: cada palavra cai e quica num bloco (amarelo, branco, laranja)
{ n: 2, t0: 3.5, t1: 7.5, post: .1,
  cam: { y: [[3.55, 0], [4.05, -1920, 'inE']], mby: [[3.55, 0], [3.9, 60, 'inQ'], [4.05, 0, 'outQ']] },
  layers: [ area([
    caixa('Jovem.', sol, mar, 150, .1, -2),
    caixa('Engenheiro.', '#fff', roy, 104, .5, 1.5),
    caixa('E daqui.', lar, '#fff', 150, .9, -1.5),
  ]) ] },
// 3 · mapa desenhado em linha branca, com eco mais claro atrás
{ n: 3, t0: 7.5, t1: 11.5, pre: .55, post: .1,
  cam: { y: [[-.55, 1920], [-.05, 0, 'inE'], [.0, 0]], o: [[3.75, 1], [4.1, 0, 'lin']] },
  layers: [
    { k: 'map', id: 'v2b', w: 1040, echo: true, echoColor: '#CFE2FF', sw: 6, stroke: '#FFFFFF', css: { left: '0px', top: '640px' },
      tr: { dash: [[.1, 0], [2.3, 1, 'ioQ']], echoDash: [[.45, 0], [2.7, 1, 'ioQ']], fill: [[2.2, 0], [3.0, .8, 'outQ']], x: [[0, 30], [4, -30, 'lin']] } },
    area([blk(['FILHO DE', 'SÃO JOÃO BATISTA,'], { w: 900, max: 140, cls: 'A', extra: { tr: { clip: wipe('u', .2, .6), y: [[.2, 60], [.8, 0, 'outC']] } } })], { y0: 280, y1: 600, css: { filter: SH } }),
    area([blk(['CORAÇÃO DA', '*BAIXADA.*'], { w: 760, max: 150, extra: { parts: words(['CORAÇÃO DA', 'BAIXADA.'], 1.4, .15) } })], { y0: 1300, y1: 1600, css: { filter: SH } }),
  ] },
// 4 · contador de 2000 a 2024 em 1,5 s (Anton gigante) e rótulo espaçado embaixo
{ n: 4, t0: 11.5, t1: 15.5, post: .1,
  cam: { o: [[-.05, 0], [.15, 1, 'lin'], [3.75, 1], [4.05, 0, 'lin']], s: [[3.6, 1], [4.05, .9, 'inC']] },
  layers: [
    { cls: 'A', count: [[.15, 2000], [1.65, 2024, 'outC']], css: { left: 0, width: '1080px', top: '560px', textAlign: 'center', fontSize: '440px', filter: SH },
      tr: { s: [[.05, .6], [.6, 1, 'outB']], o: [[.05, 0], [.2, 1, 'lin']], col: [[1.6, '#FFFFFF'], [1.9, sol, 'lin']] } },
    { cls: 'Lb', html: 'Vereador<br>mais bem votado', css: { left: 0, width: '1080px', textAlign: 'center', top: '1020px', fontSize: '54px', lineHeight: '1.45', paddingLeft: '.38em', filter: SH },
      tr: { ls: [[1.75, .9], [2.45, .38, 'outC']], o: [[1.75, 0], [2.1, 1, 'lin']], y: [[1.75, 30], [2.3, 0, 'outC']] } },
  ] },
// 5 · máscara: TROFÉU sai num wipe para a esquerda, COMPROMISSO entra em amarelo
{ n: 5, t0: 15.5, t1: 19, post: .05,
  cam: { y: [[3.15, 0], [3.55, -1920, 'ioE']], mby: [[3.15, 0], [3.35, 70, 'inQ'], [3.55, 0, 'outQ']] },
  layers: [
    area([blk(['NÃO ENCARO COMO'], { w: 860, max: 110, extra: { parts: words(['NÃO ENCARO COMO'], .1, .13), tr: { o: [[1.95, 1], [2.25, 0, 'lin']], y: [[1.95, 0], [2.25, -40, 'inQ']] } } }),
          blk(['TROFÉU.'], { w: 860, max: 230, css: { marginTop: '14px' }, extra: { tr: { clip: [[.4, [-12, 100, -12, -2]], [.85, [-12, -2, -12, -2], 'ioE'], [1.95, [-12, -2, -12, -2]], [2.4, [-12, 100, -12, -2], 'ioE']], x: [[1.95, 0], [2.4, -160, 'inC']] } } })]),
    area([blk(['ENCARO COMO'], { w: 860, max: 130, extra: { tr: { o: [[2.15, 0], [2.4, 1, 'lin']], y: [[2.15, 40], [2.45, 0, 'outC']] } } }),
          blk(['*COMPROMISSO.*'], { w: 900, max: 230, css: { marginTop: '14px' }, extra: { tr: { clip: [[2.2, [-12, -2, -12, 100]], [2.65, [-12, -2, -12, -2], 'ioE']], x: [[2.2, 120], [2.65, 0, 'outC']] } } })], { css: { filter: SH } }),
  ] },
// 6 · whip pan para baixo até a foto (entra pela esquerda); texto em máquina de escrever num bloco branco
{ n: 6, t0: 19, t1: 23.5, pre: .35, post: .3,
  cam: { y: [[-.35, 1920], [.05, 0, 'ioE']], mby: [[-.35, 0], [-.15, 70, 'inQ'], [.05, 0, 'outQ']], o: [[4.2, 1], [4.5, 0, 'lin']], s: [[4.1, 1], [4.6, 1.1, 'inC']] },
  layers: [
    { k: 'map', id: 'v2c', w: 1100, echo: true, stroke: '#BFD8FF', sw: 3, css: { left: '200px', top: '980px' }, tr: { o: [[0, .55]], x: [[0, 30], [4.5, -40, 'lin']] } },
    { k: 'photo', src: 'f02', face: { cx: 360, cy: 1140, w: 285 }, tr: { x: [[.1, -700], [.75, 0, 'outE'], [4.5, 25, 'lin']], mbx: [[.1, 40], [.6, 0, 'outQ']], s: [[0, 1], [4.5, 1.05, 'lin']] } },
    { cls: 'box', css: { left: '70px', top: '300px', width: '940px', padding: '34px 40px 30px', background: '#fff' },
      tr: { clip: wipe('d', .3, .45), y: [[0, 0], [4.5, -15, 'lin']] },
      kids: [
        { cls: 'B', type: { text: 'QUEM É ENGENHEIRO\nOLHA A RUA', t0: .7, t1: 1.8, hide: 1.95 }, css: { position: 'relative', fontSize: '74px', lineHeight: '1.05', color: roy } },
        { cls: 'B', type: { text: 'E ENTENDE O\nQUE PRECISA.', t0: 2.0, t1: 2.9 }, css: { position: 'relative', marginTop: '18px', fontSize: '74px', lineHeight: '1.05', color: lar } },
      ] },
  ] },
// 7 · morph de blocos: um quadrado laranja vira 4 blocos, um por palavra, e eles se juntam de novo
{ n: 7, t0: 23.5, t1: 27.5, post: .1,
  layers: [
    ...bloco(0, 'Estrada.', lar, '#fff'), ...bloco(1, 'Ponte.', sol, mar), ...bloco(2, 'Rua.', '#fff', roy), ...bloco(3, 'Drenagem.', mar, sol),
  ] },
// 8 · tipografia cinética: linhas deslizando na horizontal em sentidos opostos
{ n: 8, t0: 27.5, t1: 31.5, post: .1,
  cam: { o: [[3.7, 1], [4.05, 0, 'lin']] },
  layers: [ area([
    blk(['ENERGIA PRA'], { w: 900, max: 150, extra: { tr: { x: [[.05, -1300], [.55, 0, 'outE'], [4, 30, 'lin']], mbx: [[.05, 60], [.5, 0, 'outQ']] } } }),
    blk(['ESTAR NA *RUA,*'], { w: 900, max: 150, css: { marginTop: '10px' }, extra: { tr: { x: [[.2, 1300], [.7, 0, 'outE'], [4, -30, 'lin']], mbx: [[.2, 60], [.65, 0, 'outQ']] } } }),
    blk(['NO BAIRRO E'], { w: 900, max: 150, css: { marginTop: '40px' }, extra: { tr: { x: [[1.2, -1300], [1.7, 0, 'outE'], [4, 30, 'lin']], mbx: [[1.2, 60], [1.65, 0, 'outQ']] } } }),
    blk(['NO *POVOADO.*'], { w: 900, max: 150, css: { marginTop: '10px' }, extra: { tr: { x: [[1.35, 1300], [1.85, 0, 'outE'], [4, -30, 'lin']], mbx: [[1.35, 60], [1.8, 0, 'outQ']] } } }),
  ], { css: { filter: SH } }) ] },
// 9 · paralaxe leve com a foto à direita e etiqueta branca com letra royal
{ n: 9, t0: 31.5, t1: 35.5, post: .1,
  cam: { o: [[-.05, 0], [.25, 1, 'lin']] },
  layers: [
    { k: 'map', id: 'v2d', w: 1150, echo: true, stroke: '#BFD8FF', sw: 3, css: { left: '-30px', top: '900px' }, tr: { o: [[0, .6]], x: [[0, -30], [4, 30, 'lin']] } },
    { k: 'photo', src: 'f30', face: { cx: 720, cy: 1210, w: 370 }, tr: { x: [[0, 120], [.7, 0, 'outE'], [4, -20, 'lin']], s: [[0, 1], [4, 1.05, 'lin']], o: [[0, 0], [.3, 1, 'lin']] } },
    area([blk(['E VOCÊ,'], { w: 900, max: 130, extra: { parts: words(['E VOCÊ,'], .3, .14) } }), blk(['É DE *ONDE?*'], { w: 900, max: 170, css: { marginTop: '10px' }, extra: { parts: words(['É DE ONDE?'], .6, .16) } })],
      { y0: 280, y1: 760, tr: { x: [[0, -12], [4, 12, 'lin']] }, css: { filter: SH } }),
    { cls: 'B box', html: 'Me conta no direct', css: { left: '70px', top: '835px', padding: '20px 30px 16px', fontSize: '40px', letterSpacing: '.02em', background: '#fff', color: roy },
      tr: { clip: wipe('l', 1.4, .5), x: [[1.4, -30], [1.9, 0, 'outC']] } },
  ] },
// 10 · cartão final: blocos LEO e PINTO se montam, logo sobe, compromisso em Kaushan
{ n: 10, t0: 35.5, t1: 40, bg: BG,
  cam: { poly: [[0, [0, 0, 0, 0, 0, 0, 0, 0]], [.5, [0, 0, 200, 0, 0, 200, 0, 0], 'ioE']] },
  layers: [
    { cls: 'Lb', html: 'Jovem <span class="y">•</span> Engenheiro', css: { left: 0, width: '1080px', textAlign: 'center', top: '330px', fontSize: '36px' }, tr: { ls: [[.3, .7], [1, .38, 'outC']], o: [[.3, 0], [.7, 1, 'lin']] } },
    { cls: 'box', css: { left: '540px', top: '420px', width: '0px', height: '196px', background: sol }, tr: { l: [[.4, 540], [.85, 200, 'ioE']], w: [[.4, 0], [.85, 470, 'ioE']] } },
    { cls: 'B', html: 'LEO', css: { left: '200px', width: '470px', top: '420px', height: '196px', textAlign: 'center', paddingTop: '22px', fontSize: '190px', lineHeight: '.92', color: mar }, tr: pop(.8, .35) },
    { cls: 'box', css: { left: '540px', top: '630px', width: '0px', height: '196px', background: '#fff' }, tr: { l: [[.6, 540], [1.05, 175, 'ioE']], w: [[.6, 0], [1.05, 730, 'ioE']] } },
    { cls: 'B', html: 'PINTO', css: { left: '175px', width: '730px', top: '630px', height: '196px', textAlign: 'center', paddingTop: '22px', fontSize: '190px', lineHeight: '.92', color: roy }, tr: pop(1.0, .35) },
    { cls: 'K', html: 'compromisso com<br>São João Batista', css: { left: 0, width: '1080px', top: '875px', textAlign: 'center', fontSize: '84px', color: sol, filter: SH }, tr: { clip: wipe('l', 1.5, .8, 'ioQ') } },
    { k: 'img', src: '@logo.png', css: { left: '415px', top: '1150px', width: '370px', filter: SH }, tr: { y: [[2.0, 160], [2.6, 0, 'outE']], o: [[2.0, 0], [2.3, 1, 'lin']] } },
  ] },
] };
})();
