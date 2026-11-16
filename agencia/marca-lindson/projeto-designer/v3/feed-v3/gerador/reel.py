# Reel animado Barzakh feed v3 (conta Leandro, 16/11/2026). 10 s, 1080x1920, 30 fps, motion + SFX + trilha (sem narração).
# Estilos do catálogo 200 Motion: #41 tipografia cinética, #48 fita em loop, #163 zoom, #169 flash de luz, #35 grão.
import os, subprocess, shutil
from playwright.sync_api import sync_playwright
from feed3 import CSS, fundo, fita, selo, mock, u, OB, MA, AU, LOGO, CHROME
G = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.dirname(G) + '/reels'
FR = '/tmp/claude-0/reelfr'; shutil.rmtree(FR, ignore_errors=True); os.makedirs(FR)
B = '/home/user/lindson/conteudo/reels/leva-30s/banco'
an = lambda t, s, st='': f'<div class="a an" style="{st};font-size:{s}px">{t}</div>'
html = f'''<html><head><meta charset="utf-8"><style>{CSS} .pg{{margin:0}} .sc{{position:absolute;inset:0;opacity:0}}</style></head><body>
<section class="pg" id="r" style="height:1920px">
 <div class="sc" id="s1">{fundo('O')}
   <div class="a an" id="t1" style="left:0;right:0;top:330px;text-align:center;font-size:520px;color:{OB}">SUA</div>
   <div class="a an" id="t2" style="left:0;right:0;top:800px;text-align:center;font-size:400px;color:{OB}">MARCA</div>
   <div class="a" id="f1" style="left:0;top:0;width:1080px;height:1920px">{fita(1330,-5,'IDENTIDADE ✦ MARCA ✦ TRAVESSIA ✦ ',OB,AU)}</div>
   <div class="a" style="left:0;right:0;top:1480px;text-align:center;font-size:76px;color:{OB}" id="t3"><span class="it">está à altura do seu negócio?</span></div></div>
 <div class="sc" id="s2">{fundo('D')}
   <div id="m1" class="a" style="inset:0">{mock('oregano-embalagem.jpg',40,520,620,700,-9)}</div>
   <div id="m2" class="a" style="inset:0">{mock('realtime-poster.jpg',460,440,580,780,8)}</div>
   <div class="a an" id="t4" style="left:0;right:0;top:230px;text-align:center;font-size:300px;color:{MA};z-index:10">PARECE</div>
   <div class="a an" id="t5" style="left:0;right:0;top:1330px;text-align:center;font-size:330px;z-index:10"><span class="cx">MENOR?</span></div></div>
 <div class="sc" id="s3">{fundo('D')}
   <img id="lg" class="a" src="{u(LOGO+'/barzakh-simbolo-ouro.png')}" style="left:340px;top:330px;width:400px;z-index:5">
   <div class="a an" id="t6" style="left:0;right:0;top:800px;text-align:center;font-size:250px;color:{AU};z-index:6">BARZAKH</div>
   <div class="a" id="t7" style="left:0;right:0;top:1070px;text-align:center;font-size:80px;color:{MA};z-index:6"><span class="it">a passagem da sua marca.</span></div>
   <div id="f2" class="a" style="inset:0">{fita(1300,-4)}{fita(1390,4,'UM ESTÚDIO AL KÁNTARA ✦ ',OB,AU,8)}</div>
   <div class="a mn" style="left:0;right:0;top:1560px;text-align:center;font-size:30px;color:{MA}">@barzakhstudio · link na bio</div></div>
 {selo(800,130,210)}
 <div class="a" id="fl" style="inset:0;background:#fff3d6;opacity:0;z-index:25"></div>
</section></body></html>'''
open(G + '/reel.html', 'w').write(html)
JS = '''() => {
 const A=[]; const g=(id)=>document.getElementById(id);
 const an=(el,kf,o)=>{const a=el.animate(kf,Object.assign({fill:'both'},o));a.pause();A.push(a)};
 const vis=(id,t0,t1)=>an(g(id),[{opacity:0,offset:0},{opacity:0,offset:t0/10},{opacity:1,offset:t0/10+.0001},{opacity:1,offset:t1/10},{opacity:0,offset:Math.min(1,t1/10+.0001)},{opacity:0,offset:1}],{duration:10000});
 vis('s1',0,3.3); vis('s2',3.3,6.6); vis('s3',6.6,9.999);
 const slam=(id,d)=>an(g(id),[{transform:'scale(3)',opacity:0},{transform:'scale(.94)',opacity:1,offset:.7},{transform:'scale(1)',opacity:1}],{duration:380,delay:d,easing:'cubic-bezier(.2,.8,.2,1)'});
 slam('t1',100); slam('t2',650); slam('t4',3400); slam('t5',4300); slam('t6',7000);
 an(g('t3'),[{transform:'translateY(80px)',opacity:0},{transform:'none',opacity:1}],{duration:400,delay:1400});
 an(g('t7'),[{transform:'translateY(80px)',opacity:0},{transform:'none',opacity:1}],{duration:400,delay:7600});
 an(g('m1'),[{transform:'translateX(-900px) rotate(-20deg)'},{transform:'none'}],{duration:500,delay:3600,easing:'cubic-bezier(.2,.8,.2,1)'});
 an(g('m2'),[{transform:'translateX(900px) rotate(20deg)'},{transform:'none'}],{duration:500,delay:3800,easing:'cubic-bezier(.2,.8,.2,1)'});
 an(g('s2'),[{transform:'translate(0,0)'},{transform:'translate(-14px,10px)'},{transform:'translate(12px,-8px)'},{transform:'translate(0,0)'}],{duration:240,delay:4300});
 an(g('lg'),[{transform:'scale(0) rotate(-90deg)'},{transform:'scale(1.08)',offset:.8},{transform:'scale(1) rotate(0)'}],{duration:600,delay:6650});
 an(g('s3'),[{transform:'scale(1.12)'},{transform:'scale(1)'}],{duration:3300,delay:6600});
 document.querySelectorAll('.giro').forEach(e=>an(e,[{transform:'rotate(0)'},{transform:'rotate(360deg)'}],{duration:8000,iterations:2}));
 document.querySelectorAll('.run').forEach((e,i)=>an(e,[{transform:'translateX(0)'},{transform:'translateX(-700px)'}],{duration:10000}));
 an(g('fl'),[{opacity:0},{opacity:0,offset:.329},{opacity:.95,offset:.33},{opacity:0,offset:.36},{opacity:0,offset:.659},{opacity:.95,offset:.66},{opacity:0,offset:.69},{opacity:0}],{duration:10000});
 window.__A=A; }'''
with sync_playwright() as p:
    b = p.chromium.launch(executable_path=CHROME); pg = b.new_page(viewport={'width': 1080, 'height': 1920})
    pg.goto(u(G + '/reel.html')); pg.wait_for_timeout(1500); pg.evaluate(JS)
    for f in range(300):
        pg.evaluate(f'()=>window.__A.forEach(a=>a.currentTime={f*1000/30})')
        pg.locator('#r').screenshot(path=f'{FR}/{f:04d}.jpg', type='jpeg', quality=88)
    b.close()
# SFX: whoosh+impacto nas batidas (0.1, 0.65, 3.3, 4.3, 6.6, 7.0), trilha com fade
ev = [(B+'/sfx/whoosh-impacto-grave.mp3', 100), (B+'/sfx/whoosh-rapido.mp3', 650), (B+'/sfx/whoosh-impacto-grave.mp3', 3300), (B+'/sfx/glitch-quebra.mp3', 4300), (B+'/sfx/whoosh-impacto-grave.mp3', 6600), (B+'/sfx/sweep-curto.mp3', 7000)]
ins = ['-i', B+'/trilha/trap-electro-vibes-112bpm.mp3'] + sum([['-i', e[0]] for e in ev], [])
flt = '[1:a]atrim=0:10,afade=t=in:d=0.3,afade=t=out:st=9:d=1,volume=0.55[m];' + ''.join(f'[{k+2}:a]adelay={d}|{d},volume=1.1[s{k}];' for k, (_, d) in enumerate(ev)) + '[m]' + ''.join(f'[s{k}]' for k in range(len(ev))) + f'amix=inputs={len(ev)+1}:normalize=0,alimiter=limit=0.95[a]'
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-framerate', '30', '-i', f'{FR}/%04d.jpg'] + ins + ['-filter_complex', flt, '-map', '0:v', '-map', '[a]', '-t', '10', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '21', '-c:a', 'aac', '-b:a', '160k', OUT + '/reel-barzakh-v3-1080x1920.mp4'], check=True)
print('ok')
