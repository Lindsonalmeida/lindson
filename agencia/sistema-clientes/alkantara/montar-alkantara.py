"""Painel do cliente Al Kántara Group (holding do Lindson) = o modelo da Central (../prototipo/painel.html), seguindo o montar-wf.py.
Identidade da holding (paleta.json): Obsidiana #0A0C10, Grafite #22262E, Pedra #8A8F98, Bronze #B4935A, Marfim #EEEAE2; Instrument Serif + Inter Tight.
Aprovações = v1 (reprovada 16/11), referências e contratos; lê SOZINHO agencia/marca-holding/v2/ (PDFs, pranchas/imagens, PERSONAS.md, site, deck, kit, vídeos):
rode de novo e as entregas novas da v2 entram. Abas extras: Marca, Divisões, Arquivos.
  python3 montar-alkantara.py   -> painel-alkantara.html aqui + cópia no privado painel/alkantara.html e arquivos em painel/alkantara/
Conta Pedro, 16/11/2026."""
import base64, html, json, os, re, shutil
D = os.path.dirname(os.path.abspath(__file__)); SC = os.path.join(D, '..')
MH = os.path.join(D, '..', '..', 'marca-holding'); V2 = os.path.join(MH, 'v2')
PRIV = os.environ.get('CENTRAL') or next((c for c in [os.path.normpath(os.path.join(D, '..', '..', '..', '..', 'centrallindsonalmeida')), os.path.expanduser('~/centrallindsonalmeida'), '/home/user/centrallindsonalmeida'] if os.path.isdir(os.path.join(c, '.git'))), '')
OUT = os.path.join(PRIV, 'painel', 'alkantara'); WEB = '/painel/alkantara/'
MAXMB = 24  # arquivo maior que isso não vai para o Git (fica registrado)

s = open(os.path.join(SC, 'prototipo', 'painel.html')).read()
def troca(velho, novo, n=1):
    global s
    assert velho in s, 'o modelo mudou, ajuste: ' + velho[:60]
    s = s.replace(velho, novo, n)

# 1 · identidade
troca('<title>Painel do Cliente</title>', '<title>Al Kántara Group · Central</title>')
troca('family=Big+Shoulders+Display:wght@700;800&family=Manrope:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500', 'family=Instrument+Serif:ital@0;1&family=Inter+Tight:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500')
troca("--fundo:#09090A;--painel:#121213;--painel2:#18181A;--linha:#242427;--amarelo:#F5C518;--amarelo2:#FFDD55;",
      "--fundo:#0A0C10;--painel:#14171D;--painel2:#22262E;--linha:#2A2E37;--amarelo:#B4935A;--amarelo2:#D2B583;")
troca("--texto:#F3F0E6;--apagado:#8E8B83;", "--texto:#EEEAE2;--apagado:#8A8F98;")
troca("--f-titulo:'Big Shoulders Display','Arial Narrow',Impact,sans-serif;--f-corpo:'Manrope',system-ui,sans-serif;--f-dado:'IBM Plex Mono',ui-monospace,monospace;",
      "--f-titulo:'Instrument Serif',Georgia,serif;--f-corpo:'Inter Tight',system-ui,sans-serif;--f-dado:'JetBrains Mono',ui-monospace,monospace;")
for a, b in [('rgba(245,197,24', 'rgba(180,147,90'), ('#F5C518', '#B4935A'), ('#242427', '#2A2E37'), ('#8E8B83', '#8A8F98'), ('#121213', '#14171D'),
             ('#F3F0E6', '#EEEAE2'), ('rgba(9,9,10,.92)', 'rgba(10,12,16,.92)'), ("['#F5C518','#C99A10','#6E5A1C']", "['#D2B583','#B4935A','#6E5A3A']")]:
    s = s.replace(a, b)
troca('.topo h1{margin:0;font:800 26px/1', '.topo h1{margin:0;font:400 30px/1')

LOGO = next((p for p in [os.path.join(V2, 'logos', 'png', 'alkantara-horizontal-mono-branco.png'), os.path.join(MH, 'elementos', 'logos', 'png', 'alkantara-horizontal-mono-branco.png')] if os.path.exists(p)), '')
def _logo(p):
    import io; from PIL import Image
    im = Image.open(p); im.thumbnail((680, 200)); b = io.BytesIO(); im.save(b, 'PNG', optimize=True)
    return 'data:image/png;base64,' + base64.b64encode(b.getvalue()).decode()
logo = _logo(LOGO) if LOGO else ''
troca('<div class="logo"><b>LA</b>Central</div>', f'<div class="logo" style="display:grid;gap:10px;justify-items:start"><img src="{logo}" alt="Al Kántara Group" style="width:170px"><span style="font:500 10px var(--f-dado);letter-spacing:.24em;color:#B4935A">CENTRAL DO CLIENTE</span></div>')
s = re.sub(r'<div class="seletor">.*?</select></div>', '', s, count=1, flags=re.S)
troca("let cli='apple';", "let cli='alkantara';")
troca("try{cli=localStorage.getItem('painel-cliente')||'apple'}catch(e){}", '')
troca("$('#cliente').onchange=e=>{cli=e.target.value;try{localStorage.setItem('painel-cliente',cli)}catch(_){}render()};", '')
troca(";$('#cliente').value=cli;", ';')
troca('<div class="avatar" title="Lindson Almeida (admin)">LA</div>', '<div class="avatar" title="Al Kántara Group">AK</div>')
troca("const BASE={", "const BASE={alkantara:{nome:'Al Kántara Group',seg:'Holding de tecnologia',plano:'',inicio:'Novembro/2026',kpis:[],canais:[],metas:[]},")
troca("const FRASES={", "const FRASES={alkantara:['Uma ponte não é feita de pressa: é feita de cálculo.','O bronze é raro de propósito: quanto menos aparece, mais vale.','Quatro divisões, uma estrutura: Labs, Studio, Media e Ventures.'],")
troca("const MISSOES={", "const MISSOES={alkantara:[['Revisar as entregas da v2 na aba Aprovações',40],['Aprovar ou pedir ajuste em cada peça',30],['Conferir a plataforma de marca na aba Marca',30]],")

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

# 3 · v2 (lida sozinha; a mais nova vem primeiro)
v2_md = {}
if os.path.isdir(V2):
    for raiz, dirs, fs in os.walk(V2):
        dirs.sort(); rel = os.path.relpath(raiz, V2)
        if rel.startswith('referencias'): continue
        imgs = sorted(f for f in fs if f.lower().endswith(IMG))
        so_arq = rel.split(os.sep)[0] in ('logos', 'fontes', 'elementos', 'icones')  # peças soltas do kit: só na aba Arquivos
        for f in sorted(fs):
            src = os.path.join(raiz, f); r = os.path.normpath(os.path.join(rel, f)); ext = os.path.splitext(f)[1].lower()
            if ext == '.md': v2_md[r] = open(src).read(); continue
            if ext == '.pdf':
                l = pub(src, 'v2/' + r); arq('v2 · ' + r, 'PDF', '16/11/2026', 'aguardando', l)
                if not so_arq: itens.append({'t': 'PDF', 'titulo': 'v2 · ' + r, 'data': 'Entrega v2', 'linha': 'Marca v2', 'st': 'aguardando', 'arq': l})
            elif ext in VID:
                l = pub(src, 'v2/' + r); arq('v2 · ' + r, 'Vídeo', '16/11/2026', 'aguardando', l)
                if l: itens.append({'t': 'Vídeo', 'titulo': 'v2 · ' + r, 'data': 'Entrega v2', 'linha': 'Marca v2', 'st': 'aguardando', 'video': l})
            elif ext in ('.zip', '.html', '.pptx', '.key'):
                l = pub(src, 'v2/' + r); arq('v2 · ' + r, ext[1:].upper(), '16/11/2026', 'aguardando', l)
                if ext in ('.zip', '.html', '.pptx') and not so_arq: itens.append({'t': ext[1:].upper(), 'titulo': 'v2 · ' + r, 'data': 'Entrega v2', 'linha': 'Marca v2', 'st': 'aguardando', 'arq': l})
        if imgs:  # pasta de pranchas/imagens = 1 cartão com as telas
            tl = [thumb(os.path.join(raiz, f), 'v2/' + os.path.normpath(os.path.join(rel, os.path.splitext(f)[0] + '.jpg'))) for f in imgs]
            itens.append({'t': f'Imagens · {len(tl)}', 'titulo': 'v2 · ' + ('pranchas' if rel == '.' else rel), 'data': 'Entrega v2', 'linha': 'Marca v2', 'st': 'aguardando', 'img': tl[0], 'telas': tl[1:]})
    ref2 = os.path.join(V2, 'referencias')
    if os.path.isdir(ref2):
        tl = [thumb(os.path.join(ref2, f), 'v2/referencias/' + os.path.splitext(f)[0] + '.jpg', 700) for f in sorted(os.listdir(ref2)) if f.lower().endswith(IMG)]
        if tl: itens.append({'t': f'Referências · {len(tl)}', 'titulo': 'Pesquisa premium da v2', 'data': '16/11/2026', 'linha': 'Pesquisa', 'st': 'entregue', 'img': tl[0], 'telas': tl[1:],
                             'legenda': ', '.join(os.path.splitext(f)[0] for f in sorted(os.listdir(ref2)) if f.lower().endswith(IMG))})

# 4 · v1 (reprovada) + referências v1 + contratos
E = os.path.join(MH, 'entregas'); NOTA = 'v1 reprovada 16/11'
for nome, pag in [('alkantara-manual-de-marca', 'alkantara-manual-de-marca'), ('alkantara-branding-book', 'alkantara-branding-book')]:
    l = pub(os.path.join(E, nome + '.pdf'), 'v1/' + nome + '.pdf'); arq('v1 · ' + nome + '.pdf', 'PDF', '16/11/2026', 'reprovado', l)
    pd = os.path.join(E, 'paginas', pag); tl = [thumb(os.path.join(pd, f), f'v1/{pag}/{f.rsplit(".",1)[0]}.jpg', 700) for f in sorted(os.listdir(pd))[:8]] if os.path.isdir(pd) else []
    itens.append({'t': 'PDF', 'titulo': 'v1 · ' + ('Manual de marca' if 'manual' in nome else 'Branding book'), 'data': '16/11/2026', 'linha': 'Marca v1', 'st': 'reprovado', 'nota': NOTA, 'arq': l, 'img': tl[0] if tl else '', 'telas': tl[1:]})
l = pub(os.path.join(E, 'alkantara-elementos.zip'), 'v1/alkantara-elementos.zip'); arq('v1 · alkantara-elementos.zip', 'ZIP', '16/11/2026', 'reprovado', l)
tp = os.path.join(E, 'templates'); tl = [thumb(os.path.join(tp, f), 'v1/templates/' + f.rsplit('.', 1)[0] + '.jpg', 700) for f in sorted(os.listdir(tp))] if os.path.isdir(tp) else []
itens.append({'t': 'ZIP · kit', 'titulo': 'v1 · Kit de elementos (logos, paleta, ícones, templates)', 'data': '16/11/2026', 'linha': 'Marca v1', 'st': 'reprovado', 'nota': NOTA, 'arq': l, 'img': tl[0] if tl else '', 'telas': tl[1:]})
rf = os.path.join(MH, 'referencias'); tl = [thumb(os.path.join(rf, f), 'v1/referencias/' + f.rsplit('.', 1)[0] + '.jpg', 700) for f in sorted(os.listdir(rf)) if f.lower().endswith(IMG)]
itens.append({'t': f'Referências · {len(tl)}', 'titulo': 'Pesquisa premium da v1 (Mubadala, SoftBank, Collins escolhidas)', 'data': '16/11/2026', 'linha': 'Pesquisa', 'st': 'entregue', 'img': tl[0] if tl else '', 'telas': tl[1:]})
ra = os.path.join(MH, 'referencia-antiga'); tl = [thumb(os.path.join(ra, f), 'antiga/' + f.rsplit('.', 1)[0] + '.jpg', 700) for f in sorted(os.listdir(ra)) if f.lower().endswith(IMG)] if os.path.isdir(ra) else []
if tl: itens.append({'t': 'Marca antiga', 'titulo': 'Al Kántara Connections (marca antiga, ponto de partida)', 'data': 'Antes de 16/11', 'linha': 'Pesquisa', 'st': 'entregue', 'img': tl[0], 'telas': tl[1:]})
CONTR = 'https://claude.ai/artifact/B9QirY7ndLJWP9iZ61mozz'
itens.append({'t': 'Contratos', 'titulo': 'Contratos Alkantara (modelo agencia/processos/modelo-contrato/)', 'data': 'Antigos', 'linha': 'Contratos', 'st': 'entregue', 'arq': CONTR, 'ext': 1})
arquivos.append(['Contratos Alkantara (página)', 'Link', 'Antigos', 'entregue', CONTR])
arquivos.append(['Downloads Alkantara (PDFs, demos)', 'Link', 'Antigos', 'entregue', 'https://claude.ai/artifact/3Vn9qpHt3iXgG2JAhcubs7'])

aprov = ','.join(json.dumps(x, ensure_ascii=False) for x in itens)
s = re.sub(r"const APROV=\[.*?\];", lambda m: f"const APROV=[{aprov}];", s, count=1, flags=re.S)
st_ = "st=x=>({"; assert st_ in s; s = s.replace(st_, "st=x=>({reprovado:'ve',", 1)
troca('<div class="post"><div class="img">${p.titulo}</div>', '<div class="post">${p.video?`<video src="${p.video}" controls playsinline preload="none" style="width:100%;aspect-ratio:16/9;display:block;background:#000"></video>`:p.img?`<img src="${p.img}" alt="" loading="lazy" style="width:100%;aspect-ratio:4/3;object-fit:cover;display:block">`:`<div class="img">${p.titulo}</div>`}')
troca('<div class="d" style="color:var(--apagado);font-size:12.5px">${p.data}</div>',
      '<div class="d" style="color:var(--apagado);font-size:12.5px">${p.data}</div>${p.linha?`<span style="display:inline-block;margin-top:8px;padding:3px 10px;border-radius:999px;font-size:11.5px;font-weight:700;background:#B4935A;color:#0A0C10">${p.linha}</span>`:\'\'}<div style="font-weight:600;margin:6px 0 2px">${p.titulo}</div>'
      '${p.nota?`<div style="color:#E07A6A;font-weight:700;font-size:12.5px">✕ ${p.nota}</div>`:\'\'}'
      '${p.telas&&p.telas.length?`<div style="display:flex;gap:6px;overflow-x:auto;margin:8px 0;padding-bottom:4px">${p.telas.map(t=>`<a href="${t}" target="_blank"><img src="${t}" loading="lazy" style="height:100px;border-radius:6px;flex:none"></a>`).join(\'\')}</div>`:\'\'}'
      '${p.arq?`<a class="btn lin" href="${p.arq}" ${p.ext?\'target="_blank" rel="noopener"\':\'download\'} style="display:inline-block;margin:8px 0">${p.ext?\'Abrir\':\'⬇ Baixar\'}</a>`:\'\'}'
      '${p.legenda?`<details style="margin:8px 0"><summary style="cursor:pointer;color:var(--amarelo);font-weight:700">Detalhes</summary><pre style="white-space:pre-wrap;font:inherit;font-size:13px;margin:10px 0">${p.legenda.replace(/</g,"&lt;")}</pre></details>`:\'\'}')

# 5 · menu: tira leads de exemplo, põe Marca, Divisões, Arquivos
s = re.sub(r'<a href="#leads" data-v="leads">.*?</a>', '', s, count=1, flags=re.S)
IC = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="{}"/></svg>'
troca('<a href="#entregas" data-v="entregas">',
      '<a href="#marca" data-v="marca">' + IC.format('M4 20 12 4l8 16M8 13h8') + 'Marca</a>'
      '<a href="#divisoes" data-v="divisoes">' + IC.format('M3 3h8v8H3zM13 3h8v8h-8zM3 13h8v8H3zM13 13h8v8h-8z') + 'Divisões</a>'
      '<a href="#arquivos" data-v="arquivos">' + IC.format('M3 7h6l2 2h10v11H3z') + 'Arquivos</a><a href="#entregas" data-v="entregas">')
troca("const V={", "const V=window.__V={"); troca("const T={", "const T=window.__T={")
troca("function toast(t){", "window.__toast=t=>toast(t);function toast(t){")
troca("addEventListener('hashchange',render);render();", "window.__render=render;window.__h={BASE,APROV,PEDIDOS,bomDia,chip,cli:()=>cli};addEventListener('hashchange',render);setTimeout(render,0);")

# 6 · conteúdo das abas extras (Marca lê o PERSONAS.md da v2 quando existir)
MARCA = {'nome': 'Al Kántara Group', 'descritor': 'Holding de tecnologia · São Luís, Brasil',
         'proposito': 'Encurtar a distância entre quem faz e o que é possível.',
         'missao': 'Criar, operar e escalar empresas de tecnologia que resolvem problemas reais de negócios e pessoas, começando pelo Norte e Nordeste do Brasil.',
         'visao': 'Ser reconhecido como o grupo de tecnologia que provou que se constrói produto de classe mundial a partir de São Luís.',
         'paleta': json.load(open(os.path.join(MH, 'elementos', 'paleta', 'paleta.json')))['cores'],
         'fontes': ['Instrument Serif · títulos', 'Inter Tight · textos', 'JetBrains Mono · rótulos'],
         'docs': {k: v for k, v in v2_md.items() if re.search(r'persona|plataforma|marca|manifesto', k, re.I)}}
DIV = [('Labs', 'IA e software', 'VEKTOR, Dublê e a Central de Comando. Onde o grupo constrói tecnologia própria.'),
       ('Studio', 'Design, sites e vendas', 'Lindson Almeida Studio, sites de clientes e os apps de SDR. A ponte com o mercado.'),
       ('Media', 'Canais e conteúdo', 'Passaporte da Bíblia e Raposa e Leão. Audiência própria em escala.'),
       ('Ventures', 'Negócios próprios', 'Orégano Turbo e Estado Próprio. Onde a tecnologia vira operação real.')]
J = lambda o: json.dumps(o, ensure_ascii=False).replace('</', '<\\/')
EXTRA = f"""window.__AK={{marca:{J(MARCA)},div:{J(DIV)},arq:{J(arquivos)},fora:{J(fora)}}};
(function(){{const A=window.__AK,esc=t=>String(t).replace(/[&<]/g,c=>c=='&'?'&amp;':'&lt;'),ser="font-family:var(--f-titulo);font-weight:400";
window.__V.marca=()=>`<div class="card"><h3>Plataforma de marca</h3><div style="${{ser}};font-size:34px;line-height:1.1;margin:10px 0 4px">${{A.marca.nome}}</div><p class="sub">${{A.marca.descritor}}</p>
<div style="display:grid;gap:14px;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));margin-top:14px">${{[['Propósito',A.marca.proposito],['Missão',A.marca.missao],['Visão',A.marca.visao]].map(x=>`<div style="background:var(--painel2);border-radius:12px;padding:18px"><div style="font:500 11px var(--f-dado);letter-spacing:.14em;color:#B4935A;text-transform:uppercase">${{x[0]}}</div><div style="${{ser}};font-size:22px;line-height:1.25;margin-top:8px">${{x[1]}}</div></div>`).join('')}}</div></div>
<div class="card"><h3>Paleta e tipografia</h3><div style="display:flex;flex-wrap:wrap;gap:10px;margin:10px 0">${{Object.entries(A.marca.paleta).map(([n,c])=>`<div style="width:120px"><div style="height:64px;border-radius:10px;background:${{c}};border:1px solid var(--linha)"></div><div style="font-size:12.5px;margin-top:6px">${{n}}</div><div style="font:500 11px var(--f-dado);color:var(--apagado)">${{c}}</div></div>`).join('')}}</div><p class="sub">${{A.marca.fontes.join(' · ')}}</p></div>
<div class="card"><h3>Personas e plataforma (v2)</h3>${{Object.keys(A.marca.docs).length?Object.entries(A.marca.docs).map(([n,t])=>`<details open style="margin:8px 0"><summary style="cursor:pointer;color:var(--amarelo);font-weight:700">${{esc(n)}}</summary><pre style="white-space:pre-wrap;font:inherit;font-size:13.5px;line-height:1.55;margin:10px 0">${{esc(t)}}</pre></details>`).join(''):'<p class="sub">A v2 está em produção. As personas entram aqui sozinhas quando o PERSONAS.md for entregue.</p>'}}</div>`;
window.__V.divisoes=()=>`<div class="card"><h3>Arquitetura do grupo</h3><p class="sub">4 divisões, uma estrutura.</p><div style="display:grid;gap:14px;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));margin-top:14px">${{A.div.map((d,i)=>`<div style="background:var(--painel2);border-radius:14px;padding:22px;border-top:2px solid #B4935A"><div style="font:500 11px var(--f-dado);color:#B4935A">0${{i+1}}</div><div style="${{ser}};font-size:32px;margin:6px 0">Al Kántara <i>${{d[0]}}</i></div><div style="font-weight:600">${{d[1]}}</div><p class="sub" style="margin-top:8px">${{d[2]}}</p></div>`).join('')}}</div></div>`;
window.__V.arquivos=()=>`<div class="card"><h3>Arquivos</h3><p class="sub">Tudo o que já foi feito para a Al Kántara. Toque para baixar.</p><div class="tab"><table><thead><tr><th>Arquivo</th><th>Tipo</th><th>Data</th><th>Status</th><th></th></tr></thead><tbody>${{A.arq.map(e=>`<tr><td>${{esc(e[0])}}</td><td>${{e[1]}}</td><td>${{e[2]}}</td><td>${{window.__h.chip(e[3])}}</td><td><a class="btn lin" href="${{e[4]}}" ${{e[4].startsWith('http')?'target="_blank" rel="noopener"':'download'}}>${{e[4].startsWith('http')?'Abrir':'Baixar'}}</a></td></tr>`).join('')}}</tbody></table></div>${{A.fora.length?`<p class="sub" style="margin-top:10px">Grandes demais para o site (ficam no repositório lindson): ${{A.fora.map(esc).join(', ')}}</p>`:''}}</div>`;
window.__V.entregas=window.__V.arquivos;
Object.assign(window.__T,{{marca:'Marca',divisoes:'Divisões',arquivos:'Arquivos'}});}})();"""
extra = EXTRA + '\n' + open(os.path.join(SC, 'prototipo', 'interacoes.js')).read() + '\n' + open(os.path.join(SC, 'prototipo', 'movimento.js')).read()
s = s.replace('</script>', '</script>\n<script>\n' + extra + '\n</script>', 1)
open(os.path.join(D, 'painel-alkantara.html'), 'w').write(s)
if os.path.isdir(os.path.join(PRIV, 'painel')):
    open(os.path.join(PRIV, 'painel', 'alkantara.html'), 'w').write(s)
    import sys; sys.path.insert(0, os.path.join(SC, 'site', 'painel-feitas')); import injetar; injetar.injetar(os.path.join(PRIV, 'painel'))
print('painel-alkantara.html', round(len(s) / 1024), 'KB ·', len(itens), 'cartões ·', len(arquivos), 'arquivos', '· fora:', fora)
