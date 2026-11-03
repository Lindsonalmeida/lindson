// node grava_video.js <fps> <pasta> [t1,t2,... só esses tempos]
const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const [fps,dir,lista]=process.argv.slice(2);fs.mkdirSync(dir,{recursive:true});
const b=await chromium.launch({proxy:{server:process.env.HTTPS_PROXY},args:['--allow-file-access-from-files']});
const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.goto('file://'+__dirname+'/video.html');await p.waitForFunction('window.pronto===true');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(600);
const ts=lista?lista.split(',').map(Number):Array.from({length:30*fps},(_,i)=>i/fps);
for(const [i,t] of ts.entries()){await p.evaluate(t=>desenha(t),t);await p.screenshot({path:`${dir}/${String(i).padStart(5,'0')}.png`});if(i%150===0)console.log(i,'/',ts.length);}
await b.close()})();
