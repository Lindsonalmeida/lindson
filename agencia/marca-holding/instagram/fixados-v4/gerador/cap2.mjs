import { chromium } from '/opt/node-tools/node_modules/playwright/index.mjs';
const sites=[['11-vitra-ch','https://www.vitra.com/en-int/magazine'],['12-commonplace-jp','https://www.claska.com/'],['13-jilsander-de','https://www.jilsander.com/'],['14-hermes-fr','https://www.hermes.com/us/en/'],['15-koto-uk','https://koto.studio/'],['16-mucca-us','https://www.mucca.com/']];
const b=await chromium.launch();
for(const [n,u] of sites){const p=await b.newPage({viewport:{width:1440,height:1800}});
try{await p.goto(u,{timeout:30000,waitUntil:'domcontentloaded'});await p.waitForTimeout(5000);await p.screenshot({path:`../referencias/${n}.jpg`,quality:80,type:'jpeg'});console.log('ok',n)}catch(e){console.log('erro',n)}await p.close()}
await b.close();
