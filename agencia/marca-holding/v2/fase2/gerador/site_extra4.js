/* v4 luxo (conta Pedro, 18/11/2026): mídia por nome de arquivo, galeria horizontal fixada no scroll, vídeo de abertura */
(()=>{const red=matchMedia('(prefers-reduced-motion: reduce)').matches;
document.querySelectorAll('.mv[data-m]').forEach(el=>{const src=el.dataset.m,box=el.querySelector('.ph-in');
 if(src.endsWith('.mp4')){fetch(src,{method:'HEAD'}).then(r=>{if(!r.ok||!(r.headers.get('content-type')||'').includes('video'))return;const v=document.createElement('video');v.muted=true;v.loop=true;v.playsInline=true;v.preload='metadata';v.src=src;box.appendChild(v);el.classList.add('ok');new IntersectionObserver(es=>es.forEach(e=>e.isIntersecting&&!red?v.play().catch(()=>{}):v.pause())).observe(el)}).catch(()=>{})}
 else{const i=new Image();i.onload=()=>{box.style.backgroundImage='url('+src+')';el.classList.add('ok')};i.src=src}});

addEventListener('load',()=>{if(red||!window.gsap||!window.ScrollTrigger||innerWidth<800)return;const t=document.querySelector('.vida-trilho');if(!t)return;
 gsap.to(t,{x:()=>-(t.scrollWidth-innerWidth+40),ease:'none',scrollTrigger:{trigger:'.vida',start:'top top',end:()=>'+='+(t.scrollWidth),pin:true,scrub:1,invalidateOnRefresh:true}});
 gsap.from('.tec-t',{y:80,opacity:0,duration:1.2,ease:'expo.out',scrollTrigger:{trigger:'.tec',start:'top 60%'}})})})();
