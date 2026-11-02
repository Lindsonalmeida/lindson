// Movimento dos painéis da Central (todos: clientes e administrador). Entra por último no montar de cada painel.
// Botões com elevação, brilho e "onda" no toque; cartões que sobem ao passar o mouse; entrada suave de cada tela em cascata;
// cartões que aparecem ao rolar; números dos indicadores contando; barras que enchem; topo com sombra ao rolar.
// Usa a cor de destaque de cada cliente (--amarelo). Quem pede menos movimento no aparelho não vê animação. Conta Lindson, 02/11/2026.
(() => {
const calmo = matchMedia('(prefers-reduced-motion: reduce)').matches;
document.head.insertAdjacentHTML('beforeend', `<style>
html{scroll-behavior:smooth}
.btn,.grupo a,.subabas button,.fr-tog button,.fr-chips button,.ft-filtros button{position:relative;overflow:hidden;transition:transform .18s cubic-bezier(.2,.8,.2,1),box-shadow .25s,background-color .2s,color .2s,border-color .2s}
.btn:hover{transform:translateY(-2px)}
.btn.am:hover,.btn.wa:hover{box-shadow:0 10px 24px -10px var(--amarelo)}
.btn:active,.subabas button:active,.fr-chips button:active{transform:translateY(0) scale(.96)}
.mv-onda{position:absolute;border-radius:50%;background:currentColor;opacity:.28;transform:scale(0);pointer-events:none;animation:mv-onda .6s ease-out forwards}
@keyframes mv-onda{to{transform:scale(2.6);opacity:0}}
.card{transition:transform .28s cubic-bezier(.2,.8,.2,1),border-color .28s,box-shadow .28s}
.card:hover{transform:translateY(-3px);border-color:color-mix(in srgb,var(--amarelo) 38%,var(--linha));box-shadow:0 18px 40px -24px rgba(0,0,0,.8)}
.grupo a svg{transition:transform .2s}
.grupo a:hover svg{transform:translateX(3px) scale(1.08)}
.grupo a::before{content:"";position:absolute;left:0;top:22%;bottom:22%;width:3px;border-radius:3px;background:var(--amarelo);transform:scaleY(0);transition:transform .22s}
.grupo a:hover::before,.grupo a[aria-current="page"]::before{transform:scaleY(1)}
.mv-entra{opacity:0;transform:translateY(14px)}
.mv-entra.mv-vis{opacity:1;transform:none;transition:opacity .5s ease,transform .55s cubic-bezier(.2,.8,.2,1)}
.barra i,.fr-bar i{transition:width 1s cubic-bezier(.2,.8,.2,1)}
.topo{transition:box-shadow .25s,background-color .25s}
.topo.mv-rolou{box-shadow:0 10px 30px -18px rgba(0,0,0,.9)}
#toast.on{animation:mv-toast .45s cubic-bezier(.2,1.4,.4,1)}
@keyframes mv-toast{from{transform:translate(-50%,24px) scale(.96);opacity:0}}
.fr-modal{animation:mv-fundo .25s ease}.fr-caixa{animation:mv-caixa .35s cubic-bezier(.2,1.2,.4,1)}
@keyframes mv-fundo{from{opacity:0}}@keyframes mv-caixa{from{transform:translateY(18px) scale(.97);opacity:0}}
.kpi .val{font-variant-numeric:tabular-nums}
@media (prefers-reduced-motion: reduce){*,*::before,*::after{animation:none!important;transition:none!important;scroll-behavior:auto!important}.mv-entra{opacity:1;transform:none}}
</style>`);
if (calmo) return;

// onda no toque
document.addEventListener('pointerdown', e => {
  const b = e.target.closest('.btn,.grupo a,.subabas button,.fr-tog button,.fr-chips button,.ft-filtros button'); if (!b) return;
  const r = b.getBoundingClientRect(), d = Math.max(r.width, r.height), o = document.createElement('span');
  o.className = 'mv-onda'; o.style.cssText = `width:${d}px;height:${d}px;left:${e.clientX - r.left - d / 2}px;top:${e.clientY - r.top - d / 2}px`;
  b.appendChild(o); setTimeout(() => o.remove(), 650);
}, { passive: true });

// números contando (só formatos simples: 1.050 · 29,4 mil · 9.629 · 33 · +23)
function conta(el) {
  const t = el.textContent.trim(), m = t.match(/^([+-]?)([\d.]+)(,(\d+))?(\s*mil)?$/); if (!m || el.dataset.mvContou) return;
  el.dataset.mvContou = '1';
  const alvo = parseFloat(m[2].replace(/\./g, '') + (m[4] ? '.' + m[4] : '')), dec = m[4] ? m[4].length : 0, ini = performance.now(), dur = 900;
  if (!(alvo > 0)) return;
  const fmt = v => m[1] + (dec ? v.toFixed(dec).replace('.', ',') : Math.round(v).toLocaleString('pt-BR')) + (m[5] || '');
  const passo = k => { const u = Math.min(1, (k - ini) / dur), e = 1 - Math.pow(1 - u, 3); el.textContent = fmt(alvo * e); if (u < 1) requestAnimationFrame(passo); else el.textContent = t; };
  requestAnimationFrame(passo);
}
// barras que enchem
function enche(i) { const w = i.style.width; if (!w || i.dataset.mvEncheu) return; i.dataset.mvEncheu = '1'; i.style.width = '0%'; requestAnimationFrame(() => requestAnimationFrame(() => { i.style.width = w; })); }

// entrada da tela em cascata + revelar ao rolar
const vis = new IntersectionObserver(es => es.forEach(en => { if (!en.isIntersecting) return; const el = en.target; vis.unobserve(el);
  el.classList.add('mv-vis'); el.querySelectorAll('.kpi .val').forEach(conta); el.querySelectorAll('.barra i,.fr-bar i').forEach(enche); }), { rootMargin: '0px 0px -6% 0px' });
function anima() {
  const m = document.getElementById('conteudo'); if (!m) return;
  const blocos = [...m.querySelectorAll(':scope > .card, :scope > .grade > *, :scope > .grade, :scope > section, :scope > p, :scope > .fr-barra, :scope > .fr-funil, :scope > div > .card')]
    .filter((el, i, a) => !a.some(o => o !== el && o.contains(el)) && !el.classList.contains('mv-entra'));
  blocos.forEach((el, i) => { el.classList.add('mv-entra'); el.style.transitionDelay = Math.min(i, 8) * 55 + 'ms'; vis.observe(el); setTimeout(() => { el.style.transitionDelay = ''; }, 1400); });
}
// só anima quando muda de tela (redesenhos da mesma tela, como digitar numa busca, não piscam)
let ultimo = null;
new MutationObserver(() => { const v = location.hash || '#inicio'; if (v === ultimo) return; ultimo = v; window.scrollTo({ top: 0, behavior: 'instant' }); requestAnimationFrame(anima); })
  .observe(document.getElementById('conteudo') || document.body, { childList: true });

// topo com sombra ao rolar
const topo = document.querySelector('.topo');
if (topo) addEventListener('scroll', () => topo.classList.toggle('mv-rolou', scrollY > 8), { passive: true });
})();
