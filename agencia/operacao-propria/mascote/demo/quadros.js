// Quadros do vídeo: node quadros.js tl.json pasta [--alfa]  (conta Pedro, 15/11/2026)
// --alfa: fundo transparente (só o boneco) para sobrepor no motor de Reels.
const {chromium}=require('playwright');const fs=require('fs');const path=require('path');
const [tl,dir]=process.argv.slice(2);const alfa=process.argv.includes('--alfa');const TL=JSON.parse(fs.readFileSync(tl));
(async()=>{fs.mkdirSync(dir,{recursive:true});const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
p.on('pageerror',e=>{console.log('ERRO',e.message);process.exit(1)});
await p.goto('file://'+path.join(__dirname,'cena.html'));await p.waitForFunction('window.PRONTO');
await p.evaluate(({TL,alfa})=>{window.TL=TL;if(alfa){document.querySelectorAll('#c>*:not(#st)').forEach(e=>e.style.display='none');document.getElementById('c').style.background='transparent';document.body.style.background='transparent'}},{TL,alfa});
const n=Math.round(TL.dur*30);for(let i=0;i<n;i++){await p.evaluate(t=>render(t),i/30);await p.screenshot({path:path.join(dir,String(i).padStart(5,'0')+'.png'),omitBackground:alfa})}
await b.close()})();
