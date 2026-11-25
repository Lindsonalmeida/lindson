const {chromium}=require('playwright');const path=require('path');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1100,height:2000}});
await p.goto('file://'+path.join(__dirname,'grupo.html'));await p.waitForLoadState('networkidle');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(800);
for(const m of ['guia','limpo']){await p.evaluate(x=>document.body.classList.toggle('limpo',x==='limpo'),m);
for(const id of ['grupo-feed','grupo-story','grupo-perfil'])await p.locator('#'+id).screenshot({path:path.join(process.argv[2],id+(id==='grupo-story'?'-'+m:'')+'.jpg'),type:'jpeg',quality:93});}
await b.close()})();
