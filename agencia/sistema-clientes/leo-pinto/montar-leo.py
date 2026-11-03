"""Painel do Vereador Leo Pinto = o modelo da Central (../prototipo/painel.html, feito pela outra equipe)
com a identidade do mandato (book) e a área Gabinete (gabinete.js, demandas com banco real).
python3 montar-leo.py -> painel-leo.html (arquivo único, publicado como artifact com db + user)
Não reescreve o modelo: aplica trocas pontuais. Se o modelo mudar, rode de novo."""
import base64, io, os, re
from PIL import Image
D = os.path.dirname(os.path.abspath(__file__)); SC = os.path.join(D, '..')
IG = os.path.join(D, '..', '..', 'clientes', 'leo-pinto', 'instagram-v12-feed')

def uri(p, w, fmt='PNG', q=82):
    im = Image.open(p); im.thumbnail((w, w * 4))
    if fmt == 'JPEG': im = im.convert('RGB')
    b = io.BytesIO(); im.save(b, fmt, quality=q, optimize=True)
    return f'data:image/{fmt.lower()};base64,' + base64.b64encode(b.getvalue()).decode()
def webp(p): return 'data:image/webp;base64,' + base64.b64encode(open(p, 'rb').read()).decode()

s = open(os.path.join(SC, 'prototipo', 'painel.html')).read()
def troca(velho, novo, n=1):
    global s
    assert velho in s, 'o modelo mudou, ajuste: ' + velho[:60]
    s = s.replace(velho, novo) if n == 0 else s.replace(velho, novo, n)

# 1 · identidade do mandato (book): Montserrat, marinho, royal, sol, laranja, maré
troca('<title>Painel do Cliente</title>', '<title>Gabinete Leo Pinto</title>')
troca('family=Big+Shoulders+Display:wght@700;800&family=Manrope:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500', 'family=Montserrat:wght@500;600;700;800;900')
troca("--fundo:#09090A;--painel:#121213;--painel2:#18181A;--linha:#242427;--amarelo:#F5C518;--amarelo2:#FFDD55;",
      "--fundo:#06102B;--painel:#0C1B44;--painel2:#12245A;--linha:#1E3266;--amarelo:#FFC20E;--amarelo2:#FFD84D;--royal:#2350F5;--mare:#08BDFF;--laranja:#FF7A1A;")
troca("--texto:#F3F0E6;--apagado:#8E8B83;", "--texto:#EAF0FF;--apagado:#9DB0D9;")
troca("--f-titulo:'Big Shoulders Display','Arial Narrow',Impact,sans-serif;--f-corpo:'Manrope',system-ui,sans-serif;--f-dado:'IBM Plex Mono',ui-monospace,monospace;",
      "--f-titulo:'Montserrat',system-ui,sans-serif;--f-corpo:'Montserrat',system-ui,sans-serif;--f-dado:'Montserrat',system-ui,sans-serif;")
for a, b in [('rgba(245,197,24', 'rgba(255,194,14'), ('#F5C518', '#FFC20E'), ('#0C0C0D', '#031034'), ('rgba(9,9,10,.92)', 'rgba(6,16,43,.92)'),
             ('#070707', '#041030'), ('#C9C5BA', '#C5D2EE'), ('#0A0A0A', '#05316E'), ('#2a2412,#0f0f10', '#1A3CCB,#05316E'), ('#242427', '#1E3266'), ('#8E8B83', '#9DB0D9'),
             ('#121213', '#0C1B44'), ('#F3F0E6', '#EAF0FF'), ("['#FFC20E','#C99A10','#6E5A1C']", "['#FFC20E','#08BDFF','#2350F5']")]:
    s = s.replace(a, b)
troca('.menu{position:sticky;top:0;height:100vh;', '.menu{background:linear-gradient(180deg,#05316E,#021440)!important;position:sticky;top:0;height:100vh;')
troca('.kpi .val{font:800 34px/1.1', '.kpi .val{font:900 32px/1.1')
troca('textarea{min-height:80px;resize:vertical}', 'textarea{min-height:80px;resize:vertical}\n#nova-dem input:not([type=checkbox]),#nova-dem select,#nova-ag input,#f-bairro,#f-causa,#dlg-dem textarea{background:var(--painel2);color:var(--texto);border:1px solid var(--linha);border-radius:9px;padding:10px 12px;font:500 14px var(--f-corpo);width:100%}\n#dlg-dem::backdrop{background:rgba(2,10,40,.6)}')
troca('.topo h1{margin:0;font:800 26px/1', '.topo h1{margin:0;font:900 22px/1')

# 2 · cabeçalho do menu: logo oficial do mandato; o painel é do cliente LEO (sem seletor de admin)
troca('<div class="logo"><b>LA</b>Central</div>', '<div class="logo" style="display:grid;gap:8px"><img src="__LOGO__" alt="Vereador Leo Pinto" style="width:150px"><span style="font:700 10px var(--f-dado);letter-spacing:.24em;color:var(--amarelo)">CENTRAL · GABINETE</span></div>')
s = re.sub(r'<div class="seletor">.*?</select></div>', '', s, count=1, flags=re.S)
troca("let cli='apple';", "let cli='leo';")
troca("try{cli=localStorage.getItem('painel-cliente')||'apple'}catch(e){}", '')
troca("$('#cliente').onchange=e=>{cli=e.target.value;try{localStorage.setItem('painel-cliente',cli)}catch(_){}render()};", '')
troca(";$('#cliente').value=cli;", ';')
troca('<div class="avatar" title="Lindson Almeida (admin)">LA</div>', '<div class="avatar" title="Gabinete Leo Pinto">LP</div>')

# 3 · grupo "Vendas e tráfego" vira "Gabinete" (demandas, prestação de contas, agenda) + campanhas
troca('<div class="grupo"><h4>Vendas e tráfego</h4>', '<div class="grupo"><h4>Gabinete</h4>'
      '<a href="#demandas" data-v="demandas"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 5h16M4 12h16M4 19h10"/></svg>Demandas</a>'
      '<a href="#prestacao" data-v="prestacao"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M5 13l4 4L19 7"/></svg>Prestação de contas</a>'
      '<a href="#agenda" data-v="agenda"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/></svg>Agenda do mandato</a>')
s = re.sub(r'<a href="#leads" data-v="leads">.*?</a>', '', s, count=1, flags=re.S)
troca("const V={", "const V=window.__V={"); troca("const T={", "const T=window.__T={")
troca("function toast(t){", "window.__toast=t=>toast(t);function toast(t){")
troca("const f=$('#novo-ped');", "if(window.__pos)window.__pos(view);const f=$('#novo-ped');")
troca("addEventListener('hashchange',render);render();", "window.__render=render;window.__h={BASE,APROV,PEDIDOS,bomDia,chip,cli:()=>cli};addEventListener('hashchange',render);setTimeout(render,0);")

# 4 · Aprovações: as 3 artes de apresentação (feed v13, versão 3) com as legendas. Os exemplos antigos (v12) saíram
#     a pedido do Lindson (02/11/2026): usavam os grafismos eliminados da identidade.
import json as _j
V13 = os.path.join(D, '..', '..', 'clientes', 'leo-pinto', 'instagram-v13-apresentacao')
def _legendas():
    t = open(os.path.join(V13, 'TEXTOS.md')).read().split('## 3. Legendas da versão 3')[1]
    partes = re.split(r'\n### Post \d[^\n]*\n', t)[1:]
    return [x.split('\n---')[0].strip() for x in partes]
LEG = _legendas()
POSTS13 = [('leo-v13-3-direita', 'Post único', 'Apresentação 1/3 · Do povo para o povo', 'Postar 1º (painel da direita)'),
           ('leo-v13-2-meio', 'Post único', 'Apresentação 2/3 · Leo Pinto, vereador mais bem votado', 'Postar 2º (painel do meio)'),
           ('leo-v13-1-esquerda', 'Post único', 'Apresentação 3/3 · Prazer, eu sou o Leo', 'Postar 3º (painel da esquerda)')]
assert len(LEG) == 3, 'legendas da versão 3 não encontradas no TEXTOS.md'
# datas comemorativas (feed v14, versão 2, 03/11/2026): legendas do TEXTOS.md e tag da linha editorial de cada post
V14 = os.path.join(D, '..', '..', 'clientes', 'leo-pinto', 'instagram-v14-datas')
LEG14 = re.findall(r'\*\*Legenda:\*\*\s*```\n(.*?)\n```', open(os.path.join(V14, 'TEXTOS.md')).read(), flags=re.S)
T14 = _j.load(open(os.path.join(V14, 'textos.json')))
POSTS14 = [('p1-15-11', 'p1'), ('p2-20-11', 'p2'), ('p3-11-12', 'p3'), ('p4-25-12', 'p4'), ('p5-31-12', 'p5'), ('p6-01-01', 'p6')]
assert len(LEG14) == 6, 'legendas do v14 não encontradas no TEXTOS.md'
itens = [{'t': t, 'titulo': ti, 'data': da, 'linha': 'Apresentação', 'st': 'aguardando', 'img': uri(os.path.join(V13, n + '.jpg'), 720, 'JPEG'), 'legenda': LEG[i]}
         for i, (n, t, ti, da) in enumerate(POSTS13)]
itens += [{'t': 'Post único', 'titulo': 'Data comemorativa · ' + T14[k]['data'], 'data': f'Postar em {T14[k]["data"].split(" ·")[0]}', 'linha': T14[k]['linha'], 'st': 'aguardando',
           'img': uri(os.path.join(V14, n + '.jpg'), 720, 'JPEG'), 'legenda': LEG14[i]} for i, (n, k) in enumerate(POSTS14)]
aprov = ','.join(_j.dumps(x, ensure_ascii=False) for x in itens)
PREVIA14 = uri(os.path.join(V14, 'previa-feed.jpg'), 1000, 'JPEG')
PREVIA = uri(os.path.join(V13, 'previa-grade.jpg'), 1000, 'JPEG')
s = re.sub(r"const APROV=\[.*?\];", lambda m: f"const APROV=[{aprov}];", s, count=1, flags=re.S)
troca('<div class="post"><div class="img">${p.titulo}</div>', '<div class="post">${p.img?`<img src="${p.img}" alt="${p.titulo}" style="width:100%;aspect-ratio:4/5;object-fit:cover;display:block">`:`<div class="img">${p.titulo}</div>`}')
troca('<div class="d" style="color:var(--apagado);font-size:12.5px">${p.data}</div>',
      '<div class="d" style="color:var(--apagado);font-size:12.5px">${p.data}</div>${p.linha?`<span style="display:inline-block;margin-top:8px;padding:3px 10px;border-radius:999px;font-size:11.5px;font-weight:800;background:var(--laranja);color:#fff">${p.linha}</span>`:\'\'}<div style="font-weight:700;margin:6px 0 2px">${p.titulo}</div>'
      '${p.legenda?`<details style="margin:8px 0"><summary style="cursor:pointer;color:var(--amarelo);font-weight:700">Ver legenda</summary><pre style="white-space:pre-wrap;font:inherit;font-size:13px;line-height:1.5;margin:10px 0;max-height:320px;overflow:auto">${p.legenda.replace(/</g,"&lt;")}</pre><button class="btn lin" onclick="navigator.clipboard.writeText(this.previousElementSibling.textContent);window.__toast&&window.__toast(\'Legenda copiada\')">Copiar legenda</button></details>`:\'\'}')
troca('<p class="sub">Aprove ou peça ajuste. A equipe é avisada na hora.</p>',
      '<p class="sub">Aprove ou peça ajuste. A equipe é avisada na hora.</p>'
      f'<div style="margin:6px 0 18px;max-width:560px"><div style="font-weight:700;margin-bottom:8px">Como o seu feed fica (ordem de postagem, mais novo no topo)</div><img src="{PREVIA14}" alt="Prévia do feed" style="width:100%;border-radius:12px;display:block"><p class="sub" style="margin-top:8px">Embaixo, a apresentação em 3 partes (postar 1º, 2º e 3º sem outro post no meio e fixar as três). Em cima, as datas comemorativas até 01/01. A etiqueta laranja em cada post mostra a linha editorial: com quem ele fala.</p></div>')
troca("carrosseis:[['5 erros que fazem você perder clientes','aprovado'],['Antes de comprar, veja isso','em revisão'],['Perguntas que mais recebemos','em produção']]",
      "carrosseis:[['Pedimos, fizemos, entregamos: capa do carrossel','em produção'],['O que a gente já fez no mês','ideia'],['Causas do mandato: saúde, água, obras','ideia']]")
troca("reels:[['Bastidores da semana','aprovado'],['Um dia com a equipe','em produção'],['Responda em 30 segundos: dúvida do cliente','ideia']]",
      "reels:[['Um dia de mandato na rua','em produção'],['30 segundos: a pauta da Câmara','ideia'],['Visita ao povoado','ideia']]")
troca("datas:[['15/11','Proclamação da República','Post institucional'],['20/11','Dia da Consciência Negra','Carrossel de valorização'],['28/11','Black Friday','Campanha + stories em sequência'],['25/12','Natal','Reels de agradecimento']]",
      "datas:[['15/11','Proclamação da República','Post institucional'],['20/11','Dia da Consciência Negra','Carrossel de valorização'],['24/06','São João (padroeiro)','Post de festa e cultura'],['25/12','Natal','Reels de agradecimento']]")

# 5 · bloco de promoção do Lindson: portfólio real; a foto do Lindson fica fora do Git (sem ela, o slide 1 mostra só o nome)
CASOS = os.path.join(SC, 'fotos', 'casos')
for k, f in [('RAFAEL1', 'rafael.webp'), ('SF1', 'sf.webp'), ('PASSAPORTE1', 'passaporte-1.webp'), ('RAPOSA1', 'raposa-1.webp')]:
    p = os.path.join(CASOS, f); s = s.replace(f'__{k}__', webp(p) if os.path.exists(p) else '')
cine = os.path.join(SC, 'fotos', 'principal-cine.webp')
s = s.replace('<img src="__CINE__" alt="Lindson Almeida">', f'<img src="{webp(cine)}" alt="Lindson Almeida">' if os.path.exists(cine) else '')

s = s.replace('__LOGO__', uri(os.path.join(IG, 'marca', 'logo_principal.png'), 360))
# dados reais: no repositório PRIVADO (CentralLindsonALmeida/dados/leo.json), lidos aqui e aplicados pelo prototipo/real.js (conta Lindson, 01/11)
import json
pj = os.path.join(os.environ.get('CENTRAL_DADOS', os.path.join(D, '..', '..', '..', '..', 'centrallindsonalmeida', 'dados')), 'leo.json')
if os.path.exists(pj): dados = json.load(open(pj))
else:
    print('AVISO: sem', pj, '· o painel sai com tudo "a medir"')
    dados = {'nome': 'Vereador Leo Pinto', 'seg': 'Vereador de São João Batista/MA', 'plano': 'Comunicação do mandato', 'inicio': 'Outubro/2026', 'atualizado': '—'}
extra = ('window.__DADOS=' + json.dumps(dados, ensure_ascii=False).replace('</', '<\\/') + ';\n' + open(os.path.join(SC, 'prototipo', 'real.js')).read()
         + '\n' + open(os.path.join(SC, 'prototipo', 'kvdb.js')).read() + '\n' + open(os.path.join(D, 'gabinete.js')).read() + '\n' + open(os.path.join(SC, 'prototipo', 'fotos.js')).read() + '\n' + open(os.path.join(SC, 'prototipo', 'interacoes.js')).read() + '\n' + open(os.path.join(SC, 'prototipo', 'movimento.js')).read())  # fotos.js por último: ele encadeia o __pos dos anteriores
s = s.replace('</script>', '</script>\n<script>\n' + extra + '\n</script>', 1)
s = s.replace('<meta charset="utf-8">\n', '', 1)
open(os.path.join(D, 'painel-leo.html'), 'w').write(s)
print('painel-leo.html', round(len(s) / 1024), 'KB')
