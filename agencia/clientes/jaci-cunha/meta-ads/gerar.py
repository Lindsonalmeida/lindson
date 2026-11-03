# 10 criativos de Meta Ads da Dra. Jaci (1080×1350). Cada um copia uma composição de post real dela (comentário em cada layout).
# Anúncio: sem foto com produto (frasco/caixa), CTA "Chame no WhatsApp", texto curto. Conta Lindson, 03/11/2026.
import sys, json
d, FOT = sys.argv[1], sys.argv[2]
exec(open(f'{d}/base.py').read().replace("F='FOTOS'", f"F='{FOT}'"))
A = json.load(open(f'{d}/criativos.json'))
CTA = lambda c, cor='#fff', bd='#fff': f'<div class="pill" style="color:{cor};border-color:{bd}">{c} →</div>'
def L(n, a):
    s, b, c = a['serif'], md(a['sans']), a.get('cta', 'Chame no WhatsApp')
    if n == 0:  # "botox · O QUE NINGUÉM RESPONDE": balão + serif gigante
        return (foto('jaci-preto-sorriso-aberto.jpg', '50% 18%') + '<div class="a" style="inset:0;background:linear-gradient(180deg,rgba(0,0,0,0) 45%,rgba(0,0,0,.5) 100%)"></div>' + topo() +
          f'<div class="a" style="left:0;width:1080px;top:760px;text-align:center"><div class="S" style="color:#fff;font-size:{150 if len(s) < 14 else 92}px;line-height:.95;padding:0 70px">{s}</div><div class="sans" style="color:#fff;margin-top:12px">{b}</div>{CTA(c)}</div>' + rodape('#fff', True))
    if n == 1:  # "Bioestimulador de Colágeno": faixa dourada com fio
        return (foto('jaci-nude-sofa-corpo-inteiro.jpg', '50% 30%') + '<div class="a" style="inset:0;background:linear-gradient(180deg,rgba(0,0,0,0) 45%,rgba(0,0,0,.5) 100%)"></div>' + topo(OURO) +
          f'<div class="a" style="left:0;width:1080px;top:820px;text-align:center"><div class="fio"><i></i><span class="S" style="font-size:{64 if len(s) < 28 else 50}px">{s}</span><i></i></div><div class="sans u" style="color:#fff">{b}</div>{CTA(c)}</div>' + rodape('#fff', True))
    if n == 2:  # "Preenchimento facial, por que alguns ficam…": faixa translúcida + sans com bold
        return (foto('jaci-preto-mao-no-cabelo.jpg', '50% 20%') + '<div class="a" style="inset:0;background:linear-gradient(180deg,rgba(0,0,0,0) 40%,rgba(0,0,0,.55) 100%)"></div>' + topo() +
          f'<div class="a" style="left:0;width:1080px;top:780px;text-align:center"><span class="faixa S" style="font-size:66px">{s}</span><div class="sans" style="color:#fff;font-size:38px;line-height:1.2;margin:12px 80px 0;font-weight:400">{b}</div>{CTA(c)}</div>' + rodape('#fff', True))
    if n == 3:  # "Entramos na reta final do ano… / E EU SEMPRE AVISO": texto à esquerda + faixas vinho à direita
        return (foto('jaci-branco-cadeira-sorrindo.jpg', '60% 30%') + '<div class="a" style="inset:0;background:linear-gradient(0deg,rgba(0,0,0,.4) 0,rgba(0,0,0,0) 40%)"></div>' + topo(CAFE) +
          f'<div class="a" style="left:96px;top:290px;width:420px;color:{CAFE}"><div class="S" style="font-size:70px;line-height:1">{s}</div></div>'
          f'<div class="a" style="right:96px;top:960px;text-align:right">' + ''.join(f'<div><span class="fv">{md(x)}</span></div>' for x in a['sans'].split(' / ')) + f'{CTA(c)}</div>' + rodape())
    if n == 4:  # "frases que eu amo ouvir": frases curtas espalhadas em volta dela + título com faixa
        fr = ['"dói?"', '"vai ficar natural?"', '"quanto tempo dura?"', '"posso trabalhar no mesmo dia?"']  # perguntas que ela ouve (não são depoimentos: nada de avaliação inventada)
        pos = [(110, 330), (720, 330), (90, 560), (740, 600)]
        return (foto('jaci-off-white-sofa-sorrindo.jpg', '50% 25%', 'filter:brightness(1.05)') + topo(CAFE) +
          ''.join(f'<div class="a S" style="left:{x}px;top:{y}px;width:270px;text-align:center;font-size:30px;line-height:1.1;color:{CAFE}">{t}</div>' for (x, y), t in zip(pos, fr)) +
          '<div class="a" style="inset:0;background:linear-gradient(180deg,rgba(0,0,0,0) 55%,rgba(40,25,20,.6) 100%)"></div>' + f'<div class="a" style="left:0;width:1080px;top:820px;text-align:center"><span class="faixa S" style="font-size:72px;background:rgba(185,162,122,.85)">{s}</span><div class="sans" style="color:#fff;margin:14px 90px 0;text-shadow:0 2px 10px rgba(0,0,0,.5)">{b}</div>{CTA(c)}</div>' + rodape('#fff'))
    if n == 5:  # "checklist do pós botox": tablet + palavra gigante serif fina + faixa vinho
        return (foto('jaci-off-white-tablet.jpg', '50% 25%') + '<div class="a" style="inset:0;background:linear-gradient(180deg,rgba(0,0,0,0) 45%,rgba(0,0,0,.6) 100%)"></div>' + topo() +
          f'<div class="a" style="left:0;width:1080px;top:820px;text-align:center"><span class="fv" style="font-size:30px;text-transform:none;font-weight:500;max-width:860px;line-height:1.3">{b}</span>'
          f'<div class="S" style="padding:0 60px;text-shadow:0 4px 20px rgba(0,0,0,.35);font-size:{170 if len(s) < 10 else 92}px;line-height:1;color:#fff;font-style:normal;font-weight:400;margin-top:-4px">{s}</div>{CTA(c)}</div>' + rodape('#fff'))
    if n == 6:  # tríptico "a artista:" → foto nítida dividida + creme
        return (f'<div class="a" style="inset:0;background:{CREME}"></div><img class="a" src="{F}/jaci-nude-sofa-corpo-inteiro.jpg" style="right:0;top:0;width:520px;height:1350px;object-fit:cover;object-position:40% 30%">' + topo(CAFE) +
          f'<div class="a" style="left:88px;width:440px;top:260px;height:880px;display:flex;flex-direction:column;justify-content:center;color:{CAFE}"><div class="S" style="font-size:{64 if len(s) < 26 else 50}px;line-height:1.05">{s}</div>'
          f'<div class="sans" style="margin-top:22px;font-size:32px;line-height:1.3">{b}</div><div>{CTA(c, VINHO, VINHO)}</div></div>' + rodape(CAFE))
    if n == 7:  # "Antes de qualquer procedimento, eu observo": faixa café + sans itálico + pílula
        return (foto('jaci-preto-mao-no-cabelo.jpg', '40% 15%', 'transform:scaleX(-1)') + '<div class="a" style="inset:0;background:linear-gradient(180deg,rgba(0,0,0,0) 45%,rgba(0,0,0,.55) 100%)"></div>' + topo() +
          f'<div class="a" style="left:0;width:1080px;top:790px;text-align:center"><span class="faixa S" style="font-size:60px;background:{CAFE}">{s}</span>'
          f'<div class="sans" style="color:#fff;font-size:34px;font-style:italic;font-weight:400;margin:16px auto 0;width:820px;line-height:1.3">{b}</div>{CTA(c)}</div>' + rodape('#fff', True))
    if n == 8:  # creme tipográfico com número dourado e faixa com fio (tela de carrossel aprovada)
        return (f'<div class="a" style="inset:0;background:{CREME}"></div>' + topo(CAFE) +
          f'<div class="a" style="left:0;width:1080px;top:{300 if a.get("numero") else 470}px;text-align:center;color:{CAFE}">{f'<div class="S" style="font-size:240px;line-height:1;color:{OURO}">{a["numero"]}</div>' if a.get('numero') else '<div style="height:60px"></div>'}'
          f'<div class="fio"><i></i><span class="S" style="font-size:72px">{s}</span><i></i></div><div class="sans" style="width:800px;margin:30px auto 0;font-size:36px;line-height:1.35">{b}</div>{CTA(c, VINHO, VINHO)}</div>' + rodape(CAFE))
    # 9: cor invertida vinho (faixas vinho de "E EU SEMPRE AVISO")
    return (f'<div class="a" style="inset:0;background:radial-gradient(900px 800px at 30% 20%,#86283B,{VINHO} 60%,#4A0F1B)"></div>' + topo('#F3EADD') +
      f'<div class="a" style="left:110px;width:860px;top:300px;height:820px;display:flex;flex-direction:column;justify-content:center;color:#F7EFE6"><div class="S" style="font-size:80px;line-height:1.05;border-left:4px solid {OURO};padding-left:26px">{s}</div>'
      f'<div class="sans" style="margin-top:30px;font-size:36px;line-height:1.35">{b}</div><div>{CTA(c, "#F3EADD", OURO)}</div></div>' + rodape('#F3EADD'))
secs = ''.join(f'<section class="f" id="{x["id"]}">{L(i, x)}</section>' for i, x in enumerate(A))
open(f'{d}/artes.html', 'w').write(f'<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;1,400;1,500;1,600&family=Poppins:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400;1,600&display=swap" rel="stylesheet">{CSS}</head><body>{secs}</body></html>')
print(len(A), 'criativos')
