const { chromium } = require('playwright');
const out='/home/user/lindson/agencia/operacao-propria/youtube/pesquisa/';
const L=[['ooni','https://www.youtube.com/@ooni'],['gozney','https://www.youtube.com/@Gozney'],['vito','https://www.youtube.com/@vitoiacopelli'],['toast','https://www.youtube.com/@ToastTab'],['restaurantboss','https://www.youtube.com/@TheRestaurantBoss'],['sebrae','https://www.youtube.com/@sebrae'],['mrbeastburger','https://www.youtube.com/@MrBeastBurger'],['dominos','https://www.youtube.com/@Dominos'],['pizzahutbr','https://www.youtube.com/@PizzaHutBrasil'],['50toppizza','https://www.youtube.com/@50toppizza'],['ifood','https://www.youtube.com/@iFood']];
(async()=>{const b=await chromium.launch();const c=await b.newContext({viewport:{width:1440,height:1000},locale:'pt-BR'});
await c.addCookies([{name:'SOCS',value:'CAI',domain:'.youtube.com',path:'/'}]);
for(const [n,u] of L){try{const p=await c.newPage();await p.goto(u,{timeout:30000,waitUntil:'domcontentloaded'});await p.waitForTimeout(5000);await p.screenshot({path:out+n+'.jpg',type:'jpeg',quality:80});console.log('ok',n,await p.title());await p.close()}catch(e){console.log('erro',n,e.message.slice(0,80))}}
await b.close()})();
