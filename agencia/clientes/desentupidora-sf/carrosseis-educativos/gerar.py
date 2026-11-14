# Desentupidora SF · 4 carrosséis educativos sobre entupimento (conta Lindson, 14/11/2026)
# Gera carrosseis.html (cada tela 1080x1350); render.js tira as capturas.
import json,os,html
D=os.path.dirname(os.path.abspath(__file__))
WA='(98) 92010-5710'; AT='@desentupidorasf_slz'
CSS='''
@font-face{font-family:MBI;src:url(fonts/Montserrat-BlackItalic.ttf)}@font-face{font-family:MB;src:url(fonts/Montserrat-Bold.ttf)}
*{margin:0;padding:0;box-sizing:border-box}body{background:#888}
.s{width:1080px;height:1350px;position:relative;overflow:hidden;font-family:MB;color:#061a4a}
.t{font-family:MBI;text-transform:uppercase;line-height:.95;letter-spacing:-.01em}
.bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.sig{position:absolute;left:56px;bottom:46px;display:flex;align-items:center;gap:18px;font-size:24px}
.sig img{width:78px;height:78px;border-radius:50%;box-shadow:0 0 0 4px #fff}
.sig b{display:block;font-size:26px}.n{position:absolute;right:56px;bottom:62px;font-size:24px;opacity:.75}
.tag{display:inline-block;background:#ff8a00;color:#061a4a;font-family:MBI;text-transform:uppercase;font-size:30px;padding:12px 24px;border-radius:12px}
.grain:after{content:"";position:absolute;inset:0;background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='3'/><feColorMatrix values='0 0 0 0 .5 0 0 0 0 .5 0 0 0 0 .5 0 0 0 .9 0'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>");opacity:.06;mix-blend-mode:overlay;pointer-events:none}
.p{font-size:38px;line-height:1.35}
'''
def sig(dark=True,i=1,n=7):
    c='#fff' if dark else '#061a4a'; c2='rgba(255,255,255,.85)' if dark else '#1d5fd0'
    return f'<div class="sig" style="color:{c}"><img src="img/logo.jpg"><div><b>{AT}</b><span style="color:{c2}">WhatsApp {WA}</span></div></div><div class="n" style="color:{c}">{i}/{n}</div>'

# ---------- layouts (nenhuma tela repete o layout da anterior) ----------
def capa(img,tag,l1,l2,i):
    return f'''<section class="s grain" style="background:#061a4a"><img class="bg" src="img/{img}" style="filter:saturate(1.05)">
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(6,26,74,.15) 30%,rgba(6,26,74,.95) 72%)"></div>
<div style="position:absolute;left:56px;right:56px;bottom:190px"><span class="tag">{tag}</span>
<div class="t" style="font-size:104px;color:#fff;margin-top:26px">{l1}</div><div class="t" style="font-size:104px;color:#ff8a00">{l2}</div>
<div style="color:#fff;font-size:30px;margin-top:22px;opacity:.9">Arraste para o lado →</div></div>{sig(True,i)}</section>'''
def numero(num,tit,txt,i,bg='#f4f8ff'):
    return f'''<section class="s grain" style="background:{bg}"><div class="t" style="position:absolute;right:-30px;top:-80px;font-size:620px;color:#1d5fd0;opacity:.12">{num}</div>
<div style="position:absolute;left:72px;right:72px;top:150px"><div class="t" style="font-size:150px;color:#ff8a00">{num}</div>
<div class="t" style="font-size:80px;margin-top:10px">{tit}</div><div style="width:120px;height:12px;background:#1d5fd0;margin:40px 0"></div>
<p class="p">{txt}</p></div>{sig(False,i)}</section>'''
def split(img,num,tit,txt,i):
    return f'''<section class="s grain" style="background:#0a2a6e;color:#fff"><img src="img/{img}" style="position:absolute;left:0;top:0;width:1080px;height:640px;object-fit:cover">
<div style="position:absolute;left:0;right:0;top:600px;height:80px;background:linear-gradient(180deg,transparent,#0a2a6e)"></div>
<div style="position:absolute;left:72px;right:72px;top:660px"><span class="tag">{num}</span><div class="t" style="font-size:70px;margin-top:24px">{tit}</div>
<p class="p" style="margin-top:24px;color:#dfe9ff">{txt}</p></div>{sig(True,i)}</section>'''
def frase(t1,t2,txt,i):
    return f'''<section class="s grain" style="background:#ff8a00"><div style="position:absolute;left:72px;right:72px;top:230px">
<div class="t" style="font-size:112px;color:#061a4a">{t1}</div><div class="t" style="font-size:112px;color:#fff">{t2}</div>
<p class="p" style="margin-top:46px;font-size:40px">{txt}</p></div>{sig(False,i)}</section>'''
def lista(tit,itens,i,img=None):
    li=''.join(f'<div style="display:flex;gap:26px;align-items:flex-start;margin-bottom:30px"><div class="t" style="min-width:74px;height:74px;border-radius:18px;background:#1d5fd0;color:#fff;font-size:40px;display:flex;align-items:center;justify-content:center">{k+1}</div><div style="font-size:36px;line-height:1.3;padding-top:8px">{x}</div></div>' for k,x in enumerate(itens))
    pic=f'<img src="img/{img}" style="position:absolute;right:-60px;top:-60px;width:420px;height:420px;object-fit:cover;border-radius:50%;border:14px solid #ff8a00">' if img else ''
    return f'''<section class="s grain" style="background:#fff">{pic}<div style="position:absolute;left:72px;right:72px;top:{360 if img else 140}px">
<div class="t" style="font-size:74px;margin-bottom:50px;max-width:{620 if img else 940}px">{tit}</div>{li}</div>{sig(False,i)}</section>'''
def versus(img,errado,certo,i):
    return f'''<section class="s grain" style="background:#061a4a;color:#fff"><div style="position:absolute;left:56px;right:56px;top:110px;display:grid;gap:28px">
<div style="background:#2a0f12;border:4px solid #e5484d;border-radius:28px;padding:40px"><div class="t" style="color:#ff6b6b;font-size:44px">✕ O que piora</div><p class="p" style="margin-top:18px">{errado}</p></div>
<div style="background:#0d3a7a;border:4px solid #3fa9ff;border-radius:28px;padding:40px;display:flex;gap:30px;align-items:center">
<div style="flex:1"><div class="t" style="color:#3fa9ff;font-size:44px">✓ O jeito certo</div><p class="p" style="margin-top:18px">{certo}</p></div>
{f'<img src="img/{img}" style="width:300px;height:380px;object-fit:cover;border-radius:20px">' if img else ''}</div></div>{sig(True,i)}</section>'''
def cartao(img,tit,txt,i):
    return f'''<section class="s grain" style="background:#1d5fd0">{f'<img class="bg" src="img/{img}" style="opacity:.25;filter:grayscale(1)">' if img else '<img src="img/logo.jpg" style="position:absolute;right:-180px;bottom:-140px;width:760px;border-radius:50%;opacity:.14">'}
<div style="position:absolute;left:64px;right:64px;top:200px;background:#fff;border-radius:34px;padding:60px;box-shadow:0 30px 80px rgba(0,0,0,.3)">
<div style="height:16px;background:#ff8a00;margin:-60px -60px 46px;border-radius:34px 34px 0 0"></div>
<div class="t" style="font-size:72px">{tit}</div><p class="p" style="margin-top:30px">{txt}</p></div>{sig(True,i)}</section>'''
def passos(img,i):
    st=[('Mande a foto','Do ralo, da pia ou da caixa, aqui no WhatsApp.'),('Orçamento grátis','A gente avalia e passa o valor antes de qualquer coisa.'),('Técnico na sua porta','Uniformizado, com máquina de cabo rotativo, sem quebra-quebra.'),('Teste na hora','O escoamento é testado na sua frente.')]
    li=''.join(f'<div style="display:flex;gap:24px;margin-bottom:26px"><div class="t" style="font-size:64px;color:#ff8a00;min-width:70px">{k+1}</div><div><div class="t" style="font-size:40px;color:#fff">{a}</div><div style="font-size:30px;color:#dfe9ff;margin-top:6px">{b}</div></div></div>' for k,(a,b) in enumerate(st))
    return f'''<section class="s grain" style="background:#061a4a"><img src="img/{img}" style="position:absolute;left:0;top:0;width:1080px;height:420px;object-fit:cover">
<div style="position:absolute;left:0;right:0;top:330px;height:90px;background:linear-gradient(180deg,transparent,#061a4a)"></div>
<div style="position:absolute;left:72px;right:72px;top:450px"><div class="t" style="font-size:66px;color:#fff;margin-bottom:34px">Como a <span style="color:#ff8a00">SF</span> resolve</div>{li}</div>{sig(True,i)}</section>'''
def cta(img,t1,t2,i,real=False):
    return f'''<section class="s grain" style="background:#061a4a"><img class="bg" src="img/{img}" style="{'object-position:center 20%' if not real else 'filter:saturate(1.1)'}">
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(6,26,74,.05) 25%,rgba(6,26,74,.96) 62%)"></div>
<div style="position:absolute;left:64px;right:64px;bottom:200px"><div class="t" style="font-size:88px;color:#fff">{t1}</div><div class="t" style="font-size:88px;color:#ff8a00">{t2}</div>
<div style="margin-top:34px;display:inline-flex;align-items:center;gap:18px;background:#ff8a00;border-radius:999px;padding:24px 40px"><span class="t" style="font-size:40px;color:#061a4a">WhatsApp {WA}</span></div>
<div style="color:#fff;font-size:30px;margin-top:22px">Orçamento grátis · Sem quebra-quebra · Teste na hora</div></div>{sig(True,i)}</section>'''

C={
'1-sinais':[capa('cena_v1c1.jpg','Antes de entupir','5 sinais que','o cano dá',1),
 numero('01','Cheiro ruim que não passa','Mesmo com tudo limpo, o mau cheiro volta pelo ralo ou pela pia. É sinal de sujeira e gordura parada dentro do cano.',2),
 split('cena_v2c3.jpg','Sinal 02','A água demora pra descer','Pia, ralo ou chuveiro escoando devagar: o cano já está estreito por dentro. Daqui a pouco, para de vez.',3),
 frase('Barulho de','"glub glub"?','Quando o ralo gorgoleja depois que a água desce, é ar preso tentando passar pela sujeira. Sinal 03.',4),
 lista('Sinais 04 e 05',['Água voltando pelo ralo do box ou da área de serviço.','Mosquinhas perto da pia e do ralo: elas gostam de resto de comida e gordura.','Se apareceu mais de um sinal, não espere alagar.'],5,'jovem.png'),
 cartao('cena_v4c1.jpg','Quanto antes, melhor','Entupimento pequeno vira grande quando a gente espera. Resolver no começo evita água suja voltando dentro de casa.',6),
 cta('tecnica.png','Viu algum','desses sinais?',7)],
'2-nao-jogue':[capa('cena_v2c1.jpg','Pia e vaso','O que nunca','jogar no ralo',1),
 numero('01','Óleo de fritura','É o campeão de entupimento. Quente ele desce fácil; no cano, esfria e vira uma crosta que vai fechando a passagem.',2,'#fff'),
 split('cena_v2c2.jpg','Por dentro do cano','A gordura gruda e endurece','Cada vez que o óleo desce, uma camada nova se junta à anterior. Um dia a água não passa mais.',3),
 lista('Também entopem a pia',['Borra de café.','Restos de comida, arroz e casca.','Farinha e massa crua.','Água de fritura "com detergente": a gordura endurece mais pra frente.'],4),
 versus('vaso.png','Lenço umedecido, fio dental, absorvente, cabelo e cotonete no vaso. Eles não se desfazem na água e formam um bolo no cano.','No vaso, só papel higiênico. O resto vai no lixo do banheiro.',5),
 frase('Óleo usado','tem destino certo','Espere esfriar, guarde numa garrafa PET fechada e leve a um ponto de coleta para reciclagem.',6),
 cta('tecnico2.png','Já entupiu?','A SF resolve.',7)],
'3-caixa-gordura':[capa('padaria.png','Cozinha de casa e de restaurante','Caixa de','gordura cheia?',1),
 cartao('padeiro.png','O que é a caixa de gordura','É a caixinha que segura a gordura da pia da cozinha antes de ela ir para o esgoto. Quando enche, a gordura passa direto e entope o cano.',2),
 lista('Sinais de que ela está cheia',['Cheiro forte de gordura e esgoto perto da cozinha.','Pia da cozinha descendo devagar.','Água voltando pela pia ou pelo ralo da área.','Tampa com gordura subindo pelas bordas.'],3),
 split('garagem.png','Condomínio e empresa','Caixa coletiva enche mais rápido','Em prédio, restaurante, lanchonete e padaria, muita gente usa a mesma caixa. Ela precisa de atenção com mais frequência.',4),
 frase('Limpar antes','é melhor','do que parar a cozinha no meio do almoço com a pia transbordando.',5),
 numero('?','De quanto em quanto tempo?','Depende do uso: quanto mais fritura e movimento, mais vezes. Na dúvida, mande uma foto da caixa aberta que a gente avalia.',6),
 cta('caixa-esgoto.jpg','Mande a foto','da sua caixa',7,real=True)],
'4-mitos':[capa('calha.png','Mitos do entupimento','Soda, arame e','água fervendo?',1),
 versus(None,'Soda cáustica: é corrosiva, pode danificar o cano e causa queimaduras graves na pele e nos olhos.','Chamar quem desentope com equipamento, sem produto agressivo dentro de casa.',2),
 numero('02','Arame e cabide','Em vez de tirar a sujeira, o arame costuma empurrar o entupimento mais pra dentro e ainda pode furar ou rachar o cano.',3,'#fff'),
 split('cena_v3c4.jpg','Mito 03','Água fervendo resolve gordura','Derrete só por um momento. Alguns metros depois a gordura esfria e endurece de novo, num lugar mais difícil de alcançar.',4),
 cartao(None,'O jeito certo: cabo rotativo','A máquina leva um cabo de aço girando até o ponto do entupimento e desfaz a sujeira por dentro. Na maioria dos casos, sem quebrar piso nem parede.',5),
 passos('veiculo-van.png',6),
 cta('veiculo-moto.png','Entupiu?','Chama a SF.',7)]}

page=f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>'
for k,ss in C.items(): page+=''.join(s.replace('<section',f'<section data-c="{k}"',1) for s in ss)
open(os.path.join(D,'carrosseis.html'),'w').write(page+'</body></html>')
print('ok',sum(len(v) for v in C.values()),'telas')
