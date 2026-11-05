// Aprovações e Pedidos à agência de verdade: salvos no servidor (/api/dados, f=aprov e f=ped), visíveis para a agência no painel.
// Ao pedir ajuste ou fazer um pedido, abre o WhatsApp do Lindson com a mensagem pronta (a agência fica sabendo na hora).
// O admin muda a situação do pedido (aberto → em andamento → concluído). Carregar por último no montar (encadeia o __pos). Conta Lindson, 01/11/2026.
(() => {
const H = window.__h, V = window.__V, cli = H.cli(), { APROV, PEDIDOS, chip } = H, D = window.__DADOS || {};
const toast = t => window.__toast(t), render = () => window.__render();
const esc = s => String(s ?? '').replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
const WA = '5598985621808', nome = D.nome || 'cliente';
const S = { aprov: { dados: { itens: [] }, versao: 0 }, ped: { dados: { itens: [] }, versao: 0 } };
let remoto = false, eu = 'cliente', meuNome = '';
const agora = () => new Date().toISOString(), uid = () => Date.now().toString(36) + Math.random().toString(36).slice(2, 7);
async function carrega(f) {
  try { const r = await fetch(`/api/dados?cli=${cli}&f=${f}`, { headers: { Accept: 'application/json' } });
    if (r.ok && (r.headers.get('content-type') || '').includes('json')) { const j = await r.json(); S[f] = { dados: j.dados || { itens: [] }, versao: j.versao || 0 }; eu = j.eu || eu; meuNome = j.nome || meuNome; remoto = true; } } catch (e) {}
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
function aplicaAprov() { const m = {}; (S.aprov.dados.itens || []).forEach(x => m[x.titulo] = x); APROV.forEach(p => { if (m[p.titulo]) { p.st = m[p.titulo].st; p.nota = m[p.titulo].nota; p.por = m[p.titulo].por; p.em = m[p.titulo].em; p.postado = m[p.titulo].postado; p.postadoEm = m[p.titulo].postadoEm; p.postadoPor = m[p.titulo].postadoPor; } }); }
function aplicaPed() { PEDIDOS.length = 0; (S.ped.dados.itens || []).slice().sort((a, b) => (b.em || '').localeCompare(a.em || '')).forEach(p => PEDIDOS.push([p.texto, p.st, new Date(p.em).toLocaleDateString('pt-BR'), p.id, p.resposta || ''])); }
Promise.all([carrega('aprov'), carrega('ped')]).then(() => { aplicaAprov(); aplicaPed(); render(); });
const abreWa = txt => window.open(`https://wa.me/${WA}?text=${encodeURIComponent(txt)}`, '_blank', 'noopener');

const ST = ['aberto', 'em andamento', 'concluído'];
V.pedidos = () => `<div class="grade g21"><div class="card"><h3>${eu === 'admin' ? 'Pedidos do cliente' : 'Seus pedidos'}</h3><p class="sub">${eu === 'admin' ? 'Mude a situação e responda. O cliente vê aqui.' : 'Acompanhe o que você pediu para a equipe.'}</p><div class="lista" id="lista-ped">
  ${PEDIDOS.map(p => `<div class="item" style="display:grid;gap:8px"><div style="display:flex;justify-content:space-between;gap:10px"><div style="min-width:0"><div class="t">${esc(p[0])}</div><div class="d">Aberto em ${esc(p[2])}${p[4] ? ' · Resposta: ' + esc(p[4]) : ''}</div></div><div class="fim">${chip(p[1] === 'aberto' ? 'aguardando' : p[1])}</div></div>
   ${eu === 'admin' ? `<div style="display:flex;flex-wrap:wrap;gap:6px">${ST.map(s => `<button class="btn lin" type="button" data-pst="${p[3]}" data-s="${s}" style="padding:5px 10px;font-size:12px" ${s === p[1] ? 'disabled' : ''}>${s}</button>`).join('')}<button class="btn lin" type="button" data-presp="${p[3]}" style="padding:5px 10px;font-size:12px">Responder</button></div>` : ''}</div>`).join('') || '<div class="vazio" style="color:var(--apagado);font-size:13px">Nenhum pedido ainda.</div>'}</div></div>
 ${eu === 'admin' ? '<div class="card"><h3>Painel da agência</h3><p class="sub" style="margin:0">Você está vendo como administrador. Os pedidos chegam aqui e no seu WhatsApp.</p></div>' : `<form class="card" id="novo-ped"><h3>Fazer um pedido</h3><p class="sub">Arte, ajuste, post novo, dúvida... a equipe responde em até 1 dia útil.</p><div style="display:grid;gap:10px"><label for="ped-t" class="sub" style="margin:0">O que você precisa?</label><textarea id="ped-t" maxlength="800" placeholder="Ex.: preciso de um post sobre o horário de fim de ano" required></textarea><button class="btn am" type="submit">Enviar pedido</button><span class="sub" style="margin:0;font-size:12px">Ao enviar, o WhatsApp abre com o pedido para avisar a equipe.</span></div></form>`}</div>`;

let abaAp = null;
const grupoDe = p => p.postado ? 'post' : p.st === 'aprovado' ? 'apr' : p.st === 'em revisão' ? 'aj' : 'pend';  // pedido de ajuste muda a arte de aba (pedido do Lindson, 05/11/2026)
function abasAprov(m) {
  const cards = [...m.querySelectorAll('.post')]; if (!cards.length || cards.length !== APROV.length) return;
  const n = { pend: 0, aj: 0, apr: 0, post: 0 }; APROV.forEach(p => n[grupoDe(p)]++);
  if (!abaAp) abaAp = n.pend ? 'pend' : n.aj ? 'aj' : n.apr ? 'apr' : 'post';
  const box = m.querySelector('.posts'); if (!box) return;
  const ab = document.createElement('div'); ab.className = 'subabas'; ab.style.margin = '6px 0 16px';
  ab.innerHTML = [['pend', 'Para aprovar'], ['aj', 'Em ajuste'], ['apr', 'Aprovados · a postar'], ['post', 'Postados']].map(([k, t]) => `<button type="button" data-abaap="${k}" class="${k === abaAp ? 'on' : ''}">${t} (${n[k]})</button>`).join('');
  box.parentNode.insertBefore(ab, box);
  ab.querySelectorAll('[data-abaap]').forEach(b => b.onclick = () => { abaAp = b.dataset.abaap; render(); });
  cards.forEach((c, i) => {
    const p = APROV[i], g = grupoDe(p); c.style.display = g === abaAp ? '' : 'none';
    const alvo = c.querySelector('.c') || c;
    // botão de baixar a arte em todos os cards (pedido do Lindson, 03/11/2026); carrossel baixa TODAS as telas de uma vez (pedido 04/11, conta Leandro)
    window.__APROV = APROV;
    const nomeArq = String(p.titulo || 'arte').normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/[^A-Za-z0-9]+/g, '-').replace(/^-|-$/g, '').toLowerCase();
    if (p.img && !c.querySelector('[data-baixar]')) alvo.insertAdjacentHTML('beforeend', (p.telas && p.telas.length)
      ? `<button class="btn lin" type="button" data-baixar data-baixarcar="${i}" style="display:block;width:100%;text-align:center;margin-top:10px">⬇ Baixar carrossel (${p.telas.length + 1} telas)</button>`
      : `<a class="btn lin" data-baixar href="${p.img}" download="${nomeArq}.jpg" style="display:block;text-align:center;margin-top:10px">⬇ Baixar arte</a>`);
    if (g === 'aj') alvo.insertAdjacentHTML('beforeend', `<div style="font-size:12.5px;margin-top:10px;padding:10px 12px;border-radius:10px;background:rgba(255,194,14,.1);border:1px solid rgba(255,194,14,.35)"><b>✎ Ajuste pedido</b>${p.por ? ' por ' + esc(p.por) : ''}${p.em ? ', ' + new Date(p.em).toLocaleDateString('pt-BR') : ''}<br>${esc(p.nota || '(sem detalhe)')}</div>` + (eu === 'admin' ? `<button class="btn am" type="button" data-volta="${i}" style="margin-top:10px;width:100%">↩ Corrigida, voltar para aprovação</button>` : `<div style="font-size:12px;color:var(--apagado);margin-top:6px">A equipe está ajustando. Quando ficar pronta, ela volta para "Para aprovar".</div>`));
    if (g === 'apr') alvo.insertAdjacentHTML('beforeend', `<button class="btn am" type="button" data-postei="${i}" style="margin-top:10px;width:100%">✓ Marquei como postado</button>`);
    if (g === 'post') alvo.insertAdjacentHTML('beforeend', `<div style="font-size:12px;color:#4ADE80;margin-top:6px">📌 Postado${p.postadoPor ? ' por ' + esc(p.postadoPor) : ''}${p.postadoEm ? ', ' + new Date(p.postadoEm).toLocaleDateString('pt-BR') : ''}</div><button class="btn lin" type="button" data-despostei="${i}" style="margin-top:8px;width:100%;font-size:12px">Desfazer (voltar para "a postar")</button>`);
  });
  if (!m.querySelector('.post:not([style*="none"])')) box.insertAdjacentHTML('afterbegin', `<p class="sub" data-vazio>Nada aqui por enquanto.</p>`);
  const marca = (i, v) => async () => { const p = APROV[i]; if (!p) return;
    if (await muda('aprov', d => { d.itens = d.itens || []; let x = d.itens.find(y => y.titulo === p.titulo); if (!x) { x = { titulo: p.titulo, st: p.st, em: p.em }; d.itens.push(x); } x.postado = v; x.postadoEm = v ? agora() : null; x.postadoPor = v ? (meuNome || eu) : null; })) {
      p.postado = v; p.postadoEm = v ? agora() : null; p.postadoPor = v ? (meuNome || eu) : null; toast(v ? 'Marcado como postado. Foi para a aba Postados.' : 'Voltou para "a postar".'); render(); } };
  m.querySelectorAll('[data-postei]').forEach(b => b.onclick = marca(+b.dataset.postei, true));
  m.querySelectorAll('[data-despostei]').forEach(b => b.onclick = marca(+b.dataset.despostei, false));
  m.querySelectorAll('[data-volta]').forEach(b => b.onclick = async () => { const p = APROV[+b.dataset.volta]; if (!p) return;
    if (await muda('aprov', d => { d.itens = (d.itens || []).filter(x => x.titulo !== p.titulo); d.itens.push({ titulo: p.titulo, st: 'aguardando', em: agora(), por: meuNome || eu }); })) { p.st = 'aguardando'; p.nota = ''; toast('Voltou para "Para aprovar".'); render(); } });
}
const anterior = window.__pos;
window.__pos = view => {
  if (anterior) anterior(view);
  const m = document.getElementById('conteudo'); if (!m) return;
  // aprovações (sobrepõe o botão do modelo, que não salvava)
  m.querySelectorAll('[data-ap]').forEach(b => b.onclick = async () => {
    const p = APROV[+b.dataset.ap]; if (!p) return;
    if (await muda('aprov', d => { d.itens = (d.itens || []).filter(x => x.titulo !== p.titulo); d.itens.push({ titulo: p.titulo, st: 'aprovado', em: agora(), por: meuNome || eu }); })) { p.st = 'aprovado'; p.por = meuNome || eu; p.em = agora(); toast('Aprovado! A equipe já vê no painel.'); render(); }
  });
  m.querySelectorAll('[data-aj]').forEach(b => b.onclick = async () => {
    const p = APROV[+b.dataset.aj]; if (!p) return;
    const nota = prompt(`O que você quer mudar em "${p.titulo}"?`); if (nota === null) return;
    if (await muda('aprov', d => { d.itens = (d.itens || []).filter(x => x.titulo !== p.titulo); d.itens.push({ titulo: p.titulo, st: 'em revisão', nota: nota.trim().slice(0, 500), em: agora(), por: meuNome || eu }); })) {
      p.st = 'em revisão'; p.nota = nota; p.por = meuNome || eu; p.em = agora(); abaAp = 'aj'; render(); toast(eu === 'admin' ? 'Pedido de ajuste salvo. A arte foi para a aba Em ajuste.' : 'Pedido de ajuste salvo. A arte foi para a aba Em ajuste e o WhatsApp vai abrir para avisar a equipe.');
      if (eu !== 'admin') abreWa(`Oi, Lindson! Pedi ajuste num post na Central (${nome}):\n"${p.titulo}"\n${nota.trim() || '(sem detalhe)'}`);
    }
  });
  // abas das aprovações: Para aprovar · Aprovados (a postar) · Postados. Botão "Marquei como postado" muda o post de aba (03/11/2026)
  if (view === 'aprovacoes') abasAprov(m);
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

// Baixar carrossel inteiro: no celular abre o "Compartilhar" com todas as telas (Salvar imagens na galeria); no computador baixa um .zip
// com as telas em ordem (01, 02…). Zip sem compressão feito aqui mesmo, sem biblioteca. Conta Leandro, 04/11/2026.
window.__zipTelas = window.__zipTelas || (() => {
  const T = new Uint32Array(256).map((_, n) => { let c = n; for (let k = 0; k < 8; k++) c = c & 1 ? 0xEDB88320 ^ (c >>> 1) : c >>> 1; return c >>> 0; });
  const crc = b => { let c = 0xFFFFFFFF; for (let i = 0; i < b.length; i++) c = T[(c ^ b[i]) & 255] ^ (c >>> 8); return (c ^ 0xFFFFFFFF) >>> 0; };
  return arqs => { const enc = new TextEncoder(), partes = [], dir = []; let pos = 0;
    for (const { nome, dados } of arqs) { const n = enc.encode(nome), c = crc(dados), h = new DataView(new ArrayBuffer(30));
      [[0, 0x04034b50, 4], [4, 20, 2], [8, 0, 2], [14, c, 4], [18, dados.length, 4], [22, dados.length, 4], [26, n.length, 2]].forEach(([o, v, t]) => t === 4 ? h.setUint32(o, v, true) : h.setUint16(o, v, true));
      partes.push(new Uint8Array(h.buffer), n, dados);
      const d = new DataView(new ArrayBuffer(46)); [[0, 0x02014b50, 4], [4, 20, 2], [6, 20, 2], [16, c, 4], [20, dados.length, 4], [24, dados.length, 4], [28, n.length, 2], [42, pos, 4]].forEach(([o, v, t]) => t === 4 ? d.setUint32(o, v, true) : d.setUint16(o, v, true));
      dir.push(new Uint8Array(d.buffer), n); pos += 30 + n.length + dados.length; }
    const tam = dir.reduce((s, x) => s + x.length, 0), f = new DataView(new ArrayBuffer(22));
    [[0, 0x06054b50, 4], [8, arqs.length, 2], [10, arqs.length, 2], [12, tam, 4], [16, pos, 4]].forEach(([o, v, t]) => t === 4 ? f.setUint32(o, v, true) : f.setUint16(o, v, true));
    return new Blob([...partes, ...dir, new Uint8Array(f.buffer)], { type: 'application/zip' }); };
})();
window.__telasProntas = window.__telasProntas || {};
document.addEventListener('click', async e => {
  const b = e.target.closest('[data-baixarcar]'); if (!b) return; e.preventDefault();
  const idx = +b.dataset.baixarcar, p = (window.__APROV || [])[idx]; if (!p) return;
  const base = String(p.titulo || 'carrossel').normalize('NFD').replace(/[\u0300-\u036f]/g, '').replace(/[^A-Za-z0-9]+/g, '-').replace(/^-|-$/g, '').toLowerCase();
  const celular = /Android|iPhone|iPad|iPod/i.test(navigator.userAgent) && !!navigator.canShare;
  const pronto = window.__telasProntas[idx];
  if (celular && pronto) {   // 2º toque: o Safari só abre o Compartilhar direto no toque, por isso as telas já estão carregadas
    try { await navigator.share({ files: pronto, title: p.titulo || 'Carrossel' }); } catch (err) {}
    return;
  }
  const urls = [p.img, ...(p.telas || [])], txt = b.dataset.txt || b.textContent; b.dataset.txt = txt; b.disabled = true; b.textContent = 'Preparando as telas…';
  try {
    const blobs = await Promise.all(urls.map(u => fetch(u).then(r => { if (!r.ok) throw new Error(r.status); return r.blob(); })));
    const files = blobs.map((x, k) => new File([x], `${base}-${String(k + 1).padStart(2, '0')}.jpg`, { type: x.type || 'image/jpeg' }));
    if (celular && navigator.canShare({ files })) { window.__telasProntas[idx] = files; b.disabled = false; b.textContent = `Toque de novo para salvar as ${files.length} telas`; return; }
    const z = window.__zipTelas(await Promise.all(files.map(async f => ({ nome: f.name, dados: new Uint8Array(await f.arrayBuffer()) }))));
    const a = document.createElement('a'); a.href = URL.createObjectURL(z); a.download = base + '.zip'; document.body.appendChild(a); a.click(); setTimeout(() => { URL.revokeObjectURL(a.href); a.remove(); }, 4000);
  } catch (err) { alert('Não consegui baixar agora. Tente de novo.'); }
  b.disabled = false; b.textContent = txt;
});
