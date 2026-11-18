/* v4.1 (conta Pedro, 18/11): mídia que ainda não chegou usa uma imagem já existente; nome de arquivo nunca aparece */
(()=>{const FB={'vida-maos.mp4':'f/div-labs.mp4','vida-estudio.mp4':'f/div-media.mp4','tec-nucleo.mp4':'f/hero-pedra.mp4','tec-holograma.mp4':'f/case-labs.jpg','materia-latao.mp4':'f/div-barzakh.mp4','final-horizonte.mp4':'f/div-ventures.mp4'};
document.querySelectorAll('.mv[data-m]').forEach(el=>{const n=el.dataset.m.split('/').pop();if(!FB[n])return;
 fetch(el.dataset.m,{method:'HEAD'}).then(r=>{if(r.ok&&(r.headers.get('content-type')||'').match(/video|image/))return;const box=el.querySelector('.ph-in');box.innerHTML='';const s=FB[n];
  if(s.endsWith('.mp4')){const v=document.createElement('video');v.muted=true;v.loop=true;v.playsInline=true;v.autoplay=true;v.src=s;box.appendChild(v);v.play().catch(()=>{})}else box.style.backgroundImage='url('+s+')';el.classList.add('ok')}).catch(()=>{})})})();
