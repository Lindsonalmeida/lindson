// Renderiza cada SVG em PNG transparente (largura alvo) e monta uma folha de conferência.
const {chromium}=require('playwright');const fs=require('fs');const path=require('path');
(async()=>{const d=path.join(__dirname,'arquivos');const svgs=JSON.parse(fs.readFileSync(d+'/lista.json'));
fs.mkdirSync(d+'/png',{recursive:true});const b=await chromium.launch();const p=await b.newPage();
for(const n of svgs){const s=fs.readFileSync(`${d}/svg/${n}.svg`,'utf8');const m=s.match(/viewBox="0 0 ([\d.]+) ([\d.]+)"/);
 const w=+m[1],h=+m[2];const target=n==='favicon'?512:(n.startsWith('horizontal')?3000:2000);const sc=target/w;
 await p.setViewportSize({width:Math.ceil(w),height:Math.ceil(h)});
 await p.setContent(`<html><body style="margin:0;background:transparent">${s}</body></html>`);
 await p.screenshot({path:`${d}/png/${n}.png`,omitBackground:true,clip:{x:0,y:0,width:w,height:h},scale:'device'}).catch(()=>{});
 const p2=await b.newPage({viewport:{width:Math.ceil(w),height:Math.ceil(h)},deviceScaleFactor:sc});
 await p2.setContent(`<html><body style="margin:0;background:transparent">${s}</body></html>`);
 await p2.screenshot({path:`${d}/png/${n}.png`,omitBackground:true,clip:{x:0,y:0,width:w,height:h}});await p2.close();}
await b.close();console.log('ok',svgs.length)})();
