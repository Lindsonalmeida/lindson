import json,os,sys,html
from playwright.sync_api import sync_playwright
exec(open('conteudo.py').read())
meta=json.load(open('meta.json'))
OUT=sys.argv[1]
SIREN='<svg class="sir" viewBox="0 0 40 40"><rect x="9" y="12" width="22" height="20" rx="11" fill="#E8262B"/><rect x="6" y="30" width="28" height="6" rx="2" fill="#E8262B"/><rect x="18" y="16" width="4" height="9" rx="2" fill="#fff"/><path d="M20 2v5M6 8l3 4M34 8l-3 4" stroke="#E8262B" stroke-width="3" stroke-linecap="round"/></svg>'
CSS='''*{margin:0;box-sizing:border-box}body{width:1080px;height:1350px;font-family:Inter,Arial,sans-serif;overflow:hidden}
.w{width:1080px;height:1350px;padding:70px 64px 56px;display:flex;flex-direction:column}
.light{background:#fff;color:#0f1419}.dark{background:#000;color:#e7e9ea}
.hd{display:flex;align-items:center;gap:26px}.hd img{width:118px;height:118px;border-radius:50%;object-fit:cover}
.nm{font-weight:800;font-size:46px;letter-spacing:-.5px}.at{font-size:36px;color:#71767b;margin-top:2px}
.tx{font-size:47px;line-height:1.3;margin:38px 0 40px;font-weight:450;letter-spacing:-.2px}
.sir{width:50px;height:50px;vertical-align:-8px;margin-right:6px}
.md{flex:1;border-radius:34px;overflow:hidden;position:relative;min-height:300px}
.md img.f{width:100%;height:100%;object-fit:cover}
.cap{position:absolute;left:0;right:0;bottom:0;padding:70px 34px 26px;background:linear-gradient(transparent,rgba(0,0,0,.85));color:#fff;font-size:28px;font-weight:600}
.cap b{color:#F5C400}
.lk{border:2px solid #cfd9de;border-radius:34px;overflow:hidden;flex:1;display:flex;flex-direction:column}.dark .lk{border-color:#333}
.lk img{width:100%;flex:1;object-fit:cover;min-height:0}.lk .lt{padding:26px 32px 30px}.lk .v{font-size:28px;color:#71767b}.lk .t{font-size:38px;font-weight:700;margin-top:6px;line-height:1.2}
.cta{flex:1;border-radius:34px;background:#F5C400;color:#000;padding:56px 54px;display:flex;flex-direction:column;justify-content:space-between}
.cta .k{font-size:30px;font-weight:700;letter-spacing:4px}.cta .h{font-family:"Inter Display",Inter;font-size:92px;font-weight:900;line-height:.95;letter-spacing:-2px;margin-top:18px}
.cta .p{font-size:36px;line-height:1.3;font-weight:500}.cta .b{display:inline-block;background:#000;color:#F5C400;padding:22px 34px;border-radius:999px;font-size:34px;font-weight:800}
.dots{display:flex;gap:12px;justify-content:center;margin-top:26px}.dots i{width:13px;height:13px;border-radius:50%;background:#71767b55}.dots i.on{background:#1d9bf0}'''
def page(c,i,theme,av,imgp):
  linha,k,veic,data,tit,tw,lic=c
  hd=f'<div class="hd"><img src="{av}"><div><div class="nm">Lindson Almeida</div><div class="at">@lindsonalmeida_</div></div></div>'
  txt=(tw[i] if i<4 else lic)
  t=html.escape(txt)
  if t.startswith('🚨'): t=SIREN+t[1:].lstrip()
  cap=f'<div class="cap">Fonte: <b>{html.escape(veic)}</b> · {data} · imagem: reprodução</div>'
  pos=['50% 50%','50% 50%','20% 40%','80% 60%']
  if i==1:
    md=f'<div class="lk"><img src="{imgp}"><div class="lt"><div class="v">{html.escape(veic)} · {data}</div><div class="t">{html.escape(meta[k]["t"].split(" | ")[0].split(" - ")[0])}</div></div></div>'
  elif i<4:
    sc='1' if i==0 else '1.35'
    md=f'<div class="md"><img class="f" src="{imgp}" style="object-position:{pos[i]};transform:scale({sc});transform-origin:{pos[i]}">{cap}</div>'
  else:
    md='<div class="cta"><div><div class="k">LINDSON ALMEIDA · SÃO LUÍS</div><div class="h">INSTAGRAM<br>QUE VENDE</div></div><div class="p">Estratégia, design e conteúdo para o seu negócio ser encontrado e escolhido.</div><div><span class="b">Me chama no direct: PROPOSTA</span></div></div>'
  dots='<div class="dots">'+''.join(f'<i class="{"on" if j==i else ""}"></i>' for j in range(5))+'</div>'
  return f'<html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="w {theme}">{hd}<div class="tx">{t}</div>{md}{dots}</div></body></html>'
with sync_playwright() as p:
  b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1350})
  cnt={}
  for n,c in enumerate(C):
    cnt[c[0]]=cnt.get(c[0],0)+1; d=f'{OUT}/{c[0]}/{cnt[c[0]]:02d}'; os.makedirs(d,exist_ok=True)
    for i in range(5):
      theme=['light','dark'][(i+n)%2]
      open('tmp.html','w').write(page(c,i,theme,'file://'+os.path.abspath('avatar.jpg'),'file://'+os.path.abspath(f'img/{c[1]}.jpg')))
      pg.goto('file://'+os.path.abspath('tmp.html')); pg.wait_for_timeout(150)
      # check overflow
      ov=pg.evaluate('(()=>{const t=document.querySelector(".tx").getBoundingClientRect(); const m=document.querySelector(".md,.lk,.cta").getBoundingClientRect(); return [m.height, document.querySelector(".w").scrollHeight]})()')
      if ov[0]<330 or ov[1]>1350: print('WARN',d,i,ov)
      pg.screenshot(path=f'{d}/{i+1:02d}.png')
  b.close()
