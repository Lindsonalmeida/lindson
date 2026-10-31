"""Completa o acervo usado pelos roteiros (longo-12 a 16): baixa cada imagem que falta em img/acervo/.
Com crédito no creditos.json, busca pelo título exato; sem crédito, busca a obra pelo nome (BUSCA abaixo).
Só aceita domínio público e registra o crédito. python3 acervo_faltantes.py"""
import glob, io, json, os, time, urllib.parse, urllib.request
from PIL import Image
D = os.path.dirname(os.path.abspath(__file__)); RL = os.path.join(D, '..'); OUT = RL + '/img/acervo'
API = 'https://commons.wikimedia.org/w/api.php'; UA = {'User-Agent': 'RaposaELeaoBot/1.0 (canal educativo; contato via GitHub Lindsonalmeida)'}
CRED = OUT + '/creditos.json'; cred = json.load(open(CRED))
BUSCA = {
    'beijo_judas_giotto.jpg': 'Giotto Kiss of Judas Scrovegni',
    'castiglione_raffaello.jpg': 'Raphael Portrait of Baldassare Castiglione Louvre',
    'cesar_assassinato_camuccini.jpg': 'Vincenzo Camuccini Morte di Cesare',
    'cesar_morte_gerome.jpg': 'Gérôme The Death of Caesar Walters',
    'coroacao_napoleao_david.jpg': 'Jacques-Louis David Coronation of Napoleon',
    'embaixadores_holbein.jpg': 'Hans Holbein the Younger The Ambassadors',
    'julio_ii_raffaello.jpg': 'Raphael Portrait of Pope Julius II National Gallery',
    'leao_x_raffaello.jpg': 'Raphael Pope Leo X with two cardinals',
    'multidao_bruegel.jpg': 'Pieter Bruegel the Elder The Procession to Calvary',
    'pollice_verso_gerome.jpg': 'Jean-Léon Gérôme Pollice Verso',
    'prisao_cristo_caravaggio.jpg': 'Caravaggio The Taking of Christ Dublin',
    'rendicao_granada_pradilla.jpg': 'Francisco Pradilla La rendición de Granada',
    'romanos_decadencia_couture.jpg': 'Thomas Couture Romans during the Decadence',
    'vercingetorix_royer.jpg': 'Lionel Royer Vercingetorix throws down his arms',
}

def api(**p):
    p['format'] = 'json'
    for k in range(6):
        try:
            return json.load(urllib.request.urlopen(urllib.request.Request(API + '?' + urllib.parse.urlencode(p), headers=UA), timeout=60))
        except Exception as e:
            print('  espera', e, flush=True); time.sleep(60 * (k + 1))
    raise RuntimeError('API indisponível')

def dominio_publico(ii):
    md = ii.get('extmetadata', {}); lic = (md.get('LicenseShortName', {}).get('value', '') + ' ' + md.get('License', {}).get('value', '')).lower()
    return any(x in lic for x in ('public domain', 'pd', 'cc0'))

def baixa(arq, ii, titulo):
    for k in range(6):
        try:
            dado = urllib.request.urlopen(urllib.request.Request(ii.get('thumburl') or ii['url'], headers=UA), timeout=120).read(); break
        except Exception as e:
            print('  espera', e, flush=True); time.sleep(60 * (k + 1))
    else:
        return False
    Image.open(io.BytesIO(dado)).convert('RGB').save(f'{OUT}/{arq}', quality=92)
    md = ii.get('extmetadata', {})
    if not any(c['arquivo'] == arq for c in cred):
        cred.append(dict(arquivo=arq, titulo=titulo, autor=md.get('Artist', {}).get('value', ''), licenca=md.get('LicenseShortName', {}).get('value', ''),
                         url_commons=ii.get('descriptionurl', ''), busca=BUSCA.get(arq, '')))
        json.dump(cred, open(CRED, 'w'), ensure_ascii=False, indent=1)
    return True

precisa = set()
for f in glob.glob(RL + '/roteiros/longo-*.json'):
    precisa |= {c['gravura'][7:] for c in json.load(open(f))['cenas'] if c['gravura'].startswith('acervo/')}
falta = sorted(a for a in precisa if not os.path.exists(f'{OUT}/{a}'))
por_arquivo = {c['arquivo']: c for c in cred}
for arq in falta:
    if arq in por_arquivo:
        r = api(action='query', titles=por_arquivo[arq]['titulo'], prop='imageinfo', iiprop='url|extmetadata', iiurlwidth=1920)
        pg = list(r['query']['pages'].values())[0]; ii = (pg.get('imageinfo') or [{}])[0]; titulo = pg['title']
    elif arq in BUSCA:
        r = api(action='query', generator='search', gsrsearch=BUSCA[arq] + ' filetype:bitmap', gsrnamespace=6, gsrlimit=5, prop='imageinfo', iiprop='url|extmetadata|size', iiurlwidth=1920)
        pgs = sorted((r.get('query') or {}).get('pages', {}).values(), key=lambda x: x.get('index', 0))
        pg = next((p for p in pgs if dominio_publico((p.get('imageinfo') or [{}])[0]) and (p['imageinfo'][0].get('width', 0) >= 900)), None)
        if not pg:
            print('NÃO ACHEI', arq, flush=True); continue
        ii = pg['imageinfo'][0]; titulo = pg['title']
    else:
        print('SEM REGRA', arq, flush=True); continue
    print('ok' if baixa(arq, ii, titulo) else 'FALHOU', arq, '<-', titulo, flush=True)
    time.sleep(8)
print('faltando:', [a for a in precisa if not os.path.exists(f'{OUT}/{a}')])
