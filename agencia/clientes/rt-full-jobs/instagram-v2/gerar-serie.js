// node gerar-serie.js -> serie/inventario-01..14.jpg (2160x2700) + previa-serie.jpg. Conta Leandro, 03/11/2026.
const {chromium}=require('playwright');const fs=require('fs');
(async()=>{fs.mkdirSync(__dirname+'/serie',{recursive:true});const b=await chromium.launch({args:['--allow-file-access-from-files']});
const p=await b.newPage({viewport:{width:1080,height:1350},deviceScaleFactor:2});const erros=[];p.on('pageerror',e=>erros.push(e.message));
for(let i=1;i<=14;i++){await p.goto('file://'+__dirname+'/serie.html?n='+i,{waitUntil:'networkidle'});await p.waitForFunction('window.pronto===true');await p.waitForTimeout(250);
 await p.screenshot({path:`${__dirname}/serie/inventario-${String(i).padStart(2,'0')}.jpg`,type:'jpeg',quality:93})}
console.log('erros:',JSON.stringify(erros));await b.close()})();
