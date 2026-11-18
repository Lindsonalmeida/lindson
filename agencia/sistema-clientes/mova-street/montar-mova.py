"""Painel do cliente Mova Street + TV Cars = o modelo da Central (../prototipo/painel.html), copiado do montar-alkantara.py.
Identidade da holding (paleta.json): Obsidiana #0A0C10, Grafite #22262E, Pedra #8A8F98, Bronze #B4935A, Marfim #EEEAE2; Instrument Serif + Inter Tight.
Aprovações = v1 (reprovada 16/11), referências e contratos; lê SOZINHO agencia/marca-holding/v2/ (PDFs, pranchas/imagens, PERSONAS.md, site, deck, kit, vídeos):
rode de novo e as entregas novas da v2 entram. Abas extras: Marca, Divisões, Arquivos.
  python3 montar-alkantara.py   -> painel-alkantara.html aqui + cópia no privado painel/alkantara.html e arquivos em painel/alkantara/
Conta Leandro, 18/11/2026."""
import base64, html, json, os, re, shutil
D = os.path.dirname(os.path.abspath(__file__)); SC = os.path.join(D, '..')
MH = V2 = ''
PRIV = os.environ.get('CENTRAL') or next((c for c in [os.path.normpath(os.path.join(D, '..', '..', '..', '..', 'centrallindsonalmeida')), os.path.expanduser('~/centrallindsonalmeida'), '/home/user/centrallindsonalmeida'] if os.path.isdir(os.path.join(c, '.git'))), '')
BR = os.path.join(PRIV, 'dados', 'clientes-arquivos', 'mova-street', 'branding-v1')
OUT = os.path.join(PRIV, 'painel', 'mova-street'); WEB = '/painel/mova-street/'
MAXMB = 24  # arquivo maior que isso não vai para o Git (fica registrado)

s = open(os.path.join(SC, 'prototipo', 'painel.html')).read()
def troca(velho, novo, n=1):
    global s
    assert velho in s, 'o modelo mudou, ajuste: ' + velho[:60]
    s = s.replace(velho, novo, n)

# 1 · identidade
troca('<title>Painel do Cliente</title>', '<title>Mova Street · Central</title>')
troca('family=Big+Shoulders+Display:wght@700;800&family=Manrope:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500', 'family=Archivo:ital,wdth,wght@0,100,400;0,100,600;1,125,900&family=JetBrains+Mono:wght@400;500')
troca("--fundo:#09090A;--painel:#121213;--painel2:#18181A;--linha:#242427;--amarelo:#F5C518;--amarelo2:#FFDD55;",
      "--fundo:#0B0D12;--painel:#14171D;--painel2:#1D222C;--linha:#2A2E37;--amarelo:#FF5A1F;--amarelo2:#FF7A45;")
troca("--texto:#F3F0E6;--apagado:#8E8B83;", "--texto:#F4F1EC;--apagado:#8A8F9C;")
troca("--f-titulo:'Big Shoulders Display','Arial Narrow',Impact,sans-serif;--f-corpo:'Manrope',system-ui,sans-serif;--f-dado:'IBM Plex Mono',ui-monospace,monospace;",
      "--f-titulo:'Archivo',Impact,sans-serif;--f-corpo:'Archivo',system-ui,sans-serif;--f-dado:'JetBrains Mono',ui-monospace,monospace;")
for a, b in [('rgba(245,197,24', 'rgba(255,90,31'), ('#F5C518', '#FF5A1F'), ('#242427', '#2A2E37'), ('#8E8B83', '#8A8F98'), ('#121213', '#14171D'),
             ('#F3F0E6', '#EEEAE2'), ('rgba(9,9,10,.92)', 'rgba(10,12,16,.92)'), ("['#F5C518','#C99A10','#6E5A1C']", "['#FF7A45','#FF5A1F','#8A2E10']")]:
    s = s.replace(a, b)
troca('.topo h1{margin:0;font:800 26px/1', '.topo h1{margin:0;font:italic 900 28px/1')

LOGO = os.path.join(BR, 'logos', 'png', 'mova-horizontal-principal.png')
def _logo(p):
    import io; from PIL import Image
    im = Image.open(p); im.thumbnail((680, 200)); b = io.BytesIO(); im.save(b, 'PNG', optimize=True)
    return 'data:image/png;base64,' + base64.b64encode(b.getvalue()).decode()
logo = _logo(LOGO) if LOGO else ''
troca('<div class="logo"><b>LA</b>Central</div>', f'<div class="logo" style="display:grid;gap:10px;justify-items:start"><img src="{logo}" alt="Mova Street" style="width:170px"><span style="font:500 10px var(--f-dado);letter-spacing:.24em;color:#FF5A1F">CENTRAL DO CLIENTE</span></div>')
s = re.sub(r'<div class="seletor">.*?</select></div>', '', s, count=1, flags=re.S)
troca("let cli='apple';", "let cli='mova';")
troca("try{cli=localStorage.getItem('painel-cliente')||'apple'}catch(e){}", '')
troca("$('#cliente').onchange=e=>{cli=e.target.value;try{localStorage.setItem('painel-cliente',cli)}catch(_){}render()};", '')
troca(";$('#cliente').value=cli;", ';')
troca('<div class="avatar" title="Lindson Almeida (admin)">LA</div>', '<div class="avatar" title="Mova Street">MS</div>')
troca("const BASE={", "const BASE={mova:{nome:'Mova Street + TV Cars',seg:'Mídia em carros de aplicativo',plano:'',inicio:'Novembro/2026',kpis:[],canais:[],metas:[]},")
troca("const FRASES={", "const FRASES={mova:['A cidade não para. Sua marca também não.','Rua + banco de trás: duas telas, uma marca.','Sua marca em movimento. Sua publicidade em evidência.'],")
troca("const MISSOES={", "const MISSOES={mova:[['Revisar o branding v1 na aba Aprovações',40],['Aprovar ou pedir ajuste na logo redesenhada',30],['Confirmar período da tabela e escopo da exclusividade',30]],")

# 2 · arquivos: copia para o privado e devolve o link web
os.makedirs(OUT, exist_ok=True)
fora = []
def pub(src, dest):
    mb = os.path.getsize(src) / 1e6
    if mb > MAXMB: fora.append(f'{os.path.relpath(src, MH)} ({mb:.0f} MB)'); return ''
    p = os.path.join(OUT, dest); os.makedirs(os.path.dirname(p), exist_ok=True)
    if not os.path.exists(p) or os.path.getsize(p) != os.path.getsize(src): shutil.copy2(src, p)
    return WEB + dest
def thumb(src, dest, w=900):
    from PIL import Image
    p = os.path.join(OUT, dest); os.makedirs(os.path.dirname(p), exist_ok=True)
    im = Image.open(src).convert('RGB'); im.thumbnail((w, w * 2)); im.save(p, 'JPEG', quality=82, optimize=True)
    return WEB + dest
IMG = ('.jpg', '.jpeg', '.png', '.webp'); VID = ('.mp4', '.webm', '.mov')

itens, arquivos = [], []
def arq(nome, tipo, data, st, link):
    if link: arquivos.append([nome, tipo, data, st, link])


v2_md = {'TEMPLATE.md (pesquisa e persona)': open(os.path.join(BR, 'TEMPLATE.md')).read()}
# 3 · branding v1 (conta Leandro, 18/11/2026) · aguardando aprovação
E = os.path.join(BR, 'entregas'); P = os.path.join(BR, 'paginas'); D18 = '18/11/2026'
lb = pub(os.path.join(E, 'mova-street-book-v1.pdf'), 'v1/mova-street-book-v1.pdf'); arq('Brand book v1 (PDF, 22 p.)', 'PDF', D18, 'aguardando', lb)
lm = pub(os.path.join(E, 'mova-street-manual-v1.pdf'), 'v1/mova-street-manual-v1.pdf'); arq('Manual de marca v1 (PDF, 22 p.)', 'PDF', D18, 'aguardando', lm)
lz = pub(os.path.join(E, 'mova-street-v1-elementos.zip'), 'v1/mova-street-v1-elementos.zip'); arq('Elementos v1 (logos SVG/PNG/PDF, fontes, paleta)', 'ZIP', D18, 'aguardando', lz)
ad = thumb(os.path.join(E, 'previa-logo-antes-depois.jpg'), 'v1/antes-depois.jpg', 1400)
itens.append({'t': 'Logo', 'titulo': 'Logo redesenhada em vetor · antes e depois', 'data': D18, 'linha': 'Branding v1', 'st': 'aguardando', 'img': ad, 'arq': lz})
for nome, l, pre in [('Brand book v1 · estratégia, voz, públicos, oferta', lb, 'book'), ('Manual de marca v1 · logo, cor, letra, grafismos, aplicações', lm, 'manual')]:
    tl = [thumb(os.path.join(P, f), f'v1/{pre}/{f[:-4]}.jpg', 900) for f in sorted(os.listdir(P)) if f.startswith(pre + '-') and f.endswith('.jpg')]
    itens.append({'t': 'PDF', 'titulo': nome, 'data': D18, 'linha': 'Branding v1', 'st': 'aguardando', 'arq': l, 'img': tl[0], 'telas': tl[1:]})
rf = os.path.join(BR, 'referencias'); tl = [thumb(os.path.join(rf, f), 'v1/referencias/' + f[:-4] + '.jpg', 700) for f in sorted(os.listdir(rf)) if f.lower().endswith(IMG)]
itens.append({'t': f'Referências · {len(tl)}', 'titulo': 'Pesquisa premium (Rimac, Vistar, McLaren escolhidas)', 'data': D18, 'linha': 'Pesquisa', 'st': 'entregue', 'img': tl[0], 'telas': tl[1:]})

aprov = ','.join(json.dumps(x, ensure_ascii=False) for x in itens)
s = re.sub(r"const APROV=\[.*?\];", lambda m: f"const APROV=[{aprov}];", s, count=1, flags=re.S)
st_ = "st=x=>({"; assert st_ in s; s = s.replace(st_, "st=x=>({reprovado:'ve',", 1)
troca('<div class="post"><div class="img">${p.titulo}</div>', '<div class="post">${p.video?`<video src="${p.video}" controls playsinline preload="none" style="width:100%;aspect-ratio:16/9;display:block;background:#000"></video>`:p.img?`<img src="${p.img}" alt="" loading="lazy" style="width:100%;aspect-ratio:4/3;object-fit:cover;display:block">`:`<div class="img">${p.titulo}</div>`}')
troca('<div class="d" style="color:var(--apagado);font-size:12.5px">${p.data}</div>',
      '<div class="d" style="color:var(--apagado);font-size:12.5px">${p.data}</div>${p.linha?`<span style="display:inline-block;margin-top:8px;padding:3px 10px;border-radius:999px;font-size:11.5px;font-weight:700;background:#FF5A1F;color:#0B0D12">${p.linha}</span>`:\'\'}<div style="font-weight:600;margin:6px 0 2px">${p.titulo}</div>'
      '${p.nota?`<div style="color:#E07A6A;font-weight:700;font-size:12.5px">✕ ${p.nota}</div>`:\'\'}'
      '${p.telas&&p.telas.length?`<div style="display:flex;gap:6px;overflow-x:auto;margin:8px 0;padding-bottom:4px">${p.telas.map(t=>`<a href="${t}" target="_blank"><img src="${t}" loading="lazy" style="height:100px;border-radius:6px;flex:none"></a>`).join(\'\')}</div>`:\'\'}'
      '${p.arq?`<a class="btn lin" href="${p.arq}" ${p.ext?\'target="_blank" rel="noopener"\':\'download\'} style="display:inline-block;margin:8px 0">${p.ext?\'Abrir\':\'⬇ Baixar\'}</a>`:\'\'}'
      '${p.legenda?`<details style="margin:8px 0"><summary style="cursor:pointer;color:var(--amarelo);font-weight:700">Detalhes</summary><pre style="white-space:pre-wrap;font:inherit;font-size:13px;margin:10px 0">${p.legenda.replace(/</g,"&lt;")}</pre></details>`:\'\'}')

# 5 · menu: tira leads de exemplo, põe Marca, Divisões, Arquivos
s = re.sub(r'<a href="#leads" data-v="leads">.*?</a>', '', s, count=1, flags=re.S)
IC = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="{}"/></svg>'
troca('<a href="#entregas" data-v="entregas">',
      '<a href="#marca" data-v="marca">' + IC.format('M4 20 12 4l8 16M8 13h8') + 'Marca</a>'
      '<a href="#divisoes" data-v="divisoes">' + IC.format('M3 3h8v8H3zM13 3h8v8h-8zM3 13h8v8H3zM13 13h8v8h-8z') + 'Produtos</a>'
      '<a href="#arquivos" data-v="arquivos">' + IC.format('M3 7h6l2 2h10v11H3z') + 'Arquivos</a><a href="#entregas" data-v="entregas">')
troca("const V={", "const V=window.__V={"); troca("const T={", "const T=window.__T={")
troca("function toast(t){", "window.__toast=t=>toast(t);function toast(t){")
troca("addEventListener('hashchange',render);render();", "window.__render=render;window.__h={BASE,APROV,PEDIDOS,bomDia,chip,cli:()=>cli};addEventListener('hashchange',render);setTimeout(render,0);")

# 6 · conteúdo das abas extras (Marca lê o PERSONAS.md da v2 quando existir)
MARCA = {'nome': 'Mova Street + TV Cars', 'descritor': 'Mídia em carros de aplicativo, táxis e entregadores · Grande Ilha de São Luís',
         'proposito': 'Colocar o negócio da cidade no caminho de quem anda por ela.',
         'missao': 'Transformar carros de aplicativo em vitrines em movimento, com acabamento de marca grande e preço fixo por tela.',
         'visao': 'Ser a mídia de quem circula pela Grande Ilha: a marca vista na rua e reencontrada dentro do carro.',
         'paleta': {'Asfalto': '#0B0D12', 'Giz': '#F4F1EC', 'Laranja Mova': '#FF5A1F', 'Âmbar TV Cars': '#FFC21A', 'Azul Noite': '#12203F'},
         'fontes': ['Archivo Expanded Black Italic · títulos', 'Archivo · textos', 'JetBrains Mono · rótulos'],
         'docs': {k: v for k, v in v2_md.items() if True}}
DIV = [('Mova Street', 'Marca-mãe · vidro traseiro', 'Adesivo perfurado no vidro traseiro, 30 a 180 dias ou personalizado, relatório de fotos e km rodados.'), ('TV Cars', 'Produto · tela do encosto', 'Anúncios de 10, 15 ou 20 s, combos de 5 ou 10 telas, QR Code fixo e relatório no sistema.')]
J = lambda o: json.dumps(o, ensure_ascii=False).replace('</', '<\\/')
EXTRA = f"""window.__AK={{marca:{J(MARCA)},div:{J(DIV)},arq:{J(arquivos)},fora:{J(fora)}}};
(function(){{const A=window.__AK,esc=t=>String(t).replace(/[&<]/g,c=>c=='&'?'&amp;':'&lt;'),ser="font-family:var(--f-titulo);font-weight:400";
window.__V.marca=()=>`<div class="card"><h3>Plataforma de marca</h3><div style="${{ser}};font-size:34px;line-height:1.1;margin:10px 0 4px">${{A.marca.nome}}</div><p class="sub">${{A.marca.descritor}}</p>
<div style="display:grid;gap:14px;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));margin-top:14px">${{[['Propósito',A.marca.proposito],['Missão',A.marca.missao],['Visão',A.marca.visao]].map(x=>`<div style="background:var(--painel2);border-radius:12px;padding:18px"><div style="font:500 11px var(--f-dado);letter-spacing:.14em;color:#B4935A;text-transform:uppercase">${{x[0]}}</div><div style="${{ser}};font-size:22px;line-height:1.25;margin-top:8px">${{x[1]}}</div></div>`).join('')}}</div></div>
<div class="card"><h3>Paleta e tipografia</h3><div style="display:flex;flex-wrap:wrap;gap:10px;margin:10px 0">${{Object.entries(A.marca.paleta).map(([n,c])=>`<div style="width:120px"><div style="height:64px;border-radius:10px;background:${{c}};border:1px solid var(--linha)"></div><div style="font-size:12.5px;margin-top:6px">${{n}}</div><div style="font:500 11px var(--f-dado);color:var(--apagado)">${{c}}</div></div>`).join('')}}</div><p class="sub">${{A.marca.fontes.join(' · ')}}</p></div>
<div class="card"><h3>Personas e plataforma (v2)</h3>${{Object.keys(A.marca.docs).length?Object.entries(A.marca.docs).map(([n,t])=>`<details open style="margin:8px 0"><summary style="cursor:pointer;color:var(--amarelo);font-weight:700">${{esc(n)}}</summary><pre style="white-space:pre-wrap;font:inherit;font-size:13.5px;line-height:1.55;margin:10px 0">${{esc(t)}}</pre></details>`).join(''):'<p class="sub">A v2 está em produção. As personas entram aqui sozinhas quando o PERSONAS.md for entregue.</p>'}}</div>`;
window.__V.divisoes=()=>`<div class="card"><h3>Arquitetura de marca</h3><p class="sub">Marca-mãe Mova Street, produto TV Cars.</p><div style="display:grid;gap:14px;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));margin-top:14px">${{A.div.map((d,i)=>`<div style="background:var(--painel2);border-radius:14px;padding:22px;border-top:2px solid #B4935A"><div style="font:500 11px var(--f-dado);color:#B4935A">0${{i+1}}</div><div style="${{ser}};font-size:32px;margin:6px 0">Al Kántara <i>${{d[0]}}</i></div><div style="font-weight:600">${{d[1]}}</div><p class="sub" style="margin-top:8px">${{d[2]}}</p></div>`).join('')}}</div></div>`;
window.__V.arquivos=()=>`<div class="card"><h3>Arquivos</h3><p class="sub">Tudo o que já foi feito para a Mova Street. Toque para baixar.</p><div class="tab"><table><thead><tr><th>Arquivo</th><th>Tipo</th><th>Data</th><th>Status</th><th></th></tr></thead><tbody>${{A.arq.map(e=>`<tr><td>${{esc(e[0])}}</td><td>${{e[1]}}</td><td>${{e[2]}}</td><td>${{window.__h.chip(e[3])}}</td><td><a class="btn lin" href="${{e[4]}}" ${{e[4].startsWith('http')?'target="_blank" rel="noopener"':'download'}}>${{e[4].startsWith('http')?'Abrir':'Baixar'}}</a></td></tr>`).join('')}}</tbody></table></div>${{A.fora.length?`<p class="sub" style="margin-top:10px">Grandes demais para o site (ficam no repositório lindson): ${{A.fora.map(esc).join(', ')}}</p>`:''}}</div>`;
window.__V.entregas=window.__V.arquivos;
Object.assign(window.__T,{{marca:'Marca',divisoes:'Produtos',arquivos:'Arquivos'}});}})();"""
extra = EXTRA + '\n' + open(os.path.join(SC, 'prototipo', 'interacoes.js')).read() + '\n' + open(os.path.join(SC, 'prototipo', 'movimento.js')).read()
s = s.replace('</script>', '</script>\n<script>\n' + extra + '\n</script>', 1)
open(os.path.join(D, 'painel-mova.html'), 'w').write(s)
if os.path.isdir(os.path.join(PRIV, 'painel')):
    open(os.path.join(PRIV, 'painel', 'mova-street.html'), 'w').write(s)
    import sys; sys.path.insert(0, os.path.join(SC, 'site', 'painel-feitas')); import injetar; injetar.injetar(os.path.join(PRIV, 'painel'))
print('painel-mova.html', round(len(s) / 1024), 'KB ·', len(itens), 'cartões ·', len(arquivos), 'arquivos', '· fora:', fora)
