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
troca("addEventListener('hashchange',render);render();", "window.__render=render;addEventListener('hashchange',render);setTimeout(render,0);")

# 4 · artes reais do feed nas Aprovações e em Conteúdos > Carrosséis
ARTES = [('v12-1-dividido', 'Post único', 'A gente não promete, volta pra mostrar'), ('v12-2-palavra', 'Post único', 'Presença'),
         ('v12-3-frase', 'Post único', 'Frase: a gente volta pra mostrar'), ('v12-4-conversa', 'Post único', 'Fala com a gente · WhatsApp'),
         ('v12-5-agenda', 'Post único', 'Agenda da semana'), ('v12-6-bom-dia', 'Post único', 'Bom dia, São João Batista')]
img = {n: uri(os.path.join(IG, n + '.png'), 420, 'JPEG') for n, _, _ in ARTES}
aprov = ','.join(f"{{t:'{t}',titulo:'{ti}',data:'Feed · semana 1',st:'{'aguardando' if i < 4 else 'aprovado'}',img:'{img[n]}'}}" for i, (n, t, ti) in enumerate(ARTES))
s = re.sub(r"const APROV=\[.*?\];", f"const APROV=[{aprov}];", s, count=1, flags=re.S)
troca('<div class="post"><div class="img">${p.titulo}</div>', '<div class="post">${p.img?`<img src="${p.img}" alt="${p.titulo}" style="width:100%;aspect-ratio:4/5;object-fit:cover;display:block">`:`<div class="img">${p.titulo}</div>`}')
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
s = s.replace('</script>', '</script>\n<script>\n' + open(os.path.join(D, 'gabinete.js')).read() + '\n</script>', 1)
s = s.replace('<meta charset="utf-8">\n', '', 1)
open(os.path.join(D, 'painel-leo.html'), 'w').write(s)
print('painel-leo.html', round(len(s) / 1024), 'KB')
