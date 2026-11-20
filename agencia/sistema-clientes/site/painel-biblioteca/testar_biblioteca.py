"""Conferência da Biblioteca em todos os painéis (Playwright, file://): sem erro de JS, aba abre, miniaturas carregam,
links de baixar existem no disco, 390 e 1440 px sem rolagem lateral, e as outras abas continuam abrindo.
  python3 testar_biblioteca.py [cliente ...] [--prints <pasta>]     (Builder Squad, 20/11/2026)"""
import json, os, re, sys
from playwright.sync_api import sync_playwright
D = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, D)
from gerar_biblioteca import PRIV, CLIENTES
PAINEL = os.path.join(PRIV, 'painel')
PRINTS = sys.argv[sys.argv.index('--prints') + 1] if '--prints' in sys.argv else ''
alvo = [a for a in sys.argv[1:] if not a.startswith('--') and a != PRINTS] or list(CLIENTES)

def manifesto(cli):
    s = open(os.path.join(PAINEL, cli, 'biblioteca', 'manifesto.js'), encoding='utf-8').read()
    return json.loads(s[s.index('=', s.index('window.__BIB[')) + 1:].rstrip().rstrip(';'))
def existe(u): return u.startswith('http') or os.path.isfile(os.path.join(PRIV, u.lstrip('/')))

def rota(route):
    u = route.request.url
    if u.startswith('file:///painel/'):
        p = os.path.join(PAINEL, u[len('file:///painel/'):].split('?')[0].split('#')[0])
        return route.fulfill(path=p) if os.path.isfile(p) else route.fulfill(status=404, body='')
    if u.startswith('file:///api/'): return route.fulfill(status=200, content_type='application/json', body='{}')
    if u.startswith('file://'): return route.continue_()
    if 'fonts.googleapis.com' in u or 'fonts.gstatic.com' in u: return route.continue_()
    return route.abort()

falhas = []; resumo = []
with sync_playwright() as pw:
    b = pw.chromium.launch()
    for cli in alvo:
        M = manifesto(cli); its = M['itens']
        sem = [(it['t'], k, it[k]) for it in its for k in ('m', 'u', 'b') if it.get(k) and not existe(it[k])] + [(it['t'], 'p', x) for it in its for x in it.get('p', []) if not existe(x)]
        if sem: falhas.append(f'{cli}: {len(sem)} arquivo(s) do manifesto não existem, ex.: {sem[:3]}')
        grandes = [it['b'] for it in its if it.get('b') and not it['b'].startswith('http') and os.path.getsize(os.path.join(PRIV, it['b'].lstrip('/'))) > 26214400]
        if grandes: falhas.append(f'{cli}: download acima de 25 MB: {grandes}')
        for w in (1440, 390):
            ctx = b.new_context(viewport={'width': w, 'height': 900}, device_scale_factor=1)
            pg = ctx.new_page(); erros = []
            pg.on('pageerror', lambda e: erros.append(str(e)[:200]))
            ctx.route('**/*', rota)
            pg.goto(f'file:///painel/{cli}.html#biblioteca', wait_until='load')
            pg.wait_for_selector('.bib-c, .bib-res .vazio, #bib-res', timeout=15000)
            pg.wait_for_timeout(600)
            assert pg.locator('#menu a[data-v="biblioteca"]').count() == 1, 'sem menu Biblioteca'
            ncards = pg.locator('.bib-c').count()
            # força as miniaturas visíveis da primeira tela de cada categoria a carregarem
            pg.evaluate("document.querySelectorAll('.bib-c img').forEach(i=>i.loading='eager')")
            pg.wait_for_timeout(2500)
            quebradas = pg.evaluate("[...document.querySelectorAll('.bib-c img')].filter(i=>i.complete&&i.naturalWidth===0).map(i=>i.getAttribute('src'))")
            phs = pg.locator('.bib-c .th .ph').count()
            lateral = pg.evaluate('document.documentElement.scrollWidth - innerWidth')
            if w == 1440 and PRINTS and cli in ('jaci', 'leo', 'mova-street'):
                os.makedirs(PRINTS, exist_ok=True); pg.evaluate('scrollTo(0,0)'); pg.screenshot(path=os.path.join(PRINTS, f'biblioteca-{cli}-1440.png'))
            # filtro, busca, visualizador
            pg.locator('[data-bib-sit="reprovado"]').first.click(); pg.wait_for_timeout(150)
            pg.locator('[data-bib-sit="ativos"]').first.click(); pg.wait_for_timeout(150)
            if ncards:
                pg.fill('#bib-q', 'zzzz-nada'); pg.wait_for_timeout(300); vaz = pg.locator('#bib-res .vazio').count(); pg.fill('#bib-q', ''); pg.wait_for_timeout(300)
                if not vaz: erros.append('busca não filtrou')
            # outras abas continuam abrindo
            abas = pg.evaluate("[...new Set([...document.querySelectorAll('#menu a[data-v]')].map(a=>a.dataset.v))]")
            ruins = []
            for v in abas:
                pg.evaluate(f"location.hash='{v}'"); pg.wait_for_timeout(120)
                if not pg.evaluate("(document.querySelector('main')||document.body).innerText.trim().length"): ruins.append(v)
            if erros: falhas.append(f'{cli} {w}px: erros de JS {erros[:3]}')
            if quebradas: falhas.append(f'{cli} {w}px: {len(quebradas)} miniatura(s) quebrada(s), ex.: {quebradas[:3]}')
            if lateral > 0: falhas.append(f'{cli} {w}px: rolagem lateral de {lateral}px')
            if ruins: falhas.append(f'{cli} {w}px: abas vazias {ruins}')
            if w == 1440: resumo.append(f'{cli}: {len(its)} itens no manifesto · {ncards} cartões na 1ª tela · {phs} sem miniatura · {len(abas)} abas ok')
            ctx.close()
    b.close()
print('\n'.join(resumo)); print('FALHAS:' if falhas else 'TUDO CERTO'); print('\n'.join(falhas))
sys.exit(1 if falhas else 0)
