<svg width="0" height="0" style="position:absolute"><defs>
<symbol id="emb" viewBox="0 0 400 400">
 <circle cx="200" cy="200" r="194" fill="none" stroke="#C9A227" stroke-width="5"/>
 <circle cx="200" cy="200" r="183" fill="none" stroke="#C9A227" stroke-width="1.5" opacity=".6"/>
 <g transform="translate(-14,6) scale(.92) translate(17,17)">
 <!-- juba do leão (só lado direito) -->
 <g id="juba"></g>
 <!-- RAPOSA (esquerda) -->
 <polygon points="200,110 170,115 150,172 200,176" fill="#B54B1C"/>
 <polygon points="120,36 108,138 170,115" fill="#D9622B"/>
 <polygon points="126,64 120,124 158,116" fill="#3a1a0c"/>
 <polygon points="170,115 108,138 150,172" fill="#C4561F"/>
 <polygon points="108,138 92,192 140,206 150,172" fill="#EE8040"/>
 <polygon points="92,192 74,236 150,266 140,206" fill="#EFE6D2"/>
 <polygon points="140,206 150,266 186,300 200,305 200,240 160,226" fill="#E2D6BC"/>
 <polygon points="150,172 140,206 160,226 200,240 200,176" fill="#D9622B"/>
 <polygon points="134,184 166,190 140,198" fill="#0B0A08"/>
 <polygon points="147,186 152,195 143,195" fill="#E2BE4A"/>
 <!-- LEÃO (direita) -->
 <polygon points="200,110 236,110 256,172 200,176" fill="#A8841C"/>
 <polygon points="236,110 262,96 282,124 256,172" fill="#C9A227"/>
 <polygon points="248,104 262,98 274,120 258,126" fill="#5a3f0a"/>
 <polygon points="256,172 282,124 304,170 300,222" fill="#C9A227"/>
 <polygon points="200,176 256,172 300,222 252,252 200,240" fill="#E2BE4A"/>
 <polygon points="200,240 252,252 268,280 226,300 200,305" fill="#D4B04A"/>
 <polygon points="252,252 300,222 290,268 268,280" fill="#A8841C"/>
 <polygon points="200,305 226,300 216,326 200,330" fill="#8A6514"/>
 <polygon points="236,182 270,184 244,198" fill="#0B0A08"/>
 <polygon points="248,186 254,195 245,195" fill="#D9622B"/>
 <!-- nariz -->
 <polygon points="186,286 214,286 200,306" fill="#0B0A08"/>
 <line x1="200" y1="110" x2="200" y2="286" stroke="#0B0A08" stroke-width="2" opacity=".5"/>
 </g>
</symbol>
</defs></svg>
<script>
const g=document.getElementById('juba');let pts=[];const cx=200,cy=200;
for(let i=0;i<=14;i++){const a=(-100+i*(200/14))*Math.PI/180;const r=i%2?132:178;pts.push([cx+Math.cos(a)*r,cy+Math.sin(a)*r])}
const ns='http://www.w3.org/2000/svg';
for(let i=0;i<pts.length-1;i++){const p=document.createElementNS(ns,'polygon');p.setAttribute('points',`${cx},${cy} ${pts[i]} ${pts[i+1]}`);p.setAttribute('fill',i%2?'#6E4A0E':'#8A5A12');g.appendChild(p)}
</script>
