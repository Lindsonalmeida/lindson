// Capturas 390x844 @2x + OG + ícone (conta Leandro, 10/11/2026). Uso: node capturar.js
const { chromium } = require('playwright'); const path=require('path');
const url='file://'+path.join(__dirname,'index.html');
(async()=>{const b=await chromium.launch();
const p=await b.newPage({viewport:{width:390,height:844},deviceScaleFactor:2});await p.goto(url);await p.waitForTimeout(2500);
await p.screenshot({path:'capturas/celular-topo.png'});
await p.evaluate(()=>document.querySelectorAll('.sobe').forEach(x=>x.classList.add('on')));await p.waitForTimeout(900);
await p.screenshot({path:'capturas/celular-pagina-inteira.png',fullPage:true});
console.log('largura',await p.evaluate(()=>[document.documentElement.scrollWidth,innerWidth]));
const o=await b.newPage({viewport:{width:1200,height:630}});
const fs=require('fs');fs.writeFileSync(path.join(__dirname,'_og.html'),`<html><head><link href="https://fonts.googleapis.com/css2?family=Inter:wght@200;300&display=swap" rel="stylesheet"></head><body style="margin:0;width:1200px;height:630px;background:#000 url('file://${path.join(__dirname,'img/hero.webp')}') right -40px center/560px auto no-repeat;font-family:Inter;color:#F5F5F7;position:relative"><div style="position:absolute;inset:0;background:linear-gradient(90deg,#000 45%,transparent 80%)"></div><img src="file://${path.join(__dirname,'img/logo.svg')}" style="position:absolute;left:80px;top:70px;height:150px"><div style="position:absolute;left:80px;top:270px;font:200 84px/1 Inter;letter-spacing:-.05em">Celular com<br><span style="background:linear-gradient(120deg,#f6f4f0,#bdb8b0 30%,#7a756e 55%,#e2ded7 78%,#8d887f);-webkit-background-clip:text;color:transparent">procedência.</span></div><div style="position:absolute;left:80px;top:470px;font:300 26px Inter;color:#C7C9CC">Laudo WF · garantia · Pix ou até 18x · São Luís</div><div style="position:absolute;right:24px;bottom:16px;font:13px Inter;color:#6e6e73">Imagem ilustrativa · Apple Newsroom</div></body></html>`);await o.goto('file://'+path.join(__dirname,'_og.html'));
await o.waitForTimeout(2000);await o.screenshot({path:'img/og.jpg',type:'jpeg',quality:82});
const i=await b.newPage({viewport:{width:180,height:180}});
fs.writeFileSync(path.join(__dirname,'_ic.html'),`<body style="margin:0;background:#000"><img src="file://${path.join(__dirname,'img/logo.svg')}" style="display:block;margin:22px auto;height:136px"></body>`);await i.goto('file://'+path.join(__dirname,'_ic.html'));await i.waitForTimeout(500);await i.screenshot({path:'img/apple-touch-icon.png'});
fs.unlinkSync(path.join(__dirname,'_og.html'));fs.unlinkSync(path.join(__dirname,'_ic.html'));await b.close()})();
