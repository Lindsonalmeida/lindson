"""Aba SDR no painel da Orégano Turbo (/painel/oregano#sdr). Pedido do Lindson, 15/11/2026 (conta Zuleide).
Coloca no painel já montado (idempotente): link no menu Gestão + tela SDR que lê /api/sdr-oregano (KV, só admin).
Funil: novo → 1º contato → D+2 → D+5 → D+10 → respondeu → diagnóstico → proposta → fechado/perdido.
Botão WhatsApp abre wa.me com a mensagem da etapa (PADRAO-COPY: Conexão → Dor → Desejo → Pergunta) e registra o envio.
Uso: python3 montar-sdr.py [pasta do privado]. Rode depois do montar-oregano.py."""
import os, sys
D = os.path.dirname(os.path.abspath(__file__))
PRIV = sys.argv[1] if len(sys.argv) > 1 else os.path.join(D, '..', '..', '..', '..', 'centrallindsonalmeida')
p = os.path.join(PRIV, 'painel', 'oregano.html'); s = open(p).read()
INI, FIM = '<!--SDR-INI-->', '<!--SDR-FIM-->'
if INI in s: s = s[:s.index(INI)] + s[s.index(FIM) + len(FIM):]
LINK = '<a href="#sdr" data-v="sdr"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M3 5h18l-7 8v6l-4 2v-8z"/></svg>SDR de pizzarias<span class="n" id="n-sdr"></span></a>'
if 'data-v="sdr"' not in s:
    a = '<a href="#crm" data-v="crm">'; assert a in s, 'o modelo mudou'
    s = s.replace(a, LINK + a, 1)
JS = r'''<!--SDR-INI--><style>
.sdr-k{display:grid;grid-template-columns:repeat(auto-fit,minmax(130px,1fr));gap:10px;margin-bottom:12px}
.sdr-f{display:flex;gap:6px;flex-wrap:wrap;margin:10px 0}.sdr-f button{border:1px solid var(--linha);background:transparent;color:var(--texto);border-radius:99px;padding:6px 11px;font:600 12px var(--f-corpo);cursor:pointer}
.sdr-f button[aria-pressed=true]{background:var(--amarelo);color:#1E5B3B;border-color:var(--amarelo)}
.sdr-l{display:grid;gap:10px}.sdr-c{border:1px solid var(--linha);border-radius:14px;padding:12px;background:var(--painel)}
.sdr-c h3{margin:0;font-size:15px}.sdr-c .m{font-size:12px;color:var(--apagado);margin:3px 0}.sdr-c .a{display:flex;gap:6px;flex-wrap:wrap;margin-top:8px}
.sdr-c select{background:var(--painel2);color:var(--texto);border:1px solid var(--linha);border-radius:9px;padding:8px}
.sdr-bar{height:8px;border-radius:9px;background:var(--painel2);overflow:hidden}.sdr-bar i{display:block;height:100%;background:var(--amarelo)}
.sdr-c pre{white-space:pre-wrap;font:12px/1.45 var(--f-corpo);background:var(--painel2);padding:8px;border-radius:9px;margin:8px 0 0}
</style><script>(()=>{const V=window.__V,T=window.__T;if(!V)return;T.sdr='SDR de pizzarias';
const E={novo:'Novo',contato1:'1º contato',fu2:'Follow-up D+2',fu5:'Follow-up D+5',fu10:'Follow-up D+10',respondeu:'Respondeu',diagnostico:'Diagnóstico agendado',proposta:'Proposta',fechado:'Fechado',perdido:'Perdido'};
const ENV=['novo','contato1','fu2','fu5'],META=30,X=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const DOR=['Fim de semana bomba e de segunda a quarta o movimento cai.','O cliente pede uma vez, gosta… e esquece de pedir de novo.','Pizza boa perde venda pra quem aparece mais no Instagram.'];
const h=x=>[...x.id].reduce((a,c)=>a+c.charCodeAt(0),0);
const MSG=c=>{const n=c.nome,d=DOR[h(c)%3];return({
novo:`Oi, ${n}! Tudo bem? Aqui é o Lindson.\n${d}\nEu ajudo pizzarias a vender mais no meio da semana, com Instagram, anúncio e pedido direto no WhatsApp.\nPosso te mostrar como faria pra vocês?`,
contato1:`Oi, ${n}! Passando de novo por aqui.\nSei que a noite de pizzaria é corrida.\nQuer que eu te mande em 1 minuto como faria pra encher a terça e a quarta?`,
fu2:`Oi, ${n}! Muita pizzaria paga taxa do app em todo pedido e ainda fica com o meio da semana fraco.\nDá pra trazer esse cliente pro WhatsApp de vocês.\nPosso te mostrar como?`,
fu5:`Oi, ${n}! Última mensagem, prometo.\nSe um dia quiser ver como ter mais pedido de segunda a quarta, é só me chamar aqui.\nPosso deixar o convite em aberto?`,
respondeu:`Que bom, ${n}! Pra eu te mostrar certinho: hoje vocês vendem mais pelo WhatsApp ou pelo app?\nPodemos marcar 20 minutos essa semana?`,
diagnostico:`Oi, ${n}! Confirmando nosso diagnóstico. Fica bom pra você?`,
proposta:`Oi, ${n}! Conseguiu olhar a proposta? Posso tirar alguma dúvida?`}[c.etapa]||'')};
const st={pronto:false,l:[],f:'hoje',q:''};
async function car(){try{const r=await fetch('/api/sdr-oregano',{headers:{Accept:'application/json'}});if(r.ok){const j=await r.json();st.l=j.leads||[]}else st.erro=r.status===401?'Só o administrador vê o SDR.':'Não carregou ('+r.status+').'}catch(e){st.erro='Sem conexão.'}st.pronto=true;window.__render()}
async function post(b){const r=await fetch('/api/sdr-oregano',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(b)});if(!r.ok){window.__toast('Não salvou. Tente de novo.');return}const j=await r.json(),i=st.l.findIndex(x=>x.id===b.id);if(i>=0)Object.assign(st.l[i],j);window.__render()}
const hoje=()=>new Date().toISOString().slice(0,10);
const due=c=>c.etapa==='novo'||(ENV.includes(c.etapa)&&c.prox&&c.prox<=hoje());
const envHoje=()=>st.l.reduce((a,c)=>a+(c.hist||[]).filter(e=>e.ev==='enviado'&&(e.em||'').slice(0,10)===hoje()).length,0);
V.sdr=()=>{if(!st.pronto){if(!st.ini){st.ini=1;car()}return '<div class="card"><p class="sub">Carregando o SDR…</p></div>'}
if(st.erro)return `<div class="card"><p class="sub">${X(st.erro)}</p></div>`;
const L=st.l,cnt=k=>L.filter(c=>c.etapa===k).length,eh=envHoje(),fila=L.filter(due).length;
const k=(r,v,n)=>`<div class="card kpi"><div class="rot">${r}</div><div class="val">${v}</div><div class="var up"><span>${n}</span></div></div>`;
const FS=[['hoje','Para hoje'],['todos','Todos'],...Object.entries(E)];
let l=st.f==='hoje'?L.filter(due):st.f==='todos'?L:L.filter(c=>c.etapa===st.f);
if(st.q){const q=st.q.toLowerCase();l=l.filter(c=>(c.nome+c.cidade+c.ig).toLowerCase().includes(q))}
const sl=c=>/São Luís|Ribamar|Paço|Raposa/.test(c.cidade||'')?1:0;l=l.slice().sort((a,b)=>sl(b)-sl(a)||(b.seg||0)-(a.seg||0));
return `<div class="sdr-k">${k('Enviados hoje',eh+'/'+META,'meta diária')}${k('Fila de hoje',fila,'novos + follow-ups vencidos')}${k('Responderam',cnt('respondeu'),'conversa aberta')}${k('Diagnósticos',cnt('diagnostico'),'agendados')}${k('Propostas',cnt('proposta'),'enviadas')}${k('Fechados',cnt('fechado'),'clientes')}</div>
<div class="card"><div class="sdr-bar"><i style="width:${Math.min(100,eh/META*100)}%"></i></div><p class="sub" style="margin:8px 0 0">Cadência: 1º contato → D+2 → D+5 → D+10 (sem resposta vira Perdido). Entram só pizzarias com WhatsApp de celular, Instagram e sinal de porte (≥ 5 mil seguidores, salão, app ou mais de 1 unidade). ${L.length} leads no total.</p>
<div class="sdr-f">${FS.map(([v,t])=>`<button data-sf="${v}" aria-pressed="${st.f===v}">${t} <b>${v==='hoje'?fila:v==='todos'?L.length:cnt(v)}</b></button>`).join('')}</div>
<input id="sdr-q" placeholder="Buscar nome, cidade ou @" value="${X(st.q)}" style="width:100%;background:var(--painel2);color:var(--texto);border:1px solid var(--linha);border-radius:9px;padding:9px"></div>
<div class="sdr-l">${l.map(c=>{const m=MSG(c),ok=ENV.includes(c.etapa);return `<div class="sdr-c"><div style="display:flex;justify-content:space-between;gap:8px"><h3>${X(c.nome)}</h3><span class="chip ${c.etapa==='fechado'?'ok':'al'}">${E[c.etapa]}</span></div>
<div class="m">${X(c.cidade)}${c.bairro?' · '+X(c.bairro):''} · <a href="https://instagram.com/${X(c.ig)}" target="_blank" rel="noopener" style="color:var(--amarelo)">@${X(c.ig)}</a> · ${(c.seg||0).toLocaleString('pt-BR')} seguidores${c.aval?' · '+c.aval+' avaliações':''}${c.estrelas?' · '+c.estrelas+'★':''}</div>
<div class="m">Porte: ${X(c.porte)}</div><div class="m">Por que entrou: ${X(c.motivo)} · <a href="${X(c.fonte)}" target="_blank" rel="noopener" style="color:var(--apagado)">fonte</a></div>
<div class="m">${c.prox?'Próxima ação: '+c.prox.split('-').reverse().join('/'):''}${c.enviadoEm?' · 1º envio '+c.enviadoEm.slice(0,10).split('-').reverse().join('/'):''}</div>
${m?`<details><summary class="m" style="cursor:pointer">Mensagem da etapa</summary><pre>${X(m)}</pre></details>`:''}
<div class="a">${m?`<a class="btn am" data-sw="${X(c.id)}" href="https://wa.me/${X(c.wa)}?text=${encodeURIComponent(m)}" target="_blank" rel="noopener">WhatsApp</a>`:''}
<select data-se="${X(c.id)}" aria-label="Etapa">${Object.entries(E).map(([v,t])=>`<option value="${v}"${v===c.etapa?' selected':''}>${t}</option>`).join('')}</select>
<button class="btn lin" data-sn="${X(c.id)}">${c.nota?'Nota ✓':'Nota'}</button></div>${c.nota?`<div class="m">📝 ${X(c.nota)}</div>`:''}</div>`}).join('')||'<div class="card"><p class="sub">Nada nesta etapa.</p></div>'}</div>`};
const ant=window.__render;window.__render=()=>{ant();const n=document.getElementById('n-sdr');if(n)n.textContent=st.pronto?(st.l.filter(due).length||''):'';const M=document.querySelector('main')||document;
M.querySelectorAll('[data-sf]').forEach(b=>b.onclick=()=>{st.f=b.dataset.sf;window.__render()});
const q=M.querySelector('#sdr-q');if(q)q.onchange=()=>{st.q=q.value;window.__render()};
M.querySelectorAll('[data-sw]').forEach(a=>a.addEventListener('click',()=>{const c=st.l.find(x=>x.id===a.dataset.sw);if(ENV.includes(c.etapa))post({id:c.id,acao:'enviado'}).then(()=>window.__toast('Envio registrado. Próxima ação agendada.'))}));
M.querySelectorAll('[data-se]').forEach(s=>s.onchange=()=>post({id:s.dataset.se,acao:'etapa',etapa:s.value}));
M.querySelectorAll('[data-sn]').forEach(b=>b.onclick=()=>{const c=st.l.find(x=>x.id===b.dataset.sn),t=prompt('Anotação',c.nota||'');if(t!==null)post({id:c.id,acao:'nota',nota:t})});};
window.removeEventListener('hashchange',ant);addEventListener('hashchange',()=>window.__render());if(location.hash==='#sdr')setTimeout(()=>window.__render(),0);car();})();</script><!--SDR-FIM-->'''
s = s.rstrip() + '\n' + JS + '\n'
open(p, 'w').write(s); print('aba SDR no painel da Orégano')
