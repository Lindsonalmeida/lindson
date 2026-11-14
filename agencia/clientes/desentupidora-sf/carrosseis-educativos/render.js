// Tira cada tela (1080x1350) do carrosseis.html em JPG: out/<carrossel>/01.jpg ...
const {chromium}=require('playwright');const fs=require('fs');const path=require('path');
(async()=>{const d=__dirname;const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1350},deviceScaleFactor:1});
await p.goto('file://'+d+'/carrosseis.html',{waitUntil:'networkidle'});await p.evaluate(()=>document.fonts.ready);
const ss=await p.$$('section');const cnt={};
for(const s of ss){const c=await s.getAttribute('data-c');cnt[c]=(cnt[c]||0)+1;const dir=path.join(d,'out',c);fs.mkdirSync(dir,{recursive:true});
await s.screenshot({path:path.join(dir,String(cnt[c]).padStart(2,'0')+'.jpg'),type:'jpeg',quality:92});}
await b.close();console.log(cnt)})();
