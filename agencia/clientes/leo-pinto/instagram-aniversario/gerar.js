// node gerar.js <pasta da pessoa> -> <pasta>/aniversario.jpg (2160x2700, alta qualidade; o Instagram aceita e reduz). Conta Leandro, 03/11/2026.
// A pasta (FORA do Git: foto de pessoa) tem: dados.json, recorte.png (pessoa(s) recortada(s), ver recortar.py), avatar.jpg (foto de perfil do Leo), logo.png e logo-marinho.png.
// dados.json: {"nome1":"JOSEF","nome2":"FIGUEIREDO","data":"03 DE NOVEMBRO","cor":"azul|laranja","chamada":"Parabéns!","frase":"…","topo":520,"largura":820,"dx":0}
const {chromium}=require('playwright');const fs=require('fs'),path=require('path');
(async()=>{const pasta=path.resolve(process.argv[2]);const d=JSON.parse(fs.readFileSync(path.join(pasta,'dados.json'),'utf8'));
const uri=f=>{const p=path.join(pasta,f);return 'data:image/'+(f.endsWith('.png')?'png':'jpeg')+';base64,'+fs.readFileSync(p).toString('base64')};
Object.assign(d,{foto:uri('recorte.png'),avatar:uri('avatar.jpg'),logo:uri('logo.png'),logoMarinho:uri('logo-marinho.png')});
const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1350},deviceScaleFactor:2}); /* alta qualidade: 2160x2700 (pedido do Lindson, 03/11) */const erros=[];p.on('pageerror',e=>erros.push(e.message));
await p.addInitScript(x=>{window.DADOS=x},d);await p.goto('file://'+__dirname+'/aniversario.html',{waitUntil:'networkidle'});
await p.waitForFunction('window.pronto===true',{timeout:30000});await p.waitForTimeout(300);
await p.screenshot({path:path.join(pasta,'aniversario.jpg'),type:'jpeg',quality:95});console.log(path.join(pasta,'aniversario.jpg'),'erros:',JSON.stringify(erros));await b.close()})();
