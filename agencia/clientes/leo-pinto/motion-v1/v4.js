// Vídeo 4 · "Se você pudesse escolher a próxima conquista…" (textos revistos em 04/11: Leo é situação) (ROTEIROS.md, conta Pedro, 04/11/2026)
// Fotos: f05 (meio corpo, mão no peito) · f19 (busto, olhar de lado) · f27 (na rua: recorte sobre rua desfocada com véu laranja).
(() => {
const { pop, wipe, words, area, blk } = H_;
const sol = C.sol, lar = C.lar, mar = C.mar, roy = C.roy;
const SH = 'drop-shadow(0 16px 28px rgba(2,12,50,.45))';
const R0 = { l: 70, tp: 330, w: 940, h: 1260 };            // retângulo das letras A/B/D
const tile = (L, bg, col, x, t) => ({ cls: 'A box', html: L, css: { left: x + 'px', top: '960px', width: '190px', height: '210px', background: bg, color: col, fontSize: '170px', lineHeight: '230px', textAlign: 'center' },
  tr: pop(t, .34, 1.12) });
window.VIDEO = { id: 'v4', shots: [
// 1 · zoom-through: o texto vem de longe e passa pela câmera; as reticências ficam
{ n: 1, t0: 0, t1: 3.5, post: .6,
  layers: [
    area([blk(['SE VOCÊ PUDESSE', 'ESCOLHER A PRÓXIMA', '*CONQUISTA*'], { w: 900, max: 200, extra: { rowCss: [{}, {}, { marginTop: '14px' }],
      tr: { s: [[0, .04], [.75, 1, 'outE'], [2.55, 1.04, 'lin'], [3.15, 9, 'inE']], o: [[0, 0], [.15, 1, 'lin'], [2.95, 1], [3.12, 0, 'lin']] } } })]),
    { cls: 'B', html: '…', css: { left: 0, width: '1080px', top: '1180px', textAlign: 'center', fontSize: '200px', color: sol, filter: SH },
      tr: { o: [[.8, 0], [1.0, 1, 'lin'], [3.45, 1], [3.7, 0, 'lin']], s: [[.8, .4], [1.1, 1, 'outB']] } },
  ] },
// 2 · mapa desenhado em amarelo com o texto dentro dele
{ n: 2, t0: 3.5, t1: 7, post: .1,
  cam: { o: [[3.2, 1], [3.6, 0, 'lin']], s: [[3.1, 1], [3.6, .9, 'inC']] },
  layers: [
    { k: 'map', id: 'v4a', w: 1060, sw: 7, stroke: sol, css: { left: '10px', top: '560px' },
      tr: { dash: [[0, 0], [2.0, 1, 'ioQ']], fill: [[1.8, 0], [2.6, 1, 'outQ']], s: [[0, 1.02], [3.5, 1.07, 'lin']] } },
    area([blk(['…EM SÃO JOÃO', 'BATISTA,'], { w: 620, max: 120, extra: { parts: words(['…EM SÃO JOÃO', 'BATISTA,'], .45, .14) } }),
          blk(['QUAL *SERIA?*'], { w: 620, max: 110, css: { marginTop: '14px' }, extra: { parts: words(['QUAL SERIA?'], 1.15, .15) } })],
      { y0: 700, y1: 1200, css: { left: '250px', width: '640px', filter: SH } }),
  ] },
// 3 · morph de blocos: um bloco laranja cresce e o "A" gigante vira número de fundo
{ n: 3, t0: 7, t1: 10.5,
  layers: [
    { cls: 'box', css: { left: '490px', top: '910px', width: '100px', height: '100px', background: lar, overflow: 'hidden' },
      tr: { s: [[0, 0], [.3, 1, 'outB']], l: [[.25, 490], [.75, R0.l, 'ioE']], tp: [[.25, 910], [.75, R0.tp, 'ioE']], w: [[.25, 100], [.75, R0.w, 'ioE']], h: [[.25, 100], [.75, R0.h, 'ioE']] },
      kids: [{ cls: 'A', html: 'A', css: { left: 0, top: '-40px', width: '940px', textAlign: 'center', fontSize: '1150px', lineHeight: '1.15', color: 'rgba(255,255,255,.16)' }, tr: { s: [[.5, 1.4], [1.1, 1, 'outE']], o: [[.5, 0], [.8, 1, 'lin'], [3.2, 1], [3.5, 0, 'lin']] } }] },
    area([blk(['A · SAÚDE'], { w: 780, max: 170 }), blk(['PERTO DE §CASA§'], { w: 780, max: 120, css: { marginTop: '16px' } })],
      { y0: 700, y1: 1220, css: { left: '150px', width: '780px' }, tr: { clip: wipe('u', .8, .5), o: [[3.15, 1], [3.4, 0, 'lin']] } }),
  ] },
// 4 · morph: o laranja vira royal e muda de forma; o "B" entra em branco
{ n: 4, t0: 10.5, t1: 14, post: .05,
  layers: [
    { cls: 'box', css: { left: R0.l + 'px', top: R0.tp + 'px', width: R0.w + 'px', height: R0.h + 'px', background: lar, overflow: 'hidden' },
      kids: [{ css: { inset: 0, background: '#1539BE' }, tr: { poly: [[0, [0, 100, 0, 100, 0, 100]], [.5, [0, -100, 200, 100, 0, 100], 'ioE']] } }],
      tr: { rad: [[0, 0], [.55, 470, 'ioE']], h: [[0, R0.h], [.55, 940, 'ioE']], tp: [[0, R0.tp], [.55, 490, 'ioE']], r: [[0, 0], [.55, 8, 'ioE'], [3.5, 0, 'lin']],
            o: [[3.3, 1], [3.5, 0, 'lin']] } },
    { cls: 'A', html: 'B', css: { left: 0, width: '1080px', top: '300px', textAlign: 'center', fontSize: '560px', lineHeight: '1' , filter: SH }, tr: { s: [[.5, 0], [.85, 1, 'outB']], o: [[3.2, 1], [3.45, 0, 'lin']] } },
    area([blk(['RUAS'], { w: 520, max: 150 }), blk(['E *ESTRADAS*'], { w: 640, max: 110, css: { marginTop: '12px' } })],
      { y0: 880, y1: 1260, tr: { clip: wipe('u', .9, .5), o: [[3.2, 1], [3.45, 0, 'lin']] }, css: { filter: SH } }),
  ] },
// 5 · tela dividida na diagonal: foto de um lado, o "C" e o texto em bloco amarelo do outro
{ n: 5, t0: 14, t1: 17.5,
  cam: { o: [[-.05, 0], [.1, 1, 'lin']] },
  layers: [
    { k: 'map', id: 'v4b', w: 1150, echo: true, stroke: '#BFD8FF', sw: 3, css: { left: '-30px', top: '1000px' }, tr: { o: [[0, .55]], x: [[0, 30], [3.5, -30, 'lin']] } },
    { k: 'photo', src: 'f05', face: { cx: 600, cy: 1265, w: 255 }, tr: { y: [[.2, 500], [.85, 0, 'outE']], s: [[0, 1], [3.5, 1.05, 'lin']] } },
    { css: { left: 0, top: 0, width: '1080px', height: '1920px', background: `linear-gradient(160deg,#FFD84A,${sol} 50%,#FFB000)` },
      tr: { poly: [[0, [0, 0, 100, 0, 100, 0, 0, 0]], [.5, [0, 0, 100, 0, 100, 44, 0, 61], 'ioE']] } },
    { cls: 'A', html: 'C', css: { left: '70px', top: '290px', width: '300px', textAlign: 'center', fontSize: '470px', lineHeight: '1', color: mar }, tr: { s: [[.45, 0], [.8, 1, 'outB']] } },
    area([blk(['EDUCAÇÃO'], { w: 600, max: 130 }), blk(['E [JUVENTUDE]'], { w: 600, max: 110, css: { marginTop: '12px' } })],
      { y0: 330, y1: 720, css: { left: '400px', width: '610px', color: mar }, tr: { clip: wipe('l', .8, .5) } }),
  ] },
// 6 · morph de blocos: o amarelo vira marinho e o "D" entra em laranja
{ n: 6, t0: 17.5, t1: 21, post: .1,
  cam: { o: [[3.25, 1], [3.6, 0, 'lin']] },
  layers: [
    { css: { left: 0, top: 0, width: '1080px', height: '1170px', background: sol, overflow: 'hidden' },
      kids: [{ css: { inset: 0, background: mar }, tr: { clip: wipe('d', .05, .45) } }],
      tr: { l: [[0, 0], [.55, R0.l, 'ioE']], tp: [[0, 0], [.55, R0.tp, 'ioE']], w: [[0, 1080], [.55, R0.w, 'ioE']], h: [[0, 1170], [.55, R0.h, 'ioE']], sk: [[0, 0], [.3, -6, 'outQ'], [.6, 0, 'ioQ']] } },
    { cls: 'A', html: 'D', css: { left: 0, width: '1080px', top: '380px', textAlign: 'center', fontSize: '560px', lineHeight: '1', color: lar }, tr: { s: [[.55, 0], [.9, 1, 'outB']] } },
    area([blk(['EMPREGO'], { w: 700, max: 150 }), blk(['E *RENDA*'], { w: 520, max: 130, css: { marginTop: '12px' } })], { y0: 980, y1: 1450, tr: { clip: wipe('u', .95, .5) } }),
  ] },
// 7 · tipografia cinética palavra por palavra; FICAR em degradê amarelo → laranja
{ n: 7, t0: 21, t1: 25.5, post: .1,
  cam: { o: [[-.05, 0], [.1, 1, 'lin'], [4.2, 1], [4.55, 0, 'lin']] },
  layers: [ area([blk(['UMA CIDADE QUE', 'CRESCE COM', 'O JOVEM'], { w: 900, max: 150, extra: { parts: words(['UMA CIDADE QUE', 'CRESCE COM', 'O JOVEM'], .25, .16) } }),
    blk(['^AQUI.^'], { w: 900, max: 220, css: { marginTop: '16px' }, extra: { parts: words(['AQUI.'], 1.65, .22, .42) } })], { css: { filter: SH } }) ] },
// 8 · paralaxe 2.5D: mapa atrás, Leo no meio, "Baixada" em Kaushan na frente; fim com whip pan para cima
{ n: 8, t0: 25.5, t1: 30, post: .05,
  cam: { y: [[4.1, 0], [4.55, 1920, 'ioE']], mby: [[4.1, 0], [4.33, 70, 'inQ'], [4.55, 0, 'outQ']] },
  layers: [
    { k: 'map', id: 'v4c', w: 1250, echo: true, stroke: '#BFD8FF', sw: 3, css: { left: '-80px', top: '700px' }, tr: { o: [[0, 0], [.4, .7, 'lin']], x: [[0, -50], [4.5, 50, 'lin']], s: [[0, 1.12], [4.5, 1.0, 'lin']] } },
    { k: 'photo', src: 'f19', face: { cx: 590, cy: 1245, w: 520 }, tr: { x: [[0, 60], [4.5, -30, 'lin']], s: [[0, 1.0], [4.5, 1.06, 'lin']], o: [[0, 0], [.35, 1, 'lin']] } },
    area([blk(['ESSE SONHO', 'NÃO É SÓ MEU.'], { w: 820, max: 120, extra: { parts: words(['ESSE SONHO', 'NÃO É SÓ MEU.'], .25, .13) } }),
          blk(['É DA NOSSA'], { w: 520, max: 80, css: { marginTop: '22px' }, extra: { parts: words(['É DA NOSSA'], 1.45, .13) } })],
      { y0: 270, y1: 690, justify: 'flex-start', tr: { x: [[0, -15], [4.5, 15, 'lin']] }, css: { filter: SH } }),
    { cls: 'K', html: 'Baixada.', css: { left: 0, width: '1080px', top: '650px', textAlign: 'center', fontSize: '200px', color: sol, filter: SH },
      tr: { clip: wipe('l', 1.95, .6, 'ioQ'), x: [[0, 25], [4.5, -35, 'lin']], s: [[1.95, 1.08], [4.5, 1, 'lin']] } },
  ] },
// 9 · máquina de escrever com as 4 letras em blocos de cor, uma por vez
{ n: 9, t0: 30, t1: 35, pre: .45, post: .1,
  cam: { y: [[-.45, -1920], [0, 0, 'ioE']], mby: [[-.45, 0], [-.22, 70, 'inQ'], [0, 0, 'outQ']], o: [[4.75, 1], [5.1, 0, 'lin']] },
  layers: [
    { cls: 'B cw', type: { text: 'COMENTA\nA LETRA:', t0: .2, t1: 1.0, hide: 1.2 }, css: { left: '90px', top: '560px', width: '900px', fontSize: '128px', lineHeight: '1.04', whiteSpace: 'nowrap' } },
    { cls: 'box', css: { left: '60px', top: '920px', width: '960px', height: '290px', background: '#fff' }, tr: { clip: wipe('l', 1.05, .4) } },
    tile('A', lar, '#fff', 90, 1.4), tile('B', roy, '#fff', 300, 1.75), tile('C', sol, mar, 510, 2.1),
    { cls: 'K', html: 'ou', css: { left: '700px', top: '1000px', width: '80px', textAlign: 'center', fontSize: '64px', color: mar }, tr: { o: [[2.35, 0], [2.5, 1, 'lin']] } },
    tile('D', mar, sol, 790, 2.55),
  ] },
// 10 · cartão final: a foto na rua sai, os blocos se fecham e a logo se monta; "começa com você" em Kaushan
{ n: 10, t0: 35, t1: 40,
  cam: { o: [[-.05, 0], [.1, 1, 'lin']] },
  layers: [
    { css: { left: 0, top: 0, width: '1080px', height: '1920px', overflow: 'hidden', background: lar }, tr: { s: [[0, 1.06], [2.2, 1, 'lin']] },
      kids: [
        { k: 'img', src: '@rua.jpg', css: { left: '-1100px', top: '0px', width: '3680px' }, tr: { x: [[0, 0], [2.2, 80, 'lin']] } },
        { css: { inset: 0, background: 'linear-gradient(180deg,rgba(255,122,26,.62),rgba(232,85,0,.78))' } },
        { k: 'photo', src: 'f27', face: { cx: 540, cy: 1060, w: 235 }, tr: { y: [[0, 60], [.6, 0, 'outC'], [1.7, 0], [2.15, 900, 'inC']], s: [[0, 1], [1.7, 1.04, 'lin']] } },
      ] },
    { css: { left: 0, top: 0, width: '1080px', height: '1920px', background: BG, clipPath: 'inset(0 50% 0 0)' }, tr: { x: [[1.75, -560], [2.2, 0, 'ioE']] } },
    { css: { left: 0, top: 0, width: '1080px', height: '1920px', background: BG, clipPath: 'inset(0 0 0 50%)' }, tr: { x: [[1.75, 560], [2.2, 0, 'ioE']] } },
    { k: 'map', id: 'v4d', w: 1100, echo: true, stroke: '#BFD8FF', sw: 3, css: { left: '-10px', top: '760px' }, tr: { o: [[2.2, 0], [2.8, .5, 'lin']] } },
    area([blk(['A CIDADE QUE'], { w: 880, max: 130, extra: { parts: words(['A CIDADE QUE'], .25, .13) } }), blk(['A GENTE *CONSTRÓI*'], { w: 880, max: 170, css: { marginTop: '10px' }, extra: { parts: words(['A GENTE CONSTRÓI'], .7, .16) } })],
      { y0: 270, y1: 760, css: { filter: SH } }),
    { cls: 'K', html: 'junto com você', css: { left: 0, width: '1080px', top: '900px', textAlign: 'center', fontSize: '104px', color: sol, filter: SH }, tr: { clip: wipe('l', 2.35, .7, 'ioQ') } },
    { k: 'img', src: '@logo.png', css: { left: '410px', top: '1130px', width: '420px', filter: SH },
      tr: { clip: [[2.4, [100, 0, 0, 0]], [3.0, [-5, -5, -5, -5], 'ioE']], s: [[2.4, .85], [3.2, 1, 'outC']] } },
  ] },
] };
})();
