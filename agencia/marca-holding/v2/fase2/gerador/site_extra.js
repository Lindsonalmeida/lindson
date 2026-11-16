/* v2 Awwwards (conta Pedro, 16/11/2026) */
(()=>{const ok=()=>document.body.classList.add('ok');addEventListener('load',()=>setTimeout(ok,700));setTimeout(ok,2500);
const c=document.querySelector('.cur');if(c){addEventListener('mousemove',e=>{c.style.left=e.clientX+'px';c.style.top=e.clientY+'px'},{passive:true});
document.querySelectorAll('a,button').forEach(a=>{a.addEventListener('mouseenter',()=>c.classList.add('big'));a.addEventListener('mouseleave',()=>c.classList.remove('big'))})}
const f=document.querySelector('.foto-slz .foto-in');if(f){const g=()=>{const r=f.parentNode.getBoundingClientRect();f.style.transform='translateY('+(r.top*-.12)+'px) scale(1.05)'};addEventListener('scroll',g,{passive:true});g()}})();
