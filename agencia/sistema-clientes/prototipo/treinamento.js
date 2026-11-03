// Aba "Treinamento" do painel: vídeos para a equipe do cliente aprender, incorporados (assiste sem sair da Central) e com o link do YouTube de reserva.
// Lista em window.__DADOS.treinamento = [{titulo, youtube, para, sobre}] (dados do cliente no repositório privado). Sem lista, a aba não aparece.
// "Já assisti" fica salvo neste aparelho. Conta Lindson, 03/11/2026.
(() => {
const D = window.__DADOS || {}, V = window.__V, T = window.__T, L = D.treinamento || [];
if (!L.length || !V) return;
const esc = s => String(s ?? '').replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
const id = u => (String(u).match(/(?:youtu\.be\/|v=|embed\/|shorts\/)([\w-]{11})/) || [])[1];
const CH = 'treino-' + (D.cliente || ''); let vistos = {}; try { vistos = JSON.parse(localStorage.getItem(CH) || '{}'); } catch (e) {}
T.treinamento = 'Treinamento';
const ent = document.querySelector('[data-v="entregas"]');
if (ent && !document.querySelector('[data-v="treinamento"]')) ent.insertAdjacentHTML('afterend', '<a href="#treinamento" data-v="treinamento"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="5" width="18" height="13" rx="2"/><path d="m10 9 5 2.5-5 2.5z"/><path d="M8 21h8"/></svg>Treinamento</a>');
V.treinamento = () => `<div class="card"><h3>Treinamento da equipe</h3><p class="sub">Vídeos escolhidos pela agência para a equipe aprender. Assista aqui mesmo e marque quando terminar. ${L.filter(v => vistos[id(v.youtube)]).length} de ${L.length} assistidos.</p></div>
 <div class="grade g2">${L.map(v => { const k = id(v.youtube); return `<div class="card">
  <div style="position:relative;aspect-ratio:16/9;border-radius:12px;overflow:hidden;background:#000"><iframe src="https://www.youtube-nocookie.com/embed/${k}?rel=0" title="${esc(v.titulo)}" style="position:absolute;inset:0;width:100%;height:100%;border:0" allow="accelerometer; encrypted-media; gyroscope; picture-in-picture; fullscreen" allowfullscreen referrerpolicy="strict-origin-when-cross-origin" loading="lazy"></iframe></div>
  <h3 style="margin-top:14px">${esc(v.titulo)}</h3>${v.para ? `<p class="sub" style="margin:4px 0">Para: ${esc(v.para)}</p>` : ''}${v.sobre ? `<p style="margin:6px 0 12px;line-height:1.5">${esc(v.sobre)}</p>` : ''}
  <div style="display:flex;gap:8px;flex-wrap:wrap"><button class="btn ${vistos[k] ? 'lin' : 'am'}" type="button" data-visto="${k}">${vistos[k] ? '✓ Assistido' : 'Marcar como assistido'}</button><a class="btn lin" href="https://youtu.be/${k}" target="_blank" rel="noopener">Abrir no YouTube</a></div></div>`; }).join('')}</div>`;
const ant = window.__pos;
window.__pos = view => { if (ant) ant(view); if (view !== 'treinamento') return;
  document.querySelectorAll('[data-visto]').forEach(b => b.onclick = () => { const k = b.dataset.visto; vistos[k] = !vistos[k]; try { localStorage.setItem(CH, JSON.stringify(vistos)); } catch (e) {} window.__render(); }); };
})();
