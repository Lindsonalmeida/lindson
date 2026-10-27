"""Gera PUBLICAR.md (título, descrição com capítulos, comentário fixado) dos longos 06 a 11
a partir dos tempos do vídeo renderizado: python3 publicar_06_11.py"""
import json, os, re
D = os.path.dirname(os.path.abspath(__file__)); L = os.path.join(D, '..', 'longos')

INFO = {
 '06': ('Ninguém escapa dele sem perceber: o bajulador. Neste vídeo, o método de Maquiavel (O Príncipe, caps. 22 e 23) para reconhecer quem só te diz o que você quer ouvir, escolher bons conselheiros e ouvir a verdade sem perder o respeito.',
        'O Príncipe, capítulos XXII e XXIII (1513).', '#maquiavel #oprincipe #lideranca #poder #falsosamigos'),
 '07': ('É melhor ser amado ou temido? A resposta completa de Maquiavel no capítulo 17 de O Príncipe: por que o medo dura mais que o amor, por que você nunca deve ser odiado e o que Aníbal e Cipião ensinam sobre liderança.',
        'O Príncipe, capítulo XVII (1513).', '#maquiavel #oprincipe #lideranca #estrategia #psicologiadopoder'),
 '08': ('Metade da sua vida é sorte. A outra metade é sua. Maquiavel compara a sorte a um rio que transborda e ensina a construir diques no tempo calmo, a não depender de uma só fonte e a mudar quando os tempos mudam.',
        'O Príncipe, capítulo XXV (1513); Discursos sobre Tito Lívio, livro III, capítulo 9.', '#maquiavel #oprincipe #mentalidade #estrategia #crise'),
 '09': ('A história de Girolamo Savonarola, o frade que dominou Florença, fez as fogueiras das vaidades e terminou executado na Piazza della Signoria em 1498. E a lição que Maquiavel tirou: todos os profetas desarmados se arruinaram.',
        'O Príncipe, capítulo VI (1513); fatos históricos de Florença, 1494 a 1498.', '#maquiavel #savonarola #historia #florenca #oprincipe'),
 '10': ('Demitido, preso e torturado em 1513, Maquiavel foi viver no campo e, à noite, vestia "roupas de corte" para conversar com os grandes do passado. Assim nasceu O Príncipe. A vida dele e a lição para quem está recomeçando.',
        'Carta de Maquiavel a Francesco Vettori (10/12/1513); biografia de Nicolau Maquiavel (1469 a 1527).', '#maquiavel #historia #oprincipe #resiliencia #biografia'),
 '11': ('Maquiavel estudou imperadores romanos e concluiu: quase todos que caíram foram odiados ou desprezados. O que causa cada erro, os casos de Marco Aurélio, Cômodo, Pertinax, Caracala e Sétimo Severo, e como evitar os dois.',
        'O Príncipe, capítulo XIX (1513).', '#maquiavel #oprincipe #lideranca #roma #poder'),
}

def mmss(t): t = int(t); return f'{t // 60}:{t % 60:02d}'

for k, (intro, fonte, tags) in INFO.items():
    rot = json.load(open(f'{L}/{k}/roteiro.json'))
    st = f'{D}/_stage_lg_{k}.html'
    caps = ['0:00 Introdução']
    if os.path.exists(st):
        sp = json.loads(re.search(r'const SP=(\{.*?\});const \$', open(st).read(), re.S).group(1))
        for g in sp['seg']:
            T = g['tela']
            if T['t'] == 'capitulo': caps.append(f"{mmss(g['ini'])} {T['n']}. {T['h']}")
            if T['t'] == 'compromisso': caps.append(f"{mmss(g['ini'])} Seu compromisso")
            if T['t'] == 'resumo': caps.append(f"{mmss(g['ini'])} Resumo")
    desc = f'''{intro}

Em cada lição tem uma aplicação prática para o trabalho, os negócios e as relações. No fim, assuma o compromisso: comente "EU VOU APLICAR".

⏱️ Capítulos
{chr(10).join(caps)}

📜 Fonte: Nicolau Maquiavel, {fonte}
🦊🦁 Raposa e Leão: Maquiavel e as leis do poder aplicadas à vida real. Inscreva-se e ative o sino.

{tags}'''
    com = 'Qual dessas lições você vai aplicar primeiro? Comenta "EU VOU APLICAR" e diz qual 👇'
    md = f'''# Longo {k} — {rot['titulo']}

**Título:**
{rot['titulo']}

**Descrição:**
{desc}

**Comentário fixado:**
{com}

**Capas para o teste A/B (Testar e comparar do YouTube):** `thumb-a.png` e `thumb-b.png`

**Na hora de subir:**
- Público: não é conteúdo para crianças
- Conteúdo alterado/sintético: não (voz de IA narrando não precisa marcar)
'''
    open(f'{L}/{k}/PUBLICAR.md', 'w').write(md)
    json.dump({'titulo': rot['titulo'], 'legenda': desc, 'comentario': com}, open(f'{L}/{k}/publicar.json', 'w'), ensure_ascii=False)
    print(k, len(caps), 'capítulos')
