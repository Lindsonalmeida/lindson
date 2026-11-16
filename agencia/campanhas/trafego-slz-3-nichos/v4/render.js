const {chromium}=require('playwright');const J=require(process.argv[2]);
(async()=>{const b=await chromium.launch();for(const [t,H,o] of J){const p=await b.newPage({viewport:{width:1080,height:H}});await p.goto('file://'+t);await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);await p.screenshot({path:o,type:'jpeg',quality:88});await p.close()}await b.close()})();
