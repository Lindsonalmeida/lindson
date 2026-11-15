"""Monta publicar/<id>.json (título, descrição SEO com capítulos, tags, capa aprovada v3) dos longos 10-12. (conta Zuleide, 15/11/2026)
Uso: python3 publicar_longos.py longo-10 [...]  (rodar depois de tempos.py <id>)"""
import json, os, sys
D = os.path.dirname(os.path.abspath(__file__)); R = os.path.join(D, '..')
TAGS = {
 'longo-10': ['milagres de Jesus','sinais de João','Jesus acalma a tempestade','multiplicação dos pães','ressurreição de Lázaro','filha de Jairo','estudo bíblico','Evangelho de Marcos','Passaporte da Bíblia'],
 'longo-11': ['Êxodo explicado','Moisés','dez pragas do Egito','Páscoa na Bíblia','mar Vermelho','maná','Dez Mandamentos','bezerro de ouro','estudo bíblico','Passaporte da Bíblia'],
 'longo-12': ['apóstolo Paulo','Saulo de Tarso','conversão de Paulo','Atos dos Apóstolos','cartas de Paulo','espinho na carne','naufrágio de Paulo','estudo bíblico','Passaporte da Bíblia']}
HASH = {'longo-10':'#milagresdejesus #estudobiblico #biblia','longo-11':'#exodo #moises #estudobiblico','longo-12':'#apostolopaulo #atosdosapostolos #estudobiblico'}
lon = {v['id']: v for v in json.load(open(R + '/longos.json'))}
tem = json.load(open(R + '/tempos.json'))
os.makedirs(R + '/publicar', exist_ok=True)
for vid in sys.argv[1:]:
    v = lon[vid]; caps = '\n'.join(f'{t} {n}' for t, n in tem.get(vid, []))
    desc = f"{v['legenda']}\n\nCapítulos\n{caps}\n\nImagens: gravuras de Gustave Doré (domínio público). Narração com voz sintética.\n\n{HASH[vid]}"
    out = {'id': vid, 'titulo': v['titulo'], 'descricao': desc[:5000], 'tags': TAGS[vid],
           'comentario_fixado': v['comentario'], 'capa': f'conteudo/youtube/passaporte/capas-longos-10-12/capa-{vid[-2:]}.jpg',
           'video': f'conteudo/youtube/passaporte/videos/{vid}.mp4 (fora do Git)', 'playlist': 'A Bíblia inteira',
           'situacao': 'pronto para agendar, aguardando OK do Lindson'}
    json.dump(out, open(f'{R}/publicar/{vid}.json', 'w'), ensure_ascii=False, indent=1); print('ok', vid)
