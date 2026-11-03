// node render.js [pasta das prévias] -> real-time-manual-de-marca-v1.pdf (conta Pedro, 03/11/2026)
const {chromium}=require('playwright');(async()=>{
const b=await chromium.launch({proxy:process.env.HTTPS_PROXY?{server:process.env.HTTPS_PROXY}:undefined,args:['--allow-file-access-from-files']});
const p=await b.newPage({viewport:{width:1080,height:1350}});
const erros=[];p.on('pageerror',e=>erros.push(e.message));
await p.goto('file://'+__dirname+'/manual.html',{waitUntil:'networkidle'});await p.waitForFunction('window.pronto===true');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(500);
const over=await p.evaluate(()=>[...document.querySelectorAll('.pg')].map((s,i)=>{const t=s.getBoundingClientRect().top;let m=0;s.querySelectorAll('.corpo *').forEach(e=>{m=Math.max(m,e.getBoundingClientRect().bottom-t)});return [i+1,Math.round(m)]}).filter(x=>x[1]>1250));
console.log('páginas', await p.$$eval('.pg',x=>x.length),'passam de 1250:',JSON.stringify(over),'erros:',JSON.stringify(erros));
await p.pdf({path:__dirname+'/real-time-manual-de-marca-v1.pdf',width:'1080px',height:'1350px',printBackground:true});
const dir=process.argv[2];if(dir){const s=await p.$$('.pg');for(const [i,e] of s.entries())await e.screenshot({path:`${dir}/m${String(i+1).padStart(2,'0')}.png`});}
await b.close()})();
