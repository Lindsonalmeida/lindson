"""Gera SEO-NN.md, PUBLICAR.md e publicar.json dos longos 17-21 (conta Leandro). Tempos dos capítulos estimados por palavras (2,5 palavras/s); após o render, rodar de novo com tempos reais se houver longos/NN/tempos.json."""
import json,os
L=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','longos')
PESQ='''Pesquisa feita em 14/11/2026 no autocomplete do YouTube (suggestqueries, ds=yt, pt-BR). Sem números de volume: a ferramenta mostra só o que as pessoas digitam, não quantas vezes. Conferir depois no YouTube Studio > Pesquisa (aba Pesquisa do público).'''
S={
'17':dict(kw='manipulação psicológica',sec=['como identificar manipulação','manipulação psicológica relacionamento','maquiavel manipulação','maquiavel poder e manipulação'],
 auto='"manipulação como identificar", "manipulação psicologica", "manipulação psicológica relacionamento", "maquiavel manipulação", "maquiavel poder e manipulação"',
 conc='Canais de psicologia e de "leis do poder" dominam o termo com listas de sinais; quase nenhum ancora em obra e capítulo. Nosso ângulo: a defesa (não o ataque), com Maquiavel citado no original.',
 A='Manipulação psicológica: os 5 sinais, segundo Maquiavel',B='Manipulação: como identificar e se defender (Maquiavel)',C='Maquiavel e a manipulação: o truque que todos caem',
 tags='manipulação psicológica, como identificar manipulação, manipulação, maquiavel, o príncipe, maquiavel manipulação, poder e manipulação, como se defender de manipulação, pessoas manipuladoras, golpe, filosofia, psicologia, raposa e leão',
 desc='Por que pessoas inteligentes caem em manipulação? Maquiavel explicou há 500 anos: "os homens julgam mais pelos olhos que pelas mãos". Neste vídeo você aprende os 5 sinais de quem manipula (promessa grande, pressa, lisonja, isolamento e a culpa jogada no outro) e um método de defesa em 5 passos, com O Príncipe e os Discursos sobre Tito Lívio.',
 fonte='Nicolau Maquiavel, O Príncipe, caps. VII, XVIII e XXIII; Discursos sobre a primeira década de Tito Lívio, livro I, caps. 3 e 53.',
 fix='📌 Qual dos 5 sinais você já viu acontecer? Escreve o número 👇 E comenta "VOU CONFERIR" se vai usar as mãos antes dos olhos.',
 hash='#manipulação #maquiavel #oprincipe #psicologia #poder'),
'18':dict(kw='poder no trabalho',sec=['48 leis do poder no trabalho','como crescer na empresa que trabalho','como ser política no trabalho','maquiavel trabalho'],
 auto='"48 leis do poder no trabalho", "abuso de poder no trabalho", "como crescer na empresa que trabalho", "como ser politica no trabalho"',
 conc='O termo é puxado pelas "48 leis do poder" (Robert Greene). Diferencial: a fonte primária (Maquiavel, que foi funcionário 14 anos) e o lado limpo do jogo, sem sabotagem.',
 A='Poder no trabalho: 7 regras de Maquiavel que ninguém conta',B='Poder no trabalho: por que o competente fica para trás',C='Como crescer na empresa: 7 regras de Maquiavel',
 tags='poder no trabalho, leis do poder no trabalho, como crescer na empresa, política no trabalho, maquiavel, o príncipe, carreira, liderança, chefe, promoção, discursos de maquiavel, raposa e leão',
 desc='Você pode ser o mais competente da empresa e mesmo assim ficar para trás. Maquiavel trabalhou 14 anos no governo de Florença e escreveu as regras que ninguém fala em voz alta: você é julgado por quem está à sua volta, os três tipos de cérebro, o teste do braço direito, por que na calmaria sobe o simpático, por que não ficar em cima do muro e o que fazer depois de uma grande vitória.',
 fonte='Nicolau Maquiavel, O Príncipe, caps. III, XXI e XXII; Discursos sobre a primeira década de Tito Lívio, livro I, cap. 30; livro III, cap. 16.',
 fix='📌 Qual das 7 regras você vai aplicar nesta semana? Comenta "VOU LER O JOGO" e o número 👇',
 hash='#maquiavel #carreira #poder #lideranca #oprincipe'),
'19':dict(kw='pessoas falsas no trabalho',sec=['líderes que fingem','chefe falso','pessoas falsas como identificar','o príncipe maquiavel resumo'],
 auto='"pessoas falsas no trabalho", "pessoas falsas como identificar", "pessoas falsas e fingidas", "chefe falso", "líderes que inspiram"',
 conc='"Pessoas falsas" é forte em vídeos de autoajuda e religiosos, quase sem base histórica. Nosso ângulo: Fernando de Aragão, o rei que Maquiavel não podia nomear, e o teste das mãos.',
 A='Líderes que fingem: o alerta de Maquiavel',B='Pessoas falsas no poder: como Maquiavel as desmascara',C='Parecer bom sem ser: o líder falso segundo Maquiavel',
 tags='pessoas falsas, pessoas falsas no trabalho, chefe falso, líder falso, líderes que fingem, maquiavel, o príncipe, fernando de aragão, parecer e ser, liderança, raposa e leão',
 desc='"Não é necessário ao príncipe ter todas as boas qualidades, mas é muito necessário parecer tê-las." A frase mais polêmica de O Príncipe explica o líder de fachada: o rei Fernando de Aragão, que pregava paz e fé e era inimigo das duas, a generosidade de vitrine, o falso sócio de Sétimo Severo e o teste das mãos para desmascarar quem finge.',
 fonte='Nicolau Maquiavel, O Príncipe, caps. XV, XVI, XVIII, XIX e XXI.',
 fix='📌 Qual "manto" você já viu um líder usar: família, propósito, missão ou fé? Escreve a palavra 👇 E comenta "PARECER E SER".',
 hash='#maquiavel #lideranca #pessoasfalsas #oprincipe #poder'),
'20':dict(kw='ingratidão das pessoas',sec=['por que as pessoas são ingratas','ingratidão','maquiavel o príncipe','amado ou temido'],
 auto='"ingratidão das pessoas", "mensagem de ingratidão das pessoas", "ingratidão" (o termo puro é dominado por músicas: por isso a palavra-chave longa)',
 conc='O tema aparece em mensagens e pregações; não achamos canal dark de filosofia tratando a ingratidão com Maquiavel e os Discursos (I.29). Ângulo novo e evergreen.',
 A='Ingratidão das pessoas: o que Maquiavel descobriu',B='Ingratidão: por que quem você ajuda some (Maquiavel)',C='Por que quem você ajuda te esquece, segundo Maquiavel',
 tags='ingratidão, ingratidão das pessoas, pessoas ingratas, por que as pessoas são ingratas, maquiavel, o príncipe, amado ou temido, cipião, gratidão, relacionamentos, raposa e leão',
 desc='Você ajudou, e quando precisou a pessoa sumiu. Maquiavel explica: "os homens são ingratos, volúveis, fogem dos perigos" e "a ingratidão nasce da avareza ou da suspeita". A história de Cipião, que salvou Roma e terminou longe dela, de Gonzalo de Córdoba e Fernando de Aragão, e 5 regras para ajudar sem ser feito de bobo.',
 fonte='Nicolau Maquiavel, O Príncipe, caps. VII, VIII, IX e XVII; Discursos sobre a primeira década de Tito Lívio, livro I, caps. 29 e 30.',
 fix='📌 Qual das 5 regras você mais quebra? 👇 E comenta "VOU AGRADECER" se vai mandar mensagem para quem te ajudou.',
 hash='#maquiavel #ingratidao #oprincipe #relacionamentos #filosofia'),
'21':dict(kw='inveja no trabalho',sec=['pessoas invejosas','inveja como lidar','inveja disfarçada','maquiavel'],
 auto='"inveja no trabalho como lidar", "inveja no trabalho como identificar", "pessoas invejosas no trabalho", "inveja disfarçada de amizade", "inveja como se proteger"',
 conc='Muito vídeo religioso e de oração contra inveja. Lacuna: explicação histórica (Discursos III.30) e método prático, sem misticismo.',
 A='Inveja no trabalho: como lidar, segundo Maquiavel',B='Pessoas invejosas: o remédio que Maquiavel descobriu',C='Inveja: o inimigo silencioso, segundo Maquiavel',
 tags='inveja, inveja no trabalho, pessoas invejosas, inveja como lidar, inveja disfarçada, maquiavel, discursos, soderini, savonarola, florença, carreira, raposa e leão',
 desc='"É necessário, antes, apagar a inveja." Nos Discursos, Maquiavel mostra por que a inveja trava os bons, os dois únicos remédios que achou na história (Camilo e Moisés) e o erro do seu chefe, Piero Soderini, que achou que bondade e paciência bastariam, e caiu em 1512. No fim, 5 jeitos de desarmar a inveja sem destruir ninguém.',
 fonte='Nicolau Maquiavel, Discursos sobre a primeira década de Tito Lívio, livro I, cap. 8; livro II, cap. 22; livro III, caps. 3, 9, 16 e 30; epigrama sobre Piero Soderini.',
 fix='📌 Você esperaria ou agiria? 👇 E comenta "VOU DIVIDIR O PALCO" se topa o desafio da semana.',
 hash='#inveja #maquiavel #carreira #florenca #filosofia')}
AG={'17':'ter 17/11 · 19h','18':'sex 20/11 · 19h','19':'ter 24/11 · 19h','20':'sex 27/11 · 19h','21':'ter 01/12 · 19h'}
def mmss(t):return f'{int(t//60)}:{int(t%60):02d}'
for n,d in S.items():
    r=json.load(open(f'{L}/{n}/roteiro.json'));tj=f'{L}/{n}/tempos.json'
    tr=json.load(open(tj)) if os.path.exists(tj) else None
    caps=[('0:00','Introdução')];t=0
    for i,g in enumerate(r['seg']):
        ini=tr[i] if tr else t
        if g['tela']['t']=='capitulo':caps.append((mmss(ini),f"{g['tela']['n']}. {g['tela']['h']}"))
        if g['tela']['t']=='compromisso':caps.append((mmss(ini),'Seu compromisso'))
        if g['tela']['t']=='resumo':caps.append((mmss(ini),'Resumo'))
        t+=len(g['txt'].split())/2.5+.7
    capt='\n'.join(f'{a} {b}' for a,b in caps)
    for k in 'ABC':assert len(d[k])<=60,(n,k,len(d[k]))
    r['titulo']=d['A'];json.dump(r,open(f'{L}/{n}/roteiro.json','w'),ensure_ascii=False,indent=1)
    desc=f"{d['desc']}\n\n⏱️ Capítulos\n{capt}\n\n📜 Fonte: {d['fonte']}\n\n🦊🦁 Raposa e Leão: Maquiavel e as leis do poder aplicadas à vida real.\n\n{d['hash']}"
    est='' if tr else ' (estimados por palavras; ajustar pelo vídeo final)'
    open(f'{L}/{n}/SEO-{n}.md','w').write(f"""# SEO do longo {n} (conta Leandro, Peter, 14/11/2026)

**Palavra-chave principal:** {d['kw']}
**Secundárias:** {', '.join(d['sec'])}

## Pesquisa
{PESQ}
- Autocomplete encontrado: {d['auto']}.
- Concorrência e ângulo: {d['conc']}

## Títulos para "Testar e comparar" (até 60 caracteres, palavra-chave na frente)
- **A:** {d['A']} ({len(d['A'])})
- **B:** {d['B']} ({len(d['B'])})
- **C:** {d['C']} ({len(d['C'])})

## Capas
`capas/longo-{n}-A.jpg`, `-B.jpg`, `-C.jpg` (C = variante "mais luz, menos texto", hipótese do Peter para testar).

## Descrição
{desc}

## Capítulos{est}
{capt}

## Tags
{d['tags']}

## Comentário fixado
{d['fix']}
""")
    pub=dict(titulo=d['A'],titulos_ab=[d['A'],d['B'],d['C']],legenda=desc,comentario=d['fix'],tags=d['tags'],capas=[f'capas/longo-{n}-{k}.jpg' for k in 'ABC'],agenda=AG[n],publico='não é conteúdo para crianças',sintetico='não (voz sintética narrando e pinturas de domínio público; nada realista que se confunda com fato)')
    json.dump(pub,open(f'{L}/{n}/publicar.json','w'),ensure_ascii=False,indent=1)
    open(f'{L}/{n}/PUBLICAR.md','w').write(f"""# Longo {n} · {d['A']}

**Agenda sugerida:** {AG[n]} (horário de Brasília). **Vídeo:** `longos/{n}/video.mp4` (fora do Git).

**Título (A):** {d['A']}
**Teste A/B/C de título:** {d['B']} · {d['C']}
**Capas (Testar e comparar):** `capas/longo-{n}-A.jpg`, `B`, `C`

**Descrição:**
{desc}

**Tags:** {d['tags']}

**Comentário fixado:** {d['fix']}

**Na hora de subir:**
- Público: não é conteúdo para crianças.
- Conteúdo alterado/sintético: não (narração de IA e pinturas de domínio público).
- Tela final + card para a playlist do canal ("O Príncipe explicado" ou "Maquiavel na prática") e o link dela no comentário fixado.
""")
    print(n,d['A'])
