# Capas v2 (fundo Gemini do Lindson) dos carrosseis Economist 2027. Designer grafico, 17/11/2026.
# Identidade raposa-e-leao/IDENTIDADE.md: Anton, 1 palavra ouro, max 1 tarja Sangue, selo Cinzel.
# Composicao copiada: thumb de mistério estilo explicador (imagem dramatica full-bleed + manchete gigante em bloco).
import os,shutil
D=os.path.dirname(os.path.abspath(__file__)); IM='/tmp/claude-0/-home-user/71909cf5-3742-5a17-8357-bcbb30dd10b8/images/'
CAPAS=[('c1','51.jpg','top','81 SÍMBOLOS. 1 AVISO.','ELES JÁ <b>SABIAM</b><br><span class="tj">O FUTURO?</span>'),
('c2','47.jpg','bot','A CAPA QUE NINGUÉM DEVIA VER','10 PREVISÕES<br><span class="tj">SOBRENATURAIS</span><br>PARA <b>2027?</b>'),
('c3','48.jpg','bot','ELES JÁ SABIAM?','O MAIOR <b>MEDO</b><br>DE 2027 ESTÁ<br><span class="tj">NESSA CAPA?</span>'),
('c4','49.jpg','bot','DOMINAÇÃO MUNDIAL?','QUEM PUXA<br>AS <b>CORDAS</b><br><span class="tj">DO MUNDO?</span>'),
('c5','50.jpg','bot','A CAPA DA ECONOMIST 2027','O QUE TEM<br>NESSA <b>SERINGA</b><span class="tj">?</span>')]
css='''*{margin:0;box-sizing:border-box}body{background:#000}.f{width:1080px;height:1350px;position:relative;overflow:hidden}
.bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;filter:contrast(1.12) saturate(1.1) sepia(.12)}
.vg{position:absolute;inset:0;background:radial-gradient(ellipse at 50% 45%,transparent 45%,rgba(0,0,0,.75) 100%)}
.gr{position:absolute;left:0;right:0;height:62%}.bot .gr{bottom:0;background:linear-gradient(transparent,rgba(11,10,8,.88) 45%,#0B0A08)}
.top .gr{top:0;background:linear-gradient(#0B0A08,rgba(11,10,8,.85) 50%,transparent)}
.tx{position:absolute;left:64px;right:64px;z-index:5}.bot .tx{bottom:120px}.top .tx{top:110px}
.et{position:absolute;top:44px;left:64px;right:64px;display:flex;justify-content:space-between;font:600 22px Cinzel;letter-spacing:4px;color:#EFE6D2;z-index:6}
.hk{display:inline-block;font:800 34px Inter;color:#0B0A08;background:#E2BE4A;padding:8px 18px;margin-bottom:22px;letter-spacing:1px}
h1{font:400 128px/1.0 Anton;color:#EFE6D2;text-transform:uppercase;text-shadow:0 6px 30px rgba(0,0,0,.8)}
h1 b{font-weight:400;color:#E2BE4A}.tj{background:#8E1B1B;padding:0 16px;display:inline-block;margin-top:10px;line-height:1.08}
.selo{position:absolute;bottom:40px;left:64px;font:600 20px Cinzel;letter-spacing:4px;color:#C9A227;z-index:10;display:flex;align-items:center;gap:14px}
.selo i{font-style:normal;width:46px;height:46px;border:2px solid #C9A227;border-radius:50%;display:grid;place-items:center;font:800 22px Cinzel}
.ia{position:absolute;bottom:50px;right:64px;font:500 15px Inter;color:#EFE6D2;opacity:.6;z-index:10}
.gn{position:absolute;inset:0;opacity:.07;background:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='200' height='200'><filter id='n'><feTurbulence baseFrequency='.9'/></filter><rect width='200' height='200' filter='url(%23n)'/></svg>")}
.pv{position:absolute;z-index:7;background:#EFE6D2;padding:12px 12px 34px;box-shadow:0 18px 40px rgba(0,0,0,.85);transform:rotate(4deg)}
.pv img{display:block;width:100%;filter:contrast(1.08)}.pv .cap{position:absolute;bottom:8px;left:12px;font:800 15px Inter;color:#0B0A08;letter-spacing:1px}
.pv:before{content:'';position:absolute;top:-16px;left:38%;width:110px;height:32px;background:rgba(226,190,74,.75);transform:rotate(-6deg)}
.pv .ci{position:absolute;border:5px solid #D0202A;border-radius:50%;box-shadow:0 0 12px rgba(208,32,42,.6)}
.ar{position:absolute;z-index:7;font:800 110px Inter;color:#D0202A;text-shadow:0 4px 14px #000}
.pr{position:absolute;z-index:7;font:800 18px Inter;color:#EFE6D2;background:#8E1B1B;padding:6px 12px;letter-spacing:2px}'''
PV={'c1':('right:70px;bottom:150px;width:250px','left:20%;top:12%;width:60%;height:50%','right:330px;bottom:330px','↖'),
'c2':('right:60px;top:120px;width:300px','left:22%;top:12%;width:60%;height:70%','right:370px;top:330px','↙'),
'c3':('right:56px;top:120px;width:380px','left:30%;top:20%;width:45%;height:70%','right:300px;top:340px','↙'),
'c4':('left:60px;top:420px;width:380px','left:8%;top:5%;width:84%;height:90%','left:430px;top:330px','↗'),
'c5':('right:56px;top:120px;width:300px','left:5%;top:5%;width:60%;height:60%','right:370px;top:360px','↙')}
h=['<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Anton&family=Cinzel:wght@600;800&family=Inter:wght@500;800&display=swap" rel="stylesheet"><style>'+css+'</style></head><body>']
for c,f,pos,hk,t in CAPAS:
    shutil.copy(IM+f,os.path.join(D,'capas-v2',c+'-fundo.jpg'))
    h.append(f'<section class="f {pos}" id="{c}-01-v2"><img class="bg" src="capas-v2/{c}-fundo.jpg"><div class="vg"></div><div class="gr"></div><div class="gn"></div>'
      f'<div class="et"><span>THE ECONOMIST · 2027</span><span>ARRASTE →</span></div><div class="tx"><div class="hk">{hk}</div><h1>{t}</h1></div>'
      f'<div class="pv" style="{PV[c][0]}"><img src="capas-v2/{c}-prova.jpg"><div class="ci" style="{PV[c][1]}"></div><div class="cap">FOTO REAL · THE ECONOMIST</div></div><div class="ar" style="{PV[c][2]}">{PV[c][3]}</div><div class="selo"><i>R</i> RAPOSA E LEÃO</div><div class="ia">imagem gerada por IA</div></section>')
open(os.path.join(D,'capas-v2.html'),'w').write(''.join(h)+'</body></html>')
