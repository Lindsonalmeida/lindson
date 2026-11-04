// Renderiza artes.html em 2x (2160x3840 Reels, 2160x2700 posts). node render.js (conta Leandro)
const {chromium}=require('playwright');const path=require('path');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1100,height:2000},deviceScaleFactor:2});
await p.goto('file://'+path.join(__dirname,'artes.html'));await p.waitForLoadState('networkidle');await p.evaluate(()=>document.fonts.ready);
for(const id of await p.$$eval('section.f',s=>s.map(x=>x.id))){const fil=process.argv[2];if(fil&&!fil.split(',').includes(id))continue;
await p.locator('#'+id).screenshot({path:path.join(__dirname,process.env.FEED?'feed':'artes',id+'.jpg'),type:'jpeg',quality:93});console.log(id);}
await b.close()})();
