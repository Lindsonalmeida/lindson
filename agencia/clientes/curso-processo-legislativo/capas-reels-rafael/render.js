const {chromium}=require('playwright');const N=require('./nomes.json');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});await p.goto('file://'+__dirname+'/pecas.html');await p.waitForTimeout(2500);
for(const n of N){await (await p.$('[id="'+n+'"] .c')).screenshot({path:n+'.jpg',type:'jpeg',quality:92})}await b.close()})();
