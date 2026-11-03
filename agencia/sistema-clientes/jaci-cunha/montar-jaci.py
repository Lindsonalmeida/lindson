"""Painel da Clínica Dra. Jaci Cunha = o modelo da Central (../prototipo/painel.html) com a identidade da clínica
(bordô e dourado, Cormorant Garamond + Montserrat, logo e posts reais) e a área "Agenda cheia" (clinica.js, da estratégia premium).
python3 montar-jaci.py -> painel-jaci.html (arquivo único). Mesmo método do montar-leo.py: trocas pontuais no modelo.
Conta Lindson, 01/11/2026."""
import base64, io, os, re
from PIL import Image
D = os.path.dirname(os.path.abspath(__file__)); SC = os.path.join(D, '..')
CL = os.path.join(D, '..', '..', 'clientes', 'jaci-cunha')
IMG = os.path.join(CL, 'identidade', 'v2', 'img')

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

# 1 · identidade da clínica: bordô e dourado, Cormorant Garamond + Montserrat
troca('<title>Painel do Cliente</title>', '<title>Clínica Dra. Jaci Cunha · Central</title>')
troca('family=Big+Shoulders+Display:wght@700;800&family=Manrope:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500',
      'family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Montserrat:wght@400;500;600;700')
troca("--fundo:#09090A;--painel:#121213;--painel2:#18181A;--linha:#242427;--amarelo:#F5C518;--amarelo2:#FFDD55;",
      "--fundo:#160709;--painel:#22100F;--painel2:#2C1519;--linha:#3D2228;--amarelo:#C6A06A;--amarelo2:#E3C9A0;")
troca("--texto:#F3F0E6;--apagado:#8E8B83;", "--texto:#F5EFE6;--apagado:#BBA49C;")
troca("--f-titulo:'Big Shoulders Display','Arial Narrow',Impact,sans-serif;--f-corpo:'Manrope',system-ui,sans-serif;--f-dado:'IBM Plex Mono',ui-monospace,monospace;",
      "--f-titulo:'Cormorant Garamond',Georgia,serif;--f-corpo:'Montserrat',system-ui,sans-serif;--f-dado:'Montserrat',system-ui,sans-serif;")
for a, b in [('rgba(245,197,24', 'rgba(198,160,106'), ('#F5C518', '#C6A06A'), ('#0C0C0D', '#1C0B0E'), ('rgba(9,9,10,.92)', 'rgba(22,7,9,.92)'),
             ('#070707', '#120507'), ('#C9C5BA', '#E3CFC6'), ('#0A0A0A', '#3A0B12'), ('#2a2412,#0f0f10', '#6B1620,#2C0A10'), ('#242427', '#3D2228'), ('#8E8B83', '#BBA49C'),
             ('#121213', '#22100F'), ('#F3F0E6', '#F5EFE6'), ("['#F5C518','#C99A10','#6E5A1C']", "['#C6A06A','#E3C9A0','#6B1620']")]:
    s = s.replace(a, b)
troca('.menu{position:sticky;top:0;height:100vh;', '.menu{background:linear-gradient(180deg,#6B1620,#2C0A10)!important;position:sticky;top:0;height:100vh;')
troca('.kpi .val{font:800 34px/1.1', '.kpi .val{font:600 36px/1.1')
troca('.topo h1{margin:0;font:800 26px/1', '.topo h1{margin:0;font:600 30px/1')

# 2 · cabeçalho do menu com o logo real; painel do cliente JAC (sem seletor de admin)
troca('<div class="logo"><b>LA</b>Central</div>', '<div class="logo" style="display:grid;gap:8px"><img src="__LOGO__" alt="Clínica Dra. Jaci Cunha" style="width:170px;border-radius:12px"><span style="font:600 10px var(--f-dado);letter-spacing:.24em;color:var(--amarelo)">CENTRAL DO CLIENTE</span></div>')
s = re.sub(r'<div class="seletor">.*?</select></div>', '', s, count=1, flags=re.S)
troca("let cli='apple';", "let cli='jaci';")
troca("try{cli=localStorage.getItem('painel-cliente')||'apple'}catch(e){}", '')
troca("$('#cliente').onchange=e=>{cli=e.target.value;try{localStorage.setItem('painel-cliente',cli)}catch(_){}render()};", '')
troca(";$('#cliente').value=cli;", ';')
troca('<div class="avatar" title="Lindson Almeida (admin)">LA</div>', '<div class="avatar" title="Clínica Dra. Jaci Cunha">JC</div>')

# 3 · dados reais: ficam no repositório PRIVADO (CentralLindsonALmeida/dados/jaci.json), nunca aqui no público.
#     O prototipo/real.js troca as telas de exemplo pelos dados desse arquivo; sem o arquivo, tudo aparece "a medir".
import json
DADOS = os.environ.get('CENTRAL_DADOS', os.path.join(D, '..', '..', '..', '..', 'centrallindsonalmeida', 'dados'))
pj = os.path.join(DADOS, 'jaci.json')
if os.path.exists(pj): dados = json.load(open(pj))
else:
    print('AVISO: sem', pj, '(clone o repositório privado ao lado deste) · o painel sai com tudo "a medir"')
    dados = {'nome': 'Clínica Dra. Jaci Cunha', 'seg': 'Harmonização orofacial e odontologia · Zé Doca/MA', 'plano': 'Plano Master', 'inicio': 'Outubro/2026', 'atualizado': '—'}
troca(re.search(r" jaci:\{nome:'Dra\. Jaci Cunha'.*?\]\]\},", s, re.S).group(0),
      " jaci:{nome:'Clínica Dra. Jaci Cunha',seg:'',plano:'',inicio:'',kpis:[],canais:[],metas:[]},")

# 4 · Aprovações: os 4 carrosséis de novembro (cópia do estilo dela, instagram-nov/) com todas as telas e a legenda.
#     Os posts antigos dela saíram das Aprovações (mesma regra do Leo, 03/11/2026).
import json as _j, glob as _g
NOV = os.path.join(CL, 'instagram-nov'); TN = _j.load(open(os.path.join(NOV, 'textos.json')))
TIT = {'c1': '3 perguntas antes de qualquer procedimento', 'c2': 'Biossegurança: o que você não vê', 'c3': 'Mitos × verdades da harmonização', 'c4': 'Vem me conhecer: como chegar e como é a clínica'}
itens = [{'t': 'Carrossel · 6 telas', 'titulo': f'{TN[k]["data"]} · {TIT[k]}', 'data': f'Postar em {TN[k]["data"]} (terça)', 'linha': TN[k]['linha'], 'st': 'aguardando',
          'img': uri(os.path.join(NOV, f'{k}-1.jpg'), 720), 'telas': [uri(f, 360, 80) for f in sorted(_g.glob(os.path.join(NOV, f'{k}-*.jpg')))[1:]], 'legenda': TN[k]['legenda']} for k in ['c1', 'c2', 'c3', 'c4']]
aprov = ','.join(_j.dumps(x, ensure_ascii=False) for x in itens)
s = re.sub(r"const APROV=\[.*?\];", lambda m: f"const APROV=[{aprov}];", s, count=1, flags=re.S)
troca('<div class="post"><div class="img">${p.titulo}</div>', '<div class="post">${p.img?`<img src="${p.img}" alt="${p.titulo}" style="width:100%;aspect-ratio:4/5;object-fit:cover;display:block">`:`<div class="img">${p.titulo}</div>`}')
troca('<div class="d" style="color:var(--apagado);font-size:12.5px">${p.data}</div>',
      '<div class="d" style="color:var(--apagado);font-size:12.5px">${p.data}</div>${p.linha?`<span style="display:inline-block;margin-top:8px;padding:3px 10px;border-radius:999px;font-size:11.5px;font-weight:800;background:var(--amarelo);color:#1a0f12">${p.linha}</span>`:\'\'}<div style="font-weight:700;margin:6px 0 2px">${p.titulo}</div>'
      '${p.telas?`<div style="display:flex;gap:6px;overflow-x:auto;margin:8px 0;padding-bottom:4px">${p.telas.map(t=>`<img src="${t}" style="height:120px;aspect-ratio:4/5;object-fit:cover;border-radius:6px;flex:none">`).join(\'\')}</div>`:\'\'}'
      '${p.por?`<div style="font-size:12px;color:${p.st===\'aprovado\'?\'#4ADE80\':\'var(--amarelo)\'};margin-top:2px">${p.st===\'aprovado\'?\'✓ Aprovado no site por\':\'Ajuste pedido\'}: ${p.por}${p.em?\', \'+new Date(p.em).toLocaleDateString(\'pt-BR\'):\'\'}</div>`:\'\'}'
      '${p.legenda?`<details style="margin:8px 0"><summary style="cursor:pointer;color:var(--amarelo);font-weight:700">Ver legenda</summary><pre style="white-space:pre-wrap;font:inherit;font-size:13px;line-height:1.5;margin:10px 0;max-height:320px;overflow:auto">${p.legenda.replace(/</g,"&lt;")}</pre><button class="btn lin" onclick="navigator.clipboard.writeText(this.previousElementSibling.textContent);window.__toast&&window.__toast(\'Legenda copiada\')">Copiar legenda</button></details>`:\'\'}')
troca("carrosseis:[['5 erros que fazem você perder clientes','aprovado'],['Antes de comprar, veja isso','em revisão'],['Perguntas que mais recebemos','em produção']]",
      "carrosseis:[['Mitos × verdades: botox deixa o rosto parado?','em produção'],['3 perguntas antes de qualquer procedimento','ideia'],['O que acontece na sua avaliação','ideia']]")
troca("reels:[['Bastidores da semana','aprovado'],['Um dia com a equipe','em produção'],['Responda em 30 segundos: dúvida do cliente','ideia']]",
      "reels:[['Um dia comigo na clínica','em produção'],['Bioestimulador ou preenchimento? 30 segundos','ideia'],['Por que eu digo não para alguns pedidos','ideia']]")

# 5 · grupo "Vendas e tráfego" vira "Agenda cheia" (funil, plano de 90 dias, pautas) + campanhas; sem a tela de leads de exemplo
troca('<div class="grupo"><h4>Vendas e tráfego</h4>', '<div class="grupo"><h4>Agenda cheia</h4>'
      '<a href="#funil" data-v="funil"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M3 4h18l-7 8v6l-4 2v-8z"/></svg>Avaliações</a>'
      '<a href="#plano90" data-v="plano90"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M5 13l4 4L19 7"/></svg>Plano de 90 dias</a>'
      '<a href="#pautas" data-v="pautas"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 5h16M4 12h16M4 19h10"/></svg>Pautas e ganchos</a>')
s = re.sub(r'<a href="#leads" data-v="leads">.*?</a>', '', s, count=1, flags=re.S)
troca("const V={", "const V=window.__V={"); troca("const T={", "const T=window.__T={")
troca("function toast(t){", "window.__toast=t=>toast(t);function toast(t){")
troca("const f=$('#novo-ped');", "if(window.__pos)window.__pos(view);const f=$('#novo-ped');")
troca("addEventListener('hashchange',render);render();", "window.__render=render;window.__h={BASE,APROV,PEDIDOS,bomDia,chip,cli:()=>cli};addEventListener('hashchange',render);setTimeout(render,0);")


# 5b · grupo "Gestão da clínica": CRM de pacientes, Financeiro e Notícias do nicho (prototipo/ferramentas.js)
troca('<div class="grupo"><h4>Agenda cheia</h4>', '<div class="grupo"><h4>Gestão da clínica</h4>'
      '<a href="#crm" data-v="crm"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="9" cy="8" r="3.5"/><path d="M2.5 20c.8-3.6 3.4-5.5 6.5-5.5s5.7 1.9 6.5 5.5M16 4.5a3.5 3.5 0 0 1 0 7M18.5 14.8c1.7.8 2.8 2.5 3.2 5.2"/></svg>CRM de pacientes</a>'
      '<a href="#financeiro" data-v="financeiro"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="2.5" y="5.5" width="19" height="13" rx="2.5"/><circle cx="12" cy="12" r="2.6"/><path d="M6 9v.01M18 15v.01"/></svg>Financeiro</a>'
      '<a href="#noticias" data-v="noticias"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 5h13v14H6a2 2 0 0 1-2-2zM17 9h3v8a2 2 0 0 1-2 2"/><path d="M7.5 9h6M7.5 12.5h6M7.5 16h4"/></svg>Notícias do nicho</a></div>'
      '<div class="grupo"><h4>Agenda cheia</h4>')
FERR = {
  'negocio': 'Clínica Dra. Jaci Cunha', 'linkGoogle': '', 'retornoDias': 150,
  'origens': ['[BTX01] Anúncio botox', '[BIO01] Anúncio flacidez', '[LAB01] Anúncio lábios', '[ODO01] Anúncio odonto', 'Instagram (direct)', 'WhatsApp direto', 'Indicação', 'Google', 'Passou na clínica', 'Outro'],
  'interesses': ['Avaliação geral', 'Toxina botulínica (botox)', 'Preenchimento', 'Bioestimulador de colágeno', 'Lábios', 'Harmonização facial', 'Odontologia (clínico geral)', 'Lentes e estética dental', 'Limpeza e prevenção', 'Outro'],
  'etapas': [
    {'id': 'novo', 'nome': 'Novo contato', 'botao': 'Respondeu', 'depois': 'conversa',
     'msg': 'Oi, {nome}! Tudo bem? Aqui é da {negocio}. Que bom que você chamou sobre {interesse}. Posso te passar os horários para a sua avaliação com a Dra. Jaci?'},
    {'id': 'conversa', 'nome': 'Conversando', 'botao': 'Marcou',
     'msg': 'Oi, {nome}! Tenho horários para a sua avaliação com a Dra. Jaci nesta semana. Qual fica melhor pra você: manhã ou tarde?'},
    {'id': 'marcada', 'nome': 'Avaliação marcada', 'botao': 'Compareceu',
     'msg': 'Oi, {nome}! Passando para confirmar a sua avaliação com a Dra. Jaci {quando}. Posso confirmar o seu horário?'},
    {'id': 'compareceu', 'nome': 'Fez a avaliação', 'botao': 'Fez procedimento',
     'msg': 'Oi, {nome}! Foi muito bom te receber aqui na clínica. Ficou alguma dúvida sobre o que a Dra. Jaci explicou? Quer que eu reserve um horário para o seu procedimento?'},
    {'id': 'fez', 'nome': 'Fez procedimento', 'botao': 'Retorno', 'depois': 'retorno',
     'msg': 'Oi, {nome}! Como você está depois do procedimento? Qualquer dúvida, me chama aqui. A Dra. Jaci quer saber como você está se sentindo.'},
    {'id': 'retorno', 'nome': 'Retorno', 'depois': 'conversa',
     'msg': 'Oi, {nome}! Já faz alguns meses do seu procedimento. Quer que eu reserve um horário para a sua revisão com a Dra. Jaci?'},
    {'id': 'perdido', 'nome': 'Não seguiu', 'depois': 'conversa',
     'msg': 'Oi, {nome}! Aqui é da {negocio}. Você ainda tem interesse em {interesse}? Se quiser, te passo os horários da semana para a sua avaliação.'}],
  'catEntradas': ['Procedimento estético', 'Odontologia', 'Avaliação', 'Retorno ou revisão', 'Outras entradas'],
  'catEntradaCRM': 'Procedimento estético', 'catOdonto': 'Odontologia', 'regexOdonto': 'odonto|dent|limpeza',
  'catSaidas': ['Materiais e insumos', 'Aluguel e condomínio', 'Salários e pró-labore', 'Energia, água e internet', 'Anúncios (Meta e Google)', 'Agência e marketing', 'Impostos e taxas', 'Maquininha e taxas de cartão', 'Equipamentos e manutenção', 'Cursos e congressos', 'Outras saídas'],
  'formas': ['Pix', 'Cartão de crédito', 'Cartão de débito', 'Dinheiro', 'Parcelado', 'Boleto', 'A definir'],
  'noticias': [
    {'nome': 'Harmonização orofacial', 'q': 'harmonização orofacial'},
    {'nome': 'Botox', 'q': 'toxina botulínica estética'},
    {'nome': 'Preenchimento e bioestimulador', 'q': 'bioestimulador de colágeno OR preenchimento ácido hialurônico'},
    {'nome': 'Odontologia estética', 'q': 'odontologia estética OR lentes de contato dental'},
    {'nome': 'Regras do CFO e Anvisa', 'q': 'Conselho Federal de Odontologia OR Anvisa harmonização'},
    {'nome': 'Marketing para clínicas', 'q': 'marketing clínica odontológica Instagram'}],
  'notaNoticias': 'Notícias de portais públicos, atualizadas sozinhas a cada 3 horas. Antes de postar sobre uma delas, abra a fonte original e siga as regras do CFO.',
  'ideiaPost': 'Gancho (rosto da Dra. nos 3 primeiros segundos): "Saiu uma notícia sobre {tema} e muita paciente vai me perguntar. Te explico em 30 segundos."\nNotícia: {titulo}\nFonte: {link}\nLembrete do CFO: sem preço, sem promoção e sem promessa de resultado.'}

# 6 · bloco de promoção do Lindson com o portfólio real (a foto dele fica fora do Git)
CASOS = os.path.join(SC, 'fotos', 'casos')
for k, f in [('RAFAEL1', 'rafael.webp'), ('SF1', 'sf.webp'), ('PASSAPORTE1', 'passaporte-1.webp'), ('RAPOSA1', 'raposa-1.webp')]:
    p = os.path.join(CASOS, f); s = s.replace(f'__{k}__', webp(p) if os.path.exists(p) else '')
cine = os.path.join(SC, 'fotos', 'principal-cine.webp')
s = s.replace('<img src="__CINE__" alt="Lindson Almeida">', f'<img src="{webp(cine)}" alt="Lindson Almeida">' if os.path.exists(cine) else '')

s = s.replace('__LOGO__', uri(os.path.join(IMG, 'assinatura.jpg'), 340))
extra = 'window.__DADOS=' + json.dumps(dados, ensure_ascii=False).replace('</', '<\\/') + ';\n' + open(os.path.join(SC, 'prototipo', 'real.js')).read() + '\n' + open(os.path.join(D, 'clinica.js')).read() + '\nwindow.__FERR=' + json.dumps(FERR, ensure_ascii=False) + ';\n' + open(os.path.join(SC, 'prototipo', 'ferramentas.js')).read() + '\n' + open(os.path.join(SC, 'prototipo', 'fotos.js')).read() + '\n' + open(os.path.join(SC, 'prototipo', 'interacoes.js')).read() + '\n' + open(os.path.join(SC, 'prototipo', 'movimento.js')).read()  # fotos.js por último: ele encadeia o __pos dos anteriores
s = s.replace('</script>', '</script>\n<script>\n' + extra + '\n</script>', 1)
s = s.replace('<meta charset="utf-8">\n', '', 1)
open(os.path.join(D, 'painel-jaci.html'), 'w').write(s)
print('painel-jaci.html', round(len(s) / 1024), 'KB')
