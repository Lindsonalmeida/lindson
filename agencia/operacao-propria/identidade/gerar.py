# Identidade visual Orégano Turbo v1 (conta Leandro, 05/11/2026) · Brand Squad + Design Squad
# Referências combinadas (TEMPLATE.md): Delivereasy (Colenso BBDO, Best Awards NZ 2024) · Pitstop Pizza (Akuma Studio) · Yazio (Koto, 2025).
# Gera pecas.html com: prancha da marca (5 páginas 4:5), avatar 1080, 6 capas de destaque, 1 post de exemplo.
# Uso: python3 mascote.py && python3 gerar.py && node render.js
import os
from mascote import mascote
VERDE, VERDE2, AMARELO, TOMATE, ASFALTO, CREME = '#2FA35A', '#1F8A4C', '#FFC81E', '#E8432E', '#141414', '#FFF3DC'
M = lambda **k: mascote(**k).replace('<svg ', '<svg width="100%" height="100%" ')
def selo(tam, fundo=AMARELO, **k):  # símbolo: mascote dentro do círculo amarelo
    return f'<div style="width:{tam}px;height:{tam}px;border-radius:50%;background:{fundo};display:grid;place-items:center;overflow:hidden"><div style="width:{int(tam*.92)}px;height:{int(tam*.92)}px;margin-left:{int(tam*.04)}px">{M(**k)}</div></div>'
def nome(tam, c1=ASFALTO, c2=TOMATE, sub=True, csub=None):  # wordmark: Rubik Black Itálico
    return (f'<div class="wm" style="font-size:{tam}px"><span style="color:{c1}">ORÉGANO</span><span style="color:{c2}">TURBO</span></div>'
            + (f'<div class="sub" style="font-size:{max(12, int(tam*.2))}px;color:{csub or c1}">MKT PARA PIZZARIAS</div>' if sub else ''))
def assinatura(tam, fundo=AMARELO, c1=ASFALTO, c2=TOMATE, cselo=AMARELO):
    return f'<div style="display:flex;align-items:center;gap:{int(tam*.25)}px">{selo(int(tam*1.9), cselo)}<div>{nome(tam, c1, c2)}</div></div>'
P = []  # (id, largura, altura, fundo, html)
ROT = lambda t, c=ASFALTO: f'<div class="rot" style="color:{c}">{t}</div>'
# 1 · capa da prancha
P.append(('prancha-01-capa', 1080, 1350, AMARELO, f'''
<div class="a" style="left:-60px;top:60px;width:1200px;font:italic 900 330px/.82 Rubik;color:rgba(20,20,20,.06);letter-spacing:-.04em">TURBO TURBO TURBO</div>
<div class="a" style="left:80px;top:80px">{ROT('Identidade visual · v1 · 05/11/2026')}</div>
<div class="a" style="left:190px;top:200px;width:700px;height:700px">{M()}</div>
<div class="a" style="left:80px;top:890px">{nome(118)}</div>
<div class="a" style="left:84px;top:1215px;font:600 34px/1.3 Inter;color:{ASFALTO};width:900px">O toque final que acelera a sua pizzaria.</div>'''))
# 2 · logo
P.append(('prancha-02-logo', 1080, 1350, CREME, f'''
<div class="a" style="left:80px;top:80px">{ROT('Logo · assinatura, símbolo e versões')}</div>
<div class="a" style="left:80px;top:150px;width:920px;height:330px;border-radius:28px;background:{AMARELO};display:grid;place-items:center">{assinatura(78)}</div>
<div class="a" style="left:80px;top:510px;width:450px;height:330px;border-radius:28px;background:{ASFALTO};display:grid;place-items:center">{assinatura(38, ASFALTO, '#fff', AMARELO)}</div>
<div class="a" style="left:550px;top:510px;width:450px;height:330px;border-radius:28px;background:{VERDE2};display:grid;place-items:center">{assinatura(38, VERDE2, '#fff', AMARELO, AMARELO)}</div>
<div class="a" style="left:80px;top:870px;width:290px;height:290px;border-radius:28px;background:#fff;display:grid;place-items:center">{selo(210)}</div>
<div class="a" style="left:395px;top:870px;width:290px;height:290px;border-radius:28px;background:{TOMATE};display:grid;place-items:center">{selo(210, AMARELO, boca='piscada', olhar=(6, 2))}</div>
<div class="a" style="left:710px;top:870px;width:290px;height:290px;border-radius:28px;background:#fff;display:grid;place-items:center;text-align:center">{nome(44, sub=False)}</div>
<div class="a" style="left:80px;top:1190px;width:920px;font:500 22px/1.45 Inter;color:{ASFALTO}">Assinatura = símbolo (mascote no círculo amarelo) + nome em Rubik Black itálico, ORÉGANO na cor do texto e TURBO em vermelho tomate. Área de proteção: meia altura do símbolo em volta. Tamanho mínimo: símbolo 48 px · assinatura 220 px.</div>'''))
# 3 · cores e letras
cores = [('Amarelo Turbo', AMARELO, '255 200 30', '40%', ASFALTO), ('Asfalto', ASFALTO, '20 20 20', '25%', '#fff'), ('Verde Orégano', VERDE, '47 163 90', '15%', '#fff'),
         ('Vermelho Tomate', TOMATE, '232 67 46', '10%', '#fff'), ('Creme Massa', CREME, '255 243 220', '10%', ASFALTO)]
P.append(('prancha-03-cores-letras', 1080, 1350, '#fff', f'''
<div class="a" style="left:80px;top:80px">{ROT('Cores e letras')}</div>
<div class="a" style="left:80px;top:140px;width:920px;display:flex;height:430px;border-radius:28px;overflow:hidden">{''.join(f'<div style="flex:{p[:-1]};background:{h};color:{t};padding:24px 16px;display:flex;flex-direction:column;justify-content:flex-end;font:600 17px/1.35 Inter"><b style="font:italic 900 24px/1.05 Rubik">{n}</b>{h}<br>RGB {r}<br>uso {p}</div>' for n, h, r, p, t in cores)}</div>
<div class="a" style="left:80px;top:620px;width:920px">
 <div style="font:italic 900 128px/.9 Rubik;color:{ASFALTO};letter-spacing:-.02em">PIZZA BOA<br><span style="color:{TOMATE}">NÃO BASTA.</span></div>
 <div style="font:600 22px Inter;color:#666;margin:14px 0 38px">Títulos · Rubik Black Itálico (900) · caixa alta · Google Fonts</div>
 <div style="font:700 44px/1.15 Inter;color:{ASFALTO}">Pedido direto no seu WhatsApp, todo dia da semana.</div>
 <div style="font:400 28px/1.5 Inter;color:#333;margin-top:14px">Textos · Inter (400, 600, 700). Simples, de conversa, como no balcão da pizzaria. Números e preços em Inter 700.</div>
 <div style="font:600 22px Inter;color:#666;margin-top:24px">Proporção: amarelo domina, asfalto dá contraste, verde e tomate são os acentos.</div></div>'''))
# 4 · mascote
P.append(('prancha-04-mascote', 1080, 1350, CREME, f'''
<div class="a" style="left:80px;top:80px">{ROT('O mascote · a folhinha de orégano')}</div>
<div class="a" style="left:80px;top:150px;width:920px;font:italic 900 74px/.95 Rubik;color:{ASFALTO}">O TEMPERO QUE<br><span style="color:{VERDE2}">ACELERA.</span></div>
{''.join(f'<div class="a" style="left:{80 + i*310}px;top:380px;width:290px;height:340px;border-radius:28px;background:{bg};padding:10px"><div style="height:270px">{M(**k)}</div><div style="text-align:center;font:italic 900 26px Rubik;color:{c}">{t}</div></div>' for i, (k, t, bg, c) in enumerate([({}, 'BORA!', AMARELO, ASFALTO), ({'boca': 'uau', 'olhar': (0, -4)}, 'UAU!', TOMATE, '#fff'), ({'boca': 'piscada', 'olhar': (6, 2)}, 'SE LIGA', VERDE2, '#fff')]))}
<div class="a" style="left:80px;top:770px;width:920px;font:400 27px/1.55 Inter;color:{ASFALTO}">
<b>Quem é:</b> o detalhe pequeno que muda a pizza inteira, como o marketing faz com a pizzaria. Óculos de corrida e lenço ao vento: está sempre com pressa de trazer pedido.<br><br>
<b>Regras:</b> sempre de frente ou com o lenço para trás (indo para a frente); nunca triste, nunca bravo, nunca segurando dinheiro; não deformar nem trocar as cores; linhas de velocidade só atrás dele. Expressões novas seguem o mesmo traço (próximas: apontando, comemorando, com o celular).</div>'''))
# 5 · aplicações
P.append(('prancha-05-aplicacoes', 1080, 1350, ASFALTO, f'''
<div class="a" style="left:80px;top:80px">{ROT('Aplicações · Instagram @oreganoturbo', '#fff')}</div>
<div class="a" style="left:80px;top:150px;display:flex;align-items:center;gap:30px">{selo(190)}<div style="color:#fff;font:400 24px/1.4 Inter"><b style="font:700 28px Inter">oreganoturbo</b><br>Orégano Turbo · Mkt Pizzarias<br><span style="color:#bbb">O toque final que acelera a sua pizzaria 🌿🏁</span></div></div>
<div class="a" style="left:80px;top:390px;display:flex;gap:26px">{''.join(f'<div style="text-align:center"><div style="width:130px;height:130px;border-radius:50%;border:4px solid #444;padding:6px"><div style="width:100%;height:100%;border-radius:50%;background:{bg};display:grid;place-items:center;font:italic 900 {fs}px/1 Rubik;color:{c}">{t}</div></div><div style="color:#ddd;font:500 18px Inter;margin-top:10px">{n}</div></div>' for t, n, bg, c, fs in [('RAIO<br>X', 'Raio-X', AMARELO, ASFALTO, 34), ('1·2·3', 'Como funciona', TOMATE, '#fff', 30), ('CASES', 'Cases', VERDE2, '#fff', 28), ('R$', 'Planos', AMARELO, TOMATE, 46), ('REC', 'Bastidores', '#fff', TOMATE, 34), ('?!', 'Dúvidas', VERDE, '#fff', 54)])}</div>
<div class="a" style="left:80px;top:610px;width:440px;height:550px;border-radius:24px;overflow:hidden;background:{AMARELO};padding:34px">
 <div style="font:italic 900 52px/.92 Rubik;color:{ASFALTO}">SUA PIZZARIA<br>VENDE NO SÁBADO<br><span style="color:{TOMATE}">E PARA NA TERÇA?</span></div>
 <div style="position:absolute;right:-20px;bottom:40px;width:270px;height:270px">{M(boca='uau', olhar=(0, -4))}</div>
 <div style="position:absolute;left:34px;bottom:34px;font:700 18px Inter;color:{ASFALTO}">@oreganoturbo</div></div>
<div class="a" style="left:560px;top:610px;width:440px;height:550px;border-radius:24px;overflow:hidden;background:{VERDE2};padding:34px;color:#fff">
 <div style="font:600 18px Inter;letter-spacing:.2em;color:{AMARELO}">PROMESSA</div>
 <div style="font:italic 900 50px/.95 Rubik;margin-top:14px">SEU ANÚNCIO SE PAGA EM PEDIDO.</div>
 <div style="font:500 26px/1.35 Inter;margin-top:18px">Ou o próximo mês é por nossa conta.</div>
 <div style="position:absolute;right:30px;bottom:30px">{selo(120)}</div></div>
<div class="a" style="left:80px;top:1195px;color:#aaa;font:500 20px/1.4 Inter;width:920px">Posts alternam amarelo · verde · asfalto · tomate, nunca dois seguidos na mesma cor. O mascote aparece em todo post de chamada; foto real de pizza e da pizzaria cliente entra nos cases.</div>'''))
# avatar e destaques (arquivos para subir no Instagram)
P.append(('avatar', 1080, 1080, AMARELO, f'<div class="a" style="left:60px;top:70px;width:960px;height:960px">{M(velocidade=False)}</div>'))
for i, (t, n, bg, c, fs) in enumerate([('RAIO<br>X', 'raio-x', AMARELO, ASFALTO, 200), ('1·2·3', 'como-funciona', TOMATE, '#fff', 170), ('CASES', 'cases', VERDE2, '#fff', 160), ('R$', 'planos', AMARELO, TOMATE, 260), ('REC', 'bastidores', '#fff', TOMATE, 200), ('?!', 'duvidas', VERDE, '#fff', 300)], 1):
    P.append((f'destaque-{i}-{n}', 1080, 1920, bg, f'<div class="a" style="left:0;top:0;width:1080px;height:1920px;display:grid;place-items:center;text-align:center;font:italic 900 {fs}px/.9 Rubik;color:{c}">{t}</div>'))
P.append(('post-exemplo-1', 1080, 1350, AMARELO, f'''
<div class="a" style="left:-40px;top:900px;width:1200px;font:italic 900 300px/.8 Rubik;color:rgba(20,20,20,.06)">TERÇA</div>
<div class="a" style="left:80px;top:110px;font:italic 900 96px/.92 Rubik;color:{ASFALTO};white-space:nowrap">SUA PIZZARIA<br>VENDE NO SÁBADO<br><span style="color:{TOMATE}">E PARA NA TERÇA?</span></div>
<div class="a" style="left:84px;top:450px;width:520px;font:500 36px/1.35 Inter;color:{ASFALTO}">Tem conserto. E começa por pedido direto no seu WhatsApp.</div>
<div class="a" style="left:500px;top:640px;width:620px;height:620px">{M(boca='uau', olhar=(0, -4))}</div>
<div class="a" style="left:80px;top:1200px;display:flex;align-items:center;gap:16px">{selo(84)}<div style="font:700 28px Inter;color:{ASFALTO}">@oreganoturbo</div></div>'''))
CSS = f'''*{{margin:0;padding:0;box-sizing:border-box}}body{{background:#333}}.f{{position:relative;overflow:hidden;margin-bottom:20px}}.a{{position:absolute}}
.wm{{font-family:Rubik;font-weight:900;font-style:italic;line-height:.86;letter-spacing:-.02em;display:flex;flex-direction:column}}
.sub{{font:700 1em Inter;letter-spacing:.32em;margin-top:.6em}}.rot{{font:700 20px Inter;letter-spacing:.24em;text-transform:uppercase}}'''
html = ('<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Rubik:ital,wght@1,900&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">'
        f'<style>{CSS}</style></head><body>' + ''.join(f'<section class="f" id="{i}" style="width:{w}px;height:{h}px;background:{bg}">{c}</section>' for i, w, h, bg, c in P) + '</body></html>')
open('pecas.html', 'w').write(html); print(len(P), 'peças')
