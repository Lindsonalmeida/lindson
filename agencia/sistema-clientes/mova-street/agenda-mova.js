/* Aba Agendamentos do painel Mova Street (pedido do Lindson, 18/11/2026, conta Leandro).
   Visitas comerciais, reuniões, instalação de adesivo/tela e renovação. Dados reais em /api/agenda (KV dados:mova-street:agenda).
   WhatsApp: botões wa.me com mensagem pronta (PADRAO-COPY) que registram o envio sozinhos; lembrete automático em /api/agenda/lembretes (desligado até ter provedor). */
(function(){
const CLI='mova-street',API='/api/agenda?cli='+CLI,$=s=>document.querySelector(s);
const TIPO={visita:['Visita comercial','#FF5A1F'],reuniao:['Reunião','#FFC21A'],adesivo:['Instalação de adesivo','#5CC98A'],tela:['Instalação de tela','#6FA8FF'],renovacao:['Renovação','#C58CFF']};
const STAT={agendado:['Agendado','am'],confirmado:['Confirmado','ok'],realizado:['Realizado','ne'],faltou:['Não compareceu','er'],cancelado:['Cancelado','er']};
const ETAPA=['—','1 Novo lead','2 Contato feito','3 Diagnóstico','4 Mapa / demonstração','5 Proposta enviada','6 Negociação','7 Fechado','8 No ar','9 Renovação / indicação','Perdido'];
const NOMET={visita:'visita',reuniao:'reunião',adesivo:'instalação do adesivo',tela:'instalação da tela',renovacao:'conversa da renovação'};
const S={itens:{},equipe:[],auto:false,modo:'mes',ref:new Date(),dia:null,fTipo:'',fResp:'',off:false,ok:false};
const esc=t=>String(t??'').replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const iso=d=>new Date(d.getTime()-d.getTimezoneOffset()*6e4).toISOString().slice(0,10);
const br=s=>s?s.split('-').reverse().join('/'):'';
const DS=['dom','seg','ter','qua','qui','sex','sáb'],MS=['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro'];
const toast=t=>window.__toast?window.__toast(t):alert(t);
const LS='mova-agenda-local';
async function carregar(){
  try{const r=await fetch(API,{credentials:'same-origin'});if(!r.ok)throw 0;const j=await r.json();S.itens=j.itens||{};S.equipe=j.equipe||[];S.auto=!!j.auto;S.off=false}
  catch(e){S.off=true;try{const l=JSON.parse(localStorage.getItem(LS)||'{}');S.itens=l.itens||{};S.equipe=l.equipe||[]}catch(_){}}
  S.ok=true;desenha();
}
async function manda(corpo){
  if(S.off){ // sem servidor (prévia): guarda só neste aparelho
    const ag=new Date().toISOString();
    if(corpo.acao==='salvar'){const id=corpo.id||'ag'+Date.now().toString(36);const a=Object.assign(S.itens[id]||{envios:[],hist:[],status:'agendado'},corpo);delete a.acao;a.id=undefined;a.em=ag;S.itens[id]=a;corpo.id=id}
    else if(corpo.acao==='apagar')delete S.itens[corpo.id];
    else if(corpo.acao==='enviou'){const a=S.itens[corpo.id];if(a)a.envios=[...(a.envios||[]),{em:ag,msg:corpo.msg,via:'botão'}]}
    else if(corpo.acao==='equipe')S.equipe=corpo.equipe;
    try{localStorage.setItem(LS,JSON.stringify({itens:S.itens,equipe:S.equipe}))}catch(_){}
    return {ok:true,id:corpo.id};
  }
  const r=await fetch(API,{method:'POST',credentials:'same-origin',headers:{'Content-Type':'application/json'},body:JSON.stringify(Object.assign({cli:CLI},corpo))});
  const j=await r.json().catch(()=>({erro:'Falha na rede.'}));
  if(!r.ok||j.erro){toast(j.erro||'Não salvou.');return null}
  S.itens=j.itens||S.itens;if(j.equipe)S.equipe=j.equipe;return j;
}
const lista=()=>Object.entries(S.itens).map(([id,a])=>Object.assign({},a,{id})).filter(a=>(!S.fTipo||a.tipo===S.fTipo)&&(!S.fResp||a.resp===S.fResp)).sort((a,b)=>(a.data+a.hora).localeCompare(b.data+b.hora));
const doDia=d=>lista().filter(a=>a.data===d);
// mensagens (PADRAO-COPY: curtas, simples, sem promessa, sem preço)
function msg(a,qual){
  const n=(a.contato||'').split(' ')[0],oi=`Oi${n?', '+n:''}! Tudo bem?`,eu=`Aqui é ${a.resp?'o '+a.resp.split(' ')[0]:'a equipe'}, da Mova Street.`,q=`${NOMET[a.tipo]||'visita'}`,dh=`${DS[new Date(a.data+'T12:00').getDay()]}, ${br(a.data).slice(0,5)}, às ${a.hora}`,onde=a.endereco?` em ${a.endereco}`:'';
  return {
    confirmacao:`${oi} ${eu}\nFicou marcada a nossa ${q} pra ${dh}${onde}.\nPosso confirmar?`,
    d1:`${oi} ${eu}\nPassando pra lembrar da nossa ${q} amanhã, às ${a.hora}.\nContinua bom pra você?`,
    dia:`${oi} ${eu}\nHoje às ${a.hora} é a nossa ${q}. Já estou com tudo pronto.\nTe espero?`,
    remarcar:`${oi} ${eu}\nA nossa ${q} mudou pra ${dh}${onde}.\nEsse horário fica bom pra você?`,
    pos:a.tipo==='visita'||a.tipo==='reuniao'?`${oi} ${eu}\nObrigado pelo tempo hoje. Conseguiu olhar a proposta da ${a.empresa}?\nSe quiser, te mostro a tela funcionando num carro.`
       :a.tipo==='renovacao'?`${oi} ${eu}\nObrigado pela conversa. Quer que eu já deixe a renovação da ${a.empresa} reservada?`
       :`${oi} ${eu}\nA instalação da ${a.empresa} ficou pronta. Daqui a pouco te mando as fotos.\nQualquer coisa, é só me chamar.`,
    equipe:`Agenda Mova: ${TIPO[a.tipo][0]} com ${a.empresa}${a.contato?' ('+a.contato+')':''}\n${dh}${onde}${a.bairro?' · '+a.bairro:''}\n${a.wa?'Contato: +'+a.wa:''}${a.obs?'\nObs.: '+a.obs:''}`
  }[qual];
}
const ROT={confirmacao:'Confirmar',d1:'Lembrete D-1',dia:'Lembrete do dia',remarcar:'Remarcação',pos:'Pós-visita',equipe:'Avisar responsável'};
function waLink(a,qual){const num=qual==='equipe'?(a.respWa||(S.equipe.find(p=>p.nome===a.resp)||{}).wa):a.wa;return num?`https://wa.me/${num}?text=${encodeURIComponent(msg(a,qual))}`:''}
window.__agWa=async(id,qual)=>{const a=Object.assign({id},S.itens[id]);const l=waLink(a,qual);
  if(!l){try{await navigator.clipboard.writeText(msg(a,qual));toast('Sem WhatsApp cadastrado: mensagem copiada.')}catch(_){toast('Cadastre o WhatsApp.')}return}
  window.open(l,'_blank','noopener');await manda({acao:'enviou',id,msg:qual});desenha();};
const enviou=(a,q)=>(a.envios||[]).some(e=>e.msg===q||(q==='d1'&&e.msg==='lembD1')||(q==='dia'&&e.msg==='lembDia'));
function cartao(a){
  const t=TIPO[a.tipo]||TIPO.visita,s=STAT[a.status]||STAT.agendado,hj=iso(new Date());
  const sug=a.status==='realizado'?['pos','equipe']:a.data>hj?['confirmacao','d1','remarcar','equipe']:a.data===hj?['dia','confirmacao','remarcar','equipe','pos']:['pos','remarcar'];
  return `<div class="ag-it" style="border-left:3px solid ${t[1]}"><div class="ag-l1"><b class="ag-h">${a.hora}</b><span class="chip ${s[1]}">${s[0]}</span><span class="ag-tp" style="color:${t[1]}">${t[0]}</span></div>
  <div class="ag-emp">${esc(a.empresa)}</div><div class="ag-meta">${esc(a.contato||'')}${a.bairro?' · '+esc(a.bairro):''}${a.resp?' · resp.: '+esc(a.resp):''}${a.etapa?' · CRM: '+ETAPA[a.etapa]:''}</div>
  ${a.endereco?`<a class="ag-meta" target="_blank" rel="noopener" href="https://www.google.com/maps/search/?api=1&query=${encodeURIComponent(a.endereco+' '+(a.bairro||'')+' São Luís MA')}">${esc(a.endereco)}</a>`:''}
  ${a.obs?`<div class="ag-meta" style="color:var(--texto)">${esc(a.obs)}</div>`:''}${a.lead?`<a class="ag-meta" style="color:var(--amarelo);cursor:pointer" onclick="window.__crmMova&&__crmMova.abrir('${a.lead}')">Abrir ficha no CRM</a>`:''}
  <div class="ag-bts">${sug.map(q=>`<button class="btn ${q==='equipe'?'lin':'am'} ag-wa" onclick="__agWa('${a.id}','${q}')">${enviou(a,q)?'✓ ':''}${ROT[q]}</button>`).join('')}</div>
  <div class="ag-bts"><button class="btn lin" onclick="__agForm('${a.id}')">Editar / remarcar</button>${a.status!=='confirmado'&&a.status!=='realizado'?`<button class="btn lin" onclick="__agSt('${a.id}','confirmado')">Confirmado</button>`:''}${a.status!=='realizado'?`<button class="btn lin" onclick="__agSt('${a.id}','realizado')">Realizado</button>`:''}${a.status!=='cancelado'?`<button class="btn lin" onclick="__agSt('${a.id}','cancelado')">Cancelar</button>`:''}</div>
  ${(a.envios||[]).length?`<div class="ag-meta">WhatsApp: ${(a.envios||[]).slice(-3).map(e=>`${ROT[e.msg]||(e.msg==='lembD1'?'D-1 auto':e.msg==='lembDia'?'dia auto':e.msg)} ${new Date(e.em).toLocaleString('pt-BR',{day:'2-digit',month:'2-digit',hour:'2-digit',minute:'2-digit'})}`).join(' · ')}</div>`:''}</div>`;
}
window.__agSt=async(id,st)=>{if(st==='cancelado'&&!confirm('Cancelar este agendamento?'))return;const a=S.itens[id];if(await manda(Object.assign({},a,{acao:'salvar',id,status:st}))){desenha();if(st==='realizado')toast('Marcado como realizado. Mande o pós-visita.')}};
function calendario(){
  const r=S.ref,hj=iso(new Date());let dias=[];
  if(S.modo==='mes'){const p=new Date(r.getFullYear(),r.getMonth(),1),ini=new Date(p);ini.setDate(1-p.getDay());for(let i=0;i<42;i++){const d=new Date(ini);d.setDate(ini.getDate()+i);dias.push(d)}}
  else{const ini=new Date(r);ini.setDate(r.getDate()-r.getDay());for(let i=0;i<7;i++){const d=new Date(ini);d.setDate(ini.getDate()+i);dias.push(d)}}
  const tit=S.modo==='mes'?`${MS[r.getMonth()]} ${r.getFullYear()}`:`${br(iso(dias[0])).slice(0,5)} a ${br(iso(dias[6])).slice(0,5)}`;
  return `<div class="ag-cab"><button class="btn lin" onclick="__agNav(-1)" aria-label="Anterior">‹</button><b class="ag-tit">${tit}</b><button class="btn lin" onclick="__agNav(1)" aria-label="Próximo">›</button><button class="btn lin" onclick="__agNav(0)">Hoje</button>
  <span class="ag-seg"><button class="${S.modo==='mes'?'on':''}" onclick="__agModo('mes')">Mês</button><button class="${S.modo==='sem'?'on':''}" onclick="__agModo('sem')">Semana</button></span></div>
  <div class="ag-cal ${S.modo}">${DS.map(d=>`<div class="ag-ds">${d}</div>`).join('')}${dias.map(d=>{const k=iso(d),it=doDia(k).filter(a=>a.status!=='cancelado'),fora=S.modo==='mes'&&d.getMonth()!==r.getMonth();
    return `<button class="ag-d${k===hj?' hj':''}${k===S.dia?' sel':''}${fora?' fora':''}" onclick="__agDia('${k}')"><span class="ag-n">${d.getDate()}</span>${S.modo==='sem'?it.slice(0,4).map(a=>`<span class="ag-ev" style="border-color:${TIPO[a.tipo][1]}">${a.hora} ${esc(a.empresa)}</span>`).join('')+(it.length>4?`<span class="ag-mais">+${it.length-4}</span>`:''):`<span class="ag-pts">${it.slice(0,4).map(a=>`<i style="background:${TIPO[a.tipo][1]}"></i>`).join('')}</span>${it.length?`<span class="ag-q">${it.length}</span>`:''}`}</button>`}).join('')}</div>`;
}
window.__agNav=n=>{const r=S.ref;if(!n){S.ref=new Date();S.dia=iso(new Date())}else if(S.modo==='mes')S.ref=new Date(r.getFullYear(),r.getMonth()+n,1);else{S.ref=new Date(r);S.ref.setDate(r.getDate()+7*n)}desenha()};
window.__agModo=m=>{S.modo=m;desenha()};window.__agDia=k=>{S.dia=k;S.ref=new Date(k+'T12:00');desenha();const el=$('#ag-lista');if(el&&innerWidth<900)el.scrollIntoView({behavior:'smooth',block:'start'})};
window.__agFiltro=(k,v)=>{S[k]=v;desenha()};
function numeros(){
  const hj=iso(new Date()),d=new Date(),i=new Date(d);i.setDate(d.getDate()-d.getDay());const f=new Date(i);f.setDate(i.getDate()+6);const a=iso(i),b=iso(f);
  const v=Object.values(S.itens),ativ=v.filter(x=>x.status!=='cancelado');
  return [['Hoje',ativ.filter(x=>x.data===hj).length,'agendamentos do dia'],['Esta semana',ativ.filter(x=>x.data>=a&&x.data<=b).length,`${br(a).slice(0,5)} a ${br(b).slice(0,5)}`],['Confirmados',v.filter(x=>x.status==='confirmado'&&x.data>=hj).length,'a partir de hoje'],['Pendentes',v.filter(x=>x.status==='agendado'&&x.data>=hj).length,'falta confirmar']];
}
function view(){
  if(!S.ok){carregar();return '<div class="card"><p class="sub">Carregando a agenda…</p></div>'}
  const dia=S.dia||iso(new Date()),it=doDia(dia),prox=lista().filter(a=>a.data>dia&&['agendado','confirmado'].includes(a.status)).slice(0,6);
  const resps=[...new Set([...S.equipe.map(p=>p.nome),...Object.values(S.itens).map(a=>a.resp).filter(Boolean)])];
  return `${S.off?'<div class="card" style="border-color:var(--alerta)"><p class="sub" style="margin:0">Sem conexão com o servidor: o que salvar agora fica só neste aparelho.</p></div>':''}
  <div class="mv-kpis">${numeros().map(([r,v,s])=>`<div><span class="mv-k">${r}</span><b class="mv-big">${v}</b><span class="mv-l2">${s}</span></div>`).join('')}</div>
  <div class="ag-barra"><button class="btn am" onclick="__agForm()">+ Novo agendamento</button>
   <select onchange="__agFiltro('fTipo',this.value)" aria-label="Tipo"><option value="">Todos os tipos</option>${Object.entries(TIPO).map(([k,t])=>`<option value="${k}"${S.fTipo===k?' selected':''}>${t[0]}</option>`).join('')}</select>
   <select onchange="__agFiltro('fResp',this.value)" aria-label="Responsável"><option value="">Toda a equipe</option>${resps.map(r=>`<option${S.fResp===r?' selected':''}>${esc(r)}</option>`).join('')}</select>
   <button class="btn lin" onclick="__agEquipe()">Equipe e WhatsApp</button></div>
  <div class="grade g21 ag-g"><div class="card">${calendario()}<div class="ag-leg">${Object.values(TIPO).map(t=>`<span><i style="background:${t[1]}"></i>${t[0]}</span>`).join('')}</div></div>
   <div class="card" id="ag-lista"><h3>${dia===iso(new Date())?'Hoje · ':''}${DS[new Date(dia+'T12:00').getDay()]}, ${br(dia)}</h3><p class="sub">${it.length?it.length+' agendamento(s)':'Nada marcado neste dia.'}</p>${it.map(cartao).join('')}
   <button class="btn lin" style="width:100%;margin-top:6px" onclick="__agForm('',\'${dia}\')">+ Agendar neste dia</button>
   ${prox.length?`<h3 style="margin-top:20px">Próximos</h3>${prox.map(a=>`<button class="ag-px" onclick="__agDia('${a.data}')"><b>${br(a.data).slice(0,5)} ${a.hora}</b> ${esc(a.empresa)} <span class="chip ${STAT[a.status][1]}">${STAT[a.status][0]}</span></button>`).join('')}`:''}</div></div>
  <div class="card"><h3>Avisos no WhatsApp</h3><p class="sub" style="margin:0">${S.auto?'Lembretes automáticos ligados: D-1 às 18h e no dia, 2 h antes, para o contato e o responsável.':'Os botões abrem o WhatsApp com a mensagem pronta e registram o envio. Lembrete automático: fica pronto para ligar assim que a Mova contratar um número de envio (ex.: Z-API).'}</p></div>`;
}
function modal(html){let m=$('#ag-modal');if(!m){m=document.createElement('div');m.id='ag-modal';document.body.appendChild(m)}m.innerHTML=`<div class="ag-fundo" onclick="if(event.target===this)__agFecha()"><div class="ag-caixa card" role="dialog" aria-modal="true">${html}</div></div>`;const f=m.querySelector('input,select');f&&f.focus()}
window.__agFecha=()=>{const m=$('#ag-modal');if(m)m.innerHTML=''};
window.__agForm=(id,dia,pref)=>{
  const a=id?S.itens[id]:Object.assign({tipo:'visita',status:'agendado',data:dia||S.dia||iso(new Date()),hora:'09:00',dur:30,etapa:1},pref||{});if(a.wa)a.wa=String(a.wa);
  const o=(arr,v)=>arr.map(([k,t])=>`<option value="${k}"${String(v)===String(k)?' selected':''}>${t}</option>`).join('');
  const resps=S.equipe.map(p=>p.nome);
  modal(`<h3>${id?'Editar agendamento':'Novo agendamento'}</h3><form id="ag-f" class="ag-form">
  <div class="w2 ag-bts" style="margin:0"><button type="button" class="btn lin" onclick="__agPuxa(this.nextElementSibling)">Puxar do CRM</button><select hidden style="flex:1;background:var(--painel2);color:var(--texto);border:1px solid var(--linha);border-radius:9px;padding:8px"></select></div><label class="w2">Empresa *<input name="empresa" required maxlength="120" value="${esc(a.empresa)}"></label>
  <label>Contato<input name="contato" maxlength="80" value="${esc(a.contato)}"></label>
  <label>WhatsApp do contato<input name="wa" inputmode="tel" placeholder="(98) 9xxxx-xxxx" value="${esc(a.wa?a.wa.replace(/^55/,''):'')}"></label>
  <label>Tipo<select name="tipo">${o(Object.entries(TIPO).map(([k,t])=>[k,t[0]]),a.tipo)}</select></label>
  <label>Status<select name="status">${o(Object.entries(STAT).map(([k,t])=>[k,t[0]]),a.status)}</select></label>
  <label>Data *<input type="date" name="data" required value="${a.data||''}"></label>
  <label>Hora *<input type="time" name="hora" required value="${a.hora||''}"></label>
  <label>Duração (min)<input type="number" name="dur" min="10" max="480" step="5" value="${a.dur||30}"></label>
  <label>Etapa do CRM<select name="etapa">${o(ETAPA.map((t,i)=>[i,t]),a.etapa||0)}</select></label>
  <label class="w2">Endereço<input name="endereco" maxlength="160" value="${esc(a.endereco)}"></label>
  <label>Bairro<input name="bairro" maxlength="60" value="${esc(a.bairro)}"></label>
  <label>Responsável<input name="resp" list="ag-resps" maxlength="60" value="${esc(a.resp)}"><datalist id="ag-resps">${resps.map(r=>`<option value="${esc(r)}">`).join('')}</datalist></label>
  <input type="hidden" name="lead" value="${esc(a.lead||'')}"><label class="w2">Observação<textarea name="obs" rows="3" maxlength="1000">${esc(a.obs)}</textarea></label>
  <div class="w2 ag-bts">${id?`<button type="button" class="btn lin" onclick="__agApaga('${id}')">Excluir</button>`:''}<span style="flex:1"></span><button type="button" class="btn lin" onclick="__agFecha()">Fechar</button><button class="btn am">Salvar</button></div></form>`);
  $('#ag-f').onsubmit=async e=>{e.preventDefault();const d=Object.fromEntries(new FormData(e.target));const ant=id&&S.itens[id];
    const j=await manda(Object.assign(d,{acao:'salvar',id:id||''}));if(!j)return;__agFecha();S.dia=d.data;S.ref=new Date(d.data+'T12:00');desenha();
    const nid=j.id||id;if(!id)toast('Agendado. Mande a confirmação no WhatsApp.');else if(ant&&(ant.data!==d.data||ant.hora!==d.hora))toast('Remarcado. Avise o contato pelo botão Remarcação.');
    if(nid&&S.itens[nid])setTimeout(()=>{const b=document.querySelector(`[onclick="__agWa('${nid}','${!id?'confirmacao':'remarcar'}')"]`);b&&b.focus()},50)};
};
window.__agApaga=async id=>{if(!confirm('Excluir de vez? (Para manter o histórico, use Cancelar.)'))return;if(await manda({acao:'apagar',id})){__agFecha();desenha()}};
window.__agEquipe=()=>{const eq=S.equipe.length?S.equipe:[{nome:'',wa:''}];
  const linha=p=>`<div class="ag-eq"><input placeholder="Nome" value="${esc(p.nome)}" maxlength="60"><input placeholder="WhatsApp" inputmode="tel" value="${esc((p.wa||'').replace(/^55/,''))}"><button type="button" class="btn lin" onclick="this.parentNode.remove()" aria-label="Remover">✕</button></div>`;
  modal(`<h3>Equipe e WhatsApp</h3><p class="sub">Quem faz as visitas e instalações. O botão "Avisar responsável" manda a agenda para este número.</p><div id="ag-eqs">${eq.map(linha).join('')}</div>
  <div class="ag-bts"><button type="button" class="btn lin" id="ag-eqmais">+ Pessoa</button><span style="flex:1"></span><button class="btn lin" onclick="__agFecha()">Fechar</button><button class="btn am" id="ag-eqsalva">Salvar</button></div>`);
  $('#ag-eqmais').onclick=()=>$('#ag-eqs').insertAdjacentHTML('beforeend',linha({nome:'',wa:''}));
  $('#ag-eqsalva').onclick=async()=>{const e=[...document.querySelectorAll('.ag-eq')].map(d=>{const i=d.querySelectorAll('input');return{nome:i[0].value.trim(),wa:i[1].value}}).filter(p=>p.nome);if(await manda({acao:'equipe',equipe:e})){__agFecha();desenha();toast('Equipe salva.')}}};
function desenha(){if((location.hash||'').slice(1)==='agenda'&&window.__render)window.__render()}
const css=document.createElement('style');css.textContent=`
.ag-barra{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 12px}.ag-barra select{background:var(--painel);color:var(--texto);border:1px solid var(--linha);border-radius:9px;padding:9px 10px;font:500 13px var(--f-corpo)}
.ag-g{margin-bottom:16px;align-items:start}.ag-cab{display:flex;align-items:center;gap:8px;flex-wrap:wrap;margin-bottom:12px}.ag-cab .btn{flex:none;padding:8px 12px}.ag-tit{font:italic 900 20px/1.1 var(--f-titulo);text-transform:capitalize;min-width:150px;text-align:center}
.ag-seg{margin-left:auto;display:inline-flex;border:1px solid var(--linha);border-radius:99px;padding:3px}.ag-seg button{background:none;border:0;color:var(--apagado);font:600 12.5px var(--f-corpo);padding:6px 14px;border-radius:99px;cursor:pointer}.ag-seg .on{background:var(--amarelo);color:#0B0D12}
.ag-cal{display:grid;grid-template-columns:repeat(7,minmax(0,1fr));gap:4px}.ag-ds{font:500 10.5px var(--f-dado);letter-spacing:.12em;text-transform:uppercase;color:var(--apagado);text-align:center;padding:4px 0}
.ag-d{position:relative;background:var(--painel2);border:1px solid transparent;border-radius:8px;min-height:72px;padding:6px;text-align:left;color:var(--texto);cursor:pointer;display:flex;flex-direction:column;gap:3px;font:inherit;min-width:0}
.ag-d:hover{border-color:var(--linha)}.ag-d.fora{opacity:.35}.ag-d.hj .ag-n{background:var(--amarelo);color:#0B0D12;border-radius:99px;padding:0 6px}.ag-d.sel{border-color:var(--amarelo)}
.ag-n{font:600 12.5px var(--f-dado);align-self:flex-start}.ag-pts{display:flex;gap:3px;flex-wrap:wrap;margin-top:auto}.ag-pts i,.ag-leg i{width:7px;height:7px;border-radius:99px;display:inline-block}.ag-q{position:absolute;right:6px;top:6px;font:500 10.5px var(--f-dado);color:var(--apagado)}
.ag-cal.sem .ag-d{min-height:200px}.ag-ev{font-size:11px;line-height:1.25;border-left:2px solid;padding-left:5px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.ag-mais{font-size:11px;color:var(--apagado)}
.ag-leg{display:flex;flex-wrap:wrap;gap:12px;margin-top:12px;font-size:12px;color:var(--apagado)}.ag-leg span{display:inline-flex;align-items:center;gap:6px}
.ag-it{background:var(--painel2);border:1px solid var(--linha);border-radius:10px;padding:12px 12px 10px 14px;margin-bottom:10px}.ag-l1{display:flex;align-items:center;gap:8px;flex-wrap:wrap}.ag-h{font:600 15px var(--f-dado)}.ag-tp{font:600 11.5px var(--f-corpo);text-transform:uppercase;letter-spacing:.06em}
.ag-emp{font:italic 900 19px/1.15 var(--f-titulo);margin:6px 0 2px}.ag-meta{display:block;color:var(--apagado);font-size:12.5px;margin-top:3px;text-decoration:none;word-break:break-word}
.ag-bts{display:flex;flex-wrap:wrap;gap:6px;margin-top:8px}.ag-bts .btn{flex:none;padding:7px 10px;font-size:12px}.ag-wa.am{background:transparent!important;border:1px solid rgba(92,201,138,.45)!important;color:#8FE0B0!important}.ag-wa.am:hover{background:rgba(92,201,138,.1)!important}
.ag-px{display:flex;gap:8px;align-items:center;width:100%;background:none;border:0;border-bottom:1px solid var(--linha);color:var(--texto);padding:9px 0;font:inherit;font-size:13px;text-align:left;cursor:pointer}.ag-px .chip{margin-left:auto}
.ag-fundo{position:fixed;inset:0;background:rgba(5,6,9,.72);z-index:999;display:grid;place-items:center;padding:16px;overflow-y:auto}.ag-caixa{width:min(640px,100%);max-height:calc(100dvh - 32px);overflow-y:auto}
.ag-form{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:12px}.ag-form .w2{grid-column:1/-1}.ag-form label{display:grid;gap:5px;font-size:12px;color:var(--apagado)}
.ag-form input,.ag-form select,.ag-form textarea,.ag-eq input{background:var(--painel2);color:var(--texto);border:1px solid var(--linha);border-radius:9px;padding:10px;font:500 15px var(--f-corpo);width:100%;box-sizing:border-box;min-width:0}
.ag-form input:focus,.ag-form select:focus,.ag-form textarea:focus{outline:2px solid var(--amarelo);border-color:transparent}.ag-eq{display:grid;grid-template-columns:1fr 1fr auto;gap:8px;margin-bottom:8px}
@media(max-width:700px){.ag-d{min-height:46px;padding:4px;border-radius:8px}.ag-q{display:none}.ag-cal.sem{grid-template-columns:1fr}.ag-cal.sem .ag-ds{display:none}.ag-cal.sem .ag-d{min-height:0;flex-direction:row;flex-wrap:wrap;gap:6px 10px}.ag-cal.sem .ag-ev{white-space:normal}
.ag-seg{margin-left:0;width:100%;display:flex}.ag-seg button{flex:1}.ag-tit{min-width:0;flex:1;font-size:17px}.ag-form{grid-template-columns:1fr}.ag-barra>*{flex:1 1 45%}.ag-barra .btn.am{flex-basis:100%}}`;
document.head.appendChild(css);

// CRM → Agendamentos: puxa empresa, contato e WhatsApp de quem já está no CRM comercial (mesmo funil da estratégia v2)
window.__agCrm=async()=>{try{const r=await fetch('/api/dados?cli='+CLI+'&f=crm');const j=await r.json();return ((j.dados||{}).itens||[])}catch(e){return[]}};
window.__agPuxa=async sel=>{const l=await __agCrm();if(!l.length){toast('O CRM ainda está vazio.');return}
  sel.innerHTML='<option value="">Escolha a empresa do CRM</option>'+l.map((p,i)=>`<option value="${i}">${esc(p.empresa||p.nome)}${p.bairro?' · '+esc(p.bairro):''}</option>`).join('');sel.hidden=false;
  sel.onchange=()=>{const p=l[+sel.value];if(!p)return;const f=$('#ag-f');f.empresa.value=p.empresa||p.nome||'';f.wa.value=String(p.whats||'').replace(/\D/g,'').replace(/^55/,'');f.etapa.value=p.etapa==='perdido'?10:(parseInt(String(p.etapa||'').slice(1))||0);f.lead.value=p.id||'';f.contato.value=p.contato||'';f.bairro.value=p.bairro||'';f.resp.value=p.resp||f.resp.value;if(false)f.obs.value=p.notas}};
// Treinamento (guia escrito; vídeo "em breve" até gravar)
const TR=(window.__DADOS||{}).treinamento||[];
window.__V.treinamento=()=>`<div class="card"><h3>Treinamento da equipe</h3><p class="sub">Passo a passo para usar a Central no dia a dia. Os vídeos entram aqui quando forem gravados.</p></div><div class="grade g2">${TR.map((t,i)=>`<div class="card"><div style="font:500 11px var(--f-dado);letter-spacing:.14em;color:var(--amarelo)">0${i+1} · ${esc(t.para)}</div><h3 style="font:italic 900 20px var(--f-titulo);margin:8px 0">${esc(t.titulo)}</h3>${t.video?`<a class="btn lin" target="_blank" rel="noopener" href="${esc(t.video)}">Assistir</a>`:'<span class="chip ne">Vídeo em breve</span>'}<ol style="margin:12px 0 0;padding-left:20px;line-height:1.6;font-size:14px">${t.passos.map(x=>`<li>${esc(x)}</li>`).join('')}</ol></div>`).join('')}</div>`;
window.__T.treinamento='Treinamento';
// Financeiro: telas vendidas e livres (das 10) antes do caixa; vazio até haver contrato
const fin0=null;if(fin0){const TL=(window.__DADOS||{}).telas||{total:10};window.__V.financeiro=()=>{const v=TL.vendidas;return `<div class="grade g4"><div class="card kpi"><div class="rot">Telas TV Cars</div><div class="val">${TL.total}</div><div class="var"><span>total da 1ª rodada</span></div></div><div class="card kpi"><div class="rot">Vendidas</div><div class="val">${v==null?'—':v}</div><div class="var"><span>${v==null?'sem contrato lançado':'contratos fechados'}</span></div></div><div class="card kpi"><div class="rot">Livres</div><div class="val">${v==null?'—':TL.total-v}</div><div class="var"><span>para vender</span></div></div><div class="card kpi"><div class="rot">Receita por contrato</div><div class="val" style="font-size:22px">no caixa abaixo</div><div class="var"><span>lance cada contrato como entrada</span></div></div></div><div style="height:16px"></div>`+fin0()}}
window.__agS=()=>S;if(!S.ok)fetch(API,{credentials:'same-origin'}).then(r=>r.ok&&r.json()).then(j=>{if(j&&!S.ok){S.itens=j.itens||{};S.equipe=j.equipe||[];S.auto=!!j.auto}}).catch(()=>{});
window.__V.agenda=view;window.__T.agenda='Agendamentos';
})();
