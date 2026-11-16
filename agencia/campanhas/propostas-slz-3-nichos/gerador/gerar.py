# Propostas premium SLZ: advogado, barbeiro, dentista (conta Leandro, 16/11/2026)
# Uso: python3 gerar.py  -> ../proposta-<nicho>.pdf + ../paginas/<nicho>-NN.jpg + ../folha.jpg
# PRECOS: edite aqui (alinhado com agencia/campanhas/vendas-slz-3-nichos/ESTRATEGIA-DE-VENDAS.md)
import asyncio, base64, io, os, qrcode
from pathlib import Path
from playwright.async_api import async_playwright
from PIL import Image

AQUI = Path(__file__).resolve().parent; RAIZ = AQUI.parent; F = RAIZ / 'fotos'
WHATS = '5598985621808'  # WhatsApp do Lindson (o mesmo do site)
LINK_VIDEOS = 'https://lindsonalmeida.pages.dev/site/portfolio/'
LINK_SITE = 'https://lindsonalmeida.pages.dev/site/'

PRECOS = {
 'advogado': {'percebido': 'R$ 8.900', 'planos': [
   ('Presença Jurídica', 'R$ 1.497', 'Para começar a ser encontrado', ['Google Meu Negócio reformado', '8 conteúdos/mês dentro do Provimento 205', 'Site bio do escritório', 'Relatório mensal em 1 página']),
   ('Autoridade Jurídica SLZ', 'R$ 2.497', 'O recomendado', ['Tudo do Presença', '12 conteúdos/mês + Reels', 'Impulsionamento informativo Meta + Google', 'Site do escritório + roteiro de WhatsApp', 'Checklist OAB em cada peça']),
   ('Escritório Completo', 'R$ 3.997', 'Para dominar a área na cidade', ['Tudo do Autoridade', 'Sistema de triagem e agenda', '1 dia de gravação por trimestre', 'Reunião de estratégia quinzenal'])]},
 'barbeiro': {'percebido': 'R$ 4.400', 'planos': [
   ('Cadeira Ocupada', 'R$ 597', 'Para encher os dias fracos', ['Anúncio Meta no raio de 3 km', '8 Stories/mês', 'Mensagem de retorno para quem sumiu', 'Google Meu Negócio no topo do bairro']),
   ('Cadeira Cheia', 'R$ 997', 'O recomendado', ['Tudo do Ocupada', '12 Reels/Stories por mês', 'Google Ads "barbearia perto de mim"', 'Site bio com agendamento', 'Clube de Assinatura montado']),
   ('Barbearia Referência', 'R$ 1.997', 'Para virar a marca do bairro', ['Tudo do Cadeira Cheia', 'Site completo + sistema de agenda', 'Gravação mensal na barbearia', 'Reunião de estratégia quinzenal'])]},
 'dentista': {'percebido': 'R$ 8.800', 'planos': [
   ('Primeira Avaliação', 'R$ 1.497', 'Para encher a agenda de avaliações', ['Campanha de avaliação Meta', '8 conteúdos/mês por especialidade', 'Roteiro de WhatsApp para a recepção', 'Google Meu Negócio reformado']),
   ('Agenda de Avaliações', 'R$ 2.497', 'O recomendado', ['Tudo do Primeira Avaliação', 'Meta + Google Ads no raio da clínica', '12 conteúdos/mês + Reels', 'Follow-up de orçamento em 7 dias', 'Site da clínica + checklist CFO']),
   ('Clínica Completa', 'R$ 4.497', 'Para ser a referência da especialidade', ['Tudo do Agenda', 'Sistema de orçamentos e reativação', 'Treino da recepção', 'Gravação mensal na clínica'])]},
}

def uri(p):
    p = Path(p); mime = 'image/png' if p.suffix == '.png' else 'image/svg+xml' if p.suffix == '.svg' else 'image/jpeg'
    if mime == 'image/jpeg':
        im = Image.open(p).convert('RGB'); im.thumbnail((1600, 2400)); b = io.BytesIO(); im.save(b, 'JPEG', quality=86); data = b.getvalue()
    else: data = p.read_bytes()
    return f'data:{mime};base64,' + base64.b64encode(data).decode()

def qr(url):
    q = qrcode.QRCode(border=1, box_size=10); q.add_data(url); q.make()
    im = q.make_image(fill_color='#0A0C10', back_color='#EEEAE2'); b = io.BytesIO(); im.save(b, 'PNG')
    return 'data:image/png;base64,' + base64.b64encode(b.getvalue()).decode()

N = lambda f: uri(F / 'nicho' / f'{f}.jpg')
SITE = lambda f: uri(F / 'sites' / f'{f}.jpg')

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Inter+Tight:wght@300;400;500;600;800&display=swap');
:root{--ob:#0A0C10;--ma:#EEEAE2;--gr:#22262E;--pe:#8A8F98;--br:#B4935A;--in:#1B1F3B}
*{margin:0;padding:0;box-sizing:border-box}
@page{size:1080px 1350px;margin:0}
body{background:var(--ob);font-family:'Inter Tight',sans-serif;color:var(--ma)}
.pg{width:1080px;height:1350px;position:relative;overflow:hidden;page-break-after:always;background:var(--ob)}
.bg{position:absolute;inset:0;background-size:cover;background-position:center}
.v{position:absolute;inset:0}
.top{position:absolute;top:56px;left:72px;right:72px;display:flex;justify-content:space-between;font-size:17px;letter-spacing:.24em;text-transform:uppercase;color:var(--pe);z-index:5}
.top b{color:var(--br);font-weight:500}
.foot{position:absolute;bottom:48px;left:72px;right:72px;display:flex;justify-content:space-between;font-size:16px;letter-spacing:.2em;text-transform:uppercase;color:var(--pe);z-index:5}
.sr{font-family:'Instrument Serif',serif;font-weight:400;line-height:.95;letter-spacing:-.01em}
.sr i{color:var(--br)}
.ey{font-size:20px;letter-spacing:.28em;text-transform:uppercase;color:var(--br);font-weight:500;margin-bottom:26px}
.p{font-size:31px;line-height:1.38;color:#cfcac0;font-weight:300}
.p b{color:var(--ma);font-weight:500}
.z{position:absolute;z-index:4}
.num{font-family:'Instrument Serif';font-size:520px;line-height:.8;color:transparent;-webkit-text-stroke:1.5px rgba(180,147,90,.35);position:absolute}
.phone{position:absolute;width:300px;height:620px;border-radius:46px;background:#000;padding:12px;box-shadow:0 40px 80px rgba(0,0,0,.6),0 0 0 2px #3a3f48 inset;z-index:4}
.phone>div{width:100%;height:100%;border-radius:36px;background-size:cover;background-position:top center}
.card{background:rgba(34,38,46,.72);backdrop-filter:blur(14px);border:1px solid rgba(180,147,90,.35);border-radius:22px;padding:34px}
.line{height:1px;background:rgba(180,147,90,.5)}
.tag{display:inline-block;border:1px solid var(--br);color:var(--br);border-radius:99px;padding:8px 20px;font-size:18px;letter-spacing:.14em;text-transform:uppercase}
.qr{width:150px;height:150px;border-radius:12px}
"""

def top(n, t): return f'<div class="top"><span><b>Al Kántara</b> · Lindson Almeida</span><span>{t}</span><span>{n:02d}</span></div>'
def foot(t='Proposta confidencial · São Luís · 2026'): return f'<div class="foot"><span>{t}</span><span>16.11.2026</span></div>'
def grad(d='180deg', a=.15, b=.96): return f'<div class="v" style="background:linear-gradient({d},rgba(10,12,16,{a}),rgba(10,12,16,{b}))"></div>'

def svc_block(i, s):
    nome, oque, entrega, venda = s
    return f'''<div style="margin-bottom:30px"><div style="display:flex;gap:26px;align-items:baseline"><span class="sr" style="font-size:72px;color:var(--br)">{i:02d}</span>
    <h3 class="sr" style="font-size:54px">{nome}</h3></div>
    <div class="line" style="margin:18px 0 22px"></div>
    <p class="p" style="font-size:24px"><b>O que é:</b> {oque}</p>
    <p class="p" style="font-size:24px;margin-top:6px"><b>Entregável:</b> {entrega}</p>
    <p class="p" style="font-size:24px;margin-top:6px;color:var(--ma)"><b style="color:var(--br)">Como vira venda:</b> {venda}</p></div>'''

def mock_gmn(nome, cat):
    return f'''<div class="card" style="position:relative;width:430px;padding:0;overflow:hidden;background:#fff;color:#202124;border:none;box-shadow:0 40px 80px rgba(0,0,0,.6)">
    <div style="height:150px;background:url({N(cat['img'])}) center/cover"></div><div style="padding:24px 28px">
    <div style="font-size:28px;font-weight:600">{nome}</div><div style="font-size:19px;color:#5f6368;margin:6px 0 14px">{cat['cat']} · São Luís, MA</div>
    <div style="display:flex;gap:10px">{''.join(f'<span style="font-size:17px;border:1px solid #dadce0;border-radius:99px;padding:8px 16px;color:#1a73e8">{x}</span>' for x in ['Rotas','Ligar','WhatsApp','Site'])}</div>
    <div style="font-size:17px;color:#5f6368;margin-top:16px">Fotos novas toda semana · Avaliações respondidas · Posts</div></div></div>'''

def mock_ad(img, txt, cta):
    return f'''<div class="phone" style="position:relative;width:250px;height:420px"><div style="background:#000;display:flex;flex-direction:column">
    <div style="padding:16px 18px;font-size:16px;color:#fff;display:flex;gap:10px;align-items:center"><span style="width:30px;height:30px;border-radius:50%;background:var(--br)"></span><b>seu.perfil</b><span style="color:#aaa">Patrocinado</span></div>
    <div style="flex:1;background:url({img}) center/cover;position:relative"><div style="position:absolute;inset:auto 0 0 0;padding:22px;background:linear-gradient(transparent,rgba(0,0,0,.85));font-family:'Instrument Serif';font-size:28px;line-height:1;color:#fff">{txt}</div></div>
    <div style="padding:14px 18px;background:#1c1f26;color:#fff;font-size:17px;display:flex;justify-content:space-between"><span>{cta}</span><span>›</span></div></div></div>'''

def mock_dash():
    bars = [38, 52, 47, 66, 74, 88]
    return f'''<div class="card" style="position:relative;width:520px">
    <div style="font-size:18px;letter-spacing:.2em;text-transform:uppercase;color:var(--pe)">Painel do cliente · ilustração</div>
    <div style="display:flex;gap:18px;margin:22px 0">{''.join(f'<div style="flex:1;border:1px solid rgba(180,147,90,.3);border-radius:14px;padding:14px"><div style="font-size:15px;color:var(--pe)">{k}</div><div class="sr" style="font-size:40px;color:var(--ma)">—</div></div>' for k in ['Contatos','Custo/contato','Fechados'])}</div>
    <div style="display:flex;align-items:flex-end;gap:16px;height:170px">{''.join(f'<div style="flex:1;height:{h}%;background:linear-gradient(var(--br),rgba(180,147,90,.15));border-radius:6px 6px 0 0"></div>' for h in bars)}</div>
    <div style="font-size:15px;color:var(--pe);margin-top:12px">Os números entram com os dados reais da sua conta, toda semana.</div></div>'''

def build(k, d):
    P = PRECOS[k]; pg = []
    capa_img = uri(F / f"{d['capa']}.jpg"); rec = uri(F / f"{d['rec']}-rec.png")
    # 01 capa
    pg.append(f'''<section class="pg"><div class="bg" style="background-image:url({capa_img});background-position:center 20%;background-size:115%;"></div>
    {grad('180deg',.05,.98)}<div class="v" style="background:linear-gradient(90deg,rgba(10,12,16,.92) 0%,rgba(10,12,16,0) 60%)"></div>
    {top(1,'Proposta')}
    <div class="z" style="left:72px;top:250px;width:620px"><div class="tag">{d['nicho_tag']} · São Luís</div></div>
    <div class="z" style="left:72px;bottom:300px;width:940px"><h1 class="sr" style="font-size:132px">{d['capa_h']}</h1>
    <p class="p" style="margin-top:30px;width:720px">{d['capa_p']}</p></div>
    <div class="z" style="left:72px;bottom:120px;display:flex;gap:26px;align-items:center"><img class="qr" src="{qr(LINK_VIDEOS)}"><div style="font-size:21px;line-height:1.5;color:var(--pe)"><b style="color:var(--ma);font-weight:500">Assista antes de ler:</b><br>vídeos e demos de sites, anúncios<br>e sistemas que já entregamos ▶</div></div>
    {foot()}</section>''')
    # 02 carta com foto
    pg.append(f'''<section class="pg"><div class="bg" style="background-image:url({N(d['img_carta'])});opacity:.55"></div>{grad('180deg',.3,.97)}{top(2,'Carta')}
    <img class="z" src="{rec}" style="right:-40px;bottom:0;height:980px;filter:drop-shadow(-30px 0 60px rgba(0,0,0,.8))">
    <div class="z" style="left:72px;top:230px;width:600px"><div class="ey">Antes de tudo</div>
    <h2 class="sr" style="font-size:92px">{d['carta_h']}</h2>
    <p class="p" style="margin-top:36px">{d['carta_p']}</p>
    <p class="sr" style="font-size:52px;margin-top:40px;color:var(--br)">Lindson Almeida</p><p style="font-size:20px;color:var(--pe);letter-spacing:.14em;text-transform:uppercase">Fundador · Al Kántara</p></div>{foot()}</section>''')
    # 03 diagnóstico
    items = ''.join(f'<div class="card" style="margin-bottom:22px;padding:28px 32px"><div class="sr" style="font-size:44px;color:var(--br)">{a}</div><p class="p" style="font-size:26px;margin-top:8px">{b}</p></div>' for a, b in d['diag'])
    pg.append(f'''<section class="pg"><div class="bg" style="background-image:url({N(d['img_diag'])})"></div><div class="v" style="background:linear-gradient(90deg,rgba(10,12,16,.25),rgba(10,12,16,.97) 55%)"></div>{top(3,'Diagnóstico')}
    <div class="z" style="right:72px;top:190px;width:560px"><div class="ey">O mercado em São Luís</div><h2 class="sr" style="font-size:84px;margin-bottom:40px">{d['diag_h']}</h2>{items}</div>{foot()}</section>''')
    # 04 o que perdem
    perdas = ''.join(f'<div style="display:flex;gap:22px;margin-bottom:30px"><span class="sr" style="font-size:54px;color:var(--br);width:60px">{i+1}</span><p class="p">{t}</p></div>' for i, t in enumerate(d['perde']))
    pg.append(f'''<section class="pg"><div class="bg" style="background-image:url({N(d['img_perde'])});height:560px;bottom:auto"></div><div class="v" style="height:560px;background:linear-gradient(180deg,rgba(10,12,16,.1),rgba(10,12,16,1))"></div>{top(4,'O que se perde hoje')}
    <div class="z" style="left:72px;top:400px;width:936px"><h2 class="sr" style="font-size:110px">{d['perde_h']}</h2><div style="margin-top:50px">{perdas}</div>
    <div class="card" style="margin-top:20px"><p class="p" style="font-size:27px"><b>A conta do cliente perdido (com os seus números):</b> {d['conta']}</p></div></div>{foot()}</section>''')
    # 05 meta 4x
    passos = ''.join(f'<div style="flex:1;border-top:2px solid var(--br);padding-top:20px"><div style="font-size:18px;letter-spacing:.2em;color:var(--br)">0{i+1}</div><div class="sr" style="font-size:40px;margin:8px 0">{a}</div><p style="font-size:21px;line-height:1.4;color:#bdb8ae">{b}</p></div>' for i, (a, b) in enumerate(d['caminho']))
    pg.append(f'''<section class="pg"><div class="bg" style="background-image:url({N(d['img_meta'])})"></div>{grad('180deg',.35,.97)}{top(5,'A meta')}
    <div class="num" style="right:-30px;top:120px">4x</div>
    <div class="z" style="left:72px;top:330px;width:900px"><div class="ey">A ambição do projeto</div><h2 class="sr" style="font-size:118px">{d['meta_h']}</h2>
    <p class="p" style="margin-top:30px;width:820px">{d['meta_p']}</p></div>
    <div class="z" style="left:72px;right:72px;bottom:150px;display:flex;gap:28px">{passos}</div>{foot('Meta de trabalho, não garantia de resultado')}</section>''')
    # 06-09 serviços (2 por página) com mockups
    sv = d['servicos']
    mocks = [
      ('<div class="z" style="right:80px;top:150px;display:flex;gap:24px">' + mock_ad(N(d['img_ad1']), d['ad1'], d['ad_cta']) + '</div>', d['img_s1']),
      ('<div class="z" style="right:70px;top:170px">' + mock_gmn(d['gmn_nome'], {'img': d['img_diag'], 'cat': d['gmn_cat']}) + '</div>', d['img_s2']),
      (f'<div class="phone" style="right:90px;top:140px;width:220px;height:460px;transform:rotate(4deg)"><div style="background-image:url({SITE(d["site1"])})"></div></div><div class="phone" style="right:320px;top:170px;transform:rotate(-5deg);width:200px;height:420px"><div style="background-image:url({SITE(d["site2"])})"></div></div>', d['img_s3']),
      ('<div class="z" style="right:60px;top:160px;transform:scale(.85);transform-origin:top right">' + mock_dash() + '</div>', d['img_s4']),
    ]
    for j in range(4):
        m, bgimg = mocks[j]
        pg.append(f'''<section class="pg"><div class="bg" style="background-image:url({N(bgimg)});opacity:.42;height:780px;bottom:auto"></div><div class="v" style="height:780px;background:linear-gradient(180deg,rgba(10,12,16,.2),rgba(10,12,16,1))"></div>{top(6+j,'Os 8 serviços')}
        <div class="z" style="left:72px;top:170px;width:420px"><div class="ey">Serviços {2*j+1} e {2*j+2} de 8</div><h2 class="sr" style="font-size:76px">{d['svc_titulos'][j]}</h2></div>{m}
        <div class="z" style="left:72px;right:72px;top:640px">{svc_block(2*j+1, sv[2*j])}{svc_block(2*j+2, sv[2*j+1])}</div>{foot()}</section>''')
    # 10 cronograma
    fases = ''.join(f'''<div class="card" style="flex:1;padding:30px"><div class="tag" style="font-size:16px">{a}</div><div class="sr" style="font-size:50px;margin:20px 0 14px">{b}</div>
      <ul style="list-style:none">{''.join(f'<li style="font-size:22px;line-height:1.4;color:#cfcac0;padding:9px 0;border-top:1px solid rgba(138,143,152,.25)">{x}</li>' for x in c)}</ul></div>''' for a, b, c in d['crono'])
    pg.append(f'''<section class="pg"><div class="bg" style="background-image:url({N(d['img_crono'])});opacity:.5;height:620px;bottom:auto"></div><div class="v" style="height:620px;background:linear-gradient(180deg,rgba(10,12,16,.2),rgba(10,12,16,1))"></div>{top(10,'Cronograma')}
    <div class="z" style="left:72px;top:220px"><div class="ey">90 dias</div><h2 class="sr" style="font-size:112px">Do primeiro dia<br>ao <i>terceiro mês.</i></h2></div>
    <div class="z" style="left:72px;right:72px;top:560px;display:flex;gap:22px">{fases}</div>{foot()}</section>''')
    # 11 métricas
    mets = ''.join(f'<div style="display:flex;justify-content:space-between;gap:30px;padding:22px 0;border-top:1px solid rgba(180,147,90,.35)"><span class="sr" style="font-size:40px">{a}</span><span style="font-size:22px;color:#bdb8ae;width:470px;line-height:1.4">{b}</span></div>' for a, b in d['metricas'])
    pg.append(f'''<section class="pg"><div class="bg" style="background-image:url({N(d['img_met'])});opacity:.3"></div>{grad('180deg',.5,.98)}{top(11,'Como medimos')}
    <div class="z" style="left:72px;top:190px;width:430px"><div class="ey">Métricas</div><h2 class="sr" style="font-size:88px">O que não se mede, <i>não cresce.</i></h2></div>
    <div class="z" style="right:72px;top:170px">{mock_dash()}</div>
    <div class="z" style="left:72px;right:72px;top:640px">{mets}<p class="p" style="font-size:22px;margin-top:20px;color:var(--pe)">Relatório em 1 página todo mês, com os dados reais da sua conta. Nenhum número inventado.</p></div>{foot()}</section>''')
    # 12 por que o Lindson
    cases = [('Clínica Dra. Jaci Cunha', 'Mini site, feed e prova social dentro do CFO', 'jaci-m'), ('Tribuna 98', 'Mini site e conteúdo do portal', 'tribuna-m'), ('Desentupidora SF', 'Mini site de serviço com WhatsApp', 'sf-m')]
    phones = ''.join(f'<div style="text-align:center"><div class="phone" style="position:relative;width:200px;height:420px;margin:0 auto"><div style="background-image:url({SITE(c)})"></div></div><div class="sr" style="font-size:30px;margin-top:18px">{a}</div><div style="font-size:17px;color:var(--pe);margin-top:4px;width:280px">{b}</div></div>' for a, b, c in cases)
    pg.append(f'''<section class="pg"><div class="bg" style="background-image:url({capa_img});background-position:center 15%;opacity:.35;filter:blur(2px)"></div>{grad('180deg',.6,.98)}{top(12,'Por que o Lindson')}
    <div class="z" style="left:72px;top:180px;width:936px"><div class="ey">Quem já confia</div><h2 class="sr" style="font-size:96px">Gente de São Luís<br>e do Maranhão <i>que já está com a gente.</i></h2></div>
    <div class="z" style="left:40px;right:40px;top:520px;display:flex;justify-content:space-around">{phones}</div>
    <div class="z" style="left:72px;right:72px;bottom:110px"><p class="p" style="font-size:22px"><b>Também:</b> Leo Pinto (Instagram, saudações animadas e painel), WF Celulares (rebranding premium), Orégano Turbo (marca e anúncios para pizzarias) e Rafael Imports (mini site). Sem depoimento inventado: os trabalhos estão no ar para você conferir.</p></div>{foot()}</section>''')
    # 13 investimento
    cards = ''
    for i, (nome, preco, sub, it) in enumerate(P['planos']):
        rec_ = i == 1
        cards += f'''<div class="card" style="flex:1;padding:34px 28px;{'background:linear-gradient(180deg,rgba(180,147,90,.28),rgba(34,38,46,.85));border:2px solid var(--br);transform:translateY(-24px)' if rec_ else ''}">
        {'<div class="tag" style="font-size:14px;margin-bottom:14px;background:var(--br);color:var(--ob)">Recomendado</div>' if rec_ else '<div style="height:52px"></div>'}
        <div class="sr" style="font-size:42px;min-height:84px">{nome}</div><div style="font-size:18px;color:var(--pe);margin:6px 0 18px">{sub}</div>
        <div class="sr" style="font-size:60px;color:{'var(--ma)' if rec_ else 'var(--br)'}">{preco}<span style="font-size:24px;color:var(--pe)">/mês</span></div>
        <ul style="list-style:none;margin-top:18px">{''.join(f'<li style="font-size:18px;line-height:1.3;color:#cfcac0;padding:7px 0;border-top:1px solid rgba(138,143,152,.25)">— {x}</li>' for x in it)}</ul></div>'''
    pg.append(f'''<section class="pg"><div class="bg" style="background-image:url({N(d['img_inv'])});opacity:.35;height:520px;bottom:auto"></div><div class="v" style="height:520px;background:linear-gradient(180deg,rgba(10,12,16,.2),rgba(10,12,16,1))"></div>{top(13,'Investimento')}
    <div class="z" style="left:72px;top:170px;width:936px"><div class="ey">Investimento</div><h2 class="sr" style="font-size:96px">Uma equipe inteira<br>pelo preço de <i>um funcionário.</i></h2>
    <p class="p" style="font-size:25px;margin-top:22px">Tráfego, conteúdo, sites e sistemas montados por fora custariam <b>{P['percebido']}/mês</b> em valor de mercado. Aqui, tudo integrado:</p></div>
    <div class="z" style="left:56px;right:56px;top:620px;display:flex;gap:20px">{cards}</div>
    <div class="z" style="left:72px;right:72px;bottom:84px;font-size:17px;color:var(--pe);line-height:1.4">Contrato de 6 meses. Verba de anúncio paga direto à Meta e ao Google (definimos juntos). Garantia de entrega do que está aqui; resultado depende também do atendimento, mas a meta de 4x guia cada decisão.</div>{foot()}</section>''')
    # 14 próximos passos
    steps = ''.join(f'<div style="display:flex;gap:24px;align-items:baseline;padding:20px 0;border-top:1px solid rgba(180,147,90,.35)"><span class="sr" style="font-size:52px;color:var(--br)">{i+1}</span><span style="font-size:28px;color:var(--ma)">{t}</span></div>' for i, t in enumerate(d['passos']))
    wa = f'https://wa.me/{WHATS}?text=' + d['wa_txt'].replace(' ', '%20')
    pg.append(f'''<section class="pg"><div class="bg" style="background-image:url({capa_img});background-position:center 18%;background-size:112%"></div><div class="v" style="background:linear-gradient(90deg,rgba(10,12,16,.97) 45%,rgba(10,12,16,.2))"></div>{top(14,'Próximos passos')}
    <div class="z" style="left:72px;top:200px;width:600px"><div class="ey">Próximos passos</div><h2 class="sr" style="font-size:104px">Vamos <i>começar?</i></h2><div style="margin-top:40px">{steps}</div>
    <div style="display:flex;gap:26px;align-items:center;margin-top:50px"><img class="qr" src="{qr(wa)}"><div><div class="tag" style="background:var(--br);color:var(--ob);font-size:20px">Responder no WhatsApp</div><p style="font-size:20px;color:var(--pe);margin-top:14px">Aponte a câmera ou responda<br>“{d['wa_txt']}”.</p></div></div>
    <div style="display:flex;gap:26px;align-items:center;margin-top:34px"><img class="qr" src="{qr(LINK_SITE)}" style="width:110px;height:110px"><p style="font-size:20px;color:var(--pe)">Site e vídeos do Lindson<br>@lindsonalmeida_</p></div></div>
    <img class="z" src="{uri(F/'alkantara-horizontal-negativo.svg')}" style="right:72px;bottom:110px;height:46px">{foot()}</section>''')
    return f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{"".join(pg)}</body></html>'

from conteudo import NICHOS

async def main():
    out = RAIZ / 'paginas'; out.mkdir(exist_ok=True)
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for k, d in NICHOS.items():
            html = build(k, d); (RAIZ / f'fonte-{k}.html').write_text(html)
            pg = await b.new_page(viewport={'width': 1080, 'height': 1350})
            await pg.set_content(html, wait_until='networkidle'); await pg.wait_for_timeout(1500)
            await pg.pdf(path=str(RAIZ / f'proposta-{k}.pdf'), width='1080px', height='1350px', print_background=True)
            secs = await pg.query_selector_all('section.pg')
            for i, s in enumerate(secs):
                await s.screenshot(path=str(out / f'{k}-{i+1:02d}.jpg'), type='jpeg', quality=80)
            print(k, len(secs), 'páginas')
        await b.close()
    capas = [Image.open(out / f'{k}-01.jpg') for k in NICHOS]
    fl = Image.new('RGB', (3 * 720 + 80, 900 + 40), (10, 12, 16))
    for i, c in enumerate(capas): c.thumbnail((720, 900)); fl.paste(c, (20 + i * 740, 20))
    fl.save(RAIZ / 'folha.jpg', quality=88)
    for k in NICHOS: (RAIZ / f'fonte-{k}.html').unlink()  # fonte = gerar.py + conteudo.py (html tem imagens embutidas)

asyncio.run(main())
