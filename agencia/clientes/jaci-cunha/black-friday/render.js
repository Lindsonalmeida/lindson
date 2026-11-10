// Black Friday Jaci: renderiza os 8 stories (guia com figurinhas marcadas e limpo) e versões 4:5 (conta Pedro, 10/11/2026)
const {chromium}=require('playwright');const path=require('path');const fs=require('fs');
const out=process.argv[2]||path.join(__dirname,'out');fs.mkdirSync(out,{recursive:true});
(async()=>{const b=await chromium.launch({proxy:process.env.HTTPS_PROXY?{server:process.env.HTTPS_PROXY}:undefined});const p=await b.newPage({viewport:{width:1100,height:2000},ignoreHTTPSErrors:true});
await p.goto('file://'+path.join(__dirname,'stories.html'));await p.waitForLoadState('networkidle');await p.evaluate(()=>document.fonts.ready);
for(const modo of ['guia','limpo']){await p.evaluate(m=>document.body.classList.toggle('limpo',m==='limpo'),modo);
for(let i=1;i<=8;i++){await p.locator('#s'+i).screenshot({path:`${out}/story${i}-${modo}.png`});}}
await b.close();console.log('ok')})();
