"""Capas A/B/C dos longos no padrão da IDENTIDADE.md (Anton, 1 palavra em ouro, no máx. 1 tarja, retrato P&B com brilho, etiqueta dourada, selo).
python3 capas_longos.py 17 18 ... -> ../capas/longo-NN-X.jpg (lê capas_v2.json). C = variante 'mais luz, menos texto' para o teste do Peter. (conta Leandro)"""
import json,os,sys,subprocess
D=os.path.dirname(os.path.abspath(__file__));R=os.path.dirname(D)
cfg=json.load(open(R+'/capas_v2.json'));idt=open(R+'/identidade.html').read()
head=idt[:idt.index('</defs></svg>')+len('</defs></svg>')];scr=idt[idt.index('<script>'):]
css='<style>body{margin:0}.p{position:relative;overflow:hidden}.th.luz .foto{filter:grayscale(1) contrast(1.05) brightness(1.18)}.th.luz{background:#1d1912}.th.luz .brilho{opacity:1.5;width:640px;height:640px}</style>'
sec=[];ids=[]
for n in sys.argv[1:]:
    for k,c in cfg['longo-'+n].items():
        i=f'c{n}{k}';ids.append((i,f'{R}/capas/longo-{n}-{k}.jpg'))
        cl='p th grao'+(' b' if c['lado']=='esq' else '')+(' luz' if c.get('luz') else '')
        fs=c.get('fs',128)
        sec.append(f'<section class="{cl}" id="{i}"><div class="brilho"></div><div class="foto" style="background-image:url(img/{c["grav"]});background-position:{c.get("pos","center 18%")}"></div><div class="txt"><div class="tag">{c["tag"]}</div><h2 style="font-size:{fs}px">{c["txt"]}</h2></div><div class="selo"><svg><use href="#emb"/></svg>{c.get("marca","RAPOSA E LEÃO")}</div></section>')
st=R+'/_capas_stage.html';open(st,'w').write(head.replace('</head>',css+'</head>') if '</head>' in head else head+css)
open(st,'a').write('\n'.join(sec)+scr)
px=os.environ.get('HTTPS_PROXY','')
js="const {chromium}=require('playwright');(async()=>{const b=await chromium.launch(%s);const p=await b.newPage({viewport:{width:1400,height:900}});await p.goto('file://%s');await p.waitForTimeout(2500);await p.evaluate(()=>document.fonts.ready);for(const [i,f] of %s){await (await p.$('#'+i)).screenshot({path:f,type:'jpeg',quality:90})}await b.close()})();"%(json.dumps({'proxy':{'server':px}} if px else {}),st,json.dumps(ids))
open('/tmp/claude-0/-home-user/b9464785-a028-5189-b9f0-a7ed9d7dd59e/scratchpad/capas.js','w').write(js)
subprocess.run(['node','/tmp/claude-0/-home-user/b9464785-a028-5189-b9f0-a7ed9d7dd59e/scratchpad/capas.js'],check=True,env={**os.environ,'NODE_PATH':subprocess.check_output(['npm','root','-g']).decode().strip()})
os.remove(st);print('\n'.join(f for _,f in ids))
