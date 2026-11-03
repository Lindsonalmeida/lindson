// Aprovações e Pedidos à agência de verdade: salvos no servidor (/api/dados, f=aprov e f=ped), visíveis para a agência no painel.
// Ao pedir ajuste ou fazer um pedido, abre o WhatsApp do Lindson com a mensagem pronta (a agência fica sabendo na hora).
// O admin muda a situação do pedido (aberto → em andamento → concluído). Carregar por último no montar (encadeia o __pos). Conta Lindson, 01/11/2026.
(() => {
const H = window.__h, V = window.__V, cli = H.cli(), { APROV, PEDIDOS, chip } = H, D = window.__DADOS || {};
const toast = t => window.__toast(t), render = () => window.__render();
const esc = s => String(s ?? '').replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
const WA = '5598985621808', nome = D.nome || 'cliente';
const S = { aprov: { dados: { itens: [] }, versao: 0 }, ped: { dados: { itens: [] }, versao: 0 } };
let remoto = false, eu = 'cliente';
const agora = () => new Date().toISOString(), uid = () => Date.now().toString(36) + Math.random().toString(36).slice(2, 7);
async function carrega(f) {
  try { const r = await fetch(`/api/dados?cli=${cli}&f=${f}`, { headers: { Accept: 'application/json' } });
    if (r.ok && (r.headers.get('content-type') || '').includes('json')) { const j = await r.json(); S[f] = { dados: j.dados || { itens: [] }, versao: j.versao || 0 }; eu = j.eu || eu; remoto = true; } } catch (e) {}
}
async function muda(f, fn) {
  if (!remoto) { fn(S[f].dados); return true; }
  for (let t = 0; t < 4; t++) {
    const copia = JSON.parse(JSON.stringify(S[f].dados)); fn(copia);
    const r = await fetch(`/api/dados?cli=${cli}&f=${f}`, { method: 'PUT', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ dados: copia, versao: S[f].versao }) });
    if (r.ok) { S[f] = { dados: copia, versao: (await r.json()).versao }; return true; }
    if (r.status === 409) { const j = await r.json(); S[f] = { dados: j.dados || { itens: [] }, versao: j.versao }; continue; }
    toast(r.status === 401 ? 'Sua sessão expirou. Entre de novo.' : 'Não consegui salvar agora. Tente de novo.'); return false;
  }
  return false;
}
// aplica as aprovações salvas nos posts do painel (pelo título)
function aplicaAprov() { const m = {}; (S.aprov.dados.itens || []).forEach(x => m[x.titulo] = x); APROV.forEach(p => { if (m[p.titulo]) { p.st = m[p.titulo].st; p.nota = m[p.titulo].nota; p.por = m[p.titulo].por; p.em = m[p.titulo].em; } }); }
function aplicaPed() { PEDIDOS.length = 0; (S.ped.dados.itens || []).slice().sort((a, b) => (b.em || '').localeCompare(a.em || '')).forEach(p => PEDIDOS.push([p.texto, p.st, new Date(p.em).toLocaleDateString('pt-BR'), p.id, p.resposta || ''])); }
Promise.all([carrega('aprov'), carrega('ped')]).then(() => { aplicaAprov(); aplicaPed(); render(); });
const abreWa = txt => window.open(`https://wa.me/${WA}?text=${encodeURIComponent(txt)}`, '_blank', 'noopener');

const ST = ['aberto', 'em andamento', 'concluído'];
V.pedidos = () => `<div class="grade g21"><div class="card"><h3>${eu === 'admin' ? 'Pedidos do cliente' : 'Seus pedidos'}</h3><p class="sub">${eu === 'admin' ? 'Mude a situação e responda. O cliente vê aqui.' : 'Acompanhe o que você pediu para a equipe.'}</p><div class="lista" id="lista-ped">
  ${PEDIDOS.map(p => `<div class="item" style="display:grid;gap:8px"><div style="display:flex;justify-content:space-between;gap:10px"><div style="min-width:0"><div class="t">${esc(p[0])}</div><div class="d">Aberto em ${esc(p[2])}${p[4] ? ' · Resposta: ' + esc(p[4]) : ''}</div></div><div class="fim">${chip(p[1] === 'aberto' ? 'aguardando' : p[1])}</div></div>
   ${eu === 'admin' ? `<div style="display:flex;flex-wrap:wrap;gap:6px">${ST.map(s => `<button class="btn lin" type="button" data-pst="${p[3]}" data-s="${s}" style="padding:5px 10px;font-size:12px" ${s === p[1] ? 'disabled' : ''}>${s}</button>`).join('')}<button class="btn lin" type="button" data-presp="${p[3]}" style="padding:5px 10px;font-size:12px">Responder</button></div>` : ''}</div>`).join('') || '<div class="vazio" style="color:var(--apagado);font-size:13px">Nenhum pedido ainda.</div>'}</div></div>
 ${eu === 'admin' ? '<div class="card"><h3>Painel da agência</h3><p class="sub" style="margin:0">Você está vendo como administrador. Os pedidos chegam aqui e no seu WhatsApp.</p></div>' : `<form class="card" id="novo-ped"><h3>Fazer um pedido</h3><p class="sub">Arte, ajuste, post novo, dúvida... a equipe responde em até 1 dia útil.</p><div style="display:grid;gap:10px"><label for="ped-t" class="sub" style="margin:0">O que você precisa?</label><textarea id="ped-t" maxlength="800" placeholder="Ex.: preciso de um post sobre o horário de fim de ano" required></textarea><button class="btn am" type="submit">Enviar pedido</button><span class="sub" style="margin:0;font-size:12px">Ao enviar, o WhatsApp abre com o pedido para avisar a equipe.</span></div></form>`}</div>`;

const anterior = window.__pos;
window.__pos = view => {
  if (anterior) anterior(view);
  const m = document.getElementById('conteudo'); if (!m) return;
  // aprovações (sobrepõe o botão do modelo, que não salvava)
  m.querySelectorAll('[data-ap]').forEach(b => b.onclick = async () => {
    const p = APROV[+b.dataset.ap]; if (!p) return;
    if (await muda('aprov', d => { d.itens = (d.itens || []).filter(x => x.titulo !== p.titulo); d.itens.push({ titulo: p.titulo, st: 'aprovado', em: agora(), por: eu }); })) { p.st = 'aprovado'; p.por = eu; p.em = agora(); toast('Aprovado! A equipe já vê no painel.'); render(); }
  });
  m.querySelectorAll('[data-aj]').forEach(b => b.onclick = async () => {
    const p = APROV[+b.dataset.aj]; if (!p) return;
    const nota = prompt(`O que você quer mudar em "${p.titulo}"?`); if (nota === null) return;
    if (await muda('aprov', d => { d.itens = (d.itens || []).filter(x => x.titulo !== p.titulo); d.itens.push({ titulo: p.titulo, st: 'em revisão', nota: nota.trim().slice(0, 500), em: agora(), por: eu }); })) {
      p.st = 'em revisão'; p.nota = nota; render(); toast('Pedido de ajuste salvo. Abrindo o WhatsApp para avisar a equipe.');
      if (eu !== 'admin') abreWa(`Oi, Lindson! Pedi ajuste num post na Central (${nome}):\n"${p.titulo}"\n${nota.trim() || '(sem detalhe)'}`);
    }
  });
  // pedidos: o modelo liga o formulário depois deste __pos; por isso trocamos no próximo ciclo
  setTimeout(() => {
    const f = m.querySelector('#novo-ped'); if (f) f.onsubmit = async e => {
      e.preventDefault(); const t = (m.querySelector('#ped-t').value || '').trim(); if (!t) return;
      const novo = { id: uid(), texto: t.slice(0, 800), st: 'aberto', em: agora(), por: eu };
      if (await muda('ped', d => { d.itens = [...(d.itens || []), novo]; })) { aplicaPed(); render(); toast('Pedido salvo. Abrindo o WhatsApp para avisar a equipe.'); abreWa(`Oi, Lindson! Fiz um pedido na Central (${nome}):\n${t}`); }
    };
  }, 0);
  m.querySelectorAll('[data-pst]').forEach(b => b.onclick = async () => { if (await muda('ped', d => { const x = d.itens.find(y => y.id === b.dataset.pst); if (x) { x.st = b.dataset.s; x.atualizado = agora(); } })) { aplicaPed(); render(); toast('Situação do pedido atualizada.'); } });
  m.querySelectorAll('[data-presp]').forEach(b => b.onclick = async () => { const r = prompt('Resposta para o cliente:'); if (!r) return; if (await muda('ped', d => { const x = d.itens.find(y => y.id === b.dataset.presp); if (x) { x.resposta = r.trim().slice(0, 500); x.atualizado = agora(); } })) { aplicaPed(); render(); toast('Resposta salva. O cliente vê no painel.'); } });
};
})();
