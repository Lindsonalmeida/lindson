# Stories dos 7 destaques da Dra. Jaci (conta Leandro, 03/11/2026). Pedido do Lindson: "crie os destaques".
# Copia as composições aprovadas dos carrosséis de novembro (../instagram-nov/gerar.py, conta Lindson), que copiam os posts reais dela
# (../instagram-estilo/README.md): capa com foto + faixa serifada, B creme com número dourado e fio, C vinho invertido, D véu com checks, fechamento com pílula.
# Formato story 1080x1920 com áreas seguras (nada importante acima de 250 px nem abaixo de 1660 px). Regras do CFO: sem preço, sem promessa, sem antes e depois.
# Uso: python3 gerar.py && node render.js
import re
F = '../fotos'
VINHO, OURO, CAFE, CREME = '#6E1A2A', '#B9A27A', '#5A4033', '#F3EADD'
def md(s):
    s = str(s).replace('\n', '<br>'); s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s); return re.sub(r'_(.+?)_', r'<i class="S">\1</i>', s)
def foto(arq, pos='50% 25%', extra=''): return f'<img class="a bg" src="{F}/{arq}" style="object-position:{pos};{extra}">'
def topo(cor='#fff'): return f'<div class="a topo" style="color:{cor}"><span><b>CLINICA.</b>DRA<b>JACI</b>CUNHA<i class="ok">✓</i></span><span>CIRURGIÃ-DENTISTA · CRO-MA 8514</span></div>'
def rodape(cor='#fff'): return f'<div class="a rod" style="color:{cor}">CLÍNICA DRA. JACI CUNHA<br><small>AV. MILITAR, EM FRENTE À PRAÇA DO VIVA - ZÉ DOCA/MA.</small></div>'
def num(i, n, cor): return f'<div class="a dots">{"".join(f"<i style=\'background:{cor};opacity:{1 if k == i else .35}\'></i>" for k in range(n))}</div>'
def lista(itens, check='#2F5B3A'): return ''.join(f'<div class="li"><i style="border-color:{check};color:{check}">✓</i><span>{md(x)}</span></div>' for x in itens)
def capa(t, i, n):  # cópia da capa c3/c2: foto da Jaci, faixa serifada translúcida, sans embaixo
    return (foto(t['foto'], t.get('pos', '50% 22%')) + '<div class="a" style="inset:0;background:linear-gradient(180deg,rgba(0,0,0,.25) 0,rgba(0,0,0,0) 22%,rgba(0,0,0,0) 45%,rgba(0,0,0,.55) 100%)"></div>' + topo() +
            f'<div class="a" style="left:0;width:1080px;top:1120px;text-align:center"><div class="sans" style="color:#fff;font-size:30px;letter-spacing:.3em;margin-bottom:26px">DESTAQUE {t["n"]}</div>'
            f'<span class="faixa S" style="font-size:104px">{t["serif"]}</span><div class="sans u" style="color:#fff;margin-top:22px;font-size:34px">{md(t["sans"])}</div></div>' + num(i, n, '#fff') + rodape())
def B(t, i, n):  # creme, número dourado, título na faixa com fio
    return (f'<div class="a" style="inset:0;background:{CREME}"></div>' + topo(CAFE) +
            f'<div class="a" style="left:0;width:1080px;top:300px;height:1260px;display:flex;flex-direction:column;justify-content:center;text-align:center;color:{CAFE}"><div class="S" style="font-size:240px;line-height:1;color:{OURO}">{t.get("num", f"{i:02d}")}</div>'
            f'<div class="fio"><i></i><span class="S" style="font-size:60px">{t["titulo"]}</span><i></i></div><div style="width:840px;margin:50px auto 0;text-align:left">{t["corpo"]}</div></div>' + num(i, n, CAFE) + rodape(CAFE))
def C(t, i, n):  # vinho invertido
    return (f'<div class="a" style="inset:0;background:radial-gradient(1000px 1200px at 30% 20%,#86283B,{VINHO} 60%,#4A0F1B)"></div>' + topo('#F3EADD') +
            f'<div class="a" style="left:110px;width:860px;top:300px;height:1300px;display:flex;flex-direction:column;justify-content:center;color:#F7EFE6">'
            f'<div class="S" style="font-size:76px;line-height:1.05;border-left:4px solid {OURO};padding-left:28px;margin-bottom:46px">{t["titulo"]}</div><div class="inv">{t["corpo"]}</div></div>' + num(i, n, '#F3EADD') + rodape('#F3EADD'))
def D(t, i, n):  # foto desfocada com véu claro e checks
    return (foto(t['foto'], '50% 30%', 'filter:blur(7px) saturate(.7);transform:scale(1.06)') + '<div class="a" style="inset:0;background:rgba(232,226,216,.78)"></div>' + topo(CAFE) +
            f'<div class="a" style="left:120px;width:840px;top:300px;height:1300px;display:flex;flex-direction:column;justify-content:center;color:{CAFE}"><div class="tit">{md(t["titulo"])}</div>{t["corpo"]}</div>' + num(i, n, CAFE) + rodape(CAFE))
def MV(t, i, n):  # mito × verdade (cópia do c3), no creme
    return (f'<div class="a" style="inset:0;background:{CREME}"></div>' + topo(CAFE) +
            f'<div class="a" style="left:110px;width:860px;top:300px;height:1300px;display:flex;flex-direction:column;justify-content:center;color:{CAFE};text-align:center">'
            f'<div class="S" style="font-size:72px;margin-bottom:50px">{t["titulo"]}</div><div class="mv"><span class="fv">MITO</span><p>{md(t["mito"])}</p></div>'
            f'<div class="mv"><span class="fv" style="background:{OURO}">VERDADE</span><p>{md(t["verdade"])}</p></div></div>' + num(i, n, CAFE) + rodape(CAFE))
def BAL(t, i, n):  # cópia da capa "botox · As PERGUNTAS que você pensa mas não faz"
    return (foto(t['foto'], '50% 18%') + '<div class="a" style="inset:0;background:linear-gradient(180deg,rgba(0,0,0,.2) 0,rgba(0,0,0,0) 30%,rgba(0,0,0,.5) 100%)"></div>' + topo() +
            f'<div class="a" style="left:0;width:1080px;top:1080px;text-align:center"><div class="balao">{md(t["balao"])}</div><div class="S" style="color:#fff;font-size:200px;line-height:.9">{t["serif"]}</div>'
            f'<div class="sans" style="color:#fff;margin-top:14px;font-size:34px">{md(t["sans"])}</div></div>' + num(i, n, '#fff') + rodape())
def FIM(t, i, n):  # cópia de "Antes de qualquer procedimento, eu observo." (faixa café + pílula)
    return (foto(t['foto'], t.get('pos', '50% 22%')) + '<div class="a" style="inset:0;background:linear-gradient(180deg,rgba(0,0,0,.2) 0,rgba(0,0,0,0) 30%,rgba(0,0,0,.55) 100%)"></div>' + topo() +
            f'<div class="a" style="left:0;width:1080px;top:1090px;text-align:center"><span class="faixa S" style="font-size:72px;background:{CAFE};opacity:.95">{t["serif"]}</span>'
            f'<div class="sans" style="color:#fff;font-size:36px;font-style:italic;margin:22px auto 0;width:840px;line-height:1.3">{md(t["sans"])}</div><div class="pill">Toque no link da bio →</div></div>' + num(i, n, '#fff') + rodape())
CTA = lambda f, pos='50% 22%': dict(tipo=FIM, foto=f, pos=pos, serif='Agende a sua avaliação', sans='O primeiro passo é **conversar**. Responda 4 perguntas no link da bio e a equipe confirma o horário com você.')
DEST = [
 ('01-avaliacao', [dict(tipo=capa, n='01', foto='jaci-off-white-tablet.jpg', serif='Avaliação', sans='**como funciona** a sua primeira consulta'),
   dict(tipo=B, titulo='Em 3 etapas', num='30', corpo=lista(['**Conversa:** o que incomoda você e o que você quer manter', '**Análise:** rosto, expressão e sorriso, com fotos no prontuário', '**Plano:** as etapas que fazem sentido para você']) + '<p class="nota">cerca de 30 minutos</p>'),
   dict(tipo=D, foto='jaci-off-white-sofa-sorrindo.jpg', titulo='Você sai da avaliação com', corpo=lista(['um **plano por etapas**', 'cada procedimento indicado **explicado com calma**', 'tempo para **pensar e decidir**', 'o **próximo horário** combinado, se quiser'])),
   CTA('jaci-preto-sorriso-aberto.jpg')]),
 ('02-harmonizacao', [dict(tipo=capa, n='02', foto='jaci-preto-mao-no-cabelo.jpg', serif='Harmonização', sans='orofacial: **o que é**'),
   dict(tipo=C, titulo='Equilíbrio, não exagero', corpo='<p class="tx">A harmonização orofacial é um conjunto de procedimentos que <b>equilibra as proporções do rosto e do sorriso</b>, respeitando os seus traços.</p><p class="tx" style="margin-top:30px">Tudo é indicado <b>só depois da avaliação</b>.</p>'),
   dict(tipo=B, titulo='O que pode entrar no plano', corpo=lista(['**Toxina botulínica:** suaviza linhas de expressão', '**Preenchimento:** repõe volume e contorno', '**Bioestimulador:** estimula o colágeno aos poucos'])),
   CTA('jaci-preto-rennova-sorrindo.jpg')]),
 ('03-odonto', [dict(tipo=capa, n='03', foto='jaci-branco-cadeira-sorrindo.jpg', pos='50% 18%', serif='Odonto', sans='**saúde e estética** do sorriso'),
   dict(tipo=D, foto='jaci-nude-sofa-corpo-inteiro.jpg', titulo='Na clínica também tem', corpo=lista(['**consulta e prevenção**', '**limpeza** e orientação', '**estética do sorriso**, indicada na avaliação', 'um **plano por etapas** para o seu tratamento'])),
   CTA('jaci-off-white-sofa-sorrindo.jpg')]),
 ('04-duvidas', [dict(tipo=BAL, n='04', foto='jaci-preto-mao-no-cabelo.jpg', balao='As **PERGUNTAS** que você pensa mas não faz:', serif='dúvidas', sans='O QUE **NINGUÉM** RESPONDE'),
   dict(tipo=MV, titulo='Botox deixa a cara parada?', mito='Todo botox **paralisa** o rosto.', verdade='Com dose e pontos bem indicados, a **expressão continua natural**. Isso é definido na avaliação.'),
   dict(tipo=MV, titulo='Preenchimento é para sempre?', mito='O preenchimento é **definitivo**.', verdade='O ácido hialurônico é **absorvido com o tempo**, e a duração varia de pessoa para pessoa.'),
   dict(tipo=C, titulo='Bioestimulador ou preenchimento?', corpo='<p class="tx">O <b>preenchimento</b> repõe volume na hora.</p><p class="tx" style="margin-top:24px">O <b>bioestimulador</b> estimula o colágeno <b>aos poucos</b>.</p><p class="tx" style="margin-top:24px">A avaliação mostra o que faz sentido <b>para você</b>.</p>'),
   CTA('jaci-off-white-tablet.jpg')]),
 ('05-pacientes', [dict(tipo=capa, n='05', foto='jaci-nude-sofa-corpo-inteiro.jpg', pos='50% 25%', serif='Pacientes', sans='**o que elas dizem**'),
   dict(tipo=B, titulo='Como entram aqui', num='✓', corpo='<p class="tx" style="font-size:38px">Neste destaque entram <b>só depoimentos com autorização por escrito</b> das pacientes.</p><p class="nota">Antes e depois, só com termo assinado (regras do CFO).</p>'),
   CTA('jaci-preto-sorriso-aberto.jpg')]),
 ('06-a-clinica', [dict(tipo=capa, n='06', foto='jaci-off-white-sofa-sorrindo.jpg', pos='60% 20%', serif='A Clínica', sans='**conheça** o nosso espaço'),
   dict(tipo=C, titulo='Feita para você ficar à vontade', corpo='<p class="tx">Avaliação <b>antes de tudo</b>, explicação <b>em cada etapa</b> e tempo para você <b>decidir com calma</b>.</p><p class="tx" style="margin-top:30px">Harmonização orofacial e odontologia no mesmo lugar.</p>'),
   CTA('jaci-preto-rennova-sorrindo.jpg')]),
 ('07-como-chegar', [dict(tipo=capa, n='07', foto='jaci-branco-cadeira-sorrindo.jpg', pos='50% 18%', serif='Como chegar', sans='**Zé Doca** · MA'),
   dict(tipo=B, titulo='Endereço', num='📍', corpo='<p class="tx" style="font-size:44px"><b>Av. Militar</b><br>em frente à <b>Praça do Viva</b><br>Zé Doca · MA</p><p class="nota">Toque no link da bio para ver o mapa e agendar.</p>'),
   CTA('jaci-off-white-tablet.jpg')])]
secs = []
for nome, telas in DEST:
    for i, t in enumerate(telas):
        secs.append(f'<section class="f" id="{nome}-{i+1}">{t["tipo"](t, i, len(telas))}</section>')
CSS = open('../instagram-nov/gerar.py').read().split('<style>')[1].split('</style>')[0].replace('{{', '{').replace('}}', '}').replace('{OURO}', OURO).replace('{VINHO}', VINHO)
CSS = CSS.replace('height:1350px', 'height:1920px').replace('.rod{left:88px;right:88px;top:1210px', '.rod{left:88px;right:88px;top:1610px').replace('.rod.c{display:block;text-align:center;top:1240px}', '')
CSS += '.li{font-size:47px!important;margin-bottom:44px}.li i{width:58px;height:58px;font-size:30px}.tx{font-size:52px!important}.tit{font-size:68px}.mv p{font-size:46px}.fv{font-size:52px}.mv .fv{font-size:50px}.nota{font-size:36px!important;margin-top:44px}.inv .tx{font-size:54px!important}.topo{top:230px}.rod{display:block;text-align:center}.dots{top:1560px;right:0;left:0;justify-content:center}.nota{font-family:Poppins;color:inherit;opacity:.8}.faixa{line-height:1.3}'
open('artes.html', 'w').write(f'''<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@1,400;1,500;1,600;1,700&family=Poppins:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400;1,600&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>{"".join(secs)}</body></html>''')
print(len(secs), 'telas')
