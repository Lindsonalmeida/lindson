"""Coloca os vídeos do Passaporte da Bíblia numa aba própria da Fábrica de Conteúdo.
python3 fabrica_pv.py <fabrica.html baixada do artifact> -> scratchpad/fabrica/index.html
Capas e vídeos usam os endereços /_blob da própria Fábrica (ativos-fabrica.json)."""
import json, os, re, sys
D = os.path.dirname(os.path.abspath(__file__)); RAIZ = os.path.join(D, '..')
OUT = '/tmp/claude-0/-home-user/5acf6937-9ac6-56e0-bc29-78bef210dc8b/scratchpad/fabrica'; os.makedirs(OUT, exist_ok=True)
html = open(sys.argv[1]).read()
html = re.sub(r'<!--PAS-INI-->.*?<!--PAS-FIM-->', '', html, flags=re.S)  # tira a versão anterior da aba
html = re.sub(r'/\*PAS-INI\*/.*?/\*PAS-FIM\*/', '', html, flags=re.S)
at = json.load(open(RAIZ + '/ativos-fabrica.json')); tempos = json.load(open(RAIZ + '/tempos.json'))
spec = {v['id']: v for v in json.load(open(RAIZ + '/pintura.json'))}
ORDEM = ['pv-01'] + [f'short-{i:02d}' for i in range(1, 21)] + [f'longo-{i:02d}' for i in range(1, 5)]
lote = []
for n, k in enumerate(ORDEM):
    v = spec[k]; longo = v['formato'] == 'longo'; pronto = os.path.exists(f'{RAIZ}/videos/{k}-app.mp4')
    leg = v['legenda'].replace('{CAPITULOS}', '\n'.join(f'{a} {b}' for a, b in tempos.get(k, [])))
    it = dict(id=k, formato=v['formato'], num=0 if k == 'pv-01' else int(k[-2:]), ordem=n, titulo=v['titulo'], legenda=leg, comentario=v.get('comentario', ''),
              aviso=('Vídeo pronto: baixe no app "Passaporte da Bíblia · Postagens" e toque em "Enviar vídeo" para guardar aqui.' if pronto else 'Vídeo em produção. Título, legenda e capa já estão prontos.'),
              rev=2 if pronto else 1)
    if longo: it.update(thumbA=at.get(f'{k}-A.jpg'), thumbB=at.get(f'{k}-B.jpg'))
    else: it['capa'] = at.get(f'{k}.jpg')
    if at.get(f'{k}-app.mp4'): it['url'] = at[f'{k}-app.mp4']; it['aviso'] = ''; it['rev'] = 3
    lote.append(it)

SECAO = '''<!--PAS-INI--><section class="view" id="v-pas" hidden>
  <div class="card">
    <div class="mono dot">Canal Passaporte da Bíblia · YouTube</div>
    <h2>Vídeos do Passaporte</h2>
    <p class="muted" style="margin:0">Gravuras de Doré com narração. Assista, baixe a capa, copie título, legenda e comentário e marque como postado. Shorts todos os dias e um vídeo longo por semana.</p>
    <div class="row" style="justify-content:space-between">
      <div class="filt" id="pas-filt"><button data-f="a postar" aria-pressed="true">A postar</button><button data-f="postado" aria-pressed="false">Postados</button></div>
    </div>
  </div>
  <div class="card"><div class="mono dot">Shorts · 9:16</div><div class="vgrid" id="pas-shorts"></div></div>
  <div class="card"><div class="mono dot">Vídeos longos · 16:9</div><div class="vgrid lg" id="pas-longos"></div></div>
</section><!--PAS-FIM-->'''
JS = '''/*PAS-INI*/
let pasVids=[],pasFiltro='a postar',pasSemeado=false;
const PAS_LOTE=__LOTE__;
function renderPas(){
  const vis=pasVids.filter(v=>(v.status||'a postar')===pasFiltro),post=pasVids.filter(v=>v.status==='postado').length;
  $$('#pas-filt button').forEach(b=>b.textContent=b.dataset.f==='postado'?`Postados (${post})`:`A postar (${pasVids.length-post})`);
  for(const [fmt,el] of [['short','#pas-shorts'],['longo','#pas-longos']]){
    const box=$(el),lista=vis.filter(v=>v.formato===fmt);
    if(!lista.length){const p=document.createElement('p');p.className='muted';p.style.margin='0';p.textContent=pasVids.some(v=>v.formato===fmt)?'Nenhum vídeo neste filtro.':'Os vídeos aparecem aqui conforme ficam prontos.';box.replaceChildren(p);continue}
    box.replaceChildren(...lista.map(cardPas));
  }
}
function semearPas(){if(pasSemeado||!db)return;pasSemeado=true;const tem=new Set(pasVids.map(v=>v.id));
  for(const v of PAS_LOTE){const ex=pasVids.find(x=>x.id===v.id);if(ex&&(v.rev||0)>(ex.rev||0)){const up={titulo:v.titulo,legenda:v.legenda,comentario:v.comentario,aviso:v.aviso,rev:v.rev,capa:v.capa||null,thumbA:v.thumbA||null,thumbB:v.thumbB||null};if(v.url)up.url=v.url;db.doc('passaporte/'+v.id).update(up).catch(e=>console.warn(e))}}
  PAS_LOTE.filter(v=>!tem.has(v.id)).forEach(async v=>{try{const a=await db.doc('passaporte/'+v.id).get();if(a&&a.exists)return}catch(e){}
    await db.doc('passaporte/'+v.id).set({...v,status:'a postar',criadoEm:Date.now()}).catch(e=>console.warn(e))})}
function cardPas(v){
  const st=v.status==='postado'?'postado':'a postar',nn=v.num?String(v.num).padStart(2,'0'):'especial',base='passaporte-'+v.formato+'-'+nn;
  const d=document.createElement('div');d.className='vid'+(st==='postado'?' postado':'');
  const capa=v.formato==='longo'?v.thumbA:v.capa;
  if(v.url){const vd=document.createElement('video');vd.src=v.url;vd.controls=true;if(capa)vd.poster=capa;vd.preload='none';vd.playsInline=true;d.appendChild(vd)}
  else if(capa){const im=document.createElement('img');im.src=capa;im.alt='';im.loading='lazy';im.style.cssText='width:100%;display:block;object-fit:cover;aspect-ratio:'+(v.formato==='longo'?'16/9':'9/16');d.appendChild(im)}
  else{const p=document.createElement('div');p.className='pend';p.textContent='Vídeo em produção';d.appendChild(p)}
  const b=document.createElement('div');b.className='vb';
  const top=document.createElement('div');top.className='row';top.style.justifyContent='space-between';
  const n=document.createElement('span');n.className='mono';n.textContent=(v.formato==='longo'?'Longo ':'Short ')+(v.num?nn:'especial');
  const c=document.createElement('span');c.className='chip '+(st==='postado'?'ok':'warn');c.textContent=st==='postado'?'Postado':'A postar';top.append(n,c);
  const t=document.createElement('b');t.textContent=v.titulo||'';b.append(top,t);
  if(v.aviso){const av=document.createElement('p');av.className='muted';av.style.margin='0';av.textContent=v.aviso;b.append(av)}
  const r1=document.createElement('div');r1.className='row';
  r1.append(btnCopiar('Copiar título',()=>v.titulo||'','sun'),btnCopiar('Copiar legenda',()=>v.legenda||'','ghost'));
  if(v.comentario)r1.append(btnCopiar('Copiar comentário',()=>v.comentario,'ghost'));
  const r2=document.createElement('div');r2.className='row';
  if(downloads){
    if(v.url)r2.append(btnBaixarUrl('Baixar vídeo',v.url,base+'.mp4'));
    if(v.capa)r2.append(btnBaixarUrl('Baixar capa',v.capa,base+'-capa.jpg'));
    if(v.thumbA)r2.append(btnBaixarUrl('Baixar capa A',v.thumbA,base+'-capa-A.jpg'));
    if(v.thumbB)r2.append(btnBaixarUrl('Baixar capa B',v.thumbB,base+'-capa-B.jpg'));
  }
  if(!v.url&&assets){const up=document.createElement('label');up.className='btn blue';up.textContent='Enviar vídeo';up.style.cursor='pointer';
    const inp=document.createElement('input');inp.type='file';inp.accept='video/mp4,video/*';inp.hidden=true;up.appendChild(inp);
    inp.onchange=async()=>{const f=inp.files[0];if(!f)return;up.firstChild.textContent='Enviando… ';
      try{const r=await assets.upload(f,{type:f.type||'video/mp4'});await db.doc('passaporte/'+v.id).update({url:r.url,videoId:r.id,aviso:''})}
      catch(e){up.firstChild.textContent=(e&&e.message&&/size|large|grande/i.test(e.message)?'Arquivo grande demais (máx. 20 MB) ':'Não enviou, tente de novo ')}};
    r2.append(up)}
  const sb=document.createElement('button');sb.className='btn '+(st==='postado'?'ghost':'blue');sb.textContent=st==='postado'?'Voltar para "a postar"':'Marcar como postado';
  sb.onclick=async()=>{sb.disabled=true;try{await db.doc('passaporte/'+v.id).update({status:st==='postado'?'a postar':'postado',postadoEm:st==='postado'?null:Date.now()})}catch(e){sb.textContent='Não salvou';sb.disabled=false}};
  r2.append(sb);b.append(r1,r2);d.appendChild(b);return d;
}
/*PAS-FIM*/'''.replace('__LOTE__', json.dumps(lote, ensure_ascii=False).replace('</', '<\\/'))

def troca(a, b, n=1):
    global html
    assert html.count(a) >= 1, a[:60]
    html = html.replace(a, b, n)
if 'data-v="pas"' not in html: troca('<button data-v="maq">Maquiavel</button>', '<button data-v="maq">Maquiavel</button>\n    <button data-v="pas">Passaporte</button>')
troca('<!-- MAQUIAVEL (canal Raposa e Leão) -->', SECAO + '\n<!-- MAQUIAVEL (canal Raposa e Leão) -->')
troca('function btnCopiar(', JS + '\nfunction btnCopiar(')
if "collection('passaporte')" not in html:
    troca("  status(sample?'':", "  db.collection('passaporte').onSnapshot(s=>{pasVids=s.docs.map(d=>({id:d.id,...d.data()})).sort((a,b)=>(a.ordem||0)-(b.ordem||0));renderPas();semearPas()},e=>console.warn(e));\n  status(sample?'':")
if '#pas-filt button' not in html.split('function ligarUI')[1][:3000]:
    troca("  $$('#maq-filt button').forEach(b=>b.onclick=", "  $$('#pas-filt button').forEach(b=>b.onclick=()=>{pasFiltro=b.dataset.f;$$('#pas-filt button').forEach(x=>x.setAttribute('aria-pressed',String(x===b)));renderPas()});\n  $$('#maq-filt button').forEach(b=>b.onclick=")
open(OUT + '/index.html', 'w').write(html)
print(OUT + '/index.html', len(lote), 'vídeos;', sum(1 for i in lote if i.get('url')), 'com vídeo')
