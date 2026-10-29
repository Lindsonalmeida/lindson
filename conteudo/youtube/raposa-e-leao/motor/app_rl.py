"""App de postagem do Raposa e Leão (mesmo modelo do app do Passaporte, na identidade do canal).
python3 app_rl.py -> scratchpad/raposa-app/index.html ; arquivos já enviados ao app ficam em ../ativos.json"""
import json, os, re, glob
D = os.path.dirname(os.path.abspath(__file__)); R = os.path.join(D, '..')
OUT = '/tmp/claude-0/-home-user/5acf6937-9ac6-56e0-bc29-78bef210dc8b/scratchpad/raposa-app'; os.makedirs(OUT, exist_ok=True)
AT = R + '/ativos.json'; ativos = json.load(open(AT)) if os.path.exists(AT) else {}
TPL = os.path.join(R, '..', 'passaporte', 'motor', 'app_pv.html')

def publicar_md(f):
    s = open(f).read()
    tit = re.search(r'\*\*Título[^\n]*\n(.+)', s).group(1).strip()
    desc = re.search(r'\*\*Descrição:\*\*\n(.*?)\n\*\*Na hora', s, re.S).group(1).strip()
    com = re.search(r'Comentário fixado: "(.+?)"\s*$', s, re.M)
    return tit, desc, com.group(1) if com else ''

TAGS = '#maquiavel #oprincipe #poder #estrategia #lideranca'
FONTE = '🦊🦁 Raposa e Leão: Maquiavel e as leis do poder aplicadas à vida real. Inscreva-se e ative o sino.'
L15 = {  # longos 01 a 05 (descrição a partir do roteiro aprovado em ROTEIROS-LONGOS.md)
 '01': ('Em 1513, um homem preso e torturado escreveu um livro proibido que é lido escondido por gente poderosa até hoje. As 7 lições de O Príncipe que mudam como você enxerga as pessoas: raposa e leão, temido ou amado, o mal de uma vez, a aparência, neutralidade e a sorte como um rio.', 'O Príncipe, capítulos VIII, XV, XVII, XVIII, XXI e XXV (1513).', 'Qual dessas 7 lições você mais precisava ouvir hoje? 👇'),
 '02': ('Você conhece alguém bom, trabalhador e honesto que sempre sai perdendo? Maquiavel explicou o porquê numa frase que incomoda. Neste vídeo: generosidade que arruína, favor que não apaga ofensa, o favor atrasado e como ser bom e estratégico ao mesmo tempo.', 'O Príncipe, capítulos III, VII, XV e XVI; Discursos sobre Tito Lívio, I.32 e III.2.', 'Você já foi a pessoa boa que saiu perdendo? Conta o que aprendeu 👇'),
 '03': ('Ele conquistou meia Itália em quatro anos, foi admirado por Maquiavel e perdeu tudo em poucos meses. A história documentada de César Bórgia, de Ramiro d\'Orco à eleição de Júlio II, e o erro que você provavelmente já cometeu.', 'O Príncipe, capítulo VII (1513); fatos históricos de 1498 a 1507.', 'Qual foi o maior erro do Bórgia, na sua opinião? 👇'),
 '04': ('Antes dos livros modernos sobre poder, Maquiavel escreveu um manual de guerra que termina com uma lista de regras. As 10 mais úteis para quem compete no trabalho e nos negócios.', 'A Arte da Guerra, de Nicolau Maquiavel (1521), regras gerais do livro VII.', 'Qual dessas regras você vai usar essa semana? 👇'),
 '05': ('Todo mundo conhece O Príncipe. Mas Maquiavel escreveu outro livro, três vezes maior, onde defende o oposto do que você pensa: os Discursos sobre Tito Lívio. O povo mais sábio que o príncipe, o conflito que fortalece, mudar com os tempos e saber parar.', 'Discursos sobre a primeira década de Tito Lívio (1517), I.4, I.58, II.27, III.1, III.9 e III.42.', 'Você já tinha ouvido falar dos Discursos? Sim ou não 👇'),
}
itens = []
for d in sorted(glob.glob(R + '/shorts/[0-9][0-9]')):
    n = d.split('/')[-1]; k = f'short-{n}'
    if os.path.exists(d + '/publicar.json'): p = json.load(open(d + '/publicar.json')); tit, desc, com = p['titulo'], p['legenda'], p['comentario']
    elif os.path.exists(d + '/PUBLICAR.md'): tit, desc, com = publicar_md(d + '/PUBLICAR.md')
    else: continue
    itens.append(dict(id=k, tipo='short', titulo=tit, legenda=desc, comentario=com, video=ativos.get(f'{k}.mp4'), arqVideo=f'raposa-e-leao-{k}.mp4',
                      capas=[dict(nome='Capa', arq=f'{k}.jpg', url=ativos.get(f'{k}.jpg'))], dur=ativos.get(f'{k}-dur', '')))
for d in sorted(glob.glob(R + '/longos/[0-9][0-9]'), key=lambda x: (not os.path.exists(x + '/publicar_novo.json'), x)):
    n = d.split('/')[-1]; k = f'longo-{n}'; rot = json.load(open(d + '/roteiro.json')) if os.path.exists(d + '/roteiro.json') else {}
    if os.path.exists(d + '/publicar.json'): p = json.load(open(d + '/publicar.json')); tit, leg, com = p['titulo'], p['legenda'], p['comentario']
    elif n in L15: intro, fonte, com = L15[n]; tit = rot['titulo']; leg = f'{intro}\n\nEm cada lição tem uma aplicação prática para o trabalho, os negócios e as relações.\n\n📜 Fonte: Nicolau Maquiavel, {fonte}\n{FONTE}\n\n{TAGS}'
    elif os.path.exists(d + '/publicar_novo.json'):
        p = json.load(open(d + '/publicar_novo.json')); tit, leg, com = p['titulo'], p['legenda'], p['comentario']
        TP = os.path.join(R, '..', 'passaporte', 'tempos.json'); tp = json.load(open(TP)).get(k, []) if os.path.exists(TP) else []
        leg = leg.replace('{CAPITULOS}', '\n'.join(f'{x} {y}' for x, y in tp) or '(os capítulos entram quando o vídeo ficar pronto)')
    else: continue
    capas = [dict(nome=f'Capa {x}', arq=f'{k}-{x}.jpg', url=ativos.get(f'{k}-{x}.jpg')) for x in 'ABC']
    capas = [c for c in capas if c['url']] or [dict(nome='Capa A', arq=f'{k}-A.jpg', url=None)]
    itens.append(dict(id=k, tipo='longo', titulo=tit, legenda=leg, comentario=com, video=ativos.get(f'{k}.mp4'), arqVideo=f'raposa-e-leao-{k}.mp4', capas=capas, dur=ativos.get(f'{k}-dur', '')))

h = open(TPL).read()
for a, b in [('<title>Passaporte da Bíblia · Postagens</title>', '<title>Raposa e Leão · Postagens</title>'),
             ('PASSAPORTE DA BÍBLIA · ESTÚDIO', 'RAPOSA E LEÃO · ESTÚDIO'), ("'passaporte-'+cp.arq", "'raposa-e-leao-'+cp.arq"),
             ("'pv-postados'", "'rl-postados'"), ('--noite:#0A0C14;--card:#141826;--card2:#1B2033;', '--noite:#0B0A08;--card:#17140F;--card2:#211C14;'),
             ('--linha:#2A3047;', '--linha:#3A3124;'), ('--selo:#D7263D;', '--selo:#D9622B;'), ('Cada bilhete tem', 'Cada ficha tem')]:
    assert a in h, a; h = h.replace(a, b)
h = h.replace('__DADOS__', json.dumps(itens, ensure_ascii=False).replace('</', '<\\/'))
open(OUT + '/index.html', 'w').write(h)
print(OUT + '/index.html', len(itens), 'itens;', sum(1 for i in itens if i['video']), 'com vídeo')
