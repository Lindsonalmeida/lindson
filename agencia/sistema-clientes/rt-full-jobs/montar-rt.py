"""Painel da Real Time (RT Full Jobs) = o modelo da Central (../prototipo/painel.html) com a marca nova v1 da Real Time
(Preto Set, Azul Real, REC vermelho, Geist + Geist Mono, símbolo rt) e a área "Gestão" (CRM de reservas, Financeiro e Notícias).
Copiado do montar-sf.py (conta Zuleide) com trocas pontuais. Aprovações = artes v1 + legendas + capas de destaques; Entregas com
os PDFs (manual e estratégia) para baixar em /painel/rt/arquivos/. python3 montar-rt.py -> painel-rt.html. Conta Leandro, 03/11/2026."""
import base64, io, json, os, re
from PIL import Image
D = os.path.dirname(os.path.abspath(__file__)); SC = os.path.join(D, '..')
CL = os.path.join(D, '..', '..', 'clientes', 'rt-full-jobs')

def uri(p, w, q=84):
    im = Image.open(p).convert('RGB'); im.thumbnail((w, w * 4))
    b = io.BytesIO(); im.save(b, 'JPEG', quality=q, optimize=True)
    return 'data:image/jpeg;base64,' + base64.b64encode(b.getvalue()).decode()
def svg(p): return 'data:image/svg+xml;base64,' + base64.b64encode(open(p, 'rb').read()).decode()
def webp(p): return 'data:image/webp;base64,' + base64.b64encode(open(p, 'rb').read()).decode()

s = open(os.path.join(SC, 'prototipo', 'painel.html')).read()
def troca(velho, novo, n=1):
    global s
    assert velho in s, 'o modelo mudou, ajuste: ' + velho[:60]
    s = s.replace(velho, novo) if n == 0 else s.replace(velho, novo, n)

# 1 · marca nova v1 (identidade/v1/README.md): Preto Set #0E0E0F, Grafite #1A1A1B, Branco Luz #F4F7FB, Azul Real #2E9BFF, REC #FF3B3B; Geist + Geist Mono
troca('<title>Painel do Cliente</title>', '<title>Real Time · Central</title>')
troca('family=Big+Shoulders+Display:wght@700;800&family=Manrope:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500', 'family=Geist:wght@400;500;600;700;800&family=Geist+Mono:wght@400;500')
troca("--fundo:#09090A;--painel:#121213;--painel2:#18181A;--linha:#242427;--amarelo:#F5C518;--amarelo2:#FFDD55;",
      "--fundo:#0E0E0F;--painel:#1A1A1B;--painel2:#222224;--linha:#2A2A2C;--amarelo:#2E9BFF;--amarelo2:#6BB8FF;")
troca("--texto:#F3F0E6;--apagado:#8E8B83;", "--texto:#F4F7FB;--apagado:#8A8A8E;")
troca("--f-titulo:'Big Shoulders Display','Arial Narrow',Impact,sans-serif;--f-corpo:'Manrope',system-ui,sans-serif;--f-dado:'IBM Plex Mono',ui-monospace,monospace;",
      "--f-titulo:'Geist',system-ui,sans-serif;--f-corpo:'Geist',system-ui,sans-serif;--f-dado:'Geist Mono',ui-monospace,monospace;")
for a, b in [('rgba(245,197,24', 'rgba(46,155,255'), ('#F5C518', '#2E9BFF'), ('#0C0C0D', '#111113'), ('rgba(9,9,10,.92)', 'rgba(14,14,15,.92)'),
             ('#070707', '#08080A'), ('#C9C5BA', '#CFD3DA'), ('#0A0A0A', '#05070B'), ('#2a2412,#0f0f10', '#4338F0,#0E0E0F'), ('#242427', '#2A2A2C'), ('#8E8B83', '#8A8A8E'),
             ('#121213', '#1A1A1B'), ('#F3F0E6', '#F4F7FB'), ("['#F5C518','#C99A10','#6E5A1C']", "['#2E9BFF','#4338F0','#FF3B3B']")]:
    s = s.replace(a, b)
troca('.menu{position:sticky;top:0;height:100vh;', '.menu{background:#0A0A0B!important;position:sticky;top:0;height:100vh;')
troca('.kpi .val{font:800 34px/1.1', '.kpi .val{font:600 32px/1.1')
troca('.topo h1{margin:0;font:800 26px/1', '.topo h1{margin:0;font:600 24px/1')

# 2 · cabeçalho do menu com a logo oficial; painel do cliente RT (sem seletor de admin)
troca('<div class="logo"><b>LA</b>Central</div>', '<div class="logo" style="display:grid;gap:8px;justify-items:start"><img src="__LOGO__" alt="Real Time" style="width:150px"><span style="font:500 10px var(--f-dado);letter-spacing:.24em;color:var(--apagado)"><i style="font-style:normal;color:#FF3B3B">●</i> CENTRAL DO CLIENTE</span></div>')
s = re.sub(r'<div class="seletor">.*?</select></div>', '', s, count=1, flags=re.S)
troca("let cli='apple';", "let cli='rt';")
troca("try{cli=localStorage.getItem('painel-cliente')||'apple'}catch(e){}", '')
troca("$('#cliente').onchange=e=>{cli=e.target.value;try{localStorage.setItem('painel-cliente',cli)}catch(_){}render()};", '')
troca(";$('#cliente').value=cli;", ';')
troca('<div class="avatar" title="Lindson Almeida (admin)">LA</div>', '<div class="avatar" title="Real Time">RT</div>')
troca("const BASE={", "const BASE={rt:{nome:'Real Time',seg:'',plano:'',inicio:'',kpis:[],canais:[],metas:[]},")
troca("const FRASES={", "const FRASES={rt:['Quem precisa de kit para sexta decide hoje. Responda o WhatsApp em poucos minutos.',"
      "'Kit parado não paga nada. Poste a agenda livre da semana nos stories.',"
      "'Todo job vira conteúdo: grave 15 segundos de bastidor antes de desmontar o set.',"
      "'Cliente satisfeito vira depoimento. Peça a fala de quem gravou ontem.'],")
troca("const MISSOES={", "const MISSOES={rt:[['Responder todo WhatsApp em poucos minutos',30],['Postar nos stories as datas livres da semana',25],"
      "['Gravar 15 s de bastidor do job do dia',20],['Pedir a fala de um cliente que gravou',15],['Mandar as fotos novas pela aba Fotos',10]],")

# 3 · dados reais no repositório PRIVADO (CentralLindsonALmeida/dados/rt.json); sem o arquivo, tudo aparece "a medir"
DADOS = os.environ.get('CENTRAL_DADOS', os.path.join(D, '..', '..', '..', '..', 'centrallindsonalmeida', 'dados'))
pj = os.path.join(DADOS, 'rt.json')
if os.path.exists(pj): dados = json.load(open(pj))
else:
    print('AVISO: sem', pj, '(clone o repositório privado ao lado deste) · o painel sai com tudo "a medir"')
    dados = {'nome': 'Real Time', 'seg': 'Locação de equipamento de cinema, estúdio e produção audiovisual', 'plano': '', 'inicio': 'Novembro/2026', 'atualizado': '—'}

# 4 · Aprovações: o Lindson mandou subir (03/11, "suba o painel do cliente e todos esses conteúdos lá") = aprovou a CRIAÇÃO; a aprovação da arte é do cliente no site.
#     Ficam de fora o post 05 e o story 03 (depoimento): só saem com fala real de cliente.
V1 = os.path.join(CL, 'instagram-v1'); itens = []
LEG = {}
for bloco in open(os.path.join(V1, 'LEGENDAS.md')).read().split('\n## ')[1:]:
    cab, _, corpo = bloco.partition('\n'); m = re.match(r'(Feed|Stories) ?(\d\d)?', cab)
    if m and m.group(2): LEG[m.group(2)] = corpo.split('\n---')[0].strip()
FEED = [('01', 'feed-01-kit-cinema', 'Seu set começa aqui (Kit Cinema)', 'Kit em ação', '09/11'), ('02', 'feed-02-estudio-verde', 'Estúdio fundo verde', 'Estúdio pronto', '11/11'),
        ('03', 'feed-03-conteudo-mensal', 'Conteúdo todo mês, sem montar set', 'Estúdio pronto', '13/11'), ('04', 'feed-04-bastidor', 'Bastidor de produção', 'Bastidor', '16/11'),
        ('06', 'feed-06-kit-luz', 'Luz que muda o take (Kit Luz)', 'Kit em ação', '18/11'), ('07', 'feed-07-kit-completo', 'Kit completo pra diária', 'Kit em ação', '20/11'),
        ('08', 'feed-08-producoes', 'Da ideia ao final (Produções)', 'Projetos', '23/11')]
for n, arq, tit, linha, dia in FEED:
    itens.append({'t': 'Post único', 'titulo': tit, 'data': 'Postar em ' + dia, 'linha': linha, 'st': 'aguardando', 'img': uri(os.path.join(V1, 'artes', arq + '.png'), 720), 'legenda': LEG.get(n, '')})
for arq, tit, linha, leg in [('story-01-agenda-aberta', 'Story · Agenda aberta (enquete)', 'Kit em ação', 'Figurinha de enquete: "Precisa de kit essa semana?" SIM / AINDA NÃO. Quem votar SIM recebe no direct: "Oi! Obrigado pelo voto 😄 Gravação em cima da hora é corrida, né? A gente separa o kit pronto para você só chegar e gravar. Qual dia é a sua diária?"'),
                             ('story-02-estudio', 'Story · Estúdio (caixa de pergunta)', 'Estúdio pronto', 'Figurinha de caixa de pergunta: "O que você quer gravar?". As respostas viram stories com foto do estúdio.')]:
    itens.append({'t': 'Story', 'titulo': tit, 'data': 'Stories da semana', 'linha': linha, 'st': 'aguardando', 'img': uri(os.path.join(V1, 'artes', arq + '.png'), 540), 'legenda': leg})
PF = os.path.join(V1, 'perfil'); BIO = open(os.path.join(PF, 'BIO.md')).read().split('<!-- bio -->')[1].split('<!-- fim -->')[0].strip()
itens.insert(0, {'t': 'Perfil', 'titulo': 'Bio nova e 6 destaques', 'data': 'Trocar antes do 1º post', 'linha': 'Perfil', 'st': 'aguardando', 'img': uri(os.path.join(PF, 'previa-perfil.png'), 720),
                 'legenda': 'Nome: Real Time · Locação de Cinema\n\nBio:\n' + BIO + '\n\nLink: wa.me/5598991331727\n\nDestaques (nesta ordem): Kits · Luz · Estúdio · Produções · Clientes · Reservar. As capas estão em Entregas e arquivos.'})
aprov = ','.join(json.dumps(x, ensure_ascii=False) for x in itens)
s = re.sub(r"const APROV=\[.*?\];", lambda m: f"const APROV=[{aprov}];", s, count=1, flags=re.S)
troca('<div class="post"><div class="img">${p.titulo}</div>', '<div class="post">${p.img?`<img src="${p.img}" alt="${p.titulo}" style="width:100%;aspect-ratio:4/5;object-fit:cover;display:block">`:`<div class="img">${p.titulo}</div>`}')
troca('<div class="d" style="color:var(--apagado);font-size:12.5px">${p.data}</div>',
      '<div class="d" style="color:var(--apagado);font-size:12.5px">${p.data}</div>${p.linha?`<span style="display:inline-block;margin-top:8px;padding:3px 10px;border-radius:999px;font-size:11.5px;font-weight:800;background:var(--amarelo);color:#04102B">${p.linha}</span>`:\'\'}<div style="font-weight:700;margin:6px 0 2px">${p.titulo}</div>'
      '${p.por?`<div style="font-size:12px;color:${p.st===\'aprovado\'?\'#4ADE80\':\'var(--amarelo)\'};margin-top:2px">${p.st===\'aprovado\'?\'✓ Aprovado no site por\':\'Ajuste pedido\'}: ${p.por}${p.em?\', \'+new Date(p.em).toLocaleDateString(\'pt-BR\'):\'\'}</div>`:\'\'}'
      '${p.legenda?`<details style="margin:8px 0"><summary style="cursor:pointer;color:var(--amarelo);font-weight:700">Ver legenda</summary><pre style="white-space:pre-wrap;font:inherit;font-size:13px;line-height:1.5;margin:10px 0;max-height:320px;overflow:auto">${p.legenda.replace(/</g,"&lt;")}</pre><button class="btn lin" onclick="navigator.clipboard.writeText(this.previousElementSibling.textContent);window.__toast&&window.__toast(\'Legenda copiada\')">Copiar legenda</button></details>`:\'\'}')
ordem = [os.path.join(V1, 'artes', f[1] + '.png') for f in reversed(FEED)]
W, H = 360, 450; pv = Image.new('RGB', (W * 3 + 8, H * 3 + 8), '#0E0E0F')
for i, a in enumerate(ordem): pv.paste(Image.open(a).convert('RGB').resize((W, H)), ((i % 3) * (W + 4), (i // 3) * (H + 4)))
pv.save(os.path.join(V1, 'previa-feed.jpg'), quality=88)
if os.path.exists(os.path.join(V1, 'previa-feed.jpg')):
    troca('<p class="sub">Aprove ou peça ajuste. A equipe é avisada na hora.</p>',
          '<p class="sub">Aprove ou peça ajuste. A equipe é avisada na hora.</p>'
          f'<div style="margin:6px 0 18px;max-width:560px"><div style="font-weight:700;margin-bottom:8px">Como o seu feed fica (ordem de postagem, mais novo no topo)</div><img src="{uri(os.path.join(V1, "previa-feed.jpg"), 1000)}" alt="Prévia do feed" style="width:100%;border-radius:12px;display:block"><p class="sub" style="margin-top:8px">A etiqueta azul em cada post mostra a linha editorial: com quem ele fala.</p></div>')
troca("carrosseis:[['5 erros que fazem você perder clientes','aprovado'],['Antes de comprar, veja isso','em revisão'],['Perguntas que mais recebemos','em produção']]",
      "carrosseis:[['Como escolher a lente certa para cada cena','ideia'],['O que vem no Kit Cinema','ideia'],['Como funciona uma reserva','ideia']]")
troca("reels:[['Bastidores da semana','aprovado'],['Um dia com a equipe','em produção'],['Responda em 30 segundos: dúvida do cliente','ideia']]",
      "reels:[['Essa câmera grava filme de cinema. E você pode alugar.','ideia'],['Antes e depois da luz certa','ideia'],['Fundo verde: grava aqui, aparece em qualquer lugar','ideia']]")

# 5 · grupo "Vendas e tráfego" vira "Gestão" (CRM de chamados, Financeiro, Notícias); sem a tela de leads de exemplo
troca('<div class="grupo"><h4>Vendas e tráfego</h4>', '<div class="grupo"><h4>Gestão</h4>'
      '<a href="#crm" data-v="crm"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="9" cy="8" r="3.5"/><path d="M2.5 20c.8-3.6 3.4-5.5 6.5-5.5s5.7 1.9 6.5 5.5M16 4.5a3.5 3.5 0 0 1 0 7M18.5 14.8c1.7.8 2.8 2.5 3.2 5.2"/></svg>CRM de reservas</a>'
      '<a href="#financeiro" data-v="financeiro"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="2.5" y="5.5" width="19" height="13" rx="2.5"/><circle cx="12" cy="12" r="2.6"/><path d="M6 9v.01M18 15v.01"/></svg>Financeiro</a>'
      '<a href="#noticias" data-v="noticias"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 5h13v14H6a2 2 0 0 1-2-2zM17 9h3v8a2 2 0 0 1-2 2"/><path d="M7.5 9h6M7.5 12.5h6M7.5 16h4"/></svg>Notícias do setor</a></div>'
      '<div class="grupo"><h4>Vendas e tráfego</h4>')
s = re.sub(r'<a href="#leads" data-v="leads">.*?</a>', '', s, count=1, flags=re.S)
troca("const V={", "const V=window.__V={"); troca("const T={", "const T=window.__T={")
troca("function toast(t){", "window.__toast=t=>toast(t);function toast(t){")
troca("const f=$('#novo-ped');", "if(window.__pos)window.__pos(view);const f=$('#novo-ped');")
troca("addEventListener('hashchange',render);render();", "window.__render=render;window.__h={BASE,APROV,PEDIDOS,bomDia,chip,cli:()=>cli};addEventListener('hashchange',render);setTimeout(render,0);")

FERR = {
  'negocio': 'Real Time', 'linkGoogle': '', 'retornoDias': 30, 'exEntrada': 'Ex.: Diária Kit Cinema · Produtora X', 'exSaida': 'Ex.: Manutenção das lentes',
  'palavras': {'pac': 'cliente', 'Pac': 'Cliente', 'pacs': 'clientes', 'aval': 'reserva', 'Aval': 'Reserva', 'avals': 'reservas', 'Avals': 'Reservas',
               'proc': 'job', 'Proc': 'Job', 'procs': 'Jobs', 'fezProc': 'Concluíram o job', 'marcaram': 'Reservaram',
               'tinhaAval': 'de quem tinha reserva', 'negocio': 'a Real Time', 'crm': 'CRM de reservas',
               'regra': 'Mensagens curtas e diretas: valor, retirada e devolução só depois de saber a data e o tipo de gravação.'},
  'origens': ['Instagram', 'WhatsApp direto', 'Anúncio (Meta) · RT-CINEMA', 'Anúncio (Meta) · RT-LUZ', 'Anúncio (Meta) · RT-ESTUDIO', 'Anúncio (Meta) · RT-MENSAL', 'Anúncio (Meta) · RT-PROD', 'Google', 'Indicação', 'Cliente antigo', 'Outro'],
  'interesses': ['Kit Cinema (FX3)', 'Kit Ópticas (VESPID, Sony, Zeiss)', 'Kit Luz (Aputure)', 'Kit completo', 'Estúdio fundo verde', 'Conteúdo mensal', 'Produção completa', 'Outro'],
  'etapas': [
    {'id': 'novo', 'nome': 'Novo contato', 'botao': 'Respondeu', 'depois': 'conversa',
     'msg': 'Oi, {nome}! Aqui é da {negocio}. Recebemos a sua mensagem sobre {interesse}. Qual dia é a gravação e o que vocês vão gravar?'},
    {'id': 'conversa', 'nome': 'Orçamento enviado', 'botao': 'Reservou',
     'msg': 'Oi, {nome}! Conseguiu ver as condições do {interesse}? A data ainda está livre. Quer que eu deixe reservado?'},
    {'id': 'marcada', 'nome': 'Reserva confirmada', 'botao': 'Retirou',
     'msg': 'Oi, {nome}! Sua reserva de {interesse} está confirmada {quando}. Qualquer dúvida sobre retirada, é só chamar.'},
    {'id': 'compareceu', 'nome': 'Em uso / gravando', 'botao': 'Job concluído',
     'msg': 'Oi, {nome}! Tudo certo com o {interesse} no set? Se precisar de algum acessório, a gente resolve.'},
    {'id': 'fez', 'nome': 'Job concluído', 'botao': 'Recorrente', 'depois': 'retorno',
     'msg': 'Oi, {nome}! Obrigado por gravar com a {negocio}. Pode mandar uma frase sobre como foi e uma foto do set? Vira depoimento no nosso perfil.'},
    {'id': 'retorno', 'nome': 'Cliente recorrente', 'depois': 'conversa',
     'msg': 'Oi, {nome}! Tem gravação vindo por aí? A agenda desta semana ainda tem datas livres para {interesse}.'},
    {'id': 'perdido', 'nome': 'Não fechou', 'depois': 'conversa',
     'msg': 'Oi, {nome}! Aqui é da {negocio}. Se a gravação de {interesse} mudou de data, me avisa: a gente tenta encaixar.'}],
  'catEntradas': ['Locação Kit Cinema', 'Locação Ópticas', 'Locação Luz', 'Estúdio', 'Conteúdo mensal', 'Produções', 'Outras entradas'],
  'catEntradaCRM': 'Locação Kit Cinema',
  'catSaidas': ['Manutenção de equipamento', 'Equipamento novo', 'Seguro', 'Estúdio (aluguel, energia)', 'Equipe e diárias', 'Transporte', 'Anúncios (Meta e Google)', 'Agência e marketing', 'Impostos e taxas', 'Outras saídas'],
  'formas': ['Pix', 'Cartão de crédito', 'Cartão de débito', 'Dinheiro', 'Boleto', 'A definir'],
  'noticias': [
    {'nome': 'Audiovisual no Maranhão', 'q': 'audiovisual Maranhão OR produção audiovisual São Luís'},
    {'nome': 'Editais e leis de incentivo', 'q': 'edital audiovisual OR Lei Paulo Gustavo OR Aldir Blanc Maranhão'},
    {'nome': 'Equipamentos de cinema', 'q': 'Sony FX3 OR Aputure OR DZOFilm lançamento'},
    {'nome': 'Publicidade e agências', 'q': 'agência de publicidade campanha audiovisual'},
    {'nome': 'Videocast e conteúdo', 'q': 'videocast OR podcast em vídeo estúdio'},
    {'nome': 'Filmmaking e técnicas', 'q': 'filmmaking dicas iluminação cinema'}],
  'notaNoticias': 'Notícias de portais públicos, atualizadas sozinhas a cada 3 horas. Antes de postar sobre uma delas, abra a fonte original.',
  'ideiaPost': 'Gancho: "Saiu uma novidade sobre {tema} e isso muda o seu próximo job. Te explico em 30 segundos."\nNotícia: {titulo}\nFonte: {link}\nFechamento: reserve seu kit no WhatsApp (98) 99133-1727. Seu job é na Real Time.'}

# 6 · bloco de promoção do Lindson: portfólio real, sem o próprio cliente
CASOS = os.path.join(SC, 'fotos', 'casos')
for k, f in [('RAFAEL1', 'rafael.webp'), ('PASSAPORTE1', 'passaporte-1.webp'), ('RAPOSA1', 'raposa-1.webp')]:
    p = os.path.join(CASOS, f); s = s.replace(f'__{k}__', webp(p) if os.path.exists(p) else '')
cine = os.path.join(SC, 'fotos', 'principal-cine.webp')
s = s.replace('<img src="__CINE__" alt="Lindson Almeida">', f'<img src="{webp(cine)}" alt="Lindson Almeida">' if os.path.exists(cine) else '')

s = s.replace('__LOGO__', svg(os.path.join(CL, 'identidade', 'v1', 'marca', 'assinatura-horizontal-mono-branco.svg')))
BAIXAR = """window.__V.entregas = () => `<div class="card"><h3>Entregas e arquivos</h3><p class="sub">Tudo o que a agência já entregou e o que está a caminho. Toque em Baixar para salvar o arquivo.</p><div class="tab"><table><thead><tr><th>Entrega</th><th>Tipo</th><th>Data</th><th>Status</th><th></th></tr></thead><tbody>${(window.__DADOS.entregas || []).map(e => `<tr><td>${e[0]}</td><td>${e[1]}</td><td>${e[2]}</td><td>${window.__h.chip(e[3])}</td><td>${e[4] ? `<a class="btn lin" href="${e[4]}" download>Baixar</a>` : ''}</td></tr>`).join('')}</tbody></table></div></div>`;"""
extra = ('window.__DADOS=' + json.dumps(dados, ensure_ascii=False).replace('</', '<\\/') + ';\n' + open(os.path.join(SC, 'prototipo', 'real.js')).read()
         + '\n' + BAIXAR + '\n' + open(os.path.join(SC, 'prototipo', 'treinamento.js')).read() + '\nwindow.__FERR=' + json.dumps(FERR, ensure_ascii=False) + ';\n'
         + open(os.path.join(SC, 'prototipo', 'ferramentas.js')).read() + '\n' + open(os.path.join(SC, 'prototipo', 'fotos.js')).read()
         + '\n' + open(os.path.join(SC, 'prototipo', 'interacoes.js')).read() + '\n' + open(os.path.join(SC, 'prototipo', 'movimento.js')).read())  # fotos.js depois das ferramentas: ele encadeia o __pos
s = s.replace('</script>', '</script>\n<script>\n' + extra + '\n</script>', 1)
s = s.replace('<meta charset="utf-8">\n', '', 1)
open(os.path.join(D, 'painel-rt.html'), 'w').write(s)
print('painel-rt.html', round(len(s) / 1024), 'KB')
