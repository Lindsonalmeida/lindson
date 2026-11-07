const fs=require('fs');const path=require('path');
const dir='/home/user/lindson/agencia/clientes/curso-processo-legislativo';
const b64=(f)=>'data:image/jpeg;base64,'+fs.readFileSync(path.join(dir,'fotos-banco/diversas',f)).toString('base64');
const BASE=`*{box-sizing:border-box;margin:0;padding:0}.c{width:1080px;height:1920px;position:relative;overflow:hidden;font-family:Inter,Arial,sans-serif}
.abs{position:absolute}.serif{font-family:"Liberation Serif","Times New Roman",serif;font-weight:700;line-height:1}
.tag{font-size:22px;letter-spacing:.2em;text-transform:uppercase;border:2px solid currentColor;padding:10px 16px}
.cta{position:absolute;left:80px;right:80px;bottom:70px;height:96px;display:flex;align-items:center;justify-content:center;font-size:30px;font-weight:700;letter-spacing:.08em;text-transform:uppercase}
.gold{color:#D9BC78}`;
const C=[
// 1: microfone, meia-tela, verde escuro embaixo
['capa-v8-01-microfone', `<div class="c" style="background:#00241C;color:#F3E9D7">
 <div class="abs" style="left:0;right:0;top:0;height:1040px;background:url(${b64('microfones.jpg')}) 50% 50%/cover"></div>
 <div class="abs" style="left:0;right:0;top:0;height:1040px;background:linear-gradient(180deg,rgba(0,36,28,0) 40%,#00241C 100%)"></div>
 <div class="abs" style="left:80px;top:80px;font-size:36px;font-weight:900;text-transform:uppercase;color:#FCFCFC">Processo Legislativo</div>
 <div class="abs tag gold" style="right:80px;top:80px">Curso básico</div>
 <div class="abs serif" style="left:80px;right:80px;top:1110px;font-size:170px">Quórum <span class="gold" style="font-style:italic;font-weight:400">é o</span> mínimo.</div>
 <div class="abs" style="left:80px;right:80px;top:1420px;font-size:38px;line-height:1.35;color:rgba(243,233,215,.9)">Para a votação valer, é preciso estar em número. Entenda como se conta.</div>
 <div class="cta" style="background:#D9BC78;color:#00241C">Veja a regra do quórum</div></div>`],
// 2: mãos em tablets, claro e editorial
['capa-v8-02-tablet', `<div class="c" style="background:#F3E9D7;color:#00241C">
 <div class="abs" style="left:80px;top:80px;font-size:36px;font-weight:900;text-transform:uppercase">Processo Legislativo</div>
 <div class="abs tag" style="right:80px;top:80px">Nº 02</div>
 <div class="abs" style="left:80px;right:80px;top:200px;height:820px;background:url(${b64('tablet-reuniao.jpg')}) 40% 50%/cover"></div>
 <div class="abs serif" style="left:80px;right:80px;top:1080px;font-size:160px">Quem pode <span style="color:#8E6B2E;font-style:italic;font-weight:400">propor</span>?</div>
 <div class="abs" style="left:80px;right:80px;top:1320px;font-size:38px;line-height:1.35">Veja quem tem a iniciativa de um projeto de lei e como ele começa a tramitar.</div>
 <div class="cta" style="background:#00241C;color:#F3E9D7">Assista à aula</div></div>`],
// 3: púlpito, cartão escuro sobre a imagem inteira
['capa-v8-03-podio', `<div class="c" style="background:#1c130b;color:#F3E9D7">
 <div class="abs" style="inset:0;background:url(${b64('podio.jpg')}) 50% 50%/cover;opacity:.55"></div>
 <div class="abs" style="inset:0;background:linear-gradient(180deg,rgba(28,19,11,.2),rgba(28,19,11,.95) 70%)"></div>
 <div class="abs" style="left:80px;top:80px;font-size:36px;font-weight:900;text-transform:uppercase">Processo Legislativo</div>
 <div class="abs" style="left:80px;right:80px;top:560px;border:2px solid rgba(217,188,120,.6);background:rgba(20,14,9,.7);padding:70px 60px">
   <div class="gold" style="font-size:24px;letter-spacing:.2em;text-transform:uppercase">Sessão</div>
   <div class="serif" style="font-size:150px;margin-top:20px">Sessão <span class="gold" style="font-style:italic;font-weight:400">secreta</span> pode acontecer?</div>
   <div style="font-size:36px;line-height:1.35;margin-top:40px;color:rgba(243,233,215,.88)">Veja o que o regimento permite, e o que não permite.</div></div>
 <div class="cta" style="background:#D9BC78;color:#1c130b">Aprenda o regimento</div></div>`],
// 4: plenário vermelho, faixa dourada e título gigante
['capa-v8-04-plenario', `<div class="c" style="background:#00241C;color:#FCFCFC">
 <div class="abs" style="left:0;right:0;top:0;height:720px;background:url(${b64('fileiras-publico.jpg')}) 50% 50%/cover"></div>
 <div class="abs" style="left:0;right:0;top:700px;height:14px;background:#D9BC78"></div>
 <div class="abs" style="left:80px;top:80px;font-size:36px;font-weight:900;text-transform:uppercase;color:#FCFCFC">Processo Legislativo</div>
 <div class="abs" style="left:80px;right:80px;top:820px;font-size:24px;letter-spacing:.2em;text-transform:uppercase;color:#D9BC78">Votação · plenário</div>
 <div class="abs" style="left:80px;right:80px;top:880px;font-weight:900;font-size:210px;letter-spacing:-.05em;line-height:.84;text-transform:uppercase">Pode<br>votar</div>
 <div class="abs" style="left:80px;right:80px;top:1270px;font-weight:900;font-size:130px;letter-spacing:-.04em;line-height:.84;text-transform:uppercase;color:#D9BC78">sem quórum?</div>
 <div class="abs" style="left:80px;right:80px;top:1480px;font-size:36px;line-height:1.35;color:rgba(252,252,252,.85)">A regra da sessão que todo servidor e vereador precisa dominar.</div>
 <div class="cta" style="background:#FCFCFC;color:#00241C">Entenda a regra</div></div>`],
];
const { chromium } = require('playwright');
(async()=>{const br=await chromium.launch({args:['--no-sandbox']});const p=await br.newPage({viewport:{width:1080,height:1920},deviceScaleFactor:1});
for(const [n,h] of C){await p.setContent(`<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>${BASE}</style></head><body style="margin:0">${h}</body></html>`,{waitUntil:'load'});await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);await (await p.$('.c')).screenshot({path:path.join(dir,'capas-v8',n+'.png')});}
await br.close();console.log('ok',C.length);})().catch(e=>{console.error(e.message);process.exit(1);});
