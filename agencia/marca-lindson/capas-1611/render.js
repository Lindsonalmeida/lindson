const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
for(const a of ['reel','h1','h2','h3','h4','h5','h6','h7','h8']){await p.goto('file://'+process.cwd()+'/capas.html?a='+a);await p.waitForFunction('window.pronto',{timeout:30000});await p.screenshot({path:'out-'+a+'.png'})}await b.close()})();
