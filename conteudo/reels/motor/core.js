// Núcleo compartilhado dos estágios de Reels: tempo, easing, legenda e SFX.
const cl=(x,a=0,b=1)=>Math.max(a,Math.min(b,x)),lerp=(a,b,t)=>a+(b-a)*t;
const eo=t=>1-Math.pow(1-cl(t),3);
const eob=t=>{t=cl(t);const c1=1.70158,c3=c1+1;return 1+c3*Math.pow(t-1,3)+c1*Math.pow(t-1,2)};
const eel=t=>{t=cl(t);if(t===0||t===1)return t;return Math.pow(2,-10*t)*Math.sin((t*10-.75)*2.0944)+1};
const p=(t,a,d)=>cl((t-a)/d);
const el=h=>{const d=document.createElement('div');d.innerHTML=h.trim();return d.firstElementChild};
const segs=TL.segs;const SFX=[];window.SFX=SFX;
const sfx=(t,k)=>SFX.push([t,k]);
function caption(capEl,t,i){const s=segs[i];let h='';s.words.forEach(([w,wt],k)=>{if(t<wt-.02)return;const on=t>=wt&&(k===s.words.length-1||t<s.words[k+1][1]);h+=`<span class="${on?'on':''}">${w}</span>`});capEl.innerHTML=h}
const sceneAt=t=>{let i=0;while(i<segs.length-1&&t>=segs[i+1].s)i++;return i};
function boot(st,B,global){
  const scenes=segs.map((s,i)=>{s.vs0=s.vs-s.s;const L=el('<div class="layer" style="opacity:0"></div>');st.append(L);const up=B[s.type](L,s,i);return {L,up}});
  window.render=t=>{const i=sceneAt(t),s=segs[i],lt=t-s.s;scenes.forEach((x,k)=>x.L.style.opacity=k===i?1:0);scenes[i].up(lt,s.e-s.s,t);global&&global(t,i,lt)};
  document.fonts.ready.then(()=>setTimeout(()=>{window.ready=true},300));
}
