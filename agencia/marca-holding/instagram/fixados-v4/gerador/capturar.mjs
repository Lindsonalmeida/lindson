import { chromium } from 'playwright';
const sites=[
['01-aesop-au','https://www.aesop.com/'],
['02-snohetta-no','https://www.snohetta.com/'],
['03-bureauborsche-de','https://www.bureauborsche.com/'],
['04-kinfolk-dk','https://www.kinfolk.com/'],
['05-loropiana-it','https://www.loropiana.com/en/'],
['06-pentagram-uk','https://www.pentagram.com/work'],
['07-landor-us','https://landor.com/'],
['08-studiofaculty-nl','https://www.thisisfaculty.com/'],
['09-johnpawson-uk','https://www.johnpawson.com/'],
['10-fabrica-br','https://www.instagram.com/barzakhstudio/'],
];
const b=await chromium.launch();
for(const [n,u] of sites){const p=await b.newPage({viewport:{width:1440,height:1800}});
try{await p.goto(u,{timeout:30000,waitUntil:'domcontentloaded'});await p.waitForTimeout(4000);await p.screenshot({path:`../referencias/${n}.jpg`,quality:80,type:'jpeg'});console.log('ok',n)}catch(e){console.log('erro',n,e.message.slice(0,80))}await p.close()}
await b.close();
