// node render.js <4x5|9x16> <pasta_frames> : quadros do vídeo hero shot (conta Zuleide, 16/11/2026)
const {chromium}=require('playwright');const fs=require('fs');const fmt=process.argv[2],out=process.argv[3];fs.mkdirSync(out,{recursive:true});
const H=fmt==='4x5'?1350:1920,[ph,yb]=fmt==='4x5'?[560,1020]:[620,1430];
const d={...JSON.parse(fs.readFileSync(__dirname+'/../pecas.json'))[0],bg:`../cenas/f-${fmt}.png`,recorte:'../../instagram-v2/recortes/metabones.png',ph,yb};
(async()=>{const b=await chromium.launch({args:['--allow-file-access-from-files']});const p=await b.newPage({viewport:{width:1080,height:H}});
await p.goto('file://'+__dirname+'/video.html?h='+H+'&d='+encodeURIComponent(JSON.stringify(d)),{waitUntil:'networkidle'});await p.waitForFunction('window.pronto===true');
const N=+(process.argv[4]||210);for(let i=0;i<N;i++){await p.evaluate(t=>render(t),i/30);await p.screenshot({path:`${out}/${String(i).padStart(4,'0')}.jpg`,type:'jpeg',quality:90})}await b.close()})();
