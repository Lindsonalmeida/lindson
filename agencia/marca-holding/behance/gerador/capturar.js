// Pesquisa premium Behance Barzakh (conta Zuleide, 18/11/2026): captura as referências.
const { chromium } = require('playwright');
const refs = [
 ['15-behance-anagrama','https://www.behance.net/anagrama'],['16-behance-bratus','https://www.behance.net/bratus'],['17-behance-atipus','https://www.behance.net/atipus'],['18-behance-search-featured','https://www.behance.net/search/projects/brand%20identity?sort=featured'],['19-behance-mubien','https://www.behance.net/mubien'],
];
(async()=>{
 const b = await chromium.launch(); const p = await b.newPage({viewport:{width:1440,height:1100}, userAgent:'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36'});
 for (const [n,u] of refs){ try{ await p.goto(u,{waitUntil:'domcontentloaded',timeout:30000}); await p.waitForTimeout(4500);
   await p.screenshot({path:`pesquisa/${n}.png`}); console.log('ok',n, (await p.title()).slice(0,60)); }catch(e){console.log('erro',n,e.message.slice(0,80));} }
 await b.close(); })();
