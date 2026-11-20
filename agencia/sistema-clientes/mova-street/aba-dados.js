/* Aba "Dados e Vendas" do painel da Mova Street (pedido do Lindson, 19/11/2026).
   4 seções: Mercado (estatísticas com fonte), Métricas (números da equipe por semana), Perspectivas (tendências e datas fortes)
   e Aplicar às vendas (argumentos por ramo, objeções, quanto custa por dia).
   Conteúdo: dados-vendas.json (window.__MOVA_DV). Números da equipe: /api/dados?cli=mova-street&f=vendas, o mesmo mecanismo
   versionado do CRM (GET {dados,versao}; PUT com versão; 409 = junta e tenta de novo). Sem internet: fica no aparelho.
   Métrica principal (Data Squad): pacotes de telas pagos. Começa vazio: nenhum número é inventado.
   Módulo próprio: não altera o CRM; só lê window.__crmMova quando a pessoa toca em "Puxar do CRM". */
(function(){
const C=window.__MOVA_DV;if(!C||!window.__V)return;
const CLI='mova-street',U='/api/dados?cli='+CLI+'&f=vendas',LS='mova-vendas-local',LSU='mova-dv-ui';
const $=s=>document.querySelector(s);
const esc=t=>String(t??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const toast=t=>window.__toast?window.__toast(t):null,rr=()=>window.__render&&window.__render();
const calmo=()=>matchMedia('(prefers-reduced-motion: reduce)').matches,celular=()=>matchMedia('(max-width:700px)').matches;
const lsGet=k=>{try{return JSON.parse(localStorage.getItem(k)||'null')}catch(e){return null}},lsSet=(k,v)=>{try{localStorage.setItem(k,JSON.stringify(v))}catch(e){}};
const nf=(v,d=0)=>(+v||0).toLocaleString('pt-BR',{minimumFractionDigits:d,maximumFractionDigits:d});
const brl=(v,d=0)=>'R$ '+nf(v,d);
const nfH=(v,d=0)=>nf(v,d).replace(/[.,]/g,m=>`<i class="vg">${m}</i>`);
const vazio=v=>v===undefined||v===null||v==='';
// datas no horário do aparelho (São Luís)
const isoDe=d=>`${d.getFullYear()}-${String(d.getMonth()+1).padStart(2,'0')}-${String(d.getDate()).padStart(2,'0')}`;
const dt=s=>new Date(s+'T12:00:00');
const mais=(s,n)=>{const d=dt(s);d.setDate(d.getDate()+n);return isoDe(d)};
const segDe=d=>{const x=new Date(d.getFullYear(),d.getMonth(),d.getDate(),12);x.setDate(x.getDate()-((x.getDay()+6)%7));return isoDe(x)};
const hoje=()=>isoDe(new Date()),semHoje=()=>segDe(new Date());
const br=s=>s.slice(8,10)+'/'+s.slice(5,7);
const rotSem=s=>br(s)+' a '+br(mais(s,6));
const mesDaSem=s=>mais(s,3).slice(0,7); // a semana conta no mês da quinta-feira
const MESES=['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro'];
const nomeMes=m=>MESES[+m.slice(5,7)-1]+' de '+m.slice(0,4);
const mesMais=(m,n)=>{const d=new Date(+m.slice(0,4),+m.slice(5,7)-1+n,1);return d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')};
const diasAte=s=>Math.round((dt(s)-dt(hoje()))/864e5);
const pct=(a,b)=>vazio(a)||vazio(b)||!+b?null:Math.round(a/b*1000)/10;
const pctTxt=p=>p===null?'—':nf(p,p%1?1:0)+'%';

// ---------- números da equipe (servidor) ----------
const CURTO={contatos:'Contatos',mapas:'Mapas',propostas:'Propostas',fechamentos:'Fechamentos',renovacoes:'Renovações',vencidos:'Venceram',pacotes:'Pacotes'};
const CAMPOS=[['contatos','Contatos','Empresas abordadas na semana (visita, WhatsApp, anúncio, indicação).'],['mapas','Mapas enviados','Mapas de visibilidade enviados.'],['propostas','Propostas','Propostas de 1 página enviadas.'],['fechamentos','Fechamentos','Contratos assinados com pagamento combinado.'],['renovacoes','Renovações','Contratos renovados na semana.'],['vencidos','Contratos que venceram','Contratos que terminaram na semana (base da taxa de renovação).'],['pacotes','Pacotes de telas pagos','Anunciantes com o pacote das 10 telas pago (fechado, no ar ou em renovação), contados no fim da semana.']];
const FUNIL=['contatos','mapas','propostas','fechamentos'];
const NOMEC=Object.fromEntries(CAMPOS.map(c=>[c[0],c[1]]));
const ui=Object.assign({aba:'mercado',vend:'Paulo',met:'fechamentos',nicho:'clinica'},lsGet(LSU)||{});
const S={d:null,v:0,carregou:false,carregando:false,off:false,nome:'',sem:semHoje(),mes:mesDaSem(semHoje()),calc:{dur:'10',meses:1,excl:false,carros:0}};
const salvaUi=()=>lsSet(LSU,ui);
function normal(x){x=x&&typeof x==='object'?x:{};if(!x.semanas||typeof x.semanas!=='object')x.semanas={};if(!x.meses||typeof x.meses!=='object')x.meses={};return x}
async function carregar(){if(S.carregando)return;S.carregando=true;
  try{const r=await fetch(U,{headers:{Accept:'application/json'}});if(!r.ok||!(r.headers.get('content-type')||'').includes('json'))throw 0;const j=await r.json();S.d=normal(j.dados);S.v=j.versao||0;S.nome=j.nome||'';S.off=false}
  catch(e){S.off=true;S.d=normal(lsGet(LS))}
  S.carregou=true;S.carregando=false;if(location.hash==='#dados')rr()}
let fila=Promise.resolve();
function mut(fn,msg){fn(S.d);rr();fila=fila.then(async()=>{
  if(S.off){lsSet(LS,S.d);msg&&toast(msg+' (só neste aparelho)');return}
  for(let t=0;t<3;t++){let r;
    try{r=await fetch(U,{method:'PUT',headers:{'Content-Type':'application/json'},body:JSON.stringify({dados:S.d,versao:S.v})})}
    catch(e){S.off=true;lsSet(LS,S.d);toast('Sem conexão: ficou salvo só neste aparelho.');rr();return}
    if(r.ok){S.v=(await r.json()).versao;msg&&toast(msg);return}
    if(r.status===409){const j=await r.json();S.d=normal(j.dados);S.v=j.versao;fn(S.d);continue}
    toast(r.status===401?'Sua sessão expirou. Entre de novo.':'Não salvou. Confira a internet.');return}
  rr()})}
const semanasDoMes=m=>Object.keys(S.d.semanas).filter(s=>mesDaSem(s)===m).sort();
function somaMes(m){const ss=semanasDoMes(m),o={};
  CAMPOS.forEach(([k])=>{if(k==='pacotes'){const c=ss.filter(s=>!vazio(S.d.semanas[s].pacotes));o[k]=c.length?+S.d.semanas[c[c.length-1]].pacotes:null;return}
    const vs=ss.map(s=>S.d.semanas[s][k]).filter(v=>!vazio(v));o[k]=vs.length?vs.reduce((a,b)=>a+ +b,0):null});return o}

// ---------- copiar ----------
const COPIA={};let nCopia=0;
const cp=t=>{const id='c'+(++nCopia);COPIA[id]=t;return id};
function copiar(t){const ok=()=>toast('Copiado.');
  if(navigator.clipboard&&window.isSecureContext){navigator.clipboard.writeText(t).then(ok,()=>velho(t))}else velho(t);
  function velho(x){const a=document.createElement('textarea');a.value=x;a.setAttribute('readonly','');a.style.cssText='position:fixed;left:-9999px;top:0';document.body.appendChild(a);a.select();try{document.execCommand('copy');ok()}catch(e){toast('Não deu para copiar. Segure o texto e copie.')}a.remove()}}
document.addEventListener('click',e=>{const b=e.target.closest('[data-dv-cp]');if(!b)return;const t=b.dataset.dvCp==='calc'?fraseCalc():COPIA[b.dataset.dvCp];if(t)copiar(t)});

// ---------- números que contam (só na primeira vez que aparecem) ----------
function conta(){if(calmo())return;document.querySelectorAll('#conteudo [data-dv-n]:not([data-dv-ok])').forEach(el=>{el.setAttribute('data-dv-ok','1');
  const alvo=+el.dataset.dvN,dec=+el.dataset.dec||0,b=el.querySelector('b');if(!b||!(alvo>0))return;const fim=b.innerHTML,ini=performance.now(),dur=850;
  const passo=k=>{const u=Math.min(1,(k-ini)/dur),e=1-Math.pow(1-u,3);b.innerHTML=nfH(alvo*e,dec);if(u<1)requestAnimationFrame(passo);else b.innerHTML=fim};requestAnimationFrame(passo)})}
const numHtml=it=>`<div class="dv-num" data-dv-n="${it.v}" data-dec="${it.dec||0}">${it.pre?`<span class="dv-pre">${esc(it.pre)}</span>`:''}<b>${nfH(it.v,it.dec||0)}</b>${it.suf?`<span class="dv-suf">${esc(it.suf)}</span>`:''}</div>`;
const fonteHtml=(f,d,u)=>`<a class="dv-fonte" href="${esc(u)}" target="_blank" rel="noopener">${esc(f)}${d?' · '+esc(d):''}<svg viewBox="0 0 12 12" aria-hidden="true"><path d="M4 2h6v6M10 2 3 9"/></svg></a>`;

// ---------- 1 · mercado ----------
function mercadoV(){
  return C.mercado.map((g,gi)=>`<section class="dv-grupo"><header class="dv-gh"><span class="dv-k">${String(gi+1).padStart(2,'0')}</span><h3>${esc(g.grupo)}</h3></header>
  ${g.itens.map(it=>`<article class="dv-stat">${numHtml(it)}
    <div class="dv-txt"><span class="dv-onde">${esc(it.onde)}</span><p>${esc(it.frase)}</p>${fonteHtml(it.fonte,it.data,it.url)}</div>
    <div class="dv-usar"><span class="dv-k or">Na venda</span><p>${esc(it.usar)}</p><button class="dv-cp" data-dv-cp="${cp(it.usar)}">Copiar frase</button></div></article>`).join('')}</section>`).join('')
  +`<section class="dv-nota"><p>${esc(C.notaMercado)}</p></section>`}

// ---------- 2 · métricas ----------
function barraMeta(v,meta){if(vazio(meta)||!+meta)return '';const p=vazio(v)?0:Math.min(100,v/meta*100);return `<div class="barra dv-meta" role="img" aria-label="${pctTxt(pct(v,meta))} da meta"><i style="width:${p}%"></i></div><span class="dv-l2">${vazio(v)?'—':nf(v)} de ${nf(meta)} · ${pctTxt(pct(v,meta))} da meta</span>`}
function crmLinha(){const api=window.__crmMova,c=api&&api.get&&api.get();if(!c){if(api&&api.carregar&&!S.crmPedido){S.crmPedido=true;api.carregar()}return ''}
  const pac=(c.itens||[]).filter(l=>['e7','e8','e9'].includes(l.etapa)&&/^(p|combo)(10|15|20)$/.test(l.plano||'')).length,tl=c.telas||[],oc=tl.filter(t=>t.st==='ocupada').length;
  return `<p class="dv-crm">No CRM agora: <b>${pac}</b> pacote${pac===1?'':'s'} fechado${pac===1?'':'s'} · <b>${oc}</b> de ${tl.length} vagas na programação ocupadas</p>`}
function grafico(){const met=ui.met,ws=Array.from({length:8},(_,i)=>mais(S.sem,(i-7)*7)),vs=ws.map(w=>{const r=S.d.semanas[w];return r&&!vazio(r[met])?+r[met]:null});
  const tem=vs.some(v=>v!==null),cel=celular(),W=cel?360:720,H=cel?210:230,l=cel?28:36,r=8,t=26,b=30,ih=H-t-b,iw=W-l-r,slot=iw/8,bw=Math.min(24,slot*.5);
  const mx=Math.max(1,...vs.filter(v=>v!==null)),passo=(()=>{const s=mx/3,p=Math.pow(10,Math.floor(Math.log10(s))),n=s/p;return Math.max(1,(n<=1?1:n<=2?2:n<=5?5:10)*p)})(),top=Math.max(passo,Math.ceil(mx/passo)*passo),y=v=>t+ih-(v/top*ih);
  const ticks=[];for(let v=0;v<=top+1e-9;v+=passo)ticks.push(v);
  const grid=ticks.map(v=>`<line x1="${l}" x2="${W-r}" y1="${y(v)}" y2="${y(v)}" class="dv-gl"/><text x="${l-6}" y="${y(v)+3.5}" class="dv-ax" text-anchor="end">${nf(v)}</text>`).join('');
  const barras=ws.map((w,i)=>{const v=vs[i],x=l+i*slot+(slot-bw)/2,cx=l+i*slot+slot/2,sel=w===S.sem;let m='';
    if(v!==null&&v>0){const yy=y(v),h=t+ih-yy,rr2=Math.min(4,h);m=`<path class="dv-bar${sel?' on':''}" d="M${x},${t+ih}V${yy+rr2}Q${x},${yy} ${x+rr2},${yy}H${x+bw-rr2}Q${x+bw},${yy} ${x+bw},${yy+rr2}V${t+ih}Z"/>`}
    const lab=sel&&v!==null?`<text x="${cx}" y="${(v>0?y(v):t+ih)-8}" class="dv-vl" text-anchor="middle">${nf(v)}</text>`:'';
    const tip=`${rotSem(w)}: ${v===null?'sem lançamento':nf(v)+' '+NOMEC[met].toLowerCase()}`;
    return `${m}${lab}<text x="${cx}" y="${H-10}" class="dv-ax${sel?' on':''}" text-anchor="middle">${br(w)}</text><rect class="dv-hit" x="${l+i*slot}" y="${t}" width="${slot}" height="${ih+4}" tabindex="0" role="img" aria-label="${esc(tip)}" data-tip="${esc(tip)}"/>`}).join('');
  return `<div class="dv-graf"><svg viewBox="0 0 ${W} ${H}" role="group" aria-label="${esc(NOMEC[met])} nas últimas 8 semanas">${grid}<line x1="${l}" x2="${W-r}" y1="${t+ih}" y2="${t+ih}" class="dv-base"/>${barras}</svg>${tem?'':'<p class="dv-vz">Sem semanas lançadas ainda</p>'}<div class="dv-tip" hidden></div></div>`}
function ligaTip(){const g=document.querySelector('#conteudo .dv-graf');if(!g)return;const tip=g.querySelector('.dv-tip');
  const mostra=(el,ev)=>{tip.textContent=el.dataset.tip;tip.hidden=false;const gr=g.getBoundingClientRect(),er=el.getBoundingClientRect();let x=(ev&&ev.clientX?ev.clientX:er.left+er.width/2)-gr.left;tip.style.left=Math.max(8,Math.min(gr.width-tip.offsetWidth-8,x-tip.offsetWidth/2))+'px';tip.style.top=Math.max(0,er.top-gr.top-6)+'px'};
  g.querySelectorAll('.dv-hit').forEach(el=>{el.addEventListener('pointermove',e=>mostra(el,e));el.addEventListener('focus',()=>mostra(el));el.addEventListener('pointerleave',()=>tip.hidden=true);el.addEventListener('blur',()=>tip.hidden=true)})}
function metricasV(){
  if(!S.carregou){carregar();return '<section class="mv-blk"><p class="dv-l2">Carregando os números…</p></section>'}
  const m=S.mes,tot=somaMes(m),M=S.d.meses[m]||{},w=S.d.semanas[S.sem]||{},wa=S.d.semanas[mais(S.sem,-7)]||{},sems=Object.keys(S.d.semanas).sort().reverse();
  const steps=FUNIL.map((k,i)=>({k,v:tot[k],c:i?pct(tot[k],tot[FUNIL[i-1]]):null})),topo=Math.max(1,...steps.map(s=>+s.v||0));
  const delta=(a,b)=>{if(vazio(a)||vazio(b))return '<span class="dv-l2">—</span>';const d=a-b;if(!d)return '<span class="dv-dl">= igual</span>';return `<span class="dv-dl ${d>0?'up':'dn'}"><svg viewBox="0 0 10 10" aria-hidden="true"><path d="${d>0?'M5 2 9 8H1z':'M5 8 1 2h8z'}"/></svg>${d>0?'+':'−'}${nf(Math.abs(d))}</span>`};
  return `${S.off?'<section class="mv-aviso">Sem conexão com o servidor: o que salvar agora fica só neste aparelho.</section>':''}
  <section class="dv-mesbar"><button class="mv-b sm" onclick="__dvMes(-1)" aria-label="Mês anterior">‹</button><b>${esc(nomeMes(m).replace(/^./,c=>c.toUpperCase()))}</b><button class="mv-b sm" onclick="__dvMes(1)" aria-label="Próximo mês">›</button><span class="mv-grow"></span><a class="mv-b pri" href="#dados" onclick="event.preventDefault();document.getElementById('dv-form').scrollIntoView({behavior:'smooth',block:'start'})">Lançar a semana</a></section>
  <section class="dv-ns">
   <div class="dv-ns1"><span class="dv-k or">Métrica principal · Data Squad</span><h3 class="dv-nt">Pacotes de telas pagos</h3><div class="dv-big">${vazio(tot.pacotes)?'—':`<span data-dv-n="${tot.pacotes}"><b>${nfH(tot.pacotes)}</b></span>`}</div>
    ${barraMeta(tot.pacotes,M.metaPacotes)||'<span class="dv-l2">Meta do mês ainda não definida.</span>'}<p class="dv-def">É o que paga a operação e mostra quanto da programação está vendida. Todos os outros números servem a este.</p>${crmLinha()}</div>
   <div><span class="dv-k">Receita do mês</span><div class="dv-big sm">${vazio(M.receita)?'—':brl(M.receita)}</div>${vazio(M.metaReceita)?`<span class="dv-l2">${vazio(M.receita)?'Lance no fim do mês, em Receita e metas.':'Sem meta definida.'}</span>`:barraMeta(M.receita,M.metaReceita)}</div>
   <div><span class="dv-k">Fechamentos no mês</span><div class="dv-big sm">${vazio(tot.fechamentos)?'—':nf(tot.fechamentos)}</div>${vazio(M.metaFechamentos)?`<span class="dv-l2">${vazio(tot.fechamentos)?'Soma das semanas lançadas no mês.':'Sem meta definida.'}</span>`:barraMeta(tot.fechamentos,M.metaFechamentos)}</div>
  </section>
  <section class="dv-g2">
   <div class="mv-blk"><h4 class="mv-h4">Funil de ${esc(MESES[+m.slice(5,7)-1])}</h4>
    ${steps.map((s,i)=>`<div class="dv-fn"><span>${String(i+1).padStart(2,'0')} ${esc(NOMEC[s.k])}</span><div class="barra"><i style="width:${vazio(s.v)?0:(+s.v/topo*100)}%"></i></div><b class="mv-mono">${vazio(s.v)?'—':nf(s.v)}</b><span class="dv-cv">${i?pctTxt(s.c):''}</span></div>`).join('')}
    <div class="dv-taxas"><div><span class="dv-k">Contato → fechamento</span><b>${pctTxt(pct(tot.fechamentos,tot.contatos))}</b></div><div><span class="dv-k">Proposta → fechamento</span><b>${pctTxt(pct(tot.fechamentos,tot.propostas))}</b></div><div><span class="dv-k">Renovação</span><b>${pctTxt(pct(tot.renovacoes,tot.vencidos))}</b><span class="dv-l2">${vazio(tot.renovacoes)?'':nf(tot.renovacoes)+' de '+(vazio(tot.vencidos)?'—':nf(tot.vencidos))+' que venceram'}</span></div></div>
   </div>
   <div class="mv-blk"><h4 class="mv-h4">Semana a semana · últimas 8</h4>
    <nav class="mv-seg dv-seg2" aria-label="Número do gráfico">${['contatos','mapas','propostas','fechamentos','pacotes'].map(k=>`<button class="${ui.met===k?'on':''}" aria-pressed="${ui.met===k}" onclick="__dvMet('${k}')">${esc(CURTO[k])}</button>`).join('')}</nav>${grafico()}</div>
  </section>
  <section class="mv-blk dv-ss"><div class="dv-semnav"><h4 class="mv-h4">Esta semana × anterior</h4><span class="mv-grow"></span><button class="mv-b sm" onclick="__dvSem(-7)" aria-label="Semana anterior">‹</button><b class="mv-mono">${rotSem(S.sem)}</b><button class="mv-b sm" onclick="__dvSem(7)" aria-label="Próxima semana">›</button></div>
   <div class="dv-tw"><table class="dv-t"><thead><tr><th>Número</th><th>${rotSem(mais(S.sem,-7))}</th><th>${rotSem(S.sem)}</th><th>Variação</th></tr></thead><tbody>
   ${CAMPOS.map(([k,n])=>`<tr><td>${esc(n)}</td><td class="mv-mono">${vazio(wa[k])?'—':nf(wa[k])}</td><td class="mv-mono">${vazio(w[k])?'—':nf(w[k])}</td><td>${delta(w[k],wa[k])}</td></tr>`).join('')}
   <tr><td>Proposta → fechamento</td><td class="mv-mono">${pctTxt(pct(wa.fechamentos,wa.propostas))}</td><td class="mv-mono">${pctTxt(pct(w.fechamentos,w.propostas))}</td><td></td></tr></tbody></table></div></section>
  <section class="mv-blk" id="dv-form"><h4 class="mv-h4">Lançar a semana de ${rotSem(S.sem)}</h4><p class="dv-l2" style="margin:0 0 12px">Só números reais da equipe. Deixe em branco o que não foi medido.${w.em?` Último lançamento: ${esc(w.por||'equipe')}, ${new Date(w.em).toLocaleString('pt-BR',{day:'2-digit',month:'2-digit',hour:'2-digit',minute:'2-digit'})}.`:''}</p>
   <form class="mv-form dv-f" onsubmit="event.preventDefault();__dvSalvaSem(this)">${CAMPOS.map(([k,n,dica])=>`<label title="${esc(dica)}">${esc(n)}<input type="number" name="${k}" min="0" step="1" inputmode="numeric" value="${vazio(w[k])?'':esc(w[k])}"></label>`).join('')}
    <label class="w2">Observação<input name="obs" maxlength="200" value="${esc(w.obs||'')}" placeholder="Ex.: 2 visitas canceladas pela chuva"></label>
    <div class="mv-acoes w2"><button type="button" class="mv-b" onclick="__dvCrm()">Puxar do CRM</button><span class="mv-grow"></span><button class="mv-b pri">Salvar semana</button></div></form>
   <details class="dv-det"><summary>Como contar cada número</summary><ul>${CAMPOS.map(([,n,dica])=>`<li><b>${esc(n)}:</b> ${esc(dica)}</li>`).join('')}<li><b>Receita do mês:</b> valor que entrou no caixa no mês.</li><li>A semana vai de segunda a domingo e conta no mês da quinta-feira.</li></ul></details></section>
  <section class="mv-blk"><h4 class="mv-h4">Receita e metas de ${esc(nomeMes(m))}</h4>
   <form class="mv-form dv-f4" onsubmit="event.preventDefault();__dvSalvaMes(this)"><label>Receita do mês (R$)<input type="number" name="receita" min="0" step="0.01" inputmode="decimal" value="${vazio(M.receita)?'':esc(M.receita)}"></label><label>Meta de pacotes pagos<input type="number" name="metaPacotes" min="0" step="1" inputmode="numeric" value="${vazio(M.metaPacotes)?'':esc(M.metaPacotes)}"></label><label>Meta de fechamentos<input type="number" name="metaFechamentos" min="0" step="1" inputmode="numeric" value="${vazio(M.metaFechamentos)?'':esc(M.metaFechamentos)}"></label><label>Meta de receita (R$)<input type="number" name="metaReceita" min="0" step="0.01" inputmode="decimal" value="${vazio(M.metaReceita)?'':esc(M.metaReceita)}"></label>
    <div class="mv-acoes w2"><span class="mv-grow"></span><button class="mv-b pri">Salvar mês</button></div></form></section>
  <section class="mv-blk"><div class="dv-semnav"><h4 class="mv-h4">Todas as semanas lançadas <span>${sems.length}</span></h4><span class="mv-grow"></span>${sems.length?'<button class="mv-b sm" onclick="__dvCsv()">Exportar CSV</button>':''}</div>
   ${sems.length?`<div class="dv-tw"><table class="dv-t"><thead><tr><th>Semana</th>${CAMPOS.map(c=>`<th>${esc(CURTO[c[0]])}</th>`).join('')}<th>Lançado por</th></tr></thead><tbody>${sems.map(s=>{const x=S.d.semanas[s];return `<tr class="dv-lk" onclick="__dvVai('${s}')"><td class="mv-mono">${rotSem(s)}</td>${CAMPOS.map(([k])=>`<td class="mv-mono">${vazio(x[k])?'—':nf(x[k])}</td>`).join('')}<td>${esc(x.por||'')}</td></tr>`}).join('')}</tbody></table></div>`:'<p class="dv-vz">Nenhuma semana lançada ainda. Os números aparecem aqui quando a equipe salvar a primeira.</p>'}</section>`}
const semDoMes=m=>{if(m===mesDaSem(semHoje()))return semHoje();let s=segDe(new Date(+m.slice(0,4),+m.slice(5,7)-1,1,12));if(mesDaSem(s)!==m)s=mais(s,7);return s};
window.__dvMes=n=>{S.mes=mesMais(S.mes,n);if(mesDaSem(S.sem)!==S.mes)S.sem=semDoMes(S.mes);rr()};
window.__dvSem=n=>{S.sem=mais(S.sem,n);S.mes=mesDaSem(S.sem);rr()};
window.__dvVai=s=>{S.sem=s;S.mes=mesDaSem(s);rr();setTimeout(()=>{const f=document.getElementById('dv-form');f&&f.scrollIntoView({behavior:'smooth',block:'start'})},60)};
window.__dvMet=k=>{ui.met=k;salvaUi();rr()};
const num=v=>{v=String(v??'').trim().replace(',','.');return v===''||isNaN(+v)||+v<0?null:+v};
window.__dvSalvaSem=f=>{const k0=S.sem,rec={};CAMPOS.forEach(([k])=>{const v=num(f[k].value);if(v!==null)rec[k]=Math.round(v)});const obs=f.obs.value.trim();if(obs)rec.obs=obs;
  if(!Object.keys(rec).length&&!S.d.semanas[k0]){toast('Preencha pelo menos um número.');return}
  rec.por=S.nome||'equipe';rec.em=new Date().toISOString();
  const tem=Object.keys(rec).length>2;mut(d=>{if(tem)d.semanas[k0]=Object.assign({},rec);else delete d.semanas[k0]},tem?'Semana salva.':'Semana apagada.')};
window.__dvSalvaMes=f=>{const m=S.mes,rec={};['receita','metaPacotes','metaFechamentos','metaReceita'].forEach(k=>{const v=num(f[k].value);if(v!==null)rec[k]=v});
  rec.por=S.nome||'equipe';rec.em=new Date().toISOString();const tem=Object.keys(rec).length>2;mut(d=>{if(tem)d.meses[m]=Object.assign({},rec);else delete d.meses[m]},tem?'Mês salvo.':'Mês limpo.')};
window.__dvCrm=async()=>{const api=window.__crmMova;if(!api){toast('O CRM não está disponível nesta página.');return}
  let c=api.get();if(!c){await api.carregar();c=api.get()}if(!c){toast('Não consegui ler o CRM agora.');return}
  const ini=dt(S.sem).getTime()-12*36e5,fim=ini+7*864e5,dentro=s=>{const x=new Date(s).getTime();return x>=ini&&x<fim};let o={contatos:0,mapas:0,propostas:0,fechamentos:0};
  (c.itens||[]).forEach(l=>{if(l.criado&&dentro(l.criado))o.contatos++;(l.hist||[]).forEach(h=>{if(h.tipo!=='etapa'||!h.em||!dentro(h.em))return;const t=h.txt||'';if(/→ Mapa \/ demonstração/.test(t))o.mapas++;else if(/→ Proposta enviada/.test(t))o.propostas++;else if(/→ Fechado/.test(t))o.fechamentos++})});
  if(S.sem===semHoje())o.pacotes=(c.itens||[]).filter(l=>['e7','e8','e9'].includes(l.etapa)&&/^(p|combo)(10|15|20)$/.test(l.plano||'')).length;
  setTimeout(()=>{const f=document.querySelector('#dv-form form');if(!f)return;Object.entries(o).forEach(([k,v])=>{if(f[k])f[k].value=v});toast('Números do CRM desta semana no formulário. Confira e salve.')},80)};
window.__dvCsv=()=>{const q=v=>`"${String(v??'').replace(/"/g,'""')}"`,ks=CAMPOS.map(c=>c[0]);
  const linhas=[['semana_inicio','semana_fim',...ks,'obs','lancado_por'].join(';'),...Object.keys(S.d.semanas).sort().map(s=>{const x=S.d.semanas[s];return [s,mais(s,6),...ks.map(k=>vazio(x[k])?'':x[k]),x.obs||'',x.por||''].map(q).join(';')})];
  const a=document.createElement('a');a.href=URL.createObjectURL(new Blob(['﻿'+linhas.join('\n')],{type:'text/csv'}));a.download=`mova-dados-vendas-${hoje()}.csv`;a.click()};

// ---------- 3 · perspectivas ----------
function perspV(){const prox=C.datas.filter(x=>(x.fim||x.ini)>=hoje()).sort((a,b)=>a.ini.localeCompare(b.ini)).slice(0,4);
  return `<section class="dv-grupo"><header class="dv-gh"><span class="dv-k">01</span><h3>Tendências</h3></header>
  ${C.perspectivas.map((p,i)=>`<article class="dv-pp"><div class="dv-pn"><span class="dv-idx mv-mono">${String(i+1).padStart(2,'0')}</span>${p.n?numHtml(p.n):''}${p.n&&p.n.rot?`<span class="dv-l2">${esc(p.n.rot)}</span>`:''}</div><div class="dv-txt"><h4 class="dv-pt">${esc(p.titulo)}</h4><p>${esc(p.dado)}</p>${fonteHtml(p.fonte,p.data,p.url)}</div>
   <div class="dv-usar"><span class="dv-k or">O que fazer</span><p>${esc(p.fazer)}</p></div></article>`).join('')}</section>
  <section class="dv-grupo"><header class="dv-gh"><span class="dv-k">02</span><h3>Datas fortes em São Luís</h3></header>
  ${prox.length?'':'<p class="dv-vz">Sem datas futuras cadastradas. Atualize o dados-vendas.json.</p>'}<ol class="dv-tl">${prox.map((x,i)=>{const n=diasAte(x.ini),dentro=n<=0&&(x.fim||x.ini)>=hoje();return `<li class="${i?'':'prox'}"><div class="dv-dt"><b>${esc(x.rotulo)}</b><span class="dv-l2">${dentro?'acontecendo agora':n===1?'falta 1 dia':`faltam ${nf(n)} dias`}</span></div>
   <div class="dv-txt"><h4 class="dv-pt">${esc(x.nome)}</h4><p>${esc(x.dado)}</p>${fonteHtml(x.fonte,x.data,x.url)}</div><div class="dv-usar"><span class="dv-k or">Quando vender</span><p>${esc(x.vender)}</p>${x.ate?`<span class="dv-prazo">${diasAte(x.ate)<0?`Prazo ideal (${br(x.ate)}) já passou: vale para o próximo ciclo.`:diasAte(x.ate)===0?'Hoje é o último dia do prazo ideal.':`Prazo ideal para fechar: ${br(x.ate)} · faltam ${nf(diasAte(x.ate))} dias`}</span>`:''}</div></li>`}).join('')}</ol></section>`}

// ---------- 4 · aplicar às vendas ----------
const T=C.tabela;
function calcVals(){const k=S.calc,p=T.pacote[k.dur],ex=!!k.excl,fat=ex?1+T.exclusividade:1,meses=ex?Math.max(k.meses,T.exclusividadeMeses):k.meses,carros=Math.max(0,Math.min(200,Math.round(+k.carros||0)));
  return {p,ex,meses,carros,dia:p*fat/T.dias,diaTela:p*fat/T.dias/T.telas,total:p*fat*meses,ins:T.telas*T.insercoesPorTela,adDia:T.adesivoMax/T.dias,adDiaTot:carros*T.adesivoMax/T.dias,adTotal:carros*T.adesivoMax*meses}}
function fraseCalc(){const v=calcVals(),k=S.calc;
  return `As 10 telas com vídeo de ${k.dur} segundos saem a partir de ${brl(v.dia,2)} por dia${v.ex?', já com a exclusividade do seu ramo':''}. Seu anúncio passa a partir de ${T.insercoesPorTela} vezes por dia em cada tela, com QR pro seu WhatsApp.${v.carros?` O adesivo no vidro sai por até ${brl(v.adDia,2)} por dia por carro, e fica mais barato com mais carros e mais meses.`:''} O valor final a gente fecha na conversa.`}
function calcSaida(){const v=calcVals(),el=document.getElementById('dv-calc-out');if(!el)return;
  el.innerHTML=`<span class="dv-k">Telas · ${S.calc.dur} s · por dia</span><div class="dv-big dv-cbig"><span class="dv-ap">a partir de</span><span><span class="dv-pre">R$</span>${nfH(v.dia,2)}</span></div>
   <p class="dv-l2">${brl(v.diaTela,2)} por tela por dia · a partir de ${nf(v.ins)} inserções por dia (${T.insercoesPorTela} em cada tela)${v.ex?' · com exclusividade (+50%)':''}</p>
   ${v.carros?`<div class="dv-ad"><span class="dv-k">Adesivo no vidro · ${v.carros} carro${v.carros>1?'s':''}</span><b>até ${brl(v.adDiaTot,2)} por dia</b><span class="dv-l2">até ${brl(v.adDia,2)} por dia por carro (R$ ${nf(T.adesivoMax)} ÷ ${T.dias} dias). Cai com mais carros e mais meses.</span></div>`:''}
   <div class="dv-tot"><div><span class="dv-k">Telas · ${v.meses} ${v.meses>1?'meses':'mês'}</span><b>a partir de ${brl(v.total)}</b></div>${v.carros?`<div><span class="dv-k">Adesivo · ${v.meses} ${v.meses>1?'meses':'mês'}</span><b>até ${brl(v.adTotal)}</b></div>`:''}</div>
   ${v.ex&&S.calc.meses<T.exclusividadeMeses?`<p class="dv-l2">A exclusividade pede contrato de ${T.exclusividadeMeses} meses: o total já considera ${T.exclusividadeMeses}.</p>`:''}
   <div class="dv-frase"><span class="dv-k or">Frase pronta</span><p>${esc(fraseCalc())}</p><button class="dv-cp" data-dv-cp="calc">Copiar frase</button></div>`}
window.__dvCalc=(k,v)=>{if(k==='dur')S.calc.dur=v;else if(k==='meses')S.calc.meses=Math.max(1,Math.min(24,parseInt(v)||1));else if(k==='excl')S.calc.excl=!!v;else if(k==='carros')S.calc.carros=Math.max(0,Math.min(200,parseInt(v)||0));
  if(k==='dur')document.querySelectorAll('#dv-calc .dv-dur button').forEach(b=>{const on=b.dataset.v===v;b.classList.toggle('on',on);b.setAttribute('aria-pressed',on)});calcSaida()};
window.__dvVend=v=>{ui.vend=(v||'').trim().slice(0,30)||'Paulo';salvaUi();document.querySelectorAll('#conteudo .dv-wa').forEach(p=>{p.textContent=p.dataset.t.replace(/\{vendedor\}/g,ui.vend)})};
window.__dvNicho=id=>{ui.nicho=id;salvaUi();rr()};
function vendasV(){const n=C.nichos.find(x=>x.id===ui.nicho)||C.nichos[0],k=S.calc;setTimeout(calcSaida,0);
  const whats=()=>n.whats.replace(/\{vendedor\}/g,ui.vend);
  return `<section class="dv-alerta" role="note"><span class="dv-k or">Lembrete fixo</span><ul>${C.lembretes.map(t=>`<li>${esc(t)}</li>`).join('')}</ul>${fonteHtml(C.lembreteFonte.texto,'',C.lembreteFonte.url)}</section>
  <section class="mv-blk dv-calc" id="dv-calc"><h4 class="mv-h4">Quanto custa por dia</h4><p class="dv-l2" style="margin:0 0 14px">Só a tabela oficial (a partir de), dividida pelos dias. Sem alcance e sem custo por mil inventados.</p>
   <div class="dv-cg"><div class="dv-cin">
    <span class="dv-k">Duração do vídeo</span><nav class="mv-seg dv-dur" aria-label="Duração do vídeo">${Object.keys(T.pacote).map(d=>`<button type="button" data-v="${d}" class="${k.dur===d?'on':''}" aria-pressed="${k.dur===d}" onclick="__dvCalc('dur','${d}')">${d} s · ${brl(T.pacote[d])}</button>`).join('')}</nav>
    <div class="mv-form dv-cf"><label>Meses de contrato<input type="number" min="1" max="24" value="${k.meses}" inputmode="numeric" oninput="__dvCalc('meses',this.value)"></label><label>Carros com adesivo<input type="number" min="0" max="200" value="${k.carros}" inputmode="numeric" oninput="__dvCalc('carros',this.value)"></label>
     <label class="mv-chk"><input type="checkbox" ${k.excl?'checked':''} onchange="__dvCalc('excl',this.checked)"> Exclusividade do ramo (+50% nas telas, contrato de ${T.exclusividadeMeses} meses)</label></div>
    <p class="dv-l2 dv-tab">${esc(T.fonte)}: pacote das ${T.telas} telas por ${T.dias} dias a partir de ${Object.entries(T.pacote).map(([d,p])=>`${brl(p)} (${d} s)`).join(', ')}. Adesivo: até ${brl(T.adesivoMax)} por carro a cada ${T.dias} dias.</p></div>
    <div class="dv-cout" id="dv-calc-out" aria-live="polite"></div></div></section>
  <section class="mv-blk"><div class="dv-semnav"><h4 class="mv-h4">Argumentos por ramo</h4><span class="mv-grow"></span><label class="dv-vend">Seu nome na mensagem<input value="${esc(ui.vend)}" maxlength="30" onchange="__dvVend(this.value)"></label></div>
   <nav class="mv-seg dv-nichos" aria-label="Ramo">${C.nichos.map(x=>`<button class="${x.id===n.id?'on':''}" aria-pressed="${x.id===n.id}" onclick="__dvNicho('${x.id}')">${esc(x.nome)}</button>`).join('')}</nav>
   <div class="dv-nicho"><div class="dv-ni1"><span class="dv-k">A dor, nas palavras dele</span><p class="dv-dor">“${esc(n.dor)}”</p><span class="dv-k">Por que a Mova encaixa</span><p>${esc(n.argumento)}</p>
     <span class="dv-k">O dado que sustenta</span><p class="dv-dado">${esc(n.dado)}</p>${fonteHtml(n.fonte,'',n.url)}${n.cuidado?`<p class="dv-cuid">${esc(n.cuidado)}</p>`:''}</div>
    <div class="dv-ni2"><span class="dv-k or">Primeira mensagem no WhatsApp</span><p class="dv-wa" data-t="${esc(n.whats)}">${esc(whats())}</p><button class="mv-b pri" onclick="__dvCopiaWa()">Copiar mensagem</button><p class="dv-l2">Troque [nome] pelo nome do dono. Padrão: conexão, dor, desejo e pergunta, sem preço e sem link.</p></div></div></section>
  <section class="mv-blk"><h4 class="mv-h4">As 6 objeções mais comuns</h4>
   ${C.objecoes.map(o=>`<div class="dv-ob"><div class="dv-ob1"><b>“${esc(o.obj)}”</b><span class="dv-l2">Por trás: ${esc(o.porTras)}</span></div><p>${esc(o.resposta)}</p><button class="dv-cp" data-dv-cp="${cp(o.resposta)}">Copiar resposta</button></div>`).join('')}</section>`}
window.__dvCopiaWa=()=>{const n=C.nichos.find(x=>x.id===ui.nicho)||C.nichos[0];copiar(n.whats.replace(/\{vendedor\}/g,ui.vend))};

// ---------- tela ----------
const ABAS=[['mercado','Mercado','Números de fontes públicas, abertos e conferidos em '+C.conferido+'. Cada um com a fonte e o jeito de usar na conversa.'],['metricas','Métricas','Os números da equipe, semana a semana. Começa vazio: só entra o que a equipe lançar.'],['perspectivas','Perspectivas','Para onde a mídia está indo e as datas que mais vendem em São Luís.'],['vendas','Aplicar às vendas','Argumentos por ramo, respostas para as objeções e quanto custa por dia.']];
window.__dvAba=k=>{ui.aba=k;salvaUi();rr();window.scrollTo({top:0,behavior:'instant'})};
function view(){for(const k in COPIA)delete COPIA[k];if(!ABAS.some(a=>a[0]===ui.aba))ui.aba='mercado';const a=ABAS.find(x=>x[0]===ui.aba);
  setTimeout(()=>{conta();ligaTip()},40);
  const corpo=ui.aba==='mercado'?mercadoV():ui.aba==='metricas'?metricasV():ui.aba==='perspectivas'?perspV():vendasV();
  return `<section class="dv-topo"><nav class="mv-seg dv-nav" aria-label="Seções de Dados e Vendas">${ABAS.map(([k,n])=>`<button class="${ui.aba===k?'on':''}" aria-pressed="${ui.aba===k}" onclick="__dvAba('${k}')">${n}</button>`).join('')}</nav><p class="dv-intro">${esc(a[2])}</p></section>${corpo}`}
window.__V.dados=view;window.__T.dados='Dados e Vendas';
{const mq=matchMedia('(max-width:700px)'),f=()=>{if(location.hash==='#dados'&&ui.aba==='metricas')rr()};mq.addEventListener?mq.addEventListener('change',f):mq.addListener&&mq.addListener(f)}

// ---------- visual (identidade da Mova: asfalto, laranja só no detalhe, Archivo + JetBrains Mono, fio de 1px) ----------
document.head.insertAdjacentHTML('beforeend',`<style id="dv-css">
#conteudo{--dv-serie:#F2541D}
.dv-k{font:500 10.5px var(--f-dado);letter-spacing:.16em;text-transform:uppercase;color:var(--apagado)}.dv-k.or{color:var(--amarelo)}
.dv-l2{color:var(--apagado);font-size:12.5px;line-height:1.5}.dv-vz{color:#5E636C;font:500 11px var(--f-dado);letter-spacing:.1em;text-transform:uppercase;padding:14px 0;margin:0}
.dv-topo{display:grid;gap:10px}.dv-nav{justify-self:start}.dv-intro{margin:0;color:var(--apagado);font-size:13px;max-width:70ch}
.dv-grupo{border-top:1px solid var(--linha);padding-top:22px}
.dv-gh{display:flex;gap:14px;align-items:baseline;margin-bottom:4px}.dv-gh h3{margin:0;font:italic 900 24px/1.1 var(--f-titulo);letter-spacing:-.01em;font-stretch:112%}
.dv-stat,.dv-pp,.dv-tl li{display:grid;grid-template-columns:minmax(170px,230px) minmax(0,1.4fr) minmax(0,1fr);gap:32px;padding:26px 0;border-bottom:1px solid var(--linha);align-items:start}
.dv-stat:last-child,.dv-pp:last-child,.dv-tl li:last-child{border-bottom:0}
.dv-num{font:500 54px/.95 var(--f-dado);letter-spacing:-.045em;color:var(--texto);font-variant-numeric:tabular-nums;white-space:nowrap}
.dv-num b{font-weight:500}.vg{font-style:normal;margin:0 -.2em}.dv-pre{font:500 .36em var(--f-corpo);letter-spacing:0;color:var(--apagado);margin-right:.3em;vertical-align:1.15em}.dv-suf{font:600 .38em var(--f-corpo);letter-spacing:0;color:var(--amarelo);margin-left:.12em}
.dv-onde{display:block;font:500 10.5px var(--f-dado);letter-spacing:.14em;text-transform:uppercase;color:var(--apagado);margin-bottom:9px}
.dv-txt p{margin:0;font-size:15.5px;line-height:1.55;color:var(--texto);max-width:58ch}
.dv-fonte{display:inline-block;justify-self:start;max-width:100%;margin-top:12px;font:500 11.5px/1.5 var(--f-dado);color:var(--apagado);text-decoration:none;border-bottom:1px solid var(--linha2);padding-bottom:1px}
.dv-fonte svg{width:9px;height:9px;fill:none;stroke:currentColor;stroke-width:1.6;margin-left:6px;vertical-align:0}.dv-fonte:hover,.dv-fonte:focus-visible{color:var(--texto);border-color:var(--amarelo)}
.dv-usar{border-left:1px solid var(--linha);padding-left:22px;display:grid;gap:9px;align-content:start}.dv-usar p{margin:0;font-size:14px;line-height:1.55;color:#CFCBC3}
.dv-cp{justify-self:start;background:none;border:1px solid var(--linha2);color:var(--texto);border-radius:var(--r1,8px);padding:6px 11px;font:600 12px var(--f-corpo);cursor:pointer}.dv-cp:hover{border-color:var(--amarelo)}.dv-cp:focus-visible{outline:2px solid var(--amarelo);outline-offset:2px}
.dv-nota{border-top:1px solid var(--linha);padding-top:14px}.dv-nota p{margin:0;color:var(--apagado);font-size:12.5px;line-height:1.6;max-width:90ch}
.dv-idx{color:var(--amarelo);font-size:13px;padding-top:4px}.dv-pt{margin:0 0 8px;font:italic 900 19px/1.2 var(--f-titulo);letter-spacing:-.005em;color:var(--texto)}
.dv-tl{list-style:none;margin:0;padding:0}.dv-dt b{display:block;font:500 22px/1.15 var(--f-dado);letter-spacing:-.02em;color:var(--texto);margin-bottom:6px}
.dv-tl li.prox .dv-dt b{color:var(--amarelo)}.dv-tl li.prox .dv-dt .dv-l2{color:var(--texto)}
/* métricas */
.dv-mesbar{display:flex;align-items:center;gap:10px;flex-wrap:wrap}.dv-mesbar b{font:italic 900 20px var(--f-titulo);min-width:0}
.dv-ns{display:grid;grid-template-columns:1.6fr 1fr 1fr;border:1px solid var(--linha);border-radius:var(--r2,12px);background:var(--painel)}
.dv-ns>div{padding:20px 22px;border-left:1px solid var(--linha);display:grid;gap:8px;align-content:start}.dv-ns>div:first-child{border-left:0}
.dv-nt{margin:0;font:italic 900 22px/1.1 var(--f-titulo);letter-spacing:-.01em}
.dv-big{font:500 46px/1 var(--f-dado);letter-spacing:-.04em;color:var(--texto);font-variant-numeric:tabular-nums}.dv-big b{font-weight:500}.dv-big.sm{font-size:30px}.dv-cbig{display:flex;align-items:baseline;gap:12px;flex-wrap:wrap}.dv-ap{font:500 14px var(--f-corpo);letter-spacing:0;color:var(--apagado)}.dv-cbig .dv-pre{vertical-align:.75em}
.dv-pn{display:grid;gap:10px;align-content:start}.dv-pn .dv-num{font-size:44px}.dv-prazo{font:500 11.5px/1.5 var(--f-dado);color:var(--texto);border-top:1px solid var(--linha);padding-top:8px}
.dv-def{margin:4px 0 0;color:var(--apagado);font-size:12.5px;line-height:1.5;max-width:52ch}.dv-crm{margin:2px 0 0;font-size:12.5px;color:#CFCBC3;border-top:1px solid var(--linha);padding-top:10px}.dv-crm b{color:var(--texto);font-family:var(--f-dado)}
.dv-meta{height:6px;margin-top:4px}
.dv-g2{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.15fr);gap:12px}.dv-g2>.mv-blk{margin:0}
.dv-fn{display:grid;grid-template-columns:150px minmax(0,1fr) 44px 52px;gap:12px;align-items:center;padding:8px 0;font-size:13px}.dv-fn .barra{height:8px}.dv-fn .barra i{background:var(--dv-serie)}
.dv-fn b{text-align:right;color:var(--texto)}.dv-cv{font:500 11.5px var(--f-dado);color:var(--apagado);text-align:right}
.dv-taxas{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px;border-top:1px solid var(--linha);margin-top:10px;padding-top:12px}.dv-taxas>div{display:grid;gap:4px}.dv-taxas b{font:500 22px var(--f-dado);letter-spacing:-.02em}
.dv-seg2{margin-bottom:6px}.dv-seg2 button{padding:6px 11px;font-size:12.5px}
.dv-graf{position:relative}.dv-graf svg{width:100%;height:auto;display:block;overflow:visible}
.dv-gl{stroke:var(--linha);stroke-width:1}.dv-base{stroke:var(--linha2);stroke-width:1}
.dv-ax{fill:var(--apagado);font:500 10.5px var(--f-dado)}.dv-ax.on{fill:var(--texto)}.dv-vl{fill:var(--texto);font:600 12px var(--f-dado)}
.dv-bar{fill:var(--dv-serie);opacity:.55}.dv-bar.on{opacity:1}.dv-hit{fill:transparent;cursor:default;outline:none}.dv-hit:focus-visible{stroke:var(--amarelo);stroke-width:1}
.dv-graf .dv-vz{position:absolute;left:0;right:0;top:38%;text-align:center}
.dv-tip{position:absolute;transform:translateY(-100%);background:var(--painel2);border:1px solid var(--linha2);color:var(--texto);font:500 12px var(--f-dado);padding:6px 9px;border-radius:6px;pointer-events:none;white-space:nowrap;z-index:2}
.dv-semnav{display:flex;align-items:center;gap:8px;flex-wrap:wrap;margin-bottom:8px}.dv-semnav .mv-h4{margin:0}
.dv-tw{overflow-x:auto}.dv-t{width:100%;border-collapse:collapse;font-size:13px}.dv-t th{text-align:left;font:500 10.5px var(--f-dado);letter-spacing:.12em;text-transform:uppercase;color:var(--apagado);padding:9px 10px;border-bottom:1px solid var(--linha);white-space:nowrap}
.dv-t td{padding:10px;border-bottom:1px solid var(--linha);white-space:nowrap}.dv-t tr:last-child td{border-bottom:0}.dv-lk{cursor:pointer}.dv-lk:hover{background:var(--painel2)}
.dv-dl{display:inline-flex;align-items:center;gap:5px;font:500 12px var(--f-dado);color:var(--texto)}.dv-dl svg{width:9px;height:9px}.dv-dl.up svg{fill:var(--ok)}.dv-dl.dn svg{fill:var(--erro)}
.dv-f{grid-template-columns:repeat(4,minmax(0,1fr))!important}.dv-f4{grid-template-columns:repeat(4,minmax(0,1fr))!important}
.dv-det{margin-top:14px;border-top:1px solid var(--linha);padding-top:10px}.dv-det summary{cursor:pointer;color:var(--apagado);font-size:13px}.dv-det ul{margin:10px 0 0;padding-left:18px;color:#CFCBC3;font-size:13px;line-height:1.6}
/* vendas */
.dv-alerta{border:1px solid var(--linha);border-left:2px solid var(--amarelo);border-radius:var(--r2,12px);background:var(--painel);padding:16px 20px;display:grid;gap:8px}
.dv-alerta ul{margin:0;padding-left:18px;display:grid;gap:4px;font-size:14px;line-height:1.5}.dv-alerta .dv-fonte{margin-top:2px}
.dv-cg{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.05fr);gap:28px;align-items:start}.dv-cin{display:grid;gap:12px}
.dv-dur{justify-self:start}.dv-cf{grid-template-columns:1fr 1fr!important}.dv-tab{margin:0}
.dv-cout{border-left:1px solid var(--linha);padding-left:26px;display:grid;gap:10px;align-content:start}
.dv-ad{display:grid;gap:4px;border-top:1px solid var(--linha);padding-top:12px}.dv-ad b{font:500 20px var(--f-dado);letter-spacing:-.02em}
.dv-tot{display:grid;grid-template-columns:1fr 1fr;gap:12px;border-top:1px solid var(--linha);padding-top:12px}.dv-tot>div{display:grid;gap:4px}.dv-tot b{font:500 16px var(--f-dado)}
.dv-frase{display:grid;gap:8px;border-top:1px solid var(--linha);padding-top:12px}.dv-frase p{margin:0;font-size:14px;line-height:1.55;color:#CFCBC3}
.dv-vend{display:flex;gap:8px;align-items:center;font:500 10.5px var(--f-dado);letter-spacing:.12em;text-transform:uppercase;color:var(--apagado)}
.dv-vend input{background:var(--painel2);color:var(--texto);border:1px solid var(--linha);border-radius:var(--r1,8px);padding:7px 9px;font:500 13px var(--f-corpo);width:130px;text-transform:none;letter-spacing:0}
.dv-nichos{margin:4px 0 14px}.dv-nicho{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,1fr);gap:28px;align-items:start}
.dv-ni1{display:grid;gap:6px}.dv-ni1 p{margin:0 0 10px;font-size:14.5px;line-height:1.55}.dv-ni1 .dv-fonte{margin-top:-4px}
.dv-dor{font:italic 900 21px/1.25 var(--f-titulo)!important;letter-spacing:-.005em;color:var(--texto)}.dv-dado{color:var(--texto)}
.dv-cuid{color:var(--alerta)!important;font-size:13px!important;margin-top:10px!important}
.dv-ni2{border-left:1px solid var(--linha);padding-left:26px;display:grid;gap:10px;align-content:start}
.dv-wa{margin:0;white-space:pre-line;background:var(--painel2);border:1px solid var(--linha);border-radius:var(--r2,12px);padding:14px 16px;font-size:14.5px;line-height:1.55}
.dv-ni2 .mv-b{justify-self:start}
.dv-ob{display:grid;grid-template-columns:minmax(0,.9fr) minmax(0,1.6fr) auto;gap:22px;align-items:start;padding:16px 0;border-top:1px solid var(--linha)}.dv-ob:first-of-type{border-top:0}
.dv-ob1{display:grid;gap:4px}.dv-ob1 b{font:italic 900 17px/1.25 var(--f-titulo)}.dv-ob p{margin:0;font-size:14px;line-height:1.55;color:#CFCBC3}
@media(max-width:1100px){.dv-g2,.dv-cg,.dv-nicho{grid-template-columns:minmax(0,1fr)}.dv-cout,.dv-ni2{border-left:0;padding-left:0;border-top:1px solid var(--linha);padding-top:16px}}
@media(max-width:900px){.dv-stat,.dv-pp,.dv-tl li{grid-template-columns:minmax(0,1fr);gap:10px;padding:22px 0}.dv-usar{border-left:0;padding-left:0;border-top:1px solid var(--linha);padding-top:12px}
 .dv-ns{grid-template-columns:1fr 1fr}.dv-ns>div:first-child{grid-column:1/-1;border-bottom:1px solid var(--linha)}.dv-ns>div:nth-child(2){border-left:0}
 .dv-ob{grid-template-columns:minmax(0,1fr);gap:10px}.dv-f,.dv-f4{grid-template-columns:1fr 1fr!important}}
@media(max-width:700px){.dv-num{font-size:42px}.dv-big{font-size:38px}.dv-big.sm{font-size:24px}.dv-gh h3{font-size:21px}.dv-ns>div{padding:16px}
 .dv-fn{grid-template-columns:minmax(0,1fr) 40px 46px;gap:8px}.dv-fn .barra{grid-column:1/-1;order:3}.dv-taxas{grid-template-columns:1fr 1fr}
 .dv-nav,.dv-nichos,.dv-dur,.dv-seg2{justify-self:stretch;display:grid;overflow:visible}.dv-nav{grid-template-columns:1fr 1fr}.dv-nichos,.dv-seg2,.dv-dur{grid-template-columns:repeat(3,minmax(0,1fr))}.dv-nav button,.dv-nichos button,.dv-dur button,.dv-seg2 button{padding:8px 6px;text-align:center}.dv-cf{grid-template-columns:1fr!important}.dv-tot{grid-template-columns:1fr}.dv-vend{width:100%}.dv-vend input{flex:1}.dv-mesbar b{font-size:18px}}
@media (prefers-reduced-motion: reduce){.dv-fonte,.dv-cp{transition:none}}
</style>`);
if(location.hash==='#dados')setTimeout(rr,0);
})();
