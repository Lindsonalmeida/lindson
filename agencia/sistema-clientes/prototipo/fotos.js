// Tela "Fotos" do painel: o cliente manda fotos pelo celular para a agência; a agência (admin) vê e baixa.
// As fotos vão para o servidor da Central (/api/fotos, KV), reduzidas no aparelho para no máximo 2048 px, mais uma miniatura de 480 px.
// Categorias por cliente em window.__DADOS.fotosCats. Fora do site (arquivo local), mostra o aviso. Conta Lindson, 01/11/2026.
(() => {
const H = window.__h, V = window.__V, cli = H.cli(), D = window.__DADOS || {};
const toast = t => window.__toast(t), render = () => window.__render();
const esc = s => String(s ?? '').replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
const CATS = D.fotosCats || ['O espaço', 'Equipe', 'Bastidores', 'Produtos e serviços', 'Clientes (com autorização)', 'Outras'];
let fotos = null, remoto = null, filtro = '', enviando = '', cat = CATS[0];

document.head.insertAdjacentHTML('beforeend', `<style>
.ft-grade{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:12px}
.ft-item{background:var(--painel2);border:1px solid var(--linha);border-radius:12px;overflow:hidden;display:grid}
.ft-item img{width:100%;aspect-ratio:4/5;object-fit:cover;display:block;background:var(--painel)}
.ft-item .c{padding:8px 10px;display:grid;gap:6px;font-size:12px}
.ft-item .c .d{color:var(--apagado)}
.ft-item .ac{display:flex;gap:6px}.ft-item .ac a,.ft-item .ac button{flex:1;padding:6px;font-size:12px}
.ft-envio{border:2px dashed var(--linha);border-radius:14px;padding:18px;text-align:center;display:grid;gap:10px;justify-items:center}
.ft-envio.arrasta{border-color:var(--amarelo)}
.ft-envio select{background:var(--painel2);color:var(--texto);border:1px solid var(--linha);border-radius:9px;padding:9px 11px;font:500 14px var(--f-corpo);max-width:100%}
.ft-filtros{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:12px}.ft-filtros button{border:1px solid var(--linha);background:none;color:var(--texto);border-radius:99px;padding:6px 12px;font:600 12px var(--f-corpo);cursor:pointer}.ft-filtros button[aria-pressed=true]{background:var(--amarelo);color:#140608;border-color:var(--amarelo)}
</style>`);

async function carrega() {
  try {
    const r = await fetch(`/api/fotos?cli=${cli}`, { headers: { Accept: 'application/json' } });
    if (r.ok && (r.headers.get('content-type') || '').includes('json')) { fotos = (await r.json()).fotos; remoto = true; }
    else { remoto = false; fotos = []; if (r.status === 401) toast('Sua sessão expirou. Entre de novo na Central.'); }
  } catch (e) { remoto = false; fotos = []; }
  if ((location.hash || '').slice(1) === 'fotos') render();
}
carrega();

function reduz(file, max, q) {
  return new Promise((ok, erro) => {
    const url = URL.createObjectURL(file), img = new Image();
    img.onload = () => {
      const k = Math.min(1, max / Math.max(img.naturalWidth, img.naturalHeight)), w = Math.round(img.naturalWidth * k), h = Math.round(img.naturalHeight * k);
      const c = document.createElement('canvas'); c.width = w; c.height = h; c.getContext('2d').drawImage(img, 0, 0, w, h); URL.revokeObjectURL(url);
      c.toBlob(b => b ? ok({ b, w, h }) : erro(new Error('falhou')), 'image/jpeg', q);
    };
    img.onerror = () => { URL.revokeObjectURL(url); erro(new Error('formato')); };
    img.src = url;
  });
}
async function envia(lista) {
  lista = [...lista].filter(f => /^image\//.test(f.type) || /\.(jpe?g|png|webp|heic|heif)$/i.test(f.name));
  if (!lista.length) return toast('Escolha fotos (JPG, PNG ou do iPhone).');
  let ok = 0, falha = 0;
  for (let i = 0; i < lista.length; i++) {
    enviando = `Enviando ${i + 1} de ${lista.length}…`; render();
    try {
      const g = await reduz(lista[i], 2048, 0.86), m = await reduz(lista[i], 480, 0.8), nome = lista[i].name.replace(/\.[^.]+$/, '').slice(0, 60);
      const r = await fetch(`/api/fotos?cli=${cli}&cat=${encodeURIComponent(cat)}&nome=${encodeURIComponent(nome)}&w=${g.w}&h=${g.h}`, { method: 'POST', headers: { 'Content-Type': 'image/jpeg' }, body: g.b });
      const j = await r.json().catch(() => ({}));
      if (!r.ok) throw new Error(j.erro || 'erro');
      await fetch(`/api/fotos?cli=${cli}&id=${j.id}&thumb=1`, { method: 'POST', headers: { 'Content-Type': 'image/jpeg' }, body: m.b });
      fotos.unshift({ id: j.id, ...j }); ok++;
    } catch (e) { falha++; if (/sessão|Entre/.test(e.message)) { toast(e.message); break; } }
  }
  enviando = ''; render();
  toast(falha ? `${ok} enviada(s), ${falha} não foi(ram). ${/iPhone|iPad/.test(navigator.userAgent) ? 'Se for foto HEIC, tente de novo pela galeria.' : 'Tente de novo.'}` : `${ok} foto(s) enviada(s). A equipe já recebeu.`);
}

V.fotos = () => {
  if (fotos === null) return `<div class="card"><p class="sub">Carregando suas fotos…</p></div>`;
  if (!remoto) return `<div class="card"><h3>Fotos</h3><p class="sub" style="margin:0">O envio de fotos funciona no site da Central (lindsonalmeida.pages.dev), com o seu login.</p></div>`;
  const l = fotos.filter(f => !filtro || f.cat === filtro), usadas = [...new Set(fotos.map(f => f.cat))];
  return `<div class="grade g21"><div class="card"><h3>Enviar fotos</h3><p class="sub">Mande fotos boas, na vertical, com luz natural. Sem marca de outras empresas. ${esc(D.fotosNota || '')}</p>
    <div class="ft-envio" id="ft-zona"><label class="sub" style="margin:0">Tipo de foto <select id="ft-cat">${CATS.map(c => `<option ${c === cat ? 'selected' : ''}>${esc(c)}</option>`).join('')}</select></label>
     <input type="file" id="ft-arq" accept="image/*" multiple hidden>
     <button class="btn am" type="button" id="ft-escolhe" ${enviando ? 'disabled' : ''}>${enviando || 'Escolher fotos'}</button>
     <span class="sub" style="margin:0;font-size:12px">Pode escolher várias de uma vez. No computador, dá para arrastar as fotos para cá.</span></div></div>
   <div class="card"><h3>Resumo</h3><p class="sub">${fotos.length} foto(s) enviada(s).</p><div class="lista">${usadas.map(c => `<div style="display:flex;justify-content:space-between;font-size:13px"><span>${esc(c)}</span><b>${fotos.filter(f => f.cat === c).length}</b></div>`).join('') || '<div class="d" style="font-size:12px;color:var(--apagado)">Nenhuma foto ainda.</div>'}</div><p class="sub" style="margin-top:10px">Dica: 1 foto por dia já mantém o conteúdo do mês cheio.</p></div></div>
  <div class="card"><h3>Suas fotos</h3>${usadas.length > 1 ? `<div class="ft-filtros"><button type="button" data-ftf="" aria-pressed="${!filtro}">Todas</button>${usadas.map(c => `<button type="button" data-ftf="${esc(c)}" aria-pressed="${filtro === c}">${esc(c)}</button>`).join('')}</div>` : ''}
   ${l.length ? `<div class="ft-grade">${l.map(f => `<div class="ft-item"><a href="/api/foto?cli=${cli}&id=${f.id}" target="_blank" rel="noopener"><img loading="lazy" src="/api/foto?cli=${cli}&id=${f.id}&mini=1" alt="${esc(f.cat)}"></a><div class="c"><b>${esc(f.cat)}</b><span class="d">${f.em ? new Date(f.em).toLocaleDateString('pt-BR') : ''} · enviada por ${esc(f.por || 'cliente')}</span><div class="ac"><a class="btn lin" href="/api/foto?cli=${cli}&id=${f.id}&baixar=1">Baixar</a><button class="btn lin" type="button" data-ftdel="${f.id}" aria-label="Excluir foto">Excluir</button></div></div></div>`).join('')}</div>`
     : '<p class="sub" style="margin:0">Nenhuma foto aqui ainda. Use "Escolher fotos" acima.</p>'}</div>`;
};

const anterior = window.__pos;
window.__pos = view => {
  if (anterior) anterior(view);
  if (view !== 'fotos') return;
  const m = document.getElementById('conteudo'), arq = m.querySelector('#ft-arq'), zona = m.querySelector('#ft-zona');
  const sel = m.querySelector('#ft-cat'); if (sel) sel.onchange = () => { cat = sel.value; };
  const bt = m.querySelector('#ft-escolhe'); if (bt) bt.onclick = () => arq.click();
  if (arq) arq.onchange = () => { if (arq.files.length) envia(arq.files); };
  if (zona) { zona.ondragover = e => { e.preventDefault(); zona.classList.add('arrasta'); }; zona.ondragleave = () => zona.classList.remove('arrasta'); zona.ondrop = e => { e.preventDefault(); zona.classList.remove('arrasta'); if (!enviando) envia(e.dataTransfer.files); }; }
  m.querySelectorAll('[data-ftf]').forEach(b => b.onclick = () => { filtro = b.dataset.ftf; render(); });
  m.querySelectorAll('[data-ftdel]').forEach(b => b.onclick = async () => {
    if (!confirm('Excluir esta foto? Não dá para desfazer.')) return;
    const r = await fetch(`/api/fotos?cli=${cli}&id=${b.dataset.ftdel}`, { method: 'DELETE' });
    if (r.ok) { fotos = fotos.filter(f => f.id !== b.dataset.ftdel); toast('Foto excluída.'); render(); } else toast('Não consegui excluir agora.');
  });
};
})();
