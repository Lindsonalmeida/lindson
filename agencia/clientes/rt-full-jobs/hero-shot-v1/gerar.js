// node gerar.js pecas.json -> cria cena (cena.py) e renderiza 4:5 e 9:16 de cada peça. Conta Zuleide, 16/11/2026.
const {chromium}=require('playwright');const fs=require('fs');const {execFileSync}=require('child_process');
const L=JSON.parse(fs.readFileSync(process.argv[2]||__dirname+'/pecas.json'));const only=process.argv[3];
(async()=>{const b=await chromium.launch({args:['--allow-file-access-from-files']});fs.mkdirSync(__dirname+'/saida',{recursive:true});fs.mkdirSync(__dirname+'/cenas',{recursive:true});
for(const d of L){for(const [fmt,H,ph,yb] of [['4x5',1350,560,1020],['9x16',1920,620,1430]]){if(only&&only!==fmt)continue;
 const bg=`cenas/${d.slug}-${d.cena}-${fmt}.png`;execFileSync('python3',[__dirname+'/cena.py',__dirname+'/'+d.recorte,__dirname+'/'+bg,'1080',''+H,d.cena,''+(d.ph?.[fmt]||ph),''+yb]);
 const p=await b.newPage({viewport:{width:1080,height:H},deviceScaleFactor:1});
 await p.goto('file://'+__dirname+'/peca.html?h='+H+'&d='+encodeURIComponent(JSON.stringify({...d,bg})),{waitUntil:'networkidle'});await p.waitForFunction('window.pronto===true');
 await p.screenshot({path:`${__dirname}/saida/${d.slug}-${d.cena}-${fmt}.jpg`,type:'jpeg',quality:92});await p.close()}}
await b.close()})();
