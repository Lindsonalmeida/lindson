// Telas do painel do ADMINISTRADOR (Lindson) dentro do modelo da Central (prototipo/painel.html), montado pelo montar-site.py.
// Dados: window.__CLIENTES (resumo real de cada cliente) e window.__APPS (apps do Lindson), ambos do repositório privado.
// Números ao vivo (fotos, CRM, demandas, pedidos, ajustes, contas) vêm do servidor da Central. Conta Lindson, 02/11/2026.
(() => {
const H = window.__h, V = window.__V, T = window.__T, chip = H.chip, CL = window.__CLIENTES || [], AP = window.__APPS || { abas: [], repetidos: [] };
const esc = s => String(s ?? '').replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
const n = v => v == null || v === '' ? 'a medir' : typeof v === 'number' ? v.toLocaleString('pt-BR') : esc(v);
const render = () => window.__render(), toast = t => window.__toast(t);
const VIVO = {}; let contas = null, carregou = false;
const pega = async url => { try { const r = await fetch(url, { headers: { Accept: 'application/json' } }); return r.ok && (r.headers.get('content-type') || '').includes('json') ? r.json() : null; } catch (e) { return null; } };
const itens = j => (j && j.dados && j.dados.itens) || [];
async function carrega() {
  await Promise.all(CL.map(async c => {
    const [f, x, p, a] = await Promise.all([pega(`/api/fotos?cli=${c.cliente}`), pega(`/api/dados?cli=${c.cliente}&f=${c.cliente === 'leo' ? 'dem' : 'crm'}`), pega(`/api/dados?cli=${c.cliente}&f=ped`), pega(`/api/dados?cli=${c.cliente}&f=aprov`)]);
    VIVO[c.cliente] = { fotos: f ? (f.fotos || []).length : null, extra: x ? itens(x).length : null, ped: p ? itens(p).filter(i => i.st !== 'concluído') : [], aj: a ? itens(a).filter(i => i.st === 'em revisão') : [] };
  }));
  const cj = await pega('/api/contas'); contas = cj ? cj.contas : null; carregou = true; render();
}
carrega();
const soma = k => carregou ? CL.reduce((s, c) => s + ((VIVO[c.cliente] || {})[k] || 0), 0) : '…';
const conta = k => carregou ? CL.reduce((s, c) => s + (((VIVO[c.cliente] || {})[k]) || []).length, 0) : '…';
const kpi = (r, v, nota, cls) => `<div class="card kpi"><div class="rot">${r}</div><div class="val">${v}</div><div class="var ${cls || 'up'}"><span>${nota || ''}</span></div></div>`;
const nomeCli = c => (CL.find(x => x.cliente === c) || {}).nome || c;

function novidades() {
  const l = [];
  CL.forEach(c => { const v = VIVO[c.cliente] || {}; (v.ped || []).forEach(p => l.push({ c: c.cliente, t: 'Pedido: ' + p.texto, d: p.em, h: '#pedidos', st: p.st })); (v.aj || []).forEach(a => l.push({ c: c.cliente, t: 'Ajuste no post "' + a.titulo + '"' + (a.nota ? ': ' + a.nota : ''), d: a.em, h: '#aprovacoes', st: 'em revisão' })); });
  return l.sort((a, b) => (b.d || '').localeCompare(a.d || ''));
}
const cartaoCli = c => { const ig = c.instagram || {}, v = VIVO[c.cliente] || {};
  return `<div class="card"><h3>${esc(c.nome)}</h3><p class="sub">${esc(c.seg)} · ${esc(ig.perfil || '')}</p>
   <div class="grade g2" style="gap:10px">${[['Seguidores', n(ig.seguidores), ig.var_seguidores], ['Visualizações 30 dias', n(ig.visualizacoes), ig.var_visualizacoes || ig.periodo], ['Fotos recebidas', carregou ? n(v.fotos) : '…', ''], [c.cliente === 'leo' ? 'Demandas' : 'Pacientes no CRM', carregou ? n(v.extra) : '…', '']]
     .map(([r, val, nt]) => `<div style="background:var(--painel2);border:1px solid var(--linha);border-radius:12px;padding:12px"><div class="rot" style="font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:var(--apagado)">${r}</div><div style="font:800 26px/1.15 var(--f-titulo);margin-top:4px">${val}</div><div class="var up"><span>${esc(nt || '')}</span></div></div>`).join('')}</div>
   ${(v.ped || []).length + (v.aj || []).length ? `<p class="sub" style="color:var(--amarelo);margin:12px 0 0;font-weight:700">${(v.ped || []).length} pedido(s) em aberto · ${(v.aj || []).length} ajuste(s) pedido(s)</p>` : ''}
   <div style="display:flex;flex-wrap:wrap;gap:8px;margin-top:14px"><a class="btn am" href="/painel/${c.cliente}">Abrir painel</a><a class="btn lin" href="/painel/${c.cliente}#fotos">Fotos</a><a class="btn lin" href="/painel/${c.cliente}#pedidos">Pedidos</a>${c.cliente === 'jaci' ? '<a class="btn lin" href="/painel/jaci#crm">CRM</a><a class="btn lin" href="/painel/jaci#financeiro">Financeiro</a>' : ''}${c.cliente === 'leo' ? '<a class="btn lin" href="/painel/leo#demandas">Demandas</a>' : ''}</div>
   <p class="sub" style="margin:12px 0 0;font-size:12px">Instagram de ${esc(ig.data || '—')} · página atualizada em ${esc(c.atualizado || '—')}</p></div>`; };

V.inicio = () => { const nv = novidades();
  return H.bomDia() + `<div class="grade g4">${kpi('Clientes ativos', CL.length, 'com painel no ar')}${kpi('Pedidos em aberto', conta('ped'), 'dos clientes', conta('ped') > 0 ? 'down' : 'up')}${kpi('Ajustes pedidos', conta('aj'), 'em posts para aprovar', conta('aj') > 0 ? 'down' : 'up')}${kpi('Fotos recebidas', soma('fotos'), 'de todos os clientes')}</div>
  <div class="grade g21"><div class="card"><h3>Novidades dos clientes</h3><p class="sub">Pedidos e ajustes que chegaram pela Central. Também chegam no seu WhatsApp.</p><div class="lista">${!carregou ? '<div class="item"><div class="d">Carregando…</div></div>' : nv.length ? nv.slice(0, 8).map(x => `<a class="item" href="/painel/${x.c}${x.h}" style="text-decoration:none;color:inherit"><div style="min-width:0"><div class="t">${esc(x.t)}</div><div class="d">${esc(nomeCli(x.c))} · ${x.d ? new Date(x.d).toLocaleDateString('pt-BR') : ''}</div></div><div class="fim">${chip(x.st === 'aberto' ? 'aguardando' : x.st)}</div></a>`).join('') : '<div class="item"><div class="d">Nada pendente. Tudo em dia!</div></div>'}</div></div>
   <div class="card"><h3>Atalhos</h3><div class="lista">${[['Minha rede social', '#rede'], ['Vendas e CRMs', '#vendas'], ['Canais dark', '#canais'], ['Contas de acesso', '#contas']].map(([t, h]) => `<a class="item" href="${h}" style="text-decoration:none;color:inherit"><div class="t">${t}</div><div class="fim">›</div></a>`).join('')}</div></div></div>
  <div class="grade g2">${CL.map(cartaoCli).join('')}</div>`; };

V.clientes = () => `<div class="grade g2">${CL.map(cartaoCli).join('')}</div>
  <div class="card"><h3>Novo cliente</h3><p class="sub" style="margin:0">Para abrir o painel de um cliente novo (ex.: Apple Black, código já reservado), peça ao Claude: ele monta o painel na identidade do cliente e gera o código de acesso.</p></div>`;

const appCard = a => `<div class="card"><h3 style="display:flex;gap:10px;align-items:center;flex-wrap:wrap">${esc(a.nome)}${a.tag === 'principal' ? ' <span class="chip am">principal</span>' : ''}</h3><p class="sub">${esc(a.faz)}</p>
  <div style="display:flex;gap:8px;align-items:center;flex-wrap:wrap"><a class="btn am" href="${esc(a.url)}"${/^[\/#]/.test(a.url) ? '' : ' target="_blank" rel="noopener"'}>Abrir</a><span class="sub" style="margin:0;font-size:12px">${/^[\/#]/.test(a.url) ? 'aqui na Central' : 'no claude.ai · conta ' + esc(a.conta)}</span></div></div>`;
const aba = id => AP.abas.find(a => a.id === id) || { apps: [], sub: '' };
V.rede = () => `<div class="grade g4">${kpi('Seguidores', 'a medir', 'mande o print do Instagram')}${kpi('Visualizações 30 dias', 'a medir', 'mande o print do Instagram')}${kpi('Teste 01 de Reels', '300', 'roteiros no Recomeço 90')}${kpi('Métricas do Teste 01', 'a medir', 'prints na aba Conteúdo')}</div>
  <p class="sub">${esc(aba('rede').sub)} Os apps abrem no claude.ai, com a conta indicada.</p><div class="grade g3">${aba('rede').apps.map(appCard).join('')}</div>`;
V.vendas = () => `<p class="sub">${esc(aba('vendas').sub)}</p><div class="grade g3">${aba('vendas').apps.map(appCard).join('')}</div>`;
V.canais = () => `<p class="sub">${esc(aba('canais').sub)}</p><div class="grade g2">${aba('canais').apps.map(appCard).join('')}</div>`;
V.repetidos = () => `<div class="card"><h3>Antigos e repetidos</h3><p class="sub">Não use mais. Cada um mostra o que usar no lugar. Para apagar algum de vez, peça ao Claude.</p><div class="tab"><table><thead><tr><th>App</th><th>Por quê</th><th>Use agora</th><th></th></tr></thead><tbody>
  ${AP.repetidos.map(r => `<tr><td><b>${esc(r.nome)}</b></td><td>${esc(r.obs)}</td><td>${esc(r.troca)}</td><td><a class="btn lin" href="${esc(r.url)}" target="_blank" rel="noopener" style="padding:5px 10px;font-size:12px">Ver</a></td></tr>`).join('')}</tbody></table></div></div>`;
const NOMES = { admin: 'Administrador', jaci: 'Dra. Jaci Cunha', leo: 'Vereador Leo Pinto', apple: 'Apple Black' };
V.contas = () => `<div class="card"><h3>Contas de acesso</h3><p class="sub">Quem criou conta e qual painel abre. Esqueceu a senha? Exclua a conta e a pessoa cria de novo com o mesmo código.</p><div class="tab"><table><thead><tr><th>Nome</th><th>E-mail</th><th>Painel</th><th>Criada em</th><th></th></tr></thead><tbody>
  ${contas === null ? `<tr><td colspan="5">${carregou ? 'Não consegui carregar (entre de novo).' : 'Carregando…'}</td></tr>` : contas.map(c => `<tr><td>${esc(c.nome)}</td><td>${esc(c.email)}</td><td>${chip(NOMES[c.cli] || c.cli)}</td><td>${c.criada ? new Date(c.criada).toLocaleDateString('pt-BR') : ''}</td><td>${c.cli === 'admin' ? '' : `<button class="btn lin" type="button" data-apaga="${esc(c.email)}" style="padding:5px 10px;font-size:12px">Excluir</button>`}</td></tr>`).join('') || '<tr><td colspan="5">Nenhuma conta.</td></tr>'}</tbody></table></div></div>`;
Object.assign(T, { inicio: 'Visão geral', clientes: 'Clientes', rede: 'Minha rede social', vendas: 'Vendas e CRMs', canais: 'Canais dark', repetidos: 'Antigos e repetidos', contas: 'Contas de acesso' });


// apps do Lindson dentro do sistema (mesma identidade e menu lateral): a tela abre o app num quadro da própria Central
const quadro = (src, titulo) => `<iframe src="${src}" title="${titulo}" style="width:100%;height:calc(100vh - 150px);min-height:560px;border:1px solid var(--linha);border-radius:16px;background:#09090A;display:block" loading="lazy"></iframe>`;
V.recomeco = () => quadro('/painel/recomeco', 'Recomeço 90');
T.recomeco = 'Recomeço 90';
V.fabrica = () => quadro('/painel/fabrica', 'Fábrica de Conteúdo');
T.fabrica = 'Fábrica de Conteúdo';
const anterior = window.__pos;
window.__pos = view => {
  if (anterior) anterior(view);
  const nb = document.getElementById('n-novid'); if (nb) { const q = carregou ? conta('ped') + conta('aj') : 0; nb.textContent = q || ''; }
  document.querySelectorAll('#conteudo [data-apaga]').forEach(b => b.onclick = async () => {
    if (!confirm(`Excluir a conta ${b.dataset.apaga}? A pessoa perde o acesso até criar de novo com o código.`)) return;
    const r = await fetch('/api/contas?email=' + encodeURIComponent(b.dataset.apaga), { method: 'DELETE' });
    if (r.ok) { contas = contas.filter(c => c.email !== b.dataset.apaga); toast('Conta excluída.'); render(); } else toast('Não consegui excluir agora.');
  });
};
})();
