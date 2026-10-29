"""Baixa pinturas em domínio público do Wikimedia Commons para o acervo do Raposa e Leão.
python3 acervo.py -> ../img/acervo/*.jpg + creditos.json (só aceita licença de domínio público)"""
import json, os, re, time, urllib.parse, urllib.request
D = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(D, '..', 'img', 'acervo'); os.makedirs(OUT, exist_ok=True)
API = 'https://commons.wikimedia.org/w/api.php'; UA = {'User-Agent': 'RaposaELeaoBot/1.0 (canal educativo; contato via GitHub Lindsonalmeida)'}
CRED = OUT + '/creditos.json'; cred = json.load(open(CRED)) if os.path.exists(CRED) else []
tem = {c['arquivo'] for c in cred} | set(os.listdir(OUT))
BUSCAS = [
 'Niccolò Machiavelli portrait painting', 'Santi di Tito Machiavelli', 'Palazzo Vecchio painting 16th century', 'Piazza della Signoria painting',
 'Florence Renaissance painting view', 'Lorenzo de Medici portrait', 'Cosimo de Medici Bronzino', 'Giuliano de Medici portrait',
 'Savonarola execution painting', 'Savonarola portrait Fra Bartolomeo', 'Cesare Borgia portrait', 'Pope Alexander VI portrait',
 'Pope Julius II Raphael', 'Louis XII of France portrait', 'Ferdinand II of Aragon portrait', 'Caterina Sforza portrait',
 'condottiero portrait painting', 'Battle of San Romano Uccello', 'Battle of Fornovo painting', 'Renaissance banquet painting',
 'Lorenzo Lotto portrait', 'Titian portrait man', 'Bronzino portrait', 'Raphael School of Athens', 'Ghirlandaio fresco Florence',
 'Moses painting Michelangelo', 'Cyrus the Great painting', 'Romulus and Remus painting', 'Theseus painting', 'Alexander the Great painting battle',
 'Hannibal crossing the Alps painting', 'Scipio Africanus painting', 'Death of Caesar painting', 'Marcus Aurelius painting',
 'Roman Senate painting Maccari', 'Roman legion painting', 'Wheel of Fortune painting medieval', 'Fortuna allegory painting',
 'flood river painting 17th century', 'lion painting Rubens', 'fox painting old master', 'lion hunt painting', 'chess players painting old',
 'conspiracy painting Renaissance', 'scholar writing candlelight painting', 'prison painting 16th century', 'coronation painting king',
 'crowd square painting Renaissance', 'Tuscan countryside painting 19th century', 'Pazzi conspiracy painting'
]
def api(**p):
    p.update(format='json'); r = urllib.request.urlopen(urllib.request.Request(API + '?' + urllib.parse.urlencode(p), headers=UA), timeout=60); return json.load(r)
def nome(t): s = re.sub(r'[^a-z0-9]+', '_', t.lower().split(':', 1)[1].rsplit('.', 1)[0])[:48].strip('_'); return s + '.jpg'
alvo = int(os.environ.get('ALVO', '85'))
for q in BUSCAS:
    if len([f for f in os.listdir(OUT) if f.endswith('.jpg')]) >= alvo: break
    try: res = api(action='query', generator='search', gsrsearch=q + ' filetype:bitmap', gsrnamespace=6, gsrlimit=6, prop='imageinfo', iiprop='url|extmetadata|size', iiurlwidth=1920)
    except Exception as e: print('busca falhou', q, e); time.sleep(600 if '429' in str(e) else 20); continue
    pegos = 0
    for pg in sorted((res.get('query') or {}).get('pages', {}).values(), key=lambda x: x.get('index', 0)):
        if pegos >= 2: break
        ii = (pg.get('imageinfo') or [{}])[0]; md = ii.get('extmetadata', {}); lic = (md.get('LicenseShortName', {}).get('value', '') + ' ' + md.get('License', {}).get('value', '')).lower()
        if not any(x in lic for x in ('public domain', 'pd', 'cc0')): continue
        if ii.get('width', 0) < 900 or ii.get('mime', 'image/jpeg') not in ('image/jpeg', 'image/png', 'image/tiff'): continue
        arq = nome(pg['title'])
        if arq in tem: continue
        try:
            dado = urllib.request.urlopen(urllib.request.Request(ii.get('thumburl') or ii['url'], headers=UA), timeout=120).read()
            from PIL import Image; import io
            im = Image.open(io.BytesIO(dado)).convert('RGB'); im.save(f'{OUT}/{arq}', 'JPEG', quality=90)
        except Exception as e: print('download falhou', arq, e); time.sleep(600 if '429' in str(e) else 20); continue
        txt = lambda k: re.sub('<[^>]+>', '', md.get(k, {}).get('value', ''))[:200]
        cred.append(dict(arquivo=arq, titulo=pg['title'], autor=txt('Artist'), data=txt('DateTimeOriginal'), licenca=txt('LicenseShortName'), url_commons=ii.get('descriptionurl', ''), busca=q))
        tem.add(arq); pegos += 1; print('ok', arq); json.dump(cred, open(CRED, 'w'), ensure_ascii=False, indent=1); time.sleep(25)
    time.sleep(25)
print(len([f for f in os.listdir(OUT) if f.endswith('.jpg')]), 'imagens')
