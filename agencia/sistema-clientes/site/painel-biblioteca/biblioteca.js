/* Biblioteca do cliente: tudo o que a agência já produziu, organizado por categoria, com busca, filtros, versão e situação.
   Lê o manifesto /painel/<cliente>/biblioteca/manifesto.js (gerado por gerar_biblioteca.py; fica na pasta do cliente,
   então só o próprio cliente ou o admin abre). Pedido do Lindson, 20/11/2026 ("menu lateral chamado BIBLIOTECA"). Builder Squad. */
(function () {
  const V = window.__V, T = window.__T; if (!V || !T || (V.biblioteca && V.biblioteca.real)) return;  // o modelo traz uma tela de reserva; esta é a de verdade
  const me = document.currentScript, cli = (me && me.dataset.cli) || (location.pathname.split('/').pop() || '').replace(/\.html$/, '');
  if (!cli) return;
  const esc = s => String(s == null ? '' : s).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[c]);
  const ICO = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 4.5h4v15H4zM10 4.5h4v15h-4z"/><path d="m16 5.2 3.8-1 3.7 14.6-3.8 1z" transform="translate(-2.4 .4)"/></svg>';
  const ST = { aprovado: ['Aprovado', 'ok'], aguardando: ['Aguardando', 'al'], reprovado: ['Reprovado', 'er'] };
  const KIND = { pdf: 'PDF', video: 'Vídeo', zip: 'ZIP', html: 'Página', link: 'Link', svg: 'Vetor' };
  let B = null, erro = '', CAT = 'tudo', SIT = 'ativos', Q = '', ANT = false, MAIS = {};
  try { const s = sessionStorage.getItem('bib-' + cli); if (s) ({ CAT, SIT, ANT } = Object.assign({ CAT, SIT, ANT }, JSON.parse(s))); } catch (e) {}
  const guarda = () => { try { sessionStorage.setItem('bib-' + cli, JSON.stringify({ CAT, SIT, ANT })); } catch (e) {} };

  // menu lateral: grupo próprio "Biblioteca", logo depois do grupo de Conteúdo (ou do primeiro grupo)
  const menu = document.getElementById('menu');
  if (menu && !menu.querySelector('a[data-v="biblioteca"]')) {
    const gs = [...menu.querySelectorAll('.grupo')];
    const ref = gs.find(g => g.querySelector('a[data-v="aprovacoes"],a[data-v="aprovar"],a[data-v="conteudos"],a[data-v="postagens"]')) || gs[0];
    const g = document.createElement('div'); g.className = 'grupo';
    g.innerHTML = `<h4>Biblioteca</h4><a href="#biblioteca" data-v="biblioteca">${ICO}Biblioteca</a>`;
    if (ref && ref.parentNode) ref.parentNode.insertBefore(g, ref.nextSibling); else menu.appendChild(g);
  }

  const st = document.createElement('style');
  st.textContent = `
.bib-topo{display:flex;flex-wrap:wrap;align-items:flex-end;justify-content:space-between;gap:12px 24px;margin:0 0 18px}
.bib-topo h2{margin:0;font:600 clamp(26px,3vw,38px)/1.05 var(--f-titulo);letter-spacing:.01em}
.bib-topo p{margin:0;color:var(--texto);opacity:.82;font-size:14px;line-height:1.55;max-width:56ch}
.bib-num{display:flex;gap:22px;flex-wrap:wrap}.bib-num div{display:grid}.bib-num b{font:600 26px/1 var(--f-titulo);font-variant-numeric:tabular-nums}.bib-num span{font:500 10px var(--f-dado);letter-spacing:.2em;text-transform:uppercase;color:var(--apagado);margin-top:6px}
.bib-barra{position:sticky;top:64px;z-index:3;display:grid;gap:10px;padding:12px 0 12px;margin:0 0 6px;background:var(--fundo);border-bottom:1px solid var(--linha)}
.bib-busca{display:flex;gap:10px;align-items:center}
.bib-busca input{flex:1;min-width:0;background:var(--painel2);color:var(--texto);border:1px solid var(--linha);border-radius:10px;padding:11px 14px;font:500 14px var(--f-corpo)}
.bib-busca input:focus-visible,.bib-pil button:focus-visible,.bib-c button:focus-visible,.bib-c a:focus-visible,.bib-ant input:focus-visible{outline:2px solid var(--amarelo);outline-offset:2px}
.bib-ant{display:flex;align-items:center;gap:7px;font:600 12px var(--f-corpo);color:var(--apagado);white-space:nowrap;cursor:pointer}
.bib-pil{display:flex;gap:6px;overflow-x:auto;scrollbar-width:none;padding-bottom:2px}.bib-pil::-webkit-scrollbar{display:none}
.bib-pil button{flex:none;font:600 12px var(--f-corpo);color:var(--texto);background:transparent;border:1px solid var(--linha);border-radius:99px;padding:6px 12px;cursor:pointer}
.bib-pil button b{margin-left:6px;font-weight:500;opacity:.6;font-variant-numeric:tabular-nums}
.bib-pil button[aria-pressed=true]{background:var(--amarelo);color:var(--fundo);border-color:var(--amarelo)}
.bib-pil.sit button{font-size:11.5px;padding:5px 11px}
.bib-sec{margin:26px 0 8px;display:flex;align-items:baseline;gap:10px}
.bib-sec h3{margin:0;font:600 20px var(--f-titulo);letter-spacing:.01em}.bib-sec span{font:500 11px var(--f-dado);letter-spacing:.16em;color:var(--apagado)}
.bib-g{display:grid;grid-template-columns:repeat(auto-fill,minmax(196px,1fr));gap:14px}
.bib-c{display:flex;flex-direction:column;border:1px solid var(--linha);border-radius:12px;overflow:hidden;background:var(--painel);min-width:0;transition:border-color .2s}
.bib-c:hover{border-color:color-mix(in srgb,var(--amarelo) 45%,var(--linha))}
.bib-c .th{position:relative;aspect-ratio:4/5;background:var(--painel2);display:grid;place-items:center;overflow:hidden;cursor:pointer;border:0;padding:0;width:100%}
.bib-c .th img{width:100%;height:100%;object-fit:cover;display:block}
.bib-c .th.doc img{object-fit:contain;padding:10px;background:var(--painel2)}
.bib-c .th .ph{font:600 13px var(--f-dado);letter-spacing:.2em;color:var(--apagado)}
.bib-c .tag{position:absolute;left:8px;top:8px;font:600 10px var(--f-dado);letter-spacing:.12em;text-transform:uppercase;background:rgba(0,0,0,.62);color:#fff;border-radius:6px;padding:3px 7px;backdrop-filter:blur(4px)}
.bib-c .ant{position:absolute;right:8px;top:8px;font:600 10px var(--f-dado);letter-spacing:.12em;text-transform:uppercase;background:rgba(0,0,0,.62);color:#ddd;border-radius:6px;padding:3px 7px}
.bib-c .cx{padding:12px;display:grid;gap:6px;flex:1;align-content:start}
.bib-c .tt{font-weight:700;font-size:13.5px;line-height:1.35;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;overflow-wrap:anywhere}
.bib-c .mt{display:flex;flex-wrap:wrap;gap:6px;align-items:center;color:var(--apagado);font-size:11.5px}
.bib-c .nt{color:var(--apagado);font-size:11.5px;line-height:1.35}
.bib-c .ac{display:flex;gap:8px;padding:0 12px 12px}.bib-c .ac .btn{flex:1;padding:8px 10px;font-size:12.5px}
.bib-mais{display:flex;justify-content:center;margin:14px 0 0}
.bib-lb{position:fixed;inset:0;z-index:2147483000;background:#070708;display:grid;grid-template-rows:auto minmax(0,1fr) auto;grid-template-columns:minmax(0,1fr);gap:10px;padding:14px}
.bib-lb .cb{display:flex;flex-wrap:wrap;align-items:center;gap:8px 10px;color:#fff;min-width:0}.bib-lb .cb b{flex:1;min-width:0;font:600 14px var(--f-corpo);overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.bib-lb .cb .btn{padding:8px 12px}
.bib-lb .pal{min-height:0;min-width:0;display:grid;place-items:center;overflow:hidden}.bib-lb .pal img,.bib-lb .pal video{max-width:100%;max-height:100%;object-fit:contain;border-radius:8px}
.bib-lb .tr{display:flex;gap:8px;overflow-x:auto;justify-content:safe center;padding-bottom:4px}
.bib-lb .tr button{flex:none;width:56px;aspect-ratio:4/5;border-radius:6px;overflow:hidden;border:2px solid transparent;padding:0;background:#222;cursor:pointer}
.bib-lb .tr button[aria-current=true]{border-color:var(--amarelo)}.bib-lb .tr img{width:100%;height:100%;object-fit:cover}
@media (max-width:640px){.bib-lb .cb b{flex-basis:100%}.bib-busca{flex-wrap:wrap}.bib-busca input{flex-basis:100%}.bib-g{grid-template-columns:repeat(2,minmax(0,1fr));gap:10px}.bib-c .cx{padding:10px}.bib-c .ac{padding:0 10px 10px;flex-direction:column;gap:6px}.bib-barra{top:56px}.bib-num{gap:16px}.bib-num b{font-size:22px}}
@media (prefers-reduced-motion:reduce){.bib-c{transition:none}}`;
  document.head.appendChild(st);

  // situação ao vivo: se o cliente aprovou ou pediu ajuste no site, vale o que está nas Aprovações (pelo título)
  function vivo(it) {
    const A = (window.__h && window.__h.APROV) || [];
    if (!it.ap || !A.length) return it.s;
    const p = A.find(x => x && x.titulo === it.ap); if (!p) return it.s;
    const s = String(p.st || '').toLowerCase();
    return /aprov|postad/.test(s) || p.postado ? 'aprovado' : /reprov|recus|substitu/.test(s) ? 'reprovado' : it.s === 'reprovado' ? 'reprovado' : 'aguardando';
  }
  const dataBR = d => d ? d.split('-').reverse().join('/') : '';
  const tam = z => !z ? '' : z > 1048576 ? (z / 1048576).toFixed(1).replace('.', ',') + ' MB' : Math.max(1, Math.round(z / 1024)) + ' KB';
  const norm = s => String(s || '').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '');
  function lista() {
    if (!B) return [];
    const q = norm(Q).split(/\s+/).filter(Boolean);
    return B.itens.map(it => (it._s = vivo(it), it)).filter(it =>
      (ANT || !it.a) &&
      (SIT === 'todos' ? true : SIT === 'ativos' ? it._s !== 'reprovado' : it._s === SIT) &&
      (!q.length || q.every(w => norm(it.t + ' ' + it.c + ' ' + (it.tp || '') + ' ' + (it.vl || '') + ' ' + (it.nt || '') + ' ' + dataBR(it.d)).includes(w))));
  }
  function cartao(it) {
    const s = ST[it._s] || ST.aguardando, doc = /^(pdf|zip|html|link)$/.test(it.k), n = (it.p || []).length;
    const tag = it.k === 'video' ? 'Vídeo' : KIND[it.k] || (n ? (n + 1) + ' telas' : '');
    const th = it.m ? `<img src="${esc(it.m)}" alt="" loading="lazy" decoding="async" onerror="this.replaceWith(Object.assign(document.createElement('span'),{className:'ph',textContent:'${esc(KIND[it.k] || 'ARQUIVO')}'}))">` : `<span class="ph">${esc(KIND[it.k] || 'ARQUIVO')}</span>`;
    const meta = [it.d ? dataBR(it.d) : '', it.vl ? esc(it.vl) : '', it.z ? tam(it.z) : ''].filter(Boolean).join(' · ');
    const conter = doc && !/^(img|video)$/.test(it.k) || it.c === 'Marca' && /logo|s[ií]mbolo|monograma|favicon/i.test(it.t) || it.k === 'svg';
    return `<article class="bib-c" aria-label="${esc(it.t)}">
<button type="button" class="th${conter ? ' doc' : ''}" data-bib-abre="${esc(it.id)}" aria-label="Abrir ${esc(it.t)}">${th}${tag ? `<span class="tag">${esc(tag)}</span>` : ''}${it.a ? '<span class="ant">versão antiga</span>' : ''}</button>
<div class="cx"><div class="tt" title="${esc(it.t)}">${esc(it.t)}</div><div class="mt"><span class="chip ${s[1]}">${s[0]}</span></div>${meta ? `<div class="mt">${meta}</div>` : ''}${it.nt ? `<div class="nt">${esc(it.nt)}</div>` : ''}</div>
<div class="ac"><button type="button" class="btn lin" data-bib-abre="${esc(it.id)}">Abrir</button>${it.b ? `<a class="btn am" href="${esc(it.b)}" download>Baixar</a>` : ''}</div></article>`;
  }
  function resultado() {
    if (!B) return `<div class="card"><p class="sub" style="margin:0">${erro || 'Carregando a biblioteca…'}</p></div>`;
    const L = lista(), cats = (B.cats || []).filter(c => L.some(i => i.c === c));
    if (!L.length) return `<div class="vazio">Nada encontrado${Q ? ` para “${esc(Q)}”` : ''}. Tente outra palavra ou mude o filtro.</div>`;
    const bloco = c => { const its = L.filter(i => i.c === c), lim = MAIS[c] || (CAT === 'tudo' ? 8 : 48);
      return `${CAT === 'tudo' ? `<div class="bib-sec"><h3>${esc(c)}</h3><span>${its.length}</span></div>` : ''}<div class="bib-g">${its.slice(0, lim).map(cartao).join('')}</div>${its.length > lim ? `<div class="bib-mais"><button type="button" class="btn lin" data-bib-mais="${esc(c)}">Mostrar mais ${Math.min(its.length - lim, 48)} de ${its.length - lim}</button></div>` : ''}`; };
    return CAT === 'tudo' ? cats.map(bloco).join('') : (cats.includes(CAT) ? bloco(CAT) : '<div class="vazio">Nada nesta categoria com este filtro.</div>');
  }
  function pilulas() {
    const L = lista(), cats = (B ? B.cats : []).filter(c => L.some(i => i.c === c));
    if (CAT !== 'tudo' && !cats.includes(CAT)) CAT = 'tudo';
    const c = `<button type="button" data-bib-cat="tudo" aria-pressed="${CAT === 'tudo'}">Tudo<b>${L.length}</b></button>` + cats.map(k => `<button type="button" data-bib-cat="${esc(k)}" aria-pressed="${CAT === k}">${esc(k)}<b>${L.filter(i => i.c === k).length}</b></button>`).join('');
    const S = [['ativos', 'Aprovados e aguardando'], ['aprovado', 'Aprovado'], ['aguardando', 'Aguardando'], ['reprovado', 'Reprovado'], ['todos', 'Todos']];
    return { c, s: S.map(([k, n]) => `<button type="button" data-bib-sit="${k}" aria-pressed="${SIT === k}">${n}</button>`).join('') };
  }
  function atualiza() {
    const r = document.getElementById('bib-res'), pc = document.getElementById('bib-cats'), ps = document.getElementById('bib-sit');
    if (!r) return; const p = pilulas(); pc.innerHTML = p.c; ps.innerHTML = p.s; r.innerHTML = resultado(); guarda();
  }
  V.biblioteca = () => {
    if (!B) return `<div class="card"><h3>Biblioteca</h3><p class="sub" style="margin:0">${erro || 'Carregando a biblioteca…'}</p></div>`;
    const todos = B.itens.map(it => (it._s = vivo(it), it)).filter(i => !i.a), p = pilulas();
    const n = s => todos.filter(i => i._s === s).length;
    return `<div class="bib-topo"><div><p>Tudo o que a agência já produziu para ${esc(B.nome || 'você')}, em um lugar só: marca, artes, vídeos, documentos e links. A versão mais nova aparece primeiro.</p></div>
<div class="bib-num"><div><b>${todos.filter(i => i._s !== 'reprovado').length}</b><span>Itens</span></div><div><b>${n('aprovado')}</b><span>Aprovados</span></div><div><b>${n('aguardando')}</b><span>Aguardando</span></div></div></div>
<div class="bib-barra"><div class="bib-busca"><input id="bib-q" type="search" placeholder="Buscar por nome, tipo ou data" aria-label="Buscar na biblioteca" value="${esc(Q)}"><label class="bib-ant"><input type="checkbox" id="bib-ant"${ANT ? ' checked' : ''}>Versões antigas</label></div>
<div class="bib-pil" id="bib-cats" role="group" aria-label="Categoria">${p.c}</div><div class="bib-pil sit" id="bib-sit" role="group" aria-label="Situação">${p.s}</div></div>
<div id="bib-res" aria-live="polite">${resultado()}</div><p class="sub" style="margin:22px 0 0">Atualizada em ${esc(B.gerado || '')}.</p>`;
  };
  V.biblioteca.real = true; T.biblioteca = 'Biblioteca';


  // Baixar tudo (Lindson, 24/11/2026): carrossel/série sem zip pronto baixa todas as telas de uma vez.
  // Celular: abre o Compartilhar com todas as imagens (Salvar na galeria). Computador: um .zip com 01, 02, 03… (conta Zuleide)
  const zipTelas = window.__zipTelas || (() => {
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
  const prontos = {};
  async function baixaTudo(it, fs, b) {
    const base = String(it.t || 'carrossel').normalize('NFD').replace(/[\u0300-\u036f]/g, '').replace(/[^A-Za-z0-9]+/g, '-').replace(/^-|-$/g, '').toLowerCase() || 'carrossel';
    const celular = /Android|iPhone|iPad|iPod/i.test(navigator.userAgent) && !!navigator.canShare;
    if (celular && prontos[it.id]) { try { await navigator.share({ files: prontos[it.id], title: it.t || 'Carrossel' }); } catch (e) {} return; }
    const txt = b.textContent; b.disabled = true; b.textContent = 'Preparando…';
    try {
      const blobs = await Promise.all(fs.map(u => fetch(u).then(r => { if (!r.ok) throw new Error(r.status); return r.blob(); })));
      const files = blobs.map((x, k) => { const ext = (fs[k].split('?')[0].match(/\.([a-z0-9]+)$/i) || [, 'jpg'])[1]; return new File([x], `${base}-${String(k + 1).padStart(2, '0')}.${ext}`, { type: x.type || 'image/jpeg' }); });
      if (celular && navigator.canShare({ files })) { prontos[it.id] = files; b.disabled = false; b.textContent = `Toque de novo para salvar as ${files.length}`; return; }
      const z = zipTelas(await Promise.all(files.map(async f => ({ nome: f.name, dados: new Uint8Array(await f.arrayBuffer()) }))));
      const a = document.createElement('a'); a.href = URL.createObjectURL(z); a.download = base + '.zip'; document.body.appendChild(a); a.click(); setTimeout(() => { URL.revokeObjectURL(a.href); a.remove(); }, 4000);
    } catch (e) { alert('Não consegui baixar agora. Tente de novo.'); }
    b.disabled = false; b.textContent = txt;
  }
  // visualizador (imagem, carrossel, vídeo); PDF, página e link abrem em outra aba
  let LB = null;
  function abre(id) {
    const it = B && B.itens.find(x => x.id === id); if (!it) return;
    if (/^(pdf|html|link|zip)$/.test(it.k)) { window.open(it.u, '_blank', 'noopener'); return; }
    const fs = [it.u].concat(it.p || []).filter(Boolean); let i = 0;
    const antes = document.activeElement;
    LB = document.createElement('div'); LB.className = 'bib-lb'; LB.setAttribute('role', 'dialog'); LB.setAttribute('aria-modal', 'true'); LB.setAttribute('aria-label', it.t);
    const midia = u => /\.(mp4|webm|mov)(\?|$)/i.test(u) ? `<video src="${esc(u)}" controls playsinline preload="metadata"></video>` : `<img src="${esc(u)}" alt="${esc(it.t)}">`;
    const pinta = () => {
      LB.innerHTML = `<div class="cb"><b>${esc(it.t)}${fs.length > 1 ? ` · ${i + 1}/${fs.length}` : ''}</b><a class="btn am" href="${esc(fs[i])}" download>Baixar</a>${it.b && it.b !== fs[i] ? `<a class="btn lin" style="color:#fff" href="${esc(it.b)}" download>Baixar tudo</a>` : fs.length > 1 ? `<button type="button" class="btn lin" style="color:#fff" data-bib-tudo>Baixar tudo (${fs.length})</button>` : ''}<button type="button" class="btn lin" style="color:#fff" data-bib-fecha aria-label="Fechar">Fechar</button></div>
<div class="pal">${midia(fs[i])}</div>${fs.length > 1 ? `<div class="tr">${fs.map((u, k) => `<button type="button" data-bib-vai="${k}" aria-label="Tela ${k + 1}" aria-current="${k === i}">${/\.(mp4|webm|mov)/i.test(u) ? '<span style="color:#fff;font-size:11px">vídeo</span>' : `<img src="${esc(u)}" alt="" loading="lazy">`}</button>`).join('')}</div>` : '<div></div>'}`;
      const f = LB.querySelector('[data-bib-fecha]'); f && f.focus();
    };
    const fecha = () => { LB && LB.remove(); LB = null; document.removeEventListener('keydown', tecla); antes && antes.focus && antes.focus(); };
    const tecla = e => { if (e.key === 'Escape') fecha(); else if (e.key === 'ArrowRight' && i < fs.length - 1) { i++; pinta(); } else if (e.key === 'ArrowLeft' && i > 0) { i--; pinta(); } };
    LB.addEventListener('click', e => { if (e.target === LB || e.target.closest('[data-bib-fecha]')) fecha(); const v = e.target.closest('[data-bib-vai]'); if (v) { i = +v.dataset.bibVai; pinta(); } const t = e.target.closest('[data-bib-tudo]'); if (t) baixaTudo(it, fs, t); });
    document.addEventListener('keydown', tecla); document.body.appendChild(LB); pinta();
  }

  document.addEventListener('click', e => {
    const a = e.target.closest('[data-bib-abre]'); if (a) { abre(a.dataset.bibAbre); return; }
    const c = e.target.closest('[data-bib-cat]'); if (c) { CAT = c.dataset.bibCat; atualiza(); return; }
    const s = e.target.closest('[data-bib-sit]'); if (s) { SIT = s.dataset.bibSit; atualiza(); return; }
    const m = e.target.closest('[data-bib-mais]'); if (m) { const k = m.dataset.bibMais; MAIS[k] = (MAIS[k] || (CAT === 'tudo' ? 8 : 48)) + 48; atualiza(); }
  });
  let tq; document.addEventListener('input', e => { if (e.target.id === 'bib-q') { clearTimeout(tq); tq = setTimeout(() => { Q = e.target.value; atualiza(); }, 140); } });
  document.addEventListener('change', e => { if (e.target.id === 'bib-ant') { ANT = e.target.checked; atualiza(); } });

  // carrega o manifesto do cliente
  const sc = document.createElement('script'); sc.src = '/painel/' + encodeURIComponent(cli) + '/biblioteca/manifesto.js'; sc.async = true;
  sc.onload = () => { B = (window.__BIB || {})[cli] || null; if (!B) erro = 'A biblioteca ainda não foi montada para este painel.'; if ((location.hash || '').slice(1) === 'biblioteca' && window.__render) window.__render(); };
  sc.onerror = () => { erro = 'Não consegui abrir a biblioteca agora. Atualize a página.'; if ((location.hash || '').slice(1) === 'biblioteca' && window.__render) window.__render(); };
  document.head.appendChild(sc);
  if ((location.hash || '').slice(1) === 'biblioteca' && window.__render) window.__render();
})();
