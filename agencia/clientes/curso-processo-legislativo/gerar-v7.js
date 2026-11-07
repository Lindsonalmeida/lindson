const fs=require('fs');
const b64="data:image/jpeg;base64,"+fs.readFileSync("fotos-banco/martelo-pexels-5668473.jpg").toString("base64");
const CSS=`*{box-sizing:border-box;margin:0;padding:0}
.c{width:1080px;height:1920px;position:relative;overflow:hidden;color:#F3E9D7;font-family:Inter,Arial,sans-serif;background:radial-gradient(900px 700px at 70% 0%,#4a3420 0%,#1c130b 55%,#0d0805 100%)}
.wood{position:absolute;inset:0;background:repeating-linear-gradient(92deg,rgba(255,220,160,.03) 0 2px,transparent 2px 46px)}
.ph{position:absolute;left:0;right:0;top:0;height:1160px;background-image:url(${b64});background-size:cover;background-repeat:no-repeat;-webkit-mask-image:linear-gradient(180deg,#000 55%,transparent 100%);mask-image:linear-gradient(180deg,#000 55%,transparent 100%);opacity:.9}
.serif{position:absolute;left:80px;right:80px;font-family:"Liberation Serif","Times New Roman",serif;font-weight:700;letter-spacing:-.01em;line-height:1}
.gold{color:#D9BC78}
.top{position:absolute;left:80px;right:80px;top:80px;display:flex;justify-content:space-between;align-items:center}
.brand{font-family:"Liberation Serif",serif;font-size:44px;font-weight:700}
.brand i{color:#D9BC78;font-weight:400}
.tag{font-size:22px;letter-spacing:.2em;text-transform:uppercase;color:#D9BC78;border:2px solid #D9BC78;padding:10px 16px}
.card{position:absolute;left:80px;right:80px;bottom:150px;padding:48px 52px;border:2px solid rgba(217,188,120,.55);background:rgba(20,14,9,.72);border-radius:6px}
.chip{display:inline-block;margin:0 12px 12px 0;padding:12px 22px;border:1.5px solid #D9BC78;border-radius:999px;color:#E9D7A8;font-size:26px;letter-spacing:.06em;text-transform:uppercase}
.cta{position:absolute;left:80px;right:80px;bottom:60px;height:90px;background:#D9BC78;color:#1c130b;display:flex;align-items:center;justify-content:center;font-size:30px;font-weight:700;letter-spacing:.08em;text-transform:uppercase}
.slot{position:absolute;right:80px;top:300px;width:420px;height:560px;border:2px dashed rgba(217,188,120,.7);display:flex;align-items:center;justify-content:center;text-align:center;color:#D9BC78;font-size:24px;letter-spacing:.08em;text-transform:uppercase;padding:30px;background:rgba(0,0,0,.25)}
.sub{position:absolute;left:80px;right:80px;font-size:38px;line-height:1.35;color:rgba(243,233,215,.9)}`;
const top=(n)=>`<div class="top"><div class="brand">Processo <i>Legislativo</i></div><div class="tag">Curso ${n}</div></div>`;
const C=[
["capa-v7-01-justica", `<div class="wood"></div><div class="ph"></div>${top("básico")}
 <div class="slot">Espaço do instrutor<br><br>(foto recortada, aguardando)</div>
 <div class="serif" style="top:880px;font-size:150px">Quórum com <span class="gold" style="font-style:italic;font-weight:400">excelência.</span></div>
 <div class="sub" style="top:1130px">Entenda a regra antes de votar, sem jargão.</div>
 <div class="card"><span class="chip">Quórum</span><span class="chip">Sessão</span><span class="chip">Regimento</span><div style="font-size:30px;color:rgba(243,233,215,.85)">Para vereadores, assessores e servidores da câmara.</div></div>
 <div class="cta">Assista ao curso básico</div>`],
["capa-v7-02-pode", `<div class="wood"></div><div class="ph" style="background-position:30% 60%"></div>${top("pode votar")}
 <div class="serif" style="top:800px;font-size:160px">Pode votar <span class="gold" style="font-style:italic;font-weight:400">sem</span> quórum?</div>
 <div class="sub" style="top:1100px">A regra da sessão que todo vereador precisa dominar.</div>
 <div class="card"><span class="chip">Votação</span><span class="chip">Regra</span><span class="chip">Sessão</span><div style="font-size:30px;color:rgba(243,233,215,.85)">Estudo da regra, sem promessa de resultado.</div></div>
 <div class="cta">Saiba a regra antes da sessão</div>`]];
const html=(b)=>`<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>${CSS}</style></head><body style="margin:0"><section class="c">${b}</section></body></html>`;
const { chromium } = require('playwright');
const path = require('path');
const dir = process.cwd();
(async()=>{const br=await chromium.launch({args:['--no-sandbox']});const p=await br.newPage({viewport:{width:1080,height:1920},deviceScaleFactor:1});
for(const [n,b] of C){await p.setContent(html(b),{waitUntil:'load'});await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);await (await p.$('section')).screenshot({path:path.join(dir,'capas-v7',n+'.png')});}
await br.close();console.log('ok',C.length);})().catch(e=>{console.error(e.message);process.exit(1);});
