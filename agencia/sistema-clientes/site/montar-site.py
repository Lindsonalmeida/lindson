"""Monta o site publicável da Central do Cliente em site/publico/ (Cloudflare Pages + Functions). Conta Lindson, 01/11/2026.
  python3 montar-site.py
Um sistema só: cria a conta uma vez (nome, e-mail, senha e código), depois entra com e-mail e senha e cai no próprio painel; o admin vê todos.
Gera: publico/index.html (tela de acesso), publico/painel/{admin,contas,jaci,leo}.html, publico/_headers.
Antes, gere os painéis: python3 ../jaci-cunha/montar-jaci.py, python3 ../leo-pinto/montar-leo.py python3 ../desentupidora-sf/montar-sf.py e python3 ../rt-full-jobs/montar-rt.py.
O acesso é conferido no servidor (functions/). Os códigos ficam só nas variáveis da Cloudflare (ver README)."""
import base64, os, re, shutil
D = os.path.dirname(os.path.abspath(__file__)); SC = os.path.join(D, '..'); OUT = os.path.join(D, 'publico')
shutil.rmtree(OUT, ignore_errors=True); os.makedirs(os.path.join(OUT, 'painel'))
webp = lambda p: 'data:image/webp;base64,' + base64.b64encode(open(p, 'rb').read()).decode()
FOTOS = os.path.join(SC, 'fotos')

def troca(s, velho, novo):
    assert velho in s, 'mudou, ajuste: ' + velho[:70]
    return s.replace(velho, novo, 1)

SAIR = '<a href="/sair" style="font:600 12px var(--f-corpo);color:var(--apagado);text-decoration:none;border:1px solid var(--linha);border-radius:99px;padding:6px 12px">Sair</a>'

CAB = '<!doctype html>\n<html lang="pt-BR">\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
def doc(x):
    """As páginas vêm no formato de artifact (sem doctype nem viewport). No site, sem isso o celular abre como página de computador."""
    x = x.lstrip()
    if x.startswith('<meta charset="utf-8">'): x = x[len('<meta charset="utf-8">'):].lstrip()
    return x if x.lower().startswith('<!doctype') else CAB + x

def com_sair(s):
    return troca(s, '<span class="exemplo">Dados de exemplo</span>', '<span class="exemplo">Dados de exemplo</span>' + SAIR)

# 1 · tela de acesso: o login aprovado (prototipo/login.html), agora com e-mail + código conferido no servidor
s = open(os.path.join(SC, 'prototipo', 'login.html')).read()
for k in ['rafael', 'sf', 'passaporte', 'raposa']:
    p = os.path.join(FOTOS, 'casos', k + '.webp')
    if os.path.exists(p): s = s.replace(f'__{k.upper()}__', webp(p))
    for i in range(1, 5):
        p = os.path.join(FOTOS, 'casos', f'{k}-{i}.webp')
        if os.path.exists(p): s = s.replace(f'__{k.upper()}{i}__', webp(p))
for k, f in [('CINE', 'principal-cine.webp'), ('PROF', 'principal-prof.webp')]:
    p = os.path.join(FOTOS, f)
    s = s.replace(f'__{k}__', webp(p)) if os.path.exists(p) else re.sub(rf'<img id="foto\w+" src="__{k}__"[^>]*>', '', s)
s = troca(s, '<p class="sub">Primeira vez aqui? Crie sua conta com o código de acesso que você recebeu da nossa equipe.</p>',
          '<p class="sub">Primeira vez aqui? Crie sua conta com o código de acesso que você recebeu da nossa equipe. Depois é só entrar com e-mail e senha.</p>')
s = re.sub(r"const PAINEIS=\{.*?\};\n", '', s, count=1, flags=re.S)
s = re.sub(r"async function resumo\(t\)\{.*?\}\n", '', s, count=1)
novo = """f.addEventListener('submit',async e=>{e.preventDefault();av.className='aviso';const email=document.getElementById('usuario').value.trim();
 let rota='/api/entrar',corpo={email,senha:se.value};
 if(modo==='entrar'){if(!email||!se.value){av.textContent='Preencha o e-mail e a senha para entrar.';return}}
 else{const nome=document.getElementById('nome').value.trim();
  if(!nome||!email||!se.value||!cod.value){av.textContent='Preencha nome, e-mail, senha e código de acesso.';return}
  if(se.value.length<8){av.textContent='Use uma senha com pelo menos 8 caracteres.';return}
  rota='/api/criar';corpo={nome,email,senha:se.value,codigo:cod.value}}
 btn.disabled=true;av.textContent=modo==='entrar'?'Conferindo…':'Criando a sua conta…';
 try{const r=await fetch(rota,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(corpo)});const j=await r.json().catch(()=>({}));
  if(r.ok&&j.destino){av.className='aviso ok';av.textContent='Tudo certo. Abrindo o seu painel…';location.href=j.destino;return}
  av.textContent=j.erro||'Não consegui entrar agora. Tente de novo.'}catch(err){av.textContent='Sem conexão com a Central. Tente de novo.'}
 btn.disabled=false});
document.getElementById('esqueci').addEventListener('click',e=>{e.preventDefault();av.textContent='Esqueceu a senha? Fale com a nossa equipe pelo WhatsApp: a gente libera para você criar a conta de novo.'});"""
s = re.sub(r"f\.addEventListener\('submit',async e=>\{.*?\n(?=\}\)\(\);)", novo + '\n', s, count=1, flags=re.S)
s = troca(s, 'const ok=i=>i.complete&&', 'if(!im||!dp)return;const ok=i=>i.complete&&')  # sem a foto do Lindson, o efeito 3D não roda
assert '/api/entrar' in s and '/api/criar' in s and 'PAINEIS' not in s and 'resumo(' not in s
open(os.path.join(OUT, 'index.html'), 'w').write(doc(s))

# 2 · painéis dos clientes (gerados pelos scripts de cada cliente) com o botão Sair
for cli, arq in [('jaci', os.path.join(SC, 'jaci-cunha', 'painel-jaci.html')), ('leo', os.path.join(SC, 'leo-pinto', 'painel-leo.html')), ('sf', os.path.join(SC, 'desentupidora-sf', 'painel-sf.html')), ('rt', os.path.join(SC, 'rt-full-jobs', 'painel-rt.html'))]:
    open(os.path.join(OUT, 'painel', cli + '.html'), 'w').write(doc(com_sair(open(arq).read())))

# 3 · painel do ADMINISTRADOR (Lindson): o mesmo sistema da Central (prototipo/painel.html), preto e amarelo, com menu lateral,
#     e telas próprias (site/admin-sistema.js): visão geral com novidades, clientes, rede social, vendas e CRMs, canais, contas e antigos.
import json
DADOS = os.environ.get('CENTRAL_DADOS', os.path.join(D, '..', '..', '..', '..', 'centrallindsonalmeida', 'dados'))
clientes = [json.load(open(os.path.join(DADOS, c + '.json'))) for c in ['jaci', 'leo', 'sf', 'rt'] if os.path.exists(os.path.join(DADOS, c + '.json'))]
resumo = [{k: c.get(k) for k in ['cliente', 'nome', 'seg', 'atualizado', 'instagram']} for c in clientes]
for r in resumo:
    if r.get('instagram'): r['instagram'] = {k: r['instagram'].get(k) for k in ['perfil', 'data', 'periodo', 'seguidores', 'visualizacoes', 'var_seguidores', 'var_visualizacoes']}
apps = json.load(open(os.path.join(DADOS, 'apps.json'))) if os.path.exists(os.path.join(DADOS, 'apps.json')) else {'abas': [], 'repetidos': []}
# rede social do Lindson (agencia/marca-lindson/, conta Pedro 03/11/2026): estratégia, calendário e artes aprovadas para as abas do admin-rede.js
ML = os.path.join(SC, '..', 'marca-lindson')
REDE = {'est': json.load(open(os.path.join(ML, 'estrategia.json'))) if os.path.exists(os.path.join(ML, 'estrategia.json')) else {},
        'cal': json.load(open(os.path.join(ML, 'calendario.json'))) if os.path.exists(os.path.join(ML, 'calendario.json')) else {'dias': []},
        'artes': json.load(open(os.path.join(ML, 'artes-aprovadas.json'))) if os.path.exists(os.path.join(ML, 'artes-aprovadas.json')) else [],
        # agenda do Instagram (fonte única de status: postado, agendado, aguardando aprovação, bloqueado), conta Zuleide 09/11/2026
        'agenda': json.load(open(os.path.join(ML, 'agenda-status.json'))) if os.path.exists(os.path.join(ML, 'agenda-status.json')) else {'posts': []}}
a = open(os.path.join(SC, 'prototipo', 'painel.html')).read()
a = troca(a, '<title>Painel do Cliente</title>', '<title>Central · Administrador</title>')
IC = {'inicio': '<rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/><rect x="3" y="14" width="7" height="7" rx="1.5"/><rect x="14" y="14" width="7" height="7" rx="1.5"/>',
      'missoes': '<path d="m12 3 2.6 5.5 6 .8-4.4 4.1 1.1 6L12 16.6 6.7 19.4l1.1-6L3.4 9.3l6-.8z"/>',
      'clientes': '<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20c.8-3.6 3.4-5.5 6.5-5.5s5.7 1.9 6.5 5.5M16 4.5a3.5 3.5 0 0 1 0 7M18.5 14.8c1.7.8 2.8 2.5 3.2 5.2"/>',
      'ir': '<path d="M7 17 17 7M9 7h8v8"/>', 'rede': '<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><path d="M17.5 6.5v.01"/>',
      'vendas': '<path d="M3 4h18l-7 8v6l-4 2v-8z"/>', 'canais': '<rect x="2.5" y="5" width="19" height="14" rx="3"/><path d="m10 9 5 3-5 3z"/>',
      'contas': '<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>', 'repetidos': '<path d="M4 7h16M7 7l1 13h8l1-13M10 7V4h4v3"/>', 'sair': '<path d="M15 4h4v16h-4M10 8l-4 4 4 4M6 12h10"/>'}
lk = lambda h, ic, t, v=None, extra='': f'<a href="{h}"' + (f' data-v="{v}"' if v else '') + f'><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">{IC[ic]}</svg>{t}{extra}</a>'
menu = ('<div class="grupo"><h4>Visão</h4><a href="/painel/comando" style="color:var(--amarelo);background:rgba(245,197,24,.10)"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5 11a7 7 0 0 0 14 0M12 18v3"/></svg>Central de Comando</a>' + lk('#inicio', 'inicio', 'Visão geral', 'inicio', '<span class="n" id="n-novid"></span>') + lk('#missoes', 'missoes', 'Missões do dia', 'missoes', '<span class="n" id="n-miss"></span>') + '</div>'
        '<div class="grupo"><h4>Minha rede social</h4>' + lk('#rede', 'rede', 'Visão da rede', 'rede') + lk('#rede-estrategia', 'missoes', 'Estratégia', 'rede-estrategia') + lk('#rede-calendario', 'inicio', 'Calendário editorial', 'rede-calendario') + lk('#rede-lote', 'canais', 'Gravação da semana', 'rede-lote') + lk('#rede-leads', 'clientes', 'Leads das iscas', 'rede-leads') + lk('#rede-relatorio', 'vendas', 'Relatório semanal', 'rede-relatorio') + lk('#rede-fotos', 'rede', 'Minhas fotos', 'rede-fotos') + lk('#rede-artes', 'rede', 'Artes', 'rede-artes') + '</div>'
        '<div class="grupo"><h4>Clientes</h4>' + lk('#clientes', 'clientes', 'Todos os clientes', 'clientes') + ''.join(lk('/painel/' + c['cliente'], 'ir', c['nome']) for c in clientes) + '</div>'
        '<div class="grupo"><h4>Minha agência</h4>' + lk('#recomeco', 'missoes', 'Recomeço 90', 'recomeco') + lk('#fabrica', 'rede', 'Fábrica de Conteúdo', 'fabrica') + lk('#legendas', 'rede', 'Legendas Top X', 'legendas') + lk('#marca', 'inicio', 'Marca e Design System', 'marca') + lk('#propostas', 'vendas', 'Gerador de propostas', 'propostas') + lk('#vendas', 'vendas', 'Vendas e CRMs', 'vendas') + lk('#canais', 'canais', 'Canais dark', 'canais') + '</div>'
        '<div class="grupo"><h4>Sistema</h4>' + lk('#contas', 'contas', 'Contas de acesso', 'contas') + lk('#repetidos', 'repetidos', 'Antigos e repetidos', 'repetidos') + lk('/sair', 'sair', 'Sair') + '</div>'
        '<span id="n-aprov" hidden></span></nav>')
a = re.sub(r'<div class="seletor">.*?</nav>', lambda m: menu, a, count=1, flags=re.S)
a = troca(a, "let cli='apple';", "let cli='admin';")
a = troca(a, "try{cli=localStorage.getItem('painel-cliente')||'apple'}catch(e){}", '')
a = troca(a, "$('#cliente').onchange=e=>{cli=e.target.value;try{localStorage.setItem('painel-cliente',cli)}catch(_){}render()};", '')
a = troca(a, ";$('#cliente').value=cli;", ';')
a = troca(a, "const BASE={", "const BASE={admin:{nome:'Lindson',seg:'Administrador da Central',plano:'',inicio:'',kpis:[],canais:[],metas:[]},")
a = troca(a, "const FRASES={", "const FRASES={admin:['Cliente bem atendido renova e indica. Responda os pedidos de hoje.','Constância vence talento: grave um roteiro do Teste 01 hoje.','Prova vende: transforme uma entrega de cliente em post.','Quem mede, melhora. Atualize os números dos clientes esta semana.'],")
a = troca(a, "const MISSOES={", "const MISSOES={admin:[['Responder os pedidos e ajustes dos clientes',30],['Gravar 1 roteiro do Teste 01 de Reels',25],['Postar no seu Instagram',20],['Mandar 10 mensagens da lista de leads',25],['Atualizar os números de um cliente',15]],")
a = troca(a, '<span class="exemplo">Dados de exemplo</span>', '<span class="exemplo">Administrador</span>')
a = troca(a, '<div class="avatar" title="Lindson Almeida (admin)">LA</div>', '<a class="avatar" href="/sair" title="Sair" style="text-decoration:none">LA</a>')
a = troca(a, "main.innerHTML=V[view](d)+promo();", "main.innerHTML=V[view](d);")
a = troca(a, "const V={", "const V=window.__V={"); a = troca(a, "const T={", "const T=window.__T={")
a = troca(a, "function toast(t){", "window.__toast=t=>toast(t);function toast(t){")
a = troca(a, "const f=$('#novo-ped');", "if(window.__pos)window.__pos(view);const f=$('#novo-ped');")
a = troca(a, "addEventListener('hashchange',render);render();", "window.__render=render;window.__h={BASE,APROV,PEDIDOS,bomDia,chip,cli:()=>cli};addEventListener('hashchange',render);setTimeout(render,0);")
extra = ('window.__CLIENTES=' + json.dumps(resumo, ensure_ascii=False) + ';\nwindow.__APPS=' + json.dumps(apps, ensure_ascii=False) + ';\n').replace('</', '<\\/') + open(os.path.join(D, 'admin-sistema.js')).read() + '\n' + open(os.path.join(D, 'admin-apps.js')).read() + '\n' + 'window.__REDE=' + json.dumps(REDE, ensure_ascii=False).replace('</', '<\\/') + ';\n' + open(os.path.join(D, 'admin-rede.js')).read() + '\n' + open(os.path.join(SC, 'prototipo', 'movimento.js')).read()
a = a.replace('</script>', '</script>\n<script>\n' + extra + '\n</script>', 1)
open(os.path.join(OUT, 'painel', 'admin.html'), 'w').write(doc(a))
# 3b · apps do Lindson dentro da Central (só o admin abre: ficam em /painel/, e o middleware barra quem não é admin)
#      O app original roda igual, com o "window.claude" trocado pelo banco do servidor (prototipo/claude-shim.js).
#      Na primeira vez, traz os dados do app antigo do claude.ai (dados/importar/<app>/, repositório privado).
VOLTA = '<a href="/painel/admin" style="position:fixed;left:12px;bottom:12px;z-index:2147483000;background:#F5C518;color:#0A0A0A;font:700 13px system-ui;padding:9px 14px;border-radius:99px;text-decoration:none;box-shadow:0 8px 24px -8px #000">← Central</a>'
SHIM = open(os.path.join(SC, 'prototipo', 'claude-shim.js')).read()
def app_na_central(fonte, saida, importar=None, temas=('tema-central.css',)):
    h = open(fonte).read()
    cab = (f"<script>window.__IMPORTAR={json.dumps(importar)}</script>" if importar else '') + '<script>\n' + SHIM + '\n</script>'
    h = re.sub(r'(<head[^>]*>)', lambda m: m.group(1) + cab, h, count=1, flags=re.I) if re.search(r'<head[^>]*>', h, re.I) else cab + h
    tema = ''.join('<style>' + open(os.path.join(SC, 'prototipo', t)).read() + '</style>' for t in temas)
    volta = VOLTA.replace('<a href', '<a id="volta-central" href') + '<script>if(window.top!==window){var v=document.getElementById("volta-central");if(v)v.remove()}</script>'
    h = re.sub(r'(</body>)', lambda m: tema + volta + m.group(1), h, count=1, flags=re.I) if re.search(r'</body>', h, re.I) else h + tema + volta
    open(os.path.join(OUT, 'painel', saida), 'w').write(doc(h))
def importar_js(pasta, base, saida):
    docs = []
    for raiz, _, arqs in os.walk(pasta):
        for a in arqs:
            if not a.endswith('.json'): continue
            rel = os.path.relpath(os.path.join(raiz, a), pasta)[:-5].split(os.sep)
            docs.append({'col': '/'.join(([base] if base else []) + rel[:-1]), 'id': rel[-1], 'data': json.load(open(os.path.join(raiz, a)))})
    open(os.path.join(OUT, 'painel', saida), 'w').write('window.__DADOS_IMPORTAR=' + json.dumps(docs, ensure_ascii=False) + ';')
    return len(docs)
APPS_DIR = os.path.join(SC, '..', 'app')
app_na_central(os.path.join(APPS_DIR, 'recomeco90.html'), 'recomeco.html', {'script': '/painel/r90-importar.js', 'marca': 'data/users/lindson/progresso'})
if os.path.isdir(os.path.join(DADOS, 'importar', 'r90')): print('recomeco: importar', importar_js(os.path.join(DADOS, 'importar', 'r90'), 'data/users/lindson', 'r90-importar.js'), 'documentos')
app_na_central(os.path.join(APPS_DIR, 'fabrica.html'), 'fabrica.html', {'script': '/painel/fabrica-importar.js', 'marca': 'app/config'}, ('tema-central.css', 'tema-fabrica.css'))
if os.path.isdir(os.path.join(DADOS, 'importar', 'fabrica')): print('fabrica: importar', importar_js(os.path.join(DADOS, 'importar', 'fabrica'), '', 'fabrica-importar.js'), 'documentos')
if os.path.isdir(os.path.join(DADOS, 'importar', 'fabrica-blobs')): shutil.copytree(os.path.join(DADOS, 'importar', 'fabrica-blobs'), os.path.join(OUT, 'painel', 'fabrica-fotos'), dirs_exist_ok=True)  # imagens antigas (/_blob/<id>)
shutil.copy(os.path.join(D, 'contas.html'), os.path.join(OUT, 'painel', 'contas.html'))
shutil.copy(os.path.join(D, 'membros.html'), os.path.join(OUT, 'painel', 'membros.html'))  # membros dos produtos (Hubla), só o admin (Builder Squad, 04/11/2026)
# página da assessoria para pizzarias (operação própria + estudo da franquia Alpha), só o admin (conta Leandro, 05/11/2026)
import importlib.util as _iu
_sp = _iu.spec_from_file_location('pizz', os.path.join(SC, '..', 'operacao-propria', 'painel.py')); _m = _iu.module_from_spec(_sp); _sp.loader.exec_module(_m)
print('pizzarias.html', _m.montar(os.path.join(OUT, 'painel')), 'documentos')
open(os.path.join(OUT, '_headers'), 'w').write("/*\n  X-Frame-Options: SAMEORIGIN\n  Referrer-Policy: same-origin\n  X-Content-Type-Options: nosniff\n/painel/*\n  Cache-Control: private, no-store\n  X-Robots-Tag: noindex\n")
open(os.path.join(OUT, 'robots.txt'), 'w').write("User-agent: *\nAllow: /site/\nAllow: /bio/\nAllow: /sitemap.xml\nDisallow: /\n\nSitemap: https://lindsonalmeida.pages.dev/sitemap.xml\n")
# sitemap só das páginas públicas (site oficial, portfólio e bio) — conta Leandro, 05/11/2026
open(os.path.join(OUT, 'sitemap.xml'), 'w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'  <url><loc>https://lindsonalmeida.pages.dev{u}</loc><changefreq>weekly</changefreq><priority>{p}</priority></url>\n' for u, p in [('/site/', '1.0'), ('/site/portfolio/', '0.8'), ('/bio/', '0.6')]) + '</urlset>\n')
for r, _, fs in os.walk(OUT):
    for f in fs: print(os.path.relpath(os.path.join(r, f), OUT), os.path.getsize(os.path.join(r, f)) // 1024, 'KB')
