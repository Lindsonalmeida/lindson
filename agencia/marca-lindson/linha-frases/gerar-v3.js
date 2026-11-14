// Gera as artes da linha de frases e da linha Provedor (conta Leandro, 14/11/2026). Uso: node gerar.js
const {chromium}=require('playwright'),path=require('path'),fs=require('fs'),D=__dirname;
const ids=['p1','p2','p3','p4'];for(const c of ['c1','c2','c3','c4'])for(let i=1;i<=6;i++)ids.push(c+'_'+i);
(async()=>{const b=await chromium.launch();for(const id of ids){const p=await b.newPage({viewport:{width:1080,height:1350}});
await p.goto('file://'+path.join(D,'arte-v3.html')+'?a='+id);await p.waitForFunction(()=>window.pronto,null,{timeout:30000});await p.waitForTimeout(300);
const o='artes-provedor-v3';await p.screenshot({path:path.join(D,o,id+'.jpg'),type:'jpeg',quality:88});await p.close();}
await b.close();})();
