"""Painel da WF Celulares = o modelo da Central (../prototipo/painel.html) com a identidade aprovada da WF
(caminho B "Assinatura", universo Apple: preto, grafite, titânio, prata, branco gelo; Inter; logo B branca).
Copiado do montar-rt.py com trocas pontuais. Aprovações = artes-02 (feed escuro), artes-marca (3 posts), avatar e destaques,
5 stories do case e o vídeo do processo, com as imagens em /painel/wf/ (privado). Entregas e arquivos = manual e logo.
Tela nova "Linha do tempo" (dados/wf.json → linha). python3 montar-wf.py -> painel-wf.html. Conta Zuleide, 10/11/2026."""
import base64, io, json, os, re
from PIL import Image
D = os.path.dirname(os.path.abspath(__file__)); SC = os.path.join(D, '..')
CL = os.path.join(D, '..', '..', 'clientes', 'wf-celulares')

def uri(p, w, q=84):
    im = Image.open(p).convert('RGB'); im.thumbnail((w, w * 4))
    b = io.BytesIO(); im.save(b, 'JPEG', quality=q, optimize=True)
    return 'data:image/jpeg;base64,' + base64.b64encode(b.getvalue()).decode()
def png(p): return 'data:image/png;base64,' + base64.b64encode(open(p, 'rb').read()).decode()
def webp(p): return 'data:image/webp;base64,' + base64.b64encode(open(p, 'rb').read()).decode()

s = open(os.path.join(SC, 'prototipo', 'painel.html')).read()
def troca(velho, novo, n=1):
    global s
    assert velho in s, 'o modelo mudou, ajuste: ' + velho[:60]
    s = s.replace(velho, novo) if n == 0 else s.replace(velho, novo, n)

# 1 · identidade aprovada (identidade/README.md, FINAL caminho B): preto #000, grafite #1D1D1F, titânio #8E8A84, prata #C7C9CC, gelo #F5F5F7; Inter
troca('<title>Painel do Cliente</title>', '<title>WF Celulares · Central</title>')
troca('family=Big+Shoulders+Display:wght@700;800&family=Manrope:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500', 'family=Inter:wght@400;500;600;700;800')
troca("--fundo:#09090A;--painel:#121213;--painel2:#18181A;--linha:#242427;--amarelo:#F5C518;--amarelo2:#FFDD55;",
      "--fundo:#000000;--painel:#1D1D1F;--painel2:#252527;--linha:#2E2E31;--amarelo:#C7C9CC;--amarelo2:#F5F5F7;")
troca("--texto:#F3F0E6;--apagado:#8E8B83;", "--texto:#F5F5F7;--apagado:#8E8A84;")
troca("--f-titulo:'Big Shoulders Display','Arial Narrow',Impact,sans-serif;--f-corpo:'Manrope',system-ui,sans-serif;--f-dado:'IBM Plex Mono',ui-monospace,monospace;",
      "--f-titulo:'Inter',system-ui,sans-serif;--f-corpo:'Inter',system-ui,sans-serif;--f-dado:'Inter',system-ui,sans-serif;")
for a, b in [('rgba(245,197,24', 'rgba(199,201,204'), ('#F5C518', '#C7C9CC'), ('#0C0C0D', '#0A0A0B'), ('rgba(9,9,10,.92)', 'rgba(0,0,0,.92)'),
             ('#070707', '#000000'), ('#C9C5BA', '#D2D2D7'), ('#0A0A0A', '#000000'), ('#2a2412,#0f0f10', '#3A3936,#0A0A0B'), ('#242427', '#2E2E31'), ('#8E8B83', '#8E8A84'),
             ('#121213', '#1D1D1F'), ('#F3F0E6', '#F5F5F7'), ("['#F5C518','#C99A10','#6E5A1C']", "['#F5F5F7','#C7C9CC','#8E8A84']")]:
    s = s.replace(a, b)
troca('.menu{position:sticky;top:0;height:100vh;', '.menu{background:linear-gradient(180deg,#1D1D1F,#000)!important;position:sticky;top:0;height:100vh;')
troca('.kpi .val{font:800 34px/1.1', '.kpi .val{font:600 32px/1.1;letter-spacing:-.02em')
troca('.topo h1{margin:0;font:800 26px/1', '.topo h1{margin:0;font:600 24px/1;letter-spacing:-.02em')

# 2 · cabeçalho do menu com a logo B branca; painel do cliente WF (sem seletor de admin)
troca('<div class="logo"><b>LA</b>Central</div>', '<div class="logo" style="display:grid;gap:10px;justify-items:start"><img src="__LOGO__" alt="WF Celulares" style="width:150px"><span style="font:600 10px var(--f-dado);letter-spacing:.24em;background:linear-gradient(90deg,#8E8A84,#C7C9CC);-webkit-background-clip:text;color:transparent">CENTRAL DO CLIENTE</span></div>')
s = re.sub(r'<div class="seletor">.*?</select></div>', '', s, count=1, flags=re.S)
troca("let cli='apple';", "let cli='wf';")
troca("try{cli=localStorage.getItem('painel-cliente')||'apple'}catch(e){}", '')
troca("$('#cliente').onchange=e=>{cli=e.target.value;try{localStorage.setItem('painel-cliente',cli)}catch(_){}render()};", '')
troca(";$('#cliente').value=cli;", ';')
troca('<div class="avatar" title="Lindson Almeida (admin)">LA</div>', '<div class="avatar" title="WF Celulares">WF</div>')
troca("const BASE={", "const BASE={wf:{nome:'WF Celulares',seg:'',plano:'',inicio:'',kpis:[],canais:[],metas:[]},")
troca("const FRASES={", "const FRASES={wf:['Quem pergunta preço de iPhone no WhatsApp está comparando lojas. Responda em poucos minutos.',"
      "'Seminovo vende com prova: mostre o laudo do aparelho no story antes de mandar o preço.',"
      "'Cliente que comprou bem indica. Peça um print do story dele marcando a loja.',"
      "'Foto real da loja vale mais que foto de banco. Mande as fotos novas pela aba Fotos.'],")
troca("const MISSOES={", "const MISSOES={wf:[['Responder todo WhatsApp em poucos minutos',30],['Postar nos stories 1 aparelho com o laudo',25],"
      "['Fotografar a loja e o balcão (São Cristóvão e Renascença)',20],['Pedir a um cliente o print do story marcando a WF',15],['Mandar as fotos novas pela aba Fotos',10]],")

# 3 · dados reais no repositório PRIVADO (CentralLindsonALmeida/dados/wf.json)
DADOS = os.environ.get('CENTRAL_DADOS', os.path.join(D, '..', '..', '..', '..', 'centrallindsonalmeida', 'dados'))
pj = os.path.join(DADOS, 'wf.json')
if os.path.exists(pj): dados = json.load(open(pj))
else:
    print('AVISO: sem', pj, '(clone o repositório privado ao lado deste) · o painel sai com tudo "a medir"')
    dados = {'nome': 'WF Celulares', 'seg': 'Loja de iPhone em São Luís', 'plano': '', 'inicio': 'Novembro/2026', 'atualizado': '—'}

# 4 · Aprovações: tudo "aguardando" (o cliente aprova no site). Fora: identidade v1 e artes-01 (reprovadas).
#     As imagens ficam no privado, em /painel/wf/ (só abre com login da WF ou do admin).
def legendas(md):
    t = open(md).read().split('## Legendas', 1)[1]
    return [x.strip() for x in re.split(r'\n\*\*\d\d · [^\n]*\n', t)[1:]]
L02 = legendas(os.path.join(CL, 'artes-01', 'README.md'))  # artes-02 usa as mesmas legendas (README da artes-02)
LM = legendas(os.path.join(CL, 'artes-marca', 'README.md'))
assert len(L02) == 9 and len(LM) == 3, 'legendas não encontradas'
FEED = [('01-black-30-dias', '30 dias de Black Friday', 'Oferta'), ('02-oferta-12-pro-max', 'iPhone 12 Pro Max · R$ 2.299', 'Oferta'),
        ('03-assistencia', 'Assistência técnica', 'Assistência'), ('04-oferta-17-pro-max-silver', 'iPhone 17 Pro Max Silver · R$ 6.499', 'Oferta'),
        ('05-laudo-wf', 'Laudo WF', 'Procedência'), ('06-oferta-iphone-11', 'iPhone 11 · R$ 1.399', 'Oferta'),
        ('07-prova-social', 'Quem compra na WF, volta', 'Prova'), ('08-oferta-17-pro-max-256', 'iPhone 17 Pro Max 256 GB · R$ 6.950', 'Oferta'),
        ('09-pagamento-entrega', 'Pagamento e entrega', 'Como comprar')]
MARCA = [('03-onde-estamos', 'Marca nova 1/3 · Onde estamos', 'Postar 1º'), ('02-procedencia', 'Marca nova 2/3 · Procedência', 'Postar 2º'),
         ('01-nova-wf', 'Marca nova 3/3 · Nova WF (revelação)', 'Postar 3º')]
LMD = dict(zip(['01-nova-wf', '02-procedencia', '03-onde-estamos'], LM))
NOTA = '\n\nImagem ilustrativa · Apple Newsroom. Uso da marca Apple autorizado ao cliente.'
itens = [{'t': 'Post único', 'titulo': t, 'data': o + ' · abre o feed novo', 'linha': 'Marca nova', 'st': 'aguardando', 'img': f'/painel/wf/marca/{n}.jpg', 'legenda': LMD[n] + NOTA} for n, t, o in MARCA]
for i, (n, t, l) in enumerate(FEED):
    leg = L02[i] + NOTA + ('\n\nATENÇÃO: o depoimento é exemplo ilustrativo. Publicar só com print real e autorização do cliente.' if n.startswith('07') else '')
    itens.append({'t': 'Post único', 'titulo': f'Feed {i + 1}/9 · {t}', 'data': 'Postar depois dos 3 da marca nova', 'linha': l, 'st': 'aguardando', 'img': f'/painel/wf/feed/{n}.jpg', 'legenda': leg})
BIO = 'Loja de celulares · São Luís\niPhone e Xiaomi lacrados e seminovos com laudo e garantia\nAssistência técnica com orçamento antes de mexer\n📍 São Cristóvão | Renascença'
itens.insert(0, {'t': 'Perfil · avatar + 6 destaques', 'titulo': 'Perfil novo: avatar, destaques e bio', 'data': 'Trocar antes do 1º post', 'linha': 'Perfil', 'st': 'aguardando',
                 'img': '/painel/wf/perfil/03-avatar.jpg', 'telas': [f'/painel/wf/perfil/{n}.jpg' for n in ['04-destaque-lacrados', '05-destaque-seminovos', '06-destaque-assistencia', '07-destaque-avaliacoes', '08-destaque-entrega', '09-destaque-localizacao']],
                 'legenda': 'Bio nova (até 150 caracteres):\n' + BIO + '\n\nCategoria: Loja de celulares · Link: WhatsApp (98) 98827-1882 com mensagem pronta.\nDestaques (nesta ordem): Lacrados · Seminovos · Assistência · Avaliações · Entrega · Localização.'})
itens.append({'t': 'Vídeo · Reels ~56 s', 'titulo': 'Vídeo do processo: a nova WF em 1 minuto', 'data': 'Postar como Reels depois dos 3 posts da marca', 'linha': 'Marca nova', 'st': 'aguardando',
              'img': '/painel/wf/video/poster.jpg', 'video': '/painel/wf/video/wf-processo.mp4',
              'legenda': 'Como nasceu a nova WF Celulares: do perfil antigo à marca nova, com o Laudo WF, o manual e as artes do feed.\nWhatsApp (98) 98827-1882.\n#WFCelulares #iPhoneSaoLuis #SaoLuisMA\n\nTrilha e efeitos: Mixkit (licença Mixkit). A voz é provisória e pode ser trocada.'})
itens.append({'t': 'Stories · 5 telas', 'titulo': 'Stories do case: antes e depois da marca (perfil do Lindson)', 'data': 'Para aprovar a divulgação do case', 'linha': 'Case', 'st': 'aguardando',
              'img': '/painel/wf/stories/01-antes-depois.jpg', 'telas': [f'/painel/wf/stories/{n}.jpg' for n in ['02-o-que-travava', '03-nova-marca', '04-aplicacoes', '05-cta']],
              'legenda': 'Sequência de 5 stories em que a agência mostra o trabalho da WF: 1 antes × depois · 2 o que travava · 3 nova marca e procedência · 4 aplicações (feed, avatar, fachada, manual) · 5 chamada.\nVão no perfil @lindsonalmeida_, marcando a loja. Só postamos com o seu OK aqui.'})
aprov = ','.join(json.dumps(x, ensure_ascii=False) for x in itens)
s = re.sub(r"const APROV=\[.*?\];", lambda m: f"const APROV=[{aprov}];", s, count=1, flags=re.S)
troca('<div class="post"><div class="img">${p.titulo}</div>', '<div class="post">${p.video?`<video src="${p.video}" poster="${p.img}" controls playsinline preload="none" style="width:100%;aspect-ratio:9/16;object-fit:cover;display:block;background:#000"></video><a class="btn lin" href="${p.video}" download style="display:block;text-align:center;margin:10px 12px 0">⬇ Baixar vídeo</a>`:p.img?`<img src="${p.img}" alt="${p.titulo}" style="width:100%;aspect-ratio:4/5;object-fit:cover;display:block">`:`<div class="img">${p.titulo}</div>`}')
troca('<div class="d" style="color:var(--apagado);font-size:12.5px">${p.data}</div>',
      '<div class="d" style="color:var(--apagado);font-size:12.5px">${p.data}</div>${p.linha?`<span style="display:inline-block;margin-top:8px;padding:3px 10px;border-radius:999px;font-size:11.5px;font-weight:700;background:linear-gradient(90deg,#8E8A84,#C7C9CC);color:#000">${p.linha}</span>`:\'\'}<div style="font-weight:700;margin:6px 0 2px">${p.titulo}</div>'
      '${p.telas?`<div style="display:flex;gap:6px;overflow-x:auto;margin:8px 0;padding-bottom:4px">${p.telas.map(t=>`<img src="${t}" style="height:120px;aspect-ratio:4/5;object-fit:cover;border-radius:6px;flex:none">`).join(\'\')}</div>`:\'\'}'
      '${p.por?`<div style="font-size:12px;color:${p.st===\'aprovado\'?\'#4ADE80\':\'var(--amarelo)\'};margin-top:2px">${p.st===\'aprovado\'?\'✓ Aprovado no site por\':\'Ajuste pedido\'}: ${p.por}${p.em?\', \'+new Date(p.em).toLocaleDateString(\'pt-BR\'):\'\'}</div>`:\'\'}'
      '${p.legenda?`<details style="margin:8px 0"><summary style="cursor:pointer;color:var(--amarelo);font-weight:700">Ver legenda</summary><pre style="white-space:pre-wrap;font:inherit;font-size:13px;line-height:1.5;margin:10px 0;max-height:320px;overflow:auto">${p.legenda.replace(/</g,"&lt;")}</pre><button class="btn lin" onclick="navigator.clipboard.writeText(this.previousElementSibling.textContent);window.__toast&&window.__toast(\'Legenda copiada\')">Copiar legenda</button></details>`:\'\'}')
troca('<p class="sub">Aprove ou peça ajuste. A equipe é avisada na hora.</p>',
      '<p class="sub">Aprove ou peça ajuste. A equipe é avisada na hora.</p>'
      '<div style="margin:6px 0 18px;max-width:560px"><div style="font-weight:700;margin-bottom:8px">Como as 9 artes ficam no seu feed</div><img src="/painel/wf/feed/previa.jpg" alt="Prévia do feed" style="width:100%;border-radius:12px;display:block"><p class="sub" style="margin-top:8px">Primeiro os 3 posts da marca nova, depois as 9 artes. As imagens são ilustrativas (Apple Newsroom) até chegarem as fotos reais da loja.</p></div>')
troca("carrosseis:[['5 erros que fazem você perder clientes','aprovado'],['Antes de comprar, veja isso','em revisão'],['Perguntas que mais recebemos','em produção']]",
      "carrosseis:[['Como conferir um iPhone seminovo antes de comprar','ideia'],['O que vem no Laudo WF','ideia'],['Lacrado ou seminovo: qual vale mais a pena?','ideia']]")
troca("reels:[['Bastidores da semana','aprovado'],['Um dia com a equipe','em produção'],['Responda em 30 segundos: dúvida do cliente','ideia']]",
      "reels:[['Abrindo a caixa de um iPhone lacrado','ideia'],['O teste do laudo em 30 segundos','ideia'],['Troca de tela do começo ao fim','ideia']]")

# 5 · sem a tela de leads de exemplo; tela nova "Linha do tempo" no grupo Conteúdo
s = re.sub(r'<a href="#leads" data-v="leads">.*?</a>', '', s, count=1, flags=re.S)
troca('<a href="#entregas" data-v="entregas">', '<a href="#linha" data-v="linha"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M6 3v18"/><circle cx="6" cy="7" r="2"/><circle cx="6" cy="17" r="2"/><path d="M11 7h9M11 17h9"/></svg>Linha do tempo</a><a href="#entregas" data-v="entregas">')
troca("const V={", "const V=window.__V={"); troca("const T={", "const T=window.__T={")
troca("function toast(t){", "window.__toast=t=>toast(t);function toast(t){")
troca("const f=$('#novo-ped');", "if(window.__pos)window.__pos(view);const f=$('#novo-ped');")
troca("addEventListener('hashchange',render);render();", "window.__render=render;window.__h={BASE,APROV,PEDIDOS,bomDia,chip,cli:()=>cli};addEventListener('hashchange',render);setTimeout(render,0);")

# 6 · bloco de promoção do Lindson: portfólio real
CASOS = os.path.join(SC, 'fotos', 'casos')
for k, f in [('RAFAEL1', 'rafael.webp'), ('SF1', 'sf.webp'), ('PASSAPORTE1', 'passaporte-1.webp'), ('RAPOSA1', 'raposa-1.webp')]:
    p = os.path.join(CASOS, f); s = s.replace(f'__{k}__', webp(p) if os.path.exists(p) else '')
cine = os.path.join(SC, 'fotos', 'principal-cine.webp')
s = s.replace('<img src="__CINE__" alt="Lindson Almeida">', f'<img src="{webp(cine)}" alt="Lindson Almeida">' if os.path.exists(cine) else '')

s = s.replace('__LOGO__', png(os.path.join(CL, 'identidade', 'logo-b', 'wf-logo-b-branca.png')))
BAIXAR = """window.__V.entregas = () => `<div class="card"><h3>Entregas e arquivos</h3><p class="sub">Manual da marca, logo e tudo o que a agência já entregou. Toque em Baixar para salvar o arquivo.</p><div class="tab"><table><thead><tr><th>Entrega</th><th>Tipo</th><th>Data</th><th>Status</th><th></th></tr></thead><tbody>${(window.__DADOS.entregas || []).map(e => `<tr><td>${e[0]}</td><td>${e[1]}</td><td>${e[2]}</td><td>${window.__h.chip(e[3])}</td><td>${e[4] ? `<a class="btn lin" href="${e[4]}" download>Baixar</a>` : ''}</td></tr>`).join('')}</tbody></table></div></div>`;
window.__V.linha = () => `<div class="card"><h3>Linha do tempo</h3><p class="sub">O que já foi feito na sua marca e o que vem agora.</p><div style="display:grid;gap:0;margin-top:10px">${(window.__DADOS.linha || []).map((e, i, a) => `<div style="display:grid;grid-template-columns:22px 1fr;gap:12px"><div style="display:flex;flex-direction:column;align-items:center"><span style="width:12px;height:12px;border-radius:50%;margin-top:4px;background:${e[2] === 'feito' ? 'linear-gradient(135deg,#F5F5F7,#8E8A84)' : 'transparent'};border:2px solid #C7C9CC"></span>${i < a.length - 1 ? '<span style="flex:1;width:2px;background:var(--linha);margin:4px 0"></span>' : ''}</div><div style="padding-bottom:18px"><div style="font:600 11px var(--f-dado);letter-spacing:.12em;color:var(--apagado);text-transform:uppercase">${e[0]}</div><div style="font-weight:600;margin:3px 0 6px">${e[1]}</div>${window.__h.chip(e[2])}</div></div>`).join('')}</div></div>`;
if (window.__T) window.__T.linha = 'Linha do tempo';"""
extra = ('window.__DADOS=' + json.dumps(dados, ensure_ascii=False).replace('</', '<\\/') + ';\n' + open(os.path.join(SC, 'prototipo', 'real.js')).read()
         + '\n' + BAIXAR + '\n' + open(os.path.join(SC, 'prototipo', 'treinamento.js')).read() + '\n' + open(os.path.join(SC, 'prototipo', 'fotos.js')).read()
         + '\n' + open(os.path.join(SC, 'prototipo', 'interacoes.js')).read() + '\n' + open(os.path.join(SC, 'prototipo', 'movimento.js')).read())  # fotos.js por último entre os de tela: ele encadeia o __pos
s = s.replace('</script>', '</script>\n<script>\n' + extra + '\n</script>', 1)
s = s.replace('<meta charset="utf-8">\n', '', 1)
open(os.path.join(D, 'painel-wf.html'), 'w').write(s)
print('painel-wf.html', round(len(s) / 1024), 'KB')
