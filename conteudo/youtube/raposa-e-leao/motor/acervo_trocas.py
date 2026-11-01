"""Plano B do acervo: troca nos roteiros cada imagem que não foi possível baixar (Wikimedia bloqueada)
por uma obra em domínio público do mesmo tema que já está no acervo, sem repetir a imagem da cena anterior.
Guarda a original em 'gravura_original' (para voltar quando o download funcionar) e registra no creditos.json.
ROTEIROS=longo-09 python3 acervo_trocas.py só nesse roteiro (padrão longo-1[2-6]).
python3 acervo_trocas.py            -> aplica      |      python3 acervo_trocas.py desfaz -> volta às originais que já existem"""
import glob, json, os, sys
D = os.path.dirname(os.path.abspath(__file__)); RL = os.path.join(D, '..'); IMG = RL + '/img'
CRED = IMG + '/acervo/creditos.json'
# candidatas por tema (em ordem de preferência); só imagens de MAPA.md, sem fotos modernas
TEMA = {
    'acervo/portrait_of_niccol_machiavelli_by_santi_di_tito.jpg': ['maquiavel.jpg', 'maquiavel2.jpg'],
    'acervo/bernardo_bellotto_the_piazza_della_signoria_in_f.jpg': ['hist/bonfire_of_the_vanities.jpg', 'lorenzo.jpg'],
    'acervo/julio_ii_raffaello.jpg': ['hist/pope_julius_ii.jpg', 'hist/pope_alexander_vi.jpg'],
    'acervo/leao_x_raffaello.jpg': ['lorenzo.jpg', 'hist/pope_alexander_vi.jpg'],
    'acervo/botticelli_giuliano_de_medici_accademia_carrara.jpg': ['lorenzo.jpg', 'hist/girolamo_savonarola.jpg'],
    'acervo/sandro_botticelli_giuliano_de_medici_gem_ldegale.jpg': ['lorenzo.jpg', 'hist/girolamo_savonarola.jpg'],
    'acervo/castiglione_raffaello.jpg': ['maquiavel2.jpg', 'lorenzo.jpg'],
    'acervo/ferdinand_of_aragon_isabella_of_castile.jpg': ['hist/ferdinand_ii_of_aragon.jpg', 'hist/pope_alexander_vi.jpg'],
    'acervo/embaixadores_holbein.jpg': ['borgia.jpg', 'hist/pope_alexander_vi.jpg'],
    'acervo/multidao_bruegel.jpg': ['hist/bonfire_of_the_vanities.jpg', 'hist/arco_severo.jpg'],
    'acervo/rendicao_granada_pradilla.jpg': ['hist/ferdinand_ii_of_aragon.jpg', 'hist/marcus_equestre.jpg'],
    'acervo/coroacao_napoleao_david.jpg': ['hist/marcus_equestre.jpg', 'hist/marcus_aurelius.jpg'],
    'acervo/beijo_judas_giotto.jpg': ['borgia.jpg', 'hist/caracalla.jpg'],
    'acervo/prisao_cristo_caravaggio.jpg': ['hist/caracalla.jpg', 'borgia.jpg'],
    'acervo/cesar_assassinato_camuccini.jpg': ['cesar.jpg', 'hist/arco_severo.jpg'],
    'acervo/cesar_morte_gerome.jpg': ['cesar.jpg', 'hist/arco_severo.jpg'],
    'acervo/jean_l_on_g_r_me_the_death_of_caesar_walters_378.jpg': ['cesar.jpg', 'hist/arco_severo.jpg'],
    'acervo/pollice_verso_gerome.jpg': ['hist/commodus.jpg', 'hist/arco_severo.jpg'],
    'acervo/romanos_decadencia_couture.jpg': ['hist/caracalla.jpg', 'hist/commodus.jpg'],
    'acervo/vercingetorix_royer.jpg': ['cesar.jpg', 'hist/marcus_equestre.jpg'],
    'acervo/hannibal_and_scipio_africanus.jpg': ['hist/hannibal.jpg', 'hist/alexander_the_great.jpg', 'hist/marcus_equestre.jpg'],
    'acervo/the_battle_of_alexander_at_issus_by_albrecht_alt.jpg': ['acervo/albrecht_altdorfer_schlacht_bei_issus_alte_pinak.jpg', 'hist/alexander_the_great.jpg'],
    'acervo/albrecht_altdorfer_schlacht_bei_issus_alte_pinak.jpg': ['hist/alexander_the_great.jpg', 'hist/hannibal.jpg'],
}
existe = lambda g: os.path.exists(f'{IMG}/{g}')
cred = json.load(open(CRED)); trocas = {}
for f in sorted(glob.glob(RL + '/roteiros/' + os.environ.get('ROTEIROS', 'longo-1[2-6]') + '.json')):
    v = json.load(open(f)); ant = None; mud = 0
    cs = v['cenas']
    for i, c in enumerate(cs):
        if len(sys.argv) > 1 and sys.argv[1] == 'desfaz':
            if 'gravura_original' in c and existe(c['gravura_original']): c['gravura'] = c.pop('gravura_original'); mud += 1
        elif not existe(c['gravura']):
            orig = c['gravura']; cand = [g for g in TEMA.get(orig, []) if existe(g)]
            if not cand: sys.exit(f'sem substituta para {orig}')
            prox = cs[i + 1]['gravura'] if i + 1 < len(cs) else None
            if prox and not existe(prox): prox = next((g for g in TEMA.get(prox, []) if existe(g)), None)
            g = next((x for x in cand if x not in (ant, prox)), None) or next((x for x in cand if x != ant), cand[0])
            c.setdefault('gravura_original', orig); c['gravura'] = g; mud += 1
            trocas.setdefault(orig[7:], set()).add(g)
        ant = c['gravura']
    json.dump(v, open(f, 'w'), ensure_ascii=False, indent=1); print(os.path.basename(f), mud, 'cenas alteradas')
for arq, subs in trocas.items():
    reg = next((c for c in cred if c['arquivo'] == arq), None)
    if reg is None: reg = dict(arquivo=arq); cred.append(reg)
    reg['trocada_por'] = sorted(set(reg.get('trocada_por', [])) | subs)
    reg['motivo_troca'] = 'Wikimedia Commons bloqueou o download (HTTP 429) em 31/10/2026; usada obra em domínio público do mesmo tema já presente no acervo'
json.dump(cred, open(CRED, 'w'), ensure_ascii=False, indent=1)
