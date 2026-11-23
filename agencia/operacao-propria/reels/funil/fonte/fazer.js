const {chromium}=require('playwright');const fs=require('fs');
const [cfgf,dir]=process.argv.slice(2);const C=JSON.parse(fs.readFileSync(cfgf));
(async()=>{fs.mkdirSync(dir,{recursive:true});const b=await chromium.launch({executablePath:process.env.CH});const p=await b.newPage({viewport:{width:1080,height:1920}});
p.on('pageerror',e=>{console.log('ERRO',e.message);process.exit(1)});
await p.goto('file://'+__dirname+'/turbo.html');await p.waitForFunction('window.PRONTO');await p.evaluate(C=>setup(C),C);
const n=Math.round(C.dur*30);for(let i=0;i<n;i++){await p.evaluate(t=>render(t),i/30);await p.screenshot({path:dir+'/'+String(i).padStart(4,'0')+'.jpg',type:'jpeg',quality:88})}
await b.close()})();
