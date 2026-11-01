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

# 3 · dados reais da cliente (o que não tem número real fica marcado)
troca(re.search(r" jaci:\{nome:'Dra\. Jaci Cunha'.*?\]\]\},", s, re.S).group(0),
      " jaci:{nome:'Clínica Dra. Jaci Cunha',seg:'Harmonização orofacial e odontologia · Zé Doca/MA',plano:'Plano Master: redes, conteúdo e tráfego pago',inicio:'Outubro/2026',"
      "kpis:[['Seguidores','1.052','print de out/2026',2],['Visualizações (30 dias)','35,4 mil','print de out/2026',2],['Post da inauguração','50,6 mil','visualizações',2],['Avaliações agendadas','a medir','campanhas de novembro',2]],"
      "canais:[['Instagram',70],['Indicação',20],['Google',10]],metas:[['Avaliações no Google (90 dias)',0,30],['Reels por semana',0,4],['Carrosséis por semana',0,1]]},")
troca('<div class="var ${p.startsWith(\'-\')&&!r.startsWith(\'Custo\')?\'down\':\'up\'}">${p} <span>vs mês anterior</span></div>',
      '<div class="var ${p.startsWith(\'-\')&&!r.startsWith(\'Custo\')?\'down\':\'up\'}">${p} <span>${u===2?\'\':\'vs mês anterior\'}</span></div>')
troca(re.search(r"const ENTREGAS=\[.*?\];", s).group(0),
      "const ENTREGAS=[['Contrato do Plano Master','PDF','26/10','entregue'],['Estratégia de vendas (24 páginas)','PDF','out/2026','entregue'],['Manual de identidade (16 páginas)','PDF','01/11','entregue'],"
      "['Bio, destaques e Perfil do Google','Perfil','nov · sem. 1-2','em produção'],['Mini site com chat de avaliação','Link','nov · sem. 1-2','em produção'],['Campanhas A, B e C no Meta','Anúncios','nov · sem. 3-4','em produção']];")
troca(re.search(r"const PAGT=\[.*?\];", s).group(0), "const PAGT=[['Dezembro/2026','26/12','a vencer'],['Novembro/2026','26/11','a vencer'],['Outubro/2026','26/10','a confirmar']];")

# 4 · posts reais nas Aprovações e pautas da clínica em Conteúdos
POSTS = [('post-botox.jpg', 'Carrossel', 'Botox: o que ninguém responde', 'aguardando'), ('post-preenchimento.jpg', 'Carrossel', 'Preenchimento facial natural', 'aguardando'),
         ('post-bioestimulador.jpg', 'Carrossel', 'Bioestimulador: quando começar?', 'aguardando'), ('post-reta-final.jpg', 'Carrossel', 'Reta final do ano', 'aprovado'),
         ('post-frases.jpg', 'Post único', 'Frases que eu amo ouvir', 'aprovado'), ('post-observo.jpg', 'Post único', 'Antes de qualquer procedimento, eu observo', 'aprovado')]
aprov = ','.join(f"{{t:'{t}',titulo:'{ti}',data:'Feed · referência aprovada',st:'{st}',img:'{uri(os.path.join(IMG, f), 420)}'}}" for f, t, ti, st in POSTS)
s = re.sub(r"const APROV=\[.*?\];", f"const APROV=[{aprov}];", s, count=1, flags=re.S)
troca('<div class="post"><div class="img">${p.titulo}</div>', '<div class="post">${p.img?`<img src="${p.img}" alt="${p.titulo}" style="width:100%;aspect-ratio:4/5;object-fit:cover;display:block">`:`<div class="img">${p.titulo}</div>`}')
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
troca("addEventListener('hashchange',render);render();", "window.__render=render;addEventListener('hashchange',render);setTimeout(render,0);")

# 6 · bloco de promoção do Lindson com o portfólio real (a foto dele fica fora do Git)
CASOS = os.path.join(SC, 'fotos', 'casos')
for k, f in [('RAFAEL1', 'rafael.webp'), ('SF1', 'sf.webp'), ('PASSAPORTE1', 'passaporte-1.webp'), ('RAPOSA1', 'raposa-1.webp')]:
    p = os.path.join(CASOS, f); s = s.replace(f'__{k}__', webp(p) if os.path.exists(p) else '')
cine = os.path.join(SC, 'fotos', 'principal-cine.webp')
s = s.replace('<img src="__CINE__" alt="Lindson Almeida">', f'<img src="{webp(cine)}" alt="Lindson Almeida">' if os.path.exists(cine) else '')

s = s.replace('__LOGO__', uri(os.path.join(IMG, 'assinatura.jpg'), 340))
s = s.replace('</script>', '</script>\n<script>\n' + open(os.path.join(D, 'clinica.js')).read() + '\n</script>', 1)
s = s.replace('<meta charset="utf-8">\n', '', 1)
open(os.path.join(D, 'painel-jaci.html'), 'w').write(s)
print('painel-jaci.html', round(len(s) / 1024), 'KB')
