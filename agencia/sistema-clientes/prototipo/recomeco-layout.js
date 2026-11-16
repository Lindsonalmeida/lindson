// Recomeço 90 v2 · layout de computador e linha do tempo dos 90 dias (conta Leandro, 16/11/2026).
// Só move os blocos que já existem (mesmos ids, mesmos eventos) para 3 colunas no computador e devolve no celular.
(() => {
const app = document.getElementById('app'); if (!app) return;
const $ = id => document.getElementById(id);
const mq = matchMedia('(min-width: 980px)');
// linha do tempo (todas as larguras), logo abaixo do topo
const hud = app.querySelector('.hud');
const tl = document.createElement('div'); tl.className = 'r9-tl'; tl.setAttribute('aria-hidden', 'true');
tl.innerHTML = '<div class="r9-tl-h"><b id="r9-dia">1<em>/90</em></b><span id="r9-falta"></span></div><div class="r9-ticks">' + '<i></i>'.repeat(90) + '</div><div class="r9-ph"><span>Fase 1 · Sobreviver</span><span>Fase 2 · Estabilizar</span><span>Fase 3 · Organizar</span></div>';
hud.after(tl);
function linha() {
  const m = ($('hud-day').textContent || '').match(/Dia\s+(\d+)/); const n = m ? +m[1] : 1;
  $('r9-dia').innerHTML = Math.min(n, 90) + '<em>/90</em>';
  $('r9-falta').textContent = n < 90 ? 'faltam ' + (90 - n) + ' dias' : 'ciclo completo';
  tl.querySelectorAll('.r9-ticks i').forEach((t, i) => { t.className = (i + 1 < n ? 'p' : i + 1 === n ? 'c' : '') + ((i + 1) % 30 === 1 ? ' f' : ''); });
  tl.querySelectorAll('.r9-ph span').forEach((s, i) => s.classList.toggle('on', n > i * 30 && n <= (i + 1) * 30));
}
linha(); new MutationObserver(linha).observe($('hud-day'), { childList: true, characterData: true, subtree: true });
// colunas
const pecas = { esq: ['.score', '#phase'], dir: ['#counter', '#r9-dia-h', '#daily', '#p-hoje > .hint'] };
const hoje = $('p-hoje'); const dh = $('daily').previousElementSibling; if (dh) dh.id = 'r9-dia-h';
const lugares = new Map();
let mont = null;
function monta() {
  if (mont) return;
  const top = document.createElement('div'); top.className = 'r9-top';
  const esq = document.createElement('aside'); esq.className = 'r9-esq'; esq.setAttribute('aria-label', 'Placar');
  const meio = document.createElement('div'); meio.className = 'r9-meio';
  const dir = document.createElement('aside'); dir.className = 'r9-dir'; dir.setAttribute('aria-label', 'Hoje');
  const mover = (sel, alvo) => { const el = typeof sel === 'string' ? app.querySelector(sel) : sel; if (!el) return; const ph = document.createComment('r9'); el.before(ph); lugares.set(el, ph); alvo.appendChild(el); };
  app.prepend(top, esq, meio, dir);
  mover('.hud', top); mover('.r9-tl', top);
  pecas.esq.forEach(s => mover(s, esq));
  pecas.dir.forEach(s => mover(s, dir));
  [...app.children].filter(e => ![top, esq, meio, dir].includes(e) && !e.matches('.foot,.dsp,.toast,.pop') && !e.matches('#dsp')).forEach(e => mover(e, meio));
  app.classList.add('r9-desk'); mont = [top, esq, meio, dir];
}
function desmonta() {
  if (!mont) return;
  lugares.forEach((ph, el) => { ph.replaceWith(el); }); lugares.clear();
  mont.forEach(e => e.remove()); mont = null; app.classList.remove('r9-desk');
}
const aplica = () => (mq.matches ? monta() : desmonta());
aplica(); mq.addEventListener('change', aplica);
// microinteração: a onda do movimento.js nos botões principais
document.querySelectorAll('.tabs button,.counter .btns button,.fu-new,.dsp-go,.form button.add,.deck-nav button').forEach(b => b.classList.add('btn'));
})();
