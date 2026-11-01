"""Acervo extra (31/10): baixa obras em domínio público sem usar a API da Wikimedia (bloqueada com 429).
- Wikimedia: arquivo original direto de upload.wikimedia.org (caminho pelo md5 do nome), reduzido a 1920 px.
- SMK (Statens Museum for Kunst, Copenhague): API aberta, só obras marcadas public_domain.
Registra o crédito em img/acervo/creditos.json. Já baixadas são puladas. python3 acervo_extra.py"""
import hashlib, io, json, os, time, urllib.parse, urllib.request
from PIL import Image
Image.MAX_IMAGE_PIXELS = None
D = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(D, '..', 'img', 'acervo')
UA = {'User-Agent': 'RaposaELeaoBot/1.0 (canal educativo; contato via GitHub Lindsonalmeida)'}
CRED = OUT + '/creditos.json'; cred = json.load(open(CRED))
WIKI = {  # arquivo local: nome exato do arquivo no Commons
    'portrait_of_niccol_machiavelli_by_santi_di_tito.jpg': 'Portrait of Niccolò Machiavelli by Santi di Tito.jpg',
    'bernardo_bellotto_the_piazza_della_signoria_in_f.jpg': 'Bernardo Bellotto - The Piazza della Signoria in Florence - Google Art Project.jpg',
    'botticelli_giuliano_de_medici_accademia_carrara.jpg': "Botticelli - Giuliano de' Medici - Accademia Carrara Bergamo.jpg",
    'ferdinand_of_aragon_isabella_of_castile.jpg': 'Ferdinand of Aragon, Isabella of Castile.jpg',
    'albrecht_altdorfer_schlacht_bei_issus_alte_pinak.jpg': 'Albrecht Altdorfer - Schlacht bei Issus (Alte Pinakothek, München) - Google Art Project.jpg',
    'hannibal_and_scipio_africanus.jpg': 'Hannibal and Scipio Africanus.jpg',
    'jean_l_on_g_r_me_the_death_of_caesar_walters_378.jpg': 'Jean-Léon Gérôme - The Death of Caesar - Walters 37884.jpg',
    'castiglione_raffaello.jpg': 'Baldassare Castiglione, by Raffaello Sanzio, from C2RMF retouched.jpg',
    'beijo_judas_giotto.jpg': 'Giotto di Bondone - No. 31 Scenes from the Life of Christ - 15. The Arrest of Christ (Kiss of Judas) - WGA09216.jpg',
}
SMK = {  # arquivo local: número de inventário no SMK
    'smk_stormflod_vernet.jpg': 'KMSst564', 'smk_storm_bakhuizen.jpg': 'KMSsp544', 'smk_skibbrud_dahl.jpg': 'KMS216',
    'smk_efter_stormen_friedrich.jpg': 'KMS8817', 'smk_flod_klipper_doughty.jpg': 'KMS3128', 'smk_flod_ruysdael.jpg': 'KMS726',
    'smk_uvejr_gaard_juel.jpg': 'KMS137', 'smk_efter_regn_skovgaard.jpg': 'KMS1472', 'smk_vandfald_ruisdael.jpg': 'KMSsp573',
    'smk_skibbrud_vernet.jpg': 'KMSsp708', 'smk_havn_bakhuizen.jpg': 'KMSsp548', 'smk_flod_bjerg_vernet.jpg': 'KMS3765',
    'smk_spaakone_wijck.jpg': 'KMS3023', 'smk_uvejr_dietrich.jpg': 'KMSst194', 'smk_borg_flod_haagen.jpg': 'KMS672',
}

def pega(url, tentativas=5):
    for k in range(tentativas):
        try:
            return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=180).read()
        except Exception as e:
            print('  espera', e, flush=True); time.sleep(20 * (k + 1))

def salva(arq, dado, **reg):
    im = Image.open(io.BytesIO(dado)).convert('RGB'); im.thumbnail((1920, 1920)); im.save(f'{OUT}/{arq}', quality=92)
    if not any(c['arquivo'] == arq for c in cred): cred.append(dict(arquivo=arq, **reg))
    json.dump(cred, open(CRED, 'w'), ensure_ascii=False, indent=1); print('ok', arq, im.size, flush=True)

for arq, nome in WIKI.items():
    if os.path.exists(f'{OUT}/{arq}'): continue
    n = nome.replace(' ', '_'); h = hashlib.md5(n.encode()).hexdigest()
    dado = pega(tentativas=1, url=f'https://upload.wikimedia.org/wikipedia/commons/{h[0]}/{h[:2]}/{urllib.parse.quote(n)}')
    if dado: salva(arq, dado, titulo='File:' + nome, licenca='Public domain', url_commons='https://commons.wikimedia.org/wiki/File:' + urllib.parse.quote(n))
    else: print('FALHOU', arq)
for arq, inv in SMK.items():
    if os.path.exists(f'{OUT}/{arq}'): continue
    r = json.loads(pega('https://api.smk.dk/api/v1/art/?' + urllib.parse.urlencode({'object_number': inv})))
    it = r['items'][0]
    if not it.get('public_domain'): print('NÃO É DOMÍNIO PÚBLICO', arq); continue
    url = it['image_iiif_id'] + '/full/!1920,1920/0/default.jpg' if it.get('image_iiif_id') else it.get('image_native') or it['image_thumbnail']
    dado = pega(url)
    if dado: salva(arq, dado, titulo=it['titles'][0]['title'], autor=(it.get('production') or [{}])[0].get('creator', ''),
                   data=(it.get('production_date') or [{}])[0].get('period', ''), licenca='Public domain (SMK Open)',
                   url_commons='https://open.smk.dk/artwork/image/' + inv)
    else: print('FALHOU', arq)
