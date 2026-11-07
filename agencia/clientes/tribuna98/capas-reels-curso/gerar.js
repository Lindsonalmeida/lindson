// Gera as 9 capas de Reels do curso de processo legislativo, 1080x1920 (PNG). Uso: node gerar.js
// Conta Leandro, 07/11/2026. Modelo: capas.html (assinatura do instagram-perfil/destaques.html).
const {chromium}=require('playwright');const path=require('path');
const NOMES=['01-urgencia','02-pode-votar','03-projeto-tramitar','04-devido-processo','05-sessao-secreta','06-principio','07-medida-provisoria','08-quorum','09-quem-propoe'];
(async()=>{
  const b=await chromium.launch();
  const p=await b.newPage({viewport:{width:1080,height:1920},deviceScaleFactor:1});
  await p.goto('file://'+path.join(__dirname,'capas.html'));
  await p.waitForLoadState('networkidle');await p.evaluate(()=>document.fonts.ready);
  for(let i=1;i<=9;i++){
    const id=`capa-0${i}`;
    await p.evaluate(id=>mostra(id),id);
    await p.waitForTimeout(150);
    await p.locator('#'+id).screenshot({path:path.join(__dirname,`capa-${NOMES[i-1]}.png`)});
    console.log(id,'ok');
  }
  await b.close();
})();
