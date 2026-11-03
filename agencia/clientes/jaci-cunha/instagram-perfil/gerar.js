// node gerar.js -> capa-01..07.jpg (2160x3840, alta qualidade) + previa.jpg (círculos). Conta Leandro, 03/11/2026.
const {chromium}=require('playwright');
const N=['avaliacao','harmonizacao','odonto','duvidas','pacientes','a-clinica','como-chegar'];
(async()=>{const b=await chromium.launch({args:['--allow-file-access-from-files']});const p=await b.newPage({viewport:{width:1080,height:1920},deviceScaleFactor:2});
for(let d=0;d<7;d++){await p.goto('file://'+__dirname+'/destaques.html?d='+d,{waitUntil:'networkidle'});await p.waitForFunction('window.pronto===true');
 await p.screenshot({path:`${__dirname}/capa-0${d+1}-${N[d]}.jpg`,type:'jpeg',quality:95})}
await b.close()})();
