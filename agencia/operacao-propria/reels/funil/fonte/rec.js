const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:process.env.CH});
const c=await b.newContext({viewport:{width:1080,height:1920},recordVideo:{dir:__dirname+'/vid',size:{width:1080,height:1920}}});const p=await c.newPage();
await p.goto('file://'+__dirname+'/index.html');await p.waitForTimeout(1400);
for(let i=0;i<60;i++){await p.mouse.wheel(0,14);await p.waitForTimeout(40)}await p.waitForTimeout(500);
for(let i=0;i<50;i++){await p.mouse.wheel(0,-16);await p.waitForTimeout(40)}await p.waitForTimeout(800);await c.close();await b.close()})();
