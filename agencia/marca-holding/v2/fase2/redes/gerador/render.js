// node render.js lista.json  -> [{html,png,w,h}]
const {chromium}=require('playwright');const L=require(require('path').resolve(process.argv[2]));
(async()=>{const b=await chromium.launch();const p=await b.newPage();for(const x of L){await p.setViewportSize({width:x.w,height:x.h});await p.goto('file://'+x.html);await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(150);await p.screenshot({path:x.png,type:x.png.endsWith('.jpg')?'jpeg':'png',quality:x.png.endsWith('.jpg')?90:undefined});}await b.close()})();
