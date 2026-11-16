const { chromium } = require('playwright');
const R=[['alphabet-us','https://abc.xyz'],['prosus-nl','https://www.prosus.com'],['kinnevik-se','https://www.kinnevik.com'],['investor-se','https://www.investorab.com'],['softbank-jp','https://group.softbank/en'],['tata-in','https://www.tata.com'],['constellation-ca','https://www.csisoftware.com'],['locomotive-ca','https://locomotive.ca'],['basement-ar','https://basement.studio'],['instrument-us','https://www.instrument.com'],['pentagram-uk','https://www.pentagram.com'],['stefanini-br','https://stefanini.com/pt-br']];
(async()=>{const b=await chromium.launch();const O=__dirname+'/../referencias';
for(const[n,u]of R){try{const p=await b.newPage({viewport:{width:1440,height:900}});await p.goto(u,{timeout:25000,waitUntil:'domcontentloaded'});await p.waitForTimeout(3500);
await p.screenshot({path:`${O}/${n}-1.jpg`,type:'jpeg',quality:70});await p.mouse.wheel(0,1400);await p.waitForTimeout(1500);await p.screenshot({path:`${O}/${n}-2.jpg`,type:'jpeg',quality:70});console.log('ok',n);await p.close()}catch(e){console.log('falhou',n,e.message.slice(0,80))}}
await b.close()})();
