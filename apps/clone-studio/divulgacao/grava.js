// grava cada story quadro a quadro: node grava.js <cena> <duração s> <fps> <pasta>
const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const [c,dur,fps,dir]=process.argv.slice(2);fs.mkdirSync(dir,{recursive:true});
const b=await chromium.launch({proxy:{server:process.env.HTTPS_PROXY}});const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.goto('file://'+__dirname+`/story.html?c=${c}&dur=${dur}`);await p.waitForFunction('window.pronto===true');await p.waitForTimeout(500);
const n=Math.round(dur*fps);for(let i=0;i<n;i++){await p.evaluate(t=>desenha(t),i/fps);await p.screenshot({path:`${dir}/${String(i).padStart(4,'0')}.png`});}
console.log('cena',c,n,'quadros');await b.close()})();
