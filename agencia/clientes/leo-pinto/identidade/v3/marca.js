// Sistema de marca v3 · Leo Pinto (compartilhado pelo manual e pelos mockups)
const C={l:'#F26A1B',a:'#FFC20E',g:'#3FB8E8',b:'#0E4DA4',n:'#0A2A5E',c:'#F4EFE6',w:'#FFFFFF'};
let _id=0;const uid=()=> 'u'+(++_id);
// Monograma LP: haste = Leo de pé · bojo do P = sol · pé do L = água
function glyph({L=C.w,sun=C.a,water=C.g}={}){return `<rect x="58" y="38" width="32" height="118" rx="3" fill="${L}"/><path d="M90 38h12a37 37 0 0 1 0 74H90z" fill="${sun}"/><path d="M90 156V132c10-8 20-8 30 0s20 8 30 0v24z" fill="${water}"/>`}
function mono({bg=C.l,s=200,...g}={}){return `<svg viewBox="0 0 200 200" width="${s}" height="${s}"><circle cx="100" cy="100" r="98" fill="${bg}"/><g transform="translate(8 3)">${glyph(g)}</g></svg>`}
// Selo de mandato com texto em anel
function selo({s=300,bg=C.n,ring=C.a,txt=C.w,inner=C.l,...g}={}){const id=uid();const t='DO POVO, PRO POVO · SÃO JOÃO BATISTA · MA · ';
return `<svg viewBox="0 0 300 300" width="${s}" height="${s}"><defs><path id="${id}" d="M150 150m-118 0a118 118 0 1 1 236 0a118 118 0 1 1-236 0"/></defs><circle cx="150" cy="150" r="148" fill="${bg}"/><circle cx="150" cy="150" r="138" fill="none" stroke="${ring}" stroke-width="2"/><circle cx="150" cy="150" r="98" fill="none" stroke="${ring}" stroke-width="2"/><text font-family="Archivo" font-weight="800" font-size="19.5" fill="${txt}"><textPath href="#${id}" textLength="738" lengthAdjust="spacing">${t}</textPath></text><circle cx="150" cy="150" r="88" fill="${inner}"/><g transform="translate(150 150) scale(.82) translate(-92 -97)">${glyph(g)}</g></svg>`}
// Wordmark
function word({c1=C.n,c2=C.l,fs=120,tag='Vereador · São João Batista',tc=null,stack=false}={}){return `<div style="font-family:Archivo;font-weight:900;font-stretch:72%;font-size:${fs}px;line-height:.82;letter-spacing:-.01em;color:${c1};white-space:nowrap">LEO${stack?'<br>':' '}<span style="color:${c2}">PINTO</span></div>${tag?`<div style="font-family:Inter;font-weight:600;font-size:${Math.max(fs*.12,10)}px;letter-spacing:.32em;text-transform:uppercase;color:${tc||c1};margin-top:${fs*.16}px;opacity:.9">${tag}</div>`:''}`}
function lockup({fs=110,m={},...w}={}){return `<div style="display:flex;align-items:center;gap:${fs*.26}px">${mono({s:fs*1.55,...m})}<div>${word({fs,...w})}</div></div>`}
// Grão de filme (overlay)
const GRAIN=`url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='300'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='3' stitchTiles='stitch'/%3E%3CfeColorMatrix values='0 0 0 0 .5 0 0 0 0 .5 0 0 0 0 .5 0 0 0 .55 0'/%3E%3C/filter%3E%3Crect width='300' height='300' filter='url(%23n)'/%3E%3C/svg%3E")`;
// Azulejo da Baixada (padrão de 120 px)
function azulejo({fg=C.b,bg=C.c,ac=C.l,su=C.a,s=120}={}){const id=uid();return {id,def:`<pattern id="${id}" width="${s}" height="${s}" patternUnits="userSpaceOnUse"><g transform="scale(${s/120})"><rect width="120" height="120" fill="${bg}"/>
${[[0,0],[120,0],[0,120],[120,120]].map(([x,y])=>`<circle cx="${x}" cy="${y}" r="34" fill="${fg}"/><circle cx="${x}" cy="${y}" r="22" fill="${bg}"/><circle cx="${x}" cy="${y}" r="12" fill="${ac}"/>`).join('')}
<g transform="translate(60 60)">${[0,45,90,135].map(r=>`<ellipse rx="30" ry="9" transform="rotate(${r})" fill="${fg}"/>`).join('')}<circle r="13" fill="${bg}"/><circle r="8" fill="${su}"/></g>
<path d="M14 60c6-5 12-5 18 0M88 60c6-5 12-5 18 0M60 14c-5 6-5 12 0 18M60 88c-5 6-5 12 0 18" stroke="${fg}" stroke-width="3.5" fill="none" stroke-linecap="round"/></g></pattern>`}}
// Ondas da Baixada
const wave=(c,y,a=40,w=1080,h=2000)=>`<path d="M0 ${y}c${w/8}-${a} ${w/4}-${a} ${w*3/8} 0s${w/4} ${a} ${w*3/8} 0 ${w/4}-${a} ${w*3/8} 0v${h}H0z" fill="${c}"/>`;
// Bandeirinhas
function flags(n,w,cols=[C.l,C.a,C.g,C.b,C.w],sag=34){let s=`<svg viewBox="0 0 ${w} ${sag+70}" width="${w}" style="display:block"><path d="M0 6Q${w/2} ${sag*2} ${w} 6" stroke="${C.n}" stroke-width="2.5" fill="none"/>`;for(let i=0;i<n;i++){const t=(i+.5)/n,x=t*w,y=6+(1-(2*t-1)**2)*sag;s+=`<path d="M${x-22} ${y}h44v46l-22-13-22 13z" fill="${cols[i%cols.length]}" transform="rotate(${(t-.5)*-14} ${x} ${y})"/>`}return s+'</svg>'}
// Ícones: traço 6, cantos redondos, ponto de acento
const ICONS={
'Saúde':'<path d="M50 82C22 64 14 50 14 38a18 18 0 0 1 36-6 18 18 0 0 1 36 6c0 12-8 26-36 44z"/><path d="M50 42v20M40 52h20" class="ac"/>',
'Educação':'<path d="M12 30c14-6 26-6 38 4 12-10 24-10 38-4v48c-14-6-26-6-38 4-12-10-24-10-38-4z"/><path d="M50 34v48"/><path d="M24 46h14M62 46h14" class="ac"/>',
'Esporte':'<circle cx="50" cy="50" r="34"/><path d="M50 32l15 11-6 18H41l-6-18z" class="ac"/><path d="M50 16v16M82 41l-17 2M70 78l-11-17M30 78l11-17M18 41l17 2"/>',
'Pesca':'<path d="M14 50c18-22 48-22 62 0-14 22-44 22-62 0z"/><path d="M76 50l12-13v26z"/><circle cx="32" cy="47" r="3" class="dot"/><path d="M48 38c4 8 4 16 0 24" class="ac"/>',
'Água':'<path d="M50 14C36 34 26 46 26 60a24 24 0 0 0 48 0c0-14-10-26-24-46z"/><path d="M38 62a12 12 0 0 0 12 12" class="ac"/>',
'Lagos':'<path d="M10 38c10-8 20-8 30 0s20 8 30 0 20-8 30 0"/><path d="M10 56c10-8 20-8 30 0s20 8 30 0 20-8 30 0" class="ac"/><path d="M10 74c10-8 20-8 30 0s20 8 30 0 20-8 30 0"/>',
'Fé':'<path d="M28 86V46l22-22 22 22v40z"/><path d="M50 6v18M42 13h16" class="ac"/><path d="M43 86V70a7 7 0 0 1 14 0v16"/><path d="M14 86h72"/>',
'Obras':'<path d="M28 88L42 16M72 88L58 16"/><path d="M50 22v10M50 44v12M50 68v16" class="ac"/><path d="M12 88h76"/>',
'Juventude':'<path d="M34 88V58l-6-8V32a6 6 0 0 1 12 0v10-16a6 6 0 0 1 12 0v16-12a6 6 0 0 1 12 0v12-6a6 6 0 0 1 12 0v20c0 10-6 18-14 22v10"/><path d="M40 70h20" class="ac"/>',
'Povo':'<circle cx="28" cy="34" r="9"/><circle cx="72" cy="34" r="9"/><circle cx="50" cy="40" r="11" class="ac"/><path d="M12 74c0-12 7-21 16-21M88 74c0-12-7-21-16-21M28 88c0-17 10-26 22-26s22 9 22 26"/>',
'Escuta':'<path d="M16 26h68v40H48L30 82V66H16z"/><path d="M32 42h36M32 52h22" class="ac"/>',
'São João':'<path d="M6 22Q50 50 94 22"/><path d="M16 28v30l9-7 9 7V35" class="ac"/><path d="M41 37v30l9-7 9 7V37"/><path d="M66 35v23l9-7 9 7V28" class="ac"/>'};
function icon(k,{bg=C.b,fg=C.w,ac=C.a,s=170}={}){return `<svg viewBox="0 0 100 100" width="${s}" height="${s}"><circle cx="50" cy="50" r="50" fill="${bg}"/><g transform="translate(50 50) scale(.6) translate(-50 -50)" fill="none" stroke="${fg}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round">${ICONS[k].replaceAll('class="ac"',`stroke="${ac}"`).replaceAll('class="dot"',`fill="${fg}"`)}</g></svg>`}
