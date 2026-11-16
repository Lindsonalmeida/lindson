"""v4 advogado (conta Zuleide, 16/11/2026): cenas do Gemini com o rosto do Lindson (v3/cenas-gemini/) usadas INTEIRAS como protagonista.
Copia a composição da referência aprovada Denis Bugatti 2026 (referencias-lindson/22-26): linha fina + palavras gigantes condensadas, 1 palavra neon, assinatura.
Energia: luz de borda na cor neon, vazamento de luz, grão, tarja do nicho. Copy revisada (social media, copy, Maquiavel, /arte-advocacia: sem promessa, Provimento 205).
python3 gerar_v4.py"""
import asyncio,os
from playwright.async_api import async_playwright
D=os.path.dirname(os.path.abspath(__file__)); C=os.path.abspath(f'{D}/../v3/cenas-gemini')
A='/home/user/lindson/conteudo/youtube/raposa-e-leao/produto/fonts/Anton-Regular.ttf'
RED,LIME,GOLD='#FF2E3B','#C8FF2E','#FFC83D'
# nome: posicao Y da cena (4:5), cor, linha fina, gigante, linha final, tarja
P={'ADV-1':('-360px',LIME,'quem te procura e não acha','SÓ VÊ A SUA<br><n>SOMBRA</n>','manda ADV no WhatsApp','01 · ADVOGADO'),
 'ADV-2':('-300px',GOLD,'sério na lei,','E <n>INVISÍVEL</n><br>NO GOOGLE?','conteúdo dentro do Provimento 205','02 · ADVOGADO'),
 'ADV-3':('-60px',RED,'você estudou anos.','O CLIENTE<br><n>TE ACHA?</n>','manda ADV no WhatsApp','03 · ADVOGADO'),
 'ADV-4':('-230px',LIME,'seu marketing','JOGA XADREZ<br>OU <n>DAMAS?</n>','estratégia antes do anúncio','04 · ADVOGADO')}
CAPA=('30%',RED,'advogado de São Luís','DÁ PRA ANUNCIAR<br><n>SEM FERIR</n> A OAB?','▶ assista','REELS · ADVOGADO')
def html(H,cena,pos,cor,fina,giga,fim,tag):
    return f"""<html><head><style>@font-face{{font-family:A;src:url('file://{A}')}}*{{margin:0;box-sizing:border-box}}
body{{width:1080px;height:{H}px;overflow:hidden;position:relative;background:#000;font-family:Inter}}
.bg{{position:absolute;inset:0;background:url('file://{C}/{cena}.jpg') 50% {pos}/{'cover' if pos=='50%' else '100% auto'};filter:saturate(1.2) contrast(1.1)}}
.lk{{position:absolute;inset:0;mix-blend-mode:screen;background:radial-gradient(ellipse at 100% 0%,{cor}55,transparent 45%),radial-gradient(ellipse at 0% 60%,{cor}22,transparent 40%)}}
.sh{{position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.45),transparent 14%,transparent 55%,rgba(0,0,0,.85) 74%,#000 96%)}}
.tg{{position:absolute;top:{H*.04:.0f}px;left:54px;font:800 20px Inter;letter-spacing:.3em;color:#000;background:{cor};padding:9px 16px}}
.tl{{position:absolute;top:{H*.04+12:.0f}px;right:54px;font:600 18px Inter;letter-spacing:.3em;color:#fff;opacity:.8}}
.t{{position:absolute;left:50px;right:50px;bottom:{H*(.075 if H>1500 else .06):.0f}px;text-align:center;color:#fff}}
.f{{font:300 {H*.028:.0f}px Inter;text-transform:uppercase;letter-spacing:.04em;margin-bottom:12px}}
.g{{white-space:nowrap;font-family:A;font-size:{H*(.105 if H>1500 else .092):.0f}px;line-height:.92;text-transform:uppercase;text-shadow:0 8px 30px rgba(0,0,0,.7)}}
n{{color:{cor};text-shadow:0 0 20px {cor}bb,0 0 60px {cor}77}}
.e{{display:inline-block;margin-top:18px;font:700 {H*.017:.0f}px Inter;text-transform:uppercase;letter-spacing:.18em;border:2px solid {cor};padding:10px 22px}}
.s{{position:absolute;bottom:{H*.022:.0f}px;left:0;right:0;text-align:center;font:800 18px Inter;letter-spacing:.32em;color:#fff;opacity:.75}}
.gr{{position:absolute;inset:0;opacity:.12;mix-blend-mode:overlay;background:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='200' height='200'><filter id='n'><feTurbulence baseFrequency='.9' numOctaves='2'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>")}}
</style></head><body><div class="bg"></div><div class="lk"></div><div class="sh"></div><div class="gr"></div><div class="tg">{tag}</div><div class="tl">SÃO LUÍS</div>
<div class="t"><div class="f">{fina}</div><div class="g">{giga}</div><div class="e">{fim}</div></div><div class="s">LINDSON ALMEIDA</div>
<script>const g=document.querySelector('.g');let z=parseFloat(getComputedStyle(g).fontSize);while(g.scrollWidth>980&&z>40){{z-=4;g.style.fontSize=z+'px'}}</script></body></html>"""
def main():
    import json,subprocess;J=[]
    def shot(h,H,out):
        t=f'{D}/_h{len(J)}.html';open(t,'w').write(h);J.append([t,H,out])
    for n,a in P.items():
        shot(html(1920,n,'50%',*a[1:]),1920,f'{D}/artes/{n}-9x16.jpg'); shot(html(1350,n,*a),1350,f'{D}/artes/{n}-4x5.jpg')
    shot(html(1920,'CAPA-ADV','50%',*CAPA[1:]),1920,f'{D}/artes/ADV-capa-reels-9x16.jpg')
    open(f'{D}/_j.json','w').write(json.dumps(J));subprocess.run(['node',f'{D}/render.js',f'{D}/_j.json'],check=True,cwd='/home/user/lindson')
    for t,_,_ in J: os.remove(t)
    os.remove(f'{D}/_j.json')
    from PIL import Image
    w,h=300,533;ns=list(P)+['ADV-capa-reels'];S=Image.new('RGB',(5*(w+20)+20,h+20+380+40),'#111')
    for j,n in enumerate(ns):
        im=Image.open(f'{D}/artes/{n}-9x16.jpg').resize((w,h));S.paste(im,(20+j*(w+20),20))
        if n in P: im=Image.open(f'{D}/artes/{n}-4x5.jpg').resize((w,375));S.paste(im,(20+j*(w+20),h+40))
    S.save(f'{D}/folha-adv.jpg',quality=88)
main()
