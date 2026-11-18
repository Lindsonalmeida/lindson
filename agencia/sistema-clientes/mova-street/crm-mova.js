/* CRM comercial da Mova Street (pedido do Lindson, 18/11/2026, conta Leandro): "o mais completo de todos".
   Base: estratégia v2 §7 (9 etapas + perdido, scripts PADRAO-COPY, follow-up D1/D3/D7/D15/D30, objeções), regra dos apps de SDR
   (botão WhatsApp com a mensagem da etapa que registra o envio e avança a cadência), ferramentas.js (persistência /api/dados versionada).
   Dados: /api/dados?cli=mova-street&f=crm → {itens:[lead], tarefas:[], telas:[10], exclus:{ramo:leadId}}. Agendamentos ligados pelo campo lead. */
(function(){
const CLI='mova-street',U='/api/dados?cli='+CLI+'&f=crm',$=s=>document.querySelector(s),$$=s=>[...document.querySelectorAll(s)];
const toast=t=>window.__toast?window.__toast(t):alert(t),rr=()=>window.__render&&window.__render();
const esc=t=>String(t??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const hoje=()=>{const d=new Date();d.setMinutes(d.getMinutes()-d.getTimezoneOffset());return d.toISOString().slice(0,10)};
const mais=(n,b=hoje())=>{const d=new Date(b+'T12:00');d.setDate(d.getDate()+n);return d.toISOString().slice(0,10)};
const br=s=>s?s.slice(0,10).split('-').reverse().join('/'):'';const uid=()=>Date.now().toString(36)+Math.random().toString(36).slice(2,6);
const brl=n=>(+n||0).toLocaleString('pt-BR',{style:'currency',currency:'BRL',maximumFractionDigits:0});
const fone=s=>{const d=String(s||'').replace(/\D/g,'');return d.length>=10&&d.length<=13?(d.startsWith('55')&&d.length>=12?d:'55'+d):''};
const ET=[['e1','Novo lead','Responder em até 5 min'],['e2','Contato feito','Diagnóstico na mesma conversa'],['e3','Diagnóstico','Montar o mapa em até 24 h'],['e4','Mapa / demonstração','Mandar a proposta no mesmo dia'],['e5','Proposta enviada','Follow-up D1, D3, D7'],['e6','Negociação','Resolver a objeção e pedir o sim'],['e7','Fechado','Pedir logo/vídeo e o WhatsApp do QR'],['e8','No ar','Foto/vídeo do anúncio no 1º dia'],['e9','Renovação / indicação','Renovação 7 dias antes do fim'],['perdido','Perdido','Voltar a falar em 30 dias']];
const EN=Object.fromEntries(ET.map((e,i)=>[e[0],i])),nomeE=id=>(ET[EN[id]]||ET[0])[1];
const ORIG=['Visita na rua','Anúncio (Meta)','Instagram','Site','WhatsApp direto','Indicação','Cliente antigo','Outro'];
const PLANOS=[['','—',0],['largada','Largada · 5 telas · 10 s',800],['presenca','Presença · 5 telas · 15 s',900],['destaque','Destaque · 5 telas · 20 s',1000],['cidade10','Cidade 10 · 10 telas · 10 s',1600],['cidade15','Cidade 15 · 10 telas · 15 s',1800],['cidade20','Cidade 20 · 10 telas · 20 s',2000],['adesivo','Adesivo no vidro traseiro',0],['combo','Combo rua + dentro',0]];
const PL=Object.fromEntries(PLANOS.map(p=>[p[0],p]));
const MOTIVOS=['Preço','Momento','Não decide sozinho','Sem retorno','Já tem outra mídia','Outro'];
const RAMOS=['Alimentação','Saúde e estética','Moda e varejo','Automotivo','Imobiliário','Educação','Serviços','Academia e esporte','Outro'];
// scripts (estratégia v2 §7, PADRAO-COPY: curtos, sem promessa, preço "a partir de")
const pn=l=>(l.contato||'').split(' ')[0]||l.empresa;
const MSG={
 e1:l=>`Oi, ${pn(l)}! Tudo bem? Aqui é ${l.resp?'o '+l.resp.split(' ')[0]:'o Paulo'}, da Mova Street, de São Luís.\nMuita gente passa perto da ${l.empresa} e nem sabe que ela existe.\nA gente coloca sua marca na tela e no vidro dos carros de aplicativo.\nPosso te mostrar como fica?`,
 e2:l=>`Oi, ${pn(l)}! Pra eu montar o mapa certinho: em quais bairros estão os clientes da ${l.empresa} e o que você quer divulgar primeiro?`,
 e3:l=>`Oi, ${pn(l)}! Já montei o mapa de onde a ${l.empresa} aparece. Posso passar aí pra te mostrar a tela funcionando num carro?`,
 e4:l=>`Oi, ${pn(l)}! Segue a proposta da ${l.empresa}, de 1 página: ${propLink(l)}\nQualquer dúvida, me chama aqui.`,
 e5:l=>`Oi, ${pn(l)}! Conseguiu olhar a proposta? Se quiser, te mostro a tela funcionando num carro. Pode ser hoje?`,
 e6:l=>`Entendi, ${pn(l)}. Pra começar com segurança, dá pra entrar no plano Largada: 5 telas, anúncio de 10 s, a partir de R$ 800. Depois, com o relatório na mão, você decide se aumenta. Fechamos assim?`,
 e7:l=>`Oi, ${pn(l)}! Bem-vindo à Mova! Me manda a logo (ou o vídeo) da ${l.empresa} e o WhatsApp que vai no QR Code?`,
 e8:l=>`Oi, ${pn(l)}! O anúncio da ${l.empresa} já está rodando. Te mando as fotos dele no carro.`,
 e9:l=>`Oi, ${pn(l)}! O período da ${l.empresa} está chegando ao fim. Quer que eu já deixe a renovação reservada?`,
 perdido:l=>`Oi, ${pn(l)}! Tudo bem por aí? Temos novidade na frota. Posso te mandar como ficou?`,
 D1:l=>MSG.e5(l),
 D3:l=>`${pn(l)}, passando pra avisar: das 10 telas, ${livres()} ainda estão livres. Quer que eu segure a sua até sexta?`,
 D7:l=>`Oi, ${pn(l)}! Vou fechar a lista da primeira rodada. Deixo a ${l.empresa} na lista de espera ou fechamos agora?`,
 D15:l=>`Oi, ${pn(l)}! Abriu espaço pra uma nova rodada. Quer que eu atualize a proposta da ${l.empresa}?`,
 D30:l=>MSG.perdido(l),
 REN:l=>MSG.e9(l), IND:l=>`Oi, ${pn(l)}! Obrigado pela parceria. Se conhecer alguém que queira aparecer nas telas também, me indica?`
};
const OBJ=[['Tá caro','Entendo. Pra começar, o plano Largada sai a partir de R$ 800 por 5 telas, com QR Code e relatório. Você testa e decide com dado na mão. Quer começar por ele?'],['Já faço Instagram','Ótimo, continua! O Instagram fala com quem já te segue. A tela fala com quem tá na rua e ainda não te conhece, e o QR leva pro seu WhatsApp.'],['Como sei que funciona?','O sistema mostra cliques no QR, tempo de tela ligada e mapa de calor das rotas. No vidro, você recebe fotos e km rodados.'],['Quantas pessoas vão ver?','A estimativa da empresa é de cerca de 5 mil visualizações com 5 telas e 10 mil com 10 telas. E o QR mostra quantos chamaram de verdade.'],['Vou pensar','Claro. Te deixo a proposta de 1 página. Posso te chamar amanhã pra tirar alguma dúvida? E se quiser, seguro a tela até sexta.'],['Não tenho arte','Sem problema: a gente prepara a arte a partir do seu logo e das suas fotos.'],['Agora não','Entendo. Dezembro e janeiro são meses de muita gente circulando. Quer que eu deixe a sua empresa na lista da próxima rodada?'],['Concorrente junto?','Só se você não tiver exclusividade. Com +50% e contrato de 6 meses, o seu ramo fica só seu nas telas.']];
// cadência criada ao entrar na etapa
const CAD={e1:[['Responder','e1',0]],e3:[['Mandar o mapa','e3',1]],e4:[['Mandar a proposta','e4',0]],e5:[['Follow-up D1','D1',1],['Follow-up D3','D3',3],['Follow-up D7','D7',7],['Follow-up D15','D15',15]],e7:[['Pedir logo e WhatsApp do QR','e7',0]],e8:[['Mandar foto do anúncio no ar','e8',0]],e9:[['Pedir indicação','IND',2]],perdido:[['Voltar a falar (D30)','D30',30]]};
const S={d:null,v:0,carregou:false,off:false,aba:'funil',busca:'',fE:'',fO:'',fR:'',lead:null,drag:null};
const D=()=>S.d;
function base(){return{itens:[],tarefas:[],telas:Array.from({length:10},(_,i)=>({n:i+1,st:'livre',lead:'',ate:''})),exclus:{}}}
function normal(x){const b=base();x=x&&typeof x==='object'?x:{};x.itens=Array.isArray(x.itens)?x.itens:[];x.tarefas=Array.isArray(x.tarefas)?x.tarefas:[];x.telas=Array.isArray(x.telas)&&x.telas.length?x.telas:b.telas;x.exclus=x.exclus||{};x.itens.forEach(l=>{if(!EN.hasOwnProperty(l.etapa))l.etapa='e1';l.hist=l.hist||[];l.empresa=l.empresa||l.nome||'';l.nome=l.empresa;l.whats=l.whats||l.wa||''});return x}
const LS='mova-crm-local';
async function carregar(){try{const r=await fetch(U,{headers:{Accept:'application/json'}});if(!r.ok)throw 0;const j=await r.json();S.d=normal(j.dados);S.v=j.versao||0;S.off=false}catch(e){S.off=true;try{const l=JSON.parse(localStorage.getItem(LS)||'null');S.d=normal(l)}catch(_){S.d=normal(null)}}S.carregou=true;rr()}
window.__crmMova={carregar,get:()=>S.d,abrir:id=>{location.hash='crm';S.lead=id;setTimeout(rr,0)}};
let fila=Promise.resolve();
function mut(fn,msg){fn(S.d);rr();fila=fila.then(async()=>{
  if(S.off){try{localStorage.setItem(LS,JSON.stringify(S.d))}catch(_){}msg&&toast(msg);return}
  for(let t=0;t<3;t++){const r=await fetch(U,{method:'PUT',headers:{'Content-Type':'application/json'},body:JSON.stringify({dados:S.d,versao:S.v})});
    if(r.ok){S.v=(await r.json()).versao;msg&&toast(msg);return}
    if(r.status===409){const j=await r.json();S.d=normal(j.dados);S.v=j.versao;fn(S.d);continue}
    toast('Não salvou. Confira a internet.');return}
  rr()})}
const L=id=>S.d.itens.find(l=>l.id===id);
const livres=()=>S.d.telas.filter(t=>t.st==='livre').length;
const propLink=l=>`${location.origin}/painel/mova-street/proposta.html?empresa=${encodeURIComponent(l.empresa||'')}`;
const waUrl=(l,k)=>{const f=fone(l.whats);return f?`https://wa.me/${f}?text=${encodeURIComponent(MSG[k](l))}`:''};
function hist(l,txt,tipo='nota'){l.hist.push({em:new Date().toISOString(),txt,tipo});if(l.hist.length>200)l.hist.shift()}
function moveEtapa(d,l,nova,motivo){const antes=l.etapa;if(antes===nova)return;l.etapa=nova;l.em=new Date().toISOString();l.max=Math.max(l.max||0,EN[nova]===9?0:EN[nova]);
  hist(l,`Etapa: ${nomeE(antes)} → ${nomeE(nova)}${motivo?' · motivo: '+motivo:''}`,'etapa');
  d.tarefas.forEach(t=>{if(t.lead===l.id&&!t.feito&&t.etapa!==nova){t.feito=true;t.auto='etapa mudou'}});
  (CAD[nova]||[]).forEach(([tit,k,n])=>d.tarefas.push({id:uid(),lead:l.id,tit,k,quando:mais(n),etapa:nova,feito:false}));
  if(nova==='perdido'){l.motivo=motivo||l.motivo||'';d.telas.forEach(t=>{if(t.lead===l.id&&t.st==='reservada'){t.st='livre';t.lead=''}})}
}
window.__crmWa=(id,k,tarefa)=>{const l=L(id);if(!l)return;const u=waUrl(l,k);
  if(!u){navigator.clipboard&&navigator.clipboard.writeText(MSG[k](l)).catch(()=>{});toast('Sem WhatsApp no cadastro: mensagem copiada.');return}
  window.open(u,'_blank','noopener');
  mut(d=>{const x=d.itens.find(q=>q.id===id);if(!x)return;x.toques=(x.toques||0)+1;x.ult=new Date().toISOString();hist(x,`WhatsApp enviado: ${tarefa?d.tarefas.find(t=>t.id===tarefa)?.tit||k:nomeE(k)||k}`,'wa');
    const t=tarefa?d.tarefas.find(t=>t.id===tarefa):d.tarefas.filter(t=>t.lead===id&&!t.feito).sort((a,b)=>a.quando.localeCompare(b.quando))[0];if(t){t.feito=true;t.em=new Date().toISOString()}
    if(!tarefa){const i=EN[x.etapa];if(['e1','e3','e4'].includes(x.etapa)&&i<8)moveEtapa(d,x,ET[i+1][0])}},'Envio registrado.')};
// ---------- telas ----------
const chipE=id=>`<span class="mv-et" data-e="${id}">${esc(nomeE(id))}</span>`;
function kanban(lista){return `<div class="mv-kb">${ET.map(([id,n,acao])=>{const g=lista.filter(l=>l.etapa===id),v=g.reduce((a,l)=>a+(+l.valor||0),0);
  return `<section class="mv-col" data-col="${id}" ondragover="event.preventDefault();this.classList.add('on')" ondragleave="this.classList.remove('on')" ondrop="__crmDrop(event,'${id}')"><header><span class="mv-n">${String(EN[id]+1).padStart(2,'0')}</span><b>${n}</b><span class="mv-c">${g.length}</span></header><p class="mv-acao">${acao}${v?' · '+brl(v):''}</p>
  ${g.map(cartaoLead).join('')||'<div class="mv-vz">vazio</div>'}</section>`}).join('')}</div>`}
function cartaoLead(l){const pend=S.d.tarefas.filter(t=>t.lead===l.id&&!t.feito).sort((a,b)=>a.quando.localeCompare(b.quando))[0],atras=pend&&pend.quando<hoje();
  return `<article class="mv-lead" draggable="true" ondragstart="__crmDrag('${l.id}')" onclick="__crmAbre('${l.id}')"><div class="mv-l1"><b>${esc(l.empresa)}</b>${l.exclusivo?'<span class="mv-tag">EXCL.</span>':''}</div>
  <div class="mv-l2">${esc([l.ramo,l.bairro].filter(Boolean).join(' · '))}</div><div class="mv-l3"><span>${esc(l.resp||'sem resp.')}</span>${l.valor?`<span class="mv-mono">${brl(l.valor)}</span>`:''}</div>
  ${pend?`<div class="mv-prox${atras?' atr':''}">${atras?'atrasado · ':''}${esc(pend.tit)} · ${br(pend.quando).slice(0,5)}</div>`:''}
  <div class="mv-l4"><button class="mv-b wa" onclick="event.stopPropagation();__crmWa('${l.id}','${l.etapa}')">WhatsApp</button><select class="mv-sel" onclick="event.stopPropagation()" onchange="__crmMove('${l.id}',this.value)" aria-label="Mover etapa">${ET.map(e=>`<option value="${e[0]}"${e[0]===l.etapa?' selected':''}>${e[1]}</option>`).join('')}</select></div></article>`}
window.__crmDrag=id=>S.drag=id;
window.__crmDrop=(ev,col)=>{ev.preventDefault();const id=S.drag;S.drag=null;if(id)__crmMove(id,col)};
window.__crmMove=(id,nova)=>{let motivo='';if(nova==='perdido'){motivo=prompt('Motivo da perda: '+MOTIVOS.join(', '),'Sem retorno');if(motivo===null){rr();return}}
  mut(d=>{const l=d.itens.find(x=>x.id===id);l&&moveEtapa(d,l,nova,motivo)},'Etapa: '+nomeE(nova))};
function filtrada(){const b=S.busca.toLowerCase();return S.d.itens.filter(l=>(!S.fE||l.etapa===S.fE)&&(!S.fO||l.origem===S.fO)&&(!S.fR||l.resp===S.fR)&&(!b||[l.empresa,l.contato,l.whats,l.bairro,l.ramo,l.ig,l.notas].join(' ').toLowerCase().includes(b)))}
function listaV(lista){return `<div class="mv-tab"><table><thead><tr><th>Empresa</th><th>Etapa</th><th>Ramo · bairro</th><th>Origem</th><th>Responsável</th><th>Plano</th><th>Próximo passo</th><th></th></tr></thead><tbody>${lista.slice().sort((a,b)=>(b.em||'').localeCompare(a.em||'')).map(l=>`<tr onclick="__crmAbre('${l.id}')"><td><b>${esc(l.empresa)}</b><div class="mv-l2">${esc(l.contato||'')}</div></td><td>${chipE(l.etapa)}</td><td>${esc([l.ramo,l.bairro].filter(Boolean).join(' · '))}</td><td>${esc(l.origem||'')}</td><td>${esc(l.resp||'')}</td><td>${l.plano?esc(PL[l.plano][1].split(' ·')[0]):''}</td><td class="mv-mono">${l.proxData?br(l.proxData).slice(0,5)+' ':''}${esc(l.prox||'')}</td><td><button class="mv-b wa" onclick="event.stopPropagation();__crmWa('${l.id}','${l.etapa}')">WhatsApp</button></td></tr>`).join('')||'<tr><td colspan="8" class="mv-vz">Nenhuma empresa ainda. Toque em + Nova empresa ou importe um CSV.</td></tr>'}</tbody></table></div>`}
function tarefasV(){const t=S.d.tarefas.filter(t=>!t.feito&&L(t.lead)).sort((a,b)=>a.quando.localeCompare(b.quando)),h=hoje();
  const grp=[['Atrasadas',t.filter(x=>x.quando<h)],['Hoje',t.filter(x=>x.quando===h)],['Próximos 7 dias',t.filter(x=>x.quando>h&&x.quando<=mais(7))],['Depois',t.filter(x=>x.quando>mais(7))]];
  return grp.map(([n,g])=>`<div class="mv-blk"><h4 class="mv-h4">${n} <span>${g.length}</span></h4>${g.map(x=>{const l=L(x.lead);return `<div class="mv-row"><span class="mv-mono mv-dt">${br(x.quando).slice(0,5)}</span><div class="mv-grow"><b>${esc(x.tit)}</b> · <a onclick="__crmAbre('${l.id}')">${esc(l.empresa)}</a><div class="mv-l2">${esc(nomeE(l.etapa))} · ${esc(l.resp||'')}</div></div><button class="mv-b wa" onclick="__crmWa('${l.id}','${x.k}','${x.id}')">WhatsApp</button><button class="mv-b" onclick="__crmFeito('${x.id}')">Feito</button></div>`}).join('')||'<div class="mv-vz">nada</div>'}</div>`).join('')}
window.__crmFeito=id=>mut(d=>{const t=d.tarefas.find(x=>x.id===id);if(t){t.feito=true;t.em=new Date().toISOString();const l=d.itens.find(x=>x.id===t.lead);l&&hist(l,'Tarefa feita: '+t.tit,'tarefa')}},'Tarefa feita.');
function telasV(){const ex=Object.entries(S.d.exclus).filter(([,id])=>L(id));
  return `<div class="mv-telas">${S.d.telas.map(t=>{const l=L(t.lead);return `<button class="mv-tela" data-st="${t.st}" onclick="__crmTela(${t.n})"><span class="mv-mono">TELA ${String(t.n).padStart(2,'0')}</span><b>${t.st==='livre'?'Livre':t.st==='reservada'?'Reservada':'Ocupada'}</b><span class="mv-l2">${l?esc(l.empresa):'—'}${t.ate?' · até '+br(t.ate).slice(0,5):''}</span></button>`}).join('')}</div>
  <div class="mv-blk"><h4 class="mv-h4">Exclusividade por ramo <span>${ex.length}</span></h4>${ex.map(([r,id])=>`<div class="mv-row"><b class="mv-grow">${esc(r)}</b><a onclick="__crmAbre('${id}')">${esc(L(id).empresa)}</a></div>`).join('')||'<div class="mv-vz">Nenhum ramo exclusivo. Marque "Exclusividade" na ficha de um contrato fechado.</div>'}</div>`}
window.__crmTela=n=>{const t=S.d.telas[n-1],ops=S.d.itens.filter(l=>!['perdido'].includes(l.etapa));
  modal(`<h3 class="mv-mt">Tela ${String(n).padStart(2,'0')}</h3><form id="mv-tf" class="mv-form"><label>Situação<select name="st">${['livre','reservada','ocupada'].map(s=>`<option${t.st===s?' selected':''}>${s}</option>`).join('')}</select></label>
  <label>Anunciante<select name="lead"><option value="">—</option>${ops.map(l=>`<option value="${l.id}"${l.id===t.lead?' selected':''}>${esc(l.empresa)}</option>`).join('')}</select></label><label>Até<input type="date" name="ate" value="${t.ate||''}"></label>
  <div class="mv-acoes w2"><span class="mv-grow"></span><button type="button" class="mv-b" onclick="__crmFecha()">Fechar</button><button class="mv-b pri">Salvar</button></div></form>`);
  $('#mv-tf').onsubmit=e=>{e.preventDefault();const f=Object.fromEntries(new FormData(e.target));if(f.st==='livre')f.lead='';
    const l=L(f.lead);if(l&&l.ramo&&S.d.exclus[l.ramo]&&S.d.exclus[l.ramo]!==l.id&&!confirm(`O ramo ${l.ramo} é exclusivo de ${L(S.d.exclus[l.ramo])?.empresa}. Continuar?`))return;
    mut(d=>{Object.assign(d.telas[n-1],f);if(l){const x=d.itens.find(q=>q.id===l.id);hist(x,`Tela ${n}: ${f.st}`,'tela')}},'Tela atualizada.');__crmFecha()}};
function metricasV(){const it=S.d.itens,oc=S.d.telas.filter(t=>t.st==='ocupada').length,res=S.d.telas.filter(t=>t.st==='reservada').length;
  const chegou=i=>it.filter(l=>(l.max||EN[l.etapa])>=i&&l.etapa!=='perdido'||((l.max||0)>=i)).length;
  const funil=ET.slice(0,9).map(([id,n],i)=>[n,chegou(i)]);const top=Math.max(1,funil[0][1]);
  const contratos=it.filter(l=>['e7','e8','e9'].includes(l.etapa)),rec=contratos.reduce((a,l)=>a+(+l.valor||0),0);
  const por=(k,lst)=>lst.map(o=>{const g=it.filter(l=>(l[k]||'')===o);return g.length?[o,g.length,g.filter(l=>['e7','e8','e9'].includes(l.etapa)).length]:null}).filter(Boolean);
  const resps=[...new Set(it.map(l=>l.resp).filter(Boolean))];
  const tab=(t,rows)=>`<div class="mv-blk"><h4 class="mv-h4">${t}</h4>${rows.length?rows.map(([n,a,b])=>`<div class="mv-row"><span class="mv-grow">${esc(n)}</span><span class="mv-mono">${a} leads · ${b} fechados · ${a?Math.round(b/a*100):0}%</span></div>`).join(''):'<div class="mv-vz">sem dados ainda</div>'}</div>`;
  return `<div class="mv-ns"><div><span class="mv-k">North star · telas ocupadas pagas</span><div class="mv-big">${oc}<small>/10</small></div><div class="mv-bar"><i style="width:${oc*10}%"></i><i class="r" style="width:${res*10}%"></i></div><span class="mv-l2">${res} reservada(s) · ${10-oc-res} livre(s)</span></div>
  <div><span class="mv-k">Contratos ativos</span><div class="mv-big">${contratos.length}</div><span class="mv-l2">valor lançado: ${rec?brl(rec):'—'}</span></div><div><span class="mv-k">Perdidos</span><div class="mv-big">${it.filter(l=>l.etapa==='perdido').length}</div><span class="mv-l2">${esc(Object.entries(it.filter(l=>l.etapa==='perdido').reduce((a,l)=>(a[l.motivo||'sem motivo']=(a[l.motivo||'sem motivo']||0)+1,a),{})).map(x=>x.join(': ')).join(' · ')||'—')}</span></div></div>
  <div class="mv-blk"><h4 class="mv-h4">Conversão por etapa</h4>${funil.map(([n,v],i)=>`<div class="mv-fn"><span>${String(i+1).padStart(2,'0')} ${n}</span><div class="mv-bar"><i style="width:${v/top*100}%"></i></div><span class="mv-mono">${v}${i?` · ${funil[i-1][1]?Math.round(v/funil[i-1][1]*100):0}%`:''}</span></div>`).join('')}</div>
  <div class="mv-g2">${tab('Por origem',por('origem',ORIG))}${tab('Por responsável',por('resp',resps))}</div>`}
// ---------- ficha ----------
function modal(h,larga){let m=$('#mv-modal');if(!m){m=document.createElement('div');m.id='mv-modal';document.body.appendChild(m)}m.innerHTML=`<div class="mv-fundo" onclick="if(event.target===this)__crmFecha()"><div class="mv-caixa${larga?' lg':''}" role="dialog" aria-modal="true">${h}</div></div>`}
window.__crmFecha=()=>{const m=$('#mv-modal');if(m)m.innerHTML='';S.lead=null};
window.__crmAbre=id=>{S.lead=id;ficha()};
function ficha(){const id=S.lead,l=id?L(id):{etapa:'e1',origem:'Visita na rua',hist:[]};if(id&&!l)return;
  const o=(arr,v)=>arr.map(x=>Array.isArray(x)?`<option value="${x[0]}"${x[0]===v?' selected':''}>${x[1]}</option>`:`<option${x===v?' selected':''}>${esc(x)}</option>`).join('');
  const ags=window.__agS?Object.entries(window.__agS().itens).filter(([,a])=>a.lead===id).sort((a,b)=>(b[1].data+b[1].hora).localeCompare(a[1].data+a[1].hora)):[];
  const tar=id?S.d.tarefas.filter(t=>t.lead===id).sort((a,b)=>a.quando.localeCompare(b.quando)):[];const tel=id?S.d.telas.filter(t=>t.lead===id):[];
  modal(`<div class="mv-fh"><div><span class="mv-k">${id?nomeE(l.etapa):'Nova empresa'}</span><h3 class="mv-mt">${esc(l.empresa||'Cadastrar empresa')}</h3></div><button class="mv-b" onclick="__crmFecha()" aria-label="Fechar">Fechar</button></div>
  ${id?`<div class="mv-acoes"><button class="mv-b wa" onclick="__crmWa('${id}','${l.etapa}')">WhatsApp da etapa</button><button class="mv-b" onclick="__crmAg('${id}')">Agendar visita</button><a class="mv-b" target="_blank" rel="noopener" href="${propLink(l)}">Abrir proposta</a><button class="mv-b" onclick="navigator.clipboard.writeText('${propLink(l)}').then(()=>__toast('Link da proposta copiado.'))">Copiar link</button>${l.ig?`<a class="mv-b" target="_blank" rel="noopener" href="https://instagram.com/${esc(l.ig.replace(/^@/,''))}">Instagram</a>`:''}</div>
  <div class="mv-steps">${ET.slice(0,9).map(e=>`<button class="${EN[e[0]]<=EN[l.etapa]&&l.etapa!=='perdido'?'ok':''}${e[0]===l.etapa?' at':''}" onclick="__crmMove('${id}','${e[0]}');setTimeout(()=>__crmAbre('${id}'),30)" title="${e[1]}">${EN[e[0]]+1}</button>`).join('')}<button class="${l.etapa==='perdido'?'at pd':''}" onclick="__crmMove('${id}','perdido');setTimeout(()=>__crmAbre('${id}'),30)">Perdido</button></div>`:''}
  <div class="mv-fg"><form id="mv-lf" class="mv-form">
   <label class="w2">Empresa *<input name="empresa" required maxlength="120" value="${esc(l.empresa)}"></label>
   <label>Ramo<select name="ramo"><option value="">—</option>${o(RAMOS,l.ramo)}</select></label><label>Bairro<input name="bairro" maxlength="60" value="${esc(l.bairro)}"></label>
   <label>Contato (decisor)<input name="contato" maxlength="80" value="${esc(l.contato)}"></label><label>WhatsApp<input name="whats" inputmode="tel" value="${esc(String(l.whats||'').replace(/^55/,''))}"></label>
   <label>Instagram<input name="ig" maxlength="60" placeholder="@empresa" value="${esc(l.ig)}"></label><label>Origem<select name="origem">${o(ORIG,l.origem)}</select></label>
   <label>Plano de interesse<select name="plano">${o(PLANOS.map(p=>[p[0],p[1]]),l.plano||'')}</select></label><label>Telas<input type="number" name="telas" min="0" max="10" value="${esc(l.telas||'')}"></label>
   <label>Valor fechado (R$)<input type="number" name="valor" min="0" step="10" value="${esc(l.valor||'')}" placeholder="${l.plano&&PL[l.plano][2]?'a partir de '+PL[l.plano][2]:''}"></label><label>Responsável<input name="resp" maxlength="60" list="mv-resps" value="${esc(l.resp)}"><datalist id="mv-resps">${[...new Set(S.d.itens.map(x=>x.resp).filter(Boolean))].map(r=>`<option value="${esc(r)}">`).join('')}</datalist></label>
   <label>Próximo passo<input name="prox" maxlength="120" value="${esc(l.prox)}"></label><label>Data do próximo passo<input type="date" name="proxData" value="${esc(l.proxData)}"></label>
   <label>Contrato: início<input type="date" name="cIni" value="${esc(l.cIni)}"></label><label>Contrato: fim<input type="date" name="cFim" value="${esc(l.cFim)}"></label>
   <label class="mv-chk"><input type="checkbox" name="exclusivo"${l.exclusivo?' checked':''}> Exclusividade do ramo (+50%, 6 meses)</label>${l.etapa==='perdido'?`<label>Motivo da perda<select name="motivo">${o(MOTIVOS,l.motivo)}</select></label>`:''}
   <label class="w2">Notas<textarea name="notas" rows="3" maxlength="2000">${esc(l.notas)}</textarea></label>
   <div class="mv-acoes w2">${id?`<button type="button" class="mv-b dg" onclick="__crmApaga('${id}')">Excluir</button>`:''}<span class="mv-grow"></span><button class="mv-b pri">Salvar</button></div></form>
  ${id?`<aside class="mv-side"><h4 class="mv-h4">Telas</h4>${tel.map(t=>`<div class="mv-row"><span class="mv-mono">TELA ${String(t.n).padStart(2,'0')}</span><span class="mv-grow">${t.st}${t.ate?' até '+br(t.ate):''}</span></div>`).join('')||'<div class="mv-vz">nenhuma</div>'}
   <h4 class="mv-h4">Follow-up</h4>${tar.map(t=>`<div class="mv-row${t.feito?' done':''}"><span class="mv-mono mv-dt">${br(t.quando).slice(0,5)}</span><span class="mv-grow">${esc(t.tit)}</span>${t.feito?'<span class="mv-l2">feito</span>':`<button class="mv-b wa sm" onclick="__crmWa('${id}','${t.k}','${t.id}');setTimeout(()=>__crmAbre('${id}'),30)">Enviar</button>`}</div>`).join('')||'<div class="mv-vz">sem tarefas</div>'}
   <h4 class="mv-h4">Agendamentos</h4>${ags.map(([,a])=>`<div class="mv-row"><span class="mv-mono mv-dt">${br(a.data).slice(0,5)} ${a.hora}</span><span class="mv-grow">${esc(a.tipo)} · ${esc(a.status)}</span></div>`).join('')||'<div class="mv-vz">nenhum</div>'}
   <h4 class="mv-h4">Objeções (resposta pronta)</h4><div class="mv-obj">${OBJ.map(([q,r])=>`<button class="mv-b sm" onclick="navigator.clipboard.writeText(${esc(JSON.stringify(r))}).then(()=>__toast('Resposta copiada.'))">${q}</button>`).join('')}</div>
   <h4 class="mv-h4">Linha do tempo</h4><form class="mv-nota" onsubmit="event.preventDefault();__crmNota('${id}',this.t.value);this.reset()"><input name="t" placeholder="Registrar ligação, visita, conversa…" maxlength="300"><button class="mv-b">Anotar</button></form>
   <ol class="mv-tl">${l.hist.slice().reverse().map(h=>`<li data-t="${h.tipo}"><span class="mv-mono">${new Date(h.em).toLocaleString('pt-BR',{day:'2-digit',month:'2-digit',hour:'2-digit',minute:'2-digit'})}</span>${esc(h.txt)}</li>`).join('')}</ol></aside>`:''}</div>`,true);
  $('#mv-lf').onsubmit=e=>{e.preventDefault();const f=Object.fromEntries(new FormData(e.target));f.exclusivo=!!f.exclusivo;f.whats=fone(f.whats);f.nome=f.empresa;
    if(f.exclusivo&&f.ramo&&S.d.exclus[f.ramo]&&S.d.exclus[f.ramo]!==id&&L(S.d.exclus[f.ramo])){toast(`O ramo ${f.ramo} já é exclusivo de ${L(S.d.exclus[f.ramo]).empresa}.`);return}
    let nid=id;mut(d=>{let x=id&&d.itens.find(q=>q.id===id);
      if(!x){x={id:nid=nid||uid(),etapa:'e1',hist:[],criado:new Date().toISOString(),max:0};d.itens.push(x);Object.assign(x,f);hist(x,'Cadastrada · origem: '+(f.origem||''),'etapa');(CAD.e1||[]).forEach(([tit,k,n])=>d.tarefas.push({id:uid(),lead:x.id,tit,k,quando:mais(n),etapa:'e1',feito:false}))}
      else{const ant=x.cFim;Object.assign(x,f);x.em=new Date().toISOString();hist(x,'Ficha atualizada','nota');if(f.cFim&&f.cFim!==ant){d.tarefas.push({id:uid(),lead:x.id,tit:'Proposta de renovação',k:'REN',quando:mais(-7,f.cFim),etapa:x.etapa,feito:false})}}
      Object.keys(d.exclus).forEach(r=>{if(d.exclus[r]===x.id)delete d.exclus[r]});if(x.exclusivo&&x.ramo)d.exclus[x.ramo]=x.id},'Salvo.');
    S.lead=nid;setTimeout(ficha,20)};
}
window.__crmNota=(id,t)=>{if(!t.trim())return;mut(d=>{const l=d.itens.find(x=>x.id===id);l&&hist(l,t.trim(),'nota')});setTimeout(()=>__crmAbre(id),30)};
window.__crmApaga=id=>{if(!confirm('Excluir esta empresa e as tarefas dela?'))return;mut(d=>{d.itens=d.itens.filter(x=>x.id!==id);d.tarefas=d.tarefas.filter(t=>t.lead!==id);d.telas.forEach(t=>{if(t.lead===id){t.lead='';t.st='livre'}});Object.keys(d.exclus).forEach(r=>{if(d.exclus[r]===id)delete d.exclus[r]})},'Excluída.');__crmFecha()};
window.__crmAg=id=>{const l=L(id);__crmFecha();location.hash='agenda';setTimeout(()=>window.__agForm&&window.__agForm('','',{empresa:l.empresa,contato:l.contato,wa:l.whats,bairro:l.bairro,resp:l.resp,lead:id,etapa:EN[l.etapa]+1,tipo:'visita'}),60)};
// ---------- CSV ----------
const COLS=['empresa','ramo','bairro','contato','whats','ig','origem','plano','telas','valor','resp','prox','proxData','etapa','motivo','cIni','cFim','exclusivo','notas'];
window.__crmCsv=()=>{const q=v=>`"${String(v??'').replace(/"/g,'""')}"`;const t=[COLS.join(';'),...S.d.itens.map(l=>COLS.map(c=>q(c==='etapa'?nomeE(l.etapa):l[c])).join(';'))].join('\n');
  const a=document.createElement('a');a.href=URL.createObjectURL(new Blob(['﻿'+t],{type:'text/csv'}));a.download=`crm-mova-${hoje()}.csv`;a.click()};
window.__crmImp=inp=>{const f=inp.files[0];if(!f)return;f.text().then(t=>{const ls=t.replace(/^﻿/,'').split(/\r?\n/).filter(Boolean);const sep=ls[0].includes(';')?';':',';
  const parse=s=>{const o=[];let c='',q=false;for(let i=0;i<s.length;i++){const ch=s[i];if(q){if(ch=='"'&&s[i+1]=='"'){c+='"';i++}else if(ch=='"')q=false;else c+=ch}else if(ch=='"')q=true;else if(ch==sep){o.push(c);c=''}else c+=ch}o.push(c);return o};
  const h=parse(ls[0]).map(x=>x.trim().toLowerCase());const ix=k=>h.indexOf(k.toLowerCase());let n=0;
  mut(d=>{ls.slice(1).forEach(li=>{const v=parse(li),g=k=>{const i=ix(k);return i>-1?(v[i]||'').trim():''};const emp=g('empresa')||g('nome');if(!emp)return;
    const et=ET.find(e=>e[1].toLowerCase()===g('etapa').toLowerCase()||e[0]===g('etapa'));const x={id:uid(),hist:[],criado:new Date().toISOString(),etapa:et?et[0]:'e1'};
    COLS.forEach(c=>{if(c!=='etapa'){const val=g(c);if(val)x[c]=val}});x.empresa=x.nome=emp;x.whats=fone(x.whats||g('whatsapp')||g('telefone'));x.exclusivo=/^(sim|true|1)$/i.test(g('exclusivo'));x.max=EN[x.etapa];hist(x,'Importada por CSV','etapa');d.itens.push(x);n++})});
  toast(n+' empresa(s) importada(s).');inp.value=''})};
// ---------- tela principal ----------
function view(){if(!S.carregou){carregar();return '<div class="mv-pn"><p class="mv-l2">Carregando o CRM…</p></div>'}
  const it=S.d.itens,h=hoje(),tp=S.d.tarefas.filter(t=>!t.feito&&L(t.lead)),lista=filtrada(),resps=[...new Set(it.map(l=>l.resp).filter(Boolean))];
  const kp=[['Empresas no funil',it.filter(l=>!['perdido','e7','e8','e9'].includes(l.etapa)).length],['Propostas abertas',it.filter(l=>['e5','e6'].includes(l.etapa)).length],['Follow-ups hoje',tp.filter(t=>t.quando<=h).length],['Telas ocupadas',S.d.telas.filter(t=>t.st==='ocupada').length+'/10']];
  setTimeout(()=>{if(S.lead&&!$('#mv-modal .mv-caixa'))ficha()},0);
  return `${S.off?'<div class="mv-aviso">Sem conexão com o servidor: o que salvar agora fica só neste aparelho.</div>':''}
  <div class="mv-kpis">${kp.map(([r,v])=>`<div><span class="mv-k">${r}</span><b class="mv-big">${v}</b></div>`).join('')}</div>
  <div class="mv-bar2"><nav class="mv-seg">${[['funil','Funil'],['lista','Lista'],['tarefas','Follow-up'+(tp.filter(t=>t.quando<=h).length?' · '+tp.filter(t=>t.quando<=h).length:'')],['telas','Telas'],['metricas','Métricas']].map(([k,n])=>`<button class="${S.aba===k?'on':''}" onclick="__crmAba('${k}')">${n}</button>`).join('')}</nav>
   <span class="mv-grow"></span><button class="mv-b pri" onclick="__crmAbre('')">+ Nova empresa</button><button class="mv-b" onclick="__crmCsv()">Exportar CSV</button><label class="mv-b">Importar CSV<input type="file" accept=".csv,text/csv" hidden onchange="__crmImp(this)"></label></div>
  ${['funil','lista'].includes(S.aba)?`<div class="mv-filtros"><input type="search" placeholder="Buscar empresa, contato, bairro…" value="${esc(S.busca)}" oninput="__crmF('busca',this.value)">
   <select onchange="__crmF('fE',this.value)"><option value="">Todas as etapas</option>${ET.map(e=>`<option value="${e[0]}"${S.fE===e[0]?' selected':''}>${e[1]}</option>`).join('')}</select>
   <select onchange="__crmF('fO',this.value)"><option value="">Todas as origens</option>${ORIG.map(o=>`<option${S.fO===o?' selected':''}>${o}</option>`).join('')}</select>
   <select onchange="__crmF('fR',this.value)"><option value="">Toda a equipe</option>${resps.map(o=>`<option${S.fR===o?' selected':''}>${esc(o)}</option>`).join('')}</select></div>`:''}
  <div class="mv-pn" id="mv-corpo">${S.aba==='funil'?kanban(lista):S.aba==='lista'?listaV(lista):S.aba==='tarefas'?tarefasV():S.aba==='telas'?telasV():metricasV()}</div>`}
window.__crmAba=k=>{S.aba=k;rr()};
let tb;window.__crmF=(k,v)=>{S[k]=v;clearTimeout(tb);tb=setTimeout(()=>{const a=document.activeElement,pos=a&&a.selectionStart;rr();if(k==='busca'){const i=$('.mv-filtros input');i&&(i.focus(),i.setSelectionRange(pos,pos))}},k==='busca'?250:0)};

// Visão geral só com dado real (sem gráfico de exemplo do modelo): agenda de hoje, follow-ups, funil e telas
window.__V.inicio=()=>{if(!S.carregou){carregar();return '<div class="mv-pn"><p class="mv-l2">Carregando…</p></div>'}
  const h=hoje(),ag=window.__agS?Object.entries(window.__agS().itens).map(([id,a])=>Object.assign({id},a)).filter(a=>a.data===h&&a.status!=='cancelado').sort((a,b)=>a.hora.localeCompare(b.hora)):[];
  const tp=S.d.tarefas.filter(t=>!t.feito&&L(t.lead)&&t.quando<=h),oc=S.d.telas.filter(t=>t.st==='ocupada').length;
  const bd=window.__h&&window.__h.bomDia?window.__h.bomDia():'';
  return `${bd}<div class="mv-kpis"><div><span class="mv-k">Agenda de hoje</span><b class="mv-big">${ag.length}</b></div><div><span class="mv-k">Follow-ups pendentes</span><b class="mv-big">${tp.length}</b></div><div><span class="mv-k">Empresas no funil</span><b class="mv-big">${S.d.itens.filter(l=>!['perdido','e7','e8','e9'].includes(l.etapa)).length}</b></div><div><span class="mv-k">Telas ocupadas</span><b class="mv-big">${oc}<small>/10</small></b></div></div>
  <div class="mv-g2"><div class="mv-blk"><h4 class="mv-h4">Hoje na rua <span>${ag.length}</span></h4>${ag.map(a=>`<div class="mv-row"><span class="mv-mono mv-dt">${a.hora}</span><span class="mv-grow"><b>${esc(a.empresa)}</b><div class="mv-l2">${esc([a.bairro,a.resp].filter(Boolean).join(' · '))}</div></span></div>`).join('')||'<div class="mv-vz">nada marcado hoje</div>'}<a class="mv-b" href="#agenda" style="margin-top:8px">Abrir agendamentos</a></div>
  <div class="mv-blk"><h4 class="mv-h4">Follow-up de hoje <span>${tp.length}</span></h4>${tp.slice(0,6).map(t=>{const l=L(t.lead);return `<div class="mv-row"><span class="mv-mono mv-dt">${br(t.quando).slice(0,5)}</span><span class="mv-grow"><b>${esc(t.tit)}</b> · ${esc(l.empresa)}</span><button class="mv-b wa sm" onclick="__crmWa('${l.id}','${t.k}','${t.id}')">WhatsApp</button></div>`}).join('')||'<div class="mv-vz">em dia</div>'}<a class="mv-b" href="#crm" style="margin-top:8px">Abrir CRM</a></div></div>`};

// Financeiro: as 10 telas e a receita dos contratos vêm do CRM (dado real; vazio até haver contrato)
const fin0=window.__V.financeiro;if(fin0)window.__V.financeiro=()=>{if(!S.carregou){carregar()}const d=S.d||base(),oc=d.telas.filter(t=>t.st==='ocupada').length,rs=d.telas.filter(t=>t.st==='reservada').length,ct=d.itens.filter(l=>['e7','e8','e9'].includes(l.etapa)),v=ct.reduce((a,l)=>a+(+l.valor||0),0);
  return `<div class="mv-kpis"><div><span class="mv-k">Telas ocupadas</span><b class="mv-big">${oc}<small>/10</small></b></div><div><span class="mv-k">Reservadas</span><b class="mv-big">${rs}</b></div><div><span class="mv-k">Livres</span><b class="mv-big">${10-oc-rs}</b></div><div><span class="mv-k">Contratos · valor</span><b class="mv-big">${ct.length}</b><span class="mv-l2">${v?brl(v):'sem valor lançado'}</span></div></div>`+fin0()};

// Abas do modelo: nada de exemplo. Métricas = números reais do CRM; Calendário e Reuniões = agenda; o resto aguarda dado real.
const vazio=(t,txt,lnk)=>`<div class="mv-blk" style="padding:48px 24px;text-align:center"><span class="mv-k">${t}</span><div class="mv-mt" style="margin:14px 0 8px">Aguardando dados</div><p class="mv-l2" style="max-width:460px;margin:0 auto">${txt}</p>${lnk?`<a class="mv-b" style="margin-top:18px" href="${lnk[0]}">${lnk[1]}</a>`:''}</div>`;
Object.assign(window.__V,{
 resultados:()=>{if(!S.carregou){carregar();return ''}return metricasV()},
 calendario:()=>window.__V.agenda(), reunioes:()=>window.__V.agenda(),
 planejamento:()=>vazio('Planejamento','O planejamento do mês entra aqui quando a agência publicar o calendário aprovado da Mova.',['#aprovacoes','Ver aprovações']),
 relatorios:()=>vazio('Relatórios','Os relatórios mensais entram aqui com os números reais do Instagram, dos anúncios e do CRM.',['#resultados','Ver métricas do CRM']),
 conteudos:()=>vazio('Conteúdos','As peças da Mova ficam em Aprovações enquanto aguardam o seu ok, e em Postados depois de publicadas.',['#aprovacoes','Abrir aprovações']),
 campanhas:()=>vazio('Campanhas','As campanhas de anúncio aparecem aqui quando forem ao ar, com investimento e resultado reais.'),
 contrato:()=>vazio('Contrato','O contrato da Mova com a agência entra aqui quando for assinado.'),
 pedidos:()=>vazio('Pedidos','Para pedir arte, ajuste ou tirar dúvida, fale com a agência no WhatsApp. Os pedidos registrados aparecem aqui.'),
 fotos:()=>vazio('Fotos','As fotos enviadas pela Mova aparecem aqui, separadas entre novas e usadas.')});
Object.assign(window.__T,{resultados:'Métricas',calendario:'Agendamentos',reunioes:'Agendamentos'});
window.__V.crm=view;window.__T.crm='CRM comercial';
})();
