"""Biblioteca do cliente: monta o manifesto de TUDO o que já foi produzido para cada cliente e põe a aba "Biblioteca"
no menu lateral de todos os painéis (pedido do Lindson, 20/11/2026: "organize a biblioteca de cada cliente, no painel
de cada cliente, na Central do cliente. Coloque um menu lateral chamado BIBLIOTECA"). Builder Squad, conta Lindson.

  python3 gerar_biblioteca.py                 # todos os clientes (privado em ../../../../../centrallindsonalmeida)
  python3 gerar_biblioteca.py jaci leo        # só esses
  python3 gerar_biblioteca.py --seco          # mostra o que faria, sem copiar nem gravar
  CENTRAL=/caminho/do/privado python3 gerar_biblioteca.py

De onde vêm os itens (nesta ordem, sem repetir arquivo):
  1. Aprovações do painel (const APROV no painel/<cliente>.html): título, situação, versão, telas, vídeo, PDF.
  2. Arquivos já servidos em painel/<pasta>/ do privado (agrupados: c1-1..c1-6 vira 1 carrossel; pasta de logos vira 1 item).
  3. Entregáveis finais que só existiam em dados/clientes-arquivos/<x>/ ou agencia/clientes/<x>/ (PDF, logo, vídeo ≤ 10 MB,
     imagem de pasta de entrega): COPIADOS para painel/<cliente>/biblioteca/arquivos/ (dados/ não é público).
  4. Links do site e da bio do cliente.
Grava painel/<cliente>/biblioteca/manifesto.js (window.__BIB) e as miniaturas em painel/<cliente>/biblioteca/mini/.
O manifesto fica DENTRO da pasta do cliente: o middleware da Central só deixa o próprio cliente (ou o admin) abrir.
Regras: nada acima de 24 MB; nada de .json/.md/.py/.csv/.xlsx; nada com contrato, CPF, RG, TCLE ou comprovante no nome;
a última versão aparece primeiro e as antigas ficam marcadas (escondidas por padrão); reprovado escondido por padrão.
"""
import hashlib, io, json, os, re, shutil, subprocess, sys, zipfile
from datetime import datetime, timezone, timedelta

D = os.path.dirname(os.path.abspath(__file__))
LINDSON = os.path.normpath(os.path.join(D, '..', '..', '..', '..'))
PRIV = os.environ.get('CENTRAL') or next((c for c in [os.path.normpath(os.path.join(LINDSON, '..', 'centrallindsonalmeida')), '/home/user/centrallindsonalmeida', os.path.expanduser('~/centrallindsonalmeida')] if os.path.isdir(os.path.join(c, 'painel'))), '')
PAINEL = os.path.join(PRIV, 'painel'); DADOS = os.path.join(PRIV, 'dados', 'clientes-arquivos'); CLI_L = os.path.join(LINDSON, 'agencia', 'clientes')
MAX = 24 * 1024 * 1024; MAX_VIDEO_COPIA = 10 * 1024 * 1024
SECO = '--seco' in sys.argv

# ---------------------------------------------------------------- clientes (painel → pastas servidas, fontes a copiar, links)
# 'pastas': pastas já servidas em painel/ (a primeira é a do login do cliente; as outras são copiadas para dentro dela).
# 'fontes': (repo, pasta) com entregáveis finais que ainda não estavam no painel. 'links': site, bio e páginas públicas.
# 'reprovado' / 'antiga': trechos de caminho ou título marcados à mão (MEMORIA-DO-LINDSON, reprovados).
CLIENTES = {
  'jaci': {'nome': 'Clínica Dra. Jaci Cunha', 'pastas': ['jaci'],
           'fontes': [('dados', 'jaci'), ('dados', 'jaci-criativos-bf'), ('dados', 'jaci-criativos-v2'), ('dados', 'jaci-criativos-v3'), ('lindson', 'jaci-cunha')],
           'links': [('Site da clínica', 'https://drajacicunha.pages.dev/'), ('Bio do Instagram', 'https://drajacicunha.pages.dev/bio/')],
           'reprovado': [r'site v2', r'site-v2/', r'/prova-social/(?!v2/)', r'jaci-criativos-v2/']},  # MEMORIA: site v2 (04/11), prova social v1 (07/11), criativos v2 (13/11)
  'leo': {'nome': 'Vereador Leo Pinto', 'pastas': ['leo'], 'fontes': [('dados', 'leo'), ('dados', 'leo-pinto'), ('lindson', 'leo-pinto')], 'links': [],
          'reprovado': [r'instagram-v1[23]', r'/identidade/v[123]/', r'redes-v3|v3-redes|identidade v3 · redes', r'identidade-v2/entregas/templates/']},  # MEMORIA 18/11: identidade antiga v1-v3, redes v3, templates de redes da v2
  'wf': {'nome': 'WF Celulares', 'pastas': ['wf'], 'fontes': [('dados', 'wf-celulares'), ('lindson', 'wf-celulares')],
         'links': [('Site e bio', 'https://wfcelulares.pages.dev/')], 'reprovado': [r'artes-01']},  # MEMORIA 10/11: artes-01 (fundo branco)
  'mova-street': {'nome': 'Mova Street + TV Cars', 'pastas': ['mova-street'], 'fontes': [('dados', 'mova-street'), ('lindson', 'mova-street')], 'links': [], 'reprovado': [r'branding-v1/']},  # MEMORIA 18/11: logo v1 redesenhada
  'rt': {'nome': 'Real Time', 'pastas': ['rt'], 'fontes': [('dados', 'rt-full-jobs'), ('lindson', 'rt-full-jobs')],
         'links': [('Site', 'https://realtimeslz.pages.dev/'), ('Bio do Instagram', 'https://realtimeslz.pages.dev/bio/')], 'reprovado': [r'feed-v[34]/|feed v[34]\b']},  # MEMORIA 16/11: feed v3 e v4
  'sf': {'nome': 'Desentupidora SF', 'pastas': ['sf'], 'fontes': [('lindson', 'desentupidora-sf')],
         'links': [('Site e bio', 'https://desentupidorasf.pages.dev/')], 'reprovado': [r'criativos-16-11/', r'videos-2026-11-24/']},  # MEMORIA 16/11: criativos v1
  'oregano': {'nome': 'Orégano Turbo', 'pastas': ['oregano'], 'fontes': [('dados', 'oregano')], 'links': [('Site', 'https://oreganoturbo.pages.dev/')]},
  'alkantara': {'nome': 'Al Kántara Group', 'pastas': ['alkantara'], 'fontes': [], 'links': [('Site', 'https://alkantaragroup.pages.dev/')],
                'reprovado': [r'/painel/alkantara/v1/', r'^v1 ·']},  # v1 reprovada, vale a v2
  'tribuna': {'nome': 'Tribuna 98', 'pastas': ['tribuna'], 'fontes': [('dados', 'tribuna98'), ('lindson', 'tribuna98')], 'links': [('Site e bio', 'https://tribuna98.pages.dev/')]},
  'curso': {'nome': 'Curso de Processo Legislativo', 'pastas': ['curso', 'curso-capas-reels'], 'fontes': [('dados', 'curso'), ('lindson', 'curso-processo-legislativo')], 'links': [], 'antiga': [r'pdfs-originais/']},
}

CATS = ['Marca', 'Artes e posts', 'Carrosséis', 'Stories', 'Vídeos e Reels', 'Capas', 'Documentos', 'Site e bio', 'Referências e pesquisas', 'Fotos']
IMG = {'jpg', 'jpeg', 'png', 'webp', 'gif', 'svg'}; VID = {'mp4', 'mov', 'webm'}
SERVIR = IMG | VID | {'pdf', 'zip', 'html'}
PESSOAL = re.compile(r'contrato|\bcpf\b|(^|[-_/ ])rg([-_. ]|$)|comprovante|tcle|procura[cç]|identidade-pessoal|dados-pessoais|\.dev\.vars|\.env|segredo|senha|codigo', re.I)
NAO_COPIA = re.compile(r'referenc|captura|(^|/)ref/|/tmp|teste|rascunho|__pycache__|node_modules|(^|/)\.|/banco/|/assets?/|/fotos?/|/img/|/cenas/|-fonte/|/fontes/|original|/prova|/frames?/|/quadros?/|/thumbs?/|/mini/|/previas?-ia/|/geradas?/|/upload|/paginas(-v\d+)?/|/[a-z-]*pags/|/exemplo', re.I)
IMG_FINAL = re.compile(r'(^|/)(entregas?|finais|final|logos?|marca|identidade(-v\d+)?|paleta|brand(-book)?|aprovad\w*)(/|$)', re.I)
VER = re.compile(r'(?:^|[^a-z0-9])v(\d+(?:\.\d+)?)(?=$|[^a-z0-9.]|\.[a-z]{2,4}$)', re.I)

def h(s): return hashlib.sha1(s.encode()).hexdigest()[:12]
def md5(p):
    m = hashlib.md5()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''): m.update(b)
    return m.hexdigest()
def ext(p): return p.rsplit('.', 1)[-1].lower() if '.' in os.path.basename(p) else ''
def tipo(p):
    e = ext(p)
    if p.startswith('http'): return 'link'
    return 'img' if e in IMG - {'svg'} else 'svg' if e == 'svg' else 'video' if e in VID else e if e in ('pdf', 'zip', 'html') else 'outro'
def humano(rel):
    b = os.path.splitext(os.path.basename(rel.rstrip('/')))[0]
    b = re.sub(r'[-_]+', ' ', b).strip(); b = re.sub(r'\s+', ' ', b)
    return (b[:1].upper() + b[1:]) if b else rel
def versao(txt):
    vs = [float(x) for x in VER.findall(txt or '')]
    v = max(vs) if vs else 0.0
    if re.search(r'revisad|corrigid', txt or '', re.I): v += 0.001
    return v
def sem_versao(txt):
    t = VER.sub(' ', (txt or '').lower()); t = re.sub(r'\(revisad\w*\)|revisad\w*|vers[aã]o \d+', ' ', t)
    return re.sub(r'[^a-z0-9à-ú]+', ' ', t).strip()

GENERICAS = {'entregas', 'entrega', 'arquivos', 'artes', 'arte', 'video', 'videos', 'img', 'imagens', 'png', 'svg', 'pdf', 'jpg', 'logos', 'logo', 'finais', 'final', 'marca', 'servidos', 'biblioteca', 'aprov', 'feed'}
def contexto(pasta_rel, nomes_cliente):
    """'leo-pinto/identidade-v2/entregas/redes-v3' → 'Identidade v2 · Redes v3' (sem o nome do cliente nem pasta genérica)."""
    ps = [x for x in (pasta_rel or '').split('/') if x and x.lower() not in GENERICAS and x not in nomes_cliente]
    return ' · '.join(humano(x) for x in ps[-2:])

# ---------------------------------------------------------------- datas (commit que adicionou o arquivo), uma chamada de git por pasta
_DATAS = {}
def datas_git(repo, pastas):
    out = {}
    try:
        r = subprocess.run(['git', '-C', repo, 'log', '--diff-filter=A', '--format=%x01%ad', '--date=short', '--name-only', '--'] + pastas, capture_output=True, text=True, timeout=300)
        d = None
        for ln in r.stdout.splitlines():
            if ln.startswith('\x01'): d = ln[1:]
            elif ln.strip() and d: out[os.path.join(repo, ln.strip())] = d  # log vem do mais novo ao mais velho: fica a data em que entrou
    except Exception as e: print('aviso: git log', e)
    return out
def data_de(p):
    if p in _DATAS: return _DATAS[p]
    return datetime.fromtimestamp(os.path.getmtime(p), timezone(timedelta(hours=-3))).strftime('%Y-%m-%d')

# ---------------------------------------------------------------- APROV do painel
def arr(s, i):
    i = s.index('[', i); d = 0; q = None; e = False
    for j in range(i, len(s)):
        c = s[j]
        if q:
            if e: e = False
            elif c == '\\': e = True
            elif c == q: q = None
        elif c in '"\'`': q = c
        elif c == '[': d += 1
        elif c == ']':
            d -= 1
            if d == 0: return s[i:j + 1]
def aprov_do_painel(cli):
    p = os.path.join(PAINEL, cli + '.html')
    if not os.path.exists(p): return []
    s = open(p, encoding='utf-8').read(); m = re.search(r'const APROV\s*=\s*\[', s)
    if not m: return []
    try: return json.loads(arr(s, m.start()))
    except Exception as e: print(f'aviso: APROV de {cli} não é JSON ({e}); só os arquivos do disco'); return []

def st_de(st):
    st = (st or '').lower()
    if st in ('aprovado', 'postado', 'ok'): return 'aprovado'
    if 'reprov' in st or 'recus' in st or 'substitu' in st: return 'reprovado'
    return 'aguardando'

def categoria(texto, k, n_telas=0):
    t = texto.lower()
    if re.search(r'referênc|referenc|pesquisa premium|benchmark|/pesquisa', t): return 'Referências e pesquisas'
    if k == 'link' or k == 'html' or re.search(r'\bsite\b|site-|/bio/|\bbio\b|landing|mini ?site', t):
        if k in ('link', 'html') or re.search(r'\bsite\b|landing|mini ?site', t): return 'Site e bio'
    if re.search(r'logo|monograma|s[ií]mbolo|favicon|paleta|brand ?book|brand-book|manual de (identidade|marca)|manual-de-(identidade|marca)|manual-identidade|identidade visual|(^|[/ ·-])identidade([/ ·-]|$)|/marca/|marca antiga|tipografia', t): return 'Marca'
    if k == 'video' or re.search(r'reels?\b|vídeo|video|motion|tiktok|youtube', t) and k not in ('img', 'svg', 'pdf'):
        return 'Vídeos e Reels'
    if k in ('pdf', 'zip'): return 'Documentos'
    if re.search(r'\bcapas?\b|capa[- ]|thumb|destaque|banner', t): return 'Capas'
    if re.search(r'stor(y|ies)', t): return 'Stories'
    if re.search(r'carrossel|carousel', t) or n_telas >= 2 and re.search(r'feed|post|tela', t) and not re.search(r'stor', t): return 'Carrosséis'
    if re.search(r'estrat[eé]gia|proposta|relat[oó]rio|plano|roteiro|kit ', t): return 'Documentos'
    if re.search(r'(^|/)fotos?(-[a-z0-9.]+)?/|\bfotos?\b|ensaio', t): return 'Fotos'
    return 'Artes e posts'

# ---------------------------------------------------------------- miniaturas
def miniatura(src_abs, saida_dir, web_dir):
    """Miniatura 480 px em webp (cache pelo caminho + tamanho). Imagem, 1ª página do PDF ou quadro do vídeo."""
    if not src_abs or not os.path.exists(src_abs): return ''
    k = tipo(src_abs)
    if k == 'svg': return None  # svg serve como miniatura dele mesmo
    nome = h(src_abs + str(os.path.getsize(src_abs))) + '.webp'; out = os.path.join(saida_dir, nome)
    if os.path.exists(out): return web_dir + nome
    if SECO: return web_dir + nome
    os.makedirs(saida_dir, exist_ok=True)
    try:
        from PIL import Image
        if k == 'img': im = Image.open(src_abs)
        elif k == 'pdf':
            r = subprocess.run(['pdftoppm', '-f', '1', '-l', '1', '-scale-to', '640', '-jpeg', src_abs], capture_output=True, timeout=120)
            if not r.stdout: return ''
            im = Image.open(io.BytesIO(r.stdout))
        elif k == 'video':
            r = subprocess.run(['ffmpeg', '-v', 'error', '-ss', '0.8', '-i', src_abs, '-frames:v', '1', '-vf', 'scale=640:-2', '-f', 'image2pipe', '-vcodec', 'mjpeg', '-'], capture_output=True, timeout=120)
            if not r.stdout:
                r = subprocess.run(['ffmpeg', '-v', 'error', '-i', src_abs, '-frames:v', '1', '-vf', 'scale=640:-2', '-f', 'image2pipe', '-vcodec', 'mjpeg', '-'], capture_output=True, timeout=120)
            if not r.stdout: return ''
            im = Image.open(io.BytesIO(r.stdout))
        else: return ''
        im = im.convert('RGBA') if im.mode in ('RGBA', 'LA', 'P') else im.convert('RGB')
        im.thumbnail((480, 720))
        im.save(out, 'WEBP', quality=78, method=5)
        return web_dir + nome
    except Exception as e:
        print('  aviso: miniatura', os.path.basename(src_abs), e); return ''

def web_para_abs(u):
    if not u or not u.startswith('/painel/'): return None
    p = os.path.join(PRIV, u.lstrip('/').split('?')[0].split('#')[0])
    return p if os.path.isfile(p) else None

# ---------------------------------------------------------------- agrupamento dos arquivos soltos
SERIE = re.compile(r'^(.*?)[-_ ]?(\d{1,3})(?:[-_ ]?(feed|story|stories|capa|4x5|9x16|1x1))?$', re.I)
def agrupar(arqs):
    """arqs: lista de (web, abs). Junta por pasta: 'c1-1..c1-6' → 1 item; pasta de logos → 1 item; o resto fica 1 por arquivo."""
    por_pasta = {}
    for w, a in arqs: por_pasta.setdefault(os.path.dirname(w), []).append((w, a))
    grupos = []
    for pasta, fs in por_pasta.items():
        fs.sort(key=lambda x: [int(t) if t.isdigit() else t for t in re.split(r'(\d+)', x[0])])
        nome_pasta = os.path.basename(pasta).lower()
        if re.search(r'^(logos?|png|svg|pdf|marca)$', nome_pasta) and len(fs) > 2:  # pacote de logos: um item com todas as versões
            grupos.append({'pasta': pasta, 'arqs': fs, 'pacote': True}); continue
        imgs_p = [x for x in fs if tipo(x[1]) in ('img', 'svg')]
        numerados = [x for x in imgs_p if re.match(r'^\d{1,3}([-_ .]|$)', os.path.basename(x[0]))]
        if len(imgs_p) >= 3 and (len(numerados) >= 0.7 * len(imgs_p) or len(imgs_p) > 8):  # peças numeradas ou pasta cheia: 1 item com todas
            grupos.append({'pasta': pasta, 'arqs': imgs_p, 'serie': nome_pasta, 'pasta_toda': True})
            fs = [x for x in fs if x not in imgs_p]
        series = {}
        for w, a in fs:
            k = tipo(a)
            if k not in ('img', 'svg'): grupos.append({'pasta': pasta, 'arqs': [(w, a)]}); continue
            base = os.path.splitext(os.path.basename(w))[0]; m = SERIE.match(base)
            chave = ((m.group(1) or nome_pasta) if m else base).rstrip('-_ ').lower()
            series.setdefault(chave, []).append((w, a))
        for chave, sfs in series.items():
            if len(sfs) >= 2 and chave and not re.fullmatch(r'[a-z]?', chave): grupos.append({'pasta': pasta, 'arqs': sfs, 'serie': chave})
            elif len(sfs) >= 2: grupos.extend({'pasta': pasta, 'arqs': [x]} for x in sfs)
            else: grupos.append({'pasta': pasta, 'arqs': sfs})
    return grupos

# ---------------------------------------------------------------- um cliente
def gerar(cli):
    cfg = CLIENTES[cli]; base_dir = os.path.join(PAINEL, cfg['pastas'][0], 'biblioteca'); WB = f"/painel/{cfg['pastas'][0]}/biblioteca/"
    mini_dir = os.path.join(base_dir, 'mini'); copia_dir = os.path.join(base_dir, 'arquivos')
    fora = []; itens = []; cobertos = set(); rep_cfg = re.compile('|'.join(cfg['reprovado']), re.I) if cfg.get('reprovado') else None; ant_cfg = re.compile('|'.join(cfg['antiga']), re.I) if cfg.get('antiga') else None
    os.makedirs(base_dir, exist_ok=True) if not SECO else None

    # datas pelo git (privado: painel + dados; lindson: agencia/clientes)
    _DATAS.update(datas_git(PRIV, ['painel/' + p for p in cfg['pastas']] + ['dados/clientes-arquivos/' + f for r, f in cfg['fontes'] if r == 'dados']))
    lf = ['agencia/clientes/' + f for r, f in cfg['fontes'] if r == 'lindson']
    if lf: _DATAS.update(datas_git(LINDSON, lf))

    # 0 · pastas extras servidas (ex.: curso-capas-reels) entram copiadas na pasta do login do cliente (o middleware barra outra pasta)
    servidos = []  # (web, abs)
    for i, pasta in enumerate(cfg['pastas']):
        raiz = os.path.join(PAINEL, pasta)
        if not os.path.isdir(raiz): continue
        for r, ds, fs in os.walk(raiz):
            ds[:] = [d for d in ds if not d.startswith('.') and not (i == 0 and r == raiz and d == 'biblioteca')]
            for f in fs:
                a = os.path.join(r, f)
                if ext(a) not in SERVIR or PESSOAL.search(a[len(PAINEL):]): continue
                if os.path.getsize(a) > 26 * 1024 * 1024: fora.append((a[len(PRIV):], 'acima de 25 MB')); continue
                if i == 0: servidos.append(('/' + os.path.relpath(a, PRIV), a))
                else:
                    dst = os.path.join(base_dir, 'servidos', pasta, os.path.relpath(a, raiz))
                    if not SECO:
                        os.makedirs(os.path.dirname(dst), exist_ok=True)
                        if not os.path.exists(dst) or os.path.getsize(dst) != os.path.getsize(a): shutil.copy2(a, dst)
                    _DATAS[dst] = _DATAS.get(a) or data_de(a)
                    servidos.append(('/' + os.path.relpath(dst, PRIV), a if SECO else dst))
    # arquivos da própria biblioteca copiados em rodadas anteriores (arquivos/ e servidos/ de pastas extras) também contam
    hashes = {}
    for w, a in servidos:
        if os.path.getsize(a) < 30 * 1024 * 1024: hashes.setdefault(md5(a), w)
    web_existe = {w for w, a in servidos}

    # 1 · Aprovações
    aprov = aprov_do_painel(cli); dir_st = {}
    for n, p in enumerate(aprov):
        tit = p.get('titulo') or p.get('t') or f'Item {n + 1}'
        img = p.get('img') or ''
        if img.startswith('data:image'):  # miniatura embutida no painel: vira arquivo para poder baixar
            try:
                import base64
                bruto = base64.b64decode(img.split(',', 1)[1]); e = 'png' if 'image/png' in img[:30] else 'jpg'
                nome = 'aprov-' + hashlib.sha1(bruto).hexdigest()[:12] + '.' + e; dst = os.path.join(base_dir, 'aprov', nome)
                if not SECO and not os.path.exists(dst): os.makedirs(os.path.dirname(dst), exist_ok=True); open(dst, 'wb').write(bruto)
                img = WB + 'aprov/' + nome
            except Exception: img = ''
        telas = [t for t in (p.get('telas') or []) if isinstance(t, str) and not t.startswith('data:')]
        video = p.get('video') or ''; arq = p.get('arq') or ''; baixar = p.get('baixar') or ''; capa = p.get('capa') or ''
        if isinstance(arq, str) and arq.endswith('/'): arq = ''
        if isinstance(baixar, str) and baixar.endswith('/'): baixar = ''
        arquivos = [x for x in [arq, video, baixar, capa, img] + telas if isinstance(x, str) and x]
        for x in arquivos: cobertos.add(x.split('?')[0])
        principal = arq or video or baixar or img
        k = tipo(principal) if principal else 'outro'
        if k == 'outro' and not img: continue
        texto = ' '.join(str(p.get(c, '')) for c in ('t', 'titulo', 'linha')) + ' ' + principal
        st = st_de(p.get('st'))
        if rep_cfg and (rep_cfg.search(tit) or any(rep_cfg.search(x) for x in arquivos)): st = 'reprovado'
        for x in arquivos:
            if x.startswith('/painel/'): dir_st.setdefault(os.path.dirname(x), set()).add(st)
        ab = web_para_abs(principal); thumb_src = web_para_abs(capa or img) or ab
        thumb = miniatura(thumb_src, mini_dir, WB + 'mini/') if thumb_src else ''
        if thumb is None: thumb = capa or img
        dt = (_DATAS.get(ab) or (data_de(ab) if ab else '')) if ab else ''
        if not dt and thumb_src: dt = _DATAS.get(thumb_src) or data_de(thumb_src)
        down = principal if principal.startswith('/painel/') and web_para_abs(principal) else (img if web_para_abs(img) else '')
        it = {'id': 'a' + h(cli + tit + str(n)), 'c': categoria(texto, k, len(telas) + 1), 't': tit, 'tp': p.get('t', ''), 'd': dt, 'v': versao(tit + ' ' + principal),
              's': st, 'm': thumb or '', 'u': principal if principal else img, 'b': down, 'k': k, 'z': os.path.getsize(ab) if ab else 0,
              'p': [x for x in ([img] if (video or arq) and img and img != principal else []) + telas], 'ap': p.get('titulo', ''), 'nt': p.get('nota', '') or ''}
        if p.get('ext') or (principal.startswith('http')): it['k'] = 'link'; it['b'] = ''
        itens.append(it)

    # 2 · arquivos servidos sem item nas Aprovações
    soltos = [(w, a) for w, a in servidos if w not in cobertos and not w.startswith(WB + 'mini/')]
    # html: só o index de cada pasta (as páginas internas abrem pelo index)
    soltos = [(w, a) for w, a in soltos if tipo(a) != 'html' or os.path.basename(a) == 'index.html' or not os.path.exists(os.path.join(os.path.dirname(a), 'index.html'))]

    # 3 · entregáveis finais que só existiam em dados/ ou agencia/clientes/: copiar para painel/<cliente>/biblioteca/arquivos/
    copiados = 0
    for repo, pasta in cfg['fontes']:
        raiz = os.path.join(DADOS, pasta) if repo == 'dados' else os.path.join(CLI_L, pasta)
        if not os.path.isdir(raiz): continue
        for r, ds, fs in os.walk(raiz):
            ds[:] = [d for d in ds if not d.startswith('.')]
            for f in fs:
                a = os.path.join(r, f); rel = os.path.relpath(a, raiz).replace(os.sep, '/'); e = ext(a); z = os.path.getsize(a)
                if PESSOAL.search('/' + rel) or NAO_COPIA.search('/' + rel): continue
                ok = e == 'pdf' or e in VID or e in IMG and IMG_FINAL.search('/' + os.path.dirname(rel) + '/') and not re.search(r'/pdf/', '/' + rel)
                if not ok: continue
                hs = md5(a)
                if hs in hashes: continue  # já está no painel (mesmo conteúdo)
                if e in VID and z > MAX_VIDEO_COPIA: fora.append((f'{pasta}/{rel}', 'vídeo acima de 10 MB sem versão comprimida')); continue
                if z > MAX: fora.append((f'{pasta}/{rel}', 'acima de 24 MB')); continue
                dst_rel = (pasta + '/' + rel).replace(' ', '-'); dst = os.path.join(copia_dir, dst_rel)
                if not SECO:
                    os.makedirs(os.path.dirname(dst), exist_ok=True)
                    if not os.path.exists(dst) or os.path.getsize(dst) != z: shutil.copy2(a, dst)
                _DATAS[dst] = _DATAS.get(a) or data_de(a)
                w = WB + 'arquivos/' + dst_rel; hashes[hs] = w; copiados += 1
                if w not in web_existe: soltos.append((w, a if SECO else dst)); web_existe.add(w)

    for g in agrupar(soltos):
        fs = g['arqs']; w0, a0 = fs[0]; k = 'pacote' if g.get('pacote') else tipo(a0)
        pasta_rel = re.sub(r'^/painel/[^/]+/(biblioteca/(arquivos|servidos)/)?', '', g['pasta'])
        ctx = contexto(pasta_rel, [f for r, f in cfg['fontes']] + cfg['pastas'])
        if g.get('pacote'):
            fmt = os.path.basename(pasta_rel).lower(); fmt = fmt.upper() if fmt in ('png', 'svg', 'pdf') else ''
            tit = 'Logos da marca' + (f' · {fmt}' if fmt else '') + (f' · {ctx}' if ctx else '')
        elif g.get('pasta_toda'):
            nome = humano(g['serie']); tit = f"{nome} · {len(fs)} peças" + (f' · {contexto(os.path.dirname(pasta_rel), [f for r, f in cfg["fontes"]] + cfg["pastas"])}' if os.path.dirname(pasta_rel) else '')
        elif g.get('serie'):
            tit = f"{humano(g['serie'])} · {len(fs)} telas" + (f' · {ctx}' if ctx and ctx.lower() != humano(g['serie']).lower() else '')
        else:
            tit = humano(w0) + (f' · {ctx}' if ctx and ctx.lower() not in humano(w0).lower() else '')
        texto = tit + ' ' + w0
        st = 'aguardando'; sts = dir_st.get(g['pasta'])
        if sts and len(sts) == 1: st = next(iter(sts))
        if rep_cfg and (rep_cfg.search(tit) or rep_cfg.search(w0)): st = 'reprovado'
        imgs = [x for x in fs if tipo(x[1]) in ('img', 'svg')]
        thumb_src = (imgs[0][1] if imgs else a0)
        thumb = miniatura(thumb_src, mini_dir, WB + 'mini/')
        if thumb is None: thumb = [w for w, a in fs if a == thumb_src][0]
        down = w0
        if g.get('pacote') or (g.get('serie') and len(fs) >= 2):  # pacote zip para baixar tudo de uma vez
            zn = 'pacote-' + h(g['pasta'] + (g.get('serie') or '')) + '.zip'; zp = os.path.join(base_dir, 'pacotes', zn)
            tot = sum(os.path.getsize(a) for w, a in fs)
            if tot <= (MAX if g.get('pacote') else 8 * 1024 * 1024):  # zip só de pacote de logos e de série pequena (não dobra o peso do repositório)
                if not SECO and (not os.path.exists(zp) or os.path.getmtime(zp) < max(os.path.getmtime(a) for w, a in fs)):
                    os.makedirs(os.path.dirname(zp), exist_ok=True)
                    with zipfile.ZipFile(zp, 'w', zipfile.ZIP_STORED) as zf:
                        for w, a in fs: zf.write(a, os.path.basename(a))
                down = WB + 'pacotes/' + zn
        kk = 'img' if g.get('serie') or g.get('pacote') and imgs else k
        it = {'id': 'f' + h(cli + w0), 'c': categoria(texto if not g.get('pacote') else 'logo ' + texto, kk, len(fs)), 't': tit, 'tp': '', 'd': _DATAS.get(a0) or data_de(a0),
              'v': versao(w0), 's': st, 'm': thumb or '', 'u': w0 if k != 'pacote' else (imgs[0][0] if imgs else w0), 'b': down, 'k': kk if kk != 'pacote' else 'img',
              'z': sum(os.path.getsize(a) for w, a in fs), 'p': [w for w, a in fs[1:]] if len(fs) > 1 else [], 'ap': '', 'nt': ''}
        if g.get('pacote'): it['p'] = [w for w, a in fs if tipo(a) in ('img', 'svg')][1:]
        if ant_cfg and ant_cfg.search(w0): it['a'] = 1
        da = os.path.dirname(a0)  # pasta com subpasta v2/v3…: os arquivos soltos nela são a versão anterior
        if os.path.normpath(da) not in [os.path.join(PAINEL, x) for x in cfg['pastas']] and os.path.isdir(da) and any(re.fullmatch(r'v\d+(\.\d+)?', x) and os.path.isdir(os.path.join(da, x)) for x in os.listdir(da)):
            it['a'] = 1
        itens.append(it)

    # 4 · links
    for tit, url in cfg.get('links', []):
        itens.append({'id': 'l' + h(cli + url), 'c': 'Site e bio', 't': tit, 'tp': 'Link', 'd': '', 'v': 0, 's': 'aguardando', 'm': '', 'u': url, 'b': '', 'k': 'link', 'z': 0, 'p': [], 'ap': '', 'nt': url.replace('https://', '')})

    # versões: dentro da mesma categoria, mesmo título/caminho sem o "vN" → só a maior fica como atual
    grupos = {}
    for it in itens:
        chave = (it['c'], sem_versao(re.sub(r'\(.*?\)', '', it['t'])) or sem_versao(it['u']))
        grupos.setdefault(chave, []).append(it)
    for g in grupos.values():
        if len(g) < 2: continue
        vmax = max(x['v'] for x in g)
        if vmax <= 0: continue
        for x in g:
            if x['v'] < vmax: x['a'] = 1
    for it in itens:
        rv = round(it['v'] * 1000) % 10 == 1; vb = round(it['v'] - (0.001 if rv else 0), 2)
        if vb: it['vl'] = 'v%g' % vb + (' revisada' if rv else '')
        elif rv: it['vl'] = 'revisada'
        it['v'] = round(it['v'], 3)
        if not it['p']: del it['p']
        for c in ('ap', 'nt', 'tp'):
            if not it.get(c): it.pop(c, None)
        if it.get('a') is None: it.pop('a', None)
    ordem = {c: i for i, c in enumerate(CATS)}
    itens.sort(key=lambda x: (ordem.get(x['c'], 99), x.get('a', 0), {'aprovado': 0, 'aguardando': 1, 'reprovado': 2}[x['s']], -(int(x['d'].replace('-', '')) if x['d'] else 0), x['t']))
    agora = datetime.now(timezone(timedelta(hours=-3))).strftime('%d/%m/%Y %H:%M')
    js = ('window.__BIB=window.__BIB||{};window.__BIB[' + json.dumps(cli) + ']=' + json.dumps({'cli': cli, 'nome': cfg['nome'], 'gerado': agora, 'cats': CATS, 'itens': itens}, ensure_ascii=False, separators=(',', ':')) + ';\n').replace('</', '<\\/')
    if not SECO: open(os.path.join(base_dir, 'manifesto.js'), 'w', encoding='utf-8').write(js)
    cont = {}
    for it in itens: cont[it['c']] = cont.get(it['c'], 0) + 1
    return {'cli': cli, 'itens': len(itens), 'copiados': copiados, 'cats': cont, 'fora': fora, 'kb': len(js) // 1024}

if __name__ == '__main__':
    if not os.path.isdir(PAINEL): sys.exit('Privado não encontrado. Clone CentralLindsonALmeida ao lado do repositório lindson ou use CENTRAL=<caminho>.')
    alvo = [a for a in sys.argv[1:] if not a.startswith('--')] or list(CLIENTES)
    for c in alvo:
        r = gerar(c)
        print(f"{r['cli']}: {r['itens']} itens ({r['copiados']} copiados) · manifesto {r['kb']} KB · " + ', '.join(f'{k} {v}' for k, v in r['cats'].items()))
        for f, m in r['fora'][:12]: print('   fora:', f, '·', m)
        if len(r['fora']) > 12: print(f"   … e mais {len(r['fora']) - 12} fora")
    if not SECO:
        sys.path.insert(0, os.path.join(D, '..', 'painel-feitas')); from injetar import injetar
        print('injetados:', injetar(PAINEL))
