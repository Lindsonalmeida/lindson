/* Seu Turbo · rig do mascote da Orégano Turbo (conta Pedro, 15/11/2026).
   Uma fonte só para tudo: SVG estático, folha de modelo, rig ao vivo e vídeo.
   Uso:  const t = SeuTurbo.criar(elementoSvg);  t.aplicar(estado);
   Cada parte é um <g id="st-..."> com nome, para animar em qualquer ferramenta (GSAP, After Effects via SVG, Rive). */
(function (G) {
  const C = { tomate: '#C8302B', verde: '#1E5B3B', creme: '#F3EEE6', carvao: '#141311', acafrao: '#F2B33D',
    pele: '#EDB48C', pele2: '#D98F66', luva: '#FFFFFF', lente: '#CFE7EE', boca: '#5A1410' };
  const LW = 7; // traço da marca
  const NS = 'http://www.w3.org/2000/svg';
  const st = `stroke="${C.carvao}" stroke-width="${LW}" stroke-linejoin="round" stroke-linecap="round"`;

  // ---------- BOCAS (6 de lip-sync + 4 de expressão) ----------
  const BOCAS = {
    repouso: `<path d="M276 362 Q300 377 324 362" fill="none" ${st}/>`,
    A: `<path d="M268 350 Q300 347 332 350 Q330 410 300 412 Q270 410 268 350Z" fill="${C.boca}" ${st}/><ellipse cx="300" cy="394" rx="17" ry="9" fill="${C.tomate}"/>`,
    E: `<path d="M262 352 Q300 349 338 352 Q328 388 300 390 Q272 388 262 352Z" fill="${C.boca}" ${st}/><path d="M270 354 L330 354 L326 364 L274 364Z" fill="#fff"/>`,
    O: `<ellipse cx="300" cy="374" rx="16" ry="22" fill="${C.boca}" ${st}/><ellipse cx="300" cy="386" rx="8" ry="5" fill="${C.tomate}"/>`,
    MBP: `<path d="M278 362 Q300 370 322 362" fill="none" stroke="${C.carvao}" stroke-width="10" stroke-linecap="round"/><path d="M286 372 Q300 378 314 372" fill="none" stroke="${C.pele2}" stroke-width="5" stroke-linecap="round"/>`,
    F: `<path d="M274 354 Q300 352 326 354 Q320 378 300 380 Q280 378 274 354Z" fill="${C.boca}" ${st}/><rect x="282" y="352" width="36" height="10" rx="3" fill="#fff"/><path d="M280 372 Q300 366 320 372" fill="none" stroke="${C.tomate}" stroke-width="7" stroke-linecap="round"/>`,
    sorriso: `<path d="M258 352 Q300 352 342 352 Q334 408 300 410 Q266 408 258 352Z" fill="${C.boca}" ${st}/><path d="M266 354 L334 354 L330 366 L270 366Z" fill="#fff"/><ellipse cx="300" cy="396" rx="18" ry="8" fill="${C.tomate}"/>`,
    uau: `<ellipse cx="300" cy="380" rx="21" ry="29" fill="${C.boca}" ${st}/><ellipse cx="300" cy="396" rx="11" ry="7" fill="${C.tomate}"/>`,
    hmm: `<path d="M284 370 Q300 362 320 372" fill="none" ${st}/>`,
    debochado: `<path d="M274 366 Q306 380 334 354" fill="none" ${st}/><path d="M330 352 Q338 356 336 364" fill="none" ${st}/>`,
  };
  G.SeuTurboBocas = Object.keys(BOCAS);

  // ---------- LUVAS (desenhadas com o pulso na origem e os dedos para cima) ----------
  const linhasLuva = `<g fill="none" stroke="${C.carvao}" stroke-width="4" stroke-linecap="round"><path d="M-10 -14 L-10 0"/><path d="M0 -12 L0 2"/><path d="M10 -14 L10 0"/></g>`;
  const punhoBase = `<path d="M-30 -10 C-32 -46 32 -46 30 -10 C30 10 -30 10 -30 -10Z" fill="${C.luva}" ${st}/>`;
  const punhos = `<path d="M-22 2 L22 2 L25 22 L-25 22Z" fill="${C.luva}" ${st}/>`;
  const MAOS = {
    punho: `${punhos}${punhoBase}<g fill="none" ${st} stroke-width="5"><path d="M-14 -38 L-14 -26"/><path d="M0 -40 L0 -27"/><path d="M14 -38 L14 -26"/></g>`,
    aberta: `${punhos}<g fill="${C.luva}" ${st}><rect x="-29" y="-74" width="15" height="50" rx="7.5"/><rect x="-13" y="-84" width="15" height="58" rx="7.5"/><rect x="3" y="-80" width="15" height="54" rx="7.5"/><rect x="19" y="-68" width="14" height="44" rx="7"/><rect x="-52" y="-40" width="34" height="15" rx="7.5" transform="rotate(-30 -35 -32)"/></g><path d="M-30 -30 C-30 -48 33 -48 33 -30 L30 -6 C28 10 -28 10 -30 -6Z" fill="${C.luva}" ${st}/>${linhasLuva}`,
    joinha: `${punhos}<rect x="-15" y="-90" width="24" height="66" rx="12" fill="${C.luva}" ${st}/>${punhoBase}<g fill="none" ${st} stroke-width="5"><path d="M10 -36 L28 -36"/><path d="M8 -22 L29 -22"/></g>`,
    aponta: `${punhos}<rect x="-11" y="-100" width="19" height="78" rx="9.5" fill="${C.luva}" ${st}/>${punhoBase}<g fill="none" ${st} stroke-width="5"><path d="M12 -36 L28 -32"/></g>`,
  };
  G.SeuTurboMaos = Object.keys(MAOS);

  // ---------- EXPRESSÕES ----------
  const EXPR = {
    neutro:    { bE: [2, 4], bD: [2, -4], pE: .2, pD: .2, olhar: [2, 3], boca: 'repouso' },
    feliz:     { bE: [-8, -4], bD: [-8, 4], pE: .1, pD: .1, olhar: [0, 2], boca: 'sorriso' },
    surpreso:  { bE: [-20, -6], bD: [-20, 6], pE: 0, pD: 0, olhar: [0, 0], boca: 'uau', pupila: .8 },
    pensando:  { bE: [-14, -10], bD: [4, 10], pE: .15, pD: .15, olhar: [8, -10], boca: 'hmm' },
    confiante: { bE: [4, 10], bD: [-6, -6], pE: .38, pD: .38, olhar: [-3, 2], boca: 'debochado' },
    piscada:   { bE: [-8, -4], bD: [6, 8], pE: 0, pD: 1, olhar: [0, 2], boca: 'sorriso' },
  };
  G.SeuTurboExpr = EXPR;

  // ---------- POSES DOS BRAÇOS (alvo do pulso em coordenadas do desenho 600x900) ----------
  const POSES = {
    neutro:   { L: { x: 196, y: 598, curva: -.25, mao: 'punho' }, R: { x: 404, y: 598, curva: .25, mao: 'punho' } },
    aceno:    { L: { x: 196, y: 598, curva: -.25, mao: 'punho' }, R: { x: 478, y: 262, curva: -.35, mao: 'aberta', giro: 12 } },
    aponta:   { L: { x: 196, y: 598, curva: -.25, mao: 'punho' }, R: { x: 548, y: 412, curva: .22, mao: 'aponta' } },
    joinha:   { L: { x: 186, y: 566, curva: .95, mao: 'punho' }, R: { x: 470, y: 470, curva: .55, mao: 'joinha', fixa: .6 } },
    confiante:{ L: { x: 186, y: 566, curva: .95, mao: 'punho' }, R: { x: 414, y: 566, curva: -.95, mao: 'punho' } },
    pensando: { L: { x: 196, y: 598, curva: -.25, mao: 'punho' }, R: { x: 318, y: 418, curva: -.9, mao: 'punho', fixa: 1 } },
    apresenta:{ L: { x: 104, y: 470, curva: .3, mao: 'aberta', giro: -20 }, R: { x: 496, y: 470, curva: -.3, mao: 'aberta', giro: 20 } },
  };
  G.SeuTurboPoses = POSES;

  const OMBRO = { L: [236, 444], R: [364, 444] };
  const OLHO = { E: [258, 272], D: [342, 272] };

  function esqueleto(uid) {
    const clip = (k) => `<clipPath id="${uid}-c${k}"><ellipse cx="${OLHO[k][0]}" cy="${OLHO[k][1]}" rx="23" ry="30"/></clipPath>`;
    const olho = (k) => `<g id="st-olho-${k === 'E' ? 'esq' : 'dir'}">
      <g data-p="esclera"><ellipse cx="${OLHO[k][0]}" cy="${OLHO[k][1]}" rx="23" ry="30" fill="#fff"/>
      <g clip-path="url(#${uid}-c${k})"><g data-p="pupila"><ellipse cx="${OLHO[k][0]}" cy="${OLHO[k][1]}" rx="11.5" ry="17" fill="${C.carvao}"/><path d="M${OLHO[k][0] + 2} ${OLHO[k][1] - 12} l8 -2 l-3 9Z" fill="#fff"/></g>
      <rect data-p="palpebra" x="${OLHO[k][0] - 28}" y="${OLHO[k][1] - 34}" width="56" height="0" fill="${C.pele}"/></g>
      <ellipse data-p="contorno" cx="${OLHO[k][0]}" cy="${OLHO[k][1]}" rx="23" ry="30" fill="none" ${st}/>
      <path data-p="linha" d="M0 0" fill="none" ${st}/></g>
      <path data-p="fechado" d="M${OLHO[k][0] - 22} ${OLHO[k][1] + 2} Q${OLHO[k][0]} ${OLHO[k][1] + 16} ${OLHO[k][0] + 22} ${OLHO[k][1] + 2}" fill="none" ${st} stroke-width="8" opacity="0"/></g>`;
    const meiaBigode = `<path d="M300 330 C 282 316, 252 314, 232 326 C 216 336, 204 334, 198 318 C 186 340, 206 362, 238 358 C 262 356, 284 350, 300 346 Z" fill="${C.carvao}"/>`;
    const sapato = `<path d="M330 808 Q 398 800 404 834 Q 362 846 322 838 Z" fill="${C.carvao}" ${st}/><path d="M360 814 Q 380 812 390 822" fill="none" stroke="${C.creme}" stroke-width="5" stroke-linecap="round" opacity=".7"/>`;
    const simbolo = `<g transform="translate(276 588) scale(.5)"><path d="M18 86 C 14 50, 40 18, 86 14 C 86 58, 58 88, 18 86 Z" fill="${C.creme}"/><path d="M26 76 L44 58 L54 66 L72 40" fill="none" stroke="${C.verde}" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/><path d="M60 38 L74 38 L74 52" fill="none" stroke="${C.verde}" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/></g>`;
    const braco = (k) => `<g id="st-braco-${k === 'L' ? 'esq' : 'dir'}"><path data-p="manga-fora" fill="none" stroke="${C.carvao}" stroke-width="40" stroke-linecap="round"/><path data-p="manga" fill="none" stroke="${C.creme}" stroke-width="26" stroke-linecap="round"/>
      <g id="st-mao-${k === 'L' ? 'esq' : 'dir'}" data-p="mao">${Object.entries(MAOS).map(([n, s]) => `<g data-mao="${n}" id="st-mao-${k === 'L' ? 'esq' : 'dir'}-${n}" style="display:none">${s}</g>`).join('')}</g></g>`;
    return `<defs>${clip('E')}${clip('D')}</defs>
<g id="st-raiz">
 <ellipse id="st-sombra" cx="300" cy="850" rx="150" ry="17" fill="#000" opacity=".22"/>
 <g id="st-pernas"><g id="st-perna-esq"><path d="M266 650 Q262 740 256 812" fill="none" stroke="${C.carvao}" stroke-width="34" stroke-linecap="round"/><g transform="translate(600 0) scale(-1 1)">${sapato}</g></g>
  <g id="st-perna-dir"><path d="M334 650 Q338 740 344 812" fill="none" stroke="${C.carvao}" stroke-width="34" stroke-linecap="round"/>${sapato}</g></g>
 <g id="st-corpo">
  <path d="M222 420 C 244 404, 356 404, 378 420 C 408 470, 420 560, 410 646 Q300 676 190 646 C 180 560, 192 470, 222 420 Z" fill="${C.creme}" ${st}/>
  <g id="st-botoes"><path d="M300 420 L322 470 L322 560" fill="none" ${st} stroke-width="5"/>${[[288, 478], [336, 478], [288, 524], [336, 524]].map(([x, y]) => `<circle cx="${x}" cy="${y}" r="7.5" fill="${C.tomate}" ${st} stroke-width="4"/>`).join('')}</g>
  <g id="st-avental"><path d="M204 556 L396 556 L406 656 Q300 692 194 656 Z" fill="${C.verde}" ${st}/><path d="M204 556 L396 556 L398 574 L202 574Z" fill="${C.carvao}" opacity=".35"/>${simbolo}</g>
 </g>
 <g id="st-lenco"><path d="M248 400 L352 400 L300 456 Z" fill="${C.tomate}" ${st}/><circle cx="300" cy="404" r="15" fill="${C.tomate}" ${st}/><path d="M276 420 L300 448 M300 420 L320 434" stroke="${C.creme}" stroke-width="5" stroke-linecap="round" opacity=".55"/></g>
 <g id="st-cabeca">
  <g id="st-orelhas"><g id="st-orelha-esq"><circle cx="184" cy="298" r="24" fill="${C.pele}" ${st}/><path d="M178 288 Q192 298 180 310" fill="none" ${st} stroke-width="5"/></g>
   <g id="st-orelha-dir"><circle cx="416" cy="298" r="24" fill="${C.pele}" ${st}/><path d="M422 288 Q408 298 420 310" fill="none" ${st} stroke-width="5"/></g></g>
  <ellipse id="st-rosto" cx="300" cy="292" rx="120" ry="120" fill="${C.pele}" ${st}/>
  <g id="st-face">
   <g id="st-bochechas" opacity=".28"><ellipse cx="226" cy="326" rx="20" ry="11" fill="${C.tomate}"/><ellipse cx="374" cy="326" rx="20" ry="11" fill="${C.tomate}"/></g>
   <g id="st-olhos">${olho('E')}${olho('D')}</g>
   <g id="st-sobrancelhas"><rect id="st-sobr-esq" x="230" y="222" width="56" height="15" rx="7.5" fill="${C.carvao}"/><rect id="st-sobr-dir" x="314" y="222" width="56" height="15" rx="7.5" fill="${C.carvao}"/></g>
   <g id="st-boca" transform="translate(0 -8)">${Object.entries(BOCAS).map(([n, s]) => `<g data-boca="${n}" id="st-boca-${n}" style="display:none">${s}</g>`).join('')}</g>
   <g id="st-nariz"><ellipse cx="300" cy="312" rx="25" ry="19" fill="${C.pele2}" ${st}/><ellipse cx="292" cy="305" rx="7" ry="4" fill="#fff" opacity=".55"/></g>
   <g id="st-bigode">${meiaBigode}<g transform="translate(600 0) scale(-1 1)">${meiaBigode}</g></g>
  </g>
  <g id="st-chapeu">
   <path d="M192 196 C 168 150, 196 104, 238 116 C 248 78, 302 66, 322 98 C 350 74, 404 92, 398 138 C 432 150, 428 196, 410 198 Z" fill="${C.creme}" ${st}/>
   <path d="M250 120 C 262 140, 266 160, 262 176 M326 104 C 336 130, 338 156, 334 176" fill="none" stroke="${C.carvao}" stroke-width="4" opacity=".35" stroke-linecap="round"/>
   <rect x="184" y="168" width="232" height="40" rx="12" fill="${C.verde}" ${st}/>
   <g id="st-oculos"><rect x="270" y="181" width="60" height="12" rx="6" fill="${C.carvao}"/>
    ${[262, 338].map(x => `<circle cx="${x}" cy="186" r="25" fill="${C.acafrao}" ${st}/><circle cx="${x}" cy="186" r="14" fill="${C.lente}" stroke="${C.carvao}" stroke-width="4"/><path d="M${x - 8} ${180} Q${x - 2} ${174} ${x + 5} ${176}" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round"/>`).join('')}</g>
  </g>
 </g>
 ${braco('L')}${braco('R')}
</g>`;
  }

  function criar(svg, uid) {
    uid = uid || 'st' + Math.random().toString(36).slice(2, 7);
    svg.setAttribute('viewBox', '0 0 600 900');
    svg.innerHTML = esqueleto(uid);
    const q = (s) => svg.querySelector(s);
    const P = {
      raiz: q('#st-raiz'), cabeca: q('#st-cabeca'), face: q('#st-face'), chapeu: q('#st-chapeu'), corpo: q('#st-corpo'),
      lenco: q('#st-lenco'), botoes: q('#st-botoes'), orE: q('#st-orelha-esq'), orD: q('#st-orelha-dir'),
      sE: q('#st-sobr-esq'), sD: q('#st-sobr-dir'), sombra: q('#st-sombra'),
      olhos: { E: q('#st-olho-esq'), D: q('#st-olho-dir') }, bocas: [...svg.querySelectorAll('[data-boca]')],
      bracos: { L: q('#st-braco-esq'), R: q('#st-braco-dir') },
    };
    function braco(k, a, dy) {
      const [sx, sy0] = OMBRO[k], sy = sy0 + dy, g = P.bracos[k];
      const wx = a.x, wy = a.y + dy, mx = (sx + wx) / 2, my = (sy + wy) / 2, dx = wx - sx, dyy = wy - sy, len = Math.hypot(dx, dyy);
      const cx = mx - dyy / len * a.curva * len * .45, cy = my + dx / len * a.curva * len * .45;
      const d = `M${sx} ${sy} Q${cx.toFixed(1)} ${cy.toFixed(1)} ${wx.toFixed(1)} ${wy.toFixed(1)}`;
      g.querySelectorAll('path[data-p^=manga]').forEach(p => p.setAttribute('d', d));
      const ang = Math.atan2(wy - cy, wx - cx) * 180 / Math.PI + 90;
      const rot = ang * (1 - (a.fixa || 0)) + (a.giro || 0);
      const m = g.querySelector('[data-p=mao]');
      m.setAttribute('transform', `translate(${wx.toFixed(1)} ${wy.toFixed(1)}) rotate(${rot.toFixed(1)})${k === 'L' ? ' scale(-1 1)' : ''}`);
      m.querySelectorAll('[data-mao]').forEach(h => h.style.display = h.dataset.mao === a.mao ? '' : 'none');
    }
    function olho(k, fech, olhar, pup) {
      const g = P.olhos[k], [cx, cy] = OLHO[k];
      const f = Math.max(0, Math.min(1, fech));
      g.querySelector('[data-p=palpebra]').setAttribute('height', (68 * f).toFixed(1));
      const ly = cy - 34 + 68 * f;
      const ln = g.querySelector('[data-p=linha]');
      ln.setAttribute('d', f > .04 && f < .9 ? `M${cx - 24} ${ly.toFixed(1)} L${cx + 24} ${ly.toFixed(1)}` : 'M0 0');
      g.querySelector('[data-p=pupila]').setAttribute('transform', `translate(${olhar[0]} ${olhar[1]}) translate(${cx} ${cy}) scale(${pup}) translate(${-cx} ${-cy})`);
      const aberto = f < .9;
      g.querySelector('[data-p=esclera]').style.opacity = aberto ? 1 : 0;
      g.querySelector('[data-p=contorno]').style.opacity = aberto ? 1 : 0;
      g.querySelector('[data-p=fechado]').style.opacity = aberto ? 0 : 1;
    }
    /* estado: { expr, boca, pose, piscar(0-1), respira(-1..1), inclina(graus), vira(0-1), x, y, escala, rot, olhar:[x,y], L:{}, R:{}, squash } */
    function aplicar(s) {
      const e = Object.assign({}, EXPR[s.expr || 'neutro']);
      const pose = POSES[s.pose || 'neutro'];
      const L = Object.assign({}, pose.L, s.L || {}), R = Object.assign({}, pose.R, s.R || {});
      const resp = (s.respira || 0), dy = resp * 4, vira = s.vira || 0, sq = s.squash || 0;
      P.raiz.setAttribute('transform', `translate(${s.x || 0} ${s.y || 0}) translate(300 850) rotate(${s.rot || 0}) scale(${(s.escala || 1) * (1 + sq * .12)} ${(s.escala || 1) * (1 - sq * .12)}) translate(-300 -850)`);
      P.corpo.setAttribute('transform', `translate(300 650) scale(${1 - vira * .06} ${1 + resp * .015}) translate(-300 -650)`);
      P.botoes.setAttribute('transform', `translate(${vira * 16} 0)`);
      P.lenco.setAttribute('transform', `translate(${vira * 10} ${dy * .8})`);
      P.cabeca.setAttribute('transform', `translate(${vira * 6} ${dy}) rotate(${s.inclina || 0} 300 400)`);
      P.face.setAttribute('transform', `translate(${vira * 34} 0)`);
      P.chapeu.setAttribute('transform', `translate(${vira * 14} 0)`);
      P.orE.setAttribute('transform', `translate(${vira * 40} 0)`); P.orD.setAttribute('transform', `translate(${-vira * 10} 0)`);
      const sb = (el, [d, r], cx) => el.setAttribute('transform', `translate(0 ${d + (s.sobe || 0)}) rotate(${r} ${cx} 229)`);
      sb(P.sE, e.bE, 258); sb(P.sD, e.bD, 342);
      const olhar = s.olhar || e.olhar, pis = s.piscar || 0;
      olho('E', Math.max(e.pE, pis), olhar, e.pupila || 1);
      olho('D', Math.max(e.pD, pis), olhar, e.pupila || 1);
      const b = s.boca || e.boca;
      P.bocas.forEach(g => g.style.display = g.dataset.boca === b ? '' : 'none');
      P.sombra.setAttribute('rx', (150 * (1 - Math.min(.5, Math.abs(s.y || 0) / 600))).toFixed(1));
      braco('L', L, dy); braco('R', R, dy);
    }
    aplicar({});
    return { aplicar, partes: P, cores: C };
  }

  // Lip-sync: volume (0-1) + "chiado" (taxa de cruzamentos por zero) -> boca
  function visema(vol, chiado, fase) {
    if (vol < .06) return 'repouso';
    if (vol < .16) return chiado > .5 ? 'F' : 'MBP';
    if (chiado > .55) return 'F';
    if (vol < .32) return ['E', 'O', 'E'][Math.floor(fase) % 3];
    return ['A', 'E', 'A', 'O'][Math.floor(fase) % 4];
  }
  // Piscada natural: devolve 0-1 (fecha) para um tempo t em segundos
  function piscada(t, periodo = 3.4) {
    const k = (t % periodo) / .16; return k < 1 ? Math.sin(k * Math.PI) : 0;
  }
  G.SeuTurbo = { criar, visema, piscada, cores: C };
})(typeof window !== 'undefined' ? window : globalThis);
