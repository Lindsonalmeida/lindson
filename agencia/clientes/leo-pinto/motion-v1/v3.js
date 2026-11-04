// Vídeo 3 · "A gente ouve. A gente volta pra mostrar." (textos revistos em 04/11: Leo é situação) (ROTEIROS.md, conta Pedro, 04/11/2026)
// Fotos: f04 (meio corpo, punho erguido) · f15 (na rua: recorte sobre rua desfocada com véu royal) · f18 (close sorrindo).
(() => {
const { pop, wipe, words, area, blk } = H_;
const sol = C.sol, lar = C.lar, mar = C.mar, roy = C.roy;
const SH = 'drop-shadow(0 16px 28px rgba(2,12,50,.45))';
const LAR_BG = `linear-gradient(165deg,#FF9A22,${lar} 50%,#E85500)`;
// número que rola (contador dos passos): coluna de dígitos dentro de uma janela
const roll = (digs, t, css, col = sol, fs = 560) => ({ css: Object.assign({ overflow: 'hidden', height: fs * .98 + 'px', width: fs * .62 + 'px' }, css),
  kids: [{ cls: 'A', html: digs.map(d => `<div style="height:${fs * .98}px;line-height:${fs * 1.0}px;text-align:center">${d}</div>`).join(''), css: { position: 'relative', fontSize: fs + 'px', color: col, width: '100%' },
    tr: { y: [[t, 0], [t + .65, -(digs.length - 1) * fs * .98, 'ioE']], blur: [[t, 0], [t + .3, 6, 'inQ'], [t + .65, 0, 'outQ']] } }] });
window.VIDEO = { id: 'v3', shots: [
// 1 · máquina de escrever num bloco branco sobre fundo laranja, cursor marinho
{ n: 1, t0: 0, t1: 3.5, bg: LAR_BG, post: .45,
  cam: { x: [[3.1, 0], [3.55, 1080, 'ioE']], mbx: [[3.1, 0], [3.32, 70, 'inQ'], [3.55, 0, 'outQ']] },
  layers: [
    { cls: 'box', css: { left: '60px', top: '720px', width: '960px', height: '380px', background: '#fff' }, tr: { sx: [[0, 0], [.35, 1, 'outE']], s: [[0, 1]] } },
    { cls: 'B', type: { text: 'A GENTE\nOUVE.', t0: .45, t1: 1.3 }, css: { left: '110px', top: '790px', width: '880px', fontSize: '106px', lineHeight: '1.1', color: mar, whiteSpace: 'nowrap' } },
  ] },
// 2 · whip pan para a esquerda até o fundo azul; foto em paralaxe; MOSTRAR em degradê
{ n: 2, t0: 3.5, t1: 7, pre: .35, post: .1,
  cam: { x: [[-.35, -1080], [.1, 0, 'ioE']], mbx: [[-.35, 0], [-.13, 70, 'inQ'], [.1, 0, 'outQ']], o: [[3.25, 1], [3.6, 0, 'lin']], s: [[3.2, 1], [3.6, 1.12, 'inC']] },
  layers: [
    { k: 'map', id: 'v3a', w: 1200, echo: true, stroke: '#BFD8FF', sw: 3, css: { left: '-60px', top: '780px' }, tr: { o: [[0, .6]], x: [[0, 50], [3.6, -30, 'lin']], s: [[0, 1.1], [3.6, 1, 'lin']] } },
    { k: 'photo', src: 'f04', face: { cx: 770, cy: 1250, w: 290 }, tr: { x: [[0, 140], [.8, 0, 'outE'], [3.6, -20, 'lin']], s: [[0, 1], [3.6, 1.06, 'lin']] } },
    area([blk(['A GENTE VOLTA'], { w: 900, max: 120, extra: { parts: words(['A GENTE VOLTA'], .3, .14) } }), blk(['PRA ^MOSTRAR.^'], { w: 900, max: 160, css: { marginTop: '12px' }, extra: { parts: words(['PRA MOSTRAR.'], .8, .18, .4) } })],
      { y0: 290, y1: 900, tr: { x: [[0, -15], [3.6, 15, 'lin']] }, css: { filter: SH } }),
  ] },
// 3 · contador de passos: o "1" gigante rola para dentro como número de fundo
{ n: 3, t0: 7, t1: 11, pre: .1, post: .1,
  cam: { o: [[-.1, 0], [.15, 1, 'lin'], [3.8, 1], [4.05, 0, 'lin']] },
  layers: [
    roll(['', '1'], .05, { left: '260px', top: '300px' }, sol, 900),
    area([blk(['VOCÊ MANDA'], { w: 900, max: 140 }), blk(['A *DEMANDA.*'], { w: 900, max: 150, css: { marginTop: '10px' } })],
      { y0: 1180, y1: 1600, css: { filter: SH }, tr: { clip: wipe('u', .55, .5), y: [[.55, 60], [1.05, 0, 'outC']] } }),
  ] },
// 4 · tela dividida na horizontal: foto na rua em cima; número e texto embaixo; o 1 rola para 2
{ n: 4, t0: 11, t1: 15, post: .05,
  cam: { o: [[3.85, 1], [4.05, 0, 'lin']] },
  layers: [
    { css: { left: 0, top: 0, width: '1080px', height: '960px', overflow: 'hidden', background: mar },
      tr: { y: [[0, -960], [.55, 0, 'outE']] },
      kids: [
        { k: 'img', src: '@rua.jpg', css: { left: '-420px', top: '-40px', width: '1920px' }, imgCss: { width: '100%' }, tr: { x: [[0, 0], [4, -60, 'lin']], s: [[0, 1.08], [4, 1.0, 'lin']] } },
        { css: { inset: 0, background: 'linear-gradient(180deg,rgba(35,80,245,.55),rgba(8,32,99,.72))' } },
        { k: 'photo', src: 'f15', face: { cx: 540, cy: 470, w: 175 }, tr: { y: [[.2, 120], [.9, 0, 'outE']], s: [[0, 1], [4, 1.04, 'lin']] } },
      ] },
    { css: { left: 0, top: '960px', width: '1080px', height: '960px', background: BG }, tr: { y: [[0, 960], [.55, 0, 'outE']] } },
    roll(['1', '2'], .8, { left: '60px', top: '1010px' }, sol, 560),
    area([blk(['EU REGISTRO'], { w: 580, max: 110 }), blk(['E VOU ATÉ *LÁ.*'], { w: 580, max: 110, css: { marginTop: '10px' } })],
      { y0: 1030, y1: 1580, css: { left: '420px', width: '600px', filter: SH }, tr: { clip: wipe('l', 1.2, .5), x: [[1.2, 40], [1.7, 0, 'outC']] } }),
  ] },
// 5 · morph de blocos: o bloco do 2 vira um retângulo marinho e o 3 rola dentro dele
{ n: 5, t0: 15, t1: 19, post: .1,
  cam: { o: [[3.8, 1], [4.05, 0, 'lin']] },
  layers: [
    { cls: 'box', css: { left: '60px', top: '1010px', width: '347px', height: '549px', background: sol, overflow: 'hidden' },
      tr: { l: [[0, 60], [.6, 70, 'ioE']], tp: [[0, 1010], [.6, 330, 'ioE']], w: [[0, 347], [.6, 940, 'ioE']], h: [[0, 549], [.6, 1220, 'ioE']], rad: [[0, 0], [.3, 40, 'outQ'], [.6, 0, 'inQ']] },
      kids: [{ css: { inset: 0, background: mar }, tr: { clip: wipe('u', .25, .45) } }] },
    Object.assign(roll(['2', '3'], .75, { left: '366px', top: '380px' }, sol, 560), { tr: { o: [[.45, 0], [.6, 1, 'lin']], y: [[.45, 40], [.7, 0, 'outC']] } }),
    area([blk(['LEVO PRA CÂMARA'], { w: 820, max: 100 }), blk(['E SOMO COM A'], { w: 820, max: 100, css: { marginTop: '10px' } }), blk(['*PREFEITURA.*'], { w: 820, max: 130, css: { marginTop: '10px' } })],
      { y0: 1000, y1: 1500, css: { left: '130px', width: '820px' }, tr: { clip: wipe('u', 1.1, .5) } }),
  ] },
// 6 · máscara: um wipe diagonal laranja revela o 4 e o texto
{ n: 6, t0: 19, t1: 23, bg: LAR_BG, post: .15,
  cam: { poly: [[0, [100, 100, 100, 100, 100, 100]], [.55, [-110, 100, 100, -110, 100, 100], 'ioE']], o: [[3.8, 1], [4.15, 0, 'lin']], s: [[3.7, 1], [4.15, .92, 'inC']] },
  layers: [
    { cls: 'A', html: '4', css: { left: 0, width: '1080px', top: '260px', textAlign: 'center', fontSize: '640px', lineHeight: '1', color: '#fff', filter: 'drop-shadow(0 20px 34px rgba(120,40,0,.45))' },
      tr: { s: [[.35, .7], [.9, 1, 'outB']], o: [[.35, 0], [.5, 1, 'lin']] } },
    area([blk(['VOLTO E TE MOSTRO'], { w: 900, max: 110 }), blk(['O §ANDAMENTO.§'], { w: 900, max: 140, css: { marginTop: '10px' } })],
      { y0: 1050, y1: 1520, tr: { clip: wipe('l', .8, .55) }, css: { filter: 'drop-shadow(0 12px 22px rgba(120,40,0,.35))' } }),
  ] },
// 7 · tipografia cinética: PEDIU? salta em branco, TÁ FEITO. bate em amarelo gigante com tremor de 2 quadros
{ n: 7, t0: 23, t1: 27.5, post: .1,
  cam: { x: [[.95, 0], [.9833, 16, 'lin'], [1.0167, -14, 'lin'], [1.05, 0, 'lin']], y: [[.95, 0], [.9833, -10, 'lin'], [1.0167, 8, 'lin'], [1.05, 0, 'lin']], o: [[-.05, 0], [.1, 1, 'lin'], [4.25, 1], [4.6, 0, 'lin']] },
  layers: [
    { k: 'map', id: 'v3b', w: 1150, echo: true, stroke: '#BFD8FF', sw: 3, css: { left: '-35px', top: '820px' }, tr: { o: [[0, 0], [1, .55, 'lin']], s: [[0, 1.1], [4.5, 1, 'lin']] } },
    { cls: 'B', html: 'Pediu?', css: { left: 0, width: '1080px', top: '400px', textAlign: 'center', fontSize: '190px', filter: SH }, tr: pop(.15, .4, 1.12) },
    area([blk(['*TÁ*', '*FEITO.*'], { w: 900, max: 300, extra: { tr: { s: [[.75, 2.6], [.95, 1, 'inC']], o: [[.75, 0], [.85, 1, 'lin']], blur: [[.75, 14], [.95, 0, 'inQ']] } } })], { y0: 640, y1: 1500, css: { filter: SH } }),
  ] },
// 8 · máquina de escrever em 2 linhas sobre marinho chapado (transparência, não promessa)
{ n: 8, t0: 27.5, t1: 32, bg: mar, pre: .05, post: .1,
  cam: { clip: [[-.05, [0, 0, 0, 100]], [.3, [0, 0, 0, 0], 'ioE']], o: [[4.3, 1], [4.6, 0, 'lin']] },
  layers: [
    { cls: 'B cw', type: { text: 'TRABALHANDO\nJUNTO,', t0: .35, t1: 1.35, hide: 1.5 }, css: { left: '80px', top: '730px', width: '940px', fontSize: '84px', lineHeight: '1.08', whiteSpace: 'nowrap' } },
    { cls: 'B cw', type: { text: 'PRA CIDADE\nANDAR.', t0: 1.6, t1: 2.45 }, css: { left: '80px', top: '960px', width: '940px', fontSize: '84px', lineHeight: '1.08', whiteSpace: 'nowrap', color: sol } },
  ] },
// 9 · paralaxe: foto à esquerda e etiqueta laranja à direita
{ n: 9, t0: 32, t1: 36, post: .05,
  cam: { o: [[-.1, 0], [.2, 1, 'lin']] },
  layers: [
    { k: 'map', id: 'v3c', w: 1100, echo: true, stroke: '#BFD8FF', sw: 3, css: { left: '120px', top: '760px' }, tr: { o: [[0, .55]], x: [[0, 40], [4, -40, 'lin']] } },
    { k: 'photo', src: 'f18', face: { cx: 470, cy: 1300, w: 540 }, tr: { x: [[0, -120], [.7, 0, 'outE'], [4, 15, 'lin']], s: [[0, 1], [4, 1.05, 'lin']], o: [[0, 0], [.3, 1, 'lin']] } },
    area([blk(['MANDA NO DIRECT'], { w: 900, max: 120, extra: { parts: words(['MANDA NO DIRECT'], .3, .13) } }), blk(['A DEMANDA DO', 'SEU *BAIRRO.*'], { w: 900, max: 120, css: { marginTop: '12px' }, extra: { parts: words(['A DEMANDA DO', 'SEU BAIRRO.'], .9, .12) } })],
      { y0: 270, y1: 760, tr: { x: [[0, 12], [4, -12, 'lin']] }, css: { filter: SH } }),
    { cls: 'B box', html: 'Com foto, se puder', css: { left: '560px', top: '790px', width: '450px', padding: '18px 0 14px', textAlign: 'center', fontSize: '36px', letterSpacing: '.02em', background: `linear-gradient(90deg,${lar},#FF9A22)` },
      tr: { clip: wipe('r', 1.9, .5), x: [[1.9, 40], [2.4, 0, 'outC']] } },
  ] },
// 10 · cartão final: os blocos de cor se fecham no centro, a logo se monta e o nome do quadro aparece em Kaushan
{ n: 10, t0: 36, t1: 40,
  layers: [
    { css: { left: 0, top: 0, width: '1080px', height: '1920px', background: BG, clipPath: 'inset(0 0 50% 0)' }, tr: { y: [[0, -960], [.5, 0, 'ioE']] } },
    { css: { left: 0, top: '0px', width: '1080px', height: '1920px', background: BG, clipPath: 'inset(50% 0 0 0)' }, tr: { y: [[0, 960], [.5, 0, 'ioE']] } },
    { css: { left: 0, top: '952px', width: '1080px', height: '16px', background: sol }, tr: { sx: [[.35, 1], [.75, 0, 'inC']], o: [[0, 0], [.3, 1, 'lin'], [.75, 1], [.76, 0, 'lin']] } },
    { k: 'map', id: 'v3d', w: 1100, echo: true, stroke: '#BFD8FF', sw: 3, css: { left: '-10px', top: '780px' }, tr: { o: [[.5, 0], [1.2, .5, 'lin']] } },
    { k: 'img', src: '@logo.png', css: { left: '343px', top: '400px', width: '580px', filter: SH },
      tr: { clip: [[.6, [100, 0, 0, 0]], [1.2, [-5, -5, -5, -5], 'ioE']], s: [[.6, .85], [1.4, 1, 'outC']] } },
    { cls: 'K', html: 'Pediu? Tá feito.', css: { left: 0, width: '1080px', top: '960px', textAlign: 'center', fontSize: '124px', color: sol, filter: SH }, tr: { clip: wipe('l', 1.3, .7, 'ioQ') } },
    { cls: 'K', html: 'juntos podemos mais!', css: { left: 0, width: '1080px', top: '1130px', textAlign: 'center', fontSize: '74px', color: '#fff', filter: SH }, tr: { o: [[2.0, 0], [2.4, 1, 'lin']], y: [[2.0, 30], [2.5, 0, 'outC']] } },
  ] },
] };
})();
