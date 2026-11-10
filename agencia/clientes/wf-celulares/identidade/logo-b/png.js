// SVG do logo B -> PNG transparente 2000 px (conta Leandro, 10/11/2026)
const { chromium } = require('playwright'); const fs=require('fs'), path=require('path');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1000,height:1200},deviceScaleFactor:2});
for(const f of fs.readdirSync(__dirname).filter(f=>f.endsWith('.svg'))){
 await p.setContent(`<html><head><link href="https://fonts.googleapis.com/css2?family=Inter:wght@500&display=swap" rel="stylesheet"><style>body{margin:0;background:transparent}svg{width:1000px;height:1200px;display:block}</style></head><body>${fs.readFileSync(path.join(__dirname,f),'utf8')}</body></html>`,{waitUntil:'networkidle'});
 await p.evaluate(()=>document.fonts.ready);await p.locator('svg').screenshot({path:path.join(__dirname,f.replace('.svg','.png')),omitBackground:true});}
await b.close()})();
