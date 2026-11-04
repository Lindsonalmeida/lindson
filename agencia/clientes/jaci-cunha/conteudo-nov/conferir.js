// Conferência automática das artes (conta Leandro, 04/11/2026): texto fora da arte, texto em cima do rosto, texto em cima de outro texto
// ou do rodapé, imagem quebrada. Uso: node conferir.js <artes.html>
const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1100,height:2000}});
await p.goto('file://'+require('path').resolve(process.argv[2]));await p.waitForLoadState('networkidle');await p.evaluate(()=>document.fonts.ready);
const r=await p.evaluate(()=>{const out=[];const ov=(a,b,m=0)=>a.left<b.right-m&&a.right>b.left+m&&a.top<b.bottom-m&&a.bottom>b.top+m;
for(const s of document.querySelectorAll('section.f')){const S=s.getBoundingClientRect();const rel=x=>({left:x.left-S.left,right:x.right-S.left,top:x.top-S.top,bottom:x.bottom-S.top});
 for(const im of s.querySelectorAll('img')) if(!im.complete||!im.naturalWidth) out.push([s.id,'imagem quebrada',im.src.slice(-40)]);
 // linhas de texto reais (Range por nó de texto)
 const linhas=[];const w=document.createTreeWalker(s,NodeFilter.SHOW_TEXT);let n;
 while(n=w.nextNode()){if(!n.textContent.trim())continue;const el=n.parentElement;const cs=getComputedStyle(el);if(cs.visibility=='hidden'||+cs.opacity===0)continue;
  const rg=document.createRange();rg.selectNodeContents(n);for(const q of rg.getClientRects()){if(q.width<2)continue;
   const isRod=!!el.closest('.rod'),isTopo=!!el.closest('.topo');linhas.push({...rel(q),t:n.textContent.trim().slice(0,30),rod:isRod,topo:isTopo,bloco:el.closest('.a')})}}
 for(const L of linhas){ if(L.left<20||L.right>1060||L.top<10||L.bottom>S.height-8) out.push([s.id,'texto encostado/fora da borda',L.t,Math.round(L.left),Math.round(L.right),Math.round(L.top),Math.round(L.bottom)]);}
 const ro=s.dataset.rosto;if(ro){const[x1,y1,x2,y2]=ro.split(',').map(Number);const F={left:x1,right:x2,top:y1-(y2-y1)*.35,bottom:y2};
  for(const L of linhas){if(L.topo||L.rod)continue;if(ov(L,F,4))out.push([s.id,'texto em cima do rosto',L.t]);}}
 for(let i=0;i<linhas.length;i++)for(let j=i+1;j<linhas.length;j++){const A=linhas[i],B=linhas[j];if(A.bloco===B.bloco&&!(A.rod!==B.rod))continue;if(ov(A,B,3))out.push([s.id,'texto sobre texto',A.t,'×',B.t]);}
}return out});
console.log(r.length?r.map(x=>x.join(' | ')).join('\n'):'nenhum problema');await b.close()})();
