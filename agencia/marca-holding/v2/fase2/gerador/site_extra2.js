/* v3 motion (conta Pedro, 16/11/2026): Lenis, GSAP/ScrollTrigger, imagens quando existirem, transição entre páginas */
(()=>{const red=matchMedia('(prefers-reduced-motion: reduce)').matches;
const tenta=(src,ok)=>{const i=new Image();i.onload=()=>ok(src);i.src=src};
document.querySelectorAll('[data-img]').forEach(el=>tenta(el.dataset.img,s=>{const a=el.querySelector('.ph-in')||el;a.style.backgroundImage='url('+s+')';el.classList.add('ok')}));
const v=document.querySelector('.hero-vid');if(v&&!red&&innerWidth>700){const tv=(u,nx)=>fetch(u,{method:'HEAD'}).then(r=>{if(r.ok&&(r.headers.get('content-type')||'').includes('video')){v.src=u;v.play().then(()=>v.classList.add('on')).catch(()=>{})}else if(nx)tv(nx)}).catch(()=>nx&&tv(nx));tv(v.dataset.vid,v.dataset.alt)}
const tr=document.createElement('div');tr.className='troca';document.body.appendChild(tr);
document.querySelectorAll('a[href$=".html"],a[href="./"]').forEach(a=>a.addEventListener('click',e=>{if(e.metaKey||e.ctrlKey||a.target)return;e.preventDefault();document.body.classList.add('sai');setTimeout(()=>location.href=a.href,450)}));
addEventListener('pageshow',()=>document.body.classList.remove('sai'));
const go=()=>{if(red||!window.gsap)return;const g=window.gsap;if(window.ScrollTrigger)g.registerPlugin(ScrollTrigger);

document.querySelectorAll('.h-l').forEach(h=>{g.fromTo(h,{yPercent:30,opacity:0},{yPercent:0,opacity:1,duration:1.1,ease:'expo.out',scrollTrigger:{trigger:h,start:'top 88%'}})});
document.querySelectorAll('.ph.par .ph-in').forEach(p=>g.to(p,{yPercent:12,ease:'none',scrollTrigger:{trigger:p.parentNode,start:'top bottom',end:'bottom top',scrub:true}}));
document.querySelectorAll('.ph').forEach(p=>g.from(p,{clipPath:'inset(18% 8% 18% 8%)',duration:1.4,ease:'expo.out',scrollTrigger:{trigger:p,start:'top 85%'}}));
document.querySelectorAll('.div-card,.case,.val').forEach((c,i)=>{c.classList.add('on');c.style.transition='none';g.fromTo(c,{y:60,opacity:0},{y:0,opacity:1,duration:.9,delay:(i%4)*.08,ease:'power3.out',scrollTrigger:{trigger:c,start:'top 92%'}})});
const gig=document.querySelector('.gigante');if(gig)g.from(gig,{yPercent:40,ease:'none',scrollTrigger:{trigger:gig,start:'top bottom',end:'bottom bottom',scrub:true}})};
if(document.readyState==='complete')go();else addEventListener('load',go)})();
