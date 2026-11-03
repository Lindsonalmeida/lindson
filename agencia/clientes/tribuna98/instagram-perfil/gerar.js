// Gera as capas 2160x3840 (2x). node gerar.js  (conta Leandro)
const {chromium}=require('playwright');const path=require('path');
const L=[['01-noticias','noticias','Notícias','Maranhão e Brasil'],['02-bastidores','bastidores','Bastidores','O que não aparece'],['03-entrevistas','entrevistas','Entrevistas','Quem decide fala'],
['04-fiscaliza','fiscaliza','Fiscaliza','De olho no dinheiro'],['05-eleicoes','eleicoes','Eleições','Cobertura completa'],['06-anuncie','anuncie','Anuncie','Sua marca aqui'],['07-contato','contato','Contato','Mande sua pauta']];
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920},deviceScaleFactor:2});
await p.goto('file://'+path.join(__dirname,'destaques.html'));await p.waitForLoadState('networkidle');await p.evaluate(()=>document.fonts.ready);
for(const [n,ic,t,r] of L){await p.evaluate(d=>monta(d),{ic,t,r});await p.waitForTimeout(150);await p.locator('#c').screenshot({path:path.join(__dirname,`capa-${n}.jpg`),type:'jpeg',quality:94});console.log(n);}
await b.close()})();
