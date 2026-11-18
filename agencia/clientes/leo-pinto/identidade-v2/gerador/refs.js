const { chromium } = require('playwright');
const L=[
['02-obama-2008-sendermatic-us','https://en.wikipedia.org/wiki/Barack_Obama_2008_presidential_campaign'],['03-aoc-2018-tandem-us','https://en.wikipedia.org/wiki/2018_New_York%27s_14th_congressional_district_election'],['05-porto-whitestudio-pt','https://www.behance.net/search/projects/porto%20city%20identity'],['07-campanha-politica-behance-br','https://www.behance.net/search/projects/campanha%20pol%C3%ADtica%20identidade'],['08-political-branding-behance','https://www.behance.net/search/projects/political%20campaign%20branding'],['15-rolex-ch','https://en.wikipedia.org/wiki/Rolex'],['16-tom-ford-us','https://en.wikipedia.org/wiki/Tom_Ford_(brand)'],['18-ralph-lauren-us','https://en.wikipedia.org/wiki/Ralph_Lauren_Corporation'],['19-luxury-menswear-behance','https://www.behance.net/search/projects/luxury%20menswear%20brand%20identity'],['20-sinek-macron-2017-fr','https://en.wikipedia.org/wiki/Emmanuel_Macron_2017_presidential_campaign'],
];const L0=[
['01-obama-hope-us','https://en.wikipedia.org/wiki/Barack_Obama_%22Hope%22_poster'],
['02-obama-identity-sendermatic-us','https://www.fastcompany.com/90165578/the-story-behind-obamas-iconic-logo'],
['03-aoc-tandem-us','https://www.tandemdesign.co/aoc'],
['04-macron-en-marche-fr','https://en.wikipedia.org/wiki/La_R%C3%A9publique_En_Marche!'],
['05-porto-whitestudio-pt','https://www.whitestudio.pt/work/porto'],
['06-pentagram-stuttgart-de','https://www.pentagram.com/work'],
['07-kamala-harris-wideeye-us','https://www.underconsideration.com/brandnew/archives/new_logo_and_identity_for_kamala_harris_presidential_campaign.php'],
['08-hermes-fr','https://www.hermes.com/us/en/'],
['09-loropiana-it','https://us.loropiana.com/en/'],
['10-bottega-veneta-it','https://www.bottegaveneta.com/en-us'],
['11-mayor-london-uk','https://www.london.gov.uk/'],
['12-lula-2022-br','https://pt.wikipedia.org/wiki/Campanha_presidencial_de_Lula_em_2022'],
['13-buenos-aires-ar','https://buenosaires.gob.ar/'],
['14-collins-work-us','https://www.wearecollins.com/work/'],
];
(async()=>{const b=await chromium.launch();const c=await b.newContext({viewport:{width:1440,height:900},userAgent:'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/124 Safari/537.36'});
for(const [n,u] of L){const p=await c.newPage();try{await p.goto(u,{timeout:25000,waitUntil:'domcontentloaded'});await p.waitForTimeout(3500);await p.screenshot({path:'../referencias/'+n+'.jpg',type:'jpeg',quality:70});console.log('ok',n)}catch(e){console.log('x',n,e.message.slice(0,60))}await p.close()}
await b.close()})();
