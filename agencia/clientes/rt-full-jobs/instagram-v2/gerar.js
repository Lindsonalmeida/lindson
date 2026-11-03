// node gerar.js -> artes/post-01..06.jpg (2160x2700, alta qualidade) + previa-feed.jpg. Conta Leandro, 03/11/2026.
const {chromium}=require('playwright');const fs=require('fs');
(async()=>{fs.mkdirSync(__dirname+'/artes',{recursive:true});const b=await chromium.launch({args:['--allow-file-access-from-files']});
const p=await b.newPage({viewport:{width:1080,height:1350},deviceScaleFactor:2});const erros=[];p.on('pageerror',e=>erros.push(e.message));
for(let i=1;i<=6;i++){await p.goto('file://'+__dirname+'/posts.html?p='+i,{waitUntil:'networkidle'});await p.waitForFunction('window.pronto===true');await p.waitForTimeout(300);
 await p.screenshot({path:`${__dirname}/artes/post-0${i}.jpg`,type:'jpeg',quality:94})}
console.log('erros:',JSON.stringify(erros));await b.close()})();
