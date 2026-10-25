// BOMBOU — desenho do post de notícia (1080x1350). Usado na identidade e na Fábrica.
const BOMBOU_ARROBA='@bombouof';
// item: {titulo (com *destaque*), chapeu, regiao:'MA'|'BR', fonte, quando, foto(img já carregada ou null)}
function bombouArte(cv,item,img){
  const W=1080,H=1350;cv.width=W;cv.height=H;const x=cv.getContext('2d');
  const RED='#E10600',YEL='#FFD400',INK='#0A0A0A',WH='#FFFFFF';
  x.fillStyle=INK;x.fillRect(0,0,W,H);
  const raw0=(item.titulo||'').toUpperCase();const toks=[];{let hl=false;for(const p of raw0.split(/(\*)/)){if(p==='*'){hl=!hl;continue}for(const w of p.split(/\s+/).filter(Boolean))toks.push({w,hl})}}
  function quebra(fs){x.font=`400 ${fs}px Anton`;const L=[[]];let lw=0;for(const t of toks){const ww=x.measureText(t.w+' ').width;if(lw+ww>984&&L[L.length-1].length){L.push([]);lw=0}L[L.length-1].push(t);lw+=ww}return L}
  let fotoH=H,fs=100,lines;
  if(img){for(fs=96;fs>=60;fs-=4){lines=quebra(fs);if(lines.length*fs*1.02<=340)break}}
  if(img){ // post inteiro com a própria foto desfocada + a foto INTEIRA (sem corte) grande no centro
    const r0=Math.max(W/img.width,H/img.height)*1.08,w0=img.width*r0,h0=img.height*r0;
    x.filter='blur(34px) brightness(.45) saturate(1.2)';x.drawImage(img,(W-w0)/2,(H-h0)/2,w0,h0);x.filter='none';
    const topo=150,base=H-170-lines.length*fs*1.02-70,boxH=base-topo;
    const sc=Math.min(W/img.width,boxH/img.height),w=img.width*sc,h=img.height*sc,ix=(W-w)/2,iy=topo+(boxH-h)/2;
    x.save();x.shadowColor='rgba(0,0,0,.6)';x.shadowBlur=40;x.drawImage(img,ix,iy,w,h);x.restore();
    const g=x.createLinearGradient(0,base-40,0,H);g.addColorStop(0,'rgba(10,10,10,0)');g.addColorStop(.25,'rgba(10,10,10,.85)');g.addColorStop(1,'rgba(10,10,10,.97)');x.fillStyle=g;x.fillRect(0,base-40,W,H-base+40)}
  else{ // fundo de marca: listras diagonais + sigla gigante
    x.save();x.globalAlpha=.10;x.fillStyle=RED;for(let i=-H;i<W+H;i+=90){x.beginPath();x.moveTo(i,0);x.lineTo(i+40,0);x.lineTo(i+40-H,H);x.lineTo(i-H,H);x.fill()}x.restore();
    const rg=x.createRadialGradient(W/2,420,40,W/2,420,700);rg.addColorStop(0,'rgba(225,6,0,.45)');rg.addColorStop(1,'rgba(225,6,0,0)');x.fillStyle=rg;x.fillRect(0,0,W,H);
    x.save();x.font='400 560px Anton';x.textAlign='center';x.fillStyle='rgba(255,255,255,.06)';x.fillText(item.regiao==='MA'?'MA':'BR',W/2,640);x.restore();
    // sirene
    x.save();x.translate(W/2,330);x.fillStyle=RED;x.beginPath();x.arc(0,0,110,Math.PI,0);x.lineTo(110,40);x.lineTo(-110,40);x.fill();x.fillStyle=YEL;x.fillRect(-140,40,280,36);
    x.strokeStyle=YEL;x.lineWidth=12;x.lineCap='round';for(const a of[-2.6,-2.2,-1.57,-.94,-.54]){x.beginPath();x.moveTo(Math.cos(a)*150,Math.sin(a)*150);x.lineTo(Math.cos(a)*200,Math.sin(a)*200);x.stroke()}
    x.fillStyle='rgba(255,255,255,.35)';x.beginPath();x.ellipse(-40,-40,22,40,-.5,0,7);x.fill();x.restore();
  }
  // logo
  x.fillStyle=RED;x.fillRect(48,48,300,92);x.font='400 70px Anton';x.fillStyle=WH;x.textBaseline='middle';x.fillText('BOMBOU',70,96);
  x.fillStyle=YEL;x.beginPath();x.moveTo(318,58);x.lineTo(340,58);x.lineTo(332,108);x.lineTo(326,108);x.fill();x.fillRect(325,116,9,9);
  const reg=item.regiao==='MA'?'MARANHÃO':'BRASIL';x.font='700 30px "Archivo Black", Anton';const rw=x.measureText(reg).width+40;
  x.fillStyle=YEL;x.fillRect(348,48,rw,92);x.fillStyle=INK;x.fillText(reg,368,96);
  // chapéu
  const ch=(item.chapeu||'URGENTE').toUpperCase();x.font='400 46px Anton';const cw=x.measureText(ch).width;
  let ty=img?fotoH-30:760;
  if(!img){for(fs=100;fs>=58;fs-=4){lines=quebra(fs);if(lines.length*fs*1.02<=H-ty-170)break}}
  const lh=fs*1.02;let y0=img?H-160-lines.length*lh+fs*.5:ty;
  // barra do chapéu acima da manchete
  const cy=y0-lh/2-58;x.fillStyle=RED;x.fillRect(48,cy-34,cw+92,68);x.fillStyle=WH;x.beginPath();x.arc(80,cy,12,0,7);x.fill();x.font='400 46px Anton';x.fillText(ch,104,cy+2);
  x.font=`400 ${fs}px Anton`;x.textBaseline='middle';
  lines.forEach((ln,i)=>{let lx=48;const y=y0+i*lh;for(const t of ln){const ww=x.measureText(t.w).width;if(t.hl){x.fillStyle=YEL;x.fillRect(lx-6,y-fs*.5,ww+12,fs*.98);x.fillStyle=INK}else x.fillStyle=WH;x.fillText(t.w,lx,y+2);lx+=ww+x.measureText(' ').width}});
  // rodapé
  x.fillStyle=YEL;x.fillRect(48,H-112,984,6);x.font='700 30px "Archivo Black", Anton';x.fillStyle=WH;x.textBaseline='alphabetic';
  x.fillText(BOMBOU_ARROBA,48,H-56);x.textAlign='right';x.fillStyle='rgba(255,255,255,.7)';x.font='600 28px Archivo, sans-serif';
  x.fillText((item.fonte?'Fonte: '+item.fonte:'')+'  •  leia a legenda',1032,H-56);x.textAlign='left';
}
