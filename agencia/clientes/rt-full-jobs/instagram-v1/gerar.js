// node gerar.js -> artes/feed-01..08.png (1080x1350) e artes/story-01..03.png (1080x1920) (conta Pedro, 03/11/2026)
const {chromium}=require('playwright');const fs=require('fs');
(async()=>{fs.mkdirSync(__dirname+'/artes',{recursive:true});
const b=await chromium.launch({proxy:process.env.HTTPS_PROXY?{server:process.env.HTTPS_PROXY}:undefined,args:['--allow-file-access-from-files']});
const nomes=['','kit-cinema','estudio-verde','conteudo-mensal','bastidor','depoimento','kit-luz','kit-completo','producoes'];
for(let i=1;i<=8;i++){const p=await b.newPage({viewport:{width:1080,height:1350}});await p.goto('file://'+__dirname+'/modelos.html?m='+i);await p.waitForFunction('window.pronto===true');await p.waitForTimeout(400);
 await p.screenshot({path:`${__dirname}/artes/feed-0${i}-${nomes[i]}.png`});await p.close();}
const sn=['','agenda-aberta','estudio','depoimento'];
for(let i=1;i<=3;i++){const p=await b.newPage({viewport:{width:1080,height:1920}});await p.goto('file://'+__dirname+'/modelos.html?s='+i);await p.waitForFunction('window.pronto===true');await p.waitForTimeout(400);
 await p.screenshot({path:`${__dirname}/artes/story-0${i}-${sn[i]}.png`});await p.close();}
await b.close();console.log('ok')})();
