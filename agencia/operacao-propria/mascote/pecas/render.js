// Renderiza as peças do Seu Turbo: node pecas/render.js [modo...]  (conta Pedro, 15/11/2026)
const {chromium}=require('playwright');const path=require('path');const fs=require('fs');
const modos=process.argv.slice(2).length?process.argv.slice(2):['principal','expressoes','poses','folha','reel','post','direcoes'];
const transp=['principal','expressoes','poses'];
(async()=>{const b=await chromium.launch();fs.mkdirSync(path.join(__dirname,'png'),{recursive:true});
for(const m of modos){const p=await b.newPage();p.on('pageerror',e=>console.log('ERRO',m,e.message));
 await p.goto('file://'+path.join(__dirname,'palco.html')+'?modo='+m);await p.waitForFunction('window.PRONTO');await p.waitForTimeout(300);
 const box=await p.$('#cena');await box.screenshot({path:path.join(__dirname,'png',m+'.png'),omitBackground:transp.includes(m)});
 if(m==='principal'){const svg=await p.$eval('svg.st',s=>{const c=s.cloneNode(true);c.setAttribute('xmlns','http://www.w3.org/2000/svg');c.removeAttribute('class');c.removeAttribute('style');c.setAttribute('width','600');c.setAttribute('height','900');return c.outerHTML});fs.writeFileSync(path.join(__dirname,'..','seu-turbo.svg'),'<?xml version="1.0" encoding="UTF-8"?>\n<!-- Seu Turbo, mascote da Orégano Turbo (conta Pedro, 15/11/2026). Cada parte é um <g id="st-..."> -->\n'+svg)}
 console.log('ok',m);await p.close()}
await b.close()})();
