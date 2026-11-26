// Gera as 7 telas do carrossel 1.2 (conta Leandro, 26/11/2026). Uso: node gerar.js
const {chromium}=require('playwright'),path=require('path'),D=require('path').resolve(__dirname,'..');
(async()=>{const b=await chromium.launch();for(let i=1;i<=7;i++){const p=await b.newPage({viewport:{width:1080,height:1350}});
await p.goto('file://'+path.join(D,'v3/arte.html')+'?a='+i);await p.waitForFunction(()=>window.pronto,null,{timeout:30000});await p.waitForTimeout(400);
await p.screenshot({path:path.join(D,'v3','0'+i+'.jpg'),type:'jpeg',quality:90});await p.close();}await b.close();})();
