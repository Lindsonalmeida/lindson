// Identidade v1 · Dra. Jaci Cunha (conta Lindson, 01/11/2026)
// Símbolo: o C aberto é o cuidado que acolhe, a curva do J é o sorriso, o ponto é o brilho.
const C = { p: '#0F4C4A', v: '#8FD3C7', c: '#F07F67', o: '#C8A46B', a: '#F6F0E8', g: '#1F2B2C', w: '#FFFFFF' };

// Monograma JC (viewBox 100x100)
function mono({ s = 120, cc = C.p, jc = C.c, dc = C.o, sw = 9 } = {}) {
  return `<svg width="${s}" height="${s}" viewBox="0 0 100 100" fill="none" stroke-linecap="round" stroke-linejoin="round">
<path d="M81.5 25.2A40 40 0 1 0 81.5 74.8" stroke="${cc}" stroke-width="${sw}"/>
<path d="M60 28V54.5A14 14 0 0 1 32 54.5" stroke="${jc}" stroke-width="${sw}"/>
<circle cx="36" cy="31" r="${(sw * 0.55).toFixed(1)}" fill="${dc}" stroke="none"/></svg>`;
}

// Assinatura: símbolo + nome + descritor
function lockup({ fs = 64, cc = C.p, jc = C.c, dc = C.o, t1 = C.p, t2 = C.g, dir = 'h', sub = 'Odontologia Especializada', city = '' } = {}) {
  const m = mono({ s: fs * 1.55, cc, jc, dc });
  const txt = `<div style="display:flex;flex-direction:column;gap:${fs * 0.14}px;${dir === 'v' ? 'align-items:center;text-align:center' : ''}">
<span style="font-family:Fraunces;font-weight:560;font-size:${fs}px;line-height:1;letter-spacing:-.015em;color:${t1};font-variation-settings:'SOFT' 80,'opsz' 96">Dra. Jaci Cunha</span>
<span style="font-family:Manrope;font-weight:600;font-size:${fs * 0.235}px;letter-spacing:.32em;text-transform:uppercase;color:${t2}">${sub}</span>
${city ? `<span style="font-family:Manrope;font-weight:500;font-size:${fs * 0.2}px;letter-spacing:.32em;text-transform:uppercase;color:${t2};opacity:.65">${city}</span>` : ''}</div>`;
  return dir === 'v'
    ? `<div style="display:inline-flex;flex-direction:column;align-items:center;gap:${fs * 0.42}px">${m}${txt}</div>`
    : `<div style="display:inline-flex;align-items:center;gap:${fs * 0.42}px">${m}${txt}</div>`;
}

// Grafismo "Linha do sorriso": arcos suaves e pontos de brilho em padrão
function sorriso({ id = 'ls', fg = C.v, dot = C.c, op = 1, sc = 1 } = {}) {
  const w = 160 * sc, h = 110 * sc;
  return {
    id,
    def: `<pattern id="${id}" width="${w}" height="${h}" patternUnits="userSpaceOnUse">
<path d="M${20 * sc} ${38 * sc}Q${80 * sc} ${86 * sc} ${140 * sc} ${38 * sc}" stroke="${fg}" stroke-width="${4 * sc}" fill="none" stroke-linecap="round" opacity="${op}"/>
<circle cx="${80 * sc}" cy="${18 * sc}" r="${4 * sc}" fill="${dot}" opacity="${op}"/>
<path d="M${-60 * sc} ${93 * sc}Q${0} ${141 * sc} ${60 * sc} ${93 * sc}M${100 * sc} ${93 * sc}Q${160 * sc} ${141 * sc} ${220 * sc} ${93 * sc}" stroke="${fg}" stroke-width="${4 * sc}" fill="none" stroke-linecap="round" opacity="${op}"/></pattern>`
  };
}

// Ícones dos tratamentos (traço 5, viewBox 64, ponto de brilho em coral)
const DENTE = 'M20 12c-6 0-10 5-10 12 0 6 3 10 4 15 1 6 2 13 6 13 4 0 4-9 7-13 2-3 4-3 6 0 3 4 3 13 7 13 4 0 5-7 6-13 1-5 4-9 4-15 0-7-4-12-10-12-5 0-7 3-10 3s-5-3-10-3z';
const ICON = {
  'Avaliação': `<path d="${DENTE}"/><circle cx="46" cy="46" r="8" /><path d="M52 52l6 6"/>`,
  'Prevenção e limpeza': `<path d="M6 44H34"/><rect x="34" y="38" width="22" height="10" rx="4"/><path d="M38 38v-10M44 38v-10M50 38v-10"/>`,
  'Clareamento': `<path d="${DENTE}"/><path d="M8 2v10M3 7h10"/>`,
  'Ortodontia': `<path d="M8 30h48"/><rect x="12" y="24" width="10" height="12" rx="2"/><rect x="27" y="24" width="10" height="12" rx="2"/><rect x="42" y="24" width="10" height="12" rx="2"/>`,
  'Implante': `<path d="M18 12h28l-3 14H21z"/><path d="M26 26v26M38 26v26M22 34h20M23 42h18M25 50h14"/>`,
  'Prótese': `<path d="M10 40c6-14 38-14 44 0"/><path d="M18 36v8M26 33v10M34 32v10M42 33v10M48 36v6"/>`,
  'Canal (endodontia)': `<path d="${DENTE}"/><path d="M27 30v14M37 30v14"/>`,
  'Estética do sorriso': `<path d="M12 30q20 22 40 0"/><path d="M18 33q14 10 28 0"/>`,
  'Odontopediatria': `<circle cx="32" cy="26" r="14"/><path d="M26 30q6 5 12 0"/><path d="M22 52q10-10 20 0"/>`
};
function icone(n, { s = 64, c = C.p, dot = C.c, bg = null, sw = 5 } = {}) {
  const body = `<g fill="none" stroke="${c}" stroke-width="${sw}" stroke-linecap="round" stroke-linejoin="round">${ICON[n]}</g><circle cx="56" cy="8" r="3.6" fill="${dot}"/>`;
  if (!bg) return `<svg width="${s}" height="${s}" viewBox="0 0 64 64">${body}</svg>`;
  return `<svg width="${s}" height="${s}" viewBox="-14 -14 92 92"><circle cx="32" cy="32" r="46" fill="${bg}"/>${body}</svg>`;
}
