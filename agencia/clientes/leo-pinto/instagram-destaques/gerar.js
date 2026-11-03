// node gerar.js [pasta] -> capa-01..06.jpg (2160x3840, alta qualidade, JPEG 95) (como aparece no perfil). Conta Leandro, 03/11/2026.
const {chromium}=require('playwright');const path=require('path');const out=path.resolve(process.argv[2]||__dirname);
const N=['quem-sou','na-rua','feito','camara','nossa-baixada','fale-comigo'];
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920},deviceScaleFactor:2});
for(let d=0;d<6;d++){await p.goto('file://'+__dirname+'/destaques.html?d='+d,{waitUntil:'networkidle'});await p.waitForFunction('window.pronto===true');await p.waitForTimeout(300);
 await p.screenshot({path:`${out}/capa-0${d+1}-${N[d]}.jpg`,type:'jpeg',quality:95})}
await b.close()})();
