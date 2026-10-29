<style>
.iw{position:absolute;opacity:0;font-family:Anton;color:#EFE6D2}
.iw .tg{display:inline-block;font:700 calc(30px*var(--s)) Cinzel;letter-spacing:.2em;color:#0B0A08;background:#C9A227;padding:calc(10px*var(--s)) calc(24px*var(--s))}
.iw .card{margin-top:calc(22px*var(--s));background:#17140F;border:2px solid #3a3226;border-radius:calc(26px*var(--s));padding:calc(30px*var(--s)) calc(40px*var(--s));display:flex;gap:calc(28px*var(--s));align-items:center;text-align:left;box-shadow:0 20px 60px rgba(0,0,0,.6)}
.iw .av{flex:none;width:calc(96px*var(--s));height:calc(96px*var(--s));border-radius:50%;background:#C9A227;display:grid;place-items:center;font:900 calc(44px*var(--s)) Cinzel;color:#0B0A08}
.iw .us{font:700 calc(28px*var(--s)) Cinzel;color:#cdbf9f;letter-spacing:.06em}
.iw .ty{font:400 calc(64px*var(--s)) Anton;text-transform:uppercase;min-height:calc(72px*var(--s));margin-top:calc(6px*var(--s))}
.iw .ac{display:flex;gap:calc(34px*var(--s));margin-top:calc(14px*var(--s));font:700 calc(26px*var(--s)) Cinzel;color:#9b8f76}
.iw .bt{display:inline-flex;align-items:center;gap:calc(24px*var(--s));font:400 calc(80px*var(--s)) Anton;padding:calc(26px*var(--s)) calc(56px*var(--s));border-radius:calc(22px*var(--s));background:#CC0000;color:#fff;margin-top:calc(26px*var(--s))}
.iw .ic{flex:none;width:calc(120px*var(--s));height:calc(120px*var(--s));border-radius:50%;border:calc(6px*var(--s)) solid #C9A227;display:grid;place-items:center;background:#0B0A08}
.iw .ic svg{width:60%;height:60%}
.iw .big{font:400 calc(70px*var(--s))/1.05 Anton;text-transform:uppercase}
.iw .ring{position:absolute;border-radius:50%;border:calc(5px*var(--s)) solid #D9622B;opacity:0}
</style>
<script>
// Componente de interação com o ouvinte: comenta | checkin | segue | salva | manda
const IW_ICON={
 salva:'<svg viewBox="0 0 24 24" fill="#E2BE4A"><path d="M6 2h12a1 1 0 0 1 1 1v19l-7-4.5L5 22V3a1 1 0 0 1 1-1z"/></svg>',
 manda:'<svg viewBox="0 0 24 24" fill="#E2BE4A"><path d="M2 21l21-9L2 3v7l15 2-15 2z"/></svg>',
 checkin:'<svg viewBox="0 0 24 24" fill="#E2BE4A"><path d="M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20zm-1.5 14.5l-4-4 1.4-1.4 2.6 2.6 6.1-6.1 1.4 1.4z"/></svg>'};
const IW_SINO='<svg width="1em" height="1em" viewBox="0 0 24 24" fill="#fff" class="sino"><path d="M12 22a2.5 2.5 0 0 0 2.45-2h-4.9A2.5 2.5 0 0 0 12 22zm7-6V11a7 7 0 0 0-5.5-6.84V3.5a1.5 1.5 0 0 0-3 0v.66A7 7 0 0 0 5 11v5l-2 2v1h18v-1z"/></svg>';
const IW_CUR='<svg class="cur" viewBox="0 0 24 24" style="position:absolute;width:calc(100px*var(--s));height:calc(100px*var(--s));opacity:0"><path d="M4 2l14 9-6 1.5 3.5 7-2.5 1.2-3.5-7L4 18z" fill="#fff" stroke="#000" stroke-width="1"/></svg>';
function iwHTML(id,it,css,s){
 const st=`${css};--s:${s}`;
 if(it.tipo==='comenta')return `<div class="iw" id="${id}" style="${st}"><span class="tg">${it.txt}</span><div class="card"><div class="av">VC</div><div style="flex:1"><div class="us">@você · agora</div><div class="ty" id="${id}y"></div><div class="ac"><span>👍</span><span>👎</span><span>RESPONDER</span></div></div></div></div>`;
 if(it.tipo==='segue')return `<div class="iw" id="${id}" style="${st};text-align:center"><span class="tg">${it.txt}</span><br><span class="bt" id="${id}b"><span id="${id}l">INSCREVER-SE</span>${IW_SINO}</span>${IW_CUR}</div>`;
 const ic=IW_ICON[it.tipo]||IW_ICON.checkin;
 return `<div class="iw" id="${id}" style="${st}"><div class="card" style="justify-content:center"><div class="ic" style="position:relative">${ic}<i class="ring"></i></div><div class="big">${it.txt}</div></div></div>`;
}
function iwAnim(id,it,t0,t1,R,SFX){
 const el=document.getElementById(id);if(!el)return;
 R.push(t=>{const k=ease((t-t0)/.45)*cl((t1-t)/.3);el.style.opacity=k;el.style.transform=`translateY(${(1-ease((t-t0)/.45))*40}px)`});SFX.push([t0,'ding']);
 if(it.tipo==='comenta'){const y=document.getElementById(id+'y'),tx=it.digita||'',a=t0+.9;R.push(t=>{y.textContent=[...tx].slice(0,Math.floor(cl((t-a)/Math.max(.8,tx.length*.06))*[...tx].length)).join('')})}
 if(it.tipo==='segue'){const b=document.getElementById(id+'b'),l=document.getElementById(id+'l'),cu=el.querySelector('.cur'),si=el.querySelector('.sino'),c0=t0+1.4;
  R.push(t=>{const m=ease((t-t0-.4)/.9);cu.style.opacity=cl((t-t0-.3)/.2)*(t<c0+1.2?1:cl((c0+1.6-t)/.4));cu.style.left=(70-m*22)+'%';cu.style.top=(140-m*55)+'%';
   const d=t>=c0;b.style.transform=`scale(${t>c0&&t<c0+.18?.92:1})`;b.style.background=d?'#272727':'#CC0000';l.textContent=d?'INSCRITO':'INSCREVER-SE';
   const sw=t>c0+.6?Math.sin((t-c0-.6)*30)*Math.exp(-(t-c0-.6)*3)*25:0;si.style.transform=`rotate(${sw}deg)`});SFX.push([c0,'punch'])}
 if(it.tipo!=='comenta'&&it.tipo!=='segue'){const r=el.querySelector('.ring');R.push(t=>{const u=((t-t0)%1.4)/1.4;r.style.opacity=t>t0?(1-u)*.9:0;r.style.inset=(-u*30)+'px'})}
}
</script>
