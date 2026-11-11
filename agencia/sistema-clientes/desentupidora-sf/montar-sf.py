"""Painel da Desentupidora SF = o modelo da Central (../prototipo/painel.html) com a identidade do cliente
(azul marinho e royal + laranja, Montserrat, logo oficial do site desentupidorasf.pages.dev) e a área "Gestão" (CRM de chamados,
Financeiro e Notícias, prototipo/ferramentas.js com as palavras do negócio). Mesmo método do montar-jaci.py: trocas pontuais no modelo.
python3 montar-sf.py -> painel-sf.html. Conta Zuleide, 03/11/2026."""
import base64, io, json, os, re
from PIL import Image
D = os.path.dirname(os.path.abspath(__file__)); SC = os.path.join(D, '..')
CL = os.path.join(D, '..', '..', 'clientes', 'desentupidora-sf')

def uri(p, w, q=84):
    im = Image.open(p).convert('RGB'); im.thumbnail((w, w * 4))
    b = io.BytesIO(); im.save(b, 'JPEG', quality=q, optimize=True)
    return 'data:image/jpeg;base64,' + base64.b64encode(b.getvalue()).decode()
def webp(p): return 'data:image/webp;base64,' + base64.b64encode(open(p, 'rb').read()).decode()

s = open(os.path.join(SC, 'prototipo', 'painel.html')).read()
def troca(velho, novo, n=1):
    global s
    assert velho in s, 'o modelo mudou, ajuste: ' + velho[:60]
    s = s.replace(velho, novo) if n == 0 else s.replace(velho, novo, n)

# 1 · identidade do cliente (site e flyer): marinho #0a2a6e, royal #1d5fd0, céu #3fa9ff, laranja #ff6a00/#ff8a00, Montserrat
troca('<title>Painel do Cliente</title>', '<title>Desentupidora SF · Central</title>')
troca('family=Big+Shoulders+Display:wght@700;800&family=Manrope:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500', 'family=Montserrat:ital,wght@0,500;0,600;0,700;0,800;0,900;1,900')
troca("--fundo:#09090A;--painel:#121213;--painel2:#18181A;--linha:#242427;--amarelo:#F5C518;--amarelo2:#FFDD55;",
      "--fundo:#04102B;--painel:#0A2150;--painel2:#0F2A61;--linha:#1C3B7A;--amarelo:#FF8A00;--amarelo2:#FFB020;")
troca("--texto:#F3F0E6;--apagado:#8E8B83;", "--texto:#EEF4FF;--apagado:#A3B7DD;")
troca("--f-titulo:'Big Shoulders Display','Arial Narrow',Impact,sans-serif;--f-corpo:'Manrope',system-ui,sans-serif;--f-dado:'IBM Plex Mono',ui-monospace,monospace;",
      "--f-titulo:'Montserrat',system-ui,sans-serif;--f-corpo:'Montserrat',system-ui,sans-serif;--f-dado:'Montserrat',system-ui,sans-serif;")
for a, b in [('rgba(245,197,24', 'rgba(255,138,0'), ('#F5C518', '#FF8A00'), ('#0C0C0D', '#061639'), ('rgba(9,9,10,.92)', 'rgba(4,16,43,.92)'),
             ('#070707', '#030C22'), ('#C9C5BA', '#C8D6F2'), ('#0A0A0A', '#0A2A6E'), ('#2a2412,#0f0f10', '#1D5FD0,#0A2A6E'), ('#242427', '#1C3B7A'), ('#8E8B83', '#A3B7DD'),
             ('#121213', '#0A2150'), ('#F3F0E6', '#EEF4FF'), ("['#F5C518','#C99A10','#6E5A1C']", "['#FF8A00','#3FA9FF','#1D5FD0']")]:
    s = s.replace(a, b)
troca('.menu{position:sticky;top:0;height:100vh;', '.menu{background:linear-gradient(180deg,#0A2A6E,#04102B)!important;position:sticky;top:0;height:100vh;')
troca('.kpi .val{font:800 34px/1.1', '.kpi .val{font:900 32px/1.1')
troca('.topo h1{margin:0;font:800 26px/1', '.topo h1{margin:0;font:900 italic 24px/1')

# 2 · cabeçalho do menu com a logo oficial; painel do cliente SF (sem seletor de admin)
troca('<div class="logo"><b>LA</b>Central</div>', '<div class="logo" style="display:grid;gap:8px;justify-items:start"><img src="__LOGO__" alt="Desentupidora SF" style="width:96px;border-radius:50%"><span style="font:800 10px var(--f-dado);letter-spacing:.24em;color:var(--amarelo)">CENTRAL DO CLIENTE</span></div>')
s = re.sub(r'<div class="seletor">.*?</select></div>', '', s, count=1, flags=re.S)
troca("let cli='apple';", "let cli='sf';")
troca("try{cli=localStorage.getItem('painel-cliente')||'apple'}catch(e){}", '')
troca("$('#cliente').onchange=e=>{cli=e.target.value;try{localStorage.setItem('painel-cliente',cli)}catch(_){}render()};", '')
troca(";$('#cliente').value=cli;", ';')
troca('<div class="avatar" title="Lindson Almeida (admin)">LA</div>', '<div class="avatar" title="Desentupidora SF">SF</div>')
troca("const BASE={", "const BASE={sf:{nome:'Desentupidora SF',seg:'',plano:'',inicio:'',kpis:[],canais:[],metas:[]},")
troca("const FRASES={", "const FRASES={sf:['Quem está com a pia entupida não pesquisa: chama quem responde primeiro. Responda o WhatsApp em até 5 minutos.',"
      "'Foto de antes e depois vende mais que qualquer anúncio. Fotografe o serviço de hoje.',"
      "'Cliente atendido bem vira avaliação no Google. Peça a sua hoje.',"
      "'Caixa de gordura limpa hoje é chamado garantido daqui a 6 meses. Anote o retorno no CRM.'],")
troca("const MISSOES={", "const MISSOES={sf:[['Responder todo WhatsApp em até 5 minutos',30],['Fotografar antes e depois de um serviço (com autorização)',25],"
      "['Pedir avaliação no Google para um cliente atendido',20],['Postar 1 story do serviço do dia',15],['Mandar as fotos novas pela aba Fotos',10]],")

# 3 · dados reais no repositório PRIVADO (CentralLindsonALmeida/dados/sf.json); sem o arquivo, tudo aparece "a medir"
DADOS = os.environ.get('CENTRAL_DADOS', os.path.join(D, '..', '..', '..', '..', 'centrallindsonalmeida', 'dados'))
pj = os.path.join(DADOS, 'sf.json')
if os.path.exists(pj): dados = json.load(open(pj))
else:
    print('AVISO: sem', pj, '(clone o repositório privado ao lado deste) · o painel sai com tudo "a medir"')
    dados = {'nome': 'Desentupidora SF', 'seg': 'Desentupimento em São Luís e Grande Ilha', 'plano': '', 'inicio': 'Outubro/2026', 'atualizado': '—'}

# 4 · Aprovações: só entra o que o Lindson aprovou na conversa (regra 7b da MEMORIA). As artes ficam em clientes/desentupidora-sf/instagram-v1/.
MOSTRAR_V1 = True  # aprovadas pelo Lindson em 03/11/2026 ("aprovado, pode subir")
V1 = os.path.join(CL, 'instagram-v1'); itens = []
if MOSTRAR_V1:
    TX = json.load(open(os.path.join(V1, 'textos.json')))
    TIT = {'p1': 'Água voltando pelo ralo?', 'p2': 'Óleo na pia entope o cano', 'p3': 'Caixa de esgoto cheia assim?', 'p4': 'Enquete: o que já entupiu aí na sua casa?'}
    for k in sorted(TX):
        t = TX[k]; arq = os.path.join(V1, t.get('arquivo', k + '.jpg'))
        itens.append({'t': 'Post único', 'titulo': t.get('titulo') or TIT.get(k, k), 'data': 'Postar em ' + t.get('data', 'a combinar'), 'linha': t.get('linha', ''), 'st': 'aguardando', 'img': uri(arq, 720), 'legenda': t.get('legenda', '')})
aprov = ','.join(json.dumps(x, ensure_ascii=False) for x in itens)
s = re.sub(r"const APROV=\[.*?\];", lambda m: f"const APROV=[{aprov}];", s, count=1, flags=re.S)
troca('<div class="post"><div class="img">${p.titulo}</div>', '<div class="post">${p.img?`<img src="${p.img}" alt="${p.titulo}" style="width:100%;aspect-ratio:4/5;object-fit:cover;display:block">`:`<div class="img">${p.titulo}</div>`}')
troca('<div class="d" style="color:var(--apagado);font-size:12.5px">${p.data}</div>',
      '<div class="d" style="color:var(--apagado);font-size:12.5px">${p.data}</div>${p.linha?`<span style="display:inline-block;margin-top:8px;padding:3px 10px;border-radius:999px;font-size:11.5px;font-weight:800;background:var(--amarelo);color:#04102B">${p.linha}</span>`:\'\'}<div style="font-weight:700;margin:6px 0 2px">${p.titulo}</div>'
      '${p.por?`<div style="font-size:12px;color:${p.st===\'aprovado\'?\'#4ADE80\':\'var(--amarelo)\'};margin-top:2px">${p.st===\'aprovado\'?\'✓ Aprovado no site por\':\'Ajuste pedido\'}: ${p.por}${p.em?\', \'+new Date(p.em).toLocaleDateString(\'pt-BR\'):\'\'}</div>`:\'\'}'
      '${p.legenda?`<details style="margin:8px 0"><summary style="cursor:pointer;color:var(--amarelo);font-weight:700">Ver legenda</summary><pre style="white-space:pre-wrap;font:inherit;font-size:13px;line-height:1.5;margin:10px 0;max-height:320px;overflow:auto">${p.legenda.replace(/</g,"&lt;")}</pre><button class="btn lin" onclick="navigator.clipboard.writeText(this.previousElementSibling.textContent);window.__toast&&window.__toast(\'Legenda copiada\')">Copiar legenda</button></details>`:\'\'}')
if MOSTRAR_V1 and os.path.exists(os.path.join(V1, 'previa-feed.jpg')):
    troca('<p class="sub">Aprove ou peça ajuste. A equipe é avisada na hora.</p>',
          '<p class="sub">Aprove ou peça ajuste. A equipe é avisada na hora.</p>'
          f'<div style="margin:6px 0 18px;max-width:560px"><div style="font-weight:700;margin-bottom:8px">Como o seu feed fica (ordem de postagem, mais novo no topo)</div><img src="{uri(os.path.join(V1, "previa-feed.jpg"), 1000)}" alt="Prévia do feed" style="width:100%;border-radius:12px;display:block"><p class="sub" style="margin-top:8px">A etiqueta laranja em cada post mostra a linha editorial: com quem ele fala.</p></div>')
troca("carrosseis:[['5 erros que fazem você perder clientes','aprovado'],['Antes de comprar, veja isso','em revisão'],['Perguntas que mais recebemos','em produção']]",
      "carrosseis:[['5 sinais de que o esgoto vai entupir','ideia'],['O que nunca jogar na pia','ideia'],['Como funciona a visita da SF','ideia']]")
troca("reels:[['Bastidores da semana','aprovado'],['Um dia com a equipe','em produção'],['Responda em 30 segundos: dúvida do cliente','ideia']]",
      "reels:[['Antes e depois de um desentupimento','ideia'],['O equipamento que resolve sem quebrar o piso','ideia'],['Caixa de gordura: de quanto em quanto tempo limpar','ideia']]")

# 5 · grupo "Vendas e tráfego" vira "Gestão" (CRM de chamados, Financeiro, Notícias); sem a tela de leads de exemplo
troca('<div class="grupo"><h4>Vendas e tráfego</h4>', '<div class="grupo"><h4>Gestão</h4>'
      '<a href="#crm" data-v="crm"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="9" cy="8" r="3.5"/><path d="M2.5 20c.8-3.6 3.4-5.5 6.5-5.5s5.7 1.9 6.5 5.5M16 4.5a3.5 3.5 0 0 1 0 7M18.5 14.8c1.7.8 2.8 2.5 3.2 5.2"/></svg>CRM de chamados</a>'
      '<a href="#financeiro" data-v="financeiro"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="2.5" y="5.5" width="19" height="13" rx="2.5"/><circle cx="12" cy="12" r="2.6"/><path d="M6 9v.01M18 15v.01"/></svg>Financeiro</a>'
      '<a href="#noticias" data-v="noticias"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 5h13v14H6a2 2 0 0 1-2-2zM17 9h3v8a2 2 0 0 1-2 2"/><path d="M7.5 9h6M7.5 12.5h6M7.5 16h4"/></svg>Notícias do setor</a></div>'
      '<div class="grupo"><h4>Vendas e tráfego</h4>')
s = re.sub(r'<a href="#leads" data-v="leads">.*?</a>', '', s, count=1, flags=re.S)
troca("const V={", "const V=window.__V={"); troca("const T={", "const T=window.__T={")
troca("function toast(t){", "window.__toast=t=>toast(t);function toast(t){")
troca("const f=$('#novo-ped');", "if(window.__pos)window.__pos(view);const f=$('#novo-ped');")
troca("addEventListener('hashchange',render);render();", "window.__render=render;window.__h={BASE,APROV,PEDIDOS,bomDia,chip,cli:()=>cli};addEventListener('hashchange',render);setTimeout(render,0);")

FERR = {
  'negocio': 'Desentupidora SF', 'linkGoogle': '', 'retornoDias': 180, 'exEntrada': 'Ex.: Desentupimento de pia · João', 'exSaida': 'Ex.: Combustível da semana',
  'palavras': {'pac': 'cliente', 'Pac': 'Cliente', 'pacs': 'clientes', 'aval': 'visita', 'Aval': 'Visita', 'avals': 'visitas', 'Avals': 'Visitas',
               'proc': 'serviço', 'Proc': 'Serviço', 'procs': 'Serviços', 'fezProc': 'Fizeram o serviço', 'marcaram': 'Agendaram visita',
               'tinhaAval': 'de quem tinha visita agendada', 'negocio': 'a desentupidora', 'crm': 'CRM de chamados',
               'regra': 'Mensagens curtas e diretas: sem prometer preço antes de ver o serviço e sem prazo que a equipe não consegue cumprir.'},
  'origens': ['Google (site desentupidorasf.pages.dev)', 'Google Maps', 'Instagram', 'WhatsApp direto', 'Ligação', 'Indicação', 'Anúncio (Meta)', 'Cliente antigo', 'Outro'],
  'interesses': ['Desentupimento de pia', 'Desentupimento de ralo', 'Desentupimento de vaso sanitário', 'Desentupimento de esgoto', 'Limpeza de caixa de gordura', 'Desentupimento de calhas', 'Outro serviço'],
  'etapas': [
    {'id': 'novo', 'nome': 'Novo chamado', 'botao': 'Respondeu', 'depois': 'conversa',
     'msg': 'Oi, {nome}! Aqui é da {negocio}. Recebemos o seu chamado sobre {interesse}. Pode me mandar o endereço e uma foto do local? Assim já te passo o orçamento.'},
    {'id': 'conversa', 'nome': 'Orçamento enviado', 'botao': 'Agendou',
     'msg': 'Oi, {nome}! Conseguiu ver o orçamento para {interesse}? Tenho técnico disponível. Qual o melhor horário para a visita?'},
    {'id': 'marcada', 'nome': 'Visita agendada', 'botao': 'Técnico foi',
     'msg': 'Oi, {nome}! Confirmando a visita da {negocio} {quando}. O técnico avisa quando estiver a caminho.'},
    {'id': 'compareceu', 'nome': 'Visita feita', 'botao': 'Serviço feito',
     'msg': 'Oi, {nome}! O técnico já passou aí. Ficou alguma dúvida sobre o serviço? Posso fechar para fazer agora?'},
    {'id': 'fez', 'nome': 'Serviço feito', 'botao': 'Preventiva', 'depois': 'retorno',
     'msg': 'Oi, {nome}! Obrigado por chamar a {negocio}. Está tudo funcionando? Se puder, deixe uma avaliação no Google: ajuda muito a gente.'},
    {'id': 'retorno', 'nome': 'Manutenção preventiva', 'depois': 'conversa',
     'msg': 'Oi, {nome}! Já faz uns meses do serviço de {interesse}. Quer agendar uma limpeza preventiva para não entupir de novo?'},
    {'id': 'perdido', 'nome': 'Não fechou', 'depois': 'conversa',
     'msg': 'Oi, {nome}! Aqui é da {negocio}. O problema de {interesse} foi resolvido? Se ainda precisar, temos técnico disponível.'}],
  'catEntradas': ['Desentupimento', 'Limpeza de caixa de gordura', 'Esgoto e fossa', 'Calhas', 'Visita técnica', 'Outras entradas'],
  'catEntradaCRM': 'Desentupimento',
  'catSaidas': ['Combustível e deslocamento', 'Equipamentos e manutenção', 'Materiais e produtos', 'Salários e diárias', 'Anúncios (Meta e Google)', 'Agência e marketing', 'Impostos e taxas', 'Maquininha e taxas de cartão', 'Telefone e internet', 'Outras saídas'],
  'formas': ['Pix', 'Cartão de crédito', 'Cartão de débito', 'Dinheiro', 'Boleto', 'A definir'],
  'noticias': [
    {'nome': 'Desentupimento', 'q': 'desentupidora OR desentupimento'},
    {'nome': 'Saneamento em São Luís', 'q': 'saneamento São Luís OR Caema esgoto'},
    {'nome': 'Chuvas e alagamentos na Ilha', 'q': 'chuva São Luís alagamento'},
    {'nome': 'Caixa de gordura e esgoto', 'q': 'caixa de gordura OR rede de esgoto entupida'},
    {'nome': 'Serviços para casa', 'q': 'encanador OR serviços residenciais manutenção'},
    {'nome': 'Marketing para prestador de serviço', 'q': 'marketing prestador de serviços Google Meu Negócio'}],
  'notaNoticias': 'Notícias de portais públicos, atualizadas sozinhas a cada 3 horas. Antes de postar sobre uma delas, abra a fonte original.',
  'ideiaPost': 'Gancho: "Saiu uma notícia sobre {tema} e isso pode virar dor de cabeça na sua casa. Te explico em 30 segundos."\nNotícia: {titulo}\nFonte: {link}\nFechamento: chame a SF no WhatsApp (98) 92010-5710.'}

# 6 · bloco de promoção do Lindson: portfólio real, sem o próprio cliente
s = s.replace(" ['Conheça um dos nossos clientes','Desentupidora <em>SF</em>','Mini site para quem tem urgência: orçamento no WhatsApp e ligação em um toque.','__SF1__'],\n", '', 1)
CASOS = os.path.join(SC, 'fotos', 'casos')
for k, f in [('RAFAEL1', 'rafael.webp'), ('PASSAPORTE1', 'passaporte-1.webp'), ('RAPOSA1', 'raposa-1.webp')]:
    p = os.path.join(CASOS, f); s = s.replace(f'__{k}__', webp(p) if os.path.exists(p) else '')
cine = os.path.join(SC, 'fotos', 'principal-cine.webp')
s = s.replace('<img src="__CINE__" alt="Lindson Almeida">', f'<img src="{webp(cine)}" alt="Lindson Almeida">' if os.path.exists(cine) else '')

s = s.replace('__LOGO__', uri(os.path.join(D, 'logo.jpg'), 220))
extra = ('window.__DADOS=' + json.dumps(dados, ensure_ascii=False).replace('</', '<\\/') + ';\n' + open(os.path.join(SC, 'prototipo', 'real.js')).read()
         + '\n' + open(os.path.join(SC, 'prototipo', 'treinamento.js')).read() + '\nwindow.__FERR=' + json.dumps(FERR, ensure_ascii=False) + ';\n'
         + open(os.path.join(SC, 'prototipo', 'ferramentas.js')).read() + '\n' + open(os.path.join(SC, 'prototipo', 'fotos.js')).read()
         + '\n' + open(os.path.join(SC, 'prototipo', 'interacoes.js')).read() + '\n' + open(os.path.join(SC, 'prototipo', 'movimento.js')).read())  # fotos.js depois das ferramentas: ele encadeia o __pos
s = s.replace('</script>', '</script>\n<script>\n' + extra + '\n</script>', 1)
s = s.replace('<meta charset="utf-8">\n', '', 1)
open(os.path.join(D, 'painel-sf.html'), 'w').write(s)
print('painel-sf.html', round(len(s) / 1024), 'KB')
