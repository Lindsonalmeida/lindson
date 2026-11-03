// node gerar.js -> capa-01..06.png (1080x1920) e previa-perfil.png (conta Leandro, 03/11/2026)
const {chromium}=require('playwright');const fs=require('fs');
const BIO=fs.readFileSync(__dirname+'/BIO.md','utf8').split('<!-- bio -->')[1].split('<!-- fim -->')[0].trim().replace(/`/g,'');
(async()=>{const b=await chromium.launch({proxy:process.env.HTTPS_PROXY?{server:process.env.HTTPS_PROXY}:undefined,args:['--allow-file-access-from-files']});
for(let d=0;d<6;d++){const p=await b.newPage({viewport:{width:1080,height:1920}});await p.goto('file://'+__dirname+'/destaques.html?d='+d,{waitUntil:'networkidle'});await p.evaluate(()=>document.fonts.ready);await p.screenshot({path:`${__dirname}/capa-0${d+1}.png`});await p.close()}
const p=await b.newPage({viewport:{width:1080,height:1350}});await p.addInitScript(t=>{window.BIO=t},BIO);await p.goto('file://'+__dirname+'/destaques.html?perfil=1',{waitUntil:'networkidle'});await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);await p.screenshot({path:__dirname+'/previa-perfil.png'});
await b.close()})();
