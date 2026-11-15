/* Aba "Arquivos" do painel SF: tudo o que as contas fizeram para o cliente (conta Zuleide, 15/11/2026).
   Arquivos em CentralLindsonALmeida/painel/sf/ (atrás do login). Item novo: acrescente uma linha em ARQ. */
(() => {
const B = '/painel/sf/', ST = { aprovado: ['Aprovado', '#4ADE80'], aguardando: ['Aguardando aprovação', '#FFB020'], reprovado: ['Reprovado (refeito na v2)', '#F87171'], 'no ar': ['No ar', '#4ADE80'] };
const MOT = [['01', 'vaso-agua-subiu', 'Deu descarga e a água subiu?'], ['02', 'vaso-tres-sinais', 'Vaso entupido: 3 sinais'], ['03', 'ralo-agua-parada', 'Água parada no box?'], ['04', 'ralo-antes-depois', 'Pia: antes e depois'], ['05', 'caixa-de-gordura', 'Caixa de gordura no restaurante']];
const ARQ = [
  ...MOT.map(([n, s, t]) => ({ tipo: 'Vídeos', t: `Motion v2 · ${n} · ${t}`, data: '14/11/2026', conta: 'Zuleide', st: 'aguardando', video: `${B}videos/sf-motion-v2-${n}-${s}.mp4`, capa: `${B}artes/capa-motion-v2-${n}.jpg` })),
  ...MOT.map(([n, s, t]) => ({ tipo: 'Vídeos', t: `Motion v1 · ${n} · ${t}`, data: '14/11/2026', conta: 'Zuleide', st: 'reprovado', video: `${B}videos/sf-motion-${n}-${s}.mp4`, capa: `${B}artes/capa-motion-${n}.jpg` })),
  ...[['p1-socorro-rapido', 'Socorro rápido'], ['p2-evite-o-prejuizo', 'Evite o prejuízo'], ['p3-bastidores', 'Bastidores do serviço'], ['p4-fala-com-a-gente', 'Fala com a gente']].map(([f, t]) => ({ tipo: 'Artes', t: `Feed v1 · ${t}`, data: '03/11/2026', conta: 'Zuleide', st: 'aprovado', img: `${B}artes/${f}.jpg` })),
  { tipo: 'Artes', t: 'Prévia do feed v1', data: '03/11/2026', conta: 'Zuleide', st: 'aprovado', img: `${B}artes/previa-feed.jpg` },
  { tipo: 'Identidade', t: 'Logo oficial', data: 'do cliente', conta: 'cliente', st: 'aprovado', img: `${B}artes/logo-sf.jpg` },
  { tipo: 'Identidade', t: 'Flyer de serviços', data: 'do cliente', conta: 'cliente', st: 'aprovado', img: `${B}artes/flyer-servicos.jpg` },
  { tipo: 'Site', t: 'Site desentupidorasf.pages.dev', data: '26/10/2026', conta: 'Lindson', st: 'no ar', img: `${B}artes/site-celular.jpg`, link: 'https://desentupidorasf.pages.dev' },
];
const TIPOS = ['Vídeos', 'Artes', 'Carrosséis', 'Identidade', 'Site'];
const V = window.__V, T = window.__T;
if (T) T.arquivos = 'Arquivos';
V.arquivos = () => TIPOS.map(tp => {
  const l = ARQ.filter(a => a.tipo === tp);
  const cor = `<div style="display:flex;gap:6px;align-items:center;font-size:12px;color:var(--apagado)">`;
  return `<div class="card" style="margin-bottom:16px"><h3>${tp} <span class="sub" style="font-size:13px">(${l.length})</span></h3>${l.length ? `<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,220px),1fr));gap:14px">${l.map(a => {
    const [nome, c] = ST[a.st] || [a.st, 'var(--apagado)'];
    const midia = a.video ? `<video controls playsinline preload="none" poster="${a.capa}" src="${a.video}" style="width:100%;aspect-ratio:9/16;object-fit:cover;border-radius:12px;background:#000;display:block"></video>`
      : `<a href="${a.link || a.img}" target="_blank" rel="noopener"><img loading="lazy" src="${a.img}" alt="${a.t}" style="width:100%;aspect-ratio:4/5;object-fit:cover;border-radius:12px;display:block"></a>`;
    const arq = a.video || a.img;
    return `<div>${midia}<div style="font-weight:700;margin:8px 0 4px;font-size:14px">${a.t}</div>${cor}<span style="width:8px;height:8px;border-radius:50%;background:${c}"></span><b style="color:${c}">${nome}</b></div><div style="font-size:12px;color:var(--apagado);margin:2px 0 8px">${a.data} · conta ${a.conta}</div><a class="btn lin" href="${arq}" download>Baixar</a>${a.link ? ` <a class="btn lin" href="${a.link}" target="_blank" rel="noopener">Abrir site</a>` : ''}</div>`;
  }).join('')}</div>` : '<p class="sub" style="margin:0">Nada ainda.</p>'}</div>`;
}).join('');
})();
